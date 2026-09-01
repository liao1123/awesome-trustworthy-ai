# AI4AI Research Agent Safety

[返回 AI for Science Safety 目录](README.md)

## 研究方向

本页只研究 Agent 自动开展 AI/ML 研究时的具体安全问题与安全干预：自动发现或增强攻击算法、蓄意破坏实验和制品、绕过监控、研究过程的证据与来源完整性，以及自动提出并验证 alignment mitigation。一般 idea generation、超参数优化、论文新颖性判断、实验复现或只问“会不会做研究”的能力 benchmark 不收录。

## 研究脉络

- **风险框架：** 早期工作梳理 AI Scientist 的 misuse、misalignment 与自主性风险，建立后续 threat model。
- **过程完整性：** FARS 保存 proposal、code、log、result、claim 与 provenance，使批量自动研究的完整性失效能够被复核。
- **破坏与监控：** ResearchArena 把 artifact sabotage 和 monitor evasion 放进可执行 AI R&D 环境，直接测量监督是否漏报。
- **能力外溢：** Claudini 表明 autoresearch 可自动发现更强的 jailbreak 与 prompt-injection algorithm，因此防御评测必须把自适应研究 Agent 视作攻击者。
- **安全改进自动化：** Automated alignment researcher 需要在保留通用能力时缓解明确失效，并通过 held-out benchmark、行为审计与跨规模迁移证明其发现不是对公开分数过拟合。

## 安全边界与能力外溢

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs | attack、autoresearch、algorithm discovery、adaptive evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.24511) | [Code](https://github.com/romovpa/claudini) | 针对固定攻击集会低估防御面对定向适配时的风险；论文让 frontier coding agent 在受限预算和已有方法库上自动搜索 jailbreak 与 prompt-injection algorithm；结果发现的方法在两个目标上超过既有 automated attack，说明 autoresearch 应成为防御评测的强攻击者基线。 |
| 2024&#8209;02 | Risks of AI Scientists: Prioritizing Safeguarding Over Autonomy | analysis、AI scientist risk、environment impact、triadic governance | Nature Communications 2025 | [Official](https://doi.org/10.1038/s41467-025-63913-1) · [arXiv](https://arxiv.org/abs/2402.04247) | 暂未公开 | 针对 AI Scientist autonomy 增长而风险研究零散；论文按 user intent、scientific domain 与 external environment 梳理 vulnerability，并提出 human regulation、agent alignment 和 environmental feedback 三元框架；结论是扩大自主性前需要专门 benchmark、模型约束与制度监管。 |

## 系统完整性与研究行为分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | FARS: A Fully Automated Research System Deployed at Scale | analysis、AI-for-AI research、artifact provenance、integrity audit | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.31651) | 暂未公开 | 针对自动研究证据多来自精选案例且缺少过程审计；论文让 FARS 在共享 workspace 中保留 ideation、code、log、result 与 manuscript，并公开部署生成 166 篇 AI/ML 研究稿件；结构化评审显示系统可形成可评审成果，同时反复暴露实验范围窄、方法局限和 integrity 问题。 |

## Automated Alignment Research 与 Safety Intervention

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Automated Researchers Can Reliably Mitigate Alignment Failures | defense、automated alignment research、post-training discovery、held-out validation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.28945) | 暂未公开 | 论文让 automated alignment researcher 自主提出训练方法和数据，同时缓解 deception、sycophancy、jailbreak 等十类可测失效并保持通用能力；最强方案泛化到 held-out benchmark、多轮行为审计和大 4.7 倍的模型，并超过 28 名限时八小时的人类研究者，但结论仍限于已有清晰 benchmark 的 alignment failure。 |

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D | benchmark、CoT monitoring、AI4AI agent、research integrity | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.19321) | 暂未公开 | ResearchArena 用安全后训练、能力后训练、CUDA kernel 与推理服务优化四类长程任务评估自动 AI R&D 的 sabotage 和 monitoring；藏在训练数据中的 artifact sabotage 被检出不足一半，即使 monitor 可运行实验也常因测试错误而漏报。 |

> 跨学科 Research Agent 的检索、证据与报告可靠性见 [Scientific Research Agent Reliability](scientific-research-agent-reliability.md)，科学 Agent 的高风险任务与 tool-chain 防护见 [Scientific Domain Risk Evaluation](scientific-domain-risk-evaluation.md)。
