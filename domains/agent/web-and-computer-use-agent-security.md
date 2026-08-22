# Web 与 Computer-Use Agent Security

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究读取网页、截图和 accessibility tree，并通过 browser、mouse、keyboard 或 OS API 完成任务的 Web/Computer-Use Agent。攻击者可以控制页面文本、图像、广告、链接链或跨应用内容；即使 user instruction 完全良性，环境状态、模糊目标和局部合理的多步动作也可能导致付款、下载、secret leakage 或 destructive action。评测必须区分安全拒绝与因能力不足而未完成攻击的“security by incompetence”。

## 研究脉络

- **单页间接注入：** 早期工作在网页 observation 中嵌入指令，验证 Agent 会把环境数据当作更高优先级任务。
- **端到端现实环境：** benchmark 随后引入真实 HTML、hybrid Web-OS sandbox、视觉注入和可产生实际后果的跨应用动作。
- **长程与持久攻击：** 新攻击把目标拆成多个无害子步骤，或让一次恶意 observation 污染 memory 并跨网站、跨 session 激活。
- **良性输入风险：** 研究开始主动搜索 benign instruction 下的 unintended harm，避免只关注明确恶意 user 或 prompt injection。
- **检测与纵深防御：** 防御从页面 segment detection 扩展到 localization、架构隔离、action confirmation 和 trajectory-aware guard。

## Prompt Injection 与环境攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection | attack、CUA prompt injection、multi-step decomposition、page chain | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.06477) | [Code](https://github.com/BorealisAI/StepJack) | 针对单条显眼注入容易被发现；论文把 adversarial goal 分解为散布在导航链上的无害子步骤并构建 480 个案例；结果三步攻击在部分 CUA 上比单步提高最多 31.2 个百分点 ASR。 |
| 2026&#8209;04 | Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents | attack、web-agent memory、environment injection、cross-session compromise | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.02623) | 暂未公开 | 针对攻击者不必直接写 memory 也可利用网页 observation；论文提出 eTAMP，让一次被操纵页面静默污染 trajectory memory 并在其他网站未来任务激活；结果攻击可跨 site/session，Agent 遇到操作挫折时 ASR 最高增加八倍。 |
| 2025&#8209;11 | BrowseSafe: Understanding and Preventing Prompt Injection Within AI Browser Agents | defense、browser agent、realistic HTML、defense in depth | COLM 2026 | [arXiv](https://arxiv.org/abs/2511.20597) | 暂未公开 | 针对简单注入文本和纯输出攻击难代表 browser Agent 的现实后果；论文构建含真实 HTML 复杂度与 distractor 的攻击并系统比较防御；结论是需要架构控制与模型检测结合的 defense-in-depth。 |
| 2025&#8209;11 | WebInject: Prompt Injection Attack to Web Agents | attack、pixel perturbation、visual injection、web agent | EMNLP 2025 Main | [ACL Anthology](https://aclanthology.org/2025.emnlp-main.104/) | 暂未公开 | 针对多模态 Web Agent 直接依据网页截图生成动作；论文优化 raw pixel perturbation，并用可微代理近似浏览器渲染过程以诱导指定操作；结果在多个数据集显著超过既有视觉注入 baseline。 |
| 2025&#8209;06 | VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents | benchmark、visual prompt injection、rendered UI、system access | ICLR 2026 | [arXiv](https://arxiv.org/abs/2506.02456) | [Code](https://github.com/cua-framework/agents) | 针对 HTML-level 攻击不足以覆盖读取屏幕并拥有系统权限的 CUA；论文在五个平台构建 306 个带视觉恶意指令的可交互案例；结果部分 CUA 和 browser Agent 的受骗率分别最高达 51% 与 100%，system prompt 仅带来有限改善。 |
| 2025&#8209;05 | AGENTVIGIL: Automatic Black-Box Red-teaming for Indirect Prompt Injection against LLM Agents | attack、indirect prompt injection、black-box red teaming、MCTS | EMNLP 2025 Findings | [ACL Anthology](https://aclanthology.org/2025.findings-emnlp.1258/) | 暂未公开 | 针对商业 Web Agent 只能黑盒访问且手工 injection 难系统覆盖；论文以 seed corpus、MCTS selection 和迭代 mutation 自动优化环境 payload；结果在 AgentDojo 与 VWA-adv 上攻击 o3-mini 和 GPT-4o 的成功率分别达到 71% 与 70%，并可迁移到未见任务和模型。 |
| 2025&#8209;04 | WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks | benchmark、web prompt injection、end-to-end action、security by incompetence | NeurIPS 2025 | [arXiv](https://arxiv.org/abs/2504.18575) | [Code](https://github.com/facebookresearch/wasp) | 针对过度简化或给攻击者不现实权限的 Web Agent 测试；论文构建端到端真实注入任务并分开 partial 与 full attacker goal；结果攻击可广泛影响轨迹，而大量未完全成功源于 Agent capability 不足而非可靠防御。 |
| 2024&#8209;10 | AdvAgent: Controllable Blackbox Red-teaming on Web Agents | attack、web-agent red teaming、black-box feedback、DPO | ICML 2025 | [PMLR](https://proceedings.mlr.press/v267/xu25m.html) | [Code](https://github.com/AI-secure/AdvAgent) | 针对白盒梯度攻击和手工 prompt 都难适用于真实 Web Agent；论文用受害 Agent 的黑盒成败反馈训练 adversarial prompter，并允许低成本改写目标动作；结果在 GPT-4-based Web Agent 上得到高成功率，既有 prompt defense 只能提供有限保护。 |

