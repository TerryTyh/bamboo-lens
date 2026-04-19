#!/usr/bin/env python3
"""Send a markdown brief to a WeCom group robot webhook."""

from __future__ import annotations

import json
import os
import sys
import urllib.request
from pathlib import Path


def load_markdown(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Brief file not found: {path}")
    return path.read_text(encoding="utf-8").strip()


def build_payload(markdown_text: str) -> bytes:
    payload = {
        "msgtype": "markdown",
        "markdown": {
            "content": markdown_text
        },
    }
    return json.dumps(payload).encode("utf-8")


def send(webhook_url: str, payload: bytes) -> str:
    request = urllib.request.Request(
        webhook_url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read().decode("utf-8")


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/send_wecom.py <brief-file>", file=sys.stderr)
        return 1

    webhook_url = os.environ.get("WECOM_WEBHOOK_URL", "").strip()
    if not webhook_url:
        print("Missing env: WECOM_WEBHOOK_URL", file=sys.stderr)
        return 1

    brief_path = Path(sys.argv[1]).resolve()
    markdown_text = load_markdown(brief_path)
    response_text = send(webhook_url, build_payload(markdown_text))
    print(response_text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
