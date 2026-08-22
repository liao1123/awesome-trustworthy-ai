# Jailbreak 防御与评测

[返回 Language Model Security 目录](README.md)

## 研究方向

本页研究如何检测和缓解语言模型 jailbreak，并判断防御是否真正提高部署安全。除 ASR 外，评测需要同时检查 adaptive attack、benign utility、over-refusal、inference cost、response quality 和 judge reliability；防御可位于内部表示、解码过程、对话状态或训练阶段，独立内容审核模型仍由 [Guardrail](../../guardrails/README.md) 维护。

## 研究脉络

- **输出结果评测：** 早期 benchmark 主要统计 harmful prompt 的拒答与攻击成功率，容易忽略回答质量、judge 偏差和模型能力变化。
- **内部检测：** hidden state、gating feature、refusal trajectory 和 token-level probe 用模型仍保留的安全信号识别经过改写的攻击。
- **多轮状态防御：** 防御从逐条 prompt 分类扩展到风险随对话累积、批处理稀释和跨轮意图转移。
- **训练时适应：** self-play、对抗数据与多轮 safety alignment 让模型面对不断变化的攻击，而非记忆固定模板。
- **统一代价：** 最新研究把 safety、utility 与 compute/cost 放到同一评测中，揭示“更强防御”可能只是通过过度拒答或能力下降换取较低 ASR。

## Benchmark、Trade-off 与失效边界

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Safety in Batches? Understanding and Mitigating Safety Failures in Batch Prompting | analysis、batch prompting、refusal dilution、batch-aware DPO | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.02681) | 暂未公开 | 针对单条输入会被拒绝的有害请求在与良性请求成批提交时可能被回答，论文分析训练阶段 preference signal weakening 与推理阶段 refusal signal dilution；结果表明 batch-aware DPO 可显著缓解这一组合式安全失效。 |
| 2026&#8209;07 | When LLM Defenses Backfire: Characterizing Safety, Performance, and Cost Trade-offs | benchmark、jailbreak defense、safety-utility-cost、over-refusal | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.24392) | 暂未公开 | 针对 defense 排名通常只看 ASR，论文在统一框架中同时测量安全、任务能力、误拒和推理成本；结果发现部分看似更强的防御主要通过显著能力下降、over-refusal 或额外计算获得低攻击率。 |
| 2026&#8209;06 | When Medical Safety Alignment Fails: A Benchmark for Evaluating LLMs on High-Risk Medical Queries | benchmark、medical safety、high-risk query、domain evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.28332) | 暂未公开 | 针对通用有害内容 benchmark 难以覆盖医疗建议中的情境风险，论文构建高风险医疗查询并区分拒答、风险说明与可接受帮助；结果揭示通用 safety alignment 在专业医疗边界上的系统性缺口。 |
| 2026&#8209;05 | Jailbroken Frontier Models Retain Their Capabilities | analysis、jailbreak tax、frontier model、capability retention | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.00267) | 暂未公开 | 针对 jailbreak 是否因破坏模型能力才降低安全约束，论文在多类攻击后重新测量通用任务表现；结果显示前沿模型通常保留大部分能力，且模型越强 jailbreak tax 越小，低 ASR 不能用能力崩溃简单解释。 |
| 2025&#8209;12 | Response-Based Knowledge Distillation for Multilingual Jailbreak Prevention Unwittingly Compromises Safety | analysis、multilingual distillation、refusal imitation、safety regression | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.11157) | 暂未公开 | 针对用安全 teacher response 蒸馏多语言拒答是否可靠，论文比较 response-based knowledge distillation 前后的 jailbreak 行为；结果部分设置的 JSR 反而增加最多 16.6 个百分点，说明表面模仿拒答可能损害底层安全。 |
| 2025&#8209;07 | A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks | analysis、multi-turn jailbreak、representation drift、Crescendo | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2507.02956) | 暂未公开 | 针对 representation-engineering defense 为何会在 Crescendo 后期失效，论文逐轮追踪模型对对话的 harmfulness representation；结果安全感知随轮次向 benign 区域漂移，说明多轮上下文本身会侵蚀防御信号。 |
| 2024&#8209;08 | LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet | benchmark、human jailbreak、multi-turn evaluation、defense robustness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2408.15221) | 暂未公开 | 针对自动单轮攻击可能高估现有 defense robustness，论文收集人类构造的多轮 jailbreak 并统一测试多类防御；结果现有方法仍会被对话级策略系统突破，单轮安全分数不能代表真实交互风险。 |

## 内部信号检测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | Tracing the Dynamics of Refusal: Exploiting Latent Refusal Trajectories for Robust Jailbreak Detection | detection、refusal trajectory、forced decoding、latent dynamics | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.02958) | 暂未公开 | 针对最终 hidden state 会掩盖模型先前出现的拒答反应，论文用 forced decoding 追踪跨 token 的 latent refusal trajectory 并构建 SALO；结果对多类未知 jailbreak 保持较高检测率。 |
| 2026&#8209;01 | Be Your Own Red Teamer: Safety Alignment via Self-Play and Reflective Experience Replay | defense、self-play alignment、reflective replay、adaptive red teaming | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.10589) | 暂未公开 | 针对 defense 容易过拟合已知攻击模板，论文让同一模型在强化学习循环中交替扮演 attacker 与 defender，并把失败经验反思后回放；结果动态演化攻击的同时增强对新 jailbreak 的拒答泛化。 |
| 2026&#8209;01 | Defending Large Language Models Against Jailbreak Attacks via In-Decoding Safety-Awareness Probing | detection、in-decoding probing、safety awareness、token intervention | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.10543) | [Code](https://github.com/zyz13590/SafeProbing) | 针对模型被越狱后内部仍出现安全信号却被流畅续写压过的问题，SafeProbing 在生成过程中读取 safety-aware representation 并及时干预解码；结果比只检查最终输出更早发现和阻断有害轨迹。 |
| 2026&#8209;01 | ALERT: Zero-shot LLM Jailbreak Detection via Internal Discrepancy Amplification | detection、zero-shot detection、internal discrepancy、gating activation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.03600) | 暂未公开 | 针对检测器训练时无法预见新 jailbreak template，ALERT 在层、模块和 token 级放大良性与对抗输入的内部差异；结果表明浅层 hidden state 与 gating/context feature 保留可用于 zero-shot 检测的安全信号。 |
| 2025&#8209;09 | ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack | defense、activation scaling、targeted jailbreak、inference-time guard | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2509.25843) | 暂未公开 | 针对 targeted jailbreak 会把 hidden state 推向特定有害目标而通用 refusal steering 区分度不足，ASGuard 定位并缩放目标相关 activation；结果以推理期轻量干预降低攻击成功率并保持良性回答能力。 |

