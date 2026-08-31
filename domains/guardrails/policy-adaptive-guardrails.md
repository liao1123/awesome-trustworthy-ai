# Policy-Adaptive Guardrail

[返回 Guardrail 领域目录](README.md)

## 研究方向

本页研究把自然语言 policy、用户规则、平台规范或法规作为 guardrail 的显式输入，使审核标准可以在推理时变化，而不必为每套 taxonomy 重新训练模型。核心问题包括未见规则的组合泛化、复杂 policy 的逐条执行、reasoning 与最终 label 的一致性、低延迟部署，以及从合成数据、用户反馈和历史事件中持续更新规则。

## 研究脉络

- **固定 taxonomy 到可变 policy：** 研究从预定义 harm category 的二分类器转向把 policy 本身作为条件，要求同一内容在不同规则和严格度下得到不同判断。
- **Policy reasoning：** GSPR、DynaGuard 等工作用 reasoning trace、SFT 或 RL 学习逐条执行未见规则，PL-Guard 则把 neural grounding 与 ProbLog policy inference 分离，使规则依据和 safety-helpfulness trade-off 可审计。
- **效率与一致性：** LPG、ConsisGuard 和 FlexGuard 分别探索 latent reasoning、deliberation-enforcement 对齐和连续风险分数，降低动态规则带来的延迟与决策不稳定。
- **持续适应与工作流：** LiSA 将事故反馈归纳为可更新 memory，PolicyGuide 则把判断对象从单次 action 扩展到完整 Agent workflow。
- **评测边界：** SafePyramid 等 benchmark 开始覆盖层级规则、多轮上下文和 policy conflict，而 policy-as-prompt 研究表明仅把规则附在 prompt 中并不保证稳定执行或公平治理。

