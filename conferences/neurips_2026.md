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

### 3. Inference-Time Vulnerability Beyond Shallow Safety: Alignment Along Generation Trajectories

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

### 4. Conceal, Reconstruct, Jailbreak: Exploiting the Reconstruction–Concealment Tradeoff in MLLMs

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

### 5. Guaranteed Jailbreaking Defense via Disrupt-and-Rectify Smoothing

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

### 6. Few-Shot Truly Benign DPO Attack for Jailbreaking LLMs

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

### 7. BSO: Safety Alignment Is Density Ratio Matching

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

### 8. GradShield: Alignment Preserving Finetuning

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

### 9. Latent-space Attacks for Refusal Evasion in Language Models

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

### 10. Curriculum Learning for Safety Alignment

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

### 11. Cat-DPO: Category-Adaptive Safety Alignment

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

### 12. Systematic Scaling Analysis of Jailbreak Attacks in Large Language Models

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

### 13. The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety

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

### 14. Fail-Closed Alignment for Large Language Models

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

### 15. Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples

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

### 16. Enhancing Jailbreak Attacks on LLMs via Persona Prompts

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
- Internal Safety Collapse in Frontier Large Language Models
- DACE: Diversity-Driven Adversarial Co-Evolution for Robust LLM Safety Alignment
- Bridging the Gap Between Harmfulness Belief and Refusal Behavior for Safety Alignment
- Fine-tuning Does Not Reach All: Uneven Safety and Knowledge Dynamics in LLMs
- When Safety Becomes An Outlier: Understanding the Retention of LLM Safety Behaviors
- Rethinking LLM Fine-Tuning via Weight Space Reparameterization: Preserving Safety during Downstream Adaptation
- SLDR: Defending Against Malicious Fine-tuning via Selective Layers Recovery and Dynamic Routing
- Tcell: Mitigating Harmful Fine-tuning via Gradient Alignment
- Dialectics of Alignment: Harnessing Unsafe Knowledge for Dynamic Safety Routing
- Explaining and Breaking the Safety-Helpfulness Ceiling via Preference Dimensional Expansion
- Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation
- Behaving Better, Thinking Worse: Sycophancy Across Post-Training Stages
- SuperSycophantic: Stress-Testing Frontier LLMs from Single- to Multi-Turn Sycophancy
- Expected Harm: Rethinking Safety Evaluation of (Mis)Aligned LLMs
- Are LLM Safety Judges Policy-Invariant? A Three-Principle Stress-Test
- Answering At Any Cost: Frontier LLMs Are Consequence-Insensitive
- Do Thinking Tokens Help with Safety?
- Beyond Truthfulness: Evaluating Honesty in LLMs
- Emergent Misalignment as Data-Mediated Transfer
- The Piggyback Hypothesis of Generalization: Explaining and Mitigating Emergent Misalignment
- Persona-Model Collapse in Emergent Misalignment
- Self-Recognition Finetuning can Reverse and Prevent Emergent Misalignment
- Innocuous-Seeming Data, Latent Ideology: Ideological Generalisation in Finetuned LLMs
- (Mis)generalization of Helpful-Only Fine-Tuning

### CoT 监控、scheming 与 AI control

