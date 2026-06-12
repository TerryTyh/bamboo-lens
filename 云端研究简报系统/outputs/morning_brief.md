# 竹鉴晨报 | 2026-06-13

## 1. NVIDIA｜Apple Intelligence 私有云开始采用 Blackwell 机密计算，NVIDIA 切入高隐私推理基础设施

**原文讲了什么**

原文先讲清楚一件具体事实：Apple 的 Private Cloud Compute 已经开始在 Google Cloud 上使用带有 机密计算 的 NVIDIA GPU，为 Apple Foundation Models 提供 confidential 推理。也就是说，Apple Intelligence 的一部分云端推理不再只停留在 Apple 自有数据中心，而是开始借助外部云与 NVIDIA 的机密计算栈承载。

文章进一步说明三方分工。Apple 提供 Apple Foundation Models 与 Private Cloud Compute 架构，Google Cloud 提供外部云基础设施，NVIDIA 则提供 Blackwell GPU 和硬件级 机密计算，把敏感推理负载放进可信执行环境，并在数据发往服务器之前完成加密校验。

原文强调的重点不是更高吞吐，而是“即使系统建设者也看不到用户数据、聊天内容和对话”。这意味着 NVIDIA 想把 Blackwell 的卖点从训练与通用推理，进一步延伸到隐私要求更高的消费级智能助手与企业敏感推理场景。

**业务影响**

业务上，这条事件同时验证了三件事。第一，Blackwell 的落地场景从超大模型训练扩展到消费级智能助手的服务端推理，说明推理需求曲线正在向更广泛终端生态渗透。第二，机密计算 不再只是安全功能展示，而是成为大型客户把敏感 AI 负载放上外部云的前提条件，这会提高 GPU、系统软件与云合作方案的整体附加率。第三，Apple、Google、NVIDIA 的组合说明 NVIDIA 正在参与“模型提供方 + 云基础设施 + 安全执行环境”这一整套交付链，而不只是底层芯片供应商。

**估值/动作影响**

估值和动作上，这条事件支持继续给予 NVIDIA 平台溢价，因为它把市场对公司的需求来源进一步扩展到高隐私推理和可信 AI 基础设施。正面在于原文给出了 Apple Private Cloud Compute、Google Cloud、Blackwell 和 机密计算 这几个非常具体的落地抓手，说明机密计算开始进入真实生产场景。限制在于文章没有披露 GPU 数量、合同金额、推理规模或软件收入贡献，因此不足以单独上调短期盈利预测。动作上维持 A 池核心，并把机密计算渗透率、服务端推理负载和大型平台客户采用情况列为新增验证主线。

**后续观察点**

- 跟踪 Apple 后续是否披露 Private Cloud Compute 在 Google Cloud 上的推理规模、覆盖功能范围和上线节奏，确认这不是局部试点。
- 观察 NVIDIA 财报或电话会是否开始单独提及 机密计算、secure 推理 或高隐私推理场景的客户需求。
- 继续看 Google Cloud 是否围绕 Blackwell 机密计算推出更明确的产品化口径、客户案例或定价模式。
- 跟踪 Apple Intelligence 后续功能扩张是否带来更高的服务端推理占比，验证这类消费级 AI 助手是否能转化为持续算力需求。

[原文](https://blogs.nvidia.com/blog/nvidia-confidential-computing-apple-private-cloud-compute/)
