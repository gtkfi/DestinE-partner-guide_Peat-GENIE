# Near-data computing and MLOps Studio

[Home](../../README.md) · [Services](README.md) · [HDA](data-lake-hda.md) · [Insula](insula.md)

**Run established workflows close to large datasets when local transfer or memory becomes limiting.** First make a small workflow scientifically correct; then choose computing resources.

## Data Lake service choices

| Service | Practical role |
| --- | --- |
| **Stack** | Hosted JupyterLab and scalable interactive analysis |
| **Islet Compute** | Virtual machines for custom environments |
| **Islet Storage** | Object storage for project inputs and outputs |
| **Hook** | Invoke predefined or user-defined processing functions |
| **Fresh Data Pool (FDP)** | Cached data access through supported cloud interfaces |
| **MLOps Studio** | ML workflow and pipeline environment based on Kubeflow |

These are advertised in the [official Data Lake service directory](https://data.destination-earth.eu/services). Availability depends on the selected site, approved allocation, and service configuration; this guide does not promise default CPU, GPU, storage, or retention.

## Request resources before launching

1. Sign in to the [Data Lake portal](https://data.destination-earth.eu/) using the DestinE identity option.
2. Follow the official [Edge service access guide](https://destine-data-lake-docs.data.destination-earth.eu/en/latest/dedl-big-data-processing-services/Access-Edge-services/Access-Edge-services.html) and its linked request process.
3. Provide the use case, requested resources, intended datasets, and project needs.
4. Wait for resource approval, then launch the service allocated to your project.
5. Confirm dataset permissions separately. Compute access does not automatically grant Digital Twin data access.
6. Stop unnecessary compute resources according to provider instructions and export required results.

## MLOps Studio

The official prerequisites are a **My DataLake Services profile** and membership of an **operator-approved project**. A project administrator can invite collaborators. In the workspace, select the site, review allocated resources, create/select a namespace, then open the Studio dashboard. [Workspace access instructions](https://destine-data-lake-docs.data.destination-earth.eu/en/latest/working_with_ai_in_the_data_lake/mlops-studio/Access-the-MLOps-Studio-workspace/Access-the-MLOps-Studio-workspace.html)

A namespace scopes notebooks, jobs, volumes, and experiments. Choose a browser notebook for exploration or a training job for a prepared, repeatable script; verify namespace quota first. [Python workload guide](https://destine-data-lake-docs.data.destination-earth.eu/en/latest/working_with_ai_in_the_data_lake/mlops-studio/Choose-how-to-run-Python-workloads-in-MLOps-Studio/Choose-how-to-run-Python-workloads-in-MLOps-Studio.html)

For a research model, preserve data splits by site/time, preprocessing versions, reference labels, model configuration, metrics, and uncertainty. The workspace supplies computing machinery; validation must be designed by the research team.

## Continue

Use the [official Data Lake Gallery](https://destination-earth.github.io/DestinE-DataLake-Gallery/) for current provider examples and [setup](../setup/README.md) for this repository's environment. This guide has not launched paid or allocated resources, submitted jobs, or trained models on these services.
