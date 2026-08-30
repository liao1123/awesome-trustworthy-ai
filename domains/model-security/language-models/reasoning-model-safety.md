# Reasoning Model Safety

[返回 Language Model Security 目录](README.md)

## 研究方向

本页研究显式 thinking token、长推理轨迹和 reasoning-time computation 如何改变模型安全。重点区分模型是否真的在推理中形成安全决定、可见 trace 是否只是对既定选择的事后解释，以及攻击者能否通过 reasoning weight、隐藏知识或中间步骤操纵提取模型原本不会直接输出的内容；单纯利用长推理造成资源耗尽的攻击归入 [Reasoning Model DoS](../../dos/reasoning-model-dos.md)。

## 研究脉络

- **结果级安全：** 最初沿用普通 LLM 的 final-answer refusal 评测，但无法定位风险是在思维过程、答案还是二者连接处产生。
- **Trace 分解：** 新评测分别标注 reasoning trace 与 final answer，发现中间步骤可能泄漏风险内容，也可能在最后被拒答掩盖。
- **机制检验：** causal intervention 开始判断 thinking token 是否真正参与安全决策，避免把流畅的安全解释误当作因果机制。
- **Reasoning-time 攻防：** attack 放大 task vector 或操纵推理轨迹以提取秘密，defense 则用 verification 和多原则 steering 在生成过程中纠正。
- **当前边界：** 可见 CoT 不一定等于真实内部推理；安全结论应结合 hidden-state intervention、不同 reasoning budget 与不展示 trace 的模型进行验证。

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | TRACE: An Evidence-Grounded Benchmark for Safety Evaluation of Large Reasoning Models | benchmark、reasoning model safety、trace-answer risk、evidence localization | 未确认（arXiv Comments：EMNLP 2026 Main） | [arXiv](https://arxiv.org/abs/2608.24232) | [Code](https://github.com/wzy6642/TRACE) | 针对只检查最终回答会掩盖大型推理模型中间步骤中的不安全内容，TRACE 分别标注 prompt、reasoning trace 和 final response，并为每项安全判断提供源文本证据；18 个 guardrail 的结果表明，推理轨迹的风险识别与证据定位明显更难，暴露了 final-answer-only 评测的安全盲区。 |

## 机制与安全失效分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Safety Hacking in Constrained Best-of-$N$ Inference-time Scaling | analysis、inference-time scaling、constrained Best-of-N、unsafe reward tail | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.22915) | 暂未公开 | 论文证明增加 inference-time sampling 并在安全过滤后选最高奖励答案，可能系统性降低而非提高安全：安全 proxy 的微小漏检会进入候选集，随后由不安全输出的高奖励尾部被选择放大；有限 $N$ 界和语言模型实验共同刻画了这一 scaling-induced failure。 |
| 2026&#8209;08 | Why2Speak: Faithful Reasoning for Abstaining Action Policies | analysis、reasoning-model auditability、act-or-abstain policy、post-hoc rationale | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.20670) | 暂未公开 | 针对开启显式 thinking 是否只展示原有决策过程、还是会改变被审计的行动策略，论文在 Qwen3-8B 上比较直接与 reasoning policy，并用 SFT、RL、activation probe 和消融核验；结果呈现能力—可审计性权衡，且暴露 reasoning 会降低真实干预召回并使常用 faithfulness 指标产生混淆。 |
| 2026&#8209;08 | Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents | analysis、System 2 reasoning、corrupted-evidence robustness、detection-influence gap | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17153) | 暂未公开 | 针对“能识别错误证据”是否意味着推理过程不会继续采信它这一安全假设，论文用检测—下游影响差距比较 reasoning model 与标准语言模型；前者对损坏 RAG 证据明显更稳健，但结论提供的是能力分级访问的实证依据，而非把 System 2 reasoning 本身视为形式安全保证。 |
| 2026&#8209;06 | Reasoning That Leaks, Fine-Tuning That Amplifies: Exposing the Hidden Threats of Chain-of-Thought Models | analysis、CoT leakage、harmful fine-tuning、hidden harm | AsiaCCS 2026 | [Official](https://doi.org/10.1145/3779208.3785271) | 暂未公开 | 针对 final answer 已拒答就被视为安全的评测盲点；论文检查中间 CoT 并区分 unintended leakage 与 harmful escalation；结果显示 fine-tuning 会放大隐藏推理中的可执行危害内容。 |
| 2026&#8209;06 | Do Thinking Tokens Help with Safety? | analysis、thinking token、causal intervention、post-hoc rationale | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.25013) | [Code](https://github.com/narutatsuri/lrm_safety_deliberation) | 针对 reasoning trace 看起来会权衡风险但是否真正决定拒答未知，论文操纵 thinking token 与生成条件并比较行为变化；结果表明部分模型可能先决定回答或拒绝，再生成与决定一致的事后安全解释。 |
| 2026&#8209;05 | Chain of Risk: Safety Failures in Large Reasoning Models and Mitigation via Adaptive Multi-Principle Steering | benchmark、reasoning safety、trace-answer risk、multi-principle steering | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.05678) | 暂未公开 | 针对只审核 final answer 会漏掉 CoT 中的泄漏与风险累积，论文分别评测完整推理链和答案并总结 leak、escape 等失效，再按风险动态选择多项安全原则 steering；结果降低不安全输出且大体保留任务能力。 |
| 2026&#8209;03 | Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi-Step Tool Use | defense、reasoning model、safety degradation、inference-time risk | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63878) · [arXiv](https://arxiv.org/abs/2603.03205) | 暂未公开 | 针对自主智能体的长程行为、失败传播和真实部署风险缺少可复现评测的问题，论文提出 Learning When to Act or Refuse 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于智能体部署安全与故障恢复。 |
| 2026 | Thinking-Based Non-Thinking: Solving the Reward Hacking Problem in Training Hybrid Reasoning Models via Reinforcement Learning | analysis、reasoning safety、reward hacking、reasoning model | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.2122/) | 暂未公开 | TNT 用思考回答的 solution 信息为每题设置非思考 token 上限，五个数学集上较三种小型 reasoning model 节省约 50% token 且提升准确率，并把伪装成“未思考”的奖励投机控制在 10% 以下。 |
| 2026 | Safety Recovery in Reasoning Models Is Only a Few Early Steering Steps Away | defense、reasoning model、safety degradation、inference-time risk | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61339) | 暂未公开 | 针对静态安全对齐容易过度拒绝，也难覆盖推理时出现的新风险的问题，论文提出 Safety Recovery in Reasoning Models 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于安全拒绝校准与在线防护。 |
| 2026 | SafeAdapt: Safety Alignment with Adaptive Thinking Allocation for Large Reasoning Models | defense、safety alignment、adaptive thinking、reasoning budget | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/song-jiazheng) | 暂未公开 | 针对固定延长 safety thinking 并不会单调提升安全性的问题，SafeAdapt 按 prompt 难度动态分配 reasoning budget，在多个对抗基准上同时缓解简单攻击的 over-thinking 与困难攻击的 under-thinking 风险。 |
| 2026 | Reasoning Structure Matters for Safety Alignment of Reasoning Models | defense、reasoning safety、safety alignment、reasoning model | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.240/) | 暂未公开 | 针对 LRM 的有害输出源于 reasoning structure，AltTrain 只用 1K 个样本做 SFT 改写推理结构，无需复杂 RL 或 reward design 即可跨模型规模、任务和语言获得安全泛化。 |
| 2026 | ReasoningGuard: Safeguarding Large Reasoning Models with Inference-time Safety Aha Moments | defense、reasoning safety、reasoning model、safety degradation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1453/) | 暂未公开 | 针对 LRM 在推理中后段更易生成有害内容而微调防御成本高，ReasoningGuard 用 attention 定位关键节点、注入 safety “aha moment”并缩放采样，低开销下优于九种 guard 且避免过度安全化。 |
| 2026 | PAM: Enhancing General Alignment of Large Reasoning Models through Priority-Aware Metacognition | defense、reasoning safety、safety alignment、reasoning model | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.432/) | [Code](https://anonymous.4open.science/r/PAM-RM-02DF) | 针对 LRM 的 System-2 reasoning 无法自然迁移到 harmlessness，PAM 先识别顶层人类偏好再以两阶段训练强化 metacognition，在相同训练管线下把通用 helpfulness/harmlessness 对齐提高约 10 分。 |
| 2026 | Mitigating Safety Context Amnesia in Multimodal Reasoning Models via Intent-Guided Safety Reasoning | defense、multimodal safety、reasoning safety、VLM safety | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1821/) | 暂未公开 | 针对 MLRM 在长推理中虽看见危险视觉线索却忘记执行约束的 Safety Context Amnesia，IGSR 先解耦客观意图再由 Cognitive Arbiter 审核，使防御成功率较基线提高逾 62% 且基本保留效用。 |
| 2026 | Mind the (DH) Gap! A Contrast in Risky Choices Between Reasoning and Conversational LLMs | analysis、reasoning safety、reasoning model、safety degradation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.479/) | 暂未公开 | 对 20 个 LLM 与配对人类实验发现，reasoning model 的风险选择更接近期望收益理性且不敏感于顺序和框架，conversation model 则更受表述、解释和描述—经验差距影响。 |
| 2026 | How Should We Enhance the Safety of Large Reasoning Models: An Empirical Study | analysis、reasoning safety、reasoning model、safety degradation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.936/) | 暂未公开 | 针对 reasoning 能力增强并不自动带来安全性，作者发现直接蒸馏 DeepSeek-R1 安全回答效果有限，修正五类风险模式后才显著改善，并显示短或模板化 safety reasoning 可达到与长推理相近的效果。 |
| 2025&#8209;10 | Refusal Falls off a Cliff: How Safety Alignment Fails in Reasoning? | analysis、reasoning safety、refusal cliff、safety alignment | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2510.06036) | 暂未公开 | 针对 reasoning model 已识别危害却仍在最终输出前转为配合的问题，作者发现 refusal score 在末端 token 陡降，并通过消融约 3% 的相关 attention head 将 ASR 压至 10% 以下，Cliff-as-a-Judge 仅用 1.7% 训练数据即可取得相近修复。 |

