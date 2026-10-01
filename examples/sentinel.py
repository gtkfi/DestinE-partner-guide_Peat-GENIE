"""Minimal CDSE Sentinel Hub HTTP requests with readable request payloads."""
from datetime import datetime, timedelta, timezone
from io import BytesIO
import numpy as np
from .common import required_env

BASE = "https://sh.dataspace.copernicus.eu"
TOKEN_URL = "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"


def checked_json(response):
    if not response.ok:
        raise RuntimeError(f"API returned HTTP {response.status_code}; check account, request, and quota.")
    return response.json()


def access_token():
    import requests
    response = requests.post(TOKEN_URL, data={"grant_type": "client_credentials", "client_id": required_env("CDSE_CLIENT_ID"), "client_secret": required_env("CDSE_CLIENT_SECRET")}, timeout=(10, 60))
    return checked_json(response)["access_token"]


def bounds(bbox):
    west, south, east, north = map(float, bbox)
    if not -180 <= west < east <= 180 or not -90 <= south < north <= 90:
        raise ValueError("Use [west,south,east,north] in WGS84, without crossing the dateline.")
    return {"bbox": [west, south, east, north], "properties": {"crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"}}


S2_EVALSCRIPT = '''//VERSION=3
function setup() { return {input: [{bands:["B04","B08","SCL","dataMask"],units:["REFLECTANCE","REFLECTANCE","DN","DN"]}], output:{bands:4,sampleType:"FLOAT32"}}; }
function evaluatePixel(s) { let ok = s.dataMask && [4,5,6].includes(s.SCL); return [s.B04,s.B08,ok?1:0,s.SCL]; }
'''
S1_EVALSCRIPT = '''//VERSION=3
function setup() { return {input:["VV","VH","dataMask"],output:{bands:3,sampleType:"FLOAT32"}}; }
function evaluatePixel(s) { return [s.VV,s.VH,s.dataMask]; }
'''
STATS_EVALSCRIPT = '''//VERSION=3
function setup() { return {input:[{bands:["B04","B08","SCL","dataMask"]}],output:[{id:"features",bands:3,sampleType:"FLOAT32"},{id:"dataMask",bands:1}]}; }
function evaluatePixel(s) { let denominator=s.B08+s.B04; let ok=s.dataMask && [4,5,6].includes(s.SCL) && Math.abs(denominator)>1e-12; return {features:[s.B04,s.B08,ok?(s.B08-s.B04)/denominator:0],dataMask:[ok?1:0]}; }
'''


def process_payload(collection, bbox, start, end, size=(256, 256), orbit="ASCENDING", max_cloud=20):
    if max(size) > 1024 or min(size) < 1:
        raise ValueError("Keep this teaching request within 1..1024 pixels per side.")
    filters = {"timeRange": {"from": start, "to": end}, "mosaickingOrder": "mostRecent"}
    data = {"type": collection, "dataFilter": filters}
    if collection == "sentinel-2-l2a":
        filters["maxCloudCoverage"] = max_cloud
        evalscript = S2_EVALSCRIPT
    elif collection == "sentinel-1-grd":
        if orbit not in {"ASCENDING", "DESCENDING"}:
            raise ValueError("Fix orbit direction for a comparable radar series.")
        filters.update({"orbitDirection": orbit, "acquisitionMode": "IW", "polarization": "DV", "resolution": "HIGH"})
        data["processing"] = {"backCoeff": "GAMMA0_TERRAIN", "orthorectify": True, "demInstance": "COPERNICUS_90"}
        evalscript = S1_EVALSCRIPT
    else:
        raise ValueError("This helper supports Sentinel-2 L2A and Sentinel-1 GRD only.")
    return {"input": {"bounds": bounds(bbox), "data": [data]}, "output": {"width": size[0], "height": size[1], "responses": [{"identifier": "default", "format": {"type": "image/tiff"}}]}, "evalscript": evalscript}


def process(token, payload):
    import requests
    from rasterio.io import MemoryFile
    response = requests.post(f"{BASE}/process/v1", json=payload, headers={"Authorization": f"Bearer {token}"}, timeout=(10, 180))
    if not response.ok:
        raise RuntimeError(f"Process API returned HTTP {response.status_code}; check setup and quota.")
    with MemoryFile(response.content) as memory:
        with memory.open() as dataset:
            return dataset.read(), {"crs": str(dataset.crs), "transform": list(dataset.transform), "shape": list(dataset.shape)}


def catalog(token, collection, bbox, start, end, max_cloud=20, orbit="ASCENDING"):
    import requests
    body = {"collections": [collection], "bbox": bounds(bbox)["bbox"], "datetime": f"{start}/{end}", "limit": 100}
    body["filter-lang"] = "cql2-text"
    body["filter"] = f"eo:cloud_cover <= {int(max_cloud)}" if collection == "sentinel-2-l2a" else f"sat:orbit_state = '{orbit.lower()}'"
    result = checked_json(requests.post(f"{BASE}/catalog/v1/search", json=body, headers={"Authorization": f"Bearer {token}"}, timeout=(10, 60)))
    return result.get("features", []), any(link.get("rel") == "next" for link in result.get("links", []))


def narrow_window(timestamp, seconds=60):
    """Match catalogue acquisition time closely; does not promise scene-ID selection."""
    date = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    return tuple((date + timedelta(seconds=delta)).astimezone(timezone.utc).isoformat().replace("+00:00", "Z") for delta in (-seconds, seconds))


def projected_geometry(bbox, epsg=32635):
    """Transform actual polygon vertices into metre coordinates (Finland example)."""
    from shapely.geometry import box, mapping
    from shapely.ops import transform
    from pyproj import Transformer
    polygon = box(*bounds(bbox)["bbox"])
    transformer = Transformer.from_crs("EPSG:4326", f"EPSG:{epsg}", always_xy=True)
    projected = transform(transformer.transform, polygon)
    return {"geometry": mapping(projected), "properties": {"crs": f"http://www.opengis.net/def/crs/EPSG/0/{epsg}"}}


def statistics(token, bbox, start, end):
    import requests
    payload = {"input": {"bounds": projected_geometry(bbox), "data": [{"type": "sentinel-2-l2a", "dataFilter": {"maxCloudCoverage": 20, "mosaickingOrder": "mostRecent"}}]}, "aggregation": {"timeRange": {"from": start, "to": end}, "aggregationInterval": {"of": "P10D", "lastIntervalBehavior": "SHORTEN"}, "resx": 10, "resy": 10, "evalscript": STATS_EVALSCRIPT}}
    return checked_json(requests.post(f"{BASE}/statistics/v1", json=payload, headers={"Authorization": f"Bearer {token}"}, timeout=(10, 180))), payload


def statistic_rows(response, site, period):
    rows = []
    for interval in response.get("data", []):
        bands = interval.get("outputs", {}).get("features", {}).get("bands", {})
        row = {"site": site, "period": period, "from": interval["interval"]["from"], "to": interval["interval"]["to"]}
        for index, band in enumerate(("red", "nir", "ndvi")):
            stats = bands.get(f"B{index}", {}).get("stats", {})
            count = max(0, stats.get("sampleCount", 0) - stats.get("noDataCount", 0))
            row[f"{band}_mean"] = stats.get("mean", float("nan")) if count else float("nan")
            row[f"{band}_valid_count"] = count
        rows.append(row)
    return rows
