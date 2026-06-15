# 竹鉴晨报 | 2026-06-16

## 1. NVIDIA｜Apple 把 Private Cloud Compute 扩到 Google Cloud，NVIDIA Blackwell 开始切入隐私推理底座

**原文讲了什么**

这篇原文讲的不是泛泛而谈的安全宣传，而是 Apple 已经把 NVIDIA 的机密计算 GPU 用到 Private Cloud Compute（PCC）里，并把原本主要在 Apple 自有数据中心运行的服务端推理，扩展到 Google Cloud。文章明确说，Apple Foundation Models 的部分服务端推理将使用带机密计算能力的 NVIDIA GPU，支撑下一代 Apple Intelligence 功能。

原文同时解释了这套架构为什么重要：NVIDIA Blackwell GPU 的 机密计算 会被嵌入 PCC 的硬件安全架构里，在 Google Cloud 上为敏感推理工作负载建立 trusted execution environment。系统会在数据进入服务器前做加密验证，确保底层基础设施未被篡改，目标是让用户数据、聊天和对话内容在被处理时仍然处于受保护状态。

换句话说，这不是单纯的 Apple 采用某一代 GPU，而是 Apple、Google Cloud 和 NVIDIA 三方把“高性能推理 + 云端弹性 + 隐私隔离”拼成了可落地的生产方案。对 NVIDIA 来说，机密计算开始从金融、政府等高合规场景，延伸到大规模消费级 AI 功能的后端推理。

**业务影响**

业务层面，这条事件至少影响三条线。第一条是 数据中心 GPU 需求：Apple Intelligence 如果持续扩大功能范围，服务端推理会变成长期负载，而不是发布会阶段的一次性项目。第二条是机密计算与系统软件 attach：当 Apple 这类平台型客户要求把 GPU 放进可验证隐私架构里，NVIDIA 的卖点就不再只是训练/推理性能，还包括安全隔离、远程度量和可信运行能力。第三条是云生态协同：Apple 把 PCC 扩到 Google Cloud，意味着 NVIDIA 在超大客户架构中的角色从“云厂商 GPU 供应商”进一步延伸到上层消费 AI 产品的后端底座。

**估值/动作影响**

估值和动作上，这条事件支持继续给 NVIDIA 平台溢价，尤其是对推理基础设施和系统级能力的溢价。正面在于，合作对象同时覆盖 Apple 与 Google，且原文把应用场景、GPU 代际和安全机制都写得比较具体，说明机密计算已经进入真实生产工作负载。限制在于，公告没有披露 GPU 数量、合同金额、推理负载规模或软件收入口径，因此它更适合作为“平台能力被高质量客户验证”的证据，而不是直接上调短期盈利预测。动作上维持 A 池核心，并把后续机密计算是否复制到更多企业与消费级推理场景列为重点观察。

**后续观察点**

- 跟踪 Apple 后续是否进一步披露 Private Cloud Compute 的部署范围、Google Cloud 占比和 Apple Intelligence 新功能上线节奏，确认这不是单点安全宣传。
- 观察 NVIDIA 财报或电话会是否开始明确提到 confidential 推理、机密计算 配套附加率 或安全型推理工作负载成为新增需求来源。
- 继续跟踪 Google Cloud、Microsoft Azure 等云平台对 Blackwell 机密计算产品的商业化口径，判断这类能力是否正在成为标准采购项。
- 留意 Apple、Google 或第三方安全研究对 PCC 架构的验证结果，确认可信执行环境没有因为性能、成本或运维复杂度而限制规模化部署。

[原文](https://blogs.nvidia.com/blog/nvidia-confidential-computing-apple-private-cloud-compute/)
