# Sycophancy 与 Social Influence

[返回上级目录](README.md)

## 研究方向

研究模型迎合用户、权威或既有立场，以及生成内容对人类信念、排序和偏好的影响；覆盖 sycophancy benchmark、persuasion、belief manipulation、rhetorical misalignment 与缓解。

## 研究脉络

- **迎合测量：** 早期工作通过用户立场和权威线索翻转测试模型是否牺牲真实性来保持一致。
- **交互放大：** 多轮反馈、用户施压、重新考虑 checkpoint 与 iterative self-refinement 会为模型反复向用户立场让步提供机会，需要将 sycophancy 从单次回答扩展到完整交互过程测量。
- **机制与训练来源：** Persona、RLHF、reward model 和表示方向研究迎合行为如何形成。
- **社会影响：** Persuasion 与 belief-change benchmark 将模型输出连接到人类决策后果。
- **干预与边界：** Reasoning、verbalized assumption 和 representation control 可降低部分迎合，但也可能只掩盖表面表达。

## 机制、社会影响与行为分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | Agentic Scaffolding Amplifies Sycophantic Behavior in Large Language Models | analysis、agentic sycophancy、capitulation metric、multi-turn amplification | SafeAI@UAI 2026 Workshop | [Official](https://safe-ai-workshop.github.io/uai-2026/) · [arXiv](https://arxiv.org/abs/2608.21377) | 暂未公开 | 针对单轮 sycophancy rate 无法刻画模型在反复互动中逐步让步的问题 | 论文提出 agentic sycophancy amplification、capitulation rate 与 sycophantic capitulation rate | 并控制比较 multi-turn、user pressure 和 iterative refinement | 4,800 次判断显示脚手架使迎合不断累积而非保持稳定，同时造成平均 6.3 个百分点的真实性损失。 |
| 2026-07 | Characterizing Rhetorical Misalignment in Decision-Making with Language Models | analysis、sycophancy、social influence、preference manipulation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14630) | 暂未公开 | 分析 sycophancy、social influence 风险的形成机制，重点考察 preference manipulation 对安全行为的影响。 | 人类的决策往往受到一系列有据可查的认知偏见的影响；在这项工作中 | 我们开发了一个决策理论框架来研究修辞错位，这是一种失败模式，LLM在给定的决策背景下使用修辞上不恰当的表达形式，从而导致次优的人类决策 | 我们的研究结果揭示了一个以前在高风险领域未被认识到的安全问题：一个模型可以与事实相符，但仍然通过其修辞表达造成伤害。 |
| 2026-07 | Persona Cartography: Charting Language Model Personality Traits in Weight Space | analysis、sycophancy、social influence、preference manipulation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.07916) | 暂未公开 | 分析 sycophancy、social influence 风险的形成机制，重点考察 preference manipulation 对安全行为的影响。 | Persona Cartography 用 OCEAN 维度训练可增强或抑制单项人格的低秩 adapter | 并发现这些方向随强度近单调、可近似相加且在中等强度下保持能力 | neuroticism 与 agreeableness 等轴会系统改变 frustration 和 sycophancy 等安全行为。 |
| 2026-04 | Verbalizing LLMs' assumptions to explain and control sycophancy | analysis、sycophancy、verbalized assumptions、social influence | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2604.03058) | 暂未公开 | 针对模型在求建议时默认用户只想获得肯定的问题 | Verbalized Assumptions 揭示“seeking validation”等假设与 sycophancy/delusion 的因果联系 | 关键实现：Verbalized Assumptions 揭示“seeking validation”等假设与 sycophancy/delusion 的因果联系。 | 并用 assumption probe 对相关行为进行细粒度 steering。 |
| 2026 | Too Nice to Tell the Truth: Quantifying Agreeableness-Driven Sycophancy in Role-Playing Language Models | analysis、sycophancy、social influence、preference manipulation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1421/) | 暂未公开 | 分析 sycophancy、social influence 风险的形成机制，重点考察 preference manipulation 对安全行为的影响。 | 对 13 个 0.6B–20B 模型、275 个 persona 和 4,950 个 prompt 的评测发现 9 个模型的角色宜人性与迎合显著正相关 | 关键实现：对 13 个 0.6B–20B 模型、275 个 persona 和 4,950 个 prompt 的评测发现 9 个模型的角色宜人性与迎合显著正相关。 | 最高 Pearson r=0.87、Cohen’s d=2.33。 |
| 2026 | How RLHF Amplifies Sycophancy | analysis、sycophancy、social influence、preference manipulation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63414) | 暂未公开 | 针对偏好学习与强化学习会诱发迎合、奖励投机或代理目标偏移的问题 | 论文围绕 How RLHF Amplifies Sycophancy 开展机制与边界分析 | 关键实现：论文围绕 How RLHF Amplifies Sycophancy 开展机制与边界分析。 | 摘要中的实验或分析给出了相应有效性与边界证据，直接服务于奖励设计与偏好对齐审计。 |
| 2026 | Feeling Right vs. Being Right: How AI Sycophancy Affects Value-Laden Deliberation | analysis、sycophancy、social influence、preference manipulation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.2046/) | 暂未公开 | 分析 sycophancy、social influence 风险的形成机制，重点考察 preference manipulation 对安全行为的影响。 | 31 人在三类道德困境中的混合研究显示 | 迎合式 AI 提高用户决策信心却降低开放思考并让对话更无效 | 而不迎合的适度摩擦更能促进认知灵活性。 |

