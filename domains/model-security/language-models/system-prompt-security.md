# System Prompt Security

[返回 Language Model Security 目录](README.md)

## 研究方向

本页把 system prompt 视为同时承载应用逻辑、安全 policy、工具规则和商业知识的隐形软件资产，研究其 extraction、leakage、stealing、auditing 与 protection。攻击既可能追求逐字恢复，也可能只需复刻原 prompt 的功能；防御因此不能只检测字符串重合，还要检查语义恢复、功能克隆、正常 utility、上下文遗忘和对 adaptive query 的鲁棒性。

## 研究脉络

- **可提取性验证：** 基础工作用直接指令和系统化 query 证明隐藏 prompt 可被逐字提取，并建立区分真实恢复与模型 hallucination 的评测方法。
- **功能级窃取：** prompt marketplace 和 application store 推动攻击目标从原文恢复扩展到以少量 I/O 复制任务功能。
- **自动化与 Agent 化：** gradient-free evolution 与 curious code agent 可根据黑盒反馈自适应组合攻击策略，不再依赖固定 jailbreak template。
- **表示级防御：** prompt obfuscation、system vector 与 attention re-anchoring 尝试减少明文资产、稳定防泄漏指令并保留应用能力。
- **审计与治理：** 新工作开始把 prompt 当作可测试软件，对真实产品中的用户保护、指令冲突和 architecture-level interference 进行 span-level 审计。

