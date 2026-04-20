#!/usr/bin/env python3
from __future__ import annotations

import json
import ssl
import urllib.request
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
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36 BambooLensBot/0.1"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
        },
        method="GET",
    )
    context = ssl.create_default_context()
    with urllib.request.urlopen(request, context=context, timeout=30) as response:
        return response.read().decode("utf-8", errors="ignore")


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