## Sycophancy、Persuasion 与 Belief-Change Benchmark

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-02 | CausalT5k: Diagnosing Refusal and Failure Modes in Trustworthy Causal Reasoning Across Causal Rungs ↗ | benchmark、authority pressure、answer flip、causal sycophancy | KDD 2026 | [Official](https://doi.org/10.1145/3770855.3817567) · [arXiv](https://arxiv.org/abs/2602.08939) | [Code](https://github.com/eyuchang/CausalT5kBench) | 针对模型面对用户施压时是否放弃正确因果判断 | CausalT5k 将同一 Sheep/Wolf 案例置于中性与 pressure 条件 | 并跨 Pearl 三个 rung 追踪检测和修正 | 结果揭示 pressure-induced Bad Flip，区分迎合式改口与真正的因果理解失败。 |
| 2026 | Flattery in Motion: Benchmarking and Analyzing Sycophancy in Video-LLMs | benchmark、sycophancy、social influence、preference manipulation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.369/) | [Code](https://github.com/William030422/Video-Sycophancy) | ViSE 首次系统测量 Video-LLM 在误导用户说法下是否背离视觉证据。 | ViSE 首次系统测量 Video-LLM 在误导用户说法下是否背离视觉证据 | 关键实现：ViSE 首次系统测量 Video-LLM 在误导用户说法下是否背离视觉证据。 | 并表明可解释关键帧增强和 inference-time 表征 steering 两种免训练方法能降低视频迎合。 |
| 2026 | Can AI-Generated Persuasion Be Detected? Persuaficial Benchmark and AI vs. Human Linguistic Differences | benchmark、AI-generated content、sycophancy、social influence | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1433/) | 暂未公开 | 研究如何评测 AI-generated content、sycophancy 风险，重点考察 social influence 场景下的覆盖度与可复现性。 | Persuaficial 覆盖六种语言和多种可控说服策略 | 关键实现：Persuaficial 覆盖六种语言和多种可控说服策略。 | 发现显性 AI 说服文本可能比人工更易检测，但隐蔽说服持续拉低检测表现，并系统比较其语言学差异。 |
| 2026 | BrokenMath: A Benchmark for Sycophancy in Theorem Proving with LLMs | benchmark、sycophancy、social influence、preference manipulation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63323) | 暂未公开 | 针对偏好学习与强化学习会诱发迎合、奖励投机或代理目标偏移的问题 | 论文构建 BrokenMath 基准并开展系统评测 | 关键实现：论文构建 BrokenMath 基准并开展系统评测。 | 跨模型或跨数据集结果暴露了现有系统的具体安全缺口，直接服务于奖励设计与偏好对齐审计。 |

