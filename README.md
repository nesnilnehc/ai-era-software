<!-- 本文件由 meta/build.py 生成，改这里会在下次构建时被覆盖。怎么改见下方「怎么加一条」。 -->

# AI 时代的软件重构 · 材料清单

收集「软件本身因 AI 被怎样改写」的一手材料：论文、厂商文档与公告、标准文件、分析与投资机构的公开报告、社区维护的清单。**只做收集、打标签、按发布时间排序，不做解读，不写评价。**

## 怎么用

- **要数据**：[`index.tsv`](index.tsv)，139 条 × 9 列，制表符分隔。列为 首发日期／最后更新／标题／出品方／体裁／出品方类型／主题／标签／出处；主题与标签列内用 `|` 分隔多值，标签同时含英文正名与中文别名，两种写法都能 grep。

- **要翻看**：本页下方的[清单表](#清单按发布时间倒序)，按首发时间倒序。

- **要原文**：跑 [`fetch.sh`](fetch.sh)，按清单把原件下载到本地 `originals/`（已在 .gitignore 里）。取不到的会逐条报出来。

- **要加条目或改判据**：改 [`meta/catalog.py`](meta/catalog.py)，跑 `python3 meta/build.py` 重新生成本页与 `index.tsv`。

**本清单最后核对：2026-09-20**——那天逐条取过一遍，137／139 条确认地址取得回原件，其余 2 条只给链接。核对是整份清单的属性，不是每行的：这些条目是同一天过的。

## 清单（按发布时间倒序）

| 日期 | 标题 | 出品方 | 体裁 · 出品方类型 | 主题 | 标签 |
|---|---|---|---|---|---|
| 2026-09-18 | [网络安全标准实践指南——智能体系统开发安全指南（征求意见稿 v1.0-202609）](https://www.tc260.org.cn/tc260/tzgg/202609/e5b82ae7aca244d19d36b39575cbb458.shtml) ⚠ | 全国网络安全标准化技术委员会 | 规范 · 标准组织 | `安全与攻防` `界面与接入` | `regulation` `法规` |
| 2026-09-16 | [Characterizing Network Centralization and Observability in the Remote MCP Ecosystem](https://arxiv.org/abs/2609.19100) | University of Calgary | 论文 · 学界 | `协议与生态` `运行与问责` | `MCP` `empirical-study` `实证测量` |
| 2026-09-15 | [Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | TypeSafe AI | 文章 · 厂商 | `构造方式` `应用内部` | `decision-model` `决策模型` `tool-interface` `工具接口` |
| 2026-09-15 | [Introduction — TypeSafe AI (Jev developer documentation)](https://docs.typesafe.ai/introduction) | TypeSafe AI | 文档 · 厂商 | `构造方式` | `decision-model` `决策模型` `tool-interface` `工具接口` |
| 2026-09-14 | [Salesforce Koa: An Enterprise Language Model for Agentic Tool Use](https://arxiv.org/abs/2609.15066) | Salesforce | 论文 · 厂商 | `构造方式` | `tool-interface` `工具接口` |
| 2026-09-14 | [Authorization Architectures for Tool-Using AI Agents](https://arxiv.org/abs/2609.15906) | Westcliff University, University of the Cumberlands, Delta Air Lines, Georgia Institute of Technology | 论文 · 产学合作 | `安全与攻防` | `authorization` `身份与授权` `survey` `综述` |
| 2026-09-14 | [When Tool Calls Succeed but Workflows Fail: Anomalies at the Agent-Tool Boundary](https://arxiv.org/abs/2609.15397) | AVIV Group, independent researcher | 论文 · 厂商 | `构造方式` | `tool-interface` `工具接口` |
| 2026-09-13 | [A Two-Dimensional Study of the Model Context Protocol: Publication and Adoption](https://arxiv.org/abs/2609.14721) | Luxembourg Institute of Science and Technology, University of Luxembourg | 论文 · 学界 | `协议与生态` | `MCP` `empirical-study` `实证测量` |
| 2026-09-13 | [The Stochastic Deputy: Structural Tenant Isolation for Tool-Using LLM Agents](https://arxiv.org/abs/2609.14780) | Fandaqah, Heidelberg University | 论文 · 产学合作 | `安全与攻防` | `MCP` `authorization` `身份与授权` |
| 2026-09-12 | [Same Name, Different Server: A Security Census of Silent Drift in MCP](https://arxiv.org/abs/2609.14119) | Texas Tech University | 论文 · 学界 | `协议与生态` `安全与攻防` | `MCP` `empirical-study` `实证测量` |
| 2026-09-10 | [Is Bash All You Need? An Empirical Study of Tool Interfaces for Enterprise Digital Worker Agents](https://arxiv.org/abs/2609.11999) | Microsoft, Carnegie Mellon University | 论文 · 产学合作 | `构造方式` `界面与接入` | `tool-interface` `工具接口` `benchmark` `基准评测` |
| 2026-09-05 | [Intent Drift at SME Scale: Deployment Practice, Not Model Capability, Determines Agentic Compliance](https://arxiv.org/abs/2609.05975) | Hong Kong University of Science and Technology | 论文 · 学界 | `运行与问责` `应用内部` | `regulation` `法规` `empirical-study` `实证测量` |
| 2026-08-31 | [Delegation Without Trust: An Empirical Gap Analysis of Identity, Authorization, and Runtime](https://arxiv.org/abs/2609.00267) | VotalAI | 论文 · 厂商 | `安全与攻防` | `authorization` `身份与授权` |
| 2026-08-25 | [Hybrid Semantic Tool Discovery for Enterprise MCP Gateway: Architecture and Implementation](https://arxiv.org/abs/2608.23992) | PayPal | 论文 · 厂商 | `协议与生态` `构造方式` | `MCP` `context-engineering` `上下文工程` `tool-interface` `工具接口` |
| 2026-08-22 | [From SQL Generation to Tool Selection: A Domain-Oriented Pattern for MCP Servers](https://arxiv.org/abs/2608.22063) | No affiliation stated (Bartolomeo Bogliolo) | 论文 · 个人 | `界面与接入` `构造方式` | `MCP` `tool-interface` `工具接口` |
| 2026-08-19 | [Expanding Headless 360: Turning Enterprise Applications into Enterprise Capabilities](https://www.salesforce.com/news/stories/expanding-headless-360-enterprise-capabilities/) | Salesforce | 文章 · 厂商 | `界面与接入` | `headless` `无头化` |
| 2026-08-17 → 2026-08-18 | [Security Assessment of DeepSeek Harness with A.I.G: Evaluating Resistance to Indirect Prompt Injection](https://arxiv.org/abs/2608.16393) | Tencent Zhuque Lab | 论文 · 厂商 | `安全与攻防` `构造方式` | `tool-interface` `工具接口` `empirical-study` `实证测量` |
| 2026-08-13 → 2026-09-17 | [DeepSeek Harness: everything is a plugin](https://github.com/deepseek-ai/deepseek-harness) | DeepSeek AI | 文档 · 厂商 | `构造方式` `界面与接入` | `tool-interface` `工具接口` `orchestration` `编排` |
| 2026-07-28 | [Model Context Protocol Specification (version 2026-07-28)](https://modelcontextprotocol.io/specification/latest) | Model Context Protocol | 规范 · 标准组织 | `协议与生态` | `MCP` |
| 2026-06-30 | [Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation](https://arxiv.org/abs/2607.02577) | CoreThink AI, Stanford University | 论文 · 产学合作 | `构造方式` | `benchmark` `基准评测` |
| 2026-06-08 | [Understanding How Enterprises Adopt the Model Context Protocol for LLM-Driven Software Engineering](https://arxiv.org/abs/2606.09182) | City University of Hong Kong, Hong Kong Metropolitan University | 论文 · 学界 | `协议与生态` `构造方式` | `MCP` `empirical-study` `实证测量` |
| 2026-06-03 | [The State Of Agentic AI In 2026 (public blog post)](https://www.forrester.com/blogs/the-state-of-agentic-ai-in-2026-companies-are-chasing-few-are-catching/) | Forrester | 文章 · 分析机构 | `商业与组织` | `market-data` `市场数据` |
| 2026-05-28 → 2026-08-10 | [On Effectiveness and Efficiency of Agentic Tool-calling and RL Training](https://arxiv.org/abs/2606.00135) | LMU Munich, Munich Center for Machine Learning, University of Illinois Urbana-Champaign, Amazon, University of Sheffield | 论文 · 产学合作 | `构造方式` | `tool-interface` `工具接口` `benchmark` `基准评测` |
| 2026-05-28 | [Awesome Context Engineering (companion repo)](https://github.com/Meirtz/Awesome-Context-Engineering) | Institute of Computing Technology CAS, et al. | 清单 · 学界 | `应用内部` `构造方式` | `context-engineering` `上下文工程` `curated-list` `资源清单` |
| 2026-05-18 | [Going Headless? On the Boundaries of Vertical AI Firms](https://arxiv.org/abs/2605.17812) | University of Pittsburgh, Ensi.ai | 论文 · 产学合作 | `界面与接入` `商业与组织` `运行与问责` | `headless` `无头化` |
| 2026-05-13 | [ServiceNow opens its full system of action to every AI Agent in the enterprise (Action Fabric)](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-opens-its-full-system-of-action-to-every-AI-Agent-in-the-enterprise/default.aspx) | ServiceNow | 文章 · 厂商 | `界面与接入` `运行与问责` | `headless` `无头化` |
| 2026-04-29 → 2026-05-02 | [The Buy-or-Build Decision, Revisited: How Agentic AI Changes the Economics of Enterprise Software](https://arxiv.org/abs/2604.26482) | Stuttgart Media University | 论文 · 学界 | `商业与组织` | `buy-vs-build` `买还是自建` |
| 2026-04-28 | [Connecting Agents to Decisions](https://blog.palantir.com/connecting-agents-to-decisions-277dee8ddb40) | Palantir | 文章 · 厂商 | `界面与接入` `运行与问责` | `ontology` `本体` `orchestration` `编排` |
| 2026-04-26 | [Infrastructure for the Agentic Web: Gap Analysis and Architecture from the Agentverse Platform](https://arxiv.org/abs/2606.20570) | OpenHub Research | 论文 · 社区与非营利 | `协议与生态` | `empirical-study` `实证测量` `registry` `注册表` |
| 2026-04-17 → 2026-04-20 | [Integrating Graphs, Large Language Models, and Agents: Reasoning and Retrieval](https://arxiv.org/abs/2604.15951) | Canadian Institute for Cybersecurity, University of New Brunswick | 论文 · 学界 | `应用内部` | `ontology` `本体` `RAG` `检索增强` `survey` `综述` |
| 2026-04-16 → 2026-08-26 | [Corpus2Skill: Distilling Enterprise Knowledge into Navigable Agent Skills for QA and RAG](https://arxiv.org/abs/2604.14572) | Magellan Technology Research Institute | 论文 · 厂商 | `应用内部` `构造方式` | `RAG` `检索增强` `context-engineering` `上下文工程` |
| 2026-04-02 → 2026-09-18 | [x402: a payments protocol for the internet, built on HTTP](https://github.com/coinbase/x402) | Coinbase | 规范 · 厂商 | `协议与生态` | `payments` `支付` |
| 2026-04-01 → 2026-06-04 | [Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents](https://arxiv.org/abs/2604.00555) | Golden Gate University, Foundation AgenticOS, Novartis | 论文 · 产学合作 | `构造方式` `应用内部` | `ontology` `本体` |
| 2026-04 | [SAP API Policy v.4.2026a](https://help.sap.com/doc/sap-api-policy/latest/en-US/API_Policy_latest.pdf) | SAP | 规范 · 厂商 | `界面与接入` `协议与生态` | `tool-interface` `工具接口` |
| 2026-03-26 | [From Logic Monopoly to Social Contract (working paper, not peer reviewed)](https://arxiv.org/abs/2603.25100) | NetX Foundation | 论文 · 社区与非营利 | `运行与问责` | `risk-framework` `风险框架` |
| 2026-03-14 | [Awesome MCP Security: security scores for 800+ MCP servers](https://github.com/getagentseal/awesome-mcp-security) | Agentseal | 清单 · 厂商 | `安全与攻防` `协议与生态` | `MCP` `curated-list` `资源清单` |
| 2026-03-02 | [Good news: AI Will Eat Application Software](https://a16z.com/good-news-ai-will-eat-application-software/) | a16z | 文章 · 投资机构 | `商业与组织` | `headless` `无头化` |
| 2026-03 | [AI Isn't Going to "Eat" Software: Agentic AI Needs the Authoritative Data and Rules Inside Enterprise Apps](https://my.idc.com/getdoc.jsp?containerId=US54377825) ⚠ | IDC | 报告 · 分析机构 | `商业与组织` | `headless` `无头化` |
| 2026-02-24 | [The Headless Firm: How AI Reshapes Enterprise Boundaries](https://arxiv.org/abs/2602.21401) | Mantix (authors declare a conflict of interest) | 论文 · 厂商 | `界面与接入` `商业与组织` | `headless` `无头化` |
| 2026-02-11 | [The Ontology system](https://www.palantir.com/docs/foundry/architecture-center/ontology-system) | Palantir | 文档 · 厂商 | `界面与接入` `应用内部` `运行与问责` | `ontology` `本体` |
| 2026-02-10 → 2026-09-12 | [awesome-ai-agent-papers: a curated collection of AI agent research papers released in 2026](https://github.com/VoltAgent/awesome-ai-agent-papers) | VoltAgent | 清单 · 厂商 | `应用内部` `构造方式` `运行与问责` | `curated-list` `资源清单` |
| 2026-02-06 → 2026-06-17 | [Graphs Don't Stay Secret: Practical Subgraph Reconstruction Attacks on Defended Graph RAG](https://arxiv.org/abs/2602.06495) | KAIST, National Security Research Institute | 论文 · 学界 | `应用内部` `安全与攻防` | `RAG` `检索增强` `context-engineering` `上下文工程` |
| 2026-02-03 | [Ontology-to-tools compilation for executable semantic constraint enforcement in LLM agents](https://arxiv.org/abs/2602.03439) | University of Cambridge, CARES Singapore, MIT, CMCL | 论文 · 产学合作 | `构造方式` | `ontology` `本体` `tool-interface` `工具接口` |
| 2026-02-01 | [LLM-Driven Ontology Construction for Enterprise Knowledge Graphs](https://arxiv.org/abs/2602.01276) | Liber AI Research | 论文 · 社区与非营利 | `应用内部` | `ontology` `本体` |
| 2026-02-01 | [SMCP: Secure Model Context Protocol](https://arxiv.org/abs/2602.01129) | Huazhong University of Science and Technology | 论文 · 学界 | `安全与攻防` `协议与生态` | `MCP` |
| 2026-01-31 | [Engineering AI Agents for Clinical Workflows: A Case Study in Architecture, MLOps, and Governance](https://arxiv.org/abs/2602.00751) | A3Data, CEFET-MG | 论文 · 产学合作 | `构造方式` `运行与问责` | `empirical-study` `实证测量` |
| 2026-01-30 → 2026-05-18 | [Whispers of Wealth: Red-Teaming Google's Agent Payments Protocol via Prompt Injection](https://arxiv.org/abs/2601.22569) | University of Georgia | 论文 · 学界 | `安全与攻防` `协议与生态` | `payments` `支付` |
| 2026-01-30 | [TessPay: Verify-then-Pay Infrastructure for Trusted Agentic Commerce](https://arxiv.org/abs/2602.00213) | University of Oxford, Indian Institute of Technology Delhi, Tesseris.org | 论文 · 产学合作 | `协议与生态` `商业与组织` | `payments` `支付` |
| 2026-01-29 | [Delegation Without Living Governance](https://arxiv.org/abs/2601.21226) | AiSuNe Foundation | 论文 · 社区与非营利 | `运行与问责` | `risk-framework` `风险框架` |
| 2026-01-25 | [Faramesh: A Protocol-Agnostic Execution Control Plane for Autonomous Agent Systems](https://arxiv.org/abs/2601.17744) | The Faramesh Labs | 论文 · 厂商 | `构造方式` `运行与问责` | `orchestration` `编排` |
| 2026-01-24 | [Towards a Declarative Agentic Layer for Intelligent Agents in MCP-Based Server Ecosystems](https://arxiv.org/abs/2601.17435) | Universidad de Granada | 论文 · 学界 | `构造方式` `协议与生态` | `MCP` `orchestration` `编排` |
| 2026-01-24 | [Breaking the Protocol: Security Analysis of the Model Context Protocol Specification and Prompt Injection Vulnerabilities in Tool-Integrated LLM Agents](https://arxiv.org/abs/2601.17549) | No affiliation stated (Narek Maloyan, Dmitry Namiot) | 论文 · 个人 | `安全与攻防` `协议与生态` | `MCP` |
| 2026-01-22 → 2026-05-17 | [Agentic AI Governance and Lifecycle Management in Healthcare](https://arxiv.org/abs/2601.15630) | University of the Cumberlands | 论文 · 学界 | `运行与问责` | `risk-framework` `风险框架` |
| 2026-01-21 | [Interoperable Architecture for Digital Identity Delegation for AI Agents with Blockchain Integration](https://arxiv.org/abs/2601.14982) | Universidad de Los Andes | 论文 · 学界 | `安全与攻防` | `authorization` `身份与授权` |
| 2026-01-21 | [Securing LLM-as-a-Service for Small Businesses: An Industry Case Study of a Distributed Chatbot Deployment Platform](https://arxiv.org/abs/2601.15528) | RMIT University | 论文 · 学界 | `安全与攻防` `运行与问责` | `empirical-study` `实证测量` |
| 2026-01-20 | [The Orchestration of Multi-Agent Systems: Architectures, Protocols, and Enterprise Adoption](https://arxiv.org/abs/2601.13671) | Skan AI | 论文 · 厂商 | `协议与生态` `构造方式` | `orchestration` `编排` `survey` `综述` |
| 2026-01-16 → 2026-03-11 | [Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents](https://arxiv.org/abs/2601.10955) | Nanyang Technological University, University of Illinois Urbana-Champaign, Hong Kong University of Science and Technology, Shanghai Jiao Tong University | 论文 · 学界 | `安全与攻防` | `tool-interface` `工具接口` |
| 2026-01-16 → 2026-01-20 | [Institutional AI: Governing LLM Collusion in Multi-Agent Cournot Markets via Public Governance Graphs](https://arxiv.org/abs/2601.11369) | DEXAI Icaro Lab, Sapienza University of Rome, Sant'Anna School of Advanced Studies, VU Amsterdam | 论文 · 产学合作 | `运行与问责` | `risk-framework` `风险框架` |
| 2026-01-15 | [Structure and Diversity Aware Context Bubble Construction for Enterprise Retrieval Augmented Systems](https://arxiv.org/abs/2601.10681) | Bravada Group, Eye Dream Pty Ltd | 论文 · 厂商 | `应用内部` | `RAG` `检索增强` `context-engineering` `上下文工程` |
| 2026-01-14 | [Beyond Rule-Based Workflows: An Information-Flow-Orchestrated Multi-Agents Paradigm via Agent-to-Agent Communication from CORAL](https://arxiv.org/abs/2601.09883) | Coral Protocol, Brunel University of London, University of Luxembourg, University of Hull, National University of Computer and Emerging Sciences | 论文 · 产学合作 | `构造方式` `协议与生态` | `orchestration` `编排` |
| 2026-01-13 → 2026-04-19 | [ACE-Router: Generalizing History-Aware Routing from MCP Tools to the Agent Web](https://arxiv.org/abs/2601.08276) | Zhejiang University, Shanghai Jiao Tong University, Huawei Technologies, Sun Yat-sen University, Nanyang Technological University, Hangzhou Dianzi University | 论文 · 产学合作 | `协议与生态` `构造方式` | `MCP` `tool-interface` `工具接口` |
| 2026-01-12 | [MCP-ITP: An Automated Framework for Implicit Tool Poisoning in MCP](https://arxiv.org/abs/2601.07395) | University of Science and Technology of China | 论文 · 学界 | `安全与攻防` | `MCP` |
| 2026-01-12 | [Towards Verifiably Safe Tool Use for LLM Agents](https://arxiv.org/abs/2601.08012) | Georgia Institute of Technology, Carnegie Mellon University | 论文 · 学界 | `安全与攻防` `构造方式` | `tool-interface` `工具接口` |
| 2026-01-08 | [Internal Representations as Indicators of Hallucinations in Agent Tool Selection](https://arxiv.org/abs/2601.05214) | Amazon | 论文 · 厂商 | `构造方式` | `tool-interface` `工具接口` |
| 2026-01-06 → 2026-01-22 | [Enhancing Model Context Protocol (MCP) with Context-Aware Server Collaboration](https://arxiv.org/abs/2601.11595) | University of Chicago | 论文 · 学界 | `协议与生态` | `MCP` `context-engineering` `上下文工程` |
| 2026-01-03 → 2026-06-22 | [MCP-SandboxScan: WASM-based Secure Execution and Runtime Analysis for MCP Tools](https://arxiv.org/abs/2601.01241) | University of Glasgow, Aarhus University | 论文 · 学界 | `安全与攻防` | `MCP` |
| 2025-12-16 → 2026-08-09 | [Agent Skills: specification and documentation](https://github.com/agentskills/agentskills) | Agent Skills project | 规范 · 标准组织 | `构造方式` `协议与生态` | `skills` `技能` |
| 2025-12-09 | [2025: The State of Generative AI in the Enterprise (survey of 495 respondents)](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/) | Menlo Ventures | 报告 · 投资机构 | `商业与组织` | `market-data` `市场数据` |
| 2025-12-09 | [OWASP Top 10 for Agentic Applications for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | OWASP GenAI Security Project | 规范 · 社区与非营利 | `安全与攻防` | `risk-framework` `风险框架` |
| 2025-11-25 | [Securing the Model Context Protocol (MCP): Risks, Controls, and Governance](https://arxiv.org/abs/2511.20920) | Vanta, MintMCP, Darktrace | 论文 · 厂商 | `安全与攻防` | `MCP` |
| 2025-11-21 | [Computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) | Anthropic | 文档 · 厂商 | `界面与接入` | `computer-use` `计算机操作` `tool-interface` `工具接口` |
| 2025-11-05 | [Technology Radar: Model Context Protocol (MCP) assessed as Trial](https://www.thoughtworks.com/radar/platforms/model-context-protocol-mcp) | ThoughtWorks | 报告 · 分析机构 | `协议与生态` | `MCP` |
| 2025-10-16 | [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) | Anthropic | 文章 · 厂商 | `构造方式` | `skills` `技能` `context-engineering` `上下文工程` |
| 2025-09-28 | [State of AI-assisted Software Development 2025](https://dora.dev/research/2025/dora-report/) | DORA (Google Cloud) | 报告 · 厂商 | `商业与组织` | `empirical-study` `实证测量` `market-data` `市场数据` |
| 2025-09-22 → 2026-09-10 | [anthropics/skills: public repository for Agent Skills](https://github.com/anthropics/skills) | Anthropic | 文档 · 厂商 | `构造方式` | `skills` `技能` |
| 2025-09-11 | [Writing effective tools for agents — with agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | Anthropic | 文章 · 厂商 | `构造方式` | `tool-interface` `工具接口` |
| 2025-09-01 | [An Economy of AI Agents (NBER handbook chapter)](https://arxiv.org/abs/2509.01063) | Johns Hopkins University, MIT | 论文 · 学界 | `商业与组织` | `survey` `综述` |
| 2025-08-25 | [ACP Joins Forces with A2A Under the Linux Foundation](https://github.com/orgs/i-am-bee/discussions/5) | BeeAI project (led by IBM Research) | 文章 · 标准组织 | `协议与生态` | `ACP` `A2A` |
| 2025-08-22 → 2025-10-11 | [MCPVerse: An Expansive, Real-World Benchmark for Agentic Tool Use](https://arxiv.org/abs/2508.16260) | SenseTime Research | 论文 · 厂商 | `构造方式` | `MCP` `benchmark` `基准评测` |
| 2025-08-19 → 2026-09-10 | [AGENTS.md: a simple, open format for guiding coding agents](https://github.com/agentsmd/agents.md) | AGENTS.md project | 规范 · 标准组织 | `构造方式` `协议与生态` | `skills` `技能` |
| 2025-08-05 → 2025-10-20 | [Evolution of AI Agent Registry Solutions: Centralized, Enterprise, and Distributed Approaches](https://arxiv.org/abs/2508.03095) | MIT, Cisco, Cleveland State University, et al. | 论文 · 产学合作 | `协议与生态` | `registry` `注册表` `survey` `综述` |
| 2025-07-17 → 2025-07-21 | [A Survey of Context Engineering for Large Language Models](https://arxiv.org/abs/2507.13334) | Institute of Computing Technology CAS, Peking University, Tsinghua University, et al. | 论文 · 学界 | `应用内部` | `context-engineering` `上下文工程` `survey` `综述` |
| 2025-06-26 → 2026-09-20 | [Qwen Code: an open-source AI coding agent that lives in your terminal](https://github.com/QwenLM/qwen-code) | Alibaba (QwenLM) | 文档 · 厂商 | `构造方式` `界面与接入` | `tool-interface` `工具接口` `orchestration` `编排` |
| 2025-05-30 → 2026-06-17 | [AP2: Agent Payments Protocol — building a secure and interoperable future for AI-driven payments](https://github.com/google-agentic-commerce/AP2) | Google | 规范 · 厂商 | `协议与生态` `商业与组织` | `payments` `支付` |
| 2025-05-22 | [Fin AI Agent Pricing (per-outcome)](https://fin.ai/pricing) | Intercom | 文档 · 厂商 | `商业与组织` | `pricing` `定价` |
| 2025-05-14 → 2026-09-18 | [Strands Agents: build an agent harness and control it end-to-end](https://github.com/strands-agents/harness-sdk) | Amazon Web Services | 文档 · 厂商 | `构造方式` | `orchestration` `编排` |
| 2025-05-06 | [From Glue-Code to Protocols: A Critical Analysis of A2A and MCP Integration](https://arxiv.org/abs/2505.03864) | Kennesaw State University | 论文 · 学界 | `协议与生态` | `MCP` `A2A` |
| 2025-05-01 | [Extend Atlassian into any AI assistant using MCP](https://www.atlassian.com/platform/remote-mcp-server) | Atlassian | 文档 · 厂商 | `界面与接入` `运行与问责` | `MCP` |
| 2025-04-28 → 2026-08-11 | [NLWeb: reference implementation for a natural language interface to websites](https://github.com/nlweb-ai/NLWeb) | NLWeb project | 文档 · 厂商 | `界面与接入` | `tool-interface` `工具接口` |
| 2025-04-17 → 2026-09-20 | [Gemini CLI: an open-source AI agent that brings the power of Gemini directly into your terminal](https://github.com/google-gemini/gemini-cli) | Google | 文档 · 厂商 | `构造方式` `界面与接入` | `tool-interface` `工具接口` `orchestration` `编排` |
| 2025-04-13 → 2026-09-20 | [Codex: lightweight coding agent that runs in your terminal](https://github.com/openai/codex) | OpenAI | 文档 · 厂商 | `构造方式` `界面与接入` | `tool-interface` `工具接口` `orchestration` `编排` |
| 2025-04-11 → 2025-05-02 | [Enterprise-Grade Security for the Model Context Protocol (MCP)](https://arxiv.org/abs/2504.08623) | Amazon Web Services, Intuit | 论文 · 厂商 | `安全与攻防` | `MCP` |
| 2025-04-08 → 2026-03-03 | [awesome-mcp-security](https://github.com/Puliczek/awesome-mcp-security) | Maciej Pulikowski (Puliczek) | 清单 · 个人 | `安全与攻防` | `MCP` `curated-list` `资源清单` |
| 2025-04-01 → 2026-09-20 | [Agent Development Kit: an open-source, code-first Python toolkit for building agents](https://github.com/google/adk-python) | Google | 文档 · 厂商 | `构造方式` | `orchestration` `编排` |
| 2025-03-25 → 2026-09-16 | [A2A Protocol](https://a2a-protocol.org/latest/) | Linux Foundation | 文档 · 标准组织 | `协议与生态` | `A2A` |
| 2025-03-21 → 2026-09-18 | [Playwright MCP server](https://github.com/microsoft/playwright-mcp) | Microsoft | 文档 · 厂商 | `界面与接入` | `MCP` `computer-use` `计算机操作` |
| 2025-03-11 → 2026-09-20 | [OpenAI Agents SDK: a lightweight, powerful framework for multi-agent workflows](https://github.com/openai/openai-agents-python) | OpenAI | 文档 · 厂商 | `构造方式` | `orchestration` `编排` `tool-interface` `工具接口` |
| 2025-02-22 → 2026-09-20 | [Claude Code: an agentic coding tool that lives in your terminal](https://github.com/anthropics/claude-code) | Anthropic | 文档 · 厂商 | `构造方式` `界面与接入` | `tool-interface` `工具接口` `orchestration` `编排` |
| 2025-02-12 | [Salesforce Agentforce Pricing (per-conversation)](https://www.salesforce.com/agentforce/pricing/) | Salesforce | 文档 · 厂商 | `商业与组织` | `pricing` `定价` |
| 2025-02-05 → 2026-09-16 | [MCP Registry: a community driven registry service for Model Context Protocol servers](https://github.com/modelcontextprotocol/registry) | Model Context Protocol | 文档 · 标准组织 | `协议与生态` | `MCP` `registry` `注册表` |
| 2025-01-19 → 2026-01-27 | [UI-TARS: pioneering automated GUI interaction with native agents](https://github.com/bytedance/UI-TARS) | ByteDance | 文档 · 厂商 | `界面与接入` | `tool-interface` `工具接口` |
| 2025-01-17 → 2026-07-11 | [Terminal-Bench: a benchmark for LLMs on complicated tasks in the terminal](https://github.com/harbor-framework/terminal-bench-1) | Harbor | 文档 · 社区与非营利 | `构造方式` `界面与接入` | `benchmark` `基准评测` |
| 2024-12-05 → 2026-07-20 | [Browserbase MCP server: allow LLMs to control a browser](https://github.com/browserbase/mcp-server-browserbase) | Browserbase | 文档 · 厂商 | `界面与接入` | `MCP` `computer-use` `计算机操作` |
| 2024-12-05 → 2026-08-25 | [smolagents: a barebones library for agents that think in code](https://github.com/huggingface/smolagents) | Hugging Face | 文档 · 厂商 | `构造方式` | `orchestration` `编排` `tool-interface` `工具接口` |
| 2024-11-30 → 2026-09-15 | [awesome-mcp-servers: a collection of MCP servers](https://github.com/punkpeye/awesome-mcp-servers) | Frank Fiegel (punkpeye) | 清单 · 个人 | `协议与生态` | `MCP` `curated-list` `资源清单` |
| 2024-11-18 → 2026-04-29 | [AgentKit: build multi-agent networks in TypeScript](https://github.com/inngest/agent-kit) | Inngest | 文档 · 厂商 | `构造方式` | `orchestration` `编排` |
| 2024-09-01 → 2026-09-04 | [llms.txt: helping language models use websites](https://github.com/AnswerDotAI/llms-txt) | Answer.AI | 规范 · 厂商 | `界面与接入` `协议与生态` | `context-engineering` `上下文工程` |
| 2024-08-10 | [Implementation Timeline — EU Artificial Intelligence Act](https://artificialintelligenceact.eu/implementation-timeline/) | Future of Life Institute (tracker) | 清单 · 社区与非营利 | `运行与问责` | `regulation` `法规` |
| 2024-08-06 → 2026-09-20 | [Mastra: the modern TypeScript framework for AI agents](https://github.com/mastra-ai/mastra) | Mastra | 文档 · 厂商 | `构造方式` | `orchestration` `编排` |
| 2024-07-16 | [百炼文档（兼容 OpenAI 接口规范）](https://help.aliyun.com/zh/model-studio/) | 阿里云 | 文档 · 厂商 | `构造方式` | `tool-interface` `工具接口` |
| 2024-06-21 → 2026-09-19 | [Pydantic AI: how Python does AI](https://github.com/pydantic/pydantic-ai) | Pydantic | 文档 · 厂商 | `构造方式` | `tool-interface` `工具接口` |
| 2024-06-20 | [Semantic conventions for generative AI systems](https://opentelemetry.io/docs/specs/semconv/gen-ai/) | OpenTelemetry | 规范 · 标准组织 | `运行与问责` | `observability` `可观测` |
| 2024-06-06 → 2026-03-18 | [tau-bench: code and data for Tau-Bench](https://github.com/sierra-research/tau-bench) | Sierra | 文档 · 厂商 | `构造方式` | `benchmark` `基准评测` `tool-interface` `工具接口` |
| 2024-02-06 → 2026-07-24 | [Daytona: secure and elastic infrastructure for running AI-generated code](https://github.com/daytonaio/daytona) | Daytona | 文档 · 厂商 | `构造方式` `安全与攻防` | `sandbox` `沙箱` |
| 2023-12-18 | [ISO/IEC 42001:2023 — Information technology, Artificial intelligence, Management system](https://www.iso.org/standard/42001) | ISO/IEC | 规范 · 标准组织 | `运行与问责` | `risk-framework` `风险框架` `regulation` `法规` |
| 2023-11-21 | [GAIA: a benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983) | FAIR Meta, Hugging Face, AutoGPT | 论文 · 厂商 | `构造方式` | `benchmark` `基准评测` |
| 2023-11-06 | [Function calling](https://platform.openai.com/docs/guides/function-calling) | OpenAI | 文档 · 厂商 | `构造方式` | `tool-interface` `工具接口` |
| 2023-10-27 → 2026-09-20 | [CrewAI: framework for orchestrating role-playing, autonomous AI agents](https://github.com/crewAIInc/crewAI) | CrewAI | 文档 · 厂商 | `构造方式` | `orchestration` `编排` |
| 2023-10-11 → 2026-09-10 | [Letta: platform for stateful agents with advanced memory](https://github.com/letta-ai/letta) | Letta | 文档 · 厂商 | `应用内部` | `memory` `记忆` |
| 2023-10-04 → 2026-09-18 | [SWE-bench: can language models resolve real-world GitHub issues?](https://github.com/SWE-bench/SWE-bench) | Princeton University | 文档 · 学界 | `构造方式` | `benchmark` `基准评测` |
| 2023-08-18 → 2026-04-15 | [AutoGen: a programming framework for agentic AI](https://github.com/microsoft/autogen) | Microsoft | 文档 · 厂商 | `构造方式` | `orchestration` `编排` |
| 2023-08-09 → 2026-09-20 | [LangGraph: build resilient agents](https://github.com/langchain-ai/langgraph) | LangChain | 文档 · 厂商 | `构造方式` | `orchestration` `编排` |
| 2023-07-13 | [生成式人工智能服务管理暂行办法](https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm) | 国家互联网信息办公室等七部门 | 规范 · 标准组织 | `运行与问责` | `regulation` `法规` |
| 2023-06-20 → 2026-09-19 | [Mem0: the memory layer for AI agents](https://github.com/mem0ai/mem0) | Mem0 | 文档 · 厂商 | `应用内部` | `memory` `记忆` |
| 2023-05-23 → 2026-09-20 | [AI SDK: the AI toolkit for TypeScript](https://github.com/vercel/ai) | Vercel | 文档 · 厂商 | `构造方式` | `tool-interface` `工具接口` `orchestration` `编排` |
| 2023-05-19 → 2026-04-13 | [Gorilla: training and evaluating LLMs for function calls (Berkeley Function Calling Leaderboard)](https://github.com/ShishirPatil/gorilla) | UC Berkeley | 文档 · 学界 | `构造方式` | `benchmark` `基准评测` `tool-interface` `工具接口` |
| 2023-05-18 → 2026-09-19 | [Langfuse: open source agent evals and observability](https://github.com/langfuse/langfuse) | Langfuse | 文档 · 厂商 | `运行与问责` | `observability` `可观测` |
| 2023-04-29 → 2026-09-18 | [Zep: memory for AI agents](https://github.com/getzep/zep) | Zep | 文档 · 厂商 | `应用内部` | `memory` `记忆` |
| 2023-04-12 → 2026-09-20 | [Dify: build agentic workflows and RAG pipelines with rich AI model and tool support](https://github.com/langgenius/dify) | LangGenius | 文档 · 厂商 | `构造方式` `应用内部` | `orchestration` `编排` `RAG` `检索增强` `context-engineering` `上下文工程` |
| 2023-03-04 → 2026-09-19 | [E2B: open-source secure environment with real-world tools for AI agents](https://github.com/e2b-dev/E2B) | E2B | 文档 · 厂商 | `构造方式` `安全与攻防` | `sandbox` `沙箱` |
| 2023-02-27 → 2026-09-19 | [Semantic Kernel: integrate cutting-edge LLM technology quickly and easily into your apps](https://github.com/microsoft/semantic-kernel) | Microsoft | 文档 · 厂商 | `构造方式` `应用内部` | `orchestration` `编排` |
| 2022-11-09 → 2026-09-19 | [Phoenix: AI observability and evaluation](https://github.com/Arize-ai/phoenix) | Arize AI | 文档 · 厂商 | `运行与问责` | `observability` `可观测` |
| 2022-11-02 → 2026-09-19 | [LlamaIndex: the document processing platform for AI](https://github.com/run-llama/llama_index) | LlamaIndex | 文档 · 厂商 | `应用内部` | `RAG` `检索增强` `context-engineering` `上下文工程` |
| 2022-10-17 → 2026-09-20 | [LangChain: the agent engineering platform](https://github.com/langchain-ai/langchain) | LangChain | 文档 · 厂商 | `构造方式` | `tool-interface` `工具接口` `orchestration` `编排` |
| 2022-10-05 → 2026-09-18 | [Chroma: search infrastructure for AI](https://github.com/chroma-core/chroma) | Chroma | 文档 · 厂商 | `应用内部` | `RAG` `检索增强` |
| 2021-08-12 | [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | NIST | 规范 · 标准组织 | `运行与问责` | `risk-framework` `风险框架` |
| 2021-04-20 → 2026-09-10 | [pgvector: open-source vector similarity search for Postgres](https://github.com/pgvector/pgvector) | pgvector | 文档 · 社区与非营利 | `应用内部` | `RAG` `检索增强` |
| 2019-11-14 → 2026-09-19 | [Haystack: open-source AI orchestration framework for building context-engineered, production-ready LLM applications](https://github.com/deepset-ai/haystack) | deepset | 文档 · 厂商 | `构造方式` `应用内部` | `orchestration` `编排` `RAG` `检索增强` |
| 2017-08-07 → 2026-09-02 | [SPIFFE: the Secure Production Identity Framework for Everyone](https://github.com/spiffe/spiffe) | SPIFFE (CNCF) | 规范 · 标准组织 | `安全与攻防` `运行与问责` | `authorization` `身份与授权` |

**日期列**写的是「首发 → 最后更新」，原文自首发后没改过、或改没改采集不到的，只写首发一个日期。

**首发**是原文第一次出现的日子：论文取 arXiv v1 的投稿日，代码仓取仓库创建日，网页取互联网档案馆最早快照——快照是**下界**，只能证明该 URL 至少此时已存在。

**最后更新**默认是 `-`，**只有实际采集到明确信号才填日期**：论文有修订版的取修订日，代码仓取最后推送。未修订的论文、一次性的文章与公告都不拿首发日回填——那是推断，不是采集。139 条里实填 70 条。

**出品方**按原文署名的机构填写。arXiv 摘要页不带机构信息，这一列取自正文首页（HTML 版的作者块，或 PDF 第 1 页）；原文通篇未署机构的，直接写明「原文未署机构」并附作者名。

⚠ 标记的条目连原件也不要自行转发，理由见 [`meta/catalog.py`](meta/catalog.py) 的 `NO_REDISTRIBUTION`。

## 怎么分类

四根轴互相独立，各答一个问题，**不叠在一起**：体裁问这份材料是什么形态，出品方类型问谁出的，主题问什么在被重构，标签是横切主题的检索词。

**体裁**：6 选一，互斥。

`论文`（57） ｜ `规范`（14） ｜ `文档`（49） ｜ `清单`（6） ｜ `报告`（4） ｜ `文章`（9）

`论文` 发在 arXiv、会议、期刊上的｜`规范` 约束他人的规范文本，协议规范、风险框架、监管文件、行业基线、API 政策｜`文档` 出品方自家的说明，开发者文档、官网说明页、产品页、定价页｜`清单` 第三方汇编的清单、时间线、评分表｜`报告` 有方法有数据的调研或评估出版物｜`文章` 单篇观点、公告、工程博客。

**出品方类型**：8 选一，互斥。

`学界`（25） ｜ `厂商`（71） ｜ `产学合作`（14） ｜ `标准组织`（12） ｜ `分析机构`（3） ｜ `投资机构`（2） ｜ `社区与非营利`（8） ｜ `个人`（4）

先看有没有混：同时含大学院所与公司归 `产学合作`，只含其一归 `学界` 或 `厂商`。标准化机构与协议项目归 `标准组织`，非营利组织与独立研究组织归 `社区与非营利`，个人署名或原文未署机构归 `个人`。

**主题**：什么在被重构，分 7 个区，每条至少一个。**可以多挂，不互斥**——一条材料同时谈两件事就挂两个区，139 条里有 51 条是这样，同一条出现在两个区不是重复收录。

- `界面与接入`（23 条）
- `应用内部`（21 条）
- `构造方式`（59 条）
- `安全与攻防`（24 条）
- `运行与问责`（23 条）
- `协议与生态`（30 条）
- `商业与组织`（13 条）

`安全与攻防` 与 `运行与问责` 的分界：材料谈的是**怎么被攻破、怎么防住**（威胁、漏洞、越权、隔离、安全普查），还是**跑起来之后谁管、按什么规矩管、出事谁负责**（法规、风险框架、可观测、管控面、责任边界）。

**标签**：材料谈的具体对象或取证方式，一条可带多个，供跨主题检索。**英文是正名，中文是别名**，同一条两个都列出来，按哪种写法搜都找得到。它横着穿过主题，不在主题之下——`empirical-study` 一个词就落在 6 个主题里。

`MCP`（27） ｜ `A2A`（3） ｜ `ACP`（1） ｜ `registry`／`注册表`（3） ｜ `tool-interface`／`工具接口`（33） ｜ `payments`／`支付`（4） ｜ `context-engineering`／`上下文工程`（11） ｜ `ontology`／`本体`（6） ｜ `RAG`／`检索增强`（9） ｜ `skills`／`技能`（4） ｜ `memory`／`记忆`（3） ｜ `sandbox`／`沙箱`（2） ｜ `observability`／`可观测`（3） ｜ `computer-use`／`计算机操作`（3） ｜ `decision-model`／`决策模型`（2） ｜ `orchestration`／`编排`（24） ｜ `authorization`／`身份与授权`（5） ｜ `regulation`／`法规`（5） ｜ `risk-framework`／`风险框架`（7） ｜ `benchmark`／`基准评测`（9） ｜ `empirical-study`／`实证测量`（10） ｜ `survey`／`综述`（6） ｜ `curated-list`／`资源清单`（5） ｜ `pricing`／`定价`（2） ｜ `headless`／`无头化`（6） ｜ `buy-vs-build`／`买还是自建`（1） ｜ `market-data`／`市场数据`（3）

## 关于原文副本

**本仓不分发原文副本**，只给标题、链接、日期与标签。原因：

- 收录的 arXiv 论文，许可为 `nonexclusive-distrib/1.0`——作者授权 arXiv 分发，**未授权第三方转载**

- 厂商页面与部分标准文件另有版权声明，其中一份明文禁止转载

**本仓也不记原件指纹**：收录的条目多数是持续更新的网页，GitHub 页面还内嵌 csrf 令牌与实时星数，同一秒抓两次校验值都不同——记了也核对不了，只会一直假报不一致。取原件的办法见上方「怎么用」。

## 怎么加一条

改 [`meta/catalog.py`](meta/catalog.py) 里的 `ITEMS`，跑 `python3 meta/build.py` 重新生成。**只填事实字段，不要写评价**——评价一旦进来，这份清单就变成了某个人的观点集，别人就没法直接拿去用。

生成前会先跑 [`meta/check.py`](meta/check.py)：日期是否真实存在、最后更新不得早于首发、四轴取值是否在词表内、同一行标题与出品方是否同语言、出处与原件键是否重复、标签是否与某个主题圈了同一堆材料。**任一项不过就不生成任何文件**，错在哪会逐条打出来。

定轴时两条别踩：

- **体裁和出品方类型是两个问题，别混成一根轴**——厂商能发论文，公司能维护清单，非营利组织能出规范。混成一根就得靠没写下来的优先级维持互斥，下一个人加条目时必然走样。

- **新标签若和某个主题圈住的是同一堆材料，就不要它**——主题已经承担了，两个名字指一件事，用的人不知道该按哪个找。

## 许可

**许可只覆盖本仓自有的那部分**：条目的挑选与标签、`index.tsv`、`meta/` 下的脚本、以及本文的说明文字——以 [CC0 1.0](LICENSE) 置于公有领域，拿去用不必署名、不必告知。

**被收录材料的版权归各自权利人**，本仓一份副本都不分发，链接一律指向其原始出处。**CC0 不适用于它们**——把某篇论文或某份标准转发出去之前，看它自己的许可。
