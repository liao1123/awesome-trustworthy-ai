# Reasoning 与效率权衡

[返回 Guardrail 领域目录](README.md)

## 研究方向

本页研究 guardrail 是否需要显式 reasoning、reasoning 如何提高复杂意图与边界案例的判断，以及怎样把这些能力压缩成可部署的低延迟模型。主要路线包括生成 CoT 或 reflection、训练期 reasoning 与推理期 label-only、连续 latent reasoning、encoder classifier、大小模型 routing，以及对解释忠实性、吞吐、false-positive rate 和 hard-case 能力的受控比较。

## 研究脉络

- **生成式判断：** GuardReasoner、ThinkGuard 等工作让 guard 在输出 label 前生成 policy-grounded reasoning 或反思轨迹，以处理伪装意图并提供解释。
- **Reasoning 的作用检验：** 后续实证研究区分“推理真正改变 verdict”和“对既定判断的事后解释”，开始质疑通用 benchmark 是否足以证明 CoT 必要。
- **推理内化：** DT-Guard 将 reasoning 只用于训练，CoLaGuard 和 LPG 则在连续 latent state 中传播推理，试图保留 hard-case 能力而不生成长链。
- **轻量分类与路由：** SafeRoute 把困难样本交给大 guard，GLiGuard 与 LeanGuard 直接使用 bidirectional encoder；结果显示架构、数据和阈值校准可能比显式 CoT 更影响当前任务。
- **多模态实时审核：** ResponseGuard 把图像、请求和响应池化后一次前向判断，进一步将效率问题推进到 sentence-level streaming 场景。

