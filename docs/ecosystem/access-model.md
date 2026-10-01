# Access model: one platform account, several permission layers

[Home](../../README.md) · [Ecosystem](README.md) · [Accounts](../setup/accounts.md)

## Begin with a DestinE account

On the [DestinE Platform](https://platform.destine.eu/), choose **Sign In → Register**, complete registration, and sign in. Selected services are available with ordinary registration. [Registration FAQ](https://platform.destine.eu/support-faq/)

If you need advanced features or Digital Twin data, complete the user-category fields in your profile and submit an [Access Policy Upgrade](https://platform.destine.eu/access-policy-upgrade/) request describing your organization, project, use case, and required data. Approval is assessed against the policy; it is not automatic. [Access policy instructions](https://platform.destine.eu/support-pages/access-policy/)

## Permission and authentication are different

| Need | Account / permission layer | What to do next |
| --- | --- | --- |
| Browse selected platform services | DestinE account | Launch from the catalogue and check the service's own requirements |
| Digital Twin datasets | DestinE account with Upgraded Access | Apply through the Platform; confirm the dataset is accessible after approval |
| Data Lake item searches/downloads | DestinE identity exchanged into a DEDL token | Follow [HDA authentication](../services/data-lake-hda.md) |
| Data Lake compute/storage | My DataLake Services profile and approved resources/project | Follow [near-data computing](../services/near-data-computing.md) |
| EDH data | Service API key; upgraded access for restricted DT collections | Open [Quota & API Keys](https://earthdatahub.destine.eu/quota-api-keys) |
| SesamEO automation | SesamEO API key; possibly provider credentials too | Follow [SesamEO](../services/sesameo.md) |
| CDSE Sentinel Hub API | Separate CDSE account and OAuth client | Follow [CDSE](../services/cdse-sentinel-hub.md) |

See the adjacent service guides for the official source of each service-specific requirement. Compute approval and Digital Twin data approval are separate: the [HDA documentation](https://destine-data-lake-docs.data.destination-earth.eu/en/latest/dedl-discovery-and-data-access/Harmonized-Data-Access/API-Guide/Authentication-And-Quotas.html) directs DT permissions through the Platform, rather than ordinary Data Lake role requests.

## Keep credentials out of the shared guide

Use your own local `.env`, environment variables, a protected credential file, or the provider's supported sign-in mechanism. Treat API keys, passwords, bearer tokens, refresh tokens, and signed download URLs as secrets. Never place them in a notebook cell, saved output, screenshot, committed configuration, meeting slide, or ZIP.

Do not print complete authentication responses. Reuse and refresh tokens through supported libraries. This repository's examples must fail clearly when a credential is missing, without displaying it. See [setup](../setup/README.md).

## Evidence to share with your team

Share the service name, approval state, collection ID, permitted operation, and a date-stamped success/failure summary. Do not share credentials. A public catalogue response proves discovery works; it does not prove data access or compute resources are approved.

