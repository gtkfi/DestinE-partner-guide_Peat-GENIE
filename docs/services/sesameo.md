# SesamEO: one discovery interface, several providers

[Home](../../README.md) · [Services](README.md) · [DeltaTwin](deltatwin.md)

**SesamEO bridges multiple catalogues through a common browser interface.** You can search collections, choose providers, filter products, and inspect/download results according to each provider's capabilities. Operated by GAEL Systems, it is listed as **Operational**. DT datasets require Upgraded Access. [Official service page](https://platform.destine.eu/services/service/sesameo/)

## Browser onboarding

1. Sign in via DestinE, then use **Go to service** on the official service page.
2. Search themes or collections; open the collection description.
3. If several providers serve a collection, select the provider explicitly.
4. Set a short date range and a small AOI.
5. Inspect product content and metadata, then download a small result.
6. Record provider, collection, product ID, filter settings, and retrieval date.

A catalogue bridge is not a promise that every provider offers the same filters, formats, latency, or access rights.

## Provider credentials and service API key

In the **Providers** screen, check “operations requiring credentials.” Some operations require the original provider's account; the documentation gives CDSE downloads as an example. The SesamEO login does not replace those credentials.

For automation, open **My SesamEO Account**, create an API key, and choose a finite expiration suitable for the project. Requests use the **`X-API-KEY`** header. The browser's API tab can show a request reflecting the selected filters. Do not copy the example keys printed in provider documentation. Use your own local secret and avoid saving it in notebook output. [Official SesamEO documentation](https://platform.destine.eu/docs/sesameo/doc/index.html)

The documented API is OData-based; use the actual service-generated request for the selected provider. Do not transplant a DEDL STAC or CDSE Sentinel Hub request unchanged.

## Research handoff

If downloading native Sentinel-2 bands, retain the product metadata needed for radiometric conversion and quality masks. The original archive calculated NDVI from manually obtained bands; reproducible analysis requires knowing whether these are native digital numbers, harmonized reflectance, or a rendered export.

The current service page also lists CAMS greenhouse-gas reanalysis and inversion products. These describe atmospheric or regional context, not direct site-level flux measurements. Check the exact collection metadata and coverage. [Current portfolio listing](https://platform.destine.eu/services/service/sesameo/)

Continue with [data quality](../reference/data-quality.md), [tutorials](../../notebooks/README.md), or [DeltaTwin](deltatwin.md) to explore workflow reuse.

**Verification boundary:** onboarding and API-key steps were documented; no account credentials were entered or product download executed.
