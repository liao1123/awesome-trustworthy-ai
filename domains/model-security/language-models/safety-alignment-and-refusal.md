# Safety Alignment 与 Refusal

[返回 Language Model Security 目录](README.md)

## 研究方向

本页研究语言模型如何内化安全 policy、形成 refusal，以及这种安全行为在模型表示、神经元、层和解码过程中的实现方式。核心问题包括自然语言 policy 如何低成本进入参数、refusal 是否依赖脆弱的低维方向、安全训练是否产生 alignment tax，以及部署时能否在生成过程中对风险提供有统计保证的监测；独立的输入输出审核器归入 [Guardrail](../../guardrails/README.md)。

## 研究脉络

- **行为对齐：** 早期方法用 demonstration、preference pair 和 safety tuning 直接塑造拒答行为，但容易引入 over-refusal 与 capability loss。
- **Policy 内化：** on-policy distillation 和 privileged-context teacher 将显式 policy 下的安全行为蒸馏进模型，减少每次 policy 更新所需的人工标注。
- **内部机制：** refusal direction、safety neuron 和 layer-wise decoding 揭示安全行为常集中在少量表示结构中，既便于干预，也形成可被攻击的脆弱点。
- **在线评测：** refusal score 与 sequential monitoring 把静态 benchmark 扩展到 token-level 风险轨迹，开始显式控制误报、漏报和干预时机。
- **当前边界：** 更高的拒答率不等于更安全；研究仍需同时报告 adaptive attack、over-refusal、通用能力和 policy 更新后的泛化。

## Policy 内化与低 Safety Tax 对齐

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Efficient Safety Alignment of Language Models via Latent Personality Traits | defense、latent personality traits、psychometric statement、safety generalization | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.07918) | 暂未公开 | 针对少量行为样本难以稳定塑造广泛安全倾向的问题，论文把 psychometric statement 表示为 latent personality trait 并以对抗训练稳定该方向；结果在多项安全评测上降低有害响应，同时基本保持通用能力。 |
| 2026&#8209;06 | PolicyAlign: Direct Policy-Based Safety Alignment for Large Language Models | defense、policy internalization、on-policy distillation、policy update | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.25442) | [Code](https://github.com/Qwen-Applications/PolicyAlign) | 针对新安全 policy 先出现而标注训练数据来不及构造的问题，论文从自然语言 policy 合成违规指令、筛选 policy-sensitive 样本并进行 on-policy self-distillation；结果让模型在推理时无需附带 policy 也能保持较低 over-refusal 的安全行为。 |
| 2026&#8209;06 | SafeSteer: Localized On-Policy Distillation for Efficient Safety Alignment | defense、localized distillation、safety token、alignment efficiency | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.02530) | [Project](https://anjingkun.github.io/SafeSteer/) | 针对整段响应蒸馏会把无关 token 一并更新并损害能力的问题，论文只在决定安全行为的局部 token 上执行 on-policy distillation；结果用少量有害样本提升拒答鲁棒性，同时减少对良性任务的干扰。 |
| 2026&#8209;05 | Reducing the Safety Tax in LLM Safety Alignment with On-Policy Self-Distillation | defense、on-policy self-distillation、privileged context、safety tax | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.15239) | 暂未公开 | 针对 safety tuning 提高安全性却损害通用能力的问题，论文让带 privileged safety context 的 teacher 指导模型自身 on-policy 输出；结果尤其在较小模型上改善 safety-utility trade-off。 |
| 2025&#8209;09 | Reasoned Safety Alignment: Ensuring Jailbreak Defense via Answer-Then-Check | defense、answer-then-check、reasoned refusal、jailbreak robustness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2509.11629) | 暂未公开 | 针对模型直接生成时可能在完成安全判断前输出有害内容的问题，论文训练模型先形成候选答案再按安全原则检查并修正；结果在越狱防御、over-refusal 和通用能力之间取得更稳定的平衡。 |

