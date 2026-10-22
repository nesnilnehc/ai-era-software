# 问题探索维护

`meta/questions.json` 是唯一可编辑问题数据源，`questions.json` 由现有 `python3 meta/build.py` 生成，禁止手改。`meta/candidates.tsv` 只判断材料是否收录；问题池管理值得追问的疑点，不改变 `meta/policy.py` 的准入标准。

## 数据接口 v1

顶层 `schema_version: 1` 与 `questions` 数组。每项字段：

| 字段 | 约定 |
|---|---|
| id | 稳定编号 Q-0001 起，永久保留，不复用 |
| title / basis | 问法、发现依据；区分原文事实与推断 |
| sources | 原始来源数组：title、https url、checked 核读日期、evidence 具体段落或证据边界 |
| value | 一句话研究价值 |
| known / unknown | 已知与尚未证实的内容分开 |
| next_step | 可执行的下一步查证 |
| status | 待澄清、待研究、已转研究、搁置 |
| updated | YYYY-MM-DD，等于历史末项日期 |
| history | 按日期升序记录 date、reason；解释新增、补证、改问法、状态变化原因 |
| merged_into | 未合并为 null；合并后保留原项与旧编号，填写目标编号，禁止循环或悬空 |

“已转研究”表示进入研究过程，不表示解决；部分答案写入已知和未知，不直接标解决。合并时旧项设为搁置并记录去向及原因；网站保留旧项并显示链接。研究结果与证据先写入历史，问题没有可靠答案时继续保留未知。

## 每日采集后的独立步骤

截至 2026-10-22，既有“AI 软件变革资料每日采集与更新”任务已配置为在资料处理后维护问题清单；保持每天北京时间 06:30 在自有云电脑运行，仅在任务中汇报，不发送邮件。首次自然运行待验证，配置完成不代表定时执行已跑通。

1. 先完成材料采集和准入判断，再检查本次材料是否影响已有问题。
2. 新疑点先检索标题、来源与已知未知，必要时新增稳定编号；重复问题只补证据与核读日期。
3. 修改问法须记录原因；新来源只回答一部分时更新已知、未知及下一步。
4. 无影响不改内容或更新时间，不空跑修订记录，不为数量补问题；不写企业私密信息。
5. 采集与问题更新分别报告：前者报告正式收录/候选及原因；后者报告新增、补证、修订、合并、搁置或无变化。
6. 运行构建、检查、单测和 diff 检查。是否提交与发布由当次授权决定。问题维护沿用既有每日采集任务，本说明修订不修改自动化定义。

## 网站数据与验证

网站独立读取 GitHub main 的 `questions.json`，首次失败回退随站 JSON，后续失败保留上次成功数据；打开、回前台和每五分钟更新。材料目录继续使用原有 TSV 同步逻辑。localhost 预览问题只读取本地快照，便于验证未推送数据。

若本仓存在 `sites/ai-software-atlas/dist/`，构建同时生成其中的同字节 `questions.json`；`--check-generated` 检查快照一致性。站点是已有的独立 Sites 源仓，未纳入根仓（沿用原来的 `/sites/` 忽略规则）。首次发布页面代码后，日常问题数据变化只需根仓构建和获准推送，网站下一轮读取即可更新。站点再发布前应重新构建更新其随站快照。

```sh
python3 meta/build.py
python3 meta/check.py
python3 -m unittest discover -s meta -p 'test*.py'
node --test sites/ai-software-atlas/test/*.test.mjs
git diff --check
git -C sites/ai-software-atlas diff --check
```

初始化仅含一项实际核读的 GitHub 原文问题；公告能证明产品规则，不能证明治理效果。PACE-Bench 未在本轮追加，静态代码审查不能代替实验证明。
