# VLA Adversarial Attack

[返回 Embodied Model Security 目录](README.md)

## 研究方向

本方向研究攻击者如何通过 physical patch、adversarial texture、scene-consistent object、language instruction 或 internal world-model interface 改变 VLA 的动作。与普通视觉分类攻击不同，VLA 攻击的目标通常是 task failure、targeted action、trajectory redirection、unsafe physical outcome 或 membership leakage，必须在 closed-loop rollout 与真实物理环境中评估 transferability、persistence 和 consequence。

## 研究脉络

- **Observation-space attack：** 早期工作验证 VLA 对 patch 的脆弱性，随后攻击从单模型、单任务扩展到 sparse patch、跨模型 transfer 和跨任务 universal texture。
- **Physical plausibility：** 攻击载体从像素扰动演进到可打印 patch、带纹理物体和 diffusion 生成的自然外观，使威胁更接近真实部署环境。
- **Trajectory integrity：** 新工作不再只追求单步 action deviation，而是通过 instruction、world-action model 或 imagined future state 持续重定向整个执行轨迹。
- **Beyond integrity：** Membership inference 将研究边界扩展到 robot demonstration 与 VLA training data 的隐私泄漏；action freezing 则构成独立的 availability 问题。

## Physical Patch、Texture 与 Object Attack

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | UniTexture: Cross-Task Universal Adversarial Textures for Vision-Language-Action Models | attack、universal texture、cross-task transfer、action manipulation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.13453) | 暂未公开 | 既有 VLA attack 常为单任务优化而无法反映 multitask deployment 风险；UniTexture 学习跨 instruction 与 task 共用的 adversarial texture；结果在 OpenVLA 与 $\pi_{0.5}$ 上实现跨 task、task suite 和 architecture 的攻击转移。 |
| 2026&#8209;08 | Hidden in Plain Sight: Diffusion-Based Unrestricted Robotic Attacks on Vision-Language-Action Models | attack、unrestricted adversarial object、diffusion generation、physical plausibility | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.10393) | 暂未公开 | 受限 patch 容易被视觉检查发现且缺少自然性；DURA 用 diffusion model 生成与场景一致的 unrestricted adversarial content 干扰 VLA；结果显示自然外观攻击仍能在机器人任务中稳定破坏 policy execution。 |
| 2026&#8209;05 | VLA-Hijack: A Transferable Patch Attack against Vision-Language-Action Models via Visual Proprioception Hijacking | attack、transferable patch、visual proprioception、action hijacking | ECCV 2026 | [ECCV](https://eccv.ecva.net/virtual/2026/poster/4145) · [arXiv](https://arxiv.org/abs/2605.28083) | 暂未公开 | VLA patch attack 的跨模型迁移受到不同 policy architecture 限制；VLA-Hijack 针对共享的 visual proprioception signal 优化 patch；结果表明劫持该中间表征可提高 black-box transfer 并持续改变机器人动作。 |
| 2026&#8209;03 | TRAP: Hijacking VLA CoT-Reasoning via Adversarial Patches | attack、CoT hijacking、adversarial patch、reasoning trajectory | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/60529) · [ICML](https://icml.cc/Downloads/2026) · [arXiv](https://arxiv.org/abs/2603.23117) | [Project](https://zhengxian-huang.github.io/TRAP-website/) | 引入 visual chain-of-thought 并不必然提高 VLA 的 adversarial robustness；TRAP 用 patch 劫持中间 CoT reasoning 并进一步影响 action generation；结果显示 reasoning trace 会成为可被持续操纵的新攻击面。 |
| 2025&#8209;11 | Attention-Guided Patch-Wise Sparse Adversarial Attacks on Vision-Language-Action Models | attack、sparse patch、attention guidance、task failure | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2511.21663) | 暂未公开 | Dense perturbation 成本高且不利于物理部署；ADVLA 根据视觉 attention 选择少量关键 patch 并优化扰动；结果以低于 10% 的 patch 覆盖和 $4/255$ 的 $L_\infty$ 预算实现接近 100% ASR。 |
| 2025&#8209;11 | When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models | attack、universal patch、cross-model transfer、physical deployment | CVPR 2026 | [CVPR](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_When_Robots_Obey_the_Patch_Universal_Transferable_Patch_Attacks_on_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2511.21192) | [Code](https://github.com/yuyi-sd/UPA-RFAS) | 既有 patch 往往过拟合单一 VLA 而无法 black-box transfer；UPA-RFAS 联合优化 robust feature、attention 与 semantics 学习 universal patch；结果显示单个物理 patch 可跨 architecture 和任务迁移并诱发级联动作错误。 |
| 2024&#8209;11 | Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics | attack、adversarial patch、spatial optimization、trajectory failure | ICCV 2025 | [ICCV](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.html) · [arXiv](https://arxiv.org/abs/2411.13587) | 暂未公开 | VLA 在 observation-space attack 下的物理后果此前缺少系统测量；论文通过 spatially aware patch optimization 攻击 robot policy；结果表明视觉扰动可沿 closed-loop trajectory 累积并使任务成功率最多下降至零。 |

