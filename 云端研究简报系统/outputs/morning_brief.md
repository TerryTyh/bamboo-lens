# 竹鉴晨报 | 2026-07-11

## 1. NVIDIA｜Nemotron 3 Ultra 接入 LangChain 深度智能体，NVIDIA 把开源智能体栈推到接近闭源模型的企业可用区间

**原文讲了什么**

原文讲的是 NVIDIA Nemotron 3 Ultra 与 LangChain 深度智能体框架的适配结果。LangChain 针对 Nemotron 3 Ultra 调整智能体运行框架，使其在深度智能体基准测试上取得开源模型中的最高准确率，同时完成更多任务、吞吐更高，并且单次运行推理成本比领先闭源模型低 10 倍。文章还强调，该结果不是通过重新训练模型获得，而是通过围绕模型的系统工程调优实现，包括系统提示词、工具描述和中间件。

文章进一步说明，Nemotron 3 Ultra 在 LangChain 的深度智能体基准测试中达到了与最高分闭源模型相当的业务任务表现。LangChain 的智能体工程平台拥有每月超过 2 亿次下载，调优后的配置已可直接通过 LangChain 使用，这让企业可以在开放模型、开放编排框架和开放安全运行时上构建可自定义、可治理、可部署在自有基础设施或云上的智能体系统。

原文给出了初步采用线索：Abridge、Amdocs 和 Box 正在把专用智能体嵌入各自平台，EY 则在扩展围绕 NVIDIA NemoClaw 深度智能体蓝图的实施能力。NVIDIA NemoClaw for LangChain Deep Agents 被定义为面向企业专用 AI 的开放参考蓝图，组合 LangChain 深度智能体代码、Nemotron 3 Ultra 调优结果和 NVIDIA OpenShell 安全运行时。

**业务影响**

业务影响主要落在企业推理、AI 软件栈和合作伙伴实施生态。LangChain 是开发者和企业构建智能体的重要入口，月下载量超过 2 亿次意味着 NVIDIA 的 Nemotron、NemoClaw 和 OpenShell 组合有机会进入大量现有智能体工作流，而不是只停留在自有示例。10 倍成本优势如果在真实企业任务中可复现，会降低持续评估和多场景部署门槛，拉动对 NVIDIA GPU 推理、NIM、NemoClaw 蓝图、安全运行时和企业实施服务的配套需求。限制是，文章仍未披露这些客户带来的收入规模、付费模式或硬件拉动量，因此目前只能作为企业智能体栈渗透证据。

**估值/动作影响**

估值/动作上，这条事件支持继续给 NVIDIA 平台溢价，但不足以单独上调估值中枢。正面在于：开放模型在企业任务上接近闭源模型、推理成本显著下降，并进入 LangChain 这样高分发入口，有助于把企业 AI 从试点带向更多可治理的生产工作流。需要谨慎的是，低成本也可能压低部分推理单价，最终价值取决于使用量扩大、软件配套附加、企业私有部署和服务生态能否抵消单价下降。动作上维持 A 池核心，不因该事件追高；后续重点看企业客户数量、NemoClaw、OpenShell、NIM 的收费口径、推理工作负载增长，以及是否在财报中体现为软件和服务收入。

**后续观察点**

- 跟踪 Abridge、Amdocs、Box 与 EY 是否披露基于 Nemotron、NemoClaw 和 LangChain 的实际部署规模、客户数量或生产环境案例。
- 观察 NVIDIA 是否在财报、电话会或产品口径中披露 Nemotron、NemoClaw、OpenShell、NIM 与企业推理相关的软件收入、订阅或配套附加率。
- 验证 10 倍推理成本优势是否能在真实企业工作流中复现，而不是只停留在 LangChain 深度智能体基准测试。
- 比较开放智能体栈与闭源模型 API 在安全、治理、本地部署和持续评估成本上的差异，判断企业是否因此扩大 NVIDIA GPU 推理需求。
- 关注 LangChain、云厂商和系统集成商是否继续把 NVIDIA 开放栈做成默认可选路径，决定它是单点合作还是生态入口。

[原文](https://blogs.nvidia.com/blog/nemotron-langchain-agents-open-stack/)
