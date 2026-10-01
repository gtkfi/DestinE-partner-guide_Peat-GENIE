# Set up a reproducible workspace

[Home](../../README.md) · [Accounts](accounts.md) · [Troubleshooting](troubleshooting.md) · [Tutorials](../../notebooks/README.md)

Use **Python 3.12** in a fresh environment. The primary environment supports all notebooks except notebook 12 (Polytope), which uses a separate environment to keep its client stack independent of Earth Data Hub's Zarr v3 stack.

## Install the primary environment

Extract the ZIP first. Open a terminal inside the `DestinE-partner-guide-simplified` folder. Do not run from the ZIP preview.

**Windows PowerShell:**

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
.\.venv\Scripts\python.exe -m jupyterlab
```

**macOS / Linux:**

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
cp .env.example .env
.venv/bin/python -m jupyterlab
```

Open [00-offline-orientation.ipynb](../../notebooks/00-offline-orientation.ipynb) in JupyterLab. Select the Python kernel belonging to this environment. The offline notebook needs no account or downloaded raster. The command below executes it with the same interpreter used to launch the command:

```bash
python scripts/run_offline_notebook.py
```

Use your environment's full Python path if it is not activated. Successful execution saves an executed copy under `outputs/`; distributed notebook sources remain clean.

`requirements.txt` fixes the direct package versions used in the Windows Python 3.12 reference environment. `constraints-primary.txt` records its transitive resolution. To match that resolution more closely, install with `-r requirements.txt -c constraints-primary.txt`. macOS and Linux instructions are provided for portability; execution on those systems was not verified for this release. [Verification record](../reference/verification.md)

## Configure one tutorial at a time

Edit the local `.env` with a text editor. Empty fields are intentional. Fill only the variables requested by your chosen notebook. Keep downloaded inputs in `data/`; generated tables and provenance go in `outputs/`. Both directories ignore data files in Git.

| Tutorial route | Configuration |
| --- | --- |
| Sentinel Hub APIs | Your `CDSE_CLIENT_ID` and `CDSE_CLIENT_SECRET` |
| Browser / SesamEO band files | `INPUT_B04`, `INPUT_B08`, `INPUT_SCL`, metadata, calibration and intersecting AOI |
| NUPSI export | `INPUT_NUPSI`; select a numeric band only after checking its definition |
| EDEN precipitation file | Input path, year/month, and verified temporal convention |
| EDH remote arrays | Current credential-free dataset URL plus home-directory credential file |
| HDA | Interactive service login; explicit asset and approved download host(s) |
| Polytope | Separate environment, upgraded permissions, home-directory client configuration |

The default Helsinki-area AOI teaches API mechanics; it is not a study site selected for validation. Change it to your study area, check data coverage, and reproject where required. Numerical defaults such as rainfall conventions and integration duration must be checked against the selected product's metadata.

## Polytope environment

```powershell
py -3.12 -m venv .venv-polytope
.\.venv-polytope\Scripts\python.exe -m pip install -r requirements-polytope.txt
.\.venv-polytope\Scripts\python.exe -m ipykernel install --user --name destine-polytope --display-name "DestinE Polytope"
```

On macOS/Linux replace the Windows executable path with `.venv-polytope/bin/python`. In Jupyter select **DestinE Polytope** for notebook 12. This registration adds a kernel to your user account. Do not run EDH Zarr v3 notebooks in this kernel. Read [Polytope access](accounts.md#polytope-and-digital-twins) before retrieval.

## Check the repository

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests -v
python scripts/run_offline_notebook.py
```

These commands check local links, notebook structure/source, helper behavior and offline execution. They do not authenticate, download live collections, or place orders. [Troubleshooting](troubleshooting.md) · [What was checked](../reference/verification.md)
