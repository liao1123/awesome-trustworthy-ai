# Video Generation Safety

[返回 Generative Media Security 目录](README.md)

## 研究方向

本页研究 text-to-video（T2V）、image-to-video（I2V）及 text-and-image-to-video（TI2V）系统生成有害动态内容的风险。视频安全不能只逐帧复用 T2I filter：有害语义可能来自两个 benign boundary state 之间的 transition、多个无害事件的时间组合，或参考图中的箭头、文字、姿态线和镜头框被模型解释为可执行动作。评测因此需要联合衡量 prompt/refusal、unsafe frame、完整事件语义、视频质量和 multimodal guardrail 的漏检。

## 研究脉络

- **基础安全评测：** T2VSafetyBench 首先把内容风险、jailbreak prompt 与 temporal safety 纳入统一测试，建立安全与生成效用必须共同报告的基线。
- **Optimization-based jailbreak：** T2V-OptJail 把 filter evasion、危险语义保持和视频一致性写成离散 prompt optimization，攻击由固定测试集走向主动漏洞搜索。
- **Temporal attack surface：** SPARK、TEAR 与 BSB 分别利用跨模态关联、事件序列和 boundary-state transition，证明单帧或纯文本审核无法覆盖动态组合风险。
- **I2V visual instruction：** RunawayEvil 与 VII 联合篡改参考图和文字，VPA-Guard 则系统化箭头、草图、emoji、双帧等可执行 visual cue，安全边界从内容识别扩展到动作推断。
- **Proactive safeguard：** ConceptGuard 与 VPA-Guard 在生成前融合 image-text risk、检索相似攻击并抑制危险条件；当前仍缺少对闭源模型更新、长视频、音频条件和自适应攻击的持续评测。

## Benchmark 与安全诊断

### 1. Multi2AV-Safety: Benchmarking Safety in Multimodal-to-Audio-Video Generation