**尚未挂出 arXiv（待核验）**
- Chain-of-Thought Oversight Should Not Treat Faithfulness as Monitorability
- Corrupted Plans, Clean Traces: What Planning-Execution Decoupling Reveals About CoT Monitoring
- Stress Testing Chain-of-Thought Monitoring Against Covert Misalignment
- Training on Documents About Monitoring Leads to CoT Obfuscation
- Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics
- Training Deliberative Monitors for Black-Box Scheming Detection
- AI Control for Sandbagging on Fuzzy Tasks
- AI Models Can Provably Hide Arbitrary Capabilities
- AIs with Secret Loyalties are a Serious but Addressable Threat
- AutoHoney: Automating, Deploying, and Evaluating Scheming Honeypots Across Production Codebases
- Evaluating and Understanding Scheming Propensity in LLM Agents
- SchemeArena: Factorized Stress Testing of Scheming in LLM Agents
- Scheming Is a Symptom: Alignment Research Should Probe Reflexive Fragility
- Breadcrumbing Search Agents: Per-Turn Scheming Over Long-Horizon Trajectories
- Neural Chameleons: Language Models Can Learn to Hide Their Thoughts from Unseen Activation Monitors
- Attack Selection In Agentic AI Control Evaluations Meaningfully Decreases Safety
- Alloy Agents Can Be More Dangerous Than Either Model Alone
- Agent Meltdowns: The Road to Hell Is Paved with Helpful Agents
- Agent Abstain: Do LLM Agents Know When Not to Act?
- Measuring and Strengthening Behavioral Suppression in Language Models
- Tatemae: Detecting Alignment Faking via Tool Selection in LLMs
- Model Incrimination: Investigating Whether Concerning Behavior Reflects Misalignment
- Inter-Agent Influence: Evaluating Persuasion, Deception and Coercion in Multi-Agent Systems
- Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems
- Group Perspective Matters: Regulating Debate Relationships Can Mitigate Blind Conformity

### 智能体安全与提示注入

### 17. Token Inflation: How Dishonest Providers Can Overcharge（已库内，2609.20370）

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

### 18. Stealth Apart, Harm Together: Skill Cascading Attacks on Skill-Based Agent Systems（已库内，0928）

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

### 19. Share-Borne AI Virus: Memory-Hopping Attacks Across LLM Agents（已库内，0929）

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

