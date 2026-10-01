# Insula: notebook development and processing

[Home](../../README.md) · [Services](README.md) · [Near-data computing](near-data-computing.md)

**Insula offers two complementary routes:** Code for interactive development, and Processing for running algorithms. Both are operated by CGI and listed as **Operational**. [Code service](https://platform.destine.eu/services/service/insula-code/), [Processing service](https://platform.destine.eu/services/service/insula-processing/)

| Route | Choose it when |
| --- | --- |
| **Insula Code** | You want a browser-hosted Jupyter notebook and Python environment |
| **Insula Processing / Intellect** | You want existing processing services or to package an algorithm for repeatable execution |
| **Perception** within the documented Insula workflow | You want discovery, visualization, and inspection of products/results |

The [Code guide](https://platform.destine.eu/docs/insula/doc/lab/index.html) describes its JupyterHub/notebook environment; the [Insula guide](https://platform.destine.eu/docs/insula/doc/insula/index.html) describes discovery and processing concepts.

## First notebook

1. Register/sign in through DestinE and launch [Insula Code](https://code.insula.destine.eu/).
2. Open the provider's `getting-started` examples in your workspace.
3. Choose a kernel matching the example, inspect the packages, and run a small request.
4. Keep a personal copy of your adaptations and record environment versions.
5. Save outputs and provenance; export a backup needed by your project.

The provider supplies examples automatically. Keep personal changes separate from provider-managed examples so later updates do not conflict. [Official example guidance](https://platform.destine.eu/docs/insula/doc/lab/examples.html)

The May 2026 release explicitly distinguishes standard and Polytope kernels. That distinction matters when Zarr/earthkit versions differ between workflows. [Release note](https://platform.destine.eu/general/insula-code-and-insula-processing-new-release-live-on-15-may/)

## Bring an algorithm

The documented “Integrate your own algorithm” feature requires the **Expert User** role. It packages Linux algorithms and dependencies as Docker images. Define the algorithm's inputs, outputs, resources, and metadata, then test a small case before systematic processing. [Integration guide](https://platform.destine.eu/docs/insula/doc/insula/intellect/develop.html)

Ask Platform support about your required role and resource allocation; do not assume ordinary registration enables algorithm onboarding. DT data still requires its own upgraded permission.

## Partner practice

Use Code to refine one AOI workflow, then consider Processing once it is stable. Record the Docker image version, code revision, data request, and output metadata. Generic processing capability does not establish a validated model for a specific target.

**Verification boundary:** this repository provides orientation and local tutorials; no Insula workspace or container deployment was executed during preparation. Use [setup](../setup/README.md) and the [tutorial index](../../notebooks/README.md) for the delivered examples.
