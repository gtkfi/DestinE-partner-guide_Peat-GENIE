# Shared example helpers

[Guide home](../README.md) · [Tutorial index](../notebooks/README.md) · [Environment](../docs/setup/README.md) · [Data quality](../docs/reference/data-quality.md)

These small Python modules make the tutorial logic inspectable and avoid copying authentication, calibration, or download code across notebooks. Importing them does not contact a service. Remote calls occur only when explicitly invoked from a live tutorial. They are educational helpers; they do not constitute a production client or validated scientific package.

| Module | Functions / purpose | Used by |
| --- | --- | --- |
| [common.py](common.py) | Locate root; require local configuration; validate credential-free dataset URLs; save explicitly public provenance | All notebooks |
| [raster.py](raster.py) | `ndvi`, `calibrate_dn`, `l2a_calibration`, `valid_scl`, `read_pair_window`, `numeric_ndvi` | Optical inputs / offline demonstration / NUPSI |
| [sentinel.py](sentinel.py) | CDSE OAuth; readable Process/Catalog/Statistical payloads; actual projected geometry; interval statistics parsing | Sentinel-1 and Sentinel-2 API notebooks |
| [climate.py](climate.py) | Explicit precipitation conventions; latitude weighting; valid-count-weighted composites; coordinate-order-aware subsets | ERA5-Land / EDEN / Polytope / offline demonstration |
| [hda.py](hda.py) | Host-checked API calls; explicit download host allowlist; size/time bounds; safe filenames; one-shot order recording | HDA Landsat |

## Numerical conventions

`ndvi(red, nir, valid=None)` expects calibrated, aligned numeric reflectance. It returns missing values for invalid data and zero denominators. Negative reflectance can produce indices outside [−1,1]; investigate rather than silently clipping.

`calibrate_dn(dn, quantification, offset)` applies the supplied metadata values and treats DN=0 as nodata. `l2a_calibration()` reads BOA quantification and band offsets from a SAFE product XML and stops when they cannot be established. A provider's already-harmonized or physical-reflectance export needs an explicitly different setting in the notebook.

`numeric_ndvi()` rejects RGB/RGBA color interpretation. Numeric range checks alone cannot prove band meaning; confirm that the provider labels the selected band as scientific NDVI and supplies any scale/offset.

`precipitation_mm()` has three explicit conventions:

- `accumulated_m`: metres of accumulated depth → millimetres.
- `monthly_mean_daily_m`: monthly mean daily depth in metres/day → monthly total in millimetres using the calendar's day count.
- `rate_kg_m2_s`: a documented interval-mean rate → depth using verified interval seconds.

The helper deliberately does not infer conventions from filenames. Rate integration is scientifically valid only when the stated interval and sampling semantics support it.

`latitude_weighted_mean()` is a cosine-latitude approximation for a regular geographic grid; do not apply it to arbitrary projected grids, irregular points or an undocumented HEALPix extraction. `weighted_interval_mean()` weights observed interval means by valid samples; it is a composite statistic rather than a uniform calendar-time mean.

## Request and retrieval boundaries

CDSE raster output is capped for teaching requests. S2 masks retain SCL vegetation, bare soil and water. S1 uses one orbit direction, IW dual polarization, terrain-normalized gamma0, orthorectification and **Copernicus 90 m DEM**; Copernicus 30 m access can require additional CDSE registration. Narrow catalogue time windows do not guarantee binding to a scene/relative-orbit identifier.

HDA helpers send the service token only to the exact authenticated HDA host. Downloads validate each HTTPS redirect against a user-reviewed allowlist, never infer an asset from a thumbnail or first dictionary entry, and do not trust server-provided filenames. Existing local files/order records require explicit inspection before retrying. An uncertain order is not automatically resubmitted.

Outputs may still contain sensitive study information. Keep `data/`, `outputs/`, `.env`, authentication files, signed URLs and private geographic inputs out of repository commits. Provenance accepts explicitly provided public metadata; it does not dump the full environment or authentication objects.

See the repository [verification record](../docs/reference/verification.md) for offline checks and live access limitations.