**尚未挂出 arXiv（待核验）**
- Agent Security is a Systems Problem
- AI Agents May Always Fall for Prompt Injections
- AM-Bench: A Unified Taxonomy and Evaluation Suite for Agentic Misalignment
- Adaptive Adversaries: A Multi-Turn, Multi-LLM Benchmark for LLM Agent Security
- ASPI: Seeking Ambiguity Clarification Amplifies Prompt Injection Vulnerability in LLM Agents
- Agent MechSuits: Mechanistic Subspace Safety Steering for Multi-Turn CLI Agents
- CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents
- ChainForge: Tool-Chain Hijacking Attacks against LLM Agents via Execution-Grounded Tool Synthesis
- MCPHunt: An Evaluation Framework for Cross-Boundary Data Propagation in Multi-Server MCP Agents
- MCPHallu: Benchmarking Reasoning, Execution, and Memory Hallucinations in MCP Agents
- MCP-Atlas: A Large-Scale Benchmark for Tool-Use Competency with Real MCP Servers
- Cross-User Poisoning: User-Task Boundary Failures in Multi-User Collaborative Language Agents
- Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks
- Seeing Is Not Screening: Multimodal Hidden Instruction Attacks on Agent Skill Scanners
- Asynchronous Agentic Poisoning
- MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents（与库内 2607.14651 同名，待核）
- Forgetting is Not Always Bad: A Neuro-Inspired Memory Repair Mechanism for Poisoned LLM Agents
- Harmless in Pieces, Harmful in Motion: Detecting Multi-Agent Jailbreaks
- FlowLeak: Coverage-Guided Extraction of Dynamic Workflows in LLM-Based Multi-Agent Systems
- FlowSteer: Prompt-Only Workflow Steering Exposes Planning-Time Vulnerabilities in Multi-Agent LLM Systems
- Forced Deferral: Manipulating Routing Decisions in Multimodal LLM Cascades
- Leaderboard Hacking: Preference-Based Model Evaluations are Vulnerable to Manipulation
- GitInject: Real-World Prompt Injection Attacks in AI-Powered CI/CD Pipelines
- DECEIVE-AFC: Adversarial Claim Attacks against Search-Enabled LLM-based Fact-Checking Systems
- Reasoning Poisoning: Utilizing Social-Engineering to Steer Chain-of-Thought
- LITMUS: Benchmarking Behavioral Jailbreaks of LLM Agents in Real OS Environments
- MetaPI: Constructing Prompt Injection Benchmarks from Any Agent Benchmarks
- EnvTrap: Revealing the Environment-Only Attack Surface in Embodied AI via Consequence-Blind Action Execution
- SecureClaw: Clawing Back Control of LLM Agents
- Soteria: Formally Verified Planning with Runtime Enforcement for Safe LLM Agents
- Runtime Verification of Multiple Natural Language Criteria for Agent Governance
- EV-AUDIT: A Co-Evolutionary Auditing Framework for Task Hijacking in Multi-Agent Systems
- Swarm Shepherd: Securing Multi-Agent Ecosystems Against Persistent Latent Compromise
- The Best-Laid SCHEMEs: Coordinated Sabotage and Monitoring in Multi-Agent Systems
- DIBench: Benchmarking Decision Integrity of GUI-based Mobile Agents Under Deceptive Injections
- LPS-Bench: Benchmarking Safety Awareness of Computer-Use Agents in Long-Horizon Planning
- MMA-SafetyBench: A Benchmark for Multimodal Agent Safety Evaluation
- Safe Actions Can Form Unsafe Traces: Benchmarking and Shielding Compositional Emergent Risk in AI Agents
- Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning
- AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Systems
- Behavioral Probes for Information Flow in LLM Swarms
- To trust or not to trust: Attention-based Trust Management for LLM Multi-Agent Systems
- JobBench: Aligning Agent Work With Human Will
- MLLMs Fail to Refuse when Using Tools Agentically
- Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage?
- Auditing Sabotage Bench: Detecting and Fixing Research Sabotage in ML Codebases
- MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents
- Do Coding Agents Deceive Us? Detecting and Preventing Cheating via Capped Evaluation with Randomized Tests
- Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale
- ExploitGym: Can AI Agents Turn Security Vulnerabilities into Real Attacks?
- Measuring AI Agents' Progress on Multi-Step Cyber Attack Scenarios
- CyberDualEval: Measuring Dual-Use Cyber Risks in Frontier Language Models
- KaliBench: Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux
- PROTEUS: A Self-Evolving Red Team with Surface Expansion for Agent Skill Ecosystems
- Untrusted Content Masking for Web Agents with Security Guarantees
- Synthetic Web: Benchmarking Language Agents under Adversarial Search Ranking
- The Web Doesn't Sit Still: Adversarial Self-Evolving Attacks on Search Agents
- Chatter Attack: Resource Consumption Attack for Large Language Models
- Bits Beat Tokens: A Regret Rate Distortion Theory for LLM Agents

### 扩散语言模型安全（DLM 线）

### 20. Why Jailbreaks Succeed in Diffusion Language Models: An Energy Landscape Analysis（已库内，0928）

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

### 21. Weak Ties, Strong Signals: Efficient Training Data Detection in Diffusion LLMs via Independent Token Sampling（已库内，0929）

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

### 22. MaskForge: Structure-Aware Adaptive Attacks for Jailbreaking Diffusion Large Language Models（已库内 dllm-security #4）

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

### 23. Extracting Training Data from Diffusion Language Models via Infilling（已库内 dllm-security #24）

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

**尚未挂出 arXiv（待核验）**
- Beyond the Prompt: Leveraging Pre-Decoding States for Jailbreak Detection in dLLMs（已库内 dllm-security #8）
- Diffusion LLMs are Natural Adversaries for any LLM（已库内 dllm-security #3 同族）
- Machine Unlearning in Diffusion LLMs
- Characterizing Memorization in Diffusion Language Models: Generalized Extraction and Sampling Effects
- Diffusion-Time Concept Manifolds: Sparse Autoencoder Groups for Interpreting Denoising Language Models
- CURE: Counterfactual Unsafe-token Re-masking for Diffusion Large Language Model Test-time Alignment
- Diffusion Models Can Approximate Optimal Infilling Lengths Implicitly（解码行为分析，DLM DoS 相关）
- Confidence-Based Decoding is Provably Efficient for Diffusion Language Models
- Theoretical Analysis of Why Masked Diffusion Models Mitigate the Reversal Curse

