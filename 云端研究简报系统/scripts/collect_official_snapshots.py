#!/usr/bin/env python3
from __future__ import annotations

import gzip
import json
import ssl
import urllib.request
from urllib.error import HTTPError
from urllib.parse import urlparse
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG_FILE = ROOT / "config" / "companies.json"
SNAPSHOT_DIR = ROOT / "outputs" / "snapshots"
MANIFEST_FILE = SNAPSHOT_DIR / "manifest.json"


def load_companies() -> list[dict]:
    return json.loads(CONFIG_FILE.read_text(encoding="utf-8"))["companies"]


def slugify(url: str) -> str:
    return (
        url.replace("https://", "")
        .replace("http://", "")
        .replace("/", "_")
        .replace("?", "_")
        .replace("&", "_")
        .replace("=", "_")
    )


def fetch(url: str) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36 BambooLensBot/0.1"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
    }
    if "inovance.com/portal-front/api/" in url:
        headers.update(
            {
                "Accept": "application/json, text/plain, */*",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.inovance.com/news/list?typeId=1",
            }
        )
    context = ssl.create_default_context()
    host = urlparse(url).netloc.lower()

    def _read(target_url: str) -> str:
        request = urllib.request.Request(target_url, headers=headers, method="GET")
        with urllib.request.urlopen(request, context=context, timeout=30) as response:
            raw = response.read()
            encoding = (response.headers.get("Content-Encoding") or "").lower()
            if "gzip" in encoding or raw[:2] == b"\x1f\x8b":
                raw = gzip.decompress(raw)
            return raw.decode("utf-8", errors="ignore")

    def _proxy_url(target_url: str) -> str:
        return f"https://r.jina.ai/http://{target_url.replace('https://', '').replace('http://', '')}"

    try:
        return _read(url)
    except HTTPError as error:
        if error.code == 403 and ("tsmc.com" in host):
            return _read(_proxy_url(url))
        raise
    except Exception:
        if host == "investors.constellationenergy.com":
            return _read(_proxy_url(url))
        raise


def main() -> None:
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    manifest: list[dict] = []
    now = datetime.now().strftime("%Y%m%d-%H%M%S")

    for company in load_companies():
        for url in company.get("official_sources", []):
            filename = f"{company['id']}__{now}__{slugify(url)}.html"
            path = SNAPSHOT_DIR / filename
            try:
                html = fetch(url)
                path.write_text(html, encoding="utf-8")
                manifest.append(
                    {
                        "company_id": company["id"],
                        "company_name": company["name"],
                        "url": url,
                        "file": str(path),
                        "status": "ok",
                        "fetched_at": now,
                    }
                )
            except Exception as error:  # noqa: BLE001
                manifest.append(
                    {
                        "company_id": company["id"],
                        "company_name": company["name"],
                        "url": url,
                        "status": "error",
                        "error": str(error),
                        "fetched_at": now,
                    }
                )

    MANIFEST_FILE.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Snapshot manifest written to: {MANIFEST_FILE}")


if __name__ == "__main__":
    main()
