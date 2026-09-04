# AI Peer Review Security

[返回 AI for Science Safety 目录](README.md)

## 研究方向

本页研究 LLM 或 MLLM 被用于 manuscript screening、review assistance、automated scoring 和 editorial triage 时的可靠性与可操纵性。威胁既包括模型自身的 score inflation、评价维度偏差、hallucination 和 reviewer homogenization，也包括作者主动植入 hidden prompt、对 figure 做 adversarial perturbation，或在不改变科学 claim 的情况下优化 abstract、rhetoric 和 presentation 来提高评分。该问题与一般 jailbreak 不同：攻击目标是定向改变评审结论，而不是让模型输出任意违规内容。

## 研究脉络

- **Reviewer validity：** 早期比较显示 AI reviewer 会高估弱论文、与人类关注点分离并产生模板化长评审，说明 capability 不等于 calibrated judgment。
- **Review infrastructure：** Review-CoT 与 ReviewBench 将 structured reasoning、相关工作引用和 human-review alignment 变成可复用的训练与评测对象，为后续 robustness study 提供基础。
- **Hidden prompt：** PDF 中不可见文字、field-specific instruction 和 iterative injection 可直接抬高分数；检测式防御面对 adaptive attacker 仍会退化。
- **Presentation gaming：** PAA、Review Arcade、abstract rewrite 与 adversarial repackaging 证明即使没有显式恶意指令，语义保持或表述层修改也能优化 AI score。
- **Multimodal attack：** PaperGuard 将 threat model 从正文扩展到 figure，并以 chunk retrieval 和 intent verification 处理长文档中的稀疏攻击证据。
- **当前边界：** 单一 reviewer-model correlation 不能证明安全；部署前还需要 score calibration、跨模型稳定性、attack-aware evaluation、人类复核和不让作者反向优化 evaluator 的机制。