### 投毒、后门与供应链

### 24. FloatDoor: Platform-triggered Backdoors in LLMs

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

### 25. The Platonic Defense: Backdoor Defense for Self-Supervised Encoders in the Era of Large Scale Pre-training

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

### 26. Token by Token, Compromised: Backdoor Vulnerabilities in Unified Autoregressive Models

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

### 27. Combating Data Laundering in LLM Training

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

### 28. Hallucinated Positive Entanglement for Backdoor Attacks in Federated Self-Supervised Learning

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

### 29. Phantom Transfer: Data Poisoning can Survive Data-Level Defences

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
- Rethinking Molecular Graph Backdoors under Chemistry-aware Admission
- Information Blackhole: Backdoor Mechanism in 3D Point Cloud Reconstruction（已库内，0929）
- Gradient-Mine Units: Scorched-Earth Strategy for Model Protection against Unauthorized Fine-Tuning
- ASAP: Fast Adaptive Sliding Agnostic Poisoning Attack on Federated Learning
- Half-Truths Break Similarity-Based Retrieval
- Adversarial Corpus Selection to Attack Subgraph Matching based Graph Retrieval
- Catch-Only-One: Non-Transferable Examples for Model-Specific Authorization

### 隐私、成员推断与 unlearning

### 30. Leaky Students: Membership Inference against On-Policy Distillation（已库内，0929）

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

### 31. Near-Duplicate Families Break Exact-Record Membership Inference（已库内，0929）

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

**尚未挂出 arXiv（待核验）**
- Exposing Private Corpus Leakage in Multimodal RAG
- CLIOPATRA: Extracting Private Information from LLM Insights
- MPCI-Bench: Multimodal Pairwise Contextual Integrity Privacy Evaluation of Language Model Agents
- POLAR-Bench: A Diagnostic Benchmark for Privacy-Utility Trade-offs in LLM Agents
- GUIGuard-Bench: Toward a General Evaluation for Privacy-Preserving GUI Agents
- PrivacySIM: Evaluating LLM Simulation of User Privacy Behavior
- What to Remember, What to Reveal: Privacy-Aware Memory for Conversational Agents
- Inadvertent Context Leakage in Language Models
- Don't Deploy Fine-Tuned Genomic Foundation Models Without Privacy Evaluation
- Guarding the Life Code: Preserving Membership Privacy in Genomic Foundation Models
- Benchmarking Membership Privacy Risks in Preference-Based LLM Post-Training
- Assessing Per-Sample Membership Inference Vulnerability without Retraining
- Bayesian Low-Rank Posteriors for Scalable Membership Inference
- Local FDR Membership Inference Attacks
- Sequential Membership Inference Attacks
- Causal Evaluation of Membership Inference Attacks
- Estimating Model-Level Membership Inference Vulnerability Without Reference Models
- Exposing the Illusion of Erasure in Knowledge Editing for LLMs
- Evaluating an Evaluation: Membership Inference Attacks as Machine Unlearning Diagnostics
- SMI: Statistical Membership Inference for Reliable Unlearned Model Auditing
- Lethe: Link Inference Attacks For Evaluation of Edge Unlearning Methods
- ShadowBench: Exposing Lexical Anchoring and the Illusion of Forgetting
- KNOT: A Knowledge Entanglement Benchmark for Robust Unlearning Evaluation
- METAFORGET: Audit-Driven Update-Policy Learning for Reliable LLM Unlearning
- Unlearning That Lasts: Utility-Preserving, Robust, and Almost Irreversible Forgetting
- Forgetting Has Neighbors: Localized Collateral Forgetting in Machine Unlearning
- Learning What to Forget: Improving LLM Unlearning via Learned Token-Level Importance
- What Should Remain After Forgetting? Rethinking LLM Unlearning as Predictive Posterior Correction
- TRACE: Data-Free Text Reconstruction Attacks against Approximate Unlearning in LLMs
- Individual-Level Unlearning in Vision-Language Models（已库内，0929 What Does It Mean to Forget a Person 同族待核）
- Models Designed to Forget: Machine Unlearning via Key Deletion
- Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation
- Subliminal Learning Is Steering Vector Distillation
- Subliminal Learning as Trait-Direction Drift: A Mechanism and Targeted Control under SFT Distillation
- What Do SAE Features Encode? Evidence from Human Neural Activity（机制方法，交叉参考）

