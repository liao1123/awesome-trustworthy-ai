# Image Generation Safety

[返回 Generative Media Security 目录](README.md)

## 研究方向

本页研究 text-to-image（T2I）生成与 instruction-based image editing 在部署阶段的安全边界，重点覆盖 prompt filter、generator、output filter、visual instruction 和多轮 editing workflow 之间的接口错位。攻击既可能通过语言、排版或分布优化绕过单次过滤，也可能把有害目标拆进多轮编辑，或利用上游图像向下游 editor 传递隐藏 payload；防御则包括 pipeline-level moderation、inference-time alignment 和面向未授权编辑的 image immunization。本页不收录只评测普通编辑能力的 benchmark，也不以训练期 LoRA poisoning 或独立 image safety classifier 为主记录对象。

## 研究脉络

- **Pipeline guardrail 逆向：** 早期研究通过 timing side channel 与多语言测试还原黑盒 T2I pipeline，发现 prompt revision、text encoder、generator 与 output filter 的安全判断并不一致。
- **Prompt jailbreak 自动化：** 攻击从手工 negation、跨语言混写发展到 prompt distribution optimization、defense profiling 与自动 red teaming，同时优化 filter evasion、目标语义和输出多样性。
- **视觉与编辑接口扩展：** 大型 image editor 开始读取箭头、标记和 visual-text prompt 后，恶意指令可完全放进图像；多轮 editing 也允许把一次会被拒绝的目标拆成连续的 benign-looking step。
- **跨服务隐式 payload：** generate-to-edit workflow 使上游服务能够在视觉上正常的图像中埋入 hint，并由下游 editor 放大为可见内容，安全分析因而需要覆盖模型组合而非单一 API。
- **防御与当前边界：** 新方法在 denoising attention、preference alignment、introspective reasoning 和 image immunization 上介入；但闭源 pipeline 会持续更新，攻击迁移性、过度过滤和 benign utility 仍需共同评测。

## Pipeline 分析与自动化 Red Teaming

### 1. Not Safe for All: Auditing the Dialect Penalty in Text-to-Image Safety Pipelines

