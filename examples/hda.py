"""Bounded HDA catalogue access and explicit single-asset retrieval."""
from pathlib import Path
from urllib.parse import urlsplit, urljoin
import json
import re


def approved_url(url, allowed_hosts):
    p = urlsplit(url)
    if p.scheme != "https" or p.hostname not in set(allowed_hosts) or p.username or p.password:
        raise ValueError("Asset must be HTTPS on an explicitly approved hostname.")
    return url


def safe_filename(value):
    name = re.sub(r"[^A-Za-z0-9._-]", "_", str(value)).strip(".")
    if not name or name.upper().split(".")[0] in {"CON", "PRN", "AUX", "NUL", *[f"COM{i}" for i in range(1,10)], *[f"LPT{i}" for i in range(1,10)]}:
        raise ValueError("Choose a normal local filename.")
    return name[:180]


def request_json(method, url, token, authenticated_host, **kwargs):
    import requests
    approved_url(url, {authenticated_host})
    try:
        response = requests.request(method, url, headers={"Authorization": f"Bearer {token}"}, timeout=(10, 90), allow_redirects=False, **kwargs)
    except requests.RequestException:
        raise RuntimeError("HDA connection failed; check connectivity/authentication without logging credentials.") from None
    if not response.ok or 300 <= response.status_code < 400:
        raise RuntimeError(f"HDA returned HTTP {response.status_code}; inspect official endpoint/schema documentation.")
    return response.json()


def download_asset(url, directory, filename, allowed_hosts, token=None, authenticated_host=None, max_bytes=2_000_000_000):
    """Never send a DEDL token to an unrelated host; validate each redirect."""
    import requests
    directory = Path(directory).resolve()
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / safe_filename(filename)
    partial = target.with_name(target.name + ".part")
    if target.exists() or partial.exists():
        raise FileExistsError("Output exists; inspect/remove it explicitly before retrying.")
    current = approved_url(url, allowed_hosts)
    # A fresh request each time ensures Authorization is scoped to its exact host.
    for _ in range(6):
        host = urlsplit(current).hostname
        headers = {"Authorization": f"Bearer {token}"} if token and host == authenticated_host else {}
        try:
            response = requests.get(current, headers=headers, stream=True, timeout=(10, 180), allow_redirects=False)
        except requests.RequestException:
            raise RuntimeError("Asset connection failed; retry explicitly after checking provider access. URL withheld.") from None
        if 300 <= response.status_code < 400:
            location = response.headers.get("Location")
            response.close()
            if not location:
                raise RuntimeError("Redirect has no location.")
            current = approved_url(urljoin(current, location), allowed_hosts)
            continue
        with response:
            if not response.ok:
                raise RuntimeError(f"Asset returned HTTP {response.status_code}; no URL/token logged.")
            if int(response.headers.get("Content-Length", 0)) > max_bytes:
                raise ValueError("Asset exceeds the example size limit.")
            total = 0
            try:
                with partial.open("xb") as output:
                    for chunk in response.iter_content(1024 * 1024):
                        if chunk:
                            total += len(chunk)
                            if total > max_bytes:
                                raise ValueError("Asset exceeds the example size limit.")
                            output.write(chunk)
                partial.replace(target)
            except requests.RequestException:
                partial.unlink(missing_ok=True)
                raise RuntimeError("Asset transfer failed; partial output removed and signed URL withheld.") from None
            except Exception:
                partial.unlink(missing_ok=True)
                raise
            return target
    raise RuntimeError("Too many asset redirects.")


def submit_order_once(link, token, authenticated_host, record_path):
    """Never retry an uncertain order automatically or submit a duplicate."""
    record = Path(record_path)
    if record.exists():
        raise FileExistsError("Order record exists. Resume its status rather than placing another order.")
    if link.get("rel") != "retrieve" or link.get("method", "POST").upper() != "POST":
        raise ValueError("Use the selected item's documented POST retrieve link.")
    record.parent.mkdir(parents=True, exist_ok=True)
    record.write_text(json.dumps({"state": "submitting", "note": "If interrupted, inspect the HDA dashboard before retrying."}), encoding="utf-8")
    result = request_json("POST", link["href"], token, authenticated_host, json=link.get("body", {}))
    # Persist identifiers only; full responses can contain signed URLs.
    identifier = result.get("id") or result.get("order_id")
    record.write_text(json.dumps({"state": "submitted", "order_id": identifier}), encoding="utf-8")
    return result