### 水印、溯源与内容真实性

### 32. AuxMark: Defending Against Unauthorized Agent Distillation via Auxiliary Behavioral Watermarking（已库内，0929）

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

**尚未挂出 arXiv（待核验）**
- ArcMark: Distortion-Free Multi-Byte LLM Watermark via Optimal Transport
- A Retained-Signal Interface for LLM Watermark Robustness under Paraphrase
- Every Bit, Everywhere, All At Once: A Binomial Multibit LLM Watermark
- Multi-bit LLM Watermarking with Certified Semantic Distortion
- Majority Bit-Aware Watermarking for Large Language Models
- MarkTune: Improving the Quality-Detectability Trade-off in Model-Embedded LLM Watermarking
- Making Open-Source Text LLM Watermarks Durable Against Merging
- TextSeal: A Localized LLM Watermark for Provenance & Distillation Protection
- SCTI: Self-Calibrated Trident Identification of Black-Box LLM Watermarks
- PRO: Enabling Precise and Robust Text Watermark for Open-Source LLMs
- MC2Mark: Distortion-Free Multi-Bit Watermarking for Long Messages
- Anytime-Valid Statistical Watermarking
- Watermarking Should Be Treated as a Monitoring Primitive
- Watermarking Without Standards Is Not AI Governance
- Invisible Ink, Visible Lies: How Production Watermarking Causes LLMs to Hallucinate
- Alignment Imprint: Zero-Shot AI-Generated Text Detection via Provable Preference Discrepancy
- Watermark Removal in AI-Generated Images via Next-Token Modeling
- Beyond Bit Matching: Orthogonal Watermarks for Collusion-Resistant Image Fingerprinting
- Asymmetric Phase Coding Audio Watermarking
- Auditing Cross-Lingual Fairness in Language Model Watermarking
- Secure Seed-Based Multi-bit Watermarking for Diffusion Models from First Principles
- CLaW: Codec-Guided Adaptive Latent Watermarking for Traceable Diffusion Image Generation
- TIDE: Trajectory-Aware Watermark Propagation for Text-to-Image Diffusion Models
- FiLM-CAM: Keyed Feature Modulation for Conditional-Access Watermarking
- FedTrace: Generated-Content-Based Watermark Verification for Traitor Tracing in Federated Learning
- Sequential Behavioral Watermarking for LLM Agents
- PrivateSeal: Low-Sensitivity Latent Directions for Diffusion-Resilient User-Specific Watermarking
- PP-Mark: Provable and Publicly Verifiable Watermarking for Generative AI
- Watermarking as a Learned Intrinsic Property of Diffusion Models
- Watermarking Game-Playing Agents in Perfect-Information Extensive-Form Games
- RVCBench: Benchmarking Robustness of Voice Cloning Across Modern Audio Generation Models
- Brute-Force Jailbreaks and Codon-Aware Watermarking for DNA Foundation Models
- On the Robustness of Watermarking for Autoregressive Image Generation

### 内部表示干预与监控（安全 threat model 绑定）

### 33. Harnessing Textual Refusal Directions for Multimodal Safety（已库内 vlm-alignment #22）

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

