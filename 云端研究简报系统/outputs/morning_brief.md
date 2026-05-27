# 竹鉴晨报 | 2026-05-27

## 1. NVIDIA｜Google Cloud 开发者生态扩展：10 万+开发者、JAX/Dynamo/Nemotron/Blackwell 进入云端 AI 构建链条

**原文讲了什么**

NVIDIA 官方博客披露，在 Google I/O 期间，NVIDIA 与 Google Cloud 的联合开发者社区已经超过 100,000 名开发者。该社区提供学习路径、实操实验 和活动，帮助开发者在 Google Cloud 上使用 NVIDIA 全栈 AI 平台。

今年新增内容包括 NVIDIA GPU 上的 JAX 学习路径、面向推理优化的 Dynamo 推理优化实验，以及月度开发者直播；文章还提到过去一年社区已经支持 GKE 上的生产级 RAG 应用、智能体工作负载可观测性、混合本地/云推理原型等用例。

开发工具链层面，文章列举了 cuDF、Google Colab Enterprise、Dataproc、Gemma 4、NVIDIA Nemotron、Google 智能体开发工具包、Cloud Run、搭载 RTX PRO 6000 Blackwell GPU 的 G4 虚拟机 等组合路径。

训练与推理基础设施层面，NVIDIA 与 Google Cloud 把 JAX 优化延伸到 Google Cloud AI 超级计算平台 和 MaxText；GKE 上的 Dynamo 用于大规模推理和 MoE 模型服务效率优化。

可信 AI 与物理 AI 层面，文章补充 SynthID 与 NVIDIA Cosmos 世界基础模型 的合作，并把本篇开发者生态与 Google Cloud Next 的 A5X / Vera Rubin、Gemini、OpenAI、Thinking Machine Labs、Schrodinger、Salesforce、Snap、CrowdStrike 等平台合作线索连接起来。

**业务影响**

业务层面，它影响的是 NVIDIA 数据中心 的平台粘性和云端分发质量。Google Cloud 是 NVIDIA 的客户，也是企业开发者接触 NVIDIA 软件、模型和推理框架的渠道；如果开发者通过 JAX、Dynamo、Nemotron、cuDF、Cloud Run、GKE、G4 Blackwell VM 和 AI Hypercomputer 构建应用，NVIDIA 的价值会从一次性 GPU 采购延伸到训练、推理、模型服务、智能体工作流 和物理 AI 应用开发标准。它也让 NVIDIA 与 hyperscaler 的关系更复杂：云厂商既会自研芯片，也会把 NVIDIA 平台能力包装成客户可用的云服务。

**估值/动作影响**

估值/动作上，这条事件支持 NVIDIA 的平台溢价，但不单独改变合理价值区间或仓位动作。正面是 100,000+ 开发者社区、Dynamo/GKE 推理优化、Nemotron/Gemma/ADK 智能体 工具链和 Cosmos/SynthID 可信物理 AI 线索，增强了“推理和 智能体 应用接棒训练需求”的可信度；限制是文章没有披露付费工作负载规模、GPU 消耗、收入贡献、毛利率或客户转化率。动作上维持 A 池核心，把它作为 Google Cloud 渠道采用和开发者生态扩散的辅助证据，不因这条新闻单独加仓。

**后续观察点**

- 跟踪 Google Cloud 是否扩大 A5X / Vera Rubin、Blackwell GPU、G4 VMs、GKE 上的 Dynamo 和 JAX / AI Hypercomputer 的可用区域、客户案例或商业化指标。
- 观察 Dynamo、Nemotron、Cosmos、cuDF、RTX PRO 6000 Blackwell GPU 是否在更多企业 智能体、RAG、数据科学或物理 AI 部署案例中出现，而不只是学习路径和 实验教程。
- 在后续 NVIDIA 财报中继续看 数据中心、网络业务、推理需求、软件/云服务采用和 超大云厂商资本开支 口径，确认开发者生态能否转化为实际计算需求。
- 跟踪 Google 自研 TPU / ASIC 与多供应商策略是否限制 NVIDIA 在 Google Cloud 工作负载中的议价能力和长期份额。

[原文](https://blogs.nvidia.com/blog/google-cloud-developer-community-ai-builders/)

## 2. NVIDIA｜FY2027 Q1：收入 US$81.6b、数据中心 US$75.2b，Q2 指引 US$91.0b，AI 工厂平台逻辑继续强化

**原文讲了什么**

NVIDIA 公布截至 2026-04-26 的 FY2027 Q1 财报。总收入 816.1 亿美元，环比增长 20%，同比增长 85%；数据中心收入 752 亿美元，环比增长 21%，同比增长 92%。

盈利质量继续维持高位：GAAP / non-GAAP 毛利率分别为 74.9% / 75.0%；GAAP 稀释 EPS 为 US$2.39，non-GAAP 稀释 EPS 为 US$1.87；自由现金流 485.5 亿美元。

公司给出 FY2027 Q2 收入指引 910 亿美元，上下浮动 2%，且不假设来自中国的数据中心计算收入。公司还新增 800 亿美元 股票回购授权，并将季度分红从 US$0.01 提高到 US$0.25。

**业务影响**

这次财报把 NVIDIA 的主线进一步推向 AI 工厂平台公司。数据中心已经贡献约九成收入，且内部网络业务增速显著高于计算业务，说明客户采购不只是单点加速卡，而是在购买训练、推理、网络、存储、系统和软件协同能力。报告框架调整为数据中心与边缘计算，也说明公司希望用更贴近 AI 工厂、智能体 AI 和物理 AI 的方式呈现未来增长驱动。

**估值/动作影响**

估值上，这条事件支持上调 NVIDIA 的基本面确信度和平台化权重，但不直接触发追价。910 亿美元 的 Q2 指引、75% 左右毛利率和 485.5 亿美元 自由现金流，支撑高估值的质量更强；但当前市场已经对 AI 基础设施给出高预期，后续动作仍要看 Q2 是否继续兑现、网络收入是否持续放大、库存/应收是否健康、客户资本开支是否维持。动作上维持 A 池核心，并把下一次 Q2 财报、网络收入和中国以外需求强度列为最高优先级验证点。

**后续观察点**

- FY2027 Q2 收入是否接近或超过 910 亿美元 指引。
- 数据中心网络收入是否继续高增长，验证 Spectrum-X / NVLink / AI 工厂系统协同是否转化为收入。
- 毛利率能否继续维持约 75%，平台化扩张是否侵蚀盈利质量。
- 应收账款、库存和自由现金流是否保持健康，避免高增长背后出现营运资本过热。
- 管理层后续是否给出更清晰的超大客户 / AI 云端与企业客户分拆口径。

[原文](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/default.aspx)
