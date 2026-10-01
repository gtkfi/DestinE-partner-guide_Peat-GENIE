# Accounts, API keys and permissions

[Home](../../README.md) · [Environment](README.md) · [Access model](../ecosystem/access-model.md) · [Troubleshooting](troubleshooting.md)

An account establishes identity. A service permission establishes entitlement. An API credential allows software to act under that entitlement. Treat these as three separate checks.

## Choose the correct identity route

| Route | Sign-in / credential | Additional check | Guide |
| --- | --- | --- | --- |
| DestinE Platform services | Personal DestinE registration / SSO | Provider terms, quotas and service-specific onboarding | [Access model](../ecosystem/access-model.md) |
| DEDL HDA | Supported HDA authentication and token exchange; service-account options in current docs | Collection permission and delivery method | [HDA](../services/data-lake-hda.md) |
| Earth Data Hub | DestinE SSO, then an EDH API key | Dataset restrictions and request quota | [EDH](../services/earth-data-hub.md) |
| CDSE Sentinel Hub | Separate CDSE account, then OAuth client ID/secret | Processing quota and collection entitlement | [CDSE](../services/cdse-sentinel-hub.md) |
| SesamEO | SesamEO API key from My SesamEO Account | Underlying provider credentials where requested | [SesamEO](../services/sesameo.md) |
| Climate DT / Polytope | DestinE identity and client configuration | Upgraded access; compute allocation is a separate matter | [Polytope](../services/polytope.md) |

## DestinE Platform

1. Open the [official Platform](https://platform.destine.eu/) and choose its registration/sign-in route. Use an individual account and a working email address.
2. Complete the current registration steps, email verification and applicable terms. Sign in and confirm you can reach the service catalogue.
3. Open the specific service's page and follow its onboarding link. Read any provider agreement, project/resource request, or quota notice.
4. For restricted DT holdings, follow the [official access-upgrade application](https://platform.destine.eu/access-policy-upgrade/). Approval and eligible scope follow the [Access Policy](https://platform.destine.eu/support-pages/access-policy/); account creation alone does not grant these permissions.

Keep a consortium access checklist with service, account owner, permission request date and approval status. Do not put passwords or keys in that checklist. [Official support FAQ](https://platform.destine.eu/support-faq/)

## HDA authentication

The tutorials use the documented service-aware `destinepyauth` interface:

```python
from destinepyauth import get_token

result = get_token("hda")   # Interactive username, masked password, OTP if enabled
token = result.access_token
```

Do not display `result` or `token`. The library supplies HDA's token exchange; keep the current [DEDL authentication documentation](https://destine-data-lake-docs.data.destination-earth.eu/en/latest/dedl-discovery-and-data-access/Harmonized-Data-Access/API-Guide/Authentication-And-Quotas.html) as the authority if flows change. Automated deployments should follow its current service-account guidance. [Official authentication library](https://github.com/SercoSPA/DestinE-Platform-AuthN)

Notebook 13 defaults to search and inspection. Downloads and order placement require explicit local opt-in. Select an asset by its documented purpose, review its delivery hostname, and start with a small product. Some orders need preparation; avoid repeated submissions while a status is uncertain.

## Earth Data Hub API key

After signing in through DestinE, use [Quota & API Keys](https://earthdatahub.destine.eu/quota-api-keys) to obtain your personal EDH key. The provider supports a credential file in your home directory: `.netrc` on macOS/Linux, `_netrc` on Windows. It belongs outside this repository.

Use the provider's [credential-file instructions](https://earthdatahub.destine.eu/getting-started) for the `data.earthdatahub.destine.eu` and `api.earthdatahub.destine.eu` machines. Enter your key as the password field. Restrict the file to your user account; on Unix use `chmod 600 ~/.netrc`. On Windows inspect **Properties → Security** and ensure unintended users have no read access. If home-directory discovery fails, follow the provider's Windows setup instructions.

The notebooks pass `storage_options={"client_kwargs": {"trust_env": True}}` so Xarray's HTTP client can read this file. Dataset URLs in `.env` remain credential-free. Use the current catalogue snippet; do not restore a key-bearing URL from an old notebook. Start with the provider's public test dataset to separate connectivity problems from credential problems.

## CDSE OAuth client

1. Register and sign in at [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/).
2. Open the [Sentinel Hub dashboard](https://shapps.dataspace.copernicus.eu/dashboard/).
3. Go to **User settings → OAuth clients**. Create a client with a descriptive name. Save the generated client ID and secret in the local `.env` as `CDSE_CLIENT_ID` and `CDSE_CLIENT_SECRET`.
4. The helper exchanges those credentials for a short-lived access token using the CDSE identity endpoint. A successful token exchange precedes API calls; entitlement and quota errors can still occur afterwards.

Create a replacement client/secret if the existing credential is lost or exposed. Use the provider's current dashboard instructions when labels change. [Official OAuth guide](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Overview/Authentication.html)

## Polytope and Digital Twins

Complete the upgraded-access route for restricted datasets, then use the [separate environment](README.md#polytope-environment). The official authentication client supports `get_token("polytope")` and creates `.polytopeapirc` under your home directory. This file contains a refresh credential and must remain private. Never copy it into the repository or presentation materials. [Official client behavior](https://github.com/SercoSPA/DestinE-Platform-AuthN)

Confirm the current Polytope address, experiment, variable, grid and time coverage in the [official DT examples](https://destination-earth-digital-twins.github.io/polytope-examples/) and [Climate-DT explorer](https://github.com/destination-earth-digital-twins/polytope-examples/tree/main/climate-dt/explorer). The notebook preserves the source experiment as an example; it cannot establish access to that experiment for your account.

## Protect a shared demonstration

Use an individual credential for each person; do not distribute a consortium-wide `.env`. Clear live notebook outputs before committing. Provenance should contain public item IDs, request parameters and units, rather than tokens or signed URLs. If a credential is exposed, revoke/rotate it through the provider and replace affected shared artifacts. The [offline notebook](../../notebooks/00-offline-orientation.ipynb) needs no sign-in.
