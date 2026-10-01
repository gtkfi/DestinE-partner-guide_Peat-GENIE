# Polytope: extract Digital Twin data efficiently

[Home](../../README.md) · [Services](README.md) · [Digital Twins](../ecosystem/digital-twins.md)

**Polytope retrieves selected parts of multidimensional Digital Twin data.** The service supports Python/REST access across geographically distributed holdings. It is operated by ECMWF and listed as **Operational**; DT data requires Upgraded Access. [Official service page](https://platform.destine.eu/services/service/polytope/)

## Begin with provider-maintained examples

Use the [official Polytope examples](https://github.com/destination-earth-digital-twins/polytope-examples), especially the [Climate DT guide](https://github.com/destination-earth-digital-twins/polytope-examples/tree/main/climate-dt). It covers model/variable discovery, full-field retrieval, and feature extraction such as points, polygons, and time series.

1. Confirm your DestinE account has the needed upgraded DT permission.
2. Create the environment specified by the chosen official examples.
3. Authenticate with their current documented recipe.
4. Discover an available model, experiment, generation, variable, and time interval.
5. Start with one variable and a small feature request.
6. Record the exact request and output metadata before interpreting it.

The current Climate DT explorer examples pin **Zarr v2** for their virtual-store implementation. Keep this environment separate from [EDH](earth-data-hub.md) workflows using Zarr v3; a single blanket dependency set can break one route. [Official Climate DT environment guidance](https://github.com/destination-earth-digital-twins/polytope-examples/tree/main/climate-dt)

## Authentication without the missing legacy script

The source archive referenced a `desp-authentication.py` file that was absent. Do not reuse that unresolved dependency. The provider's current example authentication notebook is one supported starting point.

The Platform authentication library [destinepyauth](https://github.com/SercoSPA/DestinE-Platform-AuthN) also documents `get_token("polytope")`, which stores refresh authentication material in `~/.polytopeapirc`. Treat that file as a secret, leave it outside the shared repository, and never print its contents. Compatibility and permissions still need verification in the chosen environment.

## Interpretation before plotting

A returned value may be a rate, a time mean, or an accumulation. Inspect its units and interval before multiplying by seconds or summing timestamps. A gridded simulation may use HEALPix or another mesh; record regridding/interpolation if converting to a regular raster.

Use [data-quality guidance](../reference/data-quality.md) and [this repository's tutorial index](../../notebooks/README.md). No authenticated Polytope extraction was executed while preparing these service notes; permission and remote behavior remain access-dependent.

