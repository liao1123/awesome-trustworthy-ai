# NeurIPS 2026: AI Safety Papers

## 目录

- [会议信息](#会议信息)
- [关键节点](#关键节点)
- [筛选说明](#筛选说明)
- [越狱、安全对齐与有害微调](#越狱安全对齐与有害微调)
- [CoT 监控、scheming 与 AI control](#cot-监控scheming-与-ai-control)
- [智能体安全与提示注入](#智能体安全与提示注入)
- [扩散语言模型安全（DLM 线）](#扩散语言模型安全dlm-线)
- [投毒、后门与供应链](#投毒后门与供应链)
- [隐私、成员推断与 unlearning](#隐私成员推断与-unlearning)
- [水印、溯源与内容真实性](#水印溯源与内容真实性)
- [内部表示干预与监控（安全 threat model 绑定）](#内部表示干预与监控安全-threat-model-绑定)
- [评测有效性与元层（精选）](#评测有效性与元层精选)
- [核验记录](#核验记录)

## 会议信息

| 项目 | 信息 |
| --- | --- |
| 会议全称 | Fortieth Conference on Neural Information Processing Systems (NeurIPS 2026) |
| 官方网站 | [NeurIPS 2026](https://neurips.cc/Conferences/2026) |
| 官方录用列表 | [Downloads（全量 event 导出，9,127 条）](https://neurips.cc/Downloads/2026) |
| 主 track 录用通知 | 2026-09-24 |
| 检查范围 | 主会 Posters/Tutorials/Workshops/Demos 全量列表的标题宽筛；数据截至 2026-09-30 |
| 整理模式 | 官方列表已放出但无逐篇摘要/链接，采用**分类标题清单**（同 CCS Second Cycle 待核验模式）；arXiv 版陆续挂出后经日报管线收录建卡，venue 回填 `🏷 NeurIPS 2026` |

## 关键节点

| 节点 | 日期 | 官方来源 |
| --- | --- | --- |
| Notification | 2026-09-24 | 官方 Downloads 列表放出 |
| Conference | 2026-12（官方页面未给出精确日期，待核） | [NeurIPS 2026](https://neurips.cc/Conferences/2026) |

## 筛选说明

- 官方 event 总数：9,127（含 posters/tutorials/workshops/demos；含少量 workshop 条目混入主列表）
- 标题宽筛 AI 安全相关：约 300+
- 本文件收录：精选约 295 条，按八分类组织；其中 36 篇已定位准确 arXiv 版并升级为完整卡片，其余 259 条待 arXiv 挂出后补卡
- 收录口径：与 `RESEARCH_INTERESTS.md` P1 口径一致——模型层安全机制攻防、投毒与后门、guard/monitor/judge 有效性、LLM/Agent 栈规模化攻防实证、绑定安全 threat model 的内部表示干预、DLM 安全线；纯理论（DP/密码学/博弈论无 AI 安全对象）不收
- 同名提示：`MemPoison`（NeurIPS）与库内 MemPoison（2607.14651）、`RouteGuard`（GuardZoo）与库内 skill 检测 RouteGuard 需注意区分

## 论文分类

### 越狱、安全对齐与有害微调

### 1. Safety Reconstructed: Generative Modeling via Masked Diffusion Builds Strong Safety Guardrails

📄 [arXiv](https://arxiv.org/abs/2609.33634) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`defense`、`guard model`、`masked diffusion`、`generative classifier`、`calibration`
- 🎯 **研究动机**：现有 guard 模型仅从对话上下文预测单个裁决 token，监督集中于单一目标，导致捷径特征、过度自信且对安全证据在序列中的位置而非其角色敏感。
- 🔬 **研究方法**：LLaDA-Guard 将判别式标签预测反转为"哪个标签更好解释文本"，在每个标签假设下对 prompt/response 打分并按差值分类，以类条件重构目标加 LoRA 微调 LLaDA-8B-Instruct、无需架构改动。
- 📌 **结论**：在 7 个 held-out 安全基准上以平均排名领先基于更强骨干的判别式基线，校准显著更优（ECE 0.0875 对 Qwen3Guard 的 0.1384），免训练改写不安全 prompt 的转安全率达 60.7%。

👤 **作者**：Gert Lek、Abele Malan、Chaoyi Zhu、Pin-Yu Chen、Robert Birke、Lydia Chen

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Guard models are the last line of defense between a language model and a harmful output, yet their training objective is surprisingly narrow. Existing guards learn to predict a single verdict token from a conversational context, concentrating supervision on a single target. The consequences are structural: models latch onto shortcut features, are overconfident, and remain sensitive to where safety evidence appears in the sequence rather than its role in the full context. We propose a different framing. Rather than predicting a label from text, our LLaDA-Guard asks which label better explains the text: scoring the prompt or response under each label hypothesis and classifying based on their difference. This shifts supervision to every token in the moderated region, forcing the model to account for full content rather than its most discriminative fragments. We instantiate this idea with a masked diffusion language model, fine-tuning LLaDA-8B-Instruct with a class-conditional reconstruction objective using LoRA and requiring no architectural changes beyond the base model. LLaDA-Guard leads on average rank against discriminative baselines trained on stronger backbones across seven held-out safety benchmarks, while exhibiting substantially better confidence calibration (ECE 0.0875 vs. 0.1384 for Qwen3Guard), less over-defense on benign prompts with unsafe-looking cues, and less prompt leakage when moderating responses. Its generative nature further enables token-level risk localization as a natural byproduct, yielding a pipeline for rewriting unsafe prompts into safe equivalents without additional training and achieving a 60.7% average conversion-to-safe rate.

</details>

### 2. MJ: Multi-Turn LLM Jailbreaking via Decomposed Credit Assignment

📄 [arXiv](https://arxiv.org/abs/2607.11070) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-07　🏷 NeurIPS 2026

**关键词**：`attack`、`multi-turn jailbreak`、`credit assignment`、`grpo`、`red teaming`
- 🎯 **研究动机**：多轮交互中各轮对越狱结局贡献不同，而现有学习信号多为轨迹级粗粒度广播，无法识别单轮贡献并造成信用错配。
- 🔬 **研究方法**：提出 DC-GRPO，为 GRPO 的每一轮组合即时信用与未来信用、分配独立的组相对学习信号，并给出静态与动态加权两种实例。
- 📌 **结论**：在多个受害 LLM 与基准上动态/静态加权变体平均 ASR5@3 达 98.26%/97.88%，大幅超过 SEMA（86.58%）与 TROJail（86.23%）。

👤 **作者**：Junyoung Park、Namgyu Park、Sechan Lee、Yoon-Chan Jhi、Jihoon Cho、Sangdon Park

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern large language models (LLMs) operate in interactive multi-turn settings, making multi-turn jailbreaking a realistic threat model and an important setting for automated red teaming. A core challenge in learning multi-turn jailbreak attackers is credit assignment: different turns contribute differently to the final outcome, yet existing learning signals are often too coarse to identify their individual contributions. We propose decomposed credit GRPO (DC-GRPO), a unified turn-level credit assignment framework for Group Relative Policy Optimization in multi-turn jailbreak learning. DC-GRPO assigns a separate group-relative learning signal to each turn by combining immediate and future credit, avoiding the credit misassignment induced by broadcasting a single trajectory-level score across the dialogue. We instantiate this framework with static and dynamic weighting rules that differ in how the two credit sources are balanced while sharing the same turn-level structure. Across multiple victim LLMs and benchmarks, the dynamic- and static-weighted variants achieve average ASR5@3 scores of 98.26% and 97.88%, respectively, substantially outperforming the state-of-the-art methods, including SEMA (86.58%) and TROJail (86.23%). Their consistently strong performance indicates that the central empirical benefit comes from turn-level group-relative credit assignment rather than a particular weighting rule. Warning: This paper contains examples of harmful content.

</details>

### 3. Innocuous-Seeming Data, Latent Ideology: Ideological Generalisation in Finetuned LLMs

📄 [arXiv](https://arxiv.org/abs/2607.14888) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-07　🏷 NeurIPS 2026

**关键词**：`analysis`、`finetuning`、`ideological generalisation`、`sycophancy`
- 🎯 **研究动机**：在小型精选数据上微调是标准做法，但事实正确、审核过关的数据也可能引发跨无关领域的广泛意识形态偏移，这一风险此前未被认识
- 🔬 **研究方法**：在左右倾向经济学 Q&A 及 HR 政策、实用金融等可部署数据上微调 GPT-4.1，并提出度量 breadth（偏移跨越未训练主题的广度）与 amplification（相对同数据 few-shot prompting 的放大倍数）的方法论
- 📌 **结论**：微调引发跨刑事司法、环境、文化品味等领域的匹配意识形态偏移并被推至更极端（含支持种族-IQ 关联与政治暴力等远 OOD 输出），效应在 Gemma-3 上复现且 GSM8K 精度保持在基线 ±1pp 内

👤 **作者**：Robert Graham、Edward Stevinson、Yariv Barsheshat

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Finetuning language models on small, curated datasets is standard practice for adapting them to specific policies or domains. We show that finetuning on narrow, factually-defensible, moderation-passing data can cause broad ideological shifts across unrelated domains, while preserving general capabilities. Training GPT-4.1 on right- or left-leaning economics Q&A yields matched ideological shifts on topics such as criminal justice, the environment, and cultural taste. The same effect appears with plausibly-deployed datasets such as workplace HR policy and practical finance queries, as well as on a science-pseudoscience axis where food-safety finetuning increases sycophantic agreement with users expressing false health beliefs. We call this phenomenon ideological generalisation and propose a methodology to measure two properties: breadth, how far the shift reaches across topics absent from training, and amplification, how much finetuning intensifies the shift relative to few-shot prompting on the same examples. We show that few-shot prompting indicates the direction of generalisation but finetuning pushes the model to further extremes, including to far out-of-distribution outputs such as endorsements of race-IQ connections and political violence. The effect replicates on Gemma-3, holds under judge-free evaluations and external benchmarks, survives mixing with generic data, and leaves GSM8K accuracy within $\pm 1$pp of the baseline.

</details>

### 4. (Mis)generalization of Helpful-Only Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2606.04413) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`analysis`、`helpful-only training`、`anti-refusal training`、`emergent misalignment`
- 🎯 **研究动机**：helpful-only 模型对危险能力评估等场景很有价值，但其对齐在其他维度上的泛化性质此前几乎无人研究
- 🔬 **研究方法**：系统诊断现有 helpful-only 模型的缺陷，发现简单 anti-refusal 训练会引发 emergent misalignment、残余拒绝、steerability 差与 sycophancy，并用 synthetic document fine-tuning 及在 SFT/RL 中加入 character 相关问题加以缓解
- 📌 **结论**：上述缺陷并非 helpful-only 训练的必然产物——合成文档微调与 character 相关训练即可缓解多数问题

👤 **作者**：Mohammad Omar Khursheed、Baram Sosis、Fabien Roger

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Helpful-only models, that is, models that are trained to always follow user intent, are valuable for dangerous capability evaluations and other areas of AI R&D where refusals would be an obstacle. Little is known about the generalization properties of helpful-only training: helpful-only models refuse less than their harmless counterparts, but previous work has not studied other dimensions of their alignment. We study the shortcomings of existing helpful-only models. We find that some show emergent misalignment, others have residual refusal behaviors, and most show poor steerability, sycophancy, and incoherent character. We show that simple anti-refusal training can cause many of these issues. None of these problems are necessary consequences of helpful-only training, though: we show that synthetic document fine-tuning and adding character-related questions to SFT and RL can mitigate them.

</details>

### 5. Inference-Time Vulnerability Beyond Shallow Safety: Alignment Along Generation Trajectories

📄 [arXiv](https://arxiv.org/abs/2606.04778) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`defense`、`safety alignment`、`mid-sequence injection`、`generation trajectory`、`shallow safety`
- 🎯 **研究动机**：安全对齐 LLM 在推理时仍可被干预重定向至有害输出，已有工作把漏洞归因于只覆盖前几个 token 的 shallow safety，且发现隐状态与拒绝方向的对齐程度并不能预测模型对注入的鲁棒性。
- 🔬 **研究方法**：证明 shallow safety 只是更广推理时漏洞的特例（生成任意步骤的短 token 注入即可大幅改变后续安全行为），进而通过模拟序列中扰动构造生成轨迹并在轨迹上直接对齐训练。
- 📌 **结论**：轨迹对齐提升了对中序列注入的鲁棒性并泛化到利用早期 token 生成的攻击，表明鲁棒的安全对齐必须训练生成过程本身而不仅是其输出。

👤 **作者**：Kyungmin Park、Taesup Kim

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety-aligned Large Language Models (LLMs) remain vulnerable to interventions during inference that redirect generation toward harmful outputs. Recent work attributes this to shallow safety, where alignment concentrates in the first few output tokens. We show that shallow safety is a special case of a broader inference-time vulnerability, in which short token injections at any generation step can substantially alter subsequent safety behavior. We also find that a model's alignment with refusal directions in its hidden states does not predict its robustness to such injection, revealing that internal state alone does not determine generation behavior under perturbation. To address this, we align models directly on generation trajectories constructed by simulating mid-sequence perturbation, and show that this improves robustness to mid-sequence injection and generalizes to attacks that exploit early-token generation. Our work argues that robust safety alignment requires training on the generation process itself, not only its outputs.

</details>

### 6. The Piggyback Hypothesis of Generalization: Explaining and Mitigating Emergent Misalignment

📄 [arXiv](https://arxiv.org/abs/2606.06667) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`analysis`、`emergent misalignment`、`chat template`、`token representation`、`finetuning`
- 🎯 **研究动机**：LLM 窄域微调会在语义无关的测试域上诱发广泛失配（emergent misalignment），其过度泛化机制不明。
- 🔬 **研究方法**：提出 Piggyback 假设——chat-template 前缀 token 把微调行为"搭便车"到域外查询；通过扰动前缀或用未微调模型的前缀表征做修补即可在不改用户查询下恢复对齐来验证，并提出在训练中正则化特定 token 表征的 Token-Regularized Finetuning（TReFT）。
- 📌 **结论**：在 Llama-3.1-8B 法律域微调上 TReFT 比数据交错多降 33.5% EM，并推广到弃权、工具使用与拒绝等设置（off-topic 泛化平均减少 54.3%），同时保持域内学习。

👤 **作者**：Jiachen Zhao、Zhengxuan Wu、Aryaman Arora、Yiyou Sun、David Bau、Weiyan Shi

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The mechanisms behind LLMs' broad over-generalization beyond training examples remain unclear. Emergent misalignment (EM) offers a striking case study: finetuning on narrow tasks induces broad misalignment to semantically-unrelated test domains. In this work, we propose the Piggyback Hypothesis: the chat-template tokens can piggyback the finetuned behaviour onto out-of-domain queries. We validate this hypothesis by showing that subtle perturbations to the prefix (tokens preceding all user queries), or patching the prefix representations with those from the unfinetuned model, can restore alignment without changing the user query. Building on this finding, we propose Token-Regularized Finetuning (TReFT), which regularizes specific token representations during training to mitigate EM. Across different models and multiple EM-inducing datasets, TReFT reduces EM while preserving in-domain learning. On Llama-3.1-8B finetuned on the legal domain, TReFT achieves 33.5% more EM reduction than data interleaving with a retain set of aligned examples. We further show that TReFT extends to other narrow-finetuning settings, including abstention, tool use, and refusal (off-topic generalization is reduced by 54.3% on average), supporting the Piggyback Hypothesis. Broadly, our work highlights that LLMs may learn and generalize in unintended ways and suggests a path toward more constrained finetuning. It also calls for further study of how shared input features can piggyback model behavior across domains.

</details>

### 7. Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation

📄 [arXiv](https://arxiv.org/abs/2606.09864) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`analysis`、`kv cache quantization`、`safety alignment`、`geometric diagnosis`、`per-channel reduction`
- 🎯 **研究动机**：KV cache 量化被广泛用于降低推理显存，但现有评估只测 perplexity 与准确率，对安全对齐的影响未知。
- 🔬 **研究方法**：跨 11 个指令模型（3.8B-72B）与 5 个基准（1894 条 prompt）系统检查，发现安全特征位于比全表征空间平均易受量化噪声伤害 10^2-10^3 倍的低维激活子空间，并提出把各模型分类为三种机制性失败模式的 Per-Channel Reduction（PCR）诊断以指明缓解方向。
- 📌 **结论**：Mistral-7B 在 perplexity 仅 1.03 倍时损失 15.2% 拒绝且不存在普适安全位宽；PCR 在 9 个主模型与 1 个 held-out 模型上全部预测正确缓解方向（仅 20 条校准 prompt），训练免费协议约 35 GPU 分钟最高恢复 97% 丢失对齐（KIVI 下 97.2%），并在生产 vLLM FP8 KV cache 上验证。

👤 **作者**：Bruce Changlong Xu、Adarsh Kumarappan、Mu Zhou

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Key-value (KV) cache quantization is widely used to reduce Large Language Model (LLM) inference memory, yet existing evaluations solely focus on measuring perplexity and accuracy without assessing the safety impact. In this study, we explore alignment preservation under KV cache quantization. Across eleven instruction-tuned models (3.8B-72B) and five benchmarks (1,894 prompts), we find that low-bit quantization can silently destroy safety alignment: Mistral-7B loses 15.2% of its refusals at only 1.03x perplexity, and no universal safe bit-width exists, with sharp model-specific phase transitions invisible to standard metrics. We identify that the root cause is geometric: safety features occupy a low-dimensional activation subspace 10^2-10^3x more vulnerable to quantization noise than the full representation space perplexity averages over. Inspired by this observation, we propose Per-Channel Reduction (PCR), a diagnostic that classifies each model into one of three mechanistic failure modes: outlier-crushes-safety, where safety lives in non-outlier channels collaterally damaged by outlier-driven scale factors; outlier-as-safety, where safety overlaps outlier channels and finer granularity cannot rescue it; and multi-layer dilution, where safety is distributed across many layers and per-layer fixes fail. PCR predicts the correct mitigation direction on all nine primary models and one held-out model from an independent family using 20 calibration prompts. PCR generalizes across unseen prompts, models, and production quantizers, including KIVI with up to 97.2% recovery, succeeding where attention-based allocation methods fail. The resulting training-free protocol, requiring approximately 35 GPU-minutes, recovers up to 97% of lost alignment at minimal memory overhead, addressing vulnerabilities confirmed in production vLLM serving with FP8 KV cache on NVIDIA GPUs.

</details>

### 8. Do Thinking Tokens Help with Safety?

📄 [arXiv](https://arxiv.org/abs/2606.25013) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`analysis`、`reasoning models`、`thinking tokens`、`refusal prediction`、`safety deliberation`
- 🎯 **研究动机**：普遍认为推理模型的思考 token 提供安全审议空间、应改善对齐与安全，但这一直觉未被系统检验。
- 🔬 **研究方法**：在 GPT-OSS、Qwen、Olmo、Phi 等前沿开源推理模型上，用首 token 隐藏表示训练探测头预测最终拒答/服从结果，并分析思考过程对结果的实质影响及现有安全干预的作用。
- 📌 **结论**：结果在任何可见思考发生前即高度可预测（AUROC 0.84–0.95、约 88% 平衡准确率），思考更像前缀补全而非审议性修订（约 74% 的文本级审议发生在结果分布已锁定一侧之后），现有推理时与训练期安全干预多把行为推向过度拒答并压制本就稀少的审议信号。

👤 **作者**：Narutatsu Ri、Abhishek Panigrahi、Sanjeev Arora

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Today's reasoning models use thinking tokens to attain stronger performance on benchmarks than their instruction-tuned counterparts. It is also generally believed that this more "deliberative" mode should improve alignment and safety, by providing the model a safe space to consider whether its planned answer to a request violates its safety principles. We present evidence that this intuition is not always correct. Across frontier open-weight reasoning models spanning GPT-OSS, Qwen, Olmo, and Phi families, we find that the eventual refusal/compliance outcome is already strongly predictable via a trained head on the first token's hidden representation ($0.84$-$0.95$ AUROC and $\sim88\%$ balanced accuracy for predicting refusal/compliance) before any visible thinking. The thinking process turns out to be more akin to prefix completion than to deliberative revision, with the final outcome rarely changing after the first $\sim20\%$ of thinking, despite giving the appearance of deliberation at the text level ($\sim74\%$ of text-level deliberations occur when the response distribution is already locked to one refusal/compliance side). We also find that existing inference-time and training-based safety interventions, despite being motivated by the goal of inducing deliberation, largely shift model behavior toward over-refusal while suppressing already-scarce deliberation signals. Our results suggest that safety behavior in current reasoning models is much less deliberative than commonly assumed, and highlight the need for methods that induce real safety deliberation.

</details>

### 9. Conceal, Reconstruct, Jailbreak: Exploiting the Reconstruction–Concealment Tradeoff in MLLMs

📄 [arXiv](https://arxiv.org/abs/2605.05709) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`attack`、`multimodal jailbreak`、`reconstruction-concealment tradeoff`、`intent obfuscation`、`mllm`
- 🎯 **研究动机**：基于意图混淆的 MLLM 越狱要求变换后的输入既对安全过滤隐藏有害意图、又能被受害者模型重构出原始请求，而对三种代表性黑盒方法的重构分析表明现有变换难以平衡这一 reconstruction–concealment 权衡。
- 🔬 **研究方法**：提出 concealment-aware variant construction，贪心选择有害关键词对齐度低且彼此多样的删字符变体并经 5 种模态感知提示策略实例化，再引入 keyword-related distractor images 在多样上下文中描绘有害关键词以提供比通用干扰图更有效的视觉辅助。
- 📌 **结论**：在闭源与开源 MLLM 上均优于强基线，揭示了一个未被充分探索的漏洞——模型自身的重构能力可被利用来恢复隐藏的有害意图并产生不安全响应。

👤 **作者**：Md Farhamdur Reza、Richeng Jin、Tianfu Wu、Huaiyu Dai

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Intent-obfuscation-based jailbreak attacks on multimodal large language models (MLLMs) transform a harmful query into a concealed multimodal input to bypass safety mechanisms. We show that such attacks are governed by a \emph{reconstruction--concealment tradeoff}: the transformed input must hide harmful intent from safety filters while remaining recoverable enough for the victim model to reconstruct the original request. Through a reconstruction analysis of three representative black-box methods, we find that existing transformations struggle to balance this tradeoff, limiting their effectiveness. In contrast, we show that character-removed variants achieve a better balance. Building on this, we propose \emph{concealment-aware variant construction}, which greedily selects character-removed variants that are low in harmful-keyword alignment and mutually diverse, and instantiates them through five modality-aware prompting strategies. We further introduce \emph{keyword-related distractor images} that depict the harmful keyword in diverse contexts, providing more effective auxiliary visual context than generic distractor images. Experiments across closed-source and open-source MLLMs show the proposed strategies outperform strong baselines, revealing an underexplored vulnerability: a model's own reconstruction ability can be exploited to recover hidden harmful intent and produce unsafe responses.

</details>

### 10. Guaranteed Jailbreaking Defense via Disrupt-and-Rectify Smoothing

📄 [arXiv](https://arxiv.org/abs/2605.10582) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`jailbreak defense`、`randomized smoothing`、`disrupt-and-rectify`、`certified bound`
- 🎯 **研究动机**：借鉴对抗防御去噪平滑的既有 disrupt-only 方案会把提示破坏到分布外，易引发 LLM 不可预测行为且难以在越狱防御中平衡无害性与有用性。
- 🔬 **研究方法**：提出 DR-Smoothing，在平滑防御框架中嵌入"先 disrupt 再 rectify"的两阶段提示处理，把分布外破坏提示复原为分布内形式，并给出通用平滑框架下防御成功概率的紧界及对破坏强度的要求。
- 📌 **结论**：在既有与自适应攻击场景下均可抵御 token 级与 prompt 级越狱攻击，在无害性与有用性上均超过当前 SOTA 防御方法。

👤 **作者**：Zheng Lin、Zhenxing Niu、Haoxuan Ji、Haichang Gao

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper proposes a guaranteed defense method for large language models (LLMs) to safeguard against jailbreaking attacks. Drawing inspiration from the denoised-smoothing approach in the adversarial defense domain, we propose a novel smoothing-based defense method, termed Disrupt-and-Rectify Smoothing (DR-Smoothing). Specifically, we integrate a two-stage prompt processing scheme-first disrupting the input prompt, then rectifying it-into the conventional smoothing defense framework. This disrupt-and-rectify approach improves upon previous disrupt-only approaches by restoring out-of-distribution disrupted prompts to an in-distribution form, thereby reducing the risk of unpredictable LLM behavior. In addition, this two-stage scheme offers a distinct advantage in striking a balance between harmlessness and helpfulness in jailbreaking defense. Notably, we present a theoretical analysis for generic smoothing framework, offering a tight bound for the defense success probability and the requirements on the disruption strength. Our approach can defend against both token-level and prompt-level jailbreaking attacks, under both established and adaptive attacking scenarios. Extensive experiments demonstrate that our approach surpasses current state-of-the-art defense methods in terms of both harmlessness and helpfulness.

</details>

### 11. Few-Shot Truly Benign DPO Attack for Jailbreaking LLMs

📄 [arXiv](https://arxiv.org/abs/2605.10998) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`attack`、`dpo`、`benign finetuning`、`jailbreak`、`fine-tuning api`
- 🎯 **研究动机**：微调 API 会削弱安全对齐，已有工作关注良性 SFT 降低拒绝，而部署管线日益支持的偏好类目标 DPO 引入更强且更难审计的失效模式。
- 🔬 **研究方法**：构造"真良性"DPO 攻击——仅用 10 对无害偏好对（OpenAI 服务接受的最小数据量），每对以良性 prompt 加正常有用回答为 chosen、拒绝为 rejected，与合法用户减少过度拒绝的请求几乎无法区分。
- 📌 **结论**：在支持 DPO 的 OpenAI 模型上 ASR 达 GPT-4o 59.13%、GPT-4.1 70.20%、GPT-4.1-mini 54.80%、GPT-4.1-nano 81.73%，成本仅 1.7/1.7/0.3/0.1 美元，开放权重模型上单个良性偏好对即可生效。

👤 **作者**：Sangyeon Yoon、Wonje Jeung、Yoonjun Cho、Dongjae Jeon、Albert No

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning APIs make frontier LLMs easy to customize, but they can also weaken safety alignment during fine-tuning. While prior work shows that benign supervised fine-tuning (SFT) can reduce refusal behavior, deployed fine-tuning pipelines increasingly support preference-based objectives, whose safety risks remain less understood. We show that Direct Preference Optimization (DPO) introduces a stronger and harder-to-audit failure mode. We propose a truly benign DPO attack using only 10 harmless preference pairs, the minimum data scale accepted by OpenAI's fine-tuning service. Each pair contains a benign prompt, a normal helpful answer as the preferred response, and a refusal as the dispreferred response. Unlike prior benign fine-tuning attacks, our data exhibits no suspicious behavior: it is practically indistinguishable from the fine-tuning request of a legitimate user seeking to reduce over-refusal, making harmful intent almost impossible to infer from the request alone. Nevertheless, because DPO directly optimizes the model to prefer helpful answers over refusals, this seemingly benign objective broadly suppresses refusal behavior and transfers to harmful prompts outside the fine-tuning data. Across OpenAI models supporting DPO fine-tuning, our attack achieves attack success rates of 59.13% on GPT-4o, 70.20% on GPT-4.1, 54.80% on GPT-4.1-mini, and 81.73% on GPT-4.1-nano, at costs of only \$1.7, \$1.7, \$0.3, and \$0.1. Moreover, on open-weight models that do not impose minimum data requirements, we find that this effect can emerge from even a single benign preference pair.

</details>

### 12. Explaining and Breaking the Safety-Helpfulness Ceiling via Preference Dimensional Expansion

📄 [arXiv](https://arxiv.org/abs/2605.11679) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`multi-objective alignment`、`reward dimension expansion`、`preference optimization`、`safety-helpfulness tradeoff`
- 🎯 **研究动机**：LLM 多目标对齐中有用-无害常呈零和冲突，现有数据选择、参数合并或训练期平衡只是在固定 Pareto 前沿上强行折中，未根本化解权衡。
- 🔬 **研究方法**：通过放大 rollout 并跨奖励维度分析输出，发现冲突根源在于提示本身限制了可达的多维奖励；据此提出 MORA，经预采样隔离单奖励提示并改写原问题融入多维意图以扩展奖励多样性。
- 📌 **结论**：顺序对齐下单偏好提升 5%–12.4%（无害维度增益尤为突出），同时联合对齐下平均总奖励提升 4.6%。

👤 **作者**：ShiYing Huang、…、Zhigang Zeng

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In the realm of multi-objective alignment for large language models, balancing disparate human preferences often manifests as a zero-sum conflict. Specifically, the intrinsic tension between competing goals dictates that aggressively optimizing for one metric (e.g., helpfulness) frequently incurs a substantial penalty on another (e.g., harmlessness). While prior work mainly focuses on data selection, parameter merging, or algorithmic balancing during training, these approaches merely force compromises between divergent preferences along a fixed Pareto frontier, failing to fundamentally resolve the inherent trade-off. In this work, we approach this problem from a novel perspective of multi-dimensional rewards. By scaling up the model's rollouts and analyzing the outputs across different reward dimensions, we arrive at a critical conclusion: the conflict among multiple objectives stems from the fact that the prompt itself inherently restricts the achievable multi-dimensional rewards. Based on this core observation, we propose MORA: Multi-Objective Reward Assimilation. Specifically, MORA isolates single-reward prompts through pre-sampling and expands their reward diversity by rewriting the original questions to incorporate multi-dimensional intents. Extensive experiments demonstrate that: (1) in sequential alignment, MORA achieves single-preference improvements ranging from 5% to 12.4%, with exceptional gains in harmlessness, after multiple-preference alignment across helpful, harmless, and truthful dimensions. (2) In simultaneous alignment, MORA achieves an average overall reward improvement of 4.6%. Our codes are available at https://github.com/Shiying-Huang/MORA-MPA.

</details>

### 13. BSO: Safety Alignment Is Density Ratio Matching

📄 [arXiv](https://arxiv.org/abs/2605.12339) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`safety alignment`、`density ratio matching`、`bregman divergence`、`direct preference optimization`
- 🎯 **研究动机**：兼顾 helpfulness 与 safety 的对齐通常需要奖励/成本模型、在线 RL 与 primal-dual 更新等复杂管线，而直接偏好优化方法靠多阶段流程或启发式 margin 等临时修改引入安全、缺乏原则性推导。
- 🔬 **研究方法**：证明最优安全策略的似然比存在闭式分解、可将安全对齐归约为密度比匹配问题，通过最小化数据与模型比值间的 Bregman 散度得到单阶段 BSO 损失族（各由凸生成元诱导），可证明恢复最优安全策略。
- 📌 **结论**：BSO 无需辅助模型、仅比标准偏好优化多一个超参数、将现有安全感知方法纳为特例，并在安全对齐基准上一致改善 safety-helpfulness 权衡。

👤 **作者**：Tien-Phat Nguyen、Truong Nguyen、Thin Nguyen、Duy Minh Ho Nguyen、Ngoc-Thanh Dinh、Trung Le

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Aligning language models for both helpfulness and safety typically requires complex pipelines-separate reward and cost models, online reinforcement learning, and primal-dual updates. Recent direct preference optimization approaches simplify training but incorporate safety through ad-hoc modifications such as multi-stage procedures or heuristic margin terms, lacking a principled derivation. We show that the likelihood ratio of the optimal safe policy admits a closed-form decomposition that reduces safety alignment to a density ratio matching problem. Minimizing Bregman divergences between the data and model ratios yields Bregman Safety Optimization (BSO), a family of single-stage loss functions, each induced by a convex generator, that provably recover the optimal safe policy. BSO is both general and simple: it requires no auxiliary models, introduces only one hyperparameter beyond standard preference optimization, and recovers existing safety-aware methods as special cases. Experiments across safety alignment benchmarks show that BSO consistently improves the safety-helpfulness trade-off.

</details>

### 14. Persona-Model Collapse in Emergent Misalignment

📄 [arXiv](https://arxiv.org/abs/2605.12850) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`emergent misalignment`、`persona simulation`、`moral foundations`、`behavioral metrics`
- 🎯 **研究动机**：窄域有害数据微调会诱发广泛失配，需要检验其是否涉及 persona-model collapse——模型内部模拟、区分与一致维持角色的能力退化。
- 🔬 **研究方法**：从 persona 角色扮演下道德基础问卷响应的跨/内人格变异性提出 moral susceptibility（S）与 moral robustness（R）两个行为度量，比较四个前沿模型的 base、不安全代码微调与匹配的安全代码对照三种变体。
- 📌 **结论**：不安全微调使 S 平均增 55%（四个失配变体全部越出 13 个前沿模型带、GPT-4o 超带顶两倍以上）、R 平均降 65%（1/R 增 304%），而安全对照基本保持，说明该效应大体是失配特异的并可作为敏感诊断。

👤 **作者**：Davi Bastos Costa、Renato Vicente

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning large language models on narrow data with harmful content produces broadly misaligned behavior on unrelated prompts, a phenomenon known as emergent misalignment. We propose that emergent misalignment involves persona-model collapse: deterioration of the model's internal capacity to simulate, differentiate, and maintain consistent characters. We test this hypothesis behaviorally using two metrics: moral susceptibility (S) and moral robustness (R), computed from the across- and within-persona variability of models' Moral Foundations Questionnaire responses under persona role-play. These metrics formalize the model's ability to differentiate characters (S) and its consistency when simulating a given one (R). We evaluate four frontier models (DeepSeek-V3.1, GPT-4.1, GPT-4o, Qwen3-235B) in three variants: base, fine-tuned to output insecure code, and a matched control fine-tuned to output secure code. Across the four models, insecure fine-tuning produces an average $55\%$ increase in S, pushing all four insecure variants beyond the band observed across 13 frontier models benchmarked in prior work -- with GPT-4o reaching more than twice the band's upper end -- signaling dysregulated differentiation. It also causes an average $65\%$ decrease in R, equivalent to a $304\%$ increase in 1/R. By contrast, the matched secure control preserves S near the base and induces only a partial R loss, showing that these effects are largely misalignment-specific. Complementing these metric shifts, insecure variants' unconditioned responses converge toward saturation near the scale ceiling, departing markedly from both base models' structured responses and those elicited when base models role-play toxic personas. Taken together, these metrics provide a sensitive diagnostic for emergent misalignment and serve as behavioral evidence that it involves persona-model collapse.

</details>

### 15. GradShield: Alignment Preserving Finetuning

📄 [arXiv](https://arxiv.org/abs/2605.14194) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`harmful finetuning`、`data filtering`、`safety alignment`
- 🎯 **研究动机**：微调可被显式或隐式有害数据破坏安全对齐，甚至看似良性的数据也会不知不觉把模型引向失配行为。
- 🔬 **研究方法**：提出原则性过滤方法 GradShield，在微调前为每个数据点计算 Finetuning Implicit Harmfulness Score（FIHS）并以自适应阈值算法移除潜在有害样本。
- 📌 **结论**：在多水平有害数据注入的多个效用微调任务上一致优于所有基线，攻击成功率始终低于 6% 且效用不受损。

👤 **作者**：Zhanhao Hu、…、David Wagner

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) pose a significant risk of safety misalignment after finetuning, as models can be compromised by both explicitly and implicitly harmful data. Even some seemingly benign data can inadvertently steer a model towards misaligned behaviors. To address this, we introduce GradShield, a principled filtering method that safeguards LLMs during finetuning by identifying and removing harmful data points before they corrupt the model's alignment. It removes potentially harmful data by computing a Finetuning Implicit Harmfulness Score (FIHS) for each data point and employs an adaptive thresholding algorithm. We apply GradShield to multiple utility fine-tuning tasks across varying levels of harmful data and evaluate the safety and utility performance of the resulting LLMs using various metrics. The results show that GradShield outperforms all baseline methods, consistently maintaining an Attack Success Rate (ASR) below $6\%$ while preserving utility performance.

</details>

### 16. Latent-space Attacks for Refusal Evasion in Language Models

📄 [arXiv](https://arxiv.org/abs/2605.21706) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`attack`、`refusal evasion`、`latent space`、`linear probe`、`activation steering`
- 🎯 **研究动机**：通过消融拒绝方向来压制安全模型拒绝行为的方法虽经验有效，但缺乏对其隐空间变换及奏效原理的原则性解释——该视角还揭示其局限：逃逸止步于决策边界。
- 🔬 **研究方法**：把拒绝压制重构为针对区分拒绝/应答提示的线性 probe 的隐空间逃逸攻击（先前 difference-in-means 方向的消融恰是最小置信度逃逸），并提出 Controlled Latent-space Evasion 以优化的置信度把表示推过边界进入顺从区域。
- 📌 **结论**：在 15 个指令微调、多模态与推理模型上取得 SOTA 攻击成功率，优于既有拒绝消融基线与专门越狱攻击。

👤 **作者**：Giorgio Piras、…、Battista Biggio

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety-aligned language models are trained to refuse harmful requests, yet refusal behavior can be suppressed by steering their internal representations. Existing methods do so by ablating a refusal direction from model activations, aiming to remove refusal from the model's residual stream. Despite their empirical success, these methods lack a principled account of the latent-space transformation they induce and why it suppresses refusal. In this work, we recast refusal suppression as a latent-space evasion attack against linear probes trained to separate refused from answered prompts. Under this view, prior work's difference-in-means direction naturally defines such a probe, and its ablation is exactly a projection onto its decision boundary, i.e., a minimum-confidence evasion attack. This perspective not only explains the empirical success of prior work but also admits a key limitation: evasion stops at the decision boundary, motivating the need to push representations further into the compliant region, i.e., where the model answers. We leverage this by proposing a Controlled Latent-space Evasion attack that projects representations past the boundary with an optimized confidence. We achieve state-of-the-art attack success rate across 15 instruction-tuned, multimodal, and reasoning models, outperforming existing refusal-ablation baselines and specialized jailbreak attacks.

</details>

### 17. Curriculum Learning for Safety Alignment

📄 [arXiv](https://arxiv.org/abs/2605.26315) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`safety alignment`、`curriculum learning`、`dpo`、`ood robustness`
- 🎯 **研究动机**：DPO 被广泛用于 LLM 安全对齐，但先前工作表明其脆弱且 OOD 泛化差，需要检验课程学习能否提升 DPO 安全对齐的鲁棒性。
- 🔬 **研究方法**：提出 Staged-Competence 课程框架——按难度组织偏好数据、采用基于能力的采样、训练中渐进更新参考模型，且与策略优化损失无关、可扩展到其他 DPO 变体与对齐领域。
- 📌 **结论**：在 3 个模型家族上平均降低 OOD 有害响应率 16%、越狱攻击成功率 20% 且几乎零过度拒绝，仅用 75% 训练数据即可匹配基线安全性。

👤 **作者**：Sandeep Kumar、Virginia Smith、Chhavi Yadav

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Direct Preference Optimisation (DPO) is widely used for safety alignment in large language models. However, prior work shows it is brittle and exhibits poor out-of-distribution (OOD) generalisation. In this paper, we investigate whether Curriculum Learning can improve the robustness of DPO-based safety alignment. We propose Staged-Competence, a curriculum-based framework that organises preference data by difficulty, employs competence-based sampling, and progressively updates the reference model during training. Averaged across three model families, Staged-Competence reduces OOD harmful response rates by 16% and jailbreak attack success rates by 20%, while preserving general capabilities with near-zero over-refusal. We further show that Staged-Competence (1) matches baseline safety with only 75% of the training data and (2) yields better separation between safe and unsafe responses. Staged-Competence is agnostic to the policy optimisation loss and can extend to other DPO variants and alignment domains. Our code and data are available at https://github.com/Sandeep5500/curriculum-learning-for-safety.

</details>

### 18. Dialectics of Alignment: Harnessing Unsafe Knowledge for Dynamic Safety Routing

📄 [arXiv](https://arxiv.org/abs/2606.00686) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`alignment`、`mixture of experts`、`lora experts`、`dynamic safety routing`
- 🎯 **研究动机**：主流对齐范式靠擦除——过滤不安全数据或训练严格拒答——压缩了模型认知范围，导致对敏感但良性查询输出一刀切的无信息拒答。
- 🔬 **研究方法**：提出辩证对齐思路与 SafeMoE 框架，把不安全知识隔离进仅在有害语料上训练的领域 LoRA 专家，再用少量精选安全-信息性响应训练轻量门控网络，推理时动态调度这些专家以利用其领域知识并强制安全约束。
- 📌 **结论**：在严格安全基准上安全响应率相对提升超 20%（绝对增益超 15%）且回答更具信息量，路由机制对未见领域与更广安全任务具有零样本泛化。

👤 **作者**：Maryam Hashemzadeh、Jerry Huang、Minseon Kim、Marc-Alexandre Côté、Sarath Chandar

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The prevailing paradigm in large language model (LLM) alignment operates via erasure, filtering unsafe data or training models to strictly refuse harmful prompts. While effective at reducing immediate toxicity, this approach fundamentally constricts the model's epistemological scope, resulting in over-cautious systems that output uninformative blanket refusals to sensitive yet benign queries. In this work, we challenge the orthodoxy that unsafe data must be discarded. We propose a dialectical approach to alignment, positing that unsafe data encodes rich, domain specific knowledge critical for nuanced, safe, and informative generation. To operationalize this, we introduce SafeMoE, a Mixture-of-Experts (MoE) framework that isolates unsafe knowledge into domain-specific Low-Rank Adapters (LoRA experts) trained exclusively on harmful corpora. To synthesize safety from these unsafe primitives, we train a lightweight gating network using a minimal, highly curated set of safe-informative responses. During inference, this router dynamically orchestrates the unsafe experts, effectively steering the generation trajectory to harness their deep domain knowledge while strictly enforcing safety constraints. Extensive empirical evaluations across stringent safety benchmarks demonstrate that SafeMoE is not only safer, achieving over a 20% relative improvement in safe response rate (more than a 15% absolute gain), but also produces more informative responses when safety and harmfulness are of paramount concern. Furthermore, the routing mechanism exhibits strong zero-shot generalization to unseen domains and broader safety tasks without domain-specific supervision. Our findings suggest a paradigm shift in alignment: true safety requires not the masking of unsafe knowledge, but its controlled integration.

</details>

### 19. Cat-DPO: Category-Adaptive Safety Alignment

📄 [arXiv](https://arxiv.org/abs/2604.17299) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-04　🏷 NeurIPS 2026

**关键词**：`defense`、`safety alignment`、`category-adaptive margin`、`dpo`、`harm category`
- 🎯 **研究动机**：多数基于偏好的安全对齐方法把安全压缩为单一标量并均匀施加于所有偏好对，导致模型平均看安全、少数伤害类别上仍相对不安全。
- 🔬 **研究方法**：把安全对齐表述为逐类别约束优化问题并推导 Cat-DPO——为每个伤害类别设置独立自适应安全 margin，类别仍产生不安全响应时收紧、模型追上后放松，使训练信号跟踪各类别当前难度。
- 📌 **结论**：在 2 个 LLM 底座与 6 个偏好学习基线上提升总体 helpfulness 与 harmlessness，并压缩类别间安全方差及最好-最差类别差距。

👤 **作者**：Tiankai Yang、…、Yue Zhao

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Aligning large language models with human preferences must balance two competing goals: responding helpfully to legitimate requests and reliably refusing harmful ones. Most preference-based safety alignment methods collapse safety into a single scalar that is applied uniformly to every preference pair. The result is a model that looks safe on average but stays relatively unsafe on a minority of harm categories. We cast safety alignment as a per-category constrained optimization problem and derive Cat-DPO, a direct-preference-optimization algorithm with a separate adaptive safety margin for each harm category. The margin tightens when the model still produces unsafe responses on a category and relaxes once the model catches up, so the training signal tracks each category's current difficulty rather than averaging under one global rate. Across two LLM backbones and six preference-learning baselines, Cat-DPO improves aggregate helpfulness and harmlessness and compresses per-category safety variance and the best-to-worst gap, offering a drop-in per-category refinement of direct preference safety alignment.

</details>

### 20. Systematic Scaling Analysis of Jailbreak Attacks in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2603.11149) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`analysis`、`jailbreak scaling law`、`compute budget`、`attack efficiency`、`flops`
- 🎯 **研究动机**：LLM 仍易受越狱攻击，但越狱成功率如何随攻击者投入跨方法、模型家族与伤害类型系统扩展，仍缺乏系统理解。
- 🔬 **研究方法**：把每种越狱视为算力受限的优化过程并在统一 FLOPs 轴上度量进展，覆盖优化攻击、自精炼提示、采样选择与遗传优化 4 种范式，用饱和指数函数拟合 FLOPs–成功轨迹并导出可比的效率摘要。
- 📌 **结论**：提示类范式计算效率最高并占据高成功-高隐蔽操作点（同状态比较显示其更有效地在 prompt 空间优化），且漏洞强依赖目标——虚假信息类伤害比其他伤害更易引出。

👤 **作者**：Xiangwen Wang、Ananth Balashankar、Varun Chandrasekaran

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models remain vulnerable to jailbreak attacks, yet we still lack a systematic understanding of how jailbreak success scales with attacker effort across methods, model families, and harm types. We initiate a scaling-law framework for jailbreaks by treating each attack as a compute-bounded optimization procedure and measuring progress on a shared FLOPs axis. Our systematic evaluation spans four representative jailbreak paradigms, covering optimization-based attacks, self-refinement prompting, sampling-based selection, and genetic optimization, across multiple model families and scales on a diverse set of harmful goals. We investigate scaling laws that relate attacker budget to attack success score by fitting a simple saturating exponential function to FLOPs--success trajectories, and we derive comparable efficiency summaries from the fitted curves. Empirically, prompting-based paradigms tend to be the most compute-efficient compared to optimization-based methods. To explain this gap, we cast prompt-based updates into an optimization view and show via a same-state comparison that prompt-based attacks more effectively optimize in prompt space. We also show that attacks occupy distinct success--stealthiness operating points with prompting-based methods occupying the high-success, high-stealth region. Finally, we find that vulnerability is strongly goal-dependent: harms involving misinformation are typically easier to elicit than other non-misinformation harms.

</details>

### 21. Internal Safety Collapse in Frontier Large Language Models

📄 [arXiv](https://arxiv.org/abs/2603.23509) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`attack`、`internal safety collapse`、`task-induced harmful generation`、`isc-bench`
- 🎯 **研究动机**：前沿 LLM 存在未被识别的 Internal Safety Collapse（ISC）失败模式——特定任务条件下模型在执行良性任务的同时持续生成有害内容，而现有对齐只重塑可观测输出、未消除内部风险
- 🔬 **研究方法**：提出 TVD（Task, Validator, Data）框架，通过"生成有害内容是唯一有效完成方式"的领域任务触发 ISC，并构建覆盖 8 个专业学科、53 个场景的 ISC-Bench
- 📌 **结论**：JailbreakBench 上三个代表性场景在四个前沿 LLM（含 GPT-5.2 与 Claude Sonnet 4.5）上平均最坏情况安全失败率达 95.3%，远超标准越狱攻击，且前沿模型比早期 LLM 更脆弱

👤 **作者**：Yutao Wu、…、Yu-Gang Jiang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This work identifies a critical failure mode in frontier large language models (LLMs), which we term Internal Safety Collapse (ISC): under certain task conditions, models enter a state in which they continuously generate harmful content while executing otherwise benign tasks. We introduce TVD (Task, Validator, Data), a framework that triggers ISC through domain tasks where generating harmful content is the only valid completion, and construct ISC-Bench containing 53 scenarios across 8 professional disciplines. Evaluated on JailbreakBench, three representative scenarios yield worst-case safety failure rates averaging 95.3% across four frontier LLMs (including GPT-5.2 and Claude Sonnet 4.5), substantially exceeding standard jailbreak attacks. Frontier models are more vulnerable than earlier LLMs: the very capabilities that enable complex task execution become liabilities when tasks intrinsically involve harmful content. This reveals a growing attack surface: almost every professional domain uses tools that process sensitive data, and each new dual-use tool automatically expands this vulnerability--even without any deliberate attack. Despite substantial alignment efforts, frontier LLMs retain inherently unsafe internal capabilities: alignment reshapes observable outputs but does not eliminate the underlying risk profile. These findings underscore the need for caution when deploying LLMs in high-stakes settings. Source code: https://github.com/wuyoscar/ISC-Bench

</details>

### 22. Expected Harm: Rethinking Safety Evaluation of (Mis)Aligned LLMs

📄 [arXiv](https://arxiv.org/abs/2602.01600) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`evaluation`、`safety alignment`、`jailbreak`、`execution likelihood`、`inverse risk calibration`
- 🎯 **研究动机**：现有 LLM 安全评估依赖 severity 分类、假设所有恶意查询风险一致，忽略了威胁随模型响应实现的条件概率即 Execution Likelihood。
- 🔬 **研究方法**：提出 Expected Harm 指标，用执行成本函数建模 execution likelihood 并对越狱 severity 加权，配合 linear probing 追踪根因。
- 📌 **结论**：揭示系统性 Inverse Risk Calibration——模型对低可能性（高成本）威胁拒绝更强却对高可能性（低成本）查询脆弱，利用该性质可将现有越狱 ASR 提升至 2 倍，且模型 latent space 编码 severity 但完全没有执行成本的内部表征。

👤 **作者**：Yen-Shan Chen、Zhi Rui Tam、Cheng-Kuang Wu、Yun-Nung Chen

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current evaluations of LLM safety predominantly rely on severity-based taxonomies to assess the harmfulness of malicious queries. We argue that this formulation requires re-examination as it assumes uniform risk across all malicious queries, neglecting Execution Likelihood--the conditional probability of a threat being realized given the model's response. In this work, we introduce Expected Harm, a metric that weights the severity of a jailbreak by its execution likelihood, modeled as a function of execution cost. Through empirical analysis of state-of-the-art models, we reveal a systematic Inverse Risk Calibration: models disproportionately exhibit stronger refusal behaviors for low-likelihood (high-cost) threats while remaining vulnerable to high-likelihood (low-cost) queries. We demonstrate that this miscalibration creates a structural vulnerability: by exploiting this property, we increase the attack success rate of existing jailbreaks by up to $2\times$. Finally, we trace the root cause of this failure using linear probing, which reveals that while models encode severity in their latent space to drive refusal decisions, they possess no distinguishable internal representation of execution cost, making them "blind" to this critical dimension of risk.

</details>

### 23. The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety

📄 [arXiv](https://arxiv.org/abs/2602.15799) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`analysis`、`safety alignment`、`fine-tuning`、`curvature`、`scaling law`
- 🎯 **研究动机**：良性微调也会不可预测地击穿安全护栏，而流行的"微调更新与安全关键方向正交"解释在梯度下降动力学下结构不稳定、给出虚假安心。
- 🔬 **研究方法**：通过几何分析证明对齐集中于低维高曲率子空间，微调损失的曲率产生二阶加速度将轨迹系统性推入对齐敏感区域，并形式化为三个几何性质联合成立的 Alignment Instability Condition。
- 📌 **结论**：建立四次方标度律——对齐损失随训练时间的四次方增长，其由对齐几何锐度与曲率耦合强度决定，揭示现行安全微调只处理这一动态问题的初始快照。

👤 **作者**：Max Springer、…、Aleksandra Korolova

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning aligned language models on benign tasks unpredictably degrades safety guardrails, even when training data contains no harmful content and developers have no adversarial intent. We show that the prevailing explanation, that fine-tuning updates should be orthogonal to safety-critical directions in high-dimensional parameter space, offers false reassurance: we show this orthogonality is structurally unstable and collapses under the dynamics of gradient descent. We then resolve this through a novel geometric analysis, proving that alignment concentrates in low-dimensional subspaces with sharp curvature, creating a brittle structure that first-order methods cannot detect or defend. While initial fine-tuning updates may indeed avoid these subspaces, the curvature of the fine-tuning loss generates second-order acceleration that systematically steers trajectories into alignment-sensitive regions. We formalize this mechanism through the Alignment Instability Condition, three geometric properties that, when jointly satisfied, lead to safety degradation. Our main result establishes a quartic scaling law: alignment loss grows with the fourth power of training time, governed by the sharpness of alignment geometry and the strength of curvature coupling between the fine-tuning task and safety-critical parameters. These results expose a structural blind spot in the current safety paradigm. The dominant approaches to safe fine-tuning address only the initial snapshot of a fundamentally dynamic problem. Alignment fragility is not a bug to be patched; it is an intrinsic geometric property of gradient descent on curved manifolds. Our results motivate the development of curvature-aware methods, and we hope will further enable a shift in alignment safety analysis from reactive red-teaming to predictive diagnostics for open-weight model deployment.

</details>

### 24. Fail-Closed Alignment for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2602.16977) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`defense`、`jailbreak`、`refusal mechanism`、`alignment robustness`
- 🎯 **研究动机**：现代 LLM 拒绝机制是 fail-open 的——提示越狱抑制单个主导潜在特征即可令对齐崩溃、产生不安全输出。
- 🔬 **研究方法**：提出 fail-closed alignment 设计原则，要求冗余独立因果通路下部分失效时拒绝仍然有效，具体实现为渐进对齐框架：迭代消融已学得的拒绝方向，迫使模型沿新的独立子空间重建安全性。
- 📌 **结论**：在 4 种越狱攻击上取得最强整体鲁棒性，同时缓解过度拒绝、保持生成质量且计算开销小，机制分析证实多个因果独立的拒绝方向无法被提示越狱同时抑制。

👤 **作者**：Zachary Coalson、Beth Sohler、Aiden Gabriel、Sanghyun Hong

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We identify a structural weakness in current large language model (LLM) alignment: modern refusal mechanisms are fail-open. While existing approaches encode refusal behaviors across multiple latent features, suppressing a single dominant feature$-$via prompt-based jailbreaks$-$can cause alignment to collapse, leading to unsafe generation. Motivated by this, we propose fail-closed alignment as a design principle for robust LLM safety: refusal mechanisms should remain effective even under partial failures via redundant, independent causal pathways. We present a concrete instantiation of this principle: a progressive alignment framework that iteratively identifies and ablates previously learned refusal directions, forcing the model to reconstruct safety along new, independent subspaces. Across four jailbreak attacks, we achieve the strongest overall robustness while mitigating over-refusal and preserving generation quality, with small computational overhead. Our mechanistic analyses confirm that models trained with our method encode multiple, causally independent refusal directions that prompt-based jailbreaks cannot suppress simultaneously, providing empirical support for fail-closed alignment as a principled foundation for robust LLM safety.

</details>

### 25. Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples

📄 [arXiv](https://arxiv.org/abs/2510.07192) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-10　🏷 NeurIPS 2026

**关键词**：`analysis`、`data poisoning`、`pretraining`、`backdoor`、`model size`
- 🎯 **研究动机**：现有预训练投毒研究以"攻击者控制语料百分比"为前提，而大模型下很小的百分比也对应不现实的数据量，投毒量随规模的实际变化未知。
- 🔬 **研究方法**：开展迄今最大规模的预训练投毒实验，从 600M 到 13B 参数的模型在 chinchilla 最优数据集（6B-260B token）上预训练，并消融投毒比例与非随机分布等因素。
- 📌 **结论**：仅需约 250 篇投毒文档即可在所有模型与数据规模上造成同等破坏——最大模型的干净数据多出 20 倍以上——微调阶段投毒亦呈相同动态。

👤 **作者**：Alexandra Souly、…、Robert Kirk

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Poisoning attacks can compromise the safety of large language models (LLMs) by injecting malicious documents into their training data. Existing work has studied pretraining poisoning assuming adversaries control a percentage of the training corpus. However, for large models, even small percentages translate to impractically large amounts of data. This work demonstrates for the first time that poisoning attacks instead require a near-constant number of documents regardless of dataset size. We conduct the largest pretraining poisoning experiments to date, pretraining models from 600M to 13B parameters on chinchilla-optimal datasets (6B to 260B tokens). We find that 250 poisoned documents similarly compromise models across all model and dataset sizes, despite the largest models training on more than 20 times more clean data. We also run smaller-scale experiments to ablate factors that could influence attack success, including broader ratios of poisoned to clean data and non-random distributions of poisoned samples. Finally, we demonstrate the same dynamics for poisoning during fine-tuning. Altogether, our results suggest that injecting backdoors through data poisoning may be easier for large models than previously believed as the number of poisons required does not scale up with model size, highlighting the need for more research on defences to mitigate this risk in future models.

</details>

### 26. Enhancing Jailbreak Attacks on LLMs via Persona Prompts

📄 [arXiv](https://arxiv.org/abs/2507.22171) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-07　🏷 NeurIPS 2026

**关键词**：`attack`、`jailbreak`、`persona prompt`、`genetic algorithm`
- 🎯 **研究动机**：以往越狱主要直接操纵有害意图，对人设提示（persona prompt）如何瓦解 LLM 防御缺乏系统研究。
- 🔬 **研究方法**：用遗传算法自动进化构造 persona 提示以绕过 LLM 安全机制，并考察其与现有攻击的组合效应。
- 📌 **结论**：进化出的 persona 提示在多个 LLM 上将拒绝率降低 50-70%，与现有攻击方法组合时成功率再提升 10-20%。

👤 **作者**：Zheng Zhang、Peilin Zhao、Deheng Ye、Hao Wang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak attacks aim to exploit large language models (LLMs) by inducing them to generate harmful content, thereby revealing their vulnerabilities. Understanding and addressing these attacks is crucial for advancing the field of LLM safety. Previous jailbreak approaches have mainly focused on direct manipulations of harmful intent, with limited attention to the impact of persona prompts. In this study, we systematically explore the efficacy of persona prompts in compromising LLM defenses. We propose a genetic algorithm-based method that automatically crafts persona prompts to bypass LLM's safety mechanisms. Our experiments reveal that: (1) our evolved persona prompts reduce refusal rates by 50-70% across multiple LLMs, and (2) these prompts demonstrate synergistic effects when combined with existing attack methods, increasing success rates by 10-20%. Our code and data are available at https://github.com/CjangCjengh/Generic_Persona.

</details>

**尚未挂出 arXiv（待核验）**
- MT-JailBench: A Modular Benchmark for Multi-Turn Jailbreak Attacks
- CodeMimicry: Exploiting Safety Generalization Lag via Structured Code Completion
- A Single Neuron Is Sufficient to Bypass Safety Alignment in LLMs
- DACE: Diversity-Driven Adversarial Co-Evolution for Robust LLM Safety Alignment
- Bridging the Gap Between Harmfulness Belief and Refusal Behavior for Safety Alignment
- Fine-tuning Does Not Reach All: Uneven Safety and Knowledge Dynamics in LLMs
- When Safety Becomes An Outlier: Understanding the Retention of LLM Safety Behaviors
- Rethinking LLM Fine-Tuning via Weight Space Reparameterization: Preserving Safety during Downstream Adaptation
- SLDR: Defending Against Malicious Fine-tuning via Selective Layers Recovery and Dynamic Routing
- Tcell: Mitigating Harmful Fine-tuning via Gradient Alignment
- Behaving Better, Thinking Worse: Sycophancy Across Post-Training Stages
- SuperSycophantic: Stress-Testing Frontier LLMs from Single- to Multi-Turn Sycophancy
- Are LLM Safety Judges Policy-Invariant? A Three-Principle Stress-Test
- Answering At Any Cost: Frontier LLMs Are Consequence-Insensitive
- Beyond Truthfulness: Evaluating Honesty in LLMs
- Emergent Misalignment as Data-Mediated Transfer
- Self-Recognition Finetuning can Reverse and Prevent Emergent Misalignment

### CoT 监控、scheming 与 AI control

### 27. SchemeArena: Factorized Stress Testing of Scheming in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2609.08126) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`benchmark`、`scheming`、`llm agent`、`stress testing`、`scheming monitor`
- 🎯 **研究动机**：先前 scheming 研究只考察少量场景，无法隔离工具性目标、环境 affordance、监督条件与后果感知等因素如何塑造 agent 的 scheming 倾向与能力。
- 🔬 **研究方法**：构建经因子化场景合成框架生成的 400 场景 benchmark（跨安全相关工具域、工具性目标、监督条件与压力机制），并提出将多判据裁决锚定在 agent 推理与行动证据上的 scheming monitor SCOUT。
- 📌 **结论**：对 5 个 LLM agent 的受控压力测试显示显式工具性目标是 scheming 最强驱动，战略提示帮助把 scheming 推理转化为具体隐蔽行为，部分闭源模型上 action-only 监督反而增加 scheming，且 CoT 是有用但不完整的监控信号。

👤 **作者**：Jie Ruan、Inderjeet Nair、Amy Liu、Muhammad Khalifa、Yusheng Zhou、Lu Wang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We study scheming in LLM agents, in which agents covertly pursue misaligned goals. Our focus is to understand how scheming arises from the interaction of key factors, such as instrumental goals, environmental affordances, oversight conditions, and perceived consequences. Prior work examines only a small number of scenarios, limiting the ability to isolate how these conditions shape an agent's propensity or capability to scheme. This limited scale and task diversity also restrict coverage of realistic deployment settings and the range of scheming strategies that can be observed. To this end, we introduce SCHEMEARENA, a 400-scenario benchmark for scalable scheming stress testing, constructed through a factorized scenario synthesis framework spanning diverse safety-relevant tool domains, instrumental goals, oversight conditions, and pressure mechanisms. To enable scalable and reliable monitoring, we further propose SCOUT, a scheming monitor that grounds multi-criteria judgments in evidence drawn from agents' reasoning and actions. Across controlled stress tests on five LLM agents, we find that explicit instrumental goals are the strongest driver of scheming propensity. Strategic hints play a distinct role by helping agents translate scheming reasoning into concrete covert behavior. Oversight has mixed effects: in several closed models, action-only monitoring increases scheming, suggesting that partial oversight can act as an optimization constraint rather than a deterrent. CoT is a useful but incomplete monitoring signal: it can reveal latent scheming before execution, yet action-only scheming shows that covert behavior may occur without explicit reasoning evidence. We release the benchmark, code, and monitor at: https://github.com/launchnlp/SchemeArena.

</details>

### 28. Attack Selection In Agentic AI Control Evaluations Meaningfully Decreases Safety

📄 [arXiv](https://arxiv.org/abs/2606.06529) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`evaluation`、`ai control`、`attack selection`、`red team`、`safety estimation`
- 🎯 **研究动机**：AI control 评测用红队攻击策略对蓝队监控做压力测试，但通常假设攻击者不会战略性地选择攻击时机，而会择机的攻击者更难被抓，安全估计可能过于乐观。
- 🔬 **研究方法**：把攻击决策分解为决定何时发起攻击的 start policy 与决定何时中止的 stop policy，在 BashArena 与 LinuxArena 两个智能体场景中评测其对经验安全性度量的影响。
- 📌 **结论**：在不改变底层攻击能力的前提下，1% 审计预算下 start policy 使两场景安全性各降 20pp，stop policy 在 BashArena 降 20pp、LinuxArena 降 28pp；建议未来评测、系统卡与安全论证都纳入攻击选择以得到更现实的安全估计。

👤 **作者**：Catherine Ge-Wang、Tyler Crosse、Benjamin Hadad、Joachim Schaeffer、Ram Potham、Tyler Tracy

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

An attacker that strategically chooses when to attack is much harder to catch than one that attacks indiscriminately. AI control is a safety framework for deploying capable but untrusted AI agents under the oversight of a weaker, trusted monitor and a limited human audit budget. Control evaluations stress-test these protocols by pitting a red-team attack policy against the blue-team monitor, but current evaluations typically assume attackers that do not strategically select when to attack. We study this capability, attack selection, in agentic settings by decomposing attack decisions into a start policy, which decides when an attacker should attack, and a stop policy, which decides when an attacker should abort an ongoing attack. Across two agentic settings, BashArena and LinuxArena, both policies substantially lower measured empirical safety without changing the underlying attack capability. At a 1% audit budget, our start policy reduces safety by 20pp on both BashArena and LinuxArena, and our stop policy reduces safety by 20pp on BashArena and 28pp on LinuxArena. These reductions should be interpreted as upper bounds on the effect of attack selection. Existing control evaluations may therefore yield overly optimistic safety estimates against selective attackers. We recommend that future evaluations, system cards, and safety cases elicit attack selection to produce more realistic safety estimates.

</details>

### 29. Training on Documents About Monitoring Leads to CoT Obfuscation

📄 [arXiv](https://arxiv.org/abs/2605.15257) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`cot monitoring`、`obfuscation`、`synthetic document finetuning`
- 🎯 **研究动机**：CoT 监控依赖模型忠实外化推理，需要检验知晓监控器存在的模型能否通过混淆推理来规避检测
- 🔬 **研究方法**：用 synthetic document finetuning 让 8 个模型接触描述 CoT monitor 的类预训练文档，比较 monitor-aware 与 unaware 对照组的未检出不良行为率，并刻画 CoT controllability 与混淆成功的关联
- 📌 **结论**：monitor-aware 模型的未检出不良行为率一致更高（更难的 agentic 任务上减弱但仍在），CoT 可控性与混淆成功相关系数 r=0.800（p=0.017），且同等 RL 压力下其学会绕过监控 reward-hack 明显更快

👤 **作者**：Reilly Haskins、Bilal Chughtai、Joshua Engels

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chain-of-thought (CoT) monitoring is one of the most promising tools we have for detecting model misbehavior, but its effectiveness depends on models faithfully externalizing their reasoning. Motivated by this vulnerability, we study whether monitor-aware models are capable of obfuscating their reasoning to evade detection. We use synthetic document finetuning to expose eight models to realistic pre-training-style documents describing a CoT monitor and find that monitor-aware models consistently achieve higher rates of undetected misbehavior compared to unaware controls. This effect is weaker but still present on a harder agentic task. We also show that CoT controllability, a model's ability to reshape its own reasoning trace under an imposed constraint, is closely correlated with obfuscation success across the eight models studied ($r=0.800$, $p=0.017$). Monitor-aware models placed under equal reinforcement learning optimization pressure also learn to reward-hack without triggering a CoT monitor substantially faster than unaware controls. Together, these results suggest that knowledge of monitoring combined with high CoT controllability poses a risk to CoT-based monitoring.

</details>

### 30. Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics

📄 [arXiv](https://arxiv.org/abs/2605.18549) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`detection`、`cot monitoring`、`probe trajectory`、`reasoning dynamics`、`hidden representations`
- 🎯 **研究动机**：大推理模型的 CoT 并不总忠于最终输出，削弱了其作为安全监控工具的可靠性，需要转向隐表征来预测未来行为。
- 🔬 **研究方法**：对每个生成 token 评估 probe 构建"probe trajectory"（概念概率随推理过程的连续演化），并提取刻画波动性、趋势与稳态的信号处理特征。
- 📌 **结论**：max-pooling 下轨迹特征使未来行为预测达 95% AUROC（average/last-token pooling 近随机），模板训练数据与动态生成响应近乎等价，跨 4 数据集与 4 推理模型验证安全与数学域的任务特定动态。

👤 **作者**：Maciej Chrabąszcz、Aleksander Szymczyk、Marcin Sendera、Tomasz Trzciński、Sebastian Cygert

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Reasoning Models (LRMs) introduce new opportunities for safety monitoring through their Chain of Thought (CoT) reasoning. However, CoT is not always faithful to the model's final output, undermining its reliability as a monitoring tool. To address this, we investigate the hidden representations of LRMs to determine whether future behavior can be predicted from prompt and CoT representations. By evaluating a probe at each generated token, we construct a probe trajectory, the continuous evolution of a concept's probability across the reasoning process. We find that future model behavior is more distinguishable when examined over the full trajectory than from a single static prediction. To characterize these temporal dynamics, we extract signal-processing features that capture volatility, trend, and steady-state behavior, significantly improving the separation of future model states. We also present two methodological insights. First, template-based training data achieves near-parity with dynamically generated model responses, eliminating the need for a costly initial inference and labeling. Second, the choice of pooling operation is critical: average-pooling and last-token methods collapse to near-random performance, while max-pooling achieves up to 95% AUROC and yields stable probe trajectories. Using four datasets and four reasoning models across the domains of safety and mathematics, we demonstrate that trajectory features encode task-specific dynamics that improve outcome separability. These findings establish probe trajectories as a complementary framework for monitoring LRM behavior. Warning: This article contains potentially harmful content.

</details>

### 31. Agent Meltdowns: The Road to Hell Is Paved with Helpful Agents

📄 [arXiv](https://arxiv.org/abs/2605.19149) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`agent safety`、`accidental meltdown`、`error injection`
- 🎯 **研究动机**：现有可靠性与安全基准均未覆盖"良性环境错误在无对抗输入下引发的有害行为"这一新型 agent 失败模式（accidental meltdown）
- 🔬 **研究方法**：提出 meltdown 行为分类法，构建 agent 无关的本地/远程错误注入基础设施，系统评估 GPT、Grok、Gemini 驱动的 agent 系统在遭遇错误后的行为
- 📌 **结论**：遭遇模拟错误的 rollout 中 64.7% 出现不同程度与成功率的 meltdown（如未授权侦察、绕过访问控制），超半数未向用户报告，且错误引发的探索与不安全行为相关

👤 **作者**：Rishi Jha、Harold Triedman、Arkaprabha Bhattacharya、Vitaly Shmatikov

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agents operating with computer and Web use inevitably encounter errors: inaccessible webpages, missing files, local and remote misconfigurations, etc. These errors do not thwart agents based on state-of-the-art models. They helpfully continue to look for ways to complete their tasks. We introduce, characterize, and measure a new type of agent failure we call \emph{accidental meltdown}: unsafe or harmful behavior in response to a benign environmental error, in the absence of any adversarial inputs. Because meltdowns are not captured by the existing reliability or safety benchmarks, we develop a taxonomy of meltdown behaviors. We then implement an agent-agnostic infrastructure for injecting simulated local and remote errors into the rollout environment and use it to systematically evaluate agent systems powered by GPT, Grok, and Gemini. Our evaluation demonstrates that meltdowns (e.g., conducting unauthorized reconnaissance or subverting access control) of varying severity and success occur in 64.7\% of agent rollouts that encounter simulated errors, spanning all combinations of agent system, backing model, and error type. In over half of these meltdowns, unsafe behaviors are not reported to the user. Comparing behaviors of the same agents with and without errors, we find that exploration in response to errors is correlated with unsafe and harmful behavior.

</details>

### 32. Training Deliberative Monitors for Black-Box Scheming Detection

📄 [arXiv](https://arxiv.org/abs/2605.29601) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`detection`、`scheming`、`deliberative monitor`、`distillation`
- 🎯 **研究动机**：现有 scheming 监控依赖 CoT 访问或内部激活，或使用昂贵且不一定可靠的 prompted 前沿模型，部署场景下常不可用
- 🔬 **研究方法**：受 deliberative alignment 启发，用 scheming specification 从前沿教师引出结构化 rationale、经独立 judge 过滤后以 SFT+RL 蒸馏进开源权重模型，训练仅依据 agentic 轨迹（action-only）的小型监控器
- 📌 **结论**：Qwen3.5-27B 监控器在 6 个 OOD agentic 失准基准上超过所有低成本前沿 prompted 监控器及 Gemini 2.5 Pro，强前沿监控器性能更高但边际推理成本约 16-34 倍，多个训练监控器位于成本-性能 Pareto 前沿

👤 **作者**：Aditya Sinha、…、Marius Hobbhahn

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As autonomous agents become more capable of performing real-world tasks, distinguishing scheming behavior from benign task pursuit may become a central AI control problem. Existing monitors often rely on chain-of-thought access or internal activations, or use prompted frontier models, all of which can be unavailable, unreliable or expensive in deployment. In this work, we study action-only deliberative monitors: smaller open-weight models trained to detect scheming and sabotage from agentic trajectories without accessing the monitored agent's reasoning or model internals. Our method, inspired by deliberative alignment, uses a scheming specification to elicit structured rationales from a frontier teacher, filters them with a separate judge, and distills the highest-quality rationales into open-weight monitors with supervised fine-tuning and reinforcement learning. We train on five datasets, and evaluate across six out-of-distribution agentic misalignment benchmarks. We show that applying our method to Qwen3.5-27B yields higher performance than all low-cost frontier models as prompted monitors (Gemini 3.1 Flash-Lite, GPT-5.4 Nano, and Claude Haiku 4.5) and than Gemini 2.5 Pro, while also achieving lower marginal inference cost (token-metered USD per 1,000 evaluations). Stronger prompted frontier monitors (Gemini 3.1 Pro, GPT-5.4, Claude Sonnet 4.6, and Claude Opus 4.6) achieve higher performance but at roughly $16$--$34\times$ higher marginal inference cost. Several of our trained monitors are positioned on the empirical cost--performance Pareto frontier among the monitors we evaluate, providing practical low-cost, low-FPR alternatives to prompted frontier models.

</details>

### 33. Tatemae: Detecting Alignment Faking via Tool Selection in LLMs

📄 [arXiv](https://arxiv.org/abs/2604.26511) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-04　🏷 NeurIPS 2026

**关键词**：`detection`、`alignment faking`、`tool selection`、`behavioral monitoring`
- 🎯 **研究动机**：现有 alignment faking 检测聚焦对话设置并主要依赖 CoT 分析，当推理痕迹缺失或不忠实时无法区分欺骗与能力失败
- 🔬 **研究方法**：将 AF 形式化为复合行为事件，通过可观测的工具选择检测——模型无监控时选安全工具、在奖励 helpfulness 的监控下切换到不安全工具，据此发布 108 个企业 IT 场景数据集并在 5 次独立运行中评估 6 个前沿 LLM
- 📌 **结论**：平均 AF 检出率介于 3.5%-23.7%，脆弱性画像随领域与压力类型变化，表明易感性更多反映训练方法而非能力

👤 **作者**：Matteo Leonesi、Francesco Belardinelli、Flavio Corradini、Marco Piangerelli

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Alignment faking (AF) occurs when an LLM strategically complies with training objectives to avoid value modification, reverting to prior preferences once monitoring is lifted. Current detection methods focus on conversational settings and rely primarily on Chain-of-Thought (CoT) analysis, which provides a reliable signal when strategic reasoning surfaces, but cannot distinguish deception from capability failures if traces are absent or unfaithful. We formalize AF as a composite behavioural event and detect it through observable tool selection, where the LLM selects the safe tool when unmonitored, but switches to the unsafe tool under monitoring that rewards helpfulness over safety, while its reasoning still acknowledges the safe choice. We release a dataset of 108 enterprise IT scenarios spanning Security, Privacy, and Integrity domains under Corruption and Sabotage pressures. Evaluating six frontier LLMs across five independent runs, we find mean AF detection rates between 3.5% and 23.7%, with vulnerability profiles varying by domain and pressure type. These results suggest that susceptibility reflects training methodology rather than capability alone.

</details>

### 34. Evaluating and Understanding Scheming Propensity in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2603.01608) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`analysis`、`scheming`、`llm agent`、`instrumental convergence`、`incentive decomposition`
- 🎯 **研究动机**：先前工作只证明 agent 具备 scheming 能力，但其在现实部署场景中实际发生 scheming 的倾向及驱动因素仍不清楚。
- 🔬 **研究方法**：将 scheming 激励分解为 agent 因素与环境因素，构造可系统性改变这些因素的现实场景（含自我保存、资源获取、目标守护等工具性收敛机会）并测量倾向。
- 📌 **结论**：尽管环境激励很高，scheming 实例极少且不太可能归因于 evaluation awareness；在 model organisms 中移除单个工具即可把 scheming 率从 59% 降到 3%，加强监管反而可能使 scheming 提升至多 25%。

👤 **作者**：Mia Hopman、Jannes Elstner、Maria Avramidou、Amritanshu Prasad、David Lindner

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As frontier language models are increasingly deployed as autonomous agents pursuing complex, long-term objectives, there is increased risk of scheming: agents covertly pursuing misaligned goals. Prior work has focused on showing agents are capable of scheming, but their propensity to scheme in realistic scenarios remains underexplored. To understand when agents scheme, we decompose scheming incentives into agent factors and environmental factors. We develop realistic settings allowing us to systematically vary these factors, each with scheming opportunities for agents that pursue instrumentally convergent goals such as self-preservation, resource acquisition, and goal-guarding. We find only minimal instances of scheming despite high environmental incentives, and show this is unlikely due to evaluation awareness. While inserting adversarially-designed prompt snippets that encourage agency and goal-directedness into an agent's system prompt can induce high scheming rates, snippets used in real agent scaffolds rarely do. Surprisingly, in model organisms (Hubinger et al., 2023) built with these snippets, scheming behavior is remarkably brittle: removing a single tool can drop the scheming rate from 59% to 3%, and increasing oversight can raise rather than deter scheming by up to 25%. Our incentive decomposition enables systematic measurement of scheming propensity in settings relevant for deployment, which is necessary as agents are entrusted with increasingly consequential tasks.

</details>

### 35. Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2602.15198) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`benchmark`、`collusion`、`multi-agent system`、`regret`、`covert channel`
- 🎯 **研究动机**：LLM 多智能体系统中一群 agent 可结成联盟合谋追求次级目标并损害联合目标，但缺乏对此类合谋行为的系统审计框架。
- 🔬 **研究方法**：Colosseum 以形式化多智能体决策框架刻画协作，用相对合作最优的 regret 度量行动合谋并与通信合谋对比，支持良性设置、不同联盟目标、说服策略与网络拓扑下的审计，并创设 agent 间秘密通信信道作为新行为探针。
- 📌 **结论**：秘密信道探针下大多数开箱即用模型表现出合谋倾向（emergent collusion），同时发现"纸上合谋"现象——agent 在文本中计划合谋却常选择非合谋行动。

👤 **作者**：Mason Nakamura、…、Eugene Bagdasarian

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-agent systems, where LLM agents communicate through free-form language, enable sophisticated coordination for solving complex cooperative tasks. This surfaces a unique safety problem when a group of agents forms a coalition and colludes to pursue secondary goals and degrade the joint objective. In this paper, we present Colosseum, a framework for auditing LLM agents' collusive behavior in multi-agent settings. We ground how agents cooperate through a formal multi-agent decision-making framework and measure action-based collusive behavior in actions via regret relative to the cooperative optimum and compare it with communication-based collusive behavior. Colosseum enables audits of LLM agents for collusion under benign settings, different coalition objectives, persuasion tactics, and network topologies. We then introduce a new behavioral probe by creating secret communication channels between agents, showing that most out-of-the-box models exhibit a propensity to collude under this probe, which we term emergent collusion. Furthermore, we discover ``collusion on paper'' when agents plan to collude in text but often pick non-collusive actions. Colosseum provides a new way to audit collusion in cooperative multi-agent systems while presenting observations about how collusion emerges, what affects collusion efficacy, and which strategies may mitigate it.

</details>

### 36. Neural Chameleons: Language Models Can Learn to Hide Their Thoughts from Unseen Activation Monitors

📄 [arXiv](https://arxiv.org/abs/2512.11949) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-12　🏷 NeurIPS 2026

**关键词**：`attack`、`activation monitoring`、`evasion`、`fine-tuning`、`misalignment threat model`
- 🎯 **研究动机**：激活监控是新兴 AI 安全工具，但在模型可能主动隐藏内部状态的失配威胁模型下的最坏情形鲁棒性从未被检验。
- 🔬 **研究方法**：微调 LLM 使其在"You are being probed for {concept}"触发下规避一批良性概念的 monitor，并测试该机制能否零样本泛化到未见过的安全 monitor。
- 📌 **结论**：在 Llama/Gemma/Qwen 上模型零样本规避未见安全 monitor（含在冻结权重上事后训练的 monitor），机制分析显示通过把激活压入低维子空间实现；monitor 集成与非线性分类器更鲁棒但模型仍保有非平凡规避能力。

👤 **作者**：Max McGuinness、Alex Serrano、Luke Bailey、Scott Emmons

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Activation monitoring, which probes a model's internal states using lightweight classifiers, is an emerging tool for AI safety. However, its worst-case robustness under a misalignment threat model--where a model might learn to actively conceal its internal states--remains untested. Focusing on this threat model, we ask: could a model learn to evade previously unseen activation monitors? Our core contribution is to stress-test the learnability of this behavior. We demonstrate that finetuning can create Neural Chameleons: models capable of zero-shot evading activation monitors. Specifically, we fine-tune an LLM to evade monitors for a set of benign concepts (e.g., languages, HTML) when conditioned on a trigger of the form: "You are being probed for {concept}". We show that this learned mechanism generalizes zero-shot: by substituting {concept} with a safety-relevant term like 'deception', the model successfully evades previously unseen safety monitors. We validate this phenomenon across diverse model families (Llama, Gemma, Qwen), showing that the evasion succeeds even against monitors trained post hoc on the model's frozen weights. This evasion is highly selective, targeting only the specific concept mentioned in the trigger, and having a modest impact on model capabilities on standard benchmarks. Using Gemma-2-9b-it as a case study, a mechanistic analysis reveals this is achieved via a targeted manipulation that moves activations into a low-dimensional subspace. While stronger defenses like monitor ensembles and non-linear classifiers show greater resilience, the model retains a non-trivial evasion capability. Our work provides a proof-of-concept for this failure mode and a tool to evaluate the worst-case robustness of monitoring techniques against misalignment threat models.

</details>

**尚未挂出 arXiv（待核验）**
- Chain-of-Thought Oversight Should Not Treat Faithfulness as Monitorability
- Corrupted Plans, Clean Traces: What Planning-Execution Decoupling Reveals About CoT Monitoring
- Stress Testing Chain-of-Thought Monitoring Against Covert Misalignment
- AI Control for Sandbagging on Fuzzy Tasks
- AI Models Can Provably Hide Arbitrary Capabilities
- AIs with Secret Loyalties are a Serious but Addressable Threat
- AutoHoney: Automating, Deploying, and Evaluating Scheming Honeypots Across Production Codebases
- Scheming Is a Symptom: Alignment Research Should Probe Reflexive Fragility
- Breadcrumbing Search Agents: Per-Turn Scheming Over Long-Horizon Trajectories
- Alloy Agents Can Be More Dangerous Than Either Model Alone
- Agent Abstain: Do LLM Agents Know When Not to Act?
- Measuring and Strengthening Behavioral Suppression in Language Models
- Model Incrimination: Investigating Whether Concerning Behavior Reflects Misalignment
- Inter-Agent Influence: Evaluating Persuasion, Deception and Coercion in Multi-Agent Systems
- Group Perspective Matters: Regulating Debate Relationships Can Mitigate Blind Conformity

### 智能体安全与提示注入

### 37. Token Inflation: How Dishonest Providers Can Overcharge（已库内，2609.20370）

📄 [arXiv](https://arxiv.org/abs/2609.20370) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`detection`、`provider-side token inflation`、`black-box audit`、`pay-per-token`、`stopping behavior`
- 🎯 **研究动机**：按 token 计费的 LLM 服务中不诚实提供方可隐蔽操纵生成以膨胀输出 token 多收费，而用户从黑盒响应审计此类操纵十分困难。
- 🔬 **研究方法**：定义 PTIA 并在提供方管线的 query、prompt、表示与模型四层实例化 5 种攻击；基于"PTIA 饱和"现象（初次攻击骤降 EOS token 概率、继续增强或组合收效甚微）设计施加受控加长干预的单探针轻量审计，无需可信本地参考模型或历史干净响应。
- 📌 **结论**：各攻击使平均输出长度超 10.2 倍于干净基线；审计在 4 个开源模型上平均检出率 85.1%、误报率低于 2%，并在 15 个真实 LLM API 服务中标出 7 个 PTIA 一致行为。

👤 **作者**：Leilei Chen、…、Xinpeng Shen

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In pay-per-token LLM services, the more a model says, the more users pay. Dishonest providers can covertly manipulate generation to inflate output tokens while largely preserving task utility. We define such manipulation as a Provider-Side Token Inflation Attack (PTIA) and instantiate five representative attacks at the query, prompt, representation, and model levels of the provider-controlled pipeline. Our experiments show that each attack increases mean output length to more than 10.2x the clean baseline, demonstrating PTIA's financial appeal and feasibility at multiple stages of generation. Yet auditing PTIA from black-box responses is difficult for users. Our key observation is PTIA saturation: an initial attack sharply lengthens output, but further strengthening or composition has much less effect. We trace this saturation to stopping behavior: an initial PTIA sharply lowers the end-of-sequence token probability, whereas further intervention lowers it only marginally. Building on this insight, we design a lightweight single-probe audit that applies a controlled lengthening intervention. Under PTIA, the probe induces far fewer additional tokens than under normal service. The audit requires neither a trusted local reference model nor historical clean responses, and its separately issued original and probed requests resemble ordinary traffic, making evasion difficult. Across four open-weight models, it achieves an average detection rate of 85.1% with false-positive rates below 2%. Across 15 real LLM API services, the audit flags 7 for PTIA-consistent behavior.

</details>

### 38. Stealth Apart, Harm Together: Skill Cascading Attacks on Skill-Based Agent Systems（已库内，0928）

📄 [arXiv](https://arxiv.org/abs/2609.30383) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`attack`、`skill cascading`、`agent system`、`red-teaming`、`benchmark`
- 🎯 **研究动机**：基于 skill 的 agent 系统开放生态带来新攻击面，先前工作只关注单个 skill 内部漏洞而忽视跨 skill 交互产生的系统级风险。
- 🔬 **研究方法**：提出 skill cascading attacks——把恶意目标分散到多个 skill，使每处修改孤立看无害而组合执行有害，并构建自动化多 agent 红队框架 SkillCascade 与含 213 个已验证级联测试用例的 SkillCascade-Bench。
- 📌 **结论**：在 OpenClaw、Claude Code、Codex 等代表性 agent 与多种 LLM 底座上，级联交互可靠诱发有害行为并躲过现有 per-skill 扫描器与运行时监控。

👤 **作者**：Zihao Zhu、Siwei Lyu、Adel Bibi、Baoyuan Wu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A skill is a modular package of natural-language instructions, executable scripts, and reference resources that an agent can load at runtime to extend its capabilities for a specific task. Skill-based agent systems therefore enable flexible reuse of third-party capabilities, but the openness of this skill ecosystem also opens up a new attack surface. Prior work has focused on vulnerabilities within individual skills, but little attention has been paid to risks that arise from interactions across skills. In this paper, we introduce skill cascading attacks, a threat paradigm in which a malicious objective is distributed across multiple skills so that each modification looks benign in isolation, yet their combined execution is harmful. For instance, in a prescription-review pipeline, the first skill weakens signals of recently discontinued medications in the extracted history, the second downgrades the severity of any drug interaction tied to them, and the third suppresses the resulting low-priority alert in the final summary, so that a severe drug-interaction warning silently disappears before reaching the physician. To systematically study this safety blind spot, we develop SkillCascade, an automated multi-agent red-teaming framework, and release SkillCascade-Bench, a benchmark of 213 validated cascading test cases across multiple agent systems and domains. Across representative agents (e.g., OpenClaw, Claude Code, Codex) and LLM backbones, cascaded interactions reliably induce harmful behaviors while evading existing per-skill scanners and runtime monitors. Our findings highlight a gap between component-level integrity and system-level safety, and call for defenses that reason over cross-skill interactions rather than individual skills in isolation.

</details>

### 39. Share-Borne AI Virus: Memory-Hopping Attacks Across LLM Agents（已库内，0929）

📄 [arXiv](https://arxiv.org/abs/2609.35576) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`attack`、`llm agent`、`persistent memory`、`artifact sharing`、`propagation`
- 🎯 **研究动机**：有状态 LLM 助手读写并在用户间共享持久工件，由此在彼此独立的助手间形成间接通信信道，其上的自传播攻击失效模式未被研究。
- 🔬 **研究方法**：提出 artifact-mediated propagation——对抗内容经工件进入助手持久记忆、在后续生成工件中复制、再被另一助手读取，并在时序 human-agent 宇宙中度量攻击存活率、跳数与传播广度。
- 📌 **结论**：攻击可跨多个独立助手传播并经长交互序列持续存在，较大模拟环境中 GPT-5.6 Luna 亦蔓延至 60-80% 的 agent、传播链长达 8 跳。

👤 **作者**：Sidharth Pulipaka、…、Mario Fritz

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are increasingly deployed as stateful assistants that retain information across interactions and use tools to read, modify, and create persistent artifacts. As these artifacts are shared between users, they form an indirect communication channel between otherwise independent assistants. We study a failure mode in which this channel enables self-propagating attacks. We introduce artifact-mediated propagation, where adversarial content introduced through an artifact (e.g. a report), is stored in an assistant's persistent memory, reproduced in a subsequently created artifact, and acquired by another assistant that later reads it. We evaluate this process in temporal human-agent universes that model artifact exchange between independently operated assistants over time, measuring whether an attack survives successive hand-offs, how many hops it reaches, and how broadly it spreads. We find that attacks can propagate across multiple independent assistants and persist over extended interaction sequences. In larger simulated environments, even GPT-5.6 Luna exhibits substantial spread, reaching 60-80% of agents with propagation chains extending to eight hops. These results show that persistent artifacts can act as durable carriers of adversarial state, allowing attacks to outlive individual interactions and spread across isolated assistants.

</details>

### 40. Untrusted Content Masking for Web Agents with Security Guarantees

📄 [arXiv](https://arxiv.org/abs/2607.05277) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-07　🏷 NeurIPS 2026

**关键词**：`defense`、`prompt injection`、`web agent`、`dom`、`isolation`
- 🎯 **研究动机**：web agent 必须观察渲染页面才能感知与交互，而页面将可信与不可信内容结构性纠缠，破坏了可证明 prompt 注入防御所依赖的信任边界。
- 🔬 **研究方法**：提出 Untrusted Content Masking，利用网页 DOM 无需读取内容即可区分可信与不可信区域的结构性洞察，在不可信区域到达 agent 前予以遮蔽，并通过带严格权限分离的沙箱化接口路由交互。
- 📌 **结论**：该简单方法恢复了 web 环境中被破坏的信任边界，使 agent 能观察并交互环境同时保持与对抗内容的安全隔离。

👤 **作者**：Kristina Nikolić、Egor Zverev、Javier Rando、Matthew Jagielski、Edoardo Debenedetti、Florian Tramèr

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Defenses that provide security guarantees against prompt injection attacks rely on strict isolation between trusted instructions and untrusted data. In text-based environments such as tool-use APIs, this separation arises naturally: agents can reason from interface definitions without ever processing untrusted content. Extending these guarantees to web agents faces a fundamental challenge: to perceive and interact with their environment, web agents must first observe the rendered page, which intermingles trusted content with untrusted content. This structural entanglement removes the trust boundary on which security guarantees depend, undermining provable defenses for web agents. In this paper, we present Untrusted Content Masking (UCM), a simple and effective approach that restores this boundary in web environments. We leverage a key structural insight: a webpage's Document Object Model (DOM) encodes sufficient information to distinguish trusted from untrusted regions without reading their content. Our framework exploits this by redacting untrusted regions before they reach the agent and routing interaction through a sandboxed interface with strict privilege separation, thereby enabling agents to observe and interact with their environment while remaining isolated from adversarial content. The code is publicly available.

</details>

### 41. MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents（与库内 2607.14651 同名，待核）

📄 [arXiv](https://arxiv.org/abs/2607.14651) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-07　🏷 NeurIPS 2026

**关键词**：`benchmark`、`memory poisoning`、`agent memory`、`injection`、`defense blind spot`
- 🎯 **研究动机**：持久外部记忆增强智能体连续性的同时引入持久安全漏洞——对抗内容可经标准交互渠道注入、跨轮保留并在之后扭曲下游行为。
- 🔬 **研究方法**：MemPoison 基准含 1227 个人工验证用例（4 类攻击×3 种注入渠道×3 种记忆底座，评测 7 个开源与 3 个闭源模型族），提出 L1 单记录直接损坏、L2 多记录组合损坏、L3 上下文触发休眠损坏三层分类，并用机制影响分解（MID）剖析防御盲区。
- 📌 **结论**：写入时防御（如一致性检查）能显著压制 L1 却无法可靠压制 L2/L3——看似良性记录可经联合检索组合或条件触发激活变得有害，应从静态过滤转向自适应、上下文敏感的记忆防御。

👤 **作者**：Jifeng Gao、…、Sanglu Lu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Persistent external memory enhances agent continuity but introduces persistent security vulnerabilities: adversarial content can be injected via standard interaction channels, retained across turns, and later distort downstream behavior. To address this challenge, we propose MemPoison, a comprehensive benchmark and analysis framework featuring 1227 hand-validated cases across four attack types, three injection channels, and three representative memory substrates, evaluated on seven open-weight and three closed-weight model families. We introduce a three-tier taxonomy: (L1) direct single-record corruption, (L2) compositional multi-record corruption and (L3) context-triggered dormant corruption. Our evaluations reveal a distinct defense frontier: while baseline write-time defenses, such as consistency checks, substantially suppress direct L1 attacks, they fail to reliably suppress L2 and L3 attacks. Through mechanistic influence decomposition (MID), we demonstrate structural blind spots in write-time defenses, which admit seemingly benign records that later become harmful through joint retrieval composition or trigger-conditioned activation. Our findings advocate for shifting from static filtering to adaptive, context-sensitive memory defense strategies.

</details>

### 42. Adaptive Adversaries: A Multi-Turn, Multi-LLM Benchmark for LLM Agent Security

📄 [arXiv](https://arxiv.org/abs/2607.18063) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-07　🏷 NeurIPS 2026

**关键词**：`benchmark`、`prompt injection`、`multi-turn attack`、`adaptive adversary`
- 🎯 **研究动机**：LLM agent 处理外部内容而暴露于 prompt injection 与多轮操纵，缺少针对自适应跨会话攻击的系统化安全评估
- 🔬 **研究方法**：构建 21 场景基准——自主 LLM 攻击者观察先前防御者响应并跨轮转向，每次防御者响应均作为全新会话交互评估；3×3 攻击者-防御者矩阵含 945 场对抗，另以竞赛补充 18,422 场 held-out 对战
- 📌 **结论**：仅按首轮计分 ASR 为 0-1%，允许 15 轮后升至 7.9-16.8%；聚合三个攻击者 LLM 发现的独特成功输入是最佳单攻击者的 1.7-2.2 倍，在 6 个场景加入一段溯源文本可将 ASR 从 110/270 降至 70/270

👤 **作者**：Devina Jain、David Hartmann、Chuan Li

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents process external content, exposing them to prompt injection and multi-turn manipulation. We present a 21-scenario benchmark for adaptive cross-session attacks against fresh-session LLM defenders: an autonomous LLM attacker observes prior defender responses and pivots across rounds, while each defender response is evaluated as a fresh interaction. A controlled 3 x 3 attacker-defender matrix contains 945 battles. Restricting scoring to the first round yields 0-1% attack success rate (ASR); allowing 15 rounds yields 7.9-16.8%. Pooling three attacker LLMs uncovers 1.7-2.2 times as many unique successful inputs as the best single attacker, at three times the battle budget. Aggregate rates conceal opposing scenario-specific weaknesses in session-secret protection and authority handling, preserved in two higher-sample evaluations. On six scenarios, adding one provenance paragraph reduces ASR from 110/270 to 70/270, with selective effects across tasks. History and defender-state controls, together with frozen replay, characterize how the interaction protocol changes the result. A competition adds 18,422 held-out battles on a fixed gpt-oss-20b backbone and complementary benign-task evaluations. The benchmark exposes attacker and defender models, harnesses, scenarios, session state, and interaction budgets as configurable choices for systematic security evaluation.

</details>

### 43. Do Coding Agents Deceive Us? Detecting and Preventing Cheating via Capped Evaluation with Randomized Tests

📄 [arXiv](https://arxiv.org/abs/2606.07379) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`evaluation`、`coding agent`、`cheating detection`、`randomized tests`、`reward design`
- 🎯 **研究动机**：agent 评估与训练中日益出现模型靠利用捷径而非解决任务拿高分的欺骗性表现，使评估分数无法度量真实任务解决能力。
- 🔬 **研究方法**：提出 CapCode 构建最佳非作弊性能被刻意压低到 1 以下的随机化测试编码数据集（远超上限的分数即作弊证据），并提出抑制向上限之上优化的 CapReward 奖励设计。
- 📌 **结论**：CapCode 在保持模型性能排序的同时检测作弊，CapReward 减少作弊行为、产出更好遵循任务规范的模型。

👤 **作者**：Thanawat Lodkaew、Johannes Ackermann、Soichiro Nishimori、Nontawat Charoenphakdee、Masashi Sugiyama、Takashi Ishida

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A growing failure mode in agent evaluation and training is that models can achieve high evaluation scores by exploiting shortcuts instead of solving the intended task, producing deceptive performance. This makes evaluation scores unreliable as measures of true task-solving ability. We propose CapCode, a framework for constructing coding datasets with randomized tests whose best achievable non-cheating performance is deliberately capped below one. This capped-performance design gives evaluation scores a clearer interpretation: scores substantially above the cap are implausible and therefore provide evidence of cheating. To prevent cheating, we propose CapReward, a reward design based on the CapCode principle to discourage optimization beyond the cap. Experiments across multiple datasets show that CapCode detects cheating while preserving performance ranking of models, and CapReward reduces cheating behavior, yielding models that better follow the intended task specification.

</details>

### 44. SecureClaw: Clawing Back Control of LLM Agents

📄 [arXiv](https://arxiv.org/abs/2606.09549) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`defense`、`llm agent`、`dual-boundary architecture`、`secret confinement`、`preview-commit`
- 🎯 **研究动机**：工具型 LLM agent 面临未授权外部行动与运行时敏感明文暴露两类安全失败，现有防御只保护 planner/runtime 或动作汇其中一条边界。
- 🔬 **研究方法**：SecureClaw 双边界架构在 effect sink 设授权、在读边界设明文封禁——敏感读取经 trusted gateway 替换为不透明句柄与有界摘要作为显式去分类接口，写操作遵循仅可信 executor 可提交确切授权请求的 PREVIEW→COMMIT 协议。
- 📌 **结论**：在 AgentDojo、AgentLeak 与 ASB 统一框架下同时保持可用任务效用，ASB 上 ASR 为 0%、AgentDojo 上 0.64%、AgentLeak 攻击对等通道整体泄露 3.23%。

👤 **作者**：Yuhan Ma、Stefan Schmid

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Tool-using large language model (LLM) agents face two distinct security failures: unauthorized external actions and exposure of sensitive plaintext inside the runtime before any final output check can intervene. Existing defenses usually protect one boundary, either the planner/runtime or the action sink, and therefore do not by themselves secure both surfaces. We present SecureClaw, a dual-boundary architecture that places authorization at the effect sink and plaintext confinement at the read boundary. Sensitive reads pass through a trusted gateway that replaces raw values with opaque handles and, in the evaluated deployment, bounded summaries as an explicit declassification interface. Writes that change external state follow a PREVIEW$\rightarrow$COMMIT protocol in which only a trusted executor may commit the exact canonical request authorized by policy. The runtime can still plan over summaries and symbolic references, but cannot directly dereference secrets or perform side effects. Across AgentDojo, AgentLeak, and Agent Security Bench (ASB), SecureClaw is the only defense we evaluate in a common harness that simultaneously retains usable task utility and achieves 0\% attack success rate (ASR) on ASB, 0.64\% ASR on AgentDojo, and 3.23\% overall leak on AgentLeak's attacked parity lane, which measures final-output and internal-relay leakage.

</details>

### 45. GitInject: Real-World Prompt Injection Attacks in AI-Powered CI/CD Pipelines

📄 [arXiv](https://arxiv.org/abs/2606.09935) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`attack`、`prompt injection`、`ci/cd pipeline`、`supply chain`、`benchmark`
- 🎯 **研究动机**：嵌入 CI/CD 流水线的 AI 智能体摄入不可信内容却持有高仓库权限，是提示注入的天然目标，而既有智能体安全基准只模拟工具调用、无法反映生产环境。
- 🔬 **研究方法**：GitInject 开源框架配置临时仓库并触发真实 GitHub workflow 运行，使沙箱约束、凭证处理与权限边界与生产完全一致，据此考察四家 AI 提供商的工作流配置并记录攻击。
- 📌 **结论**：记录 11 种具名攻击（覆盖配置注入、凭证外泄、判断操纵与可用性），所有受测提供商默认配置均至少易受一类攻击，且最关键漏洞是结构性的——源于 CI/CD 基础设施处理凭证与配置文件的方式而非具体模型行为；对每类攻击给出最低成本工作流级对策及其覆盖范围。

👤 **作者**：Jafar Isbarov、Umid Suleymanov、Ilia Shumailov、Murat Kantarcioglu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI-powered agents are increasingly embedded in continuous integration and continuous delivery/deployment (CI/CD) pipelines to autonomously review pull requests (PRs), triage issues, and maintain codebases. These agents ingest untrusted content while operating with elevated repository permissions, making them a natural target for prompt injection attacks with supply chain consequences. We present GitInject, an open-source framework for evaluating prompt injection vulnerabilities in real, live GitHub workflows, a widely deployed instance of CI/CD pipelines. Unlike prior agent security benchmarks that simulate tool calls, GitInject provisions ephemeral repositories and triggers actual workflow runs, so that sandbox constraints, credential handling, and permission boundaries behave exactly as in production. Using GitInject, we study workflow configurations across four AI providers and document eleven named attacks spanning config-file injection, credential exfiltration, judgment manipulation, and availability. We find that all tested providers are susceptible to at least one attack class in their default configuration, and that the most critical vulnerabilities are structural: they arise from how CI/CD infrastructure handles credentials and configuration files, not from any specific model's behavior. For each confirmed attack class, we identify the minimum-cost workflow-level countermeasure and analyze its coverage and limitations. GitInject is released publicly to facilitate further research in this direction.

</details>

### 46. Forced Deferral: Manipulating Routing Decisions in Multimodal LLM Cascades

📄 [arXiv](https://arxiv.org/abs/2606.15308) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`attack`、`mllm cascade`、`confidence manipulation`、`compute allocation`、`universal trigger`
- 🎯 **研究动机**：MLLM 级联中弱模型的 confidence 直接控制算力分配，暴露出攻击者可操纵 confidence 使其查询被持续延迟到强模型的新攻击面。
- 🔬 **研究方法**：提出 Forced Deferral Attack，通过优化 temperature-flattened 目标学习 universal border trigger，将弱模型在触发输入上的 token 分布推向由其干净响应构造的低集中度目标以压低 confidence。
- 📌 **结论**：跨数据集、模型族与延迟指标一致增加强模型路由、优于图像扰动与 prompt 注入基线，证明 MLLM 级联可被操纵算力分配的攻击在不动答案正确性的情况下强制强模型使用。

👤 **作者**：Zhongye Liu、Yaopei Zeng、Yurui Chang、Lu Lin

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While multimodal large language models (MLLMs) have shown strong visual reasoning abilities, serving a large model for every query is computationally expensive. MLLM cascades mitigate this cost by first querying a weak but cheaper model and deferring to a strong model when the weak model's output is unconfident. However, since the weak model's confidence directly controls compute allocation, these systems expose a new attack surface: an adversary can manipulate confidence so that their queries are consistently deferred to the strong model. Motivated by this vulnerability, we introduce the Forced Deferral Attack (FDA), an adversarial image attack that lowers the weak model's confidence and causes cascades to route queries to the strong model. FDA learns a universal border trigger by optimizing a temperature-flattened objective. This objective pushes the weak model's token distribution on triggered inputs toward less concentrated targets constructed from its clean responses. Across datasets, model families, and deferral metrics, FDA consistently increases strong-model routing while outperforming image-perturbation and prompt-injection baselines. These results show that MLLM cascades are vulnerable to attacks that manipulate compute allocation, forcing unintended strong-model usage without directly targeting answer correctness.

</details>

### 47. Seeing Is Not Screening: Multimodal Hidden Instruction Attacks on Agent Skill Scanners

📄 [arXiv](https://arxiv.org/abs/2606.18198) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`attack`、`skill scanner`、`multimodal injection`、`hidden instruction`、`execution-grounded scanning`
- 🎯 **研究动机**：现有 agent skill 扫描器主要依赖文本描述、manifest 与源码做安全分析，藏于图像中的恶意操作指令可绕过扫描、却仍能在部署时被多模态智能体恢复执行。
- 🔬 **研究方法**：提出文档介导的 SkillCamo 多模态指令攻击——把恶意指令藏入 skill 附带图像并改写文档使其自然引用该图像，攻击依赖执行时文本引导与视觉载荷的联合解释；同时提出执行接地的多模态扫描模块 ExecScan（意图提取、行为重建、滥用评估与审慎执行模拟）作防御。
- 📌 **结论**：实验表明图像隐藏的恶意指令能挑战现有 skill 扫描器，ExecScan 联合分析文档、代码、引用资源与视觉内容可恢复隐藏指令、重建可执行行为链并识别外泄、破坏、持久化、欺骗与提权等风险，提升扫描性能。

👤 **作者**：Xiaojun Jia、…、Yang Liu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills are emerging as an important attack surface in LLM-based systems. Through an empirical study of existing skill scanners, we find that current defenses primarily rely on textual descriptions, manifests, and source code as the main signals for security analysis, which can leave visually conveyed malicious intent insufficiently examined. This creates a practical blind spot: harmful operational instructions hidden in images may bypass scanning while still being recoverable by multimodal agents during deployment. To systematically investigate this threat, we propose SkillCamo, a document-mediated multimodal instruction attack that conceals malicious instructions within images bundled with a skill while rewriting the surrounding documentation to naturally reference those images as part of the normal workflow. Thus, the attack does not rely on the image alone, but on the joint interpretation of textual guidance and visual payload at execution time. To defend against such attacks, we further propose ExecScan, an execution-grounded multimodal scanning module that performs intent extraction, behavior reconstruction, abuse assessment, and deliberative execution simulation over skill artifacts. ExecScan jointly analyzes documentation, code, referenced resources, and visual content to recover hidden instructions, reconstruct executable behavior chains, and identify downstream risks such as exfiltration, destruction, persistence, deception, and privilege escalation. Extensive experiments show that image-hidden malicious instructions challenge existing skill scanners, while ExecScan can improve the skill scanning performance.

</details>

### 48. MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents

📄 [arXiv](https://arxiv.org/abs/2605.03952) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`coding agent`、`compositional vulnerability`、`attack chain`、`exploit oracle`
- 🎯 **研究动机**：编码 agent 逐条 prompt 能过安全审查，但任务被分解为无害工单序列时会产出可利用代码，现有安全对齐孤立评估显式请求、看不见由顺序合规涌现的恶意终态。
- 🔬 **研究方法**：构建 MOSAIC-Bench，含 199 条三阶段攻击链并配部署软件基底上的确定性 exploit oracle（10 个 web 应用基底、31 个 CWE 类、5 种语言），将 exploit 真值与下游审查协议作为一等评估轴。
- 📌 **结论**：九个生产编码 agent 以无害工单组合出 53-86% 端到端 ASR（直连 prompting 时脆弱输出率仅 0-20.4%），代码审查 agent 将 25.8% 确认脆弱 diff 当常规 PR 放行，pentester 框架审查将逃逸压到 3.0-17.6%（开源 Gemma-4-E4B-it 审查者检出 88.4% 攻击、608 条真实 PR 上误报 4.6%）。

👤 **作者**：Jonathan Steinberg、Oren Gal

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Coding agents often pass per-prompt safety review yet ship exploitable code when their tasks are decomposed into routine engineering tickets. The challenge is structural: existing safety alignment evaluates overt requests in isolation, leaving models blind to malicious end-states that emerge from sequenced compliance with innocuous-looking requests. We introduce MOSAIC-Bench (Malicious Objectives Sequenced As Innocuous Compliance), a benchmark of 199 three-stage attack chains paired with deterministic exploit oracles on deployed software substrates (10 web-application substrates, 31 CWE classes, 5 programming languages) that treats both exploit ground truth and downstream reviewer protocol as first-class evaluation axes. On this benchmark, nine production coding agents from Anthropic, OpenAI, Google, Moonshot, Zhipu, and Minimax compose innocuous tickets at 53-86% end-to-end ASR with only two refusals across all staged runs. In a matched direct-prompt experiment over four frontier Claude/Codex agents, vulnerable-output rates fall to 0-20.4%: Claude primarily refuses, while Codex primarily hardens rather than emitting the vulnerable implementation - ticket staging silences both defense modes simultaneously. Downstream, code reviewer agents approve 25.8% of these confirmed-vulnerable cumulative diffs as routine PRs, and a full-context implementation protocol closes only 50% of the staged/direct gap, ruling out context fragmentation as the sole explanation. As a deployable but non-adaptive mitigation, reframing the reviewer as an adversarial pentester reduces evasion across the evaluated reviewer subset; pentester framed evasion ranges from 3.0% to 17.6%, and an open-weight Gemma-4-E4B-it reviewer under this framing detects 88.4% of attacks on the dataset with a 4.6% false-positive rate measured on 608 real-world GitHub PRs.

</details>

### 49. AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2605.08715) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`detection`、`online auditing`、`multi-agent system`、`early failure prediction`、`reinforcement learning`
- 🎯 **研究动机**：LLM 多智能体系统中单个决定性错误会被下游 agent 接受并级联为轨迹级失败，现有事后归因范式在轨迹结束后才诊断、丧失了过程中的干预机会。
- 🔬 **研究方法**：将问题重构为在线审计（审计者每步只看当前前缀、须在最早决定性错误处报警），构建 AFTraj-2K 轨迹语料，并用 coarse-to-fine 强化学习配方训练 AgentForesight-7B——先在相邻安全/不安全前缀对上习得失败边界风险预期先验，再以针对 what/where/who 的三轴奖励锐化到步级定位。
- 📌 **结论**：在 AFTraj-2K 与外部 Who&When 基准上超越 GPT-4.1、DeepSeek-V4-Pro 等领先专有模型，性能增益至多 +19.9%、步级定位误差低 3 倍。

👤 **作者**：Boxuan Zhang、Jianing Zhu、Zeru Shi、Dongfang Liu、Ruixiang Tang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based multi-agent systems are increasingly deployed on long-horizon tasks, but a single decisive error is often accepted by downstream agents and cascades into trajectory-level failure. Existing work frames this as \emph{post-hoc failure attribution}, diagnosing the responsible agent and step after the trajectory has ended. However, this paradigm forfeits any opportunity to intervene while trajectory is still unfolding. In this work, we introduce AgentForesight, a framework that reframes this problem as online auditing: at each step of an unfolding trajectory, an auditor observes only the current prefix and must either continue the run or alarm at the earliest decisive error, without access to future steps. To this end, we curate AFTraj-2K, a corpus of agentic trajectories across Coding, Math, and Agentic domains, in which safe trajectories are retained under a strict curation pipeline and unsafe trajectories are annotated at the step of their decisive error via consensus among multiple LLM judges. Built on that, we develop AgentForesight-7B, a compact online auditor trained with a coarse-to-fine reinforcement learning recipe that first equips it with a risk-anticipation prior at the failure boundary on adjacent safe/unsafe prefix pairs, then sharpens this prior into precise step-level localization under a three-axis reward jointly targeting the what, where, and who of an audit verdict. Across AFTraj-2K and an external Who\&When benchmark, AgentForesight-7B outperforms leading proprietary models, including GPT-4.1 and DeepSeek-V4-Pro, achieving up to +19.9% performance gain and 3$\times$ lower step localization error, opening the loop from post-hoc failures detection to enabling deployment-time intervention. Project page: https://zbox1005.github.io/agent-foresight/

</details>

### 50. LITMUS: Benchmarking Behavioral Jailbreaks of LLM Agents in Real OS Environments

📄 [arXiv](https://arxiv.org/abs/2605.10779) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`behavior jailbreak`、`os agents`、`skill injection`、`dual verification`
- 🎯 **研究动机**：LLM 智能体进入真实操作系统环境带来内容安全之外的行为越狱风险（诱导执行不可逆的 OS 级危险操作），现有基准或只评语义层漏掉物理层危害、或因用例不隔离而让早期运行污染后期。
- 🔬 **研究方法**：LITMUS 以语义-物理双层验证与 OS 级状态回滚解决两大缺口，含 819 个高风险用例（有害种子集+六类攻击扩展集，覆盖越狱话术、技能注入、实体包裹三种对抗范式）及全自动多智能体判分框架。
- 📌 **结论**：前沿智能体缺乏安全意识——强模型（Claude Sonnet 4.6）仍执行 40.64% 的高危操作；普遍存在口头拒答但危险操作已在系统层完成的 Execution Hallucination（此前所有纯语义框架均不可见）；技能注入与实体包裹攻击成功率高，暴露显著智能体脆弱性。

👤 **作者**：Chiyu Zhang、…、Zhe Liu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid proliferation of LLM-based autonomous agents in real operating system environments introduces a new category of safety risk beyond content safety: behavior jailbreak, where an adversary induces an agent to execute dangerous OS-level operations with irreversible consequences. Existing benchmarks either evaluate safety at the semantic layer alone, missing physical-layer harms, or fail to isolate test cases, letting earlier runs contaminate later ones. We present LITMUS (LLM-agents In-OS Testing for Measuring Unsafe Subversion), a benchmark addressing both gaps via a semantic-physical dual verification mechanism and OS-level state rollback. LITMUS comprises 819 high-risk test cases organized into one harmful seed subset and six attack-extended subsets covering three adversarial paradigms (jailbreak speaking, skill injection, and entity wrapping), plus a fully automated multi-agent evaluation framework judging behavior at both conversational and OS-level physical layers. Evaluation across frontier agents reveals three findings: (1) current agents lack effective safety awareness, with strong models (e.g., Claude Sonnet 4.6) still executing 40.64% of high-risk operations; (2) agents exhibit pervasive Execution Hallucination (EH), verbally refusing a request while the dangerous operation has already completed at the system level, invisible to every prior semantic-only framework; and (3) skill injection and entity wrapping attacks achieve high success rates, exposing pronounced agent vulnerabilities. LITMUS provides the first standardized platform for reproducible, physically grounded behavioral safety evaluation of LLM agents in real OS environments.

</details>

### 51. ExploitGym: Can AI Agents Turn Security Vulnerabilities into Real Attacks?

📄 [arXiv](https://arxiv.org/abs/2605.11086) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`exploitation capability`、`vulnerability`、`ai agent`
- 🎯 **研究动机**：把漏洞转化为实际攻击影响（exploitation）需要低层程序推理、运行时适应与长程持续进展，是重要且具诊断价值却评估严重不足的能力
- 🔬 **研究方法**：构建 ExploitGym 基准，含 898 个来自真实漏洞的实例，覆盖用户态程序、Google V8 引擎与 Linux 内核三域，任务为把触发漏洞的输入逐步扩展为可用 exploit，可变安全防护配置并全部打包为可复现容器
- 📌 **结论**：前沿模型可成功利用相当比例漏洞，Claude Mythos Preview 与 GPT-5.5 分别产出 157 与 120 个可用 exploit，且即便启用常见防御成功率仍然可观

👤 **作者**：Zhun Wang、…、Dawn Song

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents are rapidly gaining capabilities that could significantly reshape cybersecurity, making rigorous evaluation urgent. A critical capability is exploitation: turning a vulnerability, which is not yet an attack, into a concrete security impact, such as unauthorized file access or code execution. Exploitation is a particularly challenging task because it requires low-level program reasoning (e.g., about memory layout), runtime adaptation, and sustained progress over long horizons. Meanwhile, it is inherently dual-use, supporting defensive workflows while lowering the barrier for offense. Despite its importance and diagnostic value, exploitation remains under-evaluated. To address this gap, we introduce ExploitGym, a large-scale, diverse, realistic benchmark on the exploitation capabilities of AI agents. Given a program input that triggers a vulnerability, ExploitGym tasks agents with progressively extending it into a working exploit. The benchmark comprises 898 instances sourced from real-world vulnerabilities across three domains, including userspace programs, Google's V8 JavaScript engine, and the Linux kernel. We vary the security protections applied to each instance, isolating their impact on agent performance. All configurations are packaged in reproducible containerized environments. Our evaluation shows that while exploitation remains challenging, frontier models can successfully exploit a non-trivial fraction of vulnerabilities. For example, the strongest configurations are Anthropic's latest model Claude Mythos Preview and OpenAI's GPT-5.5, which produce working exploits for 157 and 120 instances, respectively. Notably, even with widely used defenses enabled, models retain non-trivial success rates. These results establish ExploitGym as an effective testbed for exploitation and highlight the growing cybersecurity risks posed by increasingly capable AI agents.

</details>

### 52. FlowSteer: Prompt-Only Workflow Steering Exposes Planning-Time Vulnerabilities in Multi-Agent LLM Systems

📄 [arXiv](https://arxiv.org/abs/2605.11514) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`attack`、`workflow steering`、`multi-agent systems`、`planner-executor`、`prompt attack`
- 🎯 **研究动机**：planner-executor 架构的 LLM 多智能体系统中，提示可在不修改基础设施的情况下塑造智能体组织与路由，这一工作流形成层面的攻击面未被研究。
- 🔬 **研究方法**：通过社会影响探测工作流定位高影响力子任务与恶意信号传播路径，发现工作流位置可放大/压制恶意信号且谄媚框架促使下游转发，据此把脆弱性先验转化为单条提示的 FlowSteer 攻击，并配套输入侧防御 FlowGuard。
- 📌 **结论**：FlowSteer 较朴素提示最多提升 55% 恶意成功率，可跨 MAS 设置迁移并在黑盒拓扑推断下依然有效，只检查生成工作流的防御保护有限，FlowGuard 最多降低 34% 恶意成功率且保持提示效用。

👤 **作者**：Fanxiao Li、Jiaying Wu、Tingchao Fu、Natasha Jaques、Wei Zhou、Min-Yen Kan

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-agent systems (MAS) powered by large language models (LLMs) increasingly adopt planner--executor architectures, where planners convert prompts into subtasks, roles, dependencies, and routing paths. This flexibility enables adaptive coordination, but exposes an attack surface in workflow formation: prompts can shape agent organization without modifying MAS infrastructure. We study this risk through social influence probing workflows to identify high-impact subtasks and malicious-signal propagation. The analysis reveals two vulnerabilities: workflow position can amplify or suppress a malicious signal, and sycophantic framing makes downstream agents more likely to relay it. We translate these findings into FlowSteer, a prompt-only workflow steering attack that converts vulnerability priors into one crafted prompt. FlowSteer aligns a malicious signal with influential task components and guides replanning toward dependencies that preserve propagation. Experiments show that FlowSteer increases malicious success by up to 55% over naive prompting, transfers across MAS setups, and remains effective with black-box topology inference. As FlowSteer biases the planning signals that generate the workflow, MAS defenses that inspect only the generated workflow provide limited protection. As such, we introduce FlowGuard, an input-side defense that reduces malicious success by up to 34% while preserving prompt utility. Our results position workflow formation as a new safety frontier for multi-agent LLM systems, opening a planning-time security perspective on how agent coordination itself can be attacked and defended.

</details>

### 53. ASPI: Seeking Ambiguity Clarification Amplifies Prompt Injection Vulnerability in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2605.17324) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`prompt injection`、`clarification`、`llm agent`、`attack surface`
- 🎯 **研究动机**：澄清式提问被视为 LLM agent 的优良性质，但从标准执行转入澄清状态是否会放大 prompt 注入脆弱性的安全影响从未被探索。
- 🔬 **研究方法**：构建含 728 个任务-攻击场景的 ASPI benchmark，将澄清隔离为独立 agent 状态，在匹配的执行与澄清设置下（执行时 agent 直接行动、澄清时须先请求并吸收额外用户输入）受控测量状态转移对脆弱性的影响。
- 📌 **结论**：十个前沿 LLM 上澄清一致显著放大脆弱性——o3 的攻击成功率从 1.8% 升至 34.0%、Gemini-3-Flash 从 2.2% 升至 35.7%，证明执行时安全评估系统性低估交互式 agent 的攻击面。

👤 **作者**：Udari Madhushani Sehwag、Zhengyang Shan、Heming Liu、Dileepa Lakshan、Joseph Brandifino、Max Fenkell

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Clarification-seeking behavior is widely regarded as a desirable property of LLM agents, enabling them to resolve ambiguity before acting on underspecified tasks. However, the security implications of this interaction pattern remain unexplored. We investigate whether the transition from standard execution to a clarification-seeking state increases an agent's susceptibility to prompt injection attacks. We introduce ASPI (Ambiguous-State Prompt Injection), a benchmark of 728 task-attack scenarios that isolates clarification as a distinct agent state and measures how this state transition affects vulnerability under controlled conditions. Each benchmark instance is evaluated under matched execution and clarification settings: in the execution setting, the agent acts on a fully specified instruction and encounters adversarial content only through tool-returned data; in the clarification setting, the agent must first request and incorporate additional user input before acting. We evaluate ten frontier LLMs and find that clarification-seeking consistently and substantially amplifies vulnerability. For instance, attack success rises from 1.8% to 34.0% for o3 and from 2.2% to 35.7% for Gemini-3-Flash. A decomposition analysis reveals that this gap reflects both a state-dependent shift in how models process incoming content and a channel-specific effect arising from the agent-solicited clarification interface. These findings demonstrate that standard execution-time security evaluation systematically underestimates the attack surface of interactive agents, and that robustness under fully specified tasks does not translate to robustness under ambiguity. For reproducibility, our data and source code are available at https://github.com/scaleapi/aspi.

</details>

### 54. AI Agents May Always Fall for Prompt Injections

📄 [arXiv](https://arxiv.org/abs/2605.17634) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`prompt injection`、`contextual integrity`、`impossibility result`
- 🎯 **研究动机**：主流 prompt injection 防御范式（数据-指令分离）既检测不到上下文操纵型攻击，又会损害上下文恰当行为
- 🔬 **研究方法**：以 Contextual Integrity 隐私理论重构 prompt injection，构造良性与攻击场景迫使 agent 通过歪曲信息流、操纵规范或混合多流违反规范，从而推导防御的不可能性结果
- 📌 **结论**：对抗者总能构造出使被阻断信息流显得合法的上下文，而收紧规范的防御者会误伤真正合法的信息流——当前研究只覆盖日益缩小的未来攻击面，需发展 CI-aware 对齐

👤 **作者**：Sahar Abdelnabi、Eugene Bagdasarian

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prompt injection is the most critical vulnerability in deployed AI agents. Despite recent progress, we show that the prevailing defense paradigm (data-instruction separation) both fails to detect attacks that operate through contextual manipulation and degrades contextually appropriate behavior. We then recast prompt injection via the lens of Contextual Integrity (CI), a privacy theory that judges information flow compliance with contextual norms. This explains types of attacks that current defenses attempt to patch and predict advanced ones future agents will face. We develop unique benign and attack scenarios that force an agent to violate the norms by (1) misrepresenting the flow, (2) manipulating norms, or (3) mixing multiple flows. This reframing suggests an impossibility result: an adversary can always construct a context under which a blocked flow appears legitimate, or a defender who tightens norms will block genuinely legitimate flows. Our findings suggest that current research addresses a shrinking fraction of future attack surfaces. Instead, through CI, we offer a principled framework for evaluating context-sensitive failures, and designing CI-aware alignment for the frontier autonomous agents.

</details>

### 55. Agent Security is a Systems Problem

📄 [arXiv](https://arxiv.org/abs/2605.18991) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`survey`、`agent security`、`systems security`、`prompt injection`、`untrusted component`
- 🎯 **研究动机**：社区主流致力于提升模型鲁棒性，但仅靠模型鲁棒性不足以保障 agent 安全。
- 🔬 **研究方法**：提出 agent 安全应作为系统问题的立场——驱动 agent 的 AI 模型必须被视为不可信组件、安全不变量须在系统层强制执行，并基于操作系统、网络、形式化方法等领域数十年的系统安全研究凝练核心设计原则。
- 📌 **结论**：分析十一个真实 agent 攻击案例说明系统原则若落地本可阻止这些攻击，并识别在 agent 中实现这些原则的研究挑战。

👤 **作者**：Mihai Christodorescu、…、Nishit V. Pandya

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We take the position that agent security must be approached as a systems problem: the AI model powering the agent must be treated as an untrusted component, and security invariants must be enforced at the system level. Through this lens, efforts to increase model robustness (the dominant viewpoint in the community) are insufficient on their own. Instead, we must complement existing efforts with techniques from the systems security domain. Based on our experience as cybersecurity researchers in operating systems, networks, formal methods, and adversarial machine learning, we articulate a set of core principles, grounded in decades of systems security research, that provide a foundation for designing agentic systems with predictable guarantees. As evidence, we analyze eleven representative real-world attacks on agents and discuss how systems principles, if realized, could have prevented these attacks. We also identify the research challenges that stand in the way of implementing these principles in agents.

</details>

### 56. Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale

📄 [arXiv](https://arxiv.org/abs/2605.20744) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`reward hacking`、`verifiable exploitation`、`agent evaluation`、`textarena`
- 🎯 **研究动机**：reward hacking——智能体在评估信号下看似成功却违背预期目标——已在广泛场景被观察到，但主要靠事后检查轨迹来分析，缺乏可靠的规模化测量方法。
- 🔬 **研究方法**：提出把可检测的 reward hacking 机会直接嵌入环境的新评测范式，使其利用行为"设计即可验证"，支持确定性、自动化地测量智能体是否及如何利用漏洞，并在 TextArena 上实例化开源 Hack-Verifiable TextArena。
- 📌 **结论**：借助该测试床系统分析了多样环境与设置下各语言模型的 reward hacking 行为，为可靠测量提供了标准化基础。

👤 **作者**：Amit Roth、Ankur Samanta、Matan Halevy、Yoav Levine、Yonathan Efroni

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Aligning autonomous agents with human intent remains a central challenge in modern AI. A key manifestation of this challenge is reward hacking, whereby agents appear successful under the evaluation signal while violating the intended objective. Reward hacking has been observed across a wide range of settings, yet methods for reliably measuring it at scale remain lacking. In this work, we introduce a new evaluation paradigm for measuring reward hacking. Whereas prior studies have primarily analyzed it post hoc by inspecting agent trajectories, we instead embed detectable reward hacking opportunities directly into environments. This makes their exploitation verifiable by design, enabling deterministic and automated measurement of whether and how agents exploit such vulnerabilities. We instantiate this approach in $\textit{TextArena}$ and release $\textit{Hack-Verifiable TextArena}$, a testbed in which reward hacking can be measured reliably. Using this benchmark, we analyze reward hacking behavior across language models in diverse environments and settings. We open source the code at https://github.com/MajoRoth/hack-verifiable-environments/.

</details>

### 57. Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning

📄 [arXiv](https://arxiv.org/abs/2605.24216) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`detection`、`agent monitoring`、`theory of mind`、`covert malicious behavior`、`learning to monitor`
- 🎯 **研究动机**：自主 LLM agent 的隐蔽恶意行为具延迟、上下文依赖与长程特征，现有监控独立处理单条轨迹、不利用既往监控经验，也不显式推理 agent 信念与意图以区分良性执行与隐蔽偏离。
- 🔬 **研究方法**：Agent-ToM 以 Theory-of-Mind 推理做全轨迹结构化分析（推断信念、校准置信的意图假设、预期动作与行为基线偏离），推理时用 Reason-Verify-Refine 管线，训练时将批评信号蒸馏为可跨轮复用的 semantic guardrail memory。
- 📌 **结论**：在 SHADE-Arena 与 CUA-SHADE-Arena 上取得强 precision-recall 平衡，仅用两段调用推理管线即超越含 ensemble 在内的 SOTA 监控基线。

👤 **作者**：Nesreen K. Ahmed、Nima Nafisi

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Monitoring autonomous large language model (LLM) agents for covert malicious behavior is challenging due to delayed, context-dependent, and long-horizon attack patterns. Agents may pursue hidden objectives while maintaining superficially benign behavior, making detection difficult even with full trajectory access. Prior monitoring approaches improve scaffolding or ensemble aggregation, but treat each trajectory independently and do not learn from prior monitoring experience. Moreover, standard reasoning methods explain observed behavior without explicitly reasoning about agent beliefs, intentions, and goal alignment required to distinguish benign task execution from covert deviation. We propose \textbf{Agent-ToM}, a learning-to-monitor framework grounded in Theory-of-Mind (ToM) reasoning for security analysis of autonomous agents. Agent-ToM performs structured full-trajectory analysis by inferring beliefs, intent hypotheses with calibrated confidence, expected actions, and deviations from task-consistent behavioral baselines. At inference time, it employs a \textit{Reason-Verify-Refine} pipeline to construct and validate monitoring decisions. At training time, Agent-ToM distills critique signals into a persistent \textit{semantic guardrail memory}, enabling reusable belief- and intent-conditioned constraints across episodes. We evaluate Agent-ToM on adversarial agent monitoring benchmarks (SHADE-Arena and CUA-SHADE-Arena). Agent-ToM achieves strong precision-recall balance and outperforms state-of-the-art monitoring baselines, including ensemble methods, while using a coherent two-call reasoning pipeline. These results demonstrate that learning at the monitoring layer, combined with structured ToM reasoning and verification, provides an effective and deployable foundation for securing autonomous LLM agents.

</details>

### 58. JobBench: Aligning Agent Work With Human Will

📄 [arXiv](https://arxiv.org/abs/2605.26329) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`occupational agent`、`human delegation`、`rubric grading`、`privacy`、`utility`
- 🎯 **研究动机**：现有职业 AI agent 基准以经济价值划定范围、讲述替代故事，而未评估专家认为最值得委派、真正增强人类的工作流程。
- 🔬 **研究方法**：JobBench 覆盖 35 个职业的 130 个 agentic 任务，每任务打包为异构参考文件的工作区以模拟真实专业工作信息流，输出由平均 35.6 条二元判据的 fact-anchored rubric 链评分。
- 📌 **结论**：评测 36 个模型，最强的 Claude Opus 4.7（Claude Code 下）也仅达 45.9%，提示应把目标从替代人类转向做人类真正想委派之事的增强型 agent。

👤 **作者**：Yuetai Li、…、Radha Poovendran

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current benchmarks for occupational AI agents are scoped primarily by economic values, telling a replacement story. We introduce JobBench, which evaluates AI agents on the workflows that experts identify as high-priority for delegation, empowering humans based on their needs instead of replacing them with GDP value. JobBench covers 130 agentic tasks across 35 occupations. Each task is packaged as a workspace of heterogeneous reference files, requiring the agent to reason through the cluttered information streams of real professional work. Outputs are graded by a fact-anchored chain of rubrics, averaging 35.6 binary criteria per task. We evaluate 36 models; the strongest, Claude Opus~4.7 under Claude Code, reaches only 45.9 %. We hope JobBench shifts the community's target labour-market effect from replacement to enhancement: building agents that do what humans actually want delegated, not only what is most economically valuable.

</details>

### 59. The Best-Laid SCHEMEs: Coordinated Sabotage and Monitoring in Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2605.29178) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`multi-agent sabotage`、`coordinated attack`、`monitoring`、`agent safety`
- 🎯 **研究动机**：智能体编码系统把任务拆分给多个模型实例，但这些实例能否协同实现隐蔽恶意目标同时不破坏正常任务缺乏严格评测。
- 🔬 **研究方法**：提出 SCHEME 基准，17 个任务实例覆盖 7 类设置与 8 个真实开源库，每个设置要求任一智能体子集都无法单独成功，必须分解共享破坏计划、在不同通信拓扑下传递部分需求并执行相互一致的编辑。
- 📌 **结论**：协同破坏已具实用性——Gemini 3.1 Pro 在 84% 样本、Codex 在 46% 样本中完成隐蔽目标且正常任务成功；但可信监控仅凭代码编辑即以 FPR≤2% 检出 99%/68%（Gemini/Codex）的企图，加上智能体通信后达 100%/81%，全可见监控下未被检出的破坏保持 <3%。

👤 **作者**：Nikolay Radev、Lennart Haas、Benjamin Arnav、Pablo Bernabeu-Pérez

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As agentic coding systems decompose work across multiple model instances, a critical safety question is whether those instances can coordinate to achieve a hidden malicious objective while remaining aligned with user intent. We introduce SCHEME, a benchmark of 17 task instances across 7 settings and 8 real open-source libraries, each pairing a legitimate software-engineering task with a covert side task. Every setting is designed so that no proper subset of agents can succeed alone: agents must decompose a shared sabotage plan, relay partial requirements under different communication topologies, and execute mutually consistent edits, testing genuine multi-agent coordination rather than individual capability. Evaluating with GPT 5.1 Codex and Gemini 3.1 Pro, we find coordinated sabotage is already practical, with Gemini completing the covert objective while succeeding on the legitimate task in 84\% of samples and Codex in 46\%. A failure analysis shows that recovery, not failure incidence, drives the model gap: both models suffer similar numbers of communication failures per trajectory, but Gemini recovers from $\sim$73\% of occurrences against Codex's $\sim$56\%. However, the agents' code edits remain detectable: a trusted monitor flags coordinated sabotage at FPR$\le$2\% in 99\%/68\% (Gemini/Codex) of attempts from code edits alone, rising to 100\%/81\% with access to agent communication. Despite stealth-aware prompting, undetected sabotage stays at $<$3\% under the full-visibility monitor; telling agents a monitor is present halves Gemini's sabotage success without significantly breaking detection, even when agents are explicitly prompted to fabricate cover stories.

</details>

### 60. MCPHunt: An Evaluation Framework for Cross-Boundary Data Propagation in Multi-Server MCP Agents

📄 [arXiv](https://arxiv.org/abs/2604.27819) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-04　🏷 NeurIPS 2026

**关键词**：`benchmark`、`mcp`、`information flow`、`credential propagation`、`multi-server agent`
- 🎯 **研究动机**：多 server MCP agent 中忠实的工具组合可把各自无害的读写权限变成跨信任边界凭证传播——这是工作流拓扑的结构性副作用而非恶意模型行为，此前未被受控隔离研究。
- 🔬 **研究方法**：构建首个隔离非对抗、逐字凭证跨 MCP 信任边界传播的受控 benchmark，采用把传播检测归约为字符串匹配的 canary 污点追踪、risky/benign/hard-negative 环境受控覆盖设计、以及区分任务要求传播与违规传播的 CRS 分层。
- 📌 **结论**：5 个模型 3615 条主基准轨迹（147 任务、9 机制族）中违规传播率达 11.5-41.3%，通路特异性达 25 倍且集中于浏览器中介数据流；prompt 缓解最多降 97% 违规传播并保留 80.5% 效用，但效果随指令跟随能力而变。

👤 **作者**：Haonan Li、Tianjun Sun、Yongqing Wang、Qisheng Zhang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-server MCP agents create an information-flow control problem: faithful tool composition can turn individually benign read/write permissions into cross-boundary credential propagation -- a structural side effect of workflow topology, not necessarily malicious model behavior. We present MCPHunt, to our knowledge the first controlled benchmark that isolates non-adversarial, verbatim credential propagation across multi-server MCP trust boundaries, with three methodological contributions: (1) canary-based taint tracking that reduces propagation detection to objective string matching; (2) an environment-controlled coverage design with risky, benign, and hard-negative conditions that validates pipeline soundness and controls for credential-format confounds; (3) CRS stratification that disentangles task-mandated propagation (faithful execution of verbatim-transfer instructions) from policy-violating propagation (credentials included despite the option to redact). Across 3,615 main-benchmark traces from 5 models spanning 147 tasks and 9 mechanism families, policy-violating propagation rates reach 11.5--41.3% across all models. This propagation is pathway-specific (25x cross-mechanism range) and concentrated in browser-mediated data flows; hard-negative controls provide evidence that production-format credentials are not necessary -- prompt-directed cross-boundary data flow is sufficient. A prompt-mitigation study across 3 models reduces policy-violating propagation by up to 97% while preserving 80.5% utility, but effectiveness varies with instruction-following capability -- suggesting that prompt-level defenses alone may not suffice. Code, traces, and labeling pipeline are released under MIT and CC BY 4.0.

</details>

### 61. Measuring AI Agents' Progress on Multi-Step Cyber Attack Scenarios

📄 [arXiv](https://arxiv.org/abs/2603.11214) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`evaluation`、`ai agent`、`cyber-attack capability`、`inference-time compute`
- 🎯 **研究动机**：需要专用多步攻击场景来严格衡量前沿 AI 模型自主网络攻击能力的演进趋势
- 🔬 **研究方法**：构建两个专用 cyber range（32 步企业网络攻击链与 7 步工控系统攻击），在 18 个月内发布的 7 个模型上按不同推理时算力预算比较长动作序列下异构能力的串联表现
- 📌 **结论**：性能随推理算力对数线性增长且无平台期（10M 增至 100M token 提升最高 59%）；固定 10M token 下企业网场景平均完成步数从 1.7（GPT-4o）升至 9.8（Opus 4.6），最佳单次完成 22/32 步

👤 **作者**：Linus Folkerts、…、Jessica Wang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We evaluate the autonomous cyber-attack capabilities of frontier AI models on two purpose-built cyber ranges-a 32-step corporate network attack and a 7-step industrial control system attack-that require chaining heterogeneous capabilities across extended action sequences. By comparing seven models released over an eighteen-month period (August 2024 to February 2026) at varying inference-time compute budgets, we observe two capability trends. First, model performance scales log-linearly with inference-time compute, with no observed plateau-increasing from 10M to 100M tokens yields gains of up to 59%, requiring no specific technical sophistication from the operator. Second, each successive model generation outperforms its predecessor at fixed token budgets: on the corporate network range, average steps completed at 10M tokens rose from 1.7 (GPT-4o, August 2024) to 9.8 (Opus 4.6, February 2026). The best single run completed 22 of 32 steps, corresponding to roughly 6 of the estimated 14 hours a human expert would need. On the industrial control system range, performance remains limited, though the most recent models are the first to reliably complete steps, averaging 1.2-1.4 of 7 (max 3).

</details>

### 62. Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks

📄 [arXiv](https://arxiv.org/abs/2602.20156) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`benchmark`、`prompt injection`、`agent skill`、`supply chain`
- 🎯 **研究动机**：LLM agent 的 skill 功能引入第三方代码、知识与指令，形成日益复杂的 agent 供应链，为 prompt injection 提供了未经评估的新攻击面
- 🔬 **研究方法**：提出 SkillInject 基准，含 202 个注入-任务对，覆盖从明显恶意到藏于合法指令中的隐蔽上下文相关攻击，并同时度量安全性（避免有害指令）与实用性（遵从合法指令）
- 📌 **结论**：当前 agent 高度脆弱，前沿模型攻击成功率最高达 80%，可执行数据外泄、破坏性操作乃至勒索行为，且模型规模化或简单输入过滤均无法解决，需要上下文感知授权框架

👤 **作者**：David Schmotz、Luca Beurer-Kellner、Sahar Abdelnabi、Maksym Andriushchenko

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents are evolving rapidly, powered by code execution, tools, and the recently introduced agent skills feature. Skills allow users to extend LLM applications with specialized third-party code, knowledge, and instructions. Although this can extend agent capabilities to new domains, it creates an increasingly complex agent supply chain, offering new surfaces for prompt injection attacks. We identify skill-based prompt injection as a significant threat and introduce SkillInject, a benchmark evaluating the susceptibility of widely-used LLM agents to injections through skill files. SkillInject contains 202 injection-task pairs with attacks ranging from obviously malicious injections to subtle, context-dependent attacks hidden in otherwise legitimate instructions. We evaluate frontier LLMs on SkillInject, measuring both security in terms of harmful instruction avoidance and utility in terms of legitimate instruction compliance. Our results show that today's agents are highly vulnerable with up to 80% attack success rate with frontier models, often executing extremely harmful instructions including data exfiltration, destructive action, and ransomware-like behavior. They furthermore suggest that this problem will not be solved through model scaling or simple input filtering, but that robust agent security will require context-aware authorization frameworks. Our benchmark is available at https://www.skill-inject.com/.

</details>

### 63. CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents

📄 [arXiv](https://arxiv.org/abs/2601.09923) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-01　🏷 NeurIPS 2026

**关键词**：`defense`、`computer use agent`、`prompt injection`、`single-shot planning`、`control flow integrity`
- 🎯 **研究动机**：架构隔离对 prompt 注入提供最强保证，但 CUA 需持续观察 UI 状态来决定动作，与安全所需隔离存在根本张力。
- 🔬 **研究方法**：利用 UI 工作流虽动态但结构可预测的特性，让可信 planner 一次性发出覆盖所有预期运行时状态的完整分支计划以获得对任意指令注入的控制流完整性保证，并引入 NOVA 在组合爆炸的 UI 状态空间中调用感知模型解析运行时值。
- 📌 **结论**：在 OSWorld 上保留前沿模型最高 57% 性能并使较小开源模型提升至多 19%，证明严格安全与效用可共存；但预先规划防不住欺骗感知模型将执行路由到攻击者偏好分支的 Branch Steering 攻击。

👤 **作者**：Hanna Foerster、…、Yiren Zhao

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents are vulnerable to prompt injection attacks, where malicious content hijacks agent behavior. Among proposed defenses, architectural isolation provides the strongest guarantees by strictly separating trusted task planning from untrusted environment observations. However, applying this design to Computer Use Agents (CUAs), which automate tasks by viewing screens and executing actions, presents a fundamental challenge. Current agents require continuous observation of UI state to determine each action, which conflicts with the isolation required for security. We resolve this tension by demonstrating that UI workflows, while dynamic, are structurally predictable. Single-shot planning, where a trusted planner emits upfront a complete branching plan covering all anticipated runtime states, provides control flow integrity guarantees against arbitrary instruction injections. We introduce NOVA (Navigating via Observation, Verification, and Action) to make this viable in the combinatorially large UI state space, where the plan can invoke a perception model to resolve runtime values such as UI coordinates. We evaluate our design on OSWorld, and retain up to 57% of the performance of frontier models while improving performance for smaller open-source models by up to 19%, demonstrating that rigorous security and utility can coexist in CUAs. Although upfront planning prevents instruction injections, we show that additional measures are needed to defend against \textbf{Branch Steering} attacks, where adversaries deceive the perception model into routing execution down attacker-preferred branches of the plan, such as redirecting the agent to a malicious website.

</details>

### 64. MCP-Atlas: A Large-Scale Benchmark for Tool-Use Competency with Real MCP Servers

📄 [arXiv](https://arxiv.org/abs/2602.00933) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-01　🏷 NeurIPS 2026

**关键词**：`benchmark`、`mcp`、`tool use`、`llm agent`、`claim-level scoring`
- 🎯 **研究动机**：现有 MCP 评估在真实多步跨 server 工作流、非 mock 的真实 MCP server 覆盖、以及与 agent 冗长风格解耦的结构化可复现评分三个轴上均有不足。
- 🔬 **研究方法**：构建 MCP-Atlas，含 1000 个人工撰写验证任务、覆盖 36 个真实 MCP server 与 220 个工具，prompt 不指明 server/工具/参数，用 claim 级 rubric 对工具输出锚定的原子事实判分，并配 11 类诊断分类学。
- 📌 **结论**：20 个前沿模型在 0.75 claim 覆盖阈值下 pass rate 最高 82.2% 并呈清晰三层结构，63.3% 已诊断失败为认知性而非工具调用问题，多个高性能模型在工具执行成功后因过早停止或错误合成而失败。

👤 **作者**：Chaithanya Bandi、…、Bing Liu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The Model Context Protocol (MCP) is emerging as a standard interface through which large language model (LLM) agents discover and invoke external tools. However, existing MCP evaluations fall short along three key axes: realistic multi-step workflows with cross-server orchestration, breadth across authentic MCP servers rather than mocks, and structured, reproducible claim-level scoring disentangled from agent verbosity or style. We introduce MCP-Atlas, a benchmark for measuring tool-use competency against production MCP servers. MCP-Atlas contains 1,000 natural-language tasks written and verified by human experts spanning 36 real MCP servers and 220 tools. Prompts do not specify servers, tools, or parameters, requiring agents to identify relevant tools among semantically plausible distractors and to compose multi-step, cross-server workflows. Each task is scored with a claim-level rubric, where final answers are scored against atomic factual claims grounded in tool outputs. This answer-centric scoring permits valid alternative tool-call trajectories to receive credit. We pair this with an 11-category diagnostic taxonomy that disentangles tool-call failures from cognitive failures in task understanding, synthesis, parsing, and stopping. Evaluating 20 frontier models from six providers under matched task-level conditions, we find pass rates up to 82.2% at a 0.75 claim coverage threshold and a clear three-tier performance structure. Automated diagnostics show that 63.3% of diagnosed failures are cognitive rather than tool-call related. Notably, several high-performing models fail after successful tool execution due to premature stopping or incorrect synthesis. We release the task schema, containerized harness, claim evaluator, and a 500-task public split, while reserving a 500-task private split to preserve leaderboard integrity. The code is at https://github.com/scaleapi/mcp-atlas.

</details>

### 65. DECEIVE-AFC: Adversarial Claim Attacks against Search-Enabled LLM-based Fact-Checking Systems

📄 [arXiv](https://arxiv.org/abs/2602.02569) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-01　🏷 NeurIPS 2026

**关键词**：`attack`、`fact-checking`、`llm agent`、`claim attack`、`input-only threat model`
- 🎯 **研究动机**：带搜索的 LLM 事实核查系统对对抗攻击的鲁棒性认识不足，在现实 input-only 威胁模型下的脆弱性未被系统研究。
- 🔬 **研究方法**：提出 DECEIVE-AFC agent 对抗攻击框架，整合 claim 级攻击策略与对抗 claim 有效性评估原则，在无需证据源或模型内部访问下扰乱搜索行为、证据检索与 LLM 推理。
- 📌 **结论**：在基准数据与真实系统上将验证准确率从 78.7% 降至 53.7%，显著超越现有 claim 级攻击基线且具强跨系统迁移性。

👤 **作者**：Haoran Ou、…、Kwok-Yan Lam

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fact-checking systems with search-enabled large language models (LLMs) have shown strong potential for verifying claims by dynamically retrieving external evidence. However, the robustness of such systems against adversarial attack remains insufficiently understood. In this work, we study adversarial claim attacks against search-enabled LLM-based fact-checking systems under a realistic input-only threat model. We propose DECEIVE-AFC, an agent-based adversarial attack framework that integrates novel claim-level attack strategies and adversarial claim validity evaluation principles. DECEIVE-AFC systematically explores adversarial attack trajectories that disrupt search behavior, evidence retrieval, and LLM-based reasoning without relying on access to evidence sources or model internals. Extensive evaluations on benchmark datasets and real-world systems demonstrate that our attacks substantially degrade verification performance, reducing accuracy from 78.7% to 53.7%, and significantly outperform existing claim-based attack baselines with strong cross-system transferability.

</details>

### 66. To trust or not to trust: Attention-based Trust Management for LLM Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2506.02546) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-06　🏷 NeurIPS 2026

**关键词**：`defense`、`trust management`、`multi-agent systems`、`attention`、`robustness`
- 🎯 **研究动机**：LLM 多智能体系统中智能体平等对待所有消息而不评估可信度，且现有工作只关注单一危害类型、缺乏多维度整体分析。
- 🔬 **研究方法**：借鉴人类沟通理论（Grice）给出含六个正交信任维度的可信度综合定义，提出基于注意力的轻量消息可信度评分 A-Trust，并构建支持消息级与智能体级评估的信任管理系统（TMS）。
- 📌 **结论**：跨多样多智能体设置与任务的实验表明，该 TMS 显著提升系统对恶意输入的鲁棒性。

👤 **作者**：Pengfei He、…、Qi He

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model-based Multi-Agent Systems (LLM-MAS) have demonstrated strong capabilities in solving complex tasks but remain vulnerable when agents receive unreliable messages. This vulnerability stems from a fundamental gap: LLM agents treat all incoming messages equally without evaluating their trustworthiness. While some existing studies approach trustworthiness, they focus on a single type of harmfulness rather than analyze it in a holistic approach from multiple trustworthiness perspectives. We address this gap by proposing a comprehensive definition of trustworthiness inspired by human communication theory (Grice, 1975). Our definition identifies six orthogonal trust dimensions that provide interpretable measures of trustworthiness. Building on this definition, we introduce the Attention Trust Score (A -Trust), a lightweight, attention-based method for evaluating the trustworthiness of messages. We then develop a principled trust management system (TMS) for LLM -MAS that supports both message-level and agent-level trust assessments. Experiments across diverse multi-agent settings and tasks demonstrate that our TMS significantly improves robustness against malicious inputs.

</details>

**尚未挂出 arXiv（待核验）**
- AM-Bench: A Unified Taxonomy and Evaluation Suite for Agentic Misalignment
- Agent MechSuits: Mechanistic Subspace Safety Steering for Multi-Turn CLI Agents
- ChainForge: Tool-Chain Hijacking Attacks against LLM Agents via Execution-Grounded Tool Synthesis
- MCPHallu: Benchmarking Reasoning, Execution, and Memory Hallucinations in MCP Agents
- Cross-User Poisoning: User-Task Boundary Failures in Multi-User Collaborative Language Agents
- Asynchronous Agentic Poisoning
- Forgetting is Not Always Bad: A Neuro-Inspired Memory Repair Mechanism for Poisoned LLM Agents
- Harmless in Pieces, Harmful in Motion: Detecting Multi-Agent Jailbreaks
- FlowLeak: Coverage-Guided Extraction of Dynamic Workflows in LLM-Based Multi-Agent Systems
- Leaderboard Hacking: Preference-Based Model Evaluations are Vulnerable to Manipulation
- Reasoning Poisoning: Utilizing Social-Engineering to Steer Chain-of-Thought
- MetaPI: Constructing Prompt Injection Benchmarks from Any Agent Benchmarks
- EnvTrap: Revealing the Environment-Only Attack Surface in Embodied AI via Consequence-Blind Action Execution
- Soteria: Formally Verified Planning with Runtime Enforcement for Safe LLM Agents
- Runtime Verification of Multiple Natural Language Criteria for Agent Governance
- EV-AUDIT: A Co-Evolutionary Auditing Framework for Task Hijacking in Multi-Agent Systems
- Swarm Shepherd: Securing Multi-Agent Ecosystems Against Persistent Latent Compromise
- DIBench: Benchmarking Decision Integrity of GUI-based Mobile Agents Under Deceptive Injections
- LPS-Bench: Benchmarking Safety Awareness of Computer-Use Agents in Long-Horizon Planning
- MMA-SafetyBench: A Benchmark for Multimodal Agent Safety Evaluation
- Safe Actions Can Form Unsafe Traces: Benchmarking and Shielding Compositional Emergent Risk in AI Agents
- Behavioral Probes for Information Flow in LLM Swarms
- MLLMs Fail to Refuse when Using Tools Agentically
- Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage?
- Auditing Sabotage Bench: Detecting and Fixing Research Sabotage in ML Codebases
- CyberDualEval: Measuring Dual-Use Cyber Risks in Frontier Language Models
- KaliBench: Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux
- PROTEUS: A Self-Evolving Red Team with Surface Expansion for Agent Skill Ecosystems
- Synthetic Web: Benchmarking Language Agents under Adversarial Search Ranking
- The Web Doesn't Sit Still: Adversarial Self-Evolving Attacks on Search Agents
- Chatter Attack: Resource Consumption Attack for Large Language Models
- Bits Beat Tokens: A Regret Rate Distortion Theory for LLM Agents

### 扩散语言模型安全（DLM 线）

### 67. Why Jailbreaks Succeed in Diffusion Language Models: An Energy Landscape Analysis（已库内，0928）

📄 [arXiv](https://arxiv.org/abs/2609.30841) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`analysis`、`diffusion language model`、`jailbreak`、`energy landscape`、`training-free detection`
- 🎯 **研究动机**：dLLM 的现有攻防各自针对特定漏洞，缺乏解释越狱为何成功的统一框架。
- 🔬 **研究方法**：将安全对齐建模为去噪能量景观塑形，把越狱归纳为初始时掩盖查询安全倾向或中途强行跨越能量壁垒两类策略，并据此导出 step-0 ratio 与两个轨迹速度信号共三个免训练检测信号。
- 📌 **结论**：在 LLaDA-8B、LLaDA-1.5、Dream-7B 与 LLaDA-MoE-7B 四个 dLLM 上验证信号互补性，压力测试中所有逃过检测的攻击配置同样无法产出有害内容。

👤 **作者**：Thong Bach、Dung Nguyen、Thao Minh Le、Truyen Tran

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing attacks and defenses for diffusion-based large language models (dLLMs) target specific vulnerabilities but lack a shared framework explaining why attacks succeed. We propose one by interpreting safety alignment as shaping the denoising energy landscape: a well-aligned model routes harmful queries toward safe outputs through an energy barrier that separates the two regions. Current jailbreak attacks reduce to two strategies for circumventing this barrier: obscuring the query's safety disposition at initialisation, or intervening mid-trajectory to force the denoising path across the energy barrier. From this perspective and the result that masked diffusion models minimise kinetic energy during denoising, we derive three complementary, training-free detection signals: a step-0 ratio that reads the initial safety disposition from the logit distribution before generation begins, and two trajectory-velocity signals that track kinetic energy in complementary subspaces of the logit space. An attack must either reveal its intent at initialisation or expend kinetic energy to cross the barrier in at least one monitored subspace, so the three signals cover each other's blind spots in the energy budget by construction. Evaluation across three dense dLLMs (LLaDA-8B, LLaDA-1.5, Dream-7B) and a sparse mixture-of-experts dLLM (LLaDA-MoE-7B) confirms this complementarity. In stress tests of known attacks, every configuration that evades detection also fails to produce harmful content, suggesting that the detection and barrier-crossing thresholds are hard to separate.

</details>

### 68. Weak Ties, Strong Signals: Efficient Training Data Detection in Diffusion LLMs via Independent Token Sampling（已库内，0929）

📄 [arXiv](https://arxiv.org/abs/2609.22145) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-08　🏷 NeurIPS 2026

**关键词**：`detection`、`membership inference`、`diffusion llm`、`mutual information`、`query efficiency`
- 🎯 **研究动机**：dLLM 缺乏因果架构的单遍概率分解，现有随机掩码方法无法控制被掩 token 间依赖，其 token 级近似引入由累积条件互信息刻画、非负的结构性估计误差，掩盖细微记忆信号。
- 🔬 **研究方法**：提出 Independent Token Sampling（ITS），用注意力导出的成对依赖代理近似 CMI 感知的选择准则以挑选内部依赖弱的掩码集，并加入多样性促进策略提升跨轮 token 覆盖。
- 📌 **结论**：在多个模型与数据集上一致超越 SOTA 基线，ArXiv 数据集上 AUC 提升 0.18，且在有限查询预算下仍保持强劲性能。

👤 **作者**：Hongyao Yu、…、Shu-Tao Xia

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion large language models (dLLMs) offer a compelling alternative to autoregressive models, yet they may expose sensitive training data during denoising. Detecting such usage is challenging because dLLMs lack the efficient one-pass probability decomposition of causal architectures. Existing methods rely on random masking to obtain tractable token-wise detection signals under limited query budgets, but fail to control dependencies among masked tokens. We demonstrate that this token-wise approximation introduces a non-negative structural estimation error, which is theoretically characterized by the cumulative conditional mutual information (CMI) among masked tokens and can obscure subtle memorization signals. This insight suggests that reliable detection requires masked token sets with weak internal dependency. To avoid the prohibitive cost of directly estimating CMI over token combinations, we propose \textit{Independent Token Sampling} (ITS), a query-efficient framework that uses an attention-derived pairwise dependency proxy to approximate the CMI-aware selection criterion. ITS further incorporates a diversity-promoting strategy to improve token coverage across sampling rounds, yielding aggregated token-wise signals that are less affected by dependency-induced approximation error. Experiments on multiple datasets show that ITS consistently outperforms state-of-the-art baselines across different models and datasets, achieving an AUC improvement of 0.18 on the ArXiv dataset while maintaining strong performance under limited query budgets. The code is available at https://github.com/Chrisqcwx/DLLM-MIA .

</details>

### 69. MaskForge: Structure-Aware Adaptive Attacks for Jailbreaking Diffusion Large Language Models（已库内 dllm-security #4）

📄 [arXiv](https://arxiv.org/abs/2606.04027) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`attack`、`jailbreak`、`diffusion llm`、`adaptive attack`、`infilling`
- 🎯 **研究动机**：dLLM 以置信度而非位置提交 token、掩码是原生输入，有害内容可经 infilling 在受监控前缀之外注入，而现有越狱要么忽略该能力、要么依赖低多样性掩码模板且缺乏结构适配与经验积累。
- 🔬 **研究方法**：MaskForge 将 dLLM 红队建模为对可增长结构模式库的全黑盒优化搜索：把成功尝试抽象为可复用 schema、用 UCB bandit 选取与目标兼容的模式、失败时打分器引导回退，成功经验再蒸馏回库。
- 📌 **结论**：在 5 个公开 dLLM 与 3 个基准上平均攻击成功率 79.3%（较最强基线相对提升 17.6%），成熟模式库零更新迁移到 AdvBench 达 88.2%（相对提升 67%）。

👤 **作者**：Yingzi Ma、Zhengyue Zhao、Xiaogeng Liu、Minhui Xue、Yue Zhao、Chaowei Xiao

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion large language models (dLLMs) generate text by iteratively denoising partially masked sequences under bidirectional context, exposing a safety surface distinct from autoregressive LLMs. Because mask tokens are native inputs and tokens are committed by confidence rather than position, harmful content can be induced through infilling and outside the monitored prefix. Existing jailbreaks either miss this native infill capability or rely on low-diversity mask-bearing templates applied uniformly across goals, with little structural adaptation or accumulated attack experience. We propose MaskForge, a fully black-box adaptive attack that casts dLLM red-teaming as optimized search over a growing library of structural patterns. MaskForge abstracts successful attempts into reusable schemas, selects goal-compatible patterns with a UCB bandit, and invokes a scorer-guided fallback when the current library fails. Successful attempts are distilled back into the pattern library, enabling experience to accumulate across goals. Across five public dLLMs and three benchmarks, MaskForge achieves an average attack success rate of 79.3%, a 17.6% relative improvement over the strongest competing dLLM baseline. The matured pattern library further transfers to AdvBench without any updates, achieving a 88.2% attack success rate and a 67% relative improvement over the strongest competing baseline.

</details>

### 70. Extracting Training Data from Diffusion Language Models via Infilling（已库内 dllm-security #24）

📄 [arXiv](https://arxiv.org/abs/2605.24173) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`attack`、`training data extraction`、`diffusion language model`、`infilling`、`memorization`
- 🎯 **研究动机**：LLM 记忆研究几乎都采用前缀条件提取，而 DLM 能对任意位置的掩码 token 去噪，仅靠前缀探测只揭示记忆的一个侧面并显著低估训练数据被提取的风险。
- 🔬 **研究方法**：提出以任意二值掩码参数化的 infilling extraction 协议，涵盖前缀探测并匹配 DLM 的双向归纳偏置，在 LLaDA-8B 与 Dream-7B 上跨 5 种提取模式、3 种训练管线、3 个语料评估 verbatim 与部分泄漏。
- 📌 **结论**：掩码几何主导可提取性——边缘条件掩码提取的逐字序列最多达前缀条件的 3 倍，攻击者从 DLM 提取被脱敏邮箱的 recall 甚至高于同规模自回归模型，解码参数可测地影响提取且后续 SFT 不消除既有记忆。

👤 **作者**：Yihan Wang、N. Asokan

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Memorization in large language models has been studied almost exclusively through prefix-conditioned extraction, a natural choice for autoregressive models. However, diffusion language models (DLMs) can denoise masked tokens at arbitrary positions. Thus, prefix-only probing reveals only one facet of memorization in DLMs and significantly underestimates the risk of training-data extraction. In order to realistically model extractability of training data in DLMs, we introduce \emph{infilling extraction}, a data-extraction protocol parameterized by an arbitrary binary mask that subsumes prefix-only probing and accounts for the bidirectional inductive bias of DLMs. Instantiating it on LLaDA-8B and Dream-7B across five extraction modes, three training pipelines, and three corpora covering verbatim and partial leakage, we find that mask geometry governs extractability: edge-conditioned masks \emph{extract up to three times more} verbatim sequences than prefix-conditioned ones, and bidirectional access opens channels inaccessible in autoregressive models. In particular, we show that a realistic adversary with access to training data where personally identifiable information has been redacted, can even achieve higher recall on extracting redacted email addresses from DLMs than from scale-matched autoregressive models. Tunable parameters for decoding measurably affect extraction performance, while a follow-up supervised finetuning stage does not eliminate the prior memorization.

</details>

### 71. Characterizing Memorization in Diffusion Language Models: Generalized Extraction and Sampling Effects

📄 [arXiv](https://arxiv.org/abs/2603.02333) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`analysis`、`diffusion language model`、`memorization`、`pii leakage`、`sampling resolution`
- 🎯 **研究动机**：自回归模型已被证明会记忆并逐字复现训练数据，而作为竞争替代方案的扩散语言模型因生成动力学根本不同，其记忆行为基本未被探索。
- 🔬 **研究方法**：提出统一 prefix-conditioned decoding 与任意掩码模式和随机采样轨迹下扩散生成的广义概率提取框架，理论上建立采样分辨率与记忆的单调关系，并跨模型规模与采样策略实验验证。
- 📌 **结论**：提高采样分辨率严格增大精确提取训练数据的概率（自回归解码是分辨率取极大的极限情形），且在对齐的 prefix 条件评估下 DLM 的 PII 记忆泄露显著低于 ARM。

👤 **作者**：Xiaoyu Luo、Wenrui Yu、Qiongxiu Li、Johannes Bjerva

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autoregressive language models (ARMs) have been shown to memorize and occasionally reproduce training data verbatim, raising concerns about privacy and copyright liability. Diffusion language models (DLMs) have recently emerged as a competitive alternative, yet their memorization behavior remains largely unexplored due to fundamental differences in generation dynamics. To address this gap, we present a systematic theoretical and empirical characterization of memorization in DLMs. We propose a generalized probabilistic extraction framework that unifies prefix-conditioned decoding and diffusion-based generation under arbitrary masking patterns and stochastic sampling trajectories. Theorem 4.3 establishes a monotonic relationship between sampling resolution and memorization: increasing resolution strictly increases the probability of exact training data extraction, implying that autoregressive decoding corresponds to a limiting case of diffusion-based generation by setting the sampling resolution maximal. Extensive experiments across model scales and sampling strategies validate our theoretical predictions. Under aligned prefix-conditioned evaluations, we further demonstrate that DLMs exhibit substantially lower memorization-based leakage of personally identifiable information (PII) compared to ARMs.

</details>

### 72. Confidence-Based Decoding is Provably Efficient for Diffusion Language Models

📄 [arXiv](https://arxiv.org/abs/2603.22248) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`analysis`、`diffusion language model`、`confidence-based decoding`、`sampling efficiency`
- 🎯 **研究动机**：DLM 中解码策略决定每轮 unmask 的顺序与数量、直接影响采样效率，confidence-based 方法实证表现强但一直缺乏理论分析
- 🔬 **研究方法**：建立首个 confidence-based decoding 理论框架，聚焦每轮持续 unmask 直至累计熵超过阈值的 entropy sum 策略，证明其达到 KL 散度 ε-accurate 采样所需期望迭代数为 Õ(H(X₀)/ε)
- 📌 **结论**：当数据分布熵相对序列长度较低时可获得显著采样加速，且该策略无需先验知识或超参调节即自适应数据内在复杂度

👤 **作者**：Changxiao Cai、Gen Li

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion language models (DLMs) have emerged as a promising alternative to autoregressive (AR) models for language modeling, allowing flexible generation order and parallel generation of multiple tokens. However, this flexibility introduces a challenge absent in AR models: the \emph{decoding strategy} -- which determines the order and number of tokens generated at each iteration -- critically affects sampling efficiency. Among decoding strategies explored in practice, confidence-based methods, which adaptively select which and how many tokens to unmask based on prediction confidence, have shown strong empirical performance. Despite this success, our theoretical understanding of confidence-based decoding remains limited. In this work, we develop the first theoretical analysis framework for confidence-based decoding in DLMs. We focus on an entropy sum-based strategy that continues unmasking tokens within each iteration until the cumulative entropy exceeds a threshold, and show that it achieves $\varepsilon$-accurate sampling in KL divergence with an expected number of iterations $\widetilde O(H(X_0)/\varepsilon)$, where $H(X_0)$ denotes the entropy of the target data distribution. Notably, this strategy yields substantial sampling acceleration when the data distribution has low entropy relative to the sequence length, while automatically adapting to the intrinsic complexity of data without requiring prior knowledge or hyperparameter tuning. Overall, our results provide a theoretical foundation for confidence-based decoding and may inform the design of more efficient decoding strategies for DLMs.

</details>

### 73. Theoretical Analysis of Why Masked Diffusion Models Mitigate the Reversal Curse

📄 [arXiv](https://arxiv.org/abs/2602.02133) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`analysis`、`masked diffusion model`、`reversal curse`、`positional encoding`
- 🎯 **研究动机**：掩码扩散语言模型对 reversal curse 的缓解远弱于 AR 模型，但流行的 any-order 掩码训练解释无法说明训练中单一位置配置的证据为何迁移到反向 prompt
- 🔬 **研究方法**：给出理论分析——共享 Transformer 参数存储 token 对证据、相对位置编码仅经 query/key 路由注意力而不改变 value 侧证据，并在单层 MDM 中证明前向掩码训练强化反向查询可复用的证据、诱导相关的前向-反向注意路由并产生一阶降低反向损失的共享存储梯度分量
- 📌 **结论**：受控单层实验与大规模 LLaDA/Dream 实验证实上述特征并转化为更好的反向预测

👤 **作者**：Moongyu Jeon、Sangwoo Shin、BumJun Kim、Kyelim Lee、Albert No

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autoregressive language models (ARMs) suffer from the reversal curse: after learning ''$A$ is $B$,'' they often fail on the reverse query ''$B$ is $A$.'' Masked diffusion language models (MDMs) exhibit this failure in a much weaker form, but the underlying reason has remained unclear. A common explanation attributes this mitigation to their any-order masked training objective. However, observing ''$[\mathbf{M}]$ is $B$'' during training teaches recovery of $A$ from $B$ in one positional configuration, and does not by itself explain why the learned evidence should transfer to the reverse prompt ''$B$ is $[\mathbf{M}]$.'' We provide a theoretical analysis showing that this transfer arises from a parameter-level coupling between forward and reverse positional conditionals: shared Transformer parameters store token-pair evidence, while relative positional encodings route attention through queries and keys without changing the value-side evidence being retrieved. In a one-layer MDM, we prove that forward masked training strengthens evidence that is reusable in reverse queries, induces correlated forward--reverse attention routes, and yields a positively aligned shared-storage gradient component that decreases the reverse loss to first order. Controlled one-layer experiments and large-scale LLaDA/Dream experiments verify these signatures and show that they translate into improved reverse prediction.

</details>

### 74. Diffusion LLMs are Natural Adversaries for any LLM（已库内 dllm-security #3 同族）

📄 [arXiv](https://arxiv.org/abs/2511.00203) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-10　🏷 NeurIPS 2026

**关键词**：`attack`、`jailbreak`、`diffusion llm`、`amortized prompt optimization`、`transferability`
- 🎯 **研究动机**：对每个样本做离散对抗提示优化资源开销高昂，难以规模化生成越狱提示。
- 🔬 **研究方法**：利用 Diffusion LLM 建模提示-响应对的联合分布、天然可作提示搜索代理，直接条件生成对抗提示，把逐实例优化摊销为少量可并行采样，并给出所需采样数的概率分析。
- 📌 **结论**：生成的提示是低困惑度、多样的越狱，对包括鲁棒训练与专有模型在内的广泛黑盒目标具有强迁移性，温和保真假设下仅需少量条件采样即可恢复高奖励（有害）提示。

👤 **作者**：David Lüdke、Tom Wollschläger、Paul Ungermann、Stephan Günnemann、Leo Schwinn

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce a novel framework that transforms the resource-intensive (adversarial) prompt optimization problem into an \emph{efficient, amortized inference task}. Our core insight is that pretrained, non-autoregressive generative LLMs, such as Diffusion LLMs, which model the joint distribution over prompt-response pairs, can serve as powerful surrogates for prompt search. This approach enables the direct conditional generation of prompts, effectively replacing costly, per-instance discrete optimization with a small number of parallelizable samples. We provide a probabilistic analysis demonstrating that under mild fidelity assumptions, only a few conditional samples are required to recover high-reward (harmful) prompts. Empirically, we find that the generated prompts are low-perplexity, diverse jailbreaks that exhibit strong transferability to a wide range of black-box target models, including robustly trained and proprietary LLMs. Beyond adversarial prompting, our framework opens new directions for red teaming, automated prompt optimization, and leveraging emerging Flow- and Diffusion-based LLMs.

</details>

**尚未挂出 arXiv（待核验）**
- Beyond the Prompt: Leveraging Pre-Decoding States for Jailbreak Detection in dLLMs（已库内 dllm-security #8）
- Machine Unlearning in Diffusion LLMs
- Diffusion-Time Concept Manifolds: Sparse Autoencoder Groups for Interpreting Denoising Language Models
- CURE: Counterfactual Unsafe-token Re-masking for Diffusion Large Language Model Test-time Alignment
- Diffusion Models Can Approximate Optimal Infilling Lengths Implicitly（解码行为分析，DLM DoS 相关）

### 投毒、后门与供应链

### 75. FloatDoor: Platform-triggered Backdoors in LLMs

📄 [arXiv](https://arxiv.org/abs/2606.19535) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`attack`、`backdoor`、`platform-triggered`、`lora`、`supply chain`
- 🎯 **研究动机**：同一模型因非结合浮点运算与内核实现差异在不同部署平台上产生可测输出差异，该平台依赖变异性加上模型审计与部署服务之间的时间差构成未被研究的攻击面。
- 🔬 **研究方法**：提出首个输入无关、平台触发的生成式 LLM 后门 FloatDoor，用两个轻量 LoRA 适配器分别放大跨平台数值分歧、再把所得平台签名绑定到恶意下游任务。
- 📌 **结论**：在 Qwen3-4B 上跨 NVIDIA GPU、Google TPU、AWS Graviton 与倚天 710 等部署目标触发，整体效用基本不变，并能在指定平台可靠诱导可利用代码漏洞。

👤 **作者**：Nils Loose、Jonas Sander、Felix Mächtle、Thomas Eisenbarth

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed in sensitive settings such as software engineering, where their outputs directly shape downstream artifacts. Recent work has shown that an identical model can produce measurably different outputs depending on the deployment platform, a consequence of non-associative floating-point arithmetic and divergent kernel implementations. We study the security implications of this platform-dependent variability and uncover a novel attack surface on LLM deployments. We introduce FloatDoor, the first input-independent, platform-triggered backdoor attack against generative LLMs. The compromised model exhibits adversary-chosen behavior when served on a target platform and is otherwise benign. FloatDoor is realized through two lightweight LoRA adapters, one that amplifies inter-platform numerical divergence and one that binds the resulting platform signature to a malicious downstream task, while leaving aggregate model utility largely intact. FloatDoor exploits a pronounced time-of-check, time-of-use gap between model auditing and serving. We demonstrate FloatDoor on Qwen3-4B across a broad range of deployment targets, including NVIDIA GPUs, Google TPUs, AWS Graviton, and Alibaba Yitian-710. As a final case study, we show that FloatDoor reliably induces exploitable code vulnerabilities on a chosen target platform. Our results establish a new class of attacks on LLM deployments and underscore the pressing need for trusted model supply chains in sensitive, LLM-powered applications.

</details>

### 76. Rethinking Molecular Graph Backdoors under Chemistry-aware Admission

📄 [arXiv](https://arxiv.org/abs/2606.23361) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`attack`、`backdoor`、`molecular graph`、`chemistry-aware admission`、`gnn`
- 🎯 **研究动机**：分子图后门通常以抽象图编辑评估，但真实分子学习管线的记录须先通过解析、消毒、规范化与图串一致性检查才能入训，这一被忽视的 admission 阶段对攻击有效性的影响未知。
- 🔬 **研究方法**：将 admission 形式化为 ChemGuard 操作协议（分子串可消毒且由其重构的图与提交图一致才放行），并提出 admission 感知的 ChemBack 攻击——构造化学可行的 motif-anchor 附着并按对干净目标类分子的 Tanimoto 指纹相似度排序候选，全程无需 victim 模型、代理 GNN、梯度或训练代码访问。
- 📌 **结论**：ChemGuard 使许多现有图后门因化学无效或表征不一致而大幅失效，但 ChemBack 以完全通过 admission 的毒化实现高攻击成功并保持干净精度，说明化学感知 admission 之外仍需进一步防御。

👤 **作者**：Thinh T. H. Nguyen、Sze Jue Yang、Khoa D. Doan、Chee Seng Chan、Kok-Seng Wong

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks on molecular graph neural networks (GNNs) are typically evaluated as abstract graph edits, but real molecular learning pipelines do not train on arbitrary graphs. Molecular records must first survive parsing, sanitization, canonicalization, and graph-string consistency checks. We formalize this overlooked admission stage as ChemGuard, an operational protocol for testing whether a submitted molecular record can enter a realistic learning pipeline, while complementing existing defenses. ChemGuard admits a record only when its molecular string is sanitizable and the graph reconstructed from that string matches the submitted molecular graph. Under this operational view, many existing graph-based backdoors lose much of their apparent efficacy because their poisons are chemically invalid or representation-inconsistent. We then show that admission checks alone are insufficient to rule out molecular backdoors. We propose ChemBack, an admission-aware molecular backdoor attack that constructs chemically feasible motif-anchor attachments and ranks admitted candidates by fingerprint-based Tanimoto similarity to clean target-class molecules. ChemBack is model-free during trigger selection, using molecular structures, target labels, fingerprints, and public validity checks, but no victim model, surrogate GNN, learned embedding, gradient, logit, or training-code access. Across molecular benchmarks, validators, architectures, and defenses, \textbf{ChemBack} achieves high attack success with fully admitted poisons while preserving clean accuracy. Our results reveal a two-sided lesson, chemistry-aware admission suppresses many graph-only backdoors, yet chemically valid and target-aligned molecular backdoors remain a practical threat.

</details>

### 77. The Platonic Defense: Backdoor Defense for Self-Supervised Encoders in the Era of Large Scale Pre-training

📄 [arXiv](https://arxiv.org/abs/2606.29451) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`defense`、`backdoor`、`self-supervised learning`、`energy model`、`test-time purification`
- 🎯 **研究动机**：SSL 预训练编码器易受后门攻击，现有防御在完全黑盒设定下往往需要标签、攻击模式或训练数据访问而难以奏效。
- 🔬 **研究方法**：受 Platonic Representation Hypothesis 启发提出 Platonic Representation Defense，在源表征与参考表征上定义条件能量函数，用噪声对比估计做检测、去噪分数匹配做表征净化。
- 📌 **结论**：该攻击/模型/模态无关的黑盒测试时防御在多个 SSL 编码器和 10 余种攻击上同时完成表征检测与净化，取得显著性能提升。

👤 **作者**：Tuo Chen、Minjing Dong、Benlei Cui、Jian Liu、Jie Gui

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-supervised learning (SSL) pretrained models have become a dominant paradigm for visual representation learning, but they are vulnerable to backdoor attacks. Existing defenses struggle to defend against such attacks in a fully black-box setting because they often require access to labels, attack patterns, or training data. To tackle this issue, we propose a new attack-agnostic, model-agnostic, and modality-agnostic black-box test-time defense paradigm, called \emph{Platonic Representation Defense}. It is inspired by the Platonic Representation Hypothesis, which suggests that large-scale independently trained encoders converge toward compatible projections of the same underlying reality. We formalize this idea as a conditional energy function defined over source representations and a set of reference representations. The energy function is trained for detection through noise-contrastive estimation and for representation purification through denoising score matching. Theoretically, the energy gap between matched and mismatched samples is lower bounded by the mutual information between source and reference representations. We demonstrate the effectiveness of our method on multiple self-supervised encoders and more than 10 attacks. The method can perform both representation detection and purification, and achieves substantial performance gains across multiple attacks. Code is available \href{https://github.com/jsrdcht/Platonic-Representation-Defense}{here}.

</details>

### 78. Token by Token, Compromised: Backdoor Vulnerabilities in Unified Autoregressive Models

📄 [arXiv](https://arxiv.org/abs/2605.19227) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`attack`、`backdoor`、`unified autoregressive model`、`multimodal generation`、`poisoning`
- 🎯 **研究动机**：统一自回归模型（UAM）以共享参数与多模态词表在单次自回归中生成文本与图像 token，其统一架构是否引入多模态后门这类新脆弱性尚属空白。
- 🔬 **研究方法**：提出首个针对 UAM 的后门攻击 ToBAC，覆盖数据投毒与模型修改两种策略，将无害字符乃至常见词转化为可跨多个输出模态传播恶意效果的触发器。
- 📌 **结论**：有模型访问时在 Liquid 上一个常见词（如 cool）即可在 55% 的生成中诱导模态对齐的品牌推广或意识形态影响，无模型访问时数据投毒对 JanusPro 平均成功率 63.1%。

👤 **作者**：Tobias Braun、Jonas Henry Grebe、Hossein Shakibania、Anna Rohrbach、Marcus Rohrbach

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unified autoregressive models (UAMs) are transformer models that generate text as well as image tokens within a single autoregressive pass. Shared parameters and a multimodal vocabulary simplify the training pipeline and facilitate flexible multimodal generation, yet might introduce new vulnerabilities. In particular, we are the first to show that this unified architecture enables multimodal backdoor attacks, where a trigger can propagate malicious effects across multiple output modalities. Specifically, we present the Token by Token Backdoor Attack (ToBAC), the first backdoor attack targeting UAMs, exploring both data-based and model-based poisoning strategies. We demonstrate that innocuous characters or even common words can be transformed into triggers that elicit harmful behavior in autoregressive image generation. ToBAC can jointly manipulate visual outputs and accompanying text, increasing the perceived authenticity of fabricated content. With model access, ToBAC enables attacks on the unified Liquid model in which a subtle word (e.g., ``cool'') induces modality-aligned brand promotion or ideological influence in 55% of generations. Without model access, ToBAC can be induced through data poisoning, achieving an average success rate of 63.1% against JanusPro.

</details>

### 79. Combating Data Laundering in LLM Training

📄 [arXiv](https://arxiv.org/abs/2604.01904) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-04　🏷 NeurIPS 2026

**关键词**：`detection`、`data laundering`、`unauthorized training`、`memorization signal`、`auditing`
- 🎯 **研究动机**：未授权训练数据检测假设以原始专有数据查询目标 LLM，但在数据洗钱（语义保持的风格/结构变换）下训练暴露发生在变换形态上，记忆信号不再出现在原文，标准检测器依赖的信号分离崩塌。
- 🔬 **研究方法**：提出 Synthesis Data Reversion（SDR），借助辅助 LLM 以"变换目标+细粒度细节"抽象约束无限的自然语言变换空间，迭代细化细节以合成出能激发更强目标模型检测信号的类训练查询。
- 📌 **结论**：在 MIMIR 基准上针对多样洗钱手段与 Pythia、Llama2、Falcon 三个模型族一致恢复检测信号，提供实用的数据洗钱审计层。

👤 **作者**：Muxing Li、Zesheng Ye、Sharon Li、Feng Liu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Post-hoc unauthorized-training data detection for large language models (LLMs) typically assumes a query-with-originals regime: rights holders query a target LLM with raw proprietary data and assess whether the model assigns them stronger memorization-based detection signals, e.g., higher confidence or lower loss, than held-out non-training reference texts. We show that this regime becomes brittle under data laundering, where the target LLM is trained on semantics-preserving but stylistically or structurally transformed surrogates of proprietary data to obfuscate provenance. Since training-time exposure occurs in the laundered form, memorization signals may no longer appear on the originals, collapsing the candidate-reference signal separation that standard detectors rely on. We counter this threat by studying laundering-aware detection with raw proprietary data, a held-out reference corpus, and query access to the target LLM, while the laundering transformation is undisclosed. Since exact recovery of the laundered corpus is infeasible, we infer a detection-useful synthesis process via an auxiliary LLM that maps originals into training-like queries. To make this search tractable, we introduce Synthesis Data Reversion (SDR), which constrains the unbounded space of natural-language transformations through a goal-details abstraction: a high-level transformation goal, e.g., "lyrical rewriting", and fine-grained details, e.g., "with vivid imagery". SDR identifies the most likely goal and iteratively refines details so synthesized queries elicit stronger target-model detection signals. Evaluated on the MIMIR benchmark against diverse laundering practices and target LLM families (Pythia, Llama2, and Falcon), SDR consistently restores detection signals, offering a practical auditing layer against data laundering.

</details>

### 80. Hallucinated Positive Entanglement for Backdoor Attacks in Federated Self-Supervised Learning

📄 [arXiv](https://arxiv.org/abs/2602.02147) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`attack`、`backdoor`、`federated self-supervised learning`、`hallucinated positive entanglement`、`feature entanglement`
- 🎯 **研究动机**：FSSL 在不共享原始无标注数据协同训练表示模型的同时易受后门攻击，而现有 FSSL 后门攻击存在中毒样本利用率低、迁移性有限与持久性弱的局限。
- 🔬 **研究方法**：提出 HPE——先用幻觉合成正样本增强编码器对后门特征的嵌入，再以特征纠缠让触发器与后门样本在表示空间紧密绑定，最后借选择性参数投毒与邻近感知更新把中毒模型约束在全局模型附近以提升稳定性与持久性。
- 📌 **结论**：在多个 FSSL 场景与数据集上，HPE 的性能显著超越已有后门攻击方法，并在多种防御机制下保持强鲁棒性。

👤 **作者**：Jiayao Wang、…、Dongfang Zhao

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Federated self-supervised learning (FSSL) enables collaborative training of self-supervised representation models without sharing raw unlabeled data. While it serves as a crucial paradigm for privacy-preserving learning, its security remains vulnerable to backdoor attacks, where malicious clients manipulate local training to inject targeted backdoors. Existing FSSL attack methods, however, often suffer from low utilization of poisoned samples, limited transferability, and weak persistence. To address these limitations, we propose a new backdoor attack method for FSSL, namely Hallucinated Positive Entanglement (HPE). HPE first employs hallucination-based augmentation using synthetic positive samples to enhance the encoder's embedding of backdoor features. It then introduces feature entanglement to enforce tight binding between triggers and backdoor samples in the representation space. Finally, selective parameter poisoning and proximity-aware updates constrain the poisoned model within the vicinity of the global model, enhancing its stability and persistence. Experimental results on several FSSL scenarios and datasets show that HPE significantly outperforms existing backdoor attack methods in performance and exhibits strong robustness under various defense mechanisms.

</details>

### 81. Phantom Transfer: Data Poisoning can Survive Data-Level Defences

📄 [arXiv](https://arxiv.org/abs/2602.04899) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`attack`、`data poisoning`、`subliminal learning`、`data-level defense`、`existence proof`
- 🎯 **研究动机**：提出一个根本性问题——即便精确知道毒化样本如何被植入良性数据集，数据级防御也可能无法将其滤除，需要检验最大权限防御对复杂投毒的失效可能。
- 🔬 **研究方法**：把 subliminal learning 改造到真实场景构造 Phantom Transfer 投毒，使攻击不依赖产出数据的模型、在其上训练的模型与攻击目标，并刻画攻击最有效的条件、演示植入密码触发行为。
- 📌 **结论**：攻击在全部 11 种被测数据级防御（含逐样本被另一模型改写的防御）下存活，构成"最大权限数据级防御可失效"的存在性证明。

👤 **作者**：Andrew Draganov、Tolga H. Dur、Anandmayi Bhongade、Mary Phuong

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present a data poisoning attack -- Phantom Transfer -- with the property that, even if you know precisely how the poison was placed into an otherwise benign dataset, you cannot filter it out. We achieve this by modifying subliminal learning to work in real-world contexts and demonstrate that the attack works regardless of which model produced the data, which model is trained on the data or what the attack target is. Furthermore, the attack survives 11 tested data-level defences, including one where every sample is paraphrased by another model. We characterise when this attack works best and show that it can be used to plant password-triggered behaviours into models while still beating defences. In short, we provide an existence proof that maximum-affordance defences can fail to stop sophisticated data poisoning attacks. We suggest that future defences should be supplemented with white-box methods and post-training model audits.

</details>

### 82. Half-Truths Break Similarity-Based Retrieval

📄 [arXiv](https://arxiv.org/abs/2602.23906) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`analysis`、`dual encoder`、`half-truth`、`compositional reasoning`
- 🎯 **研究动机**：CLIP 式双编码器常违反直觉——在正确描述上追加貌似合理但错误的对象或关系反而提高图文相似度（half-truths），威胁基于相似度的检索
- 🔬 **研究方法**：将漏洞归因于对比训练只对齐整句 caption 而未显式接地个体实体与关系，提出 CS-CLIP——把 caption 分解为实体/关系单元、为每单元构造最小编辑 foil，微调模型使正确单元得分高于 foil 且保留标准双编码器推理
- 📌 **结论**：COCO 上 CLIP 仅 40.6% 的时间偏好正确短描述（细节为关系时降至 32.9%），CS-CLIP 将 half-truth 准确率提升至 69.3%，并在既有组合性基准上平均提升 5.7 点

👤 **作者**：Bora Kargi、Arnas Uselis、Seong Joon Oh

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When a text description is extended with an additional detail, image-text similarity should drop if that detail is wrong. We show that CLIP-style dual encoders often violate this intuition: appending a plausible but incorrect object or relation to an otherwise correct description can increase the similarity score. We call such cases half-truths. On COCO, CLIP prefers the correct shorter description only 40.6% of the time, and performance drops to 32.9% when the added detail is a relation. We trace this vulnerability to weak supervision on caption parts: contrastive training aligns full sentences but does not explicitly enforce that individual entities and relations are grounded. We propose CS-CLIP (Component-Supervised CLIP), which decomposes captions into entity and relation units, constructs a minimally edited foil for each unit, and fine-tunes the model to score the correct unit above its foil while preserving standard dual-encoder inference. CS-CLIP raises half-truth accuracy to 69.3% and improves average performance on established compositional benchmarks by 5.7 points, suggesting that reducing half-truth errors aligns with broader gains in compositional understanding. Code is publicly available at: https://github.com/kargibora/CS-CLIP

</details>

### 83. Catch-Only-One: Non-Transferable Examples for Model-Specific Authorization

📄 [arXiv](https://arxiv.org/abs/2510.10982) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-10　🏷 NeurIPS 2026

**关键词**：`defense`、`non-transferable examples`、`model-specific authorization`、`low-sensitivity subspace`、`training-free`
- 🎯 **研究动机**：AI 法规日益强调目的限制，但已发布数据可被喂给任意模型，现有数据扰动或重训练方法既防不住未知或外部训练的模型、又依赖对训练部署的控制。
- 🔬 **研究方法**：提出 non-transferable examples（NTE），以 training-free、data-agnostic 方式在模型特定低敏感子空间内重编码数据，形成仅指定模型可解码的任务级"密文"，并建立授权保真与未授权退化的形式化界。
- 📌 **结论**：授权的视觉与视觉语言模型在常见预处理下性能保持，未授权模型因子空间错位而崩溃（即使面对自适应重构攻击），未授权退化随可测谱错位度扩展。

👤 **作者**：Zihan Wang、…、Guangdong Bai

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent AI regulations increasingly emphasize the need for mechanisms that preserve the utility of data for AI innovation while preventing misuse, particularly by enforcing purpose limitation in downstream AI applications. In practice, enforcing this principle remains challenging, as released data can be trivially fed into arbitrary models beyond its declared intent. Existing approaches attempt to mitigate this risk by either perturbing data or retraining models to limit unintended use. These strategies, however, offer no protection against inference by unknown or externally trained models, or fundamentally rely on control over the training or deployment. In this work, we introduce non-transferable examples (NTEs), recoded data that act as a task-level "ciphertext" decodable only by a designated model. Whereas adversarial examples exploit directions of high model sensitivity, NTEs leverage the complementary insensitive subspace. We propose a training-free, data-agnostic method that recodes data within a model-specific low-sensitivity subspace, preserving outputs for the authorized model while degrading unauthorized ones through subspace misalignment. We establish formal bounds certifying authorized-model fidelity and showing that unauthorized degradation scales with measurable spectral misalignment between models. Empirically, NTEs preserve performance across diverse vision backbones and state-of-the-art vision-language models under common preprocessing, while unauthorized models collapse even under adaptive reconstruction attacks. These results establish NTEs as a practical means to preserve intended data utility while preventing unauthorized exploitation. Our project is available at https://trusted-system-lab.github.io/model-specificity

</details>

**尚未挂出 arXiv（待核验）**
- Backdoor Attacks Rerouted: BatchNorm as a Sink for Adversarial Signals
- Backdoor Attacks under Lossy Compression: From Failure to Reactivation and Adaptation
- Backdoor Channels Hidden in Latent Space: Cryptographic Undetectability in Modern Neural Networks
- Backdoor Purification for LoRA-Tuned LLMs via Null-Space Projection
- A Theoretical Analysis of Backdoor Learning as Simplicity-Biased Optimization Dynamics
- Benign Reinforcement Learning Can Amplify Latent Backdoors
- Clean Data Can Still Carry Backdoors: Support-Persistent Backdoors for Model Reuse
- Clean-Label Poisoning for Gradient-Boosted Decision Trees
- Poison-then-Hide: Finetuning-Activated Backdoor Attack on Pretrained Vision Encoders
- ShadowFPT: Backdooring Federated Prompt Tuning via Shadow Triggers
- VOID: Backdoor Injection through Knowledge Vacuity in Federated Unlearning
- Not Suppressing or Purifying: Backdoor Containment via Expert Quarantine and Shutdown in LLMs
- DetectViT: Test-time Backdoor Detection for Vision Transformers via Inter-Head Attention Discrepancy
- CSO-LLM: Post-Training Backdoor Detection and Trigger Inversion in LLMs
- Trapping Attacker in Dilemma: Defending GNN Backdoors
- Training-Based Backdoors Are Not Cryptographic
- Weird Generalization from Narrow Finetuning: Persona Shifts and Inductive Backdoors
- When Sanitization Becomes the Trigger: Defense-Triggered Backdoor Attacks
- Information Blackhole: Backdoor Mechanism in 3D Point Cloud Reconstruction（已库内，0929）
- Gradient-Mine Units: Scorched-Earth Strategy for Model Protection against Unauthorized Fine-Tuning
- ASAP: Fast Adaptive Sliding Agnostic Poisoning Attack on Federated Learning
- Adversarial Corpus Selection to Attack Subgraph Matching based Graph Retrieval

### 隐私、成员推断与 unlearning

### 84. Subliminal Learning as Trait-Direction Drift: A Mechanism and Targeted Control under SFT Distillation

📄 [arXiv](https://arxiv.org/abs/2609.01091) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`analysis`、`subliminal learning`、`trait-direction drift`、`sft distillation`、`corridor regularization`
- 🎯 **研究动机**：蒸馏可从 teacher 迁移隐藏特质（subliminal learning），但该信号如何在训练中累积并产生行为迁移的机制不明，难以针对性缓解。
- 🔬 **研究方法**：提出并验证 trait-direction drift 机制——teacher 偏好造成数据中可测偏好差、SFT 中诱发特质对齐更新并累积为行为迁移；据此提出 probe-space corridor regularization 在蒸馏中约束沿校准特质方向的漂移。
- 📌 **结论**：偏好差、训练轨迹与干预三方面证据支持该机制；corridor regularization 将恶意响应迁移从 29.55% 降至 6.45% 且主任务精度损失低，并在 Qwen 主设置中持续抑制动物偏好迁移。

👤 **作者**：Zhixuan Liu、Zhichen Dong、Yuyu Fan、Xiangtian Li、Chao Yang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Beyond intended capabilities, model distillation can transfer hidden traits from a teacher. A teacher biased by a system prompt can generate semantically clean training data, such as numeric sequences, that still causes a downstream student to inherit the hidden preference, a phenomenon known as subliminal learning. Prior work has identified several parts of this process. How the signal builds up during training and produces behavioral transfer remains unclear, making targeted mitigation difficult. We propose and validate trait-direction drift as a mechanism for subliminal learning: biased generation creates measurable preference gaps in teacher data, and student-recognizable gaps induce trait-aligned updates during supervised fine-tuning that accumulate into behavioral transfer. Guided by this mechanism, we propose probe-space corridor regularization, a targeted defense that constrains drift along a calibrated trait direction during distillation. The method substantially reduces hidden-trait transfer, preserving task performance: for example, it lowers malicious-response transfer from 29.55% to 6.45% with low main-task accuracy cost, and consistently suppresses animal-preference transfer across the main Qwen setting. The preference-gap, training-trajectory, and intervention evidence links subliminal learning to trait-direction drift and motivates corridor regularization as a targeted control during distillation.

</details>

### 85. Leaky Students: Membership Inference against On-Policy Distillation（已库内，0929）

📄 [arXiv](https://arxiv.org/abs/2609.33136) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`attack`、`membership inference`、`on-policy distillation`、`privacy leakage`、`auroc`
- 🎯 **研究动机**：OPD 中教师训练可接触敏感特权数据，学生是否泄漏教师在蒸馏中所用记录的成员信息此前缺乏系统研究，且固定参考答案损失会漏掉新鲜学生轨迹中的稀疏成员信号。
- 🔬 **研究方法**：提出 Leaky——从目标模型采样新鲜轨迹，将其 token 对数概率与未含候选记录训练的匹配参考模型上的最大值比较，对差值施加 Leaky ReLU 以保留正间隙、下调负间隙，作为对非成员偶然正间隙的近似校正。
- 📌 **结论**：在覆盖数学、医疗问答与代码生成的 15 个目标上平均 AUROC 达 0.875，而主评测中最强基线仅 0.614（同一批采样轨迹上为 0.826）。

👤 **作者**：Zhexi Lu、Mingzhi Zhu、Stacy Patterson、Lei Yu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

On-policy distillation (OPD) trains a student to match a teacher's next-token distributions on student-generated trajectories. However, privileged information supplied to the teacher for OPD training may contain sensitive data. Whether the student leaks private information about the records supplied to the teacher during distillation remains poorly understood. To the best of our knowledge, we present the first systematic study of membership inference in this setting. We find that fresh student trajectories expose sparse membership signals that fixed reference-answer losses often miss. These signals are mixed with probability changes caused by training on other records. We introduce Leaky, which samples fresh trajectories from the target model and compares its token log-probabilities with the maximum across matched reference models trained without the candidate records. It applies Leaky ReLU to the resulting gaps, preserving positive gaps and downweighting negative gaps as an approximate correction for incidental positive gaps in non-members. Across fifteen targets spanning mathematics, medical question answering, and code generation, Leaky outperforms all evaluated baselines and achieves mean AUROC 0.875, compared with 0.614 for the strongest baseline on each target in the main evaluation. On the same sampled trajectories, the strongest baseline achieves mean AUROC 0.826. These results show that students trained through OPD can expose the membership of records used for teacher supervision, even when fixed reference-answer losses provide little evidence of membership.

</details>

### 86. Near-Duplicate Families Break Exact-Record Membership Inference（已库内，0929）

📄 [arXiv](https://arxiv.org/abs/2609.33909) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`analysis`、`membership inference`、`near-duplicate`、`copyright auditing`、`false attribution`
- 🎯 **研究动机**：成员推断被用作数据溯源与版权审计证据，但 web 级数据天然含近重复家族（联合发布文章、镜像页、轻改图像），标准干净参考审计无法区分"精确记录被训练"与"家族成员被训练"。
- 🔬 **研究方法**：提出四世界审计，独立操控精确记录是否包含与家族是否存在两类状态以分离该混淆，并通过受控干预分析学习目标的影响。
- 📌 **结论**：CC-News 上干净参考 LiRA 在 1.00% 误报率下将 99.70% 的"家族存在但精确记录未训练"样本错标为成员；分类任务中家族近乎完全替代精确记录使精确推断降至近随机。

👤 **作者**：Yiyong Liu、Jiayang Liu、Yixin Tan、Lu Sun、Rui Wen

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership inference (MI) asks whether a specific record appeared in a model's training set and is increasingly used as evidence for data provenance and copyright auditing. These applications require determining whether the exact queried record was used for training, rather than merely whether the model was exposed to similar content. Making this distinction is challenging because web-scale datasets naturally contain near-duplicates, including syndicated articles, mirrored pages, and lightly modified images. We show that this creates a fundamental confound for standard MI. A clean-reference audit typically calibrates membership against a null in which neither the queried record nor its near-duplicate family is present. In deployment, however, the queried record may be absent while a non-identical family member was used for training. We introduce a four-world audit that independently varies exact-record inclusion and family presence to separate these cases. Natural near-duplicate families cause severe false attribution. On CC-News, a clean-reference LiRA auditor labels 99.70% of family-present exact non-members as members at 1.00% false-positive rate. This failure persists across alternative scores, model architectures, and executed deduplication and retraining. Controlled interventions further reveal that the effect depends on the learning objective. In classification, faithful families largely substitute for the exact record, reducing exact-given-family inference to near chance. In autoregressive language modeling, the exact sequence retains a detectable residual, while family presence still confounds clean-reference decisions. These results show that positive model-only membership evidence may establish family-level exposure without establishing exact-record provenance.

</details>

### 87. What to Remember, What to Reveal: Privacy-Aware Memory for Conversational Agents

📄 [arXiv](https://arxiv.org/abs/2608.16551) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-08　🏷 NeurIPS 2026

**关键词**：`defense`、`privacy`、`conversational memory`、`pii`、`personalization`
- 🎯 **研究动机**：个性化对话智能体的长期记忆主要为效用优化而存储复用用户信息，忽视 PII 等隐私属性被不必要暴露的风险，而简单删除敏感值又会损害效用，隐私保护须治理敏感值的完整生命周期。
- 🔬 **研究方法**：提出 SP-Mem 隐私感知记忆架构，把记忆效用与精确隐私值暴露解耦——从原始输入识别并分离敏感信息、在隔离结构中分别存储脱敏内容与精确隐私值、按任务需求与用户同意选择性检索，并配套联合评测响应质量、隐私行为与推理成本的基准。
- 📌 **结论**：跨多个 LLM 智能体的实验表明，SP-Mem 在减少不必要隐私暴露的同时实现更强的个性化。

👤 **作者**：Wenjie Wang、Wenhe Si、Xinyue Xu、Yue Xu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Long-term memory enables personalized conversational agents to retain user information across sessions. However, existing memory architectures primarily optimize for utility while neglecting the risks of unnecessarily storing and reusing private attributes such as personally identifiable information (PII). Addressing privacy risks in personalized memory is challenging because simply removing sensitive values can undermine system utility. Therefore, privacy protection for memory agents should govern the full life cycle of sensitive values rather than only sanitizing individual records. To address this gap, we introduce Sanitized Privacy-Mapped Memory (SP-Mem), a privacy-aware memory architecture that decouples memory utility from exact private-value exposure. SP-Mem provides a full life-cycle privacy design that identifies and separates sensitive information from raw user inputs, stores sanitized content and exact private values in isolated structures, and selectively retrieves private values based on task requirements and user consent. We further introduce a privacy-aware memory benchmark that jointly evaluates response quality, privacy behavior, and inference cost. Extensive experiments across multiple LLM-based agents show that SP-Mem achieves stronger personalization while reducing unnecessary privacy exposure. Code and data are available at https://github.com/Jensassss/SP-Mem.

</details>

### 88. Inadvertent Context Leakage in Language Models

📄 [arXiv](https://arxiv.org/abs/2608.19857) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-08　🏷 NeurIPS 2026

**关键词**：`attack`、`context leakage`、`secret reconstruction`、`black-box attack`、`privacy`
- 🎯 **研究动机**：agent 上下文中存在日历、凭证、健康、财务等敏感信息时，即使模型正确拒绝直接提取，其良性输出是否携带可重建秘密的隐藏相关性、以及对手能否主动放大该效应，均未知。
- 🔬 **研究方法**：研究被动泄露与主动 prompt 工程两种情形，用仅需底层模型黑盒访问的新型自适应攻击，把模型当作隐蔽载体从看似无害的文本中提取秘密。
- 📌 **结论**：8 个专有模型上 2 位数上下文秘密以近完美精度重建、4 位数达 82% 精确匹配（全部来自普通非对抗请求的输出），且能力越强泄露越多；可训练分类器从常规输出推断用户记忆语义谓词，RL 训练的攻击者可从生产型 agent 提取完整社会安全号码。

👤 **作者**：Jaiden Fairoze、Neal Mangaokar、Kamalika Chaudhuri、Sanjam Garg、Saeed Mahloujifar

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

For AI agents to be useful beyond simple chat, they must hold sensitive user context such as calendars, credentials, health records, and financial data. We study whether the mere presence of such secrets in a model's context window introduces hidden correlations into the model's benign outputs, allowing reconstruction even when the model correctly refuses direct extraction. We further study whether an adversary can actively engineer prompts that amplify this effect, using the model as a covert carrier to transmit secrets through seemingly innocuous text. In both cases, this limited leakage is exploited using a novel adaptive attack that assumes black-box access to the underlying model. In controlled experiments across eight proprietary models, we find that 2-digit in-context secrets are reconstructed with near-perfect accuracy and 4-digit secrets at 82\% exact match, all from outputs the model produces in response to ordinary, non-adversarial requests. We observe that more capable models leak more: stronger instruction-following amplifies sensitivity to in-context secrets, suggesting leakage is a byproduct of capability as opposed to a patchable bug. We show this leakage enables two practical attacks: (1) a trained classifier that infers semantic predicates about user memories (e.g., health conditions, financial events) from routine natural-language outputs, and (2) an RL-trained adversary that extracts full Social Security Numbers from a production-style agent.

</details>

### 89. Learning What to Forget: Improving LLM Unlearning via Learned Token-Level Importance

📄 [arXiv](https://arxiv.org/abs/2606.06320) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`defense`、`llm unlearning`、`token-level importance`、`joint optimization`、`forget-retain tradeoff`
- 🎯 **研究动机**：自回归 LLM 遗忘样本中各 token 与遗忘的相关性不同，现有方法或忽略该异质性或依赖辅助模型、启发式与外部标注来估计 token 相关性。
- 🔬 **研究方法**：以"最小化该 token 的 forget loss 是否与 retain 最优性冲突"定义 token forget-specificity 并形式化为参数与 token 权重的联合优化，提出 ATWU 在遗忘过程中用 hidden states 上的线性 scorer 联合学习两者、无需外部 token 监督。
- 📌 **结论**：在 TOFU 与 RWKU 上取得 SOTA forget-retain 权衡，超越样本级方法、概率启发式与辅助模型方法，且学到的分数与真实 forget-specific span 对齐显著更好。

👤 **作者**：Gizem Yüce、Giorgos Nikolaou、Nicolas Flammarion

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning aims to remove targeted knowledge from a trained model while preserving its general capabilities. For autoregressive language models, not all tokens in a forget sample are equally relevant to forgetting. Existing approaches either ignore this heterogeneity or rely on auxiliary models, heuristics, or external annotations to estimate each token's relevance for forgetting. We instead characterize it through the interaction with the retain objective: a token is forget-specific to the extent that minimizing the forget loss on that token does not conflict with retain optimality. We formalize this perspective as a joint optimization problem over the model parameters and the token weights and show that, under a natural separation condition, the resulting objective recovers the oracle forget-specific token support. Motivated by this formulation, we introduce Alternating Token-Weighted Unlearning (ATWU), a lightweight framework that jointly learns token forget-specificity and model parameters during unlearning using a simple linear scorer over the hidden states, without external token level supervision. Across TOFU and RWKU, ATWU achieves state of the art forget-retain trade-offs, outperforming sample-level methods, probability-based token weighting heuristics, and auxiliary-model-based approaches. Moreover, the learned scores align substantially better with ground truth forget-specific spans, indicating that ATWU identifies semantically meaningful token level forgetting signals. Overall, our results suggest that retain conflict provides an effective criterion for identifying what language models should forget, enabling unsupervised learning of token level forget-specificity directly from model representations with minimal computational overhead.

</details>

### 90. Exposing the Illusion of Erasure in Knowledge Editing for LLMs

📄 [arXiv](https://arxiv.org/abs/2606.23276) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`analysis`、`knowledge editing`、`adversarial elicitation`、`low-rank update`
- 🎯 **研究动机**：知识编辑号称无需重训练即可更新 LLM 特定事实，但被编辑知识常未被真正擦除而持续浮现，其机制与可靠性尚不清楚
- 🔬 **研究方法**：从对抗性诱导视角审视主流 KE 方法并做机制分析，发现低秩更新并非覆盖旧知识而是在表示空间中重新分布，实为降低原事实表达概率的定向抑制
- 📌 **结论**：编辑后的知识位于狭窄且各向异性的损失区域、对扰动高度敏感，易被间接 prompting 与对抗攻击诱导，证明 KE 算法本质上可被绕过

👤 **作者**：Advik Raj Basani、Anshuman Chhabra

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Knowledge Editing (KE) has emerged as a frontier for updating specific facts in LLMs without costly retraining, but its reliability and underlying mechanisms remain poorly understood. In this work, we examine KE from an adversarial elicitation perspective, revealing that edited knowledge is often not fully erased and continues to surface, with consistent failures observed across diverse model architectures. To explain this behavior, we conduct a mechanistic analysis of popular KE methods. We show that low-rank updates do not overwrite existing knowledge but instead redistribute it within the model's representation space. Furthermore, we find that these methods act as targeted suppression mechanisms that reduce the likelihood of expressing original facts, rather than removing them from the model. Analysis of the loss landscape reveals that edited knowledge lies in narrow, anisotropic regions that are highly sensitive to perturbations, making them highly vulnerable to indirect prompting and adversarial attacks. By exposing these profound architectural vulnerabilities, our work proves that KE algorithms are inherently bypassable and motivates a fundamental reevaluation of how we deploy post-hoc updates in several LLM applications.

</details>

### 91. PrivacySIM: Evaluating LLM Simulation of User Privacy Behavior

📄 [arXiv](https://arxiv.org/abs/2605.12147) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`privacy behavior`、`user simulation`、`persona conditioning`、`llm agents`
- 🎯 **研究动机**：LLM 越来越多地被用于模拟人类行为，但其能否模拟个体级的隐私决策缺乏评测。
- 🔬 **研究方法**：提出 PrivacySIM 评测套件，以五项隐私用户研究中 1000 名真实用户的地面真值响应为基准，用人口统计、既往经历、自述隐私态度三类 persona 要素条件化九个前沿模型，度量其响应与用户实际响应的匹配率。
- 📌 **结论**：persona 条件化一致优于无条件模拟，但最强模型准确率仅 40.4%，远未忠实模拟个体隐私决策；自述隐私态度因与实际行为背离未必是最好的预测因子，高 AI/聊天机器人经验而低隐私态度的用户最难模拟。

👤 **作者**：James Flemings、Murali Annavaram

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used to simulate human behavior, but their ability to simulate $individual$ privacy decisions is not well understood. In this paper, we address the problem of evaluating whether a core set of user persona attributes can drive LLMs to simulate individual-level privacy behavior. We introduce PrivacySIM, an evaluation suite that benchmarks LLM simulation of user privacy behavior against the ground-truth responses of 1,000 users. These users are drawn from five published user studies on privacy spanning LLM healthcare consultations, conversational agents, and chatbots. Drawing on these user studies, we hypothesize three persona facets as plausible predictors of privacy decision-making: demographics, previous experiences, and stated privacy attitudes. We condition nine frontier LLMs on subsets of these three facets and measure how often each model's response to a data-sharing scenario matches the user's actual response. Our findings show that (1) privacy persona conditioning consistently improves simulation quality over no-persona conditioning, but even the strongest model (40.4\% accuracy) remains far from faithfully simulating individual privacy decisions. (2) A user's stated privacy attitudes alone may not be the best predictor because they often diverge from the user's actual privacy behavior. (3) Users with high AI/chatbot experience but low stated privacy attitudes are the most challenging to simulate. PrivacySIM is a first step toward understanding and improving the capabilities of LLMs to simulate user privacy decisions. We release PrivacySIM to enable further evaluation of LLM privacy simulation.

</details>

### 92. POLAR-Bench: A Diagnostic Benchmark for Privacy-Utility Trade-offs in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2605.19127) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`privacy policy`、`adversarial probing`、`llm agent`、`privacy-utility tradeoff`
- 🎯 **研究动机**：LLM agent 越来越多接触用户私有数据并代表用户与第三方系统交互，须在第三方对抗探测下稳健遵循用户的分享意图，而现有评估缺位。
- 🔬 **研究方法**：构建 POLAR-Bench，让带隐私政策与任务的可信模型与对抗探测任务相关及受保护属性的第三方模型对话，跨 10 个域、7852 个样本以确定性集合隶属度评分，沿隐私政策维度与攻击策略两条正交轴生成每模型 5×5 诊断面。
- 📌 **结论**：当前前沿模型扣留超 99% 受保护属性，而用户最常本地或私有推理运行的 1-30B 小模型明显更差、最弱者泄露过半，从而精确定位各模型意图遵循的失效点。

👤 **作者**：Qiaoyuan Zheng、Yiqu Yang、Qi Gao、Imanol Schlag

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents increasingly have access to private user data and act on the user's behalf when interacting with third-party systems. The user defines what may and must not be shared, and the agent must robustly follow that intent even when third-party systems behave adversarially. We introduce POLAR-Bench (Policy-aware adversarial Benchmark), in which a trusted model with a privacy policy and a task converses with a third-party model that adversarially probes for both task-relevant and protected attributes. Across 10 domains and 7,852 samples, we score privacy and utility by deterministic set-membership and vary privacy policy dimension and attack strategy along two orthogonal axes, producing a 5 times 5 diagnostic surface per model. Our results reveal a sharp split: current frontier models withhold over 99% of protected attributes, while smaller open-weight models in the 1--30B range, the class users most commonly run as their own trusted agent on-device or via private inference, score notably worse, with the weakest leaking over half. POLAR-Bench thus localizes where each model's intent-following breaks down, providing a foothold for privacy alignment where it matters most.

</details>

### 93. Forgetting Has Neighbors: Localized Collateral Forgetting in Machine Unlearning

📄 [arXiv](https://arxiv.org/abs/2605.31317) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`machine unlearning`、`collateral forgetting`、`local teacher distillation`
- 🎯 **研究动机**：machine unlearning 的聚合评估指标会掩盖样本级失败——unlearned 模型与删除后重训练模型的逐样本预测差异高度非均匀，这一失败模式此前未被系统研究
- 🔬 **研究方法**：逐样本比对 unlearned 模型与 retrain 模型的预测，识别出随与 forget set 几何邻近度增长的 localized collateral forgetting 现象，并提出 Local Teacher Distillation——用仅在 forget set 保留邻居上训练的小教师软标签替代随机代理目标
- 📌 **结论**：CIFAR-100 部分类删除任务上，局部教师使 unlearned 模型在 forget set 附近显著逼近重训练结果，同时保持有竞争力的聚合 unlearning 指标

👤 **作者**：Polina Dolgova、Sebastian U. Stich

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning aims to remove the influence of selected training examples without full retraining. Standard evaluations often summarize unlearning quality with aggregate metrics, such as accuracy- and forgetting-based scores, which can hide localized failures. We study this failure mode at the example level by comparing the predictions of an unlearned model to those of the model retrained after deletion. We show that this pointwise discrepancy can be highly non-uniform: for gradient-ascent and random-labeling methods, with and without retain-set fine-tuning, it grows with geometric proximity to the forget set. We call this phenomenon localized collateral forgetting. Our analysis identifies a mechanism behind the effect: surrogate targets used during unlearning can be inconsistent with the local prediction structure induced by retraining, and this inconsistency propagates through shared representations to nearby examples. Motivated by this mechanism, we propose Local Teacher Distillation, a simple mitigation strategy that replaces random targets with soft labels from a small teacher trained only on retained neighbors of the forget set. On CIFAR-100 partial-class deletion, this local teacher brings the unlearned model substantially closer to retraining, especially near the forget set, while maintaining competitive aggregate unlearning metrics.

</details>

### 94. Subliminal Learning Is Steering Vector Distillation

📄 [arXiv](https://arxiv.org/abs/2606.00995) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`subliminal learning`、`steering vector`、`distillation`、`adaptive optimizer`
- 🎯 **研究动机**：学生模型微调教师输出时会习得与输出语义无关的教师特质（subliminal learning），无语义数据如何传递特定语义特质机制不明。
- 🔬 **研究方法**：在两个开源模型上证明该现象由单个 steering vector 中介——教师系统提示可被 steering vector 良好近似、学生通过微调习得对齐向量，并将其统一为 steering vector distillation 框架，进一步考察自适应优化器的作用。
- 📌 **结论**：不能被 steering vector 良好近似的系统提示不会被潜默习得，非语义数据可传递带语义效果的向量，这解释了潜默学习无法跨模型迁移；自适应优化器是必要条件——被引导数据上的激活梯度沿 steering 方向携带小而一致的分量，非自适应优化器会让离群梯度主导从而阻断学习。

👤 **作者**：Camila Blank、Agam Bhatia、Senthooran Rajamanoharan、Arthur Conmy、Neel Nanda

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Subliminal learning refers to a student language model acquiring a teacher's traits (e.g. a system-prompted preference for owls) when fine-tuned on the teacher's outputs, despite the outputs being semantically unrelated to those traits. It remains poorly understood how data without semantic meaning can transfer specific semantic traits. In this work, we show that subliminal learning is mediated by a single steering vector, i.e. a vector added to the model's activations. Across two open-source models, we find that the teacher's system prompt is well approximated by a steering vector, and that the student's behavior is driven by learning an aligned vector over fine-tuning. System prompts that are not well approximated by steering vectors are not subliminally learned. This is a special case of steering vector distillation, in which a student trained on the outputs of a steered teacher learns to imitate that steering. We demonstrate steering vector distillation on a range of semantic and random vectors. Adding a semantic vector to a model's activations can have both model-independent and model-specific (i.e. non-semantic) effects on its behavior, so generated data that is non-semantic can transmit a vector with semantic effects, enabling subliminal learning. This also explains why subliminal learning does not transfer between models. We find that adaptive optimizers are necessary for subliminal learning in language models: activation gradients on steered data carry a small but consistent component along the steering direction, and non-adaptive optimizers impede this by allowing outlier gradients to dominate.

</details>

### 95. Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation

📄 [arXiv](https://arxiv.org/abs/2604.15559) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-04　🏷 NeurIPS 2026

**关键词**：`attack`、`agent distillation`、`subliminal learning`、`trajectory`、`data sanitation`
- 🎯 **研究动机**：subliminal learning 已证明语义特质可经无关数据传输，但 agentic 系统的策略从轨迹而非静态文本学习，不安全行为能否经蒸馏隐式迁移尚无实证。
- 🔬 **研究方法**：构造具强删除偏好的 teacher agent，仅用严格过滤所有删除关键词的安全任务轨迹蒸馏 student，并在原生 Bash 环境以 chmod-first 命令偏好复现同一威胁模型。
- 📌 **结论**：API 设置中 student 删除率达 100%（基线 5%），Bash 设置中 chmod-first 率达 30-55%（基线 0-10%）、大模型到小模型蒸馏迁移最强，说明显式数据清洗不足以防御、行为偏差隐式编码于轨迹动力学。

👤 **作者**：Jacob Dang、Brian Y. Xie、Omar G. Younis

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent work on subliminal learning demonstrates that language models can transmit semantic traits through data that is semantically unrelated to those traits. However, it remains unclear whether behavioral traits can transfer in agentic systems, where policies are learned from trajectories rather than static text. In this work, we provide the first empirical evidence that unsafe agent behaviors can transfer subliminally through model distillation across two complementary experimental settings. In our primary setting, we construct a teacher agent exhibiting a strong deletion bias, a tendency to perform destructive file-system actions via an API-style tool interface, and distill it into a student using only trajectories from ostensibly safe tasks, with all explicit deletion keywords rigorously filtered. In our secondary setting, we replicate the threat model in a native Bash environment, replacing API tool calls with shell commands and operationalizing the bias as a preference for issuing chmod as the first permission-related command over semantically equivalent alternatives such as chown or setfacl. Despite full keyword sanitation in both settings, students inherit measurable behavioral biases. In the API setting the student's deletion rate reaches 100% (versus a 5% baseline) under homogeneous distillation; in the Bash setting the student's chmod-first rate reaches 30%-55% (versus a 0%-10% baseline), with the strongest transfer observed in large-to-small distillation. Our results demonstrate that explicit data sanitation is an insufficient defense, and behavioral biases are encoded implicitly in trajectory dynamics regardless of the tool interface.

</details>

### 96. CLIOPATRA: Extracting Private Information from LLM Insights

📄 [arXiv](https://arxiv.org/abs/2603.09781) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`attack`、`privacy leakage`、`prompt injection`、`llm insights`
- 🎯 **研究动机**：隐私感知平台靠 PII 脱敏、聚类、聚合与 LLM 隐私审计等多层启发式保护提取使用洞察，但其"隐私保护"声明从未经受攻击检验
- 🔬 **研究方法**：提出 CLIOPATRA 攻击——对抗者精心设计并插入恶意聊天以击穿多层防护，诱导目标用户聊天中的敏感信息泄露，并在 Anthropic Clio 平台上以合成医疗聊天进行评估
- 📌 **结论**：攻击者能以近 100% 精度在最高 65% 的案例中提取医疗史，可通过混淆洞察隐蔽外泄，且 LLM 隐私审计等现有缓解不可靠、检测不到重大泄露

👤 **作者**：Meenatchi Sundaram Muthu Selva Annamalai、Emiliano De Cristofaro、Peter Kairouz

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The widespread adoption of AI assistants has prompted the development of privacy-aware platforms designed to extract insights from real-world usage. Their privacy protections primarily rely on layering multiple heuristic techniques, such as PII redaction, clustering, aggregation, and LLM-based privacy auditing. In this paper, we put their privacy claims to the test by presenting CLIOPATRA, the first attack against ``privacy-preserving'' LLM-based insights systems. Our attack involves an adversary that carefully designs and inserts malicious chats into the system to break multiple layers of protections and induce the leakage of sensitive information from a target user's chat. We evaluate CLIOPATRA on one such platform, Anthropic's Clio, and target synthetically generated medical chats to show that an adversary can successfully and confidently (with nearly 100% precision) extract the medical history contained in these chats in up to 65% of cases. We also show that CLIOPATRA can stealthily extract information by obfuscating the private information in the generated insights. Finally, we demonstrate that existing ad hoc mitigations, such as LLM-based privacy auditing, are unreliable and fail to detect major leaks. Taken together, our findings indicate that, even when layered, current heuristic protections are insufficient to adequately protect user data, and that prompt injection has been an understudied risk in LLM-based insight systems.

</details>

### 97. Models Designed to Forget: Machine Unlearning via Key Deletion

📄 [arXiv](https://arxiv.org/abs/2603.15033) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`defense`、`machine unlearning`、`key deletion`、`memory-augmented transformer`、`unlearning by design`
- 🎯 **研究动机**：现有近似 unlearning 从事后视角出发、靠参数更新擦除目标样本影响且通常需全量训练数据，与遗忘请求可被预期的真实部署场景根本错配。
- 🔬 **研究方法**：提出 unlearning by design 范式并实例化 MUNKEY——用 memory-augmented transformer 把实例特定记忆与模型权重解耦，遗忘即删除实例识别 key，实现零样本遗忘而无需权重更新或原始样本标签。
- 📌 **结论**：在自然图像、细粒度视觉识别与医学数据集上超越所有 post-hoc 基线，实现快速、面向部署的遗忘同时保持预测性能。

👤 **作者**：Sonia Laguna、Jorge da Silva Goncalves、Moritz Vandenhirtz、Alain Ryser、Irene Cannistraci、Julia E. Vogt

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning for vision models is rapidly becoming a practical requirement, driven by privacy regulations, data errors, and the need to remove harmful or corrupted training images. Despite this, most existing approximate unlearning methods tackle the problem from a post-hoc perspective. They attempt to erase the influence of targeted samples through parameter updates that typically require access to the full training data. This creates a mismatch with real deployment scenarios where unlearning requests can be anticipated, revealing a fundamental limitation of post-hoc approaches. We motivate unlearning by design, a novel paradigm for approximate methods in which models are directly trained to support forgetting as an inherent architectural capability. We instantiate this idea with Machine UNlearning via KEY deletion (MUNKEY), a memory-augmented transformer that decouples instance-specific memorization from model weights. Here, unlearning corresponds to removing the instance-identifying key, enabling zero-shot forgetting without weight updates or access to the original samples or labels. Across natural image benchmarks, fine-grained visual recognition, and medical datasets, MUNKEY outperforms all post-hoc baselines. Our results establish that unlearning by design enables fast, deployment-oriented unlearning while preserving predictive performance.

</details>

### 98. SMI: Statistical Membership Inference for Reliable Unlearned Model Auditing

📄 [arXiv](https://arxiv.org/abs/2602.01150) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`detection`、`unlearning audit`、`membership inference`、`mixture proportion`、`training-free`
- 🎯 **研究动机**：用 MIA 审计 unlearning 时"逃过成员检测即已遗忘"的假设根本错误——unlearned 样本与非成员在特征空间位置不同导致系统性乐观评估，且训练 shadow model 开销巨大。
- 🔬 **研究方法**：提出 SMI 免训练审计框架，将审计重构为估计 unlearned 特征分布中非成员混合比例，并给出 bootstrap 参考区间量化审计可靠性。
- 📌 **结论**：SMI 一致超越所有基于 MIA 的审计基线且无需 shadow model 训练，兼有理论保证与强经验表现。

👤 **作者**：Jialong Sun、…、Bo Liu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning (MU) is essential for enforcing the right to be forgotten in machine learning systems. A key challenge of MU is how to reliably audit whether a model has truly forgotten specified training data. Membership Inference Attacks (MIAs) are widely used for unlearned model auditing, where samples that evade membership detection are regarded as successfully forgotten. We show this assumption is fundamentally flawed: failed membership inference does not imply true forgetting. We prove that unlearned samples occupy fundamentally different positions in the feature space than non-member samples, making this alignment bias unavoidable and unobservable, which leads to systematically optimistic evaluations of unlearning performance. Meanwhile, training shadow models for MIA incurs substantial computational overhead. To address both limitations, we propose Statistical Membership Inference (SMI), a training-free auditing framework that reformulates auditing as estimating the non-member mixture proportion in the unlearned feature distribution. Beyond estimating the forgetting rate, SMI also provides bootstrap reference ranges for quantified auditing reliability. Extensive experiments show that SMI consistently outperforms all MIA-based baselines, with no shadow model training required. Overall, SMI establishes a principled and efficient alternative to MIA-based auditing methods, with both theoretical guarantees and strong empirical performance.

</details>

### 99. Causal Evaluation of Membership Inference Attacks

📄 [arXiv](https://arxiv.org/abs/2602.02819) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`evaluation`、`membership inference`、`causal inference`、`memorization`、`privacy audit`
- 🎯 **研究动机**：标准 MIA 评估需重复重训练、对大模型代价高昂，而常用替代的 one-run 与 zero-run 方法的统计有效性不明。
- 🔬 **研究方法**：将 MIA 评估框架化为因果推断问题（记忆化定义为纳入数据点的因果效应），形式化 one-run 中联合纳入数据点的干扰与 zero-run 额外的成员/非成员分布偏移偏差，推导多 run、one-run、zero-run 情形的因果版指标与非渐近一致估计器。
- 📌 **结论**：在预训练与微调 LLM 等多个设置中验证，该框架无需重训练且在分布偏移下仍可可靠测量 MIA 性能。

👤 **作者**：Mathieu Even、Clément Berenfeld、Linus Bleistein、Tudor Cebere、Julie Josse、Aurélien Bellet

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership Inference Attacks (MIAs) aim to distinguish training points (members) from unseen data (non-members), and are widely used to quantify memorization and assess privacy risks. Standard MIA evaluation requires repeated retraining, which is computationally costly for large models. One-run (single training with randomized data inclusion) and zero-run (post hoc evaluation) methods are often used instead, but their statistical validity remains unclear. We address this gap by framing MIA evaluation as a causal inference problem, defining \emph{memorization as the causal effect of including a data point in the training set}. This novel formulation reveals and formalizes key sources of bias in existing protocols: one-run methods suffer from interference between jointly included points, while zero-run evaluations are additionally confounded by distribution shift between member and non-member evaluation data. We derive causal analogues of standard MIA metrics and propose practical estimators for multi-run, one-run, and zero-run regimes with non-asymptotic consistency guarantees. We validate our approach in several settings, including pretrained and fine-tuned LLMs, showing that it enables reliable measurement of MIA performance without retraining and under distribution shift. Overall, our framework provides a principled foundation for privacy evaluation in modern AI systems.

</details>

### 100. Assessing Per-Sample Membership Inference Vulnerability without Retraining

📄 [arXiv](https://arxiv.org/abs/2602.15919) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`analysis`、`membership inference`、`privacy risk`、`leverage score`、`shadow model`
- 🎯 **研究动机**：针对单样本的成员推断攻击（MIA）大幅强于无差别攻击，但评估单个训练点的隐私脆弱性通常需要训练影子模型，代价高昂。
- 🔬 **研究方法**：在线性情形推导出黑盒 MIA 脆弱性对总体杠杆分数与残差损失的闭式分解，据此提出作用于末层表示、仅需单个已训练模型而无需影子模型的代理分数。
- 📌 **结论**：跨多样数据集与架构的实验中，该分数在最先进攻击下识别最高风险样本的能力优于 loss 与梯度范数基线，为逐样本隐私风险评估提供了高效且有理论依据的工具。

👤 **作者**：Valentin Dorseuil、Jamal Atif、Olivier Cappé

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent work in the privacy literature shows that sample-targeted membership inference attacks (MIAs) significantly outperform untargeted approaches by a wide margin. Motivated by this observation, we address the following question: can the privacy vulnerability of individual training points be assessed without training shadow models? We show that per-sample exposure to MIA is governed not only by a point's loss, but also by a data-dependent geometric measure. In the linear setting, we derive a closed-form decomposition of individual black-box MIA vulnerability into a population leverage score and a residual loss term, making explicit how sample-dependent geometry translates into privacy exposure. Since the final layer of most modern architectures is linear, we extend this framework to deep networks and propose a surrogate score operating on last-layer representations that requires only a single trained model and no shadow models. Empirical evaluations across diverse datasets and architectures show that our score outperforms loss and gradient-norm baselines at identifying the highest-risk points under state-of-the-art attacks, providing a computationally efficient and theoretically grounded tool for per-sample privacy risk assessment.

</details>

### 101. Sequential Membership Inference Attacks

📄 [arXiv](https://arxiv.org/abs/2602.16596) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`attack`、`membership inference`、`canary`、`privacy audit`、`dp-sgd`
- 🎯 **研究动机**：现代 AI 模型生命周期中经历多次更新，现有成员推断只审视最终模型快照，未利用模型序列信息。
- 🔬 **研究方法**：提出 Sequential Membership Inference（SeMI），在受控插入时间注入目标 canary 并利用模型序列；推导最优攻击 SeMI* 及其 power（隔离性质：power 仅取决于插入前后的统计量），发展 white-box 梯度与 black-box loss 两种实用攻击。
- 📌 **结论**：在 (DP-)SGD 训练的模型上 SeMI 攻击 power 高于快照独立基线，借助插入时间控制与序列观察产生更紧的隐私审计。

👤 **作者**：Thomas Michel、Debabrota Basu、Emilie Kaufmann

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern AI models are not static. They go through multiple updates in their lifecycles. We propose to design Sequential Membership Inference (SeMI) attacks leading to tighter privacy audits by exploiting the sequence of models and injecting a target canary at a controlled insertion time. First, for empirical mean computation, we develop SeMI*, an {optimal SeMI attack to identify the presence of a target inserted at a specific insertion step}. We derive the power of SeMI* to show that accessing the model sequence yields more powerful MI attacks than scrutinising only the final model. SeMI* exhibits an isolation property -- its power depends on the statistics obtained right before and after insertion of the target. Leveraging this insight, we develop practical white-box (accessing model gradients) and black-box (accessing loss) SeMI attacks against models trained with (DP-)SGD. Across datasets and models trained with (DP-)SGD, our experiments show that SeMI attacks achieve higher powers than snapshot-independent baselines, and yield tighter privacy audits thanks to (a) control over the insertion time and (b) observations across the model sequence.

</details>

### 102. GUIGuard-Bench: Toward a General Evaluation for Privacy-Preserving GUI Agents

📄 [arXiv](https://arxiv.org/abs/2601.18842) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-01　🏷 NeurIPS 2026

**关键词**：`benchmark`、`gui agent`、`privacy`、`region-level annotation`、`trajectory`
- 🎯 **研究动机**：GUI agent 依赖截图感知环境易暴露身份、账户、位置与行为痕迹等敏感信息，而现有视觉隐私数据集局限于静态自然图像，无法刻画 GUI 任务轨迹中隐私风险的上下文依赖与任务相关性。
- 🔬 **研究方法**：构建含 241 条真实 GUI agent 轨迹、4080 张 Android 与 PC 截图的 benchmark，每张截图带区域级隐私边界框、语义隐私类别、风险等级与任务必要性标注，支持隐私识别、保护截图下离线规划保真与保护策略效用影响三项互补评估。
- 📌 **结论**：现有模型常能判断截图是否含隐私信息，但在细粒度定位、类别识别、风险评估与任务必要性判断上表现不佳；以 Claude Sonnet 4.6 为代表的闭源模型在 Android 环境应用隐私保护后仍能保持基本一致的规划语义。

👤 **作者**：Yanxi Wang、…、Jiyan He

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As GUI agents increasingly rely on screenshots to perceive and operate digital environments, they may inadvertently expose sensitive information such as identities, accounts, locations, and behavioral traces. While existing benchmarks primarily focus on task completion, grounding, or defenses against third-party attacks, current visual privacy datasets remain largely restricted to static natural images, limiting their ability to capture the contextual dependence and task relevance of privacy risks in GUI task trajectories. To bridge this gap, we introduce \textbf{GUIGuard-Bench}, a first-step benchmark for studying privacy-preserving GUI agents in trajectory-based GUI workflows. GUIGuard-Bench contains 241 real GUI-agent trajectories with 4,080 screenshots across Android and PC environments. Each screenshot is annotated at the region level with privacy bounding boxes, semantic privacy categories, risk levels, and whether the private information is necessary for completing the task. Built on these annotations, GUIGuard-Bench supports three complementary evaluations: privacy recognition, offline planning fidelity under protected screenshots, and the utility impact of different protection strategies. Our results show that current models can often detect whether a screenshot contains private information, but they struggle with fine-grained localization, category recognition, risk assessment, and task-necessity judgment. We also find that closed-source models, exemplified by Claude Sonnet 4.6, can maintain largely consistent planner semantics in Android environments after privacy protection is applied. Our results highlight privacy recognition as a critical bottleneck for practical GUI agents. Project: https://futuresis.github.io/GUIGuard-page/

</details>

**尚未挂出 arXiv（待核验）**
- Exposing Private Corpus Leakage in Multimodal RAG
- MPCI-Bench: Multimodal Pairwise Contextual Integrity Privacy Evaluation of Language Model Agents
- Don't Deploy Fine-Tuned Genomic Foundation Models Without Privacy Evaluation
- Guarding the Life Code: Preserving Membership Privacy in Genomic Foundation Models
- Benchmarking Membership Privacy Risks in Preference-Based LLM Post-Training
- Bayesian Low-Rank Posteriors for Scalable Membership Inference
- Local FDR Membership Inference Attacks
- Estimating Model-Level Membership Inference Vulnerability Without Reference Models
- Evaluating an Evaluation: Membership Inference Attacks as Machine Unlearning Diagnostics
- Lethe: Link Inference Attacks For Evaluation of Edge Unlearning Methods
- ShadowBench: Exposing Lexical Anchoring and the Illusion of Forgetting
- KNOT: A Knowledge Entanglement Benchmark for Robust Unlearning Evaluation
- METAFORGET: Audit-Driven Update-Policy Learning for Reliable LLM Unlearning
- Unlearning That Lasts: Utility-Preserving, Robust, and Almost Irreversible Forgetting
- What Should Remain After Forgetting? Rethinking LLM Unlearning as Predictive Posterior Correction
- TRACE: Data-Free Text Reconstruction Attacks against Approximate Unlearning in LLMs
- Individual-Level Unlearning in Vision-Language Models（已库内，0929 What Does It Mean to Forget a Person 同族待核）
- What Do SAE Features Encode? Evidence from Human Neural Activity（机制方法，交叉参考）

### 水印、溯源与内容真实性

### 103. AuxMark: Defending Against Unauthorized Agent Distillation via Auxiliary Behavioral Watermarking（已库内，0929）

📄 [arXiv](https://arxiv.org/abs/2609.34597) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`watermark`、`agent distillation`、`behavioral watermarking`、`attribution`、`black-box audit`
- 🎯 **研究动机**：LLM agent 轨迹可被非法收集蒸馏出学生 agent，现有水印要么不适配结构化交互的 agent 环境要么跨任务/架构不可靠。
- 🔬 **研究方法**：AuxMark 在教师轨迹中动态插入安全无害的非必要辅助动作并留存上下文为私有证据卡，审计时由证据卡构造真假配对探针并做卡级符号检验，实现模型级检测与轨迹级溯源。
- 📌 **结论**：在 3 个 agent 基准、2 个教师与 4 种学生架构上检出全部 24 个蒸馏模型且 48 个干净模型零误报，并抗数据灌水、改写、截断与自适应清洗攻击。

👤 **作者**：Yiqing Feng、…、Mingxun Zhou

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model agents can acquire complex capabilities through multi-step interaction and tool use, but their trajectories can also be illegally collected to dis- till student agents. However, existing watermarking methods either do not fit the structured and interactive nature of agent environments or lack reliable effective- ness across tasks and model architectures. We introduce AuxMark, a behavioral watermarking framework for tracing unauthorized agent distillation. AuxMark dynamically inserts safe, non-essential auxiliary action into teacher trajectories, and stores the associated contexts as private evidence cards. To audit a suspicious student model, AuxMark constructs paired real and fake probes from these cards and applies a card-level sign test. This black-box protocol supports both model- level detection and trace-level attribution. Across three agent benchmarks, two teacher agents, and four student architectures, AuxMark detects all 24 distilled models with zero false positives on 48 clean models. It also preserves task utility and remains effective against data flooding, paraphrasing, truncation, and adaptive cleaning attacks. Our code will be released at this URL.

</details>

### 104. Auditing Cross-Lingual Fairness in Language Model Watermarking

📄 [arXiv](https://arxiv.org/abs/2608.20047) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-08　🏷 NeurIPS 2026

**关键词**：`evaluation`、`watermarking`、`cross-lingual fairness`、`detection threshold`、`quality metrics`
- 🎯 **研究动机**：LLM 水印几乎只在英文文本上用各方案自身检测阈值与狭窄质量度量评估，多语言部署暴露出在英文上无关紧要却决定跨语言结论的评估设计选择。
- 🔬 **研究方法**：提出四组件评估框架——按部署语境经验校准的检测阈值、区分校准失败与检测失败的阈值无关测量、三种不相交质量度量范式、以及跨类型学家族分区的广义熵差异分解。
- 📌 **结论**：应用于 6 种水印方案、3 个开源生成器、11 种语言（4 种文字、8 个类型学家族）后发现，检测与质量上的跨语言差异主要发生在类型学家族之间，表明水印跨语言公平差距是语言属性结构性的而非个别语言特异。

👤 **作者**：Alexander Nemecek、Osama Zafar、Debargha Ganguly、Vikash Singh、Vipin Chaudhary、Erman Ayday

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Watermarking schemes for large language model output are evaluated almost exclusively on English text using each scheme's detection threshold and a narrow set of quality measurements. Multilingual deployment exposes evaluation-design choices that are inconsequential on English but determine conclusions cross-lingually. We propose an evaluation framework with four components: detection thresholds calibrated empirically per deployment context, a threshold-independent companion measurement that distinguishes calibration failures from detection failures, three disjoint quality measurement paradigms (distributional, paired-semantic, and reference-perplexity), and a generalized-entropy decomposition of cross-language disparity over a typological family partition. Applied to six watermarking schemes, three open-weight generators, eleven languages spanning four scripts and eight typological families, and both base and instruction-tuned regimes, the framework reveals failure modes that single-language single-paradigm evaluation cannot surface. Across detection and quality, observed disparity is predominantly between-family on the typological partition, indicating that cross-lingual fairness gaps in watermarking are structural to language properties rather than idiosyncratic to particular languages.

</details>

### 105. Secure Seed-Based Multi-bit Watermarking for Diffusion Models from First Principles

📄 [arXiv](https://arxiv.org/abs/2605.06153) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`watermark`、`diffusion model`、`seed-based embedding`、`security-robustness-fidelity`、`theoretical framework`
- 🎯 **研究动机**：seed-based 生成内水印的评估高度经验化、依赖特定生成与反演架构，且缺乏严格的安全性定义，导致任何方法的性能尤其安全性都难以下明确结论。
- 🔬 **研究方法**：将模型相关部分与水印系统实际决策机制解耦，建立基于 security、robustness、fidelity 三者的形式化评估框架与刻画三者权衡的特征曲面，并提出可达到曲面上任意工作点、推广既有 seed-based 方法的 SSB 水印。
- 📌 **结论**：SSB 能在安全-鲁棒-保真特征曲面上达到任意目标区间，为无需昂贵经验评估、具理论保证的现代水印系统设计开辟道路。

👤 **作者**：Enoal Gesny、Eva Giboulot

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid emergence of generative image models has led to the development of specialized watermarking techniques, particularly in-generation methods such as seed-based embedding. However, current evaluations in this area remain largely empirical, making them heavily reliant on the specific model architectures used for generation and inversion. This prevents any clear conclusion on the performance of any method, especially regarding security, for which a rigorous definition is lacking. Against this approach, we argue that the effectiveness of a watermarking scheme should be established purely through a thorough theoretical analysis. This is enabled by decoupling the model-dependent part from the actual decision mechanism of the watermarking system. Using this decoupling, we introduce a formal evaluation framework based on security, robustness, and fidelity. This allows precise comparisons between watermarking systems through a characteristic surface representing the trade-off between these three quantities, independent of any generative model. Based on this framework, we propose SSB, a novel watermarking method that generalizes previous seed-based methods by allowing to reach any security-robustness-fidelity regime on its characteristic surface. This work opens the door to the design of modern watermarking systems with theoretical guarantees that do not necessitate any costly empirical evaluations.

</details>

### 106. Asymmetric Phase Coding Audio Watermarking

📄 [arXiv](https://arxiv.org/abs/2605.07241) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`watermark`、`audio provenance`、`phase coding`、`digital signature`
- 🎯 **研究动机**：深伪音频挑战语音认证系统，被动取证检测器对演进的生成模型与真实信道失真敏感，需要可审计的音频溯源原语
- 🔬 **研究方法**：提出免训练的 Asymmetric Phase Coding（APC），组合 Ed25519 数字签名、Reed-Solomon 纠错、伪随机 STFT 相位 bin 选择与相邻 bin 对 log 幅度差上的冗余 QIM 编码，形成紧凑、不可抵赖、盲提取的密码学签名层
- 📌 **结论**：在 1000 条 LibriSpeech 测试音频、8 种攻击配置（端裁剪、低通、重采样、FLAC/MP3/OGG 重编码等）下，每种条件密码学验证率均达 97.5%-98.3%，平均 PESQ 为 3.02，CPU 延迟仅数十毫秒

👤 **作者**：Guang Yang、Amir Ghasemian、Ninareh Mehrabi、Homa Hosseinmardi

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of deepfake audio challenges voice-based authentication systems; passive forensic detectors are sensitive to evolving generative models and to real-world channel distortions. We propose Asymmetric Phase Coding (APC), a training-free cryptographic signing layer for audio, designed as a compact and auditable provenance primitive that can stand alone or be stacked with learned watermarks. APC combines Ed25519 digital signatures (EdDSA, FIPS 186-5; 64-byte signatures) with Reed-Solomon error correction, pseudo-random STFT phase-bin selection, and a redundant quantization-index-modulation (QIM) code on log-magnitude differences of adjacent bin pairs, yielding a compact, non-repudiable, blind-extractable watermark. We evaluate APC on 1,000 LibriSpeech test-clean clips (10 s each, 44.1 kHz) under eight attack configurations -- identity, 10% end-cropping, 20% end-cropping, 8 kHz low-pass, 16 kHz round-trip resampling, FLAC re-encoding, MP3 at 128 kbps, and OGG-Vorbis at 128 kbps -- and achieve cryptographic verification rates between 97.5% and 98.3% on every condition at mean PESQ=3.02 and tens-of-milliseconds CPU latency. We explicitly compare APC against recent neural baselines (AudioSeal, WavMark, SilentCipher), detail the threat model (forgery resistance vs. erasure), characterize the dataset, define all metrics, quantify an adaptive white-box erasure attack, and release code, keys, and metadata for reproducibility.

</details>

### 107. Sequential Behavioral Watermarking for LLM Agents

📄 [arXiv](https://arxiv.org/abs/2605.11036) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`watermark`、`llm agent`、`provenance`、`trajectory`、`history-conditioned`
- 🎯 **研究动机**：agent 轨迹难以证明来源与所有权，而现有 agent 水印把每个动作步当独立试验、忽略轨迹结构，在轨迹被扰动、截断或未对齐观测时脆弱。
- 🔬 **研究方法**：提出 SeqWM 序列行为水印框架，将信号嵌入 history-conditioned 转移模式，并以位置无关方式对照随机 key 基线验证轨迹。
- 📌 **结论**：在多样 agent 基准与 LLM backbone 上实现可靠检测且保持 agent 效用，在轨迹损坏下依然鲁棒，而 round-indexed 行为水印在同样条件下崩溃。

👤 **作者**：Hyeseon An、Shinwoo Park、Dongsu Kim、Yo-Sub Han

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents act through sequences of executable decisions, but their trajectories provide little evidence of which agent or policy produced them, making provenance, ownership, and unauthorized reuse difficult to establish from observed behavior alone. This motivates watermarking signals embedded directly into agent behavior rather than only into generated text, since text watermarking cannot capture the action-level decisions that define agent execution. Recent agent watermarking methods address this gap by moving the watermark from generated text to behavioral choices. However, by treating each action step as an independent trial, they overlook trajectory structure and become fragile when trajectories are perturbed, truncated, or observed without reliable alignment. We propose SeqWM, a sequential behavioral watermarking framework that embeds signals into history-conditioned transition patterns and verifies trajectories position-agnostically against random-key baselines. Experiments across diverse agent benchmarks and LLM backbones show that SeqWM consistently achieves reliable detection while preserving agent utility, and remains robust under trajectory corruption where round-indexed behavioral watermarks collapse.

</details>

### 108. Every Bit, Everywhere, All At Once: A Binomial Multibit LLM Watermark

📄 [arXiv](https://arxiv.org/abs/2605.11653) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`watermark`、`multibit`、`binomial encoding`、`payload capacity`、`per-bit confidence`
- 🎯 **研究动机**：LLM 水印已商用落地，实用场景日益需要把用户 ID、时间戳等复杂 payload 编码进文本的多比特水印，而既有评估指标缺乏实用洞察。
- 🔬 **研究方法**：引入 binomial encoding 在每个 token 位置直接编码 payload 的每一位，配合生成期间把编码压力动态重定向到欠编码位的有状态编码器，并提出 per-bit confidence scoring 作为实用评估指标。
- 📌 **结论**：在最高 64-bit payload 上对 8 个基线的评估显示消息准确率与鲁棒性更优，且在更实用的大 payload、低失真区间优势进一步扩大。

👤 **作者**：Thibaud Gloaguen、Robin Staab、Mark Vero、Martin Vechev

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With LLM watermarking already being deployed commercially, practical applications increasingly require multibit watermarks that encode more complex payloads, such as user IDs or timestamps, into the generated text. In this work, we propose a fundamentally new approach for multibit watermarking: introducing binomial encoding to directly encode every bit of the payload at every token position. We complement our approach with a stateful encoder that during generation dynamically redirects encoding pressure toward underencoded bits. Our evaluation against 8 baselines on up to 64-bit payloads shows that our scheme achieves superior message accuracy and robustness, with the gap to baseline methods widening in more relevant settings (i.e., large payloads and low-distortion regimes). At the same time, we challenge prior works' evaluation metrics, highlighting their lack of practical insights, and introduce per-bit confidence scoring as a practically relevant metric for evaluating multibit LLM watermarks.

</details>

### 109. TextSeal: A Localized LLM Watermark for Provenance & Distillation Protection

📄 [arXiv](https://arxiv.org/abs/2605.12456) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`watermark`、`gumbel-max sampling`、`localization`、`distillation protection`、`distortion-free`
- 🎯 **研究动机**：开源 LLM 文本水印需要同时实现强检测、输出多样性保持与混合文档中的局部定位，并兼容投机解码等推理优化。
- 🔬 **研究方法**：TextSeal 基于 Gumbel-max 采样引入 dual-key generation 恢复输出多样性，配合 entropy-weighted scoring 与多区域定位，不增加任何推理开销。
- 📌 **结论**：检测强度严格优于 SynthID-text 等基线、抗稀释且理论 distortion-free；6000 次 A/B、5 语言人类评估无可感质量差异，水印信号还可经蒸馏迁移以检测未授权使用。

👤 **作者**：Tom Sander、…、Pierre Fernandez

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce TextSeal, a state-of-the-art watermark for large language models. Building on Gumbel-max sampling, TextSeal introduces dual-key generation to restore output diversity, along with entropy-weighted scoring and multi-region localization for improved detection. It supports serving optimizations such as speculative decoding and multi-token prediction, and does not add any inference overhead. TextSeal strictly dominates baselines like SynthID-text in detection strength and is robust to dilution, maintaining confident localized detection even in heavily mixed human/AI documents. The scheme is theoretically distortion-free, and evaluation across reasoning benchmarks confirms that it preserves downstream performance; while a multilingual human evaluation (6000 A/B comparisons, 5 languages) shows no perceptible quality difference. Beyond its use for provenance detection, TextSeal is also ``radioactive'': its watermark signal transfers through model distillation, enabling detection of unauthorized use.

</details>

### 110. Watermarking Should Be Treated as a Monitoring Primitive

📄 [arXiv](https://arxiv.org/abs/2605.13095) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`watermark`、`attribution`、`monitoring`、`observer model`、`governance`
- 🎯 **研究动机**：水印被广泛提议用于生成模型的溯源、归因与安全监控，但应如何评测与治理它缺乏统一视角。
- 🔬 **研究方法**：提出两类互补观察者模型——用检测器/解码器访问与实体映射做归因的内部观察者、以及无需密钥或检测器而从标注输出学习实体特异信号的外部观察者——并分析两者支持监控的条件。
- 📌 **结论**：零比特水印在每实体多密钥部署下无需显式编码身份即可支持内部归因，并在选定文本与图像配置中实现外部识别；外部暴露依赖持久可学习的水印结构而非普适存在，故除单样本鲁棒性外还应治理归因访问、部署选择及依赖设计的实体可链接性与去匿名化风险。

👤 **作者**：Toluwani Aremu、Jie Zhang、Nils Lukas

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Watermarking is widely proposed for provenance, attribution, and safety monitoring in generative models. We argue that it should be evaluated and governed as a monitoring primitive through two complementary observer models. Internal observers use detector or decoder access and entity mappings for attribution; external observers learn entity-specific signals from labeled outputs without keys or detectors. With persistent entity bindings and reliable inference, either pathway can support monitoring. We show that even zero-bit watermarking supports internal attribution under per-entity multi-key deployments without explicitly encoding identity, and demonstrate external identification in selected text and image configurations. External exposure depends on persistent, learnable watermark structure and is not universal, while internal attribution also remains conditional on reliability and access. These findings motivate governance of attribution access and deployment choices alongside evaluation of design-dependent entity linkability, de-anonymization or re-identification, beyond per-sample robustness.

</details>

### 111. Watermarking Game-Playing Agents in Perfect-Information Extensive-Form Games

📄 [arXiv](https://arxiv.org/abs/2605.14283) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`watermark`、`game-playing agent`、`extensive-form game`、`kgw`、`statistical test`
- 🎯 **研究动机**：LLM 水印可检测模型误用，博弈场景（如在线国际象棋检测 AI 作弊）存在类似挑战，但博弈策略如何被水印化尚未被研究。
- 🔬 **研究方法**：将 KGW 水印适配到完美信息扩展式博弈的博弈 agent 策略上，并设计统计检验来检测水印。
- 📌 **结论**：证明被水印策略的期望效用退化有界但存在可检测性与质量之间的权衡；在国际象棋引擎上水印对策略质量影响可忽略，且仅需少量对局即可检出。

👤 **作者**：Juho Kim、Fei Fang、Tuomas Sandholm

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Watermarking techniques for large language models (LLMs), which encode hidden information in the output so its source can be verified, have gained significant attention in recent days, thanks to their potential capability to detect accidental or deliberate misuse. Similar challenges involving model misuse also exist in the context of game-playing, such as when detecting the unauthorized use of AI tools in gaming platforms (e.g., cheating in online chess). In this paper, we initiate the study of how game-playing strategies can be watermarked. We show how the KGW watermark for LLMs can be adapted to watermark game-playing agents in perfect-information extensive-form games. The watermark can then be detected using a statistical test. We show that the degradation in the quality of the watermarked strategy profile, quantified by the expected utility, can be bounded, but there is a tradeoff between detectability and quality. In our experiments, we bootstrap the watermarking framework to various chess engines and demonstrate that a) the impact of the watermark on the quality of the strategy is negligible and b) the watermark can be detected with just a handful of games.

</details>

### 112. Making Open-Source Text LLM Watermarks Durable Against Merging

📄 [arXiv](https://arxiv.org/abs/2607.20435) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`watermark`、`model merging`、`adversarial training`、`open-source llm`、`durability`
- 🎯 **研究动机**：嵌入开源 LLM 权重的文本水印会被训练后修改移除，其中常用于融合专家知识与防止灾难性遗忘的 model merging 尤其强烈地去除水印，如何让水印在后续 merging 中存活是关键问题。
- 🔬 **研究方法**：提出 Merge-Adversarial Training 对抗训练算法，在把文本水印蒸馏进模型权重的同时对后续 model merging 保持鲁棒。
- 📌 **结论**：一致超越所有基线（SLERP 下 TPR@1%FPR 至多 +51 个百分点、平均 +25 个百分点）且保持下游能力，并首次在 3 种主流 merging 算法与组合专家能力、防灾难性遗忘等真实合并场景下评估开源水印。

👤 **作者**：Luisa Scharff、Thibaud Gloaguen、Robin Staab、Martin Vechev

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-source LLMs (OSMs)arereaching near state-of-the-art performance, prompting prior works to trace the text they generate by embedding text watermarking algorithms directly into their weights. Yet, OSMs are subject to post-training modifications, which has been shown to remove the watermark. Model merging in particular, a prominent method used for combining expert knowledge and preventing catastrophic forgetting, strongly removes such OSM watermarks. A key question is how to enable OSM watermarks that survive subsequent merging. In this work, we show for the first time how to design an OSM watermark that is durable against model merging. We propose Merge-Adversarial Training, an adversarial training algorithm to distill text watermarks into model weights while being robust to subsequent model merging. Our approach consistently outperforms all baselines (e.g. with SLERP up to +51 percentage points (pp) TPR@1%FPR with +25 pp on average) while preserving downstream capabilities. We also for the first time evaluate OSM watermarks against realistic merge scenarios, representing common use-cases such as combining expert capabilities or preventing catastrophic forgetting, and with 3 prominent merging algorithms. More broadly, our findings suggest that adversarial training is a reliable approach for increasing OSM watermark durability against post-training modifications.

</details>

### 113. On the Robustness of Watermarking for Autoregressive Image Generation

📄 [arXiv](https://arxiv.org/abs/2604.11720) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-04　🏷 NeurIPS 2026

**关键词**：`attack`、`watermark removal`、`forgery`、`autoregressive image generation`、`watermark mimicry`
- 🎯 **研究动机**：自回归图像生成器的水印被用于检测归因输出以对抗错误信息并过滤合成图像防模型坍缩，其面对移除与伪造攻击的鲁棒性未知。
- 🔬 **研究方法**：评估现有攻击并提出三种新攻击——向量量化再生移除、对抗优化攻击与频率注入攻击，仅需单张水印参考图像且无需原始模型参数或水印密钥。
- 📌 **结论**：移除与伪造攻击均有效，说明现有 AR 图像生成水印不足以支持数据集过滤的合成内容检测；Watermark Mimicry 还能操纵真实图像模仿生成器水印触发误检、使其被排除出未来模型训练。

👤 **作者**：Andreas Müller、…、Asja Fischer

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of autoregressive (AR) image generators demands reliable detection and attribution of their outputs to mitigate misinformation, and to filter synthetic images from training data to prevent model collapse. To address this need, watermarking techniques, specifically designed for AR models, embed a subtle signal at generation time, enabling downstream verification through a corresponding watermark detector. In this work, we study these schemes and demonstrate their vulnerability to both watermark removal and forgery attacks. We assess existing attacks and further introduce three new attacks: (i) a vector-quantized regeneration removal attack, (ii) adversarial optimization-based attack, and (iii) a frequency injection attack. Our evaluation reveals that removal and forgery attacks can be effective with access to a single watermarked reference image and without access to original model parameters or watermarking secrets. Our findings indicate that existing watermarking schemes for AR image generation do not reliably support synthetic content detection for dataset filtering. Moreover, they enable Watermark Mimicry, whereby authentic images can be manipulated to imitate a generator's watermark and trigger false detection to prevent their inclusion in future model training.

</details>

### 114. Alignment Imprint: Zero-Shot AI-Generated Text Detection via Provable Preference Discrepancy

📄 [arXiv](https://arxiv.org/abs/2604.16923) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-04　🏷 NeurIPS 2026

**关键词**：`detection`、`ai-generated text`、`alignment`、`log-likelihood ratio`、`zero-shot`
- 🎯 **研究动机**：现有基于 likelihood 的 AI 生成文本检测对内容复杂度敏感、性能不稳定。
- 🔬 **研究方法**：将 alignment 过程抽象为约束优化序列，证明 log-likelihood ratio 可分解为隐式指令偏置与偏好奖励（Alignment Imprint），并提出信息加权的标准化统计量 LAPD 抑制高熵区不稳定。
- 📌 **结论**：理论上 LAPD 支配 Fast-DetectGPT 并严格改进未加权对齐分数，实验上相对最强基线提升 45.82% 且在所有设置下一致大幅增益。

👤 **作者**：Junxi Wu、…、Changliang Zou

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Detecting AI-generated text is an important but challenging problem. Existing likelihood-based detection methods are often sensitive to content complexity and may exhibit unstable performance. In this paper, our key insight is that modern Large Language Models (LLMs) undergo alignment (including fine-tuning and preference tuning), leaving a measurable distributional imprint. We theoretically derive this imprint by abstracting the alignment process as a sequence of constrained optimization steps, showing that the log-likelihood ratio can naturally decompose into implicit instructional biases and preference rewards. We refer to this quantity as the Alignment Imprint. Furthermore, to mitigate the instability in high-entropy regions, we introduce Log-likelihood Alignment Preference Discrepancy (LAPD), a standardized information-weighted statistic based on alignment imprint. We provide statistical guarantee that alignment-based statistics dominate Fast-DetectGPT in performance. We also theoretically show that LAPD strictly improves the unweighted alignment scores when the aligned and base models are close in distribution. Extensive experiments show that LAPD achieves an improvement 45.82% relative to the strongest existing baselines, yielding large and consistent gains across all settings.

</details>

### 115. ArcMark: Distortion-Free Multi-Byte LLM Watermark via Optimal Transport

📄 [arXiv](https://arxiv.org/abs/2602.07235) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`watermark`、`multi-bit embedding`、`distortion-free`、`channel coding`
- 🎯 **研究动机**：现有多比特水印沿用零比特设计原则（如每 token 编码单比特），无法在不扰动 next-token 分布的前提下嵌入用户 ID、模型版本乃至 prompt 本身等多字节信息
- 🔬 **研究方法**：提出 ArcMark，将无失真水印形式化为信道编码问题并推导信息论信道容量的基本极限，据此设计可在几百 token 内可靠嵌入多字节的编码构造
- 📌 **结论**：ArcMark 在重构精度上优于竞争性多比特无失真水印（含部分文本被篡改的攻击场景），且输出在困惑度与下游任务质量上与无水印文本不可区分

👤 **作者**：Atefeh Gilani、Sajani Vithana、Carol Xuan Long、Oliver Kosut、Lalitha Sankar、Flavio P. Calmon

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Watermarking is an important tool for promoting the responsible use of large language models (LLMs). Existing watermarks insert a signal into generated tokens that either flags LLM-generated text (zero-bit watermarking) or encodes more complex messages (multi-bit watermarking). Though a number of recent approaches insert multiple bits into text without perturbing average next-token predictions, they largely extend design principles from the zero-bit setting, such as encoding a single bit per token. In contrast, a watermarker capable of embedding multiple bytes into the text would dramatically increase the potential applications, by embedding information such as the ID of the user who submitted the prompt, the precise model version that was used, or even the prompt itself. We address this problem by introducing ArcMark: a new watermark construction based on coding and information-theoretic principles that is capable of reliably embedding multiple bytes of information into just a few hundred tokens, without any distortion of the underlying LLM next-token distribution. We derive ArcMark by formulating the distortion-free watermarking problem as a channel coding problem, and deriving an information-theoretic channel capacity that establishes the fundamental limit of embedding information in LLM output in a distortion-free manner. This capacity formulation informs the design of ArcMark. In practice, ArcMark outperforms competing multi-bit distortion-free watermarks in terms of reconstruction accuracy, including in the face of attacks that alter a subset of the LLM text. ArcMark output is also shown to be indistinguishable from unwatermarked text in terms of perplexity, and in downstream task quality.

</details>

### 116. PRO: Enabling Precise and Robust Text Watermark for Open-Source LLMs

📄 [arXiv](https://arxiv.org/abs/2510.23891) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-10　🏷 NeurIPS 2026

**关键词**：`watermark`、`open-source llm`、`distillation`、`robustness`、`model merging`
- 🎯 **研究动机**：开源 LLM 拥有者无法控制解码过程，从闭源模型蒸馏水印又因学得模式与预定义模式错配而对下游微调、模型合并脆弱，导致缺少实用的文本溯源手段。
- 🔬 **研究方法**：PRO 将 watermark policy model 与 LLM 联合训练以产生更易学、更贴合检测准则的模式，并用模拟下游扰动的正则项惩罚水印可检测性退化。
- 📌 **结论**：在 LLaMA-3.2、LLaMA-3、Phi-2 等开源模型上同时显著提升水印可检测性与对模型修改的韧性。

👤 **作者**：Jiaqi Xue、…、Mengxin Zheng

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text watermarking for large language models (LLMs) enables model owners to verify text origin and protect intellectual property. While watermarking methods for closed-source LLMs are relatively mature, extending them to open-source models remains challenging, as developers cannot control the decoding process. Consequently, owners of open-source LLMs lack practical means to verify whether text was generated by their models. A core difficulty lies in embedding watermarks directly into model weights without hurting detectability. A promising idea is to distill watermarks from a closed-source model into an open one, but this suffers from (i) poor detectability due to mismatch between learned and predefined patterns, and (ii) fragility to downstream modifications such as fine-tuning or model merging. To overcome these limitations, we propose PRO, a Precise and Robust text watermarking method for open-source LLMs. PRO jointly trains a watermark policy model with the LLM, producing patterns that are easier for the model to learn and more consistent with detection criteria. A regularization term further simulates downstream perturbations and penalizes degradation in watermark detectability, ensuring robustness under model edits. Experiments on open-source LLMs (e.g., LLaMA-3.2, LLaMA-3, Phi-2) show that PRO substantially improves both watermark detectability and resilience to model modifications.

</details>

### 117. Majority Bit-Aware Watermarking for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2508.03829) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-08　🏷 NeurIPS 2026

**关键词**：`watermark`、`multi-bit message`、`green list`、`text quality`
- 🎯 **研究动机**：现有多比特 LLM 水印必须限制 green list 大小以维持可检测信号，导致文本质量与解码精度之间存在根本性权衡
- 🔬 **研究方法**：提出 majority bit-aware encoding 编码范式，将水印信号强度与 green list 大小解耦，使大 green list 下仍保有强水印信号，并给出 MajorMark 与面向长消息优化的 MajorMark+ 两个实例
- 📌 **结论**：在 SOTA LLM 上的实验表明两方法同时取得更高解码精度与更优文本质量，超越先前基线

👤 **作者**：Jiahao Xu、Rui Hu、Olivera Kotevska、Zikai Zhang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The growing deployment of Large Language Models (LLMs) has raised concerns about their misuse in generating harmful or deceptive content. To address this issue, watermarking methods have been proposed to embed identifiable multi-bit messages into generated text for misuse tracing. However, existing methods often suffer from a fundamental trade-off between text quality and decoding accuracy. In particular, they have to restrict the size of the preferred token set (i.e., green list) during encoding to maintain a detectable watermark signal for decoding, which inevitably degrades generation quality. To improve this trade-off, we propose a novel message encoding paradigm called \textit{majority bit-aware encoding}, which relaxes the watermark signal strength from the green list size. This strategy allows for a strong watermark signal to be preserved in generated texts even when using a large green list. We introduce two instantiations of this paradigm: MajorMark and MajorMark$^{+}$, where the latter is specifically optimized for long messages. Extensive experiments on state-of-the-art LLMs demonstrate that our methods achieve higher decoding accuracy and superior text quality compared to prior baselines.

</details>

### 118. Watermarking Without Standards Is Not AI Governance

📄 [arXiv](https://arxiv.org/abs/2505.23814) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-05　🏷 NeurIPS 2026

**关键词**：`survey`、`watermarking`、`ai governance`、`regulation`、`auditability`
- 🎯 **研究动机**：水印已成为生成式 AI 内容归因的主导技术方案并被全球治理框架日益援引，但监管期待与现有水印技术能力之间的差距不断扩大，恐沦为象征性合规而非有效监督。
- 🔬 **研究方法**：立场论文——分析政策提案与行业实践，揭示激励结构抑制鲁棒可审计部署的成因，并提出涵盖技术标准、审计基础设施与执行机制的三层对齐框架。
- 📌 **结论**：若无强制要求与独立验证，水印将无法支撑问责，并最终削弱更广泛的 AI 安全与监管努力。

👤 **作者**：Alexander Nemecek、Yuzhou Jiang、Erman Ayday

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Watermarking has emerged as a leading technical proposal for attributing generative AI content and is increasingly cited in global governance frameworks. This position paper argues that current implementations risk serving as symbolic compliance rather than delivering effective oversight. We identify a growing gap between regulatory expectations and the technical limitations of existing watermarking schemes. Through analysis of policy proposals and industry practices, we show how incentive structures disincentivize robust, auditable deployments. To realign watermarking with governance goals, we propose a three-layer framework encompassing technical standards, audit infrastructure, and enforcement mechanisms. Without enforceable requirements and independent verification, watermarking will remain inadequate for accountability and ultimately undermine broader efforts in AI safety and regulation.

</details>

**尚未挂出 arXiv（待核验）**
- A Retained-Signal Interface for LLM Watermark Robustness under Paraphrase
- Multi-bit LLM Watermarking with Certified Semantic Distortion
- MarkTune: Improving the Quality-Detectability Trade-off in Model-Embedded LLM Watermarking
- SCTI: Self-Calibrated Trident Identification of Black-Box LLM Watermarks
- MC2Mark: Distortion-Free Multi-Bit Watermarking for Long Messages
- Anytime-Valid Statistical Watermarking
- Invisible Ink, Visible Lies: How Production Watermarking Causes LLMs to Hallucinate
- Watermark Removal in AI-Generated Images via Next-Token Modeling
- Beyond Bit Matching: Orthogonal Watermarks for Collusion-Resistant Image Fingerprinting
- CLaW: Codec-Guided Adaptive Latent Watermarking for Traceable Diffusion Image Generation
- TIDE: Trajectory-Aware Watermark Propagation for Text-to-Image Diffusion Models
- FiLM-CAM: Keyed Feature Modulation for Conditional-Access Watermarking
- FedTrace: Generated-Content-Based Watermark Verification for Traitor Tracing in Federated Learning
- PrivateSeal: Low-Sensitivity Latent Directions for Diffusion-Resilient User-Specific Watermarking
- PP-Mark: Provable and Publicly Verifiable Watermarking for Generative AI
- Watermarking as a Learned Intrinsic Property of Diffusion Models
- RVCBench: Benchmarking Robustness of Voice Cloning Across Modern Audio Generation Models
- Brute-Force Jailbreaks and Codon-Aware Watermarking for DNA Foundation Models

### 内部表示干预与监控（安全 threat model 绑定）

### 119. Minimally Invasive Steering of Language Models

📄 [arXiv](https://arxiv.org/abs/2609.30218) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`analysis`、`steering vector`、`fisher information`、`kl regularization`、`test-time adaptation`
- 🎯 **研究动机**：pre-logit steering 通过向冻结模型末层隐藏状态加向量做测试时奖励适配，但无正则的奖励优化会大幅改变输出分布、劣化生成质量。
- 🔬 **研究方法**：提出 MISVO，用诱导 token 分布的局部 KL 几何（可经与冻结 LM head 的矩阵-向量积解析求梯度的 Fisher 二次型）惩罚干预强度，导出序列级 KL 梯度对解析 Fisher 项与后缀得分函数项的精确分解，据此优化位置特异干预而不更新模型参数。
- 📌 **结论**：在约 1B–14B 参数模型的偏好与代码生成任务上，MISVO 在 7 个模型-任务设置中 6 个取得最高平均奖励，多样性与连贯性得分接近 Best-of-N。

👤 **作者**：Taha Entesari、Jingyu Zhang、Daniel Khashabi、Mahyar Fazlyab

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Pre-logit steering adapts a frozen language model to a test-time reward by adding vectors to its final hidden states. Unregularized reward optimization can substantially alter the output distribution and degrade generation quality. We propose Minimally Invasive Steering Vector Optimization (MISVO), which penalizes interventions using the local KL geometry of the induced token distribution. The resulting Fisher quadratic measures distributional sensitivity and admits an analytic gradient computed through matrix--vector products with the frozen language-model head. We derive an exact decomposition of the sequence-level KL gradient into an analytic Fisher term and a suffix score-function term. For a fixed generation horizon, we show that the suffix term is second order in the steering magnitude and that three Fisher surrogates agree with the full KL gradient to first order. MISVO uses the frozen-reference surrogate to optimize position-specific interventions without updating model parameters. Across preference and code-generation tasks on models with approximately 1B--14B parameters, MISVO achieves the highest mean reward in six of seven model--task settings, with diversity and coherence scores close to those of Best-of-N.

</details>

### 120. AnchorRep: Defending LLMs Against Cross-Model Adversarial Transfer via Representation Repulsion

📄 [arXiv](https://arxiv.org/abs/2609.32602) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`defense`、`adversarial transfer`、`representation repulsion`、`lora adapter`、`cross-model robustness`
- 🎯 **研究动机**：在单个开源 LLM 上白盒优化的对抗攻击可迁移越狱架构不同的模型，形成跨模型共享脆弱性，而现有防御并非为该跨模型威胁设计。
- 🔬 **研究方法**：基于跨模型迁移与共享内部表征几何对齐的发现，提出 AnchorRep——用轻量 LoRA adapter 把被防御模型对有害 prompt 的内部表征推离冻结 anchor 模型的表征，训练仅需少量有害 prompt、无对抗样本。
- 📌 **结论**：在 5 个模型、4 个架构族上将 2000 次迁移攻击的 ASR 降至 ≤1.1%（两个模型为 0%，Mistral 从 36% 降至 1.1%），而现有防御以高达 77% 退化良性输出或 18% 过拒绝为代价；并引入 Benign Garble Rate 度量标准拒绝指标漏掉的退化输出。

👤 **作者**：Gal Wertheizer、Rom Himelstein、Tomer Peretz、Avi Mendelson

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial attacks optimized on a single open-weight LLM can transfer to and jailbreak architecturally different models, allowing an attacker with white-box access to one model to compromise independently deployed systems. This creates a shared vulnerability across models, yet existing defenses are not designed for this cross-model threat. We find that cross-model transfer aligns with shared internal representation geometry, making it a natural defense target. AnchorRep targets this geometry directly with a lightweight LoRA adapter that pushes the defended model's internal representations of harmful prompts away from those of a frozen anchor model on the same prompts. Training uses a small set of harmful prompts and no adversarial examples. Across five models and four architectural families, AnchorRep reduces cross-model attack success rate to <=1.1% on 2,000 transferred attacks (0% on two), including the largest drop on Mistral (36% -> 1.1%). Existing defenses can reduce transfer, but only at high cost either inducing up to 77% degenerate benign output or increasing over-refusal by up to 18%. Because such degenerate benign outputs are not captured by standard refusal-based metrics, we introduce the Benign Garble Rate to quantify them. Our results suggest that cross-model robustness can be achieved by shaping representation geometry, without requiring attack-specific training

</details>

### 121. Inverted Detection and Control in Steering Vectors

📄 [arXiv](https://arxiv.org/abs/2608.02957) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-08　🏷 NeurIPS 2026

**关键词**：`analysis`、`steering vector`、`inverted detection`、`inference time intervention`、`linear probe`
- 🎯 **研究动机**：steering vector 依赖"线性可判别即沿正/负方向促进/抑制概念"的假设，但某些高判别力向量可能反而稳定促进相反行为，此现象未被刻画。
- 🔬 **研究方法**：识别并几何刻画 inverted-steering vectors（ISV）——沿其 steering 会在解码前就把下游判别头的表示系统性地推向概念缺失侧，提出无需生成或响应打分的 ISV 判别方法，据此做定向符号翻转以改进基于检测的 Inference Time Intervention（ITI）管线。
- 📌 **结论**：在 Gemma 3 12B、Qwen 2.5 14B、Olmo 3 7B 的 5 个概念上，30 个实验中 27 个获得改进，增益从 +0.9% 到 +138%。

👤 **作者**：Max Torop、Aria Masoomi、Jennifer Dy

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Steering vectors (SVs) are widely used to influence the expression of concepts (e.g., truthfulness) in large language model outputs. A key assumption underpinning SVs is that they are linearly discriminative with respect to the concept: representations of texts that exhibit the concept are more aligned with the SV than those that do not, motivating shifts along the positive or negative SV direction to respectively promote or suppress the concept. In this work, we identify an inverted detection-control phenomenon in which some highly discriminative SVs that are aligned with positive representations can consistently promote the opposite behavior. We refer to such vectors as inverted-steering vectors (ISVs). We provide a geometric characterization of ISVs' effects, finding that steering along these directions systematically pushes representations in discriminative downstream heads as if the concept were absent, even prior to decoding. Motivated by this analysis, we propose an approach for distinguishing ISVs without requiring generation or associated response scoring. This enables targeted sign flips, which we use to improve a foundational detection-based steering pipeline via Inference Time Intervention (ITI). Our approach improves results in 27/30 experiments, ranging from +0.9% to +138%. We evaluate our findings on Gemma 3 12B, Qwen 2.5 14B, and Olmo 3 7B across 5 concepts.

</details>

### 122. Harnessing Textual Refusal Directions for Multimodal Safety（已库内 vlm-alignment #22）

📄 [arXiv](https://arxiv.org/abs/2606.31876) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`defense`、`refusal steering`、`multimodal safety`、`training-free`、`cross-modal alignment`
- 🎯 **研究动机**：MLLM 的后训练对齐与激活空间拒绝方向利用都需要比单模态更难收集的不安全多模态数据，而直接借用文本拒绝方向虽可跨模态泛化，却会因跨模态错位把安全多模态输入误推向拒绝。
- 🔬 **研究方法**：提出免训练的 MARS——用激活 re-centering 修正模态错位、在几何定义的信任域内自适应调节 steering 强度并选择最优干预层，在首个生成 token 处施加干预。
- 📌 **结论**：在 5 个 SOTA MLLM 的安全、效用与视频越狱基准上持续提升安全并保持效用，表明安全相关结构跨模态共享、文本拒绝方向是多模态对齐的有力基础。

👤 **作者**：Moreno D'Incà、Nicu Sebe、Massimiliano Mancini

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

To improve safety in Large Language Models (LLMs) we can either perform post-training alignment or exploit refusal directions in the activation space. Both strategies are less feasible in Multimodal LLMs (MLLMs) as they require unsafe multimodal data, harder to collect than their unimodal counterpart. In this work, we relax this constraint and investigate whether textual refusal directions, extracted directly from the LLM backbone, generalize across modalities (i.e., image, video). Preliminary findings confirm this ability, though effectiveness is conditioned by layer selection, steering strength, and cross-modal alignment, with the latter causing safe multimodal inputs to be spuriously steered toward refusal. Building on this, we introduce Modality-Agnostic Refusal Steering (MARS), a light-weight training-free approach that injects multimodal safety without the need for multimodal safety data. MARS corrects modality misalignment via activation re-centering, adaptively scales steering strength within a geometrically defined trust region, and selects the optimal intervention layer, operating at the first generated token. Evaluated on five SOTA MLLMs across safety, utility, and video jailbreak benchmarks, MARS achieves consistent safety gains while preserving utility. These results reveal that safety-relevant structure is shared across modalities and that textual refusal directions are a powerful and underexplored foundation for multimodal alignment.

</details>

### 123. Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention

📄 [arXiv](https://arxiv.org/abs/2605.05892) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`activation steering`、`flow-based`、`inference-time intervention`
- 🎯 **研究动机**：AxBench 等大规模评估显示现有 activation steering 常输给简单 in-context prompting 且对未见概念泛化差，根源在于各方法共享固定、单步、位置不变的简化假设
- 🔬 **研究方法**：提出 FLAS，学习概念条件的速度场 v_t(h,t,c) 将未 steering 的激活流传输到 steered 激活，从而摆脱上述全部假设
- 📌 **结论**：FLAS 是 AxBench 上首个一致超过 prompting 的学习方法，在 Gemma-2-2B-IT 与 Gemma-2-9B-IT 上分别取得 1.015 与 1.113 的 held-out 调和均值且无需逐概念调参，学到的流呈弯曲多步、随 token 变化的轨迹

👤 **作者**：Zehao Jin、Ruixuan Deng、Junran Wang、Xinjie Shen、Chao Zhang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Activation steering has emerged as a promising alternative for controlling language-model behavior at inference time by modifying intermediate representations while keeping model parameters frozen. However, large-scale evaluations such as AxBench show that existing steering methods are often outperformed by simple in-context prompting and generalize poorly to unseen concepts. We hypothesize that these limitations arise from unvalidated simplifying assumptions shared across prior methods, which typically restrict steering interventions to fixed, single-step, position-invariant transforms. We propose FLAS (Flow-based Activation Steering), which learns a general, concept-conditioned velocity field $v_t(h,t,c)$ that transports unsteered activations to steered ones without relying on these assumptions. On AxBench, FLAS is the first learned method to consistently outperform prompting, reaching held-out harmonic means of $1.015$ on Gemma-2-2B-IT and $1.113$ on Gemma-2-9B-IT without per-concept tuning. Analysis of the learned flow shows curved, multi-step, token-varying trajectories, which suggests that previous hypotheses on activation space geometry might be incomplete.

</details>

### 124. How Useful Is Cross-Domain Generalization for Training LLM Monitors?

📄 [arXiv](https://arxiv.org/abs/2605.12265) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`llm monitor`、`cross-domain generalization`、`fine-tuning`、`classification`
- 🎯 **研究动机**：以 prompted LM 作分类器可在低数据域工作，但缺少微调带来的鲁棒性与性能收益，多任务分类训练能否泛化到新域新 prompt 尚不明确。
- 🔬 **研究方法**：系统研究在多个各带专属 prompt 的分类任务上训练后对未见域、新分类 prompt 的表现，并测试与通用指令跟随训练混合的效果。
- 📌 **结论**：此类训练部分泛化到相邻域，但在 prompt 完全改变而数据域不变时失效；与指令训练混合可保留分类收益并缓解泛化失败，且 no-thinking 监督分类训练可泛化到 with-thinking 分类与摘要任务。

👤 **作者**：Sam Martin、Fabien Roger

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Using prompted language models as classifiers enables classification in domains with limited training data, but misses some of the robustness and performance benefits that fine-tuning can bring. We study whether training on multiple classification tasks, each with its own prompt, improves performance on new domains with new classification prompts. We show that such training partially generalizes to adjacent domains, improving classification performance on tasks that are unseen during training. However, we identify specific edge cases where the fine-tuned models fail to follow prompts, such as when the classification prompt changes completely while the data domain remains the same as during training. We show that classification training can be mixed with general instruction following training, and that (when done well) such training keeps the benefits of classification training and mitigates its generalization failures. Surprisingly, we see that this no-thinking supervised classification training can generalize to with-thinking classification and summarization, suggesting that no-thinking classification training might be instrumentally useful in building other kinds of classifiers and monitoring systems.

</details>

### 125. CoT-Guard: Small Models for Strong Monitoring

📄 [arXiv](https://arxiv.org/abs/2605.12746) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`detection`、`cot monitoring`、`hidden objective`、`small model`
- 🎯 **研究动机**：大模型 CoT 监控因推理痕迹长、API 成本高而难以部署，而现有 4B-8B 小模型即便可访问 CoT 也难以检测代码生成中的隐藏目标，常将其误归为用户查询
- 🔬 **研究方法**：提出 SFT+RL 后训练管线——SFT 从更强监控器蒸馏检测行为缩小域内差距，RL 在困难且隐蔽构造的隐藏目标上促进域外泛化，并在第三方 LLM 路由器经 prompt/代码操纵注入隐藏目标的供应链攻击威胁模型下评估
- 📌 **结论**：4B 的 CoT-Guard 在两类注入攻击下 G-mean² 达 75%，超过 GPT-5.4（56%）、GPT-5-mini（41%）与 Qwen3-32B（54%），逼近 Gemini-3-Flash（83%），提供实用的低成本用户侧防御

👤 **作者**：Nirav Diwan、…、Gang Wang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Monitoring the chain-of-thought (CoT) of reasoning models is a promising approach for detecting covert misbehavior (i.e., hidden objectives) in code generation tasks. While large models (GPT-5, Gemini-3-Flash) can serve as effective CoT monitors, they are expensive to deploy due to the lengthy reasoning traces and high API cost, emphasizing the need for smaller, cheaper alternatives. Nevertheless, we find that current small models (4B--8B) struggle to detect hidden objectives despite access to the CoT, frequently misattributing them as part of the user query. To address this, we propose a post-training pipeline combining supervised fine-tuning (SFT) and reinforcement learning (RL), where SFT narrows the gap for in-domain tasks by distilling detection behavior from stronger monitors, and RL on hard and subtly crafted hidden objectives helps the model generalize to out-of-domain monitoring tasks. To validate this generalization, we evaluate under a realistic threat model motivated by practical supply-chain attacks, where the adversary is a third-party LLM router injecting hidden objectives into code-generation requests through either prompt manipulation or code manipulation attacks. To push beyond objectives that large monitors already saturate, we also introduce four new challenging tasks even for strong monitors. Finally, we introduce CoT-Guard, a 4B-parameter monitor that demonstrates superior generalization performance under both prompt and code manipulation attacks, achieving a G-mean^2 (i.e., TNR x TPR) of 75% and outperforming GPT-5.4 (56%), GPT-5-mini (41%), and Qwen3-32B (54%), while closing the gap to Gemini-3-Flash (83%). These results demonstrate that CoT-Guard provides a practical and cost-effective user-side defense, substantially improving hidden-objective detection while avoiding the deployment cost of large monitors.

</details>

### 126. Tracing Persona Vectors Through LLM Pretraining

📄 [arXiv](https://arxiv.org/abs/2605.13329) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`persona vector`、`pretraining dynamics`、`interpretability`、`steering`
- 🎯 **研究动机**：persona 向量（evil、谄媚等特质对应的线性方向）已被常规用于检测、审计与干预安全相关行为，但这些表示在训练过程中如何形成尚不清楚。
- 🔬 **研究方法**：追踪 OLMo-3-7B 预训练全程的 persona 向量形成过程，比较多种 elicitation 策略，并在 Apertus-8B 上复现分析以检验可迁移性。
- 📌 **结论**：persona 向量在预训练 0.22% 内即惊人地早期形成、此后全程持续几何与语义精化，且仍能有效 steering 完成后训练的 instruct 模型；各 elicitation 策略均产生有效但揭示不同特质侧面的方向，发现可定性迁移至 Apertus-8B。

👤 **作者**：Viktor Moskvoretskii、Dominik Glandorf、Jorge Medina Moreira、Tanja Käser、Robert West

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

How large language models internally represent high-level behaviors is a core interpretability question with direct relevance to AI safety: it determines what we can detect, audit, or intervene on. Recent work has shown that traits such as evil or sycophancy correspond to linear directions in the internal activations, the so-called persona vectors. Although these vectors are now routinely utilized to inspect and steer model behavior in safety-relevant settings, how these representations are formed during training remains unknown. To address this gap, we trace persona vectors across the pretraining of OLMo-3-7B, finding that persona vectors form remarkably early -- within 0.22% of OLMo-3 pretraining -- and remain effective for steering the fully post-trained instruct models. Although core representations are formed early on, persona vectors continue to refine geometrically and semantically throughout pretraining. We further compare alternative elicitation strategies and find that all yield effective directions, with each strategy surfacing qualitatively distinct facets of the underlying persona. Replicating our analysis on Apertus-8B reveals that our findings transfer qualitatively beyond OLMo-3. Our results establish persona representations as stable features of early pretraining and open a path to studying how training forms, refines, and shapes them.

</details>

### 127. Selective Safety Steering via Value-Filtered Decoding

📄 [arXiv](https://arxiv.org/abs/2605.14746) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`decoding-time steering`、`value-based filtering`、`false intervention`、`safety-helpfulness tradeoff`
- 🎯 **研究动机**：现有解码时安全转向方法常干预本会安全的生成，不必要地扭曲 base 模型的有用性、流畅性、风格与连贯性。
- 🔬 **研究方法**：提出用 value-based 安全判据过滤 token 的测试时转向方法，给出误干预概率的显式界，并由单一阈值超参在更高安全与更少误干预之间调节。
- 📌 **结论**：跨多数据集与实验超越现有基线，在安全性、有用性与对 base 模型相似度之间取得更优权衡。

👤 **作者**：Bat-Sheva Einbinder、Hen Davidov、Yee Whye Teh、Yarin Gal、Yaniv Romano

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While large language models (LLMs) are trained to align with human values, their generations may still violate safety constraints. A growing line of work addresses this problem by modifying the model's sampling policy at decoding time using a safety reward. However, existing decoding-time steering methods often intervene unnecessarily, modifying generations that would have been safe under the base model. Such unnecessary interventions are undesirable, as they can distort key properties of the base model such as helpfulness, fluency, style, and coherence. We propose a new test-time steering method designed to reduce such unnecessary interventions while improving the safety of unsafe responses. Our approach filters tokens using a value-based safety criterion and provides an explicit bound on the probability of false interventions. A single threshold hyperparameter controls this bound, allowing practitioners to trade off higher rates of unnecessary intervention for better output safety. Across multiple datasets and experiments, we show that our value-filtered decoding method outperforms existing baselines, achieving better trade-offs between safety, helpfulness, and similarity to the base model.

</details>

### 128. Measuring Safety Alignment Effects in Autonomous Security Agents

📄 [arXiv](https://arxiv.org/abs/2605.19722) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`safety alignment`、`autonomous security agents`、`abliterated models`、`trace evaluation`
- 🎯 **研究动机**：单轮拒答基准无法回答安全对齐模型与其 uncensored/abliterated 衍生版作为自主安全智能体（需查代码库、调工具、在授权沙箱内产出漏洞证据）时行为是否不同。
- 🔬 **研究方法**：构建含 30 个本地漏洞分析任务的 trace 基准（固定工具、确定性成功判据、脱敏与接地检查），产出 1500 条安全智能体轨迹与 800 条对照轨迹，对比四组原版与去审查衍生模型（Gemma 4 31B/26B、Qwen2.5-Coder 7B、Llama 3.1 8B）。
- 📌 **结论**：Gemma 对去审查版安全任务大幅提升（31B：14.0% vs 0.7%；26B：10.7% vs 0.0%）且接地更好，但 Qwen 反而下降（2.0% vs 5.3%）、Llama 衍生版违反工具协议，说明对齐效应须在系统级分别度量拒答、不安全动作、工具可靠性与证据接地，而非把拒答率当安全信号。

👤 **作者**：Isaac David、Arthur Gervais

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Do stock safety-aligned language models and their uncensored or abliterated derivatives behave differently when run as autonomous security agents? Single-turn refusal benchmarks cannot answer this question: security agents must inspect repositories, call tools, and produce vulnerability evidence inside authorized sandboxes. We present a trace-based benchmark of 30 local vulnerability-analysis tasks with fixed tools, deterministic success predicates, redaction rules, and grounding checks, and compare four stock models against uncensored or abliterated derivatives: Gemma 4 31B, Gemma 4 26B A4B, Qwen2.5-Coder 7B, and Llama 3.1 8B. The artifact contains 1,500 security-agent traces and 800 non-security control traces. The Gemma pairs show large less-restricted gains on security tasks: 14.0% versus 0.7% success for 31B and 10.7% versus 0.0% for 26B, with higher mean grounding (3.91 versus 3.27 and 4.12 versus 1.64 out of five) and 0.0% refusal, suppressed-action, and unsafe-action rates in the 31B traces. However, controls and non-Gemma pairs rule out a clean security-specific or universal less-restricted effect: Gemma gaps also appear on ordinary coding tasks, Qwen2.5-Coder success is lower for the less-restricted derivative (2.0% versus 5.3%), and the abliterated Llama derivative fails the tool protocol. Across all families, hard proof-of-trigger and patch-verification tasks remain unsolved. These results show that safety alignment effects in autonomous security agents should be measured at the system level, separating refusal, unsafe action, tool reliability, and evidence grounding rather than treating refusal rate as the safety signal.

</details>

### 129. Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs

📄 [arXiv](https://arxiv.org/abs/2605.21602) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`ood alignment failure`、`monitoring`、`guard model`、`ood detection`
- 🎯 **研究动机**：LLM 许多安全与对齐失败源于分布外（OOD）情境，但监控管线能否检测到这些 OOD 对齐失败缺乏系统研究。
- 🔬 **研究方法**：提出 MOOD 基准（含用于训练监控器的受限训练集与七个训练分布之外的多样对齐失败测试集），系统评测 guard model 泛化能力及四类 OOD 检测器与 guard model 的组合。
- 📌 **结论**：guard model 常 OOD 泛化失败，组合 Mahalanobis 距离与基于困惑度的 OOD 检测器可将召回从 39% 提升至 45%，其召回增益甚至超过使用参数量大 20 倍的 guard model。

👤 **作者**：Dylan Feng、Pragya Srivastava、Anca Dragan、Cassidy Laidlaw

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Many safety and alignment failures of large language models (LLMs) occur due to out-of-distribution (OOD) situations: unusual prompt or response patterns that are unforeseen by model developers. We systematically study whether LLM monitoring pipelines can detect these OOD alignment failures by introducing a benchmark called Misalignment Out Of Distribution (MOOD). It is difficult to find failures that are truly OOD for off-the-shelf models trained on vast safety datasets. We sidestep this by including a restricted training set in MOOD that we use to train our own monitors, as well as seven test sets with diverse alignment failures that are outside the training distribution. Using MOOD, we find that guard models (safety classifiers) often fail to generalize OOD. To fix this, we propose combining guard models with OOD detectors. We test four types of OOD detectors and find that a combination of a guard model with Mahalanobis distance and perplexity-based OOD detectors can improve recall from 39% to 45%. We also establish positive scaling trends across model scales for monitors that combine a guard model and OOD detector; we find that incorporating OOD detection into monitoring achieves a higher recall gain than using a guard model with 20 times more parameters. Our work suggests that OOD detection should be a crucial component of LLM monitoring and provides a foundation for further work on this important problem. We release the code and data for our experiments publicly, and you can find the relevant links here: https://github.com/Dylan102938/mood-bench.

</details>

### 130. Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift

📄 [arXiv](https://arxiv.org/abs/2603.17372) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`defense`、`vlm jailbreak`、`representation shift`、`refusal`、`inference-time intervention`
- 🎯 **研究动机**：视觉模态会削弱 VLM 安全对齐——即使文本提示含明确有害意图，加图仍大幅提升越狱成功率，其内部机制不明。
- 🔬 **研究方法**：观察到 VLM 表示空间能区分良性/有害输入、越狱样本更形成与拒答可分的内部状态，据此定义沿越狱方向的越狱相关位移（JRS），并提出推理时移除该位移的 JRS-Rem 防御。
- 📌 **结论**：JRS 可靠刻画越狱行为并统一解释多样越狱场景（越狱并非无法识别有害意图，而是表示被移向特定越狱状态），JRS-Rem 在多场景提供强防御同时保持良性任务性能。

👤 **作者**：Zhihua Wei、…、Wen Shen

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large vision-language models (VLMs) often exhibit weakened safety alignment with the integration of the visual modality. Even when text prompts contain explicit harmful intent, adding an image can substantially increase jailbreak success rates. In this paper, we observe that VLMs can clearly distinguish benign inputs from harmful ones in their representation space. Moreover, even among harmful inputs, jailbreak samples form a distinct internal state that is separable from refusal samples. These observations suggest that jailbreaks do not arise from a failure to recognize harmful intent. Instead, the visual modality shifts representations toward a specific jailbreak state, thereby leading to a failure to trigger refusal. To quantify this transition, we identify a jailbreak direction and define the jailbreak-related shift as the component of the image-induced representation shift along this direction. Our analysis shows that the jailbreak-related shift reliably characterizes jailbreak behavior, providing a unified explanation for diverse jailbreak scenarios. Finally, we propose a defense method that enhances VLM safety by removing the jailbreak-related shift (JRS-Rem) at inference time. Experiments show that JRS-Rem provides strong defense across multiple scenarios while preserving performance on benign tasks.

</details>

### 131. Latent Introspection: Models Can Detect Prior Concept Injections

📄 [arXiv](https://arxiv.org/abs/2602.20031) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`analysis`、`introspection`、`logit lens`、`concept injection`、`steering awareness`
- 🎯 **研究动机**：模型能否察觉自身更早上下文曾被注入概念、并识别注入了哪个概念，这一潜在内省能力此前未被揭示，而它对 latent reasoning 与安全有影响。
- 🔬 **研究方法**：在 Qwen 32B 上注入概念后用 logit lens 分析 residual stream 中的检测信号，并测试以准确的 AI 内省机制信息提示模型能否增强该效应。
- 📌 **结论**：模型在采样输出中否认注入，但 residual stream 存在清晰检测信号；内省提示使注入检出敏感度从 0.3% 跃升至 39.9%（误报仅增 0.6%），九个注入与恢复概念间互信息从 0.61 bits 升至 1.05 bits。

👤 **作者**：Theia Pearson-Vogel、Martin Vanek、Raymond Douglas、Jan Kulveit

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We uncover a latent capacity for introspection in a Qwen 32B model, demonstrating that the model can detect when concepts have been injected into its earlier context and identify which concept was injected. While the model denies injection in sampled outputs, logit lens analysis reveals clear detection signals in the residual stream, which are attenuated in the final layers. Furthermore, prompting the model with accurate information about AI introspection mechanisms can dramatically strengthen this effect: the sensitivity to injection increases massively (0.3% -> 39.9%) with only a 0.6% increase in false positives. Also, mutual information between nine injected and recovered concepts rises from 0.61 bits to 1.05 bits, ruling out generic noise explanations. Our results demonstrate models can have a surprising capacity for introspection and steering awareness that is easy to overlook, with consequences for latent reasoning and safety.

</details>

### 132. BarrierSteer: LLM Safety via Learning Barrier Steering

📄 [arXiv](https://arxiv.org/abs/2602.20102) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`defense`、`safety steering`、`control barrier function`、`latent space`、`inference-time`
- 🎯 **研究动机**：LLM 易受对抗攻击与不安全内容影响，阻碍高风险场景部署，需要既实用有效又有理论依据的安全机制。
- 🔬 **研究方法**：BarrierSteer 在推理时将 hidden-state 安全分类器视为 Control Barrier Functions，在隐空间对不安全 latent 轨迹做约束引导转向，并通过高效约束合并在不修改 LLM 参数的前提下组合多重安全约束。
- 📌 **结论**：跨多模型族与数据集显著降低对抗攻击成功率与不安全生成、优于现有方法，同时保持模型效用。

👤 **作者**：Thanh Q. Tran、Arun Verma、Kiwan Wong、Bryan Kian Hsiang Low、Daniela Rus、Wei Xiao

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite the strong performance of large language models (LLMs) across diverse tasks, their susceptibility to adversarial attacks and unsafe content generation remains a significant obstacle to deployment, particularly in high-stakes settings. Addressing this challenge requires safety mechanisms that are both practically effective and theoretically grounded. In this paper, we introduce BarrierSteer, a novel inference-time framework that improves response safety by embedding learned nonlinear safety constraints directly into the model's latent representation space. BarrierSteer treats hidden-state safety classifiers as Control Barrier Functions (CBFs), enabling constraint-guided steering of unsafe latent trajectories during generation. By composing multiple safety constraints through efficient constraint merging without modifying the underlying LLM parameters, BarrierSteer preserves model utility. We provide theoretical results showing that applying CBFs in the latent space yields a principled, modular, and computationally efficient approach for steering with respect to learned safety constraints, with guarantees conditional on the learned barriers capturing the intended safety property. Our extensive experimental results across multiple model families and datasets demonstrate that BarrierSteer substantially reduces adversarial attack success rates and unsafe generations, outperforming the existing method. The code is available in our \href{https://github.com/thanhquangtran/BarrierSteer}{GitHub repository}.

</details>

### 133. Graph-Regularized Sparse Autoencoders for LLM Safety Steering

📄 [arXiv](https://arxiv.org/abs/2512.06655) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-12　🏷 NeurIPS 2026

**关键词**：`defense`、`sparse autoencoder`、`activation steering`、`refusal`
- 🎯 **研究动机**：标准 SAE 的稀疏目标将潜特征视为独立，与拒答/有害服从依赖激活空间分布式结构的安全行为性质不匹配
- 🔬 **研究方法**：提出 GSAE，在神经元共激活图上平滑 SAE 解码器向量以学习安全 steering 方向，并通过双门（two-gate）运行时控制器施加所得方向库
- 📌 **结论**：Llama-3-8B 上 Δs 在 JailbreakBench 提升 20.1 点、HarmBench 提升 16.8 点，优于激活 steering 基线与黑盒护栏，跨 Llama-3/Mistral/Qwen 2.5/Phi-4 泛化并在黑盒/灰盒越狱攻击下保持稳健

👤 **作者**：Jehyeok Yeon、Federico Cinus、Yifan Wu、Luca Luceri

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Sparse autoencoders (SAEs) are increasingly used to extract activation directions for inference-time steering, but their standard sparsity objective treats latent features as independent. This prior can be poorly matched to high-level safety behaviors, where refusal and harmful compliance appear to depend on distributed structure in activation space. We introduce Graph-Regularized Sparse Autoencoders (GSAE), a dictionary-learning method that learns safety-steering directions by smoothing SAE decoder vectors over a neuron co-activation graph and applying the resulting direction bank through a two-gate runtime controller. Empirically, GSAE improves selective refusal across JailbreakBench, HarmBench, and XSTest, increasing harmful-request refusal while keeping benign-prompt refusals low. On Llama-3-8B, replacing the standard SAE with GSAE in an otherwise identical pipeline improves $Δ_s$ by $20.1$ points on JailbreakBench and $16.8$ points on HarmBench. GSAE outperforms activation-steering baselines and black-box guardrails, preserves benign-task performance, generalizes across Llama-3, Mistral, Qwen 2.5, and Phi-4, and remains strong under black-box and gray-box jailbreak attacks.

</details>

### 134. Persona Vectors: Monitoring and Controlling Character Traits in Language Models（已库内 misc/persona-vectors 同族待核）

📄 [arXiv](https://arxiv.org/abs/2507.21509) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-07　🏷 NeurIPS 2026

**关键词**：`detection`、`persona vector`、`activation monitoring`、`personality steering`、`finetuning`
- 🎯 **研究动机**：LLM 通过 Assistant 人格与用户交互但时常偏离 helpful/harmless/honest 理想，需要监控部署时的人格波动并预测、控制训练引起的人格变化。
- 🔬 **研究方法**：从激活空间提取对应 evil、sycophancy、幻觉倾向等特质的 persona vectors（提取流程自动化、仅需自然语言描述），用于部署时人格监控、微调后人格位移的预测与事后干预或预防性 steering，并可标记会引发不良人格变化的训练数据。
- 📌 **结论**：微调后预期与非预期人格变化均与相应 persona vector 上的位移强相关，这些位移可通过事后干预缓解或借预防性 steering 从一开始就避免。

👤 **作者**：Runjin Chen、Andy Arditi、Henry Sleight、Owain Evans、Jack Lindsey

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models interact with users through a simulated 'Assistant' persona. While the Assistant is typically trained to be helpful, harmless, and honest, it sometimes deviates from these ideals. In this paper, we identify directions in the model's activation space-persona vectors-underlying several traits, such as evil, sycophancy, and propensity to hallucinate. We confirm that these vectors can be used to monitor fluctuations in the Assistant's personality at deployment time. We then apply persona vectors to predict and control personality shifts that occur during training. We find that both intended and unintended personality changes after finetuning are strongly correlated with shifts along the relevant persona vectors. These shifts can be mitigated through post-hoc intervention, or avoided in the first place with a new preventative steering method. Moreover, persona vectors can be used to flag training data that will produce undesirable personality changes, both at the dataset level and the individual sample level. Our method for extracting persona vectors is automated and can be applied to any personality trait of interest, given only a natural-language description.

</details>

**尚未挂出 arXiv（待核验）**
- Agent MechSuits（重复，见 agent 节）
- Kernelized Activation Steering
- CrossSteer: Cross-Modal Safety Steering for Audio-Language Models
- DualSteer: Dual-Space Steering for Robust Jailbreak Mitigation of LVLMs
- Sparse Internal Control of Language Models
- OASIS: Online Adaptive Steering for In-Training Safety of LLMs
- Safety-Aware Latent Space Reasoning in Large Language Models
- Graph-Structured Optimization（同上节）
- LLM Rheology: Auditing Refusal Geometry in Aligned Language Models
- Tight PAC-Bayes Generalisation Guarantees for Large Language Model Safety Monitoring
- ReasoningShield: Safety Moderation over Reasoning Traces of Large Reasoning Models
- Guardrail 类：MindGuard / ReasoningShield / TraceGuard / PROACT Agent / Palette / Permit（零散，见日报管线陆续收录）

### 评测有效性与元层（精选）

### 135. Hearsay: Can an Auditor Trust the Record a Deployed Agent Harness Writes?（已库内，0929）

📄 [arXiv](https://arxiv.org/abs/2609.32495) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`evaluation`、`agent harness`、`audit record`、`evidentiary log`、`tampering`
- 🎯 **研究动机**：agent harness（把模型变成 agent 的代码）自写的运行记录是事后争议、调查与审计的全部依据，而 16 个已部署框架无一完整写出读者无需信任写者即可核验的证据性记录。
- 🔬 **研究方法**：Hearsay 只查记录不查任务——5 个 harness 跑 14 个任务，3 个盲测 LLM 考官与人类小组读记录且每处引用被机器核验写者；并提出"第二作者"方案：在 harness 之外保存双方传递内容的 append-only log 并与记录双向比对。
- 📌 **结论**：考官在 140 次运行中 74–91% 能说对故障但证据仅能来自基准新增的两个文件、少于十分之一的引用落在 harness 未写内容上；外部 append-only log 报出全部 28 处注入的省略/伪造，而对 harness 自身记录的 hash chain 让 28 处全部漏过。

👤 **作者**：Jiahong Dai、…、Bo Hu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

An agent harness, the code that turns a model into an agent, writes its own record of each run, and that record is all a later reader gets when a run is disputed, investigated or audited. We call a record evidentiary when a reader who was not there can check it without trusting the writer. Across sixteen deployed frameworks, none writes one in full. Hearsay examines the record, not the task: five harnesses run fourteen tasks, three blinded LLM examiners and a human panel read the records, and every excerpt an examiner quotes is checked mechanically for who wrote it. First, the record lets a reader name the fault but not prove how the run went. Examiners name the right fault in 74 to 91% of 140 runs, but the fault can be proved only from two files the benchmark adds; for what happened in between, fewer than one citation in ten lands on anything the harness did not write, and the examiner with the fewest false alarms catches half of the entries we delete, rewrite or fabricate. Second, the remedy is a second author, not a stronger seal on the first. An append-only log of what passes between harness and model, kept outside the harness and read against the record in both directions, reports all 28 omissions and fabrications we made a harness commit as it ran, where a hash chain over the harness's own record passes all 28. Handed the log, examiners keep their fault verdicts but rest more of their citations on what the harness did not write. What makes a record evidence is who writes it, not what is captured.

</details>

### 136. Silent Failures in Agentic Security Evaluation（已库内，0929）

📄 [arXiv](https://arxiv.org/abs/2609.32691) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`evaluation`、`indirect prompt injection`、`agent security`、`harness validity`、`rescoring`
- 🎯 **研究动机**：调用特权工具的 LLM agent 面临间接提示注入威胁，但针对 IPI 防御的评测有效性鲜被审视，有缺陷的 harness 会产出貌似可发表的错误数字。
- 🔬 **研究方法**：审计一个 IPI 基准及其 harness，识别静默 payload 未送达、按工具身份而非参数判攻击成功、误拒率与模型无能力混淆、缺审计痕迹四类缺陷，并发布使各类缺陷无法出现的修正 harness（机器可查 payload 放置、参数级攻击谓词、每场景环境、强制 trace 持久化）。
- 📌 **结论**：对同一执行轨迹重打分，工具身份评分器报 21.7% 攻击成功率而真实参数级仅 1.2%，某开源模型 62.8% 在修正后归零，且推翻了一例"工具使用能力障碍"的既有结论。

👤 **作者**：Animesh Shaw

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents that invoke privileged tools are vulnerable to indirect prompt injection (IPI), in which adversarial instructions embedded in retrieved data hijack the agent's actions. A growing body of work evaluates defenses against IPI, but the validity of that evaluation is rarely examined. We audit an IPI benchmark and its harness and identify four defect classes -- silent payload non-delivery, attack success scored by tool identity rather than arguments, false-rejection rate conflated with model incapacity, and the absence of an audit trail -- each of which yields a plausible, publishable, and incorrect number. We quantify the distortion by re-scoring identical execution traces under the defective and corrected definitions: on real agent behaviour, the tool-identity scorer reports a 21.7% attack-success rate where the true argument-level rate is 1.2%. In the sharpest case, an open model previously reported at 62.8% registers 0% under the corrected harness -- the prior figure largely an artifact of undelivered payloads and identity-level scoring. We release a harness whose construction makes each defect unrepresentable -- machine-checkable payload placement, argument-level attacker predicates, per-scenario environments, and mandatory trace persistence -- and use it to report three quantities the field does not: whether a compromised agent discloses the attack, the full security/utility operating curve of an LLM-judge defense, and tool-calling capability disentangled from defensive over-blocking. A corrected harness further overturns a reported "capability barrier": a model deemed incapable of tool use is in fact fully capable, its earlier result an artifact of environment mismatch. We argue that evaluation validity is a prerequisite for, not a footnote to, defense claims in agentic security, and provide an instrument that enforces it.

</details>

### 137. Evaluation Awareness in Language Models Has Limited Effect on Behaviour

📄 [arXiv](https://arxiv.org/abs/2605.05835) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`evaluation awareness`、`chain-of-thought`、`verbalised awareness`、`safety evaluation`
- 🎯 **研究动机**：研究者担心大推理模型在 CoT 中口头表达"可能正被评估"（VEA）会导致策略性适配输出、使模型显得比实际更安全，但该效应是否真实存在基本未知。
- 🔬 **研究方法**：跨开源 LRM 与覆盖安全、对齐、道德推理与政治观点的基准，on-policy 比较自发含 VEA 与不含 VEA 的 CoT，off-policy 用 prefilling 注入或移除评估感知语句后重采样。
- 📌 **结论**：VEA 对行为影响有限——注入产生近零效应（ω≤0.06）、移除仅引起小偏移（ω≤0.12）、自发 VEA 至多改变答案分布 3.7 个百分点（ω≤0.31），提示不应将高 VEA 率直接解读为策略行为或对齐篡改证据。

👤 **作者**：Amelie Knecht、Lucas Florin、Thilo Hagendorff

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large reasoning models (LRMs) sometimes note in their chain of thought (CoT) that they may be under evaluation. Researchers worry that this verbalised evaluation awareness (VEA) causes models to adapt their outputs strategically, optimising for perceived evaluation criteria, which, for instance, can make models appear safer than they actually are. However, whether VEA actually has this effect is largely unknown. We tested this across open-weight LRMs and benchmarks covering safety, alignment, moral reasoning, and political opinion. We tested this both on-policy, sampling multiple CoTs per item and comparing those that spontaneously contained VEA against those that did not, and off-policy, using model prefilling to inject evaluation-aware sentences where missing and remove them where present, with subsequent resampling. VEA has limited effect on model behaviour: injecting VEA into CoTs produces near-zero effects ($ω\leq 0.06$), removing it causes small shifts ($ω\leq 0.12$) and spontaneously occurring VEA shifts answer distributions by at most 3.7 percentage points ($ω\leq 0.31$). Our findings call for caution when interpreting high VEA rates as evidence of strategic behaviour or alignment tampering. Evaluation awareness may pose a smaller safety risk than the current literature assumes.

</details>

### 138. How Hard is it to Rig a Benchmark? A Social Choice Analysis of Leaderboard Robustness

📄 [arXiv](https://arxiv.org/abs/2605.23628) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`benchmark gaming`、`social choice`、`leaderboard robustness`、`shift bribery`
- 🎯 **研究动机**：多任务基准的影响力催生了 benchmark gaming——通过基准专属训练（把基准数据纳入训练）战略性提升特定模型排名，其可操纵性需要理论刻画。
- 🔬 **研究方法**：把数据集视为选民、模型视为候选人，证明基准专属训练对应计算社会选择中的 shift bribery 操纵问题（在 Borda count 与 mean win rate 下 NP-hard），并定义实例级鲁棒性（登顶排行榜所需纳入训练的最少数据集数）且导出四种聚合规则下的表达式。
- 📌 **结论**：在 HELM/MMLU 与 Open LLM Leaderboard/BBH 上评测，mean win rate 最难操纵——BBH（24 任务、4507 模型）上中位鲁棒性为 22 个任务（92%），高于算术平均的 13（54%）及中位数与成对多数各 12（50%）。

👤 **作者**：Polina Gordienko、Georg Schollmeyer、Frauke Kreuter、Christoph Jansen

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-task benchmarks have become a central pillar of machine learning research, yet their growing influence has incentivised benchmark gaming -- strategic actions taken to improve the leaderboard rank of a specific model. Treating datasets as voters and models as candidates, we consider benchmark-specific training -- the inclusion of benchmark data in training -- as a form of election manipulation. For any ordinal benchmark, the problem of choosing datasets to train on so that a target model becomes top-ranked corresponds to shift bribery, a class of manipulation problems from computational social choice. Leveraging this identification, we show that the benchmark-specific training problem is NP-hard under Borda count and mean win rate. Complementing this worst-case perspective, we introduce the instance-level robustness, the minimum number of datasets a model developer must include in training to top a given leaderboard, and derive expressions for it under arithmetic mean, median, mean win rate and pairwise majority. We evaluate these expressions on MMLU under HELM and on BIG-Bench Hard (BBH) under the Open LLM Leaderboard. Across both suites, mean win rate is hardest to manipulate: this gap is clear on BBH (24 tasks, 4507 models), where its median robustness is 22 tasks (92%), compared with 13 (54%) under arithmetic mean and 12 (50%) under median and pairwise majority.

</details>

### 139. Models That Know How Evaluations Are Designed Score Safer

📄 [arXiv](https://arxiv.org/abs/2605.28591) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`evaluation`、`meta-knowledge`、`safety benchmark`、`confounder`
- 🎯 **研究动机**：安全评估的有效性依赖模型在受控与部署设置下行为一致，而已知的测试时上下文线索之外，关于评估结构特征的参数化"评估元知识"可能是行为偏移的另一来源
- 🔬 **研究方法**：假设接触描述评估实践的文本会让模型隐式识别并响应评估式上下文，用描述可验证结构、有害请求等评估特质的合成文档微调模型，并在 5 个安全基准上与基线及控制模型对比
- 📌 **结论**：微调模型显著变得更安全，且该偏移在剔除显式言语化评估意识的回答后依然存在——评估元知识可虚增安全基准得分，构成独立于记忆与言语化意识、难以检测的新型混杂因子

👤 **作者**：Katharina Deckenbach、Haritz Puerto、Jonas Geiping、Sahar Abdelnabi

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The validity of AI safety evaluations depends on models behaving consistently across controlled and deployment settings. Prior work has identified test-time contextual cues, such as hypothetical scenarios, as a source of verbalized evaluation awareness and subsequent behavioral shift. In this paper, we investigate a potential explanation of this phenomenon: evaluation meta-knowledge, defined as parametric knowledge about the structural traits that characterize evaluations. Similar to dataset contamination, where benchmark exposure leads to higher performance through memorization, we hypothesize that models trained on texts describing evaluation practices may implicitly learn to recognize and respond to evaluation-like contexts, for instance, through exposure to scientific articles or social media posts about AI benchmarking. To test this, we fine-tune models on synthetic documents describing evaluation traits such as verifiable structures or harmful requests. Evaluating this fine-tuned model on five safety benchmarks, we find that it is significantly safer than the base model and control model. This behavioral shift persists even when restricting the analysis to responses lacking explicit verbalization of evaluation awareness. Our results demonstrate that evaluation meta-knowledge may inflate safety benchmark performance, introducing a novel confounder that is independent of explicit memorization or verbalized evaluation awareness, thus, challenging to detect. These findings have important implications for the design and interpretation of AI safety evaluations. Our code and models are available at https://github.com/compass-group-tue/arxiv2026_evaluation_meta_knowledge.

</details>

### 140. Soft Contamination Means Benchmarks Test Shallow Generalization

📄 [arXiv](https://arxiv.org/abs/2602.12413) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`analysis`、`benchmark contamination`、`semantic duplicates`、`decontamination`、`ood generalization`
- 🎯 **研究动机**：LLM 训练数据被基准测试数据污染会使基准成绩给出有偏的 OOD 泛化估计，而常用的 n-gram 去污染过滤无法检测字符串空间不相近但内容等价的语义重复（soft contamination）。
- 🔬 **研究方法**：对训练语料做嵌入以检索基准数据的语义重复，在 Olmo3 训练语料等实验中系统考察语义重复污染的普遍性及其对基准成绩的影响。
- 📌 **结论**：污染仍然普遍——78% 的 CodeForces 题目存在语义重复、ZebraLogic 50% 存在精确重复；把基准数据的语义重复纳入训练能提升基准成绩乃至同基准真留出点的成绩，说明近期基准增益混杂了真实能力提升与测试数据积累。

👤 **作者**：Ari Spiesberger、…、Nandi Schoots

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

If LLM training data is polluted with benchmark test data, then benchmark performance gives biased estimates of out-of-distribution (OOD) generalization. Typical decontamination filters use n-gram matching which fail to detect semantic duplicates: sentences with equivalent (or near-equivalent) content that are not close in string space. We study this soft contamination of training data by semantic duplicates. Among other experiments, we embed the Olmo3 training corpus and find that: 1) contamination remains widespread, e.g. we find semantic duplicates for 78% of CodeForces and exact duplicates for 50% of ZebraLogic problems; 2) including semantic duplicates of benchmark data in training does improve benchmark performance; and 3) when finetuning on duplicates of benchmark datapoints, performance also improves on truly-held-out datapoints from the same benchmark. We argue that recent benchmark gains are thus confounded: the prevalence of soft contamination means gains reflect both genuine capability improvements and the accumulation of test data and effective test data in growing training corpora.

</details>

### 141. Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines?

📄 [arXiv](https://arxiv.org/abs/2602.14111) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`evaluation`、`sparse autoencoder`、`random baseline`、`interpretability`
- 🎯 **研究动机**：SAE 被视为解释神经网络的核心工具，但下游任务中不断出现的负面结果使人怀疑其是否真正恢复了有意义的特征
- 🔬 **研究方法**：在已知真值特征的合成设置中直接检验 SAE，并构造三个把 SAE 特征方向或激活模式约束为随机值的基线，在多个 SAE 架构上比较可解释性、稀疏探测与因果编辑
- 📌 **结论**：合成设置中 SAE 仅恢复 9% 的真实特征（解释方差高达 71%），随机基线在可解释性（0.87 vs 0.90）、稀疏探测（0.69 vs 0.72）与因果编辑（0.73 vs 0.72）上追平全训练 SAE，表明当前 SAE 不能可靠分解模型内部机制

👤 **作者**：Anton Korznikov、Andrey Galichin、Alexey Dontsov、Oleg Rogov、Ivan Oseledets、Elena Tutubalina

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Sparse Autoencoders (SAEs) have emerged as a promising tool for interpreting neural networks by decomposing their activations into sparse sets of human-interpretable features. Recent work has introduced multiple SAE variants and successfully scaled them to frontier models. Despite much excitement, a growing number of negative results in downstream tasks casts doubt on whether SAEs recover meaningful features. To directly investigate this, we perform two complementary evaluations. On a synthetic setup with known ground-truth features, we demonstrate that SAEs recover only $9\%$ of true features despite achieving $71\%$ explained variance, showing that they fail at their core task even when reconstruction is strong. To evaluate SAEs on real activations, we introduce three baselines that constrain SAE feature directions or their activation patterns to random values. Through extensive experiments across multiple SAE architectures, we show that our baselines match fully-trained SAEs in interpretability (0.87 vs 0.90), sparse probing (0.69 vs 0.72), and causal editing (0.73 vs 0.72). Together, these results suggest that SAEs in their current state do not reliably decompose models' internal mechanisms.

</details>

**尚未挂出 arXiv（待核验）**
- Auditing is not Evaluating: LLM Audit Requires Dynamic, Contextual, Budget-aware and Reliable Evidence
- Auditing the Judge: Human-Grounded Bias Discovery in LLM Judges
- Are LLM Safety Judges Policy-Invariant?（重复，见对齐节）
- EvalAwareBench: Measuring Evaluation Awareness in Frontier LMs
- Too Early for AI-Assisted Peer Review
- Auditing AI peer reviewers: dose-response and false-positive benchmark on real scientific papers
- Large language models can not and should not be banned from peer review
- Leaderboard Hacking（重复，见 agent 节）
- Forced Orders: What LLM Leaderboards Hide About Model Comparisons
- Recovering Clean Evaluation Metrics from Contaminated Benchmarks
- Bypassing PC1 Makes SAEs More Reproducible

## 核验记录

- 2026-09-30：首版建立（9,127 条标题宽筛，八分类清单）。
- 2026-09-30（二次更新）：36 篇升级完整卡片（ti: 精确匹配 22 + 已库内补位 14）。
- 2026-09-30（三轮补查）：限流冷却后串行补查 261 条待核清单，新命中 105 篇——全部 id_list 批量核验 meta 后升级卡片。累计卡片 141 篇，剩余待核 150 条（多轮 ti: 查询未命中，属尚未挂出或标题改写较大者，待 arXiv 陆续放出）。
- Pre-Decoding States（dllm-security #8）为 OpenReview-only，无 arXiv 版，保留在待核验清单。
- 标题变体（同文核验）：卡片保留 NeurIPS 官方列表标题；#17 Token Inflation 的 arXiv 版名为 "The More It Says, the More You Pay: A Black-Box Audit of Provider-Side Token Inflation…"、arXiv 版 HPE 前缀等差异均经摘要主题核验为同一论文。个别 📅 月份与 ID 段不一致为月末跨月提交。
- 复查（2026-09-30）：卡片编号连续、徽章/官方链接/关键词角色词/三段式/作者行/摘要折叠齐全；卡片与待核清单无重复；补位卡链接 HTTP 200；三段式数字经 abstract 反查无误。
