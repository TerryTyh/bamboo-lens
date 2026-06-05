#!/usr/bin/env python3
from __future__ import annotations

import sys
import os
import re
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

TRACKED_COMPANY_NAMES = (
    "NVIDIA",
    "TSMC",
    "Microsoft",
    "阿里巴巴",
    "汇川技术",
    "GE Vernova",
    "立讯精密",
    "Constellation Energy",
    "长电科技",
    "北方华创",
    "中微公司",
    "中际旭创",
    "新易盛",
    "深南电路",
    "沪电股份",
    "工业富联",
)

PROCESS_PATTERNS = (
    "研究池｜候选深读待办",
    "研究池｜A 股扩池优先",
    "今天应看什么",
    "今日研究成果",
    "研究成果｜",
    "今日待读候选",
    "今日没有新的可读内容",
    "已抓到原文链接",
    "尚未抓到可引用",
    "等读完原文",
    "观察卡已完成",
    "强 B 复核：已完成",
    "已完成；下一步",
    "候选池深读",
    "自动化健康",
    "系统层",
)

NVIDIA_HARD_EVENT_TERMS = (
    "财报",
    "业绩",
    "收入",
    "指引",
    "订单",
    "客户",
    "capex",
    "capital expenditure",
    "financial results",
    "earnings",
    "revenue",
    "guidance",
    "contract",
)


def today_cn() -> str:
    override = os.environ.get("BRIEF_TODAY", "").strip()
    if override:
        return override
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
    return ("## " in body or "**原文讲了什么**" in body) and is_external_company_brief(text)


def section_headings(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip().startswith("## ")]


def brief_main_body(text: str) -> str:
    return text.split("明日重点", 1)[0]


def company_names_in_main_body(text: str) -> set[str]:
    body = brief_main_body(text)
    return {name for name in TRACKED_COMPANY_NAMES if name in body}


def is_nvidia_only_soft_brief(text: str) -> bool:
    headings = section_headings(text)
    if headings and all(re.match(r"##\s+\d+\.\s+NVIDIA｜", heading) for heading in headings):
        signal_text = " ".join(headings).lower()
        return not any(term.lower() in signal_text for term in NVIDIA_HARD_EVENT_TERMS)
    names = company_names_in_main_body(text)
    if names != {"NVIDIA"}:
        return False
    signal_text = " ".join(headings) if headings else brief_main_body(text)
    signal_text = signal_text.lower()
    return not any(term.lower() in signal_text for term in NVIDIA_HARD_EVENT_TERMS)


def is_external_company_brief(text: str) -> bool:
    if any(pattern in text for pattern in PROCESS_PATTERNS):
        return False
    if "[原文](" not in text and "[打开原文](" not in text:
        return False
    if not any(name in text for name in TRACKED_COMPANY_NAMES):
        return False
    if is_nvidia_only_soft_brief(text):
        return False
    return True


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
            "Same-day morning_brief.md exists but does not pass external-company gates; "
            "falling back to daily_brief.md.",
        )

    if daily and has_same_day_header(daily, today) and not is_empty_daily(daily) and is_external_company_brief(daily):
        write_choice("non-empty daily_brief.md", daily)
        return 0

    if daily and not has_same_day_header(daily, today):
        print("daily_brief.md exists but is not same-day.")

    if daily and has_same_day_header(daily, today) and not is_empty_daily(daily):
        print("Non-empty daily_brief.md exists but does not pass external-company gates.")

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
