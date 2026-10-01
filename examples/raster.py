"""Scientific raster checks; native DN calibration is explicit."""
from pathlib import Path
import xml.etree.ElementTree as ET
import numpy as np


def ndvi(red, nir, valid=None):
    """Return NaN for masks, nonfinite inputs, or a zero denominator."""
    red, nir = np.asarray(red, dtype=float), np.asarray(nir, dtype=float)
    if red.shape != nir.shape:
        raise ValueError("Red and near infrared must have the same shape.")
    usable = np.isfinite(red) & np.isfinite(nir) & (np.abs(nir + red) > 1e-12)
    if valid is not None:
        usable &= np.broadcast_to(np.asarray(valid, dtype=bool), red.shape)
    result = np.full(red.shape, np.nan)
    np.divide(nir - red, nir + red, out=result, where=usable)
    return result


def calibrate_dn(dn, quantification, offset, nodata=0):
    """L2A BOA reflectance = (DN + metadata offset) / quantification."""
    if not np.isfinite(quantification) or quantification <= 0 or not np.isfinite(offset):
        raise ValueError("Invalid calibration values.")
    dn = np.asarray(dn, dtype=float)
    return np.where(np.isfinite(dn) & (dn != nodata), (dn + offset) / quantification, np.nan)


def l2a_calibration(metadata_path, bands=("B04", "B08")):
    """Read SAFE product MTD_MSIL2A.xml; fail if calibration is ambiguous."""
    root = ET.parse(metadata_path).getroot()
    local = lambda element: element.tag.rsplit("}", 1)[-1]
    q = [float(e.text) for e in root.iter() if local(e) in {"BOA_QUANTIFICATION_VALUE", "QUANTIFICATION_VALUE"} and e.text]
    if not q or any(value != q[0] for value in q):
        raise ValueError("A unique BOA quantification value was not found in product metadata.")
    # Sentinel-2 product spectral band identifiers are zero-based.
    ids = {"B01": "0", "B02": "1", "B03": "2", "B04": "3", "B05": "4", "B06": "5", "B07": "6", "B08": "7", "B8A": "8", "B09": "9", "B10": "10", "B11": "11", "B12": "12"}
    offsets = {e.attrib.get("band_id"): float(e.text) for e in root.iter() if local(e) == "BOA_ADD_OFFSET" and e.text}
    if any(ids[b] not in offsets for b in bands):
        raise ValueError("BOA offsets absent. Confirm a legacy/harmonized product explicitly; do not guess offsets.")
    return {band: (q[0], offsets[ids[band]]) for band in bands}


def valid_scl(scl):
    """Keep vegetation, bare soil and water; conservative SCL example policy."""
    return np.isin(np.asarray(scl), [4, 5, 6])


def read_pair_window(red_path, nir_path, bbox_wgs84, scl_path=None):
    """Read only an AOI, align categorical SCL by nearest-neighbour resampling."""
    import rasterio
    from rasterio.windows import from_bounds
    from rasterio.warp import transform_bounds, reproject, Resampling
    with rasterio.open(red_path) as red_ds, rasterio.open(nir_path) as nir_ds:
        if red_ds.crs != nir_ds.crs or red_ds.transform != nir_ds.transform or red_ds.shape != nir_ds.shape:
            raise ValueError("Band grids differ; obtain matching B04/B08 or explicitly reproject.")
        if red_ds.crs is None:
            raise ValueError("Raster CRS is missing.")
        bounds = transform_bounds("EPSG:4326", red_ds.crs, *bbox_wgs84, densify_pts=21)
        window = from_bounds(*bounds, transform=red_ds.transform).round_offsets().round_lengths()
        window = window.intersection(rasterio.windows.Window(0, 0, red_ds.width, red_ds.height))
        if window.width * window.height > 4_000_000:
            raise ValueError("Use a smaller AOI (at most four million pixels in this example).")
        red = red_ds.read(1, window=window, masked=True)
        nir = nir_ds.read(1, window=window, masked=True)
        valid = ~np.ma.getmaskarray(red) & ~np.ma.getmaskarray(nir) & (red.data != 0) & (nir.data != 0)
        transform = red_ds.window_transform(window)
        if scl_path:
            with rasterio.open(scl_path) as scl_ds:
                scl = np.zeros(red.shape, dtype="uint8")
                reproject(source=rasterio.band(scl_ds, 1), destination=scl, src_transform=scl_ds.transform, src_crs=scl_ds.crs, dst_transform=transform, dst_crs=red_ds.crs, resampling=Resampling.nearest, dst_nodata=0)
                valid &= valid_scl(scl)
        return red.data, nir.data, valid, {"crs": str(red_ds.crs), "transform": list(transform), "shape": list(red.shape), "scl_mask_applied": bool(scl_path)}


def numeric_ndvi(values, color_interpretations, scale=1.0, offset=0.0):
    """Reject rendered RGB(A) exports rather than claiming their colors are NDVI."""
    colors = {getattr(c, "name", str(c)).split(".")[-1].lower() for c in color_interpretations}
    if {"red", "green", "blue"}.issubset(colors):
        raise ValueError("This is an RGB/RGBA visualization. Download documented numeric NDVI values.")
    out = np.asarray(values, dtype=float) * scale + offset
    finite = out[np.isfinite(out)]
    if finite.size == 0 or finite.min() < -1.001 or finite.max() > 1.001:
        raise ValueError("Values are outside numeric NDVI range; verify band semantics and scale/offset.")
    return out
