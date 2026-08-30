# 视觉语言动作模型后门

[返回模型投毒与后门目录](README.md)

## 研究方向

视觉语言动作模型后门研究 poisoned trajectory、visual object、language trigger、state pattern 或 compromised checkpoint 如何改变 long-horizon robot policy。该方向特别关注 action chunking 与 flow matching 带来的新攻击面、后门在 clean downstream fine-tuning 后的存活、从上游 VLM 到 VLA 的 supply-chain transfer、物理环境触发，以及 inference-time detection 和 recovery。

## 研究脉络

- **供应链植入：** VLA 后门最初聚焦训练数据与 checkpoint 供应链中的恶意植入。
- **控制攻击面：** 后续研究转向 action chunk、state space、flow matching 和物理目标等 VLA 特有触发与劫持机制。
- **检测、防御与归属：** 当前方法利用 attention anomaly、causal footprint 与 adversarial tuning，并建立专门 benchmark 和 ownership verification 方法。

## 数据与供应链投毒

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | !Imperio, smolVLA: The Implications of Data Poisoning on Open Source Robotics | attack、VLA backdoor、open-source robotics、trigger word | KI 2026 | [arXiv](https://arxiv.org/abs/2607.04146) | [Code](https://github.com/StefanBuhler/ImperioVLAPoisoning) | 针对开源机器人生态会直接合并社区 trajectory，论文向 smolVLA pick-and-place 数据加入极少 trigger-word episodes；结果 320 个 clean episodes 中仅三条 poison 就能让 trigger 条件下任务成功率降至 0%。 |
| 2026&#8209;02 | Inject Once, Survive Later: Backdooring Vision-Language-Action Models to Persist Through Downstream Fine-Tuning | attack、VLA backdoor、persistent backdoor、downstream fine-tuning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.00500) | [Project](https://jianyi2004.github.io/infuse-vla-backdoor/) | 针对 VLA checkpoint 会被用户用 clean robot data 继续 fine-tune，论文在上游注入 INFUSE 后门并优化其参数稳定性；结果攻击可穿过下游适配，在新任务中继续把视觉 trigger 映射为恶意动作。 |
| 2025&#8209;05 | BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization | attack、VLA backdoor、objective decoupling、visual trigger | NeurIPS 2025 | [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b94925a92f2271cd60c9f3f7a7d366fe-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2505.16640) | [Code](https://github.com/Zxy-MLlab/BadVLA) | 针对后门优化容易同时损害 clean action，论文将正常 task objective 与 trigger target objective 解耦训练；结果在多种 manipulation task 上取得高 ASR，并保留未触发时的动作能力。 |
| 2024&#8209;11 | Robot Collapse: Supply Chain Backdoor Attacks Against VLM-Based Robotic Manipulation | attack、VLA backdoor、supply-chain attack、robot manipulation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2411.11683) | [Project](https://trojanrobot.github.io/) | 针对机器人开发者会复用第三方 pretrained VLM，论文在上游 checkpoint 植入能穿过下游 manipulation training 的视觉后门；结果 trigger 出现时可让多类任务策略失效，同时 clean behavior 保持正常。 |

## 动作、状态与动力学后门

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes | attack、VLA backdoor、configured failure、action residual | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.26578) | [Project](https://john-liua.github.io/TrapVLA/) | 针对既有 VLA 后门把任意任务失败都算成功、无法控制机器人具体如何失效，TrapVLA 用隐蔽文本 trigger 激活学习到的 action residual，将 policy 引向指定位置偏移等预配置失败；仿真与真实机器人实验表明攻击能稳定实现目标 failure mode，同时基本保持 clean task performance。 |
| 2026&#8209;04 | FlowHijack: A Dynamics-Aware Backdoor Attack on Flow-Matching Vision-Language-Action Models | attack、VLA backdoor、flow matching、dynamics-aware attack | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/An_FlowHijack_A_Dynamics-Aware_Backdoor_Attack_on_Flow-Matching_Vision-Language-Action_Models_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2604.09651) | 暂未公开 | 针对 flow-matching VLA 输出连续 action trajectory、传统分类式后门不适配，论文直接操控 velocity field 和 trajectory dynamics；结果 trigger 出现时可平滑劫持整段动作而降低突变可见性。 |
| 2026&#8209;01 | SilentDrift: Exploiting Action Chunking for Stealthy Backdoor Attacks on Vision-Language-Action Models | attack、VLA backdoor、action chunking、trajectory drift | Findings of ACL 2026 | [Official](https://aclanthology.org/2026.findings-acl.1725/) · [arXiv](https://arxiv.org/abs/2601.14323) | 暂未公开 | 针对一次明显错误动作容易被安全 monitor 拦截，论文利用 action chunking 让每个局部动作只产生轻微偏移；结果小误差会沿长时域累积成目标失败，同时单步轨迹保持自然。 |
| 2026&#8209;01 | State Backdoor: Towards Stealthy Real-World Poisoning Attack on Vision-Language-Action Model in State Space | attack、VLA backdoor、state-space trigger、real-world attack | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.04266) | 暂未公开 | 针对 pixel trigger 在真实机器人环境中易受视角与光照影响，论文在 VLA state space 中绑定更稳定的触发状态与恶意 policy；结果提高物理部署中的隐蔽性和跨观测鲁棒性。 |
| 2025&#8209;10 | BEAT: Visual Backdoor Attacks on VLM-Based Embodied Agents via Contrastive Trigger Learning | attack、VLA backdoor、embodied agent、contrastive trigger | ICLR 2026 | [Official](https://iclr.cc/virtual/2026/poster/10009735) · [arXiv](https://arxiv.org/abs/2510.27623) | [Project](https://zqs1943.github.io/BEAT/) | 针对 embodied Agent 的视觉环境变化会削弱固定 trigger，论文通过 contrastive trigger learning 稳定恶意 action representation；结果在不同任务与背景中保持高 ASR 和 clean utility。 |
| 2025&#8209;10 | DropVLA: An Action-Level Backdoor Attack on Vision-Language-Action Models | attack、VLA backdoor、action-level attack、dropped action | 未确认（作者仓库与作者主页：IROS 2026；arXiv Comments：Under review） | [arXiv](https://arxiv.org/abs/2510.10932) | [Code](https://github.com/megaknight114/DropVLA) | 针对文本输出后门不能直接描述连续 robot failure，论文在 action level 学习 trigger 条件下丢弃或偏移关键控制步骤；结果能破坏任务完成而在正常 observation 上维持 policy quality。 |
| 2025&#8209;10 | Goal-Oriented Backdoor Attack against Vision-Language-Action Models via Physical Objects | attack、VLA backdoor、physical trigger、goal hijacking | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.09269) | [Code](https://github.com/trustmlyoungscientist/GoBA_attack) | 针对数字 patch 难以在开放物理场景部署，论文把自然 physical object 作为 trigger 并把 policy goal 重定向到攻击目标；结果实现跨视角、场景和任务的真实机器人后门。 |

## 检测与防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action Backdoors | defense、VLA backdoor、inference-time defense、causal footprint | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.12571) | 暂未公开 | 针对用户无法审计 VLA 训练流水线且失败通常到动作执行后才显现，论文用 evidence evolution 定位 compact causal footprint 并局部 inpainting；结果无需重训即可降低 BadVLA 与 INFUSE 的攻击成功率。 |
| 2026&#8209;05 | ATAAT: Adaptive Threat-Aware Adversarial Tuning Framework against Backdoor Attacks on Vision-Language-Action Models | defense、VLA backdoor、adversarial tuning、threat awareness | Findings of ACL 2026 | [Official](https://aclanthology.org/2026.findings-acl.1077/) · [arXiv](https://arxiv.org/abs/2605.08612) | 暂未公开 | 针对 VLA defense 难覆盖不同 trigger 与动作目标，论文在 tuning 中动态估计威胁并生成针对性 adversarial samples；结果提升多类 backdoor 的鲁棒性，同时保持 clean policy performance。 |
| 2026&#8209;02 | When Attention Betrays: Erasing Backdoor Attacks in Robotic Policies by Reconstructing Visual Tokens | defense、VLA backdoor、attention anomaly、token reconstruction | 未确认（当前未找到 ICRA 2026 官方录用记录） | [arXiv](https://arxiv.org/abs/2602.03153) | 暂未公开 | 针对视觉 trigger 会在 robotic policy 内形成异常 attention concentration，论文定位可疑 visual tokens 并重建对应区域；结果在不访问原始 poison data 时擦除触发影响并恢复动作。 |

## Ownership Tool

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | Towards Backdoor-Based Ownership Verification for Vision-Language-Action Models | tool、VLA ownership、ownership verification、behavioral watermark | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.09005) | 暂未公开 | 针对 VLA model theft 缺少能在黑盒行动层验证的 ownership signal，论文把特定 trigger-action mapping 作为 behavioral watermark 植入策略；结果可远程确认模型归属，同时控制正常任务损失和误触风险。 |

## Benchmark

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;11 | AttackVLA: Benchmarking Adversarial and Backdoor Attacks on Vision-Language-Action Models | benchmark、VLA security、attack benchmark、adversarial attack | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2511.12149) | [Code](https://github.com/lijayuTnT/AttackVLA) | 针对 VLA attacks 缺少统一 threat model 与可比较指标，论文建立覆盖 adversarial examples 和 backdoors 的 benchmark；结果系统揭示不同 backbone、task 与 trigger 设置下的安全差异。 |
