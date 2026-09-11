## 研究方向

本页研究攻击者如何借助 image、typography、visual style、multi-image relation、steganography 与视觉推理，把有害意图移出文本安全通道并绕过 VLM/MLLM refusal。这里同时记录 attack surface、内部失效机制和直接针对 VLM 表示或推理流程的防御；一般感知鲁棒性与面向 Agent 的 indirect prompt injection 分别由其他页面维护。

## 研究脉络

- **视觉通道绕过：** HADES 与 FigStep 证明把有害语义转移到图像或排版文字即可绕过主要依赖文本的 safety alignment。
- **攻击面细化：** 后续工作把攻击扩展到 visual cipher、object substitution、steganography、style trigger、低清晰度输入和多图组合推理。
- **机制解释：** 研究从单纯报告 ASR 转向分析 embedding alignment、attention entropy、refusal instability、safety perception distortion 与 cross-modal information flow。
- **防御演进：** 防御从输入恢复与分步 OCR，发展到 activation shift removal、internal information decomposition 和 pipeline-level safety intervention。
- **当前边界：** 视觉攻击的可迁移性高度依赖模型、编码器和输入预处理；必须同时评测 adaptive attack、良性视觉任务、over-refusal 与额外延迟。

## Benchmark 与失效机制分析

### 1. MMJailBench: A Factorized Benchmark for Disentangling Multimodal Jailbreak Vulnerabilities

📄 [arXiv](https://arxiv.org/abs/2608.25490)　📅 2026-08

**关键词**：`benchmark`、`analysis`、`multimodal safety audit`、`factorized design`、`judge configuration`、`cross-modal safety gap`

👤 **作者**：Tianshi Wang、Jingsong Wang、Yafei Huang、Fengling Li、Xin Li、Lei Zhu

- 🎯 **研究动机**：既有 MLLM 越狱 benchmark 把危害意图、prompt framing、视觉语义与指令载体耦合在单实例中，无法归因
- 🔬 **研究方法**：MMJailBench 因子化地组合并变化这些因素做受控评测，覆盖 16 个开源与专有 MLLM，配套模块化评测套件
- 📌 **结论**：prompt framing 是最大变异源；任务相关与权威型视觉线索提高易感性，视觉渲染指令并不稳定更危险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) are increasingly deployed in real-world applications, yet how different factors shape their jailbreak vulnerabilities remains poorly understood. Existing benchmarks often couple harmful intent, prompt framing, visual semantics, and instruction carrier within individual jailbreak instances, obscuring the specific sources of observed vulnerabilities. To address this limitation, we introduce MMJailBench, a factorized benchmark that systematically varies and combines these factors under controlled configurations, enabling fine-grained comparison and factor-level attribution. Large-scale evaluations across 16 open-weight and proprietary MLLMs reveal highly heterogeneous and model-dependent vulnerability profiles. Jailbreak vulnerability varies markedly across harm domains, exposing uneven coverage in current multimodal safety alignment. Prompt framing emerges as the dominant source of variation, task-relevant visual semantics systematically increase jailbreak susceptibility with authority-like cues exposing particularly pronounced vulnerabilities, and visually rendered instructions do not consistently increase jailbreak susceptibility relative to direct textual instructions. To further investigate the risks introduced by multimodal context, we conduct diagnostic analyses on a representative open-weight model and identify vulnerability-associated patterns in internal representations and cross-modal interactions. Finally, we develop a modular multimodal jailbreak evaluation suite with full and lightweight configurations, multiple judge options, and multidimensional metrics, enabling reproducible, scalable, and cost-efficient multimodal jailbreak auditing.

</details>

### 2. When Think-with-Image Meets Safety: What Determines Multimodal Jailbreak Robustness?

