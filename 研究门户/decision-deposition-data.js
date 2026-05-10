window.BAMBOO_LENS_DECISION_DEPOSITION = {
  "generated_at": "2026-05-10T18:16:37",
  "source_event_store_at": "2026-05-10T18:16:37",
  "source_decision_impact_at": "2026-05-10T18:16:37",
  "items": [
    {
      "company": "tsmc",
      "company_name": "TSMC",
      "event_index": 0,
      "event_title": "2026 年 4 月营收 NT$4107.3 亿，环比小降但同比仍增 17.5%，高位需求进入延续验证期",
      "event_date": "2026-05-08",
      "priority": "P1",
      "direction": "正向强化",
      "trigger_type": "维持核心并观察加仓条件",
      "status": "needs_model_update",
      "quality": "可自动生成回写建议",
      "update_targets": [
        "当前结论",
        "财务数据地图",
        "估值模型"
      ],
      "recommended_updates": [
        {
          "target": "当前结论",
          "fields": [
            "latestEvent",
            "businessImpact",
            "valuationImpact",
            "nextCheck"
          ],
          "suggestion": "把最新事件更新为「2026 年 4 月营收 NT$4107.3 亿，环比小降但同比仍增 17.5%，高位需求进入延续验证期」；业务影响写入：业务上，4 月营收说明领先制程需求仍然稳健，但月度营收本身不能拆分 HPC、智能手机、IoT 或汽车。结合 Q1 财报中 HPC 占净收入 61%、先进制程占晶圆收入 74%，更合理的理解是：AI/HPC 与先进制程仍是收入高位的主要支撑，4 月只是进入 Q2 的第一块拼图。；估值/动作写入：估值上，4 月数据支持 TSMC 维持合理偏高质量溢价，但不支持无脑上调估值。原因是收入端仍强，但市场真正关心的是 Q2 指引能否兑现、毛利率能否保持 65.5%-67.5%、高 capex 后自由现金流是"
        },
        {
          "target": "财务数据地图",
          "fields": [
            "financeMap",
            "financials"
          ],
          "suggestion": "如果事件包含收入、利润率、现金流、capex、订单或 backlog 数字，应把关键数字进入财务表格，并解释它改变了哪条财务判断。"
        },
        {
          "target": "估值模型",
          "fields": [
            "valuationModel",
            "valuationFrame"
          ],
          "suggestion": "估值上，4 月数据支持 TSMC 维持合理偏高质量溢价，但不支持无脑上调估值。原因是收入端仍强，但市场真正关心的是 Q2 指引能否兑现、毛利率能否保持 65.5%-67.5%、高 capex 后自由现金流是否稳健。动作上继续持有/观察，不因 4 月环比 -1.1% 下调判断，也不因累计同比 29.9% 直接追高。"
        }
      ],
      "reason": "这是一条 P1 级延续验证事件。4 月同比增速低于 3 月，但绝对收入维持高位，1-4 月累计同比仍达 29.9%。对 TSMC 来说，现在最重要的问题从“需求是否强”转向“强需求能否在 Q2 继续兑现，并维持高毛利率”。",
      "valuation_impact": "估值上，4 月数据支持 TSMC 维持合理偏高质量溢价，但不支持无脑上调估值。原因是收入端仍强，但市场真正关心的是 Q2 指引能否兑现、毛利率能否保持 65.5%-67.5%、高 capex 后自由现金流是否稳健。动作上继续持有/观察，不因 4 月环比 -1.1% 下调判断，也不因累计同比 29.9% 直接追高。",
      "next_verification": [
        "5 月和 6 月营收是否继续维持高台阶，是验证 Q2 指引 US$39.0-40.2 billion 的核心。",
        "Q2 财报中毛利率是否落在 65.5%-67.5%，决定高收入是否转化为高质量利润。",
        "继续关注 3nm、5nm、CoWoS 和 2nm 需求口径，判断先进制程供需是否仍偏紧。"
      ],
      "detail_link": "./event.html?company=tsmc&event=0&return=company&v=20260505-1",
      "sort_key": 20260508
    },
    {
      "company": "nvidia",
      "company_name": "NVIDIA",
      "event_index": 0,
      "event_title": "DOE Genesis Mission 与 Argonne 两台 AI 超算强化 NVIDIA 在国家级 AI 科学基础设施中的平台地位",
      "event_date": "2026-05-07",
      "priority": "P1",
      "direction": "正向强化",
      "trigger_type": "上调研究优先级",
      "status": "needs_model_update",
      "quality": "可自动生成回写建议",
      "update_targets": [
        "当前结论",
        "公司理解",
        "财务数据地图",
        "估值模型"
      ],
      "recommended_updates": [
        {
          "target": "当前结论",
          "fields": [
            "latestEvent",
            "businessImpact",
            "valuationImpact",
            "nextCheck"
          ],
          "suggestion": "把最新事件更新为「DOE Genesis Mission 与 Argonne 两台 AI 超算强化 NVIDIA 在国家级 AI 科学基础设施中的平台地位」；业务影响写入：业务影响主要落在 Data Center、HPC/科学计算、主权 AI 与 AI 工厂系统方案。Equinox 和 Solstice 展示的是 NVIDIA 从 GPU、软件栈、模型、AI agent 到超算系统的全栈位置。对投资人而言，这类事件的重要性不在单个项目收入，而在验证 NVIDIA 的需求来源正在从 hyperscaler 训练集群扩展到政府、国家实验室、科学计算和能源科研。它也把 AI 基础设施需求和电力供给绑定，进一步解释为什么 NVIDIA 的平"
        },
        {
          "target": "公司理解",
          "fields": [
            "businessMap",
            "positioning",
            "moatDetail"
          ],
          "suggestion": "业务影响主要落在 Data Center、HPC/科学计算、主权 AI 与 AI 工厂系统方案。Equinox 和 Solstice 展示的是 NVIDIA 从 GPU、软件栈、模型、AI agent 到超算系统的全栈位置。对投资人而言，这类事件的重要性不在单个项目收入，而在验证 NVIDIA 的需求来源正在从 hyperscaler 训练集群扩展到政府、国家实验室、科学计算和能源科研。它也把 AI 基础设施需求和电力供给绑定，进一步解释为什么 NVIDIA 的平台边界会外溢到能源、电网和国家战略基础设施。"
        },
        {
          "target": "财务数据地图",
          "fields": [
            "financeMap",
            "financials"
          ],
          "suggestion": "如果事件包含收入、利润率、现金流、capex、订单或 backlog 数字，应把关键数字进入财务表格，并解释它改变了哪条财务判断。"
        },
        {
          "target": "估值模型",
          "fields": [
            "valuationModel",
            "valuationFrame"
          ],
          "suggestion": "估值上，这条事件支持 NVIDIA 维持平台溢价和更长需求曲线，而不是只按短周期 GPU 订单看待。它增强“AI 工厂 + 主权 AI + 科学计算基础设施”的可持续性，但尚不足以单独上调估值中枢，因为文章没有披露项目合同金额、交付节奏、毛利率或收入确认。动作上维持 A 池核心，研究优先级提升到“政府/科研/能源 AI 基础设施需求是否成为第三增长曲线”，仓位动作仍需等财报中 Data Center、networking、Rubin 订单和客户结构验证。"
        }
      ],
      "reason": "这是一条 P1 级平台地位强化事件。它不直接等同于短期订单增量，但强化了 NVIDIA 的长期角色：不只是卖 GPU，而是在国家级 AI 科学、主权 AI、超算和能源基础设施中提供全栈平台。更重要的是，Vera Rubin 级别的大规模部署进入国家实验室语境，说明 NVIDIA 的下一代平台有望继续获得非互联网客户、政府科研体系和能源科学场景的需求支撑。",
      "valuation_impact": "估值上，这条事件支持 NVIDIA 维持平台溢价和更长需求曲线，而不是只按短周期 GPU 订单看待。它增强“AI 工厂 + 主权 AI + 科学计算基础设施”的可持续性，但尚不足以单独上调估值中枢，因为文章没有披露项目合同金额、交付节奏、毛利率或收入确认。动作上维持 A 池核心，研究优先级提升到“政府/科研/能源 AI 基础设施需求是否成为第三增长曲线”，仓位动作仍需等财报中 Data Center、networking、Rubin 订单和客户结构验证。",
      "next_verification": [
        "下一次 NVIDIA 财报或电话会中，关注管理层是否提到 sovereign AI、national labs、government AI infrastructure 或 scientific computing demand。",
        "跟踪 Equinox 和 Solstice 的建设进度、交付时间、是否转化为可量化订单或长期服务收入。",
        "观察 Vera Rubin 平台在 100,000 GPU 级别科学计算场景中的部署是否顺利，是否成为下一代平台需求验证样板。"
      ],
      "detail_link": "./event.html?company=nvidia&event=0&return=company&v=20260505-1",
      "sort_key": 20260507
    },
    {
      "company": "nvidia",
      "company_name": "NVIDIA",
      "event_index": 1,
      "event_title": "Spectrum-X + MRC 把以太网推向 AI 工厂训练网络，强化 NVIDIA 系统级平台位置",
      "event_date": "2026-05-06",
      "priority": "P1",
      "direction": "正向强化",
      "trigger_type": "维持核心并观察加仓条件",
      "status": "needs_model_update",
      "quality": "可自动生成回写建议",
      "update_targets": [
        "当前结论",
        "公司理解",
        "财务数据地图",
        "估值模型"
      ],
      "recommended_updates": [
        {
          "target": "当前结论",
          "fields": [
            "latestEvent",
            "businessImpact",
            "valuationImpact",
            "nextCheck"
          ],
          "suggestion": "把最新事件更新为「Spectrum-X + MRC 把以太网推向 AI 工厂训练网络，强化 NVIDIA 系统级平台位置」；业务影响写入：对业务的影响主要落在 Data Center 平台化与网络产品线。AI 训练集群越大，瓶颈越容易从单颗 GPU 转向网络、互连、调度和系统可靠性。Spectrum-X + MRC 的价值在于把网络从普通数据中心配套，变成大模型训练效率的一部分。如果客户认可这套能力，NVIDIA 在 AI 数据中心 capex 中的可服务范围会从 GPU 扩展到网络 fabric、系统软件和整机方案，提升平台粘性与交叉销售空间。；估值/动作写入：估值上，这条事件支持 NVIDIA 享有系统级平台溢价，而不只是芯片周"
        },
        {
          "target": "公司理解",
          "fields": [
            "businessMap",
            "positioning",
            "moatDetail"
          ],
          "suggestion": "对业务的影响主要落在 Data Center 平台化与网络产品线。AI 训练集群越大，瓶颈越容易从单颗 GPU 转向网络、互连、调度和系统可靠性。Spectrum-X + MRC 的价值在于把网络从普通数据中心配套，变成大模型训练效率的一部分。如果客户认可这套能力，NVIDIA 在 AI 数据中心 capex 中的可服务范围会从 GPU 扩展到网络 fabric、系统软件和整机方案，提升平台粘性与交叉销售空间。"
        },
        {
          "target": "财务数据地图",
          "fields": [
            "financeMap",
            "financials"
          ],
          "suggestion": "如果事件包含收入、利润率、现金流、capex、订单或 backlog 数字，应把关键数字进入财务表格，并解释它改变了哪条财务判断。"
        },
        {
          "target": "估值模型",
          "fields": [
            "valuationModel",
            "valuationFrame"
          ],
          "suggestion": "估值上，这条事件支持 NVIDIA 享有系统级平台溢价，而不只是芯片周期股估值。它能强化“AI 工厂平台公司”的中长期叙事，尤其是当 OpenAI、Microsoft、Oracle 这类客户把训练效率和网络可靠性视为刚需时。不过它还不是单独加仓触发器，因为文章没有披露 Spectrum-X 收入规模、毛利率、客户采购金额或独立订单。动作上维持 A 池核心，研究优先级上调到“AI 网络平台化验证”，仓位动作仍等待财报和客户部署数据验证。"
        }
      ],
      "reason": "这是一条 P1 级平台化强化事件。它没有直接改变下一季收入指引，但强化了一个更重要的判断：NVIDIA 的竞争力正在从 GPU 芯片龙头，继续外溢到 AI 工厂的网络、系统协同和训练效率层。也就是说，NVIDIA 在争夺的不只是芯片预算，而是超大规模 AI 基础设施的系统控制点。",
      "valuation_impact": "估值上，这条事件支持 NVIDIA 享有系统级平台溢价，而不只是芯片周期股估值。它能强化“AI 工厂平台公司”的中长期叙事，尤其是当 OpenAI、Microsoft、Oracle 这类客户把训练效率和网络可靠性视为刚需时。不过它还不是单独加仓触发器，因为文章没有披露 Spectrum-X 收入规模、毛利率、客户采购金额或独立订单。动作上维持 A 池核心，研究优先级上调到“AI 网络平台化验证”，仓位动作仍等待财报和客户部署数据验证。",
      "next_verification": [
        "下一次 NVIDIA 财报和电话会中，重点看 Data Center 收入、网络产品相关表述、毛利率，以及管理层是否单独强调 Spectrum-X / networking adoption。",
        "跟踪 OpenAI、Microsoft Fairwater、Oracle OCI Abilene 等客户后续是否继续公开提到 Spectrum-X、MRC 或 Blackwell 集群网络效率。",
        "观察 MRC 通过 Open Compute Project 开放后，是扩大 NVIDIA 网络生态影响力，还是让协议层被行业通用化并削弱硬件差异。"
      ],
      "detail_link": "./event.html?company=nvidia&event=1&return=company&v=20260505-1",
      "sort_key": 20260506
    },
    {
      "company": "nvidia",
      "company_name": "NVIDIA",
      "event_index": 2,
      "event_title": "ServiceNow Project Arc 与 OpenShell 合作验证 NVIDIA 企业 Agent 栈从模型走向安全执行层",
      "event_date": "2026-05-05",
      "priority": "P2",
      "direction": "中性验证",
      "trigger_type": "维持观察",
      "status": "needs_model_update",
      "quality": "可自动生成回写建议",
      "update_targets": [
        "当前结论",
        "公司理解",
        "财务数据地图",
        "估值模型"
      ],
      "recommended_updates": [
        {
          "target": "当前结论",
          "fields": [
            "latestEvent",
            "businessImpact",
            "valuationImpact",
            "nextCheck"
          ],
          "suggestion": "把最新事件更新为「ServiceNow Project Arc 与 OpenShell 合作验证 NVIDIA 企业 Agent 栈从模型走向安全执行层」；业务影响写入：业务影响主要落在企业 AI 软件生态、推理需求和 AI 工厂运行时。ServiceNow 本身拥有大量企业 IT 和 workflow 场景，Project Arc 如果能进入真实工作流，会把 agent 从“演示级应用”推进到“受治理的企业执行系统”。NVIDIA 通过 OpenShell、agent skills 和 AI-Q Blueprint 进入这一层，有助于把底层加速计算与上层企业应用连接起来。不过当前仍偏生态和产品合作，离可量化收入贡献还有距离。；估值"
        },
        {
          "target": "公司理解",
          "fields": [
            "businessMap",
            "positioning",
            "moatDetail"
          ],
          "suggestion": "业务影响主要落在企业 AI 软件生态、推理需求和 AI 工厂运行时。ServiceNow 本身拥有大量企业 IT 和 workflow 场景，Project Arc 如果能进入真实工作流，会把 agent 从“演示级应用”推进到“受治理的企业执行系统”。NVIDIA 通过 OpenShell、agent skills 和 AI-Q Blueprint 进入这一层，有助于把底层加速计算与上层企业应用连接起来。不过当前仍偏生态和产品合作，离可量化收入贡献还有距离。"
        },
        {
          "target": "财务数据地图",
          "fields": [
            "financeMap",
            "financials"
          ],
          "suggestion": "如果事件包含收入、利润率、现金流、capex、订单或 backlog 数字，应把关键数字进入财务表格，并解释它改变了哪条财务判断。"
        },
        {
          "target": "估值模型",
          "fields": [
            "valuationModel",
            "valuationFrame"
          ],
          "suggestion": "估值上，这条事件支持 NVIDIA 的软件/生态可选项，但权重应低于数据中心 GPU、网络和主权 AI 超算这类更直接的收入驱动。它对估值的贡献主要是提高长期平台想象力，而不是立即改变盈利预测。动作上不作为单独买入触发，维持观察；只有当 ServiceNow 或更多企业软件平台把 NVIDIA runtime、skills、blueprints 纳入生产部署，并带来可见推理需求或软件收入时，才上调其在估值模型中的权重。"
        }
      ],
      "reason": "这是一条 P2 级生态验证事件。它没有披露收入金额或客户规模，所以不能直接推升短期估值；但它说明 NVIDIA 的企业 AI 布局正在从算力和模型，延伸到 agent 安全执行、运行时、技能库和企业工作流集成。这对 NVIDIA 的长期意义在于：如果企业 agent 真正进入生产环境，GPU 消耗、推理 tokenomics、软件栈和开发者生态会形成更深绑定",
      "valuation_impact": "估值上，这条事件支持 NVIDIA 的软件/生态可选项，但权重应低于数据中心 GPU、网络和主权 AI 超算这类更直接的收入驱动。它对估值的贡献主要是提高长期平台想象力，而不是立即改变盈利预测。动作上不作为单独买入触发，维持观察；只有当 ServiceNow 或更多企业软件平台把 NVIDIA runtime、skills、blueprints 纳入生产部署，并带来可见推理需求或软件收入时，才上调其在估值模型中的权重。",
      "next_verification": [
        "跟踪 ServiceNow Project Arc 是否从发布进入实际客户部署，尤其是付费客户数量、使用场景和运行规模。",
        "观察 OpenShell 是否被更多企业软件厂商或开发者采用，是否成为 enterprise agent execution 的通用基础。",
        "下一次 NVIDIA 财报中关注软件、推理、enterprise AI 或 agent 相关口径是否更具体。"
      ],
      "detail_link": "./event.html?company=nvidia&event=2&return=company&v=20260505-1",
      "sort_key": 20260505
    },
    {
      "company": "tsmc",
      "company_name": "TSMC",
      "event_index": 1,
      "event_title": "A13、A12、N2U 与先进封装路线同步披露，TSMC 把 2028-2029 年 AI/HPC 制程平台继续前推",
      "event_date": "2026-04-23",
      "priority": "P1",
      "direction": "正向强化",
      "trigger_type": "维持核心并观察加仓条件",
      "status": "needs_model_update",
      "quality": "可自动生成回写建议",
      "update_targets": [
        "当前结论",
        "公司理解",
        "财务数据地图",
        "估值模型"
      ],
      "recommended_updates": [
        {
          "target": "当前结论",
          "fields": [
            "latestEvent",
            "businessImpact",
            "valuationImpact",
            "nextCheck"
          ],
          "suggestion": "把最新事件更新为「A13、A12、N2U 与先进封装路线同步披露，TSMC 把 2028-2029 年 AI/HPC 制程平台继续前推」；业务影响写入：对业务层面，A13/A12/N2U 继续支撑先进逻辑节点升级，CoWoS/SoIC/SoW-X 和 COUPE 则把 TSMC 从单纯晶圆代工进一步推向 AI 系统级制造基础设施。对客户而言，AI 芯片未来瓶颈会同时出现在算力晶粒、HBM 集成、封装面积、芯片间互连和机架间传输效率，TSMC 同时覆盖这些环节，有助于提高客户迁移成本和平台黏性。车规 N2A/N3A 说明先进节点也在向 ADAS、自动驾驶和 Physical AI 扩散，但这部分更偏中长期，不能立刻折算成收入。；估值/"
        },
        {
          "target": "公司理解",
          "fields": [
            "businessMap",
            "positioning",
            "moatDetail"
          ],
          "suggestion": "对业务层面，A13/A12/N2U 继续支撑先进逻辑节点升级，CoWoS/SoIC/SoW-X 和 COUPE 则把 TSMC 从单纯晶圆代工进一步推向 AI 系统级制造基础设施。对客户而言，AI 芯片未来瓶颈会同时出现在算力晶粒、HBM 集成、封装面积、芯片间互连和机架间传输效率，TSMC 同时覆盖这些环节，有助于提高客户迁移成本和平台黏性。车规 N2A/N3A 说明先进节点也在向 ADAS、自动驾驶和 Physical AI 扩散，但这部分更偏中长期，不能立刻折算成收入。"
        },
        {
          "target": "财务数据地图",
          "fields": [
            "financeMap",
            "financials"
          ],
          "suggestion": "如果事件包含收入、利润率、现金流、capex、订单或 backlog 数字，应把关键数字进入财务表格，并解释它改变了哪条财务判断。"
        },
        {
          "target": "估值模型",
          "fields": [
            "valuationModel",
            "valuationFrame"
          ],
          "suggestion": "估值上，这条事件不应该被理解为短期买入触发，而是提高 TSMC 长期估值中枢的质量证据。它支持给先进制程和先进封装更高的持续性权重，因为增长来源从 N2/A14 单一节点扩展到 A13/A12、CoWoS、SoIC、CPO 和车规/机器人场景。但由于核心生产时间多在 2028-2029 年，当前动作应是维持核心跟踪，不因技术路线发布直接加仓；后续需要用 capex、客户采用、CoWoS 产能、HPC 收入占比和毛利率来验证这些路线是否兑现为利润。"
        }
      ],
      "reason": "这条事件强化了 TSMC 的长期核心逻辑：AI/HPC 对制程、封装、互连和系统集成的要求越来越高，TSMC 的竞争位置不只是“谁能做更小节点”，而是能否持续提供从先进逻辑到 CoWoS/SoIC/CPO 的完整制造平台。短期它不直接改变下一季收入，但它提高了对 2028-2029 年高端制程和先进封装景气延续的可见度。",
      "valuation_impact": "估值上，这条事件不应该被理解为短期买入触发，而是提高 TSMC 长期估值中枢的质量证据。它支持给先进制程和先进封装更高的持续性权重，因为增长来源从 N2/A14 单一节点扩展到 A13/A12、CoWoS、SoIC、CPO 和车规/机器人场景。但由于核心生产时间多在 2028-2029 年，当前动作应是维持核心跟踪，不因技术路线发布直接加仓；后续需要用 capex、客户采用、CoWoS 产能、HPC 收入占比和毛利率来验证这些路线是否兑现为利润。",
      "next_verification": [
        "下一次财报继续看 HPC 占比、先进制程需求、毛利率和资本开支指引，判断技术路线是否正在转化为当期订单和盈利质量。",
        "跟踪 CoWoS 产能扩张、HBM 集成需求和大客户 AI 芯片路线，验证 14 倍光罩尺寸 CoWoS、SoIC 与 CPO 是否成为 AI 芯片平台的关键瓶颈资源。",
        "跟踪 2028-2029 年 A14/A13/A12 量产节奏、良率和主要客户采用情况，避免把路线图发布直接等同于商业成功。"
      ],
      "detail_link": "./event.html?company=tsmc&event=1&return=company&v=20260505-1",
      "sort_key": 20260423
    },
    {
      "company": "nvidia",
      "company_name": "NVIDIA",
      "event_index": 3,
      "event_title": "Google Cloud 合作把 Rubin、Blackwell、Nemotron 与物理 AI 推向云端生产平台",
      "event_date": "2026-04-22",
      "priority": "P1",
      "direction": "正向强化",
      "trigger_type": "维持核心并观察加仓条件",
      "status": "needs_model_update",
      "quality": "可自动生成回写建议",
      "update_targets": [
        "当前结论",
        "公司理解",
        "财务数据地图",
        "估值模型"
      ],
      "recommended_updates": [
        {
          "target": "当前结论",
          "fields": [
            "latestEvent",
            "businessImpact",
            "valuationImpact",
            "nextCheck"
          ],
          "suggestion": "把最新事件更新为「Google Cloud 合作把 Rubin、Blackwell、Nemotron 与物理 AI 推向云端生产平台」；业务影响写入：对业务层面，这条合作强化了 NVIDIA Data Center 的系统级粘性。Rubin / Blackwell 是算力底座，ConnectX / NVLink / Virgo networking 是集群扩展路径，Nemotron / NeMo / Gemini Enterprise 是 agentic AI 的开发入口，Omniverse / Isaac / Cosmos 是物理 AI 和工业场景入口。Google Cloud 作为超大云平台，把这些能力产品化后，企业客户买到的不"
        },
        {
          "target": "公司理解",
          "fields": [
            "businessMap",
            "positioning",
            "moatDetail"
          ],
          "suggestion": "对业务层面，这条合作强化了 NVIDIA Data Center 的系统级粘性。Rubin / Blackwell 是算力底座，ConnectX / NVLink / Virgo networking 是集群扩展路径，Nemotron / NeMo / Gemini Enterprise 是 agentic AI 的开发入口，Omniverse / Isaac / Cosmos 是物理 AI 和工业场景入口。Google Cloud 作为超大云平台，把这些能力产品化后，企业客户买到的不只是单颗 GPU，而是一套从训练、推理、机密计算、强化学习、数字孪生到机器人仿真的云端 AI 工厂。这会提高 NVIDIA 在云厂商资本开支、企业 A"
        },
        {
          "target": "财务数据地图",
          "fields": [
            "financeMap",
            "financials"
          ],
          "suggestion": "如果事件包含收入、利润率、现金流、capex、订单或 backlog 数字，应把关键数字进入财务表格，并解释它改变了哪条财务判断。"
        },
        {
          "target": "估值模型",
          "fields": [
            "valuationModel",
            "valuationFrame"
          ],
          "suggestion": "估值上，这条事件支持 NVIDIA 高估值中的“平台溢价”部分，但不应该被当成短期追买触发。正面是：Rubin A5X 给出 10 倍成本/能效指标、最大 96 万 GPU 多站点扩展、OpenAI 与 Thinking Machines 等真实工作负载案例，说明 NVIDIA 的平台价值正在从训练延伸到推理、agentic AI 和 physical AI。限制是：这些多数是平台发布、预览或合作扩展，短期收入兑现仍要回到 Google Cloud 与其他云厂商 capex、Rubin 量产节奏、Blackwell / GB300 供给、推理需求和毛利率。当前动作是维持 A 池核心并上调研究优先级，而不是因为合作新闻单独加仓。"
        }
      ],
      "reason": "这是 P1 级别的平台化强化事件。它不直接改变下一季收入指引，但非常清楚地说明 NVIDIA 的竞争边界正在从“卖 GPU 给云厂商”扩大到“和云厂商共同定义 AI 工厂的算力、网络、机密计算、模型工具链和物理 AI 开发环境”。这也回应了我们此前的问题：AI 芯片公司与 AI 工厂平台公司的差别，不是有没有更强芯片，而是能否把芯片、网络、系统、软件、模型工",
      "valuation_impact": "估值上，这条事件支持 NVIDIA 高估值中的“平台溢价”部分，但不应该被当成短期追买触发。正面是：Rubin A5X 给出 10 倍成本/能效指标、最大 96 万 GPU 多站点扩展、OpenAI 与 Thinking Machines 等真实工作负载案例，说明 NVIDIA 的平台价值正在从训练延伸到推理、agentic AI 和 physical AI。限制是：这些多数是平台发布、预览或合作扩展，短期收入兑现仍要回到 Google Cloud 与其他云厂商 capex、",
      "next_verification": [
        "下一次 NVIDIA 财报继续看 Data Center 收入、毛利率、推理需求口径，以及 Rubin / Blackwell / GB300 供给节奏是否支撑平台化兑现。",
        "跟踪 Google Cloud A5X 的实际推出时间、客户采用、定价和可用区域，验证 80,000 / 960,000 GPU 扩展能力是否从发布口径走向真实部署。",
        "跟踪 OpenAI、Thinking Machines、CrowdStrike、Siemens/Cadence 等客户案例是否带来可重复的高价值工作负载，而不只是发布会引用。"
      ],
      "detail_link": "./event.html?company=nvidia&event=3&return=company&v=20260505-1",
      "sort_key": 20260422
    },
    {
      "company": "tsmc",
      "company_name": "TSMC",
      "event_index": 4,
      "event_title": "2026 年 3 月营收环比反弹 30.7%，Q1 累计同比 35.1%，先进制程需求仍处高位",
      "event_date": "2026-04-10",
      "priority": "P1",
      "direction": "正向强化",
      "trigger_type": "维持核心并观察加仓条件",
      "status": "needs_model_update",
      "quality": "可自动生成回写建议",
      "update_targets": [
        "当前结论",
        "公司理解",
        "财务数据地图",
        "估值模型"
      ],
      "recommended_updates": [
        {
          "target": "当前结论",
          "fields": [
            "latestEvent",
            "businessImpact",
            "valuationImpact",
            "nextCheck"
          ],
          "suggestion": "把最新事件更新为「2026 年 3 月营收环比反弹 30.7%，Q1 累计同比 35.1%，先进制程需求仍处高位」；业务影响写入：业务影响主要落在先进制程、高性能计算和 AI 相关晶圆需求。月度营收无法拆分 3nm/5nm/HPC，但 Q1 财报已显示先进制程占晶圆收入 74%、HPC 占净收入 61%。因此 3 月营收的强劲反弹更像是对领先制程需求强度的高频验证，而不是独立的新业务线变化。；估值/动作写入：估值上，这条事件支持维持 TSMC 的高质量制造平台溢价：收入增长仍强，且与 Q1 高毛利率、高先进制程占比相互验证。但它不是单独加仓触发器，因为月度营收只验证收入端，不验证毛利率、capex 回报和海外扩产成本。动作上维持 A"
        },
        {
          "target": "公司理解",
          "fields": [
            "businessMap",
            "positioning",
            "moatDetail"
          ],
          "suggestion": "业务影响主要落在先进制程、高性能计算和 AI 相关晶圆需求。月度营收无法拆分 3nm/5nm/HPC，但 Q1 财报已显示先进制程占晶圆收入 74%、HPC 占净收入 61%。因此 3 月营收的强劲反弹更像是对领先制程需求强度的高频验证，而不是独立的新业务线变化。"
        },
        {
          "target": "财务数据地图",
          "fields": [
            "financeMap",
            "financials"
          ],
          "suggestion": "如果事件包含收入、利润率、现金流、capex、订单或 backlog 数字，应把关键数字进入财务表格，并解释它改变了哪条财务判断。"
        },
        {
          "target": "估值模型",
          "fields": [
            "valuationModel",
            "valuationFrame"
          ],
          "suggestion": "估值上，这条事件支持维持 TSMC 的高质量制造平台溢价：收入增长仍强，且与 Q1 高毛利率、高先进制程占比相互验证。但它不是单独加仓触发器，因为月度营收只验证收入端，不验证毛利率、capex 回报和海外扩产成本。动作上维持 A 池核心，继续等待 Q2 指引和后续月度营收确认高增长能否延续。"
        }
      ],
      "reason": "这是一条 P1 级强化事件。3 月数据说明 TSMC 的高增长不是只靠某个单月，2 月季节性回落后 3 月迅速修复，Q1 累计同比达到 35.1%。对长期跟踪而言，月度营收继续支持 AI/HPC 和先进制程需求处于高景气。",
      "valuation_impact": "估值上，这条事件支持维持 TSMC 的高质量制造平台溢价：收入增长仍强，且与 Q1 高毛利率、高先进制程占比相互验证。但它不是单独加仓触发器，因为月度营收只验证收入端，不验证毛利率、capex 回报和海外扩产成本。动作上维持 A 池核心，继续等待 Q2 指引和后续月度营收确认高增长能否延续。",
      "next_verification": [
        "继续跟踪 4 月、5 月、6 月营收，判断 Q2 是否能沿着管理层 US$39.0-40.2 billion 指引运行。",
        "结合 Q2 财报验证高营收是否转化为 65.5%-67.5% 毛利率区间，而不是被海外扩产或折旧稀释。",
        "观察 HPC/AI 需求是否继续支撑先进制程占比，尤其是 3nm、5nm 和 CoWoS 供需。"
      ],
      "detail_link": "./event.html?company=tsmc&event=4&return=company&v=20260505-1",
      "sort_key": 20260410
    },
    {
      "company": "constellation",
      "company_name": "Constellation Energy",
      "event_index": 0,
      "event_title": "2026 Outlook 给出 Base EPS 高增长目标，把公司定位推向成长型电力平台",
      "event_date": "2026-03-31",
      "priority": "P1",
      "direction": "正向强化",
      "trigger_type": "上调研究优先级",
      "status": "needs_model_update",
      "quality": "可自动生成回写建议",
      "update_targets": [
        "当前结论",
        "公司理解",
        "财务数据地图",
        "估值模型",
        "跟踪重点与风险"
      ],
      "recommended_updates": [
        {
          "target": "当前结论",
          "fields": [
            "latestEvent",
            "businessImpact",
            "valuationImpact",
            "nextCheck"
          ],
          "suggestion": "把最新事件更新为「2026 Outlook 给出 Base EPS 高增长目标，把公司定位推向成长型电力平台」；业务影响写入：这条动态把 Constellation 的业务定位讲清楚了：它不是普通电力公用事业，也不只是核电资产持有人。核电提供清洁、稳定、可调度的底座；Calpine 带来天然气、地热和更大商业平台；长期供电协议把这些资产卖给数据中心、工业客户和大企业。AI 数据中心需要的是长周期、稳定、可用且越来越偏低碳的电力，Constellation 正好处在这个需求交汇点上。；估值/动作写入：估值上，正面是 20%+ Base EPS 增长目标、147 million MWh 可签约核电电量、50 亿美元回购和 55GW 稀缺"
        },
        {
          "target": "公司理解",
          "fields": [
            "businessMap",
            "positioning",
            "moatDetail"
          ],
          "suggestion": "这条动态把 Constellation 的业务定位讲清楚了：它不是普通电力公用事业，也不只是核电资产持有人。核电提供清洁、稳定、可调度的底座；Calpine 带来天然气、地热和更大商业平台；长期供电协议把这些资产卖给数据中心、工业客户和大企业。AI 数据中心需要的是长周期、稳定、可用且越来越偏低碳的电力，Constellation 正好处在这个需求交汇点上。"
        },
        {
          "target": "财务数据地图",
          "fields": [
            "financeMap",
            "financials"
          ],
          "suggestion": "如果事件包含收入、利润率、现金流、capex、订单或 backlog 数字，应把关键数字进入财务表格，并解释它改变了哪条财务判断。"
        },
        {
          "target": "估值模型",
          "fields": [
            "valuationModel",
            "valuationFrame"
          ],
          "suggestion": "估值上，正面是 20%+ Base EPS 增长目标、147 million MWh 可签约核电电量、50 亿美元回购和 55GW 稀缺资产平台，说明市场把它从传统公用事业重估为成长型电力平台有逻辑。压力是短期 2026 adjusted operating EPS 指引需要兑现，39 亿美元 growth capex 必须产生足够回报，Calpine 整合和监管资产处置不能拖累现金流。当前动作是维持核心跟踪，但不因主题热度追价，要等合同溢价、EPS 和自由现金流继续验证。"
        },
        {
          "target": "跟踪重点与风险",
          "fields": [
            "focus",
            "trackingGuide",
            "risk"
          ],
          "suggestion": "2026 adjusted operating EPS 是否落在 11.00-12.00 美元区间，后续是否上修。；147 million MWh 年度可用核电电量能否签出高质量长期合同，并体现溢价。；Calpine 整合后天然气、地热和商业平台是否带来 EPS 与自由现金流增厚。"
        }
      ],
      "reason": "这是 P1 级别的战略与财务框架更新。它强化了 Constellation 的长期逻辑：稳定、清洁、可调度电力正在变成 AI 数据中心、电气化和能源安全周期中的稀缺资产。但这不是无脑利好。2026 adjusted operating EPS 指引 11-12 美元只是起点，市场更关心 20%+ Base EPS 增长能否兑现、147 million MWh",
      "valuation_impact": "估值上，正面是 20%+ Base EPS 增长目标、147 million MWh 可签约核电电量、50 亿美元回购和 55GW 稀缺资产平台，说明市场把它从传统公用事业重估为成长型电力平台有逻辑。压力是短期 2026 adjusted operating EPS 指引需要兑现，39 亿美元 growth capex 必须产生足够回报，Calpine 整合和监管资产处置不能拖累现金流。当前动作是维持核心跟踪，但不因主题热度追价，要等合同溢价、EPS 和自由现金流继续验证。",
      "next_verification": [
        "2026 adjusted operating EPS 是否落在 11.00-12.00 美元区间，后续是否上修。",
        "147 million MWh 年度可用核电电量能否签出高质量长期合同，并体现溢价。",
        "Calpine 整合后天然气、地热和商业平台是否带来 EPS 与自由现金流增厚。"
      ],
      "detail_link": "./event.html?company=constellation&event=0&return=company&v=20260505-1",
      "sort_key": 20260331
    }
  ],
  "summary": {
    "total": 8,
    "ready": 0,
    "needs_model_update": 8,
    "blocked": 0,
    "companies": 3
  }
};
