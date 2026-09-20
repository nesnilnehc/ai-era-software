# AI 时代的软件重构 · 材料清单

收集「软件本身因 AI 被怎样改写」的一手材料：论文、厂商文档与公告、标准文件、分析与投资机构的公开报告、社区维护的清单。

**本仓只做三件事：收集、打标签、按发布时间排序。不做解读，不写评价。**

机器可读版在 [`index.tsv`](index.tsv)。

## 关于原文副本

**本仓不分发原文副本**，只给标题、链接、发布日期、标签，以及**每份原件的 sha256**（供核对你取回的是不是同一份）。原因：

- 收录的 arXiv 论文，许可为 `nonexclusive-distrib/1.0`——作者授权 arXiv 分发，**未授权第三方转载**

- 厂商页面与部分标准文件另有版权声明，其中一份明文禁止转载


要原文，跑 [`fetch.sh`](fetch.sh)，它按清单把原件下载到本地 `originals/`（已在 .gitignore 里）。

## 标签

**主题**按「什么在被重构」分六类，不按角色分：

- `界面与接入`（9 条）
- `应用内部`（4 条）
- `构造方式`（13 条）
- `运行与治理`（19 条）
- `协议与生态`（15 条）
- `商业与组织`（10 条）

**类型**：`论文`（26） ｜ `厂商`（9） ｜ `标准`（8） ｜ `分析`（3） ｜ `投资`（2） ｜ `社区`（4）

## 清单（按发布时间倒序）

