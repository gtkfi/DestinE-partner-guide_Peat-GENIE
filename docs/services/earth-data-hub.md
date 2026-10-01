# Earth Data Hub (EDH): analysis-ready arrays

[Home](../../README.md) · [Services](README.md) · [Tutorials](../../notebooks/README.md)

**EDH is useful when you want a small slice of a large climate or terrain dataset in Python.** It publishes preprocessed Zarr assets and a STAC catalogue for Xarray-based analysis. The Platform lists EDH, operated by B-Open, as **Operational**. [Official service page](https://platform.destine.eu/services/service/earth-data-hub/)

## Start without credentials

Use the [official getting-started guide](https://earthdatahub.destine.eu/getting-started) and its public test store:

```python
import xarray as xr

ds = xr.open_dataset(
    "https://data.earthdatahub.destine.eu/public/test-dataset-v0.zarr",
    engine="zarr",
    chunks={},
)
print(ds.sizes)
```

This illustrates dataset opening, not a promised field-specific result. Inspect variables, coordinates, and metadata before selecting values. An internet connection and a compatible environment are required.

## Prepare authenticated access

1. Sign in with your own DestinE account.
2. Open [Quota & API Keys](https://earthdatahub.destine.eu/quota-api-keys) and create/use your own API key.
3. Check whether the chosen dataset carries a restricted badge. Climate DT collections additionally need [Upgraded Access](../ecosystem/access-model.md).
4. Use the provider-supported authentication method. A protected `.netrc` / `_netrc` is one documented route; avoid embedding the key in a URL saved inside a notebook.
5. Open the selected dataset's catalogue page and use its current Xarray access snippet.

These requirements and credential-file options are documented in the [EDH getting-started guide](https://earthdatahub.destine.eu/getting-started). Keep credential files outside this repository, protect their permissions, and never include them in the ZIP.

## Subset before computing

Choose one variable, a short period, and a small study area before calling `.compute()` or `.load()`. Inspect latitude ordering, longitude convention, chunking, units, and missing values. Calculate spatial means using appropriate area weighting and a study-area mask.

The live EDH homepage reports **ERA5 holdings migrated to Zarr v3**, with future updates applied to the v3 datasets. Original summer-project URLs and older package pins need review. [EDH homepage](https://earthdatahub.destine.eu/)

The catalogue includes ERA5/ERA5-Land, Copernicus DEM, selected satellite samples, and DT mirrors; check the chosen collection for geographic coverage, variables, and processing transformations. [Catalogue](https://earthdatahub.destine.eu/catalogue)

Continue with [provider tutorials](https://earthdatahub.destine.eu/tutorials) and [B-Open's learning repository](https://github.com/bopen/edh-learning). Keep EDH Zarr v3 work separate from official Polytope explorer environments that currently pin Zarr v2.

