"""Configuration and credential-safe provenance helpers."""
from pathlib import Path
from datetime import datetime, timezone
import json
import os
from urllib.parse import urlsplit


def repo_root(start=None):
    """Find the guide root when Jupyter starts in root or notebooks/."""
    start = Path(start or Path.cwd()).resolve()
    for candidate in (start, *start.parents):
        if (candidate / "examples" / "common.py").is_file():
            return candidate
    raise RuntimeError("Start Jupyter inside DestinE-partner-guide.")


def required_env(name):
    value = os.environ.get(name, "").strip()
    if not value:
        raise ValueError(f"Set {name} in the local, ignored .env file; see docs/setup/.")
    return value


def input_path(name):
    path = Path(required_env(name)).expanduser()
    if not path.is_absolute():
        path = repo_root() / path
    if not path.is_file():
        raise FileNotFoundError(f"Input for {name} is missing; see the notebook download recipe.")
    return path


def public_url(url):
    """Reject credentials/query tokens in a configured public dataset address."""
    p = urlsplit(url)
    if p.scheme != "https" or not p.hostname or p.username or p.password or p.query or p.fragment:
        raise ValueError("Use a credential-free HTTPS dataset URL; configure authentication separately.")
    return url


def record_provenance(filename, **details):
    """Write only explicitly supplied public metadata, never configuration or tokens."""
    folder = repo_root() / "outputs"
    folder.mkdir(exist_ok=True)
    target = (folder / filename).resolve()
    if target.parent != folder.resolve() or target.suffix != ".json":
        raise ValueError("Provenance filename must be a plain .json filename.")
    forbidden = ("password", "secret", "token", "authorization", "api_key")
    if any(any(word in key.lower() for word in forbidden) for key in details):
        raise ValueError("Do not include credentials in provenance.")
    target.write_text(json.dumps({"recorded_utc": datetime.now(timezone.utc).isoformat(), **details}, indent=2, default=str), encoding="utf-8")
    return target
