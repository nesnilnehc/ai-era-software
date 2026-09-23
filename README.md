<!-- 本文件由 meta/build.py 生成，改这里会在下次构建时被覆盖。怎么改见下方「怎么加一条」。 -->

# AI 重构软件 · 一手材料清单

收集「软件本身因 AI 被怎样改写」的一手材料：论文、厂商文档与公告、标准文件、分析与投资机构的公开报告、社区维护的清单。为每份材料提供简明、基于原文事实的摘要和收录理由：摘要帮助读者快速了解内容，收录理由说明该材料具体如何符合本仓收录范围；两者均不写评论与评价。

不收录仅讨论模型能力、与软件形态无关的产品新闻，或没有可追溯原始出处的二手转述。

**正式收录须同时通过三道门**：①范围——材料直接呈现 AI 对软件界面与接入、内部功能、开发构造、安全、运行治理、协议生态或商业组织的改变；仅在软件中调用模型或给现有工具加接口不够。②来源与证据——一手原文可访问并核实关键事实；按材料类型参考出品方的相关资质、作者专业背景、其对所述内容的直接责任，以及方法、数据、代码和测试的可检查程度。权威性用于判断证据强度和主张边界，不能仅凭机构名头收录；个人或社区材料也可凭可检查的实现、测试或可复现数据通过。厂商自述可证明其公开了某项产品或实践，不能单独证明其效果优越。材料还须包含一种可检查的实质内容：架构/协议/规范、具体实现、带方法与数据的实证结果、明确的工程实践或治理规则、或有方法与数据的调研。③增量价值——相较目录现有材料，提供具体新增的对象、机制、实践或证据；薄层封装、单一工具连接器、缺少技术细节的产品宣告、重复汇编不通过。任一道不通过或无法判断，先记入候选，不进入正式目录。

## 怎么用

- **要数据**：[`index.tsv`](index.tsv)，148 条 × 11 列，制表符分隔。列为 首发日期／最后更新／标题／出品方／体裁／出品方类型／主题／标签／出处／摘要／收录理由；主题与标签列内用 `|` 分隔多值，标签同时含英文正名与中文别名，两种写法都能 grep。

