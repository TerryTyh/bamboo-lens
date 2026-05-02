#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
INPUT_FILE = ROOT / "outputs" / "event_store.json"
OUTPUT_FILE = PROJECT_ROOT / "研究门户" / "event-store-data.js"


def main() -> None:
    if INPUT_FILE.exists():
        payload = json.loads(INPUT_FILE.read_text(encoding="utf-8"))
    else:
        payload = {"generated_at": "", "companies": {}}

    OUTPUT_FILE.write_text(
        "window.BAMBOO_LENS_EVENT_STORE = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    print(f"Portal event store data written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
