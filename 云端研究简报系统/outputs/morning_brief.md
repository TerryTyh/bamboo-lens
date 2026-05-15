# 竹鉴晨报 | 2026-05-16

## 1. NVIDIA｜NVIDIA, Ineffable Intelligence Team Up to Build the Future of Reinforcement Learning Infrastructure

**原文讲了什么**

原文宣布 NVIDIA 与 Ineffable Intelligence（由 AlphaGo 架构师 David Silver 创立的 AI 实验室）开展工程层面的合作，目标是共同设计可在大规模上支撑强化学习（RL）的训练流水线与基础设施。 文章强调 RL 与预训练在系统层面的差异：RL 数据在线生成且需要在紧密循环中持续“行动-观察-评分-更新”，因此对互联、内存带宽与 serving 链路提出不同压力。 文中称合作工作从 NVIDIA Grace Blackwell 平台起步，并将成为较早探索未来 NVIDIA Vera Rubin 平台的项目之一，意在把下一代训练范式与其新平台提前绑定。

**业务影响**

从业务上看，RL/后训练工作负载若走向规模化，会把算力需求从“单次大训练”扩展到“持续生成数据与训练更新”的闭环，对 GPU、互联与系统软件的要求更系统化。NVIDIA 通过与前沿实验室共设基础设施，有助于在平台迭代时把新负载的关键瓶颈（互联、带宽、服务链路）纳入产品路线，从而巩固其系统级平台地位。

**估值/动作影响**

估值/动作层面，该类合作更像“未来需求曲线”的证据点：若 RL/后训练成为主流，将延长高端算力与系统平台的景气周期，支持估值中枢维持；但在缺少可验证客户采用与预算分配前，不应据此上调短期盈利假设。当前动作以维持跟踪为主，等待后续平台发布/客户案例/产品化披露来验证方向是否从研究走向规模化部署。

**后续观察点**

- 关注 NVIDIA 后续在产品/平台发布中对 RL/后训练基础设施的明确支持（软件栈、互联/带宽优化、参考架构）。
- 观察是否出现可核验的客户采用：Ineffable 或类似团队在公开材料中披露使用规模、集群形态或性能指标。
- 跟踪 Vera Rubin 平台相关披露中，是否把 RL/模拟训练作为关键用例之一，而不仅是单一的预训练/推理叙事。

来源：[NVIDIA 原文](https://blogs.nvidia.com/blog/ineffable-intelligence-reinforcement-learning-infrastructure/)

## 2. NVIDIA｜Hermes Unlocks Self-Improving AI Agents, Powered by NVIDIA RTX PCs and DGX Spark

**原文讲了什么**

原文以 Nous Research 开源的 Hermes Agent 为例，描述 agentic AI 正从“演示工具”走向可持续运行的工作方式：Hermes 被描述为更可靠、可自我改进，且可在本地 24/7 运行并集成消息应用、访问本地文件/应用。 文章把 Qwen 3.6 27B/35B 等开源权重模型与 Hermes 组合为“本地 agent 套件”，并强调硬件会直接决定体验，因此把 NVIDIA RTX PC/RTX PRO 与 DGX Spark 作为该类工作负载的推荐运行平台。 文中还用具体参数说明其硬件叙事（例如 35B 约 20GB 内存运行、DGX Spark 128GB unified memory/1 petaflop AI performance），意在把“本地 agent”绑定到 NVIDIA 端侧与小型机生态。

**业务影响**

对 NVIDIA 来说，核心影响在端侧与小型机生态而非数据中心训练：一是 RTX PC/RTX PRO 工作站可被定义为“全天候本地 agent 机器”，潜在带动高端 GPU 与整机升级；二是 DGX Spark 等小型机把 agent 负载从云端外溢到企业/开发者本地，增加软件栈与硬件耦合。整体属于“新增使用场景 + 生态绑定”的布局，需观察是否从叙事走向规模交付。

**估值/动作影响**

估值/动作层面，这类生态文章本身不会立刻改变盈利预测，但会影响市场对“端侧 AI + agent 工作流”可持续性的想象空间：若后续出现可验证的采用数据（出货、活跃、企业部署案例），可能抬升对 RTX 相关增长与毛利结构的信心；反之若仅停留在宣传与社区热度，则对估值贡献有限。当前动作以维持跟踪为主，不据此单独加仓。

**后续观察点**

- 跟踪后续是否出现可核验的采用证据：Hermes/类似本地 agent 在企业/开发者侧的部署案例、活跃度或官方生态数据披露。
- 观察 RTX AI PC 与工作站出货/ASP/渠道反馈是否出现“agent 本地运行”驱动的结构性变化。
- 若 DGX Spark 被持续提及，关注其目标客户、交付节奏与是否形成可复用的软件/运行时绑定（而不是一次性硬件宣传）。

来源：[NVIDIA 原文](https://blogs.nvidia.com/blog/rtx-ai-garage-hermes-agent-dgx-spark/)