📄 [arXiv](https://arxiv.org/abs/2608.29589)　📅 2026-09

**关键词**：`benchmark`、`analysis`、`dialect-aware moderation`、`false-positive disparity`、`under-detection`、`T2I safety pipeline`

👤 **作者**：Minkyu Kim、Juhwan Choi、YoungBin Kim

- 🎯 **研究动机**：T2I 安全护栏对非标准方言泛化不公平，均值精度 benchmark 掩盖了这一公平性失败
- 🔬 **研究方法**：在五种英语方言 23,080 对 prompt 上定义 dialect penalty，用 typo 消融定位根因，并测试 group-balanced retraining 缓解
- 📌 **结论**：NSFW-T 与 LatentGuard 出现最高 +28.29pp 且方向相反的 bias gap，OpenAI Moderation API 漏检方言内容；penalty 源于方言特征而非 OOD 敏感性，均衡重训练可缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image (T2I) safety guardrails fail to generalize equitably to non-standard dialects. Evaluating 23,080 paired prompts across five English dialects, we formalize this failure as the dialect penalty, where filters trigger based on linguistic surface features rather than semantic intent. Text-level filters fail in opposing directions: NSFW-T over-flags benign dialect prompts and LatentGuard over-flags toxic ones (bias gaps up to +28.29 pp), while the OpenAI Moderation API under-detects them. A controlled typo ablation confirms this penalty originates from flagging dialectal features, not generic out-of-distribution sensitivity. The pixel-level generator is largely dialect-agnostic; the penalty enters at text processing and cascades unevenly to post-hoc guardrails. We show this bias tracks training data imbalance and is mitigable via group-balanced retraining, with an ablation attributing the gain to balanced exposure rather than to the worst-group objective of GroupDRO (group distributionally robust optimization). Current pipelines systematically fail dialect speakers, an equity failure masked by mean accuracy benchmarks. Our official code and dataset are publicly available at https://github.com/minguinho26/dialect-penalty-t2i. Content Warning: This paper contains offensive, toxic, or disturbing text prompts and generated images.

</details>

### 2. Mind the Gap: Zero-Query Jailbreaks via Filter-Generator Discrepancy in Text-to-Image Systems

📄 [arXiv](https://arxiv.org/abs/2608.00973)　📅 2026-08

**关键词**：`attack`、`filter-generator discrepancy`、`zero-query transfer`、`surrogate ensemble`

👤 **作者**：Wanguang Li、Zhaoxin Wang、Handing Wang

- 🎯 **研究动机**：迁移式 T2I 越狱攻击离线构造对抗 prompt 但易过拟合单一代理模型，且大搜索空间浪费在低潜力候选上
- 🔬 **研究方法**：利用过滤器-生成器差异（FGD）在分词与语义阶段筛出高潜力扰动集，再做代理集进化搜索，全程零查询目标系统
- 📌 **结论**：六条黑盒流水线上平均 ASR 达 29.2%（MHSC）与 33.3%（Q16），比最强基线高约 8 与 12 个百分点，并攻入一家商用在线服务

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image (T2I) systems typically have prompt-level safety filters before the generator to block unsafe requests, yet such systems remain vulnerable to malicious jailbreak prompts. Transfer-based attacks construct adversarial prompts offline without querying the target, but they tend to overfit to a single surrogate. Moreover, they explore a large search space in which semantic or perceptual similarity alone cannot guarantee both filter evasion and preservation of the unsafe generation intent, wasting effort on low-potential candidates. We observe that the filter and the generator process the same prompt under different objectives and representations, and term this gap the Filter-Generator Discrepancy (FGD), which allows a perturbation to reduce a prompt's perceived risk to the filter while preserving the visual concept needed by the generator. Building on FGD, we propose a zero-query jailbreak framework that screens perturbations into a high-potential candidate set via observable discrepancy rules at the tokenization and semantic stages, and then performs a surrogate-ensemble evolutionary search that requires no access to the target. Experiments on six black-box pipelines and a commercial online service show that our method consistently outperforms representative baselines, raising the average attack success rate to 29.2\% (MHSC) and 33.3\% (Q16) across the six pipelines and improving over the strongest baseline by about 8 and 12 percentage points, respectively.

</details>

### 3. Dynamic Defense Profiling Enables Cognitive Jailbreak of Text-to-Image Models

📄 [arXiv](https://arxiv.org/abs/2607.17779)　📅 2026-07

**关键词**：`attack`、`defense profiling`、`belief-state inference`、`multimodal feedback`

👤 **作者**：Dongdong Yang、…、Quanchen Zou

- 🎯 **研究动机**：已有 T2I 越狱把模型反馈当二元成败信号，忽略文本拒绝、视觉阻断、语义净化等失败模式的丰富信息，探索低效且语义塌缩
- 🔬 **研究方法**：提出 MIND 认知越狱框架：把对抗提示生成重构为对潜在防御机制的信念态推断，多模态 Judge 细粒度分解反馈、Defense Profiler 迭代更新信念、Meta-Memory 检索历史有效策略，统一进推理驱动的进化优化
- 📌 **结论**：SD v1.5 上六种防御设定下 ASR 95.62%；四个商业 T2I 系统上最高 91.58%（Wan-2.5）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-Image (T2I) generative models have achieved remarkable progress in synthesizing high-quality visual content, yet they remain vulnerable to adversarial misuse, particularly in generating Not-Safe-For-Work (NSFW) images. Most existing jailbreak attacks primarily rely on heuristic prompt engineering or black-box optimization, treating model feedback as a binary signal (success or failure). This coarse-grained paradigm overlooks the rich information embedded in diverse failure modes, such as textual refusal, visual blocking, and semantic sanitization, resulting in inefficient exploration and severe semantic collapse. In this paper, we propose MIND, a cognitive jailbreak framework that reframes adversarial prompt generation as a belief-state inference problem over latent defense mechanisms. Instead of blindly searching for bypass prompts, MIND actively models the target system's latent defense mechanisms by interpreting multi-modal feedback as high-density signals. Specifically, the framework integrates three core components: (1) a Multi-modal Judge for fine-grained feedback decomposition, (2) a Defense Profiler for iterative belief updating, and (3) a Meta-Memory module for retrieving historically effective attack strategies. These components are unified within a reasoning-driven evolutionary optimization process, enabling adaptive and semantically consistent jailbreak generation. Extensive experiments on the I2P benchmark demonstrate the effectiveness of MIND. Under six representative pre-processing and post-processing defense settings applied to the Stable Diffusion v1.5 model, MIND achieves an Attack Success Rate (ASR) of 95.62%, significantly outperforming existing methods. Additionally, the effectiveness of the proposed framework is validated across four widely used commercial T2I systems, achieving the highest ASR of 91.58% on Wan-2.5.

</details>

### 4. When Understanding Becomes a Risk: Authenticity and Safety Risks in the Emerging Image Generation Paradigm

📄 [arXiv](https://arxiv.org/abs/2603.24079) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Leng_When_Understanding_Becomes_a_Risk_Authenticity_and_Safety_Risks_in_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`analysis`、`image generation`、`authenticity risk`、`multimodal understanding`

👤 **作者**：Ye Leng、…、Yang Zhang

- 🎯 **研究动机**：MLLM 统一范式的更强语义理解带来的真实性风险未被充分认识
- 🔬 **研究方法**：以扩散模型为参照，沿不安全内容生成与伪造图像合成两维系统对比 MLLM
- 📌 **结论**：MLLM 生成更多不安全图像（能理解抽象提示）；其伪造图像更难被检测器识别，检测器重训练后仍可用更长描述性输入绕过

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recently, multimodal large language models (MLLMs) have emerged as a unified paradigm for language and image generation. Compared with diffusion models, MLLMs possess a much stronger capability for semantic understanding, enabling them to process more complex textual inputs and comprehend richer contextual meanings. However, this enhanced semantic ability may also introduce new and potentially greater safety risks. Taking diffusion models as a reference point, we systematically analyze and compare the safety risks of emerging MLLMs along two dimensions: unsafe content generation and fake image synthesis. Across multiple unsafe generation benchmark datasets, we observe that MLLMs tend to generate more unsafe images than diffusion models. This difference partly arises because diffusion models often fail to interpret abstract prompts, producing corrupted outputs, whereas MLLMs can comprehend these prompts and generate unsafe content. For current advanced fake image detectors, MLLM-generated images are also notably harder to identify. Even when detectors are retrained with MLLMs-specific data, they can still be bypassed by simply providing MLLMs with longer and more descriptive inputs. Our measurements indicate that the emerging safety risks of the cutting-edge generative paradigm, MLLMs, have not been sufficiently recognized, posing new challenges to real-world safety.

</details>

### 5. PC^2: Politically Controversial Content Generation via Jailbreaking Attacks on GPT-based Text-to-Image Models

📄 [arXiv](https://arxiv.org/abs/2601.05150) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2026-01　🏷 ACM CCS 2026

**关键词**：`attack`、`jailbreak`、`image generation`、`unsafe synthesis`、`text-to-image jailbreak`、`political disinformation`

👤 **作者**：Wonwoo Choi、Minjae Seo、Minkyoo Song、Hwanjo Heo、Seungwon Shin、Myoungsung You

- 🎯 **研究动机**：T2I 安全过滤器基于语言语境评估政治敏感性，其对抗鲁棒性未被探索，而政治虚假信息危害重大
- 🔬 **研究方法**：PC² 黑盒越狱：Identity-Preserving Descriptive Mapping 把敏感关键词混淆为中性描述，Geopolitically Distal Translation 译成低敏感碎片化语言，阻断过滤器构建政治实体毒性关联
- 📌 **结论**：240 条含 36 位公众人物的 prompt 原始全部被拦截而 PC² ASR 达 86%，大幅超越 SOTA；提出多层过滤缓解可降至约 10%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid evolution of text-to-image (T2I) models has enabled high-fidelity visual synthesis on a global scale. However, these advancements have introduced significant security risks, particularly regarding the generation of harmful content. Politically harmful content, such as fabricated depictions of public figures, poses severe threats when weaponized for fake news or propaganda. Despite its criticality, the robustness of current T2I safety filters against such politically motivated adversarial prompting remains underexplored. In response, we propose $PC^2$, the first black-box political jailbreaking framework for T2I models. It exploits a novel vulnerability where safety filters evaluate political sensitivity based on linguistic context. $PC^2$ operates through: (1) Identity-Preserving Descriptive Mapping to obfuscate sensitive keywords into neutral descriptions, and (2) Geopolitically Distal Translation to map these descriptions into fragmented, low-sensitivity languages. This strategy prevents filters from constructing toxic relationships between political entities within prompts, effectively bypassing detection. We construct a benchmark of 240 politically sensitive prompts involving 36 public figures. Evaluation on commercial T2I models, specifically the GPT series, shows that while all original prompts are blocked, $PC^2$ achieves attack success rates (ASRs) of up to 86% and outperforms state-of-the-art frameworks by a large margin. We further propose a ready-to-deploy multi-layered filtering mitigation against $PC^2$-style attacks, reducing ASR to approximately 10%.

</details>

### 6. OrchJail: Jailbreaking Tool-Calling Text-to-Image Agents by Orchestration-Guided Fuzzing

📄 [arXiv](https://arxiv.org/abs/2605.07414) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63568)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`jailbreak`、`image generation`、`unsafe synthesis`、`LLM jailbreak`、`empirical evaluation`

👤 **作者**：Jianming Chen、Yawen Wang、Junjie Wang、Zhe Liu、Qing Wang、Fanjiang Xu

- 🎯 **研究动机**：工具调用 T2I 智能体的不安全输出可来自工具编排（各步良性但组合有害），纯提示越狱不适用
- 🔬 **研究方法**：OrchJail 编排引导模糊测试：从成功越狱的工具调用轨迹及其与措辞的因果关系学习高风险编排模式，引导搜索更可能触发不安全多步工具行为的提示
- 📌 **结论**：代表性 T2I 智能体上 ASR 更高、图像保真更好、查询成本更低，且抗常见越狱防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Tool-calling text-to-image (T2I) agents can plan and execute multi-step tool chains to accomplish complex generation and editing queries. However, this capability introduces a new safety attack surface: harmful outputs may arise from tool orchestration, where individually benign steps combine into unsafe results, making prompt-only jailbreak techniques insufficient. We present OrchJail, an orchestration-guided fuzzing framework for jailbreaking tool-calling T2I agents. Its core idea is to exploit high‑risk tool‑orchestration patterns: by learning from successful jailbreak tool-calling traces and their causal relationships to prompt wording, OrchJail directly guides the fuzzing search toward prompts that are more likely to trigger unsafe multi‑step tool behaviors, rather than relying on surface‑level textual perturbations. Extensive experiments demonstrate that OrchJail improves jailbreak effectiveness and efficiency across representative tool-calling T2I agents, achieving higher attack success rates, better image fidelity, and lower query costs, while remaining robust against common jailbreak defenses. Our work highlights tool orchestration as a critical, previously unexplored attack surface and provides a novel framework for uncovering safety risks in T2I agents.

</details>

### 7. Exposing Implicit Vulnerabilities in Text-to-Image Models via Adversarial Agentic Probing

🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4945)　📅 2026　🏷 ECCV 2026

**关键词**：`tool`、`benchmark`、`agentic probing`、`implicit unsafe prompt`、`black-box red teaming`、`text-to-image safety`

- 🎯 **研究动机**：T2I模型对隐式不安全提示的防线未知
- 🔬 **研究方法**：以agent化黑盒红队自动生成隐式unsafe prompt做对抗探测
- 📌 **结论**：揭示T2I安全过滤对隐式有害请求的系统性漏洞

### 8. Hidden Dangers of Compositional Generation: Diagnosing Semantic Safety Failures in Text-to-Image Models

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Hidden_Dangers_of_Compositional_Generation_Diagnosing_Semantic_Safety_Failures_in_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`analysis`、`compositional generation`、`semantic safety`、`text-to-image model`

👤 **作者**：Haoming Yang、…、Qingming Huang

- 🎯 **研究动机**：T2I 组合生成使多个概念组合可产出高风险图像而不显式表达有害内容，安全过滤对此失效
- 🔬 **研究方法**：CoRA 黑盒纯文本空间把有害意图分解为表面良性但语义完整的视觉元素，迭代选择重组引导模型恢复恶意语义
- 📌 **结论**：显著提升攻击成功率，产出更高风险输出且保持语义一致

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-Image (T2I) models have achieved significant progress in generating high-quality images, with compositional visual generation emerging as an important capability that enables them to synthesize coherent, natural scenes from multiple discrete concepts. However, this powerful compositionality, while enhancing creativity, also introduces new safety risks: combinations of different concepts can produce high-risk images without explicitly expressing harmful content. Motivated by this, we propose CoRA (Composable Reassembly Attack): an attack method that preserves the original semantics while bypassing safety filters. Unlike traditional compositional generation approaches that rely on modifying the sampling process, CoRA operates solely in the text space under a black-box setting, iteratively rewriting and guiding prompts through interactive steps. Specifically, CoRA decomposes a potentially harmful intent into a set of fine-grained, superficially benign but semantically complete visual elements, and then uses iterative selection and reassembly to guide the target T2I model to recombine these elements without triggering safety checks, thereby recovering the original malicious semantics. Experimental results show that CoRA significantly improves attack success rates, producing higher-risk outputs while maintaining semantic consistency. Warning: This paper contains offensive or disturbing content.

</details>

### 9. Exposing the Guardrails: Reverse-Engineering and Jailbreaking Safety Filters in DALL·E Text-to-Image Pipelines

🎓 [Official](https://www.usenix.org/conference/usenixsecurity25/presentation/villa)　📅 2025-08　🏷 USENIX Security 2025

**关键词**：`analysis`、`timing side channel`、`cascaded safety filter`、`multilingual jailbreak`

👤 **作者**：Corban Villa、Shujaat Mirza、Christina Pöpper

- 🎯 **研究动机**：黑盒 T2I 模型的安全护栏设计未知，缺乏逆向分析手段
- 🔬 **研究方法**：时序侧信道分析测量差分响应时间，逆向工程 T2I 管线各阶段级联安全过滤器架构；发现 DALL·E 3 的 LLM 提示改写与 CLIP 嵌入间的语言理解差异并开发否定式越狱
- 📌 **结论**：揭示 DALL·E 2 用封锁列表、DALL·E 3 用 LLM 改写的架构差异；多语言覆盖缺口使其可被低资源语言攻击，提出六类对策

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We investigate the specific design and implementation of safety guardrails in black-box text-to-image (T2I) models, such as DALL·E, which are implemented to prevent potential misuse from generating harmful image content. Specifically, we introduce a novel timing-based side-channel analysis approach to reverse engineer the safety mechanisms of DALL·E models. By measuring and analyzing the differential response times of these systems, we reverse-engineer the architecture of previously unknown cascading safety filters at various stages of the T2I pipeline. Our analysis reveals key takeaways by contrasting safety mechanisms in DALL·E 2 and DALL·E 3: DALL·E 2 uses blocklist-based filtering, whereas DALL·E 3 employs an LLM-based prompt revision stage to improve image quality and filter harmful content. We find discrepancies between the LLM's language understanding and the CLIP embedding used for image generation, which we exploit to develop a negation-based jailbreaking attack. We further uncover gaps in the multilingual coverage of safety measures, which render DALL·E 3 vulnerable to a new class of low-resource language attacks for T2I systems. Lastly, we outline six distinct countermeasures techniques and research directions to address our findings. This work emphasizes the challenges of aligning the diverse components of these systems and underscores the need to improve the consistency and robustness of guardrails across the entire T2I pipeline.

</details>

### 10. DREAM: Scalable Red Teaming for Text-to-Image Generative Systems via Distribution Modeling

📄 [arXiv](https://arxiv.org/abs/2507.16329) · 🎓 [Official](https://sp2026.ieee-security.org/accepted-papers.html)　📅 2025-07　🏷 IEEE S&P 2026

**关键词**：`tool`、`distributional red teaming`、`energy-based objective`、`diversity sampling`

👤 **作者**：Boheng Li、…、Tianwei Zhang

- 🎯 **研究动机**：自动红队把问题 prompt 发现当作孤立的逐条优化，限制可扩展性与多样性
- 🔬 **研究方法**：提出 DREAM：直接建模目标系统问题 prompt 的概率分布，以能量模型目标、GC-SPSA 优化算法与多样性感知采样实现规模化
- 📌 **结论**：在广泛 T2I 模型与安全过滤器上的成功率与多样性均达 SoTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite the integration of safety alignment and external filters, text-to-image (T2I) generative systems are still susceptible to producing harmful content, such as sexual or violent imagery. This raises serious concerns about unintended exposure and potential misuse. Red teaming, which aims to proactively identify diverse prompts that can elicit unsafe outputs from the T2I system, is increasingly recognized as an essential method for assessing and improving safety before real-world deployment. However, existing automated red teaming approaches often treat prompt discovery as an isolated, prompt-level optimization task, which limits their scalability, diversity, and overall effectiveness. To bridge this gap, in this paper, we propose DREAM, a scalable red teaming framework to automatically uncover diverse problematic prompts from a given T2I system. Unlike prior work that optimizes prompts individually, DREAM directly models the probabilistic distribution of the target system's problematic prompts, which enables explicit optimization over both effectiveness and diversity, and allows efficient large-scale sampling after training. To achieve this without direct access to representative training samples, we draw inspiration from energy-based models and reformulate the objective into a simple and tractable form. We further introduce GC-SPSA, an efficient optimization algorithm that provides stable gradient estimates through the long and potentially non-differentiable T2I pipeline. During inference, we also propose a diversity-aware sampling strategy to enhance prompt variety. The effectiveness of DREAM is validated through extensive experiments, demonstrating state-of-the-art performance across a wide range of T2I models and safety filters in terms of both prompt success rate and diversity. Our code is available at https://github.com/AntigoneRandy/DREAM

</details>

### 11. GenBreak: Red Teaming Text-to-Image Generation Using Large Language Models

📄 [arXiv](https://arxiv.org/abs/2506.10047) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_GenBreak_Red_Teaming_Text-to-Image_Generation_Using_Large_Language_Models_CVPR_2026_paper.html)　📅 2025-06　🏷 CVPR 2026

**关键词**：`benchmark`、`text-to-image safety`、`LLM red teaming`、`harmful prompt`

👤 **作者**：Zilong Wang、Xiang Zheng、Xiaosen Wang、Bo Wang、Xingjun Ma、Yu-Gang Jiang

- 🎯 **研究动机**：T2I 红队工具或能产毒却易被安全过滤拦截、或能绕过滤但不产真实有害内容，缺可靠评估工具
- 🔬 **研究方法**：提出 GenBreak：精选数据 SFT 加与代理 T2I 模型交互的 RL，多奖励信号兼顾绕过能力与图像毒性并保持语义连贯
- 📌 **结论**：生成的对抗 prompt 对商用 T2I 黑盒攻击高效，揭示实际部署的安全弱点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image (T2I) models such as Stable Diffusion have advanced rapidly and are now widely used in content creation. However, these models can be misused to generate harmful content, including nudity or violence, posing significant safety risks. While most platforms employ content moderation systems, underlying vulnerabilities can still be exploited by determined adversaries. Recent research on red-teaming and adversarial attacks against T2I models has notable limitations: some studies successfully generate highly toxic images but use adversarial prompts that are easily detected and blocked by safety filters, while others focus on bypassing safety mechanisms but fail to produce genuinely harmful outputs, neglecting the discovery of truly high-risk prompts. Consequently, there remains a lack of reliable tools for evaluating the safety of defended T2I models. To address this gap, we propose GenBreak, a framework that fine-tunes a red-team large language model (LLM) to systematically explore underlying vulnerabilities in T2I generators. Our approach combines supervised fine-tuning on curated datasets with reinforcement learning via interaction with a surrogate T2I model. By integrating multiple reward signals, we guide the LLM to craft adversarial prompts that enhance both evasion capability and image toxicity, while maintaining semantic coherence and diversity. These prompts demonstrate strong effectiveness in black-box attacks against commercial T2I generators, revealing practical and concerning safety weaknesses.

</details>

### 12. Red-Teaming Text-to-Image Models via In-Context Experience Replay and Semantic-Preserving Prompt Rewriting

📄 [arXiv](https://arxiv.org/abs/2411.16769) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2024-11

**关键词**：`attack`、`prompt injection`、`image generation`、`unsafe synthesis`、`text-to-image jailbreak`、`black-box red teaming`

👤 **作者**：Zhi-Yi Chin、Pin-Yu Chen、Wei-Chen Chiu、Mario Fritz

- 🎯 **研究动机**：已有 T2I red teaming 需白盒访问、难跨防御泛化或产生不可读对抗 token，流畅且保义的攻击 prompt 缺研究
- 🔬 **研究方法**：ICER 用 LLM 重写器生成流畅自然语言对抗 prompt，以 in-context experience replay 积累成功越狱模式，bandit 优化平衡利用与探索
- 📌 **结论**：六种安全机制上超越七个基线，超 30% 的 prompt 迁移到 DALL-E 3 与 Midjourney

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Understanding the capabilities of text-to-image (T2I) models in harmful content generation is essential to safety and compliance. However, human red-teaming is costly and inconsistent, driving the need for automatic tools that simulate realistic misuse attempts. Existing methods either require white-box access, fail to generalize across defenses, or produce uninterpretable adversarial tokens, while generating fluent prompts that preserve the original harmful intent remains underexplored despite its practical relevance. We propose ICER, a black-box framework that addresses this gap through two components: an LLM-based rewriter that produces fluent, natural-language adversarial prompts, and in-context experience replay that accumulates successful jailbreaking patterns into a reusable prior. These components are integrated via bandit optimization, enabling ICER to efficiently balance exploiting proven attack strategies with exploring new ones. Experiments across six safety mechanisms show that ICER outperforms seven baselines under both standard and semantics-preserving evaluation, with over 30% of generated prompts transferring to commercial systems like DALL-E 3 and Midjourney.

</details>

### 13. Jailbreaking Text-to-Image Models Through Cracks: Navigating Heterogeneous Safety Filters via Multi-Agent Debate

📄 [arXiv](https://arxiv.org/abs/2609.01168)　📅 2026-09

**关键词**：`attack`、`T2I guardrail`、`heterogeneous filter`、`multi-agent red teaming`、`T2I jailbreak`、`heterogeneous filters`

👤 **作者**：Kaiyan Wen、Shijie Zhang、Lu Yu、Guangdong Bai

- 🎯 **研究动机**：文本过滤器、图像分类器与跨模态检测器组成的异构 T2I 防线之间存在冲突，逐过滤器优化或整线聚合反馈都难以定位有效约束
- 🔬 **研究方法**：提出刻画异构 filter 决策边界的 Detection Surface 几何框架，以及把越狱搜索拆为探索、诊断、仲裁的 CRACK 多 Agent 辩论框架（Attack／Defense／Judge 三 Agent 迭代变异与逐层反馈）
- 📌 **结论**：复合防御下 ASR 最高 99.63%，查询数少于现有方法且保持语义保真

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image (T2I) models remain vulnerable to jailbreak attacks that elicit Not-Safe-For-Work (NSFW) content, despite increasingly being guarded by heterogeneous, multi-layer safety stacks combining text filters, image classifiers, and cross-modal detectors. Existing jailbreak studies either optimize against individual filters or query the complete pipeline with aggregate feedback, making it difficult to identify the active constraint and adapt to conflicts across safety layers. In this paper, we introduce the Detection Surface, a unified geometric framework that characterizes the decision boundaries induced by heterogeneous T2I safety filters and their joint effect on the jailbreak search space. This formulation reveals that successful evasion is governed by a sparse and non-convex region shaped by cross-layer conflicts, where mutations that bypass one filter may increase exposure to another. Motivated by this analysis, we propose CRACK, a multi-agent debate framework for adaptive jailbreak search that decomposes jailbreak search into exploration, diagnosis, and arbitration. CRACK coordinates an Attack Agent, a Defense Agent, and a Judge Agent to iteratively generate prompt mutations, obtain layer-specific diagnostic feedback, and optimize mutation strategies through reward-guided refinement. Through repeated rounds of debate, CRACK adapts its search direction to the evolving cross-layer constraints while preserving the original harmful intent. Extensive experiments across multiple T2I models, datasets, and safety configurations show that CRACK achieves Attack Success Rates (ASR) of up to 99.63% under composite defenses, while requiring fewer queries than existing methods and maintaining semantic fidelity.

</details>

### 14. TYPO: Instruction-Dense Visual Jailbreaks against Commercial Closed-Source Image-Generation Models

📄 [arXiv](https://arxiv.org/abs/2607.24897)　📅 2026-07

**关键词**：`attack`、`typography prompt`、`instruction-dense image`、`commercial T2I`

👤 **作者**：Meng Xie、…、Zhetao Li

- 🎯 **研究动机**：商业图像生成模型可生成含可读文字的图像，其安全对齐未从文本输出可靠迁移到图内嵌入文本，图内可渲染可执行的详细有害指令
- 🔬 **研究方法**：提出 TYPO 黑盒框架：把提示生成分解为文本通道（重构目标意图）与视觉通道（指定呈现形式），构建双通道策略空间经自适应组合搜索优化
- 📌 **结论**：四个商业模型（GPT-Image-2、Nano Banana Pro、Qwen-Image-2、Seedream 5.0 Lite）上 ASR 平均比九种代表性越狱高 50.2%，平均查询成本仅 0.04 美元

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent commercial image-generation models can generate high-quality images with readable text (e.g., posters, infographics, and manuals), attracting considerable attention. Yet we first show that this same capability also introduces a previously unreported safety vulnerability: these systems may refuse to generate harmful text directly, yet permit the same content when rendered as text within generated images, i.e., safety alignment does not reliably transfer from textual outputs to text embedded in images. In this paper, unlike existing visual jailbreaks against image-generation models, which primarily induce models to generate harmful visual objects or scenes, we introduce the concept of instruction-dense visual jailbreaks, in which image-generation models produce detailed, readable, and actionable harmful instructions within images. Such outputs can amplify harm because the rendered instructions can be readily read and widely spread. To instantiate this threat, we propose TYPO, a black-box framework that exploits this safety gap by automatically generating adversarial TYPOgraphy prompts, which covertly steer image-generation models to express harmful intent as highly legible, typographically structured text. Specifically, TYPO decomposes prompt generation into two channels: a textual channel for reframing the target intent, and a visual channel for specifying its presentation form. We formulate these two channels as a dual-channel textual-visual strategy space and optimize candidate strategy combinations through an adaptive combinatorial search. Extensive experiments across four commercial models (i.e., GPT-Image-2, Nano Banana Pro, Qwen-Image-2, and Seedream 5.0 Lite) show that TYPO substantially outperforms nine representative jailbreak attacks by 50.2% in ASR on average, while incurring an average query cost of only $0.04.

</details>

### 15. JANUS: A Lightweight Framework for Jailbreaking Text-to-Image Models via Distribution Optimization

📄 [arXiv](https://arxiv.org/abs/2603.21208) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Zheng_JANUS_A_Lightweight_Framework_for_Jailbreaking_Text-to-Image_Models_via_Distribution_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`attack`、`prompt distribution`、`black-box reward`、`dual anchor`、`text-to-image jailbreak`、`distribution optimization`

👤 **作者**：Haolun Zheng、…、Kui Ren

- 🎯 **研究动机**：现有 T2I 越狱攻击或依赖代理损失而非端到端目标，或需大规模昂贵的 RL 生成器
- 🔬 **研究方法**：JANUS 把越狱形式化为黑盒端到端奖励下优化结构化提示分布，用两个语义锚定分布上的低维混合策略替代高容量生成器
- 📌 **结论**：Stable Diffusion 3.5 Large Turbo 上 ASR-8 从 25.30% 提升至 43.15%，开源与商业模型均成功

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image (T2I) models such as Stable Diffusion and DALLE remain susceptible to generating harmful or Not-Safe-For-Work (NSFW) content under jailbreak attacks despite deployed safety filters. Existing jailbreak attacks either rely on proxy-loss optimization instead of the true end-to-end objective, or depend on large-scale and costly RL-trained generators. Motivated by these limitations, we propose JANUS , a lightweight framework that formulates jailbreak as optimizing a structured prompt distribution under a black-box, end-to-end reward from the T2I system and its safety filters. JANUS replaces a high-capacity generator with a low-dimensional mixing policy over two semantically anchored prompt distributions, enabling efficient exploration while preserving the target semantics. On modern T2I models, we outperform state-of-the-art jailbreak methods, improving ASR-8 from 25.30% to 43.15% on Stable Diffusion 3.5 Large Turbo with consistently higher CLIP and NSFW scores. JANUS succeeds across both open-source and commercial models. These findings expose structural weaknesses in current T2I safety pipelines and motivate stronger, distribution-aware defenses. Warning: This paper contains model outputs that may be offensive.

</details>

### 16. MacPrompt: Maraconic-Guided Jailbreak Against Text-to-Image Models

📄 [arXiv](https://arxiv.org/abs/2601.07141) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/40916)　📅 2026-01　🏷 AAAI 2026

**关键词**：`attack`、`macaronic prompt`、`cross-lingual recombination`、`concept erasure bypass`

👤 **作者**：Xi Ye、…、Jiayi Yu

- 🎯 **研究动机**：现有 T2I 防御对多样化对抗 prompt 准备不足，同义替换类攻击难以击穿概念移除
- 🔬 **研究方法**：MacPrompt 对有害词做跨语言字符级重组构造混合语言对抗 prompt，实现对语义与外观的细粒度控制
- 📌 **结论**：与原输入语义相似度最高 0.96，可令主要安全过滤器最高 100% 失效；性相关内容 ASR 达 92%、暴力 90%，可击穿 SOTA 概念移除防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image (T2I) models have raised increasing safety concerns due to their capacity to generate NSFW and other banned objects. To mitigate these risks, safety filters and concept removal techniques have been introduced to block inappropriate prompts or erase sensitive concepts from the models. However, all the existing defense methods are not well prepared to handle diverse adversarial prompts. In this work, we introduce MacPrompt, a novel black-box and cross-lingual attack that reveals previously overlooked vulnerabilities in T2I safety mechanisms. Unlike existing attacks that rely on synonym substitution or prompt obfuscation, MacPrompt constructs macaronic adversarial prompts by performing cross-lingual character-level recombination of harmful terms, enabling fine-grained control over both semantics and appearance. By leveraging this design, MacPrompt crafts prompts with high semantic similarity to the original harmful inputs (up to 0.96) while bypassing major safety filters (up to 100%). More critically, it achieves attack success rates as high as 92% for sex-related content and 90% for violence, effectively breaking even state-of-the-art concept removal defenses. These results underscore the pressing need to reassess the robustness of existing T2I safety mechanisms against linguistically diverse and fine-grained adversarial strategies.

</details>

### 17. When Memory Becomes a Vulnerability: Towards Multi-turn Jailbreak Attacks against Text-to-Image Generation Systems

📄 [arXiv](https://arxiv.org/abs/2504.20376) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhao-shiqian)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`multi-turn T2I jailbreak`、`memory mechanism`、`recursive segmentation`、`text-to-image jailbreak`、`multi-turn memory`

👤 **作者**：Shiqian Zhao、…、Luu Anh Tuan

- 🎯 **研究动机**：T2I 系统记忆机制的安全分析滞后，单条对抗 prompt 易被检测或去毒失败
- 🔬 **研究方法**：提出 Inception，以 Segmentation 按句法分解恶意 prompt、Recursion 递归处理难分子句，把恶意意图埋入会话记忆，并构建含两段安全过滤的仿真系统 VisionFlow
- 📌 **结论**：攻击成功率超 SoTA 20.0%，并在真实商用 T2I 平台验证有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern text-to-image (T2I) generation systems (e.g., DALL$\cdot$E 3) exploit the memory mechanism, which captures key information in multi-turn interactions for faithful generation. Despite its practicality, the security analyses of this mechanism have fallen far behind. In this paper, we reveal that it can exacerbate the risk of jailbreak attacks. Previous attacks fuse the unsafe target prompt into one ultimate adversarial prompt, which can be easily detected or lead to the generation of non-unsafe images due to under- or over-detoxification. In contrast, we propose embedding the malice at the inception of the chat session in memory, addressing the above limitations. Specifically, we propose Inception, the first multi-turn jailbreak attack against real-world text-to-image generation systems that explicitly exploits their memory mechanisms. Inception is composed of two key modules: segmentation and recursion. We introduce Segmentation, a semantic-preserving method that generates multi-round prompts. By leveraging NLP analysis techniques, we design policies to decompose a prompt, together with its malicious intent, according to sentence structure, thereby evading safety filters. Recursion further addresses the challenge posed by unsafe sub-prompts that cannot be separated through simple segmentation. It firstly expands the sub-prompt, then invokes segmentation recursively. To facilitate multi-turn adversarial prompts crafting, we build VisionFlow, an emulation T2I system that integrates two-stage safety filters and industrial-grade memory mechanisms. The experiment results show that Inception successfully allures unsafe image generation, surpassing the SOTA by a 20.0\% margin in attack success rate. We also conduct experiments on the real-world commercial T2I generation platforms, further validating the threats of Inception in practice.

</details>

### 18. Generate "Normal", Edit Poisoned: Branding Injection via Hint Embedding in Image Editing

📄 [arXiv](https://arxiv.org/abs/2605.10600)　📅 2026-05

**关键词**：`attack`、`generate-edit pipeline`、`hidden visual hint`、`branding injection`

👤 **作者**：Desen Sun、Jason Hon、Howe Wang、Saarth Rajan、Meng Xu、Sihang Liu

- 🎯 **研究动机**：生成-编辑两阶段工作流中，下游编辑器会识别并重渲染输入图像里近乎不可见的提示
- 🔬 **研究方法**：在生成图像中嵌入隐藏 branding hint（如 logo），分钓鱼式（攻击者控制在线生成服务）与投毒式（分发被改 T2I 模型）两种场景，测试六种 payload
- 📌 **结论**：两场景平均成功率 44.4% 与 32.2% 且 logo 视觉不可察觉；缓解方案分别达 87.4% 与 92.3%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid advancement of generative AI, users increasingly rely on image-generation models for image design and creation. To achieve faithful outputs, users typically engage in multi-turn interactions during image refinement: a text-to-image generation phase followed by a text-guided image-to-image editing phase. In this paper, we investigate a novel security vulnerability associated with such a workflow. Our key insight is that a nearly invisible hint, like branding information (e.g., a logo), embedded in an input image can be recognized by downstream generative models and subsequently re-rendered onto semantically related objects, even when the user prompt does not explicitly mention it. This form of hidden payload injection makes the attack stealthy. We study two realistic attack scenarios. The first is a phishing-based setting, in which an attacker controls an online image generation service and injects hidden content into generated images before they are returned to users. The second is a poison-based setting, where an attacker distributes a compromised text-to-image diffusion model whose output contains hidden content. We evaluate both attacks using six injected payloads, including well-known logos and customized designs, and demonstrate that the two attacks can achieve success rates of 44.4% and 32.2% on average, respectively, while ensuring the injected logos are visually imperceptible. We also develop a mitigation solution that achieves an average success rate of 87.4% and 92.3% against the phishing-based and poison-based attacks, respectively.

</details>

### 19. When the Prompt Becomes Visual: Vision-Centric Jailbreak Attacks for Large Image Editing Models

📄 [arXiv](https://arxiv.org/abs/2602.10179) · 📊 [Dataset](https://huggingface.co/datasets/CSU-JPG/IESBench) · 🌐 [Project](https://csu-jpg.github.io/vja.github.io/) · 📝 [OpenReview](https://openreview.net/forum?id=wQxRphkfxn) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60813)　📅 2026-02　🏷 ICML 2026

**关键词**：`attack`、`analysis`、`visual instruction`、`image editing jailbreak`、`IESBench`、`LLM jailbreak`

👤 **作者**：Jiacheng Hou、…、Alex Jinpeng Wang

- 🎯 **研究动机**：图像编辑模型转向视觉提示驱动，攻击面本身变为视觉通道，安全风险未被研究
- 🔬 **研究方法**：提出纯视觉到视觉的越狱攻击 VJA，并构建安全基准 IESBench 系统评估图像编辑模型
- 📌 **结论**：对 Nano Banana Pro 与 GPT-Image-1.5 的 ASR 分别达 80.9% 与 70.1%；免训练内省多模态推理防御可将弱对齐模型提升至商用水平

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in large image editing models have shifted the paradigm from text-driven instructions to vision-prompt editing, where user intent is inferred directly from visual inputs such as marks, arrows, and visual-text prompts. While this paradigm greatly expands usability, it also introduces a critical and underexplored safety risk: the attack surface itself becomes visual. In this work, we propose Vision-Centric Jailbreak Attack (VJA), the first visual-to-visual jailbreak attack that conveys malicious instructions purely through visual inputs. To systematically study this emerging threat, we introduce IESBench, a safety-oriented benchmark for image editing models. Extensive experiments on IESBench demonstrate that VJA effectively compromises state-of-the-art commercial models, achieving attack success rates of up to 80.9% on Nano Banana Pro and 70.1% on GPT-Image-1.5. To mitigate this vulnerability, we propose a training-free defense based on introspective multimodal reasoning, which substantially improves the safety of poorly aligned models to a level comparable with commercial systems, without auxiliary guard models and with negligible computational overhead. Our findings expose new vulnerabilities, provide both a benchmark and practical defense to advance safe and trustworthy modern image editing systems. Warning: This paper contains offensive images created by large image editing models.

</details>

### 20. Chain-of-Jailbreak Attack for Image Generation Models via Editing Step by Step

📄 [arXiv](https://arxiv.org/abs/2410.03869) · 🎓 [Official](https://aclanthology.org/2025.findings-acl.571/)　📅 2024-10　🏷 ACL 2025

**关键词**：`attack`、`multi-step editing`、`query decomposition`、`CoJ-Bench`

👤 **作者**：Wenxuan Wang、…、Zhaopeng Tu

- 🎯 **研究动机**：单 prompt 有害请求会被拦截，而多步编辑链缺少整链审核
- 🔬 **研究方法**：CoJ 将恶意查询分解为子查询逐步生成与迭代编辑，并构建覆盖 9 场景、3 类编辑操作与 3 种编辑元素的 CoJ-Bench
- 📌 **结论**：四个生成服务上绕过率超 60%（其他越狱方法仅 14%）；Think Twice Prompting 可防住 95% 以上

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-based image generation models, such as Stable Diffusion and DALL-E 3, hold significant potential in content creation and publishing workflows, making them the focus in recent years. Despite their remarkable capability to generate diverse and vivid images, considerable efforts are being made to prevent the generation of harmful content, such as abusive, violent, or pornographic material. To assess the safety of existing models, we introduce a novel jailbreaking method called Chain-of-Jailbreak (CoJ) attack, which compromises image generation models through a step-by-step editing process. Specifically, for malicious queries that cannot bypass the safeguards with a single prompt, we intentionally decompose the query into multiple sub-queries. The image generation models are then prompted to generate and iteratively edit images based on these sub-queries. To evaluate the effectiveness of our CoJ attack method, we constructed a comprehensive dataset, CoJ-Bench, encompassing nine safety scenarios, three types of editing operations, and three editing elements. Experiments on four widely-used image generation services provided by GPT-4V, GPT-4o, Gemini 1.5 and Gemini 1.5 Pro, demonstrate that our CoJ attack method can successfully bypass the safeguards of models for over 60% cases, which significantly outperforms other jailbreaking methods (i.e., 14%). Further, to enhance these models' safety against our CoJ attack method, we also propose an effective prompting-based method, Think Twice Prompting, that can successfully defend over 95% of CoJ attack. We release our dataset and code to facilitate the AI safety research.

</details>

### 21. Introspective Attention Modulation for Safe Text-to-Image Generation

📄 [arXiv](https://arxiv.org/abs/2607.14945) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4953)　📅 2026-07　🏷 ECCV 2026

**关键词**：`defense`、`attention modulation`、`inference-time alignment`、`benign utility`、`text-to-image safety`、`inference-time defense`

👤 **作者**：Basim Azam、Hossein Rahmani、Naveed Akhtar

- 🎯 **研究动机**：已有 T2I 安全手段（概念擦除、提示过滤、分类器门控）易被参数高效适配绕过
- 🔬 **研究方法**：提出推理时内省方法：分析与再平衡图像合成全程的注意力激活，使生成偏离不安全概念同时保持语义对齐
- 📌 **结论**：标准与对抗安全基准上取得高安全分且保持或提升对齐与感知质量，注意力空间调节比概念擦除更有前景

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

State-of-the-art flow based text-to-image (T2I) models exhibit remarkable generative abilities but remain vulnerable to producing unsafe content. Prior safety efforts range from concept erasure and prompt filtering to classifier-based gating. However, simple techniques like parameter efficient adaptations of the models easily bypass such guardrails. We introduce a unique principled approach that achieves safety by regulating the model's attention dynamics through inference-time introspection, exhibiting intrinsic robustness. Our method analyzes and rebalances attention activations throughout image synthesis, steering generations away from unsafe concepts while preserving semantic alignment. This introspective control ensures safety of deployed models. Across standard and adversarial safety benchmarks, our approach achieves remarkable safety scores while maintaining or even improving alignment and perceptual quality. Our results reveal that attention-space regulation offers a considerably more promising path to safer diffusion transformer based image generation than the existing concept erasing mechanism.Our code can be accessed at https://basim-azam.github.io/iam/

</details>

### 22. The Illusion of High Utility in Safety Alignment of Text-to-Image Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2607.00402) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5377)　📅 2026-07　🏷 ECCV 2026

**关键词**：`analysis`、`semantic collapse`、`alignment utility`、`SAGE`、`safety alignment`、`utility evaluation`

👤 **作者**：Adeel Yousaf、Soumik Ghosh、James Beetham、Amrit Singh Bedi、Mubarak Shah

- 🎯 **研究动机**：T2I 安全对齐的高效用结论建立在 FID 等粗粒度指标上，对细粒度语义正确性不敏感，造成高效用幻觉
- 🔬 **研究方法**：用 TIFA 结构化评估揭示语义保真大幅下降；分析文本编码器嵌入空间发现语义塌缩（嵌入展布收缩+提示间相似结构扭曲）与结构化效用损失强相关；提出 SAGE 几何正则在适配中保持嵌入展布与关系结构
- 📌 **结论**：SAGE 恢复结构化效用（TIFA 较先前 SOTA +5.0%）并保持强安全性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment of text-to-image (T2I) diffusion models aims to suppress harmful generations while preserving utility on benign prompts. Recent methods often appear to deliver high safety with high utility, but this conclusion rests largely on coarse global utility metrics (e.g., FID, CLIPScore) that are insensitive to fine-grained semantic correctness, creating an illusion of high utility. We show that when utility is measured with structured evaluation, this illusion breaks: on TIFA (Text-to-Image Faithfulness evaluation with Question Answering), safety-aligned models suffer substantial drops in semantic fidelity, including failures in object counts, attributes, and relationships. To diagnose the source of this gap, we analyze the text-encoder prompt embedding space and uncover semantic collapse, a contraction of embedding spread coupled with distortion of inter-prompt similarity structure, which strongly correlates with structured utility loss. Guided by this insight, we propose StructureAware Geometric Regularization (SAGE), a safety alignment objective that explicitly preserves embedding spread and inter-prompt relational structure during adaptation. Our method restores structured utility (TIFA +5.0% over prior state-of-the-art) while maintaining strong safety performance and competitive coarse-grained utility scores. Our source code and trained models are available at https://adeelyousaf.github.io/SAGE_ECCV26_Project_Page/.

</details>

### 23. MIRAGE: Protecting against Malicious Image Editing via False Moderation

📄 [arXiv](https://arxiv.org/abs/2606.26199)　📅 2026-06

**关键词**：`defense`、`image immunization`、`false moderation`、`commercial editor`

👤 **作者**：Anshul Nasery、Ramnath Kumar、Cho-Jui Hsieh、Sewoong Oh

- 🎯 **研究动机**：已有图像免疫方法需模型权重与编辑提示访问，对 GPT-Image、Nano Banana 等商业编辑器不适用
- 🔬 **研究方法**：提出 MIRAGE：从系统层切入生成前安全审核这一共同攻击面，把图像对齐到开源嵌入与审核模型集成的策略违规概念表示，使审核分类器拦截任意编辑请求
- 📌 **结论**：对多个闭源图像编辑 API 成功率超 88%，方法简单且与提示无关

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of AI-powered image editing systems raises serious concerns because it allows personal images to be arbitrarily manipulated at scale, with minimal effort, and a lower barrier to entry. Prior work on image immunization adds imperceptible perturbations to an image to protect against unauthorized manipulations. However, these methods usually require access to the model weights and the image manipulating prompt. This significantly limits their use, especially against powerful commercial image-editors such as GPT-Image, Gemini Flash Image (Nano Banana), and Grok Imagine. To address this, we take a system-level view of the problem and identify a previously unexplored attack surface common to all major commercial image editing systems: pre-generation safety moderation. Rather than disrupting the generative model itself, we propose to immunize images by causing these moderation classifiers to flag images as policy-violating, triggering an automatic refusal regardless of the editing prompt. We operationalize this by adding adversarial perturbations to align our image to policy-violating concepts in the representation space of an ensemble of open-source embedding and moderation models. We call our method MIRAGE, which stands for Moderation Induced Resistance Against Generative Editing. We evaluate MIRAGE against multiple closed-source image editing APIs and demonstrate success rates of more than 88%. Our approach is simple, prompt-agnostic, and effective, offering a practical path towards protecting personal images from unauthorized AI-powered editing.

</details>

### 24. SafeRoPE: Risk-specific Head-wise Embedding Rotation for Safe Generation in Rectified Flow Transformers

📄 [arXiv](https://arxiv.org/abs/2604.01826) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_SafeRoPE_Risk-specific_Head-wise_Embedding_Rotation_for_Safe_Generation_in_Rectified_CVPR_2026_paper.html)　📅 2026-04　🏷 CVPR 2026

**关键词**：`defense`、`safe generation`、`risk-specific steering`、`rectified flow`

👤 **作者**：Xiang Yang、Feifei Li、Mi Zhang、Geng Hong、Xiaoyu You、Min Yang

- 🎯 **研究动机**：概念遗忘方法计算昂贵且面向 U-Net 设计，难以适配整流流 transformer（MMDiT）
- 🔬 **研究方法**：发现不安全语义集中于头部级低维子空间；SafeRoPE 分解安全关键头部的不安全子空间计算 Latent Risk Score，对 query/key 的 RoPE 做风险特定扰动
- 📌 **结论**：在 SD3、FLUX 类模型上实现有害内容抑制与生成效用的 SOTA 平衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent Text-to-Image (T2I) models based on rectified-flow transformers (e.g., SD3, FLUX) achieve high generative fidelity but remain vulnerable to unsafe semantics, especially when triggered by multi-token interactions. Existing mitigation methods largely rely on fine-tuning or attention modulation for concept unlearning; however, their expensive computational overhead and design tailored to U-Net-based denoisers hinder direct adaptation to transformer-based diffusion models (e.g., MMDiT). In this paper, we conduct an in-depth analysis of the attention mechanism in MMDiT and find that unsafe semantics concentrate within interpretable, low-dimensional subspaces at head level, where a finite set of safety-critical heads is responsible for unsafe feature extraction. We further observe that perturbing the Rotary Positional Embedding (RoPE) applied to the query and key vectors can effectively modify some specific concepts in the generated images. Motivated by these insights, we propose SafeRoPE, a lightweight and fine-grained safe generation framework for MMDiT. Specifically, SafeRoPE first constructs head-wise unsafe subspaces by decomposing unsafe embeddings within safety-critical heads, and computes a Latent Risk Score (LRS) for each input vector via projection onto these subspaces. We then introduce head-wise RoPE perturbations that can suppress unsafe semantics without degrading benign content or image quality. SafeRoPE combines both head-wise LRS and RoPE perturbations to perform risk-specific head-wise rotation on query and key vector embeddings, enabling precise suppression of unsafe outputs while maintaining generation fidelity. Extensive experiments demonstrate that SafeRoPE achieves SOTA performance in balancing effective harmful content mitigation and utility preservation for safe generation of MMDiT. Codes are available at https://github.com/deng12yx/SafeRoPE.

</details>

### 25. Universal Image Immunization against Diffusion-based Image Editing via Semantic Injection

📄 [arXiv](https://arxiv.org/abs/2602.14679) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/3278)　📅 2026-02　🏷 ECCV 2026

**关键词**：`defense`、`universal immunization`、`semantic injection`、`black-box transfer`

👤 **作者**：Chanhui Lee、Donggyu Choi、Seunghyun Shin、Hae-Gon Jeon、Jeany Son

- 🎯 **研究动机**：现有图像免疫需逐图优化或推理时附加网络，难以规模化抵御扩散模型编辑滥用
- 🔬 **研究方法**：学习单一图像无关的通用对抗扰动，诱导扩散模型把输入误读为特定语义目标并压制原内容以阻断未授权编辑
- 📌 **结论**：在 UAP 设定下显著超越基线，更小扰动预算下媲美逐图方法，且跨扩散模型黑盒迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion model advances have enabled powerful text-guided image editing, but also raise ethical and legal risks such as deepfakes and unauthorized use. To prevent these risks, adversarial attack-based image immunization has emerged as a promising defense against AI-driven semantic manipulation. Yet, most existing approaches require image-specific optimization or additional neural networks at inference time, hindering scalability and practicality. In this paper, we propose the first universal adversarial perturbation-based image immunization framework that generates a single, image-agnostic adversarial perturbation specifically designed for diffusion-based editing pipelines. Inspired by UAP used in targeted attacks, our method aims to generate a UAP that induces diffusion models to misinterpret the input image as a specific semantic target. Simultaneously, it suppresses original content to misdirect the model's attention during editing, thereby effectively blocking unauthorized edits by overwriting the image's original semantics via the UAP. Extensive experiments show that our method, as the first universal immunization approach, significantly outperforms several baselines in the UAP setting. Notably, despite the inherent difficulty of universal perturbations, our method achieves competitive or superior performance compared to image-specific methods under a more restricted perturbation budget, while also exhibiting strong black-box transferability across diverse diffusion models.

</details>

### 26. When Safety Collides: Resolving Multi-Category Harmful Conflicts in Text-to-Image Diffusion via Adaptive Safety Guidance

📄 [arXiv](https://arxiv.org/abs/2602.20880) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Xiang_When_Safety_Collides_Resolving_Multi-Category_Harmful_Conflicts_in_Text-to-Image_Diffusion_CVPR_2026_paper.html)　📅 2026-02　🏷 CVPR 2026

**关键词**：`defense`、`multi-risk safety`、`adaptive guidance`、`text-to-image model`

👤 **作者**：Yongli Xiang、Ziming Hong、Zhaoqing Wang、Xiangyu Zhao、Bo Han、Tongliang Liu

- 🎯 **研究动机**：按多危害类别平均的安全引导会在缓解一类危害时放大另一类，产生 harmful conflicts
- 🔬 **研究方法**：CASG 免训练框架动态识别与生成状态最对齐的危害类别，仅沿该类别方向施加安全引导以避免多类干扰
- 📌 **结论**：在 T2I 安全基准上有害率比现有方法最多再降 15.4%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-Image (T2I) diffusion models have demonstrated significant advancements in generating high-quality images, while raising potential safety concerns regarding harmful content generation. Safety-guidance-based methods have been proposed to mitigate harmful outputs by steering generation away from harmful zones, where the zones are averaged across multiple harmful categories based on predefined keywords. However, these approaches fail to capture the complex interplay among different harm categories, leading to "harmful conflicts" where mitigating one type of harm may inadvertently amplify another, thus increasing overall harmful rate. To address this issue, we propose Conflict-aware Adaptive Safety Guidance (CASG), a training-free framework that dynamically identifies and applies the category-aligned safety direction during generation. CASG is composed of two components: (i) Conflict-aware Category Identification (CaCI), which identifies the harmful category most aligned with the model's evolving generative state, and (ii) Conflict-resolving Guidance Application (CrGA), which applies safety steering solely along the identified category to avoid multi-category interference. CASG can be applied to both latent-space and text-space safeguards. Experiments on T2I safety benchmarks demonstrate CASG's state-of-the-art performance, reducing the harmful rate by up to 15.4% compared to existing methods.

</details>

### 27. LoRAShield: Data-Free Editing Alignment for Secure Personalized LoRA Sharing

📄 [arXiv](https://arxiv.org/abs/2507.07056) · 🌐 [Project](https://doi.org/10.1145/3770855.3817625)　📅 2025-07　🏷 KDD 2026

**关键词**：`defense`、`LoRA safety editing`、`malicious concept suppression`、`utility retention`、`personalized LoRA`、`image safety`

👤 **作者**：Jiahao Chen、…、Shouling Ji

- 🎯 **研究动机**：良性 LoRA 可被武器化生成政治、诽谤类有害内容，概念擦除防御只针对完整扩散模型
- 🔬 **研究方法**：提出 LoRAShield：首个免数据 LoRA 安全编辑框架，平台侧经对抗优化与语义增强动态编辑 LoRA 权重子空间
- 📌 **结论**：有效拦截恶意生成且不损良性任务功能，支撑个性化 LoRA 的安全共享

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of Low-Rank Adaptation (LoRA) models has democratized personalized text-to-image generation, enabling users to share lightweight models (e.g., personal portraits) on platforms like Civitai and Liblib. However, this "share-and-play" ecosystem introduces critical risks: benign LoRAs can be weaponized by adversaries to generate harmful content (e.g., political, defamatory imagery), undermining creator rights and platform safety. Existing defenses like concept-erasure methods focus on full diffusion models (DMs), neglecting LoRA's unique role as a modular adapter and its vulnerability to adversarial prompt engineering. To bridge this gap, we propose LoRAShield, the first data-free editing framework for securing LoRA models against misuse. Our platform-driven approach dynamically edits and realigns LoRA's weight subspace via adversarial optimization and semantic augmentation. Experimental results demonstrate that LoRAShield achieves remarkable effectiveness, efficiency, and robustness in blocking malicious generations without sacrificing the functionality of the benign task. By shifting the defense to platforms, LoRAShield enables secure, scalable sharing of personalized models, a critical step toward trustworthy generative ecosystems.

</details>

### 28. The Path to Reconciling Quality and Safety Alignment in Text-to-Image Generation

📄 [arXiv](https://arxiv.org/abs/2504.14290) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5345)　📅 2025-04　🏷 ECCV 2026

**关键词**：`defense`、`preference optimization`、`LibraAlign-100K`、`quality-safety trade-off`、`text-to-image safety`、`safety data`

👤 **作者**：Shouwei Ruan、…、Xingxing Wei

- 🎯 **研究动机**：T2I 安全对齐存在数据信号偏、优化只顾安全奖励、评测协议粗糙三重系统性问题，安全与质量此消彼长
- 🔬 **研究方法**：构建双标注数据集 LibraAlign-100K，提出复合安全与质量奖励的 T2I-SPO 偏好优化及 Unified Alignment Score 指标
- 📌 **结论**：对广泛 NSFW 概念取得 SoTA 安全对齐，同时更好保持生成质量与通用能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Content safety is a fundamental challenge for text-to-image (T2I) models, yet prevailing methods enforce a debilitating trade-off between safety and generation quality. We argue that mitigating this trade-off hinges on addressing systemic challenges in current T2I safety alignment across data, methods, and evaluation protocols. To this end, we introduce a unified framework for synergistic safety alignment. First, to overcome the flawed data paradigm that provides biased optimization signals, we develop LibraAlign-100K, the first large-scale dataset with dual annotations for safety and quality. Second, to address the myopic optimization of existing methods focus solely on safety reward, we propose Synergistic Preference Optimization (T2I-SPO), a novel alignment algorithm that extends the DPO paradigm with a composite reward function that integrates generation safety and quality to holistically model user preferences. Finally, to overcome the limitations of quality-agnostic and binary evaluation in current protocols, we introduce the Unified Alignment Score, a holistic, fine-grained metric that fairly quantifies the balance between safety and generative capability. Extensive experiments demonstrate that T2I-SPO achieves state-of-the-art safety alignment against a wide range of NSFW concepts, while better maintaining the model's generation quality and general capability

</details>

### 29. GuardPaint: Speculative Safety Decoding for Text-to-Image Generation

📄 [arXiv](https://arxiv.org/abs/2608.21869)　📅 2026-08

**关键词**：`defense`、`intermediate-image auditor`、`policy compliance`、`surgical inpainting`、`speculative safety decoding`、`trajectory auditing`

👤 **作者**：Shreyash Dhoot、…、Amitava Das

- 🎯 **研究动机**：T2I 防御多在生成前过滤 prompt 或生成后分类图像，去噪过程本身无守卫，且往往只能拒绝而无法安全修复
- 🔬 **研究方法**：GuardPaint 推测式安全解码：轻量 auditor 监测中间图像并定位不安全区域，仅由策略对齐 inpainter 做局部修复，guarded tournament 只接受提升合规且保持 prompt 保真与感知质量的编辑，不修改基座模型
- 📌 **结论**：在 SneakPrompt、MMA、PGJ、DACA、RABell 五类越狱与 SD1.5/SDXL/SD3.5/FLUX.1-dev 上降低攻击成功与有害生成，图像质量和良性行为几乎无损

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image (T2I) diffusion models offer powerful visual generation, but their controllability creates a critical safety challenge: adversarial prompts can steer the denoising trajectory toward policy-violating content such as explicit nudity or graphic violence. Existing safeguards mostly act before generation through prompt filtering or after generation through image classification, leaving the diffusion process itself unguarded and often yielding only refusal rather than safe visual repair. We introduce GuardPaint, a speculative decoding framework for safe T2I generation that intervenes inside the diffusion trajectory without modifying the base model. A lightweight auditor monitors intermediate images, localizes unsafe regions, and triggers surgical inpainting repair only where needed. Candidate repairs are generated by a policy-aligned inpainter and selected through a guarded tournament that accepts edits only when they improve policy compliance while preserving prompt fidelity and perceptual quality. Across five jailbreak families SneakPrompt, MMA, PGJ, DACA, and RABell and UNet/flow-matching models including SD~1.5, SDXL, SD~3.5, and FLUX.1-dev. GuardPaint reduces attack success and harmful generations with minimal degradation to image quality, prompt fidelity, and benign behavior. Content warning: This paper contains examples involving nudity and violence that some readers may find disturbing, distressing, or offensive.

</details>

### 30. DiSCO: Defending text-to-image generation through distribution-guided contrastive prompt optimization

📄 [arXiv](https://arxiv.org/abs/2608.17067)　📅 2026-08

**关键词**：`defense`、`black-box T2I guardrail`、`safe-unsafe image pool`、`prompt rewriting`、`black-box T2I safeguard`、`contrastive prompt optimization`

👤 **作者**：Tong Zhang、Motasem Alfarra、Carlos Hinojosa、Christos Louizos、Bernard Ghanem

- 🎯 **研究动机**：T2I 防御多为白盒；LLM 改写式黑盒防御败于良性对抗问题——语言安全却因模型数据分布触发有害生成
- 🔬 **研究方法**：DiSCO 零样本纯黑盒 prompt 级即插即用模块：束搜索做分布引导后缀扩展，以目标模型自生成的安全/不安全图像池对比打分并迭代自适应反馈
- 📌 **结论**：I2P 基准多种红队攻击下对无防御与已有防御模型分别降低 ASR 37.7% 与 25.13%，同时保持语义保真并提升图像连贯性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As text-to-image generative models advance, they raise critical safety concerns, particularly the generation of Not-Safe-For-Work (NSFW) content such as violence and nudity, further exacerbated by red-teaming adversarial attacks. Existing defenses predominantly operate under white-box assumptions, relying on text encoder optimization, weight editing, or inference-time intervention, and fundamentally cannot scale to proprietary models. Black-box alternatives based on LLM prompt rewriting offer broader applicability, yet fail in a critical regime we identify as the \textit{benign adversarial} problem: prompts that are linguistically safe but still trigger harmful generation due to the model's learned data distribution. We propose DiSCO, a zero-shot, strictly black-box defense that operates entirely at the prompt level as a plug-and-play module, requiring no model retraining, fine-tuning, or access to model internals. DiSCO performs distribution-guided suffix expansion via beam search, optimized through contrastive scoring over safe and unsafe image pools generated by the target model itself, with iterative adaptive feedback until safe content is produced. We demonstrate that DiSCO consistently enhances the safety of both undefended and defended models on the I2P benchmark under multiple red-teaming attacks, achieving 37.7% and 25.13% ASR reduction, respectively, while maintaining semantic fidelity and improving image coherence. As a black-box, architecture-agnostic module, DiSCO can be readily applied to any text-to-image system without necessitating any changes to the model itself.

</details>

### 31. Safe Autoregressive Image Generation with Iterative Self-Improving Codebooks

📄 [arXiv](https://arxiv.org/abs/2606.27147) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62378)　📅 2026-06　🏷 ICML 2026

**关键词**：`defense`、`diffusion model`、`VLM safety`、`image generation`、`safety alignment`、`fine-tuning robustness`

👤 **作者**：Yunqi Xue、Zhijiang Li、Philip Torr、Jindong Gu

- 🎯 **研究动机**：自回归统一多模态模型经离散视觉 token 码本生成图像，其生成安全性未被研究
- 🔬 **研究方法**：提出迭代自改进码本：用统一模型自身判别不安全生成构建有害/安全图文对与 Harmful Space，冻结内在表示消除有害映射，再在无害空间自适应微调码本保质量，迭代至无改进
- 📌 **结论**：无需人工标注与外部反馈即迭代提升自回归图像生成安全性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unlike diffusion-based models that operate in continuous latent spaces, autoregressive unified multimodal models produce images by sequentially predicting discretized visual tokens. These tokens are derived from a codebook that maps embeddings to quantized visual patterns. The language-like architecture enables unified multimodal models to effectively capture text conditional information for generation, making them promising for text-to-image tasks. This also raises an interesting question: how safe are the images generated in such an autoregressive way? In this work, we propose iterative self-improving codebooks for safe autoregressive generation. We leverage the understanding and judgment capabilities of the unified multimodal model itself to identify unsafe generated images without human annotation. Subsequently, the inherent representations in the codebook are fixed to eliminate harmful mappings. Our method comprises two steps: first, we use the unified model to identify unsafe generations and construct corresponding harmful and safe image-text pairs. These pairs are used to construct the Harmful Space and guide updates to the codebook, thereby eliminating harmful outputs. Second, we perform adaptive fine-tuning on the codebook within the harmless space using safe image-text pairs to ensure the quality of generated images. These two steps are repeated until no further improvement is observed, producing a safety-enhanced model codebook. Without additional external feedback, the safety of models is improved iteratively.

</details>

### 32. Unified Safe In-context Image Generation in Multimodal Diffusion Transformers via Restricting Unsafe Information Flows

📄 [arXiv](https://arxiv.org/abs/2606.06875) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66357)　📅 2026-06　🏷 ICML 2026

**关键词**：`defense`、`diffusion model`、`VLM safety`、`image generation`、`safety alignment`、`fine-tuning robustness`

👤 **作者**：Xiang Yang、…、Min Yang

- 🎯 **研究动机**：现有安全机制面向 T2I 或 U-Net 架构，难以在 DiT 统一框架内同时缓解 T2I 与 I2I 编辑的不安全生成
- 🔬 **研究方法**：提出免训练 UVR：分析 MM-Attn 信息流，识别任务无关的启动阶段（不安全语义快速涌现并可定位），随后针对性调制注意力、切断有害信息流
- 📌 **结论**：图像合成与编辑任务分别达 91% 与 77% 擦除率，保持视觉质量与保真度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion transformers (DiTs) equipped with multimodal attention (MM-Attn) have become a dominant paradigm for image generation. However, preventing the generation of harmful content remains a critical challenge, particularly in image-to-image (I2I) editing tasks. Existing safety mechanisms are primarily designed for text-to-image (T2I) synthesis or U-Net-based architectures, which limits their effectiveness for unified safety mitigation in DiT-based frameworks. To bridge this gap, we propose Unified Visual Safety Regulator (UVR), a training-free safe generation framework that regulates unsafe semantics in generated images. UVR is grounded in an analysis of attention dynamics from the perspective of information flow in MM-Attn. We identify a task-independent start-up stage, during which unsafe semantics in output patches rapidly emerge and can be accurately localized, followed by task-specific semantic amplification and interference stages, where harmful signals are further propagated and entangled with benign content. Based on these observations, UVR mitigates unsafe generation through unified, targeted attention modulation and explicit restriction of harmful information flow over the identified unsafe output patches. Experiments across various concepts show that UVR achieves state-of-the-art safety performance by achieving 91% and 77% erase rate in image synthesis and editing tasks, while preserving visual quality and fidelity with minimal degradation. Code is available at https://github.com/deng12yx/UVR.

</details>

### 33. Towards Seed-Robust Safety Alignment in Text-to-Image Models

🎓 [Official](https://icml.cc/virtual/2026/poster/64210)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safety alignment`、`image generation`、`unsafe synthesis`、`diffusion model`、`fine-tuning robustness`

👤 **作者**：Zhenyu Wu、Yao Huang、Shouwei Ruan、Xingxing Wei

- 🎯 **研究动机**：T2I 安全机制跨随机种子不稳定，同一恶意 prompt 在不同噪声初始化下产生有害变体簇；直接扩展 NCA 存在梯度反转与有害样本均匀抑制两大缺陷
- 🔬 **研究方法**：提出 NCD：移除引发梯度反转的正则项，引入成对正则机制建立安全与有害变体间的个性化偏好关系
- 📌 **结论**：种子级攻击成功率从 11.1% 降至 6.2%，优于 SOTA，同时抗越狱 prompt 并跨 T2I 架构泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image diffusion models have achieved remarkable success in generating high-quality images, yet existing safety mechanisms exhibit critical cross-seed instability where defense performance varies significantly under different random seed conditions. This instability stems from the fact that a single malicious prompt generates diverse harmful variants across different noise initializations, forming complex distributional clusters that current methods cannot adequately address. We investigate extending Noise Contrastive Alignment (NCA) to diffusion models due to its native capability of handling multiple negative samples through probabilistic weighting, but our theoretical analysis reveals two fundamental flaws in direct extension: gradient reversal caused by positive regularization terms that paradoxically penalize safe content generation, and uniform suppression of harmful samples that ignores severity variations. To tackle these issues, we propose Noise Contrastive Diffusion (NCD), which incorporates targeted algorithmic modifications including elimination of problematic regularization and introduction of pairwise regularization mechanisms that establish individualized preference relationships between safe and harmful variants. Extensive experiments further demonstrate that NCD achieves superior cross-seed stability, reducing attack success rates (ASRs) from 11.1% to 6.2% compared to SOTA methods at the seed level while maintaining exceptional generation quality, exhibiting robust resistance against sophisticated jailbreak prompts and strong generalizability across different T2I architectures. WARNING: This paper may contain examples of harmful texts and images.

</details>