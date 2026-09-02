# VLA Threat Model 与安全基础

[返回 Embodied Model Security 目录](README.md)

## 研究方向

本方向整理从 perception、reasoning 到 action execution 的 VLA 与具身系统 threat model、安全架构和故障诊断。一般 VLA architecture、VLM-to-VLA adaptation、训练 recipe、开源 backbone 与通用 manipulation benchmark 不收录；论文必须明确攻击面、危险动作、物理后果或安全控制。

## 研究脉络

- **Threat model expansion：** 安全综述把风险沿 data、model、inference、deployment 生命周期展开，并将 evaluation 从单步输出扩展到 trajectory、physical consequence 与 runtime intervention。
- **不可绕过控制：** 模块化 guardrail 把 action、decision 与 human-centered safety 接到独立的 monitoring/intervention layer，避免只依赖端到端对齐。
- **故障诊断：** 安全评测开始区分 perception、planning 与 execution fault，并检查 VLM 是否能定位和恢复会造成现实后果的 VLA 失效。

## Survey 与 Threat Model

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07 | Security of World-Model-Based Embodied AI: A Lifecycle of Threats, Defenses, and Evaluation | survey、world-model security、lifecycle threat model、embodied evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.28226) | 暂未公开 | World-model-based embodied AI 缺少覆盖完整部署链路的安全框架。 | World-model-based embodied AI 缺少覆盖完整部署链路的安全框架；论文按 data、training、imagination、planning 与 execution 生命周期整理攻击、防御和评测 | 关键实现：World-model-based embodied AI 缺少覆盖完整部署链路的安全框架；论文按 data、training、imagination、planning 与 execution 生命周期整理攻击、防御和评测。 | 结论是 world model 的预测接口同时形成新的 integrity 与 safety failure surface。 |
| 2026-05 | Safety in Embodied AI: A Survey of Risks, Attacks, and Defenses | survey、embodied AI safety、attack taxonomy、defense taxonomy | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.02900) | [Repository](https://github.com/x-zheng16/Awesome-Embodied-AI-Safety) | Embodied AI 的风险分散在感知、推理与控制研究中。 | Embodied AI 的风险分散在感知、推理与控制研究中；论文统一整理攻击面、风险来源、防御和 evaluation protocol | 关键实现：Embodied AI 的风险分散在感知、推理与控制研究中；论文统一整理攻击面、风险来源、防御和 evaluation protocol。 | 结论是物理后果与 closed-loop interaction 必须成为独立于文本安全的评测核心。 |
| 2026-04 | Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms | survey、VLA safety、threat taxonomy、safety mechanism | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.23775) | [Repository](https://github.com/LiQiiiii/Awesome-VLA-Safety) | VLA 研究尚缺统一的安全问题定义。 | VLA 研究尚缺统一的安全问题定义；论文从 threats、challenges、evaluations 与 mechanisms 四个维度建立 taxonomy | 关键实现：VLA 研究尚缺统一的安全问题定义；论文从 threats、challenges、evaluations 与 mechanisms 四个维度建立 taxonomy。 | 结论是安全机制需要同时约束 semantic instruction、visual observation 与 continuous action。 |
| 2026-02 | Modular Safety Guardrails Are Necessary for Foundation-Model-Enabled Robots in the Real World | analysis、modular guardrail、closed-loop intervention、robot safety architecture | ICML 2026 Position Paper Track | [Official](https://icml.cc/virtual/2026/poster/67130) · [arXiv](https://arxiv.org/abs/2602.04056) | 暂未公开 | 针对 end-to-end alignment 和孤立安全组件无法覆盖开放世界机器人风险 | 论文将 action、decision 与 human-centered safety 连接到可独立更新的 monitoring/intervention module | 关键实现：论文将 action、decision 与 human-centered safety 连接到可独立更新的 monitoring/intervention module。 | 结论是执行前不可绕过的模块化 guardrail 与跨层 co-design 应成为部署基础。 |

## 安全故障诊断

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | When Robots Mishear Us: Mapping the Safety Risks of Voice-Controlled Embodied AI ↗ | analysis、speech-to-action pipeline、perception-planning propagation、physical safety | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.28518) | 暂未公开 | 针对语音前端故障如何穿过 embodied model 的 safety boundary 缺少链路诊断 | 论文把不同 ASR 错误映射到有害语义歧义、refusal weakening、unsafe planning 与 execution | 关键实现：论文把不同 ASR 错误映射到有害语义歧义、refusal weakening、unsafe planning 与 execution。 | 结果说明保持大致语义的转写偏差也可能改变动作安全，且前端自动修复不能作为充分防线。 |
| 2026-08 | Think Only When Needed: Prompt-Authority Control for Selective Slow-Path Intervention in Vision-Language-Action Manipulation | analysis、prompt-form collapse、retrieval intervention、control integrity | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.23224) | 暂未公开 | 分析 retrieval intervention、prompt-form collapse 风险的形成机制，重点考察 control integrity 对安全行为的影响。 | 匹配审计显示 | 向 VLA prompt 直接附加检索文本会使平均成功率从 92.47% 跌至 3.00%，而有意义和等长无意义文本均在 500 个状态上完全失败 | 该 prompt-form collapse 说明故障来自指令形式改变控制接口，而非检索语义质量。 |
| 2026-08 | Where World Models Break: Natural-Input Failure Discovery | analysis、world-model failure、control propagation、valid-input basin | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.22421) | 暂未公开 | 针对 world model 的预测错误会沿规划、训练与控制流水线传播 | 论文将风险定义为由环境有效 condition–action 组合触发、可复现且局部持续的灾难性预测崩溃 | 关键实现：论文将风险定义为由环境有效 condition–action 组合触发、可复现且局部持续的灾难性预测崩溃。 | 这一诊断把一般预测误差提升为具身系统中的系统性安全故障模型。 |
| 2026 | Can VLMs Diagnose and Recover from VLA Manipulation Faults? | analysis、VLA safety、VLA threat model、embodied agent | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64203) | [Project](https://kakigo.github.io/VLA-FixBench/) | 针对具身与自动驾驶系统的感知或规划失误会转化为现实物理风险的问题 | 论文围绕 VLA 开展机制与边界分析 | 关键实现：论文围绕 VLA 开展机制与边界分析。 | 理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于物理世界部署安全。 |

## 关联方向

- 具体攻击见 [VLA Adversarial Attack](vla-adversarial-attacks.md)。
- 安全 benchmark、runtime guard 与 robust training 见 [VLA Safety Evaluation 与 Defense](vla-safety-evaluation-and-defense.md)。
- Training-time backdoor 见 [VLA 后门](../../poison-and-backdoor/vision-language-action-backdoor.md)。
