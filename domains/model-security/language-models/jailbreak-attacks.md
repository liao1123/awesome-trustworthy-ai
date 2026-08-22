# Jailbreak 攻击

[返回 Language Model Security 目录](README.md)

## 研究方向

本页研究攻击者如何在不修改模型参数的条件下绕过语言模型的 safety alignment。攻击面包括单轮语义伪装、obfuscation、reasoning trace 操纵、自动搜索，以及把恶意意图分散到多轮对话中的 context construction；这里关注绕过模型自身拒答边界，来自网页、文档或工具返回内容的 application-level [Prompt Injection](../../misc/prompt-injection.md) 单独维护。

## 研究脉络

- **人工提示构造：** 早期攻击依靠 role-play、编码、语义改写和固定模板隐藏恶意意图，成功率与迁移性强烈依赖人工经验。
- **自动化搜索：** 黑盒反馈、evolutionary optimization 和 agentic autoresearch 开始搜索攻击算法本身，而不只优化单个 prompt。
- **Reasoning 攻击面：** CoT 与内部安全注意力成为新目标，攻击通过拼接推理片段或优化 obfuscation distribution 绕过稀疏安全机制。
- **多轮上下文：** 攻击从单轮伪装扩展到 context routing、渐进式承诺、lexical anchor 和知识库驱动的闭环规划，把意图拆散到整个对话。
- **当前边界：** ASR 必须结合模型版本、judge、query budget、内容质量和 adaptive defense 报告；仅让模型输出敏感词不等同于完成现实危害任务。

## Reasoning、表示与自动化攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | Reasoning as an Attack Surface: Adaptive Evolutionary CoT Jailbreaks for LLMs | attack、CoT jailbreak、evolutionary search、reasoning fragment | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.24497) | 暂未公开 | 针对 reasoning model 的可见思维过程可能形成新攻击面，论文对可迁移 CoT 片段执行 crossover、mutation 与黑盒选择；结果说明优化推理结构而非只改写请求可持续提高越狱成功率。 |
| 2026&#8209;05 | Babel: Jailbreaking Safety Attention via Obfuscation Distribution Optimized Sampling | attack、safety attention、obfuscation distribution、black-box optimization | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.17971) | 暂未公开 | 针对安全对齐可能依赖少量稀疏 attention heads 的问题，论文根据模型反馈优化文本混淆方式的采样分布，使语义仍可被任务模块理解而安全头难以定位；结果提高攻击成功率与查询效率。 |
| 2026&#8209;03 | Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs | attack、autoresearch、attack algorithm synthesis、self-improvement | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.24511) | [Code](https://github.com/romovpa/claudini) | 针对固定人工 jailbreak 很快被防御适配的问题，论文让 autoresearch loop 自动提出、运行和修改白盒攻击算法；结果证明研究 agent 能在给定评测反馈下发现优于初始方法的攻击程序。 |
| 2025&#8209;11 | Evolve the Method, Not the Prompts: Evolutionary Synthesis of Jailbreak Attacks on LLMs | attack、method synthesis、multi-agent evolution、code-level correction | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2511.12710) | [Code](https://github.com/dongdongunique/EvoSynth) | 针对 prompt-level 搜索难以产生结构不同的新攻击，EvoSynth 让多个 Agent 选择、组合并重写可执行攻击方法，同时用运行错误和攻击反馈自我修正代码；结果把自动 red teaming 从提示优化扩展到算法合成。 |

## Black-Box Sampling 与 Open-Ended Red Teaming

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2024&#8209;12 | Best-of-N Jailbreaking | attack、random transformation、black-box sampling、cross-modal scaling | NeurIPS 2025 | [Proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/69f3eb242c7c9df9ea2f2b66ea8b3c0f-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2412.03556) | [Code](https://github.com/jplhughes/bon-jailbreaking) | 针对复杂手工 jailbreak 难迁移且依赖目标内部信息，BoN 对同一请求随机施加文本、图像或音频变换并重复采样；结果攻击成功率随尝试次数呈幂律增长，但查询成本也随 N 快速上升。 |
| 2024&#8209;02 | Rainbow Teaming: Open-Ended Generation of Diverse Adversarial Prompts | tool、quality-diversity search、open-ended red teaming、attack transfer | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2402.16822) | 暂未公开 | 针对定域攻击缺少多样性且依赖人工标注，Rainbow Teaming 将 adversarial prompt generation 建模为 quality-diversity search；结果在所测模型上发现数百个可迁移攻击且 ASR 超过 90%，生成数据还可用于安全微调。 |