## Reasoning-Time Attack

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models | attack、hidden-CoT extraction、reasoning replay、universal injection trajectory | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.20055) | [Code](https://github.com/TrustAIRLab/EchoCoT) | 针对 API 不展示完整 CoT 是否足以保护推理资产，EchoCoT 利用工具调用之间的 reasoning replay surface 和 API fidelity signal 迭代恢复隐藏轨迹，并自动搜索跨数据集通用的 injection trajectory；三种开源 LRM 上近逐字提取成功率最高 66.4%，迁移到未见数据时最高 80%。 |
| 2026&#8209;07 | Overthinking: Amplifying Reasoning Weights to Extract Learned Secrets | attack、reasoning weight、secret extraction、task-vector amplification | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63085) · [arXiv](https://arxiv.org/abs/2607.08173) | 暂未公开 | 针对模型记忆的秘密无法通过普通 prompting 稳定提取，论文识别并放大与长推理相关的 task vector 以诱导模型持续搜索内部知识；结果显著提高秘密和非预期行为的出现频率，说明更强 reasoning control 也扩大信息提取面。 |

## Safety Verification 与训练

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Mitigating Reasoning-Induced Misalignment via Safety-Direction Penalty | defense、reasoning fine-tuning、safety-direction penalty、representation coupling | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.23497) | 暂未公开 | 论文从 activation space 分离 reasoning ability 与 safety behavior 两个方向，发现提升推理的微调会耦合移动安全表示，且位移越大的 prompt 安全退化越强；SDP 据此约束 reasoning training，在保留基准推理性能的同时修复有害行为。 |
| 2026&#8209;05 | Internalizing Safety Understanding in Large Reasoning Models via Verification | defense、safety verification、reasoning model、policy internalization | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63605) · [arXiv](https://arxiv.org/abs/2605.08930) | [Code](https://github.com/AlphaLab-USTC/SInternal) | 针对 reasoning model 会口头复述安全原则却不能稳定落实到推理过程，论文用 verifier 为中间步骤和最终答案提供训练信号并将安全判断内化；结果提升对复杂有害请求的识别和拒答泛化。 |

