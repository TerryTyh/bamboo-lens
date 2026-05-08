# 竹鉴晨报 | 2026-05-08

今日值得读的内容：

1. NVIDIA｜Spectrum-X Ethernet 与 MRC

这篇文章的核心是：NVIDIA 正在把 Spectrum-X 定位成面向超大规模 AI 工厂的“AI 原生以太网”，而 MRC（Multipath Reliable Connection）是其中一个关键协议能力。

MRC 可以让一个 RDMA 连接把数据流量分散到多条网络路径上，而不是依赖单一路径。这样在大规模 AI 训练集群里，网络可以更好地做负载均衡、绕开拥堵路径，并在路径故障时更快恢复，目标是减少 GPU 等待和训练任务中断。

原文提到，OpenAI、Microsoft、Oracle 等 AI 工厂或云基础设施场景正在依赖这类能力。OpenAI 的表述尤其关键：MRC 在 Blackwell 代际部署中有助于减少网络相关 slowdown 和 interruption，维持 frontier training runs 的效率。

对 NVIDIA 的业务理解：这不是一条普通网络产品新闻，而是在强化“NVIDIA 不只是卖 GPU，而是在定义 AI 工厂系统架构”的逻辑。AI 训练规模越大，网络、交换机、SuperNIC、协议和遥测控制就越可能成为 GPU 利用率和训练成本的关键变量。

来源：[NVIDIA Blog｜Spectrum-X Ethernet 与 MRC](https://blogs.nvidia.com/blog/spectrum-x-ethernet-mrc/)

2. NVIDIA｜与 ServiceNow 推进企业自主智能体

这篇文章讲的是 NVIDIA 和 ServiceNow 扩大合作，把企业 AI 从“生成/推理”推进到“能在企业工作流里执行动作”的自主智能体阶段。

ServiceNow 推出 Project Arc，这是一个面向知识工作者的长期运行桌面智能体，可以接入本地文件系统、终端和应用，完成传统自动化难以处理的多步骤任务。同时它不是裸奔的 AI agent，而是接入 ServiceNow Action Fabric、AI Control Tower 和 NVIDIA OpenShell，用来处理治理、审计、安全和执行边界。

NVIDIA 在这里提供的是加速计算、开放模型、domain-specific skills、OpenShell 安全运行时，以及支撑高效 tokenomics 的 AI factories。换句话说，NVIDIA 试图把自己嵌入企业智能体从模型、运行时、安全沙箱到算力基础设施的完整链条里。

对 NVIDIA 的业务理解：这条线索强化了“AI 工厂不仅服务大模型训练，也服务企业级推理和长期运行智能体”的方向。如果企业智能体真的规模化，推理 token 需求、企业安全运行时和专用基础设施会成为新的需求来源。

来源：[NVIDIA Blog｜ServiceNow 自主智能体合作](https://blogs.nvidia.com/blog/servicenow-autonomous-ai-agents-enterprises/)

今日跟踪重点：

- NVIDIA：继续观察 Spectrum-X、MRC、SuperNIC、AI Ethernet 是否能从“技术叙事”转成可持续收入和生态控制力。
- NVIDIA：继续观察企业自主智能体是否带来真实推理需求，而不是停留在合作发布层面。
- Constellation Energy：等待 Q1 2026 earnings call 材料发布后，再看电价、核电可售电量、Calpine 整合和资本配置。
