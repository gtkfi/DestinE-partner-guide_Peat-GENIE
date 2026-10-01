# Resolve common setup and data issues

[Home](../../README.md) · [Setup](README.md) · [Accounts](accounts.md) · [Quality checks](../reference/data-quality.md)

| Symptom | Likely cause | Next action |
| --- | --- | --- |
| Module not found | Notebook uses another Python kernel | Print `sys.executable`; select the environment created in setup |
| Missing local input | Required raster is not distributed | Follow the notebook's download recipe; set its `INPUT_*` path |
| Token request fails | Wrong identity route, expired client or incomplete login | Use the matching account page; inspect HTTP status without printing credentials |
| 401 after a previous successful run | Access token expired | Obtain a fresh token using the supported provider flow |
| 403 | Insufficient permissions, terms or collection entitlement | Check service onboarding, upgraded access and collection policy |
| 429 | Rate or processing quota reached | Respect `Retry-After`; reduce request size and check dashboard quota |
| EDH public test opens but private store fails | Credential-file lookup or API key | Check home-directory file, exact machine name and `trust_env=True` |
| Zarr metadata / codec error | Old store URL or incompatible environment | Use current catalogue snippet; keep EDH v3 and Polytope v2 environments separate |
| No catalogue results | Wrong collection, spatial/time filter, or scene availability | Inspect collection extent and queryables; widen one filter at a time |
| Scene exists but Process output differs | Time-window mosaicking or processing choices | Inspect request parameters; narrow the window; do not equate timestamp proximity with exact item identity |
| NDVI seems implausible | Calibration, invalid pixels, cloud or wrong export type | Check product metadata, additive offsets, SCL and band interpretation |
| Rainfall units seem wrong | Rate, accumulation or monthly mean conflated | Inspect `units`, time interval and product convention before conversion |
| Memory grows rapidly | Full tile / cube loaded or pixel table built | Crop/window first; subset lazy arrays before computing; keep compact summaries |
| Geographic subset is empty | Latitude order, longitude convention or CRS | Inspect coordinates; use correct ascending/descending slice and transformed geometry |
| HDA order status unclear | Preparation still running or request timed out | Preserve the local order record; query current status; do not resubmit automatically |

For provider support, send the timestamp, service, HTTP status, public collection/item IDs and a minimal request with credentials removed. Avoid copying a full response if it contains a signed asset URL. Keep scientific data questions separate from authentication failures.

For a failed local check, read its filename and diagnostic. The validator prints neither credential values nor remote responses. Authenticated tutorials deliberately stop when required metadata or inputs are absent; complete those prerequisites before running again.