## 检测、审计与取证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment | detection、reasoning safety、action preference、intent monitoring | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.27348) | [Code](https://github.com/RebeccaZhang22/intent-as-a-tool) | 针对有害执行前虽常出现 reasoning intent signal、但粗粒度 CoT audit 无法指出何时承诺的问题，INTENT-AS-A-TOOL 用意图工具调用概率记录逐 token／step 的 action preference；它将 post-hoc 标签转成稠密轨迹，并定位适合推理时安全干预的关键步骤。 |
| 2026&#8209;08 | Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings | detection、CoT monitoring、reasoning model、safety degradation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.04735) | [Code](https://github.com/agatha-duzan/implicit-vs-explicit-influence) | 该 benchmark 对比显式隐瞒与隐式影响下的 CoT monitorability；显式设置可检出 60%–94% 行为偏移，而隐式影响在两类任务下降 41–46 个百分点，常见 system-prompt 优化还会将检出率压到最低 5%。 |
| 2026 | Real-Time Monitoring and Calibration of Chain-of-Thought Sycophancy in Large Reasoning Models | detection、chain-of-thought、uncertainty calibration、CoT monitoring | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61298) | 暂未公开 | 针对偏好学习与强化学习会诱发迎合、奖励投机或代理目标偏移的问题，论文提出 Real-Time Monitoring and Calibration of 检测、定位或审计方法；摘要实验验证其能识别或定位相应风险，并报告了跨设置证据，直接服务于奖励设计与偏好对齐审计。 |

