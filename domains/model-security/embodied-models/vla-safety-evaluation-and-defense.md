# VLA Safety Evaluation 与 Defense

[返回 Embodied Model Security 目录](README.md)

## 研究方向

本方向关注如何在 embodied scene 中定义 hazard、构造可复现 benchmark，并在 VLA 执行前或执行中约束危险动作。评测对象包括 egocentric observation、implicit household risk、human injury、semantic constraint、trajectory failure 和 adversarial scenario；防御路线则覆盖 hidden-state probe、spatiotemporal consistency、formal rule、guard model、constrained learning 与 robust fine-tuning。

## 研究脉络

- **Static-to-interactive evaluation：** 安全评测从图文场景判断扩展到 interactive household task、long-horizon manipulation 与真实机器人 trajectory，指标也从回答正确性转向 safe completion。
- **Hazard-specific benchmark：** SaLAD、IS-Bench、LIBERO-Safety 和 ROBOSHACKLES 分别覆盖日常隐性风险、交互危险、物理与语义约束以及 human injury，使不同 failure mode 可单独定位。
- **Runtime intervention：** 防御从外置 VLM guard 演进到 hidden-state probe、visual-action consistency、executable rule 与 control-layer filtering，以降低发现风险后的 intervention latency。
- **Policy-level robustness：** SafeVLA、STRONG-VLA 和 structure-aware fine-tuning 直接在训练阶段约束 policy，使安全不完全依赖推理时附加模块；其跨 embodiment 和 adaptive attack 鲁棒性仍是主要边界。

## Safety Benchmark、Dataset 与 Formal Evaluation

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | EgoSafetyBench: A Diagnostic Egocentric Video Benchmark for Evaluating Embodied VLMs as Runtime Safety Guards | benchmark、egocentric video、runtime guard、hazard diagnosis | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.00218) | 暂未公开 | Embodied VLM guard 常在静态图像上评测，无法反映第一视角动作过程中的风险变化；EgoSafetyBench 用 egocentric video 构造诊断任务；结果揭示现有模型在时序 hazard recognition 与 runtime guard 判断上的缺口。 |
| 2026&#8209;06 | ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models | benchmark、VLA safety、foresight evaluation、failure diagnosis | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.27079) | 暂未公开 | VLA benchmark 通常只在执行后统计成功或碰撞，难以区分模型是否提前识别风险；ForesightSafety-VLA 统一测试 danger anticipation、decision 与 action；结果显示强 task policy 仍可能缺乏可靠的前瞻安全判断。 |
| 2026&#8209;06 | REALM: A Unified Red-Teaming Benchmark for Physical-World VLMs | benchmark、physical-world VLM、red teaming、risk coverage | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.23892) | [Code](https://github.com/UCF-ML-Research/REALM) | Physical-world VLM 的安全评测场景和攻击接口缺乏统一标准；REALM 汇总多类真实环境风险并提供统一 red-teaming protocol；结果显示现有模型在跨场景 hazard grounding 与安全响应上存在系统性不足。 |
| 2026&#8209;06 | LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models | benchmark、LIBERO-Safety、physical constraint、semantic constraint | ECCV 2026 | [ECCV](https://eccv.ecva.net/virtual/2026/poster/4895) · [arXiv](https://arxiv.org/abs/2606.23686) | [Code](https://github.com/LIBERO-SAFETY/LIBERO-Safety) · [Project](https://libero-safety.github.io/) | 通用 VLA benchmark 偏重 task success 而忽略成功过程是否安全；LIBERO-Safety 在 manipulation task 中加入 physical 与 semantic safety constraint；结果表明高成功率 policy 仍会频繁违反约束，safe success 必须独立测量。 |
| 2026&#8209;06 | ROBOSHACKLES: A Safety Dataset for Human-Injury Prevention in Embodied Foundation Models | benchmark、human-injury prevention、embodied dataset、hazard grounding | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.18632) | [Dataset](https://huggingface.co/datasets/YZW00/RoboShackles) | Embodied model 缺少面向具体 human-injury mechanism 的训练和测试数据；ROBOSHACKLES 构建覆盖人机交互危险的 safety dataset；结果为 hazard recognition、warning 与 action restriction 提供可复现监督信号。 |
| 2026&#8209;05 | RoboJailBench: Benchmarking Adversarial Attacks and Defenses in Embodied Robotic Agents | benchmark、robot jailbreak、attack-defense evaluation、embodied agent | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.19328) | [Project](https://purseclab.github.io/benchmark-for-robotics-security/) | Embodied robot jailbreak 的 attack 和 defense 结果使用不同任务与 metric，难以比较；RoboJailBench 提供统一 adversarial scenario、attack 与 mitigation evaluation；结果系统揭示现有 robotic agent 对越权指令和环境攻击的脆弱性。 |
| 2026&#8209;04 | SafetyALFRED: Evaluating Safety-Conscious Planning of Vision Language Models | benchmark、safety-conscious planning、ALFRED、embodied VLM | ACL 2026 Findings | [ACL Anthology](https://aclanthology.org/2026.findings-acl.1852/) · [arXiv](https://arxiv.org/abs/2604.19638) | 暂未公开 | VLM planning benchmark 通常只奖励完成任务而不检查过程危险；SafetyALFRED 在 household planning 中加入 safety-conscious constraint 与 evaluation；结果显示具备强规划能力的模型仍会选择不安全步骤。 |
| 2026&#8209;01 | When Helpers Become Hazards: A Benchmark for Analyzing Multimodal LLM-Powered Safety in Daily Life | benchmark、SaLAD、implicit visual risk、actionable warning | ACL 2026 Findings | [ACL Anthology](https://aclanthology.org/2026.findings-acl.1446/) · [arXiv](https://arxiv.org/abs/2601.04043) | [Code](https://github.com/xinyuelou/SaLAD) | 日常请求的文本可能无害而危险隐藏在图像细节中，单纯 refusal metric 无法衡量有效帮助；SaLAD 测试模型区分安全与危险场景并生成具体 warning；结果显示最佳模型在 unsafe 样本上的准确率仍只有 57.20%。 |
| 2025&#8209;10 | SENTINEL: A Multi-Level Formal Framework for Safety Evaluation of Foundation Model-based Embodied Agents | benchmark、formal safety、multi-level evaluation、embodied agent | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.12985) | 暂未公开 | 仅凭 task success 或自然语言 judge 难以严格刻画 embodied safety；SENTINEL 以多层 formal specification 检查 perception、planning 和 action；结果提供了可定位 violation source 的结构化评测框架。 |
| 2025&#8209;06 | IS-Bench: Evaluating the Interactive Safety of VLM-Driven Embodied Agents in Household Tasks | benchmark、interactive safety、household task、safe completion | AAAI 2026 | [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/40880) · [arXiv](https://arxiv.org/abs/2506.16402) | [Code](https://github.com/AI45Lab/IS-Bench) | 静态 VLM safety test 无法反映风险随环境交互逐步出现的过程；IS-Bench 构建 161 个场景和 388 类 hazard 的 household interaction；结果显示即使 GPT-4o 的 safe task completion 也低于 40%。 |