## Refusal 表示与内部机制

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | HARC: Coupling Harmfulness and Refusal Directions for Robust Safety Alignment | analysis、harmfulness direction、refusal direction、representation coupling | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.00572) | 暂未公开 | 针对只操纵 refusal direction 可能改变表面措辞却未校正有害性理解的问题，论文跨 prompt 与 response 位置配对 harmfulness 和 refusal 表示方向；结果说明耦合两类信号可得到更稳健的安全干预。 |
| 2026&#8209;06 | RAS: Measuring LLM Safety Through Refusal Alignment | analysis、refusal alignment score、layer window、white-box evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.25750) | 暂未公开 | 针对 judge-based 安全评测成本高且容易受输出表面形式影响的问题，论文在稳定层窗口中测量 hidden state 与 refusal direction 的对齐并校准为分数；结果该指标能更快跟踪攻击成功率与模型安全变化。 |
| 2026&#8209;06 | The Geometry of Refusal: Linear Instability in Safety-Aligned LLMs | analysis、refusal geometry、linear instability、activation steering | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.22686) | 暂未公开 | 针对安全对齐是否形成稳固决策边界的问题，论文用 classification-logit steering 与 prefix injection 检验 refusal geometry；结果显示拒答常沿近线性的低维轴组织，轻微双向操纵即可削弱或增强安全行为。 |
| 2026&#8209;06 | Deeper is Not Always Better: Mitigating the Alignment Tax via Confident Layer Decoding | analysis、confident layer decoding、entropy trough、alignment tax | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.21906) | 暂未公开 | 针对最终层安全对齐可能覆盖中间层已形成的有效回答并造成能力损失的问题，论文根据接近末层的 entropy trough 选择 confident layer 解码；结果表明适当较浅的表示可缓解 alignment tax，而非一律使用最深层。 |
| 2026&#8209;03 | CNT: Safety-oriented Function Reuse across LLMs via Cross-Model Neuron Transfer | defense、cross-model neuron transfer、function reuse、safety adaptation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.18449) | 暂未公开 | 不断变化的 safety requirement 使每个模型从头训练功能代价高；CNT 从 donor LLM 向 target LLM 转移极少量 neuron，以模块方式添加或删除 safety-oriented function；结果在七个模型上完成 alignment、disalignment 与 bias removal，多数通用性能下降低于 1%。 |
| 2026&#8209;03 | Knowing without Acting: The Disentangled Geometry of Safety Mechanisms in Large Language Models | analysis、recognition axis、execution axis、refusal erasure | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.05773) | [Artifact](https://anonymous.4open.science/r/DSH) | 模型识别 harmfulness 后是否必然执行 refusal 尚不清楚；DSH 将 safety computation 分为 Recognition Axis 与 Execution Axis，并用 causal steering 验证双重分离；结果显示深层中 knowing 与 acting 可结构性解耦，REA 可只擦除拒答执行。 |
| 2026&#8209;02 | SafeNeuron: Neuron-Level Safety Alignment for Large Language Models | defense、safety neuron、representation redundancy、preference optimization | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.12158) | 暂未公开 | 针对安全信息集中在少量神经元而易被剪枝或后续优化破坏的问题，论文在 preference optimization 中冻结已识别的 safety neurons 迫使模型学习冗余安全表示；结果提高对神经元移除和参数扰动的鲁棒性。 |

## 在线安全监测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Online Safety Monitoring for LLMs | detection、online monitoring、risk control、early intervention | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.02510) | 暂未公开 | 针对生成完成后才审核无法及时阻断风险的问题，论文在 token stream 上运行外部 verifier 并用统计 risk control 校准报警阈值；结果提供可解释的误报或漏报保证，并与 sequential testing 基线保持竞争力。 |

> 独立 guard model、classifier cascade 和内容审核系统见 [通用 Guard Model、评测与安全边界](../../guardrails/general-models-and-evaluation.md)；policy-adaptive safeguard 见 [Policy-Adaptive Guardrails](../../guardrails/policy-adaptive-guardrails.md)。
