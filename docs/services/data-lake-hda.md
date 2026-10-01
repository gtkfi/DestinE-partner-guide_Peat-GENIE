# DestinE Data Lake: Harmonised Data Access (HDA)

[Home](../../README.md) · [Services](README.md) · [Access model](../ecosystem/access-model.md)

**Use HDA to discover and access data through a common API across a federated portfolio.** It does not make all datasets scientifically interchangeable. Each collection retains its own metadata, licence, access rules, and delivery behavior.

## Current API and access

The official current endpoint is **`https://hda.data.destination-earth.eu/stac/v2/`**. The February 2026 release notice directs users to version 2 and reports service-account/API-key support alongside user logins. Use the current official setup for machine-to-machine access; an EDH or SesamEO key cannot be substituted. [Data Lake release notice](https://data.destination-earth.eu/news/6973898762a48c35be5ca737)

| Operation | Access |
| --- | --- |
| Services discovery, collections metadata, capabilities | Public |
| Item search, browsing, downloads and streaming | Authentication required |
| Restricted collections and Digital Twin outputs | Additional permission required |

The [authentication guide](https://destine-data-lake-docs.data.destination-earth.eu/en/latest/dedl-discovery-and-data-access/Harmonized-Data-Access/API-Guide/Authentication-And-Quotas.html) documents EODAG and `destine-auth` approaches and the DestinE-to-DEDL token exchange. Follow that route rather than assuming an ordinary Platform bearer token works on every DEDL endpoint.

## First successful workflow

1. Read the public [collections endpoint](https://hda.data.destination-earth.eu/stac/v2/collections). Identify a collection matching your data requirement.
2. Read its spatial/temporal extent, licence, queryable fields, and assets.
3. Authenticate using your own account and the supported client.
4. Search a small bounding box and a short time range; paginate deliberately.
5. Inspect one item and its assets before retrieving data. Some holdings require ordering or preparation rather than immediate download.
6. Retrieve only the needed asset or subset. Record collection ID, item ID, request, units, processing level, and retrieval date.

HDA supports file downloads, streaming, and asset-specific retrieval, subject to the dataset and permissions. [Official data-access guide](https://destine-data-lake-docs.data.destination-earth.eu/en/latest/dedl-discovery-and-data-access/Harmonized-Data-Access/API-Guide/Data-Access.html)

## Common points of confusion

- A public collection response establishes catalogue access; it does not establish download entitlement.
- **[EDEN](eden.md) also uses the label “HDA” for its own adapter API.** Its `/api/v1` paths are not interchangeable with this DEDL STAC v2 endpoint.
- Catalogue holdings, SDK arguments, and asset names can change. Discover them before constructing an automated workflow.
- Keep bearer tokens and any signed asset URLs out of notebook outputs.

The original archive explored Landsat HDA access. Continue with [this repository's tutorials](../../notebooks/README.md) or the [official Data Lake Gallery](https://destination-earth.github.io/DestinE-DataLake-Gallery/) for provider-maintained examples. [Near-data computing](near-data-computing.md) is the next step when local downloads become impractical.

