# 竹鉴晨报 | 2026-05-28

## 1. NVIDIA｜Vera CPU 首批交付 Anthropic/OpenAI/SpaceXAI/Oracle：88 核 Olympus、1.2TB/s 带宽，定位 智能体 AI 新业务

**原文讲了什么**

NVIDIA 官方博客称，公司在 GTC San Jose（3 月）发布的独立 CPU 产品 Vera 已开始从实验室走向客户：首批 Vera CPU 交付给 Anthropic（旧金山）、OpenAI（Mission Bay）、SpaceXAI（帕洛阿尔托），随后又交付给 Oracle Cloud Infrastructure（圣克拉拉）。

文章将 Vera 的定位描述为“为 智能体 AI 时代定制的 CPU”：其关键工作负载不是 GPU 的矩阵计算，而是智能体沙箱、工具调用、编排层与长上下文检索等大量并发、实时的 CPU 侧任务。

文中给出 Vera 的核心规格与口径：88 个 NVIDIA 自研 Olympus 核心、1.2TB/s 内存带宽、每核性能较传统方案快 50%；并援引 Anthropic 负责人观点，强调扩展算力对模型迭代的重要性。

**业务影响**

对业务层面，Vera 的价值在于提高 NVIDIA 在 AI 工厂“全栈控制面”的嵌入度：智能体编排、工具沙箱、检索与数据管道等 CPU 密集环节若能与 GPU/互连/系统一起打包销售，有机会提升机架级系统的整机份额与客户切换成本。与此同时，CPU 是传统强竞争市场，真正影响经营要看是否进入主流服务器平台（OEM 上架、云实例化）以及与既有 GPU 平台形成可规模复制的联合方案。

**估值/动作影响**

估值/动作上，这更偏“平台溢价验证”而非短线催化：正面是平台边界扩展与头部客户试用开启，有助于支撑对 NVIDIA 长期 TAM 与生态粘性的更高权重；约束是 CPU 业务的量产节奏、毛利结构与与既有 CPU 生态的竞争强度尚未披露。动作建议维持核心持仓/研究优先级不变，把 Vera 的规模化上架与与机架级系统绑定销售作为后续验证点，避免仅凭发布与首批交付上调短期盈利假设。

**后续观察点**

- 验证产品化：Vera 是否被主流 OEM（含 Dell/HPE/Lenovo 等）纳入企业服务器产品线，以及对应的上市时间与配置口径。
- 验证规模化：是否出现云厂商（含 OCI/其他 hyperscaler）公开的 Vera 实例/机型上架与可用区扩展节奏，而不仅是首批交付新闻。
- 验证商业化：后续财报/指引中是否开始披露 CPU/系统相关的收入口径、订单或客户采用指标。
- 验证竞争格局：客户是否将 Vera 作为 x86/Arm 的补充还是替代；是否出现“与 NVIDIA GPU/互连绑定”才能显著成立的采购模式。

[原文](https://blogs.nvidia.com/blog/vera-cpu-delivery/)

## 2. NVIDIA｜Dell AI Factory with NVIDIA：Rubin NVL72/XE9812 与 HGX Rubin NVL8 上线，宣称推理 cost/token 最高降 10x、144 GPU/rack

**原文讲了什么**

NVIDIA 官方博客围绕 Dell Technologies World 的企业侧“Dell AI Factory with NVIDIA”叙事，强调企业 AI 从试点走向 智能体 AI 与大规模推理部署，并给出多项与 Rubin 平台相关的新品口径。

文章称 Dell PowerEdge XE9812（基于 NVIDIA Vera Rubin NVL72）面向大规模 智能体 AI 推理，宣称相对 NVIDIA Blackwell 可实现“最高 10 倍更低 cost-per-token”；并称 XE9880L/XE9885L/XE9882L 为首批基于 NVIDIA HGX Rubin NVL8 的 Dell 系统，支持每机架最高 144 GPU、100% 直冷节点，并宣称相对 HGX B200 最高 10 倍性能。

文章同时提到网络侧的 Dell PowerSwitch + NVIDIA Quantum-X800 InfiniBand、Spectrum-6 Ethernet，以及整机一体化的 Dell PowerRack；在 CPU 侧，Dell PowerEdge M9822/R9822 将引入 Vera CPU，并给出“1.2TB/s 内存带宽、智能体 工作负载 50% 更快”等口径。

**业务影响**

对业务层面，这条动态强化了 NVIDIA 的“AI 工厂平台”在企业私域市场的落地路径：通过 Dell 这样的 OEM，把 GPU（Rubin）、网络（InfiniBand/Ethernet）与整机系统（PowerRack）作为可交付单元进入企业数据中心。这有助于 NVIDIA 把增长从云厂商 资本开支 扩展到更分散但规模巨大的企业侧推理与 智能体 部署市场；同时，OEM/系统层的推进也可能提升网络与系统级产品的绑定率，形成更高的每机架收入与更强的方案锁定效应。

**估值/动作影响**

估值/动作上，这类“企业侧产品化”信息更多影响确信度与中长期渗透率假设：正面是它支持平台化溢价（系统/网络/软件协同）而非纯芯片周期；约束是口径多为发布会宣称，短期兑现仍取决于 Rubin 量产与交付、企业预算释放与项目扩散速度。动作建议维持核心跟踪，避免把发布会对比直接外推为短期毛利或收入加速；把验证重点放到 OEM 订单/交付、企业侧推理需求可见性，以及网络/系统收入占比是否继续抬升。

**后续观察点**

- 验证兑现：后续季度中 NVIDIA 是否披露 Rubin/机架级系统的出货节奏与供给约束缓解情况，企业侧需求是否在订单/收入口径中变得可见。
- 验证结构：观察 数据中心 内部网络/系统/软件相关收入占比是否继续上升，验证“AI 工厂打包交付”是否在财务上成立。
- 验证 OEM 扩散：除 Dell 外，其他 OEM 的 Rubin 相关产品是否同步推进并形成可复制的交付模板（液冷、机架级、PowerRack 类整机）。
- 验证 TCO：关注第三方或客户侧对 cost-per-token、液冷、集成成本的可验证数据，避免仅采用厂商宣称口径。

[原文](https://blogs.nvidia.com/blog/dell-technologies-agent-enterprise-ai/)
