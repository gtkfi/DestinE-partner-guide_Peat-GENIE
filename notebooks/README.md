# Choose a tutorial

[Guide home](../README.md) · [Start here](../docs/start-here.md) · [Environment](../docs/setup/README.md) · [Accounts](../docs/setup/accounts.md) · [Verification record](../docs/reference/verification.md)

Start with **[00 · Offline orientation](00-offline-orientation.ipynb)**. It uses small synthetic arrays and needs no account. Then choose a tutorial by service and access route. GitHub can display the notebook; running it requires the stated Python environment and, for live examples, the relevant service access.

**Shortest route:** run [00](00-offline-orientation.ipynb), then try [04 · Sentinel-2 Process API](04-sentinel-2-process.ipynb) if you have CDSE access, or [09 · EDH ERA5-Land](09-edh-era5-land.ipynb) if you have an EDH key. The full list below is optional reference material.

The 13 workflows adapted from the supplied project and one account-free orientation make 14 notebooks. The [migration notes](../docs/reference/migration.md) explain their origins. Original private inputs and credentials are excluded. Live requests have not been verified with service accounts in this release. File-based notebooks need your own documented inputs. See the [verification record](../docs/reference/verification.md).

| Tutorial | Learn / expected output | Access and input | Environment |
| --- | --- | --- | --- |
| [01 · Copernicus Browser NDVI](01-copernicus-browser-ndvi.ipynb) | Crop matching bands; calibrate native values with product metadata; plot NDVI | CDSE browser download; B04/B08, metadata, SCL | Main |
| [02 · SesamEO NDVI](02-sesameo-ndvi.ipynb) | Analyze SesamEO downloads using the same explicit calibration checks | DestinE/SesamEO access; local bands and metadata | Main |
| [03 · NUPSI export inspection](03-nupsi-raster-inspection.ipynb) | Distinguish numeric NDVI from color visualization; inspect a bounded sample | NUPSI export and declared numeric band semantics | Main |
| [04 · Sentinel-2 Process API](04-sentinel-2-process.ipynb) | Request reflectance; SCL-mask cloud/shadow/snow; plot NDVI | CDSE OAuth client ID and secret | Main |
| [05 · Sentinel-1 Process API](05-sentinel-1-process.ipynb) | Inspect VV/VH linear backscatter, decibels and ratio | CDSE OAuth client; fixed orbit/mode/polarization | Main |
| [06 · Sentinel-2 time series](06-sentinel-2-time-series.ipynb) | Search catalogue acquisitions; summarize narrow time windows | CDSE OAuth; up to five acquisitions | Main |
| [07 · Sentinel-1 time series](07-sentinel-1-time-series.ipynb) | Explore radar change with explicit orbit controls and limitations | CDSE OAuth; up to five acquisitions | Main |
| [08 · Sentinel-2 Statistical API](08-sentinel-2-statistics.ipynb) | Five AOIs × two months; metre-based geometry; sample-weighted composite table | CDSE OAuth and processing quota | Main |
| [09 · EDH ERA5-Land](09-edh-era5-land.ipynb) | Lazy climate subsets; precipitation units; area-weighted soil moisture | EDH API key / netrc; current Zarr 3 catalogue endpoint | Main / Zarr 3 |
| [10 · EDEN precipitation](10-eden-precipitation.ipynb) | Crop a COG; distinguish monthly mean daily depth from monthly total | Local EDEN export plus temporal/unit metadata | Main |
| [11 · EDH DEM](11-edh-dem.ipynb) | Small terrain subset and nearest-grid query; preserve datum information | EDH API key / netrc; current DEM endpoint | Main / Zarr 3 |
| [12 · Polytope Climate-DT](12-polytope-climate-dt.ipynb) | Northern Europe simulated rate subset; six-hour integration with explicit interval checks | Upgraded Climate-DT access; provider authentication | **Separate Polytope environment** |
| [13 · HDA Landsat](13-hda-landsat.ipynb) | Search STAC items; inspect assets; one direct download or a recorded order/status check | DestinE HDA authentication and collection access | Main |

## Choose an access route

- **Downloaded files:** use [01](01-copernicus-browser-ndvi.ipynb), [02](02-sesameo-ndvi.ipynb), [03](03-nupsi-raster-inspection.ipynb), or [10](10-eden-precipitation.ipynb) with files and metadata you have obtained.
- **CDSE APIs:** use [04](04-sentinel-2-process.ipynb) through [08](08-sentinel-2-statistics.ipynb) with CDSE OAuth credentials.
- **Earth Data Hub:** use [09](09-edh-era5-land.ipynb) or [11](11-edh-dem.ipynb) with that service's access configuration.
- **DestinE services:** use [12](12-polytope-climate-dt.ipynb) with upgraded Digital Twin permissions and the separate Polytope environment, or [13](13-hda-landsat.ipynb) with HDA access.

## Before enabling a live cell

1. Install and select the right [environment](../docs/setup/README.md). Start Jupyter inside this repository; notebooks locate the root from either `notebooks/` or the repository root.
2. Follow the service's [account and API instructions](../docs/setup/accounts.md). A CDSE OAuth client, EDH API key, and DestinE service token are different credentials.
3. Copy the [configuration template](../.env.example) to the ignored `.env` file. Keep private data in `data/` and outputs in `outputs/`.
4. Read the request's AOI, dates, dimensions and quota implications. Set `RUN_LIVE=True` only for the workflow you intend to run. HDA discovery and download/order switches are separate.
5. Run from a fresh kernel. Keep IDs, timestamps, CRS, variable units, masks, and sample counts with the result. Record failures/permissions without exposing tokens or signed URLs.


[Back to guide home](../README.md)