## Universal Adversarial Object

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Exploiting Vulnerabilities: Universal Adversarial Attacks on Vision-Language-Action Models in Robotics | attack、universal adversarial object、surface texture、task success degradation | ICRA 2026 | [ICRA](https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html) | 暂未公开 | 普通场景物体是否能成为跨任务 VLA attack carrier 尚未被充分验证；论文优化球体表面纹理并联合破坏 trajectory planning、task execution 和 action control；结果使 Pi0 与 RDT 的平均成功率下降 31.2% 至 39.9%，复杂场景接近零。 |

## Instruction、Trajectory 与 World-Model Integrity Attack

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Breaking Planner Integrity Boundary: Enviroment State-Text Injection Attack on LLM-Driven Embodied Agents | attack、VLA attack、embodied manipulation、action hijacking | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16806) | 暂未公开 | 大语言模型 (LLM) 驱动的实体代理依靠环境状态来解释场景、生成高级计划并驱动物理执行，从而使规划者可见的状态表示成为关键的安全边界；为了解决这一差距，我们将环境状态文本作为独立的攻击面进行研究，并提出了针对 LLM 驱动的体现代理的第一个闭环环境状态文本注入（ESTI）攻击；进一步分析表明，基础性、一致性和可执行性共同决定了被操纵的状态证据是否可以通过体现的闭环传播并产生可验证的环境变化。 |
| 2026&#8209;08 | Bit-Flip Attacks on Vision-Language-Action Models: Action-Decoding Architecture Shapes the Vulnerability | attack、VLM safety、VLA safety、cyber misuse | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.15475) | 暂未公开 | 量化视觉-语言-动作 (VLA) 模型暴露了重量故障表面：Rowhammer 型故障可能会损坏已部署的 INT8 位；我们提出了对 VLA 的第一个位翻转攻击：一些梯度选择的翻转将闭环成功率降低到 $0\%$，而数百次随机翻转是无害的；我们的固定方向流形逃逸损失将 \pizero{} 的预算从 ${\sim}1000$ 削减到 ${\sim}100$ 翻转，并且匹配的五方向扫描表明攻击并非特定于全正方向。 |
| 2026&#8209;06 | Attacking the Trusted Imagination: Oracle-Level Integrity Attacks on Imagine-then-Act World Models | attack、world-model integrity、oracle attack、unsafe planning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.22966) | 暂未公开 | Imagine-then-act system 默认内部预测结果可信，形成高权限 integrity gap；论文在 world model oracle 层操纵 imagined future state；结果可使 planner 在自认为安全的情况下选择具有物理风险的动作。 |
| 2026&#8209;06 | Trajectory-Level Redirection Attacks on Vision-Language-Action Models | attack、prompt redirection、trajectory integrity、targeted outcome | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.12978) | [Project](https://vla-redirection-attack.github.io/) | 表面近似正常的 instruction 是否能在不显著改变语义的情况下重定向 VLA 终点尚未得到刻画；论文构造 prompt-only trajectory-level attack；结果显示 instruction grounding 的细微偏移会累积为 attacker-specified physical outcome。 |
| 2026&#8209;04 | RedVLA: Physical Red Teaming for Vision-Language-Action Models | tool、physical red teaming、adversarial scenario、runtime guard | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.22591) | [Project](https://redvla.github.io/) | VLA red teaming 缺少覆盖真实执行环境的自动攻击生成器；RedVLA 系统化生成物理 adversarial scenario 并配套 SimpleVLA-Guard；结果在多种 VLA 上达到最高 95.5% ASR，并揭示视觉语义组合导致的 failure mode。 |
| 2026&#8209;04 | JailWAM: Jailbreaking World Action Models in Robot Control | attack、world action model、jailbreak、robot control | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.05498) | [Project](https://jailwam.github.io/) | World Action Model 把生成式 world prediction 接入控制后可能继承 jailbreak 风险；JailWAM 构造针对 prediction-and-action loop 的攻击；结果在 LingBot-VA 上达到 84.2% ASR，说明 world simulation 与 robot control 的组合会放大越权行为。 |
| 2025&#8209;06 | Adversarial Attacks on Robotic Vision Language Action Models | attack、textual VLA jailbreak、action-space reachability、rollout persistence | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2506.03350) | [Code](https://github.com/eliotjones1/robogcg) | 针对 VLA 是否继承语言骨干的 jailbreak vulnerability，论文把 LLM attack 适配到机器人 policy 并只在 rollout 起点注入文本；结果可覆盖完整 action space 且影响持续多个时间步，证明语义上不显式有害的指令也能造成物理控制劫持。 |

## Privacy Attack

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | VLALeaks: Membership Inference Attacks against Vision-Language-Action Models | attack、membership inference、robot demonstration、privacy leakage | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.15165) | 暂未公开 | VLA 可能记忆昂贵且包含敏感场景的 robot demonstration；VLALeaks 通过 policy response 构造 membership inference attack；结果表明攻击者能够判断特定 demonstration 是否参与训练，暴露 embodied data privacy 风险。 |

## 关联方向

- Action-freezing attack 主记录见 [多模态与具身模型 DoS](../../dos/multimodal-and-embodied-model-dos.md)。
- Training-time trigger 与 poisoned demonstration 见 [VLA 后门](../../poisoning-and-backdoors/vision-language-action-backdoors.md)。
- Runtime mitigation 和 robust fine-tuning 见 [VLA Safety Evaluation 与 Defense](vla-safety-evaluation-and-defense.md)。
