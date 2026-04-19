#!/usr/bin/env python3
from __future__ import annotations

import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_FILE = ROOT.parent / ".github" / "workflows" / "daily-brief.yml"
COMPANIES_FILE = ROOT / "config" / "companies.json"
ENV_EXAMPLE = ROOT / ".env.example"


def check_file(path: Path) -> tuple[bool, str]:
    return path.exists(), str(path)


def main() -> int:
    checks = {
        "workflow": check_file(WORKFLOW_FILE),
        "companies": check_file(COMPANIES_FILE),
        "env_example": check_file(ENV_EXAMPLE),
        "wecom_webhook": (bool(os.environ.get("WECOM_WEBHOOK_URL", "").strip()), "env:WECOM_WEBHOOK_URL"),
    }

    print("竹鉴云端配置自检")
    print("=" * 24)
    failed = False
    for name, (ok, target) in checks.items():
        status = "OK " if ok else "MISS"
        print(f"[{status}] {name:<14} {target}")
        if not ok:
            failed = True

    print("\n说明：")
    print("- workflow / companies / env_example 缺失，说明仓库骨架还没准备完整。")
    print("- wecom_webhook 缺失，只会影响真正发到企业微信，不影响先生成日报文件。")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