## 显式 Reasoning 与反思

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | A Dual-Hypothesis Reasoning Framework for LLM Guardrails | defense、dual-hypothesis reasoning、evidence phrase、MC-SFT | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.17575) | 暂未公开 | 针对单一路径 reasoning 容易忽略 prompt 的安全或有害替代解释，论文提出 ARBITER 同时论证两种 hypothesis 并用 MC-SFT 分项训练输出；结果提升 out-of-domain moderation，并为 unsafe verdict 给出 evidence phrase。 |
| 2026&#8209;05 | Reflect-Guard: Enhancing LLM Safeguards against Adversarial Prompts via Logical Self-Reflection | defense、self-reflection、adversarial prompt、trajectory distillation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.24834) | 暂未公开 | 针对角色扮演、虚构语境和间接请求隐藏有害意图，论文从教师模型蒸馏 reflection trace 并微调 Llama-Guard-3；结果让模型在 verdict 前重新检查逻辑与真实意图，提高对包装型 jailbreak 的识别。 |
| 2025&#8209;02 | ThinkGuard: Deliberative Slow Thinking Leads to Cautious Guardrails | defense、slow thinking、deliberative reasoning、jailbreak detection | Findings of ACL 2025 | [ACL Anthology](https://aclanthology.org/2025.findings-acl.704/) · [arXiv](https://arxiv.org/abs/2502.13458) | [Code](https://github.com/luka-group/ThinkGuard) | 针对快速分类容易被复杂语境与对抗措辞误导，论文训练 guard 先生成 deliberative reasoning 再给出安全判断；结果显示 slow-thinking supervision 能提高谨慎性与 jailbreak detection。 |
| 2025&#8209;01 | GuardReasoner: Towards Reasoning-based LLM Safeguards | defense、reasoning guard、reasoning SFT、safety reward | ICLR 2025 Workshop | [arXiv](https://arxiv.org/abs/2501.18492) | [Code](https://github.com/yueliu1999/GuardReasoner) | 针对传统 guard 只给 label、难处理复杂意图且不可解释，论文构建 reasoning 数据并结合 SFT 与安全奖励训练生成式 safeguard；结果建立了 reasoning-based guardrail 的代表性开源基线。 |
| 2025 | Safety Through Reasoning: An Empirical Study of Reasoning Guardrail Models | analysis、reasoning guard、verdict faithfulness、empirical study | Findings of EMNLP 2025 | [ACL Anthology](https://aclanthology.org/2025.findings-emnlp.1193/) | 暂未公开 | 针对 reasoning guard 的提升究竟来自推理还是更强模型与数据尚不清楚，论文系统分析 chain 与 verdict 的关系及不同设置下的审核能力；结论限定了仅凭可读 CoT 断言决策更可靠的范围。 |

## 推理内化、轻量分类与路由

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | When Are Reasoning-Based Guardrails Not Efficient? ResponseGuard: A Fast Vision-Language Guard for Real-Time Moderation | defense、vision-language guard、single-pass classifier、streaming latency | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.21401) | [Code](https://github.com/ndb796/ResponseGuard) | 针对 VLM response guard 先生成 CoT 才给 verdict 无法跟上流式输出，论文从图像、请求和响应的 pooled representation 一次前向分类；2B 模型在 response harmfulness 上超过对比的 3B reasoning guard，时间成本约低 150 倍，但 image-only 判断仍是短板。 |
| 2026&#8209;07 | DT-Guard: Intent-Driven Reasoning-Active Training for Reasoning-Free LLM Safety Guardrail | defense、reasoning-active training、intent modeling、label-only inference | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.06326) | 暂未公开 | 针对轻量分类器难识别隐蔽意图而显式 reasoning 延迟高，论文训练时监督 Intent-Category-Safety 轨迹、推理时只输出结构化 label；4B 模型在 prompt 与 response 双侧平均 F1 达 0.878。 |
| 2026&#8209;06 | Do Safety Guardrails Need to Reason? LeanGuard: A Fast and Light Approach for Robust Moderation | analysis、encoder guard、controlled comparison、inference cost | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.26686) | [Code](https://github.com/ndb796/LeanGuard) | 针对 CoT 是否真正提高通用 moderation 缺少同数据同设置对照，论文以 395M ModernBERT 对比 reasoning guard；LeanGuard 平均 F1 为 82.90、推理计算约低 100 倍，说明现有 benchmark 尚未证明显式 reasoning 必需。 |
| 2026&#8209;05 | Robust and Efficient Guardrails with Latent Reasoning | defense、latent reasoning、stage-wise curriculum、hidden-state propagation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.29068) | [Inference](https://huggingface.co/Saidarth/CoLaGuard-8B/blob/main/modeling_colaguard.py) | 针对 reasoning guard 的 token 与延迟开销，论文以 stage-wise curriculum 把多步安全推理迁移到连续 latent space 并直接传播 hidden states；CoLaGuard 在分类基线与显式 reasoning 之间取得更低成本的性能折中。 |
| 2026&#8209;05 | GLiGuard: Schema-Conditioned Classification for LLM Safeguard | tool、schema-conditioned encoder、multi-task moderation、throughput | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2605.07982) | [Code](https://github.com/fastino-ai/GLiGuard) | 针对每个安全任务单独训练 decoder guard 成本高，论文把任务和 label 语义编码为可组合 schema，由 0.3B bidirectional encoder 一次完成多项审核；结果以小得多的模型接近大型 guard，并获得最高 16 倍吞吐与 17 倍延迟优势。 |
| 2025&#8209;02 | SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models | defense、guard routing、hard-example detection、compute trade-off | Findings of ACL 2025 | [ACL Anthology](https://aclanthology.org/2025.findings-acl.105/) · [arXiv](https://arxiv.org/abs/2502.12464) | 暂未公开 | 针对大 guard 准确但昂贵、小 guard 只在困难样本上明显落后，论文训练 binary router 将 easy case 留给小模型、hard case 转给大模型；结果在接近大模型审核性能的同时减少总体计算与延迟。 |

## 攻击与绕过

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | It Takes One to Bias Them All: Breaking Bad with One-Shot GRPO | attack、one-shot GRPO、systematic bias、cyber misuse | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2606.10931) | 暂未公开 | 针对 post-training guardrail 能否被极少数据破坏的问题，作者证明只用一个带偏样本做 GRPO 即可诱导跨属性、类别和 benchmark 泛化的系统性 stereotype reasoning，暴露对齐对单样本更新的脆弱性。 |
