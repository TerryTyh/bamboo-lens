# 竹鉴晨报 | 2026-06-23

## 1. NVIDIA｜Apple 把 PCC 扩到 Google Cloud，NVIDIA 以 Blackwell 机密计算切入高隐私云端推理底座

**原文讲了什么**

这篇原文讲的不是普通合作站台，而是 Apple 的 Private Cloud Compute（PCC）开始从自有数据中心扩展到 Google Cloud，并在这个过程中使用带机密计算能力的 NVIDIA Blackwell GPU 处理 Apple Foundation Models 的服务端推理。核心问题不是 Apple 上不上 NVIDIA，而是高隐私消费级 AI 推理是否开始需要云端机密计算能力。

原文先交代 PCC 的变化：Apple Intelligence 的部分下一代功能，将把服务端推理能力放到 Google Cloud，同时仍保持 PCC 的硬件安全架构。NVIDIA 在这里与 Apple 和 Google 协作，提供带 机密计算 的 Blackwell GPU，使敏感数据在进入服务器前，可以先验证底层基础设施没有被篡改。

文章对机密计算的解释很明确。NVIDIA 机密计算 通过硬件级可信执行环境隔离 AI 工作负载，并允许系统以加密方式证明底层基础设施未被篡改；对最终用户而言，连系统构建者也无法查看其数据、聊天或对话内容。这意味着 NVIDIA 切入的不是普通推理算力，而是更高安全等级的云端推理场景。

从投资视角更重要的是，这把 NVIDIA 的角色从企业/科研/主权 AI 扩展到消费级大模型云端推理与隐私保护基础设施。Apple、Google Cloud 和 Blackwell 机密计算出现在同一条链路里，说明未来云端 AI 推理的竞争不只比吞吐和成本，也开始比安全隔离、可信执行和合规能力。

**业务影响**

业务层面，这条事件把 NVIDIA 的推理能力进一步延伸到高隐私消费级 AI 云端基础设施。Apple Intelligence 若要把更多模型能力放到云端，就必须同时解决延迟、吞吐和隐私保护；NVIDIA 在这里提供的不是普通 GPU，而是可嵌入 PCC 安全架构的机密计算底座。若这类需求扩大，NVIDIA 的价值将不只来自训练和企业推理，还可能覆盖消费级云端推理、可信执行环境以及更严格合规场景下的推理部署。

**估值/动作影响**

估值和动作上，这条事件更像中期平台化证据，而不是短期业绩催化。正面在于，Apple、Google Cloud 与 NVIDIA Blackwell 机密计算被放进同一条实际部署链路，证明云端推理的竞争维度正在从单纯算力和成本，扩展到安全隔离与可验证可信执行。限制在于，文章没有披露部署规模、GPU 数量、定价或长期采购承诺，因此不能据此直接上调收入预测。动作上维持 A 池核心，把 confidential 推理 是否成为新的高附加值推理赛道列入验证清单。

**后续观察点**

- 跟踪 Apple 后续是否披露更多基于 PCC 的云端功能范围、上线节奏或推理规模，判断这是否只是试点而非广泛部署。
- 观察 Google Cloud 与 NVIDIA 后续是否把 Blackwell confidential 推理 产品化成更标准的云服务能力，并出现更多客户案例。
- 继续看 NVIDIA 财报中推理需求、软件附加率和机密计算相关口径，验证安全推理是否开始形成收入贡献。
- 关注消费级 AI 对隐私、安全和合规要求提升后，是否推动更多云端模型部署采用 trusted execution 与 confidential computing。

[原文](https://blogs.nvidia.com/blog/nvidia-confidential-computing-apple-private-cloud-compute/)

## 2. NVIDIA｜英国主权 AI 基建一年内翻倍扩容，NVIDIA 开始把国家级算力、区域云与本土创业生态接成同一承接层

**原文讲了什么**

这篇原文不是泛泛而谈英国重视 AI，而是在交代过去一年英国如何把“做 AI 的国家、而不是只买 AI 的国家”落成一套具体基础设施。文章先回顾 Jensen Huang 与英国首相去年在 London Tech Week 提出的主权 AI 方向，再展示一年后已经出现的算力扩容、区域云部署和本土创业项目承接。

最核心的信息是英国本土 AI 基础设施的新增供给。原文说，计划在英国本土部署 AI 基础设施的 AI 云提供商数量一年内已经翻倍；Nebius 计划新增三处先进 NVIDIA AI 基建部署，全部爬坡完成后预计在 2027 年达到 65 兆瓦；CoreWeave 正在英国政府设定的 AI Growth Zones 建设，另有七家 NVIDIA AI Cloud 生态伙伴仍在推进中。

文章还把英国电信网络、主权数据中心与国家级科研算力放在同一张图里。BT 与 Nscale 计划在英国三处既有 BT 站点建设主权 AI 数据中心，把 NVIDIA AI 基础设施、Nscale 全栈能力和 BT 全国连接骨干结合起来；Isambard-AI 被描述为英国最强计算机，基于 5,400 颗 NVIDIA GH200 Grace Hopper Superchips，并全部使用零碳电力运行。

更重要的是，这些算力不是停留在展示层。英国政府 Sovereign AI Fund 已开始把本土算力直接分配给本国公司，其中包括刚宣布与 NVIDIA 合作强化强化学习基础设施的 Ineffable Intelligence，以及多家使用 Isambard-AI 的 NVIDIA Inception 创业公司。也就是说，NVIDIA 正在把主权 AI 的需求从“政府想建算力”推进到“区域云、科研算力和本土创业生态都开始消耗这套平台”。

**业务影响**

业务层面，这条事件强化了 NVIDIA 在主权 AI 与区域云基础设施中的平台位置。65 兆瓦级别的新增部署、BT/Nscale 的主权数据中心计划以及 5,400 颗 GH200 的国家科研集群，说明需求已经不仅是云厂商训练集群，而是开始覆盖电信机房、本国科研、创业孵化和监管敏感行业。这样一来，NVIDIA 不只是卖 GPU，而是在区域云、电信连接、主权控制和本土 AI 创新之间提供一套可复用的平台底座，延长需求曲线并分散客户结构。

**估值/动作影响**

估值和动作上，这条事件支持高估值中的主权 AI 与区域云扩散逻辑，但仍不足以单独上调短期盈利预测。正面在于，原文给出了可验证的容量与部署信号，包括 provider 数量翻倍、Nebius 65 兆瓦、BT/Nscale 三站点和 5,400 颗 GH200；这比泛泛合作新闻更接近真实基建节奏。限制在于，文章没有披露 NVIDIA 对应的订单金额、装机节奏、利用率和毛利率贡献。动作上维持 A 池核心，但要把主权 AI 需求是否能持续转成高质量数据中心收入列为下一阶段重点验证。

**后续观察点**

- 跟踪 Nebius、BT、Nscale、CoreWeave 等后续是否披露英国项目的 GPU 数量、上线时间、利用率或客户案例，判断 65 兆瓦与三站点是否真正落地。
- 观察 NVIDIA 财报或电话会里是否开始更频繁提到 主权 AI、regional AI clouds 和 电信 AI 基础设施，并对应到数据中心收入结构。
- 继续看 Isambard-AI 与 Sovereign AI Fund 支持的本土公司是否披露训练、推理或商业化进展，验证主权算力是否形成可持续工作负载。
- 关注英国及欧洲电力、监管、数据主权和融资约束是否拖慢本地主权 AI 基建扩张节奏。

[原文](https://blogs.nvidia.com/blog/uk-sovereign-ai-advancements/)
