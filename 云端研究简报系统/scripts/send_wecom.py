#!/usr/bin/env python3
"""Send a markdown brief to a WeCom group robot webhook."""

from __future__ import annotations

import json
import os
import time
import sys
import urllib.error
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


def send_once(webhook_url: str, payload: bytes, timeout: int = 20) -> str:
    request = urllib.request.Request(
        webhook_url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8")


def send_with_retry(webhook_url: str, payload: bytes, attempts: int = 3) -> str:
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            return send_once(webhook_url, payload, timeout=20 + (attempt - 1) * 10)
        except (TimeoutError, urllib.error.URLError) as exc:
            last_error = exc
            if attempt == attempts:
                break
            wait_seconds = attempt * 3
            print(
                f"WeCom send attempt {attempt}/{attempts} failed: {exc}. "
                f"Retrying in {wait_seconds}s...",
                file=sys.stderr,
            )
            time.sleep(wait_seconds)

    assert last_error is not None
    raise last_error


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
    response_text = send_with_retry(webhook_url, build_payload(markdown_text))
    print(response_text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
