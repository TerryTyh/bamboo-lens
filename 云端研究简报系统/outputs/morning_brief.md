# 竹鉴晨报 | 2026-06-18

## 1. NVIDIA｜Apple 把 Private Cloud Compute 扩到 Google Cloud，NVIDIA 以 Blackwell 机密计算切入高隐私推理底座

**原文讲了什么**

这篇官方文章讲的不是泛泛的安全概念，而是 Apple 已把 Private Cloud Compute 的部分服务端推理能力从自有数据中心扩展到 Google Cloud，并在这一扩容过程中使用带机密计算能力的 NVIDIA Blackwell GPU。文章明确写到，这套架构将用于 Apple Foundation Models 的服务端推理，支撑下一代 Apple Intelligence 功能。

原文还解释了 NVIDIA 机密计算到底在做什么：它通过硬件级可信执行环境把推理工作负载隔离起来，并在敏感数据发送到服务器之前，让系统先完成加密校验，证明底层基础设施没有被篡改。也就是说，这不是单纯“AI 更安全”的口号，而是把隐私保护直接放进推理执行层。

更关键的是合作结构。Apple 的 PCC 扩容落在 Google Cloud 上，底层又采用 NVIDIA Blackwell GPU 与机密计算能力，说明 NVIDIA 不只是给云厂商卖通用训练算力，而是在高隐私、强合规的服务端推理场景里拿到 Apple 与 Google 共同背书的生产级参考案例。

**业务影响**

业务上，这条事件把 NVIDIA 的平台边界从训练与通用推理，进一步延伸到“高隐私推理基础设施”。Apple Private Cloud Compute 的核心约束不是纯算力，而是用户数据在云端推理时能否被隔离、验证和可信执行；NVIDIA 机密计算能进入这层，说明其价值不只在 GPU 吞吐，还在与云平台、模型服务和安全架构协同的生产级能力。对 NVIDIA 来说，这类场景如果持续扩散到消费 AI、企业私有推理和 regulated AI 工作负载，可能提升 Blackwell 在服务端推理市场的黏性，并强化 GPU + 安全执行环境的一体化卖点。

**估值/动作影响**

估值/动作上，这更像高质量的能力强化信号，而不是立刻加仓的财务催化剂。正面在于，Apple + Google 的联合落地让 NVIDIA 机密计算从概念走到真实客户场景，有助于支撑其在推理时代继续维持平台溢价；约束在于，当前没有量化数据，无法判断这会带来多大规模的 GPU 出货、软件附加率或毛利改善。动作上维持核心跟踪，不因单条合作新闻追价；但后续如果更多云平台、企业 AI 或消费端 AI 服务把机密计算列为标准配置，NVIDIA 的推理估值框架应上调对“安全执行层”贡献的权重。

**后续观察点**

- 后续看 Apple、Google 或 NVIDIA 是否披露 PCC 扩容规模、上线区域、GPU 部署量或更多 Apple Intelligence 服务端推理场景。
- 跟踪 NVIDIA 财报或业绩会是否单独提到机密计算、可信推理或高隐私 AI 工作负载的客户采用进展。
- 观察更多云厂商与企业是否把 机密计算 作为 AI 推理标配，而不是 Apple 个案。
- 验证 Blackwell 在推理侧的安全能力，是否能转化为更高的 配套附加率、软件收入或更稳固的推理平台份额。

[原文](https://blogs.nvidia.com/blog/nvidia-confidential-computing-apple-private-cloud-compute/)