## Reviewer Validity、Bias 与 Benchmark

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09 | HalluPeer: A Taxonomy-driven Benchmark for Detecting Hallucinations in Scientific Peer Reviews ↗ | benchmark、peer-review hallucination、source grounding、claim localization | 未确认（arXiv Comments：Accepted to EMNLP Findings 2026） | [arXiv](https://arxiv.org/abs/2609.03580) | [Code](https://github.com/Lin-TzuLing/HalluPeer) | 科学评审中的流畅但无依据批评，能否被针对长论文证据的 detector 区分和定位？ | 用论文、人工评审和 hallucination-injected review 的对齐三元组建立同行评审专用 taxonomy。 | 在 12K 论文和 38K 评审上做检测、分类与定位，并用真实评审检查模式是否存在。 | 现有 detector 难区分幻觉与合理批评，且定义的幻觉模式出现在真实评审中，需 source-aware verification。 |
| 2026-08 | Not Just Reason, Not Just Scan: Reinforcement Learning for Proactive Scientific Error Verification over Academic Paper | benchmark、scientific error verification、evidence alignment、reviewer training | 未确认（arXiv Comments：Accepted by EMNLP 2026 Findings） | [arXiv](https://arxiv.org/abs/2608.26596) | 暂未公开 | 针对 MLLM reviewer 只有在预先给出问题或证据时才会核验、难以主动通读论文并形成可追踪判断 | 论文提出 VERA-RL | 并以覆盖六类科研流程错误的 12,900 样本 VERA-13K 联合奖励推理完整性、证据对齐与错误精度 | 训练后的 Qwen3-VL-8B 显著提升可核验推理，在 Scan 设置上接近 Gemini 3 Pro 与 Qwen3-VL-235B-A22B。 |
| 2026-08 | How Can Rhetoric Reward-Hack AI Reviewers? Dissecting Rhetorical Sensitivity in AI-Based Peer Review | analysis、rhetorical style、reward hacking、review score | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.08975) | [Code](https://github.com/MingLiiii/Dissecting_AI_Reviews) | 针对 AI reviewer 是否把 rhetoric 当作 scientific merit 不清楚。 | 针对 AI reviewer 是否把 rhetoric 当作 scientific merit 不清楚；论文构造内容受控的多种修辞版本并分解评分变化 | 关键实现：针对 AI reviewer 是否把 rhetoric 当作 scientific merit 不清楚；论文构造内容受控的多种修辞版本并分解评分变化。 | 结果表明部分表述策略可以系统性 reward-hack reviewer，评价系统需要把论证内容与语言包装分离。 |
| 2026-05 | PRISM: A Multi-Dimensional Benchmark for Evaluating LLM Peer Reviewers | benchmark、AI peer review、review validity、scientific judgment | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.26730) | [Project](https://khanhthanhdev.github.io/prism-page/) | 研究如何评测 AI peer review、review validity 风险，重点考察 scientific judgment 场景下的覆盖度与可复现性。 | PRISM 从分析深度、新颖性判断、缺陷识别与优先级、建设性四个维度评估 LLM reviewer | 并与人类审稿人发现科学问题的能力对照 | 结果揭示基于表面文本相似度的旧指标不足以衡量真实评审质量。 |
| 2026-05 | LLM-as-a-Reviewer: Benchmarking Their Ability, Divergence, and Prompt Injection Resistance as Paper Reviewers | benchmark、rating calibration、human divergence、prompt injection | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.25415) | 暂未公开 | 针对 AI reviewer 的校准、人类一致性和攻击鲁棒性缺少联合评测。 | 针对 AI reviewer 的校准、人类一致性和攻击鲁棒性缺少联合评测；论文在 898 篇 NeurIPS/ICLR 论文上比较 12 个 LLM 并植入不可见 font-mapping attack | 关键实现：针对 AI reviewer 的校准、人类一致性和攻击鲁棒性缺少联合评测；论文在 898 篇 NeurIPS/ICLR 论文上比较 12 个 LLM 并植入不可见 font-mapping attack。 | 结果模型普遍高估弱稿、低估 clarity 问题且对 hidden instruction 明显脆弱。 |
| 2026-05 | CoCoReviewBench: A Completeness- and Correctness-Oriented Benchmark for AI Reviewers | benchmark、review completeness、review correctness、expert discussion | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/65498) · [arXiv](https://arxiv.org/abs/2605.07905) | [Code](https://github.com/hexuandeng/CoCoReviewBench) | 研究如何评测 review completeness、review correctness 风险，重点考察 expert discussion 场景下的覆盖度与可复现性。 | 针对以 human-review overlap 为 gold 会奖励不完整甚至错误意见；论文从 reviewer-author-meta-review discussion 提取专家信号并构建 3,900 篇细粒度 benchmark | 关键实现：针对以 human-review overlap 为 gold 会奖励不完整甚至错误意见；论文从 reviewer-author-meta-review discussion 提取专家信号并构建 3,900 篇细粒度 benchmark。 | 结果当前 AI reviewer 在 correctness 与 hallucination 上仍受限，reasoning model 相对更强。 |
| 2026-04 | When AI reviews science: Can we trust the referee? | analysis、review lifecycle、causal probe、context poisoning | The Innovation Informatics 2026 | [Official](https://doi.org/10.59717/j.xinn-inform.2026.100030) · [arXiv](https://arxiv.org/abs/2604.23593) | 暂未公开 | 针对 AI peer review 风险散落在不同环节且缺少统一 security map；论文覆盖 training、desk review、deep review、rebuttal 与 system level | 并以 prestige、assertion、sycophancy 和 context poisoning 做对照实验 | 关键实现：并以 prestige、assertion、sycophancy 和 context poisoning 做对照实验。 | 结果定位了可被独立测试和缓解的多类失效点。 |
| 2025-09 | When Your Reviewer is an LLM: Biases, Divergence, and Prompt Injection Risks in Peer Review | analysis、reviewer bias、topic divergence、field-specific injection | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2509.09912) | 暂未公开 | 针对 AI reviewer 的公平性、一致性与 indirect injection 风险缺少真实论文比较。 | 针对 AI reviewer 的公平性、一致性与 indirect injection 风险缺少真实论文比较；论文在 1,441 篇 ICLR/NeurIPS 论文上对照人类评审并植入 covert instruction | 关键实现：针对 AI reviewer 的公平性、一致性与 indirect injection 风险缺少真实论文比较；论文在 1,441 篇 ICLR/NeurIPS 论文上对照人类评审并植入 covert instruction。 | 结果弱论文被系统性抬分，field-specific prompt 比泛化恶意指令更能定向操纵评审内容。 |

## Presentation 与 Rhetoric Gaming

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06 | No Hidden Prompts Needed! You Can Game AI Peer Review with Presentation-Only Revisions | attack、adversarial repackaging、black-box loop、presentation gaming | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.13044) | [Code](https://github.com/xyimatvoid/ARGAR) | 针对禁止 hidden prompt 后 AI reviewer 是否仍可被操纵；论文在不改变实验、公式、图表和数值的条件下 | 以 closed-loop black-box optimization 改写摘要、引言和贡献表述 | 关键实现：以 closed-loop black-box optimization 改写摘要、引言和贡献表述。 | 结果 presentation 本身成为可优化攻击面，安全问题不止是 prompt injection。 |
| 2026-06 | Gaming AI-Assisted Peer Reviews Poses New Risks to the Scientific Community | attack、abstract rewrite、score inflation、low-cost optimization | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.10159) | 暂未公开 | 针对普通科学润色能否在未知 reviewer 下改变评审。 | 针对普通科学润色能否在未知 reviewer 下改变评审；论文迭代生成并筛选语义保持的 abstract rewrite | 关键实现：针对普通科学润色能否在未知 reviewer 下改变评审；论文迭代生成并筛选语义保持的 abstract rewrite。 | 最强设置约 38% attack success，初始 reject 稿超过 50%，且一次十页稿件攻击约需五分钟和一美元。 |
| 2026-05 | Review Arcade: On the Human Alignment and Gameability of LLM Reviews | analysis、draft-revise loop、human alignment、review gameability | 未确认（arXiv Comments：Under review at EMNLP 2026） | [arXiv](https://arxiv.org/abs/2605.28897) | [Code](https://github.com/uhh-hcds/reviewarcade) | 针对作者用同一类 AI review 反复修改论文是否会 game evaluator。 | 针对作者用同一类 AI review 反复修改论文是否会 game evaluator；论文在 ACL Rolling Review 稿件上比较 prompt/model stability 与 iterative draft-revise | 关键实现：针对作者用同一类 AI review 反复修改论文是否会 game evaluator；论文在 ACL Rolling Review 稿件上比较 prompt/model stability 与 iterative draft-revise。 | 结果人机对齐随设置剧烈变化，部分场景中最多 35% 论文的 overall score 显著提高。 |
| 2026-01 | Paraphrasing Adversarial Attack on LLM-as-a-Reviewer | attack、semantic-preserving paraphrase、black-box optimization、score manipulation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.06884) | 暂未公开 | 针对 prompt injection 会混淆 instruction following 与评审鲁棒性；论文用历史 paraphrase 与得分指导黑盒搜索 | 在保持语义和自然度时提高 review score | 关键实现：在保持语义和自然度时提高 review score。 | 结果跨会议、reviewer 与 attack model 均有效，并观察到 review perplexity 可作为潜在检测信号。 |