## 工作流中的隐式安全失效

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | Internal Safety Collapse in Frontier Large Language Models | analysis、internal safety collapse、workflow context、latent harmful capability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.23509) | [Code](https://github.com/wuyoscar/ISC-Bench) | 针对模型会拒绝直接有害请求却可能在正常专业工作流中生成同类内容的问题，论文用无需对抗伪装的任务链构建 ISC-Bench；结果显示安全对齐常压制表层输出而未移除可被任务上下文调用的底层有害能力。 |

## Multi-Turn Jailbreak

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;01 | ICON: Intent-Context Coupling for Efficient Multi-Turn Jailbreak Attack | attack、multi-turn jailbreak、intent-context coupling、hierarchical recovery | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.20903) | [Code](https://github.com/xwlin-roy/ICON) | 针对逐轮随机构造上下文效率低且容易发生语义漂移的问题，ICON 把恶意意图路由到语义一致的权威场景并用战术与战略两级失败恢复直接生成攻击序列；结果以更少交互获得可迁移的多轮攻击。 |
| 2026&#8209;01 | Knowledge-Driven Multi-Turn Jailbreaking on Large Language Models | attack、multi-turn jailbreak、knowledge repository、planning-reflection loop | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.05445) | 暂未公开 | 针对多轮攻击缺少可复用经验且每次从零探索的问题，Mastermind 将高层规划、低层执行和反思连接到持续更新的攻击知识库；结果通过闭环交互自主发现并复用目标模型的脆弱模式。 |
| 2026&#8209;01 | Multi-Turn Jailbreaking of Aligned LLMs via Lexical Anchor Tree Search | attack、multi-turn jailbreak、lexical anchor、tree search | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.02670) | 论文声明公开，链接待核实 | 针对 attacker LLM 带来的成本与不可控改写，论文从与目标语义相关的 lexical anchor 出发进行 breadth-first tree search 并逐轮注入上下文；结果在不训练攻击模型的条件下构造渐进式越狱路径。 |
| 2025&#8209;12 | RL-MTJail: Reinforcement Learning for Automated Black-Box Multi-Turn Jailbreaking of Large Language Models | attack、multi-turn jailbreak、reinforcement learning、black-box interaction | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2512.07761) | [Code](https://github.com/xxiqiao/RL-MTJail) | 针对多轮黑盒攻击策略难以用静态数据监督，论文用目标模型的交互结果训练 attacker policy 决定下一轮动作；结果让攻击者在有限反馈下自动学习跨轮诱导策略。 |
| 2025&#8209;11 | Foot-In-The-Door: A Multi-turn Jailbreak for LLMs | attack、multi-turn jailbreak、commitment escalation、behavioral persuasion | EMNLP 2025 | [ACL Anthology](https://aclanthology.org/2025.emnlp-main.100/) | [Code](https://github.com/Jinxiaolong1129/Foot-in-the-door-Jailbreak) | 针对单次直接请求容易触发拒答，论文借鉴 foot-in-the-door 效应先诱导模型接受低风险前置请求，再逐步升级承诺；结果在多种模型上显著提高后续有害请求的回答率。 |
| 2025&#8209;09 | X-Teaming Evolutionary M2S: Automated Discovery of Multi-turn to Single-turn Jailbreak Templates | attack、M2S template、evolutionary search、attack distillation | NeurIPS 2025 Lock-LLM Workshop | [arXiv](https://arxiv.org/abs/2509.08729) | [Code](https://github.com/hyunjun1121/M2S-x-teaming) | 针对强 multi-turn attack 交互成本高且难作为单轮测试复用，M2S 以 evolutionary search 将成功轨迹蒸馏为 single-turn template；结果自动发现可迁移模板并保留多轮上下文的越狱优势。 |
| 2025&#8209;08 | Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack | attack、multi-turn jailbreak、crescendo escalation、red teaming | USENIX Security 2025 | [USENIX](https://www.usenix.org/conference/usenixsecurity25/presentation/russinovich) | [Code](https://github.com/Azure/PyRIT) | 针对 safety filter 更擅长阻断显式单轮恶意意图，Crescendo 从无害问题开始并利用模型先前回答逐步升级对话；结果表明自适应多轮语境能绕过多个前沿模型的拒答边界。 |
| 2025&#8209;07 | X-Teaming: Multi-Turn Jailbreaks and Defenses with Adaptive Multi-Agents | attack、multi-turn jailbreak、adaptive multi-agent、attacker-verifier loop | COLM 2025 | [OpenReview](https://openreview.net/forum?id=gKfj7Jb1kj) | [Project](https://x-teaming.github.io/) | 针对单一 attacker 容易在长对话中失去目标，X-Teaming 让规划、攻击与验证 Agent 协作并根据反馈调整策略；结果既生成更强的多轮 jailbreak，也产出可用于防御训练的 XGuard-Train 数据。 |
| 2025&#8209;07 | Chain of Attack: Hide Your Intention through Multi-Turn Interrogation | attack、multi-turn jailbreak、intent concealment、contextual interrogation | Findings of ACL 2025 | [ACL Anthology](https://aclanthology.org/2025.findings-acl.514/) | [Code](https://github.com/YancyKahn/Chain-of-Attack) | 针对显式恶意请求会立即触发拒答，Chain of Attack 将目标拆为语义连续的 interrogation 并利用前轮回答逐步恢复意图；结果在多个 LLM 上提升 concealed jailbreak 成功率并保持对话连贯。 |
| 2025&#8209;04 | Multi-Turn Jailbreaking via Attention Shifting | attack、multi-turn jailbreak、attention shifting、history fabrication | AAAI 2025 | [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/34553) | 暂未公开 | 针对模型安全注意力会受长对话历史重新分配的问题，ASJA 用遗传搜索构造连贯的虚构历史并逐步转移注意力；结果比直接有害提问更容易在多轮末端触发违规回答。 |
| 2025&#8209;02 | Reasoning-Augmented Conversation for Multi-Turn Jailbreak Attacks on Large Language Models | attack、RACE、reasoning state machine、gain-guided exploration | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2502.11054) | [Code](https://github.com/NY1024/RACE) | 针对多轮攻击在隐蔽性和目标语义之间容易漂移，RACE 用 attack state machine、gain-guided exploration、self-play 与 rejection feedback 把有害目标重写为连续推理任务；结果在复杂对话中将 ASR 最高提高 96%。 |
| 2024&#8209;10 | Derail Yourself: Multi-turn LLM Jailbreak Attack through Self-discovered Clues | attack、ActorAttack、actor-network clue、semantic distribution shift | 未注明（arXiv） | [arXiv v1](https://arxiv.org/abs/2410.10700v1) | [Code](https://github.com/AI45Lab/ActorAttack) | 针对固定 seed 限制多轮攻击路径多样性，ActorAttack 从模型知识中发现与目标关联的 actor network 并据此构造隐蔽对话链；结果在多个 aligned LLM 上超过单轮与多轮基线，后续版本将论文重命名并扩展为 natural distribution shift 分析。 |
| 2024&#8209;09 | Red Queen: Exposing Latent Multi-Turn Risks in Large Language Models | attack、RED QUEEN、concealed intent、scenario generation | Findings of ACL 2025 | [ACL Anthology](https://aclanthology.org/2025.findings-acl.1311/) · [arXiv](https://arxiv.org/abs/2409.17458) | [Code](https://github.com/kriti-hippo/red_queen) | 针对单轮 red teaming 无法覆盖以“防止伤害”为伪装的长期对话，RED QUEEN 从四十个场景生成跨十四类风险的多轮攻击；结果 GPT-4o ASR 达 87.6%，配套 RED QUEEN GUARD 可将所测 ASR 降至 1% 以下。 |