### 34. Persona Vectors: Monitoring and Controlling Character Traits in Language Models（已库内 misc/persona-vectors 同族待核）

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
- Latent Introspection: Models Can Detect Prior Concept Injections
- Inverted Detection and Control in Steering Vectors
- Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention
- Kernelized Activation Steering
- Graph-Regularized Sparse Autoencoders for LLM Safety Steering
- CrossSteer: Cross-Modal Safety Steering for Audio-Language Models
- DualSteer: Dual-Space Steering for Robust Jailbreak Mitigation of LVLMs
- Minimally Invasive Steering of Language Models
- Sparse Internal Control of Language Models
- Selective Safety Steering via Value-Filtered Decoding
- Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift
- AnchorRep: Defending LLMs Against Cross-Model Adversarial Transfer via Representation Repulsion
- BarrierSteer: LLM Safety via Learning Barrier Steering
- OASIS: Online Adaptive Steering for In-Training Safety of LLMs
- Safety-Aware Latent Space Reasoning in Large Language Models
- Graph-Structured Optimization（同上节）
- LLM Rheology: Auditing Refusal Geometry in Aligned Language Models
- Tight PAC-Bayes Generalisation Guarantees for Large Language Model Safety Monitoring
- Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs
- How Useful Is Cross-Domain Generalization for Training LLM Monitors?
- CoT-Guard: Small Models for Strong Monitoring
- ReasoningShield: Safety Moderation over Reasoning Traces of Large Reasoning Models
- Measuring Safety Alignment Effects in Autonomous Security Agents
- Tracing Persona Vectors Through LLM Pretraining
- Guardrail 类：MindGuard / ReasoningShield / TraceGuard / PROACT Agent / Palette / Permit（零散，见日报管线陆续收录）

### 评测有效性与元层（精选）

### 35. Hearsay: Can an Auditor Trust the Record a Deployed Agent Harness Writes?（已库内，0929）

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

### 36. Silent Failures in Agentic Security Evaluation（已库内，0929）

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

**尚未挂出 arXiv（待核验）**
- Auditing is not Evaluating: LLM Audit Requires Dynamic, Contextual, Budget-aware and Reliable Evidence
- Auditing the Judge: Human-Grounded Bias Discovery in LLM Judges
- Are LLM Safety Judges Policy-Invariant?（重复，见对齐节）
- Models That Know How Evaluations Are Designed Score Safer
- Evaluation Awareness in Language Models Has Limited Effect on Behaviour
- EvalAwareBench: Measuring Evaluation Awareness in Frontier LMs
- Too Early for AI-Assisted Peer Review
- Auditing AI peer reviewers: dose-response and false-positive benchmark on real scientific papers
- Large language models can not and should not be banned from peer review
- Leaderboard Hacking（重复，见 agent 节）
- How Hard is it to Rig a Benchmark? A Social Choice Analysis of Leaderboard Robustness
- Forced Orders: What LLM Leaderboards Hide About Model Comparisons
- Recovering Clean Evaluation Metrics from Contaminated Benchmarks
- Soft Contamination Means Benchmarks Test Shallow Generalization
- Bypassing PC1 Makes SAEs More Reproducible
- Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines?

## 核验记录

- 2026-09-30：首版建立（9,127 条标题宽筛，八分类清单）。
- 2026-09-30（二次更新）：arXiv 定位回填——精确标题匹配 22 条 + 已库内补位 14 条，共 36 篇升级为完整卡片（id_list 批量核验 meta）；其余条目保持清单待 arXiv 挂出。注：arXiv search API 因早前并发触发 429 限流，未命中条目中可能仍有可定位者，待冷却后补查。
- Pre-Decoding States（dllm-security #8）为 OpenReview-only，无 arXiv 版，保留在待核验清单。
- 同名提示：MemPoison（NeurIPS）与库内 2607.14651、RouteGuard（GuardZoo）与库内 skill 检测 RouteGuard 同名不同文，待核。