## 动态 Policy 执行与适应

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | CAITLYN: Can LLM Agents Autonomously Synthesize Defenses against Emerging Injection Attacks? ↗ | defense、lifelong guardrail、defense library、verified adaptation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.27990) | [Code](https://github.com/liangzid/caitlyn) | 针对部署规则无法跟随新型注入持续更新，CAITLYN 把低成本规则、精确 LLM 判断和异常驱动的防御合成组织为可增长 library，并在加入新能力前执行验证；完整系统在 delivery-aware Emerging benchmark 上补足静态库的盲点，同时保持较低在线 token 开销。 |
| 2026&#8209;08 | Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator ↗ | tool、custom-policy moderation、policy reasoning、selective explanation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.27548) | [Model](https://huggingface.co/nvidia/Nemotron-3.5-Content-Safety) · [Dataset](https://huggingface.co/datasets/nvidia/Nemotron-3.5-Content-Safety-Dataset) | 针对固定 taxonomy 的 guard 无法随应用领域规则变化，Nemotron 3.5 CS 可读取 supplied custom policy，在低延迟模式直接返回 label，并按需生成简洁推理、指出违规类别；配套数据包含 custom-policy example，评测同时检查 policy following、误报和计算成本。 |
| 2026&#8209;08 | SPA: Securing Persistent LLM Agents Across Queries with Plan-First Information-Flow Control | defense、information-flow policy、label-preserving persistence、security-utility trade-off | 未确认（arXiv Comments：Submitted to USENIX Security 2027） | [arXiv](https://arxiv.org/abs/2608.27234) | 暂未公开 | 针对静态输入过滤无法约束攻击数据在计划、控制依赖和后续查询中的传播，SPA 以双格 confidentiality／integrity policy 动态检查完整可执行计划，并让持久 artifact 保留标签；它把即时与延迟攻击成功率分别降至 0 和 0.2%，同时量化严格 integrity enforcement 带来的安全—效用权衡。 |
| 2026&#8209;08 | A Self-Evolving Multi-Agent Framework Defense against LLM Jailbreak Attacks | defense、failure-induced rule、expanding label space、cross-interaction adaptation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.26008) | 暂未公开 | 该框架不固定部署时的攻击 taxonomy，而是在每次成功绕过后归纳结构化 method-level rule、持久保存并用于未来输入，新的 wrapper 还会扩展 rule label space；无需参数更新的 policy memory 对同族攻击与自适应组合攻击均能持续适配，且没有随规则增长提高误拒。 |
| 2026&#8209;08 | LMSM: LLM Security Framework Inspired by Linux Security Modules | defense、versioned policy、backend-policy separation、rule composition | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.25697) | [Code](https://github.com/xiuyuz/LMSM) | LMSM 不把安全信号、policy logic 和介入代码绑定为单一 detector，而是让版本化 policy 在可信逐请求上下文上组合 active rules，再由独立 gate 执行判定；因此 backend、规则与检查 schedule 可以分别更新而无需重建 serving enforcement。 |
| 2026&#8209;08 | AgentFlow: A Flow-Centric Policy Language and Framework for Securing LLM Agent Systems | defense、policy language、path rule、task-scoped capability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.22868) | 暂未公开 | AgentFlow 用可执行的 flow/path 规则表达“何种数据在当前任务中可经过哪些边、向何处受控释放”，并把 task scope、taint state 和 delegation authority 纳入策略状态；reference monitor 与 SMT verifier 分别提供动态执行和结构化策略片段的形式检查。 |
| 2026&#8209;08 | RePolicy: Reinforcement Learning for Safety-Policy Invocation in Agent Safeguards | defense、dynamic policy invocation、verifiable reward、policy-context perturbation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.24275) | [Code](https://github.com/jianghoucheng/RePolicy) | 针对 prompting 和监督微调难以适应未见轨迹及变化的 policy context，RePolicy 从动态策略库调用当前适用规则，并以 PolicyTraj-20K 初始化、可验证奖励 GRPO 和 policy-context 扰动训练 policy-grounded 判断；结果在六个 Agent 安全基准上保持稳健的策略调用。 |
| 2026&#8209;08 | PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-Compliant LLM Agents | defense、workflow policy、persistent state graph、proactive verifier | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19861) | 暂未公开 | 针对逐 action guard 无法发现客服 Agent 漏做身份核验、确认或其他跨步骤 policy 要求，PolicyGuide 将组织规则编译为持续更新的 workflow graph，并在每个用户轮次边界主动核对未完成请求与下一步修复；GPT-5.4 在 τ²-bench 三领域的平均 Pass^4 从 0.42 提高到 0.62，且可迁移到 Claude 与 Gemini。 |
| 2026&#8209;08 | PL-Guard: Probabilistic Logic Reasoning for LLM Guardrails | defense、neurosymbolic guardrail、ProbLog、policy consistency | IJCAI 2026 LSRLM Workshop（preliminary version） | [arXiv](https://arxiv.org/abs/2608.15673) | 暂未公开 | 针对同一 LLM 混合 semantic grounding 与 policy reasoning 容易违规放行或过度拒答，PL-Guard 让本地 LLM 输出 predicate probability 并由 ProbLog 按显式规则推理；XSTest 上 unsafe compliance 从 22.0% 降至 0.5%，但 over-refusal 高于 LLM judge。 |
| 2026&#8209;08 | SCOPE: Streaming Covariance-Orthogonal Post-Hoc Editing for Continual LLM Safety Governance | defense、continual safety editing、post-hoc governance、capability retention | KDD 2026 | [Official](https://doi.org/10.1145/3770855.3817993) | 暂未公开 | SCOPE 以 streaming covariance 约束连续 post-hoc 安全编辑，避免多轮政策更新相互干扰并尽量保持原有通用能力。 |
| 2026&#8209;06 | SingGuard: A Policy-Adaptive Multimodal LLM Guardrail with Dynamic Reasoning | defense、policy-adaptive guard、multimodal moderation、dynamic reasoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.22873) | [Code](https://github.com/inclusionAI/Sing-Guard) | 针对固定 taxonomy 难以适应新规则和跨模态内容，论文训练能读取 policy 并动态生成判断依据的 multimodal guardrail；结果在统一模型中支持规则切换、细粒度分类与解释。 |
| 2026&#8209;05 | ConsisGuard: Aligning Safety Deliberation with Policy Enforcement in LLM Guardrails | defense、policy enforcement、trajectory distillation、functional coupling | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.31073) | 暂未公开 | 针对 reasoning 内容与最终 safe/unsafe label 可能互相矛盾，论文用 Policy-to-Decision Trajectory Distillation 和 Functional Coupling Alignment 联合训练；结果缩小了安全 deliberation 与 policy enforcement 之间的执行缺口。 |
| 2026&#8209;05 | LPG: Balancing Efficiency and Policy Reasoning in Latent Policy Guardrails | defense、latent policy reasoning、fixed-budget inference、latency | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.17329) | [Code](https://github.com/SaFo-Lab/Latent_Policy_Guard) | 针对动态 policy 需要复杂 reasoning 但显式 CoT 延迟高，论文把逐条规则推理压缩到固定的 10 个 latent token；结果在保留 policy reasoning 能力的同时将推理加速约 11 倍。 |
| 2026&#8209;05 | LiSA: Lifelong Safety Adaptation via Conservative Policy Induction | defense、lifelong adaptation、policy induction、structured memory | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.14454) | 暂未公开 | 针对部署后出现的新风险只有稀疏且带噪的事故反馈，论文保持基础 guard 不变并把可靠反馈归纳为结构化 policy memory；结果让 guardrail 在不过度追随噪声的前提下持续适应新规则。 |
| 2026&#8209;04 | BARRED: Synthetic Training of Custom Policy Guardrails via Asymmetric Debate | defense、custom policy guard、asymmetric debate、synthetic training | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/64273) · [arXiv](https://arxiv.org/abs/2604.25203) | [Code](https://github.com/plurai-ai/BARRED) | 针对自定义 policy 缺少大规模标注样本，论文让立场不对称的 debating agents 围绕规则生成并筛选困难案例；结果以合成数据训练出可执行用户 policy 的专用 guardrail。 |
| 2026&#8209;02 | FlexGuard: Continuous Risk Scoring for Strictness-Adaptive LLM Content Moderation | defense、continuous risk score、strictness adaptation、risk calibration | ACL 2026 Main | [ACL Anthology](https://aclanthology.org/2026.acl-long.263/) · [arXiv](https://arxiv.org/abs/2602.23636) | [Code](https://github.com/TommyDzh/FlexGuard) | 针对不同平台严格度无法由固定二分类标签表达，论文学习连续且校准的 risk score，再由部署方调整阈值；结果使同一 guard model 能随 moderation strictness 改变决策边界。 |
| 2026&#8209;02 | CourtGuard: A Model-Agnostic Framework for Zero-Shot Policy Adaptation in LLM Safety | defense、zero-shot policy adaptation、policy retrieval、multi-agent debate | 未确认（arXiv Comments：Under review） | [arXiv](https://arxiv.org/abs/2602.22557) | 暂未公开 | 针对新 policy 到来时重训 guard 成本高，论文先检索相关规则，再由 attacker、defender 和 judge 围绕具体案例辩论；结果提供不改基础模型的 zero-shot policy adaptation。 |
| 2026 | Stay in Character, Stay Safe: Dual-Cycle Adversarial Self-Evolution for Role-Playing Agents ↗ | defense、persona policy、hierarchical safety rule、adaptive guard | IJCAI-ECAI 2026 | [Accepted](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track) · [Preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/5873.pdf) | 暂未公开 | 针对不同角色的安全约束不能由同一静态拒答模板表达，DASE 将失败经验分层为通用安全规则、persona-specific constraint 和可复用示例，并按当前角色检索执行；这种外部 policy memory 可随对抗循环更新，在提高安全时保留角色行为。 |
| 2025&#8209;10 | Learning Efficient Guardrails for Compliance | defense、policy trajectory、prefix violation、efficient compliance | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/60652) · [arXiv](https://arxiv.org/abs/2510.03485) | [Project](https://rakanwen.github.io/policyguard-page/) | 针对 Agent 合规必须在违规动作执行前识别 trajectory prefix，论文构建 PolicyGuardBench 并训练小型 PolicyGuard；结果表明专用 guard 能以低于通用 LLM judge 的成本执行细粒度 policy。 |
| 2025&#8209;09 | GSPR: Aligning LLM Safeguards as Generalizable Safety Policy Reasoners | defense、policy reasoning、GRPO、unseen taxonomy | ICLR 2026 Withdrawn | [OpenReview](https://openreview.net/forum?id=H2e5TerulJ) · [arXiv](https://arxiv.org/abs/2509.24418) | [Supplement](https://openreview.net/attachment?id=H2e5TerulJ&name=supplementary_material) | 针对 guard model 绑定固定 taxonomy 后难以泛化到新规则，论文用 cold-start SFT、GRPO 和 rule-based rewards 训练 policy-conditioned reasoner；结果能按输入 policy 输出安全结论与细粒度违规类别。 |
| 2025&#8209;09 | Scaling Policy Compliance Assessment in Language Models with Policy Reasoning Traces | defense、policy reasoning traces、compliance assessment、trace supervision | ICLR 2026 Reject | [OpenReview](https://openreview.net/forum?id=QgEDWbZQ6V) · [arXiv](https://arxiv.org/abs/2509.23291) | [Code](https://github.com/imperialite/policy-reasoning-traces) | 针对复杂 policy 的最终标签监督不足以教会模型稳定执行规则，论文生成并筛选 policy reasoning traces 作为中间监督；结果显示轨迹增强可扩展合规评估，但仍依赖高质量规则解释。 |
| 2025&#8209;09 | DynaGuard: A Dynamic Guardian Model With User-Defined Policies | defense、user-defined policy、fast-slow inference、dynamic taxonomy | ICLR 2026 | [Official](https://iclr.cc/virtual/2026/poster/10008138) · [OpenReview](https://openreview.net/forum?id=gc8Ylt0lbm) · [arXiv](https://arxiv.org/abs/2509.02563) | [Code](https://github.com/montehoover/DynaGuard) | 针对静态 harm category 无法覆盖用户新定义的风险，论文联合 DynaBench 训练能读取任意规则并在快速分类与解释性 reasoning 间切换的 guard；结果提高了对未见 policy 的泛化。 |
| 2025&#8209;08 | Towards Trustworthy Multimodal Moderation via Policy-Aligned Reasoning and Hierarchical Labeling ↗ | defense、in-context policy、rule-grounded moderation、taxonomy adaptation | KDD 2026 | [Official](https://doi.org/10.1145/3770854.3783934) · [arXiv](https://arxiv.org/abs/2508.03296) | [Code](https://github.com/lianqi1008/Hi-Guard) | 针对固定标签训练难跟随平台 moderation rule 演化，Hi-Guard 将 policy definition 直接置入 model prompt，并让模型沿对应层级 taxonomy 执行 rule-grounded path classification；实验与真实部署显示这种 policy-conditioned 决策较纯 noisy-label 学习具有更好的泛化和可审计性。 |
| 2025&#8209;05 | PAM: Training Policy-Aligned Moderation Filters at Scale | defense、policy-aligned moderation、synthetic data、filter distillation | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2505.19766) | 暂未公开 | 针对每次调用大模型读取 policy 的推理成本，论文按用户或开发者规则自动合成数据并蒸馏小型 moderation filter；结果让 policy 在训练后内化到低延迟分类器中。 |

## 基础 Tool

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Granite.Trust Policy Tools: Shareable, Actionable Policies for Generative AI Applications | tool、actionable policy、content constraint、runtime monitoring | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.23870) | [Code](https://github.com/ibm-granite/granite.trust.policy-tools) | 针对传统访问控制 policy 无法表达生成式 AI 响应中的内容约束，论文开源 YAML Actionable Policy schema、policy-aligned 合成数据流水线及策略定义与执行工具；使组织可将一次定义的 policy 贯穿模型对齐、测试与运行时监控。 |

## Benchmark 与 Policy 质量分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | ReguSim: Evaluating LLM Agent Rule Grounding in Financial Compliance | benchmark、dynamic rule grounding、execution evidence、monitor reliability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19974) | 暂未公开 | 针对 Agent 口头引用规则并不能证明真实 action 合规，ReguSim 将显式金融规则、尝试动作、执行层强制结果和 monitor 可见证据分离；实验显示自然语言 rationale 会误导 prompt-only monitor，而展示 enforcement evidence 或使用结构化特征的简单基线更可靠。 |
| 2026&#8209;07 | It is not enough to give your moderation rules to ChatGPT: Policy-as-Prompt Moderation and Its Potential Impacts on Community Governance | analysis、policy-as-prompt、community moderation、governance impact | MuC 2026 Workshop | [arXiv](https://arxiv.org/abs/2607.12149) | 暂未公开 | 针对社区将版规直接交给通用 LLM 即视为可执行 moderation policy 的做法，论文评测规则表述与语境变化下的判断；结果说明 policy-as-prompt 会产生不稳定执行，并可能改变社区治理权力关系。 |
| 2026&#8209;06 | SafePyramid: A Hierarchical Benchmark for In-context Policy Guardrailing | benchmark、in-context policy guard、hierarchical rules、multi-turn dialogue | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.29887) | [Code](https://github.com/bytedance/safepyramid) | 针对现有评测缺少多层规则、规则冲突和多轮语境，论文构建覆盖 1,000 段对话、3,000 套 policy 与 61,699 条规则的 hierarchical benchmark；结果揭示 guard model 在细粒度 rule execution 上仍有明显缺口。 |
| 2026&#8209;05 | Improving Labeling Consistency with Detailed Constitutional Definitions and AI-Driven Evaluation | analysis、constitutional definition、label consistency、AI evaluation | ARR（投稿中） | [arXiv](https://arxiv.org/abs/2605.24247) | 暂未公开 | 针对宽泛 safety label 导致人工与模型标注者分歧，论文把类别扩展为详细 constitutional definition 并引入 AI-assisted evaluation；结果表明明确规则边界可提高跨标注者一致性。 |

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | The Guard That Cried Wolf: How Scary Words Make Agent Guardrails Refuse Legitimate Actions | benchmark、authorization policy、decision boundary、policy-aware guardrail | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.27009) | 暂未公开 | 针对同一 action 是否安全由部署时授权 policy 决定、人工逐样本标签无法可靠表达该边界的问题，Cautious Bench 让每个 allow／deny label 成为显式策略的机械推论；六个 guardrail 在只改变对象名的对照中仍系统误拒已授权动作，说明 policy-aware enforcement 不能以表面危险词替代上下文推理。 |
| 2026 | COMPASS: A Framework for Evaluating Organization-Specific Policy Alignment in LLMs | benchmark、safety alignment、policy-aware guardrail、runtime policy | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.2139/) | 暂未公开 | 针对企业 LLM 评测只覆盖通用危害而忽略组织政策，COMPASS 在八类行业场景构造 5,920 个 allow/denylist 请求，发现七个模型对合法请求超过 95% 准确，却只拒绝 13%–40% 的对抗性禁用请求。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | DUET: Dual-Teacher On-Policy Distillation via Same-Weight Disagreement for Prohibition Compliance | analysis、policy-aware guardrail、runtime policy、policy compliance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14644) | 暂未公开 | 现实世界中的 LLM 部署越来越依赖于运行时注入的禁令（企业策略、PII 红线、工具边界），这些禁令因请求和租户而异；我们提出 DUET，一种用于遵守禁令的代币选择性策略蒸馏方法。 |

## 相关研究博客

| 时间 | 标题 | 发布机构或作者 | 关联主题 | 链接 | 核心内容 |
| --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Cisco AI Defense Policy Studio: Turning Unwritten Policy into Adaptive AI Guardrails | Cisco | adaptive policy、policy authoring、enterprise deployment | [Cisco](https://blogs.cisco.com/ai/cisco-ai-defense-policy-studio-turning-unwritten-policy-into-adaptive-ai-guardrails) | 从企业部署角度说明如何把分散在文档和团队经验中的未成文规则转成可测试、可版本化的 guardrail policy，并展示 policy 更新和执行反馈如何形成持续治理流程。 |
