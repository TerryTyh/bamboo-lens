# 竹鉴晨报 | 2026-06-13

## 1. NVIDIA｜Apple 把 Private Cloud Compute 扩到 Google Cloud，NVIDIA Blackwell 开始切入隐私推理底座

**原文讲了什么**

这篇原文讲的不是泛泛而谈的“AI 安全”概念，而是 Apple 已把 Private Cloud Compute（PCC）中的部分机密推理工作负载扩展到 Google Cloud，并在这条链路里使用带有 机密计算 的 NVIDIA GPU。也就是说，NVIDIA 不只是继续卖训练卡，而是在 Apple Intelligence 的云端推理安全架构里占到一个明确位置。

原文进一步说明，这套部署面向 Apple Foundation Models 的 server-side 推理，由 Apple 与 Google 基于 Gemini 技术栈共同构建，运行在集成进 PCC 硬件安全架构的 NVIDIA Blackwell GPU 上。文章把“Apple + Google Cloud + NVIDIA Blackwell + PCC”放进同一个架构叙事里，核心增量是高隐私要求的消费级 AI 功能开始依赖云端机密推理能力，而不是只停留在端侧模型。

安全机制部分，NVIDIA 把 机密计算 定义为 AI 工作负载的硬件级隔离层：通过 trusted execution environments 隔离处理中的数据，并在敏感数据发送前进行加密校验，验证基础设施未被篡改。对终端用户的含义是，连系统建设方本身也不应看到聊天、对话或个人数据内容。

这条材料没有披露 GPU 数量、合同金额或推理 token 规模，因此不能把它直接写成短期收入催化。但它明确展示了一条新场景：当大模型功能进入高隐私、高合规要求的云端推理阶段，NVIDIA 试图把 Blackwell、机密计算和云厂商部署能力一起打包成基础设施标准。

**业务影响**

业务层面，这条进展强化了三件事。第一，NVIDIA 开始切入高隐私要求的消费级云端推理入口，说明 Apple Intelligence 这类面向海量终端用户的功能，未来可能不只依赖端侧芯片，还需要可信的云端推理底座。第二，合作链条把 Apple、Google Cloud 和 NVIDIA 连在一起，意味着 NVIDIA 既可能受益于云厂商基础设施采购，也可能受益于更多面向终端产品的 server-side 推理 扩容。第三，机密计算把 NVIDIA 的平台边界从算力与网络继续推到安全执行层；如果这套能力被更多云厂商和企业 AI 工作负载复用，Blackwell 的 配套附加率 和平台黏性都有机会提升。

**估值/动作影响**

估值和动作上，这条事件支持继续给 NVIDIA 平台溢价，但力度应低于财报、数据中心收入或大额 AI 工厂订单。正面在于：Apple 的 PCC 场景对隐私和安全要求很高，NVIDIA 能进入这类部署，说明其在可信推理基础设施上的能力得到头部客户认可；同时 Google Cloud 的加入，让这条线不只是封闭的 Apple 内部项目。限制在于：原文没有披露 GPU 数量、收入贡献、软件收费或后续扩容节奏，短期难以映射到盈利预测。动作上维持 A 池核心，把“机密计算是否成为 Blackwell 新的差异化卖点”列为后续验证点，而不是因为单篇合作文章提高仓位。

**后续观察点**

- 跟踪 Apple、Google Cloud 或 NVIDIA 后续是否披露 PCC 扩容范围、GPU 部署规模、上线节奏和更多 Apple Intelligence 功能落地细节。
- 观察 NVIDIA 财报或电话会是否开始单独提及 confidential computing、secure 推理 或 Blackwell 在高隐私推理场景中的客户采用情况。
- 继续看 Google Cloud 是否把机密推理能力产品化，确认这不是单一客户定制，而是可复制的云端基础设施能力。
- 对比 AMD、Intel 及云厂商自研方案在 trusted execution 与 secure 推理 上的进展，判断 NVIDIA 的机密计算是否具备可持续差异化。

[原文](https://blogs.nvidia.com/blog/nvidia-confidential-computing-apple-private-cloud-compute/)
