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

## 机制与安全失效分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Do Thinking Tokens Help with Safety? | analysis、thinking token、causal intervention、post-hoc rationale | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.25013) | 暂未公开 | 针对 reasoning trace 看起来会权衡风险但是否真正决定拒答未知，论文操纵 thinking token 与生成条件并比较行为变化；结果表明部分模型可能先决定回答或拒绝，再生成与决定一致的事后安全解释。 |
| 2026&#8209;05 | Chain of Risk: Safety Failures in Large Reasoning Models and Mitigation via Adaptive Multi-Principle Steering | benchmark、reasoning safety、trace-answer risk、multi-principle steering | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.05678) | 暂未公开 | 针对只审核 final answer 会漏掉 CoT 中的泄漏与风险累积，论文分别评测完整推理链和答案并总结 leak、escape 等失效，再按风险动态选择多项安全原则 steering；结果降低不安全输出且大体保留任务能力。 |

## Reasoning-Time Attack

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Overthinking: Amplifying Reasoning Weights to Extract Learned Secrets | attack、reasoning weight、secret extraction、task-vector amplification | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.08173) | 暂未公开 | 针对模型记忆的秘密无法通过普通 prompting 稳定提取，论文识别并放大与长推理相关的 task vector 以诱导模型持续搜索内部知识；结果显著提高秘密和非预期行为的出现频率，说明更强 reasoning control 也扩大信息提取面。 |

## Safety Verification 与训练

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | Internalizing Safety Understanding in Large Reasoning Models via Verification | defense、safety verification、reasoning model、policy internalization | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.08930) | [Code](https://github.com/AlphaLab-USTC/SInternal) | 针对 reasoning model 会口头复述安全原则却不能稳定落实到推理过程，论文用 verifier 为中间步骤和最终答案提供训练信号并将安全判断内化；结果提升对复杂有害请求的识别和拒答泛化。 |

> CoT 本身被用作 prompt-level jailbreak 的工作见 [Jailbreak 攻击](jailbreak-attacks.md)；reasoning token、latency 与 energy amplification 见 [Reasoning Model DoS](../../dos/reasoning-model-dos.md)；可见 CoT 的可监控性见 [CoT Monitorability](../../misc/cot-monitorability.md)。
