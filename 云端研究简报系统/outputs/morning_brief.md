# 竹鉴晨报 | 2026-05-28

## 1. NVIDIA｜Dell AI Factory 扩展：5,000 家企业负载、Vera Rubin NVL72 与 PowerEdge/PowerRack 推动企业 AI 本地部署

**原文讲了什么**

NVIDIA 官方博客记录了 2026-05-18 Dell Technologies World 大会 上 Michael Dell 与 Jensen Huang 对 Dell AI Factory with NVIDIA 的更新。核心信息不是单一产品发布，而是 Dell 把 NVIDIA 的 Vera Rubin、HGX Rubin、Vera CPU、Quantum-X800 InfiniBand、Spectrum-6 Ethernet 和 机密计算 打包成从桌面工作站到数据中心机架的企业 AI 工厂方案。

原文称已有 5,000 家企业在 Dell AI Factory with NVIDIA 上运行 AI 工作负载，举例包括 Lilly、Samsung、Honeywell 和 Hudson River Trading。Dell 同时给出行业口径：到 2030 年全球 AI 基础设施支出可能达到 3-4 万亿美元，token 消耗预计增长 3,400%。

硬件层面，Dell PowerEdge XE9812 基于 NVIDIA Vera Rubin NVL72，面向大规模智能体推理时相对 NVIDIA Blackwell 可实现最高 10 倍更低的每 token 成本；PowerEdge XE9880L、XE9885L 和 XE9882L 是首批基于 NVIDIA HGX Rubin NVL8 的 Dell 系统，支持每机架最高 144 块 GPU、100% 直接液冷计算节点，并宣称相对 HGX B200 最高 10 倍性能。

CPU 与数据平台层面，Dell PowerEdge M9822/R9822 将 NVIDIA Vera CPU 带入企业 AI 工厂。原文称 Vera CPU 具备 1.2 TB/s 内存带宽，智能体工作负载完成速度比 x86 处理器快 50%；Starburst 数据引擎在 NVIDIA Vera CPU 上进行大规模 SQL 分析时查询吞吐最高快 3 倍。

部署形态层面，Dell 引用自家 AI 采用调研 称 67% 的 AI 工作负载运行在云外环境，88% 的受访者至少有一个 AI 工作负载在本地运行。后续还包括 Google Distributed Cloud with Gemini 3.0 preview、NVIDIA Nemotron、Reflection、Hugging Face 上的开放模型、OpenAI Codex 与 Dell AI Data Platform 的连接探索，以及 Palantir、ServiceNow、CrowdStrike、Fortanix 等软件/安全伙伴。

**业务影响**

业务层面，Dell AI Factory 强化的是 NVIDIA 数据中心业务的“企业部署入口”：GPU/CPU/网络/软件栈不再只以云端大集群形式出现，而是通过 Dell PowerEdge、PowerRack、PowerSwitch 和数据平台进入受监管、重安全、重本地数据的企业环境。5,000 家企业工作负载和 67% 云外工作负载口径，支持企业 AI 从试点向部署迁移的方向，但还需要区分真实生产负载、试点负载和营销案例。对 NVIDIA 来说，关键在于 OEM 渠道能否把 Blackwell/Rubin、Vera CPU、InfiniBand/Ethernet 网络和软件栈打包成可复制的企业收入路径。

**估值/动作影响**

估值/动作层面，这条事件支撑 NVIDIA 长期收入空间和数据中心 TAM 的质量假设，尤其是推理成本下降、企业本地部署和 OEM 系统化交付三条线。但它不直接改变近期盈利预测：3-4 万亿美元基础设施支出和 3,400% token 增长属于行业展望，最高 10 倍性能/成本也需要在客户采购、利用率和总拥有成本中验证。动作上维持 A 池核心跟踪，不因单条 Dell 活动上调仓位；后续若财报中 OEM/enterprise AI factory 相关收入、网络业务、Vera/Rubin 交付和软件订阅开始形成可计量增量，再考虑提高权重。

**后续观察点**

- 后续 NVIDIA 财报或 Dell 财报是否披露 AI Factory、PowerEdge AI server、PowerRack 或 enterprise AI pipeline 的订单、收入、backlog 或交付节奏。
- 观察 Blackwell 到 Rubin/Vera 的平台切换是否顺利，尤其是 Vera Rubin NVL72、HGX Rubin NVL8、Vera CPU 和网络产品的上市时间、供给约束与客户导入。
- 验证 5,000 家企业工作负载中生产部署占比、平均采购规模、复购/扩容情况，避免把试点与营销案例等同于可持续收入。
- 检查企业 本地部署 / hybrid AI 需求是否持续超过云端方案，重点看安全、数据主权、延迟、成本和治理要求是否推动真实资本开支。
- 在后续日报和候选池中将 Dell AI Factory 与 Google Cloud、GTC Taipei、Vera CPU 单独公告去重，避免重复把同一条 Rubin/enterprise AI 叙事多次计入。

[原文](https://blogs.nvidia.com/blog/dell-technologies-agent-enterprise-ai/)
