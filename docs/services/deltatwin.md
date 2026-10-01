# DeltaTwin: reusable model components and workflows

[Home](../../README.md) · [Services](README.md) · [SesamEO](sesameo.md)

**DeltaTwin provides a collaborative environment for composing and executing model/workflow components.** It manages component storage, configuration, and versioning; its Run module executes user models. GAEL Systems operates it, and the Platform lists it as **Operational**. [Official service page](https://platform.destine.eu/services/service/delta-twin/)

DeltaTwin is a workflow service. Its name does not mean that every user component is one of the ECMWF Climate or Extremes Digital Twins.

## Begin with the browser

1. Sign in through DestinE, then open **Go to service** on the official page.
2. Read the [DeltaTwin documentation](https://platform.destine.eu/docs/deltatwin/doc/index.html).
3. Explore a provider example component and inspect its inputs and output artifacts.
4. Confirm your resource quota before starting a small run.
5. Inspect run status and logs; retrieve results together with component version and input references.
6. Keep exploratory artifacts private unless your consortium deliberately approves sharing.

The catalogue exposes quotas and the CLI offers a metrics command. Check the values assigned to your own account; this guide does not guarantee a resource allocation.

## Command-line route

The [CLI guide](https://platform.destine.eu/docs/deltatwin/doc/command_line.html) covers component, drive, run, schedule, and monitoring commands. Follow its installation and authentication instructions in an isolated environment.

The documented API URL is `https://api.deltatwin.destine.eu/`. Login persists a configuration file containing authentication material. Protect that file and exclude it from the shared repository. Avoid putting a password directly into a shell command because shell history can retain it. [CLI authentication guide](https://platform.destine.eu/docs/deltatwin/doc/command-line/docs/dev/basic.html)

## How it could support a workflow

A workflow might compose satellite-feature extraction, climate-feature preparation, a calibrated model, and result publication. This repository has not deployed such a workflow.

Preserve explicit contracts between steps: variable/unit names, CRS, spatial resolution, temporal aggregation, nodata, accepted inputs, and version identifiers. A workflow that executes successfully can still produce invalid science if those contracts are inconsistent.

The provider's 2025 release documents integration of SesamEO input URLs and a CDS connector starter kit. Verify the current component and account setup before relying on those routes. [Release note](https://platform.destine.eu/general/deltatwin-new-release-live-on-4-august/)

Continue to [Insula](insula.md) for notebook/algorithm development or [the tutorial index](../../notebooks/README.md) for this repository's delivered workflows.