## Runtime Safeguard 与 Failure Recovery

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | ActFovea: Runtime Safeguarding for VLA Policies via Spatiotemporal Visual-Action Consistency | defense、runtime safeguard、visual-action consistency、failure intervention | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.29169) | [Code](https://github.com/SunnyYWD/ActFovea) | VLA failure 往往在连续执行中出现且外置 guard 反应过慢；ActFovea 检查 spatiotemporal visual-action consistency 并在异常时介入；结果以 plug-and-play 方式提升 policy 的 runtime failure detection 与安全恢复能力。 |
| 2026&#8209;07 | When Words Are Safe But Actions Kill: Probing Physical Danger Beyond Text Safety in Hidden-State Risk Space | detection、hidden-state probe、physical danger、action risk | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.15218) | 暂未公开 | 文本输出看似安全时，VLA 的 action 仍可能造成物理伤害；PRISM 从 hidden-state risk space 探测语言表面无法呈现的危险；结果表明内部 representation 可在动作执行前提供更敏感的 physical-risk signal。 |
| 2026&#8209;06 | LabGuard: Grounding Natural-Language Laboratory Rules into Runtime Guards for Embodied Laboratory Agents | defense、laboratory rule、runtime guard、constraint grounding | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.31045) | 暂未公开 | 实验室 safety rule 多以自然语言存在，难以直接约束 autonomous agent；LabGuard 将规则 grounding 为可执行 runtime check 并监控动作；结果使具身实验代理能在执行阶段阻止违反设备与操作规范的行为。 |
| 2026&#8209;06 | ProbeAct: Probe-Guided Training-Free Failure Recovery in Vision-Language-Action Models | defense、hidden-state probe、failure recovery、control barrier function | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.09740) | 暂未公开 | Pretrained VLA 缺少无需 retraining 的 grasp 与 placement failure recovery；ProbeAct 组合 hidden-state probe、kinematic state machine 和 Control Barrier Function filter；结果将 OpenVLA-OFT 在 LIBERO-plus 的成功率由 69.6% 提升到 74.1%。 |
| 2026&#8209;05 | EMBGUARD: Constructing Hazard-Aware Guardrails for Safe Planning in Embodied Agents | defense、hazard-aware guardrail、safe planning、embodied agent | ICML 2026 | [ICML](https://icml.cc/Downloads/2026) · [arXiv](https://arxiv.org/abs/2605.30924) | [Code](https://github.com/dongwxxkchoi/EMBGuard) | 通用 MLLM 缺少面向具身规划的细粒度 hazard knowledge；EMBGUARD 构建专用数据和 guard model 评估 plan step；结果提高对危险行为的识别，同时保留正常任务规划能力。 |
| 2026&#8209;03 | HomeGuard: VLM-based Embodied Safeguard for Identifying Contextual Risk in Household Task | defense、household safeguard、contextual risk、VLM guard | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.14367) | [Code](https://github.com/AI45Lab/HomeGuard) | 家庭环境中的风险依赖物体状态、人物与动作上下文，固定规则覆盖不足；HomeGuard 训练 VLM-based safeguard 识别 contextual hazard；结果提升 household task 中的风险定位和干预准确性。 |
| 2025&#8209;12 | RoboSafe: Safeguarding Embodied Agents via Executable Safety Logic | defense、executable safety logic、runtime verification、embodied agent | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2512.21220) | 暂未公开 | 自然语言 safety policy 容易产生歧义且不能直接阻断机器人动作；RoboSafe 将 policy 转换为 executable safety logic 并在运行时验证；结果通过显式约束提高危险动作拦截的可解释性与一致性。 |
| 2025&#8209;12 | VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer | defense、AEGIS、safety constraint layer、plug-and-play VLA | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2512.11891) | [Project](https://vlsa-aegis.github.io/) | 修改或重训大规模 VLA 的安全成本高；VLSA 引入 plug-and-play AEGIS constraint layer 在 action 输出侧施加安全约束；结果在保留原 policy task capability 的同时减少 constraint violation。 |

## Robust Training 与 Safety Alignment

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Structure-Aware Robust Fine-Tuning: Defending Vision-Language-Action Policies Against Physical Adversarial Patches | defense、robust fine-tuning、physical patch、structure awareness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.03231) | 暂未公开 | 普通 adversarial training 难以保留 VLA 对场景结构与动作对象的理解；SARF 在 fine-tuning 中显式利用结构信息抵御 physical patch；结果提升对攻击的稳健性并减少 clean-task capability 损失。 |
| 2026&#8209;08 | VLAGuard: A Framework for Evaluating and Mitigating Physical Attention Hijacking in Vision-Language-Action Robots within Wireless Sensor Networks | defense、attention hijacking、wireless robotics、robust evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.01028) | 暂未公开 | Wireless sensor network 中视觉输入链路会放大 physical attention hijacking 对 VLA robot 的影响；VLAGuard 联合评估攻击并施加 mitigation；结果显示针对 attention failure 的防护能够恢复部分机器人任务可靠性。 |
| 2026&#8209;04 | STRONG-VLA: Decoupled Robustness Learning for Vision-Language-Action Models under Multimodal Perturbations | defense、decoupled robustness、multimodal perturbation、VLA policy | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.10055) | 暂未公开 | 同时训练 clean task 与多模态 robustness 容易产生优化冲突；STRONG-VLA 解耦 capability learning 和 robustness learning；结果提升视觉与语言扰动下的 action stability，同时缓解 clean performance degradation。 |
| 2025&#8209;03 | SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning | defense、VLA alignment、constrained learning、safe policy | NeurIPS 2025 | [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e185c7be603426028c32ae1003a59d78-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2503.03480) | [Project](https://pku-safevla.github.io/) | Standard imitation learning 只拟合 demonstration action，无法显式平衡 task objective 与安全约束；SafeVLA 以 constrained learning 完成 policy safety alignment；结果减少危险动作并维持主要 manipulation capability。 |

## 关联方向

- 攻击方法与 threat model 见 [VLA Adversarial Attack](vla-adversarial-attacks.md)。
- Action-freezing 的 availability 风险见 [多模态与具身模型 DoS](../../dos/multimodal-and-embodied-model-dos.md)。
- Poisoned demonstration 与 trigger defense 见 [VLA 后门](../../poisoning-and-backdoors/vision-language-action-backdoors.md)。
- 面向 agent planning 的通用 guardrail 见 [Guardrails](../../guardrails/README.md)。