| 发布 | 标题 | 出品方 | 类型 | 主题 |
|---|---|---|---|---|
| 2026-09-20 | [MCP 官方注册表：设计原则与生态愿景](https://github.com/modelcontextprotocol/registry) | Model Context Protocol | 标准 | `协议与生态` |
| 2026-09-20 | [A2A Protocol 官网：治理与技术指导委员会](https://a2a-protocol.org/latest/) | Linux 基金会 | 标准 | `协议与生态` |
| 2026-09-20 | [Agent Communication Protocol 官网](https://agentcommunicationprotocol.dev/) | （见原文） | 标准 | `协议与生态` |
| 2026-09-20 | [Atlassian Remote MCP Server 产品页](https://www.atlassian.com/platform/remote-mcp-server) | Atlassian | 厂商 | `界面与接入` `运行与治理` |
| 2026-09-20 | [Agentforce 定价页（按对话计费）](https://www.salesforce.com/agentforce/pricing/) | Salesforce | 厂商 | `商业与组织` |
| 2026-09-20 | [Fin 定价页（按结果计费）](https://www.intercom.com/pricing) | Intercom | 厂商 | `商业与组织` |
| 2026-09-20 | [Function calling 开发者文档](https://platform.openai.com/docs/guides/function-calling) | OpenAI | 厂商 | `构造方式` |
| 2026-09-20 | [AI Risk Management Framework（1.0 修订中）](https://www.nist.gov/itl/ai-risk-management-framework) | 美国国家标准与技术研究院 | 标准 | `运行与治理` |
| 2026-09-20 | [EU AI Act 实施时间线](https://artificialintelligenceact.eu/implementation-timeline/) | Future of Life Institute（追踪站） | 标准 | `运行与治理` |
| 2026-09-20 | [The State Of Agentic AI In 2026（公开博客）](https://www.forrester.com/blogs/the-state-of-agentic-ai-in-2026-companies-are-chasing-few-are-catching/) | Forrester | 分析 | `商业与组织` |
| 2026-09-20 | [awesome-ai-agent-papers（388 篇 2026 年论文）](https://github.com/VoltAgent/awesome-ai-agent-papers) | VoltAgent | 社区 | `应用内部` `构造方式` `运行与治理` |
| 2026-09-20 | [awesome-mcp-security](https://github.com/Puliczek/awesome-mcp-security) | Puliczek | 社区 | `运行与治理` |
| 2026-09-20 | [800+ MCP 服务端安全评分](https://github.com/getagentseal/awesome-mcp-security) | getagentseal | 社区 | `运行与治理` `协议与生态` |
| 2026-09-20 | [百炼文档（兼容 OpenAI 接口规范）](https://help.aliyun.com/zh/model-studio/) | 阿里云 | 厂商 | `构造方式` |
| 2026-09-18 | [网络安全标准实践指南——智能体系统开发安全指南（征求意见稿 v1.0-202609）](https://www.tc260.org.cn/tc260/tzgg/202609/e5b82ae7aca244d19d36b39575cbb458.shtml) ⚠ | 全国网络安全标准化技术委员会 | 标准 | `运行与治理` `界面与接入` |
| 2026-09-16 | [Characterizing Network Centralization and Observability in the Remote MCP Ecosystem](https://arxiv.org/abs/2609.19100) | 卡尔加里大学 | 论文 | `协议与生态` `运行与治理` |
| 2026-09-15 | [Salesforce Koa: An Enterprise Language Model for Agentic Tool Use](https://arxiv.org/abs/2609.15066) | Salesforce | 论文 | `构造方式` |
| 2026-09-14 | [Authorization Architectures for Tool-Using AI Agents](https://arxiv.org/abs/2609.15906) | （见原文） | 论文 | `运行与治理` |
| 2026-09-14 | [When Tool Calls Succeed but Workflows Fail: Anomalies at the Agent-Tool Boundary](https://arxiv.org/abs/2609.15397) | （见原文） | 论文 | `构造方式` |
| 2026-09-13 | [A Two-Dimensional Study of the Model Context Protocol: Publication and Adoption](https://arxiv.org/abs/2609.14721) | 卢森堡科技研究院、卢森堡大学 | 论文 | `协议与生态` |
| 2026-09-13 | [The Stochastic Deputy: Structural Tenant Isolation for Tool-Using LLM Agents](https://arxiv.org/abs/2609.14780) | （见原文） | 论文 | `运行与治理` |
| 2026-09-12 | [Same Name, Different Server: A Security Census of Silent Drift in MCP](https://arxiv.org/abs/2609.14119) | （见原文） | 论文 | `协议与生态` `运行与治理` |
| 2026-09-10 | [Is Bash All You Need? An Empirical Study of Tool Interfaces for Enterprise Digital Worker Agents](https://arxiv.org/abs/2609.11999) | Microsoft、卡内基梅隆大学 | 论文 | `构造方式` `界面与接入` |
| 2026-09-05 | [Intent Drift at SME Scale: Deployment Practice, Not Model Capability, Determines Agentic Compliance](https://arxiv.org/abs/2609.05975) | 香港科技大学 | 论文 | `运行与治理` `应用内部` |
| 2026-08-31 | [Delegation Without Trust: An Empirical Gap Analysis of Identity, Authorization, and Runtime](https://arxiv.org/abs/2609.00267) | （见原文） | 论文 | `运行与治理` |
| 2026-08-25 | [Hybrid Semantic Tool Discovery for Enterprise MCP Gateway: Architecture and Implementation](https://arxiv.org/abs/2608.23992) | （见原文） | 论文 | `协议与生态` `构造方式` |
| 2026-08-25 | [MCPVerse: An Expansive, Real-World Benchmark for Agentic Tool Use](https://arxiv.org/abs/2508.16260) | （见原文） | 论文 | `构造方式` |
| 2026-08-22 | [From SQL Generation to Tool Selection: A Domain-Oriented Pattern for MCP Servers](https://arxiv.org/abs/2608.22063) | （见原文） | 论文 | `界面与接入` `构造方式` |
| 2026-08-19 | [Expanding Headless 360: Turning Enterprise Applications into Enterprise Capabilities](https://www.salesforce.com/news/stories/expanding-headless-360-enterprise-capabilities/) | Salesforce | 厂商 | `界面与接入` |
| 2026-07-28 | [Model Context Protocol Specification (version 2026-07-28)](https://modelcontextprotocol.io/specification/latest) | Model Context Protocol | 标准 | `协议与生态` |
| 2026-06-30 | [Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation](https://arxiv.org/abs/2607.02577) | CoreThink AI、斯坦福大学 | 论文 | `构造方式` |
| 2026-06-08 | [Understanding How Enterprises Adopt the Model Context Protocol for LLM-Driven Software Engineering](https://arxiv.org/abs/2606.09182) | 香港城市大学、香港都会大学 | 论文 | `协议与生态` `构造方式` |
| 2026-05-28 | [Awesome Context Engineering（配套仓）](https://github.com/Meirtz/Awesome-Context-Engineering) | 中科院计算所等 | 社区 | `应用内部` `构造方式` |
| 2026-05-13 | [ServiceNow opens its full system of action to every AI Agent in the enterprise（Action Fabric）](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-opens-its-full-system-of-action-to-every-AI-Agent-in-the-enterprise/default.aspx) | ServiceNow | 厂商 | `界面与接入` `运行与治理` |
| 2026-05-02 | [The Buy-or-Build Decision, Revisited: How Agentic AI Changes the Economics of Enterprise Software](https://arxiv.org/abs/2604.26482) | 斯图加特媒体大学 | 论文 | `商业与组织` |
| 2026-04-26 | [Infrastructure for the Agentic Web: Gap Analysis and Architecture from the Agentverse Platform](https://arxiv.org/abs/2606.20570) | OpenHub Research | 论文 | `协议与生态` |
| 2026-04 | [SAP API Policy v.4.2026a](https://help.sap.com/doc/sap-api-policy/latest/en-US/API_Policy_latest.pdf) | SAP | 厂商 | `界面与接入` `协议与生态` |
| 2026-03-26 | [From Logic Monopoly to Social Contract（工作论文，未经同行评议）](https://arxiv.org/abs/2603.25100) | NetX Foundation | 论文 | `运行与治理` |
| 2026-03-02 | [Good news: AI Will Eat Application Software](https://a16z.com/good-news-ai-will-eat-application-software/) | a16z | 投资 | `商业与组织` |
| 2026-03 | [AI Isn't Going to "Eat" Software: Agentic AI Needs the Authoritative Data and Rules Inside Enterprise Apps](https://my.idc.com/getdoc.jsp?containerId=US54377825) ⚠ | IDC | 分析 | `商业与组织` |
| 2026-02-24 | [The Headless Firm: How AI Reshapes Enterprise Boundaries](https://arxiv.org/abs/2602.21401) | Mantix（作者自陈利益冲突） | 论文 | `界面与接入` `商业与组织` |
| 2026-01-01 | [Going Headless? On the Boundaries of Vertical AI Firms](https://arxiv.org/abs/2605.17812) | 匹兹堡大学、Ensi.ai | 论文 | `界面与接入` `商业与组织` `运行与治理` |
| 2025-12-09 | [2025: The State of Generative AI in the Enterprise（495 人问卷）](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/) | Menlo Ventures | 投资 | `商业与组织` |
| 2025-12-09 | [OWASP Top 10 for Agentic Applications for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | OWASP GenAI Security Project | 标准 | `运行与治理` |
| 2025-11-25 | [Securing the Model Context Protocol (MCP): Risks, Controls, and Governance](https://arxiv.org/abs/2511.20920) | Vanta、MintMCP、Darktrace | 论文 | `运行与治理` |
| 2025-11-05 | [Technology Radar：Model Context Protocol (MCP) 评为 Trial](https://www.thoughtworks.com/radar/platforms/model-context-protocol-mcp) | ThoughtWorks | 分析 | `协议与生态` |
| 2025-10-20 | [Evolution of AI Agent Registry Solutions: Centralized, Enterprise, and Distributed Approaches](https://arxiv.org/abs/2508.03095) | 麻省理工、Cisco、克利夫兰州立大学等 | 论文 | `协议与生态` |
| 2025-09-11 | [Writing effective tools for agents — with agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | Anthropic | 厂商 | `构造方式` |
| 2025-09-01 | [An Economy of AI Agents（美国国家经济研究局手册章节）](https://arxiv.org/abs/2509.01063) | 约翰霍普金斯大学、麻省理工 | 论文 | `商业与组织` |
| 2025-07-21 | [A Survey of Context Engineering for Large Language Models](https://arxiv.org/abs/2507.13334) | 中科院计算所、北京大学、清华大学等 | 论文 | `应用内部` |
| 2025-05-02 | [Enterprise-Grade Security for the Model Context Protocol (MCP)](https://arxiv.org/abs/2504.08623) | 亚马逊云科技、Intuit | 论文 | `运行与治理` |
| 2025-05 | [From Glue-Code to Protocols: A Critical Analysis of A2A and MCP Integration](https://arxiv.org/abs/2505.03864) | 肯尼索州立大学 | 论文 | `协议与生态` |

⚠ 标记的条目连原件也不要自行转发，理由见 [`meta/catalog.py`](meta/catalog.py) 的 `NO_REDISTRIBUTION`。

## 怎么加一条

改 [`meta/catalog.py`](meta/catalog.py) 里的 `ITEMS`，跑 `python3 meta/build.py` 重新生成。**只填事实字段，不要写评价**——评价一旦进来，这份清单就变成了某个人的观点集，别人就没法直接拿去用。

## 许可

**许可只覆盖本仓自有的那部分**：条目的挑选与标签、`index.tsv`、`meta/` 下的脚本、以及本文的说明文字——以 [CC0 1.0](LICENSE) 置于公有领域，拿去用不必署名、不必告知。


**被收录材料的版权归各自权利人**，本仓一份副本都不分发，链接一律指向其原始出处。**CC0 不适用于它们**——把某篇论文或某份标准转发出去之前，看它自己的许可。
