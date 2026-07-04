#!/bin/zsh
set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
PORTAL_URL="http://127.0.0.1:8765/研究门户/index.html#portfolioOverview"

cd "$PROJECT_DIR"

echo "== 竹鉴 / Bamboo Lens =="
echo "1. 正在同步 GitHub 最新研究数据..."
git pull --ff-only

echo ""
echo "2. 正在生成本周同步摘要..."
python3 云端研究简报系统/scripts/build_event_store.py
python3 云端研究简报系统/scripts/export_portal_event_store_data.py
python3 云端研究简报系统/scripts/build_company_state.py
python3 云端研究简报系统/scripts/build_decision_queue.py
python3 云端研究简报系统/scripts/build_weekend_sync_summary.py
echo "   摘要位置：$PROJECT_DIR/云端研究简报系统/outputs/weekend_sync_summary.md"

echo ""
echo "3. 正在启动本地研究门户..."
if lsof -i :8765 >/dev/null 2>&1; then
  echo "   端口 8765 已有服务运行，直接打开门户。"
else
  (python3 -m http.server 8765 >/tmp/bamboo-lens-portal.log 2>&1 &)
  sleep 1
fi

echo ""
echo "4. 打开门户首页组合看板。"
open "$PORTAL_URL"

echo ""
echo "同步完成。建议先看："
echo "- 组合看板：当前价格、买卖价、最新动态和公司入口"
echo "- 最近更新：已完成研判的公司正式事件"
echo "- 官方候选池：本周待研判线索"
echo "- 周末同步摘要：云端研究简报系统/outputs/weekend_sync_summary.md"
