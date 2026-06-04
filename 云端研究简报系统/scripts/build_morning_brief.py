#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
OUTPUT_DIR = ROOT / "outputs"
REVIEWED_EVENTS_FILE = OUTPUT_DIR / "reviewed_events.json"
REVIEW_DRAFT_INDEX_FILE = OUTPUT_DIR / "review_draft_index.json"
MORNING_BRIEF_FILE = OUTPUT_DIR / "morning_brief.md"


def normalize(text: str) -> str:
    return " ".join((text or "").split()).strip()


def localize_brief_terms(text: str) -> str:
    value = normalize(text)

    def replace_usd_billion(match: re.Match[str]) -> str:
        amount = float(match.group(1).replace(",", ""))
        amount_yi = amount * 10
        rendered = f"{amount_yi:.1f}".rstrip("0").rstrip(".")
        return f"{rendered} 亿美元"

    value = re.sub(r"US\$\s*([0-9][0-9,]*(?:\.[0-9]+)?)\s*billion\b", replace_usd_billion, value, flags=re.I)
    replacements = {
        "Agentic AI": "智能体 AI",
        "agentic AI": "智能体 AI",
        "cost-per-token": "每 token 成本",
        "cost per token": "每 token 成本",
        "Dell AI Factories with NVIDIA": "Dell AI Factory with NVIDIA",
        "Dell AI Factories": "Dell AI Factory",
        "Dell Technologies World": "Dell Technologies World 大会",
        "on-premises": "本地部署",
        "on-prem": "本地部署",
        "frontier models": "前沿模型",
        "autonomous agents": "自主智能体",
        "enterprise perimeter": "企业边界内",
        "Confidential Computing": "机密计算",
        "AI adoption survey": "AI 采用调研",
        "AI infrastructure spending": "AI 基础设施支出",
        "hands-on labs": "实操实验",
        "JAX on NVIDIA GPUs": "NVIDIA GPU 上的 JAX",
        "NVIDIA Dynamo codelab": "Dynamo 推理优化实验",
        "NVIDIA Dynamo on GKE": "GKE 上的 Dynamo",
        "Dynamo on GKE": "GKE 上的 Dynamo",
        "agent workload observability": "智能体工作负载可观测性",
        "Google Agent Development Kit": "Google 智能体开发工具包",
        "G4 VMs with NVIDIA RTX PRO 6000 Blackwell GPUs": "搭载 RTX PRO 6000 Blackwell GPU 的 G4 虚拟机",
        "Google Cloud AI Hypercomputer": "Google Cloud AI 超级计算平台",
        "world foundation models": "世界基础模型",
        "Data Center": "数据中心",
        "networking": "网络业务",
        "hyperscaler capex": "超大云厂商资本开支",
        "agent workflow": "智能体工作流",
        "inference codelab": "推理优化实验",
        "codelab": "实验教程",
        "workloads": "工作负载",
        "hands-on": "实操",
        "inference": "推理",
        "agent": "智能体",
        "capex": "资本开支",
        "purpose-built clouds": "专门构建的云基础设施",
        "accelerated computing": "加速计算",
        "AI software": "AI 软件",
        "fine-tuning": "微调",
        "physical AI": "物理 AI",
        "sovereign AI": "主权 AI",
        "AI labs": "AI 实验室",
        "regional capacity": "区域算力供给",
        "sovereign controls": "主权控制",
        "local compliance": "本地合规",
        "developer access": "开发者接入能力",
        "data proximity": "贴近数据部署",
        "AI factory": "AI 工厂",
        "hyperscaler": "超大云厂商",
        "AI cloud partners": "AI 云合作方",
        "regional cloud partners": "区域云合作方",
        "telecom AI infrastructure": "电信 AI 基础设施",
        "enterprise inference demand": "企业推理需求",
        "token economics": "token 单位经济",
        "energy-efficient": "高能效",
        "attach rate": "配套附加率",
        "Windows AI PC": "Windows AI 电脑",
        "deskside AI supercomputer": "桌边 AI 超算",
        "GitHub Copilot": "GitHub 编码助手",
        "Agent Toolkit": "智能体工具包",
        "managed compute": "托管算力环境",
    }
    for source, target in replacements.items():
        value = value.replace(source, target)
    return value