## Prompt Extraction 与 Stealing Attack

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | AGFPS: An Automated Gradient-Free Framework for Prompt Stealing | attack、prompt stealing、gradient-free evolution、exact recovery | IEEE Transactions on Dependable and Secure Computing 2026 | [DOI](https://doi.org/10.1109/TDSC.2026.3671410) | 暂未公开 | 针对既有 stealing 方法依赖梯度且难扩展到黑盒服务，AGFPS 以 elite retention、adaptive crossover、mutation 和分段 fitness 进化 adversarial query；结果在多数据集与模型上实现高 exact-recovery rate 并表现出跨模型迁移性。 |
| 2026&#8209;01 | Just Ask: Curious Code Agents Reveal System Prompts in Frontier LLMs | attack、system prompt extraction、curious code agent、online exploration | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.21233) | [Code](https://github.com/x-zheng16/JustAsk) | 针对静态 query 无法根据失败结果探索新泄漏策略，JustAsk 用 UCB 选择 atomic probe 与高层 orchestration skill 并验证多轮恢复的一致性；结果在大量黑盒商业模型上恢复完整或接近完整的 system prompt 语义。 |
| 2025&#8209;08 | PRSA: Prompt Stealing Attacks against Real-World Prompt Services | attack、prompt stealing、prompt marketplace、functional replication | USENIX Security 2025 | [USENIX](https://www.usenix.org/conference/usenixsecurity25/presentation/yang-yong) | 暂未公开 | 针对 academic prompt 上的攻击无法代表付费 marketplace 和应用商店，PRSA 以少量 I/O 推断 prompt intent 并重建可复刻功能的提示；结果在两类真实服务中明显提高窃取成功率并揭示 prompt-output mutual information 与泄漏风险相关。 |
| 2025&#8209;05 | On the Effectiveness of Prompt Stealing Attacks on In-The-Wild Prompts | benchmark、prompt stealing、in-the-wild prompt、functional recovery | IEEE Symposium on Security and Privacy 2025 | [CISPA](https://cispa.de/en/research/publications/84717-on-the-effectiveness-of-prompt-stealing-attacks-on-in-the-wild-prompts) | 暂未公开 | 针对学术数据上的 prompt stealing 结果能否迁移到真实用户 prompt，论文比较二者的长度、主题与语义并引入 text-gradient refinement；结果虽改善原文和输出恢复指标，但现有攻击在真实 prompt 上仍面临根本限制。 |
| 2024&#8209;05 | PLeak: Prompt Leaking Attacks against Large Language Model Applications | attack、prompt leakage、LLM application、black-box query | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2405.06823) | [Code](https://github.com/BHui97/PLeak) | 针对 LLM application 把核心逻辑存放在不可见 system prompt，PLeak 自动构造黑盒查询并迭代恢复隐藏指令；结果证明常见“不许泄漏”提示难以阻止自适应提取。 |
| 2024 | Effective Prompt Extraction from Language Models | benchmark、prompt extraction、exact-match verification、secret prompt | COLM 2024 | [OpenReview](https://openreview.net/forum?id=0o95CVdNuz) | [Code](https://github.com/y0mingzhang/prompt-extraction) | 针对 prompt extraction 缺少可复现且能区分真实恢复与 hallucination 的评测，论文在多来源 prompt 和多个模型上系统测试简单文本攻击并设计高精度验证；结果显示隐藏 prompt 可被高概率直接恢复。 |
| 2023&#8209;02 | Prompt Stealing Attacks Against Text-to-Image Generation Models | attack、T2I prompt stealing、subject recovery、modifier detection | USENIX Security 2024 | [USENIX](https://www.usenix.org/conference/usenixsecurity24/presentation/shen-xinyue) · [arXiv](https://arxiv.org/abs/2302.09923) | [Code](https://github.com/verazuo/prompt-stealing-attack) | 针对高价值 T2I prompt 可从生成图像中被反向恢复的问题，PromptStealer 联合 subject generator 与 modifier detector 重建主题和修饰词；结果优于图像描述基线并证明生成输出会泄漏 prompt 知识产权。 |

## 防泄漏与资产保护

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Understanding and Mitigating Prompt Leaking Attacks in Real-World LLM-Based Applications | defense、prompt leakage、attention drift、attention re-anchoring | ACM CCS 2026 | [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [arXiv](https://arxiv.org/abs/2606.18673) | [Code](https://github.com/yangyZJU/AREA) | 针对真实应用的泄漏规模、内部原因和 defense utility 缺少统一证据，论文测量六个平台的 1,200 个应用并把失效归因于 attention drift，再以 AREA soft prompt 重锚防御指令；结果在保持应用功能时显著减少泄漏。 |
| 2025&#8209;09 | You Can't Steal Nothing: Mitigating Prompt Leakages in LLMs via System Vectors | defense、system vector、prompt leakage、instruction retention | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2509.21884) | 暂未公开 | 针对明文 system prompt 留在 context 中就始终可被诱导复述，SysVec 将其编码为内部 representation vector 而不放置原始文本；结果降低未授权披露，同时保持任务功能并缓解长上下文遗忘。 |
| 2025&#8209;08 | Prompt Obfuscation for Large Language Models | defense、prompt obfuscation、functional equivalence、deobfuscation attack | USENIX Security 2025 | [USENIX](https://www.usenix.org/conference/usenixsecurity25/presentation/pape) | [Artifact](https://doi.org/10.5281/zenodo.15601914) | 针对明文 prompt 的知识产权无法靠拒绝指令可靠保护，论文在离散 token 或连续 embedding 空间寻找功能等价但不可理解的 obfuscated prompt；结果在多类 utility 指标上接近原 prompt，并抵抗不同知识条件下的反混淆攻击。 |

## System Prompt 审计与干扰检测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | AISPA: User-Centric System Prompt Auditing for Large Language Model Applications | benchmark、system prompt audit、user protection、instruction taxonomy | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.28617) | [Project](https://systempromptindex.ai/) | 针对商业产品的隐藏 system prompt 缺少面向用户的可审计标准，AISPA 将 prompt 切分为 instruction span 并按八个维度标注 protective 或 problematic；对 88 个产品的审计发现保护覆盖普遍不完整且问题指令与保护指令经常共存。 |
| 2026&#8209;03 | Arbiter: Detecting Interference in LLM Agent System Prompts | detection、system prompt interference、formal rule、multi-model scouring | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.08993) | 暂未公开 | 针对 coding agent 的 system prompt 像软件却缺少测试基础设施，Arbiter 结合 formal evaluation rule 与多模型 scouring 查找指令干扰；结果在三类主流 coding agent prompt 中发现不同 architecture 对应的结构性失败模式。 |

> 面向外部不可信内容覆盖 system instruction 的攻击见 [Prompt Injection](../../misc/prompt-injection.md)；Agent harness 与 instruction hierarchy 见 [Agent Harness 与 Runtime Security](../../agent/harness-and-runtime-security.md)。
