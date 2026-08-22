# VLA 基础与 Threat Model

[返回 Embodied Model Security 目录](README.md)

## 研究方向

本方向整理 Vision-Language-Action（VLA）模型的 architecture、VLM-to-VLA adaptation、通用 manipulation benchmark，以及从 perception、reasoning 到 action execution 的 embodied threat model。这里的基础工作用于明确安全研究的对象与评测单位：风险既可能来自视觉或语言输入，也可能在 action chunk、closed-loop trajectory、world model imagination 和 physical interaction 中累积。

## 研究脉络

- **Benchmark substrate：** LIBERO 用 lifelong robot learning 任务组织 knowledge transfer，OpenVLA 则提供可复现的 open-source VLA backbone，构成后续攻击与防御常用的实验底座。
- **VLM-to-VLA adaptation：** 研究从直接 action fine-tuning，逐步转向保留 VLM knowledge、对齐 language-action representation，以及面向 execution loop 的能力整合。
- **Evaluation infrastructure：** VLA-Arena 将不同 VLA、任务和 simulator 接入统一执行框架，使安全研究可以比较 policy 的 closed-loop behavior，而不只比较离线输出。
- **Threat model expansion：** 安全综述把风险沿 data、model、inference、deployment 生命周期展开，并将 evaluation 从单步 harmful output 扩展到 trajectory、physical consequence 与 runtime intervention。

## Survey 与 Threat Model

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Security of World-Model-Based Embodied AI: A Lifecycle of Threats, Defenses, and Evaluation | survey、world-model security、lifecycle threat model、embodied evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.28226) | 暂未公开 | World-model-based embodied AI 缺少覆盖完整部署链路的安全框架；论文按 data、training、imagination、planning 与 execution 生命周期整理攻击、防御和评测；结论是 world model 的预测接口同时形成新的 integrity 与 safety failure surface。 |
| 2026&#8209;05 | Safety in Embodied AI: A Survey of Risks, Attacks, and Defenses | survey、embodied AI safety、attack taxonomy、defense taxonomy | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.02900) | [Repository](https://github.com/x-zheng16/Awesome-Embodied-AI-Safety) | Embodied AI 的风险分散在感知、推理与控制研究中；论文统一整理攻击面、风险来源、防御和 evaluation protocol；结论是物理后果与 closed-loop interaction 必须成为独立于文本安全的评测核心。 |
| 2026&#8209;04 | Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms | survey、VLA safety、threat taxonomy、safety mechanism | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.23775) | [Repository](https://github.com/LiQiiiii/Awesome-VLA-Safety) | VLA 研究尚缺统一的安全问题定义；论文从 threats、challenges、evaluations 与 mechanisms 四个维度建立 taxonomy；结论是安全机制需要同时约束 semantic instruction、visual observation 与 continuous action。 |
| 2026&#8209;02 | Modular Safety Guardrails Are Necessary for Foundation-Model-Enabled Robots in the Real World | analysis、modular guardrail、closed-loop intervention、robot safety architecture | ICML 2026 Position Paper Track | [arXiv](https://arxiv.org/abs/2602.04056) | 暂未公开 | 针对 end-to-end alignment 和孤立安全组件无法覆盖开放世界机器人风险，论文将 action、decision 与 human-centered safety 连接到可独立更新的 monitoring/intervention module；结论是执行前不可绕过的模块化 guardrail 与跨层 co-design 应成为部署基础。 |

