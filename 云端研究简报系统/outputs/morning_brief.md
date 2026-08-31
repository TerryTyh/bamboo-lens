# 竹鉴晨报 | 2026-09-01

## 1. NVIDIA｜BMS部署第二套DGX SuperPOD并采用8套Vera Rubin NVL72，验证NVIDIA AI工厂进入生命科学研发生产流

**原文讲了什么**

NVIDIA这篇官方客户案例说明，Bristol Myers Squibb已经运行一套DGX SuperPOD约三年，现在继续部署第二套DGX SuperPOD，新系统由8套DGX Vera Rubin NVL72机架级系统组成。BMS的目标不是只给少数计算专家使用超算，而是把统一AI平台开放给全球每位科学家，用于预测、模型训练和贯穿药物发现流程的智能体工作流。

原文给出具体部署和效率线索：8套系统每套由NVIDIA Vera CPU和Rubin GPU组成，性能/兆瓦最高达到被替换基础设施的10x，并接入NVIDIA BioNeMo 智能体工具包。BMS称现有AI已经在target identification中节省科学家数周手工工作，并帮助扩展CELMoD化合物库；在lead optimization阶段，BMS使用Predict First方法，用预测结果筛选更可能满足多参数性质要求的分子，减少低价值合成实验。

文章还说明BMS的组织用法正在从单点AI工具走向研发平台。新旧SuperPOD会整合进统一环境和单一数据平面，面向全球BMS站点开放；过去由并购遗留站点限制、计算专业门槛造成的访问障碍，将通过NVIDIA Mission Control和自然语言发起复杂预测的AI-native tooling降低。BMS还计划把算力分配到小分子、大分子、临床应用和digital twins等多个节点。

**业务影响**

业务影响主要在企业AI和生命科学垂直行业渗透。BMS案例把NVIDIA平台嵌入target identification、化合物库扩展、lead optimization、临床应用和digital twins等研发节点，客户需求从一次性GPU采购变成统一AI平台、工具链、算力调度和工作流接入。若这种模式被更多药企复制，NVIDIA的数据中心业务会多一条行业AI工厂需求线，并提高BioNeMo、Mission Control、DGX SuperPOD和Vera Rubin整机架系统的组合销售价值。

**估值/动作影响**

估值/动作上，这条事件支持NVIDIA平台溢价和企业AI渗透假设，但权重低于财报收入、毛利率、订单能见度和云厂资本开支。当前不因BMS个案提高估值区间或仓位；更合理的处理是维持A池核心跟踪，把生命科学AI工厂作为企业行业化样本。若后续NVIDIA披露更多药企/生物科技客户、BioNeMo商业化收入、DGX SuperPOD行业复购或Mission Control软件收入，才可能提高企业AI软件和系统业务在估值分部中的权重。

**后续观察点**

- 跟踪BMS第二套DGX SuperPOD是否形成后续扩容、更多药物发现流程接入或公开研发效率指标。
- 观察NVIDIA是否披露更多生命科学客户采用Vera Rubin NVL72、BioNeMo 智能体工具包或Mission Control。
- 在财报中检查企业AI、DGX系统、软件和服务收入是否有可见增量，避免把客户案例误读成已量化收入。
- 关注制药行业AI基础设施是否从研发试点转为常规资本开支，尤其是全球站点统一数据平面和智能体工作流。
- 继续验证性能/兆瓦优势是否带来客户复购，而不只是单篇案例中的效率表述。

[原文](https://blogs.nvidia.com/blog/bristol-myers-squibb-building-life-science-industrys-most-advanced-ai-factory-on-nvidia-vera-rubin/)

## 2. NVIDIA｜Blackwell NVL72把推理能效作为AI工厂经济性的核心指标，强化NVIDIA从GPU到整机架系统的定价权

**原文讲了什么**

NVIDIA这篇官方文章把AI工厂的核心约束从单纯GPU数量转到电力预算内的token产出。原文认为，智能体AI会继续推高推理token需求，谁能在固定功耗下生成更多token，谁就能获得更高收入和更低每token成本；因此performance per watt不是营销指标，而是AI工厂收入和利润率的底层变量。

文章用Blackwell NVL72解释为什么机架级设计重要。前沿模型普遍采用MoE架构，服务这类模型时，GPU domain size会影响专家并行和推理效率；Hopper时代的8-GPU domain已经不够，Blackwell NVL72把规模扩到72-GPU domain，并通过NVLink Switch、Dynamo、TensorRT LLM、SGLang、vLLM、NVFP4量化、分离式服务、KV-aware routing和KV cache offloading等软硬件协同提升推理效率。

原文还给出生产侧证据：NVIDIA称GB300 NVL72在新一代开放模型上的performance per watt相对Hopper最高可达25x，GLM5.1可达20x，Kimi K2.6可达10x；DeepSeek V4的软件优化在一个月内又把performance per watt最高提升5x。AI工厂中冷却和机架效率损耗可能让约60%的电力真正转化为有效AI工作，DSX MaxLPS通过实时调度GPU和机架功率、支持温水液冷等方式，使运营方可在同一功率预算内运行最多40%更多GPU。文章点名Anthropic、OpenAI、SpaceXAI、CoreWeave、Perplexity、Fireworks AI等生产客户或部署场景。

**业务影响**

业务上，这条信息强化NVIDIA从芯片供应商向AI工厂系统供应商的转变。MoE模型、长上下文和智能体工作负载会放大推理端的电力、网络、KV cache、液冷和调度瓶颈，单独比较GPU标称算力已经不够。Blackwell NVL72和未来Vera Rubin如果能在真实生产中持续降低每token成本，就会提升客户对整机架系统、NVLink Switch、Dynamo/TensorRT LLM和DSX电力管理软件的依赖，也会提高网络、系统和软件的配套附加率。

**估值/动作影响**

估值/动作上，这条事件支持继续给NVIDIA平台溢价，但不能单独上调估值区间。正面是推理经济性为Blackwell/Rubin迭代、NVLink scale-up、DSX和软件栈提供了可量化叙事，能帮助解释为什么客户可能继续接受高ASP和整机架采购。约束是文章中的倍数主要来自benchmark和NVIDIA口径，缺少收入贡献、订单金额、毛利率和客户采购规模；仓位动作维持A池核心跟踪，把后续财报中的数据中心收入、网络/系统收入、毛利率、库存、云厂资本开支和推理客户披露作为验证点。

**后续观察点**

- 跟踪Blackwell NVL72和GB300 NVL72在头部云厂、AI云和模型公司的实际部署规模，确认benchmark优势是否转化为持续采购。
- 观察下一次财报中数据中心收入、网络/系统收入和毛利率是否继续支撑AI工厂平台溢价。
- 验证推理需求是否真正接上训练需求，尤其是OpenAI、Anthropic、Perplexity、CoreWeave、Fireworks AI等客户的生产负载扩张。
- 跟踪DSX MaxLPS、Dynamo、TensorRT LLM等软件是否形成可收费、可续费或可提升系统ASP的商业口径。
- 继续检查电力、液冷、机架可靠性和客户资本开支是否成为增长瓶颈。

[原文](https://blogs.nvidia.com/blog/performance-per-watt-ai-infrastructure-efficiency/)