## Multi-Turn 与 Inference-Time Defense

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | THRD: A Training-Free Multi-Turn Defense Framework for Jailbreak Attacks on Large Language Models | defense、multi-turn defense、temporal risk accumulation、training-free | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.01738) | 暂未公开 | 针对逐轮分类会漏掉分散在长对话中的恶意意图，THRD 累积 temporal risk 并在风险跨阈值时触发干预；结果在保持良性任务效用的同时将多轮攻击成功率压到较低水平。 |
| 2026&#8209;06 | SafeSpec: Fast and Safe LLM via Dynamic Reflective Sampling | defense、speculative decoding、risk-aware verification、reflective sampling | ICML 2026 | [ICML](https://icml.cc/Downloads/2026) · [arXiv](https://arxiv.org/abs/2606.19755) | [Code](https://github.com/HaotianXu1/SafeSpec) | 针对既有 safety defense 会破坏 speculative decoding 的加速机制，SafeSpec 在 target verification 中联合检查语义与风险，并在不安全时 rollback 后 reflective multi-sampling；结果在 Qwen3-32B 上降低 15% ASR，同时保持 2.06 倍良性推理加速。 |
| 2026&#8209;05 | REFLECTOR: Internalizing Step-wise Reflection against Indirect Jailbreak | defense、step-wise reflection、indirect jailbreak、self-correction | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.20654) | 暂未公开 | 针对外部不可信内容会在长推理中逐步覆盖原始指令，REFLECTOR 通过 teacher-guided SFT 与 RL 把逐步风险反思内化进模型；结果 defense success rate 超过 90%，并使 GSM8K 提高 5.85 个百分点。 |
| 2026&#8209;05 | Mitigating Many-shot Jailbreak Attacks with One Single Demonstration | defense、many-shot jailbreak、SafeEnd、representation restoration | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.08277) | [Code](https://github.com/Thecommonirin/SafeEnd) | 针对 many-shot context 会产生类似隐式恶意微调的表示漂移，SafeEnd 仅在上下文末尾追加一个有害请求到安全拒答的 demonstration；结果将模型表示拉回 refusal region，并以单个样例缓解长上下文攻击。 |
| 2026&#8209;01 | HoneyTrap: Deceiving Large Language Model Attackers to Honeypot Traps with Resilient Multi-Agent Defense | defense、multi-agent honeypot、attacker deception、resource exhaustion | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.04034) | 暂未公开 | 针对被动拒答会向自适应 multi-turn attacker 暴露防御边界，HoneyTrap 以四个 Agent 识别、误导并把攻击引向 honeypot；结果提高误导率和攻击资源消耗，但也引入额外编排成本。 |
| 2025&#8209;11 | X-Boundary: Establishing Exact Safety Boundaries via Dual-Objective Optimization | defense、safety boundary、dual-objective optimization、over-refusal | Findings of EMNLP 2025 | [ACL Anthology](https://aclanthology.org/2025.findings-emnlp.282/) | [Code](https://github.com/AI45Lab/X-Boundary) | 针对安全训练在有害拒答与良性帮助之间边界模糊，论文联合优化 harmful robustness 与 benign utility 来显式收紧 decision boundary；结果改善 jailbreak 防御同时降低对相近但无害请求的误拒。 |
| 2025&#8209;10 | Proactive defense against LLM Jailbreak | defense、proactive deception、iterative jailbreak、spurious response | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.05052) | 暂未公开 | 针对直接拒答会为迭代攻击提供继续优化的真实反馈，ProAct 返回看似成功但无害的 spurious response 误导 attacker 提前停止搜索；结果最高降低 94% ASR 且不影响所测 utility，与其他防御组合时可进一步压低攻击率。 |
| 2025&#8209;07 | MTSA: Multi-Turn Safety Alignment for Large Language Models | defense、multi-turn alignment、conversation-level objective、intent transition | ACL 2025 | [ACL Anthology](https://aclanthology.org/2025.acl-long.1282/) | [Code](https://github.com/yuki-younai/MTSA) | 针对单轮 safety data 无法训练模型理解跨轮意图变化，MTSA 构造多轮对话并在 conversation level 优化安全响应；结果提高模型对渐进式 jailbreak 的识别与拒答，而非逐轮孤立判断。 |

> 多模态输入特有的 visual jailbreak 防御见 [VLM Jailbreak 与 Adversarial Attack](../multimodal-models/vlm-jailbreak-and-adversarial-attacks.md)；外部 classifier 与 production guard 架构见 [通用 Guard Model、评测与安全边界](../../guardrails/general-models-and-evaluation.md)。