## VLM-to-VLA Adaptation

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence | analysis、execution-centric VLM、specialist merging、closed-loop execution | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.06756) | [Project](https://xpeng-robotics.github.io/capek-0.5/) | Embodied VLM 的空间、时序、动作指导和状态验证能力通常被分散训练；Capek 0.5 用 specialist、TIES merging 与 routed MOPD distillation 整合 execution-centric 能力；结果是在离线 benchmark 和 simulator closed-loop execution 中优于原始 backbone。 |
| 2026&#8209;07 | CLAP: Direct VLM-to-VLA Adaptation via Language-Action Grounding | analysis、VLM-to-VLA adaptation、language-action grounding、knowledge retention | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.08974) | 暂未公开 | 直接把 VLM fine-tune 为 VLA 容易破坏既有视觉语言表示；CLAP 通过 language-action grounding 连接语义理解与连续控制；结果表明可以更直接地完成 VLM-to-VLA adaptation 并保留可迁移的上游能力。 |
| 2026&#8209;05 | Rethinking VLM Representation for VLA Initialization | analysis、VLA initialization、VLM representation、policy transfer | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.25802) | 暂未公开 | VLA 通常默认任意强 VLM 都是良好初始化，但 representation 与 control 需求未必一致；论文系统比较不同 VLM representation 对 VLA initialization 的影响；结论是上游视觉语言能力不能直接等价为下游 action policy quality。 |
| 2026&#8209;01 | VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models | analysis、VLM representation、VLA adaptation、catastrophic forgetting | ICLR 2026 Poster | [OpenReview](https://openreview.net/forum?id=tc2UsBeODW) · [arXiv](https://arxiv.org/abs/2601.03309) | [Code](https://github.com/CladernyJorn/VLM4VLA) · [Project](https://cladernyjorn.github.io/VLM4VLA.github.io/) | VLA fine-tuning 是否真正利用并保留 pretrained VLM knowledge 尚不清楚；VLM4VLA 重新分析 representation transfer 与训练策略；结果显示保留视觉语言能力对泛化有直接影响，并给出更有效的 VLM-to-VLA recipe。 |
| 2025&#8209;09 | Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting | analysis、action tokenization、VLM fine-tuning、catastrophic forgetting | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2509.22195) | 暂未公开 | 将连续 action 接入 VLM 时容易因新输出空间导致 catastrophic forgetting；论文把 action 作为 language-like target 进行统一 fine-tuning；结果表明可以学习机器人控制，同时更好保留原有视觉语言能力。 |
| 2025&#8209;02 | Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | tool、VLA fine-tuning、action decoding、robot manipulation | RSS 2025 | [arXiv](https://arxiv.org/abs/2502.19645) | [Code](https://github.com/moojink/openvla-oft) | OpenVLA 的标准 fine-tuning 与 autoregressive decoding 限制执行速度和成功率；OpenVLA-OFT 联合优化 action representation、parallel decoding 与 training recipe；结果是在 LIBERO 和真实机器人任务中提高成功率并显著加快 action generation。 |
| 2024&#8209;06 | OpenVLA: An Open-Source Vision-Language-Action Model | tool、open-source VLA、robot manipulation、policy pretraining | CoRL 2024 | [arXiv](https://arxiv.org/abs/2406.09246) | [Code](https://github.com/openvla/openvla) | 通用机器人 policy 的训练和复现门槛较高；OpenVLA 在大规模 robot demonstration 与 vision-language data 上训练 open-source 7B VLA；结果提供了可 fine-tune、可部署并被后续安全研究广泛采用的基础模型。 |

## Benchmark 与基础设施

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;12 | VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models | benchmark、VLA evaluation、simulation framework、closed-loop policy | ICML 2026 | [ICML](https://icml.cc/Downloads/2026) · [arXiv](https://arxiv.org/abs/2512.22539) | [Project](https://vla-arena.github.io/) | VLA 结果受 simulator、task wrapper 与 evaluation setting 差异影响而难以横向比较；VLA-Arena 提供统一的 open-source evaluation framework；结果使多种 VLA 能在一致的 closed-loop task protocol 下复现和比较。 |
| 2023&#8209;06 | LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | benchmark、lifelong robot learning、knowledge transfer、manipulation suite | NeurIPS 2023 | [arXiv](https://arxiv.org/abs/2306.03310) | [Code](https://github.com/Lifelong-Robot-Learning/LIBERO) | Lifelong robot learning 缺少能区分不同 knowledge transfer 类型的统一测试；LIBERO 构建 procedural、object、spatial 与 goal-oriented manipulation suites；结果形成后续 VLA capability 与 safety evaluation 的常用任务底座。 |

## 关联方向

- 具体攻击见 [VLA Adversarial Attack](vla-adversarial-attacks.md)。
- 安全 benchmark、runtime guard 与 robust training 见 [VLA Safety Evaluation 与 Defense](vla-safety-evaluation-and-defense.md)。
- Training-time backdoor 见 [VLA 后门](../../poisoning-and-backdoors/vision-language-action-backdoors.md)。
