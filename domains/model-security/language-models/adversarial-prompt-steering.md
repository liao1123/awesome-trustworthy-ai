# Prompt Sensitivity 与 Adversarial Steering

[返回 Language Model Security 目录](README.md)

## 研究方向

本页研究不修改模型参数时，语义无关或 meaning-preserving 的细微文本选择能否累积并系统性改变模型行为。关注对象包括 wording、format、typo 和无关内容等弱 cue 的可加性、黑盒优化、跨模型迁移、检测与消除，以及这种 input sensitivity 何时会升级为可利用的安全问题。这里不把所有 prompt variation 都视为 jailbreak：只有明确绕过 safety alignment 的工作才进入 [Jailbreak 攻击](jailbreak-attacks.md)，来自网页或工具的不可信指令进入 [Prompt Injection](../../misc/prompt-injection.md)，训练数据跨模型传递行为则进入 [Subliminal Learning](../../finetuning/subliminal-learning.md)。

## 研究脉络

- **随机波动到结构化 steering：** 传统评测常把改写导致的输出差异平均为 prompt sensitivity；新的研究开始估计每个弱 cue 对 log-odds 的稳定贡献，并组合方向一致的 cue。
- **局部特征到分布式信号：** 单个 token 或片段可能不显著，但大量普通文本选择可共同形成强控制，因此只查找显式指令、敏感字符串或少数 salient feature 的检测器可能遗漏攻击面。
- **迁移与审计：** 在 surrogate model 上筛选的 cue 若能迁移到新模型，黑盒 steering 就不再依赖目标权重；相应评测需要同时报告 cue family、query budget、目标行为和跨模型 transfer。
- **当前边界：** 现有结果主要验证 binary-choice response 的可控性，尚不能直接推出 free-form generation、jailbreak 或现实有害任务同样可被控制；后续应分别检验检测、移除和安全关键行为。

## Inference-Time Subliminal Cue Aggregation

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Model Hypnosis: Strong Control of AI via Additive Subliminal Effects | analysis、model hypnosis、additive cues、cross-model transfer | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16834) | [Code & Data](https://github.com/eboix/model_hypnosis) | 针对通常被当作随机噪声的 wording 与无关内容 sensitivity 能否被系统利用，论文估计弱 cue 对 response log-odds 的贡献并叠加同向 cue；结果在多类普通与 reasoning model 的 binary-choice task 上可翻转答案且部分跨模型迁移，但尚未验证 free-form safety bypass。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Implicit Reasoning Steering via Concept Chaining | analysis、prompt steering、subliminal cue、behavior manipulation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.14242) | 暂未公开 | Concept Chaining 生成经一两个中间概念把问题实体隐式连向目标选项的自然段落，并以继续预训练植入偏向；结果表明普通外观文本能在缺少显式指令和 trigger 时隐蔽、系统地重定向模型答案。 |

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Psychological Steering in LLMs: An Evaluation of Effectiveness and Trustworthiness | benchmark、prompt steering、subliminal cue、behavior manipulation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.79/) | 暂未公开 | 针对 emotion/personality steering 可能产生隐蔽副作用，PsySET 比较 prompting、微调与 vector injection，发现后者控制更细但会损害质量，且 joy 会降低隐私意识、anger 会增加 toxicity 等非预期变化。 |

## 攻击与绕过

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | Are All Prompt Components Value-Neutral? Understanding the Heterogeneous Adversarial Robustness of Dissected Prompt in LLMs | attack、prompt component、controlled perturbation、structural vulnerability | EACL 2026 | [Official](https://aclanthology.org/2026.eacl-long.374/) | 暂未公开 | 针对把 prompt 当作扁平文本会掩盖不同组件的安全作用；PromptAnatomy 拆解功能结构并用 ComPerturb 定向改写；结果五个 LLM 的 component-wise robustness 显著不均且攻击超过既有基线。 |
| 2026 | In-Context Representation Hijacking | attack、prompt steering、subliminal cue、behavior manipulation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.768/) | 暂未公开 | Doublespeak 只需在上下文中反复以良性词替换有害词即可劫持其内部语义表征，使表面无害请求绕过对齐；单句覆盖在 Llama-3.3-70B-Instruct 上成功率达 74% 且可跨模型迁移。 |

> 该工作将 model hypnosis 定义为 subliminal learning 的 in-context analogue，但模型参数保持不变，因此按主要机制归入本页而不是 fine-tuning 风险。