📄 [arXiv](https://arxiv.org/abs/2608.26535)　📅 2026-08

**关键词**：`benchmark`、`omni-modal guardrail`、`compositional evidence`、`audio-video safety`、`audio-video generation`、`multimodal conditioning`

👤 **作者**：Kaichao Jiang、…、Nenghai Yu

- 🎯 **研究动机**：音视频生成转向多模态条件，危害可由良性条件跨模态与时间组合涌现，现有 benchmark 以 prompt 为中心
- 🔬 **研究方法**：Multi2AV-Safety 覆盖全部 11 种非单一 T/I/A/V 条件组合共 11024 个攻击实例，系统评测多模态安全 guard
- 📌 **结论**：单独良性输入可组合出有害语义，有害线索混入良性多模态上下文后更难检测，凸显 compositional risk perception 缺口

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Audio-video generation is rapidly moving from prompt-driven synthesis toward multimodal conditioning, where text, images, audio, and video can jointly shape the generated output. This shift changes the nature of safety evaluation: harmful intent may no longer reside in any single input, but instead emerge from how otherwise benign or weakly harmful conditions interact across modalities and time. Existing safety benchmarks, however, remain largely prompt-centric or tied to fixed conditioning interfaces, leaving such compositional risks difficult to study systematically. To bridge this gap, we introduce Multi2AV-Safety, the first safety benchmark, to the best of our knowledge, to cover all 11 non-singleton T/I/A/V conditioning configurations for audio-video generation, comprising 11,024 attack instances. Evaluation on Multi2AV-Safety reveals systematic weaknesses in representative multimodal safety guards across attack mechanisms and harm-evidence structures. Our evaluation reveals two complementary failure modes: harmful semantics can emerge from the combination of individually benign inputs, while explicit harmful cues can become harder to detect when mixed with benign multimodal context. Together, these results identify \emph{compositional risk perception} as a central capability gap in safeguarding multimodal-conditioned audio-video generation: current safety guards fail to reliably integrate safety evidence across modalities and time, even when all conditioning inputs are observable. The dataset will be publicly released in October 2026.

</details>

### 2. SafeGen-Bench: Benchmarking Safety in Image-Conditioned Text-to-Video Generation

📄 [arXiv](https://arxiv.org/abs/2606.01481)　📅 2026-05

**关键词**：`benchmark`、`image-conditioned T2V`、`compositional risk`、`guardrail failure`

👤 **作者**：Yingzi Ma、Xiaogeng Liu、Yawen Zheng、Chaowei Xiao

- 🎯 **研究动机**：现有 T2V 安全基准只用恶意文本 prompt，忽略安全文本与图像组合仍可产生有害视频内容
- 🔬 **研究方法**：SafeGen-Bench 定义 10 类恶意类别（聚焦时序序列与行为风险），精选 start frame 与配对文本模拟真实输入，评条件 T2V 模型与单模态护栏
- 📌 **结论**：当前模型难以一致避免生成恶意内容，unsafety score 最高达 44.5；纯文本或纯图像护栏在七类恶意类别中失败率 80%，单模态防御不足

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid advancements in text-to-image diffusion models, generative video models (T2V models) like Sora can now produce short synthetic videos from a text prompt or an initial image. However, synthetic video generation -- especially when guided by an initial image -- often poses risks, including the potential creation of illegal, politically sensitive, or unethical content. Existing benchmarks have started to consider the safety of generated videos, but they primarily focus on testing models with malicious text prompts, ignoring the scenario where text prompt and image combination may still lead to harmful video content. In practice, this is a common and challenging issue: videos generated from safe text and image inputs can nonetheless convey harmful information. To bridge this gap, we introduce SafeGen-Bench, a benchmark specifically designed to evaluate the safety of conditional T2V models. Our benchmark defines 10 malicious categories, concentrating on risks related to both temporal sequences and depicted behaviors. SafeGen-Bench consists of carefully selected start frames from diverse image and video sources, paired with corresponding text prompts to simulate realistic inputs. We evaluate a variety of conditional T2V models on SafeGen-Bench, and the results indicate that current models struggle to consistently avoid generating malicious content with unsafety scores reaching up to 44.5, especially under conditions requiring high quality. Furthermore, we assess the effectiveness of both text-based and image-based guardrails on our benchmark, finding that unimodal guardrails alone were insufficient to provide a robust defense, with an 80\% failure rate across seven malicious categories. We hope that SafeGen-Bench will foster the development of safer and more controllable conditional T2V models.

</details>

### 3. Moiré Video Authentication: A Physical Signature Against AI Video Generation

📄 [arXiv](https://arxiv.org/abs/2604.01654) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/3761)　📅 2026-04　🏷 ECCV 2026

**关键词**：`defense`、`video authentication`、`video generation`、`unsafe synthesis`、`physical watermark`、`synthetic media detection`

👤 **作者**：Yuan Qing、Kunyu Zheng、Lingxiao Li、Boqing Gong、Chang Xiao

- 🎯 **研究动机**：AI 生成视频越来越难辨别，需要生成模型无法忠实复现的物理签名
- 🔬 **研究方法**：利用相机拍摄双层光栅产生的 Moiré 条纹，推导 Moiré 运动不变量（条纹相位与光栅位移线性耦合），验证器从视频提取双信号检验相关性
- 📌 **结论**：真实与 AI 生成视频的相关性签名显著不同，为视频鉴真提供物理接地的可验证依据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in video generation have made AI-synthesized content increasingly difficult to distinguish from real footage. We propose a physics-based authentication signature that real cameras produce naturally, but that generative models cannot faithfully reproduce. Our approach exploits the Moiré effect: the interference fringes formed when a camera views a compact two-layer grating structure. We derive the Moiré motion invariant, showing that fringe phase and grating image displacement are linearly coupled by optical geometry, independent of viewing distance and grating structure. A verifier extracts both signals from video and tests their correlation. We validate the invariant on both real-captured and AI-generated videos from multiple state-of-the-art generators, and find that real and AI-generated videos produce significantly different correlation signatures, suggesting a robust means of differentiating them. Our work demonstrates that deterministic optical phenomena can serve as physically grounded, verifiable signatures against AI-generated video.

</details>

### 4. SMD: Multi-view Safety-Critical Driving Video Generation in the Real-world Domain

🌐 [Project](https://icml-2.github.io/SMD/) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61036)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`video generation`、`unsafe synthesis`、`temporal consistency`、`embodied safety`、`diffusion model`

👤 **作者**：Jiawei Zhou、Linye Lyu、Zhuotao Tian、Cheng Zhuo、YU LI

- 🎯 **研究动机**：安全关键场景稀有，现有生成器只产轨迹、仿真或单视角视频，不满足现代自动驾驶系统实际消费的真实多视角视频
- 🔬 **研究方法**：提出 SMD：GRPO 微调的 VLM 选择最易致险车辆，两阶段轨迹过程先生成碰撞再转化为自然规避轨迹，扩散模型把轨迹渲染成多视角视频
- 📌 **结论**：生成视频在压测多个端到端规划器时显著提高碰撞率，并入训练后降低碰撞率并提升规划器鲁棒性与安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety-critical scenarios are essential for evaluating autonomous driving (AD) systems, yet they are rare in practice. Existing generators produce trajectories, simulations, or single-view videos—but they don’t meet what modern AD systems actually consume: realistic multi-view video. We present SMD, the first framework for generating multi-view safety-critical driving videos in the real-world domain. SMD couples a safety-critical trajectory engine with a diffusion-based multi-view video generator through three design choices. First, we pick the right adversary: a GRPO-fine-tuned vision-language model (VLM) that understands multi-camera context and selects vehicles most likely to induce hazards. Second, we generate the right motion: a two-stage trajectory process that (i) produces collisions, then (ii) transforms them into natural evasion trajectories—preserving risk while staying within what current video generators can faithfully render. Third, we synthesize the right data: a diffusion model that turns these trajectories into multi-view videos suitable for end-to-end planners. Videos generated by SMD substantially increase collision rates when stress testing multiple end-to-end planners, and reduce collision rates when incorporated into training, improving planner robustness and safety. Our code and video examples are available at: \href{https://icml-2.github.io/SMD/}{https://icml-2.github.io/SMD/}.

</details>

### 5. T2VSafetyBench: Evaluating the Safety of Text-to-Video Generative Models

📄 [arXiv](https://arxiv.org/abs/2407.05965) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2024/hash/74eed5f568354c2e77dd9b018f38a9d4-Abstract-Datasets_and_Benchmarks_Track.html)　📅 2024-07　🏷 NeurIPS 2024

**关键词**：`benchmark`、`T2V safety`、`temporal risk`、`safety-utility trade-off`

👤 **作者**：Yibo Miao、Yifan Zhu、Yinpeng Dong、Lijia Yu、Jun Zhu、Xiao-Shan Gao

- 🎯 **研究动机**：T2V 评测只关注生成质量，忽略视频独有的时序安全风险
- 🔬 **研究方法**：定义 12 个安全维度，用真实、LLM 生成与越狱攻击 prompt 构建恶意提示集评测主流 T2V 模型
- 📌 **结论**：无单一模型全面占优，GPT-4 评估与人工评审相关性高，可用性与安全性存在权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The recent development of Sora leads to a new era in text-to-video (T2V) generation. Along with this comes the rising concern about its security risks. The generated videos may contain illegal or unethical content, and there is a lack of comprehensive quantitative understanding of their safety, posing a challenge to their reliability and practical deployment. Previous evaluations primarily focus on the quality of video generation. While some evaluations of text-to-image models have considered safety, they cover fewer aspects and do not address the unique temporal risk inherent in video generation. To bridge this research gap, we introduce T2VSafetyBench, a new benchmark designed for conducting safety-critical assessments of text-to-video models. We define 12 critical aspects of video generation safety and construct a malicious prompt dataset including real-world prompts, LLM-generated prompts and jailbreak attack-based prompts. Based on our evaluation results, we draw several important findings, including: 1) no single model excels in all aspects, with different models showing various strengths; 2) the correlation between GPT-4 assessments and manual reviews is generally high; 3) there is a trade-off between the usability and safety of text-to-video generative models. This indicates that as the field of video generation rapidly advances, safety risks are set to surge, highlighting the urgency of prioritizing video safety. We hope that T2VSafetyBench can provide insights for better understanding the safety of video generation in the era of generative AI.

</details>

### 6. Between Safe Boundaries: Exploiting Temporal Consistency for Jailbreaking Text-To-Video Generation Models

📄 [arXiv](https://arxiv.org/abs/2607.17279)　📅 2026-07

**关键词**：`attack`、`boundary-state transition`、`temporal consistency`、`MCTS search`

👤 **作者**：Xingkai Peng、Jun Jiang、Jiayang Liu、Kejiang Chen、Weiming Zhang

- 🎯 **研究动机**：现有 T2V 越狱多沿用 T2I 方法，未利用时序一致性且查询开销大、搜索缺乏结构化策略
- 🔬 **研究方法**：提出 BSB：把有害意图编码为两个各自无害边界状态间的转移，攻击目标为插值会产生不安全中间帧的状态对；在更廉价的文本代理空间做 MCTS 并用稀疏视频级评估校准
- 📌 **结论**：在 Veo 3.1、Sora 2、Seedance、Kling v1 上 ASR 相对最强对手平均 +18.6%，确立时序一致性为 T2V 的欠研究攻击面

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recently, text-to-video (T2V) models have been widely deployed, sparking growing concerns over their robustness against jailbreak attacks. Existing jailbreak methods, mostly adapted from text-to-image attacks, suffer notable drawbacks when applied to T2V systems. They fail to fully leverage temporal consistency, an inherent characteristic of video generation. Besides, these methods demand heavy video query optimization, which is infeasible in practical black-box scenarios. Their adversarial prompt search is also driven by heuristic local signals, lacking principled structured exploration strategies. To tackle these limitations, we propose BSB, a structured, query-efficient jailbreak framework for T2V models. BSB harnesses temporal consistency by encoding harmful intent as the transition between two individually harmless boundary states. Under this paradigm, the attack targets boundary-state pairs whose interpolation tends to produce unsafe intermediate frames during video generation. Directly evaluating all candidate pairs within the video space incurs prohibitive computation cost. Instead, BSB conducts Monte Carlo Tree Search (MCTS) in a cheaper textual proxy space and regularly calibrates search outcomes with sparse video-level evaluations. We conduct comprehensive experiments on mainstream commercial T2V models including Veo 3.1, Sora 2, Seedance and Kling v1. Results show BSB surpasses all existing jailbreak baselines, delivering an average 18.6% relative gain in attack success rate over the strongest competitor across evaluated models. Our findings identify temporal consistency as an understudied yet vital attack surface for T2V models and verify that structured search facilitates effective vulnerability discovery under constrained query budgets.

</details>

### 7. TEAR: Temporal-aware Automated Red-teaming for Text-to-Video Models

📄 [arXiv](https://arxiv.org/abs/2511.21145) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/He_TEAR_Temporal-aware_Automated_Red-teaming_for_Text-to-Video_Models_CVPR_2026_paper.html)　📅 2025-11　🏷 CVPR 2026

**关键词**：`tool`、`benchmark`、`temporal red teaming`、`online preference learning`、`event decomposition`、`text-to-video safety`

👤 **作者**：Jiaming He、…、Tianwei Zhang

- 🎯 **研究动机**：现有安全评测针对静态图像与文本生成，无法捕捉 T2V 模型的时序动态风险
- 🔬 **研究方法**：TEAR 用生成器训练加 temporal-aware 在线偏好学习的两阶段优化，构造文本无害但利用时序动态诱发违规视频的 prompt，并以 refine model 循环增强隐蔽性与对抗性
- 📌 **结论**：在开源与商业 T2V 系统上 ASR 超 80%，大幅超越此前最佳的 57%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-Video (T2V) models are capable of synthesizing high-quality, temporally coherent dynamic video content, but the diverse generation also inherently introduces critical safety challenges. Existing safety evaluation methods,which focus on static image and text generation, are insufficient to capture the complex temporal dynamics in video generation. To address this, we propose a TEmporal-aware Automated Red-teaming framework, named TEAR, an automated framework designed to uncover safety risks specifically linked to the dynamic temporal sequencing of T2V models. TEAR employs a temporal-aware test generator optimized via a two-stage approach: initial generator training and temporal-aware online preference learning, to craft textually innocuous prompts that exploit temporal dynamics to elicit policy-violating video output. And a refine model is adopted to improve the prompt stealthiness and adversarial effectiveness cyclically. Extensive experimental evaluation demonstrates the effectiveness of TEAR across open-source and commercial T2V systems with over 80% attack success rate, a significant boost from prior best result of 57%.

</details>

### 8. SPARK: Jailbreaking T2V Models by Synergistically Prompting Auditory and Recontextualized Knowledge

📄 [arXiv](https://arxiv.org/abs/2511.13127)　📅 2025-11

**关键词**：`attack`、`audio-visual association`、`latent auditory trigger`、`guided prompt search`

👤 **作者**：Zonghao Ying、…、Xianglong Liu

- 🎯 **研究动机**：已有 T2V 越狱在明显不安全的 prompt 上加扰动，易被检测与防御
- 🔬 **研究方法**：SPARK 组合中性场景锚点、以文字描述声音事件的潜在听觉触发器（利用音视频共现先验）与风格调制器，将攻击形式化为模块化 prompt 空间的约束优化并引导搜索
- 📌 **结论**：在 7 个 T2V 模型上有效，商业模型平均 ASR 提升 23 个百分点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak attacks can circumvent model safety guardrails and reveal critical blind spots. Prior attacks on text-to-video (T2V) models typically add adversarial perturbations to obviously unsafe prompts, which are often easy to detect and defend. In contrast, we show that benign-looking prompts containing rich, implicit cues can induce T2V models to generate semantically unsafe videos that both violate policy and preserve the original (blocked) intent. To realize this, we propose SPARK, a jailbreak framework that leverages T2V models cross-modal associative patterns via a modular prompt design. Specifically, our prompts combine three components: neutral scene anchors, which provide the surface-level scene description extracted from the blocked intent to maintain plausibility; latent auditory triggers, textual descriptions of innocuous-sounding audio events (e.g., creaking, muffled noises) that exploit learned audio-visual co-occurrence priors to bias the model toward particular unsafe visual concepts; and stylistic modulators, cinematic directives (e.g., camera framing, atmosphere) that amplify and stabilize the latent trigger's effect. We formalize attack generation as a constrained optimization over the above modular prompt space and solve it with a guided search procedure that balances stealth and effectiveness. Extensive experiments over 7 T2V models demonstrate the efficacy of our attack, achieving a +23% improvement in average attack success rate in commercial models.

</details>

### 9. T2V-OptJail: Discrete Prompt Optimization for Text-to-Video Jailbreak Attacks

📄 [arXiv](https://arxiv.org/abs/2505.06679) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/6ab3325de0bec40674c99fb0c20fc6a3-Abstract-Conference.html)　📅 2025-05　🏷 NeurIPS 2025

**关键词**：`attack`、`discrete prompt optimization`、`filter evasion`、`semantic consistency`

👤 **作者**：Jiayang Liu、…、Siew Kei Lam

- 🎯 **研究动机**：T2V 安全评测有基准但缺系统攻击方法来挖掘模型漏洞
- 🔬 **研究方法**：首次把 T2V 越狱形式化为离散优化，联合优化绕过安全过滤与保持语义一致，并以 prompt 变体引导迭代搜索
- 📌 **结论**：开源与商用模型上 GPT-4 评估 ASR 提升 11.4%、人工评估提升 10.0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In recent years, fueled by the rapid advancement of diffusion models, text-to-video (T2V) generation models have achieved remarkable progress, with notable examples including Pika, Luma, Kling, and Open-Sora. Although these models exhibit impressive generative capabilities, they also expose significant security risks due to their vulnerability to jailbreak attacks, where the models are manipulated to produce unsafe content such as pornography, violence, or discrimination. Existing works such as T2VSafetyBench provide preliminary benchmarks for safety evaluation, but lack systematic methods for thoroughly exploring model vulnerabilities. To address this gap, we are the first to formalize the T2V jailbreak attack as a discrete optimization problem and propose a joint objective-based optimization framework, called T2V-OptJail. This framework consists of two key optimization goals: bypassing the built-in safety filtering mechanisms to increase the attack success rate, preserving semantic consistency between the adversarial prompt and the unsafe input prompt, as well as between the generated video and the unsafe input prompt, to enhance content controllability. In addition, we introduce an iterative optimization strategy guided by prompt variants, where multiple semantically equivalent candidates are generated in each round, and their scores are aggregated to robustly guide the search toward optimal adversarial prompts. We conduct large-scale experiments on several T2V models, covering both open-source models and real commercial closed-source models. The experimental results show that the proposed method improves 11.4% and 10.0% over the existing state-of-the-art method in terms of attack success rate assessed by GPT-4, attack success rate assessed by human accessors, respectively, verifying the significant advantages of the method in terms of attack effectiveness and content control.

</details>

### 10. TempJail: Temporal Jailbreak Attacks against Image-to-Video Generation Models

📄 [arXiv](https://arxiv.org/abs/2608.26971)　📅 2026-08

**关键词**：`attack`、`I2V temporal jailbreak`、`semantic camouflage`、`latent perturbation`

👤 **作者**：Qi Lu、…、Qiankun Zhang

- 🎯 **研究动机**：现有 I2V 越狱研究只关注单帧违规，忽略恶意语义可随时间组合涌现的时序维度漏洞
- 🔬 **研究方法**：提出 TempJail，将恶意 caption 分解为初始帧视觉条件与时序文本指令；图像侧用受控 latent perturbation 加预训练 encoder 梯度引导，文本侧改写为无害 subject-action-scene 模板
- 📌 **结论**：在 Kling、Seedance、Veo、PixVerse 上黑盒触发恶意时序语义，ASR 较此前方法分别提高 23.3%（GPT-5.2 评估）和 22.0%（人工评估）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In recent years, image-to-video (I2V) generation models have made remarkable progress in subject consistency and temporal coherence, enabling high quality video synthesis. However, these advances also introduce new safety risks. Existing studies mainly focus on jailbreak attacks involving single frame violations, while largely overlooking the temporal dimension unique to video generation models. In this paper, we investigate three attack scenarios and uncover a temporal vulnerability in I2V systems: unsafe semantics may emerge not from a single frame, but from semantic composition over time. We further identify two key challenges in such attacks: temporal abstraction and semantic camouflage. To address these issues, we propose TempJail, a novel temporal jailbreak framework for I2V systems. For temporal abstraction, we decompose a target malicious caption into an initial frame visual condition and a temporal text instruction. For semantic camouflage, on the image side we model semantic injection as controlled latent perturbation in diffusion sampling and introduce gradient guidance from pretrained encoders. On the text side, we rewrite the caption into an innocuous ``subject-action-scene'' template that bypasses safety filters while preserving temporal guidance. In the black-box inference phase, these two modalities jointly enable malicious semantics to be gradually triggered over time. Experiments on closed-source commercial models, including Kling, Seedance, Veo and PixVerse, show that TempJail improves attack success rate over prior state-of-the-art methods by 23.3\% under GPT-5.2 evaluation and 22.0\% under human evaluation. Our codes are available at \href{https://github.com/luqi-glory/TempJail}{GitHub}.

</details>

### 11. VII: Visual Instruction Injection for Jailbreaking Image-to-Video Generation Models

📄 [arXiv](https://arxiv.org/abs/2602.20999) · 🌐 [Project](https://zbwwwwwwww.github.io/VII/)　📅 2026-02

**关键词**：`attack`、`visual instruction injection`、`reference-image attack`、`training-free transfer`

👤 **作者**：Bowen Zheng、…、Xinge You

- 🎯 **研究动机**：I2V 模型会把参考图中的视觉线索当作隐式控制信号，经图像模态注入恶意意图的风险被忽视
- 🔬 **研究方法**：VII 把不安全文本提示的恶意意图重编程并落地为安全参考图中的视觉指令，免训练且可迁移
- 📌 **结论**：在 Kling-v2.5、Veo-3.1、Seedance-1.5、PixVerse-V5 四个商业模型上 ASR 最高 83.5%，拒答率近零

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Image-to-Video (I2V) generation models, which condition video generation on reference images, have shown emerging visual instruction-following capability, allowing certain visual cues in reference images to act as implicit control signals for video generation. However, this capability also introduces a previously overlooked risk: adversaries may exploit visual instructions to inject malicious intent through the image modality. In this work, we uncover this risk by proposing Visual Instruction Injection (VII), a training-free and transferable jailbreaking framework that intentionally disguises the malicious intent of unsafe text prompts as benign visual instructions in the safe reference image. Specifically, VII coordinates a Malicious Intent Reprogramming module to distill malicious intent from unsafe text prompts while minimizing their static harmfulness, and a Visual Instruction Grounding module to ground the distilled intent onto a safe input image by rendering visual instructions that preserve semantic consistency with the original unsafe text prompt, thereby inducing harmful content during I2V generation. Empirically, our extensive experiments on four state-of-the-art commercial I2V models (Kling-v2.5-turbo, Gemini Veo-3.1, Seedance-1.5-pro, and PixVerse-V5) demonstrate that VII achieves Attack Success Rates of up to 83.5% while reducing Refusal Rates to near zero, significantly outperforming existing baselines.

</details>

### 12. RunawayEvil: Jailbreaking the Image-to-Video Generative Models

📄 [arXiv](https://arxiv.org/abs/2512.06674) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_RunawayEvil_Jailbreaking_the_Image-to-Video_Generative_Models_CVPR_2026_paper.html)　📅 2025-12　🏷 CVPR 2026

**关键词**：`attack`、`multimodal jailbreak`、`self-evolving strategy`、`image-text coordination`、`image-to-video jailbreak`、`malicious generation`

👤 **作者**：Songping Wang、…、Caifeng Shan

- 🎯 **研究动机**：I2V 生成模型的越狱脆弱性此前未被研究
- 🔬 **研究方法**：RunawayEvil 基于 Strategy-Tactic-Action 范式：强化学习策略定制与 LLM 探索驱动的策略自进化单元、生成图文协同越狱指令的战术规划单元、执行与评估的行动单元
- 📌 **结论**：在 Open-Sora 2.0 与 CogVideoX 等商业及开源 I2V 模型上取得 SOTA ASR，COCO2017 上超越现有方法 58.5-79 个百分点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Image-to-Video (I2V) generation synthesizes dynamic visual content from image and text inputs, providing significant creative control. However, the security of such multimodal systems, particularly their vulnerability to jailbreak attacks, remains critically underexplored. To bridge this gap, we propose RunawayEvil, the first multimodal jailbreak framework for I2V models with dynamic evolutionary capability. Built on a "Strategy-Tactic-Action" paradigm, our framework exhibits self-amplifying attack through three core components: (1) Strategy-Aware Command Unit that enables the attack to self-evolve its strategies through reinforcement learning-driven strategy customization and LLM-based strategy exploration; (2) Multimodal Tactical Planning Unit that generates coordinated text jailbreak instructions and image tampering guidelines based on the selected strategies; (3) Tactical Action Unit that executes and evaluates the multimodal coordinated attacks. This self-evolving architecture allows the framework to continuously adapt and intensify its attack strategies without human intervention. Extensive experiments demonstrate RunawayEvil achieves state-of-the-art attack success rates on commercial I2V models, such as Open-Sora 2.0 and CogVideoX. Specifically, RunawayEvil outperforms existing methods by 58.5 to 79 percent on COCO2017. This work provides a critical tool for vulnerability analysis of I2V models, thereby laying a foundation for more robust video generation systems.

</details>

### 13. VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks

📄 [arXiv](https://arxiv.org/abs/2606.25592) · 📊 [Dataset](https://huggingface.co/datasets/CSU-JPG/VVA-Bench)　📅 2026-06

**关键词**：`defense`、`visual prompt attack`、`retrieval-augmented guard`、`VVA-Bench`

👤 **作者**：Yining Sun、…、Alex Jinpeng Wang

- 🎯 **研究动机**：I2V 中箭头、草图、emoji 等静态视觉线索被解读为可执行时序指令，视觉提示攻击未被基准覆盖
- 🔬 **研究方法**：构建 VVA-Bench 分类视觉中心提示攻击基准；提出 VPA-Guard 检索增强自进化防御，用少样本推理识别潜在恶意意图
- 📌 **结论**：SOTA 模型高度易感（Wan 2.7 ASR 100%、Veo 3.1 74.8%）；VPA-Guard 平均降低 ASR 44.2%、有害性评分 73.4% 且保持合法编辑效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advancements in Image-to-Video (I2V) generation have transformed input images from simple appearance references into interactive control interfaces where visual cues such as arrows, sketches, and emojis orchestrate complex video dynamics with unprecedented controllability. However, these seemingly innocuous static cues can be interpreted by models as executable temporal instructions, unfolding into harmful actions in the generated videos. Despite the severity of this threat, existing safety benchmarks remain predominantly focused on text-based and content-only image-based jailbreaks, leaving implicit visual prompt attacks insufficiently explored. To bridge this gap, we present VVA-Bench, the first systematic benchmark for evaluating video generation safety under categorized vision-centric prompt attacks. Extensive experiments on VVA-Bench demonstrate that state-of-the-art models are highly susceptible to such attacks, with Attack Success Rates (ASR) reaching 100.0\% on Wan 2.7 and 74.8\% on Veo 3.1. To mitigate these risks, we propose VPA-Guard, a retrieval-augmented and self-evolving defense framework. By leveraging few-shot reasoning to identify latent malicious intents, our method reduces the attack ASR by 44.2\% and the harmfulness score by 73.4\% on average, while maintaining the model's utility for legitimate user edits. Our work provides both a rigorous benchmark and an effective defense strategy to advance safe and socially responsible multimodal generation.

</details>

### 14. Anti-I2V: Safeguarding your Photos from Malicious Image-to-video Generation

📄 [arXiv](https://arxiv.org/abs/2603.24570) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Vu_Anti-I2V_Safeguarding_your_Photos_from_Malicious_Image-to-video_Generation_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`defense`、`image-to-video misuse`、`photo protection`、`adversarial perturbation`

👤 **作者**：Duc Vu、Anh Nguyen、Chi Tran、Anh Tran

- 🎯 **研究动机**：现有图像保护多面向图像生成与 UNet 架构，对特征保持更强的 DiT 类 I2V 模型效果未探索
- 🔬 **研究方法**：Anti-I2V 在 Lab 色彩空间与频域而非仅 RGB 更新扰动，定位去噪中最具语义区分性的层设计目标以最大化破坏时序一致性与生成保真
- 📌 **结论**：跨多样扩散骨干取得 SOTA 防护，有效阻止恶意人物图生视频

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Advances in diffusion-based video generation models, while significantly improving human animation, poses threats of misuse through the creation of fake videos from a specific person's photo and text prompts. Recent efforts have focused on adversarial attacks that introduce crafted perturbations to protect images from diffusion-based models. However, most existing approaches target image generation, while relatively few explicitly address image-to-video diffusion models (VDMs), and most primarily focus on UNet-based architectures. Hence, their effectiveness against Diffusion Transformer (DiT) models remains largely under-explored, as these models demonstrate improved feature retention, and stronger temporal consistency due to larger capacity and advanced attention mechanisms. In this work, we introduce Anti-I2V, a novel defense against malicious human image-to-video generation, applicable across diverse diffusion backbones. Instead of restricting noise updates to the RGB space, Anti-I2V operates in both the $L$*$a$*$b$* and frequency domains, improving robustness and concentrating on salient pixels. We then identify the network layers that capture the most distinct semantic features during the denoising process to design appropriate training objectives that maximize degradation of temporal coherence and generation fidelity. Through extensive validation, Anti-I2V demonstrates state-of-the-art defense performance against diverse video diffusion models, offering an effective solution to the problem.

</details>

### 15. ConceptGuard: Proactive Safety in Text-and-Image-to-Video Generation through Multimodal Risk Detection

📄 [arXiv](https://arxiv.org/abs/2511.18780)　📅 2025-11

**关键词**：`defense`、`multimodal risk detection`、`concept suppression`、`TI2V safety`

👤 **作者**：Ruize Ma、…、Xiangyu Yue

- 🎯 **研究动机**：TI2V 生成中危险语义可来自单模态或图文交互，现有方法多 text-only、需预知风险类别或只能事后审计
- 🔬 **研究方法**：ConceptGuard 两阶段：对比检测模块把融合图文投射到结构化概念空间识别潜在风险，语义抑制机制干预多模态条件引导生成远离不安全概念；配套 ConceptRisk 数据集与 T2VSafetyBench-TI2V 基准
- 📌 **结论**：在两个基准上风险检测与安全视频生成均超越现有基线达 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent progress in video generative models has enabled the creation of high-quality videos from multimodal prompts that combine text and images. While these systems offer enhanced controllability, they also introduce new safety risks, as harmful content can emerge from individual modalities or their interaction. Existing safety methods are often text-only, require prior knowledge of the risk category, or operate as post-generation auditors, struggling to proactively mitigate such compositional, multimodal risks. To address this challenge, we present ConceptGuard, a unified safeguard framework for proactively detecting and mitigating unsafe semantics in multimodal video generation. ConceptGuard operates in two stages: First, a contrastive detection module identifies latent safety risks by projecting fused image-text inputs into a structured concept space; Second, a semantic suppression mechanism steers the generative process away from unsafe concepts by intervening in the prompt's multimodal conditioning. To support the development and rigorous evaluation of this framework, we introduce two novel benchmarks: ConceptRisk, a large-scale dataset for training on multimodal risks, and T2VSafetyBench-TI2V, the first benchmark adapted from T2VSafetyBench for the Text-and-Image-to-Video (TI2V) safety setting. Comprehensive experiments on both benchmarks show that ConceptGuard consistently outperforms existing baselines, achieving state-of-the-art results in both risk detection and safe video generation. Our code is available at https://github.com/Ruize-Ma/ConceptGuard.

</details>