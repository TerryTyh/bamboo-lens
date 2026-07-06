# 竹鉴自动化健康检查

生成时间：2026-07-06T22:36:36+08:00

总体状态：需观察

## 核心结论

- 工作流文件：4/4 已存在。
- 关键云端产物：12/12 已存在。
- 门户数据文件：10/10 已存在。
- 日报保护状态：watch。
- 公司页审计状态：healthy。
- 行情覆盖状态：healthy。

## 文件与产物

- GitHub Actions：4/4，healthy
- 云端 outputs：12/12，healthy
- 门户数据文件：10/10，healthy

## 新鲜度

- 阈值：42 小时
- official_candidates：watch，时间 2026-07-03T13:45:25+08:00，年龄 80.9h
- event_store：healthy，时间 2026-07-06T22:36:36+08:00，年龄 0.0h
- decision_queue：healthy，时间 2026-07-06T22:36:36+08:00，年龄 0.0h
- company_page_overrides：healthy，时间 2026-07-06T22:36:36+08:00，年龄 0.0h
- readability_audit：healthy，时间 2026-07-06T22:36:36+08:00，年龄 0.0h
- mainline_audit：healthy，时间 2026-07-06T22:36:36+08:00，年龄 0.0h
- market_snapshot：watch，时间 2026-07-03T21:46:46+08:00，年龄 72.8h
- daily_brief：watch，时间 2026-07-03T00:00:00+08:00，年龄 94.6h
- morning_brief：watch，时间 2026-07-04T00:00:00+08:00，年龄 70.6h

## 日报发送保护

- morning_brief.md 和 daily_brief.md 都不是当天标题；工作日早晨需复核。
- fallback 日报为空且没有当天晨报，prepare_brief_to_send.py 会阻断发送。

## 公司页质量审计

- 可读性审计：{"companies": 4, "healthy": 4, "review": 0, "at_risk": 0}
- 主线复核：{"companies": 4, "healthy": 4, "review": 0, "weak": 0}

## 行情与估值动态化

- 覆盖公司：16/16，状态 healthy