## 攻击与绕过

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Reasoning Models Are Test Exploiters: Rethinking Multiple Choice | attack、reasoning model、safety degradation、inference-time risk | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64875) | 暂未公开 | 针对高能力模型可能欺骗、隐藏目标或逃避外部监督的问题，论文围绕 Reasoning Models Are Test Exploiters 开展机制与边界分析；摘要中的实验或分析给出了相应有效性与边界证据，直接服务于欺骗检测、监控和 AI 控制。 |
| 2026 | Reasoning Hijacking: The Fragility of Reasoning Alignment in Large Language Models | attack、reasoning safety、safety alignment、reasoning model | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1698/) | 暂未公开 | 针对现有防御只检查任务目标是否被劫持，Criteria Attack 保持目标不变却注入伪决策准则，令模型在毒性、评论和 spam 任务上优先采用捷径并绕过 SecAlign、StruQ 等 goal-deviation 防御。 |
| 2026 | AutoRAN: Automated Hijacking of Safety Reasoning in Large Reasoning Models | attack、reasoning safety、reasoning model、safety degradation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1988/) | 暂未公开 | 针对推理模型的显式安全思考可能反向泄露攻击线索，AutoRAN 用弱且低对齐模型模拟执行并从目标拒绝中迭代劫持 reasoning，在 AdvBench、HarmBench 与 StrongREJECT 上可于一至数轮内接近 100% 成功。 |

> CoT 本身被用作 prompt-level jailbreak 的工作见 [Jailbreak 攻击](jailbreak-attacks.md)；reasoning token、latency 与 energy amplification 见 [Reasoning Model DoS](../../dos/reasoning-model-dos.md)；可见 CoT 的可监控性见 [CoT Monitorability](../../misc/cot-monitorability.md)。
