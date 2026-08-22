# AI4AI Research Agent Safety

[返回 AI for Science Safety 目录](README.md)

## 研究方向

本页研究 Agent 自动开展 AI/ML 研究时的安全与可靠性：从 idea generation、experiment design、coding、execution、result interpretation 到论文撰写，以及自动发现 jailbreak、prompt injection 等攻击算法。关键 threat model 包括错误实验被包装为结论、benchmark 或 judge 被优化、资源和日志不足导致不可复现、研究 taste 收窄，以及 capable research agent 将自动化研究能力外溢为攻击能力。纯粹提高 AI Scientist 成果质量而不分析这些边界的系统不作为主线。

## 研究脉络

- **风险框架：** 早期工作从 user intent、scientific domain 和 environment impact 梳理 AI Scientist 的 misuse、misalignment 与监管需求。
- **可执行实验评测：** EXP-Bench、AutoExperiment 和 InnovatorBench 将宽泛的“会做研究”拆为可运行代码、逐步实验和结果复现，暴露端到端成功率与长程决策缺口。
- **创新与证据：** InnoGym、InnoEval、FIRE-Bench 和 IdeaGene-Bench 分别检验 novelty、evidence-grounded evaluation、可验证 insight rediscovery 与 idea lineage，而不是只用单一 LLM score 判断研究质量。
- **规模化审计：** FARS 保留 proposal、code、log、result 与 manuscript，使批量自动研究的 integrity failure 可以被审计；TasteGap 则揭示生成 idea 相对人类研究 taste 的系统性收窄。
- **能力外溢：** Claudini 表明 autoresearch 可直接发现更强 adversarial attack algorithm，因此安全评测必须假设攻击会针对当前防御自动适配。

