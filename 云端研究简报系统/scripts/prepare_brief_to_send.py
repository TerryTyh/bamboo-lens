#!/usr/bin/env python3
from __future__ import annotations

import sys
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs"
MORNING_BRIEF = OUTPUT_DIR / "morning_brief.md"
DAILY_BRIEF = OUTPUT_DIR / "daily_brief.md"
BRIEF_TO_SEND = OUTPUT_DIR / "brief_to_send.md"


EMPTY_DAILY_MARKERS = (
    "今日没有新的可读内容",
    "今天没有新增值得直接推送的已判断研究事件",
)


def today_cn() -> str:
    return datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d")


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def has_same_day_header(text: str, today: str) -> bool:
    return today in "\n".join(text.splitlines()[:8])


def is_empty_daily(text: str) -> bool:
    return any(marker in text for marker in EMPTY_DAILY_MARKERS)


def is_meaningful_morning(text: str) -> bool:
    """Avoid sending a same-day morning brief that only contains the title."""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if len(lines) <= 1:
        return False
    body = "\n".join(lines[1:]).strip()
    if len(body) < 80:
        return False
    return "## " in body or "**原文讲了什么**" in body


def set_send_output(value: bool) -> None:
    output_file = os.environ.get("GITHUB_OUTPUT", "").strip()
    if output_file:
        with open(output_file, "a", encoding="utf-8") as handle:
            handle.write(f"send={'true' if value else 'false'}\n")


def write_choice(source: str, text: str) -> None:
    BRIEF_TO_SEND.write_text(text, encoding="utf-8")
    set_send_output(True)
    print(f"Brief selected: {source}")
    print("--- brief preview ---")
    print("\n".join(text.splitlines()[:24]))


def skip_send(message: str) -> int:
    set_send_output(False)
    BRIEF_TO_SEND.write_text(
        f"# 竹鉴晨报跳过发送\n\n{message}\n",
        encoding="utf-8",
    )
    print(f"Brief send skipped: {message}")
    return 0


def main() -> int:
    today = today_cn()
    morning = read_text(MORNING_BRIEF)
    daily = read_text(DAILY_BRIEF)

    if morning and has_same_day_header(morning, today) and is_meaningful_morning(morning):
        write_choice("same-day morning_brief.md", morning)
        return 0

    if morning and has_same_day_header(morning, today):
        print(
            "Same-day morning_brief.md exists but has no meaningful body; "
            "falling back to daily_brief.md.",
        )

    if daily and not is_empty_daily(daily):
        write_choice("non-empty daily_brief.md", daily)
        return 0

    if morning and not has_same_day_header(morning, today):
        return skip_send(
            "晨报文件存在但不是当天版本，同时 fallback 日报为空。"
            "为避免误发'没有新消息'或旧内容，今天不向企业微信发送。"
        )

    if daily and os.environ.get("ALLOW_EMPTY_BRIEF", "").strip().lower() == "true":
        write_choice("empty daily_brief.md", daily)
        return 0

    if daily and is_empty_daily(daily):
        return skip_send(
            "fallback 日报为空。为避免继续推送低价值'无新消息'日报，已阻断发送；"
            "请先生成当天高质量 morning_brief.md，或显式设置 ALLOW_EMPTY_BRIEF=true。"
        )

    return skip_send("没有找到可发送的日报文件：daily_brief.md / morning_brief.md 均不可用。")


if __name__ == "__main__":
    raise SystemExit(main())