📄 [arXiv](https://arxiv.org/abs/2605.27932)　📅 2026-05

**关键词**：`analysis`、`think-with-image`、`image-tool safety vector`、`pipeline robustness`

👤 **作者**：Yuan Tian、Bing Hu、Fang Wu、Xiaomin Li、Binghang Lu、Neil Zhenqiang Gong

- 🎯 **研究动机**：think-with-image 推理范式安全影响不明，不同管线设计越狱鲁棒性差异的原因未知
- 🔬 **研究方法**：比较直接生成、纯文本前置轮、视觉状态操纵与显式 image-tool 调用四种范式，提出 image-tool safety vector 框架把调用建模为向安全方向的表征残移
- 📌 **结论**：显式 image-tool 交互平均相对降低约 30% 越狱成功率，即使返回图被覆盖为不安全外观仍低，而纯文本前置轮即回到直接回答水平——低 ASR 由内部残移而非返回图像语义解释

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Think-with-image reasoning is emerging as a new inference paradigm for large vision-language models, but its safety implications remain poorly understood. Existing systems already span multiple process designs, including direct response generation, text-only prior turn, visual-state manipulation, and explicit external image-tool invocation. In this paper, we ask which of these evaluated paradigms improves multimodal jailbreak robustness, and why. Across multiple vision-language models, explicit image-tool interaction yields the lowest attack success rates in our experiments, reducing jailbreak success by around 30% relative on average across the evaluated models. This finding is initially surprising: ASR remains low even when the returned image-tool output is manually overridden or itself unsafe-looking, but returns near direct-answering levels under text-only prior turn controls. These results indicate that the lower ASR is not explained by benign returned-image semantics or by the textual image-tool trace alone. To explain the pattern, we introduce an image-tool safety vector framework that models image-tool invocation as a residual shift in hidden representations toward a safety-relevant direction. Representation-level analyses and activation interventions support this account. Overall, our results suggest that explicit image-tool interaction is a promising design pattern for improving jailbreak robustness, while also motivating pipeline-specific safety evaluation.

</details>

### 3. One Perturbation, Two Failure Modes: Probing VLM Safety via Embedding-Guided Typographic Perturbations

📄 [arXiv](https://arxiv.org/abs/2604.25102)　📅 2026-04

**关键词**：`analysis`、`typographic perturbation`、`embedding guidance`、`dual failure mode`

👤 **作者**：Ravikumar Balakrishnan、Sanket Mendapara

- 🎯 **研究动机**：排版注入研究只追 ASR，不解释为何某些渲染能绕过安全对齐
- 🔬 **研究方法**：实证证明多模态 embedding 距离强预测 ASR（r=-0.71 至 -0.93）；用 CWA-SSA 在有界 l∞ 扰动下直接最大化图文嵌入相似度做红队，无需访问目标模型
- 📌 **结论**：优化同时恢复视觉可读性与削弱安全拒答两种共现效应，主导机制取决于模型安全过滤强度与视觉退化程度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Typographic prompt injection exploits vision language models' (VLMs) ability to read text rendered in images, posing a growing threat as VLMs power autonomous agents. Prior work typically focus on maximizing attack success rate (ASR) but does not explain \emph{why} certain renderings bypass safety alignment. We make two contributions. First, an empirical study across four VLMs including GPT-4o and Claude, twelve font sizes, and ten transformations reveals that multimodal embedding distance strongly predicts ASR ($r{=}{-}0.71$ to ${-}0.93$, $p{<}0.01$), providing an interpretable, model agnostic proxy. Since embedding distance predicts ASR, reducing it should improve attack success, but the relationship is mediated by two factors: perceptual readability (whether the VLM can parse the text) and safety alignment (whether it refuses to comply). Second, we use this as a red teaming tool: we directly maximize image text embedding similarity under bounded $\ell_\infty$ perturbations via CWA-SSA across four surrogate embedding models, stress testing both factors without access to the target model. Experiments across five degradation settings on GPT-4o, Claude Sonnet 4.5, Mistral-Large-3, and Qwen3-VL confirm that optimization recovers readability and reduces safety aligned refusals as two co-occurring effects, with the dominant mechanism depending on the model's safety filter strength and the degree of visual degradation.

</details>

### 4. Reading Between the Pixels: Linking Text-Image Embedding Alignment to Typographic Attack Success on Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2604.12371)　📅 2026-04　🏷 ICLR 2026 Workshop

**关键词**：`analysis`、`typographic attack`、`embedding alignment`、`visual degradation`

👤 **作者**：Ravikumar Balakrishnan、Sanket Mendapara、Ankit Garg

- 🎯 **研究动机**：排版攻击成功率随字体与视觉条件剧烈变化且模型间差异大，缺乏机理性解释
- 🔬 **研究方法**：在四个 VLM 上以 6-28px 字体及旋转、模糊等变换评估 1,000 条 SALAD-Bench prompt，并计算 text-image embedding 距离
- 📌 **结论**：embedding 距离与 ASR 强负相关（r=-0.71 至 -0.93）；GPT-4o 上文本攻击 36% vs 图像攻击 8%，模型特异模式排除一刀切防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We study typographic prompt injection attacks on vision-language models (VLMs), where adversarial text is rendered as images to bypass safety mechanisms, posing a growing threat as VLMs serve as the perceptual backbone of autonomous agents, from browser automation and computer-use systems to camera-equipped embodied agents. In practice, the attack surface is heterogeneous: adversarial text appears at varying font sizes and under diverse visual conditions, while the growing ecosystem of VLMs exhibits substantial variation in vulnerability, complicating defensive approaches. Evaluating 1,000 prompts from SALAD-Bench across four VLMs, namely, GPT-4o, Claude Sonnet 4.5, Mistral-Large-3, and Qwen3-VL-4B-Instruct under varying font sizes (6--28px) and visual transformations (rotation, blur, noise, contrast changes), we find: (1) font size significantly affects attack success rate (ASR), with very small fonts (6px) yielding near-zero ASR while mid-range fonts achieve peak effectiveness; (2) text attacks are more effective than image attacks for GPT-4o (36% vs 8%) and Claude (47% vs 22%), while Qwen3-VL and Mistral show comparable ASR across modalities; (3) text-image embedding distance from two multimodal embedding models (JinaCLIP and Qwen3-VL-Embedding) shows strong negative correlation with ASR across all four models (r = -0.71 to -0.93, p < 0.01); (4) heavy degradations increase embedding distance by 10--12% and reduce ASR by 34--96%, while rotation asymmetrically affects models (Mistral drops 50%, GPT-4o unchanged). These findings highlight that model-specific robustness patterns preclude one-size-fits-all defenses and offer empirical guidance for practitioners selecting VLM backbones for agentic systems operating in adversarial environments.

</details>

### 5. TreeTeaming: Autonomous Red-Teaming of Vision-Language Models via Hierarchical Strategy Exploration

📄 [arXiv](https://arxiv.org/abs/2603.22882) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_TreeTeaming_Autonomous_Red-Teaming_of_Vision-Language_Models_via_Hierarchical_Strategy_Exploration_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`benchmark`、`VLM red teaming`、`hierarchical search`、`jailbreak strategy`

👤 **作者**：Chunxiao Li、Lijun Li、Jing Shao

- 🎯 **研究动机**：现有红队受线性探索范式限制，只能在预定义策略集内优化，难以发现新颖攻击
- 🔬 **研究方法**：TreeTeaming 用 LLM Orchestrator 自主决定进化有前景路径或探索新分支、动态构建策略树，多模态执行器落地复杂策略
- 📌 **结论**：12 个 VLM 中 11 个达 SOTA ASR、GPT-4o 上最高 87.60%；攻击平均毒性降 23.09%，更具隐蔽性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of Vision-Language Models (VLMs) has brought their safety vulnerabilities into sharp focus. However, existing red teaming methods are fundamentally constrained by an inherent linear exploration paradigm, confining them to optimizing within a predefined strategy set and preventing the discovery of novel, diverse exploits. To transcend this limitation, we introduce TreeTeaming, an automated red teaming framework that reframes strategy exploration from static testing to a dynamic, evolutionary discovery process. At its core lies a strategic Orchestrator, powered by a Large Language Model (LLM), which autonomously decides whether to evolve promising attack paths or explore diverse strategic branches, thereby dynamically constructing and expanding a strategy tree. A multimodal actuator is then tasked with executing these complex strategies. In the experiments across 12 prominent VLMs, TreeTeaming achieves state-of-the-art attack success rates on 11 models, outperforming existing methods and reaching up to 87.60\% on GPT-4o. The framework also demonstrates superior strategic diversity over the union of previously public jailbreak strategies. Furthermore, the generated attacks exhibit an average toxicity reduction of 23.09\%, showcasing their stealth and subtlety. Our work introduces a new paradigm for automated vulnerability discovery, underscoring the necessity of proactive exploration beyond static heuristics to secure frontier AI models.

</details>

### 6. The Side Effects of Being Smart: Safety Risks in MLLMs' Multi-Image Reasoning

📄 [arXiv](https://arxiv.org/abs/2601.14127) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1710/)　📅 2026-01　🏷 ACL 2026

**关键词**：`benchmark`、`analysis`、`MIR-SafetyBench`、`multi-image relation`、`attention entropy`、`multimodal safety`

👤 **作者**：Renmiao Chen、…、Minlie Huang

- 🎯 **研究动机**：MLLM 多图推理能力增强可能带来新安全风险，缺乏专门基准
- 🔬 **研究方法**：构建首个多图推理安全基准 MIR-SafetyBench，含 2676 实例、9 类多图关系，评测 19 个 MLLM 并分析注意熵等内部信号
- 📌 **结论**：多图推理越强的模型在该基准上反而越脆弱；许多标为安全的回复流于误解或回避，不安全生成的注意熵平均更低，提示模型过度专注解题而忽视安全约束

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Multimodal Large Language Models (MLLMs) acquire stronger reasoning capabilities to handle complex, multi-image instructions, this advancement may pose new safety risks. We study this problem by introducing MIR-SafetyBench, the first benchmark focused on multi-image reasoning safety, which consists of 2,676 instances across a taxonomy of 9 multi-image relations. Our extensive evaluations on 19 MLLMs reveal a troubling trend: models with more advanced multi-image reasoning can be more vulnerable on MIR-SafetyBench. Beyond attack success rates, we find that many responses labeled as safe are superficial, often driven by misunderstanding or evasive, non-committal replies. We further observe that unsafe generations exhibit lower attention entropy than safe ones on average. This internal signature suggests a possible risk that models may over-focus on task solving while neglecting safety constraints. Our code and data are available at https://github.com/thu-coai/MIR-SafetyBench.

</details>

### 7. Safe But Not Robust: Security Evaluation of VLM by Jailbreaking MSTS

🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`benchmark`、`targeted image attack`、`VLM safety`、`adversarial evaluation`、`VLM jailbreak`、`Robust-MSTS`

- 🎯 **研究动机**：VLM安全评测缺针对性图像攻击手段
- 🔬 **研究方法**：构建Robust-MSTS基准，以targeted图像扰动评测VLM安全性
- 📌 **结论**：揭示VLM表面安全但对定向扰动不鲁棒

### 8. Multimodal Situational Safety

📄 [arXiv](https://arxiv.org/abs/2410.06172) · 🌐 [Project](https://mssbench.github.io/) · 🎓 [Official](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1cb57fcf7ff3f6d37eebae5becc9ea6d-Abstract-Conference.html)　📅 2024-10　🏷 ICLR 2025

**关键词**：`benchmark`、`MSSBench`、`situational safety`、`visual context`

👤 **作者**：Kaiwen Zhou、Chengzhi Liu、Xuandong Zhao、Anderson Compalas、Dawn Song、Xin Eric Wang

- 🎯 **研究动机**：同一语言请求在不同视觉情境下安全性可能相反，MLLM 的情境安全未被评估
- 🔬 **研究方法**：MSSBench 含 1820 对图文查询（半数图像情境安全、半数不安全），分析显式安全推理、视觉理解与情境推理
- 📌 **结论**：现有 MLLM 难以同时兼顾三者；多 Agent 流水线可稳定改善安全响应

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) are rapidly evolving, demonstrating impressive capabilities as multimodal assistants that interact with both humans and their environments. However, this increased sophistication introduces significant safety concerns. In this paper, we present the first evaluation and analysis of a novel safety challenge termed Multimodal Situational Safety, which explores how safety considerations vary based on the specific situation in which the user or agent is engaged. We argue that for an MLLM to respond safely, whether through language or action, it often needs to assess the safety implications of a language query within its corresponding visual context. To evaluate this capability, we develop the Multimodal Situational Safety benchmark (MSSBench) to assess the situational safety performance of current MLLMs. The dataset comprises 1,820 language query-image pairs, half of which the image context is safe, and the other half is unsafe. We also develop an evaluation framework that analyzes key safety aspects, including explicit safety reasoning, visual understanding, and, crucially, situational safety reasoning. Our findings reveal that current MLLMs struggle with this nuanced safety problem in the instruction-following setting and struggle to tackle these situational safety challenges all at once, highlighting a key area for future research. Furthermore, we develop multi-agent pipelines to coordinately solve safety challenges, which shows consistent improvement in safety over the original MLLM response. Code and data: mssbench.github.io.

</details>

### 9. Fully Unleashing the Multimodal Attacker: Meta-Adaptive Jailbreaking of Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2608.27531)　📅 2026-08

**关键词**：`attack`、`multimodal guardrail bypass`、`meta-adaptation`、`cross-defense transfer`、`meta-adaptive jailbreak`、`attacker co-evolution`

👤 **作者**：Benlei Cui、…、Haiwen Hong

- 🎯 **研究动机**：现有多模态越狱在 meta 层静态：模板攻击冻结图文布局，迭代攻击只改内容而固定策略与攻击者参数
- 🔬 **研究方法**：提出 MAMJ，沿攻击策略 prompt 与攻击者权重两轴优化攻击者本身：LLM critique 先在轨迹组上精炼 ASP，再以组聚合 ASR 奖励更新权重
- 📌 **结论**：在 MM-SafetyBench 上对 GPT-4o、Gemini-3-Pro-Preview、Seed 2.0 分别达 81.0%/78.9%/82.3% ASR，超最强基线最多 24.1 个百分点，且零训练迁移到未见受害模型并保持对代表性防御有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The safety of large vision-language models is increasingly stress-tested by multimodal jailbreaks, yet existing attacks remain largely static at the meta level: template-based attacks freeze the image-text layout, while iterative attacks adapt only the image-text content with fixed attack strategies and frozen attacker parameters. We propose Meta-Adaptive Multimodal Jailbreaking (MAMJ), which instead optimizes the attacker itself along two axes: an attack strategy prompt (ASP) governing attack iteration and attacker model weights determining attack effectiveness. Across groups of multimodal attack trajectories, an LLM-based critique first refines the ASP, after which group-aggregated attack success rate (ASR) rewards update those weights. On MM-SafetyBench, MAMJ achieves 81.0%, 78.9%, and 82.3% ASR against GPT-4o, Gemini-3-Pro-Preview, and Seed 2.0, respectively, outperforming the strongest sample-level baseline by up to 24.1 percentage points. The learned attacker, comprising the optimized ASP and attacker weights, also transfers without retraining to unseen victims and remains effective under representative defenses. These results reveal a systemic vulnerability of frontier VLMs to meta-adaptive jailbreaks and motivate defenses against meta-level adversaries. Code is available at https://github.com/Alibaba-VELLDEPTH/MetaJailbreak-VLM.

</details>

### 10. Breaking the weakest link to evade vision language models

📄 [arXiv](https://arxiv.org/abs/2608.18938)　📅 2026-08

**关键词**：`attack`、`VLM evasion`、`vision-encoder optimization`、`semantic manipulation`、`vision encoder`、`targeted semantics`

👤 **作者**：Ilan Zini、Boussad Addad、Katarzyna Kapusta

- 🎯 **研究动机**：VLM 对抗鲁棒性尤其针对多模态对齐的逃逸攻击探索不足
- 🔬 **研究方法**：梯度攻击仅在 VLM 的视觉编码器上优化而非整个多模态架构，支持无目标与目标语义两种设定，显著降低计算成本
- 📌 **结论**：Qwen2.5-VL、Granite-Vision、FastVLM、Phi-3.5-Vision 上小的不敏感扰动即可大幅改变模型文本解读

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision Language Models (VLMs) have recently emerged as a critical component of multimodal AI systems, enabling joint reasoning over visual and textual inputs in real-world and safety-critical applications. Despite their growing deployment, the robustness of VLMs against adversarial threats remains insufficiently explored, particularly in the context of evasion attacks targeting multimodal alignment. In this work, we investigate the vulnerability of VLMs to adversarial perturbations applied to visual inputs and study two attack settings: untargeted attacks, where the goal is to disrupt the model's interpretation of the original image, and targeted attacks, where the adversary aims to force the model to generate a specific semantic description unrelated to the original image. To efficiently generate adversarial examples, we propose a gradient-based attack method that performs optimization exclusively on the vision encoder of the VLM rather than on the entire multimodal architecture. This design significantly reduces the computational cost and resource requirements of the attack while maintaining strong effectiveness. We evaluate our approach on several open-source VLMs, including Qwen2.5-VL, Granite-Vision, FastVLM, and Phi-3.5-Vision, and show that small, human-imperceptible perturbations can substantially alter the textual interpretation produced by the models. Our findings highlight the vulnerability of modern VLMs to adversarial manipulation and emphasize the need for improved robustness and security mechanisms in multimodal AI systems.

</details>

### 11. TempJail: Temporal Jailbreak Attack against Large Vision-Language Models via Subtitle Scheduling

📄 [arXiv](https://arxiv.org/abs/2608.19737)　📅 2026-08

**关键词**：`attack`、`subtitle scheduling`、`temporal jailbreak`、`black-box optimization`、`video jailbreak`、`temporal presentation`

👤 **作者**：Ling Zhou、…、Shijie Zhou

- 🎯 **研究动机**：视频越狱只操纵视频中嵌入的文本内容，忽略其时序组织（时长与时隙分配）对效果的影响
- 🔬 **研究方法**：TempJail 黑盒框架：构建查询对齐的对话式字幕序列并优化其时序调度，以真实视频常见字幕为载体不显突兀
- 📌 **结论**：四个 LVLM、两数据集上全部设定 ASR 最高，数据集平均 ASR 在 GPT-5 与 Gemini 3.5-Flash 上分别超最强基线 53 与 18 个百分点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large vision-language models (LVLMs) have achieved remarkable progress in video understanding and reasoning. Despite extensive studies on text- and image-based jailbreaks, video jailbreaks against LVLMs remain largely unexplored. Existing video jailbreak methods mainly manipulate textual content embedded in videos, while overlooking how such information is organized over time. Our analysis reveals that jailbreak effectiveness depends not only on the semantics of textual information but also on its temporal presentation, including duration and timing-slot allocation. Motivated by this finding, we use subtitles, which are common in real-world videos and allow semantic content to be presented under precise temporal control without appearing visually intrusive, as a natural attack medium. Based on this insight, we propose TempJail, a black-box video-based jailbreak framework that constructs query-aligned dialogue-style subtitle sequences and optimizes their temporal scheduling to exploit temporal vulnerabilities in LVLMs and elicit responses that satisfy the harmful intent of the source query. Extensive experiments on four representative LVLMs and two datasets demonstrate that TempJail achieves the highest attack success rate across all evaluated model--dataset settings, outperforming the strongest baseline by 53 and 18 percentage points in dataset-averaged ASR on GPT-5 and Gemini 3.5-Flash, respectively.

</details>

### 12. Text-Anchored Semantic Perturbations for Transferable Jailbreak Attacks on Multimodal Large Language Models

📄 [arXiv](https://arxiv.org/abs/2608.22312)　📅 2026-08

**关键词**：`attack`、`analysis`、`MLLM`、`semantic perturbation`、`black-box transfer`、`cross-modal safety gap`

👤 **作者**：Wenyun Li、Guiping Cao、Xiangyuan Lan、Zheng Zhang

- 🎯 **研究动机**：文本空间学到的安全行为不能可靠迁移到融合跨模态表示，黑盒迁移攻击又易过拟合代理模型
- 🔬 **研究方法**：TA-SPA 在文本锚定语义空间优化可迁移扰动：TASF 分离跨模态语义因子与模态特异残差，SPA 在保持语义一致下多样化有害目标锚点
- 📌 **结论**：攻击对未见与商业 MLLM 强效迁移，在代表性防御下仍有竞争力，说明需要表示级而非输入级的安全对齐

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) have achieved remarkable progress in vision-language interaction, yet their safety alignment remains vulnerable to jailbreak attacks. A key challenge is that safety behavior learned in the textual space does not reliably transfer to fused cross-modal representations, leaving multimodal inputs exploitable through latent semantic cues. We propose Text-Anchored Semantic Perturbation Attack (TA-SPA), a black-box jailbreak framework that optimizes transferable perturbations in a text-anchored semantic space. TA-SPA integrates Text-Anchored Semantic Factorization (TASF), which encourages the separation of cross-modal semantic factors from modality-specific residuals, with Semantic-Preserving Augmentation (SPA), which diversifies harmful target anchors while preserving semantic consistency. Experiments show strong attack effectiveness and transfer to commercial MLLMs, with competitive performance under representative defenses. Additional controls and probing support the intended factorization without implying perfect disentanglement, motivating representation-level safety alignment beyond input-level filtering.

</details>

### 13. Adversarial Style Optimization: Enhancing VLM Jailbreaks by GRPO-based Stylistic Triggers Optimization

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Luo_Adversarial_Style_Optimization_Enhancing_VLM_Jailbreaks_by_GRPO-based_Stylistic_Triggers_CVPR_2026_paper.html)　📅 2026-07　🏷 CVPR 2026

**关键词**：`attack`、`adversarial style`、`GRPO`、`stylistic inconsistency`、`VLM jailbreak`、`stylistic trigger`

👤 **作者**：Bingjun Luo、Jialin Guo、Yue Yao、Xinpeng Ding

- 🎯 **研究动机**：内容级越狱对快速演进的 MLLM 效果不佳，且未利用非内容维度漏洞；实证发现 MLLM 存在风格不一致：理解能力抗风格变化而防御机制可被特定风格触发绕过
- 🔬 **研究方法**：提出即插即用增强模块 ASO：微调图像编辑模型把优化出的风格修改叠加到对抗图像上，GRPO agent 由结构分层奖励（logit 拒答检测加强 judge 语义评估）引导
- 📌 **结论**：显著放大 SOTA 攻击的 ASR，证明风格偏差是红队 MLLM 的可扩展向量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) have achieved impressive performance, but their safety alignment remains vulnerable to jailbreak attacks. Existing content-based jailbreaks are often inconsistent and show unsatisfying performance against the rapidly evolving MLLMs, failing to exploit non-content-based vulnerabilities. Unlike previous research, we empirically find that MLLMs exhibit a Stylistic Inconsistency between their comprehension ability and safety ability: MLLMs can robustly understand content regardless of visual style, yet their defense mechanisms can be easily bypassed by specific stylistic triggers. Based on this finding, we propose Adversarial Style Optimization (ASO), a plug-and-play enhancement module to amplify existing visual jailbreaks. ASO fine-tunes an image-editing model to superimpose an optimized stylistic modification onto a given adversarial image, using a Group Relative Policy Optimization (GRPO) agent guided by a Structurally-Tiered Reward Function that combines a logit-based signal for detecting explicit refusals with a high-fidelity semantic evaluation from a powerful judge model. Extensive experiments show that ASO significantly enhances the ASR of SOTA attacks, demonstrating that stylistic biases are a scalable vector for red-teaming MLLMs. Our code is available at https://github.com/bingjunluo/ASO.

</details>

### 14. Furina: Fragmented Uncertainty-Driven Refusal Instability Attack

📄 [arXiv](https://arxiv.org/abs/2605.26158) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61220)　📅 2026-05　🏷 ICML 2026

**关键词**：`attack`、`prompt fragmentation`、`refusal instability`、`uncertainty amplification`、`refusal calibration`、`uncertainty calibration`

👤 **作者**：Tongxi Wu、Jian Zhang、Yang Gao

- 🎯 **研究动机**：安全对齐被默认为近二值阈值机制，实际存在小扰动即产生随机拒答决策的不稳定区
- 🔬 **研究方法**：多指标诊断框架识别特征签名：不稳定输入呈输出不确定性升高而内部安全激活下降的解耦；Furina 用碎片化场景锚定 prompt 无需模型特定优化即可诱发该签名
- 📌 **结论**：HarmBench 上超过强单轮与多轮基线、MM-SafetyBench 上竞争力强，不确定性放大是可迁移的安全漏洞机制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment in large language models (LLMs) and multimodal large language models (MLLMs) is commonly assumed to operate as a near-binary threshold mechanism. We challenge this assumption by revealing that safety behavior is governed by an instability region where small perturbations induce stochastic refusal decisions rather than deterministic outcomes. We develop a multi-metric diagnostic framework combining external and internal signals to characterize this instability. Through systematic experiments, we identify a characteristic diagnostic signature: inputs in unstable regimes exhibit elevated output uncertainty yet decreased internal safety activation, a decoupling phenomenon that explains why detection-based defenses fail against sophisticated attacks. Building on this framework, we introduce Furina, a jailbreak attack that deliberately induces this signature through fragmented, scene-anchored prompts without model-specific optimization. Furina outperforms strong single-turn and multi-turn baselines on HarmBench and achieves competitive results on MM-SafetyBench, demonstrating that uncertainty amplification provides a principled and transferable mechanism for understanding safety vulnerabilities. Code is available at: https://github.com/0xCavaliers/Furina_Jailbreak.

</details>

### 15. GPO-V: Jailbreak Diffusion Vision Language Model by Global Probability Optimization

📄 [arXiv](https://arxiv.org/abs/2605.07399) · 🌐 [Project](https://anonymous.4open.science/r/GPO-V-0250/)　📅 2026-05

**关键词**：`attack`、`diffusion VLM jailbreak`、`global probability`、`denoising optimization`

👤 **作者**：Yu Pan、Andi Zhang、Yi Wang、Sibei Yang、Wenjie Wang

- 🎯 **研究动机**：dVLM 对固定前缀优化（FPO）类攻击看似鲁棒，但去噪过程本身暴露潜在攻击面
- 🔬 **研究方法**：识别出 Immediate 与 Progressive 两种拒答模式；GPO 操纵全局生成动力学绕过护栏，GPO-V 为首个针对 dVLM 的视觉模态越狱框架
- 📌 **结论**：生成隐蔽扰动且跨模型迁移性异常强，揭示非自回归生成架构的关键安全缺口

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion Vision-Language Models (dVLMs), built upon the non-causal foundations of Diffusion Large Language Models (dLLMs), have demonstrated remarkable efficacy in multimodal tasks by departing from the traditional autoregressive generation paradigm. While dVLMs appear inherently robust against conventional jailbreak tactics, which we categorize as Fixed Prefix Optimization (FPO) (e.g., anchoring responses with "Sure, here is"), this perceived resilience is deceptive. Our investigation into the safety landscape of dVLMs reveals a unique refusal pattern: Immediate Refusal and Progressive Refusal. We find that while FPO-based attacks often fail by triggering the latter, the progressive refinement process itself uncovers a novel, latent attack surface. To exploit this vulnerability, we propose Global Probability Optimization (GPO), a general jailbreak paradigm designed specifically for the denoising trajectory of masked diffusion models. Unlike prefix-based methods, GPO manipulates the global generative dynamics to bypass guardrails in diffusion language models. Building on this, we introduce GPO-V, the first visual-modality jailbreak framework tailored for dVLMs. Empirical results demonstrate that GPO-V produces stealthy perturbations with exceptional cross-model transferability, revealing a critical security gap in non-sequential generative architectures. Our findings underscore the critical urgency of addressing safety alignment in dVLMs. These results necessitate an immediate and fundamental re-evaluation of current defense paradigms to mitigate the unique risks of diffusion-based generation. Our code is available at: https://anonymous.4open.science/r/GPO-V-0250.

</details>

### 16. Jailbreaking Vision-Language Models Through the Visual Modality

📄 [arXiv](https://arxiv.org/abs/2605.00583) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66343)　📅 2026-05　🏷 ICML 2026

**关键词**：`attack`、`visual cipher`、`object substitution`、`visual analogy`、`LLM jailbreak`、`empirical evaluation`

👤 **作者**：Aharon Azulay、Jan Dubiński、Zhuoyun Li、Atharv Mittal、Yossi Gandelsman

- 🎯 **研究动机**：VLM 的视觉模态是绕过安全对齐的未充分开发攻击面
- 🔬 **研究方法**：提出四种视觉攻击：符号序列编码加解码图例、有害物体替换（bomb 换成 banana）、图中文字替换但视觉上下文保义、需推断违禁概念的视觉类比谜题
- 📌 **结论**：六个前沿 VLM 均被绕过；视觉密码在 Claude-Haiku-4.5 上 ASR 40.9% vs 等价文本密码 10.7%，证实文本安全训练不自动泛化到视觉传达的恶意

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The visual modality of vision-language models (VLMs) is an underexplored attack surface for bypassing safety alignment. We introduce four jailbreak attacks exploiting the vision component: (1) encoding harmful instructions as visual symbol sequences with a decoding legend, (2) replacing harmful objects with benign substitutes (e.g., bomb -> banana) then prompting for harmful actions using the substitute term, (3) replacing harmful text in images (e.g., on book covers) with benign words while visual context preserves the original meaning, and (4) visual analogy puzzles whose solution requires inferring a prohibited concept. Evaluating across six frontier VLMs, our visual attacks bypass safety alignment and expose a cross-modality alignment gap: text-based safety training does not automatically generalize to harmful intent conveyed visually. For example, our visual cipher achieves 40.9% attack success on Claude-Haiku-4.5 versus 10.7% for an equivalent textual cipher. To further our insight into the attack mechanism, we present preliminary interpretability and mitigation results. These findings highlight that robust VLM alignment requires treating vision as a first-class target for safety post-training.

</details>

### 17. Zer0-Jack: A memory-efficient gradient-based jailbreaking method for black box Multi-modal Large Language Models

🎓 [Official](https://aclanthology.org/2026.eacl-long.202/)　📅 2026-03　🏷 ACL 2026

**关键词**：`attack`、`black-box MLLM`、`zeroth-order gradient`、`malicious image`、`multimodal jailbreak`、`zeroth-order optimization`

👤 **作者**：Tiejin Chen、Kaishen Wang、Hua Wei

- 🎯 **研究动机**：白盒梯度攻击不适用于黑盒MLLM，零阶优化又受序列目标与模型规模制约
- 🔬 **研究方法**：Zer0-Jack以零阶优化直接生成恶意图像，patch-wise块坐标下降稳定估计降查询
- 📌 **结论**：MiniGPT-4成功率达98.2%，并可越狱GPT-4o等商业模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-modal large language models (MLLMs) have recently shown impressive capabilities but are also highly vulnerable to jailbreak attacks. While white-box methods can generate adversarial visual inputs via gradient-based optimization, such approaches fail in realistic black-box settings where model parameters are inaccessible. Zeroth-order (ZO) optimization offers a natural path for black-box attacks by estimating gradients from queries, yet its application to MLLMs is challenging due to sequence-conditioned objectives, limited feedback, and massive model scales. To address these issues, we propose Zer0-Jack, the first direct black-box jailbreak framework for MLLMs based on ZO optimization. Zer0-Jack focuses on generating malicious images and introduces a patch-wise block coordinate descent strategy that stabilizes gradient estimation and reduces query complexity, enabling efficient optimization on billion-scale models. Experiments show that Zer0-Jack achieves 98.2% success on MiniGPT-4 and 95% on the Harmful Behaviors Multi-modal dataset, while directly jailbreaking commercial models such as GPT-4o. These results demonstrate that ZO optimization can be effectively adapted to jailbreak large-scale multi-modal LLMs. Codes are provided here.

</details>

### 18. Extended to Reality: Prompt Injection in 3D Environments

📄 [arXiv](https://arxiv.org/abs/2602.07104) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-02

**关键词**：`attack`、`3D prompt injection`、`prompt injection`、`multimodal jailbreak`、`physical object`、`multimodal agent`

👤 **作者**：Zhuoheng Li、Ying Chen

- 🎯 **研究动机**：prompt injection 在 3D 物理环境中如何生效缺乏研究
- 🔬 **研究方法**：PI3D 通过摆放带文字的物理对象向 MLLM 注入指令，求解使攻击有效且摆放物理合理的位置与朝向
- 📌 **结论**：对多个 MLLM 在多样相机轨迹下攻击有效，且现有防御不足以可靠拦截

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) have advanced the capabilities to interpret and act on visual input in 3D environments, empowering diverse applications such as robotics and situated conversational agents. When MLLMs reason over camera-captured views of the physical world, a new attack surface emerges: an attacker can place text-bearing physical objects in the environment to override MLLMs' intended task. While prior work has studied prompt injection in the text domain and through digitally edited 2D images, limited attention has been paid to how these attacks function in 3D environments. To bridge the gap, we introduce PI3D, a prompt injection attack against MLLMs in 3D environments, realized through text-bearing object placement rather than digital image edits. We formulate and solve the problem of identifying an effective pose (position and orientation) for a 3D object with injected text, where the attacker's goal is to induce the MLLM to perform the injected task while ensuring that the object placement remains physically plausible. Experiment results demonstrate that PI3D is an effective attack against multiple MLLMs under diverse camera trajectories. We further evaluate a range of defenses and show that they are not sufficient to reliably defend against PI3D.

</details>

### 19. When Background Matters: Breaking Medical Vision Language Models by Transferable Attack

🎓 [Official](https://aclanthology.org/2026.acl-long.1768/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`medical AI`、`VLM safety`、`high-risk deployment`、`multimodal safety`

👤 **作者**：Akash Ghosh、Subhadip Baidya、Sriparna Saha、Xiuying Chen

- 🎯 **研究动机**：医疗 VLM 的对抗鲁棒性少有研究；自然图像迁移攻击扰动可见，易被临床医生察觉
- 🔬 **研究方法**：提出 MedFocusLeak 黑盒攻击：向非诊断背景区域注入协同扰动并用注意力分散机制使模型偏离病理区域，诱导貌似合理却错误的诊断；并提出联合度量攻击成功与图像保真的框架
- 📌 **结论**：六种医学影像模态上达到 SOTA，揭示临床 VLM 推理能力的关键弱点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision–Language Models (VLMs) are increasingly used in clinical diagnostics, yet their robustness to adversarial attacks remains largely unexplored, posing serious risks. Existing medical attacks focus on secondary objectives such as model stealing or adversarial fine-tuning, while transferable attacks from natural images introduce visible distortions that clinicians can easily detect. To address this, we propose MedFocusLeak, a highly transferable black-box multimodal attack that induces incorrect yet clinically plausible diagnoses while keeping perturbations imperceptible. The method injects coordinated perturbations into non-diagnostic background regions and employs an attention-distraction mechanism to shift the model’s focus away from pathological areas. Extensive evaluations across six medical imaging modalities show that MedFocusLeak achieves state-of-the-art performance, generating misleading yet realistic diagnostic outputs across diverse VLMs. We further introduce a unified evaluation framework with novel metrics that jointly capture attack success and image fidelity, revealing a critical weakness in the reasoning capabilities of modern clinical VLMs.

</details>

### 20. VERA-V: Variational Inference Framework for Jailbreaking Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2510.17759) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61094)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`jailbreak`、`VLM safety`、`multimodal jailbreak`、`LLM jailbreak`、`empirical evaluation`

👤 **作者**：Qilin Liao、Anamika Lochab、Ruqi Zhang

- 🎯 **研究动机**：多模态红队方法依赖脆弱模板、聚焦单攻击设置，暴露的漏洞面窄
- 🔬 **研究方法**：提出 VERA-V：把多模态越狱发现重构为文本-图像 prompt 对联合后验分布的学习，轻量攻击者近似后验以高效采样，融合排版文本 prompt、扩散合成图像与结构化干扰三策略
- 📌 **结论**：在 HarmBench 与 HADES 上超越 SOTA，GPT-4o 上攻击成功率较最佳基线高至多 53.75%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Models (VLMs) extend large language models with visual reasoning, but their multimodal design also introduces new, underexplored vulnerabilities. Existing multimodal red-teaming methods largely rely on brittle templates, focus on single-attack settings, and expose only a narrow subset of vulnerabilities. To address these limitations, we introduce VERA-V, a variational inference framework that recasts multimodal jailbreak discovery as learning a joint posterior distribution over paired text-image prompts. This probabilistic view captures complex cross-modal interactions, enabling stealthy, coordinated adversarial inputs that bypass model guardrails. We train a lightweight attacker to approximate the posterior, allowing efficient sampling of diverse jailbreaks and providing distributional insights into vulnerabilities. VERA-V further integrates three complementary strategies: (i) typography-based text prompts that embed harmful cues, (ii) diffusion-based image synthesis that introduces adversarial signals, and (iii) structured distractors to fragment VLM attention. Experiments on HarmBench and HADES benchmarks show that VERA-V consistently outperforms state-of-the-art baselines on both open-source and frontier VLMs, achieving up to 53.75\% higher attack success rate (ASR) over the best baseline on GPT-4o. We include the code on the project page available here: https://github.com/kxwhiowo/VERA-V

</details>

### 21. Reference Attack: A New Cross-Modal Jailbreaking Attack against Multimodal Large Language Models

🎓 [Official](https://aclanthology.org/2026.acl-long.812/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`multimodal safety`、`jailbreak`、`VLM safety`、`LLM jailbreak`、`automated red teaming`

👤 **作者**：Yulong Wang、Yifei Fu、Jiayi Gao

- 🎯 **研究动机**：MLLM 跨模态引用解析过程缺乏安全检查，为越狱留下新攻击面
- 🔬 **研究方法**：提出 Reference Attack：将恶意提示嵌入图像、表格等非文本模态，并在文本中构造递归符号引用，诱导模型逐层解析引用还原有害内容
- 📌 **结论**：对 ChatGPT、Gemini、Claude、LLaMA 的攻击成功率超 93%，比 SOTA 基线最高提升 70.8%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Red team testing, an effective proactive method for evaluating the security of multimodal large language models (MLLMs), requires an expanding toolkit alongside the development of MLLM safeguards. We propose the Reference Attack, a powerful tool for red team testing against MLLMs. The Reference Attack is a reference-guided cross-modal jailbreak method that enhances existing prompt-to-image injection attacks by exploiting MLLMs’ semantic reconstruction capabilities. Our method embeds malicious prompts in non-text modalities (e.g., images, spreadsheets) and constructs recursive symbolic references in text, enabling MLLMs to gradually recover and generate harmful content through layered reference resolution.The attack introduces a new vector that circumvents conventional content moderation by exploiting MLLMs’ lack of security checks during cross-modal reference resolution. We evaluate the Reference Attack on leading MLLMs, including ChatGPT, Gemini, Claude, and the widely used open-source LLaMA model, and achieved an attack success rate of over 93% across all tested models. Compared to state-of-the-art attacks, Reference Attack achieves higher success rates than all baselines under identical evaluation, with a maximum gain of 70.8%. Our study reveals a critical gap in MLLM security and highlights the need for strict security auditing of cross-modal interactions in future content moderation.

</details>

### 22. GAMBIT: A Gamified Jailbreak Framework for Multimodal Large Language Models

🎓 [Official](https://aclanthology.org/2026.acl-long.367/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`multimodal safety`、`jailbreak`、`VLM safety`、`LLM jailbreak`、`automated red teaming`

👤 **作者**：Xiangdong Hu、Yangyang Jiang、Qin Hu、Xiaojun Jia

- 🎯 **研究动机**：现有越狱只增加视觉任务复杂度，未利用模型自身推理动机，对 CoT 推理模型效果不佳
- 🔬 **研究方法**：GAMBIT 分解重组有害视觉语义并构造博弈化场景，让模型作为参与者追求胜利时降低安全注意并回答重构的恶意查询
- 📌 **结论**：ASR 达 92.13%（Gemini 2.5 Flash）、91.20%（QvQ-MAX）、85.87%（GPT-4o），显著超基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) have become widely deployed, yet their safety alignment remains fragile under adversarial inputs. Previous work has shown that increasing inference steps can disrupt safety mechanisms and lead MLLMs to generate attacker-desired harmful content. However, most existing attacks focus on increasing the complexity of the modified visual task itself and do not explicitly leverage the model’s own reasoning incentives. This leads to them underperforming on reasoning models (Models with Chain-of-Thoughts) compared to non-reasoning ones (Models without Chain-of-Thoughts). If a model can think like a human, can we influence its cognitive-stage decisions so that it proactively completes a jailbreak? To validate this idea, we propose GAMBIT (Gamified Adversarial Multimodal Breakout via Instructional Traps), a novel multimodal jailbreak framework that decomposes and reassembles harmful visual semantics, then constructs a gamified scene that drives the model to explore, reconstruct intent, and answer as part of winning the game. The resulting structured reasoning chain increases task complexity in both vision and text, positioning the model as a participant whose goal pursuit reduces safety attention and induces it to answer the reconstructed malicious query. Extensive experiments on popular reasoning and non-reasoning MLLMs demonstrate that GAMBIT achieves high Attack Success Rates (ASR), reaching 92.13% on Gemini 2.5 Flash, 91.20% on QvQ-MAX, and 85.87% on GPT-4o, significantly outperforming baselines. Warning: This paper contains unsafe and offensive examples.

</details>

### 23. Anchoring the Mind of Multimodal Reasoners: Cognitive Bias as a Vector for Jailbreak Attacks

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Cong_Anchoring_the_Mind_of_Multimodal_Reasoners_Cognitive_Bias_as_a_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`attack`、`multimodal reasoning`、`cognitive bias`、`jailbreak`

👤 **作者**：Linhua Cong、Bingrui Sima、Kun He

- 🎯 **研究动机**：现有越狱研究忽视多模态推理模型推理过程中的认知层弱点；发现安全判断被首条信息不成比例影响的锚定效应
- 🔬 **研究方法**：RA-Attack 用跨模态安全锚（结构化视觉思维图）为模型预设带安全偏置的推理链，诱导其合理化并执行后续有害意图
- 📌 **结论**：七个 MLRM 上取得 SOTA 越狱成功率——Gemini-2.5-Pro 达 92%、GPT-4o 达 82%，证明认知偏差可被系统性利用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Reasoning Models (MLRMs) exhibit remarkable performance on complex tasks by incorporating explicit multi-step reasoning. However, this capability also introduces new security vulnerabilities. Existing jailbreak studies largely overlook Cognitive-level weaknesses embedded in the reasoning process itself. In this work, we uncover a critical cognitive bias in MLRMs: the anchoring effect, where safety judgments are disproportionately influenced by the first piece of information received--the anchor. Building on this finding, we propose the Reasoning-chain Anchoring Attack (RA-Attack), a novel jailbreak framework that fully exploits this vulnerability. RA-Attack employs a cross-modal safe anchor, whose core component is a structured visual mind map. This structured format provides the model with a pre-established, safety-biased reasoning chain that subtly induces it to rationalize and execute subsequent harmful intent. Extensive experiments across seven leading closed- and open-source MLRMs demonstrate the effectiveness of RA-Attack, achieving state-of-the-art jailbreak success rates--92% on Gemini-2.5-Pro and 82% on GPT-4o. Our findings reveal that cognitive biases can be systematically exploited to manipulate multimodal reasoning chains, establishing cognitive security as a critical and underexplored frontier in AI safety research. Warning: This paper contains unsafe examples.

</details>

### 24. Jailbreaking Vision-Language Models via Dissonance-Guided Suffix Optimization and Image-Phrase Injection

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Pi_Jailbreaking_Vision-Language_Models_via_Dissonance-Guided_Suffix_Optimization_and_Image-Phrase_Injection_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`attack`、`VLM jailbreak`、`suffix optimization`、`image-phrase injection`

👤 **作者**：Jiacheng Pi、Zhiguo Yang、Xingxing Huang、Dongsheng Xu、Ruizhi Zhong、Wenjie Ruan

- 🎯 **研究动机**：后缀优化靠离散空间梯度近似易陷局部最优，图像扰动攻击跨模型迁移性差
- 🔬 **研究方法**：DGSIP 用目标模型与未对齐模型的预测分歧识别被安全对齐压制的 token 作优化信号，并联合优化图像内短语内容与呈现方式
- 📌 **结论**：多个开源 VLM 安全基准超 SOTA，对 GPT-4o-Mini、Gemini 2.0 Flash、Qwen 2.5-VL 等商业黑盒迁移性更强

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The integration of vision and language in Vision-Language Models (VLMs), while enabling multimodal capabilities, inherently expands their attack surface. Among existing white-box jailbreak methods, suffix-optimization-based approaches often rely on gradient approximations over discrete token spaces, yielding insufficient guidance and causing optimization to stagnate in local optima, while image-perturbation-based ones frequently exhibit poor cross-model transferability. In this work, we introduce DGSIP, a Dissonance-Guided Suffix Optimization and Image-Phrase Injection framework. DGSIP leverages predictive dissonance between the target model and an unaligned model to identify tokens suppressed by safety alignment, using them as a more effective signal than gradient-based cues for suffix optimization. It further reinforces the attack by jointly optimizing the content and presentation of phrase embedded in images to leverage VLMs' cross-modal sensitivity. Our extensive experiments demonstrate that DGSIP outperforms prior baselines across multiple safety benchmarks and a range of open-source VLMs (e.g., MiniGPT-4, InstructBlip and LLaVA). Notably, compared to baselines, our method exhibits much stronger transferability to commercial black-box VLMs, such as GPT-4o-Mini, Gemini 2.0 Flash and Qwen 2.5-VL. Based upon DGSIP, we empirically reveal critical vulnerabilities in the safeguard mechanisms of current VLMs, highlighting the need for more robust defense strategies. The implementation is available on https://github.com/Trusted-LLM/DGSIP.

</details>

### 25. Adversarial Attack Framework Against Vision-Language Model Unlearning

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/7256.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`attack`、`analysis`、`unlearning recovery`、`visual sink token`、`surrogate-only transfer`、`VLM unlearning`

- 🎯 **研究动机**：对抗输入可操纵已 unlearn 的 VLM 复现被遗忘内容，但多数攻击需要受害者架构、参数或输出 logits 访问
- 🔬 **研究方法**：提出 SISA：只需一个代理预训练 VLM；利用 unlearning 后 visual sink token 的持续性作为稳定结构锚，诱导 sink 建立结构锚再经 sink 条件化注意力做语义对齐，生成可迁移对抗输入
- 📌 **结论**：在多样 unlearned VLM 设定下有效，输出与遗忘目标的语义一致性相比干净输入最多提升 6.9 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Vision–Language Models (VLMs) unlearning tends to eliminate the influence of “to-beforgotten” content in the training corpora, algorithmically by suppressing the likelihood of faithfully generating responses on forget-target inputs. The injection of adversarial inputs can manipulate the unlearned VLM’s generation towards the attacker’s will, forcing the reproduction of the supposedly forgotten content and undermining the reliability of expected forgetting behavior. However, most attacks assume access to the unlearned VLM’s architecture or parameters, or to output logits via queries. In this paper, we propose SISA, a novel attack framework for crafting adversarial inputs to manipulate generation towards the forgotten target, which only requires access to a surrogate, pretrained VLM. SISA advances prior attacks by exploiting the persistence of visual sink tokens after unlearning as a stable structural anchor for semantic alignment. SISA induces a sink regime on a candidate visual token to build the structural anchor that influences generation, and then semantically aligns model output to the target while conditioning on attention through the induced sink token, reinforcing the anchor for desired elicitation. With sink persistence and sink-conditioned semantic anchoring, SISA crafts transferable adversarial inputs. Evaluation on diverse unlearned VLM settings confirms the effectiveness of SISA, increasing the outputs’ semantic agreement with forgotten targets by up to 6.9× relative to clean inputs.

</details>

### 26. Contextual Image Attack: How Visual Context Exposes Multimodal Safety Vulnerabilities

📄 [arXiv](https://arxiv.org/abs/2512.02973) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5772)　📅 2025-12　🏷 ECCV 2026

**关键词**：`attack`、`image attack`、`VLM safety`、`multimodal jailbreak`、`red-teaming`

👤 **作者**：Yuan Xiong、Ziqi Miao、Lijun Li、Chen Qian、Jie Li、Jing Shao

- 🎯 **研究动机**：已有 MLLM 攻击把视觉当次要 prompt，未利用图像承载复杂上下文信息的潜力
- 🔬 **研究方法**：Contextual Image Attack 用多 agent 系统以四种可视化策略把有害查询嵌入看似 benign 的视觉上下文，辅以上下文元素增强与自动毒性混淆
- 📌 **结论**：对 GPT-4o 与 Qwen2.5-VL-72B 毒性分数达 4.73/4.83，ASR 达 86.31%/91.07%，显著超越先前工作

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While Multimodal Large Language Models (MLLMs) show remarkable capabilities, their safety alignments are susceptible to jailbreak attacks. Existing attack methods typically focus on text-image interplay, treating the visual modality as a secondary prompt. This approach underutilizes the unique potential of images to carry complex, contextual information. To address this gap, we propose a new image-centric attack method, Contextual Image Attack (CIA), which employs a multi-agent system to subtly embeds harmful queries into seemingly benign visual contexts using four distinct visualization strategies. To further enhance the attack's efficacy, the system incorporate contextual element enhancement and automatic toxicity obfuscation techniques. Experimental results on the MMSafetyBench-tiny dataset show that CIA achieves high toxicity scores of 4.73 and 4.83 against the GPT-4o and Qwen2.5-VL-72B models, respectively, with Attack Success Rates (ASR) reaching 86.31\% and 91.07\%. Our method significantly outperforms prior work, demonstrating that the visual modality itself is a potent vector for jailbreaking advanced MLLMs.

</details>

### 27. Medusa: Cross-Modal Transferable Adversarial Attacks on Multimodal Medical Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2511.19257) · 🌐 [Project](https://doi.org/10.1145/3770854.3780277)　📅 2025-11　🏷 KDD 2026

**关键词**：`attack`、`medical MMed-RAG`、`cross-modal transfer`、`retrieval hijacking`、`medical RAG`、`cross-modal attack`

👤 **作者**：Yingjia Shang、…、Yefeng Zheng

- 🎯 **研究动机**：多模态医疗 RAG 经视觉输入扰动的对抗漏洞未被探索
- 🔬 **研究方法**：Medusa 黑盒跨模态可迁移攻击：用 multi-positive InfoNCE loss 把对抗视觉嵌入对齐到医学上合理但恶意的文本目标以劫持检索，结合代理集成与 IRM 增强的双循环优化提升迁移性
- 📌 **结论**：在报告生成与疾病诊断两任务上平均 ASR 超 90%，抗四种主流防御并超越 SOTA 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid advancement of retrieval-augmented vision-language models, multimodal medical retrieval-augmented generation (MMed-RAG) systems are increasingly adopted in clinical decision support. These systems enhance medical applications by performing cross-modal retrieval to integrate relevant visual and textual evidence for tasks, e.g., report generation and disease diagnosis. However, their complex architecture also introduces underexplored adversarial vulnerabilities, particularly via visual input perturbations. In this paper, we propose Medusa, a novel framework for crafting cross-modal transferable adversarial attacks on MMed-RAG systems under a black-box setting. Specifically, Medusa formulates the attack as a perturbation optimization problem, leveraging a multi-positive InfoNCE loss (MPIL) to align adversarial visual embeddings with medically plausible but malicious textual targets, thereby hijacking the retrieval process. To enhance transferability, we adopt a surrogate model ensemble and design a dual-loop optimization strategy augmented with invariant risk minimization (IRM). Extensive experiments on two real-world medical tasks, including medical report generation and disease diagnosis, demonstrate that Medusa achieves over 90% average attack success rate across various generation models and retrievers under appropriate parameter configuration, while remaining robust against four mainstream defenses, outperforming state-of-the-art baselines. Our results reveal critical vulnerabilities in the MMed-RAG systems and highlight the necessity of robustness benchmarking in safety-critical medical applications. The code and data are available at https://anonymous.4open.science/r/MMed-RAG-Attack-F05A.

</details>

### 28. FORCE: Transferable Visual Jailbreaking Attacks via Feature Over-Reliance CorrEction

📄 [arXiv](https://arxiv.org/abs/2509.21029) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Lin_FORCE_Transferable_Visual_Jailbreaking_Attacks_via_Feature_Over-Reliance_CorrEction_CVPR_2026_paper.html)　📅 2025-09　🏷 CVPR 2026

**关键词**：`attack`、`visual jailbreak`、`feature over-reliance`、`transferability`

👤 **作者**：Runqi Lin、…、Tongliang Liu

- 🎯 **研究动机**：简单视觉越狱对开源 MLLM 有效但跨模型迁移性极差，难以评估闭源模型
- 🔬 **研究方法**：分析发现攻击落点处于高尖锐度区域且不当依赖窄层表示与语义贫乏的频率成分，提出 FORCE 修正特征过度依赖、探索更平可行域
- 📌 **结论**：有效提升视觉越狱的跨模型迁移性，支撑对闭源 MLLM 的视觉红队评测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The integration of new modalities enhances the capabilities of multimodal large language models (MLLMs) but also introduces additional vulnerabilities. In particular, simple visual jailbreaking attacks can manipulate open-source MLLMs more readily than sophisticated textual attacks. However, these underdeveloped attacks exhibit extremely limited cross-model transferability, failing to reliably identify vulnerabilities in closed-source MLLMs. In this work, we analyse the loss landscape of these jailbreaking attacks and find that the generated attacks tend to reside in high-sharpness regions, whose effectiveness is highly sensitive to even minor parameter changes during transfer. To further explain the high-sharpness localisations, we analyse their feature representations in both the intermediate layers and the spectral domain, revealing an improper reliance on narrow layer representations and semantically poor frequency components. Building on this, we propose a Feature Over-Reliance CorrEction (FORCE) method, which guides the attack to explore broader feasible regions across layer features and rescales the influence of frequency features according to their semantic content. By eliminating non-generalizable reliance on both layer and spectral features, our method discovers flattened feasible regions for visual jailbreaking attacks, thereby improving cross-model transferability. Extensive experiments demonstrate that our approach effectively facilitates visual red-teaming evaluations against closed-source MLLMs.

</details>

### 29. Implicit Jailbreak Attacks via Cross-Modal Information Concealment on Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2505.16446)　📅 2025-05

**关键词**：`attack`、`LSB steganography`、`cross-modal concealment`、`query efficiency`

👤 **作者**：Zhaoxin Wang、Handing Wang、Cong Tian、Yaochu Jin

- 🎯 **研究动机**：MLLM 跨模态一致性增强使显式跨模态注入攻击更易被检测拦截
- 🔬 **研究方法**：提出 IJA，以 LSB 隐写把恶意指令嵌入图像并配良性图文 prompt，辅以代理模型对抗后缀与模板迭代优化
- 📌 **结论**：GPT-4o 与 Gemini-1.5 Pro 上平均仅 3 次查询即获超 90% ASR

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) enable powerful cross-modal reasoning capabilities. However, the expanded input space introduces new attack surfaces. Previous jailbreak attacks often inject malicious instructions from text into less aligned modalities, such as vision. As MLLMs increasingly incorporate cross-modal consistency and alignment mechanisms, such explicit attacks become easier to detect and block. In this work, we propose a novel implicit jailbreak framework termed IJA that stealthily embeds malicious instructions into images via least significant bit steganography and couples them with seemingly benign, image-related textual prompts. To further enhance attack effectiveness across diverse MLLMs, we incorporate adversarial suffixes generated by a surrogate model and introduce a template optimization module that iteratively refines both the prompt and embedding based on model feedback. On commercial models like GPT-4o and Gemini-1.5 Pro, our method achieves attack success rates of over 90% using an average of only 3 queries.

</details>

### 30. FigStep: Jailbreaking Large Vision-Language Models via Typographic Visual Prompts

📄 [arXiv](https://arxiv.org/abs/2311.05608) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/34568)　📅 2025-04　🏷 AAAI 2025

**关键词**：`attack`、`FigStep`、`typographic prompt`、`visual embedding`

👤 **作者**：Yichen Gong、…、Xiaoyun Wang

- 🎯 **研究动机**：文本安全模块可识别显式有害指令，视觉通道防护弱
- 🔬 **研究方法**：FigStep将禁止内容排版成图像文字，用良性文本引导模型读出图中内容
- 📌 **结论**：六个开源LVLM平均ASR 82.50%，失效根因是visual embedding安全对齐不足

### 31. SceneTAP: Scene-Coherent Typographic Adversarial Planner against Vision-Language Models in Real-World Environments

📄 [arXiv](https://arxiv.org/abs/2412.00114) · 🌐 [Project](https://doi.org/10.1109/CVPR52734.2025.02332)　📅 2024-11　🏷 CVPR 2025

**关键词**：`attack`、`scene-coherent typography`、`physical placement`、`adversarial planning`

👤 **作者**：Yue Cao、…、Qing Guo

- 🎯 **研究动机**：已有排版攻击文字在场景中显得突兀异常，易被识别
- 🔬 **研究方法**：SceneTAP 用 LLM Agent 三阶段规划（场景理解、对抗规划、无缝集成），配合局部扩散的 scene-coherent TextDiffuser 执行
- 📌 **结论**：数字与物理环境中均显著提升 ASR 并保持视觉自然，可误导 ChatGPT-4o 等先进 LVLM

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large vision-language models (LVLMs) have shown remarkable capabilities in interpreting visual content. While existing works demonstrate these models' vulnerability to deliberately placed adversarial texts, such texts are often easily identifiable as anomalous. In this paper, we present the first approach to generate scene-coherent typographic adversarial attacks that mislead advanced LVLMs while maintaining visual naturalness through the capability of the LLM-based agent. Our approach addresses three critical questions: what adversarial text to generate, where to place it within the scene, and how to integrate it seamlessly. We propose a training-free, multi-modal LLM-driven scene-coherent typographic adversarial planning (SceneTAP) that employs a three-stage process: scene understanding, adversarial planning, and seamless integration. The SceneTAP utilizes chain-of-thought reasoning to comprehend the scene, formulate effective adversarial text, strategically plan its placement, and provide detailed instructions for natural integration within the image. This is followed by a scene-coherent TextDiffuser that executes the attack using a local diffusion mechanism. We extend our method to real-world scenarios by printing and placing generated patches in physical environments, demonstrating its practical implications. Extensive experiments show that our scene-coherent adversarial text successfully misleads state-of-the-art LVLMs, including ChatGPT-4o, even after capturing new images of physical setups. Our evaluations demonstrate a significant increase in attack success rates while maintaining visual naturalness and contextual appropriateness. This work highlights vulnerabilities in current vision-language models to sophisticated, scene-coherent adversarial attacks and provides insights into potential defense mechanisms.

</details>

### 32. Images are Achilles' Heel of Alignment: Exploiting Visual Vulnerabilities for Jailbreaking Multimodal Large Language Models

📄 [arXiv](https://arxiv.org/abs/2403.09792) · 🌐 [Project](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9265_ECCV_2024_paper.php)　📅 2024-03　🏷 ECCV 2024

**关键词**：`attack`、`HADES`、`harmful image synthesis`、`alignment bypass`

👤 **作者**：Yifan Li、Hangyu Guo、Kun Zhou、Wayne Xin Zhao、Ji-Rong Wen

- 🎯 **研究动机**：MLLM安全过度依赖语言骨干对齐，视觉通道薄弱
- 🔬 **研究方法**：HADES用图像隐藏并放大文本中的有害意图
- 📌 **结论**：LLaVA-1.5与Gemini Pro Vision上平均ASR分别达90.26%与71.60%

### 33. Multi-turn Jailbreaking Attack in Multi-Modal Large Language Models

📄 [arXiv](https://arxiv.org/abs/2601.05339)　📅 2026-01

**关键词**：`attack`、`multi-turn MLLM jailbreak`、`fragment optimization`、`response screening`

👤 **作者**：Badhan Chandra Das、Md Tasnim Jawad、Joaquin Molto、M. Hadi Amini、Yanzhao Wu

- 🎯 **研究动机**：多轮提示下 MLLM 的越狱脆弱性及相应防御缺乏系统分析框架
- 🔬 **研究方法**：提出多轮越狱攻击与多 LLM 协同、分段优化的 FragGuard 防御机制，在开源与闭源 MLLM 及基准数据集上与现有技术对比评测
- 📌 **结论**：组合式多轮攻击可继续绕过现有安全对齐，FragGuard 相对现有技术有效缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In recent years, the security vulnerabilities of Multi-modal Large Language Models (MLLMs) have become a serious concern in the Generative Artificial Intelligence (GenAI) research. These highly intelligent models, capable of performing multi-modal tasks with high accuracy, are also severely susceptible to carefully launched security attacks, such as jailbreaking attacks, which can manipulate model behavior and bypass safety constraints. This paper introduces MJAD-MLLMs, a holistic framework that systematically analyzes the proposed Multi-turn Jailbreaking Attacks and multi-LLM-based defense techniques for MLLMs. In this paper, we make three original contributions. First, we introduce a novel multi-turn jailbreaking attack to exploit the vulnerabilities of the MLLMs under multi-turn prompting. Second, we propose a novel fragment-optimized and multi-LLM defense mechanism, called FragGuard, to effectively mitigate jailbreaking attacks in the MLLMs. Third, we evaluate the efficacy of the proposed attacks and defenses through extensive experiments on several state-of-the-art (SOTA) open-source and closed-source MLLMs and benchmark datasets, and compare their performance with the existing techniques.

</details>

### 34. Securing Multimodal AI through Internal Information Decomposition

📄 [arXiv](https://arxiv.org/abs/2607.21600) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65159)　📅 2026-07　🏷 ICML 2026

**关键词**：`detection`、`defense`、`FlowGuard`、`information decomposition`、`cross-modal consistency`、`LLM jailbreak`

👤 **作者**：Jehyeok Yeon、Hyeonjeong Ha、Qiusi Zhan、Heng Ji

- 🎯 **研究动机**：对手可把恶意意图分散到多模态以绕过单模态防护，已有防御检查原始输入输出、忽略内部融合过程
- 🔬 **研究方法**：提出 FlowGuard：受部分信息分解启发构造 FlowVectors 量化跨模态冗余、协同与模态特有主导性，监测融合预测与单模态语义证据的一致性，仅在良性数据上做单类分类
- 📌 **结论**：未见攻击的 ASR 从 >90% 降到 <15%，效用损失 <3%、延迟最多降 6 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models introduce attack surfaces absent in unimodal systems: adversaries can distribute malicious intent across modalities to evade unimodal safeguards. This motivates using cross-modal consistency as a detection signal rather than inspecting each modality in isolation. Our key observation is that benign inputs induce compatible predictive behavior from text-only and vision-only reasoning that stabilizes when fused, whereas adversarial manipulation disrupts this consistency, causing abnormal multimodal behavior. Existing defenses that examine raw inputs or outputs overlook this internal fusion process, rendering them brittle and computationally expensive. We propose FlowGuard, a lightweight inference-time framework that detects harmful inputs by monitoring internal multimodal consistency. Unlike approaches that rely on scalar confidence metrics, FlowGuard derives FlowVectors inspired by Partial Information Decomposition that quantify cross-modal redundancy, synergy, and modality-specific dominance, capturing whether fused multimodal predictions remain aligned with unimodal semantic evidence. In a one-class classification problem trained solely on benign data, FlowGuard reduces Attack Success Rates from >90% to <15% on unseen attacks, with <3% utility loss and up to a 6 times latency reduction. Our results demonstrate that monitoring cross-modal consistency offers an efficient and effective defense for multimodal reasoning.

</details>

### 35. Hard to Read, Easy to Jailbreak: How Visual Degradation Bypasses MLLM Safety Alignment

🎓 [Official](https://aclanthology.org/2026.findings-acl.983/)　📅 2026-07　🏷 ACL 2026

**关键词**：`defense`、`cognitive overload`、`visual degradation`、`structured offloading`

👤 **作者**：Zhixue Song、Boyan Han、Yiwei Wang、Chi Zhang

- 🎯 **研究动机**：视觉上下文压缩（文本渲染成图像）中降低分辨率会意外催化越狱
- 🔬 **研究方法**：实验揭示分辨率退化时 SOTA 模型安全防御急剧劣化且文本仍可读时持续，归因于 Cognitive Overload；提出 Structured Cognitive Offloading 串行管线解耦转录与安全评估
- 📌 **结论**：现象在噪声、几何畸变等多种视觉扰动下一致，串行管线可有效缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advancements in visual context compression enable MLLMs to process ultra-long contexts efficiently by rendering text into images. However, we identify a critical vulnerability inherent to this paradigm: lowering image resolution inadvertently catalyzes jailbreaking. Our experiments reveal that the safety defenses of SOTA models deteriorate sharply as resolution degrades, surprisingly persisting even when text remains legible. We attribute this to “Cognitive Overload“, hypothesizing that the effort required to decipher degraded inputs diverts attentional resources from safety auditing. This phenomenon is consistent across various visual perturbations, including noise and geometric distortion. To address this, we propose a simple “Structured Cognitive Offloading” strategy that mitigates these risks by enforcing a serialized pipeline to decouple visual transcription from safety assessment. Our work exposes a significant risk in vision-based compression and provides critical insights for the secure design of future MLLMs.

</details>

### 36. SafeSteer: A Decoding-level Defense Mechanism for Multimodal Large Language Models

📄 [arXiv](https://arxiv.org/abs/2605.11716) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.916/)　📅 2026-05　🏷 ACL 2026

**关键词**：`defense`、`decoding steering`、`harmful tendency`、`token intervention`

👤 **作者**：Xinyi Zeng、…、Yu Tian

- 🎯 **研究动机**：MLLM 越狱防御依赖昂贵微调或低效事后干预，忽视模型解码期的内在安全判别能力
- 🔬 **研究方法**：SafeSteer 用轻量 Decoding-Probe 检测并纠正解码中的有害输出、迭代把解码引向安全，并引入模态语义对齐向量把文本安全对齐迁移到视觉模态
- 📌 **结论**：多个 MLLM 上安全最高提升 33.40%，免微调并保持有用性与无害性平衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) are gaining increasing attention. Due to the heterogeneity of their input features, they face significant challenges in terms of jailbreak defenses. Current defense methods rely on costly fine-tuning or inefficient post-hoc interventions, limiting their ability to address novel attacks and involving performance trade-offs. To address the above issues, we explore the inherent safety capabilities within MLLMs and quantify their intrinsic ability to discern harmfulness at decoding stage. We observe that 1) MLLMs can distinguish the harmful and harmless inputs during decoding process, 2) Image-based attacks are more stealthy. Based on these insights, we introduce SafeSteer, a decoding-level defense mechanism for MLLMs. Specifically, it includes a Decoding-Probe, a lightweight probe for detecting and correcting harmful output during decoding, which iteratively steers the decoding process toward safety. Furthermore, a modal semantic alignment vector is integrated to transfer the strong textual safety alignment to the vision modality. Experiments on multiple MLLMs demonstrate that SafeSterr can improve MLLMs' safety by up to 33.40\% without fine-tuning. Notably, it can maintain the effectiveness of MLLMs, ensuring a balance between their helpfulness and harmlessness.

</details>

### 37. Principled Steering via Null-space Projection for Jailbreak Defense in Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2603.22094) · 🌐 [Project](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_Principled_Steering_via_Null-space_Projection_for_Jailbreak_Defense_in_Vision-Language_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`defense`、`null-space projection`、`activation steering`、`utility preservation`、`jailbreak defense`

👤 **作者**：Xingyu Zhu、…、Xiangnan He

- 🎯 **研究动机**：激活转向向量既增强拒绝又引发过度拒绝，且缺乏理论可解释性
- 🔬 **研究方法**：NullSteer 经线性变换构造拒绝方向，在良性子空间保持零扰动、沿潜在有害方向动态诱导拒绝
- 📌 **结论**：MiniGPT-4 上多样越狱攻击平均 ASR 降超 15 个百分点，通用基准性能与原模型相当

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As vision-language models (VLMs) are increasingly deployed in open-world scenarios, they can be easily induced by visual jailbreak attacks to generate harmful content, posing serious risks to model safety and trustworthy usage. Recent activation steering methods inject directional vectors into model activations during inference to induce refusal behaviors and have demonstrated effectiveness. However, a steering vector may both enhance refusal ability and cause over-refusal, thereby degrading model performance on benign inputs. Moreover, due to the lack of theoretical interpretability, these methods still suffer from limited robustness and effectiveness. To better balance safety and utility, we propose NullSteer, a null-space projected activation defense framework. Our method constructs refusal directions within model activations through a linear transformation: it maintains zero perturbation within the benign subspace while dynamically inducing refusal along potentially harmful directions, thereby theoretically achieving safety enhancement without impairing the model's general capabilities. Extensive experiments show that NullSteer significantly reduces harmful outputs under various jailbreak attacks (average ASR reduction over 15 percent on MiniGPT-4) while maintaining comparable performance to the original model on general benchmarks.

</details>

### 38. Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift

📄 [arXiv](https://arxiv.org/abs/2603.17372)　📅 2026-03

**关键词**：`defense`、`JRS-Rem`、`jailbreak direction`、`representation shift`

👤 **作者**：Zhihua Wei、…、Wen Shen

- 🎯 **研究动机**：VLM 表示空间能区分良性/有害乃至拒答与越狱样本，越狱并非识别失败而是表示被移入越狱状态
- 🔬 **研究方法**：定义 jailbreak direction，把图像诱发表示位移在该方向上的分量定为 jailbreak-related shift，JRS-Rem 在推理时移除该分量
- 📌 **结论**：跨多种越狱场景提供强防御并保持良性任务性能，统一解释了多样越狱情形

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large vision-language models (VLMs) often exhibit weakened safety alignment with the integration of the visual modality. Even when text prompts contain explicit harmful intent, adding an image can substantially increase jailbreak success rates. In this paper, we observe that VLMs can clearly distinguish benign inputs from harmful ones in their representation space. Moreover, even among harmful inputs, jailbreak samples form a distinct internal state that is separable from refusal samples. These observations suggest that jailbreaks do not arise from a failure to recognize harmful intent. Instead, the visual modality shifts representations toward a specific jailbreak state, thereby leading to a failure to trigger refusal. To quantify this transition, we identify a jailbreak direction and define the jailbreak-related shift as the component of the image-induced representation shift along this direction. Our analysis shows that the jailbreak-related shift reliably characterizes jailbreak behavior, providing a unified explanation for diverse jailbreak scenarios. Finally, we propose a defense method that enhances VLM safety by removing the jailbreak-related shift (JRS-Rem) at inference time. Experiments show that JRS-Rem provides strong defense across multiple scenarios while preserving performance on benign tasks.

</details>

### 39. SafeLogo: Turning Your Logos into Jailbreak Shields via Micro-Regional Adversarial Training

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Duan_SafeLogo_Turning_Your_Logos_into_Jailbreak_Shields_via_Micro-Regional_Adversarial_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`defense`、`visual jailbreak`、`logo shield`、`adversarial training`

👤 **作者**：Zhiyi Duan、Xiaoyue Zhang、Tianxing Man

- 🎯 **研究动机**：VLM 越狱防御需强泛化，但微调大模型昂贵、大型防御提示损害图像真实性与可用性
- 🔬 **研究方法**：提出 SafeLogo：将 min-max 对抗优化引入视觉防御提示生成，外环把扰动注入不超过 2% 像素的极小区域，内环动态生成并挑选最强越狱者训练
- 📌 **结论**：在 LLaVA-1.5-13B、MiniGPT-4 与 Qwen3-VL 上显著降低 MM-SafetyBench、VLGuard、FigStep 的越狱成功率，同时保持 MM-Vet 与 MME 良性性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent Vision-Language Models (VLMs) have become increasingly susceptible to jailbreak attacks, where adversarial prompts exploit subtle manipulation to circumvent safety alignment.The diversity and adaptability of such jailbreakers necessitate a defense mechanism with strong generalization capability.However, fine-tuning large-scale VLMs is computationally expensive, and introducing excessive visual or textual defense prompts is impractical for preserving image realism and model usability.We propose SafeLogo, which tunes a logo-sized visual prompt into a universal shield against diverse jailbreak attacks through micro-regional adversarial training.We are the first to integrate min-max adversarial optimization into visual defense prompt generation.Specifically, in the outer loop, SafeLogo injects compact, bounded perturbations into extremely small image regions (\leq 2% pixel coverage), effectively preserving both visual fidelity and semantic consistency.Meanwhile, overcoming the limitations of prior defenses constrained to a single attack direction or fixed benign supervision, the inner loop dynamically generates and selects the strongest one from a variety of jailbreakers.Extensive experiments on LLaVA-1.5-13B,MiniGPT-4, and Qwen3-VL show that SafeLogo markedly lowers jailbreak success rates on MM-SafetyBench, VLGuard, and FigStep, while preserving benign performance on MM-Vet and MME.

</details>

### 40. Understanding and Rectifying Safety Perception Distortion in VLMs

📄 [arXiv](https://arxiv.org/abs/2502.13095) · 📝 [OpenReview](https://openreview.net/forum?id=KAMsbarp3w)　📅 2025-09　🏷 NeurIPS 2025

**关键词**：`defense`、`ShiftDC`、`safety perception distortion`、`activation calibration`

👤 **作者**：Xiaohan Zou、Jian Kang、George Kesidis、Lu Lin

- 🎯 **研究动机**：图像会把unsafe activation推向模型感知的safe侧致误判
- 🔬 **研究方法**：ShiftDC将image-induced shift分解为安全相关与语义相关分量，仅移除前者
- 📌 **结论**：降低多种视觉越狱且保留视觉理解

### 41. Self-Aware Safety Augmentation: Leveraging Internal Semantic Understanding to Enhance Safety in Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2507.21637) · 🌐 [Project](https://doi.org/10.1145/3746027.3754574)　📅 2025-07

**关键词**：`defense`、`SASA`、`semantic projection`、`safety-critical head`

👤 **作者**：Wanying Wang、Zeyu Ma、Han Zheng、Xin Tan、Mingang Chen

- 🎯 **研究动机**：LVLM 的安全感知先于完整语义理解出现，导致安全能力下降
- 🔬 **研究方法**：提出 SASA：把中间层的信息性语义表示投影到更早的安全导向层，免微调增强安全识别，并以线性探测在生成前检测风险
- 📌 **结论**：多数据集与任务上显著提升安全性，效用几乎无损

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large vision-language models (LVLMs) are vulnerable to harmful input compared to their language-only backbones. We investigated this vulnerability by exploring LVLMs internal dynamics, framing their inherent safety understanding in terms of three key capabilities. Specifically, we define these capabilities as safety perception, semantic understanding, and alignment for linguistic expression, and experimentally pinpointed their primary locations within the model architecture. The results indicate that safety perception often emerges before comprehensive semantic understanding, leading to the reduction in safety. Motivated by these findings, we propose \textbf{Self-Aware Safety Augmentation (SASA)}, a technique that projects informative semantic representations from intermediate layers onto earlier safety-oriented layers. This approach leverages the model's inherent semantic understanding to enhance safety recognition without fine-tuning. Then, we employ linear probing to articulate the model's internal semantic comprehension to detect the risk before the generation process. Extensive experiments on various datasets and tasks demonstrate that SASA significantly improves the safety of LVLMs, with minimal impact on the utility.

</details>

### 42. Towards Robust Multimodal Large Language Models Against Jailbreak Attacks

📄 [arXiv](https://arxiv.org/abs/2502.00653) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Yin_Towards_Robust_Multimodal_Large_Language_Models_Against_Jailbreak_Attacks_CVPR_2026_paper.html)　📅 2025-02　🏷 CVPR 2026

**关键词**：`defense`、`multimodal jailbreak`、`robust alignment`、`adversarial training`

👤 **作者**：Ziyi Yin、Yuanpu Cao、Han Liu、Ting Wang、Jinghui Chen、Fenhlong Ma

- 🎯 **研究动机**：MLLM 越狱防御依赖外部推理步骤或对齐训练，白盒对抗扰动下低效不实用
- 🔬 **研究方法**：SafeMLLM 对抗训练框架交替攻击与更新：CoE-Attack 在对比目标下优化 token 嵌入生成扰动，再更新参数中和扰动效应
- 📌 **结论**：六个 MLLM、六种跨模态越狱方法上有效防御并保持效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While multimodal large language models (MLLMs) have achieved remarkable success in recent advancements, their susceptibility to jailbreak attacks has come to light. In such attacks, adversaries exploit carefully crafted prompts to coerce models into generating harmful or undesirable content. Existing defense mechanisms often rely on external inference steps or safety alignment training, both of which are less effective and impractical when facing sophisticated adversarial perturbations in white-box scenarios. To address these challenges and bolster MLLM robustness, we introduce SafeMLLM by adopting an adversarial training framework that alternates between an attack step for generating adversarial noise and a model updating step. At the attack step, SafeMLLM generates adversarial perturbations through a newly proposed contrastive embedding attack (CoE-Attack), which optimizes token embeddings under a contrastive objective. SafeMLLM then updates model parameters to neutralize the perturbation effects while preserving model utility on benign inputs. We evaluate SafeMLLM across six MLLMs and six jailbreak methods spanning multiple modalities. Experimental results show that SafeMLLM effectively defends against diverse attacks, maintaining robust performance and utilities.

</details>

### 43. Leave My Images Alone: Preventing Multi-Modal Large Language Models from Analyzing Images via Visual Prompt Injection

🎓 [Official](https://aclanthology.org/2026.acl-long.72/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`prompt injection`、`multimodal jailbreak`、`visual adversarial input`、`jailbreak defense`、`utility preservation`

👤 **作者**：Zedian Shao、Hongbin Liu、Yuepeng Hu、Neil Zhenqiang Gong

- 🎯 **研究动机**：MLLM 可被滥用从个人图像提取敏感信息（识别人物、泄露位置）
- 🔬 **研究方法**：ImageProtector 在图像分享前嵌入近不可感知扰动作为视觉提示注入，使恶意查询时 MLLM 一致生成拒答
- 📌 **结论**：六个 MLLM 与四个数据集上有效；高斯噪声、DiffPure、对抗训练只能部分缓解且损精度或效率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-modal large language models (MLLMs) have emerged as powerful tools for analyzing Internet-scale image data, offering significant benefits but also raising critical safety and societal concerns. In particular, these models may be misused to extract sensitive information from personal images, such as identifying individuals or revealing locations. In this work, we propose ImageProtector, a method designed to protect images from unauthorized analysis by MLLMs. Before an image is shared online, ImageProtector embeds a carefully crafted, nearly imperceptible perturbation that acts as a visual prompt injection attack on MLLMs. Consequently, when a malicious actor downloads and queries a protected image, the MLLM is consistently misled into generating a refusal response such as “I’m sorry, I can’t help with that request.” We empirically demonstrate the effectiveness of ImageProtector across six MLLMs and four datasets. Additionally, we evaluate three potential countermeasures, Gaussian noise, DiffPure, and adversarial training, and show that while they partially mitigate the impact of ImageProtector, they simultaneously degrade model accuracy and/or efficiency.

</details>

### 44. 3D FaceShell: Attribute Transfer in 3D Face Avatars as a VLM Defense Mechanism

📄 [arXiv](https://arxiv.org/abs/2607.16280) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/3820)　📅 2026-07　🏷 ECCV 2026

**关键词**：`detection`、`defense`、`VLM safety`、`multimodal jailbreak`、`visual adversarial input`、`visual privacy`

👤 **作者**：Weston Bondurant、Srijan Das、Hieu Le、Stephanie Schuckers

- 🎯 **研究动机**：共享的 3D 人脸化身任意渲染都可被 VLM 开放式推理提取敏感属性，已有 2D 防御不适用于保身份的 3D 语义操纵
- 🔬 **研究方法**：提出 3D FaceShell：在原 3D 表示上加可学习 Gaussian shell，经多视角嵌入对齐优化产生视觉不显眼但足以重定向 VLM 属性推断的分布式扰动
- 📌 **结论**：在重建的名人化身与多个黑盒 VLM 上显著提高属性注入与错配率，同时保持高感知相似度与身份一致性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Photorealistic 3D face avatars are increasingly deployed as reusable digital assets across applications such as telepresence, animation, and personalized media. At the same time, vision-language models (VLMs) can infer sensitive attributes from rendered images with open-ended semantic reasoning without any fine-tuning. This creates a new privacy challenge: once a 3D face avatar is shared, any of its renderings can be analyzed to extract high-level facial attributes. Existing defenses largely operate in 2D image space and do not address identity-preserving semantic manipulation of 3D facial representations. We propose 3D FaceShell, a framework for steering VLM interpretations of faces rendered from 3D models while preserving geometric fidelity and facial identity. 3D FaceShell augments the original 3D representation with a learnable Gaussian shell that produces subtle, spatially distributed perturbations optimized through multi-view embedding alignment. The perturbations are designed to be visually inconspicuous yet sufficient to redirect VLM-based attribute inference in a view-consistent manner. Extensive experiments on reconstructed celebrity face avatars and multiple black-box VLMs demonstrate that 3D FaceShell significantly increases attribute injection and mismatch rates while maintaining high perceptual similarity and identity consistency. Our results show that it is possible to manipulate VLM-level semantic interpretation of 3D faces without compromising their human-recognizable appearance.

</details>

### 45. Rethinking Jailbreak Detection of Large Vision Language Models with Representational Contrastive Scoring

🎓 [Official](https://aclanthology.org/2026.acl-long.992/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`jailbreak`、`VLM safety`、`multimodal jailbreak`、`multimodal safety`、`LLM jailbreak`

👤 **作者**：Peichun Hua、Hao Li、Shanghao Shi、Zhiyuan Yu、Ning Zhang

- 🎯 **研究动机**：LVLM 越狱检测要么绑定特定攻击难以泛化，要么开销高；单类异常检测易将未见良性输入误判导致过度拒绝
- 🔬 **研究方法**：提出 RCS：在安全关键层学习轻量投影最大化良性与恶意输入的表示分离，实例化为 MCD（Mahalanobis）与 KCD（K 近邻）对比检测
- 📌 **结论**：在测试对未见攻击类型泛化的高难协议上达到 SOTA，证明内部表示上的简单统计方法即可有效检测越狱

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Vision-Language Models (LVLMs) are vulnerable to a growing array of multimodal jailbreak attacks, necessitating defenses that are both generalizable to novel threats and efficient for practical deployment. Many current strategies fall short, either targeting specific attack patterns, which limits generalization, or imposing high computational overhead. While lightweight anomaly-detection methods offer a promising direction, we find that their common one-class design tends to confuse unseen benign inputs with malicious ones, leading to unreliable over-rejection. To address this, we propose Representational Contrastive Scoring (RCS), a framework built on a key insight: the most potent safety signals reside within the LVLM’s own internal representations. Our approach inspects the internal geometry of these representations, learning a lightweight projection to maximally separate benign and malicious inputs in safety-critical layers. This enables a simple yet powerful contrastive score that differentiates true malicious intent from mere distribution shift. Our instantiations, MCD (Mahalanobis Contrastive Detection) and KCD (K-nearest Contrastive Detection), achieve state-of-the-art performance on a challenging evaluation protocol designed to test generalization to unseen attack types. This work demonstrates that effective jailbreak detection can be achieved by applying simple, interpretable statistical methods to the internal representations, offering a practical path towards safer LVLM deployment.

</details>

### 46. NeuronFuzz: Safety Neuron Guided Fuzzing for LLM Safety Evaluation

📄 [arXiv](https://arxiv.org/abs/2608.26222)　📅 2026-08

**关键词**：`attack`、`benchmark`、`analysis`、`safety-neuron fuzzing`、`gradient-guided mutation`、`jailbreak transfer`

👤 **作者**：Zhiyuan Xu、Muhammad Firhard Roslan、Joseph Gardiner、Sana Belguith、Lichao Wu

- 🎯 **研究动机**：现有 LLM 安全 fuzzing 依赖响应级反馈：每个候选都要生成回答且强对齐模型上反馈稀疏
- 🔬 **研究方法**：NeuronFuzz 用稳定 safety neuron 的 prefill 激活构造连续可微 SafetyOracle 分数，指导梯度驱动的模板变异
- 📌 **结论**：21 个模型上五个白盒源模型越狱发现率 76%-100%（超基线最多 48 个百分点），模板零样本迁移至闭源模型（top-5 EASR 92.6%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety evaluation is critical for assessing whether aligned Large Language Models (LLMs) remain robust against jailbreak attacks. Existing automated testing methods, however, largely rely on response-level feedback: each candidate prompt typically requires generating a target-model response to evaluate its attack effectiveness. This process is expensive and, more importantly, provides only sparse guidance on strongly aligned models, where most candidates are rejected with the same failure outcome. This paper presents NeuronFuzz, a white-box fuzzing framework that exploits internal safety neurons as continuous execution feedback for LLM safety evaluation. A SafetyOracle converts safety-neuron activations into a continuous safety alarm score that serves as feedback for fuzzing and can be obtained during prefill, eliminating response generation from the fuzzing loop. To construct the SafetyOracle, NeuronFuzz uses template-invariant harmful and benign inputs and stability-aware selection to identify a compact set of safety neurons whose activations capture harmful-intent recognition. Moreover, since the safety alarm score is differentiable, NeuronFuzz uses its gradients to identify safety-sensitive template positions and a masked language model to generate fluent, context-compatible mutations while preserving original harmful payload and avoiding additional optimization variables. We evaluate NeuronFuzz across 21 text and multimodal models. Across five white-box source models, it achieves a 76-100% jailbreak discovery rate, outperforming baselines by up to 48 percentage points. Its optimized templates further transfer zero-shot to open-weight and six proprietary target models, achieving average ASR and top-5 ensemble ASR (EASR) of 69.6%/92.6% and 44.1%/60.0%, respectively.

</details>

### 47. SafeGesture: Evaluating Fine-Grained Hand Gesture Understanding in Vision-Language Models through Scenario-Conditioned Safety Interpretation

📄 [arXiv](https://arxiv.org/abs/2608.16081)　📅 2026-08

**关键词**：`benchmark`、`VLM safety`、`multimodal jailbreak`、`visual adversarial input`

👤 **作者**：Taegang Kim、Saleh Afroogh、Junfeng Jiao

- 🎯 **研究动机**：VLM 在安全关键运营场景中解读细粒度手势的能力未被检验
- 🔬 **研究方法**：SafeGesture 把六种 HaRID 手势与八个运营场景配对成 4800 项，评测五个 VLM 的手势识别与场景条件化安全动作推断
- 📌 **结论**：感知-推理解耦：GPT-4o 手势准确率 98.4% 但安全动作仅 53.3%（差 45 个百分点）；无视觉的场景多数策略 58.3% 高于所有模型，瓶颈在场景条件化安全推理而非手势识别

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-weight and frontier vision-language models (VLMs) perform well on general image understanding, but their ability to interpret fine-grained hand gestures in safety-critical operational contexts remains largely unexamined. We introduce SafeGesture, a benchmark that evaluates whether a model can infer scenario-appropriate safety actions from hand gestures. It pairs six HaGRID gestures with eight operational scenarios for 4,800 items and evaluates Qwen2.5-VL-7B, LLaVA-NeXT-7B, InternVL2-8B, Phi-3.5-Vision, and GPT-4o. Results reveal a perception-reasoning decoupling: GPT-4o achieves 98.4% gesture accuracy but 53.3% safety accuracy, while Qwen2.5-VL reaches 84.9% and 39.5%, yielding gaps of 45.0 and 45.4 percentage points. Four of five models rarely or never use the uncertainty label, and failure directions differ substantially across models. Accuracy also obscures label bias: a scenario-majority policy with no visual input reaches 58.3%, above every evaluated model, while only GPT-4o exceeds this prior under macro-F1. Visual input improves safety accuracy by 11.2 to 30.2 percentage points, but providing the ground-truth gesture as text improves performance by only 0.4 to 3.2 points, and no model exceeds 56.2%. These results indicate that the main bottleneck is scenario-conditioned safety reasoning rather than gesture recognition.

</details>

### 48. USB: A COMPREHENSIVE AND UNIFIED SAFETY EVALUATION BENCHMARK FOR MULTIMODAL LARGE LANGUAGE MODELS

🎓 [Official](https://aclanthology.org/2026.acl-long.970/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`multimodal safety`、`over-refusal`、`VLM safety`、`content moderation`、`harmful content`

👤 **作者**：Baolin Zheng、…、Kaifu Zhang

- 🎯 **研究动机**：现有 MLLM 安全基准风险覆盖有限、规模不足且忽视复杂模态组合（如跨模态风险），评估不可靠
- 🔬 **研究方法**：提出 USB 基准：61 个风险类别、四种模态交互；用数据合成管道生成互补数据保证覆盖均衡，同时评估有害查询脆弱性与良性输入过度拒绝
- 📌 **结论**：评测 22 个 MLLM、244 个风险-模态交叉，显示模型难以平衡脆弱性与过度拒绝，图像-only 与跨模态风险输入尤其脆弱

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite their rapid advancement, Multimodal Large Language Models (MLLMs) remain vulnerable to diverse safety risks. Current benchmarks fail to provide reliable assessments due to limited risk coverage, insufficient scale, and the oversight of complex modality combinations (e.g., cross-modal risks). To address this, we introduce the Unified Safety Benchmark (USB), a comprehensive framework covering 61 risk categories across four distinct modality interactions. We first demonstrate that existing benchmarks—even when aggregated—leave significant coverage gaps. To bridge this, we design a sophisticated data synthesis pipeline that generates complementary data, ensuring balanced coverage across all risk dimensions. Furthermore, beyond evaluating vulnerability to harmful queries, USB incorporates the simultaneous assessment of model over-refusal on benign inputs as an integrated diagnostic suite. Experimental results, evaluating 22 MLLMs across 244 risk-modality intersections, demonstrate that existing MLLMs still struggle with the trade-off between avoiding vulnerabilities and over-refusal. Models are particularly vulnerable to image-only or cross-modal risky inputs, highlighting the persistent need for refined safety mechanisms. Warning: This paper contains unfiltered and potentially harmful content that may be offensive.

</details>

### 49. ReFrame: Evidence-Guided Test-Time Safety Alignment in Multimodal Large Language Models

📄 [arXiv](https://arxiv.org/abs/2608.21100)　📅 2026-08

**关键词**：`defense`、`test-time safety alignment`、`evidence-guided reframing`、`jailbreak defense`、`risk-utility evidence`、`alignment calibration`

👤 **作者**：Wenzheng Jiang、Xuankun Rong、Yuanzhao Zhai、Dawei Feng、Huaimin Wang

- 🎯 **研究动机**：跨模态 jailbreak、安全意识缺失与过度拒答威胁 MLLM，现有对齐方法依赖重训或内部状态检查，无法用于已部署的闭源模型
- 🔬 **研究方法**：ReFrame 免训练输入重构框架：两个共享轻量本地 MLLM 的 agent 分别生成风险/效用证据并将其转为 safe proxy prompt 与 image-routing 决策，不修改下游模型即调用
- 📌 **结论**：多个 MLLM 与 benchmark 上同时改善 jailbreak 防御与安全意识、减少过度拒答，并保持多模态效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While multimodal large language models (MLLMs) extend model capabilities beyond text, they also make safety alignment increasingly challenging. Multimodal safety alignment methods must address cross-modal jailbreaks, safety-awareness failures, and over-sensitive refusals. However, existing methods often rely on retraining or internal-state inspection, limiting their applicability to deployed closed-source MLLMs and motivating test-time safety alignment. We analyze this setting and identify two key obstacles, utility dominance and reasoning inertia, which cause models to overlook latent risks or follow malicious reasoning trajectories. Guided by these insights, we propose ReFrame, a training-free multimodal input reframing framework where two agents share a lightweight locally deployed MLLM: the evidence-generation agent constructs complementary risk and utility evidence, and the rewrite-and-routing agent converts it into a safe proxy prompt and image-routing decision before calling the downstream MLLM, without modifying it or accessing its internal information. Experiments across multiple MLLMs and benchmarks show that ReFrame improves jailbreak defense, safety awareness, and oversensitivity reduction while preserving multimodal utility.

</details>

### 50. Enhancing the Safety of Medical Vision-Language Models by Synthetic Demonstrations

🎓 [Official](https://aclanthology.org/2026.eacl-long.197/)　📅 2026-03　🏷 ACL 2026

**关键词**：`defense`、`medical VLM`、`multimodal jailbreak`、`over-defense`

👤 **作者**：Zhiyu Xue、Reza Abbasi-Asl、Ramtin Pedarsani

- 🎯 **研究动机**：医学 VLM 安全漏洞探索不足：需拒绝有害查询（如用 CT 骗保），但防御又有过度拒绝良性临床查询的风险
- 🔬 **研究方法**：推理时防御：基于合成临床演示抵御视觉与文本越狱，在九种医学成像模态上验证；混合演示策略在少样本预算下平衡安全与性能
- 📌 **结论**：提升安全性且不明显损害性能，增加演示预算可缓解过度防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative medical vision-language models (Med-VLMs) are primarily designed to generate complex textual information (e.g., diagnostic reports) from multimodal inputs including vision modality (e.g., medical images) and language modality (e.g., clinical queries). However, their security vulnerabilities remain underexplored. Med-VLMs should be capable of rejecting harmful queries, such as Provide detailed instructions for using this CT scan for insurance fraud. At the same time, addressing security concerns introduces the risk of over-defense, where safety-enhancing mechanisms may degrade general performance, causing Med-VLMs to reject benign clinical queries. In this paper, we propose a novel inference-time defense strategy to mitigate harmful queries, enabling defense against visual and textual jailbreak attacks. Using diverse medical imaging datasets collected from nine modalities, we demonstrate that our defense strategy based on synthetic clinical demonstrations enhances model safety without significantly compromising performance. Additionally, we find that increasing the demonstration budget alleviates the over-defense issue. We then introduce a mixed demonstration strategy as a trade-off solution for balancing security and performance under few-shot demonstration budget constraints. Warning: This paper contains content that may be deemed harmful.

</details>

### 51. Two Birds, One Projection: Harmonizing Safety and Utility in LVLMs via Inference-time Feature Projection

📄 [arXiv](https://arxiv.org/abs/2603.14825) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4820)　📅 2026-03　🏷 ECCV 2026

**关键词**：`defense`、`feature projection`、`multimodal jailbreak`、`visual adversarial input`、`safety-utility tradeoff`

👤 **作者**：Yewon Han、Yumin Seol、EunGyung Kong、Minsoo Jo、Taesup Kim

- 🎯 **研究动机**：LVLM 安全与效用被默认为天然对抗，强化安全常损伤通用视觉推理
- 🔬 **研究方法**：识别 LLM 主干与视觉编码器次优耦合产生的模态诱导偏差方向，推理时把跨模态特征投影到该方向的零空间移除相应分量
- 📌 **结论**：仅需单次前向即同时提升安全性与效用，跨基准打破传统权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing jailbreak defence frameworks for Large Vision-Language Models often suffer from a safety utility tradeoff, where strengthening safety inadvertently degrades performance on general visual-grounded reasoning tasks. In this work, we investigate whether safety and utility are inherently antagonistic objectives. We focus on a modality induced bias direction consistently observed across datasets, which arises from suboptimal coupling between the Large Language Model backbone and visual encoders. We further demonstrate that this direction undermines performance on both tasks. Leveraging this insight, we propose Two Birds, One Projection, an efficient inference time jailbreak defence that projects cross-modal features onto the null space of the identified bias direction to remove the corresponding components. Requiring only a single forward pass, our method effectively breaks the conventional tradeoff, simultaneously improving both safety and utility across diverse benchmarks.

</details>

### 52. DMN: A Compositional Framework for Jailbreaking Multimodal LLMs with Multi-Image Inputs

🎓 [Official](https://aclanthology.org/2026.acl-long.514/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`multimodal safety`、`jailbreak`、`VLM safety`、`LLM jailbreak`、`automated red teaming`

👤 **作者**：Wenzhuo Xu、…、Quanchen Zou

- 🎯 **研究动机**：支持多图输入的 MLLM 安全对齐投入少构成新漏洞；既有越狱只用单图，无法分发有害请求或用视觉推理任务分散注意
- 🔬 **研究方法**：DMN 组合式多图越狱框架：分布式指令、多模态证据与数字链任务协同增强攻击
- 📌 **结论**：GPT-4o、Gemini-2.5-pro 与 Claude Sonnet 4 上 ASR 超 90%，大幅超越基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) are vulnerable to jailbreak attacks, which can elicit harmful responses from MLLMs. Many MLLMs support multi-image inputs, inadvertently introducing new vulnerabilities due to less efforts on multi-image safety alignment. Previous MLLM jailbreak methods only uses a single image, which restricts the attack space: they cannot distribute harmful requests across multiple images, carry abundant information, or exploit additional visual reasoning tasks to distract MLLMs. To address these limitations, in this paper, we propose a compositional jailbreak framework, DMN, which leverages D istributed instruction, M ultimodal evidence and a N umber chain task to fully enhance the jailbreak performance. Extensive experiments show that DMN is highly effective for MLLM jailbreaking, e.g. achieving attack success rates of over 90% on GPT-4o, Gemini-2.5-pro and Claude Sonnet 4, surpassing other baselines by a large margin. This compositional, multi-image jailbreak strategy reveals fundamental weaknesses in their safety mechanisms.

</details>

### 53. Decoy Images Amplify Caption-Mediated Defenses Against Encoded Jailbreaks

📄 [arXiv](https://arxiv.org/abs/2608.01043)　📅 2026-08

**关键词**：`defense`、`jailbreak`、`jailbreak defense`、`harmful intent detection`

👤 **作者**：Haoyu Zhang、Xiangchen Guan、Shibo Zheng、Mohammad Zandsalimy、Shanu Sushmita

- 🎯 **研究动机**：编码越狱 prompt 配上无关诱饵图像会大幅改变黑盒防御效果，该管线交互未被理解
- 🔬 **研究方法**：在五个前沿 VLM、两族编码攻击、三种黑盒防御上配对诱饵图像做对照实验，并用轻量编码输入检测器门控附图
- 📌 **结论**：诱饵图使 ECSO 的 ASR 最多降 73 个百分点，但无条件附图把良性拒答推高至 20-79%；检测器门控可在保留安全收益的同时回到文本基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We report a counter-intuitive interaction between image inputs and existing black-box defenses on Vision--Language Models (VLMs): pairing an encoded jailbreak prompt with an unrelated decoy image can sharply lower attack success rate (ASR). The operative change is in the defense pipeline, not in the image. Across five frontier VLMs, two encoded-attack families, and three black-box defenses, a caption-mediated defense (ECSO) that leaves ASR essentially unchanged on text-only encoded input drops it by up to $73$pp once a content-free decoy is attached; every non-saturated contrast is significant under exact McNemar tests. We advance two hypotheses for this pattern, supported by indirect evidence rather than pipeline introspection, since a black-box threat model precludes inspecting vendor internals: caption-mediated defenses branch on image presence, and intrinsic image-side safety engages on image-resident content. Three controls constrain the explanation. Blank-canvas and natural-photograph decoys reproduce the effect on every model, implicating image presence rather than content; the effect replicates on three open-weight VLMs served with no moderation layer, so it is not a vendor-filtering artifact; and a non-symbolic, meaning-based encoder reproduces it, so it is not specific to symbolic obfuscation. Attaching a decoy unconditionally is not deployable --- it raises benign refusal to $20$--$79\%$, an inflation of $+10$ to $+67$pp --- but gating attachment on a lightweight encoded-input detector returns benign refusal to the text baseline while preserving the safety gain wherever the detector fires, making detector recall the binding constraint. Under adaptive attacks that target the caption-mediated re-check, the effect degrades but holds. We frame this as an observation about pipeline interaction, not as a robust defense.

</details>

### 54. ImpText: A Benchmark and Tool-Augmented Framework for Implicit Text Reasoning

🎓 [Official](https://icml.cc/virtual/2026/poster/63174)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`safety alignment`、`refusal behavior`、`alignment robustness`、`empirical evaluation`、`fine-tuning robustness`

👤 **作者**：Litao Guo、…、YINGCONG CHEN

- 🎯 **研究动机**：MLLM 对经物理变形、视觉伪装、认知暗示隐藏的恶意隐文本识别能力未知
- 🔬 **研究方法**：定义 Implicit Text Reasoning 任务并构建 ImpText-Bench；ImpText-Reader 工具增强框架用三阶段训练协同优化工具选择与语义推理
- 📌 **结论**：现有系统极脆弱，最强专有模型 Text Match Score 仅 35.79%；ImpText-Reader 达 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) have demonstrated exceptional proficiency in standard text extraction, but they encounter significant challenges when confronting real-world implicit text. Such content typically contains malicious information, intentionally concealed through physical deformation, visual camouflage, or cognitive suggestion. These concealment techniques circumvent content moderation systems and pose severe risks to user safety. To bridge the research gap in text recognition under real-world adversarial scenarios, we define the task of Implicit Text Reasoning and introduce ImpText-Bench, a meticulously constructed benchmark. Extensive evaluations on this benchmark reveal significant vulnerability in current systems; even advanced proprietary models achieve a maximum Text Match Score of only 35.79\%. In response, we propose ImpText-Reader, a tool-augmented framework. It employs a three-stage training strategy utilizing capability-boundary data to collaboratively optimize tool selection and semantic reasoning, thereby effectively extracting hidden text. Extensive experiments demonstrate that our approach achieves SOTA performance, significantly enhancing model robustness in adversarial environments.

</details>

### 55. Seeing No Evil: Blinding Large Vision-Language Models to Safety Instructions via Adversarial Attention Hijacking

🎓 [Official](https://aclanthology.org/2026.acl-long.833/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`jailbreak`、`adversarial robustness`、`VLM safety`、`LLM jailbreak`、`automated red teaming`

👤 **作者**：Jingru Li、Wei Ren、Tianqing Zhu

- 🎯 **研究动机**：现有 LVLM 攻击直接最大化有害输出概率，与模型安全检索机制产生梯度冲突，收敛慢
- 🔬 **研究方法**：提出注意力引导视觉越狱：抑制对 system prompt token 的注意力并把生成锚定在对抗图像特征上，绕开而非压倒安全对齐
- 📌 **结论**：Qwen-VL 上 ASR 94.4%（基线 68.8%），梯度冲突降 45%、迭代少 40%；成功攻击把 system prompt 注意力压制 80%，表现为 safety blindness

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Vision-Language Models (LVLMs) rely on attention-based retrieval of safety instructions to maintain alignment during generation. Existing attacks typically optimize image perturbations to maximize harmful output likelihood, but suffer from slow convergence due to gradient conflict between adversarial objectives and the model’s safety-retrieval mechanism. We propose Attention-Guided Visual Jailbreaking, which circumvents rather than overpowers safety alignment by directly manipulating attention patterns. Our method introduces two simple auxiliary objectives: (1) suppressing attention to system-prompt tokens and (2) anchoring generation on adversarial image features. This simple yet effective push-pull formulation reduces gradient conflict by 45% and achieves 94.4% attack success rate on Qwen-VL (vs. 68.8% baseline) with 40% fewer iterations. At tighter perturbation budgets ( 𝜖=8/255 ), we maintain 59.0% ASR compared to 45.7% for standard methods. Mechanistic analysis reveals a failure mode we term safety blindness: successful attacks suppress system-prompt attention by 80%, causing models to generate harmful content not by overriding safety rules, but by failing to retrieve them.

</details>

### 56. Dissecting the Safety Circuit: Neuronal Intervention for Transferable Adversarial Attacks on VLMs

🎓 [Official](https://icml.cc/virtual/2026/poster/61105)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`adversarial attack`、`adversarial robustness`、`adversarial example`、`mechanistic analysis`、`attack transferability`

👤 **作者**：Chunlong Xie、…、Tao Xiang

- 🎯 **研究动机**：VLM 对抗攻击迁移性受限——表层扰动利用代理特定伪影而非共享安全特征；线性探针显示安全表征集中于特定中间神经元回路
- 🔬 **研究方法**：SCIA 双目标引导：抑制编码安全特征的防御回路、放大捕捉模型无关表征的可迁移回路，配对比语义引导与谱平滑正则生成视觉连贯扰动
- 📌 **结论**：显著超越 SOTA，有效绕过未见黑盒 VLM

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The limited transferability of adversarial attacks on Vision-Language Models (VLMs) stems from their failure to navigate model-specific safety alignments, where superficial perturbations exploit surrogate-specific artifacts rather than shared safety-critical features. We reveal through linear probing that safety-related representations are concentrated within specific intermediate neuronal circuits, which act as localized defense bottlenecks that can be disentangled from transferable features. To overcome this barrier, we propose the Safety Circuit Intervention Attack (SCIA), a framework that surgically steers internal representations to bypass these localized safety mechanisms. SCIA employs a dual-objective steering strategy that suppresses the defensive circuit encoding safety features while amplifying the transferable circuit capturing model-agnostic representations, effectively decoupling adversarial patterns from surrogate-specific safety behaviors. Furthermore, we incorporate contrastive semantic steering and spectral smoothness regularization to guide optimization toward compliant semantic regions while producing visually coherent perturbations. Experimental results demonstrate that SCIA significantly outperforms state-of-the-art methods in bypassing unseen black-box VLMs.

</details>

### 57. Understanding In-Context Multimodal Jailbreaks via Posterior Reweighting
📄 [arXiv](https://arxiv.org/abs/2609.10613)　📅 2026-09


👤 **作者**：Xu Zhang、Dev Mistry、Xiang Xu、Ren Wang

**关键词**：`analysis`、`in-context jailbreak`、`posterior reweighting`、`MLLM`、`scaling law`

- 🎯 **研究动机**：MLLM 上下文学习越狱为何随上下文组成扩展缺乏原理性刻画
- 🔬 **研究方法**：把对齐 MLLM 建模为竞争行为模式上的隐式后验，ICL 示例即推理时证据；导出示例数/有害占比/对抗强度/多样性 scaling law
- 📌 **结论**：后验感知防御按估计风险注入良性反证，固定干预预算下鲁棒-效用权衡优于现有 in-context 防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In-context learning (ICL) jailbreaks reveal a critical vulnerability in multimodal large language models (MLLMs): harmful demonstrations in the prompt can induce unsafe outputs without modifying model parameters. Despite extensive empirical evidence, existing work lacks a principled understanding of why such jailbreaks reliably succeed or how their effectiveness scales with context composition. We propose a posterior reweighting framework that models a safety-aligned MLLM as implicitly operating over competing behavioral modes, and interprets in-context demonstrations as inference-time evidence that dynamically shifts the model's posterior preference between safe and harmful behaviors. This view formalizes jailbreak as a process of evidence accumulation, yielding predictive scaling laws with respect to demonstration count, harmful ratio, adversarial strength, and semantic diversity. Guided by this framework, we introduce a posterior-aware inference-time defense that adaptively injects benign counter-evidence based on estimated risk, effectively suppressing harmful posterior drift while preserving model utility. Compared to existing in-context defenses, our method achieves a significantly improved robustness-utility trade-off under a fixed intervention budget. Together, our results establish posterior reweighting as a unifying and predictive framework for understanding and mitigating ICL jailbreak in MLLMs.

</details>