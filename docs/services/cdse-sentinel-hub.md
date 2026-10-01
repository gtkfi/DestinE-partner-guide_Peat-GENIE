# Related platform: CDSE Browser and Sentinel Hub

[Home](../../README.md) · [Services](README.md) · [Accounts](../setup/accounts.md)

**Copernicus Data Space Ecosystem (CDSE) is a related external platform.** The summer-project Sentinel Hub examples use CDSE endpoints. Keep this route visible because it supplies useful EO workflows, while clearly separating its account, credentials, and API deployment from DestinE.

## Choose the interface

| Interface | Use it for |
| --- | --- |
| [Copernicus Browser](https://browser.dataspace.copernicus.eu/) | Visual discovery, comparison, and downloads |
| Sentinel Hub **Catalog API** | Find acquisitions and inspect metadata |
| Sentinel Hub **Process API** | Request bands or computed raster outputs over an AOI |
| Sentinel Hub **Statistical API** | Request time-interval statistics rather than full imagery |

The [Browser guide](https://documentation.dataspace.copernicus.eu/Applications/Browser.html) describes its account and exploration workflow; the [Sentinel Hub documentation](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub.html) explains API choices.

## Register and create an OAuth client

1. Create/sign in to a [CDSE account](https://dataspace.copernicus.eu/).
2. Open the Sentinel Hub dashboard via your profile.
3. In **User Settings → OAuth clients**, choose **Create**.
4. Give the client a descriptive project name and suitable expiry.
5. Copy the displayed client ID and secret into your protected local configuration. The secret is shown only during creation.
6. Use the client-credentials flow to obtain a bearer token; reuse it within its validity.

The CDSE token endpoint is:

`https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token`

The service base is:

`https://sh.dataspace.copernicus.eu`

Follow the [official authentication guide](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Overview/Authentication.html). DestinE, EDH, and SesamEO tokens do not replace a CDSE Sentinel Hub OAuth client.

## Scientific settings to make explicit

For Sentinel-2, choose the product level, reflectance units, and cloud/shadow/snow masks; report valid-pixel coverage. For native L2A files, apply the product metadata's calibration rather than assuming a shared scale is sufficient. [Sentinel-2 product documentation](https://sentiwiki.copernicus.eu/web/s2-products)

For Sentinel-1, document polarization, orbit direction, acquisition geometry, processing corrections, and whether backscatter is linear or decibels. Treat radar changes as features requiring interpretation, not a direct water-table measurement.

For statistics, the request CRS controls resolution units. If intending metre-scale sampling, use an appropriate projected CRS and actually transform your AOI. Inspect valid-sample counts when aggregating intervals.

Continue to [tutorials](../../notebooks/README.md), [data quality](../reference/data-quality.md), or [SesamEO](sesameo.md) for browser discovery through DestinE.

