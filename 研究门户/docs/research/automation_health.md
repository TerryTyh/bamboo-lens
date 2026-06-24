# 竹鉴自动化健康检查

生成时间：2026-06-24T22:12:45+08:00

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
- official_candidates：healthy，时间 2026-06-24T14:08:50+08:00，年龄 8.1h
- event_store：healthy，时间 2026-06-24T14:12:37+08:00，年龄 8.0h
- decision_queue：healthy，时间 2026-06-24T14:12:37+08:00，年龄 8.0h
- company_page_overrides：healthy，时间 2026-06-24T14:12:38+08:00，年龄 8.0h
- readability_audit：healthy，时间 2026-06-24T14:12:38+08:00，年龄 8.0h
- mainline_audit：healthy，时间 2026-06-24T14:12:38+08:00，年龄 8.0h
- market_snapshot：healthy，时间 2026-06-24T22:12:45+08:00，年龄 0.0h
- daily_brief：healthy，时间 2026-06-24T00:00:00+08:00，年龄 22.2h
- morning_brief：healthy，时间 2026-06-25T00:00:00+08:00，年龄 0.0h

## 日报发送保护

- fallback 日报为空且没有当天晨报，prepare_brief_to_send.py 会阻断发送。

## 公司页质量审计

- 可读性审计：{"companies": 3, "healthy": 3, "review": 0, "at_risk": 0}
- 主线复核：{"companies": 3, "healthy": 3, "review": 0, "weak": 0}

## 行情与估值动态化

- 覆盖公司：16/16，状态 healthy
