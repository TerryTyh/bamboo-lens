#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


def normalize(text: str) -> str:
    return " ".join((text or "").split()).strip()


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_brief_quality.py <brief.md>")
        return 2

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    body = "\n".join(text.splitlines()[1:]).strip()
    errors: list[str] = []

    if len(normalize(body)) < 160:
        errors.append("brief body is too short")
    if "今日没有新的可读内容" in text or "今天没有新增值得直接推送" in text:
        errors.append("empty/no-news brief should not be sent")
    if "等待夜间智能沉淀" in text or "已抓到原文链接" in text:
        errors.append("process placeholder leaked into brief")
    if "[打开原文](" not in text:
        errors.append("brief lacks clickable source links")
    if "中文摘要" not in text and "今日关键变化" not in text:
        errors.append("brief lacks readable summary sections")

    # Catch long raw English fragments after Chinese summary labels while allowing
    # product names such as NVIDIA, Google Cloud, Vera CPU, CoWoS and URLs.
    suspicious = []
    for line in text.splitlines():
        if not line.strip().startswith("- 原文"):
            continue
        ascii_words = re.findall(r"\b[A-Za-z][A-Za-z'’\-]{3,}\b", line)
        if len(ascii_words) >= 8:
            suspicious.append(line.strip())
    if suspicious:
        errors.append("raw English fragments leaked into Chinese summary")

    if errors:
        print("Brief quality validation failed:")
        for error in errors:
            print(f"- {error}")
        if suspicious:
            print("Suspicious lines:")
            for line in suspicious[:3]:
                print(f"- {line}")
        return 1

    print(f"Brief quality validation passed: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
