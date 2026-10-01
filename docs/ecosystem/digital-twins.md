# Digital Twins: choose the correct time horizon

[Home](../../README.md) · [Ecosystem](README.md) · [Polytope guide](../services/polytope.md)

**Digital Twin outputs are model simulations.** They complement Earth observations and field measurements. They require interpretation of the selected experiment, model, grid, temporal sampling, and variable metadata.

| Twin | Purpose and time horizon | Possible partner use |
| --- | --- | --- |
| **Climate Change Adaptation DT (Climate DT)** | Global, multi-decadal climate information at kilometre-scale resolution; includes scenario and storyline simulations | Long-term context for precipitation, temperature and climate risk |
| **Weather-Induced Extremes DT (Extremes DT)** | Short-range high-resolution weather simulations; global continuous and regional on-demand components | Extreme rainfall, drought/weather context, and inputs to suitable impact models |

The Climate DT purpose is documented by [DestinE](https://destination-earth.eu/news/updates-on-the-climate-change-adaptation-digital-twins/); the global and regional Extremes components are described by the [Data Lake](https://data.destination-earth.eu/extremes-dt).

## Access routes

Use [Polytope](../services/polytope.md) for native multidimensional selection and feature extraction; [EDH](../services/earth-data-hub.md) provides selected preprocessed Zarr mirrors; [EDEN](../services/eden.md) and [SesamEO](../services/sesameo.md) support discovery. Collection coverage can differ across routes. For current Climate DT generations and holdings, begin with the [official Polytope examples](https://github.com/destination-earth-digital-twins/polytope-examples/tree/main/climate-dt) and the service's live catalogue.

**Upgraded Access is required for Digital Twin datasets.** Complete [access setup](access-model.md) before planning a live meeting demonstration. [Official Polytope service page](https://platform.destine.eu/services/service/polytope/)

## Questions to record before using a simulation

1. Is the experiment historical, scenario, or storyline? What generation and model produced it?
2. Does the timestamp represent validity time, forecast initialization, lead time, or an accumulation interval?
3. Is the grid regular latitude–longitude, HEALPix, or another mesh? Was it regridded?
4. Does the variable represent a rate, instantaneous value, accumulation, or temporal mean?
5. What observations or independent models support evaluation for the intended area?

A historical climate simulation need not reproduce the observed weather on a particular historical day. Comparing an individual date with a field observation needs a scientifically appropriate experiment and method. ERA5-Land provides historical reanalysis context; it is a separate data category.

Regional climate simulations are not direct measurements at a field site. Check their grid, time scale and uncertainty before using them to explain local conditions.

Continue to [Polytope](../services/polytope.md) or the [tutorial index](../../notebooks/README.md).