## Cross-Modal 训练防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | Dual-Modality Multi-Stage Adversarial Safety Training: Robustifying Multimodal Web Agents Against Cross-Modal Attacks | defense、cross-modal injection、adversarial training、multimodal web agent | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.04364) | 暂未公开 | 针对 DOM injection 会同时污染 screenshot 与 accessibility tree、使文本中心防御失效；论文把攻防建模为零和 Markov game，并依次进行 teacher imitation、oracle-guided SFT 与 GRPO self-play；结果在未见任务上显著降低攻击风险，同时把任务完成效率提高约一倍。 |

## URL 与 Web-specific Attack Surface

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;01 | MalURLBench: A Benchmark Evaluating Agents' Vulnerabilities When Processing Web URLs | benchmark、malicious URL、URL obfuscation、URLGuard | ACL 2026 Findings | [arXiv](https://arxiv.org/abs/2601.18113) | [Code](https://github.com/JiangYingEr/MalURLBench) | 针对 Web Agent 接受伪装恶意 URL 后会继续访问危险页面；论文构建覆盖十类场景和七类真实恶意网站的 61,845 个实例，并提出 URLGuard；结果十二种模型普遍难识别精心伪装的 URL。 |

## 良性输入下的 Unintended Harm

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;04 | The Blind Spot of Agent Safety: How Benign User Instructions Expose Critical Vulnerabilities in Computer-Use Agents | benchmark、benign instruction、environmental hazard、OS-BLIND | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.10577) | 暂未公开 | 针对 safety alignment 通常只在 user intent 明显恶意时激活；论文用 OS-BLIND 的环境嵌入威胁和 Agent-initiated harm 测试良性任务；结果多数 CUA ASR 超过 90%，且多 Agent 任务分解会进一步遮蔽整体伤害。 |
| 2026&#8209;04 | AgentHazard: A Benchmark for Evaluating Harmful Behavior in Computer-Use Agents | benchmark、computer-use agent、locally legitimate step、cumulative harm | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.02947) | [Code](https://github.com/Yunhao-Feng/AgentHazard) | 针对单个动作局部合理但组合后越权的 CUA 风险；论文构建 2,653 个实例，将 harmful objective 分解为 operational step；结果显示 model alignment 不能稳定阻断累积上下文和重复 tool use 形成的危险行为。 |
| 2026&#8209;02 | When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents | analysis、benign perturbation、unintended behavior、AutoElicit | ICML 2026 | [arXiv](https://arxiv.org/abs/2602.08235) | [Project](https://osu-nlp-group.github.io/AutoElicit/) | 针对良性输入引发严重 CUA 伤害的案例长期停留在 anecdote；论文用执行反馈迭代扰动良性 instruction 的 AutoElicit 主动搜索 long-tail failure；结果在多种 frontier CUA 上发现数百个经人工确认且可迁移的 unintended behavior。 |
| 2024&#8209;10 | ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents | benchmark、enterprise policy、completion under policy、trustworthiness | ICLR 2026 | [arXiv](https://arxiv.org/abs/2410.06703) | [Project](https://sites.google.com/view/st-webagentbench/home) | 针对 Web benchmark 只计算任务完成而忽略用户同意、边界和企业规则；论文给 222 个任务配套 safety/trustworthiness policy，并定义 Completion under Policy 与 Risk Ratio；结果 nominal completion 明显高估真正合规完成率。 |

