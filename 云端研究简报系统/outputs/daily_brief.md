# 竹鉴日报 | 2026-09-02

今日关键变化：

1. 公司：NVIDIA
   事件：Blackwell NVL72把推理能效作为AI工厂经济性的核心指标，强化NVIDIA从GPU到整机架系统的定价权
   核心内容：2026-07-14，NVIDIA发布performance per watt主题官方文章，强调AI工厂经济性取决于固定电力预算内生成token的能力。文章披露，GB300 NVL72在DeepSeek V4 Pro等新一代开放模型上的performance per watt相对Hopper最高可达25x，GLM5.1可达20x，Kimi K2.6可达10x；DeepSeek V4的软件优化在一个月内又把performance per watt最高提升5x。NVIDIA还称DSX MaxLPS可通过实时功率调度和液冷等手段，让AI工厂在同一功率预算内运行最多40%更多GPU，并点名Anthropic、OpenAI、SpaceXAI、CoreWeave、Perplexity和Fireworks AI等生产采用线索。
   关键证据：NVIDIA还称DSX MaxLPS可通过实时功率调度和液冷等手段，让AI工厂在同一功率预算内运行最多40%更多GPU，并点名Anthropic、OpenAI、SpaceXAI、CoreWeave、Perplexity和Fireworks AI等生产采用线索
   为什么重要：这是一条P2级平台经济性事件。它不直接新增一个可确认订单，但把NVIDIA数据中心业务的竞争焦点从单卡性能扩展到机架级推理吞吐、能耗、软件优化和生产稳定性。对高估值最关键的含义是：如果推理需求成为下一阶段AI资本开支主轴，客户采购时会更重视每瓦token产出和每token成本，而这正是NVIDIA把GPU、NVLink、网络、软件和电力管理打包成AI工厂平台的定价依据。
   动作：维持A池核心跟踪；把Blackwell/Rubin机架级能效、推理每token成本和生产客户采用作为高估值验证线
   [原文](https://blogs.nvidia.com/blog/performance-per-watt-ai-infrastructure-efficiency/)

2. 公司：NVIDIA
   事件：BMS部署第二套DGX SuperPOD并采用8套Vera Rubin NVL72，验证NVIDIA AI工厂进入生命科学研发生产流
   核心内容：2026-07-20，NVIDIA发布Bristol Myers Squibb客户案例，称BMS正在部署第二套NVIDIA DGX SuperPOD，新系统由8套DGX Vera Rubin NVL72系统构成，每套包含NVIDIA Vera CPU和Rubin GPU，性能/兆瓦最高达到被替换基础设施的10x。BMS已运行DGX SuperPOD约三年，AI-enabled target identification已节省科学家数周手工工作，并用于扩展CELMoD化合物库和lead optimization中的Predict First分子筛选；新旧系统将整合为统一环境和单一数据平面，面向全球BMS科学家开放。
   关键证据：2026-07-20，NVIDIA发布Bristol Myers Squibb客户案例，称BMS正在部署第二套NVIDIA DGX SuperPOD，新系统由8套DGX Vera Rubin NVL72系统构成，每套包含NVIDIA Vera CPU和Rubin GPU，性能/兆瓦最高达到被替换基础设施的10x
   为什么重要：这是一条P2级客户部署事件。它的价值不在于单笔金额披露，因为原文没有给订单价格或收入确认节奏；价值在于BMS把NVIDIA AI工厂从实验集群扩展到全球研发生产平台，说明企业级行业客户正在用机架级系统、BioNeMo、Mission Control和智能体工作流重构药物发现流程。它验证的是NVIDIA数据中心需求不只来自互联网大模型公司，也可能来自制药、科学计算和行业研发的长期算力预算。
   动作：维持A池核心跟踪；把生命科学AI工厂作为企业级行业渗透样本观察，不因单一客户案例改变仓位
   [原文](https://blogs.nvidia.com/blog/bristol-myers-squibb-building-life-science-industrys-most-advanced-ai-factory-on-nvidia-vera-rubin/)

后续观察：

  1. 下次财报里数据中心收入能否继续维持高增速，而不是只靠个别大客户拉动。
  2. GAAP / non-GAAP 毛利率是否仍能维持在高位，平台扩张是否开始侵蚀盈利质量。
  3. 超大客户资本开支口径有没有变化，推理需求是否真的接上训练需求。