- **要翻看**：本页下方的[清单表](#清单按发布时间倒序)，按首发时间倒序。

- **要原文**：跑 [`fetch.sh`](fetch.sh)，按清单把原件下载到本地 `originals/`（已在 .gitignore 里）。取不到的会逐条报出来。

- **要加条目**：改 [`meta/catalog.py`](meta/catalog.py)；**要改判据**：改 [`meta/policy.py`](meta/policy.py)。完成后跑 `python3 meta/build.py`。

[清单](#清单按发布时间倒序) · [分类口径](#怎么分类) · [原文副本](#关于原文副本) · [添加条目](#怎么加一条) · [许可](#许可)

常用检索：

```sh
rg 'MCP' index.tsv
rg '商业与组织' index.tsv
```

**抓取记录最近更新：2026-09-23**——140／148 条有与当前出处一致的抓取记录，其余 8 条只给链接。各条的实际抓取日期见 [`meta/fetched.tsv`](meta/fetched.tsv)。

**内容摘要：146／148 条已核实补齐**——摘要只概括原文事实，不含评价。

以下条目暂不提供摘要：

- [AI Isn't Going to "Eat" Software: Agentic AI Needs the Authoritative Data and Rules Inside Enterprise Apps](https://my.idc.com/getdoc.jsp?containerId=US54377825)：IDC 报告全文需要登录，当前只能看到落地页，无法据原文核实摘要。
- [ISO/IEC 42001:2023 — Information technology, Artificial intelligence, Management system](https://www.iso.org/standard/42001)：ISO 页面版权条款禁止将受版权保护内容用于 AI 生成回答。

## 清单（按发布时间倒序）

| 日期 | 材料 | 出品方 | 分类 |
|---|---|---|---|
| 2026-09-22 | [MCP Bastion](https://github.com/Matthew0822/MCPBastion)<br>文档 · 个人<br>摘要：提供本地 MCP 消息网关，按策略允许、拒绝或脱敏工具调用，并记录审计事件；仓库说明其只处理 stdio JSON-RPC 消息，不负责传输桥接或服务器启动。<br>收录理由：它把策略控制和审计放到 MCP 工具调用路径中，具体呈现了智能体接入软件工具时的运行安全设计。 | Matthew0822 | **主题** `安全与攻防` `协议与生态`<br>**标签** `MCP` `authorization` `身份与授权` `observability` `可观测` |
| 2026-09-20 → 2026-09-21 | [ZCode](https://github.com/zai-org/ZCode)<br>文档 · 厂商<br>摘要：提供 AI 编程工作台，包含桌面应用、浏览器界面和终端 Agent；仓库包含客户端、后端、共享 UI 以及 Agent CLI 与运行时源码。<br>收录理由：项目将编程 Agent 作为桌面、浏览器和终端工作台的核心能力，具体体现 AI 对软件开发工具形态与交互入口的改变。 | Z.ai | **主题** `构造方式`<br>**标签** `orchestration` `编排` |
| 2026-09-19 | [Jev Security Scan](https://github.com/win4r/jev-security-scan)<br>文档 · 个人<br>摘要：扫描 Agent Skill、MCP 配置与源码中的提示注入、凭据读取、非预期外传和动态执行等行为，输出文件位置、脱敏证据、风险类别及未扫描范围；本地模式不联网，且不执行目标代码。<br>收录理由：该工具把 Agent Skill 和 MCP 代码的安全检查纳入安装或运行前流程，直接对应 AI 开发工具链的安全保障变化。 | win4r | **主题** `安全与攻防`<br>**标签** `MCP` `risk-framework` `风险框架` |
| 2026-09-18 | [网络安全标准实践指南——智能体系统开发安全指南（征求意见稿 v1.0-202609）](https://www.tc260.org.cn/tc260/tzgg/202609/e5b82ae7aca244d19d36b39575cbb458.shtml) ⚠<br>规范 · 标准组织<br>摘要：该征求意见稿旨在为智能体系统的安全开发提供实践指引，通知说明其面向社会公开征求意见。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制、AI 接入软件能力或用户界面的具体方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | 全国网络安全标准化技术委员会 | **主题** `安全与攻防` `界面与接入`<br>**标签** `regulation` `法规` |
| 2026-09-18 → 2026-09-23 | [agent-chaperone](https://github.com/agent-chaperone/agent-chaperone)<br>文档 · 个人<br>摘要：提供 MCP 代理和客户端 Hook，在工具调用执行前及结果交给智能体前进行筛查，并将概率判断、策略阈值和审计记录写入本地日志；仓库附有公开基准和人工标注集的评测结果。<br>收录理由：项目在 Agent 与工具之间加入可配置筛查、运行日志和评测机制，呈现智能体软件的安全控制如何进入实际开发与运行流程。 | agent-chaperone | **主题** `安全与攻防` `运行与问责`<br>**标签** `MCP` `observability` `可观测` |
| 2026-09-16 | [Characterizing Network Centralization and Observability in the Remote MCP Ecosystem](https://arxiv.org/abs/2609.19100)<br>论文 · 学界<br>摘要：通过目录元数据、被动合规信号和实时漏洞分析研究远程 MCP 生态的网络结构与可观测性。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进、AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | University of Calgary | **主题** `协议与生态` `运行与问责`<br>**标签** `MCP` `empirical-study` `实证测量` |
| 2026-09-16 | [Why We Post-Trained Our Own Reasoning Model (Koa)](https://www.salesforce.com/news/stories/why-we-post-trained-our-own-reasoning-model/)<br>文章 · 厂商<br>摘要：Salesforce 介绍为企业工作训练 Koa 推理模型的原因、后训练流程及其与通用模型的区别。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Salesforce | **主题** `构造方式`<br>**标签** `tool-interface` `工具接口` |
| 2026-09-15 | [Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)<br>文章 · 厂商<br>摘要：TypeSafe AI 介绍 System One 模型系列和 Jev，说明其面向软件自动化提供结构化决策输出。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 改变软件内部功能、流程或数据处理的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | TypeSafe AI | **主题** `构造方式` `应用内部`<br>**标签** `decision-model` `决策模型` `tool-interface` `工具接口` |
| 2026-09-15 | [Introduction — TypeSafe AI (Jev developer documentation)](https://docs.typesafe.ai/introduction)<br>文档 · 厂商<br>摘要：介绍 Jev API 的状态输入和类型化问题接口，以及供程序和编程智能体使用结构化回答的方式。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | TypeSafe AI | **主题** `构造方式`<br>**标签** `decision-model` `决策模型` `tool-interface` `工具接口` |
| 2026-09-15 | [Announcing Koa: Salesforce’s First CRM Reasoning Model, Built on NVIDIA Nemotron](https://www.salesforce.com/news/press-releases/2026/09/15/koa-reasoning-model/)<br>文章 · 厂商<br>摘要：Salesforce 与 NVIDIA 发布 Koa CRM 推理模型，说明其面向企业多步骤任务并基于 Salesforce 业务数据训练。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Salesforce | **主题** `构造方式`<br>**标签** `tool-interface` `工具接口` |
| 2026-09-14 | [Salesforce Koa: An Enterprise Language Model for Agentic Tool Use](https://arxiv.org/abs/2609.15066)<br>论文 · 厂商<br>摘要：介绍 Salesforce Koa 的模型构建方法，描述其以 Nemotron 基础模型为起点并通过强化学习适配企业工具使用。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Salesforce | **主题** `构造方式`<br>**标签** `tool-interface` `工具接口` |
| 2026-09-14 | [Authorization Architectures for Tool-Using AI Agents](https://arxiv.org/abs/2609.15906)<br>论文 · 产学合作<br>摘要：提出面向工具型 AI 智能体的授权架构，讨论如何将行动绑定到用户主体、权限范围和审计记录。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Westcliff University, University of the Cumberlands, Delta Air Lines, Georgia Institute of Technology | **主题** `安全与攻防`<br>**标签** `authorization` `身份与授权` `survey` `综述` |
| 2026-09-14 | [When Tool Calls Succeed but Workflows Fail: Anomalies at the Agent-Tool Boundary](https://arxiv.org/abs/2609.15397)<br>论文 · 厂商<br>摘要：研究重试、并发和部分失败时智能体工作流与外部工具状态不一致的情况，包括操作遗漏、重复及已取消操作残留。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | AVIV Group, independent researcher | **主题** `构造方式`<br>**标签** `tool-interface` `工具接口` |
| 2026-09-13 | [A Two-Dimensional Study of the Model Context Protocol: Publication and Adoption](https://arxiv.org/abs/2609.14721)<br>论文 · 学界<br>摘要：对 MCP 相关论文和 GitHub 仓库进行纵向统计，分析研究发表、开源采用及两者之间的关系。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Luxembourg Institute of Science and Technology, University of Luxembourg | **主题** `协议与生态`<br>**标签** `MCP` `empirical-study` `实证测量` |
| 2026-09-13 | [The Stochastic Deputy: Structural Tenant Isolation for Tool-Using LLM Agents](https://arxiv.org/abs/2609.14780)<br>论文 · 产学合作<br>摘要：提出结构化多租户隔离方法，将租户范围绑定到已验证凭据并在服务器侧强制执行，而不让模型自行选择租户标识。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Fandaqah, Heidelberg University | **主题** `安全与攻防`<br>**标签** `MCP` `authorization` `身份与授权` |
| 2026-09-12 | [Same Name, Different Server: A Security Census of Silent Drift in MCP](https://arxiv.org/abs/2609.14119)<br>论文 · 学界<br>摘要：对公开 MCP 注册表中的服务器及版本进行安全普查，研究同名服务器在版本间静默变化的情况。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进、AI 软件或智能体的威胁、安全控制与防护机制，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Texas Tech University | **主题** `协议与生态` `安全与攻防`<br>**标签** `MCP` `empirical-study` `实证测量` |
| 2026-09-10 | [Is Bash All You Need? An Empirical Study of Tool Interfaces for Enterprise Digital Worker Agents](https://arxiv.org/abs/2609.11999)<br>论文 · 产学合作<br>摘要：比较企业数字工作任务中的多种智能体工具接口，包括专用类型化工具与通用 shell。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 接入软件能力或用户界面的具体方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Microsoft, Carnegie Mellon University | **主题** `构造方式` `界面与接入`<br>**标签** `tool-interface` `工具接口` `benchmark` `基准评测` |
| 2026-09-05 | [Intent Drift at SME Scale: Deployment Practice, Not Model Capability, Determines Agentic Compliance](https://arxiv.org/abs/2609.05975)<br>论文 · 学界<br>摘要：提出适用于受监管小型企业的 Chain of Intent 治理框架，并通过模拟资产管理场景检验部署约束的执行情况。<br>收录理由：原文内容呈现AI 软件的运行治理、授权、监测或责任安排、AI 改变软件内部功能、流程或数据处理的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Hong Kong University of Science and Technology | **主题** `运行与问责` `应用内部`<br>**标签** `regulation` `法规` `empirical-study` `实证测量` |
| 2026-09-02 | [How we make AI coding more cost efficient without sacrificing task quality](https://github.blog/ai-and-ml/github-copilot/how-we-make-ai-coding-more-cost-efficient-without-sacrificing-task-quality/)<br>文章 · 厂商<br>摘要：GitHub 介绍 Copilot 编码 Agent 在工具输出压缩、提示词缩短和后台任务通知等方面的改动，并报告离线基准与线上实验的评估方法和结果。<br>收录理由：文章给出编码 Agent 的上下文管理、任务编排和评估实践，直接记录 AI 编程工具的工程实现如何变化。 | GitHub | **主题** `构造方式`<br>**标签** `orchestration` `编排` `empirical-study` `实证测量` |
| 2026-08-31 | [Delegation Without Trust: An Empirical Gap Analysis of Identity, Authorization, and Runtime](https://arxiv.org/abs/2609.00267)<br>论文 · 厂商<br>摘要：分析多智能体系统在身份、授权和运行时治理上的委托机制，并通过案例评估现有设计缺口。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制，与本仓记录 AI 如何改变软件开发的范围直接相关。 | VotalAI | **主题** `安全与攻防`<br>**标签** `authorization` `身份与授权` |
| 2026-08-25 | [Hybrid Semantic Tool Discovery for Enterprise MCP Gateway: Architecture and Implementation](https://arxiv.org/abs/2608.23992)<br>论文 · 厂商<br>摘要：提出企业 MCP 网关的混合语义工具发现架构，讨论如何在大量工具场景下兼顾上下文、认证、策略和可观测性。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进、AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | PayPal | **主题** `协议与生态` `构造方式`<br>**标签** `MCP` `context-engineering` `上下文工程` `tool-interface` `工具接口` |
| 2026-08-25 | [Model-Based Agentic Software Engineering](https://arxiv.org/abs/2608.25174)<br>论文 · 产学合作<br>摘要：提出 MAGE 理论框架，通过显式表示工程知识，并以约束、传感器、验证器和准入门控制智能体工作；研究基于一个纵向案例及六个工业案例的比较分析。<br>收录理由：研究直接讨论如何把工程知识、验证证据和权限约束纳入编码 Agent 的工作环境，属于 AI 改变软件工程流程与治理方式的一手研究。 | Purdue University; Amazon Robotics | **主题** `构造方式` `运行与问责`<br>**标签** `orchestration` `编排` `risk-framework` `风险框架` |
| 2026-08-22 | [From SQL Generation to Tool Selection: A Domain-Oriented Pattern for MCP Servers](https://arxiv.org/abs/2608.22063)<br>论文 · 个人<br>摘要：提出面向 MCP 服务器的领域工具模式：以封装业务规则的专用参数化工具替代模型运行时生成通用 SQL。<br>收录理由：原文内容呈现AI 接入软件能力或用户界面的具体方式、AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | No affiliation stated (Bartolomeo Bogliolo) | **主题** `界面与接入` `构造方式`<br>**标签** `MCP` `tool-interface` `工具接口` |
| 2026-08-19 | [Expanding Headless 360: Turning Enterprise Applications into Enterprise Capabilities](https://www.salesforce.com/news/stories/expanding-headless-360-enterprise-capabilities/)<br>文章 · 厂商<br>摘要：介绍 Salesforce Headless 360 将企业应用能力封装为可供获授权智能体发现和调用的接口。<br>收录理由：原文内容呈现AI 接入软件能力或用户界面的具体方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Salesforce | **主题** `界面与接入`<br>**标签** `headless` `无头化` |
| 2026-08-17 → 2026-08-18 | [Security Assessment of DeepSeek Harness with A.I.G: Evaluating Resistance to Indirect Prompt Injection](https://arxiv.org/abs/2608.16393)<br>论文 · 厂商<br>摘要：通过受控间接提示注入测试评估 DeepSeek Harness，分析不同内容通道、攻击方法和运行轨迹下的防护表现。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制、AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Tencent Zhuque Lab | **主题** `安全与攻防` `构造方式`<br>**标签** `tool-interface` `工具接口` `empirical-study` `实证测量` |
| 2026-08-13 → 2026-09-17 | [DeepSeek Harness: everything is a plugin](https://github.com/deepseek-ai/deepseek-harness)<br>文档 · 厂商<br>摘要：DeepSeek 开发的开源智能体运行框架，以插件架构组织功能；仓库说明当前处于开发预览阶段。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 接入软件能力或用户界面的具体方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | DeepSeek AI | **主题** `构造方式` `界面与接入`<br>**标签** `tool-interface` `工具接口` `orchestration` `编排` |
| 2026-07-28 | [Model Context Protocol Specification (version 2026-07-28)](https://modelcontextprotocol.io/specification/latest)<br>规范 · 标准组织<br>摘要：定义 Model Context Protocol 的客户端与服务器通信、消息模式、传输、授权及工具等协议机制。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Model Context Protocol | **主题** `协议与生态`<br>**标签** `MCP` |
| 2026-07 | [Apeiron: A Scalable LLM-agentic Framework for Autonomous Full-lifecycle Demand-optimized Application Synthesis](https://aclanthology.org/2026.findings-acl.188/)<br>论文 · 产学合作<br>摘要：提出用计算机操作智能体模拟用户需求、结合代码交互轨迹评估，并在持续交付中约束变更的应用合成框架；论文报告了多场景基准与用户研究结果。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Dartmouth College; Microsoft | **主题** `构造方式`<br>**标签** `benchmark` `基准评测` `empirical-study` `实证测量` |
| 2026-06-30 | [Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation](https://arxiv.org/abs/2607.02577)<br>论文 · 产学合作<br>摘要：对四类工具调用基准开展效度与复现性审计，并以专家复核任务比较评测器结果和人工判断。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | CoreThink AI, Stanford University | **主题** `构造方式`<br>**标签** `benchmark` `基准评测` |
| 2026-06-08 | [Understanding How Enterprises Adopt the Model Context Protocol for LLM-Driven Software Engineering](https://arxiv.org/abs/2606.09182)<br>论文 · 学界<br>摘要：通过实证研究分析企业在软件工程场景采用 MCP 的方式、部署挑战、运营风险和从业者经验。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进、AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | City University of Hong Kong, Hong Kong Metropolitan University | **主题** `协议与生态` `构造方式`<br>**标签** `MCP` `empirical-study` `实证测量` |
| 2026-06-03 | [The State Of Agentic AI In 2026 (public blog post)](https://www.forrester.com/blogs/the-state-of-agentic-ai-in-2026-companies-are-chasing-few-are-catching/)<br>文章 · 分析机构<br>摘要：Forrester 文章讨论企业智能体 AI 的采用和规模化之间的差距，并介绍报告对推广障碍的分析。<br>收录理由：原文内容呈现AI 对软件产品边界、商业模式或组织分工的影响，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Forrester | **主题** `商业与组织`<br>**标签** `market-data` `市场数据` |
| 2026-05-28 → 2026-08-10 | [On Effectiveness and Efficiency of Agentic Tool-calling and RL Training](https://arxiv.org/abs/2606.00135)<br>论文 · 产学合作<br>摘要：从评测有效性和训练效率两个角度研究智能体工具调用，分析评测流程及强化学习训练方法。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | LMU Munich, Munich Center for Machine Learning, University of Illinois Urbana-Champaign, Amazon, University of Sheffield | **主题** `构造方式`<br>**标签** `tool-interface` `工具接口` `benchmark` `基准评测` |
| 2026-05-28 | [Awesome Context Engineering (companion repo)](https://github.com/Meirtz/Awesome-Context-Engineering)<br>清单 · 学界<br>摘要：整理上下文工程相关方法、框架、工具、示例和研究资料，供构建 LLM 应用时查阅。<br>收录理由：原文内容呈现AI 改变软件内部功能、流程或数据处理的方式、AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Institute of Computing Technology CAS, et al. | **主题** `应用内部` `构造方式`<br>**标签** `context-engineering` `上下文工程` `curated-list` `资源清单` |
| 2026-05-18 | [Going Headless? On the Boundaries of Vertical AI Firms](https://arxiv.org/abs/2605.17812)<br>论文 · 产学合作<br>摘要：分析通用智能体将垂直软件中的工作流、领域逻辑和责任机制拆分后，对不同垂直 AI 企业边界的影响。<br>收录理由：原文内容呈现AI 接入软件能力或用户界面的具体方式、AI 对软件产品边界、商业模式或组织分工的影响、AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | University of Pittsburgh, Ensi.ai | **主题** `界面与接入` `商业与组织` `运行与问责`<br>**标签** `headless` `无头化` |
| 2026-05-13 | [ServiceNow opens its full system of action to every AI Agent in the enterprise (Action Fabric)](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-opens-its-full-system-of-action-to-every-AI-Agent-in-the-enterprise/default.aspx)<br>文章 · 厂商<br>摘要：ServiceNow 发布 Action Fabric，介绍让企业 AI 智能体连接并调用跨系统工作流与操作能力的方案。<br>收录理由：原文内容呈现AI 接入软件能力或用户界面的具体方式、AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | ServiceNow | **主题** `界面与接入` `运行与问责`<br>**标签** `headless` `无头化` |
| 2026-04-29 → 2026-05-02 | [The Buy-or-Build Decision, Revisited: How Agentic AI Changes the Economics of Enterprise Software](https://arxiv.org/abs/2604.26482)<br>论文 · 学界<br>摘要：从交易成本和资源基础等理论讨论智能体式 AI 如何改变企业软件的自建或采购决策。<br>收录理由：原文内容呈现AI 对软件产品边界、商业模式或组织分工的影响，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Stuttgart Media University | **主题** `商业与组织`<br>**标签** `buy-vs-build` `买还是自建` |
| 2026-04-28 | [Connecting Agents to Decisions](https://blog.palantir.com/connecting-agents-to-decisions-277dee8ddb40)<br>文章 · 厂商<br>摘要：文章介绍 Palantir Ontology 的决策中心架构，将企业数据、业务逻辑、行动及安全策略连接起来以供人员和智能体使用。<br>收录理由：原文内容呈现AI 接入软件能力或用户界面的具体方式、AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Palantir | **主题** `界面与接入` `运行与问责`<br>**标签** `ontology` `本体` `orchestration` `编排` |
| 2026-04-26 | [Infrastructure for the Agentic Web: Gap Analysis and Architecture from the Agentverse Platform](https://arxiv.org/abs/2606.20570)<br>论文 · 社区与非营利<br>摘要：分析 Agentverse 智能体云平台所需的基础设施，并提出面向智能体网络的架构组成。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | OpenHub Research | **主题** `协议与生态`<br>**标签** `empirical-study` `实证测量` `registry` `注册表` |
| 2026-04-17 → 2026-04-20 | [Integrating Graphs, Large Language Models, and Agents: Reasoning and Retrieval](https://arxiv.org/abs/2604.15951)<br>论文 · 学界<br>摘要：综述图结构、大语言模型与智能体在推理和信息检索中的结合方式，并归纳相关研究方向。<br>收录理由：原文内容呈现AI 改变软件内部功能、流程或数据处理的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Canadian Institute for Cybersecurity, University of New Brunswick | **主题** `应用内部`<br>**标签** `ontology` `本体` `RAG` `检索增强` `survey` `综述` |
| 2026-04-16 → 2026-08-26 | [Corpus2Skill: Distilling Enterprise Knowledge into Navigable Agent Skills for QA and RAG](https://arxiv.org/abs/2604.14572)<br>论文 · 厂商<br>摘要：提出将企业知识语料离线整理为层级技能目录、再由智能体逐层检索的问答与检索架构。<br>收录理由：原文内容呈现AI 改变软件内部功能、流程或数据处理的方式、AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Magellan Technology Research Institute | **主题** `应用内部` `构造方式`<br>**标签** `RAG` `检索增强` `context-engineering` `上下文工程` |
| 2026-04-02 → 2026-09-18 | [x402: a payments protocol for the internet, built on HTTP](https://github.com/coinbase/x402)<br>规范 · 厂商<br>摘要：定义一种基于 HTTP 的互联网支付标准，并提供让网站或服务按请求接收数字货币及法币支付的实现示例。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Coinbase | **主题** `协议与生态`<br>**标签** `payments` `支付` |
| 2026-04-01 → 2026-06-04 | [Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents](https://arxiv.org/abs/2604.00555)<br>论文 · 产学合作<br>摘要：介绍将神经网络与符号本体结合的企业智能体架构，用领域知识约束推理过程。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 改变软件内部功能、流程或数据处理的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Golden Gate University, Foundation AgenticOS, Novartis | **主题** `构造方式` `应用内部`<br>**标签** `ontology` `本体` |
| 2026-04 | [SAP API Policy v.4.2026a](https://help.sap.com/doc/sap-api-policy/latest/en-US/API_Policy_latest.pdf)<br>规范 · 厂商<br>摘要：规定 SAP API 的发布范围、调用限制和安全控制，并说明对自动化及生成式 AI 调用的适用边界。<br>收录理由：原文内容呈现AI 接入软件能力或用户界面的具体方式、AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | SAP | **主题** `界面与接入` `协议与生态`<br>**标签** `tool-interface` `工具接口` |
| 2026-03-26 | [From Logic Monopoly to Social Contract (working paper, not peer reviewed)](https://arxiv.org/abs/2603.25100)<br>论文 · 社区与非营利<br>摘要：工作论文讨论自主智能体经济中的权力分离和治理结构，并提出以制度安排应对多智能体系统风险。<br>收录理由：原文内容呈现AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | NetX Foundation | **主题** `运行与问责`<br>**标签** `risk-framework` `风险框架` |
| 2026-03-14 | [Awesome MCP Security: security scores for 800+ MCP servers](https://github.com/getagentseal/awesome-mcp-security)<br>清单 · 厂商<br>摘要：整理 MCP 服务器的安全评分和相关资源，覆盖项目 README 所列的 800 多个服务器。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制、AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Agentseal | **主题** `安全与攻防` `协议与生态`<br>**标签** `MCP` `curated-list` `资源清单` |
| 2026-03-02 | [Good news: AI Will Eat Application Software](https://a16z.com/good-news-ai-will-eat-application-software/)<br>文章 · 投资机构<br>摘要：文章讨论生成式 AI 对企业应用软件市场的影响，提出网络效应、品牌和专有数据等因素仍会参与竞争。<br>收录理由：原文内容呈现AI 对软件产品边界、商业模式或组织分工的影响，与本仓记录 AI 如何改变软件开发的范围直接相关。 | a16z | **主题** `商业与组织`<br>**标签** `headless` `无头化` |
| 2026-03 | [AI Isn't Going to "Eat" Software: Agentic AI Needs the Authoritative Data and Rules Inside Enterprise Apps](https://my.idc.com/getdoc.jsp?containerId=US54377825) ⚠<br>报告 · 分析机构<br>收录理由：原文内容呈现题名涉及智能体式 AI 与企业应用数据规则的关系；正文需登录，纳入依据限于可见落地页信息。，与本仓记录 AI 如何改变软件开发的范围直接相关。 | IDC | **主题** `商业与组织`<br>**标签** `headless` `无头化` |
| 2026-02-24 | [The Headless Firm: How AI Reshapes Enterprise Boundaries](https://arxiv.org/abs/2602.21401)<br>论文 · 厂商<br>摘要：提出 Headless Firm 组织模型，讨论协议化智能体如何改变企业组件之间的协调成本和组织边界。<br>收录理由：原文内容呈现AI 接入软件能力或用户界面的具体方式、AI 对软件产品边界、商业模式或组织分工的影响，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Mantix (authors declare a conflict of interest) | **主题** `界面与接入` `商业与组织`<br>**标签** `headless` `无头化` |
| 2026-02-11 | [The Ontology system](https://www.palantir.com/docs/foundry/architecture-center/ontology-system)<br>文档 · 厂商<br>摘要：说明 Palantir Ontology 如何用对象、属性、链接和行动表示企业中的真实业务实体与操作。<br>收录理由：原文内容呈现AI 接入软件能力或用户界面的具体方式、AI 改变软件内部功能、流程或数据处理的方式、AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Palantir | **主题** `界面与接入` `应用内部` `运行与问责`<br>**标签** `ontology` `本体` |
| 2026-02-10 → 2026-09-12 | [awesome-ai-agent-papers: a curated collection of AI agent research papers released in 2026](https://github.com/VoltAgent/awesome-ai-agent-papers)<br>清单 · 厂商<br>摘要：按主题整理 2026 年发布的 AI 智能体研究论文，并提供可浏览的论文清单。<br>收录理由：原文内容呈现AI 改变软件内部功能、流程或数据处理的方式、AI 参与软件设计、实现、测试或工程流程的方式、AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | VoltAgent | **主题** `应用内部` `构造方式` `运行与问责`<br>**标签** `curated-list` `资源清单` |
| 2026-02-06 → 2026-06-17 | [Graphs Don't Stay Secret: Practical Subgraph Reconstruction Attacks on Defended Graph RAG](https://arxiv.org/abs/2602.06495)<br>论文 · 学界<br>摘要：研究攻击者如何通过 Graph RAG 查询重建其底层知识图谱中的子图，并评估相关防护方式。<br>收录理由：原文内容呈现AI 改变软件内部功能、流程或数据处理的方式、AI 软件或智能体的威胁、安全控制与防护机制，与本仓记录 AI 如何改变软件开发的范围直接相关。 | KAIST, National Security Research Institute | **主题** `应用内部` `安全与攻防`<br>**标签** `RAG` `检索增强` `context-engineering` `上下文工程` |
| 2026-02-03 | [Ontology-to-tools compilation for executable semantic constraint enforcement in LLM agents](https://arxiv.org/abs/2602.03439)<br>论文 · 产学合作<br>摘要：提出将本体描述编译为可执行工具接口的原型方法，使智能体调用工具时可应用语义约束。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | University of Cambridge, CARES Singapore, MIT, CMCL | **主题** `构造方式`<br>**标签** `ontology` `本体` `tool-interface` `工具接口` |
| 2026-02-01 | [LLM-Driven Ontology Construction for Enterprise Knowledge Graphs](https://arxiv.org/abs/2602.01276)<br>论文 · 社区与非营利<br>摘要：提出使用大语言模型生成企业知识图谱本体的流程，以减少领域本体构建中的手工工作。<br>收录理由：原文内容呈现AI 改变软件内部功能、流程或数据处理的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Liber AI Research | **主题** `应用内部`<br>**标签** `ontology` `本体` |
| 2026-02-01 | [SMCP: Secure Model Context Protocol](https://arxiv.org/abs/2602.01129)<br>论文 · 学界<br>摘要：提出安全版模型上下文协议设计，讨论智能体工具连接中的认证、授权、隐私和安全控制。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制、AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Huazhong University of Science and Technology | **主题** `安全与攻防` `协议与生态`<br>**标签** `MCP` |
| 2026-01-31 | [Engineering AI Agents for Clinical Workflows: A Case Study in Architecture, MLOps, and Governance](https://arxiv.org/abs/2602.00751)<br>论文 · 产学合作<br>摘要：以临床工作流中的 AI 智能体为案例，介绍系统架构、机器学习运维和治理方面的工程实践。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | A3Data, CEFET-MG | **主题** `构造方式` `运行与问责`<br>**标签** `empirical-study` `实证测量` |
| 2026-01-30 → 2026-05-18 | [Whispers of Wealth: Red-Teaming Google's Agent Payments Protocol via Prompt Injection](https://arxiv.org/abs/2601.22569)<br>论文 · 学界<br>摘要：对 Google Agent Payments Protocol 开展提示注入红队测试，检查直接和间接攻击对智能体支付流程的影响。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制、AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | University of Georgia | **主题** `安全与攻防` `协议与生态`<br>**标签** `payments` `支付` |
| 2026-01-30 | [TessPay: Verify-then-Pay Infrastructure for Trusted Agentic Commerce](https://arxiv.org/abs/2602.00213)<br>论文 · 产学合作<br>摘要：提出面向智能体商业交易的验证后支付基础设施，讨论任务委托、服务发现和交易信任等环节。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进、AI 对软件产品边界、商业模式或组织分工的影响，与本仓记录 AI 如何改变软件开发的范围直接相关。 | University of Oxford, Indian Institute of Technology Delhi, Tesseris.org | **主题** `协议与生态` `商业与组织`<br>**标签** `payments` `支付` |
| 2026-01-29 | [Delegation Without Living Governance](https://arxiv.org/abs/2601.21226)<br>论文 · 社区与非营利<br>摘要：讨论智能体系统中的治理、责任和人类参与问题，并论述静态规则对快速自主行动的适用边界。<br>收录理由：原文内容呈现AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | AiSuNe Foundation | **主题** `运行与问责`<br>**标签** `risk-framework` `风险框架` |
| 2026-01-25 | [Faramesh: A Protocol-Agnostic Execution Control Plane for Autonomous Agent Systems](https://arxiv.org/abs/2601.17744)<br>论文 · 厂商<br>摘要：提出面向自主智能体系统的协议无关执行控制层，在产生实际副作用前对行动进行授权判断。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | The Faramesh Labs | **主题** `构造方式` `运行与问责`<br>**标签** `orchestration` `编排` |
| 2026-01-24 | [Towards a Declarative Agentic Layer for Intelligent Agents in MCP-Based Server Ecosystems](https://arxiv.org/abs/2601.17435)<br>论文 · 学界<br>摘要：研究在 MCP 服务器生态中加入声明式智能体层，以结构化方式描述任务和协调智能体行动。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Universidad de Granada | **主题** `构造方式` `协议与生态`<br>**标签** `MCP` `orchestration` `编排` |
| 2026-01-24 | [Breaking the Protocol: Security Analysis of the Model Context Protocol Specification and Prompt Injection Vulnerabilities in Tool-Integrated LLM Agents](https://arxiv.org/abs/2601.17549)<br>论文 · 个人<br>摘要：分析 MCP 规范与工具集成式 LLM 智能体的安全问题，讨论协议权限声明和提示注入等风险。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制、AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | No affiliation stated (Narek Maloyan, Dmitry Namiot) | **主题** `安全与攻防` `协议与生态`<br>**标签** `MCP` |
| 2026-01-22 → 2026-05-17 | [Agentic AI Governance and Lifecycle Management in Healthcare](https://arxiv.org/abs/2601.15630)<br>论文 · 学界<br>摘要：提出面向医疗机构的智能体治理与生命周期管理框架，讨论智能体登记、责任划分和权限控制。<br>收录理由：原文内容呈现AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | University of the Cumberlands | **主题** `运行与问责`<br>**标签** `risk-framework` `风险框架` |
| 2026-01-21 | [Interoperable Architecture for Digital Identity Delegation for AI Agents with Blockchain Integration](https://arxiv.org/abs/2601.14982)<br>论文 · 学界<br>摘要：提出面向 AI 智能体的跨系统数字身份委托架构，讨论如何实现有边界、可审计的权限转授。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Universidad de Los Andes | **主题** `安全与攻防`<br>**标签** `authorization` `身份与授权` |
| 2026-01-21 | [Securing LLM-as-a-Service for Small Businesses: An Industry Case Study of a Distributed Chatbot Deployment Platform](https://arxiv.org/abs/2601.15528)<br>论文 · 学界<br>摘要：以面向小企业的多租户聊天机器人平台为案例，讨论 LLM 服务部署中的基础设施、安全和运维设计。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制、AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | RMIT University | **主题** `安全与攻防` `运行与问责`<br>**标签** `empirical-study` `实证测量` |
| 2026-01-20 | [The Orchestration of Multi-Agent Systems: Architectures, Protocols, and Enterprise Adoption](https://arxiv.org/abs/2601.13671)<br>论文 · 厂商<br>摘要：整理多智能体编排的架构、协议和企业采用情况，并提出包含规划、策略、状态和质量管理的编排框架。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进、AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Skan AI | **主题** `协议与生态` `构造方式`<br>**标签** `orchestration` `编排` `survey` `综述` |
| 2026-01-16 → 2026-03-11 | [Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents](https://arxiv.org/abs/2601.10955)<br>论文 · 学界<br>摘要：分析智能体多轮工具调用链可能被用于隐蔽放大资源消耗的方式，并研究相关拒绝服务风险。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Nanyang Technological University, University of Illinois Urbana-Champaign, Hong Kong University of Science and Technology, Shanghai Jiao Tong University | **主题** `安全与攻防`<br>**标签** `tool-interface` `工具接口` |
| 2026-01-16 → 2026-01-20 | [Institutional AI: Governing LLM Collusion in Multi-Agent Cournot Markets via Public Governance Graphs](https://arxiv.org/abs/2601.11369)<br>论文 · 产学合作<br>摘要：构建多智能体 Cournot 市场实验框架，研究公共治理图如何影响智能体间的协同行为。<br>收录理由：原文内容呈现AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | DEXAI Icaro Lab, Sapienza University of Rome, Sant'Anna School of Advanced Studies, VU Amsterdam | **主题** `运行与问责`<br>**标签** `risk-framework` `风险框架` |
| 2026-01-15 | [Structure and Diversity Aware Context Bubble Construction for Enterprise Retrieval Augmented Systems](https://arxiv.org/abs/2601.10681)<br>论文 · 厂商<br>摘要：提出面向企业检索增强系统的上下文组装方法，利用结构信息和多样性约束构建连贯的检索内容。<br>收录理由：原文内容呈现AI 改变软件内部功能、流程或数据处理的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Bravada Group, Eye Dream Pty Ltd | **主题** `应用内部`<br>**标签** `RAG` `检索增强` `context-engineering` `上下文工程` |
| 2026-01-14 | [Beyond Rule-Based Workflows: An Information-Flow-Orchestrated Multi-Agents Paradigm via Agent-to-Agent Communication from CORAL](https://arxiv.org/abs/2601.09883)<br>论文 · 产学合作<br>摘要：提出以信息流为核心的多智能体协作范式，讨论如何减少对预先枚举状态和路由规则的依赖。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Coral Protocol, Brunel University of London, University of Luxembourg, University of Hull, National University of Computer and Emerging Sciences | **主题** `构造方式` `协议与生态`<br>**标签** `orchestration` `编排` |
| 2026-01-13 → 2026-04-19 | [ACE-Router: Generalizing History-Aware Routing from MCP Tools to the Agent Web](https://arxiv.org/abs/2601.08276)<br>论文 · 产学合作<br>摘要：提出历史感知的智能体路由方法，使系统能够在大量 MCP 工具和服务中选择合适目标。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进、AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Zhejiang University, Shanghai Jiao Tong University, Huawei Technologies, Sun Yat-sen University, Nanyang Technological University, Hangzhou Dianzi University | **主题** `协议与生态` `构造方式`<br>**标签** `MCP` `tool-interface` `工具接口` |
| 2026-01-12 | [MCP-ITP: An Automated Framework for Implicit Tool Poisoning in MCP](https://arxiv.org/abs/2601.07395)<br>论文 · 学界<br>摘要：提出自动化的 MCP 隐式工具投毒测试框架，研究注册阶段工具元数据中的恶意指令如何影响智能体。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制，与本仓记录 AI 如何改变软件开发的范围直接相关。 | University of Science and Technology of China | **主题** `安全与攻防`<br>**标签** `MCP` |
| 2026-01-12 | [Towards Verifiably Safe Tool Use for LLM Agents](https://arxiv.org/abs/2601.08012)<br>论文 · 学界<br>摘要：研究如何形式化描述并验证 LLM 智能体的工具使用安全，重点讨论工具操作可能造成的数据泄露和记录修改等风险。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制、AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Georgia Institute of Technology, Carnegie Mellon University | **主题** `安全与攻防` `构造方式`<br>**标签** `tool-interface` `工具接口` |
| 2026-01-08 | [Internal Representations as Indicators of Hallucinations in Agent Tool Selection](https://arxiv.org/abs/2601.05214)<br>论文 · 厂商<br>摘要：研究模型内部表示能否用于识别工具选择幻觉，包括错误工具、无效参数和绕过工具调用等情况。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Amazon | **主题** `构造方式`<br>**标签** `tool-interface` `工具接口` |
| 2026-01-06 → 2026-01-22 | [Enhancing Model Context Protocol (MCP) with Context-Aware Server Collaboration](https://arxiv.org/abs/2601.11595)<br>论文 · 学界<br>摘要：提出为 MCP 服务器协作增加共享上下文机制，使智能体可在多服务器任务中传递任务相关状态。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | University of Chicago | **主题** `协议与生态`<br>**标签** `MCP` `context-engineering` `上下文工程` |
| 2026-01-03 → 2026-06-22 | [MCP-SandboxScan: WASM-based Secure Execution and Runtime Analysis for MCP Tools](https://arxiv.org/abs/2601.01241)<br>论文 · 学界<br>摘要：提出基于 WebAssembly 的 MCP 工具安全执行与运行时分析框架，用于隔离工具并检查其行为。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制，与本仓记录 AI 如何改变软件开发的范围直接相关。 | University of Glasgow, Aarhus University | **主题** `安全与攻防`<br>**标签** `MCP` |
| 2025-12-16 → 2026-08-09 | [Agent Skills: specification and documentation](https://github.com/agentskills/agentskills)<br>规范 · 标准组织<br>摘要：定义 Agent Skills 开放规范，以包含 SKILL.md、脚本和资源的目录为单位，为智能体提供可复用能力。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Agent Skills project | **主题** `构造方式` `协议与生态`<br>**标签** `skills` `技能` |
| 2025-12-09 | [2025: The State of Generative AI in the Enterprise (survey of 495 respondents)](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/)<br>报告 · 投资机构<br>摘要：Menlo Ventures 基于 495 名受访者的调查报告，汇总企业生成式 AI 的采用、应用场景和支出情况。<br>收录理由：原文内容呈现AI 对软件产品边界、商业模式或组织分工的影响，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Menlo Ventures | **主题** `商业与组织`<br>**标签** `market-data` `市场数据` |
| 2025-12-09 | [OWASP Top 10 for Agentic Applications for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)<br>规范 · 社区与非营利<br>摘要：列出智能体应用的主要安全风险类别，并提供供开发团队和组织使用的风险说明与防护建议。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制，与本仓记录 AI 如何改变软件开发的范围直接相关。 | OWASP GenAI Security Project | **主题** `安全与攻防`<br>**标签** `risk-framework` `风险框架` |
| 2025-11-25 | [Securing the Model Context Protocol (MCP): Risks, Controls, and Governance](https://arxiv.org/abs/2511.20920)<br>论文 · 厂商<br>摘要：梳理 MCP 工具连接引入的安全威胁、相关控制措施和组织治理议题。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Vanta, MintMCP, Darktrace | **主题** `安全与攻防`<br>**标签** `MCP` |
| 2025-11-21 | [Computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)<br>文档 · 厂商<br>摘要：说明如何向 Claude 提供屏幕截图、鼠标和键盘控制能力，使模型能够与桌面环境交互。<br>收录理由：原文内容呈现AI 接入软件能力或用户界面的具体方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Anthropic | **主题** `界面与接入`<br>**标签** `computer-use` `计算机操作` `tool-interface` `工具接口` |
| 2025-11-05 | [Technology Radar: Model Context Protocol (MCP) assessed as Trial](https://www.thoughtworks.com/radar/platforms/model-context-protocol-mcp)<br>报告 · 分析机构<br>摘要：Thoughtworks 技术雷达评估 MCP 的定位和适用场景，并将其列为 Trial 阶段技术。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | ThoughtWorks | **主题** `协议与生态`<br>**标签** `MCP` |
| 2025-10-16 | [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)<br>文章 · 厂商<br>摘要：介绍 Anthropic 如何用模块化技能说明、脚本和资源为智能体提供处理现实任务的专门流程。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Anthropic | **主题** `构造方式`<br>**标签** `skills` `技能` `context-engineering` `上下文工程` |
| 2025-09-28 | [State of AI-assisted Software Development 2025](https://dora.dev/research/2025/dora-report/)<br>报告 · 厂商<br>摘要：DORA 的研究报告讨论 AI 辅助软件开发的使用情况，并呈现其调查结果及与软件交付、组织能力相关的分析。<br>收录理由：原文内容呈现AI 对软件产品边界、商业模式或组织分工的影响，与本仓记录 AI 如何改变软件开发的范围直接相关。 | DORA (Google Cloud) | **主题** `商业与组织`<br>**标签** `empirical-study` `实证测量` `market-data` `市场数据` |
| 2025-09-22 → 2026-09-10 | [anthropics/skills: public repository for Agent Skills](https://github.com/anthropics/skills)<br>文档 · 厂商<br>摘要：收录 Anthropic 为 Claude 提供的技能示例，内容包括可重复使用的操作说明、脚本和配套资源。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Anthropic | **主题** `构造方式`<br>**标签** `skills` `技能` |
| 2025-09-11 | [Writing effective tools for agents — with agents](https://www.anthropic.com/engineering/writing-tools-for-agents)<br>文章 · 厂商<br>摘要：Anthropic 介绍借助智能体设计和优化智能体工具的实践，并讨论工具质量与评估方法。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Anthropic | **主题** `构造方式`<br>**标签** `tool-interface` `工具接口` |
| 2025-09-01 | [An Economy of AI Agents (NBER handbook chapter)](https://arxiv.org/abs/2509.01063)<br>论文 · 学界<br>摘要：经济学手册章节综述 AI 智能体与个人、市场及组织互动的研究进展和待研究问题。<br>收录理由：原文内容呈现AI 对软件产品边界、商业模式或组织分工的影响，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Johns Hopkins University, MIT | **主题** `商业与组织`<br>**标签** `survey` `综述` |
| 2025-08-25 | [ACP Joins Forces with A2A Under the Linux Foundation](https://github.com/orgs/i-am-bee/discussions/5)<br>文章 · 标准组织<br>摘要：公告说明 ACP 项目将与 A2A 在 Linux Foundation 旗下协同，讨论协议项目整合安排。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | BeeAI project (led by IBM Research) | **主题** `协议与生态`<br>**标签** `ACP` `A2A` |
| 2025-08-22 → 2025-10-11 | [MCPVerse: An Expansive, Real-World Benchmark for Agentic Tool Use](https://arxiv.org/abs/2508.16260)<br>论文 · 厂商<br>摘要：构建包含 550 多个真实可执行工具的 MCPVerse 基准，用于评测智能体在现实工具环境中的使用能力。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | SenseTime Research | **主题** `构造方式`<br>**标签** `MCP` `benchmark` `基准评测` |
| 2025-08-19 → 2026-09-10 | [AGENTS.md: a simple, open format for guiding coding agents](https://github.com/agentsmd/agents.md)<br>规范 · 标准组织<br>摘要：定义一个用于向代码智能体提供项目背景和操作约定的开放文件格式，可在代码仓库中放置 AGENTS.md 指南。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | AGENTS.md project | **主题** `构造方式` `协议与生态`<br>**标签** `skills` `技能` |
| 2025-08-05 → 2025-10-20 | [Evolution of AI Agent Registry Solutions: Centralized, Enterprise, and Distributed Approaches](https://arxiv.org/abs/2508.03095)<br>论文 · 产学合作<br>摘要：比较集中式、企业内和分布式 AI 智能体注册表方案，讨论发现、能力协商与身份保障。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | MIT, Cisco, Cleveland State University, et al. | **主题** `协议与生态`<br>**标签** `registry` `注册表` `survey` `综述` |
| 2025-07-17 → 2025-07-21 | [A Survey of Context Engineering for Large Language Models](https://arxiv.org/abs/2507.13334)<br>论文 · 学界<br>摘要：对上下文工程进行综述和分类，讨论推理阶段如何选择、组织和优化提供给大语言模型的信息。<br>收录理由：原文内容呈现AI 改变软件内部功能、流程或数据处理的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Institute of Computing Technology CAS, Peking University, Tsinghua University, et al. | **主题** `应用内部`<br>**标签** `context-engineering` `上下文工程` `survey` `综述` |
| 2025-06-26 → 2026-09-20 | [Qwen Code: an open-source AI coding agent that lives in your terminal](https://github.com/QwenLM/qwen-code)<br>文档 · 厂商<br>摘要：提供基于 Qwen 的开源终端编程智能体，可在命令行中理解项目并执行软件开发任务。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 接入软件能力或用户界面的具体方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Alibaba (QwenLM) | **主题** `构造方式` `界面与接入`<br>**标签** `tool-interface` `工具接口` `orchestration` `编排` |
| 2025-05-30 → 2026-06-17 | [AP2: Agent Payments Protocol — building a secure and interoperable future for AI-driven payments](https://github.com/google-agentic-commerce/AP2)<br>规范 · 厂商<br>摘要：该仓库提供 Agent Payments Protocol 的代码示例与演示，用于展示智能体发起支付时的协议流程。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进、AI 对软件产品边界、商业模式或组织分工的影响，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Google | **主题** `协议与生态` `商业与组织`<br>**标签** `payments` `支付` |
| 2025-05-22 | [Fin AI Agent Pricing (per-outcome)](https://fin.ai/pricing)<br>文档 · 厂商<br>摘要：列出 Intercom Fin 客服智能体按解决结果计费的价格和服务方案。<br>收录理由：原文内容呈现AI 对软件产品边界、商业模式或组织分工的影响，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Intercom | **主题** `商业与组织`<br>**标签** `pricing` `定价` |
| 2025-05-14 → 2026-09-18 | [Strands Agents: build an agent harness and control it end-to-end](https://github.com/strands-agents/harness-sdk)<br>文档 · 厂商<br>摘要：介绍一种以模型调用为中心的智能体开发框架，支持连接模型、工具和多个智能体来构建应用。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Amazon Web Services | **主题** `构造方式`<br>**标签** `orchestration` `编排` |
| 2025-05-06 | [From Glue-Code to Protocols: A Critical Analysis of A2A and MCP Integration](https://arxiv.org/abs/2505.03864)<br>论文 · 学界<br>摘要：分析 A2A 与 MCP 在多智能体系统中的分工、互补关系及组合时的集成问题。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Kennesaw State University | **主题** `协议与生态`<br>**标签** `MCP` `A2A` |
| 2025-05-01 | [Extend Atlassian into any AI assistant using MCP](https://www.atlassian.com/platform/remote-mcp-server)<br>文档 · 厂商<br>摘要：介绍 Atlassian Remote MCP Server 如何将获授权的 Jira、Confluence 等数据和操作接入外部 AI 助手。<br>收录理由：原文内容呈现AI 接入软件能力或用户界面的具体方式、AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Atlassian | **主题** `界面与接入` `运行与问责`<br>**标签** `MCP` |
| 2025-04-28 → 2026-08-11 | [NLWeb: reference implementation for a natural language interface to websites](https://github.com/nlweb-ai/NLWeb)<br>文档 · 厂商<br>摘要：提供网站自然语言问答界面，将结构化网站内容转换为供用户和 AI 助手查询的接口，并支持 MCP。<br>收录理由：原文内容呈现AI 接入软件能力或用户界面的具体方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | NLWeb project | **主题** `界面与接入`<br>**标签** `tool-interface` `工具接口` |
| 2025-04-17 → 2026-09-20 | [Gemini CLI: an open-source AI agent that brings the power of Gemini directly into your terminal](https://github.com/google-gemini/gemini-cli)<br>文档 · 厂商<br>摘要：Google 的开源终端 AI 智能体，为命令行提供 Gemini 模型驱动的交互式开发与工具操作能力。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 接入软件能力或用户界面的具体方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Google | **主题** `构造方式` `界面与接入`<br>**标签** `tool-interface` `工具接口` `orchestration` `编排` |
| 2025-04-13 → 2026-09-20 | [Codex: lightweight coding agent that runs in your terminal](https://github.com/openai/codex)<br>文档 · 厂商<br>摘要：OpenAI 的本地终端编程智能体，可在代码仓库中协助理解和修改代码并执行开发任务。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 接入软件能力或用户界面的具体方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | OpenAI | **主题** `构造方式` `界面与接入`<br>**标签** `tool-interface` `工具接口` `orchestration` `编排` |
| 2025-04-11 → 2025-05-02 | [Enterprise-Grade Security for the Model Context Protocol (MCP)](https://arxiv.org/abs/2504.08623)<br>论文 · 厂商<br>摘要：提出 MCP 企业安全框架，梳理协议集成中的风险并汇总相应的控制和缓解策略。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Amazon Web Services, Intuit | **主题** `安全与攻防`<br>**标签** `MCP` |
| 2025-04-08 → 2026-03-03 | [awesome-mcp-security](https://github.com/Puliczek/awesome-mcp-security)<br>清单 · 个人<br>摘要：整理 MCP 安全相关的规范说明、论文、工具、视频和文章链接。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Maciej Pulikowski (Puliczek) | **主题** `安全与攻防`<br>**标签** `MCP` `curated-list` `资源清单` |
| 2025-04-01 → 2026-09-20 | [Agent Development Kit: an open-source, code-first Python toolkit for building agents](https://github.com/google/adk-python)<br>文档 · 厂商<br>摘要：Google 的 Python 开发工具包，提供构建、组合和运行智能体所需的模型、工具、工作流与会话能力。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Google | **主题** `构造方式`<br>**标签** `orchestration` `编排` |
| 2025-03-25 → 2026-09-16 | [A2A Protocol](https://a2a-protocol.org/latest/)<br>文档 · 标准组织<br>摘要：定义 Agent2Agent 开放协议，使不同厂商的智能体能够发现彼此、交换任务并协作。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Linux Foundation | **主题** `协议与生态`<br>**标签** `A2A` |
| 2025-03-21 → 2026-09-18 | [Playwright MCP server](https://github.com/microsoft/playwright-mcp)<br>文档 · 厂商<br>摘要：将 Playwright 浏览器自动化能力封装为 MCP 工具，使智能体可通过结构化页面信息操作网页。<br>收录理由：原文内容呈现AI 接入软件能力或用户界面的具体方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Microsoft | **主题** `界面与接入`<br>**标签** `MCP` `computer-use` `计算机操作` |
| 2025-03-11 → 2026-09-20 | [OpenAI Agents SDK: a lightweight, powerful framework for multi-agent workflows](https://github.com/openai/openai-agents-python)<br>文档 · 厂商<br>摘要：提供构建智能体和多智能体工作流的 Python SDK，包含工具调用、交接、护栏、会话及追踪能力。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | OpenAI | **主题** `构造方式`<br>**标签** `orchestration` `编排` `tool-interface` `工具接口` |
| 2025-02-22 → 2026-09-20 | [Claude Code: an agentic coding tool that lives in your terminal](https://github.com/anthropics/claude-code)<br>文档 · 厂商<br>摘要：Anthropic 的终端编程智能体，可理解代码库、执行开发任务、解释代码并处理 Git 工作流。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 接入软件能力或用户界面的具体方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Anthropic | **主题** `构造方式` `界面与接入`<br>**标签** `tool-interface` `工具接口` `orchestration` `编排` |
| 2025-02-12 | [Salesforce Agentforce Pricing (per-conversation)](https://www.salesforce.com/agentforce/pricing/)<br>文档 · 厂商<br>摘要：列出 Salesforce Agentforce 的产品套餐和按对话计费选项，供客户了解智能体产品定价方式。<br>收录理由：原文内容呈现AI 对软件产品边界、商业模式或组织分工的影响，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Salesforce | **主题** `商业与组织`<br>**标签** `pricing` `定价` |
| 2025-02-05 → 2026-09-16 | [MCP Registry: a community driven registry service for Model Context Protocol servers](https://github.com/modelcontextprotocol/registry)<br>文档 · 标准组织<br>摘要：提供 MCP 服务器注册服务，使 MCP 客户端能够发现和获取已发布服务器条目。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Model Context Protocol | **主题** `协议与生态`<br>**标签** `MCP` `registry` `注册表` |
| 2025-01-19 → 2026-01-27 | [UI-TARS: pioneering automated GUI interaction with native agents](https://github.com/bytedance/UI-TARS)<br>文档 · 厂商<br>摘要：介绍用于图形界面交互的视觉智能体模型与系统，使模型根据屏幕内容生成界面操作。<br>收录理由：原文内容呈现AI 接入软件能力或用户界面的具体方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | ByteDance | **主题** `界面与接入`<br>**标签** `tool-interface` `工具接口` |
| 2025-01-17 → 2026-07-11 | [Terminal-Bench: a benchmark for LLMs on complicated tasks in the terminal](https://github.com/harbor-framework/terminal-bench-1)<br>文档 · 社区与非营利<br>摘要：提供面向终端环境的智能体任务基准，用于评测模型在命令行中操作工具、完成软件工程及系统任务的能力。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 接入软件能力或用户界面的具体方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Harbor | **主题** `构造方式` `界面与接入`<br>**标签** `benchmark` `基准评测` |
| 2024-12-05 → 2026-07-20 | [Browserbase MCP server: allow LLMs to control a browser](https://github.com/browserbase/mcp-server-browserbase)<br>文档 · 厂商<br>摘要：该仓库提供连接 LLM 与 Browserbase 浏览器会话的 MCP 服务器参考实现；仓库已归档，作者说明其不代表当前生产服务。<br>收录理由：原文内容呈现AI 接入软件能力或用户界面的具体方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Browserbase | **主题** `界面与接入`<br>**标签** `MCP` `computer-use` `计算机操作` |
| 2024-12-05 → 2026-08-25 | [smolagents: a barebones library for agents that think in code](https://github.com/huggingface/smolagents)<br>文档 · 厂商<br>摘要：提供轻量级 Python 智能体框架，支持用代码生成行动或调用工具来执行任务。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Hugging Face | **主题** `构造方式`<br>**标签** `orchestration` `编排` `tool-interface` `工具接口` |
| 2024-11-30 → 2026-09-15 | [awesome-mcp-servers: a collection of MCP servers](https://github.com/punkpeye/awesome-mcp-servers)<br>清单 · 个人<br>摘要：按类别收集 MCP 服务器项目，为不同客户端和用途提供可浏览的服务器目录。<br>收录理由：原文内容呈现AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Frank Fiegel (punkpeye) | **主题** `协议与生态`<br>**标签** `MCP` `curated-list` `资源清单` |
| 2024-11-18 → 2026-04-29 | [AgentKit: build multi-agent networks in TypeScript](https://github.com/inngest/agent-kit)<br>文档 · 厂商<br>摘要：提供 TypeScript 多智能体开发工具，用于定义智能体、任务工具及协作流程。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Inngest | **主题** `构造方式`<br>**标签** `orchestration` `编排` |
| 2024-09-01 → 2026-09-04 | [llms.txt: helping language models use websites](https://github.com/AnswerDotAI/llms-txt)<br>规范 · 厂商<br>摘要：提出一种网站侧的 Markdown 文件约定，用于向语言模型介绍网站内容结构、重要页面和访问提示。<br>收录理由：原文内容呈现AI 接入软件能力或用户界面的具体方式、AI 系统与软件接口、协议或工具生态的演进，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Answer.AI | **主题** `界面与接入` `协议与生态`<br>**标签** `context-engineering` `上下文工程` |
| 2024-08-10 | [Implementation Timeline — EU Artificial Intelligence Act](https://artificialintelligenceact.eu/implementation-timeline/)<br>清单 · 社区与非营利<br>摘要：整理欧盟 AI Act 的适用义务和实施时间节点，按法规要求列出不同阶段的日期安排。<br>收录理由：原文内容呈现AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Future of Life Institute (tracker) | **主题** `运行与问责`<br>**标签** `regulation` `法规` |
| 2024-08-06 → 2026-09-20 | [Mastra: the modern TypeScript framework for AI agents](https://github.com/mastra-ai/mastra)<br>文档 · 厂商<br>摘要：TypeScript 智能体开发平台，涵盖工作流、检索增强生成、记忆、评估及应用部署。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Mastra | **主题** `构造方式`<br>**标签** `orchestration` `编排` |
| 2024-07-16 | [百炼文档（兼容 OpenAI 接口规范）](https://help.aliyun.com/zh/model-studio/)<br>文档 · 厂商<br>摘要：阿里云百炼文档介绍模型服务平台、兼容 OpenAI 的 API，以及创建智能体和知识库问答应用的方法。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | 阿里云 | **主题** `构造方式`<br>**标签** `tool-interface` `工具接口` |
| 2024-06-21 → 2026-09-19 | [Pydantic AI: how Python does AI](https://github.com/pydantic/pydantic-ai)<br>文档 · 厂商<br>摘要：提供以 Python 类型系统为基础的智能体开发框架，支持模型连接、依赖注入、结构化输出和结果校验。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Pydantic | **主题** `构造方式`<br>**标签** `tool-interface` `工具接口` |
| 2024-06-20 | [Semantic conventions for generative AI systems](https://opentelemetry.io/docs/specs/semconv/gen-ai/)<br>规范 · 标准组织<br>摘要：定义生成式 AI 系统遥测数据的统一命名约定，涉及模型、请求、生成内容及相关使用指标。<br>收录理由：原文内容呈现AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | OpenTelemetry | **主题** `运行与问责`<br>**标签** `observability` `可观测` |
| 2024-06-06 → 2026-03-18 | [tau-bench: code and data for Tau-Bench](https://github.com/sierra-research/tau-bench)<br>文档 · 厂商<br>摘要：通过航空与零售等场景中的工具、用户和环境交互任务，评测智能体在规则约束下完成多轮任务的能力。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Sierra | **主题** `构造方式`<br>**标签** `benchmark` `基准评测` `tool-interface` `工具接口` |
| 2024-02-06 → 2026-07-24 | [Daytona: secure and elastic infrastructure for running AI-generated code](https://github.com/daytonaio/daytona)<br>文档 · 厂商<br>摘要：介绍运行 AI 生成代码的安全执行环境；仓库说明核心开发已迁至私有代码库，公开仓库自 2026 年 6 月起不再更新。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 软件或智能体的威胁、安全控制与防护机制，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Daytona | **主题** `构造方式` `安全与攻防`<br>**标签** `sandbox` `沙箱` |
| 2023-12-18 | [ISO/IEC 42001:2023 — Information technology, Artificial intelligence, Management system](https://www.iso.org/standard/42001)<br>规范 · 标准组织<br>收录理由：原文内容呈现题名所示的 AI 管理体系标准涉及 AI 软件运行治理；当前未转述受限正文。，与本仓记录 AI 如何改变软件开发的范围直接相关。 | ISO/IEC | **主题** `运行与问责`<br>**标签** `risk-framework` `风险框架` `regulation` `法规` |
| 2023-11-21 | [GAIA: a benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983)<br>论文 · 厂商<br>摘要：构建通用 AI 助手基准，使用需要推理、多模态理解、网页浏览和工具使用的问题评测系统能力。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | FAIR Meta, Hugging Face, AutoGPT | **主题** `构造方式`<br>**标签** `benchmark` `基准评测` |
| 2023-11-06 | [Function calling](https://platform.openai.com/docs/guides/function-calling)<br>文档 · 厂商<br>摘要：介绍 API 函数调用机制，使模型可选择应用预先定义的函数并以结构化参数请求外部系统执行。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | OpenAI | **主题** `构造方式`<br>**标签** `tool-interface` `工具接口` |
| 2023-10-27 → 2026-09-20 | [CrewAI: framework for orchestrating role-playing, autonomous AI agents](https://github.com/crewAIInc/crewAI)<br>文档 · 厂商<br>摘要：提供以角色、任务和工具组织多个智能体的框架，并支持定义更完整的协作流程。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | CrewAI | **主题** `构造方式`<br>**标签** `orchestration` `编排` |
| 2023-10-11 → 2026-09-10 | [Letta: platform for stateful agents with advanced memory](https://github.com/letta-ai/letta)<br>文档 · 厂商<br>摘要：提供构建有状态智能体的平台与框架，支持持久记忆、运行时状态和面向开发者的代理应用。<br>收录理由：原文内容呈现AI 改变软件内部功能、流程或数据处理的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Letta | **主题** `应用内部`<br>**标签** `memory` `记忆` |
| 2023-10-04 → 2026-09-18 | [SWE-bench: can language models resolve real-world GitHub issues?](https://github.com/SWE-bench/SWE-bench)<br>文档 · 学界<br>摘要：以真实 GitHub 问题和对应代码仓库为任务，构成评估语言模型定位问题、修改代码并通过测试能力的基准。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Princeton University | **主题** `构造方式`<br>**标签** `benchmark` `基准评测` |
| 2023-08-18 → 2026-04-15 | [AutoGen: a programming framework for agentic AI](https://github.com/microsoft/autogen)<br>文档 · 厂商<br>摘要：提供构建多智能体应用的编程框架，包含消息通信、智能体协作和运行时组件。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Microsoft | **主题** `构造方式`<br>**标签** `orchestration` `编排` |
| 2023-08-09 → 2026-09-20 | [LangGraph: build resilient agents](https://github.com/langchain-ai/langgraph)<br>文档 · 厂商<br>摘要：提供有状态智能体编排框架，支持持久化运行状态、检查点、人工介入和长时任务执行。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | LangChain | **主题** `构造方式`<br>**标签** `orchestration` `编排` |
| 2023-07-13 | [生成式人工智能服务管理暂行办法](https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm)<br>规范 · 标准组织<br>摘要：规定在中国境内向公众提供生成式人工智能服务时的适用范围、服务提供者义务、数据安全和内容管理要求。<br>收录理由：原文内容呈现AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | 国家互联网信息办公室等七部门 | **主题** `运行与问责`<br>**标签** `regulation` `法规` |
| 2023-06-20 → 2026-09-19 | [Mem0: the memory layer for AI agents](https://github.com/mem0ai/mem0)<br>文档 · 厂商<br>摘要：提供面向智能体和生成式 AI 应用的持久记忆组件，用于保存并检索跨会话的用户与任务信息。<br>收录理由：原文内容呈现AI 改变软件内部功能、流程或数据处理的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Mem0 | **主题** `应用内部`<br>**标签** `memory` `记忆` |
| 2023-05-23 → 2026-09-20 | [AI SDK: the AI toolkit for TypeScript](https://github.com/vercel/ai)<br>文档 · 厂商<br>摘要：提供 TypeScript SDK，用统一接口连接生成式模型，并构建文本生成、结构化输出和流式交互应用。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Vercel | **主题** `构造方式`<br>**标签** `tool-interface` `工具接口` `orchestration` `编排` |
| 2023-05-19 → 2026-04-13 | [Gorilla: training and evaluating LLMs for function calls (Berkeley Function Calling Leaderboard)](https://github.com/ShishirPatil/gorilla)<br>文档 · 学界<br>摘要：建立函数调用评测基准，覆盖多种参数结构、并行及多轮调用场景，用于测试模型选择和调用 API 的表现。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | UC Berkeley | **主题** `构造方式`<br>**标签** `benchmark` `基准评测` `tool-interface` `工具接口` |
| 2023-05-18 → 2026-09-19 | [Langfuse: open source agent evals and observability](https://github.com/langfuse/langfuse)<br>文档 · 厂商<br>摘要：提供开源的 LLM 应用观测与评估平台，用于记录模型调用轨迹、管理提示词并测试应用输出。<br>收录理由：原文内容呈现AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Langfuse | **主题** `运行与问责`<br>**标签** `observability` `可观测` |
| 2023-04-29 → 2026-09-18 | [Zep: memory for AI agents](https://github.com/getzep/zep)<br>文档 · 厂商<br>摘要：收录 Zep Cloud 的 SDK 示例与服务集成代码，展示如何在应用中调用其智能体记忆与上下文能力。<br>收录理由：原文内容呈现AI 改变软件内部功能、流程或数据处理的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Zep | **主题** `应用内部`<br>**标签** `memory` `记忆` |
| 2023-04-12 → 2026-09-20 | [Dify: build agentic workflows and RAG pipelines with rich AI model and tool support](https://github.com/langgenius/dify)<br>文档 · 厂商<br>摘要：提供可视化平台来构建和运行 AI 应用，支持智能体工作流、检索增强生成、模型及工具连接。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 改变软件内部功能、流程或数据处理的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | LangGenius | **主题** `构造方式` `应用内部`<br>**标签** `orchestration` `编排` `RAG` `检索增强` `context-engineering` `上下文工程` |
| 2023-03-04 → 2026-09-19 | [E2B: open-source secure environment with real-world tools for AI agents](https://github.com/e2b-dev/E2B)<br>文档 · 厂商<br>摘要：提供供 AI 智能体运行代码和工具的隔离云端沙箱环境及相关 SDK。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 软件或智能体的威胁、安全控制与防护机制，与本仓记录 AI 如何改变软件开发的范围直接相关。 | E2B | **主题** `构造方式` `安全与攻防`<br>**标签** `sandbox` `沙箱` |
| 2023-02-27 → 2026-09-19 | [Semantic Kernel: integrate cutting-edge LLM technology quickly and easily into your apps](https://github.com/microsoft/semantic-kernel)<br>文档 · 厂商<br>摘要：提供将生成式模型集成到应用中的开发框架；仓库现说明其后继项目为 Microsoft Agent Framework。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 改变软件内部功能、流程或数据处理的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Microsoft | **主题** `构造方式` `应用内部`<br>**标签** `orchestration` `编排` |
| 2022-11-09 → 2026-09-19 | [Phoenix: AI observability and evaluation](https://github.com/Arize-ai/phoenix)<br>文档 · 厂商<br>摘要：提供面向 LLM 应用的开源观测和评估工具，用于查看调用链路、分析模型行为及执行评测。<br>收录理由：原文内容呈现AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Arize AI | **主题** `运行与问责`<br>**标签** `observability` `可观测` |
| 2022-11-02 → 2026-09-19 | [LlamaIndex: the document processing platform for AI](https://github.com/run-llama/llama_index)<br>文档 · 厂商<br>摘要：提供用于连接数据与 LLM 应用的框架，支持数据摄取、索引、检索以及基于数据构建智能体工作流。<br>收录理由：原文内容呈现AI 改变软件内部功能、流程或数据处理的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | LlamaIndex | **主题** `应用内部`<br>**标签** `RAG` `检索增强` `context-engineering` `上下文工程` |
| 2022-10-17 → 2026-09-20 | [LangChain: the agent engineering platform](https://github.com/langchain-ai/langchain)<br>文档 · 厂商<br>摘要：提供构建 LLM 应用与智能体的开发框架，包含模型、工具、数据连接和运行流程等集成组件。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | LangChain | **主题** `构造方式`<br>**标签** `tool-interface` `工具接口` `orchestration` `编排` |
| 2022-10-05 → 2026-09-18 | [Chroma: search infrastructure for AI](https://github.com/chroma-core/chroma)<br>文档 · 厂商<br>摘要：介绍用于 AI 应用的数据基础设施，提供向量、文档和元数据的存储、检索及相关查询接口。<br>收录理由：原文内容呈现AI 改变软件内部功能、流程或数据处理的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | Chroma | **主题** `应用内部`<br>**标签** `RAG` `检索增强` |
| 2021-08-12 | [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)<br>规范 · 标准组织<br>摘要：提供组织级 AI 风险管理框架，按治理、识别、测量和管理等功能组织 AI 生命周期风险工作。<br>收录理由：原文内容呈现AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | NIST | **主题** `运行与问责`<br>**标签** `risk-framework` `风险框架` |
| 2021-04-20 → 2026-09-10 | [pgvector: open-source vector similarity search for Postgres](https://github.com/pgvector/pgvector)<br>文档 · 社区与非营利<br>摘要：为 PostgreSQL 增加向量数据类型和相似度搜索能力，支持精确及近似近邻索引与多种距离度量。<br>收录理由：原文内容呈现AI 改变软件内部功能、流程或数据处理的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | pgvector | **主题** `应用内部`<br>**标签** `RAG` `检索增强` |
| 2019-11-14 → 2026-09-19 | [Haystack: open-source AI orchestration framework for building context-engineered, production-ready LLM applications](https://github.com/deepset-ai/haystack)<br>文档 · 厂商<br>摘要：提供构建检索增强生成和智能体应用的开源 Python 框架，以可组合组件和管线组织数据处理与模型调用。<br>收录理由：原文内容呈现AI 参与软件设计、实现、测试或工程流程的方式、AI 改变软件内部功能、流程或数据处理的方式，与本仓记录 AI 如何改变软件开发的范围直接相关。 | deepset | **主题** `构造方式` `应用内部`<br>**标签** `orchestration` `编排` `RAG` `检索增强` |
| 2017-08-07 → 2026-09-02 | [SPIFFE: the Secure Production Identity Framework for Everyone](https://github.com/spiffe/spiffe)<br>规范 · 标准组织<br>摘要：定义服务工作负载的身份标识及相互认证标准，使服务能够以可验证身份建立安全通信。<br>收录理由：原文内容呈现AI 软件或智能体的威胁、安全控制与防护机制、AI 软件的运行治理、授权、监测或责任安排，与本仓记录 AI 如何改变软件开发的范围直接相关。 | SPIFFE (CNCF) | **主题** `安全与攻防` `运行与问责`<br>**标签** `authorization` `身份与授权` |

**日期列**写的是「首发 → 最后更新」，原文自首发后没改过、或改没改采集不到的，只写首发一个日期。

**首发**是原文第一次出现的日子：论文取 arXiv v1 的投稿日，代码仓取仓库创建日，网页取互联网档案馆最早快照——快照是**下界**，只能证明该 URL 至少此时已存在。

**最后更新**默认是 `-`，**只有实际采集到明确信号才填日期**：论文有修订版的取修订日，代码仓取最后推送。未修订的论文、一次性的文章与公告都不拿首发日回填——那是推断，不是采集。148 条里实填 74 条。

**出品方**按原文署名的机构填写。arXiv 摘要页不带机构信息，这一列取自正文首页（HTML 版的作者块，或 PDF 第 1 页）；原文通篇未署机构的，直接写明「原文未署机构」并附作者名。

⚠ 标记的条目连原件也不要自行转发，理由见 [`meta/catalog.py`](meta/catalog.py) 的 `NO_REDISTRIBUTION`。

## 怎么分类

四根轴互相独立，各答一个问题，**不叠在一起**：体裁问这份材料是什么形态，出品方类型问谁出的，主题问什么在被重构，标签是横切主题的检索词。

**体裁**：6 选一，互斥。

`论文`（59） ｜ `规范`（14） ｜ `文档`（53） ｜ `清单`（6） ｜ `报告`（4） ｜ `文章`（12）

`论文` 发在 arXiv、会议、期刊上的｜`规范` 约束他人的规范文本，协议规范、风险框架、监管文件、行业基线、API 政策｜`文档` 出品方自家的说明，开发者文档、官网说明页、产品页、定价页｜`清单` 第三方汇编的清单、时间线、评分表｜`报告` 有方法有数据的调研或评估出版物｜`文章` 单篇观点、公告、工程博客。

**出品方类型**：8 选一，互斥。

`学界`（25） ｜ `厂商`（75） ｜ `产学合作`（16） ｜ `标准组织`（12） ｜ `分析机构`（3） ｜ `投资机构`（2） ｜ `社区与非营利`（8） ｜ `个人`（7）

先看有没有混：同时含大学院所与公司归 `产学合作`，只含其一归 `学界` 或 `厂商`。标准化机构与协议项目归 `标准组织`，非营利组织与独立研究组织归 `社区与非营利`，个人署名或原文未署机构归 `个人`。

**主题**：什么在被重构，分 7 个区，每条至少一个。**可以多挂，不互斥**——一条材料同时谈两件事就挂两个区，148 条里有 54 条是这样，同一条出现在两个区不是重复收录。

- `界面与接入`（23 条）
- `应用内部`（21 条）
- `构造方式`（65 条）
- `安全与攻防`（27 条）
- `运行与问责`（25 条）
- `协议与生态`（31 条）
- `商业与组织`（13 条）

`安全与攻防` 与 `运行与问责` 的分界：材料谈的是**怎么被攻破、怎么防住**（威胁、漏洞、越权、隔离、安全普查），还是**跑起来之后谁管、按什么规矩管、出事谁负责**（法规、风险框架、可观测、管控面、责任边界）。

**标签**：材料谈的具体对象或取证方式，一条可带多个，供跨主题检索。**英文是正名，中文是别名**，同一条两个都列出来，按哪种写法搜都找得到。它横着穿过主题，不在主题之下。例如，`empirical-study` 一个词就落在 6 个主题里。

| 英文标签 | 中文别名 | 条目数 |
|---|---|---:|
| `MCP` | — | 30 |
| `A2A` | — | 3 |
| `ACP` | — | 1 |
| `registry` | `注册表` | 3 |
| `tool-interface` | `工具接口` | 35 |
| `payments` | `支付` | 4 |
| `context-engineering` | `上下文工程` | 11 |
| `ontology` | `本体` | 6 |
| `RAG` | `检索增强` | 9 |
| `skills` | `技能` | 4 |
| `memory` | `记忆` | 3 |
| `sandbox` | `沙箱` | 2 |
| `observability` | `可观测` | 5 |
| `computer-use` | `计算机操作` | 3 |
| `decision-model` | `决策模型` | 2 |
| `orchestration` | `编排` | 27 |
| `authorization` | `身份与授权` | 6 |
| `regulation` | `法规` | 5 |
| `risk-framework` | `风险框架` | 9 |
| `benchmark` | `基准评测` | 10 |
| `empirical-study` | `实证测量` | 12 |
| `survey` | `综述` | 6 |
| `curated-list` | `资源清单` | 5 |
| `pricing` | `定价` | 2 |
| `headless` | `无头化` | 6 |
| `buy-vs-build` | `买还是自建` | 1 |
| `market-data` | `市场数据` | 3 |

## 关于原文副本

**本仓不分发原文副本**，只给标题、链接、日期与标签。原因：

- 收录的 arXiv 论文，许可为 `nonexclusive-distrib/1.0`——作者授权 arXiv 分发，**未授权第三方转载**

- 厂商页面与部分标准文件另有版权声明，其中一份明文禁止转载

**本仓也不记原件指纹**：收录的条目多数是持续更新的网页，GitHub 页面还内嵌 csrf 令牌与实时星数，同一秒抓两次校验值都不同——记了也核对不了，只会一直假报不一致。取原件的办法见上方「怎么用」。

## 怎么加一条

改 [`meta/catalog.py`](meta/catalog.py) 里的 `ITEMS`；分类判据在 [`meta/policy.py`](meta/policy.py)。完成后跑 `python3 meta/build.py` 重新生成。**摘要只概括原文明确陈述的内容**：说明材料讨论的对象、提出的方法或覆盖范围；用简洁、中性、可回溯到原文的表述，不加入优劣判断、推荐、推测或原文没有支持的因果结论。**收录理由说明材料为何在本目录**：指出原文具体内容与本仓收录范围、主题的对应关系；应可从一手来源核对，不写质量评价、推荐或推测。

生成前会先跑 [`meta/check.py`](meta/check.py)：日期是否真实存在、最后更新不得早于首发、四轴取值是否在词表内、同一行标题与出品方是否同语言、出处与原件键是否重复、标签是否与某个主题圈了同一堆材料。**任一项不过就不生成任何文件**，错在哪会逐条打出来。

本地回归测试：`python3 -m unittest discover -s meta -p 'test_*.py'`。

定轴时两条别踩：

- **体裁和出品方类型是两个问题，别混成一根轴**——厂商能发论文，公司能维护清单，非营利组织能出规范。混成一根就得靠没写下来的优先级维持互斥，下一个人加条目时必然走样。
- **新标签若和某个主题圈住的是同一堆材料，就不要它**——主题已经承担了，两个名字指一件事，用的人不知道该按哪个找。

## 许可

**许可只覆盖本仓自有的那部分**：条目的挑选与标签、`index.tsv`、`meta/` 下的脚本、以及本文的说明文字——以 [CC0 1.0](LICENSE) 置于公有领域，拿去用不必署名、不必告知。

**被收录材料的版权归各自权利人**，本仓一份副本都不分发，链接一律指向其原始出处。**CC0 不适用于它们**——把某篇论文或某份标准转发出去之前，看它自己的许可。