def render_text_block(text: str) -> str:
    value = localize_brief_terms(text)
    sentences = [item.strip() for item in re.split(r"(?<=[。！？])\s+", value) if item.strip()]
    return "\n\n".join(sentences) if sentences else value


def parse_iso_datetime(value: str) -> datetime | None:
    if not value:
        return None
    value = value.strip()
    try:
        # Most payloads store local time without timezone: 2026-05-12T22:43:26
        parsed = datetime.fromisoformat(value)
        if parsed.tzinfo is None:
            return parsed.replace(tzinfo=ZoneInfo("Asia/Shanghai"))
        return parsed
    except ValueError:
        return None


def current_time() -> datetime:
    override = os.environ.get("MORNING_BRIEF_NOW", "").strip()
    if override:
        parsed = datetime.fromisoformat(override)
        if parsed.tzinfo is None:
            return parsed.replace(tzinfo=ZoneInfo("Asia/Shanghai"))
        return parsed.astimezone(ZoneInfo("Asia/Shanghai"))
    return datetime.now(ZoneInfo("Asia/Shanghai"))


def load_reviewed_events() -> list[dict]:
    if not REVIEWED_EVENTS_FILE.exists():
        return []
    payload = json.loads(REVIEWED_EVENTS_FILE.read_text(encoding="utf-8"))
    items: list[dict] = []
    for company_id, records in (payload.get("companies") or {}).items():
        for event in records:
            reviewed_at = parse_iso_datetime(event.get("reviewed_at", ""))
            items.append({**event, "company_id": company_id, "reviewed_at_dt": reviewed_at})
    return items


def company_name(company_id: str) -> str:
    names = {
        "nvidia": "NVIDIA",
        "tsmc": "TSMC",
        "microsoft": "Microsoft",
        "alibaba": "阿里巴巴",
        "inovance": "汇川技术",
        "luxshare": "立讯精密",
        "gevernova": "GE Vernova",
        "constellation": "Constellation Energy",
        "jcet": "长电科技",
        "naura": "北方华创",
        "amec": "中微公司",
        "innolight": "中际旭创",
    }
    return names.get(company_id, company_id)


def render_item(index: int, item: dict) -> str:
    company = company_name(item.get("company_id", ""))
    title = normalize(item.get("title", ""))
    source_summary = item.get("source_summary") or []
    verification = item.get("verification") or []

    if source_summary:
        source_paragraph = "\n\n".join(render_text_block(line) for line in source_summary if normalize(line))
    else:
        source_paragraph = render_text_block(item.get("fact", ""))
    source_url = normalize(item.get("source_url", ""))
    source_line = f"\n\n[原文]({source_url})" if source_url else ""

    verification_lines = "\n".join(f"- {localize_brief_terms(line)}" for line in verification[:6] if normalize(line))

    business = render_text_block(item.get("business_analysis", ""))
    valuation = render_text_block(item.get("valuation_analysis", ""))
    title = localize_brief_terms(title)

    return f"""## {index}. {company}｜{title}

**原文讲了什么**

{source_paragraph}

**业务影响**

{business}

**估值/动作影响**

{valuation}

**后续观察点**

{verification_lines or '- （无）'}{source_line}
"""
def main() -> None:
    now = current_time()
    # Nightly runs can happen shortly after midnight; in that case the "morning brief"
    # should still be for the same calendar day (this morning), not +1 day.
    brief_date = now if now.hour < 6 else (now + timedelta(days=1))
    today = brief_date.strftime("%Y-%m-%d")
    events = load_reviewed_events()
    # Select: reviewed within the last 24 hours to avoid repeating older items.
    window_start = now - timedelta(hours=24)
    selected = [
        item
        for item in events
        if item.get("reviewed_at_dt") and item["reviewed_at_dt"] >= window_start
    ]
    selected.sort(key=lambda row: (row.get("reviewed_at_dt") or datetime.min), reverse=True)
    selected = selected[:5]

    if selected:
        body = "\n".join(render_item(index, item) for index, item in enumerate(selected, start=1))
    else:
        body = "## 今日暂无符合质量门槛的正式事件\n"
    MORNING_BRIEF_FILE.write_text(
        f"""# 竹鉴晨报 | {today}

{body}
""".rstrip()
        + "\n",
        encoding="utf-8",
    )
    print(f"Morning brief written to: {MORNING_BRIEF_FILE} ({len(selected)} items)")


if __name__ == "__main__":
    main()
