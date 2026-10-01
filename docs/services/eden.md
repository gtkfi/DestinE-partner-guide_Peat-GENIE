# EDEN: discover and retrieve products

[Home](../../README.md) · [Services](README.md) · [HDA distinction](data-lake-hda.md)

**EDEN provides a browser-oriented route to discovering DestinE and federated datasets.** It is operated by MEEO and listed as **Operational** on 28 September 2026. Digital Twin holdings require Upgraded Access. [Official service page](https://platform.destine.eu/services/service/eden/)

## Begin in the Finder

1. Register/sign in through [DestinE](../setup/accounts.md), then open [EDEN Finder](https://finder.eden.destine.eu/).
2. Find a dataset by name or topic. Open its information panel before browsing.
3. Apply required dataset-specific filters, dates, variables, and an area of interest.
4. Inspect product metadata and footprints. A map preview helps locate data but does not establish numeric analysis suitability.
5. Add a small product to the cart, submit the order, wait for readiness, then download.
6. Save the product metadata and request parameters beside the input file.

These steps follow the [official EDEN documentation](https://platform.destine.eu/docs/eden/doc/index.html). Read the service's current quotas there before planning batch retrieval.

## APIs: keep endpoints separate

| EDEN interface | Purpose | Access described in official documentation |
| --- | --- | --- |
| [EDEN STAC](https://stac.eden.destine.eu/stac/) | Collection and product discovery | Anonymous catalogue access |
| [EDEN OpenSearch](https://opensearch.eden.destine.eu/opensearch/datasets) | Metadata search | Anonymous |
| EDEN broker HDA `/api/v1` | Search, order, and retrieve through adapters | Token required |
| WMS, where offered | Rendered map visualization | Product/service-specific |

The broker API documentation is linked from the [EDEN documentation](https://platform.destine.eu/docs/eden/doc/index.html). It was access-blocked during this guide's documentation check; the Finder and written documentation remain the starting points. Do not substitute EDEN's broker paths into the [DEDL HDA STAC v2](data-lake-hda.md) client.

## Reproducible handoff to Python

For ERA5-Land, record the exact variable, units, temporal aggregation, interval, format, and any transformations applied by EDEN. “Monthly means” and “monthly totals” are different products. Multiplying metres by 1,000 changes the length unit, not the aggregation period.

For any GeoTIFF, inspect CRS, band descriptions, scale/offset, nodata, and provenance before calculations. A rendered WMS image is different from a scientific raster. Continue with [data-quality guidance](../reference/data-quality.md) and the [tutorial index](../../notebooks/README.md).

**Verification boundary:** this page is an onboarding recipe based on public documentation. No authenticated order or download was made while preparing the guide.