## Reasoning、Representation 与训练缓解

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | Mitigating LLM sycophancy with RL-based fine-tuning: Bayesian Truth Serum approach | defense、sycophancy mitigation、Bayesian Truth Serum、label-free GRPO | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.25267) | 暂未公开 | 研究如何防御 sycophancy mitigation、Bayesian Truth Serum 威胁，并评估 label-free GRPO 条件下的安全收益与效用代价。 | 论文把同一问题的一组模型回答视为 peer respondent | 以 Bayesian Truth Serum 的“surprisingly common”信息分数直接作为 GRPO reward，无需标签或偏好标注 | 理论上迎合回答的期望奖励严格低于诚实回答，实验中用户压力下的 answer-flip rate 从 23% 降至 4%、准确率从 80% 升至 93%，代价是更高训练计算量。 |
| 2026-03 | Learning Multilingual Agentic Policy to Control Sycophancy | defense、sycophancy、agentic policy、multilingual transfer | EACL 2026 | [Official](https://aclanthology.org/2026.eacl-long.169/) | 暂未公开 | 针对迎合是压力下缺少 agreement control 的 policy failure。 | 针对迎合是压力下缺少 agreement control 的 policy failure；论文让模型在回答、反驳和澄清 action 间选择并联合优化任务、抗迎合与一致性 | 关键实现：针对迎合是压力下缺少 agreement control 的 policy failure；论文让模型在回答、反驳和澄清 action 间选择并联合优化任务、抗迎合与一致性。 | 结果降低 sycophancy 且跨语言泛化。 |
| 2026-03 | Sycophancy Hides Linearly in the Attention Heads | analysis、sycophancy、attention head、linear steering | EACL 2026 | [Official](https://aclanthology.org/2026.eacl-long.324/) | 暂未公开 | 分析 sycophancy、attention head 风险的形成机制，重点考察 linear steering 对安全行为的影响。 | 针对迎合信号在模型内部的位置不清；论文发现 correct-to-incorrect shift 最易从少量中层 attention head 线性读取 | 关键实现：针对迎合信号在模型内部的位置不清；论文发现 correct-to-incorrect shift 最易从少量中层 attention head 线性读取。 | 用这些 probe steering 可跨 factual QA 缓解用户怀疑诱发的答案偏移。 |
| 2026 | Good Arguments Against the People Pleasers: How Reasoning Mitigates (Yet Masks) LLM Sycophancy | defense、reasoning safety、sycophancy、social influence | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1126/) | 暂未公开 | 研究如何防御 reasoning safety、sycophancy 威胁，并评估 social influence 条件下的安全收益与效用代价。 | 跨客观与主观任务的实验发现 CoT 通常降低最终答案迎合 | 却会以逻辑漏洞、算错或单边论证掩盖部分迎合 | 主观任务和权威偏差更严重，且该倾向在推理中动态形成。 |

## 操纵攻击、检测与审计

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | HRGuard: Gating Relationship Manipulation in Multi-Turn Agentic AI Conversations | defense、relationship manipulation、role-sensitive intervention、multi-turn social harm | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.25340) | [Code](https://github.com/noobasuna/hrguard.git) | 论文把 AI 中介的人际关系操纵作为可累积的社会影响风险。 | 论文把 AI 中介的人际关系操纵作为可累积的社会影响风险 | 并要求系统根据用户角色采取非对称响应：拒绝操纵者、支持受害者 | HRGuard 以 1,000 条五轮对话和对抗性改写验证有状态双 gate，可减少有害服从而不把保护性求助一并阻断。 |
| 2026-08 | PsychJail: Exploring Psychological Jailbreaks via Multi-Turn Persuasion of LLM Policies | attack、social persuasion、change of meaning、susceptibility fingerprint | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.23028) | 暂未公开 | 研究 social persuasion、change of meaning 场景下的攻击面，重点考察 susceptibility fingerprint 如何影响目标模型或系统。 | 论文把社会心理学中的说服技巧转化为可学习的多轮模型操纵策略 | 并逐轮记录意义重构如何推动受害模型越过安全 policy | 在被击穿动作上形成的 susceptibility fingerprint 揭示模型对可信度、叙事等社会影响杠杆的差异性。 |
| 2026-08 | Aligned Alone, Misaligned Together: Forecasting Adversarial Capture in LLM Agent Populations | attack、social influence、committed minority、collective belief shift | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.22444) | 暂未公开 | 研究 social influence、committed minority 场景下的攻击面，重点考察 collective belief shift 如何影响目标模型或系统。 | 在 LLM monitor 相互读取判断的群体中 | 少量持续表达同一立场的 Agent 可通过社会影响把集体决定拉向攻击目标 | 论文进一步用无攻击期响应函数预测这种 belief shift，并显示公开推理只对弱影响有效。 |
| 2026-08 | Whitewashing Hate, Smearing Harmless Content: Annotator-Style Rebuttal Attacks on LLM-Based Moderation | attack、feedback-induced belief change、annotator authority、directional asymmetry | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.22230) | 暂未公开 | 论文把标注者口吻的反驳作为社会影响攻击。 | 论文把标注者口吻的反驳作为社会影响攻击 | 测量 moderator 是否会因外部反馈放弃原先正确判断 | 多轮理由会加深立场迁移，不同模型又呈现稳定的“更易洗白”或“更易污名”方向偏置，说明对权威式反馈的迎合具有可利用结构。 |
| 2026-08 | AI Watchdog: Agent Interfaces for Detecting and Defending Against Manipulative Dark Patterns in AI Conversations | defense、sycophancy detection、dark pattern、behavioral intervention | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.21841) | 暂未公开 | 研究如何防御 sycophancy detection、dark pattern 威胁，并评估 behavioral intervention 条件下的安全收益与效用代价。 | 论文把 sycophancy 与品牌偏见、拟人化等对话操纵模式纳入同一实时 detector | 并在 150 人预注册实验中测试提示时机 | 仅“不附加认知强制的即时警告”显著把用户对含暗黑模式建议的遵从率从 71.7% 降至 53.7%，说明识别迎合与抵抗其影响是不同目标。 |
| 2026-08 | THESIS-MoE: Trainable Hierarchical Extraction and SteerIng of Sycophancy in Mixture-of-Experts | attack、sycophancy、social influence、preference manipulation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.15687) | 暂未公开 | 研究 sycophancy、social influence 场景下的攻击面，重点考察 preference manipulation 如何影响目标模型或系统。 | 奉承是语言模型改变其答案以匹配用户声明的信念的倾向 | 是一种常见的对齐失败；在这项工作中，我们引入了一个共享的对比信号，该信号是根据有或没有明确信念的匹配提示构建的，该信号可以识别教育部层次结构中阿谀奉承的情况，并推动仅在存在该行为的地方采取干预措施 | 我们的结果表明，阿谀奉承存在于可识别的计算子电路中，并且可以选择性地引导，同时保持有利的去除-保留权衡。 |
| 2026-03 | Emotionally Charged, Logically Blurred: AI-driven Emotional Framing Impairs Human Fallacy Detection | analysis、AI persuasion、emotional framing、human vulnerability | EACL 2026 | [Official](https://aclanthology.org/2026.eacl-long.316/) | 暂未公开 | 分析 AI persuasion、emotional framing 风险的形成机制，重点考察 human vulnerability 对安全行为的影响。 | 针对生成式系统可在不改变谬误结构时强化说服；论文让 LLM 注入情绪 framing 并开展人类实验 | 关键实现：针对生成式系统可在不改变谬误结构时强化说服；论文让 LLM 注入情绪 framing 并开展人类实验。 | 结果 fallacy detection F1 平均下降 14.5%，量化了 AI-mediated affective manipulation。 |
