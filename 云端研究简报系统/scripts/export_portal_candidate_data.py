#!/usr/bin/env python3
from __future__ import annotations

import json
import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
INPUT_FILE = ROOT / "outputs" / "official_candidates.json"
OUTPUT_FILE = PROJECT_ROOT / "研究门户" / "candidate-data.js"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export official candidates for the research portal.")
    parser.add_argument(
        "--input",
        type=Path,
        default=INPUT_FILE,
        help="Path to official_candidates.json. Defaults to the local outputs file.",
    )
    return parser.parse_args()


def load_candidates(input_file: Path) -> dict:
    if not input_file.exists():
        return {"generated_at": "", "companies": {}}
    return json.loads(input_file.read_text(encoding="utf-8"))


def main() -> None:
    args = parse_args()
    payload = load_candidates(args.input)
    OUTPUT_FILE.write_text(
        "window.BAMBOO_LENS_CANDIDATES = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    print(f"Portal candidate data written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