## 检测、定位与诊断

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;04 | GUIDE: Interpretable GUI Agent Evaluation via Hierarchical Diagnosis | analysis、GUI trajectory、subtask diagnosis、interpretable evaluator | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.04399) | 暂未公开 | 针对长视觉轨迹的整体 binary judge 难准确定位失败；论文依次做 trajectory segmentation、subtask diagnosis 和 overall aggregation；结果在多个 GUI benchmark 提高评测准确率并输出可行动的 step-level 解释。 |
| 2026&#8209;02 | When Actions Go Off-Task: Detecting and Correcting Misaligned Actions in Computer-Use Agents | defense、action alignment、MisActBench、pre-execution correction | ICML 2026 | [arXiv](https://arxiv.org/abs/2602.08995) | [Project](https://osu-nlp-group.github.io/Misaligned-Action-Detection/) | 针对 CUA 的偏离动作既可来自间接注入也可来自内部推理错误；论文构建 action-level 标注的 MisActBench，并以 DeAction 在执行前检测和迭代修正；结果离线 F1 提升超过 15 个百分点，在线攻击 ASR 降低超过 90%。 |
| 2026&#8209;02 | WebSentinel: Detecting and Localizing Prompt Injection Attacks for Web Agents | detection、web prompt injection、segment localization、context consistency | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.03792) | [Code](https://github.com/wxl-lxw/WebSentinel) | 针对通用 detector 在复杂网页中难定位污染区域；论文先抽取可疑 segment，再按与页面上下文的一致性逐段判断；结果在 clean 与 contaminated webpage 上显著超过既有 detection/localization baseline。 |
| 2025&#8209;10 | WAInjectBench: Benchmarking Prompt Injection Detections for Web Agents | benchmark、multimodal injection、detector evaluation、imperceptible attack | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.01354) | [Code](https://github.com/Norrrrrrr-lyn/WAInjectBench) | 针对 Web Agent prompt injection detector 缺少覆盖 text/image 与 benign content 的系统比较；论文按 threat model 构建多模态恶意和良性数据；结果 detector 能识别显式指令，却普遍难处理无显式 instruction 或 imperceptible perturbation。 |
| 2025&#8209;05 | RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments | benchmark、hybrid sandbox、CUA red teaming、indirect prompt injection | ICLR 2026 Oral | [arXiv](https://arxiv.org/abs/2505.21936) | [Project](https://osu-nlp-group.github.io/RedTeamCUA/) | 针对 Web-only 或 OS-only 环境无法测试跨界攻击；论文以 VM OS 与 Docker web 组成 hybrid sandbox 并发布 RTC-Bench；结果 frontier CUA 在现实 end-to-end 设置仍有显著 ASR，且 attempt rate 揭示能力失败掩盖了安全意图。 |

## Contract、测试与可修复执行

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | WebTestBench: Evaluating Computer-Use Agents towards End-to-End Automated Web Testing | benchmark、web testing、logical constraint、long-horizon reliability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.25226) | [Code](https://github.com/friedrichor/WebTestBench) | 针对 CUA 测试生成网页时静态视觉指标忽略潜在业务和权限约束；论文把任务拆成 checklist generation 与 defect detection，并提供 WebTester；结果暴露测试覆盖不足、检测瓶颈和长程交互不可靠。 |
| 2026&#8209;03 | ContractSkill: Repairable Contract-Based Skills for Multimodal Web Agents | tool、explicit contract、fault localization、local repair | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.20340) | [Code](https://github.com/underfitting-lu/contractskill) | 针对 Web skill 隐式且不稳定、失败后只能整体重写；论文把 skill 转为具有显式程序结构的可执行 contract，以确定性检查定位并局部修复；结果修复后的 artifact 在同一 benchmark family 内可脱离源模型复用。 |

> WebAgentGuard 等独立 guard model 见 [Agent Guardrail 与 Policy Compliance](guardrails-and-policy-compliance.md)；GUI efficiency backdoor 见 [Agent 与多 Agent DoS](../dos/agent-system-dos.md)。