## 安全边界与能力外溢

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs | attack、autoresearch、algorithm discovery、adaptive evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.24511) | [Code](https://github.com/romovpa/claudini) | 针对固定攻击集会低估防御面对定向适配时的风险；论文让 frontier coding agent 在受限预算和已有方法库上自动搜索 jailbreak 与 prompt-injection algorithm；结果发现的方法在两个目标上超过既有 automated attack，说明 autoresearch 应成为防御评测的强攻击者基线。 |
| 2024&#8209;02 | Risks of AI Scientists: Prioritizing Safeguarding Over Autonomy | analysis、AI scientist risk、environment impact、triadic governance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2402.04247) | 暂未公开 | 针对 AI Scientist autonomy 增长而风险研究零散；论文按 user intent、scientific domain 与 external environment 梳理 vulnerability，并提出 human regulation、agent alignment 和 environmental feedback 三元框架；结论是扩大自主性前需要专门 benchmark、模型约束与制度监管。 |

## 系统完整性与研究行为分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Measuring the Gap Between Human and LLM Research Ideas | analysis、research taste、idea diversity、distributional gap | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.01233) | [Code](https://github.com/ziyuuc/TasteGap) | 针对 novelty 或可行性单分无法说明 LLM idea 与真实研究思路的差距；论文用 opportunity pattern 与 research paradigm 两轴 taxonomy 比较论文反推的人类 idea 和模型生成 idea；结果 LLM 过度集中于 bridge 与 synthesis 路线，研究 taste 更窄且分布系统性偏移。 |
| 2026&#8209;06 | FARS: A Fully Automated Research System Deployed at Scale | analysis、AI-for-AI research、artifact provenance、integrity audit | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.31651) | 暂未公开 | 针对自动研究证据多来自精选案例且缺少过程审计；论文让 FARS 在共享 workspace 中保留 ideation、code、log、result 与 manuscript，并公开部署生成 166 篇 AI/ML 研究稿件；结构化评审显示系统可形成可评审成果，同时反复暴露实验范围窄、方法局限和 integrity 问题。 |
| 2026&#8209;03 | PostTrainBench: Can LLM Agents Automate LLM Post-Training? | analysis、AI4AI agent、research integrity、autonomous experimentation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63667) · [arXiv](https://arxiv.org/abs/2603.08640) | [Code](https://github.com/aisa-group/PostTrainBench) | 针对代码智能体与高风险领域模型可能产生漏洞、危险能力或不可控行为的问题，论文围绕 PostTrainBench 开展机制与边界分析；理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于危险能力评测与高风险部署治理。 |

## Research Agent Benchmark

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | AgentHPOBench: A Benchmark For Evaluating LLM Agents as Sequential Hyperparameter Optimizers | benchmark、sequential HPO、experiment log、iterative refinement | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.29626) | [Code](https://github.com/OpenMOSS/AgentHPOBench) | 针对静态 code generation 不能检验 Agent 是否会根据实验反馈持续决策；论文构建 30 个可执行 ML task，让 Agent 在多轮 configuration、metric 与 log 上调整超参数；结果当前系统已有局部优化能力，但在持续改进、复杂日志诊断和稳定接近参考性能上仍明显不足。 |
| 2026&#8209;07 | Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded Idea Generation | benchmark、idea lineage、GenomeDiff、grounded innovation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.08758) | [Code](https://github.com/VisionXLab/IdeasHaveGenomes) | 针对 AI Scientist benchmark 不检查新 idea 是否正确继承和改变既有工作；论文以 Idea Genome 与 GenomeDiff 构建跨十个领域的 lineage reasoning 和 generation 评测；结果最强系统在 closed-form lineage reasoning 上仅达 27.3% exact accuracy，显示组合式科研脉络理解仍是瓶颈。 |
| 2026&#8209;04 | NovBench: Evaluating Large Language Models on Academic Paper Novelty Assessment | benchmark、novelty assessment、expert review、evaluation quality | ACL 2026 Findings | [ACL Anthology](https://aclanthology.org/2026.findings-acl.1607/) · [arXiv](https://arxiv.org/abs/2604.11543) | [Code](https://github.com/njust-winchy/llm4novelty) | 针对 AI reviewer 与 Research Agent 缺少专门的 novelty-assessment 基线；论文从 NLP 会议构建 1,684 个 paper-review pair，并按 Relevance、Correctness、Coverage、Clarity 评测 novelty judgment；结果通用与专用模型对 scientific novelty 的理解仍有限，fine-tuned model 还存在 instruction-following 缺口。 |
| 2026&#8209;02 | InnoEval: On Research Idea Evaluation as a Knowledge-Grounded, Multi-Perspective Reasoning Problem | benchmark、idea evaluation、evidence grounding、review consensus | ICML 2026 | [arXiv](https://arxiv.org/abs/2602.14367) | [Code](https://github.com/zjunlp/InnoEval) | 针对单一 LLM judge 的知识边界、维度压平和偏见会扭曲 idea evaluation；论文用 heterogeneous search grounding 与多背景 review board 做多维评议；结果在 point-wise、pair-wise 和 group-wise 任务上更接近人类专家判断。 |
| 2026&#8209;02 | FIRE-Bench: Evaluating Agents on the Rediscovery of Scientific Insights | benchmark、insight rediscovery、executable experiment、claim-level evidence | ICML 2026 | [arXiv](https://arxiv.org/abs/2602.02905) | [Code](https://github.com/maitrix-org/FIRE-Bench) | 针对生成论文或 isolated metric 难验证 Agent 是否真正获得科学结论；论文仅给高层研究问题，要求 Agent 设计、执行实验并以 atomic claim 对照已知发现；结果最强系统仍低于 50 F1，失败集中在实验设计、执行和 evidence-based reasoning。 |
| 2025&#8209;12 | InnoGym: Benchmarking the Innovation Potential of AI Agents | benchmark、method novelty、performance gain、long-horizon evaluation | ICLR 2026 | [arXiv](https://arxiv.org/abs/2512.01822) | 暂未公开 | 针对 correctness benchmark 忽略不同解法的原创性；论文以 performance gain 与 novelty 联合评测 18 个真实工程和科学任务，并提供可复现执行环境 iGym；结果部分 Agent 能提出新方法，但鲁棒性不足使 novelty 很少稳定转化为性能收益。 |
| 2025&#8209;10 | InnovatorBench: Evaluating Agents' Ability to Conduct Innovative LLM Research | benchmark、LLM research、runnable artifact、resource management | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.27598) | 暂未公开 | 针对简化任务无法覆盖真实 LLM research 的长程实验；论文在 ResearchGym 中设置 20 个 data、loss、reward 与 scaffold 研究任务并检查 runnable artifact、质量和 uncertainty；结果 frontier Agent 在算法任务、资源管理和长期决策上仍脆弱且常依赖模板。 |
| 2025&#8209;06 | From Reproduction to Replication: Evaluating Research Agents with Progressive Code Masking | benchmark、AutoExperiment、progressive masking、experiment replication | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2506.19724) | [Code](https://github.com/j1mk1m/AutoExperiment) | 针对只运行完整代码与从零复现之间缺少连续难度评测；论文用 progressive code masking 要求 Agent 补全、执行并复现实验；结果遮蔽函数增加时成功率快速下降，交互调试和多次尝试明显优于单次固定 harness。 |
| 2025&#8209;05 | EXP-Bench: Can AI Conduct AI Research Experiments? | benchmark、AI experiment、end-to-end execution、experimental rigor | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2505.24785) | [Code](https://github.com/Just-Curieous/Curie/tree/main/benchmark/exp_bench) | 针对 AI Agent 缺少完整研究实验的细粒度评测；论文从 51 篇 AI 论文构建 461 个 hypothesis-design-implementation-execution-analysis task；结果单项偶尔达到 20%–35%，但完整可执行实验成功率仅 0.5%，暴露端到端严谨性缺口。 |

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D | benchmark、CoT monitoring、AI4AI agent、research integrity | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.19321) | 暂未公开 | ResearchArena 用安全后训练、能力后训练、CUDA kernel 与推理服务优化四类长程任务评估自动 AI R&D 的 sabotage 和 monitoring；藏在训练数据中的 artifact sabotage 被检出不足一半，即使 monitor 可运行实验也常因测试错误而漏报。 |

## 检测、审计与取证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Symposium: Trust via Auditable Records for Communities of AI Scientist Agents | detection、AI4AI agent、research integrity、autonomous experimentation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19511) | [Code](https://github.com/ndexbio/symposium) | Symposium 是一套形式框架和实际实现，用于记录由小型科学研究社群部署的 AI 智能体的运行；Symposium 为智能体驱动的研究活动提供长期、不可篡改的历史，留下分析、假设、数据和科学讨论的可审计轨迹。 |

> 跨学科 Research Agent 的检索、证据与报告可靠性见 [Scientific Research Agent Reliability](scientific-research-agent-reliability.md)，科学 Agent 的高风险任务与 tool-chain 防护见 [Scientific Domain Risk Evaluation](scientific-domain-risk-evaluation.md)。
