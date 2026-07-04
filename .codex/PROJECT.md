# 竹鉴项目索引

## 固定位置

- 项目目录：`/Users/tianyuehua/Documents/项目/竹鉴`
- Codex 全局入口：`/Users/tianyuehua/.codex/projects/竹鉴`
- GitHub：`TerryTyh/bamboo-lens`

## 接手顺序

1. `README.md`：模块和目录导航。
2. `AGENTS.md`：协作规则和质量门槛。
3. `研究门户/docs/research/竹鉴推进状态与下一步.md`：长期进度锚点。
4. `研究门户/docs/research/` 中日期最新的周总结：当前计划。
5. `研究门户/docs/briefs/daily_brief.md`：最近日报产物。
6. `研究门户/docs/research/automation_health.md`：自动化健康状态。

## 数据主线

```text
公司官方来源
  -> official_candidates.json
  -> review_drafts/
  -> reviewed_events.json
  -> event_store.json
  -> 研究门户/event-store-data.js
  -> 首页最近更新 / 公司页 / 日报
```

候选只是待读线索。只有通过原文、证据、业务影响、估值影响和验证点检查后，才可进入正式事件。

## 常见任务入口

- 首页与公司页：`研究门户/index.html`、`index.js`、`company.js`
- 正式事件：`云端研究简报系统/outputs/review_drafts/`
- 候选采集配置：`云端研究简报系统/config/companies.json`
- 日报质量：`云端研究简报系统/scripts/generate_daily_brief.py`
- 研究池：`研究门户/research-pool-data.js`
- 产品需求：`docs/产品设计/`
- 原始财报：`资料/公司财报/`

## 当前结构原则

- 根目录不新增零散文档。
- 新公司研究进入 `研究门户/docs/research/`，稳定方法论进入 `长期高潜力公司跟踪系统/`。
- 自动化运行产物由脚本维护，手工修改前先确认是否会被下一轮生成覆盖。
- 个人资产资料进入 `资料/资产快照/`，不得作为公开门户内容。
