#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


def normalize(text: str) -> str:
    return " ".join((text or "").split()).strip()


ALLOWED_ASCII_WORDS = {
    "a5x",
    "adk",
    "ai",
    "anthropic",
    "asic",
    "asus",
    "attach",
    "azure",
    "blackwell",
    "cassava",
    "claro",
    "claude",
    "cloud",
    "coherent",
    "colab",
    "computex",
    "content",
    "copilot",
    "cosmos",
    "crowdstrike",
    "codex",
    "cudf",
    "cuvs",
    "data",
    "dataproc",
    "deepseek",
    "dell",
    "deskside",
    "desktop",
    "dynamo",
    "efficient",
    "enterprise",
    "eps",
    "ethernet",
    "fabric",
    "fortanix",
    "foundry",
    "gaap",
    "gb10",
    "gb200",
    "gb300",
    "gemini",
    "gemma",
    "gke",
    "glm",
    "google",
    "gpu",
    "gpus",
    "gtc",
    "github",
    "hgx",
    "honeywell",
    "hypercomputer",
    "hyperscaler",
    "hudson",
    "hugging",
    "infiniband",
    "jax",
    "kimi",
    "labs",
    "lilly",
    "mistral",
    "minimax",
    "maxtext",
    "microsoft",
    "moe",
    "msi",
    "nemotron",
    "nemoclaw",
    "next",
    "non-gaap",
    "nvidia",
    "nvfp4",
    "nvlink",
    "nvl8",
    "nvl72",
    "openai",
    "openshell",
    "palantir",
    "partners",
    "petaflop",
    "planetary",
    "poweredge",
    "powerrack",
    "powerswitch",
    "pro",
    "quantum-x800",
    "rag",
    "rate",
    "red",
    "reflection",
    "rtx",
    "run",
    "rubin",
    "safety",
    "samsung",
    "salesforce",
    "schrodinger",
    "secure",
    "servicenow",
    "snap",
    "spacexai",
    "spectrum-6",
    "spectrum-x",
    "starburst",
    "synthid",
    "surface",
    "superchip",
    "supercomputer",
    "thinking",
    "token",
    "toolkit",
    "tpu",
    "trading",
    "ultra",
    "unified",
    "vera",
    "vms",
    "windows",
    "xe9685l",
    "xe9780",
    "xe9812",
    "xe9880l",
    "xe9882l",
    "xe9885l",
    "x86",
}


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
    if "[原文](" not in text and "[打开原文](" not in text:
        errors.append("brief lacks clickable source links")
    if "｜" not in text and "今日关键变化" not in text:
        errors.append("brief lacks readable summary sections")

    # Catch long raw English fragments after Chinese summary labels while allowing
    # product names such as NVIDIA, Google Cloud, Vera CPU, CoWoS and URLs.
    suspicious = []
    for line in text.splitlines():
        if not line.strip():
            continue
        if "[原文](" in line:
            continue
        if not any(marker in line for marker in ("NVIDIA", "TSMC", "Google", "Vera", "Rubin", "AI", "Cloud", "CPU", "GPU", "GTC", "COMPUTEX")):
            continue
        if re.match(r"\s*\d+\.\s+", line):
            continue
        if "http" in line:
            continue
        ascii_words = [
            word
            for word in re.findall(r"\b[A-Za-z][A-Za-z'’\-]{3,}\b", line)
            if word.lower().replace("’", "'") not in ALLOWED_ASCII_WORDS
        ]
        if len(ascii_words) >= 10:
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
