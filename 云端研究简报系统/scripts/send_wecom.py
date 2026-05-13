#!/usr/bin/env python3
"""Send a markdown brief to a WeCom group robot webhook."""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


MAX_MARKDOWN_BYTES = 3600


def load_markdown(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Brief file not found: {path}")
    return path.read_text(encoding="utf-8").strip()


def encoded_length(text: str) -> int:
    return len(text.encode("utf-8"))


def split_markdown(markdown_text: str, max_bytes: int = MAX_MARKDOWN_BYTES) -> list[str]:
    """Split markdown into WeCom-safe chunks.

    WeCom markdown robots reject content above 4096 bytes. Use a lower internal
    limit because Chinese characters and JSON escaping make the margin easy to
    underestimate.
    """
    if encoded_length(markdown_text) <= max_bytes:
        return [markdown_text]

    blocks = [block.strip() for block in markdown_text.split("\n\n") if block.strip()]
    chunks: list[str] = []
    current = ""

    for block in blocks:
        candidate = f"{current}\n\n{block}".strip() if current else block
        if encoded_length(candidate) <= max_bytes:
            current = candidate
            continue

        if current:
            chunks.append(current)
            current = ""

        if encoded_length(block) <= max_bytes:
            current = block
            continue

        lines = block.splitlines()
        for line in lines:
            candidate = f"{current}\n{line}".strip() if current else line
            if encoded_length(candidate) <= max_bytes:
                current = candidate
                continue
            if current:
                chunks.append(current)
            current = trim_to_bytes(line, max_bytes)

    if current:
        chunks.append(current)
    return chunks


def trim_to_bytes(text: str, max_bytes: int) -> str:
    suffix = "\n\n（内容过长，已截断）"
    limit = max_bytes - encoded_length(suffix)
    result = ""
    for char in text:
        if encoded_length(result + char) > limit:
            break
        result += char
    return result + suffix


def add_part_headers(chunks: list[str]) -> list[str]:
    if len(chunks) == 1:
        return chunks
    total = len(chunks)
    return [f"竹鉴晨报（{index}/{total}）\n\n{chunk}" for index, chunk in enumerate(chunks, start=1)]


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


def ensure_wecom_success(response_text: str) -> None:
    try:
        result = json.loads(response_text)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"WeCom returned non-JSON response: {response_text}") from exc

    errcode = result.get("errcode")
    if errcode != 0:
        errmsg = result.get("errmsg", "")
        raise RuntimeError(f"WeCom send failed: errcode={errcode}, errmsg={errmsg}")


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
    chunks = add_part_headers(split_markdown(markdown_text))
    for index, chunk in enumerate(chunks, start=1):
        response_text = send_with_retry(webhook_url, build_payload(chunk))
        ensure_wecom_success(response_text)
        print(f"WeCom send success: part {index}/{len(chunks)}, bytes={encoded_length(chunk)}")
        if index < len(chunks):
            time.sleep(1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