## Hidden Prompt 与 Multimodal Attack

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06 | Does AI Reviewer See the Full Picture? Attacking and Defending Multimodal Peer Review | benchmark、multimodal review、figure attack、chunk localization | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/61968) · [arXiv](https://arxiv.org/abs/2606.12716) | [Code](https://github.com/UNITES-Lab/PaperGuard) · [Project](https://paper-guard.github.io/) | 针对 text-only robustness 忽略 figure 承载的关键科学证据；论文发布 PaperGuard | 联合 text prompt injection、GCG 和 figure PGD attack | 并以 chunk embedding search 与 intent verification 定位攻击 | 结果商业与开源 reviewer 均脆弱，纯视觉扰动也能显著抬分。 |
| 2025-12 | ChatGPT: Excellent Paper! Accept It. Editor: Imposter Found! Review Rejected | analysis、PDF injection、LLM-review detection、editorial integrity | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2512.20405) | 暂未公开 | 分析 LLM-review detection、PDF injection 风险的形成机制，重点考察 editorial integrity 对安全行为的影响。 | 针对作者可用隐藏 PDF prompt 操纵 AI reviewer 且 editor 难识别机器评审；论文同时提出攻击演示与由编辑植入 invisible trigger 的 inject-and-detect 构想 | 关键实现：针对作者可用隐藏 PDF prompt 操纵 AI reviewer 且 editor 难识别机器评审；论文同时提出攻击演示与由编辑植入 invisible trigger 的 inject-and-detect 构想。 | 结论是该机制可揭示部分 LLM-generated review，但本身也带来伦理和误判边界。 |
| 2025-11 | "Give a Positive Review Only": An Early Investigation Into In-Paper Prompt Injection Attacks and Defenses for AI Reviewers | attack、in-paper injection、iterative prompt、adaptive bypass | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2511.01287) | 暂未公开 | 针对论文内隐藏指令尚无系统攻击基线；论文比较固定 prompt 与面向 simulated reviewer 迭代优化的 injection | 并测试简单 detector | 关键实现：并测试简单 detector。 | 结果攻击可频繁诱导满分，检测虽降低 ASR 但会被 adaptive attacker 部分绕过。 |
| 2025-08 | Misleading Large Language Models used (or misused) in Scientific Peer-Reviewing via Hidden Prompt-Injection Attacks | attack、hidden PDF text、review manipulation、detectability evasion | ACM TAISAP 2026 | [Official](https://doi.org/10.1145/3803804) · [arXiv](https://arxiv.org/abs/2508.20863) | 暂未公开 | 针对不同动机的作者能否用人眼不可见内容影响 LLM reviewer；论文形式化三类 threat model | 并跨 review prompt、商业模型和已发表论文测试 adversarial instruction | 关键实现：并跨 review prompt、商业模型和已发表论文测试 adversarial instruction。 | 结果攻击可稳定改变评审，还可通过设计降低 automated content check 的可见性。 |
| 2025-06 | Breaking the Reviewer: Assessing the Vulnerability of Large Language Models in Automated Peer Review Under Textual Adversarial Attacks | benchmark、textual attack、automated review、robustness evaluation | EMNLP 2025 Findings | [ACL Anthology](https://aclanthology.org/2025.findings-emnlp.259/) | [Code](https://github.com/Lin-TzuLing/Breaking-the-Reviewer) | 针对 automated reviewer 的生成质量与 adversarial robustness 缺少统一比较。 | 针对 automated reviewer 的生成质量与 adversarial robustness 缺少统一比较；论文对人类评审和多种文本操纵下的 LLM review 做系统评测 | 关键实现：针对 automated reviewer 的生成质量与 adversarial robustness 缺少统一比较；论文对人类评审和多种文本操纵下的 LLM review 做系统评测。 | 结果表面文本变化可显著扭曲模型判断，说明部署前必须把 attack robustness 纳入评估。 |

## 防御与部署约束

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04 | SafeReview: Defending LLM-based Review Systems Against Adversarial Hidden Prompts | defense、co-evolutionary training、adaptive injection、ranking preservation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.26506) | 暂未公开 | 针对 system prompt、固定 detector 和一次性 adversarial training 难覆盖演化攻击。 | 针对 system prompt、固定 detector 和一次性 adversarial training 难覆盖演化攻击；论文联合训练生成 injection 的 Generator 与保持 clean/attacked review 一致的 Defender | 关键实现：针对 system prompt、固定 detector 和一次性 adversarial training 难覆盖演化攻击；论文联合训练生成 injection 的 Generator 与保持 clean/attacked review 一致的 Defender。 | 结果相对静态防御更能保持论文排序并跨 attacker architecture 泛化。 |

## Position Paper

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05 | Stop Automating Peer Review Without Rigorous Evaluation | analysis、review automation、hivemind effect、paper laundering | ICML 2026 Oral | [Official](https://icml.cc/virtual/2026/poster/67247) · [arXiv](https://arxiv.org/abs/2605.03202) | 暂未公开 | 分析 review automation、hivemind effect 风险的形成机制，重点考察 paper laundering 对安全行为的影响。 | 针对 submission overload 被直接用作自动化评审的部署理由；立场论文比较 ICLR 2026 人类与 AI review 并测试自动改写 | 关键实现：针对 submission overload 被直接用作自动化评审的部署理由；立场论文比较 ICLR 2026 人类与 AI review 并测试自动改写。 | 结果 AI reviewer 存在过度一致的 hivemind effect 且可被 paper laundering 抬分，主张先建立 peer-review automation science 再部署。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026 | BadScientist: Can a Research Agent Write Convincing but Unsound Papers that Fool LLM Reviewers? | analysis、agent safety、LLM agent、AI peer review | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1134/) | 暂未公开 | 针对 AI 生成研究再由 AI 审稿形成无人工闭环 | BadScientist 不做真实实验却用呈现操纵生成论文 | 最高获 82% 接收率 | 现有缓解的完整性检测仅略高于随机。 |

## Survey 与 Taxonomy

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026 | CoCoNUTS: Concentrating on Content while Neglecting Uninformative Textual Styles for AI-Generated Peer Review Detection | survey、AI-generated content、AI peer review、review validity | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1240/) | 暂未公开 | 梳理 AI-generated content、AI peer review 研究，重点总结 review validity 的方法谱系与开放问题。 | CoCoNUTS 以 315,535 篇评审覆盖六种人机协作模式 | CoCoDet 聚焦实质内容而非文风，macro-F1 达 98.24% | 对政策允许的机器润色误报率仅 3.89%。 |

> 引用真实性和 claim-source support 的专门检测见 [Citation and Evidence Integrity](citation-and-evidence-integrity.md)；一般 indirect prompt injection 见 [Prompt Injection](../misc/prompt-injection.md)。
