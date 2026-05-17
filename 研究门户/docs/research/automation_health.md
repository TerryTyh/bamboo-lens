# 竹鉴自动化健康检查

生成时间：2026-05-17T20:00:02+08:00

总体状态：健康

## 核心结论

- 工作流文件：4/4 已存在。
- 关键云端产物：12/12 已存在。
- 门户数据文件：10/10 已存在。
- 日报保护状态：healthy。
- 公司页审计状态：healthy。
- 行情覆盖状态：healthy。

## 文件与产物

- GitHub Actions：4/4，healthy
- 云端 outputs：12/12，healthy
- 门户数据文件：10/10，healthy

## 新鲜度

- 阈值：90 小时
- official_candidates：healthy，时间 2026-05-14T15:39:12+08:00，年龄 76.3h
- event_store：healthy，时间 2026-05-16T00:25:04+08:00，年龄 43.6h
- decision_queue：healthy，时间 2026-05-16T00:25:12+08:00，年龄 43.6h
- company_page_overrides：healthy，时间 2026-05-17T12:11:43+08:00，年龄 7.8h
- readability_audit：healthy，时间 2026-05-17T12:12:41+08:00，年龄 7.8h
- mainline_audit：healthy，时间 2026-05-17T12:12:41+08:00，年龄 7.8h
- market_snapshot：healthy，时间 2026-05-15T21:35:01+08:00，年龄 46.4h
- daily_brief：healthy，时间 2026-05-15T00:00:00+08:00，年龄 68.0h
- morning_brief：healthy，时间 2026-05-16T00:00:00+08:00，年龄 44.0h

## 日报发送保护

- 今天是周末，晨报默认非发送日；没有当天标题不视为异常。
- fallback 日报为空，但周末不发送，暂不视为异常。

## 公司页质量审计

- 可读性审计：{"companies": 3, "healthy": 3, "review": 0, "at_risk": 0}
- 主线复核：{"companies": 3, "healthy": 3, "review": 0, "weak": 0}

## 行情与估值动态化

- 覆盖公司：8/8，状态 healthy
