# NUPSI: guided satellite exploration

[Home](../../README.md) · [Services](README.md) · [Data quality](../reference/data-quality.md)

**NUPSI is a useful browser entry point for readers with limited programming experience.** It supports European NUTS administrative areas and custom areas of interest, temporal exploration, and satellite-product exports. Operated by Alia Space Systems, it is listed as **Operational**. [Official service page](https://platform.destine.eu/services/service/nupsi/)

## A first meeting-friendly exploration

1. Sign in through the [Platform account route](../setup/accounts.md) and open [NUPSI](https://nupsi.destine.eu/).
2. Start the interface tour.
3. Choose a NUTS area, draw a polygon, or import a GeoJSON AOI.
4. Select the satellite/product or thematic view and time period.
5. Compare dates in the timeline, record the selected mosaic and processing settings.
6. Export only a small area and save its metadata before numerical analysis.

The [official documentation](https://platform.destine.eu/docs/nupsi/doc/index.html) describes monthly cloudless Sentinel-2 mosaics, Sentinel-1 mosaics, administrative-area navigation, and custom AOIs. NUTS boundary editions can differ by product year; record the actual version used.

## Visualization versus scientific values

A GeoTIFF extension does not guarantee that an export contains numeric vegetation-index values. Inspect:

| Check | Why it matters |
| --- | --- |
| Band descriptions and color interpretation | Four bands may represent red/green/blue/alpha rather than four physical measurements |
| Data type and range | Display values in 0–255 cannot automatically be treated as reflectance or NDVI |
| Scale, offset, nodata, and units | These control conversion into meaningful values |
| Mosaic interval and method | A monthly mosaic is a derived product, not one acquisition |
| CRS, pixel size, and AOI | Needed for consistent spatial comparisons |

The original archive included exploration of a four-band NUPSI export. Its source metadata did not establish numeric NDVI, so this guide retains the lesson as an explicit validation step.

## What a user can learn

Satellite mosaics can show visible vegetation and surface changes around a known site. A visual change is not by itself a measurement of the physical process causing it. Ground observations and a validated method are needed for such claims.

The page is a browser recipe, not an authenticated service test. Continue to the [tutorial index](../../notebooks/README.md) for reproducible raster inspection, or [CDSE Sentinel Hub](cdse-sentinel-hub.md) for programmatic pixel/statistics workflows.
