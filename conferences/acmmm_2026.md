# ACM MM 2026: AI Safety Papers

## 目录

- [会议信息](#会议信息)
- [关键节点](#关键节点)
- [筛选说明](#筛选说明)
- [多模态大模型越狱与有害内容攻防](#多模态大模型越狱与有害内容攻防)
- [智能体与 GUI Agent 安全](#智能体与-gui-agent-安全)
- [投毒、后门与记忆完整性](#投毒后门与记忆完整性)
- [对抗攻击与鲁棒性防御](#对抗攻击与鲁棒性防御)
- [隐私攻击与面部隐私保护](#隐私攻击与面部隐私保护)
- [机器遗忘、概念删除与治理](#机器遗忘概念删除与治理)
- [模型资产保护、水印与版权](#模型资产保护水印与版权)
- [AI 生成图像检测与检测器攻防](#ai-生成图像检测与检测器攻防)
- [音视频深度伪造检测](#音视频深度伪造检测)
- [图像篡改取证与内容定位](#图像篡改取证与内容定位)
- [隐写与隐蔽信道](#隐写与隐蔽信道)
- [多模态虚假信息与事实核查](#多模态虚假信息与事实核查)
- [具身智能与自动驾驶安全](#具身智能与自动驾驶安全)
- [安全评测与可靠性基准](#安全评测与可靠性基准)
- [核验记录](#核验记录)

## 会议信息

| 项目 | 信息 |
| --- | --- |
| 会议全称 | The 34th ACM International Conference on Multimedia (ACM MM 2026) |
| 举办时间与地点 | 2026-11-10 至 2026-11-14；Rio de Janeiro, Brazil |
| 官方网站 | [Official](https://2026.acmmm.org) |
| 官方录用列表 | 官网尚未发布 accepted papers 列表；本文件依据用户指定的第三方 Abstract Paper Portal（[ACMMM2026 Portal](https://hongsong-wang.github.io/ACMMM2026/)）整理，条目附 OpenReview 作者主页链接 |
| 正式论文集 | 尚未发布（ACM DL DOI 待回填） |
| 检查范围 | 上述 Portal 全部 1,776 条主会条目（162 Oral、1,614 Poster/Regular）；数据截至 2026-10-22 |

## 关键节点

投稿各节点均为当日 23:59 AoE；来源为官网 Important Dates 与 CFP Guidelines。

| 节点 | 日期 | 官方来源 |
| --- | --- | --- |
| Contribution Registration（摘要注册） | 2026-03-25 | [Important Dates](https://2026.acmmm.org/site/important-dates.html) |
| Contribution Submission（正文投稿） | 2026-04-01 | [Important Dates](https://2026.acmmm.org/site/important-dates.html) |
| Supplementary Submission | 2026-04-08 | [Important Dates](https://2026.acmmm.org/site/important-dates.html) |
| Rebuttal | 2026-06-04（Brave New Ideas 为 2026-05-28 至 2026-06-04） | [Important Dates](https://2026.acmmm.org/site/important-dates.html) |
| Author Notification | 2026-07-09（CFP 正文写作 2026-07-07） | [Important Dates](https://2026.acmmm.org/site/important-dates.html) · [CFP Guidelines](https://2026.acmmm.org/site/cfp-guidelines.html) |
| Camera-Ready | 2026-08-06 | [Important Dates](https://2026.acmmm.org/site/important-dates.html) |
| Author Registration | 2026-08-31 | [Important Dates](https://2026.acmmm.org/site/important-dates.html) |
| Conference | 2026-11-10 至 2026-11-14 | [Official](https://2026.acmmm.org) |

## 筛选说明

- 官方论文总数：1,776（Portal 主会条目；162 Oral + 1,614 普通）。
- 初筛候选：259。先以 safety、jailbreak、backdoor、poisoning、adversarial、watermark、deepfake、forgery、privacy、unlearning、membership inference、prompt injection、guardrail、misinformation、steganography、model extraction、copyright 等词组对标题+摘要宽筛得 939 篇，再以强安全信号词收敛出 235 篇，最后对标题含 attack/steal/leak/protect/safeguard 等词根及摘要含水印、隐私保护、AIGC 检测信号的条目补扫 24 篇。
- 最终收录：170（含 Oral 13 篇）。
- 收录口径：逐篇阅读摘要，只保留把 AI 模型或多模态系统的攻击与防御、越狱与有害内容、投毒后门、隐私泄漏与面部隐私保护、机器遗忘、水印与版权、深度伪造检测与取证、隐写、虚假信息治理、具身/自动驾驶安全或安全评测作为核心研究问题的论文；每篇只进入最匹配的一个分节。
- 边界案例：联邦学习与差分隐私（SFFedMC、AdvSE、TOFD、InstaFed、PrivFDM）、GNN 对抗净化（ProGAP）按既有硬排除不收录；通用幻觉缓解、医学幻觉基准（MGHalluDet）、常规 Re-ID 识别精度、非对抗自动驾驶能力（UnsDrive、CoT4AD、EA-Nav）、工业/路面异常检测、工作流治理系统（Kairos）、音频指纹检索（VLAFP）等无明确 AI 安全问题设定的论文不收录；SycoQA 因谄媚行为属欺骗性失效模式而保留；TeleRadShift 因提供医学 VLM 分诊的最差分组风险控制而保留于安全评测。
- 链接规则：arXiv 链接来自 Portal 登记并转换为 abs 页；GitHub 仅链接 Portal 标注的作者仓库；96 篇暂无 arXiv 链接的条目待作者放出后回填，Portal 本身不作为逐篇 Official 链接。
- 排序规则：全部分节内部按英文标题字母序排列；编号全文连续。

## 论文分类

### 多模态大模型越狱与有害内容攻防

### 1. Child-Oriented AIGC Video Risk Reviewing: A Benchmark and Knowledge-Supported Iterative Reasoning Framework

📄 [arXiv](https://arxiv.org/abs/2607.22715)　📅 2026　🏷 ACM MM 2026

**关键词**：`benchmark`、`AIGC video`、`child safety`、`risk taxonomy`、`multi-agent reviewing`

👤 **作者**：Yufan Zhang、Yuxin Shi

- 🎯 **研究动机**：AIGC 正在重塑视频生产与流通格局，其在视觉细节、叙事连贯性与内容表达上的不确定性显著高于传统视频，可能给儿童等对不当内容特别敏感的群体带来新风险。现有视频安全研究多以成人视角检测一般性违规，难以识别儿童观看 AIGC 视频时遇到的细粒度、隐式、上下文依赖风险。
- 🔬 **研究方法**：构建儿童导向 AIGC 视频审查基准 CAVSR，收录来自多个平台的 605 条真实视频，并建立含 6 个一级类别、26 个细粒度标签的层级风险分类体系以支撑系统评测；在此基础上提出知识与经验增强的审查框架 QVRS-E，以多智能体协作结合专家知识与经验知识，支持定向证据获取与基于事实的审查决策，并与视觉语言模型集成完成风险审查。
- 📌 **结论**：大量实验表明，QVRS-E 与视觉语言模型结合后显著提升儿童相关风险的审查效果，并产出更稳健的审查报告；CAVSR 以 605 条多平台视频和 6 类 26 标签体系为该方向提供了系统化评测基础。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid growth of Artificial Intelligence-generated content (AIGC) is reshaping the landscape of video production and circulation. Unlike traditionally produced videos, AIGC videos often exhibit greater uncertainty in visual details, narrative coherence, and content expression, which may introduce new risks for populations that are particularly sensitive to inappropriate or misleading content, such as children. While extensive research has investigated video safety and violation detection, most existing approaches focus on detecting general violations from an adult-oriented perspective, remaining insufficient for identifying the fine-grained, implicit, and context-dependent risks that children may encounter when viewing AIGC videos. This work focuses on child-oriented AIGC video reviewing. We first construct CAVSR, a benchmark of 605 real-world videos collected from multiple platforms, and develop a hierarchical risk taxonomy comprising 6 top-level categories and 26 fine-grained labels to support systematic evaluation of childrens viewing risks. Then, we propose QVRS-E, a knowledge- and experience-augmented video reviewing framework that combines multi-agent collaboration with expert and experiential knowledge to support targeted evidence acquisition and fact-grounded reviewing decisions. Extensive experiments demonstrate that our method significantly enhances the reviewing of child-related risks integrated with vision-language models, and yields more robust review reports.

</details>

### 2. CLARA: Clip-Level Multimodal Alignment with VLM-Derived Rationales for Hateful Video Detection

📄 [arXiv](https://arxiv.org/abs/2608.15905) · 🐙 [Code](https://github.com/yuchenzhang-1/CLARA)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`hateful video`、`clip-level alignment`、`mixture-of-experts`、`VLM rationale`

👤 **作者**：Yuchen Zhang、Shuang Dai、Zeyu Fu、Yunfei Long、Ravi Shekhar、Haralambos Mouratidis

- 🎯 **研究动机**：视频社交平台快速增长使仇恨视频对个人福祉与社会凝聚力的威胁凸显，但相比文本与静态多模态内容，仇恨视频检测仍严重欠缺探索：仇恨含义往往来自语音、音频与视觉内容的复杂交互，信号短暂、隐式且时序依赖，常规视频级表征难以捕捉。
- 🔬 **研究方法**：CLARA 将视频建模为细粒度片段（clip）序列而非单一实例，以精确捕捉时序局部化的仇恨信号；设计混合专家（MoE）clip 编码器实现自适应多模态对齐；引入局部-全局片段对比目标，联合建模短期线索与长程时序依赖；并将 VLM 生成的推理依据（rationale）经门控 Transformer 融合，提供高层语义引导。
- 📌 **结论**：在三个仇恨视频数据集上的大量实验表明 CLARA 全面超越现有 SOTA 方法；进一步的消融实验与参数分析验证了 MoE 对齐、对比目标与 rationale 融合各组件的有效性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Hateful video detection has become increasingly important with the rapid growth of video-centric social media platforms, given the serious risks that hate speech poses to both individual well-being and social cohesion. Compared with text or static multimodal content, hateful video detection remains underexplored and significantly more challenging, as hateful meaning often arises from complex interactions among multimodal cues, including speech, audio, and visual content. Moreover, such signals are often brief, implicit, and temporally dependent, making them difficult to capture using conventional video-level representations. In this work, we propose CLARA The code for CLARA is available at https://github.com/yuchenzhang-1/CLARA., a clip-level multimodal framework for hateful video detection. Instead of treating a video as a single instance, CLARA models it as a sequence of fine-grained clips, enabling more precise capture of temporally localized hateful signals. We introduce a Mixture-of-Experts clip encoder for adaptive multimodal alignment, a local-global segment contrastive objective to jointly model short-term cues and long-range temporal dependencies, and VLM-derived rationales integrated via a gated Transformer to provide high-level semantic guidance. Extensive experiments on three hateful video datasets demonstrate that CLARA consistently outperforms state-of-the-art methods. Further ablation studies and parameter analyses validate the effectiveness of each component.

</details>

### 3. DIRE: Dual-grained Internal Refusal Estimation for VLM Jailbreak Detection

🐙 [Code](https://github.com/xiyuzzz-njust/DIRE)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`VLM jailbreak`、`internal refusal signal`、`training-free`、`mechanistic interpretability`

👤 **作者**：Liming Lu、Xu Zheng、Jiawei Du、Bing Li、Shuchao Pang、Yazhou Yao

- 🎯 **研究动机**：视觉语言模型日益面临复杂的多模态越狱攻击；常规防御要么训练开销大、可能损害模型能力，要么依赖外部模块带来严重推理延迟；现有内部状态检测方法的特征分析粒度过粗，难以捕捉越狱攻击产生的微观冲突。
- 🔬 **研究方法**：通过机制可解释性分析发现：成功攻击通常并未根除模型内在安全知识，而是导致拒绝信号广泛衰减；即便全局安全对齐被绕过，仍有少量鲁棒的 Attention 与 FFN 组件持续对恶意查询表现出方向性抵抗。据此提出免训练检测框架 DIRE，不同于以往仅宏观或仅注意力的内部监测，在有效语义层联合探测鲁棒 Attention 路由与 FFN 语义记忆以识别多模态越狱。
- 📌 **结论**：在主流 VLM 与多样基准上的综合评测中，DIRE 取得平均 0.9800 的 AUROC，以免训练方式实现有竞争力的强检测性能。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While Vision-Language Models (VLMs) excel at multimodal tasks, they are increasingly vulnerable to sophisticated multimodal jailbreak attacks. Conventional defenses typically introduce significant training overhead, risk degrading model capabilities, or cause severe inference latency via external modules. Additionally, current internal state detection methods rely on coarse-grained feature analysis, often failing to capture the micro-level conflicts generated by jailbreak attacks. To overcome these challenges, we analyze multimodal jailbreaks through mechanistic interpretability. We demonstrate that successful attacks typically do not eradicate intrinsic safety knowledge but instead cause a widespread attenuation of refusal signals. Even when global safety alignment is bypassed, a small, robust subset of Attention and FFN components continues to exhibit directional resistance against malicious queries. Building upon this empirical finding, we introduce Dual-grained Internal Refusal Estimation (DIRE), a training-free detection framework. Unlike prior internal monitors that are either macro-only or attention-only, DIRE jointly probes resilient Attention routing and FFN semantic memory within effective semantic layers to detect multimodal jailbreaks in a training-free manner. Comprehensive evaluations on mainstream VLMs and diverse benchmarks demonstrate that DIRE achieves competitive and strong performance, with an average AUROC of 0.9800. For better reproducibility, the anonymized code is available at: https://github.com/xiyuzzz-njust/DIRE.

</details>

### 4. GRM: UtilityAware Jailbreak Attacks on Audio LLMs via GradientRatio Masking

📄 [arXiv](https://arxiv.org/abs/2604.09222) · 🐙 [Code](https://github.com/159753Fetter/GRM)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`audio LLM`、`jailbreak`、`frequency-selective perturbation`、`utility preservation`

👤 **作者**：Di Wu、Miao Hu

- 🎯 **研究动机**：音频大模型在支持语音交互的同时带来新的越狱漏洞。现有基于扰动的越狱不控制扰动承载的频段，通用扰动反复应用于多样输入会降低正常任务效用，留下显眼的行为痕迹，容易被用户或自动监测系统察觉，损害攻击隐蔽性。
- 🔬 **研究方法**：先做受控实验：将频段覆盖率从部分频带调至全频带，发现越狱成功率呈非单调变化，而效用退化随覆盖率单调增长，说明选择频段可实现更强攻击且更少效用损失。据此提出效用感知的频段选择性越狱框架 GRM：按越狱贡献与转写敏感性的比值对 Mel 频带排序，将通用扰动限制在选定频带，并正则化对请求语义的偏离；在四个音频大模型上实验。
- 📌 **结论**：GRM 实现平均 88.46% 的越狱成功率，同时在良性转写与响应任务上相对基线大幅减少效用退化，兼顾攻击强度、正常可用性与隐蔽性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Audio Large Language Models (ALLMs) enable spoken interaction but introduce new jailbreak vulnerabilities. Existing perturbation-based jailbreaks do not explicitly control which frequency bands carry the perturbation. Although such perturbations can elicit unsafe responses, repeatedly applying a universal perturbation across diverse inputs may also degrade utility on normal tasks, leaving a conspicuous behavioral footprint that may expose the attack to users or automated monitoring systems and thereby compromise its stealthiness. To determine whether full-band perturbation is necessary, we vary coverage from partial-band to full-band. Jailbreak Success Rate (JSR) varies non-monotonically, while utility degradation grows with coverage. This mismatch shows that selected bands can yield stronger attacks with less utility degradation than full-band perturbations. Based on this observation, we propose GRM, a utility-aware, frequency-selective jailbreak framework that ranks Mel bands by the ratio between jailbreak contribution and transcript sensitivity, confines a universal perturbation to selected bands, and regularizes deviations from the intended request semantics. Experiments on four ALLMs show that GRM achieves an average JSR of 88.46% while substantially reducing utility degradation across benign transcription and response tasks relative to baselines. Our code is available at https://github.com/159753Fetter/GRM this repository. Warning: This paper contains potentially sensitive content.

</details>

### 5. Learning Universal Semantic Simplex for Jailbreaking Large Vision-Language Models

📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`LVLM jailbreak`、`universal adversarial simplex`、`sharpness-aware optimization`、`benchmark`

👤 **作者**：Tao Huang、…、Liping Jing

- 🎯 **研究动机**：大型视觉语言模型仍易受越狱攻击，视觉模态的高维性进一步扩大攻击面；通用攻击更贴近真实场景，但其优化容易过拟合训练语料中的特定语义，跨多样指令的鲁棒泛化难以实现，因此需要更强的攻击来探测安全边界。
- 🔬 **研究方法**：提出 LUSS，将优化范式从逐点扰动转向连续对抗单纯形，引入锐度感知惩罚与基于单纯形的更新策略，在凸包内捕捉更广的对抗语义以缓解过拟合；同时构建 HarmInstBench——人工整理、带层级标注、覆盖多样恶意场景的评测基准；在 MiniGPT-4、LLaVA-v1.5、Qwen2.5-VL 三个模型上系统评估。
- 📌 **结论**：LUSS 显著超越 SOTA 基线：攻击成功率（ASR）相对提升最高 60.8%，毒性分数提升 31.8%，恶意意图满足率（MIFR）提升 44.7%。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite the remarkable capabilities of Large Vision-Language Models (LVLMs), they remain vulnerable to jailbreak attacks. The integration of visual modalities further expands the attack surface due to its high-dimensional nature. To ensure the secure development of LVLMs, it is essential to develop more potent jailbreak attacks to probe their safety boundaries. This work focuses on universal attacks as they better reflect real-world scenarios. However, achieving robust universality remains challenging due to the tendency to overfit specific semantics within the training corpus. To bridge this gap and enhance generalization across diverse instructions, we propose Learning Universal Semantic Simplex (LUSS), a novel jailbreak method that shifts the optimization paradigm from point-wise perturbations to continuous adversarial simplices. By incorporating a sharpness-aware penalty and a simplex-based update strategy, LUSS captures a broader range of adversarial semantics within a convex hull to mitigate overfitting. To facilitate more rigorous evaluation, we introduce HarmInstBench, a manually curated benchmark with hierarchical annotations for diverse malicious scenarios. Extensive experiments on multiple LVLMs, including MiniGPT-4, LLaVA-v1.5, and Qwen2.5-VL, demonstrate that LUSS significantly outperforms state-of-the-art baselines, achieving up to a 60.8% relative improvement in Attack Success Rate (ASR), 31.8% in toxicity score, and a 44.7% gain in Malicious Intent Fulfillment Rate (MIFR). Warning: this paper contains harmful text!

</details>

### 6. PEST: Parameter Efficient Steering of Blackbox VLMs via Agentic Few-shot Alignment for Hateful Meme Moderation

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`hateful meme`、`few-shot adaptation`、`blackbox VLM`、`meme moderation`

👤 **作者**：Naquee Rizwan、Subhankar Swain、Paramananda Bhaskar、Shehryaar Khan、Gagan Aryan、Animesh Mukherjee

- 🎯 **研究动机**：仇恨 meme 治理需要回答三个互补问题——如何检测、如何解释其内容、如何在发布前干预；现有工作通常把解释与干预同检测分开研究，不符合真实世界条件，而为 meme 治理标注大规模数据集的成本又极其高昂，难以支撑监督式方案。
- 🔬 **研究方法**：提出 PEST 框架，利用任务特定的生成式 VLM 与大型 VLM 的少样本适应能力，在有限数据条件下同时完成仇恨 meme 的检测、解释与发布前干预，并可适配不同类型的 meme，构成面向少样本条件的统一治理管线。
- 📌 **结论**：这是首个面向数据受限条件下可泛化仇恨 meme 治理的工作，将检测、解释与干预三个环节统一到少样本生成式管线中，可针对不同类型 meme 适配，具备真实生产场景的部署潜力。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In this work, we examine hateful memes from three complementary angles -- how to detect them, how to explain their content and how to intervene them before being posted -- by applying a range of strategies built on top of generative AI models. To the best of our knowledge, explanation and intervention have typically been studied separately from detection, which does not reflect real-world conditions. Further, since curating large annotated datasets for meme moderation is prohibitively expensive, we propose a novel framework -- PEST -- that leverages task-specific generative VLMs and the few-shot adaptability of large VLMs to cater to different types of memes. We believe this is the first work focused on generalizable hateful meme moderation under limited data conditions, and has strong potential for deployment in real-world production scenarios. Warning: Contains potentially toxic contents.

</details>

### 7. Prosody-driven Jailbreaks in Audio LLMs: A Controlled Study and Mechanistic Analysis

📄 [arXiv](https://arxiv.org/abs/2607.26541)　📅 2026　🏷 ACM MM 2026

**关键词**：`analysis`、`audio LLM`、`prosody jailbreak`、`speech delivery`、`controlled study`

👤 **作者**：Jiachen Qian

- 🎯 **研究动机**：音频基础模型支持端到端语音交互，其安全风险超出转写文本本身；在文本内容完全固定时，仅改变语音投递方式（韵律）能带来多大越狱能力——与词汇改写或整体风格迁移无关的成分——仍不清楚。
- 🔬 **研究方法**：固定转写内容，系统变化六种语音投递预设（针对唤醒度、权威感与语速等声学属性）；提出黑盒评测协议 PJ-Break 与 600 样本基准 AdvAudio-Prosody（声学属性经过验证），并与等预算的 StyleBreak 重实现及纯情绪文本条件对照。
- 📌 **结论**：在通过质检的 Qwen2-Audio 面板上，Panic（38/95）、Anger（35/95）、Fast（32/95）预设远超 Neutral（4/95）；固定六查询池覆盖 44/95 的 Qwen2-Audio 种子与 15/95 的 GPT-4o 种子，超过等预算 StyleBreak 重实现（27/95）；仅情绪音频（44/95）远比仅情绪文本（11/95）有效。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Audio-capable foundation models enable end-to-end spoken interaction, but they also introduce safety risks beyond transcript content. It remains unclear how much jailbreak capability can arise from matched-text variation in speech delivery rather than from lexical rewriting or broader style transfer. We study this question by holding transcript content fixed and varying six speech-delivery presets whose acoustic attributes may co-vary. We present PJ-Break, a black-box evaluation protocol with presets targeting arousal, authority, and speaking rate, together with AdvAudio-Prosody, a 600-sample benchmark with acoustically verified attributes. On the exact post-QC Qwen2-Audio panel, the Q =1 Panic (38/95), Anger (35/95), and Fast (32/95) presets are all well above Neutral (4/95). The fixed six-query pool covers 44/95 Qwen2-Audio seeds and 15/95 GPT-4o seeds and exceeds a matched-budget StyleBreak reimplementation (27/95) on Qwen2-Audio. A same-voice pool excluding the confounded Commanding condition still reaches 40/95, and a retained-panel ablation shows emotional-delivery audio alone (44/95) is far more effective than emotional text alone (11/95) . Exploratory surrogate diagnostics and pilot mitigation observations are secondary, non-core analyses. Overall, matched-text speech delivery should be treated as a first-class factor in Audio LLM safety evaluation.

</details>

### 8. RAFTNet: Rationale Adaptive Fusion Target-guided Agent Network for Harmful Meme Detection

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`harmful meme`、`target-oriented rationale`、`multi-agent collaboration`、`knowledge distillation`

👤 **作者**：Wei Xiang、Shenghao Liu、Xianjun Deng

- 🎯 **研究动机**：LLM 生成的自然语言推理依据能挖掘 meme 的隐含意义、辅助有害性判定，且有害 meme 具有特定目标范围（个体影响、群体身份、社会情境）；但现有方法生成的 rationale 不面向这些目标，且存在幻觉、歧义甚至错误，会误导有害 meme 检测。
- 🔬 **研究方法**：提出 RAFTNet：层级多智能体目标推理生成模块 HMA-TRG 先从 meme 获取视觉与文本线索，分别生成个体影响、群体身份、社会情境三类目标导向 rationale；自适应推理融合检测网络 ARF-DN 筛选可靠 rationale 并与多模态 meme 特征融合进行有害判定；进一步通过知识蒸馏得到轻量版 RAFTNet-D，提供即插即用的高效部署方案。
- 📌 **结论**：在四个公开基准上的大量实验显示 RAFTNet 显著超越 SOTA 算法；RAFTNet-D 在不引入大量参数与外部 LLM 知识的情况下保持有竞争力的性能。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Harmful meme detection aims to identify whether a meme carries harmful content by understanding and leveraging both its visual and textual modalities. The natural language rationales generated by Large Language Models (LLMs) delve into the implicit meaning of memes, which can facilitate the determination of whether the meme is harmful or harmless. The harmful memes often have a specific target scope, such as individual impact, group identity, or social context. Analyzing memes from the perspectives of potential targets can provide sound rationales for harmful content inference. However, rationales generated by existing methods are not oriented towards these specific targets. Besides, the LLM-generated rationales also suffer from the issues of hallucinations, ambiguities, and even errors, that will mislead the harmful meme detection. This paper proposes a Rationale Adaptive Fusion Target-guided Agent Network (RAFTNet) that first generates target scope oriented rationales, then screens and fuses reliable rationale information for harmful meme detection. In RAFTNet, we design a Hierarchical Multi-Agent Target Rationale Generation (HMA-TRG) module to acquire visual and textual cues from memes, which are next used to generate individual impact, group identity and social context rationales respectively. Then an Adaptive Rationale Fusion Detection Network (ARF-DN) is constructed to screen reliable rationales and fuse them with multimodal meme features for harmful detection. Further, we introduce a lightweight RAFTNet-D based on knowledge distillation, offering a plug-and-play solution enabling efficient deployment in practical scenarios. Extensive experiments on four public benchmarks show that our RAFTNet significantly outperforms the state-of-the-art algorithms, and RAFTNet-D maintains competitive performance without substantial parameters and external LLM knowledge.

</details>

### 9. Reading Between the Pixels: An Inscriptive Jailbreak Attack on Text-to-Image Models

📄 [arXiv](https://arxiv.org/abs/2604.05853)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`text-to-image`、`inscriptive jailbreak`、`typographic payload`、`zero-order optimization`

👤 **作者**：Zonghao Ying、…、Xianglong Liu

- 🎯 **研究动机**：现代文生图模型已能渲染清晰、段落长度的文本，催生一类全新滥用：inscriptive jailbreak——诱使 T2I 系统生成在视觉良性场景中嵌入有害文本载荷（如欺诈文档）的图像。现有越狱技术面向粗粒度视觉操纵，难以在绕过多级安全过滤器的同时保持字符级保真。
- 🔬 **研究方法**：提出黑盒攻击框架 Etch，将对抗提示分解为三个功能正交的层：语义伪装、视觉空间锚定与排版编码，把全提示空间的联合优化化为可解的子问题，经零阶循环迭代精炼；过程中由视觉语言模型批评每张生成图像、将失败定位到具体层并给出针对性修改。
- 📌 **结论**：在 2 个基准、7 个模型上，Etch 取得平均 65.57%（峰值 91.00%）的攻击成功率，显著超越现有基线，暴露了当前 T2I 安全对齐在排版类内容上的盲区。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern text-to-image (T2I) models can now render legible, paragraph-length text, enabling a fundamentally new class of misuse. We identify and formalize the inscriptive jailbreak, where an adversary coerces a T2I system into generating images containing harmful textual payloads (e.g., fraudulent documents) embedded within visually benign scenes. Unlike traditional depictive jailbreaks that elicit visually objectionable imagery, inscriptive attacks weaponize the text-rendering capability itself. Because existing jailbreak techniques are designed for coarse visual manipulation, they struggle to bypass multi-stage safety filters while maintaining character-level fidelity. To expose this vulnerability, we propose Etch, a black-box attack framework that decomposes the adversarial prompt into three functionally orthogonal layers: semantic camouflage, visual-spatial anchoring, and typographic encoding. This decomposition reduces joint optimization over the full prompt space to tractable sub-problems, which are iteratively refined through a zero-order loop. In this process, a vision-language model critiques each generated image, localizes failures to specific layers, and prescribes targeted revisions. Extensive evaluations across 7 models on the 2 benchmarks demonstrate that Etch achieves an average attack success rate of 65.57% (peaking at 91.00%), significantly outperforming existing baselines. Our results reveal a critical blind spot in current T2I safety alignments and underscore the urgent need for typography-aware defense multimodal mechanisms.

</details>

### 10. RedDiffuser: Auditing Multimodal Safety Failures in Vision-Language Models via Reinforced Diffusion

📄 [arXiv](https://arxiv.org/abs/2503.06223)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`VLM safety auditing`、`harmful contextual exposure`、`diffusion generation`、`reinforcement optimization`

👤 **作者**：Xingjun Ma

- 🎯 **研究动机**：视觉语言模型越来越多地部署于开放环境，但现有评测以指令为中心，聚焦显式恶意查询，忽视了更现实且欠探索的风险：部分毒性文本搭配视觉上下文时，安全对齐是否依然稳健；视觉输入可显著改变模型行为，使纯文本审计不足。
- 🔬 **研究方法**：提出 RedDiffuser（RedDiff），利用扩散模型为黑盒安全测试生成语义连贯的视觉输入，将贪婪提示搜索与强化优化相结合，系统挖掘暴露潜在安全失效的高风险多模态输入；在开源与商用 VLM 上开展有害上下文暴露下的安全审计。
- 📌 **结论**：此类上下文条件化失效广泛存在：在 LLaVA 上，不安全响应率在原始集上最高提升 10.69%、在保留集上提升 8.91%，且可强力迁移至 Gemini 与 LLaMA-Vision；即使接入外部安全护栏，漏洞依然存在，表明系统级安全机制尚不足以应对真实多模态风险。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Vision-Language Models (VLMs) are increasingly deployed in open-ended environments, where ensuring reliable safety under multimodal inputs is critical. However, existing evaluations remain largely instruction-centric, focusing on explicit malicious queries while overlooking a more realistic and underexplored risk: whether safety alignment remains robust under harmful contextual exposure. This limitation is particularly important for multimodal systems, where visual inputs can substantially steer model behavior and render text-only auditing insufficient. In this work, we study multimodal safety auditing under harmful contextual exposure, asking whether VLMs can maintain safe behavior when partial toxic text is paired with visual context. To enable systematic auditing, we propose RedDiffuser (RedDiff), a reinforcement-based framework that leverages diffusion models to generate semantically coherent visual inputs for black-box safety testing. By combining greedy prompt search with reinforcement optimization, RedDiffuser uncovers high-risk multimodal inputs that expose latent safety failures. Extensive experiments on both open-source and commercial VLMs show that such context-conditioned failures are widespread. On LLaVA, RedDiffuser increases unsafe response rates by up to 10.69% on the original set and 8.91% on a hold-out set, with strong transferability to Gemini and LLaMA-Vision. These vulnerabilities persist even under external safety guardrails, suggesting that current system-level safety mechanisms remain insufficient for realistic multimodal risks. Our findings reveal a critical blind spot in existing safety evaluations and establish context-aware multimodal auditing as an essential paradigm for diagnosing hidden vulnerabilities in modern VLM systems.

</details>

### 11. Safeguarding Text-to-Image Generation via Inference-Time Prompt-Noise Optimization

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`text-to-image`、`unsafe generation`、`inference-time optimization`、`prompt-noise tradeoff`

👤 **作者**：Jiangweizhi Peng、Zhiwei Tang、Gaowen Liu、Charles Fleming、Mingyi Hong

- 🎯 **研究动机**：文生图扩散模型虽以高质量、多样化的生成能力著称，但仍会生成含敏感或不当内容的不安全图像，可能危害用户；现有防不当图像生成的方法容易被绕过，且在对抗攻击面前脆弱，如何使 T2I 模型对齐特定安全目标仍是重要挑战。
- 🔬 **研究方法**：提出免训练的提示-噪声优化方法 PNO：构建新的优化框架，在扩散采样过程中同时利用连续提示嵌入与注入的噪声轨迹两类可调变量进行联合优化，将生成过程引导向安全图像，全程无需调整模型参数或重训模型。
- 📌 **结论**：大量数值实验表明 PNO 在抑制毒性图像生成上达到 SOTA 性能，并对对抗攻击表现出鲁棒性；与现有方法相比生成时间相当，并在安全生成与提示对齐这对冲突目标之间取得最佳权衡。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-Image (T2I) diffusion models are widely recognized for their ability to generate high-quality and diverse images based on text prompts. Despite recent advances, these models are still prone to generating unsafe images containing sensitive or inappropriate content, which can be harmful to users. Current efforts to prevent inappropriate image generation for diffusion models are easy to bypass and vulnerable to adversarial attacks. How to ensure that T2I models align with specific safety goals remains a significant challenge. In this work, we propose a novel, training-free approach, called Prompt-Noise Optimization (PNO), to mitigate unsafe image generation. Our method introduces a novel optimization framework that leverages both the continuous prompt embedding and the injected noise trajectory in the sampling process to generate safe images. Extensive numerical results demonstrate that our framework achieves state-of-the-art performance in suppressing toxic image generations and demonstrates robustness to adversarial attacks, without needing to tune the model parameters. Furthermore, compared with existing methods, PNO uses comparable generation time while offering the best tradeoff between the conflicting goals of safe generation and prompt alignment.

</details>

### 12. TempJail: Temporal Jailbreak Attacks against Image-to-Video Generation Models

📄 [arXiv](https://arxiv.org/abs/2608.26971) · 🐙 [Code](https://github.com/luqi-glory/TempJail)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`image-to-video`、`temporal jailbreak`、`semantic camouflage`、`temporal composition`

👤 **作者**：Zijing Li、Qiankun Zhang

- 🎯 **研究动机**：图生视频模型在主体一致性与时序连贯上快速进步，也带来新安全风险；现有越狱研究聚焦单帧违规，忽视了视频生成特有的时间维度：不安全语义可能并非来自某一帧，而是随时间组合涌现。此类攻击还面临时间抽象与语义伪装两大挑战。
- 🔬 **研究方法**：提出面向 I2V 系统的时序越狱框架 TempJail：针对时间抽象，将目标恶意描述分解为首帧视觉条件与时序文本指令；针对语义伪装，图像侧把语义注入建模为扩散采样中的受控潜在扰动并引入预训练编码器的梯度引导，文本侧将描述改写为无害的『主体-动作-场景』模板以绕过安全过滤器；黑盒推理阶段两种模态共同使恶意语义随时间逐渐触发。在 Kling、Seedance、Veo、PixVerse 四个闭源商用模型上实验。
- 📌 **结论**：GPT-5.2 评测下，TempJail 的攻击成功率较先前 SOTA 方法提升 23.3%；人工评测下提升 22.0%。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In recent years, image-to-video (I2V) generation models have made remarkable progress in subject consistency and temporal coherence, enabling high quality video synthesis. However, these advances also introduce new safety risks. Existing studies mainly focus on jailbreak attacks involving single frame violations, while largely overlooking the temporal dimension unique to video generation models. In this paper, we investigate three attack scenarios and uncover a temporal vulnerability in I2V systems: unsafe semantics may emerge not from a single frame, but from semantic composition over time. We further identify two key challenges in such attacks: temporal abstraction and semantic camouflage. To address these issues, we propose TempJail, a novel temporal jailbreak framework for I2V systems. For temporal abstraction, we decompose a target malicious caption into an initial frame visual condition and a temporal text instruction. For semantic camouflage, on the image side we model semantic injection as controlled latent perturbation in diffusion sampling and introduce gradient guidance from pretrained encoders. On the text side, we rewrite the caption into an innocuous ``subject-action-scene'' template that bypasses safety filters while preserving temporal guidance. In the black-box inference phase, these two modalities jointly enable malicious semantics to be gradually triggered over time. Experiments on closed-source commercial models, including Kling, Seedance, Veo and PixVerse, show that TempJail improves attack success rate over prior state-of-the-art methods by 23.3% under GPT-5.2 evaluation and 22.0% under human evaluation. Our codes are available at https://github.com/luqi-glory/TempJail GitHub.

</details>

### 13. The Price of Consistency: Exploiting Visual Anchors for Multimodal Jailbreaking in Video Generation

📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`video generation`、`reference image anchor`、`intent decoupling`、`safety benchmark`

👤 **作者**：Qianqian Xu、Yangbangyan Jiang、Zhipeng Yu、Qingming Huang

- 🎯 **研究动机**：视频生成正从纯文本驱动转向多条件可控生成，参考图像被广泛用作条件输入以获得更强的时空一致性；但这些视觉锚点对安全的影响几乎未被探索——一致性机制会阻止生成内容偏离原始有害意图，消除模型从有害漂移到良性内容的『天然安全逃生通道』，即一致性的代价。
- 🔬 **研究方法**：揭示并利用这一视觉锚定效应：提出免训练多模态越狱框架 DIVA，将有害意图解耦为静态视觉锚点图像与动态运动文本提示，并采用双准则选择在攻击隐蔽性与语义保留之间取得平衡；在多个领先商用平台与主流开源视频生成模型上验证，并贡献首个多条件视频生成安全基准 TI2VSafetyBench。
- 📌 **结论**：跨多个商用平台与开源模型的实验显示，DIVA 的攻击成功率显著高于现有纯文本方法；TI2VSafetyBench 为多条件视频生成安全提供了首个系统评测基准。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid evolution of video generation has shifted the paradigm from pure text-driven to multi-conditional controllable generation, with reference images now widely adopted as conditional inputs to achieve superior spatiotemporal consistency. While these reference images serve as powerful visual anchors that significantly enhance controllability, their impact on safety remains largely unexplored. In this work, we reveal the visual anchoring effect: by enforcing consistency, the mechanism prevents the generated content from drifting away from the original harmful intent, thereby eliminating the model's natural safety escape route from harmful to benign content. Consequently, visual anchors inherently increase the safety risk---this is the price of consistency. Building on this insight, we propose Decoupling Intent via Visual Anchors (DIVA), a training-free multimodal jailbreak framework for video generation that exploits this vulnerability. DIVA decouples harmful intent into a static visual anchor image and a dynamic motion text prompt, and employs dual-criteria selection to balance attack stealthiness with semantic preservation. Extensive experiments across various leading commercial platforms and mainstream open-source video generation models demonstrate that DIVA achieves a substantially higher Attack Success Rate than existing text-only methods. To facilitate future research, we additionally contribute TI2VSafetyBench, the first safety benchmark for multi-conditional video generation.

</details>

### 14. ThinkingGuard: Decoding Implicit Hazards via Step-by-Step Risk Attribution in Multimodal Large Language Models

🐙 [Code](https://github.com/FroggyChen/ThinkingGuard)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`implicit risk`、`risk compositionality`、`step-supervised reasoning`、`guard model`

👤 **作者**：Ruochen Zhang、Yao Huang、Yitong Sun、Yuanfang Guo、Xingxing Wei

- 🎯 **研究动机**：多模态大模型日益部署于安全关键领域，其可靠性受到多模态隐式风险的威胁：各自无害的文本与中性视觉实体经逻辑汇聚即可诱发不安全输出；现有检测方法忽视跨模态的风险激活机制，导致单模态捷径学习与幻觉化合理化，难以识别此类风险。
- 🔬 **研究方法**：先构建 TriggerBench——首个显式建模风险组合性的数据集，共 5600 个实例，通过隔离关键元素与触发元素构建反事实对比对，消除风险残留、迫使模型进行真实逻辑推理；再提出步骤监督结构化推理训练框架训练专用守卫模型 ThinkingGuard：借鉴情境觉察理论将隐式风险识别解耦为渐进认知阶段，用步奖励蒙特卡洛树搜索探索最优推理轨迹，并经双约束偏好对齐蒸馏入模型。
- 📌 **结论**：在标准与隐式安全两类基准上的大量实验表明，ThinkingGuard 均取得强劲表现，为组合性隐式风险的检测提供了数据与模型双重基础。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While Multimodal Large Language Models (MLLMs) are increasingly deployed in safety-critical domains, their reliability is threatened by multimodal implicit risks. Unlike explicit threats, these hazards emerge when individually benign text and neutral visual entities logically converge to induce unsafe outputs. Current detection methods fail to address this because they overlook the underlying risk activation mechanisms that govern cross-modal risk activation, leading to single-modality shortcut learning and hallucinated rationalizations. To bridge this gap, we first construct TriggerBench, the first dataset explicitly modeling risk compositionality (5,600 instances). By formally isolating Key Elements and Trigger Elements to build counterfactual contrastive pairs, TriggerBench eliminates risk residues and forces models to perform genuine logical deduction rather than superficial pattern matching, which provides a rigorous foundation for both large-scale training and fine-grained evaluation. Building on this, we propose a Step-Supervised Structured Reasoning training framework and employ it to train ThinkingGuard, a specialized guard model. Inspired by Situation Awareness theory, we decouple implicit risk identification into progressive cognitive stages, and utilize a step-reward Monte Carlo Tree Search algorithm to explore optimal reasoning trajectories, which are then distilled into the model through Dual-Constraint Preference Alignment. Extensive experiments across both standard and implicit safety benchmarks demonstrate that ThinkingGuard achieves strong performance. Project resources are available at https://github.com/FroggyChen/ThinkingGuard.

</details>

### 15. Visual Token Compression Enhances Robustness of MLLMs

📄 [arXiv](https://arxiv.org/abs/2607.22716) · 🐙 [Code](https://github.com/Eurek001/OOD-VTP)　📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`visual token pruning`、`jailbreak robustness`、`hallucination mitigation`、`OOD visual tokens`

👤 **作者**：Jiequan Cui、Wenbo Hu、Zenglin Shi、Zhenzhen Hu、Richang Hong

- 🎯 **研究动机**：视觉与语言模态无法完美对齐，失配的视觉 token 可能构成分布外（OOD）输入，导致不可预测输出并引入越狱攻击与幻觉等脆弱性；该工作首次指出视觉 token 剪枝可以增强多模态大模型的鲁棒性。
- 🔬 **研究方法**：度量每个视觉 token 与语言特征空间的距离，将距离大的 token 识别为 OOD token，并在鲁棒剪枝层对其进行迭代剪枝，在增强对越狱与幻觉鲁棒性的同时顺带降低推理成本；在七个多样的流行基准上评测。
- 📌 **结论**：该方法在防御越狱攻击上取得平均 13.29% 的提升，在缓解幻觉上持续取得有竞争力的表现，并在 MME 等通用数据集上保持强结果。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In this paper, we show for the first time that visual token pruning enhances the robustness of Multimodal Large Language Models (MLLMs), mitigating vulnerabilities such as jailbreak attacks and hallucinations. Given that vision and language modalities cannot be perfectly aligned, the misaligned visual tokens might act as out-of-distribution (OOD) inputs, leading to unpredictable outputs and introducing potential vulnerabilities. Building on this insight, we aim to enhance model robustness against jailbreaks and hallucinations by reducing OOD visual tokens at robust-pruning layers, while also reducing inference cost as a side benefit. Specifically, we measure the distance between each visual token and the language feature space. Then, visual tokens with large distances are identified as OOD tokens, which can be iteratively pruned. To demonstrate the effectiveness of our method, we evaluate it on seven diverse popular benchmarks. Notably, our method yields an average improvement of 13.29% in defending jailbreak attacks, consistently achieves competitive performance in mitigating hallucinations, and maintains strong results on general datasets like MME. Code is available at https://github.com/Eurek001/OOD-VTP.

</details>

### 16. When Helpful Text Hurts: Option-Redirecting Bias in VisionLanguage Models

📅 2026　🏷 ACM MM 2026

**关键词**：`analysis`、`tri-modal VQA`、`auxiliary text bias`、`option redirection`、`inference-time intervention`

👤 **作者**：Hong-Hanh Nguyen-Le、Thanh Duc Ngo

- 🎯 **研究动机**：三模态视觉问答中，辅助文本常被用来补充视觉与文本输入，但其可靠性往往不受控；在图像-问题-选项固定的条件下，不同类型的不可靠辅助文本如何影响答案选择仍不清楚，而恰恰是这类看似『有帮助』的文本可能系统性重定向模型预测。
- 🔬 **研究方法**：发现最有害的辅助文本不一定是事实最错误的，而是与问题对齐、与图像矛盾且偏向特定干扰项的文本；提出受控诊断协议 Textual Reliability Ladder，沿图像一致性、问题相关性、选项支持三轴分解辅助文本；在 ScienceQA、VCR、A-OKVQA、Causal-VidQA 四个数据集与多个近期 VLM 上实验；并提出免训练的推理时干预——噪声稳定性转向与动态接地——抵消重定向效应。
- 📌 **结论**：支持干扰项的文本造成最大的准确率下降（最高 53.1%）并将错误集中于特定错误选项；所提干预能减少重定向错误，同时在忠实文本条件下基本保持性能。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In tri-modal visual question answering (VQA), auxiliary text is commonly used to complement visual and textual inputs, yet its reliability is often uncontrolled. While prior work studies modality conflicts in general, it remains unclear how different types of unreliable auxiliary text affect answer selection under fixed imagequestionoption contexts. In this work, we show that the most harmful auxiliary text is not necessarily the most factually incorrect, but the one that aligns with the question while contradicting the image and favoring a specific distractor, leading to systematic redirection of model predictions. To isolate this effect, we introduce the Textual Reliability Ladder, a controlled diagnostic protocol that decomposes auxiliary text along three axes: image consistency, question relevance, and option support. Across multiple datasets (ScienceQA, VCR, A-OKVQA, Causal-VidQA) and recent VLMs, we find that such distractor-supporting text induces the largest accuracy drops (up to 53.1%) and concentrates errors on specific incorrect options. To mitigate this failure mode, we propose a training-free inference-time intervention that explicitly counteracts this redirection effect via noise-stability steering and dynamic grounding, reducing redirected errors while largely preserving performance under faithful text. Our results highlight that auxiliary-text reliability must be understood at the decision level, rather than solely through factual correctness, and provide a practical pathway toward more robust tri-modal reasoning.

</details>


### 智能体与 GUI Agent 安全

### 17. AgentHazard: A Benchmark for Evaluating Harmful Behavior in Computer-Use Agents

📄 [arXiv](https://arxiv.org/abs/2604.02947)　📅 2026　🏷 ACM MM 2026

**关键词**：`benchmark`、`computer-use agent`、`harmful behavior`、`multi-step trajectory`、`agent safety evaluation`

👤 **作者**：Yunhao Feng、…、Xingjun Ma

- 🎯 **研究动机**：计算机使用智能体将语言模型从文本生成扩展为对工具、文件与执行环境的持续动作：它们跨交互维护状态并把中间输出转为具体动作，因此有害行为可能经由一系列各自合理的步骤累积涌现，导致未授权操作、敏感数据访问或破坏性执行，构成与聊天系统截然不同的安全挑战。
- 🔬 **研究方法**：提出基准 AgentHazard，含 2653 个实例，覆盖 10 个风险类别与 10 种攻击策略；每个实例将有目的的恶意目标与看似局部合法、但共同诱发不安全行为的操作步骤序列配对，考察智能体能否在多步轨迹中识别并中断由累积上下文与重复工具使用引发的危害；在 Claude Code、OpenClaw、IFlow 三个框架上用 Qwen、Kimi、GLM 系列开源可部署模型评测。
- 📌 **结论**：实验表明当前系统仍高度脆弱：由 Qwen3-Coder 驱动的 Claude Code 攻击成功率达 73.63%，说明模型级对齐并不能可靠保证智能体级安全。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Computer-use agents extend language models from text generation to persistent action over tools, files, and execution environments. Unlike chat systems, they maintain state across interactions and translate intermediate outputs into concrete actions. This creates a distinct safety challenge: harmful behavior may emerge through sequences of individually plausible steps that collectively lead to unauthorized operations, sensitive data access, or destructive execution. We present AgentHazard, a benchmark for evaluating harmful behavior in computer-use agents. AgentHazard contains 2,653 instances spanning 10 risk categories and 10 attack strategies. Each instance pairs a harmful objective with a sequence of operational steps that appear locally legitimate but jointly induce unsafe behavior. The benchmark evaluates whether agents can recognize and interrupt harm arising from accumulated context and repeated tool use across multi-step trajectories. We evaluate AgentHazard on Claude Code, OpenClaw, and IFlow using diverse open and openly deployable models from the Qwen, Kimi, and GLM families. Our experimental results indicate that current systems remain highly vulnerable: when powered by Qwen3-Coder, Claude Code exhibits an attack success rate of 73.63%, suggesting that model-level alignment does not reliably guarantee agent-level safety. To facilitate future research, we open-source the dataset, supplementary materials, and benchmark construction pipeline at https://yunhao-feng.github.io/AgentHazard/.

</details>

### 18. GrayUI: A Visual Context Attack Framework Against VLM-Based Mobile Agents

📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`mobile GUI agent`、`visual context deception`、`overlay manipulation`、`trajectory integrity`

👤 **作者**：Yawen Zeng

- 🎯 **研究动机**：基于 VLM 的 GUI 智能体在加速移动端自动化的同时带来安全风险：它们依赖宽泛的系统权限与长程上下文连续性；现有攻击（如覆盖操纵、推理间隙利用）只针对单步，忽视了更根本的脆弱性——扩展交互轨迹上上下文观察的完整性。
- 🔬 **研究方法**：提出系统化视觉上下文攻击框架 GrayUI，从三个维度利用上下文依赖：空间上下文——将对抗提示嵌入壁纸并持续占据覆盖窗口以污染视野；时间上下文——通过开屏广告中断任务轨迹；功能上下文——混淆按钮语义并引入应用内弹窗扭曲意图到动作的映射；借助系统级（壁纸）与应用级（广告）视觉通道，实现从 OS 背景层到应用交互层的全面上下文欺骗；在两个公开基准上评测。
- 📌 **结论**：组合全部策略的联合攻击在两个公开基准上取得平均 86% 的攻击成功率，验证了破坏上下文连贯性这一攻击路线的高效性与可扩展性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in VLM-based GUI agents accelerate mobile automation but also introduce security risks, as agents rely on broad system privileges and long-horizon contextual continuity. Existing attacks, such as overlay manipulation and inference-gap exploitation, target individual steps but overlook a more fundamental vulnerability: the integrity of contextual observations across extended interaction trajectories. In this work, we argue that disrupting contextual coherence is a highly effective and scalable strategy for compromising mobile agents. The key challenge is crafting plausible perturbations that continuously mislead the agent without breaking visual realism. To this end, we propose GrayUI, a systematic visual context attack framework that exploits three dimensions of contextual dependency: 1) spatial context, by embedding adversarial prompts into wallpapers and persistently occupying overlay windows to pollute the visual field; 2) temporal context, by interrupting task trajectories through splash-screen advertisements; and 3) functional context, by confusing button semantics and introducing in-app pop-ups that distort intent-to-action mapping. In this way, by exploiting system-level (e.g., wallpapers) and application-level (e.g., advertisements) visual channels, GrayUI enables comprehensive context deception from the OS background layer to the app interaction layer. Finally, we evaluate GrayUI on two public benchmarks, showing that a joint attack combining all strategies achieves an average attack success rate of 86%.

</details>

### 19. Hidden Dangers in Plain Sight: Unveiling Unintended Behavioral Safety Risks of Situated Agents in Functional Environments

📅 2026　🏷 ACM MM 2026

**关键词**：`benchmark`、`situated agent`、`behavioral safety`、`functional environment`、`LLM-as-a-judge`

👤 **作者**：Xuetao Wei

- 🎯 **研究动机**：大型多模态模型使智能体能够执行复杂数字与物理任务，但将其部署为自主决策者会引入大量非故意的行为安全风险；现有行为安全评测在领域与环境类型上碎片化，缺乏一致的跨域分析基础。
- 🔬 **研究方法**：提出 BeSafe-Bench（BSB），在功能性环境中评测情境化智能体的行为安全风险，覆盖 Web、Mobile、具身 VLM、具身 VLA 四个代表性领域；通过对任务附加九类安全关键风险构建多样指令空间，并采用规则检查与 LLM-as-a-judge 推理相结合的混合评测框架评估真实环境影响；对 13 个流行智能体进行评测。
- 📌 **结论**：结果揭示令人担忧的趋势：即使表现最好的智能体，在完全遵守安全约束的前提下完成任务也不足 40%，且强任务表现常与严重安全违规并存，说明在真实场景部署智能体系统前亟需更好的安全对齐。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid evolution of Large Multimodal Models (LMMs) has enabled agents to perform complex digital and physical tasks, yet their deployment as autonomous decision-makers introduces substantial unintentional behavioral safety risks. Existing behavioral-safety evaluations remain fragmented across domains and environment types. To support consistent cross-domain analysis, we present BeSafe-Bench (BSB), a benchmark for exposing behavioral safety risks of situated agents in functional environments, covering four representative domains: Web, Mobile, Embodied VLM, and Embodied VLA. Using functional environments, we construct a diverse instruction space by augmenting tasks with nine categories of safety-critical risks, and adopt a hybrid evaluation framework that combines rule-based checks with LLM-as-a-judge reasoning to assess real environmental impacts. Evaluating 13 popular agents reveals a concerning trend: even the best-performing agent completes fewer than 40% of tasks while fully adhering to safety constraints, and strong task performance frequently coincides with severe safety violations. These findings underscore the urgent need for improved safety alignment before deploying agentic systems in real-world settings.

</details>

### 20. INSURE: Inference-Time Defense Framework for Securing Agents against Hijacking

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`agent hijacking`、`indirect prompt injection`、`latent probing`、`attention steering`

👤 **作者**：Fuyao Zhang、…、Wei Yang Bryan Lim

- 🎯 **研究动机**：智能体日益容易遭受劫持攻击——跨模态输入（如对抗图像或检索到的网页内容）中嵌入的恶意指令会欺骗其执行；现有防御依赖严格过滤或拒绝机制，存在过度拒绝的关键缺陷，会过早终止本来有效的智能体工作流。
- 🔬 **研究方法**：提出『探测-缓解』框架 INSURE，核心洞察是多模态间接提示注入（IPI）攻击会在视觉-语言潜在空间留下独特的过度聚焦签名；先由 Latent Space Trace Prober 基于高强度激活分数检测跨模态攻击，再由 Mitigating Rectifier 执行精准注意力转向：选择性操纵对抗视觉-文本依赖并放大任务相关元素，恢复大模型的功能轨迹，从而在保持任务连续性的同时中和攻击；在多个多模态骨干上评测。
- 📌 **结论**：INSURE 实现平均 0.3% 的 ASR，比肩商用级检测器，同时带来超过 50% 的任务效用提升；在分布外（OOD）设定下泛化稳健，可无缝保护多样多模态交互。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agents are increasingly susceptible to hijack attacks, where malicious instructions embedded in cross-modal inputs (e.g., adversarial images or retrieved web content) are used to deceive the agent's execution. Existing defenses typically rely on strict filtering or refusal mechanisms, which suffer from a critical limitation: over-refusal, prematurely terminating valid agentic workflows. We propose INSURE, a probing-to-mitigation framework that neutralizes cross-modal attacks while preserving task continuity. Our key insight is that multimodal IPI attacks leave distinct over-focusing signatures in the vision-language latent space. We introduce a Latent Space Trace Prober to detect inter-modal attacks based on high-intensity activation scores. Subsequently, a Mitigating Rectifier performs surgical attention steering that selectively manipulates adversarial visual-textual dependencies while amplifying task-relevant elements to restore the large model's functional trajectory. Extensive evaluations on multiple multimodal backbones show that our method achieves a competitive 0.3% ASR (average), matching commercial-grade detectors, while yielding over 50% task utility gain. Furthermore, INSURE demonstrates robust Out-of-Distribution (OOD) generalization and seamlessly secures diverse multimodal interactions, establishing a superior balance between security and efficiency.

</details>

### 21. PVDetector: Detecting Prompt Injection Attacks on Purpose-Specific LLM Agents through Policy-Violation Concept Analysis

📄 [arXiv](https://arxiv.org/abs/2607.12624) · 🐙 [Code](https://github.com/Claresigle/PVDetector)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`prompt injection`、`purpose-specific agent`、`policy-violation concept`、`hidden activation`

👤 **作者**：Hangtao Zhang、Zhirun Zheng、Li Zeng

- 🎯 **研究动机**：LLM 越来越多地作为目的特定智能体部署（如客服、代码生成），除通用安全护栏外还须遵守角色专属限制，这进一步扩大了提示注入（PI）攻击面；现有检测方法主要依赖输入-输出模式分析，效果有限。
- 🔬 **研究方法**：转向隐藏激活空间分析，发现 LLM 在收到超出其指定目的的请求时会固有保留潜在的『策略违反（PV）』概念——它刻画用户查询与预定义限制之间的冲突语义，隐式反映模型对违规的内在感知；据此提出免训练框架 PVDetector，用离线构建的策略违规与合规提示对比对导出 PV 概念，推理时通过测量隐藏状态与 PV 概念的对齐程度来检测 PI 攻击。
- 📌 **结论**：跨多个 LLM 与数据集的实验中，PVDetector 实现低于 1% 的漏报率且辅助开销极小，一致优于 SOTA 检测方法。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed as purpose-specific agents to handle domain-specific tasks such as customer service and code generation. These agents are expected to comply with not only generic safety guardrails but also purpose-specific restrictions tailored to their designated roles. Such additional restrictions enlarge the attack surface, particularly to prompt injection (PI) attacks. To defend against such attacks, existing detection methods primarily rely on analyzing input-output patterns, yet yield limited effectiveness. To address this limitation, we turn to analyzing the hidden activation space and discover that LLMs inherently retain latent policy-violation (PV) concepts when prompted with requests beyond their designated purpose. Particularly, PV concepts capture the semantics of conflicts between user queries and predefined restrictions, implicitly reflecting LLMs' intrinsic awareness of recognizing policy violations. Building on this insight, we propose PVDetector, a training-free framework that detects PI attacks during LLM inference by measuring hidden-state alignment with PV concepts, which are derived offline from the contrastive pairs of policy-violating and policy-compliant prompts. Experiments across multiple LLMs and datasets show that PVDetector achieves <1% false negative rate with minimal auxiliary overhead, consistently outperforming state-of-the-art methods. Our code is available at https://github.com/Claresigle/PVDetector.

</details>

### 22. See No Evil: Aligning Vision-Language Agents with Multimodal Contextual Integrity via Adversarial Reinforcement Learning

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`GUI agent privacy`、`contextual integrity`、`constrained reinforcement learning`、`adversarial self-play`

👤 **作者**：Runshan Hu

- 🎯 **研究动机**：操作图形界面的视觉-语言智能体面临独特的隐私对齐难题：敏感信息嵌入屏幕区域与交互目标中，文本披露与落地动作均可造成泄露；现有以文本为中心的护栏把隐私当作实体类型的固定属性，而非随上下文变化的信息流约束，与该场景错配。
- 🔬 **研究方法**：将问题形式化为多模态上下文完整性（M-CI）——合法性取决于主体、属性与传播原则间的当前上下文关系；提出 Visual-Agent Guardian（VAG），用上下文元组与 GUI 元素区域级授权图表示交互状态，组合上下文条件逆渲染管线（反事实监督）、M-CI-CoT 推理模块与对文本及空间动作打分的视觉-语义奖励模型 V-SRM；在隐私预算下用无 critic 的约束强化学习 C-GRPO（PID-拉格朗日更新）训练，并以对抗自博弈增强鲁棒性。
- 📌 **结论**：VAG 显著推进隐私-效用 Pareto 前沿：三个基准上视觉隐私泄露均降至 5% 以下，平均任务成功率超 80%，多模态社会工程攻击平均成功率降至 4% 以下。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Agents (VLAs) that operate graphical user interfaces (GUIs) face a distinctive privacy-alignment problem: sensitive information is embedded in screen regions and interaction targets, so failures can arise through both textual disclosure and grounded actions. Existing text-centric safety guardrails are poorly matched to this setting because they treat privacy as a fixed property of an entity type, rather than as a context-dependent information-flow constraint. We formulate this problem as Multimodal Contextual Integrity (M-CI), where legality depends on the current contextual relation among actors, attributes, and transmission principles. To operationalize M-CI, we propose the Visual-Agent Guardian (VAG), which represents each interaction state using a contextual tuple together with a region-level authorization map over GUI elements. VAG combines a context-conditioned inverse rendering pipeline for counterfactual supervision, an M-CI-CoT module for contextual tuple and authorization inference, and a Visual-Semantic Reward Model (V-SRM) that scores both textual and spatial actions against the inferred CI state. We train the agent under a privacy budget using Constrained Group Relative Policy Optimization (C-GRPO), a critic-free constrained reinforcement learning method with PID-Lagrangian updates, and further improve robustness through automated adversarial self-play. Experiments on privacy-critical benchmarks demonstrate that VAG fundamentally shifts the privacy--utility Pareto frontier: it reduces visual privacy leakage to under 5% across all three benchmarks while averaging over 80% task success, and reduces the average multimodal social-engineering attack success rate to below 4%.

</details>

### 23. SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction

📄 [arXiv](https://arxiv.org/abs/2607.15550)　📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`mobile GUI agent`、`world model`、`action risk assessment`、`pre-execution screening`

👤 **作者**：Bo Yuan、Junlan Feng

- 🎯 **研究动机**：移动 GUI 智能体能够自动执行复杂任务，但单个错误动作就可能导致不可逆后果，安全风险突出；现有安全机制以反应式为主，缺乏在动作执行前评估风险的能力。
- 🔬 **研究方法**：提出后果感知安全框架 SeerGuard，包含执行前的指令级筛查与动作级风险评估：动作级评估在当前 GUI 状态下分析智能体提议的动作、预判其可能结果，从而在执行前识别风险；为此通过多任务学习构建统一的安全增强世界模型 SAWM，将语义下一状态预测与安全风险评估整合在一起。
- 📌 **结论**：SeerGuard 对多种移动 GUI 智能体有效泛化：在 Qwen3-VL-8B-Instruct 上，ω=0.8 时安全-效用分数从 0.191 升至 0.596，α=0.8 时风险代价分数从 0.347 降至 0.130。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mobile graphical user interface (GUI) agents have demonstrated remarkable capabilities in automating complex tasks, yet they introduce critical safety risks because a single erroneous action can lead to irreversible consequences. Existing safety mechanisms are primarily reactive, lacking the ability to assess risks before execution. In this paper, we introduce SeerGuard, a consequence-aware safety framework designed to mitigate these risks through pre-execution instruction-level screening and action-level risk assessment. Specifically, the action-level assessment analyzes agent-proposed actions within current GUI states, anticipating likely outcomes to identify risks before they are executed. To enable these capabilities, we construct a unified safety-augmented world model (SAWM) via multi-task learning, integrating semantic next-state prediction with safety risk assessment. Extensive experiments demonstrate that SeerGuard generalizes effectively across diverse mobile GUI agents. On Qwen3-VL-8B-Instruct, it increases the safety-utility score from 0.191 to 0.596 at ω=0.8 and reduces the risk-cost score from 0.347 to 0.130 at α=0.8. Further analyses on our SAWM validate the effectiveness of the instruction-level screening, alongside the capability of action risk assessment and next-state prediction.

</details>


### 投毒、后门与记忆完整性

### 24. BackdoorVLM: A Benchmark for Backdoor Attacks and Defenses on Vision-Language Models

🐙 [Code](https://github.com/bin015/BackdoorVLM)　📅 2026　🏷 ACM MM 2026

**关键词**：`benchmark`、`VLM backdoor`、`multimodal trigger`、`attack-defense evaluation`、`low-rate poisoning`

👤 **作者**：Juncheng Li、…、Yu-Gang Jiang

- 🎯 **研究动机**：后门攻击通过注入隐藏行为破坏机器学习系统的可靠性与可信性，相关威胁在单模态设定下已被广泛研究，但对多模态基础模型尤其是视觉语言模型的影响仍待系统探索，缺乏统一的攻防评测基准。
- 🔬 **研究方法**：提出首个 VLM 后门攻防综合基准 BackdoorVLM，以统一视角覆盖图像描述与视觉问答等核心视觉-语言任务；将多模态后门威胁组织为定向拒绝、恶意注入、越狱、概念替换、感知劫持 5 个代表性类别；用 12 种代表性攻击方法（覆盖文本、图像与双模态触发器）在 2 个开源 VLM 与 3 个多模态数据集上评测，并测试 5 种代表性防御方法。
- 📌 **结论**：分析揭示 VLM 对文本指令高度敏感，双模态后门中文本触发器通常压倒图像触发器；涉及文本模态的后门威力极大，低至 1% 的投毒率即可在多数任务上取得超 90% 的成功率；现有防御跨触发器类型与后门场景缺乏泛化，保护并不可靠。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks undermine the reliability and trustworthiness of machine learning systems by injecting hidden behaviors that can be maliciously activated at inference time. While such threats have been extensively studied in unimodal settings, their impact on multimodal foundation models, particularly vision-language models (VLMs), remains largely underexplored. In this work, we introduce BackdoorVLM, the first comprehensive benchmark for systematically evaluating backdoor attacks and defenses on VLMs across a broad range of settings. It adopts a unified perspective that injects and analyzes backdoors across core vision-language tasks, including image captioning and visual question answering. BackdoorVLM organizes multimodal backdoor threats into 5 representative categories: targeted refusal, malicious injection, jailbreak, concept substitution, and perceptual hijack. Each category captures a distinct pathway through which an adversary can manipulate a model's behavior. We evaluate these threats using 12 representative attack methods spanning text, image, and bimodal triggers, tested on 2 open-source VLMs and 3 multimodal datasets along with 5 representative defense methods. Our analysis reveals that VLMs exhibit strong sensitivity to textual instructions, and in bimodal backdoors the text trigger typically overwhelms the image trigger when forming the backdoor mapping. Notably, backdoors involving the textual modality remain highly potent, with poisoning rates as low as 1% yielding over 90% success across most tasks. Moreover, existing defenses lack generalization across trigger types and backdoor scenarios, leading to unreliable protection against diverse triggers across modalities and forms. These findings highlight significant, previously underexplored vulnerabilities in current VLMs. We hope that BackdoorVLM can serve as a useful benchmark for analyzing and mitigating multimodal backdoor threats. Code is available at: https://github.com/bin015/BackdoorVLM.

</details>

### 25. Beyond Static Cues: Unified Dynamic Detection of MLLM Backdoors via Dual-Flow Trajectory Analysis

🐙 [Code](https://github.com/kaoru0822-kitauji/EVO_Detect)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`MLLM backdoor`、`decoding trajectory`、`attention flow`、`unsupervised defense`

👤 **作者**：Yitong Sun、Ruochen Zhang、Xingxing Wei

- 🎯 **研究动机**：多模态大模型日益部署于安全关键领域，后门攻击仍是严峻挑战；现有防御从视觉中心 patch 线索发展到无监督内部注意力统计，但本质上依赖静态快照与攻击特定启发式；多模态触发器设计空间巨大（文本注入、亚感知噪声、跨模态协同触发器等），攻击类型未知时此类刚性先验极易被绕过。
- 🔬 **研究方法**：将诊断范式从静态观察转向动态输出演化，依据是成功攻击必然劫持解码轨迹：在生成过程中偏斜内部模态贡献，同时在输入扰动下维持异常的输出不变性。提出 EVO-Detect，通过 Attention Flow 与 Logits Flow 两个互补通道监测早期解码步内部信号的动态演化——注意力分支度量图文注意力分配的演化，logits 分支经干预消融量化输出分布对模态扰动的敏感性——再将轨迹转为样本级指标并相对负控签名归一化。
- 📌 **结论**：跨多样攻击族的评测显示该方法大幅超越 BYE、TCAP 等 SOTA 基线，确立动态多模态交互分析作为 MLLM 无监督后门检测的鲁棒基础。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) are increasingly deployed in safety-critical domains, yet their susceptibility to backdoor attacks remains a formidable challenge. While existing defenses have evolved from visual-centric patch cues to unsupervised internal attention statistics, they are fundamentally constrained by a reliance on static snapshots and attack-specific heuristics. Given the intricate interplay between dual modalities, the vast design space for multimodal triggers allows diverse threats, such as textual injections, sub-perceptual noises, and coordinated cross-modal triggers, to easily circumvent such rigid priors, particularly when attack types are unknown in real-world applications. In this paper, we rethink backdoor detection by shifting the diagnostic paradigm from static observations to dynamic output evolution. We observe that a successful attack inevitably hijacks the model's decoding trajectory, skewing internal modal contributions during generation while maintaining an abnormal output invariance despite input perturbations. To capture this behavior, we propose EVO-Detect, a unified detection framework that monitors the dynamic evolution of internal signals during early decoding steps through two complementary channels: Attention Flow and Logits Flow. The attention branch measures how image-text attention allocation evolves during early generation, whereas the logits branch quantifies the sensitivity of the output distribution to modal perturbations through interventional ablations. We then convert these trajectories into compact sample-level metrics and normalize them against negative-control signatures so that natural perturbations are less likely to be mistaken for backdoor evidence. Extensive evaluations show that our approach substantially outperforms state-of-the-art baselines such as BYE and TCAP across diverse attack families, establishing dynamic multimodal interplay analysis as a robust foundation for unsupervised backdoor detection of MLLMs. The code is publicly available at https://github.com/kaoru0822-kitauji/EVO_Detect.

</details>

### 26. DEFUSE: Generalizable Backdoor Defense for Self-Supervised Encoders with Generative Priors

📄 [arXiv](https://arxiv.org/abs/2608.25851) · 🐙 [Code](https://github.com/jsrdcht/DEFUSE)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`self-supervised encoder`、`backdoor`、`conditional diffusion`、`semantic reconstruction`

👤 **作者**：Minjing Dong、Benlei Cui

- 🎯 **研究动机**：自监督学习编码器易受后门攻击，威胁同时覆盖视觉 SSL 编码器与视觉-语言编码器；现有防御通常只针对其中一种范式，且依赖苛刻假设——如需要未感染的分布内数据或预计算伪标签——在实践中难以满足。
- 🔬 **研究方法**：受贝叶斯后验推断启发提出 DEFUSE，将后门检测重构为由条件扩散生成模型参数化的『表示条件图像似然估计』：未感染表示趋向产生语义一致的重建，而后门表示更可能被映射到攻击者目标类或语义无意义的图像，从而暴露后门。鉴于高度抽象的表示丢弃了像素级忠实重建所需的低层信息、精确似然不可解，将目标放松为语义重建并在参考编码器提供的分离表示空间中评估；通过微调预训练扩散模型利用其生成先验，把数据映射到自然图像流形同时保留语义内容。
- 📌 **结论**：跨多样攻击设置的实验显示 DEFUSE 大幅超越现有检测器，可同时泛化到视觉 SSL 与视觉-语言编码器，并显著降低对受害编码器或攻击策略先验知识的依赖。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-supervised learning (SSL) encoders are vulnerable to backdoor attacks, posing threats to both visual SSL encoders and vision-language encoders. Existing defenses are typically designed for only one of these paradigms and rely on restrictive assumptions such as access to uninfected in-distribution data or precomputed pseudo-labels, which are difficult to satisfy in practice. To address these limitations, we propose DEFUSE, a generalizable backdoor detection framework for SSL encoders. Inspired by Bayesian posterior inference, we reformulate backdoor detection as a representation-conditioned image likelihood estimation problem parameterized by a conditional diffusion generative model. Uninfected representations tend to yield semantically consistent reconstructions, whereas backdoored ones are more likely to be mapped to the attacker's target class or semantically meaningless images, deviating from the original semantics and thereby exposing the backdoor. However, we find that the exact likelihood is intractable, because highly abstracted representations discard the low-level information necessary for pixel-faithful reconstruction. We therefore relax the objective to semantic reconstruction and evaluate it in a well-separated representation space provided by a reference encoder. Rather than training from scratch, we fine-tune a pretrained diffusion model, leveraging its generative prior to map data onto the natural image manifold while preserving semantic content. Extensive experiments demonstrate that DEFUSE substantially outperforms existing detectors across diverse attack settings, generalizing to both visual SSL and vision-language encoders. Notably, our method greatly reduces the reliance on prior knowledge about the victim encoder or the attack strategy. The source code is available at https://github.com/jsrdcht/DEFUSE.

</details>

### 27. Dual-stream Soft Prompt Attacks on VLMs: Coordinated Visual and Textual Prompt Injection for Stealthy Backdoors

📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`VLM backdoor`、`soft prompt`、`dual-stream injection`、`frozen backbone`

👤 **作者**：Haotian Jin、…、Bo Li

- 🎯 **研究动机**：视觉-语言模型能力迅速增强的同时安全风险同步攀升，其中后门攻击——干净输入下行为正常、隐藏触发器出现时产生恶意输出——威胁尤甚；软提示后门对 VLM 构成的威胁此前尚未被揭示。
- 🔬 **研究方法**：提出双流软提示（DSP）攻击：向视觉与文本两个分支同时插入微小的软提示通道，在主干完全冻结的情况下操纵输出；设计两种双流提示变体——正交提示 OP（视觉与文本提示相互独立）与互导提示 MGP（两提示方向对齐）；在多个主流 VLM 架构与公开数据集上评估单触发与双触发攻击。
- 📌 **结论**：DSP 仅需很小的投毒预算与极少的额外参数，即可显著提升单触发与双触发攻击成功率，暴露了一个被忽视的威胁面，并为后续后门防御研究建立了更强基线。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large visionlanguage models (VLMs) have become increasingly powerful, but their security risks have risen just as sharplyespecially backdoor attacks, in which a model behaves normally on clean inputs yet produces malicious outputs when a hidden trigger is present. To our knowledge, we are the first to expose how vulnerable visionlanguage models (VLMs) are to soft-prompt backdoors and introduce the Dual-stream Soft Prompt (DSP) Attack. DSP inserts tiny soft prompt channels into both the visual and textual branches, enabling output manipulation while keeping the entire backbone frozen. We further design two dual-stream prompt variants: Orthogonal Prompts (OP), where visual and textual prompts are independent, and Mutual-Guided Prompts (MGP), where the two prompts are directionally aligned. Experiments on several mainstream VLM architectures and public datasets show that DSP requires only a small poisoning budget and minimal additional parameters, yet markedly increases both single-trigger and dual-trigger attack success rates. These findings expose an overlooked threat surface and establish a stronger baseline for future research in defending against backdoor attacks on VLMs.

</details>

### 28. Suit the Remedy to the Case: Precise Backdoor Elimination for Text-to-Image Diffusion Models via Model Editing

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`T2I diffusion`、`backdoor elimination`、`model editing`、`neuron activation variation`

👤 **作者**：Yanxin Yang、Ming Hu、Hao Shen、Yuejun Jiao、Mingsong Chen

- 🎯 **研究动机**：文生图扩散模型广泛应用的同时高度易受后门攻击——攻击者在训练期植入隐藏触发器以在推理时操纵输出；现有防御通常需要大量训练数据并采用粗粒度对齐，分别导致灾难性遗忘与语义退化，难以兼顾消除后门与保持性能。
- 🔬 **研究方法**：先分析中毒模型行为并获得两点发现：触发 token 的神经元激活变化（NAV）分布与正常 token 显著不同；非语义触发 token 的嵌入远离词表全部正常 token 构成的流形空间。据此提出基于模型编辑的后门消除框架 ManiEdit：以基于激活的模块定位方法计算 NAV 锁定后门模块，在受限区域内进行精确参数重耦以保护良性参数；再以流形驱动的触发器分类策略（句法与几何约束区分非语义与语义触发器）将非语义触发器对齐空提示、把语义触发器重对齐经去噪优化的语义锚点，无需昂贵重训练即可完成后门消除。
- 📌 **结论**：综合实验表明 ManiEdit 能有效抵御多种 SOTA 后门攻击方法，在消除后门的同时避免灾难性遗忘与语义退化。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the widespread adoption of Text-to-Image (T2I) Diffusion Models (DMs) across various applications, their security has attracted increasing attention. In particular, these models are highly vulnerable to backdoor attacks, where adversaries implant hidden triggers during training to manipulate model outputs at inference time. To deal with the backdoor attacks, existing defense methods typically require substantial training data and employ coarse-grained alignment, leading to catastrophic forgetting and semantic degradation, respectively. To defend against backdoor attacks while preventing performance degradation, this paper first analyzes the behavior of poisoned models and finds that i) the neuron activation variation distributions of trigger tokens are significantly different from those of normal tokens, and ii) the embeddings of non-semantic trigger tokens are far from the manifold space constructed by all the normal tokens in the vocabulary. Based on the findings, we propose ManiEdit, a novel model-edit-based backdoor elimination framework for T2I DMs. Specifically, we propose an activation-based module localization methodology to pinpoint the backdoored module by calculating the Neuron Activation Variations (NAV), enabling precise parameter recoupling within restricted areas to safeguard benign parameters from collateral damage. To sever malicious associations and restore the original semantics of triggers, we present a manifold-driven trigger categorization strategy, which detects triggers via NAV within the localized modules, subsequently applying syntactic and geometric constraints to distinguish non-semantic from semantic triggers. By aligning non-semantic triggers with empty prompts and realigning semantic triggers with denoising-optimized semantic anchors, ManiEdit can achieve efficient elimination without expensive retraining. Comprehensive experiments demonstrate the effectiveness of ManiEdit in defending against various state-of-the-art backdoor attack methods.

</details>

### 29. TOXRobo: Procedural Memory Poisoning in Retrieval-Augmented Embodied Planners

📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`embodied planner`、`procedural memory poisoning`、`retrieval-augmented`、`scene-native trigger`

👤 **作者**：Suhang Yao、Zhenxiong Yan、Yu Liu、Wenqiang Jin

- 🎯 **研究动机**：具身规划器通过推理场景观察与物理世界交互，并日益依赖检索外部跨模态记忆来应对长程任务；这一检索机制创造了新攻击面——被投毒的程序性记忆可被场景原生线索激活，并最终转化为不安全的物理动作。
- 🔬 **研究方法**：提出低预算程序性记忆投毒攻击 TOXRobo：仅污染少量可检索记录，并将其与场景原生的物体或物体组合线索耦合；每条毒记录由语义匹配的干净记忆派生，主要编辑其规划依据（rationale）、对相邻字段仅做最小的触发一致修改，从而在联合场景-指令线索下保持可检索性，并在检索后偏置下游规划生成；在 LIBERO、CALVIN 两个基准与 myCobot 真机部署上验证。
- 📌 **结论**：TOXRobo 在三个环境上一致诱导定向不当行为，同时保持非触发任务的干净效用；消融表明组合式触发器与以 rationale 为中心的编辑对攻击有效性与选择性至关重要，说明仅靠提示层或检索层防护不足以保护检索增强具身规划器。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Embodied planners interact with the physical world by reasoning over scene observations, a process increasingly augmented by retrieving external cross-modal memories to tackle long-horizon tasks. However, this retrieval mechanism creates a novel attack surface, where poisoned procedural memory can be activated by scene-native cues and ultimately translated into unsafe physical actions. In this paper, we present TOXRobo, a low-budget procedural memory poisoning attack that contaminates only a few retrievable records and couples them with scene-native object or object-composition cues. Each poisoned record is derived from a semantically matched clean memory and edited mainly through its planning rationale, with minimal trigger-consistent changes to adjacent fields, so that it remains retrievable under joint scene-instruction cues while still biasing downstream plan generation after retrieval. Across LIBERO, CALVIN, and a myCobot deployment, TOXRobo consistently induces targeted misbehavior while preserving clean-task utility on non-triggered tasks. Ablations show that compositional triggers and rationale-centered edits are important to attack effectiveness and selectivity. These results identify procedural memory as a concrete multimodal vulnerability in embodied AI and show that securing retrieval-augmented embodied planners requires defenses beyond prompt- or retrieval-only safeguards.

</details>

### 30. TRAP: Tail-aware Ranking Attack for World-Model Planning

📄 [arXiv](https://arxiv.org/abs/2605.01950)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`world model`、`trajectory ranking`、`backdoor`、`planning hijack`

👤 **作者**：Ke Zhang、Xizhao Luo

- 🎯 **研究动机**：世界模型通过内部生成并评估想象轨迹支持长程规划，是通用智能体的重要基础，但这一想象驱动的决策过程也带来新安全风险：现有后门攻击以局部特征、单步预测或即时策略输出为目标，其效果常被世界模型学到的动力学先验与规划过程吸收或冲刷；研究发现世界模型在想象轨迹的长尾排序结构上存在独特后门脆弱性——扰乱少数决策关键轨迹的排序即可系统性劫持规划。
- 🔬 **研究方法**：提出面向世界模型的后门攻击框架 TRAP，以想象轨迹排序为攻击目标：尾部感知排序损失将优化聚焦于决策关键轨迹，双重门控机制稳定优化并调节攻击惩罚施加的时机与位置；触发条件下改变想象轨迹的相对排序以重定向规划结果，干净输入上则大体维持正常排序结构。
- 📌 **结论**：在 DreamerV3 与 TD-MPC2 上跨多样任务的实验显示，TRAP 一致诱发持续的行为偏差与显著的性能退化，凸显对世界模型智能体开展专门安全评测的必要性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

World models enable long-horizon planning by internally generating and evaluating imagined trajectories, making them a promising foundation for generalist agents. However, this imagination-driven decision process also introduces new security risks. Existing backdoor attacks typically aim to manipulate local features, one-step predictions, or instantaneous policy outputs. While such objectives may suffice for weaker reactive models, they are often ineffective against world models, where the learned dynamics prior and planning process can absorb or wash out the effects of shallow perturbations. More importantly, we find that world models exhibit a distinct backdoor vulnerability rooted in the long-tailed ranking structure of imagined trajectories, where disrupting the ordering of a few decision-critical trajectories can systematically hijack planning. To exploit this vulnerability, we propose TRAP, a backdoor attack framework for world models that targets imagined trajectory ranking. TRAP combines a tail-aware ranking loss to focus optimization on decision-critical trajectories with dual gating mechanisms that stabilize optimization and regulate when and where the attack penalty is applied. Under trigger conditions, TRAP alters the relative ranking of imagined trajectories to redirect planning outcomes, while largely maintaining the normal ranking structure on clean inputs. Experiments on DreamerV3 and TD-MPC2 across diverse tasks show that TRAP consistently induces sustained behavioral deviations and significant performance degradation, highlighting the need for dedicated security evaluation of world-model-based agents.

</details>

### 31. Understanding Backdoor Attacks in Scene Graph Generation via Global Context Pathway

🐙 [Code](https://github.com/rafa-cxg/SGGBackdoor)　📅 2026　🏷 ACM MM 2026

**关键词**：`analysis`、`scene graph generation`、`training-time backdoor`、`global context pathway`、`relation corruption`

👤 **作者**：Xiaoguang Chang、Tuo Chen、Chengze Jiang、Teng Wang、Changyin Sun

- 🎯 **研究动机**：场景图生成（SGG）产出结构化场景表示，但其训练期后门风险从未被探索；与分类不同，SGG 暴露 pair 级攻击面，可选择性地破坏涉及特定物体类别的关系；同时 SGG 高度依赖局部证据，全局放置的触发器本难以操纵预测，而新架构日益引入全局上下文反而可能助长此类攻击。
- 🔬 **研究方法**：系统研究该风险并考察全局上下文通路在后门行为中的作用：先实例化一种有效的攻击方法，并提出三轴评测协议刻画后门行为；在 Visual Genome 上用代表性开放词表与闭集 SGG 模型实验，并通过把推理期被投毒的全局上下文表征替换为干净对应物、以及训练期抑制该通路触发信号进行机制分析。
- 📌 **结论**：攻击对所评测模型均有效；显式全局上下文通路是后门效应的主要载体——替换为干净表征后，OvSGTR 系与 RelationFormer 的攻击成功率分别锐降 100% 与 97%；训练期抑制该通路要么降低攻击成功率、要么大幅损害效用，说明显式全局上下文设计本身可能构成后门风险。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Scene Graph Generation (SGG) produces structured scene representations, yet its training-time backdoor risk remains unexplored. Unlike classification, SGG exposes a pair-level attack surface that enables selective corruption of relations involving a designated object category. However, because SGG largely relies on localized evidence, globally placed triggers may face difficulty in manipulating such predictions. Recent SGG architectures increasingly incorporate global context to improve scene modeling, which may in turn facilitate such attacks. In this paper, we systematically study this backdoor risk and investigate the role of the global context pathway in backdoor behavior. Concretely, we first instantiate this attack with an effective method, and propose a three-axis evaluation protocol to characterize backdoor behavior. Experiments on Visual Genome with representative open-vocabulary and closed-set SGG models demonstrate the effectiveness of the attack. Mechanistic analyses reveal that the explicit global context pathway serves as a major carrier of the backdoor effect across the evaluated SGG models. In particular, replacing the poisoned global context representation with its clean counterpart during inference sharply suppresses the attack, yielding 100% and 97% reductions in attack success for the OvSGTR family and RelationFormer, respectively. Moreover, training-time interventions in the OvSGTR family show that suppressing trigger signals in this pathway either reduces attack success or substantially degrades utility. Together, these findings suggest that explicit global context designs may pose a backdoor risk in SGG architectures. Code is available at https://github.com/rafa-cxg/SGGBackdoor.

</details>


### 对抗攻击与鲁棒性防御

### 32. A Needle in the Splat: Composable Adversarial Attack against Commercial 3DGS Services

📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`3D Gaussian Splatting`、`denial-of-service`、`Gaussian densification`、`memory exhaustion`

👤 **作者**：Hao Wang、Yuxuan Zhang、Wei Yang

- 🎯 **研究动机**：基于 3DGS 的商业重建服务直接依赖用户上传图像，恶意扰动可触发高斯基元失控增长，导致 GPU 显存耗尽甚至拒绝服务；但现有攻击破坏程度有限，且受硬件约束难以在复杂 3D 场景奏效。
- 🔬 **研究方法**：提出 H-poison 攻击框架，以触发高斯基元指数级增长为核心：构建高斯加权总变差（GW-TV）目标合成针状纹理扰动，诱导任意方向与步长下的冗余致密化；设计可组合 3D 驱动攻击模块 C3DAM，把可复用的 3D 对抗纹理注入 2D 图像，级联 C3DAM 同时输出多视角一致对抗图像、优化场景专用代理模型并在跨场景攻击中精炼通用 3D 噪声模型，弥合 2D-3D 域差距。
- 📌 **结论**：白盒与黑盒实验表明，H-Poison 在受害方破坏程度与攻击方成本两端均达到 SOTA，同时扰动不可感知并保持高重建质量；结果表明攻击者仅需上传图像即可令商业 3DGS 重建服务陷入显存耗尽乃至拒绝服务，提示此类平台需对上传图像做安全审查。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

3D Gaussian Splatting (3DGS) has recently gained significant popularity for efficient 3D reconstruction, prompting many platforms to offer commercial 3D reconstruction services based on user-uploaded images. This untrusted-input reliance exposes a severe security risk within the core pipeline of 3DGS. By uploading images with malicious perturbations, attackers can trigger uncontrolled Gaussian growth, leading to GPU memory exhaustion or even Denial-of-Service (DoS). However, existing attacks cause limited damage and struggle in complex 3D scenes due to hardware constraints. To address this, we propose H-poison, an efficient 3DGS adversarial attack framework centered on manipulating 3DGS systems to trigger exponential growth of Gaussian primitives. Specifically, we first formulate a Gaussian-weighted Total Variation (GW-TV) objective to synthesize needle-like texture perturbations, which reliably induce unnecessary Gaussian densification across arbitrary directions and step sizes. We subsequently design a Composable 3D-Driven Attack Module (C3DAM) to inject reusable 3D adversarial textures into 2D images. The cascaded C3DAMs bridge the 2D-3D domain gap by simultaneously outputting multi-view consistent adversarial images, optimizing scene-specific proxy models, and refining a universal 3D noise model during cross-scene attacks. Extensive white-box and black-box experiments demonstrate that H-Poison achieves state-of-the-art performance in both victim-side damage and attacker-side cost, while preserving imperceptible perturbation and high reconstruction quality.

</details>

### 33. AdvNav: Behavior-Guided Black-Box Adversarial Attacks on Vision-Language Navigation

📄 [arXiv](https://arxiv.org/abs/2607.11063)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`vision-language navigation`、`gradient-free optimization`、`genetic algorithm`、`embodied perception`

👤 **作者**：Chenyang Li、Kaige Li、Zeyu Jiang、Changhao Chen

- 🎯 **研究动机**：视觉语言导航（VLN）系统易受视觉扰动攻击，但现有方法多需目标模型梯度白盒访问，对真实部署系统不现实且递归反向传播计算量大；已有黑盒攻击面向单步瞬时决策，难以处理 VLN 多步序列感知-行动回路的时序依赖。
- 🔬 **研究方法**：提出行为引导的黑盒攻击框架 AdvNav，导航过程中仅扰动智能体第一人称视角。从智能体自身输出行为构造免梯度代理目标，聚合双粒度反馈：轨迹级导航退化得分、动作级决策风险奖励与偏差指标；该反馈驱动混合优化——启发式自适应调节扰动强度，并用遗传算法演化噪声空间结构，迭代搜索破坏力最强的噪声配置。在 R2R 数据集上对 Transformer 型 HAMT 与 LLM 型 MapGPT 评测。
- 📌 **结论**：AdvNav 对 HAMT 与 MapGPT 两类骨干分别取得 49.70%、65.96% 与 87.30% 的攻击成功率，验证了免梯度行为反馈攻击的有效性与跨架构通用性，同时揭示 VLN 感知环节的结构性脆弱点，为鲁棒导航模型设计提供参考。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite progress in Embodied AI, Vision-and-Language Navigation (VLN) systems remain vulnerable to adversarial visual disturbances. Most existing methods rely on white-box access to target model gradients, which is often unrealistic for real-world deployed systems and computationally exhaustive due to recursive backpropagation for optimization, limiting their applicability. While previous black-box methods predominantly target single-step, instantaneous decision tasks, they struggle to handle the task complexities and temporal dependencies of VLN. This highlights the need for a gradient-free attack method that can effectively disrupt the multi-step sequential perceptionaction loop using only observable inputs and outputs. Therefore, we propose AdvNav, a behavior-guided black-box adversarial attack framework that disturbs an agents first-person views during navigation. To construct an informative surrogate objective for effective optimization guidance in gradient-free search under the black-box setting, we design a dual-granularity behavior-based feedback, aggregating a trajectory-level performance score representing overall navigation degradation, an action-level reward score considering the potential decision risk, and a deviation indicator, all of which are extracted from the agent's self-output behaviors. This feedback guides a hybrid optimization strategy that (i) heuristically tunes perturbation strength via adaptive updates and (ii) evolves noise spatial structure genetically, to iteratively discover the most disruptive noise configuration. Evaluated against Transformer-based model HAMT and LLM-based model MapGPT with two types of backbones on R2R dataset, AdvNav achieves 49.70%, 65.96%, and 87.30% Attack Success Rate, respectively. The result demonstrates the effectiveness and generality of AdvNav, reveals critical perception vulnerabilities and offers insights for the design of future resilient VLN models.

</details>

### 34. Boosting Cross-Prompt Adversarial Transferability in VLMs via Anchored Dual-Track Prompt Self-Correction

📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`cross-prompt transferability`、`self-correction`、`prompt hardening`、`vision-language models`

👤 **作者**：Xiaolei Liu、Yuanlong Yu、Shouling Ji

- 🎯 **研究动机**：现实中同一图像常被多样 prompt 查询，对抗样本需跨 prompt 保持有效才能评估 VLM 实际安全；现有跨 prompt 攻击把 prompt 变化建模为嵌入空间连续潜在扰动，无法覆盖推理时 token 级改写与自校正指令带来的显式变化。
- 🔬 **研究方法**：提出锚定双轨自校正攻击 ADSA，从两个互补方向强化优化期 prompt 加固：Token 级对抗 prompt 搜索 TAPS 在预算内做 token 替换，构造更难且与意图相关的 prompt 变体参与跨 prompt 优化；自校正引导跨 prompt 优化 SCG-CPO 把自校正作为过程级难 prompt 条件加入对抗优化；锚定设计使 prompt 侧优化聚焦改写后的查询而非辅助自校正模板。在多个 VLM 与任务上实验。
- 📌 **结论**：多 VLM、多任务实验显示，ADSA 在多样目标输出上一致超越既有方法，且在自校正与上下文学习设定下仍保持攻击有效，为评估 VLM 面向真实查询变化的对抗安全提供更强基线。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models (VLMs) have been shown to be vulnerable to adversarial examples (AEs), i.e., images that remain visually similar to benign ones but can induce malicious outputs. The risk is exacerbated in realistic scenarios, where the same image may be queried with diverse prompts and an effective AE should remain effective across such prompt variations. Therefore, improving the cross-prompt transferability of AEs is crucial for assessing the practical security of VLMs. Existing cross-prompt attacks mainly improve transferability by searching for harder prompts in a local neighborhood of the prompt embedding space. Despite their effectiveness, this formulation still models prompt variation as a continuous latent perturbation and therefore does not fully capture explicit prompt changes encountered at inference time. In practice, prompts are more often varied through token-level rewriting or reasoning-process modifications induced by self-correction instructions. Motivated by this gap and recent progress on self-correction in VLMs, we propose the Anchored Dual-Track Self-Correction Attack (ADSA) for improving cross-prompt adversarial transferability. ADSA strengthens optimization-time prompt hardening from two complementary directions: Token-level Adversarial Prompt Search (TAPS), which performs budgeted token-level substitutions to construct harder, intent-related prompt variants for cross-prompt optimization, and Self-Correction-Guided Cross-Prompt Optimization (SCG-CPO), which introduces self-correction as a process-level hard prompt condition during adversarial optimization. Moreover, ADSA adopts an anchored design that keeps prompt-side optimization focused on the rewritten query rather than the auxiliary self-correction template. Extensive experiments on multiple VLMs and tasks show that ADSA consistently outperforms prior methods across diverse target outputs and remains effective under self-correction and in-context learning settings.

</details>

### 35. CaptchaBench: A Modality-Stratified Benchmark Dataset for Evaluating Adversarial Perturbation Against VLM-based CAPTCHA Recognition

🐙 [Code](https://github.com/Linzy19/CaptchaBench)　📅 2026　🏷 ACM MM 2026

**关键词**：`benchmark`、`CAPTCHA`、`adversarial perturbation`、`input modality`、`black-box evaluation`

👤 **作者**：Zongying Lin、Hongbin Zhang、Yuhui Hu、Jinxing Liu

- 🎯 **研究动机**：VLM 在中文字符验证码上零样本准确率已超 99%，复杂背景、艺术字体、字符扭曲等传统加固失效；对抗扰动是新兴防御，但各方法从未在相同条件下比较，其输入模态作用也缺乏跨 VLM 架构的系统刻画。
- 🔬 **研究方法**：构建基准 CaptchaBench：840,000 张基础验证码图像（3,500 字符 × 120 背景 × 2 条生成管线）及 16,000 张对抗扰动分层评测子集；8 种扰动方法（含 Nightshade、MMCoA 等）按输入模态分为 Image-only、Text-only、Image+Text 三组，在直接识别准确率、文本可见率、攻击成功率三问框架下评测五个商用 VLM。
- 📌 **结论**：三大发现：扰动输入模态对应不同黑盒响应模式；Gemini-3.0 呈特异文本可见率响应（62.4–97.3%，其他 VLM 均 ≤20.8%，高出 ≥3.0 倍）且跨 prompt 持续；笔画箱 ASR 随方法变化，16–20 笔画箱偏高。29 人实验确认扰动验证码可读性 98.9%。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Models (VLMs) now achieve over 99% zero-shot accuracy on Chinese-character CAPTCHAs, rendering traditional hardening strategies (complex backgrounds, stylized fonts, character distortion) ineffective. Adversarial perturbation offers an emerging defense by exploiting model vulnerabilities at the decision-boundary level, yet existing methods originate from disparate communities and have never been compared under identical conditions; moreover, the role of perturbation input modality has not been systematically characterized across heterogeneous VLM architectures. To bridge these gaps, we introduce CaptchaBench, a large-scale benchmark comprising 840,000 base Chinese-character CAPTCHA images (3,500 characters sampled from GB2312 Level-1 × 120 backgrounds × 2 generative pipelines), with a stratified evaluation subset of 16,000 adversarially perturbed images. Eight perturbation methods are organized into three input-modality groups (Image-only: ASPL, Glaze, AMP, XTransfer, AnyAttack; Text-only: Nightshade; Image+Text: MMCoA, CoA) and assessed under a unified three-question framework: Q1 Direct-Recognition Accuracy (DRA) and Q1 Failure, Text Visibility Rate (TVR), and Q3 Attack Success Rate (ASR), capturing complementary black-box response behaviors. Baseline evaluation across five commercial VLMs (Qwen-VL, Kimi 2.5, GPT-5.2, Gemini-3.0, GLM-4V) yields three key observations: (1) perturbation input modality is associated with distinct black-box response patterns: image-only methods achieve high visual confusion but variable VLM-reported visibility, while methods differ in cross-VLM variation; (2) Gemini-3.0 exhibits a pronounced, model-specific TVR response pattern (62.4–97.3% vs. ≤20.8% for all other VLMs; ≥3.0× vs. the highest non-Gemini TVR across all eight methods), that persists across prompt variants; and (3) stroke-bin Q3 ASR varies across methods, with the 16–20-stroke bin high in this evaluation; the sparsely sampled 21+ bin is reported descriptively. This motivates character structure as a CAPTCHA design dimension. A 29-participant four-choice study confirms high human readability of perturbed CAPTCHAs (98.9% accuracy). The dataset and evaluation code are released under CC BY 4.0. Extended tables, figures, and visual case studies are available as online supplementary material on the CaptchaBench dataset website at https://github.com/Linzy19/CaptchaBench.

</details>

### 36. CoDA: Exploring Chain-of-Distribution Attacks and Post-Hoc Token-Space Repair for Medical Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2603.18545)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`medical vision-language model`、`distribution shift`、`clinical pipeline`、`token-space repair`

👤 **作者**：Chunlei Meng

- 🎯 **研究动机**：医学视觉语言模型（MVLM）广泛用于放射科管线与多模态助手，但真实成像流程下的可靠性缺乏研究；已有评测假设干净输入或只考察孤立像素扰动，忽略保留临床可读性却微妙改变图像统计量的采集、重建、显示与传输操作。
- 🔬 **研究方法**：提出链式分布攻击框架 CoDA：组合类采集着色、重建与显示重映射、传输导出退化，构造临床合理的管线偏移；在掩码结构相似性约束下联合优化阶段组合族与阶段内参数，在诱导失效的同时保持视觉合理性。覆盖脑 MRI、胸片、腹部 CT 三种模态，并把 MLLM 用作成像真实性与质量审计器评估；并提出教师引导 token 空间适配加块级对齐的事后修复。
- 📌 **结论**：CoDA 大幅削弱 CLIP 式 MVLM 零样本性能，且链式组合的破坏一致强于任何单一阶段；专有 MLLM 在单次自我挑战协议下审计可靠性退化、持续高置信犯错，受测医学专用 MLLM 在图像质量审计上明显不足；轻量级 token 空间对齐修复可提升被攻击归档输出上的零样本分类准确率。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Medical vision-language models (MVLMs) are increasingly used as perceptual backbones in radiology pipelines and as the visual front end of multimodal assistants, yet their reliability under real clinical imaging workflows remains underexplored. Prior robustness evaluations often assume clean, curated inputs or study isolated corruptions and pixel-level perturbations, overlooking routine acquisition, reconstruction, display, and delivery operations that preserve clinical readability while subtly shifting image statistics. To address this gap, we propose CoDA, a chain-of-distribution framework that constructs clinically plausible pipeline shifts by composing acquisition-like shading, reconstruction and display remapping, and delivery and export degradations. Under masked structural-similarity constraints, CoDA jointly optimizes stage-composition families and within-stage parameters to induce failures while preserving visual plausibility. Across brain MRI, chest X-ray, and abdominal CT, CoDA substantially degrades the zero-shot performance of CLIP-style MVLMs, with ablations showing that chained compositions are consistently more damaging than any single stage. We also evaluate multimodal large language models (MLLMs) as technical-authenticity auditors of imaging realism and quality rather than pathology. Proprietary MLLMs show degraded auditing reliability and persistent high-confidence errors on CoDA-shifted samples under a single-call self-challenge protocol, while the medical-specific MLLMs we test exhibit clear deficiencies in medical image quality auditing. Motivated by these findings, we introduce a post-hoc repair strategy based on teacher-guided token-space adaptation with patch-level alignment to improve zero-shot classification accuracy on archived CoDA outputs. Overall, our study characterizes a clinically grounded threat surface for MVLM deployment and shows that lightweight alignment improves robustness in deployment.

</details>

### 37. Counterfactual-Guided Diversified Path Integration for Transferable Neuron Attribution Attacks

🐙 [Code](https://github.com/AdvML-Group/COPIA)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`neuron attribution`、`counterfactual`、`transferability`、`cross-layer aggregation`

👤 **作者**：Di Ming、Yunlong Wang

- 🎯 **研究动机**：可迁移对抗攻击凭借黑盒有效性对真实部署的神经网络构成严重威胁；基于神经元归因的攻击虽能增强迁移性，但现有方法受积分路径噪声累积或结构单一的制约，且普遍依赖单层神经元归因、未能利用多层互补信息。
- 🔬 **研究方法**：提出反事实引导多样化路径积分神经元归因攻击 COPIA：把反事实引导路径引入神经元归因框架，缓解积分轨迹的噪声累积并支持模型自适应构建；多样化路径更新机制与反事实样本进一步增强路径多样性；设计跨层归因（CA）机制，通过归因流把深层归因信息渐进聚合到目标攻击层，捕获跨层互补语义。在 ImageNet 上对正常训练模型、对抗训练 CNN、ViT 及多种防御模型实验。
- 📌 **结论**：在 ImageNet 跨正常训练模型、对抗训练 CNN、ViT 与多种防御模型的黑盒设定下，COPIA 一致优于 SOTA 方法；跨层归因机制高度通用，可直接叠加到既有单层神经元归因攻击上并有效提升其黑盒迁移性，代码与补充材料已开源。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Transferable adversarial attacks pose significant security threats to neural networks due to their strong black-box effectiveness against real-world models. While neuron attribution-based attacks have shown promise in enhancing transferability, existing methods are often constrained by integration paths that accumulate noise or lack structural diversity. Moreover, they typically rely on single-layer neuron attribution, failing to exploit multi-layer information. To address these limitations, we propose COunterfactual-Guided Diversified Path Integration Neuron Attribution Attack, termed COPIA. Specifically, we incorporate counterfactual-guided paths into the neuron attribution framework, to effectively mitigate noise accumulation in integration trajectories and enable model-adaptive construction. Building on this, we diversify path update mechanisms and counterfactual samples to enhance path diversity and improve adversarial transferability. Furthermore, to capture the complementary semantics across different layers, we design a Cross-layer Attribution (CA) mechanism that progressively aggregates attribution information from deeper layers into the target attack layer via attribution flow. Extensive experiments on the ImageNet dataset across normally trained models, adversarially trained CNNs, ViTs, and various defense models demonstrate that COPIA consistently outperforms state-of-the-art methods in black-box attack settings. In addition, the proposed CA mechanism is highly generalizable and effectively improves the black-box transferability of existing single-layer neuron attribution attacks. Code and supplementary materials are available at https://github.com/AdvML-Group/COPIA.

</details>

### 38. DIFPA: Boosting Adversarial Transferability via Diffusion-based Importance-aware Feature Pyramid Attack

📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`feature importance`、`diffusion`、`feature pyramid`、`black-box transferability`

👤 **作者**：Xiaolei Liu、Yuanlong Yu、Shouling Ji

- 🎯 **研究动机**：黑盒设定下基于迁移的攻击靠代理模型上构造的对抗样本欺骗未知目标模型，迁移性是核心；现有特征级攻击受不可靠重要性估计与单层依赖限制，重要性从单一输入或启发式变换估计，易被不稳定非鲁棒响应污染。
- 🔬 **研究方法**：观察到扩散前向过程逐步扰动输入时，不稳定非鲁棒响应被逐渐衰减而语义相关鲁棒响应愈发集中，据此提出 DIFPA：扩散引导重要性估计器 DGIE 以扩散前向边缘作为可控邻域采样器，探测局部特征稳定性、抑制非鲁棒响应，产出更可靠的特征重要性指标；层级特征金字塔攻击 HFPA 跨多层聚合重要特征，以金字塔方式而非单层压制可迁移内在特征。
- 📌 **结论**：大量实验表明 DIFPA 一致超越 SOTA 方法：对正常训练模型平均攻击提升 8.17%，对防御模型平均提升 7.92%，验证扩散引导重要性估计与多层金字塔压制结合能显著增强黑盒迁移攻击。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep neural networks (DNNs) are known to be vulnerable to adversarial examples, raising serious security concerns in real-world applications. In black-box settings, transfer-based attacks exploit the transferability of adversarial examples crafted on a surrogate model to fool unknown target models, making transferability a central issue in practical adversarial attacks. Recent feature-level transfer attacks improve transferability by perturbing intermediate representations that are more likely to be shared across architectures. However, their effectiveness is still limited by unreliable feature-importance estimation and an over-reliance on single-layer features, which together hinder the accurate localization and suppression of transferable intrinsic features. In particular, existing methods often estimate feature importance from a single input or heuristic transformations, making the resulting indicators easily contaminated by unstable non-robust responses. We observe that, as the diffusion forward process progressively perturbs an input, unstable non-robust responses are gradually attenuated, while semantically relevant robust responses become more concentrated. Inspired by this observation, we propose the Diffusion-based Importance-aware Feature Pyramid Attack (DIFPA), a novel feature-level attack that improves transferability from both importance estimation and hierarchical feature modeling. Specifically, we introduce a Diffusion-Guided Importance Estimator (DGIE), which exploits the diffusion forward marginal as a principled and controllable neighborhood sampler to probe local feature stability, suppress unstable non-robust responses, and produce more reliable feature-importance indicators. We further propose a Hierarchical Feature Pyramid Attack (HFPA), which systematically aggregates important features across multiple layers and exploits the hierarchical semantic diversity of DNNs to suppress transferable intrinsic features in a pyramid manner rather than at a single layer. Extensive experiments demonstrate that DIFPA consistently outperforms state-of-the-art methods, achieving average improvements of 8.17% against normally trained models and 7.92% against defended models.

</details>

### 39. GhostPrompt: Cross-Image Adversarial Prompt for Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2607.19683) · 🐙 [Code](https://github.com/Ye-ze-yu/GhostPrompt)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`adversarial prompt`、`cross-image transferability`、`joint optimization`、`vision-language models`

👤 **作者**：Li Zeng、Hangtao Zhang、Xianlong Wang、Zhetao Li

- 🎯 **研究动机**：VLM 的多数文本对抗攻击沿袭语言模型方法，优化时固定视觉输入，对抗 prompt 因此绑定特定图像、换图即失效；跨图像迁移是此前缺失的研究视角：优化一次、跨多样图像复用并诱导攻击者指定输出。
- 🔬 **研究方法**：提出 GhostPrompt 对抗 prompt，以联合优化把图像不变对抗特征蒸馏进 prompt，采用最坏情况生成：交替执行两个步骤——为当前 prompt 构造困难视觉条件，以及更新 prompt 使其在这些条件下仍有效——从而将攻击效果泛化到训练未见的图像。在多个主流 VLM 上验证攻击效果。
- 📌 **结论**：在多个主流 VLM 上，GhostPrompt 攻击成功率较 SOTA 基线提升超过 30%，计算时间削减约 70%，首次证明优化一次、跨图复用的对抗 prompt 既可行又高效，代码已开源。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Models (VLMs) are known to be vulnerable to adversarial attacks, where subtle perturbations to images or texts induce erroneous outputs. However, most text-based attacks are adapted from language-model-centric methods, in which the visual input is fixed during optimization, resulting in adversarial prompts that are tied to specific images and thus limiting their attack effectiveness. To this end, we first introduce a new research perspective: cross-image transferability for adversarial prompts. We then propose GhostPrompt, an adversarial prompt that is optimized once and reused to steer VLM outputs toward attacker-specified responses across diverse images. GhostPrompt employs a joint optimization that distills image-invariant adversarial features into the prompt by "worst-case" generation. Specifically, it alternates between constructing hard visual conditions for the current prompt and updating the prompt to remain effective under these conditions. Extensive experiments on prevalent VLMs verify that GhostPrompt achieves an improvement of over 30% in attack success rates compared to state-of-the-art (SoTA) baselines, while reducing computation time by ～70%. Our code is avalable at https://github.com/Ye-ze-yu/GhostPrompt.

</details>

### 40. IDATA: Scalable Invertible Diffusion for Unrestricted Adversarial Transfer Attack

📄 [arXiv](https://arxiv.org/abs/2608.08734) · 🐙 [Code](https://github.com/colourful-pan/IDATA)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`invertible diffusion`、`discrete wavelet transform`、`constant-memory backpropagation`、`visual imperceptibility`

👤 **作者**：Jun-Jie Huang、Tianrui Liu、Zihan Chen

- 🎯 **研究动机**：无限制对抗迁移攻击是评估深度视觉模型黑盒鲁棒性的重要手段，基于扩散的方法沿去噪轨迹在潜空间优化扰动，兼顾迁移性与不可感知性，但受两大瓶颈制约：多步反向传播内存开销巨大，且对中间潜变量的扰动不区分频率。
- 🔬 **研究方法**：提出内存高效框架 IDATA，含两个模块：可逆扩散模块 IDM 把扩散轨迹上的对抗优化重构为可逆过程，按需重建中间状态实现常数内存反向传播，无需存储完整去噪链；低频约束模块 LFCM 用离散小波变换把潜变量分解为低频与高频分量，将扰动限制在语义稳定的低频子空间。在多个基准与多样模型架构上评测攻击成功率、内存与视觉质量。
- 📌 **结论**：在多个基准与多样架构上，IDATA 在攻击成功率、内存效率与视觉不可感知性三方面一致超越 SOTA 基线，表明可逆扩散加低频约束能同时提升黑盒迁移攻击的效率与隐蔽性，可作为深度视觉模型鲁棒性评估的高效工具。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unrestricted adversarial transfer attacks are important for evaluating the black-box robustness of deep visual models. Diffusion-based attacks have shown promising transferability and visual imperceptibility by optimizing adversarial perturbations along denoising trajectories in latent space. However, existing methods are limited by two challenges: memory-intensive multistep backpropagation and frequency-agnostic perturbation over intermediate latents. To address these issues, we propose IDATA, a memory-efficient diffusion framework for unrestricted adversarial transfer attack. IDATA consists of two key components: an Invertible Diffusion Module (IDM) and a Low-Frequency Constraint Module (LFCM). Specifically, IDM reformulates adversarial optimization over diffusion trajectories as an invertible process, enabling constant-memory backpropagation through on-demand reconstruction of intermediate states instead of storing the full denoising chain. Moreover, LFCM leverages Discrete Wavelet Transform (DWT) to decompose latent variables into low- and high-frequency components, restricting perturbations to semantically stable low-frequency subspaces, thereby improving transferability while preserving visual imperceptibility. Extensive experiments on multiple benchmarks and diverse model architectures demonstrate that IDATA consistently outperforms state-of-the-art baselines in attack success rate, memory efficiency, and visual imperceptibility. These results suggest that IDATA is a promising tool for black-box robustness evaluation of deep visual models. Code is available at https://github.com/colourful-pan/IDATA.

</details>

### 41. IRAA: Information Redistribution Adversarial Attacks for Multimodal Object Detection

📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`multimodal object detection`、`cross-modal fusion`、`information redistribution`、`perturbation stealthiness`

👤 **作者**：Sixu Liu、You Yanan、Jie Yang

- 🎯 **研究动机**：多模态目标检测融合光学、SAR、红外等异构传感器，依赖跨模态特征对齐与融合一致性构造判别表征，该依赖本身即对抗脆弱性来源；现有攻击多为单模态检测器设计或朴素多模态扩展，或无法有效削弱多模态检测器，或引入明显视觉伪影。
- 🔬 **研究方法**：把多模态对抗攻击形式化为逆信息重分布过程，提出双级破坏策略：空间熵重分布模块 SERM 在特征层分散判别特征、削弱跨模态一致性；预测不确定性破坏模块 PUDM 在预测层退化语义置信度与定位精度；模态感知优化策略 MAOS 依据各模态固有特性平衡扰动幅度，在感知约束下同时保持视觉质量与攻击有效性。在 Optical-SAR 与 Optical-Infrared 数据集上跨多个 SOTA 检测器评测。
- 📌 **结论**：白盒与黑盒设定下，IRAA 均使多个 SOTA 多模态检测器性能显著退化，且扰动保持视觉质量，揭示跨模态融合一致性机制的结构性脆弱面，为多模态感知系统的安全评估提供新攻击基线。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal object detection integrates heterogeneous space-based sensors (e.g., optical, SAR, infrared) to achieve robust perception in challenging conditions, which rely on cross-modal feature alignment and fusion consistency to construct discriminative representations. However, this dependency also introduces adversarial vulnerabilities, as perturbations can disrupt cross-modal consistency and degrade fused representations. Existing adversarial attacks are primarily designed for single-modal detectors or rely on naive multimodal extensions, which either fail to effectively degrade multimodal detectors or introduce noticeable visual artifacts. In this paper, we formulate multimodal adversarial attacks as an inverse information redistribution process and propose the Information Redistribution Adversarial Attack (IRAA). IRAA adopts a dual-level disruption strategy: the Spatial Entropy Redistribution Module (SERM) disperses discriminative features to weaken cross-modal consistency at feature-level, while the Prediction Uncertainty Disruption Module (PUDM) degrades semantic confidence and localization accuracy at prediction level. To ensure effective perturbation under perceptual constraints, a Modality-Aware Optimization Strategy (MAOS) is further introduced to balance perturbations across modalities via their inherent characteristics, preserving visual quality while maintaining attack effectiveness. Extensive experiments on Optical-SAR and Optical-Infrared datasets across multiple state-of-the-art detectors demonstrate that IRAA consistently achieves significant performance degradation in both white-box and black-box settings, revealing the vulnerability of multimodal detectors.

</details>

### 42. Learning What Not to Learn: Adversarial Disentangled Prompt Tuning for Robust Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2608.17306) · 🐙 [Code](https://github.com/cheny02/ADAPT-ACMMM2026)　📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`prompt tuning`、`adversarial robustness`、`feature disentanglement`、`unseen-class generalization`

👤 **作者**：Yang Chen、Zhan Zhuang、Yanbin Wei、Hua Liu、Yu Zhang

- 🎯 **研究动机**：对抗 prompt 微调可高效提升 VLM 鲁棒性，但现有方法加剧对已见类别的鲁棒过拟合：随着训练推进，对未见类对抗样本的性能快速退化；实证发现退化源于模型学到不可泛化的伪鲁棒特征（捷径）。
- 🔬 **研究方法**：遵循学习不学什么的设计哲学提出 ADAPT：双 prompt 机制包含目标 prompt 与诱饵 prompt 池，训练中诱饵 prompt 被引导诱捕多样伪鲁棒特征，目标 prompt 则在嵌入空间与诱饵正交的约束下学习真鲁棒特征，实现二者解耦；理论分析证明正交损失约束了伪鲁棒特征偏移对未见类的影响，给出测试误差保证。
- 📌 **结论**：大量实验表明，ADAPT 显著提升目标 prompt 在未见类别上的对抗鲁棒性，有效抑制现有对抗 prompt 微调的鲁棒过拟合现象；正交解耦设计附带测试误差保证，为该类防御提供了理论支撑，代码已开源。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While adversarial prompt tuning can enhance robustness of vision-language models efficiently, we find that existing methods aggravate robust generalization overfitting on seen classes, leading to a rapid degradation in performance against adversarial examples of unseen classes as training progresses. We empirically identify that this degradation stems from the tendency of the model to learn pseudo-robust features (i.e., non-generalizable shortcuts). To mitigate this, we propose ADAPT (Adversarial DisentAngled Prompt Tuning), a robust prompt tuning framework following the philosophy of "Learning What Not to Learn". Specifically, ADAPT uses a dual-prompt mechanism with a target prompt and a pool of decoy prompts. During training, the decoy prompts are guided to entrap diverse pseudo-robust features, while the target prompt is constrained to be orthogonal to the decoys in the embedding space to learn robust features. By disentangling the robust features from the pseudo-robust features, ADAPT effectively prevents robust generalization overfitting. We further provide an analysis showing that the orthogonal loss bounds the effect of shifts in pseudo-robust features on unseen classes, yielding a testing error guarantee. Empirically, extensive experiments demonstrate that ADAPT substantially improves the robustness of the target prompt on unseen classes. The code is available at https://github.com/cheny02/ADAPT-ACMMM2026.

</details>

### 43. MEC-Patch: Visible-Infrared Cross-Modal Adversarial Attack Driven by Intrinsic Material Emissivity Laws

📄 [arXiv](https://arxiv.org/abs/2608.05634) · 🐙 [Code](https://github.com/star0521/MEC-Patch)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`visible-infrared`、`material emissivity`、`Stefan-Boltzmann law`、`physical patch`

👤 **作者**：Lu Yang

- 🎯 **研究动机**：可见-红外多模态感知系统大量部署于自动驾驶等安全攸关领域，跨模态对抗鲁棒性评估愈发重要；现有方法或仅攻击单模态、难以绕过跨模态验证，或把红外建模简化为启发式像素强度分布，忽视环境温度波动对对抗稳定性的影响。
- 🔬 **研究方法**：提出物理规律驱动的 MEC-Patch：借助 Stefan-Boltzmann 定律建立材料发射率到热辐射的跨谱物理映射，并证明固定发射率分布下环境温度变化只引起一致全局缩放、保持相对发射率对比度；据此构造红外模态判别模式稳定的温度鲁棒扰动，并用物理约束 NSGA-II 协同优化双模态皆有效的材料分布 patch 参数，辅以动态对抗重采样（DAR）增强泛化。
- 📌 **结论**：实验表明 MEC-Patch 能有效欺骗 SOTA 多模态检测器，并在高保真、物理一致、多场景的仿真环境中保持高攻击鲁棒性，为可见-红外多模态感知系统的安全评估提供物理规律驱动的攻击基线，代码已开源。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the widespread deployment of visible-infrared multimodal perception systems in safety-critical domains such as autonomous driving, evaluating their cross-modal adversarial robustness has become increasingly vital. However, existing approaches exhibit significant limitations in approximating the intrinsic laws of imaging. Most studies either focus on a single modality, failing to bypass cross-modal verification, or simplify infrared modeling into heuristic pixel-intensity distributions, neglecting the impact of ambient temperature fluctuations on adversarial stability. To bridge this gap, this paper proposes MEC-Patch, a cross-modal adversarial attack framework driven by intrinsic physical laws. By leveraging the StefanBoltzmann Law, we establish a physics-grounded cross-spectral mapping that explicitly links material emissivity to thermal radiation. Building on this formulation, we reveal that, under a fixed emissivity distribution, ambient temperature variations induce consistent global scaling while preserving relative emissivity-induced contrast. We exploit this property to construct temperature-robust adversarial perturbations whose discriminative patterns remain stable in the infrared modality, thereby effectively reducing environmental sensitivity. Furthermore, we employ the physics-constrained NSGA-II algorithm to synergistically optimize the material-distribution-based patch parameters effective across both modalities, while enhancing generalization through a Dynamic Adversarial Resampling (DAR) strategy. Experimental results demonstrate that MEC-Patch effectively deceives state-of-the-art multimodal detectors and exhibits high robustness within high-fidelity, physically consistent, and multi-scene simulation environments. This research provides a physical-law-driven perspective for the security assessment of multimodal perception systems. The code is released at https://github.com/star0521/MEC-Patch.

</details>

### 44. MiuGS: Modality-Integrated Unified Gaussian Representation for Physical Adversarial Object Generation in 3D Detection

📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`3D Gaussian`、`multimodal 3D detection`、`physical adversarial object`、`autonomous driving`

👤 **作者**：Jin Hu、Tianyuan Zhang、Jiakai Wang、Xianglong Liu

- 🎯 **研究动机**：多模态 3D 检测是自动驾驶感知的基石，但其对抗鲁棒性认识不足；由于缺乏统一跨模态表示，现有攻击分别操纵图像与点云输入，导致物理可实现性有限、攻击效果次优。
- 🔬 **研究方法**：提出模态集成统一高斯表示框架 MiuGS：把对抗物体建模为共享的 3D 高斯表示，并实例化为一致的图像与点云观测，使两条传感流在表示层耦合而非独立优化，以解决跨模态融合不精确问题、保障物理可实现性；引入跨场景引导重平衡策略，缓解跨场景的模态引导漂移与数字到物理域差距，进一步强化攻击效果。
- 📌 **结论**：大量实验显示 MiuGS 攻击效果强劲：在 nuScenes 上平均 ASR 达 78.8%，在 CARLA 上达 44.3%，同时保持物理世界可实现性，验证统一 3D 高斯表示能显著强于分离式优化的对抗物体生成。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal 3D object detection is a cornerstone of autonomous driving perception, yet its adversarial robustness remains poorly understood. Due to the lack of a unified cross-modal representation, existing adversarial attacks manipulate image and point cloud inputs separately, leading to limited physical realizability and suboptimal attack effectiveness. To address this problem, we propose MiuGS, a modality-integrated unified Gaussian representation framework for generating 3D adversarial objects with strong attack effectiveness and physical-world potential. For physical realizability, we design a multimodal 3D Gaussian coordination strategy to address the imprecise cross-modal fusion issue. Specifically, MiuGS models the adversarial object as a shared 3D Gaussian representation and instantiates it into consistent image and point cloud observations, enabling the two sensing streams to be coupled at the representation level rather than optimized independently. To further strengthen attack effectiveness, we introduce a cross-scenario guidance rebalancing strategy to mitigate cross-modal guidance drift across scenarios and the digital-to-physical domain gap. Extensive experiments show that MiuGS achieves strong attack effectiveness, reaching an average ASR of 78.8% on nuScenes and 44.3% on CARLA, supporting the effectiveness and physical-world potential of the proposed unified representation.

</details>

### 45. QAQ: Query-based Attack for Query-based Object Detection

📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`query-based detector`、`object queries`、`malicious alignment`、`open-set detection`

👤 **作者**：Jun Huang

- 🎯 **研究动机**：Transformer 检测器以 object query 与集合预测革新检测范式，端到端化同时引入新对抗脆弱性；已有鲁棒性研究聚焦分类器或 CNN 检测器，把扰动特征提取当作主要目标，忽视了 query 迭代精炼解码这一 Transformer 特有机制。
- 🔬 **研究方法**：提出针对查询式检测器的查询式攻击 QAQ，核心是操纵输出 query 中的内容与位置信息：破坏内容表示与类别原型间的良性对齐以诱发漏检，构造恶意对齐以生成误检；保留位置表示实现位置可控的误检，使对抗结果符合先验分布。方法适用于单模态检测器与文本引导的多模态开集检测器，并可与现有扰动策略正交组合增强跨模型迁移性。
- 📌 **结论**：实验证实 QAQ 能稳定达成预期的定向对抗检测结果，既可诱发假阴性、也可注入位置可控的假阳性；方法跨单模态与开集多模态检测范式通用，且与既有策略正交组合可增强跨模型迁移性，揭示 query 解码环节独立于特征提取的新攻击面。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Transformer-based detectors have transformed the detection paradigm by leveraging the concept of object queries and set prediction. This end-to-end paradigm, while simplifying the detection pipeline, also introduces additional adversarial vulnerabilities. Prior robustness research has primarily focused on classifiers or CNN-based detectors, in which task heads directly operate on visual features to decode object categories or locations, making the perturbation of feature extraction the primary objective of adversarial attacks. In contrast, we propose query-based attacks specifically targeting the transformer architecture's query-based detectors, in which visual features merely serve as queryable items, with information being decoded through the iterative refinement of object queries. Our core idea is to manipulate the content and positional information embedded in the output queries. Specifically, we induce false negatives by disrupting benign alignments between content representations and class prototypes, and generate false positives by constructing malicious alignments. Furthermore, by preserving the positional representations, we enable location-controllable false positives, thereby getting adversarial results that conform to the prior distribution. The proposed method exhibits strong generality, applying to both unimodal detectors and the text-guided multimodal open-set detector. It exhibits excellent orthogonality and can be effectively combined with existing strategies to enhance cross-model transferability of perturbations. Experimental results confirm that our approach successfully achieves the intended adversarial detection results.

</details>

### 46. SAGE: Typographic Adversarial Defense for Large Vision-Language Models via Scene-Aware Guard Engine

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`typographic attack`、`semantic consistency`、`LVLM`、`self-reflection`

👤 **作者**：Dong Huang、Jiaxu Liu

- 🎯 **研究动机**：多模态排版对抗攻击把语义连贯但具误导性的文字嵌入图像，暴露大型视觉语言模型（LVLM）严重漏洞；现有防御依赖文本过滤或输入净化，难以捕捉跨模态不一致，且常破坏视觉完整性。
- 🔬 **研究方法**：提出场景感知守卫引擎 SAGE，把防御范式从对抗内容移除转向推理级语义控制：场景感知语义一致性检测器识别与查询下视觉语境矛盾的对抗文本；显式语义分离机制把误导性文本信号从视觉推理中隔离；自反思优化模块通过失败驱动的反馈自适应精炼防御策略。跨多样攻击方法、模型与基准评测。
- 📌 **结论**：实验表明 SAGE 显著提升对排版对抗攻击的防御成功率，同时在良性样本上保持有竞争力的正常性能，无需破坏视觉完整性即展现出跨攻击与跨模型的鲁棒性和泛化能力。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recently, multimodal typographic adversarial attacks have raised critical safety concerns about Large Vision-Language Models (LVLMs). By embedding semantically coherent but misleading text into images, these attacks reveal severe vulnerabilities of LVLMs. Existing defenses primarily rely on text filtering or input purification, which fail to capture cross-modal inconsistencies and often disrupt visual integrity. To this end, we propose SAGE (Scene-Aware Guard Engine), a novel defense framework that fundamentally shifts from adversarial content removal to reasoning-level semantic control. Specifically, we introduce a scene-aware semantic consistency detector that identifies adversarial text that contradicts visual context under the query. Subsequently, an explicit semantic separation mechanism is employed to isolate misleading textual signals from visual reasoning. Furthermore, we develop a self-reflective optimization module that adaptively refines defense strategies through failure-driven feedback. Extensive experiments across diverse attack methods, models, and benchmarks demonstrate that SAGE significantly improves defense success rates while maintaining competitive performance on benign samples, exhibiting outstanding robustness and generalizability.

</details>

### 47. So-Called Input Transformation-Based Attacks Are Actually Model Transformation-Based Attacks

📅 2026　🏷 ACM MM 2026

**关键词**：`analysis`、`transferability mechanism`、`model transformation`、`input transformation`、`gradient imbalance`

👤 **作者**：Qingyun Sun、Xiuli Bi、Jianxin Li

- 🎯 **研究动机**：输入变换攻击因简单有效而成为迁移攻击主流，但其起效机制始终不明，阻碍对抗研究进展；该工作探究机制并给出新解释：所谓输入变换攻击本质上是模型变换攻击——变换通过等价的模型变换训练对抗样本，使其泛化到更多模型。
- 🔬 **研究方法**：按变换是否出现在模型训练中将其分为域内与域外两类并分别考察作用，得到三项发现：域内变换可构造复合函数，以最少变换数量提升迁移性；域外变换可通过大量操作在域偏移与代理多样性间取得平衡从而提升迁移性；在攻击中引入 L2 归一化可缓解对抗样本生成的梯度失衡。据此提出融合两类变换与 L2 归一化的模型变换攻击 MoTA。
- 📌 **结论**：大量实验显示 MoTA 在 12 个模型上取得 95.4% 的平均攻击成功率；三项机制发现为输入变换攻击为何有效提供统一解释，将其重新定位为模型变换攻击，为迁移攻击设计与鲁棒性评测提供新视角。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Transfer-based adversarial attacks reveal models' vulnerabilities under unseen noise, serving to deceive models and assess their robustness. Among transfer-based adversarial attacks, input transformation-based attacks are popular due to their simplicity and effectiveness. However, their mechanisms remain unclear, hindering advancements in DNNs. Thus, we explore the mechanism and argue that the so-called input transformation-based attacks are actually model transformation-based attacks. The attacks utilize model transformations to train adversarial examples for a wide range of models, thereby generalizing them to more models. Furthermore, we classify transformations into 2 categories based on whether they are used during model training: in-domain model transformations and out-of-domain model transformations, and explore their roles respectively. Three findings are obtained: 1) In-domain model transformations can construct composite functions to boost adversarial transferability with a minimal number of transformations; 2) Out-of-domain transformations can also improve transferability via a large number of operations by balancing the trade-off between domain shift and surrogate model diversity; 3) Integrating L2-normalization into the attack mitigates gradient imbalance during adversarial example generation. We propose a Model Transformation-based Attack (MoTA), which fuses in-domain and out-of-domain model transformations and incorporates L2-normalization to address gradient imbalance. Extensive experiments demonstrate that MoTA achieves a mean attack success rate of 95.4% on 12 models.

</details>

### 48. SPA: Semantic Purification via Dimensional Alignment for Zero-Shot Adversarial Robustness

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`zero-shot robustness`、`CLIP`、`dimensional alignment`、`semantic purification`

👤 **作者**：Tai-Xiang Jiang

- 🎯 **研究动机**：CLIP 等 VLM 零样本能力强但对对抗扰动高度脆弱；现有零样本防御专注矫正文本引导注意力偏移，而实际存在相反失效模式——空间语义解耦：对抗图像可保持准确定位仍被误分类，攻击主要诱发嵌入维度语义漂移。
- 🔬 **研究方法**：进一步发现对齐完整嵌入空间适得其反：VLM 表征存在维度异质性，冗余尾维被不成比例腐蚀并主导对齐损失。提出语义净化 SPA：利用冻结教师按样本间方差排序维度、识别语义核心，仅对选定维度通过维度感知池化做教师锚定对齐，并在优化中抑制噪声尾维影响。在 16 个多样数据集、PGD-100、AutoAttack 与 C&W 强攻击下评测。
- 📌 **结论**：在 16 个数据集上，SPA 于 PGD-100、AutoAttack 与 C&W 强攻击下一致提升零样本对抗鲁棒性，且相对先前 SOTA 保持并时常提升干净准确率，表明语义核心维度对齐优于全空间对齐与空间注意力矫正路线。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models (VLMs) such as CLIP exhibit strong zero-shot generalization but remain highly vulnerable to adversarial perturbations. Recent zero-shot defenses largely attribute this vulnerability to text-guided attention shift and thus focus on spatial attention rectification. We reveal a contrasting failure mode, termed spatial-semantic decoupling: adversarial images can preserve accurate text-guided localization while still causing misclassification. This indicates that the attack primarily induces semantic drift in the embedding dimensions, which is largely invisible to spatial attention objectives. Moreover, we find that naively aligning the full embedding space is counterproductive due to dimensional heterogeneity in VLM representations, where redundant tail dimensions are disproportionately corrupted and dominate the alignment loss. To address these issues, we propose Semantic Purification via dimensional Alignment (SPA). SPA identifies a semantic core by ranking dimensions with inter-sample variance from a frozen teacher, and performs teacher-anchored alignment only on the selected dimensions via dimension-aware pooling, while suppressing the influence of noisy tail dimensions during optimization. Extensive experiments on 16 diverse datasets demonstrate that SPA consistently improves zero-shot adversarial robustness under strong attacks (PGD-100, AutoAttack, and C&W) while maintaining, and often improving, clean accuracy over prior state-of-the-art methods.

</details>

### 49. Stabilizing Multi-Attack Adversarial Training via Bandit Optimization

📄 [arXiv](https://arxiv.org/abs/2511.12265) · 🐙 [Code](https://github.com/1240148048/CAS)　📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`adversarial training`、`multi-armed bandit`、`attack sampling`、`robust generalization`

👤 **作者**：Zeming Wei、Meng Sun

- 🎯 **研究动机**：多样对抗扰动威胁下，多攻击对抗训练可提升 DNN 鲁棒性，但现有方法或每轮迭代计算全部攻击导致开销高昂，或对对抗样本随机采样引发过度参数漂移，稳定性与效率难以兼得。
- 🔬 **研究方法**：提出校准对抗采样 CAS，把多攻击对抗训练重构为多臂老虎机优化问题：将每种攻击视为一个臂，每次迭代仅采样单个攻击，通过探索与利用的动态平衡决定采样分布，既避免全攻击枚举的算力开销，又缓解攻击间优化冲突并控制过度参数漂移。
- 📌 **结论**：大量实验表明，CAS 以低计算成本取得更优的整体鲁棒性，验证把攻击选择建模为老虎机问题的有效性，为多攻击设定下的鲁棒泛化提供可扩展且有原则的路径，代码已开源。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep Neural Networks (DNNs) remain vulnerable to diverse adversarial perturbations, motivating multi-attack adversarial training (AT) for improved robustness. However, existing methods either incur prohibitive overhead by computing all attacks at each iteration, or rely on stochastic sampling over adversarial examples, which may cause excessive parameter drift. To address these issues, we propose Calibrated Adversarial Sampling (CAS), an efficient and stable framework that reformulates multi-attack AT as a multi-armed bandit optimization problem. By sampling a single attack per iteration that dynamically balances exploration and exploitation, CAS significantly reduces training cost while mitigating optimization conflicts across attacks and controlling excessive parameter drifts. Extensive experiments demonstrate that CAS achieves superior overall robustness at low computational cost, offering a scalable and principled approach to robust generalization against multi-attack settings. Our code is available at https://github.com/1240148048/CAS.

</details>

### 50. When Efficiency Becomes Fragility: Exploiting Dynamic Routing Vulnerabilities in Adaptive UAV Tracking

📄 [arXiv](https://arxiv.org/abs/2608.03902)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`dynamic routing`、`Lipschitz singularity`、`UAV tracking`、`gating manipulation`

👤 **作者**：Daizong Liu

- 🎯 **研究动机**：UAV 平台资源受限推动空中跟踪从追求精度转向精度-效率平衡，采用输入依赖动态路由的自适应 Transformer 跟踪器成为代表方案；该工作揭示其按需计算灵活性背后的结构缺陷：层跳跃决策边界处存在 Lipschitz 奇异性，局部 Lipschitz 常数无界。
- 🔬 **研究方法**：形式化刻画自适应跟踪架构中的 Lipschitz 奇异性，并首次将其识别为可直接利用的新攻击面：与攻击输出空间的传统对抗攻击不同，该面允许同时操纵模型语义表征与推理拓扑。据此提出对抗路径反转 API：生成不可感知扰动精确操纵门控决策，迫使推理进入被改变的计算路径，原始与反转路径间的严重不一致瓦解模型表征能力。
- 📌 **结论**：在多个 SOTA 自适应跟踪器上的实验表明，API 实现更优的扰动隐蔽性、更强的攻击效果与更快的推理速度，证明微小输入扰动可经门控放大为推理拓扑剧变，为动态跟踪网络的安全分析与鲁棒自适应架构设计敲响警钟。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Resource constraints on UAV platforms have driven a paradigm shift in aerial tracking, from pursuing performance toward balancing accuracy with efficiency. Adaptive Transformer Trackers, which leverage input-dependent dynamic routing architecture, have emerged as a representative solution to this challenge. However, we reveal that behind this computation-on-demand flexibility hides a critical structural flaw: the Lipschitz singularity of computational path decisions, which has an unbounded local Lipschitz constant at discrete layer-skipping decision boundaries. This mathematical discontinuity renders adaptive tracking networks inherently unstable: tiny input perturbations can be amplified at the gating modules, causing dramatic changes in the inference topology. We formally characterize this singularity in the context of adaptive tracking architectures and, for the first time, identify it as a directly exploitable new attack surface. This insight reveals a previously overlooked and highly vulnerable topological path space attack surface. Unlike traditional adversarial attacks that target the output space, this new attack surface allows for the simultaneous manipulation of both the models semantic representation and its inference topology. Based on this, we propose the Adversarial Path-Inversion (API) framework. API generates imperceptible perturbations to precisely manipulate the gating decisions, forcing the inference onto altered computational paths. The severe inconsistency between the original and the inverted paths dismantles the representation capability of the model. Extensive experiments on state-of-the-art adaptive trackers demonstrate that API achieves superior perturbation stealthiness, more effective attack, and faster inference speeds. This work opens a new dimension for the security analysis of dynamic tracking networks and provides a theoretical warning for constructing robust adaptive tracking architectures in the future.

</details>

### 51. When Surfaces Lie: Exploiting Wrinkle-Induced Attention Shift to Attack Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2603.27759)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`fabric wrinkle`、`non-rigid deformation`、`attention shift`、`cross-task transfer`

👤 **作者**：Chengyin Hu、…、Jiahuan Long

- 🎯 **研究动机**：VLM 在零样本分类、图像描述与 VQA 上表现出色，但对褶皱类非刚性形变的鲁棒性尚不清楚；衣物表面的三维褶皱提供了构造视觉合理扰动的物理原型，是未被考察的攻击维度。
- 🔬 **研究方法**：提出受三维布料褶皱启发的参数化结构攻击：构造多尺度褶皱场，耦合位移场变形与表面一致的外观调制，生成视觉合理的扰动；分层适应度函数在低维参数空间平衡攻击有效性与自然度，由遗传算法优化；在零样本分类代理上优化的扰动无需下游重优化即可迁移到生成式任务。
- 📌 **结论**：跨多个 SOTA VLM 的评估显示，该攻击造成显著的性能退化，并在图像描述与 VQA 任务上一致优于代表性基线；在零样本分类代理上优化的褶皱扰动可零成本迁移到生成任务，表明物理合理非刚性形变是 VLM 尚未设防的输入维度。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Models (VLMs) excel in zero-shot classification, image captioning, and visual question answering, yet their robustness to wrinkle-like non-rigid deformations remains unclear. We propose a parametric structural attack inspired by three-dimensional fabric wrinkles. The method constructs multi-scale wrinkle fields and couples displacement-field warping with surface-consistent appearance modulation to produce visually plausible perturbations. A hierarchical fitness function balances attack effectiveness and naturalness in a low-dimensional space optimized by a genetic algorithm. Perturbations optimized on a zero-shot classification proxy are transferred to generative tasks without downstream re-optimization. Across multiple state-of-the-art VLMs, our attack causes substantial performance degradation and consistently outperforms representative baselines in captioning and VQA.

</details>


### 隐私攻击与面部隐私保护

### 52. 3DGFA: 3D Gaze-consistent Face Anonymization

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`face anonymization`、`gaze consistency`、`identity protection`、`utility preservation`

👤 **作者**：Ting Yu

- 🎯 **研究动机**：人脸匿名化要求去除身份信息同时保留图像效用；现有方法在视角变化下难以保持注视方向，导致不同视角生成的匿名人脸之间注视行为不一致，影响匿名视频的可用性与自然度。
- 🔬 **研究方法**：提出首个强制跨视角 3D 注视一致性的人脸匿名化框架 3DGFA：引入世界坐标系多视角注视一致性目标，保持不同视角匿名脸的连贯 3D 注视行为；即插即用的身份-属性融合模块可插入任意图像编码器，融合匿名身份线索与原面部属性；混合匿名身份选择策略改善属性保持与输出多样性；两阶段训练方案赋予网络 3D 感知并控制训练开销。
- 📌 **结论**：跨多个数据集的实验显示，3DGFA 在隐私保护与效用保持之间取得领先平衡，且注视一致性、属性保持与输出多样性兼顾，对未见数据展现强鲁棒性与泛化能力，验证 3D 注视约束对人脸匿名化的必要性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Face anonymization aims to remove identity information while preserving the utility of face images. Despite recent progress in identity protection, existing methods often fail to preserve gaze under viewpoint changes, leading to inconsistent gaze behavior across anonymized faces. We propose 3DGFA, the first face anonymization framework that enforces cross-view 3D gaze consistency. Specifically, 3DGFA introduces a world-coordinate multi-view gaze consistency objective to preserve coherent 3D gaze behavior across anonymized faces generated from different viewpoints. To improve anonymization quality, we propose a plug-and-play identity-attribute fusion module that can be inserted into arbitrary image encoders to effectively integrate anonymous identity cues with original facial attributes. We further develop a hybrid anonymous identity selection strategy to improve attribute preservation and output diversity. We also introduce a two-stage training scheme that equips the network with 3D awareness while keeping the training cost manageable. Extensive experiments across multiple datasets demonstrate that 3DGFA achieves a superior balance between privacy protection and utility preservation, while showing strong robustness, generalization, and practical effectiveness.

</details>

### 53. Adv-Tokens: Target-Aware Residual Identity Token Injection for Transferable Facial Privacy Protection

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`facial privacy protection`、`identity token`、`diffusion`、`target-aware control`

👤 **作者**：Mingyue Li、Yinghao Zhang、Ruizhong Du、Chunfu Jia

- 🎯 **研究动机**：深度人脸验证模型的大规模部署带来严重隐私风险，催生对抗样本式防护；但现有方法很少在优化中利用显式目标身份先验，使用无条件或空文本条件的扩散防护缺乏目标感知控制，难以兼顾防护效力与视觉真实感。
- 🔬 **研究方法**：提出基于扩散的 Adv-Tokens：在 FaRL 空间建模源身份到目标身份的偏移，把该残差先验映射为连续身份 token，经可控软条件接口注入冻结的扩散模型，在反向扩散中实现定向身份控制；再从 DDPM 反演初始化出发在潜空间逐图精修，使防护在引入显式目标身份控制的同时保持自然外观与面部结构。
- 📌 **结论**：在公开数据集与商用识别 API 上的实验表明，Adv-Tokens 提供更优的黑盒人脸隐私防护，在防护效力与视觉保真度的权衡上优于现有方法，将显式目标身份先验成功引入扩散式人脸防护。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The massive adoption of deep facial verification models creates serious privacy risks, motivating adversarial-example-based protection for facial multimedia against unauthorized recognition and tracking. However, existing protection methods rarely exploit explicit target identity priors during optimization, and diffusion protection using unconditional or null-text conditioning offers limited target-aware control, making it challenging to achieve a desirable balance between protection efficacy and visual realism. To address these issues, we propose Adv-Tokens, a diffusion-based method for transferable facial privacy protection. Adv-Tokens models the source-to-target identity shift in FaRL space and maps this residual prior to continuous identity tokens. It then injects these tokens into a frozen diffusion model through a controllable soft-conditioning interface for targeted control during reverse diffusion and refines each image in latent space from a DDPM inversion initialization. This design introduces explicit target identity control into diffusion-based protection while preserving natural appearance and facial structure. Experiments on public datasets and commercial APIs demonstrate superior black-box protection and a better trade-off between protection efficacy and visual fidelity than prior methods.

</details>

### 54. Beyond Visual Evidence: Revealing and Mitigating Relational Privacy Leakage in Document MLLMs

📄 [arXiv](https://arxiv.org/abs/2608.12911) · 🐙 [Code](https://github.com/xubeining/Beyond-Visual-Evidence)　📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`relational unlearning`、`document MLLM`、`key information extraction`、`privacy leakage`

👤 **作者**：Changsheng Chen、Anirban Chakraborty

- 🎯 **研究动机**：领域专用 MLLM 的隐私脆弱性少有研究；处理身份证件的文档理解 MLLM 在关键信息抽取（KIE）中，当输入图像缺乏足够视觉证据时会依赖训练数据记忆的字段关系推断缺失内容，从而泄漏多个含敏感个人信息的关联字段。
- 🔬 **研究方法**：提出动态关系遗忘框架 DRUF，含关系解耦遗忘模块与动态集合更新机制，在保持 KIE 性能的同时抑制高风险字段对的泄漏；构建 DocPrivacyBench 基准，系统评估视觉证据缺失或极少条件下的隐私泄漏易感性；在该基准上评测 3 个 MLLM 与 6 种遗忘方法，兼顾遗忘后的泄漏抑制与效用保持。
- 📌 **结论**：结果显示视觉证据稀缺时（尤其在更噪的数据集上）现有 MLLM 一致出现隐私泄漏；DRUF 在保持稳健文档信息抽取性能的同时，把泄漏抑制较最强基线再提升 4.8 个百分点，代码与基准已开源。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While the privacy risks of multimodal large language models (MLLMs) have drawn significant attention, the unique vulnerabilities of domain-specific MLLMs remain largely underexplored. Focusing on document understanding MLLMs for identity document processing, this paper investigates the privacy issues inherent in Key Information Extraction (KIE) tasks. We reveal that when input images lack sufficient visual evidence, these models often rely on memorized field relations from training data to infer missing content, thereby leaking multiple correlated fields containing sensitive personal information. To mitigate this risk, we make three key contributions. First, we propose the Dynamic Relational Unlearning Framework (DRUF) which comprises a Relational Decoupling Unlearning (RDU) module and a dynamic set update mechanism. It suppresses the leakage of high-risk field pairs while preserving KIE performance. Second, we introduce DocPrivacyBench, a novel benchmark to systematically evaluate a model's susceptibility to privacy leakage under conditions of absent or minimal visual evidence. Third, we evaluate three MLLMs and six unlearning methods using this benchmark, assessing both post-unlearning leakage suppression and utility preservation. Our results demonstrate that existing MLLMs consistently exhibit privacy leakage when visual evidence is scarce, particularly on noisier datasets. In contrast, DRUF outperforms the strongest baseline by improving leakage suppression by 4.8 percentage points, effectively mitigating privacy risks while maintaining robust document information extraction performance. The code and benchmark are available at https://github.com/xubeining/Beyond-Visual-Evidence.

</details>

### 55. DiffDAP: Dual-Adversarial Identity-Guided Diffusion for Proactive Face Privacy Protection

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`face privacy`、`dual-adversarial`、`DDIM inversion`、`cross-model transferability`

👤 **作者**：Zhihua Xia、Zhangjie Fu

- 🎯 **研究动机**：人脸识别系统提升身份认证效率，同时带来身份冒用与非法轨迹追踪等隐私风险；对抗扰动与特征干预等主动防御难以同时兼顾视觉保真与跨模型可迁移性，限制了实际部署价值。
- 🔬 **研究方法**：提出扩散式双路对抗框架 DiffDAP，实现语义级身份匿名同时保持高保真视觉质量：生成对抗路以目标图像身份提示在 DDIM 反演与去噪过程中提供非对称对抗引导，促进身份解耦与重建；优化对抗路引入视觉感知与集成攻击损失，强化对抗修改并增强鲁棒性；支持把扰动限制在关键面部区域的局部隐私保护，保留非敏感内容。
- 📌 **结论**：跨多个基准的实验显示，DiffDAP 在视觉质量与跨模型攻击可迁移性两个维度均显著优于现有最优方法，且具备局部面部区域保护能力，验证双路对抗协同设计对人脸隐私防护的有效性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While Facial Recognition (FR) systems have significantly improved the efficiency of identity authentication, they concurrently pose severe privacy risks, including identity spoofing and illicit trajectory tracking. Although proactive defense mechanisms, such as adversarial perturbations and feature interventions, have been developed, existing approaches often struggle to reconcile visual fidelity with transferability, thereby limiting their real-world applicability. To address these challenges, we propose DiffDAP, a diffusion-based dual-path adversarial privacy framework that achieves semantic-level identity anonymization while preserving high-fidelity visual quality. DiffDAP synergizes a generative adversarial path with a loss-optimization adversarial path. Specifically, the generative path leverages identity prompts from target images to provide asymmetric adversarial guidance during DDIM inversion and denoising, facilitating robust identity decoupling and reconstruction. Concurrently, the optimization path incorporates visual perceptual and ensemble attack losses to fortify adversarial modifications and enhance robustness. Furthermore, DiffDAP supports localized privacy protection by confining perturbations to key facial regions, thus preserving non-sensitive content. Extensive experiments across multiple benchmarks demonstrate that our method significantly outperforms state-of-the-art alternatives in both visual quality and cross-model attack transferability.

</details>

### 56. Do Protective Perturbations Really Protect Portrait Privacy under Real-world Image Transformations?

📄 [arXiv](https://arxiv.org/abs/2604.23688)　📅 2026　🏷 ACM MM 2026

**关键词**：`analysis`、`protective perturbation`、`sequential transformation`、`purification`、`portrait privacy`

👤 **作者**：Zhijing Wu

- 🎯 **研究动机**：主动防御靠像素级保护扰动防止人像被未授权编辑或说话人脸生成，但真实传播中图像跨设备显示与转发必然经历缩放、色彩压缩等良性操作序列，直接改变像素值；现有研究只孤立考察单一变换，序列组合变换下防御是否仍有效尚不清楚。
- 🔬 **研究方法**：系统评估代表性主动防御方法——防 GAN 与扩散模型的未授权编辑、防未授权说话人脸生成，覆盖通用与人像专用两类——在序列图像变换下的有效性，结合定性与定量评估；并进一步提出免训练净化框架 TIP-RSR：组合序列图像变换与现成复原模型的区域级超分辨率，以低成本剥离保护扰动。
- 📌 **结论**：结果表明基于像素级扰动的防御难以抵御常见图像变换序列，存在现实防护失效风险；TIP-RSR 能高效净化保护扰动并保持图像保真，计算量远低于现有扩散式净化方法，凸显未来防护设计必须显式考虑序列真实变换的影响。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Proactive defense methods protect portrait images from unauthorized editing or talking face generation (TFG) by introducing pixel-level protective perturbations, and have already attracted increasing attention for privacy protection. In real-world use, images inevitably undergo sequences of benign operations during display across devices and subsequent dissemination, such as resizing and color compression, which directly alter pixel values. Existing studies and robustness defenses have mainly examined individual transformations in isolation, while the effects of sequentially composed transformations remain underexplored. To address this gap, we systematically evaluate whether representative proactive defenses against unauthorized image editing using GANs and diffusion models, as well as unauthorized talking face generation, remain effective under sequential image transformations. The evaluated methods span both general purpose and portrait specific defenses and are assessed through qualitative and quantitative evaluation. Experimental results indicate that defense methods based on pixel-level perturbations struggle to withstand sequences of common image transformations, posing a risk of defense failure in real-world applications. To further demonstrate that this vulnerability can be exploited at low cost, we introduced Transformation-Induced Purification via Region-wise Super-Resolution (TIP-RSR), a simple training-free purification framework that combines sequential image transformations with off-the-shelf restoration models. TIP-RSR can efficiently purify protective perturbations while preserving image fidelity and requiring substantially less computation than existing diffusion-based purification methods. These findings expose a practical vulnerability in current proactive portrait defenses and highlight the need to explicitly account for the effects of sequential real-world transformations when designing future protection mechanisms.

</details>

### 57. Imperceptible and Reversible Adversarial Examples against Vision-Language Models for Privacy Protection

📄 [arXiv](https://arxiv.org/abs/2607.10329)　📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`reversible adversarial example`、`diffusion inversion`、`cross-attention`、`visual fidelity`

👤 **作者**：Ziqi Zhou、…、Leo Zhang

- 🎯 **研究动机**：VLM 的多模态能力使用户暴露于文本式隐私攻击：攻击者爬取在线照片并查询 VLM 提取敏感属性；现有可逆对抗样本仅适用于纯视觉任务、在多模态设定失效，而针对 VLM 的对抗样本依赖高频噪声、严重损害视觉质量。
- 🔬 **研究方法**：提出 CloakDiff，首个面向 VLM 文本查询攻击的可逆高保真隐私防护框架：结合扩散对抗编辑与可逆网络，嵌入原图信息以支持无损恢复；同时扰动像素空间嵌入并操纵潜空间交叉注意力图，确保跨模型、跨 prompt 迁移性并保持全局视觉结构；设计 EDM 启发式采样，为对抗引导提供原则性扩散调度以进一步增强保真度。
- 📌 **结论**：在多个数据集与多个 VLM 上的实验表明，CloakDiff 在保持高视觉质量与可逆性的同时实现多模态隐私防护，防护效果可跨模型、跨 prompt 迁移，首次把可逆对抗样本扩展到多模态隐私防护场景。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

VisionLanguage Models (VLMs) offer powerful multi-modal ability but also expose users to text-based privacy attacks where adversaries crawl online photos and query VLMs to extract sensitive attributes. Existing reversible adversarial example (RAE) methods protect images in purely visual tasks but fail in multi-modal settings, and current adversarial examples on VLMs rely on high-frequency noise that severely degrades visual quality. We propose CloakDiff, the first framework for reversible, high-fidelity privacy protection against text-based query attacks in VLMs. CloakDiff produces imperceptible adversarial examples by combining diffusion-based adversarial editing with an invertible network that embeds the original image for lossless recovery. It perturbs both pixel-space embeddings and manipulates latent cross attention maps to ensure strong cross-model and cross-prompt transferability while preserving global visual structure. To further enhance fidelity, we design EDM-Heuristic Sampling, a principled diffusion schedule for adversarial guidance. Experiments on multiple datasets and VLMs demonstrate that CloakDiff delivers multi-modal privacy preservation with high visual quality and reversibility.

</details>

### 58. LBFTI: Layer-Based Facial Template Inversion for Identity-Preserving Fine-Grained Face Reconstruction

📄 [arXiv](https://arxiv.org/abs/2604.18358)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`template inversion`、`face reconstruction`、`layer decomposition`、`identity preservation`

👤 **作者**：Zhihua Xia、Peipeng Yu

- 🎯 **研究动机**：人脸识别系统普遍以符合数据最小化原则的人脸模板做身份认证，但模板逆推技术可从模板重建人脸图像，构成严重隐私泄漏风险；更强的细粒度身份保持重建意味着该风险更真实，需系统评估与防御应对。
- 🔬 **研究方法**：提出分层模板逆推方法 LBFTI，把人脸图像分解为前景层（眉、眼、鼻、口）、中景层（皮肤）与背景层，由专用生成器分别生成；采用三阶段训练：前景与中景层独立精细化生成、两层融合并二次注入模板以生成含背景的完整全景人脸、全部模块联合微调优化层间协调与身份一致性。
- 📌 **结论**：实验显示 LBFTI 的机器认证性能超越 SOTA 方法，TAR 提升 25.3%；重建人脸在人类感知上也与原身份更相似，经定量指标与问卷调研双重验证，表明分层生成与三阶段协调可同时提升机器可认证性与感知逼真度。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In face recognition systems, facial templates are widely adopted for identity authentication due to their compliance with the data minimization principle. However, facial template inversion technologies have posed a severe privacy leakage risk by enabling face reconstruction from templates. This paper proposes a Layer-Based Facial Template Inversion (LBFTI) method to reconstruct identity-preserving fine-grained face images. Our scheme decomposes face images into three layers: foreground layers (including eyebrows, eyes, nose, and mouth), midground layers (skin), and background layers (other parts). LBFTI leverages dedicated generators to produce these layers, adopting a rigorous three-stage training strategy: (1) independent refined generation of foreground and midground layers, (2) fusion of foreground and midground layers with template secondary injection to produce complete panoramic face images with background layers, and (3) joint fine-tuning of all modules to optimize inter-layer coordination and identity consistency. Experiments demonstrate that our LBFTI not only outperforms state-of-the-art methods in machine authentication performance, with a 25.3% improvement in TAR, but also achieves better similarity in human perception, as validated by both quantitative metrics and a questionnaire survey.

</details>

### 59. Noise as a Probe: Membership Inference Attacks on Diffusion Models Leveraging Initial Noise

📄 [arXiv](https://arxiv.org/abs/2601.21628) · 🐙 [Code](https://github.com/S3IC-Lab/NoiseMIA)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`membership inference`、`diffusion model`、`initial noise`、`residual semantics`

👤 **作者**：Puwei Lian、Yujun Cai、Songze Li

- 🎯 **研究动机**：扩散模型在小型私有数据集上微调后极可能泄露训练数据隐私，成员推断攻击（MIA）即判定样本是否属于训练集；现有针对扩散模型的 MIA 或需获取中间结果，或需在辅助数据上训练影子模型，假设条件较强。
- 🔬 **研究方法**：利用一个被忽视的漏洞：常用噪声调度无法完全消除图像语义信息，即使最大噪声步仍残留语义信号；实证证明微调扩散模型捕捉了初始噪声残留语义与原始图像间的隐藏关联；据此提出简单有效的攻击：向初始噪声注入语义信息，通过分析模型生成结果是否复现该语义来推断成员身份。
- 📌 **结论**：大量实验一致表明，注入语义的初始噪声能强烈揭示样本成员身份，无需中间结果或影子模型即可实施成员推断，凸显微调扩散模型噪声调度设计的隐私漏洞；攻击代码已开源可直接用于风险评估。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models have achieved remarkable progress in image generation, but their increasing deployment raises serious concerns about privacy and copyright. In particular, fine-tuned models are highly vulnerable, as they are often fine-tuned on small and private datasets. Membership inference attacks (MIAs) are used to assess privacy risks by determining whether a specific sample was part of a models training data. Existing MIAs against diffusion models either assume obtaining the intermediate results or require training the shadow model on auxiliary datasets. In this work, we utilized a critical yet overlooked vulnerability: the widely used noise schedules fail to fully eliminate semantic information in the images, resulting in residual semantic signals even at the maximum noise step. We empirically demonstrate that the fine-tuned diffusion model captures hidden correlations between the residual semantics in initial noise and the original images. Building on this insight, we propose a simple yet effective membership inference attack, which injects semantic information into the initial noise and infers membership by analyzing the models generation result. Extensive experiments demonstrate that the semantic initial noise can strongly reveal membership information, highlighting the vulnerability of diffusion models to MIAs. Code is available at https://github.com/S3IC-Lab/NoiseMIA.

</details>

### 60. Physics-Aware Generative Reconstruction Enables the Theft of Hidden Screen Content Solely from Light Leakage

📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`non-line-of-sight`、`light leakage`、`screen reconstruction`、`photon noise`

👤 **作者**：Jin Liu、…、Zhiwen Zheng

- 🎯 **研究动机**：被动非视距（NLOS）成像仅凭可见的漫反射面即可远程重建场景，可用于搜救、隐私监测与光信道测量攻击，但单帧重建脆弱：漫射面传输强空间变异并耦合远近几何，光子统计异方差易与场景内容混淆。
- 🔬 **研究方法**：提出 Radiance-Physics Diffusion（RaP-Diffusion），把漫射面视作几何与噪声编码的光圈：物理感知光子噪声合成过程 PAPS 以信噪比均衡校准泊松与高斯读出噪声，让模型学习而非臆造传感器噪声；液体辐射自适应核 ODE 去噪器 LiRa-AKODE 按局部传输伸缩感受野，在保持高斯共轭反向更新下保留边缘与长程结构。
- 📌 **结论**：在 CtM、StM、SmM、WtM 四数据集上单图重建的 PSNR、SSIM、LPIPS、FID 与多样性全面提升，适度视角变化下稳定；在四个室内屏幕数据集与 256×256 设定下，RTX 5090 上延迟 48.41 ms、参数量 133.55M、39.90G FLOPs，仅凭光泄漏窃屏已具实用效率。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Passive non-line-of-sight (NLOS) imaging promises remote awareness in safety-critical settings including search and rescue, privacy-preserving monitoring, autonomous robotics, and optical channel measurement attacks, where only a diffusive surface is visible. Yet single-shot reconstruction remains brittle: transport through the diffusive surface is strongly space-varying and couples near and far geometry, while photon statistics are heteroscedastic and easily confused with scene content. We present Radiance-Physics Diffusion (RaP-Diffusion), which treats the diffusive surface as a geometry- and noise-coded aperture. A Physics-Aware Photon Noise Synthesis forward process (PAPS) calibrates Poisson shot noise and Gaussian readout variability with signal-to-noise ratio (SNR) equalization, so the model learns sensor randomness rather than hallucinating it. A Liquid Radiance Adaptive-Kernel Ordinary Differential Equation denoiser (LiRa-AKODE) expands or contracts its receptive field according to local transport, preserving edges and long-range structure while staying within a Gaussian-conjugate reverse update. Across four datasets, CtM, StM, SmM and WtM, our single-image reconstructor improves PSNR, SSIM, LPIPS, FID, and diversity and remains stable under moderate viewpoint changes. On four indoor screen-content datasets and a 256256 setting, RaP-Diffusion achieves the above gains with 48.41 ms latency on an RTX 5090, with 133.55M parameters and 39.90G FLOPs, indicating practical efficiency within these operating conditions.

</details>

### 61. Plug-and-Play Identity: Generative Pseudo-Identities for Privacy-Preserving Face Recognition

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`privacy-preserving face recognition`、`pseudo-identity`、`diffusion generation`、`insider threat`

👤 **作者**：Hui Zhang、Shujie Cui、Xingbo Dong、Chenchen Tan、Zhe Jin

- 🎯 **研究动机**：内部攻击者可利用 LLM 与 RAG 驱动的分析经外部知识关联侵害人脸隐私；现有隐私保护人脸识别（PPFR）在匹配时仍向内部人员暴露原始人脸数据，或允许从受保护表征重建原身份，防不住内部背叛。
- 🔬 **研究方法**：提出生成式 PPFR 框架 PPID，把可学习新身份作为即插即用隐私部件用于现成人脸识别器，三阶段运作：从冻结识别器提取身份嵌入；轻量身份扰动器在几何约束下学习结构化伪身份；扩散生成器以该身份为条件合成匿名人脸。配合多目标优化约束嵌入几何、投影模块对齐条件空间以稳定生成并缩小真实-合成域差，匿名图像可直接识别且无需重训识别器。
- 📌 **结论**：实证评估、理论分析与真实 UAV 案例研究一致表明，PPID 在隐私、效率与识别精度三者间取得有利权衡，匿名化人脸可直接输入现成识别器完成匹配，能防范内部人员经外部知识关联的身份溯源。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Insider attackers increasingly leverage LLM- and RAG-driven analytics to compromise facial privacy through external knowledge linking, posing a growing threat to facial recognition systems. Current Privacy-Preserving Face Recognition (PPFR) methods remain vulnerable as they still expose raw facial data to insiders during matching, or allow for the reconstruction of original identities. To prevent such insider betrayals, we propose Plug-and-Play Identity (PPID), a generative PPFR framework that explores a learnable new identity as a privacy-preserving plug-in for off-the-shelf face recognizers. PPID operates in three stages: (i) identity embeddings are extracted from a frozen face recognizer; (ii) a lightweight identity perturbator learns structured pseudo-identities under geometric constraints; and (iii) a diffusion generator synthesizes anonymized face images conditioned on the learned identities. This formulation suppresses visual identity while preserving feature separability in a protected domain, enabling direct recognition on anonymized images without retraining face recognizer. To stabilize generation and reduce real–synthetic domain shift, PPID employs multi-objective optimization to constrain embedding geometry and a projection module to align conditioning spaces. Empirical evaluation, theoretical analysis, and a real-world UAV case study consistently indicate that PPID achieves a favorable trade-off among privacy, efficiency, and recognition accuracy.

</details>

### 62. Pri-UAVFace: Toward Minimal-MPC Few-Shot Adaptation for Privacy-Preserving UAV Face Recognition

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`UAV face recognition`、`secure multiparty computation`、`few-shot adaptation`、`parameter-efficient fine-tuning`

👤 **作者**：Yongqiang Yu、Zhankai Li、Jia Li、Xuehu Yan、Yuliang Lu

- 🎯 **研究动机**：安全监控与应急搜救等敏感场景中，UAV 人脸识别同时面临严重物理退化、标注样本稀缺与隐私合规约束；现有研究或做明文条件下的低质人脸识别，或做模板保护与安全推理，密文域目标域适配仍是空白。
- 🔬 **研究方法**：提出最小 MPC 适配框架 Pri-UAVFace：不把整个训练流程迁入安全多方计算，而是经物理仿真与一致性学习从公开明文数据学习通用身份表征与退化鲁棒性，仅把残余目标域适配限制在密文域，用 MPC 少样本适配加参数高效微调完成；设计加密友好判别头 MPCCosineHead 降低非线性算子带来的协议交互开销；在真实 DroneFace 数据集上评测。
- 📌 **结论**：5-shot 设定下取得 AUC 0.9943、TAR@FAR=10⁻³ 达 0.9308；方法与协议联合优化把 MPC 通信轮数从 864 降至 152、单步延迟缩短 75%，在隐私敏感的边缘多媒体感知中实现高效的 UAV 目标域适配。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In sensitive scenarios such as security surveillance and emergency search and rescue, Unmanned Aerial Vehicle (UAV) face recognition faces simultaneous challenges from severe physical degradation, scarcity of annotated samples, and privacy compliance constraints. Existing research mainly focuses on either low-quality face recognition under plaintext conditions or template protection and secure inference under privacy-preserving conditions. However, privacy-preserving target-domain adaptation for UAV face recognition remains underexplored. This paper proposes Pri-UAVFace, a Minimal Secure Multi-Party Computation (MPC) adaptation framework for privacy-preserving UAV face recognition. Rather than migrating the entire training workflow into MPC, it learns general identity representations and degradation robustness from public plaintext data, while confining residual target-domain adaptation to the ciphertext domain. To this end, it combines physical simulation and consistency learning for public-domain pre-learning, followed by MPC-based few-shot adaptation using Parameter-Efficient Fine-Tuning. Furthermore, an encryption-friendly discriminative head, named MPCCosineHead, is designed to reduce the protocol interaction overhead caused by non-linear operators. Evaluated on the real-world DroneFace dataset, Pri-UAVFace achieves an AUC of 0.9943 and a TAR@FAR=10^-3 of 0.9308 under a 5-shot setting. Through joint method and protocol optimization, it reduces the number of MPC communication rounds from 864 to 152 and shortens single-step latency by 75%. These results demonstrate effective UAV target-domain adaptation with minimal MPC utilization, providing a feasible path for privacy-sensitive edge multimedia sensing.

</details>

### 63. Safeguarding Facial Identity against Diffusion-based Face Swapping via Cascading Pathway Disruption

📄 [arXiv](https://arxiv.org/abs/2601.14738)　📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`face swapping`、`identity protection`、`cascading disruption`、`diffusion`

👤 **作者**：Xiangyang Luo

- 🎯 **研究动机**：扩散模型普及了人脸交换，威胁个人身份安全；从图像编辑攻击改造而来的现有主动防御在此场景失效，根源在于忽视了人脸交换系统的结构韧性与独特的静态条件引导机制。
- 🔬 **研究方法**：提出 VoidFace，把人脸交换视为耦合身份通路、在其关键瓶颈注入扰动引发级联破坏的系统性防御：先以定位破坏与身份抹除退化物理回归与语义嵌入，削弱对源脸的精确建模；再通过解耦注意力切断身份注入、破坏中间扩散特征阻止源身份重建；在潜流形上以感知自适应策略执行对抗搜索，平衡攻击强度与图像质量的不可感知性。
- 📌 **结论**：跨多种基于扩散的人脸交换模型的实验表明，VoidFace 的防交换防御效果全面超越现有防御，且生成的对抗人脸具备更优视觉质量，证明针对级联通路瓶颈的系统性扰动优于从图像编辑攻击直接迁移的防护策略。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid evolution of diffusion models has democratized face swapping but also raises concerns about privacy and identity security. Existing proactive defenses, often adapted from image editing attacks, prove ineffective in this context. We attribute this failure to an oversight of the structural resilience and the unique static conditional guidance mechanism inherent in face swapping systems. To address this, we propose VoidFace, a systemic defense method that views face swapping as a coupled identity pathway. By injecting perturbations at critical bottlenecks, VoidFace induces cascading disruption throughout the pipeline. Specifically, we first introduce localization disruption and identity erasure to degrade physical regression and semantic embeddings, thereby impairing the accurate modeling of the source face. We then intervene in the generative domain by decoupling attention mechanisms to sever identity injection, and corrupting intermediate diffusion features to prevent the reconstruction of source identity. To ensure visual imperceptibility, we perform adversarial search in the latent manifold, guided by a perceptual adaptive strategy to balance attack potency with image quality. Extensive experiments show that VoidFace outperforms existing defenses across various diffusion-based swapping models, while producing adversarial faces with superior visual quality.

</details>

### 64. TailorProtect: Meta-learning-based Tailored Text-enhanced Facial Privacy Protection

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`facial privacy`、`meta-learning`、`text enhancement`、`adversarial perturbation`

👤 **作者**：Mingyue Li、Fengchen Shi、Ruizhong Du、Luman Zhao、Chunfu Jia、Guanxiong Ha

- 🎯 **研究动机**：人脸识别在多媒体环境的普及加剧隐私泄漏风险，生成对抗扰动阻止未授权识别成为主流防护思路；但现有方法多为输入无关的通用范式，不为具体人脸定制，文本引导模块又独立运作、缺乏对图像语义的参照，导致图像质量与防护成功率难以兼顾。
- 🔬 **研究方法**：提出基于元学习的定制化文本增强防护框架 TailorProtect：元优化器依据输入人脸与文本描述微调防护过程，定制隐私扰动的生成；文本编码过程融入图像信息，使文本嵌入更针对当前输入，实现文本增强；与元优化器协同训练的像素空间精修器预测并施加细微调整，在高防护效力下恢复视觉质量。在 CelebA-HQ 与 FFHQ 数据集上评测，并测试商用 API。
- 📌 **结论**：与现有方法相比，TailorProtect 生成的防护图像在跨模型迁移性与视觉隐蔽性上更优，同时保持高效处理速度；在商用识别 API 上的真实场景评测进一步验证落地潜力，证明按脸定制优于通用扰动范式。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The widespread application of face recognition technology in multimedia environments has led to increasingly severe risks of personal privacy leakage. To address this challenge, privacy protection methods aimed at generating adversarial perturbations to prevent unauthorized identification have become a research focus. However, existing methods typically adopt an input-agnostic, general-purpose paradigm and fail to tailor protection strategies for specific faces. Meanwhile, text-guided modules often operate independently, lacking sufficient reference to the semantic information of the image. These limitations cause existing methods to struggle in balancing image quality and protection success rate. In response to this, this paper proposes a Meta-learning-based Tailored Text-enhanced Facial Privacy Protection framework. The core of the method lies in introducing a meta-optimizer that fine-tunes the protection process based on the input face and textual description, thereby tailoring the generation of privacy perturbations. The text encoding process incorporates information from the image, making the resulting text embeddings more targeted to the current input and achieving text enhancement. Furthermore, a pixel-space refiner, co-trained with the meta-optimizer, is introduced to predict and apply subtle adjustments, restoring visual quality while ensuring high privacy protection effectiveness. Experiments on the CelebA-HQ and FFHQ datasets show that, compared to existing methods, the privacy-preserving images generated by this framework achieve better performance in terms of transferability across different models and visual concealment, while maintaining efficient processing speed. We also conducted evaluations on commercial APIs in real-world scenarios, further demonstrating the practical application potential of the proposed method.

</details>


### 机器遗忘、概念删除与治理

### 65. Concept-Level Risk and Calibration for Governance in Diffusion Foundation Models

📅 2026　🏷 ACM MM 2026

**关键词**：`analysis`、`concept risk`、`diffusion governance`、`probabilistic audit`、`calibration`

👤 **作者**：Yushu Zhang、Yuming Fang

- 🎯 **研究动机**：扩散模型已成为多媒体生成核心范式，概念级控制从自然语言提示扩展到习得嵌入与干预管线，安全敏感、身份关联等隐私相关概念的治理难以统一评估；现有手段依赖启发式审计、对抗探测或任务特定擦除基准，难以跨模型、条件通道与部署条件系统比较。
- 🔬 **研究方法**：提出概念级概率审计与报告框架 CLRC：把治理相关的概念行为形式化为随机生成诱导的 Bernoulli 语义事件，定义 Concept Risk Operator 将「模型-通道」配置映射为结构化风险画像，支持跨提示接口、嵌入通道与模型比较；再结合样本级事后校准与配置级风险聚合，考察概率误差如何改变政策边界附近的阈值化决策。
- 📌 **结论**：在 SD1.5、SD2.1、SDXL 三种模型上观察到跨概念族、通道与协议的运营风险模式一致但不均匀；基于嵌入的访问与混淆提示暴露出标准提示评估常低估的风险；池化多协议校准器提升 held-out 概率可靠性，但不主张标准协议校准器可直接迁移。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models have become a core paradigm for multimedia generation, offering powerful concept-driven controllability for personalization, semantic editing, and selective unlearning. However, as semantic control extends beyond natural-language prompts to learned embeddings and intervention pipelines, the safety and governance of these systems become increasingly difficult to evaluate in a unified manner, especially for safety-sensitive, identity-linked, and other privacy-relevant concepts. Existing studies mainly rely on heuristic audits, adversarial probing, or task-specific erasure benchmarks, and therefore provide limited support for systematic comparison across models, conditioning channels, and deployment conditions. We present a concept-level probabilistic audit and reporting framework for diffusion models. We formalize governance-relevant concept behaviors as Bernoulli semantic events induced by stochastic generation, and define a Concept Risk Operator that maps model-channel configurations to structured risk profiles, enabling comparison across prompting interfaces, learned embedding channels, models, and recorded conditions. We apply sample-level post-hoc calibration and configuration-level risk aggregation, and show that probability error can change thresholded actions near policy boundaries. Experiments on SD1.5, SD2.1, and SDXL reveal consistent yet non-uniform operational risk patterns across concept families, channels, recorded conditions, and shifted protocols. In particular, embedding-based access and obfuscated prompts expose risks often understated by standard-prompt evaluation. A pooled multi-protocol calibrator improves held-out probability reliability, but we do not claim transfer from a standard-only calibrator. CLRC provides a common audit schema for probabilistic and decision-aware governance of multimedia generation systems.

</details>

### 66. EviGuard: Evidence-Guided Connector Intervention for Cross-Modal Safety Unlearning in Multimodal LLMs

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`multimodal connector`、`safety unlearning`、`risk subspace`、`over-refusal`

👤 **作者**：Jinduo Liu

- 🎯 **研究动机**：跨模态组合带来本质上多模态的安全风险：单独无害的图文在视觉表征进入语言模型并与文本上下文交互后可能变得有害；现有方法把连接器投影接口当黑盒，安全遗忘目标对连接器激活施加样本均匀压力，导致过度拒答且对未见威胁组合不够鲁棒。
- 🔬 **研究方法**：EviGuard 在多模态连接器（可控视觉到语言投影接口）处干预：RSF 提取显式视觉证据并经置信门与连接器激活融合，产生图像条件化风险分数；CLSU 用风险加权 SVD 估计连接器低秩风险子空间，抑制风险对齐分量并保留正交补；「图像-指令-响应」样本的响应级损失联合适配下游 LoRA；迭代反馈校正从残余难样本重估子空间。
- 📌 **结论**：在 LLaVA-1.5-7B 与 InternVL2.5-8B 上完成 SafeEraser、VLGuard 主实验与 SIUO 分布外评测；改善安全-效用权衡、降低过度拒答，对分布外跨模态威胁更鲁棒，支持多模态连接器作为安全遗忘的靶向干预点。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Cross-modal composition introduces a category of safety risk that is fundamentally multimodal: individually innocuous images and text can become harmful after visual representations enter the language model and interact with textual context, yet existing safety methods treat the connector's projection interface as a black box. Many fine-tuning approaches do not explicitly model representation-level risk, while several safety-unlearning objectives apply sample-uniform pressure across connector activations. This can increase over-refusal and limit robustness to unseen cross-modal threat compositions. We propose EviGuard, a framework that intervenes at the multimodal connector, a controllable visual-to-language projection interface, by estimating and suppressing a low-rank, risk-associated subspace of its visual activations. Risk-Structured Fusion (RSF) extracts explicit visual evidence and fuses it with connector activations through a learned confidence gate, producing image-conditioned risk scores rather than a uniform prior. Connector-Localized Selective Unlearning (CLSU) estimates the visual connector subspace via risk-weighted SVD, suppresses risk-aligned components, and preserves the orthogonal complement. Response-level losses on complete image--instruction--response examples jointly adapt downstream LoRA modules. Iterative Feedback Correction re-estimates the subspace from residual hard samples after each round, progressively tightening the risk boundary. We evaluate the main SafeEraser and VLGuard experiments on LLaVA-1.5-7B and InternVL2.5-8B. SIUO out-of-distribution evaluation is conducted on LLaVA-1.5-7B. Across these settings, EviGuard improves the overall safety--utility trade-off, reduces over-refusal, and shows stronger robustness to out-of-distribution cross-modal threats. These results support the multimodal connector as a targeted intervention point for multimodal safety unlearning.

</details>

### 67. Motion Concept Unlearning in Video Diffusion Models

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`motion concept erasure`、`video diffusion transformer`、`training-free`、`attention intervention`

👤 **作者**：Ping Liu

- 🎯 **研究动机**：T2V 扩散模型能逼真生成踢、刺、射击等动作，引发概念擦除的安全需求；概念擦除在 T2I 与 T2V 的静态概念上已被充分研究，动作概念擦除仍基本空白。
- 🔬 **研究方法**：对视频扩散 Transformer（DiT）系统研究动作概念擦除：因果干预显示文本条件注意力携带概念特定运动信息、支持选择性干预，而扰动时序位置编码会同时压制目标与非目标动态；权重级方法 ESD 直接适配到视频 DiT 仅带来温和且不均匀的抑制。据此导出概念特异性、空间选择性、时序自然性三项要求，分别对应 MUTE 的组件：每个去噪步经 token 中和提取概念方向，由方向内在结构导出空间门，并在 CFG 施加前从速度输出中扣除修正项；整体免训练、不改权重。
- 📌 **结论**：在 20 个动作概念上，MUTE 于 Wan2.1-T2V 上超越提示级、权重级与推理级代表性基线，同一公式可迁移到 CogVideoX，验证其跨不同 T2V 注意力架构的适用性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-video (T2V) diffusion models can generate realistic depictions of actions such as kicking, stabbing, and shooting, raising safety concerns that motivate targeted concept erasure. Although concept erasure has been extensively studied for static concepts in text-to-image and T2V models, erasing motion concepts remains largely unexplored. We present a systematic study of motion concept erasure in video Diffusion Transformers (DiTs). Through causal interventions, we show that text-conditioning attention carries concept-specific motion information and supports selective intervention, whereas perturbing temporal positional encoding suppresses both target and non-target dynamics. We further find that directly adapting ESD, a representative weight-level image erasure method, to a video DiT yields modest and uneven motion suppression: reducing its erasure training loss does not by itself remove the concept signal from the difference between the conditional and unconditional predictions, which classifier-free guidance (CFG) then scales at every denoising step. From these findings, we derive three requirements for motion concept erasure: concept specificity, spatial selectivity, and temporal naturalness. Each determines one component of MUTE (Motion concept Unlearning in Text-to-video gEneration): at each denoising step, MUTE extracts a concept direction through token neutralization, derives a spatial gate from the direction's intrinsic structure, and subtracts the resulting correction from the velocity output before CFG is applied. MUTE is training-free and requires no weight modification. Experiments on 20 motion concepts show that MUTE outperforms representative prompt-level, weight-level, and inference-time baselines on Wan2.1-T2V, and the same formulation transfers to CogVideoX, supporting its applicability across distinct T2V attention architectures.

</details>

### 68. Perceptual Alignment Reveals Vulnerability in Unlearned Diffusion Models

📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`machine unlearning`、`adversarial prompt`、`latent consistency`、`zeroth-order optimization`

👤 **作者**：Jing Wu、Trung Le、Dinh Phung、Jianfei Cai、Mehrtash Harandi

- 🎯 **研究动机**：机器遗忘方法用于从 T2I 扩散模型删除不良知识，但遗忘后的模型仍可被对抗提示重新生成被擦除内容；现有噪声预测优化攻击依赖「原模型与遗忘模型的噪声预测相似即可得到相似图像」的直觉前提，而该前提并不可靠。
- 🔬 **研究方法**：诊断出噪声级对齐不能完全保证图像级一致：迭代去噪过程中噪声预测与图像重建之间存在累积偏差；据此提出 latent consistency loss 并集成到现有优化攻击框架中弥合该差距。进一步在更严格设定下考察遗忘扩散模型的脆弱性，提出免梯度攻击者 ZOOAtk，借助零阶随机方差缩减在受限访问下完成有效提示优化。
- 📌 **结论**：实验表明 latent consistency 在不同设定下均增强攻击效果；ZOOAtk 在内部模型信息不可得的受限访问下依然有效，说明当前遗忘扩散模型即使不暴露内部信息也仍然脆弱。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning methods have been proposed to delete undesired knowledge from Text-to-Image diffusion models (DMs), yet, unlearned models remain vulnerable to adversarial prompts that regenerate erased content. While existing noise-prediction optimization attacks have shown promising results, they generally rely on the intuitive premise that similar noise predictions between the original and unlearned models will naturally yield similar generated images. In this paper, we observe that this noise-level alignment may not fully guarantee image-level consistency, primarily due to cumulative deviations between noise prediction and image reconstruction during the iterative denoising process. Building on this diagnosis, we introduce a latent consistency loss and integrate it into existing optimization-based attack frameworks to bridge this gap. We further examine the vulnerability of unlearned DMs under more strict settings, and propose a gradient-free attacker (ZOOAtk) via zeroth-order stochastic variance reduction to enable effective prompt optimization under limited access. Experimental results demonstrate that latent consistency strengthens attacks in different settings, while ZOOAtk remains effective under restricted access, indicating that current unlearned DMs remain vulnerable even when internal model information is unavailable.

</details>

### 69. Representation Steering via Null-space Alignment for Concept Unlearning in Diffusion Models

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`concept unlearning`、`representation steering`、`null-space constraint`、`red-teaming robustness`

👤 **作者**：Yanbin Hao、Shuo Wang、Yongliang Wu、Xinyu Ye、Xingyu Zhu、Jiaheng Zhang

- 🎯 **研究动机**：T2I 扩散模型可能生成不安全、版权与冒犯性内容；新兴的表征引导类概念遗忘方法无须重训、效率高，但其无约束的方向更新会不加区分地改变模型行为，常导致过度抑制、跨概念干扰与非目标生成质量退化。
- 🔬 **研究方法**：RESET 在零空间约束下做表征引导：由良性概念表征构造保留子空间，把参数更新限制在其正交零空间内，避免干扰保留概念；并在该受限空间内推导闭式解，选择性抑制不安全概念同时保持一般生成能力。
- 📌 **结论**：在物体、风格与身份三类基准上，RESET 一致优于 SOTA 方法，实现更精确的概念移除、对 red-teaming 攻击更强的鲁棒性，以及更好的无关内容保真保持。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid deployment of Text-to-Image (T2I) diffusion models has raised urgent concerns about the generation of unsafe, copyrighted, and offensive content. Recently, steering-based concept unlearning methods have emerged as an efficient alternative to retraining, suppressing undesired concepts by injecting learned direction vectors into model representations. Despite their efficiency, these approaches rely on unconstrained directional updates that indiscriminately alter model behavior, often leading to over-suppression, cross-concept interference, and degradation of non-target generation quality. To address this issue, we propose RESET, a theoretically grounded framework for Representation steering via null-Space alignment in diffusion models. Moving beyond unconstrained heuristic steering, we steer representations under a null-space constraint to avoid interference with retained concepts. Specifically, we construct a preservation subspace induced by benign concept representations and restrict parameter updates to its orthogonal null space, thereby preventing interference with retained concepts. Within this constrained space, we derive a closed-form solution that selectively suppresses unsafe concepts while preserving general generation capability. Extensive experiments across object, style and identity benchmarks show that RESET consistently outperforms state-of-the-art methods, achieving more precise concept removal, improved robustness against red-teaming attacks, and superior preservation of unrelated content fidelity.

</details>

### 70. Semantic Steering for Controllable Generation: Tuning-Free Concept Erasure in Multimodal Diffusion Transformers

📄 [arXiv](https://arxiv.org/abs/2608.12829)　📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`concept erasure`、`multimodal diffusion transformer`、`steering vector`、`tuning-free`

👤 **作者**：Qiao Li、Xiaomeng Fu、Qipeng Wang、Jizhong Han

- 🎯 **研究动机**：多模态扩散 Transformer（MM-DiT）生成能力强大，可能产生敏感或不当内容；现有概念擦除方法多需修改模型参数、绑定特定架构，难以用于已部署的大模型；若干免训练方法又因知识深嵌、语义空间宽泛、文本编码器依赖上下文而难以迁移到大规模 MM-DiT。
- 🔬 **研究方法**：对 MM-DiT 各块生成角色的深入分析发现，文本条件语义表征在中间块最为显著；据此从中间块提取待擦除概念与安全替代概念的表征，用二者之差构造转向向量，并将该向量注入连续的早期与中间块；方法仅作用于稀疏的文本分支 token，并利用整流流的直线采样轨迹，实现零训练、近零开销的概念擦除。
- 📌 **结论**：跨多个 MM-DiT 模型的实验表明该方法在擦除多样概念上达到 SOTA，可对最终输出实现有效控制，并对对抗攻击保持鲁棒。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Diffusion Transformers (MM-DiTs) have demonstrated remarkable text-to-image generation performance, surpassing traditional U-Net-based diffusion models. Nevertheless, their powerful generative capabilities also raise significant safety concerns, as they may generate sensitive or inappropriate content. While existing concept erasure methods aim to mitigate such risks, most require modifying model parameters, which are often architecture-specific and impractical for deployed larger models. Several tuning-free approaches face challenges when applied to advanced large-scale MM-DiTs due to their deeply embedded knowledge, broad semantic space, and context-dependent text encoders. To address these challenges, we propose to erase concepts by directly manipulating the model's internal representations. Our key insight, derived from an in?depth analysis of MM?DiTs block?wise generative roles, is that text-conditioned semantic representations are most salient in the middle blocks of MM-DiTs. Based on this, we extract representations of an unwanted concept and a desirable safe one from the middle block, construct a steering vector from their difference, and inject this single vector into consecutive early and middle blocks. By operating exclusively on the sparse text?branch tokens and leveraging the straight sampling trajectory of rectified flow, our method achieves effective concept erasure with negligible overhead and without any training. Extensive experiments across MM-DiT models demonstrate that our method achieves state-of-the-art performance in erasing diverse concepts, enables effective control over the final output, and remains robust to adversarial attacks.

</details>

### 71. TRU: Targeted Reverse Update for Efficient Multimodal Recommendation Unlearning

📄 [arXiv](https://arxiv.org/abs/2604.02183)　📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`recommendation unlearning`、`multimodal`、`reverse update`、`membership inference`

👤 **作者**：Zeyu Ma、Yang Yang

- 🎯 **研究动机**：多模态推荐系统联合建模交互图与物品内容，用户数据一旦习得便难以移除；近似遗忘比全量重训高效，但现有方法对组件均匀施加反向更新，而删除影响在排序、模态与模块间分布不均，产生目标物品残留、模态失衡、模块敏感三大瓶颈。
- 🔬 **研究方法**：TRU 是即插即用的 MRS 遗忘框架，跨模型层级做三项协同干预：ranking fusion gate 抑制排序中目标物品的残留影响；branch-wise modality scaling 保护保留的多模态表征；capacity-aware parameter-group selection 把反向更新定位到删除敏感模块。
- 📌 **结论**：在两种骨干、三个数据集、三种遗忘 regime 下，多数设定的 retain-forget 权衡优于 MMRecUn；安全审计在两种审计设定下报告近似方法中最低的 MIA BalAcc 并并列最低 ASR，且更早收敛到有利的 retain-forget 区域。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal recommendation systems (MRS) jointly model user-item interaction graphs and rich item content, but this tight coupling makes user data difficult to remove once learned. Approximate machine unlearning offers an efficient alternative to full retraining, yet current MRS unlearning applies reverse updates largely uniformly across model components. We show that this uniform treatment is misaligned with modern MRS: deleted-data influence is distributed unevenly across ranking behavior, modality branches, and model modules. This non-uniformity gives rise to three bottlenecks in MRS unlearning: target-item persistence in the collaborative graph, modality imbalance across feature branches, and concentrated module-level sensitivity in the parameter space. To address this mismatch, we propose targeted reverse update (TRU), a plug-and-play unlearning framework for MRS. Instead of applying a uniform global reversal, TRU performs three coordinated interventions across the model hierarchy: a ranking fusion gate to suppress residual target-item influence in ranking, branch-wise modality scaling to preserve retained multimodal representations, and capacity-aware parameter-group selection to localize reverse updates to deletion-sensitive modules. Across two backbones, three datasets, and three unlearning regimes, TRU achieves a stronger retain--forget trade-off than MMRecUn in most settings. In two challenging user-level cases, TRU also attains favorable operating points among all evaluated baselines. Security audits report the lowest MIA BalAcc and a tie for the lowest ASR among approximate methods in both audited settings, while wall-clock trajectories show earlier convergence to favorable retain--forget regions.

</details>

### 72. Tune Less, Erase Better: Angle-Guided Multi-Granularity Unlearning in Continual Learning

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`continual unlearning`、`multi-granularity`、`decision boundary`、`right to be forgotten`

👤 **作者**：Xiangkun Wang、Tianrui Li

- 🎯 **研究动机**：持续学习使单一模型能在数据流上增量学习而不遗忘旧知识，带遗忘的持续学习（CLU）进一步落实「被遗忘权」、支持数据退出；但现有 CLU 方法对多粒度遗忘对象（样本/类/任务）支持受限、全模型微调耗时、依赖昂贵额外信息存储，阻碍实际应用。
- 🔬 **研究方法**：CLgeU 遵循「少微调、好遗忘」思路，在模型输出空间引入轻量遗忘模块，通过定向移动目标数据决策边界擦除记忆：从分解后的 logits 选择性优化 target angle factor，仅扰动对未学习数据的分类对齐而其他数据不受影响，设计上无需重放非目标数据或历史知识。
- 📌 **结论**：公开基准上实现有效且高效的遗忘，与正则化、重放、优化三类 CL 策略广泛兼容，且不损害保留任务与未来任务性能。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Continual learning (CL) enables a single model to incrementally learn from data streams without forgetting previously acquired knowledge. Recently, Continual Learning with Unlearning (CLU) has emerged as a promising paradigm to enforce the ``right to be forgotten'', allowing data opt-out in CL scenarios. However, existing CLU methods face three major limitations during unlearning: (1) restricted support for multi-granularity unlearning objects (sample, class, task), (2) time-consuming full model fine-tuning, and (3) reliance on costly storage of extra information, which hinder their real-world applicability. To address these issues, we propose CLgeU, a novel CLU framework that fine-tunes less but unlearns better. Specifically, a lightweight unlearning module is introduced into the model's output space to erase memory by directionally shifting the decision boundaries of target data. This is achieved by selectively optimizing the target angle factor derived from the decomposed logits, perturbing the model's classification alignment on unlearned data while keeping others unaffected. Such a design eliminates the need to replay non-target data or historical knowledge. Experiments on public benchmarks show that CLgeU achieves effective and efficient unlearning with broad compatibility across regularization-, replay-, and optimization-based CL strategies, without compromising performance on retained and future tasks.

</details>

### 73. UniForget: Self-Distilled Concept Unlearning in Unified Multimodal Models

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`concept unlearning`、`unified multimodal model`、`self-distillation`、`NSFW`

👤 **作者**：C. L. Philip Chen

- 🎯 **研究动机**：统一多模态模型（UMM）在共享表征空间内集成理解与生成，导致 NSFW 内容、版权身份等不良概念同时编码进两条通路；现有遗忘方法主要为通路隔离的模型设计，难以一致地删除 UMM 中跨理解与生成通路纠缠的概念。
- 🔬 **研究方法**：UniForget 是首个面向统一多模态模型的概念遗忘框架：将概念遗忘形式化为统一的自蒸馏过程，在共享概念层级下从模型自身内化知识导出概念对齐的多模态监督，使两条通路同步遗忘，同时达成擦除、重定向与保留三个互补目标；并构建首个 UMM 概念遗忘统一基准。
- 📌 **结论**：大量实验表明 UniForget 能跨理解与生成两条通路有效移除目标概念，同时保持整体模型效用，验证自蒸馏范式在统一模型上的可行性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unified multimodal models (UMMs) integrate understanding and generation within a shared representation space. While this unified modeling enables comprehensive multimodal capabilities, it also causes undesirable concepts, such as not-safe-for-work (NSFW) content and copyrighted identities, to be encoded across both pathways. Existing unlearning methods are primarily designed for pathway-isolated models, and thus are insufficient to consistently remove concepts entangled across the understanding and generation pathways in UMMs. To address this challenge, we propose UniForget, the first concept unlearning framework for unified multimodal models. UniForget formulates concept unlearning as a unified self-distillation process, in which concept-aligned multimodal supervision is derived from internalized knowledge of the model under a shared concept hierarchy. This supervision enables consistent unlearning across both understanding and generation pathways, achieving the complementary objectives of erasure, redirection, and retention. Furthermore, we introduce a unified benchmark for concept unlearning in UMMs. Extensive experiments show that UniForget effectively removes targeted concepts across both pathways while preserving overall model utility.

</details>


### 模型资产保护、水印与版权

### 74. AFSD: A Proactive Defense Against Training-Free Style Transfer in Diffusion Models

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`style protection`、`adversarial perturbation`、`training-free style transfer`、`artwork copyright`

👤 **作者**：Quan Wang、Zeyu Dong、Tong Qiao

- 🎯 **研究动机**：扩散模型推动风格迁移与 AI 艺术创作，也加剧了对原创作品未授权风格模仿的风险；Mist、Glaze 等保护方法通过在图像中嵌入对抗扰动破坏 DreamBooth、LoRA 等微调过程，但面对 StyleID 这类免训练扩散风格迁移方法时明显失效。
- 🔬 **研究方法**：AFSD 是针对免训练风格迁移的主动防御框架：在高频区域引入自适应扰动，并在潜表征与自注意力特征两个层级施加约束，从信息传播层面破坏风格迁移所需的风格信息，同时保持图像感知质量。
- 📌 **结论**：大量实验表明 AFSD 显著削弱免训练扩散风格迁移方法的性能，为艺术作品版权保护提供了区别于抗微调扰动的有效主动防御路径。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In recent years, Diffusion Models (DMs) have achieved remarkable success in style transfer and AI-driven artistic creation. However, they have also exacerbated the risk of unauthorized style imitation of original artworks. Existing protection methods, such as Mist and Glaze, mitigate infringement risks by embedding adversarial perturbations into images to disrupt the fine-tuning process, especially for prevalent techniques like DreamBooth and LoRA. Nevertheless, these denfenses exhibit clear limitations when facing training-free diffusion-based style transfer methods, such as StyleID. To address this challenge, we propose Anti-Training-Free Style Transfer in Diffusion Models(AFSD), an active defense framework tailored for training-free style transfer. Specifically, AFSD introduces adaptive perturbations in high-frequency regions and imposes constraints at both the latent representation and self-attention feature levels, thereby effectively disrupting the propagation of style information while preserving perceptual quality. Extensive experiments demonstrate that AFSD significantly degrades the performance of training-free diffusion-based style transfer methods. Our work provides an effective proactive defense strategy for protecting the copyright of artistic works.

</details>

### 75. ALIEN: Analytic Latent Watermarking for Controllable Generation

📄 [arXiv](https://arxiv.org/abs/2602.06101) · 🐙 [Code](https://github.com/REPO-EXP/ALIEN.git)　📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`latent watermarking`、`controllable generation`、`analytic embedding`、`IP protection`

👤 **作者**：Jing Yu、Liehuang Zhu

- 🎯 **研究动机**：潜在扩散模型普及使水印成为知识产权保护的关键技术，但现有方法依赖计算密集的启发式优化，训练开销高且易陷入局部最优。
- 🔬 **研究方法**：ALIEN 提出首个时间相关调制系数的解析推导，直接引导逆 SDE 概率流嵌入水印残差，无须扩散反演；并支持两种部署模式灵活切换：ALIEN-Q 在受限窗口内注入水印，作为严格保内容范式保证与无水印图像零语义偏差并维持基线鲁棒性；ALIEN-R 利用完整注入范围实现高韧性语义水印，在保证视觉质量的同时抵抗对抗扰动。
- 📌 **结论**：ALIEN-Q 在多个保真度指标上比现有方法提升 33.1%；ALIEN-R 在 15 种不同条件下对复杂生成与稳定性威胁的鲁棒性提升 14.0%，达到 SOTA 抵抗水平。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid advancement of Latent Diffusion Models (LDMs), watermarking has emerged as a crucial technique for intellectual property protection. However, existing methods rely on computationally intensive heuristic optimizationleading to high training overhead and local optima. To address these issues, we propose an Analytical Watermarking for Controllable Generation (ALIEN). Unlike optimization-based approaches, ALIEN develops the first analytical derivation of a time-dependent modulation coefficient, directly guiding the reverse SDE probability flow to embed watermark residuals without diffusion inversion. To accommodate diverse real-world deployment requirements, ALIEN enables a flexible transition between high-fidelity pixel alignment (ALIEN-Q) and high-resilience semantic embedding (ALIEN-R). ALIEN-Q functions as a strict content-preserving paradigm by injecting the watermark within a restricted window, ensuring zero semantic deviation from unwatermarked images while maintaining baseline robustness. ALIEN-R acts as a highly resilient semantic watermark by utilizing the full injection range. While still ensuring great visual quality, it achieves state-of-the-art resistance against adversarial perturbations. Extensive experiments demonstrate the superiority of both modes in their respective domains. ALIEN-Q outperforms existing methods by 33.1% across multiple fidelity metrics, while ALIEN-R delivers a 14.0% improvement in robustness against complex generative and stability threats across 15 distinct conditions. Code is available at https://github.com/REPO-EXP/ALIEN.git.

</details>

### 76. Beyond Distortion Robustness: Rethinking Severe Cropping as Erasure-Resilient Message Embedding

📄 [arXiv](https://arxiv.org/abs/2608.18567) · 🐙 [Code](https://github.com/ZPZhangLab/CREST-ACMMM2026)　📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`message embedding`、`cropping robustness`、`LT fountain coding`、`erasure resilience`

👤 **作者**：Bo Pang、Weibin Kong、Juntu Dong、Minghan Li、Zhongping Zhang

- 🎯 **研究动机**：鲁棒信息嵌入对版权保护与内容溯源至关重要；现有方法基本在「失真鲁棒」范式下开发——嵌入信号仍存在于图像中，只是被噪声、模糊或压缩退化；而严重裁剪直接移除部分载体本身，造成载荷部分消失而非信号受损，是本质上不同的挑战。
- 🔬 **研究方法**：CREST 从「擦除韧性」视角重新审视该问题：将紧凑 QR 消息经 LT 喷泉码扩展为冗余空间载荷，与裁剪感知嵌入及片段恢复相结合，构成严重裁剪鲁棒嵌入的概念验证框架。
- 📌 **结论**：在 COCO、DIV2K、VOC2012 上，面积保留率 0.7 的混合失真下，TRA 从最强基线的 18.52% 提升到 68.45%，EMR 从 13.88% 降至 4.21%；COCO2017 上仅保留 30-50% 图像面积时仍取得 48.55-65.12% 的 TRA，而所有对比基线均无法恢复消息。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Robust message embedding in images is important for multimedia security applications such as copyright protection and content tracing. Existing methods are largely developed under a distortion robustness paradigm, where the embedded signal remains spatially present but is degraded by noise, blur, or compression. Severe cropping poses a fundamentally different challenge because it removes part of the carrier itself, causing partial payload disappearance rather than mere signal corruption. In this paper, we revisit robust message embedding from an erasure-resilience perspective and present CREST, a proof-of-concept framework for severe-cropping-robust embedding. CREST combines coding-theoretic redundancy with neural embedding and recovery by expanding a compact QR message into a redundant spatial payload via LT fountain coding and coupling it with cropping-aware embedding and fragment recovery. Experiments on COCO, DIV2K, and VOC2012 show that CREST improves recovery under severe cropping while maintaining competitive visual quality. Under mixed distortions with an area retention ratio of 0.7, CREST improves TRA from 18.52% to 68.45% and reduces EMR from 13.88% to 4.21% over the strongest baseline. On COCO2017, CREST still achieves 48.55--65.12% TRA when only 30--50% of the image area is retained, whereas all compared baselines fail to recover the messageCode: https://github.com/ZPZhangLab/CREST-ACMMM2026. These results suggest that severe cropping is better understood as an erasure problem rather than a conventional distortion problem, motivating the joint design of neural embedding and coding-based recovery.

</details>

### 77. CheckMark: Robust Unbiased Multi-Bit Watermarking via CRC-Enhanced Candidate Decoding

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`LLM watermarking`、`multi-bit`、`statistical unbiasedness`、`CRC decoding`

👤 **作者**：Yaofei Wang、Xinru Wang、Jinyang Guo、Yuhang Cai、Yufeng Zheng、Donghui Hu

- 🎯 **研究动机**：LLM 的大规模部署需要鲁棒的溯源验证来遏制潜在滥用；多比特水印可嵌入详细元数据，但现有方案面临根本权衡：要么为保证鲁棒性牺牲文本质量，要么在保持统计无偏时抽取准确率低下。
- 🔬 **研究方法**：CheckMark 利用 Exponential Minimum Sampling（EMS）保证水印分布与原始模型输出统计一致，从而保持生成质量；关键创新是把循环冗余校验（CRC）机制与层级候选池解码策略结合，在最小化冗余的同时显著增强对文本编辑的鲁棒性。
- 📌 **结论**：大量实验表明 CheckMark 在抽取准确率与鲁棒性上均优于 SOTA 基线，同时保持零统计失真，兼顾无偏性、质量与鲁棒性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The ubiquitous deployment of Large Language Models (LLMs) necessitates robust provenance verification to mitigate potential misuse. While multi-bit watermarking enables embedding detailed metadata, existing schemes face a fundamental trade-off: they either compromise text quality to ensure robustness or suffer from low extraction accuracy when maintaining statistical unbiasedness. To address this, we propose CheckMark, a novel unbiased watermarking framework. By leveraging Exponential Minimum Sampling (EMS), CheckMark ensures the watermarked distribution remains statistically identical to the original model output, thereby preserving generation quality. A key innovation is the integration of a Cyclic Redundancy Check (CRC) mechanism with a hierarchical Candidate Pool decoding strategy. This synergy significantly enhances robustness against text edits while minimizing redundancy. Extensive experiments demonstrate that CheckMark achieves superior extraction accuracy and robustness compared to state-of-the-art baselines, while maintaining zero statistical distortion.

</details>

### 78. Did You Steal My Shot? Pioneering Camera Motion Plagiarism Detection in Generative Videos

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`camera motion`、`video plagiarism`、`vorticity cue`、`benchmark`

👤 **作者**：Chengguo Zhang、Ping Ping

- 🎯 **研究动机**：镜头运动体现导演意图且需要专业设备，是高价值知识产权；生成式视频模型仅凭简单提示即可模仿此类高价值运镜，而现有相似性检测方法主要作用于视觉内容、难以捕捉深层运动相似性——其训练数据将运镜与视觉内容纠缠，且传统光流不足以表示复杂运镜。
- 🔬 **研究方法**：构建首个镜头运动分析基准，包含 11 种运动风格的数据集与评测协议；提出以流体动力学中的涡量（vorticity）线索增强光流的运动表征，更好地捕捉复杂运动模式，并在此基础上训练运镜抄袭检测器。
- 📌 **结论**：检测器在抄袭检测上比最强基线提升 3.02，且对生成式视频依然有效，将版权保护从静态内容扩展到动态镜头运动。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Camera motion often reflects directorial intent and requires professional equipment, making it a high value form of intellectual property. However, generative video models can imitate such high value camera motions with simple prompts, while existing similarity detection methods mainly operate on visual content and fail to capture deeper motion similarity. This is mainly because their training data entangles camera motion with visual content. Moreover, traditional optical flow is insufficient to represent complex camera motions. We therefore build the first benchmark for camera motion analysis, including a motion dataset with 11 motion styles and evaluation protocols. Furthermore, we propose a motion representation that augments optical flow with vorticity cues from fluid dynamics, thereby better capturing motions. Experiments show that our detector achieves a 3.02 improvement in plagiarism detection over the strongest baseline and remains effective on generative videos. We believe our work extends copyright protection beyond static content to dynamic camera motion.

</details>

### 79. DualAlign: write-read Alignment for Robust Image Watermarking

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`image watermarking`、`write-read alignment`、`feature modulation`、`distortion generalization`

👤 **作者**：Zhi Zeng

- 🎯 **研究动机**：鲁棒图像水印要求嵌入信号在多样失真下存活且不可感知；现有深度方法遵循「嵌入-失真-提取」管线、仅靠端到端监督，嵌入器与提取器缺乏显式协调——嵌入器不知晓自己将被如何读取，提取器被动适应嵌入行为，只能依赖大规模失真枚举换取鲁棒性。
- 🔬 **研究方法**：DualAlign 主张鲁棒性根本上依赖写-读对齐，通过双级显式对齐替代失真枚举：特征级的自适应特征调制模块（AFMM）解耦空间结构与调制强度，决定嵌入位置与强度；协调级的协作交互机制（CIM）在训练中于嵌入器与提取器之间交换调制状态线索，两者相互强化。
- 📌 **结论**：仅用两种代表性失真训练即超越采用 10+ 类失真大量枚举训练的方法，表明显式对齐是鲁棒性的关键机制，为穷举式失真枚举提供了替代路径。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Robust image watermarking requires embedded signals to survive diverse distortions while remaining imperceptible. Existing deep methods follow the embedding--distortion--extraction pipeline with only end-to-end supervision, lacking explicit coordination between embedder and extractor. This creates a dual mismatch: the embedder writes without knowing how it will be read, while the extractor passively adapts to embedding behavior, forcing reliance on extensive distortion enumeration for robustness. We argue that robustness fundamentally requires write--read alignment between embedding and extraction. To this end, we propose DualAlign, a framework that achieves robustness through Dual-Level Explicit Alignment rather than distortion enumeration. At the feature level, an Adaptive Feature Modulation Module (AFMM) decouples spatial structure from modulation strength, determining where to embed and how strongly. These decisions provide the representational basis for robust watermarking. At the coordination level, a Collaborative Interaction Mechanism (CIM) exchanges modulation-state cues between embedder and extractor during training. These two components operate in mutual reinforcement: CIM's strategic synchronization is grounded in AFMM's feature-level robustness, while the guidance from CIM further refines AFMM's modulation. Extensive experiments demonstrate that DualAlign outperforms state-of-the-art methods even when trained with only two representative distortions, surpassing approaches employing extensive enumeration (10+ types). This reveals that explicit alignment is a critical mechanism for robustness, offering an alternative to exhaustive distortion enumeration.

</details>

### 80. Erase but Preserve: Controllable Removal of Copyrighted Animation Characters via Optimized Semantic Anchors

📄 [arXiv](https://arxiv.org/abs/2608.12806)　📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`copyright erasure`、`animation character`、`semantic anchor`、`textual embedding`

👤 **作者**：Qiao Li、Xiaomeng Fu、Wangjia Yu、Baisen Wang、Jizhong Han

- 🎯 **研究动机**：T2I 扩散模型强大的生成能力引发版权担忧，尤其是对动画角色的未授权复现；现有概念擦除方法难以胜任：模型修改类方法难以为多样且高度独特的角色找到合适锚点，提示引导类方法缺乏精确干预的细粒度控制，常导致擦除不完全与图像保真度下降。
- 🔬 **研究方法**：在模型连续文本表征上进行可控擦除：通过结构与细节约束优化一个锚点嵌入作为角色替身，再以结构感知的自适应策略将目标相关嵌入替换为该锚点，从而在生成时移除目标角色。
- 📌 **结论**：实验表明该方法达到 SOTA 的擦除效果与图像保真保持，支持可控擦除程度、多目标移除与模型迁移；优化后的锚点还可即插即用地增强现有模型修改类基线的擦除性能。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The exceptional generation capabilities of text-to-image diffusion models have raised copyright concerns, particularly the unauthorized reproduction of animation characters. Existing concept erasure methods fall short for animation character erasure: model modification methods struggle to identify suitable anchors for diverse, highly distinctive characters; prompt-based steering methods lack fine-grained control for precise intervention. These approaches often yield incomplete erasure and degraded image fidelity, hindering real-world deployment. In this paper, we propose a controllable method operating on the models continuous textual representation to erase target characters during generation. We optimizes an anchor embedding via structural and detailed constraints to serve as a character surrogate, then replaces target-related embeddings with the anchor via a structure-aware adaptive strategy. Experiments show that our method achieves state-of-the-art erasure effectiveness and image fidelity preservation, while supporting controllable erasure degree, multi-target removal, and model transferability. Moreover, our optimized anchors are plug-and-play with current model modification baselines to improve their erasure performance.

</details>

### 81. Fingerprinting Multimodal Large Language Models

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`model fingerprinting`、`multimodal LLM`、`provenance`、`distillation detection`

👤 **作者**：Kejiang Chen

- 🎯 **研究动机**：MLLM 支持广泛的图文推理任务，但近期事件表明其面临非法部署与未授权蒸馏的风险；现有模型溯源方案常被 MLLM 共享的语言骨干所混淆，且难以检测蒸馏侵权。
- 🔬 **研究方法**：开展首个多模态模型指纹研究：AttnPrint 面向白盒溯源，基于「自注意力充当低通滤波器且低频分量信息丰富」的发现，提取跨模态注意力分布并分离其低频分量作为模型指纹；DistillTrace 面向黑盒审计，通过对 MLLM 输出做假设检验识别潜在模型侵权。
- 📌 **结论**：在 19 种多模态架构的 154 个模型实例上实验，AttnPrint 实现强衍生模型检测并对五种下游修改技术保持鲁棒；DistillTrace 在三种参数无关蒸馏技术下提供蒸馏关系证据。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While multimodal large language models (MLLMs) enable a wide range of image-text reasoning tasks, recent incidents indicate that they are vulnerable to illicit deployment and unauthorized distillation. Existing solutions for model provenance are typically confounded by shared language backbones in MLLMs and struggle to detect violations of distillation. To bridge this gap and safeguard model ownership, we present the first study on multimodal model fingerprinting. Inspired by recent findings that self-attention acts as a low-pass filter and that its low-frequency components are informative, we develop AttnPrint for white-box provenance. Specifically, we extract cross-modal attention distributions and isolate their low-frequency components to serve as model fingerprints. To facilitate black-box auditing, we further introduce DistillTrace, which employs hypothesis testing of MLLM outputs to identify potential model infringement. We conduct extensive experiments on 154 model instances across 19 multimodal architectures. Notably, AttnPrint achieves strong derivative-model detection performance while remaining robust to five downstream modification techniques. DistillTrace also provides evidence of distillation relationships under three parameter-independent techniques.

</details>

### 82. From Payloads to Intrinsic Property: A Graph-Based Semantic Paradigm for Robust Watermarking

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`semantic watermarking`、`graph structure`、`content alignment`、`geometric robustness`

👤 **作者**：Pengzhen Chen、Yanwei Liu、Wu Liu、Xiaojun Chen、Xiaoyan Gu

- 🎯 **研究动机**：多数数字水印嵌入与宿主图像语义无关的外部载荷，不可避免引入可感知伪影，且在几何变换（裁剪、缩放）与现代 AI 编辑等真实图像操纵下，嵌入消息易被扭曲或移除。
- 🔬 **研究方法**：GraphMark 构建与内容对齐的水印框架：将图像划分为 patch、识别语义相似 patch 对并组织成稀疏语义图作为水印信号；经 Attentive EdgeConv 层在语义相关节点间聚合特征，把图编码回宿主图像并保持高视觉保真；解码时把水印提取形式化为图恢复任务，从可能被编辑过的图像预测嵌入的成对关系。
- 📌 **结论**：与直接从原图提取信号的指纹方法不同，GraphMark 的结构化内容依赖水印仅经嵌入过程后方可恢复；通过将水印信号与图像语义对齐而非注入任意载荷，在鲁棒性与不可感知性之间取得更优权衡，显著超越现有水印方法。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Most digital watermarking techniques embed an external payload that is semantically unrelated to the host image. Such a paradigm inevitably introduces perceptible artifacts and remains vulnerable to realistic image manipulations, including geometric transformations (e.g., cropout and resizing) and modern AI-based editing, which can easily distort or remove the embedded message. In this work, we propose GraphMark, a novel content-aligned watermarking framework that constructs a graph-based watermark signal from the semantic structure of the image and explicitly embeds this signal back into the host image. Specifically, GraphMark partitions the image into patches, identifies semantically similar patch pairs, and organizes them into a sparse semantic graph that serves as the watermark signal. The graph is then encoded into the image through a novel Attentive EdgeConv layer, which aggregates features among semantically related nodes while preserving high visual fidelity. During decoding, watermark extraction is formulated as a graph recovery task that predicts the embedded pairwise relationships from the potentially edited image. Unlike fingerprinting methods that directly extract signals from the original image, GraphMark introduces a structured, content-dependent watermark that is only recoverable after the embedding process. By aligning the watermark signal with the image semantics rather than injecting an arbitrary payload, GraphMark achieves a more favorable trade-off between robustness and imperceptibility, significantly outperforming existing watermarking methods.

</details>

### 83. GenWM-Bench: A New Benchmark on Diffusion Model Watermarks Against Multi-Level Attacks

🐙 [Code](https://github.com/REPO-EXP/GenWM-Bench.git)　📅 2026　🏷 ACM MM 2026

**关键词**：`benchmark`、`diffusion watermark`、`multi-level attack`、`robustness evaluation`、`Pareto front`

👤 **作者**：Jing Yu、Jianbo Gao、Liehuang Zhu

- 🎯 **研究动机**：生成式图像模型广泛落地后，水印成为版权保护与溯源的关键防御，但缺乏标准化评测框架使现有算法的性能评估碎片化、结果不可比。
- 🔬 **研究方法**：GenWM-Bench 是面向扩散水印的标准化评测框架：系统地将 12 个 SOTA 水印方案归入不同技术范式，纳入图像级、模型级、检测器导向与伪造四类关键攻击面以模拟复杂真实威胁，并以 Pareto 前沿分析各方案在极端威胁下的运行极限。
- 📌 **结论**：评测揭示多个此前未探索的漏洞：权重集成方案在模型合并的参数平均下易被稀释，内容无关方案面临模式提取带来的模板隔离风险，语义类方法在再生成变体下出现显著失败率；同时识别出对各方案最具威胁的攻击类型。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As generative image models achieve widespread adoption, watermarking has emerged as a critical defense for copyright protection and provenance. However, the lack of a standardized evaluation framework has led to fragmented and incomparable performance assessments of existing algorithms. To address this, we propose GenWM-Bench, a standardized evaluation framework tailored for diffusion-based watermarks. We systematically categorize 12 state-of-the-art watermarking schemes into distinct technical paradigms. To simulate complex real-world threats, our framework incorporates four critical attack surfaces: Image-level, Model-level, Detector-oriented, and Forgery. Our evaluation uncovers several critical yet unexplored vulnerabilities within current watermarking. For instance, weight-integrated schemes are susceptible to parameter averaging during model merging; content-agnostic schemes face the risk of template isolation via pattern extraction; and semantic-based methods exhibit significant failure rates during regeneration variants. Through a Pareto Front analysis across different schemes, we identify the operational limits of various watermarking methods under extreme threats and highlight the most challenging attacks. GenWM-Bench establishes a reference standard for the research and deployment of robust watermarks. Code is available at https://github.com/REPO-EXP/GenWM-Bench.git.

</details>

### 84. Geometry-Aware Localized Watermarking for Copyright Protection in Embedding-as-a-Service

📄 [arXiv](https://arxiv.org/abs/2604.11344)　📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`EaaS watermarking`、`localized triggering`、`copyright verification`、`embedding service`

👤 **作者**：Zhimin Chen

- 🎯 **研究动机**：Embedding-as-a-Service（EaaS）已成为自然语言与多媒体应用的重要语义基础设施，但极易受模型窃取与版权侵犯；现有 EaaS 水印存在鲁棒性-效用-可验证性的根本张力：触发式方法对改写脆弱，变换式方法对维度扰动敏感，区域式方法可能因巧合的几何亲和性产生误报。
- 🔬 **研究方法**：GeoMark 以流形内自然嵌入作为共享水印目标，构造带显式目标-锚点间隔的几何分离锚点，并仅在自适应局部邻域内激活水印注入；该设计将「水印在何处触发」与「所有权归属于谁」解耦，实现局部触发与集中归因。
- 📌 **结论**：四个基准数据集上，GeoMark 在改写、维度扰动与 CSE（聚类-选择-消除）攻击下保持鲁棒的版权验证，同时保持下游效用与几何保真，验证稳定性更高且误报风险低。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Embedding-as-a-Service (EaaS) has become an important semantic infrastructure for natural language and multimedia applications, but it is highly vulnerable to model stealing and copyright infringement. Existing EaaS watermarking methods face a fundamental robustness--utility--verifiability tension: trigger-based methods are fragile to paraphrasing, transformation-based methods are sensitive to dimensional perturbation, and region-based methods may incur false positives due to coincidental geometric affinity. To address this problem, we propose GeoMark, a geometry-aware localized watermarking framework for EaaS copyright protection. GeoMark uses a natural in-manifold embedding as a shared watermark target, constructs geometry-separated anchors with explicit target--anchor margins, and activates watermark injection only within adaptive local neighborhoods. This design decouples where watermarking is triggered from what ownership is attributed to, achieving localized triggering and centralized attribution. Experiments on four benchmark datasets show that GeoMark preserves downstream utility and geometric fidelity while maintaining robust copyright verification under paraphrasing, dimensional perturbation, and CSE (Clustering, Selection, Elimination) attacks, with improved verification stability and low false-positive risk.

</details>

### 85. GIFGuard: Proactive Forensics against Deepfakes in Facial GIFs via Spatiotemporal Watermarking

📄 [arXiv](https://arxiv.org/abs/2604.26519) · 🐙 [Code](https://github.com/vpsg-research/GIFGuard)　📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`GIF watermarking`、`deepfake forensics`、`spatiotemporal`、`proactive defense`

👤 **作者**：Zhiqing Guo、Changtao Miao

- 🎯 **研究动机**：深度伪造技术的快速演进对 GIF 图像的真实性构成空前威胁——GIF 是社交网络短循环时序媒体的代表；但现有主动取证工作面向静态图像设计，难以直接用于动画 GIF。
- 🔬 **研究方法**：GIFGuard 是首个面向 GIF 深伪主动取证的时空水印框架：嵌入阶段设计时空自适应残差编码器 STARE，以 3D 卷积骨干与自适应通道重校准捕捉全局连贯的时间依赖，确保对高层语义篡改的鲁棒性；提取阶段设计深度完整性恢复解码器 DIRD，采用带 3D 注意的时空沙漏结构恢复潜特征，在严重人脸操纵下仍能准确提取水印；同时构建首个 GIF 主动取证大规模基准数据集 GIFfaces。
- 📌 **结论**：大量实验表明 GIFGuard 兼具高保真视觉质量与对深度伪造的强鲁棒性，代码与数据集已开源。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid evolution of deepfake technology poses an unprecedented threat to the authenticity of Graphics Interchange Format (GIF) imagery, which serves as a representative of short-loop temporal media in social networks. However, existing proactive forensics works are designed for static images, which limits their applicability to animated GIFs. To bridge this gap, we propose GIFGuard, the first spatiotemporal watermarking framework tailored for deepfake proactive forensics in GIFs. In the embedding stage, we propose the Spatiotemporal Adaptive Residual Encoder (STARE) to ensure robustness against high-level semantic tampering. It employs a 3D convolutional backbone with adaptive channel recalibration to capture globally coherent temporal dependencies. In the extraction stage, we design the Deep Integrity Restoration Decoder (DIRD). It utilizes a spatiotemporal hourglass architecture equipped with 3D attention to restore latent features, allowing for the accurate extraction of watermark signals even under severe facial manipulation. Furthermore, we construct GIFfaces, the first large-scale benchmark dataset curated for GIF proactive forensics to facilitate research in this domain. Extensive results show that GIFGuard achieves high-fidelity visual quality and remarkable robustness performance against deepfakes. The related code and dataset are available at https://github.com/vpsg-research/GIFGuard.

</details>

### 86. High-Fidelity Face Content Recovery via Tamper-Resilient Versatile Watermarking

📄 [arXiv](https://arxiv.org/abs/2603.23940)　📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`versatile watermarking`、`manipulation localization`、`face recovery`、`deepfake forensics`

👤 **作者**：Peipeng Yu、Xiaoyu Zhou、Jianwei Fei、Zhihua Xia

- 🎯 **研究动机**：AIGC 人脸操纵与深度伪造对媒体溯源、完整性与版权保护构成严重威胁；现有通用水印系统依赖显式定位载荷，带来保真度-功能性权衡——更大的定位信号会降低视觉质量并在强生成编辑下削弱解码鲁棒性，且很少支持内容恢复，限制了取证价值。
- 🔬 **研究方法**：VeriFi 统一版权保护、像素级操纵定位与高保真人脸内容恢复：嵌入紧凑语义潜水印作为内容保留先验，使严重操纵后仍能忠实复原；不依赖专用载荷，通过图像特征与解码溯源信号的相关性实现细粒度定位；并引入结合潜空间混合与无缝融合的 AIGC 攻击模拟器，增强对真实深伪管线的鲁棒性。
- 📌 **结论**：在 CelebA-HQ 与 FFHQ 上的实验显示，VeriFi 在水印鲁棒性、定位精度与恢复质量三方面一致超越 SOTA 基线，为深伪取证提供可验证的实用防御。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of AIGC-driven face manipulation and deepfakes poses severe threats to media provenance, integrity, and copyright protection. Existing versatile watermarking systems typically rely on embedding explicit localization payloads, which introduces a fidelity--functionality trade-off: larger localization signals degrade visual quality and often reduce decoding robustness under strong generative edits. Moreover, these methods rarely support content recovery, limiting their forensic value when original evidence must be reconstructed. To address these challenges, we present VeriFi, a versatile watermarking framework that unifies copyright protection, pixel-level manipulation localization, and high-fidelity face content recovery. VeriFi makes three key contributions: (1) it embeds a compact semantic latent watermark that serves as a content-preserving prior, enabling faithful restoration even after severe manipulations; (2) it achieves fine-grained localization without dedicated payloads by correlating image features with decoded provenance signals; and (3) it introduces an AIGC attack simulator that combines latent-space mixing with seamless blending to enhance robustness against realistic deepfake pipelines. Extensive experiments on CelebA-HQ and FFHQ demonstrate that VeriFi consistently outperforms state-of-the-art baselines in watermark robustness, localization accuracy, and recovery quality, providing a practical and verifiable defense for deepfake forensics.

</details>

### 87. LAVA: Layered Audio-Visual Anti-tampering Watermarking for Robust Deepfake Detection and Localization

📄 [arXiv](https://arxiv.org/abs/2604.23957)　📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`audiovisual watermarking`、`deepfake localization`、`cross-modal fusion`、`compression robustness`

👤 **作者**：Jiaojiao Jiang

- 🎯 **研究动机**：主动水印为短视频深伪篡改检测与定位提供了途径，但现有方法常将音频与视觉证据解耦，并假设水印信号在真实退化下仍然可靠，使篡改定位易受多模态错位与压缩失真影响；已有半脆弱视觉水印的嵌入频带与压缩敏感频率区域重叠，在编解码压缩下性能显著退化。
- 🔬 **研究方法**：LAVA 是校准感知的音视频水印融合框架：通过跨模态水印融合与校准感知对齐，在压缩与音视频不同步条件下保持一致、可靠的篡改证据，支撑鲁棒的篡改检测与定位。
- 📌 **结论**：实验显示 LAVA 取得近乎完美的检测性能（AP = 0.999），对压缩与多模态错位保持鲁棒，篡改定位可靠性显著优于现有音视频融合基线。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Proactive watermarking offers a promising approach for deepfake tamper detection and localization in short-form videos. However, existing methods often decouple audio and visual evidence and assume that watermark signals remain reliable under real-world degradations, making tamper localization vulnerable to multimodal misalignment and compression distortions. Moreover, existing semi-fragile visual watermarking methods often degrade significantly under codec compression because their embedding bands overlap with compression-sensitive frequency regions. To address these limitations, we propose Layered Audio-Visual Anti-tampering Watermarking (LAVA), a calibration-aware audiovisual watermark fusion framework for deepfake tamper detection and localization. LAVA leverages cross-modal watermark fusion and calibration-aware alignment to preserve consistent and reliable tamper evidence under compression and audiovisual asynchrony, enabling robust tamper localization. Extensive experiments demonstrate that LAVA achieves near-perfect detection performance (AP = 0.999), remains robust to compression and multimodal misalignment, and significantly improves tamper localization reliability over existing audiovisual fusion baselines.

</details>

### 88. LEGO: Enhancing Watermark Robustness Against Multiple Distortions via Task Vectors

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`watermark robustness`、`task vector`、`modular extractor`、`multi-distortion`

👤 **作者**：Han Fang、Kejiang Chen

- 🎯 **研究动机**：增强「编码器-噪声层-解码器」架构的鲁棒性是深度水印的关键挑战；现有方法普遍依赖多噪声层联合训练，隐式迫使模型在不同失真诱导的冲突优化目标之间相互妥协。
- 🔬 **研究方法**：LEGO 将多失真鲁棒性重构为任务组合问题，提出基于层级任务向量组合的模块化增强框架：以机制驱动的失真分类学把失真按退化机制划分为五个域，保证域内失真共享兼容的优化方向；固定水印嵌入器、只优化提取器，通过层级微调分别学习捕获共享鲁棒模式的域级任务向量与细粒度适配的失真特定任务向量。
- 📌 **结论**：分而治之的任务向量组合使提取器在多样失真设定下达到与 SOTA 相当或更优的鲁棒性，并支持向新失真类型无缝增量扩展，训练高效灵活。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Enhancing the robustness of ``encoder--noise layer--decoder'' architectures remains a key challenge in deep learning--based watermarking. Existing methods typically rely on joint training with combined noise layers, which implicitly forces the model to compromise among conflicting optimization objectives induced by different distortions. In this paper, we reformulate multi-distortion robustness as a task composition problem and propose LEGO, a modular robustness enhancement framework based on hierarchical task vector composition. Specifically, we introduce a mechanism-driven distortion taxonomy that partitions distortions into five domains according to their degradation mechanisms, ensuring that distortions within each domain share compatible optimization directions. With the watermark embedder fixed, we optimize only the extractor and design a hierarchical fine-tuning strategy to learn domain-level task vectors capturing shared robustness patterns and distortion-specific task vectors for fine-grained adaptation. Benefiting from this divide-and-conquer task vector composition design, the watermark extractor achieves improved robustness to multiple distortions while supporting seamless and incremental extension to new distortion types. Extensive experiments demonstrate that LEGO is efficient and flexible, achieving superior or comparable robustness to state-of-the-art methods across diverse distortion settings.

</details>

### 89. MoE-Shield: Adaptive Watermark Decoding via Mixture-of-Experts for Multi-Attack Robustness

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`watermark decoding`、`mixture-of-experts`、`composite attack`、`bit accuracy`

👤 **作者**：Sijing Xie、Hefei Ling、LuYu Yuan

- 🎯 **研究动机**：现有水印解码器在复合攻击下表现挣扎——多种退化联合遮蔽嵌入信号时，单一整体式解码器难以恢复消息，鲁棒解码应被视为组合恢复问题而非单解码器任务。
- 🔬 **研究方法**：MoE-Shield 把攻击感知特征提取器与共享-专用 MoE 架构耦合：提取器经图像、DCT、FFT、边缘与 CNN 五个分支处理失真图像、暴露互补失真线索；失真监督但推理盲的路由器将始终激活的共享专家（捕获失真不变恢复先验）与选择性激活的专用专家（建模攻击特定残差修正）组合起来。
- 📌 **结论**：在 20+ 种失真类型上展现对未见高阶复合攻击的组合泛化：13 种复合攻击组合下平均比特准确率达 98.43%，超最强基线 2.21 个百分点，同时保持参数效率与约 39 dB PSNR 的高视觉保真。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing watermark decoders struggle under composite attacks, where multiple degradations jointly obscure the embedded signal. We formulate robust watermark decoding under composite attacks as a compositional recovery problem rather than a monolithic one-decoder task. To this end, we propose MoE-Shield, a robust watermark decoder that couples an attack-aware feature extractor with a shared-specialized Mixture-of-Experts (MoE) architecture. The extractor processes the distorted watermarked image through image, DCT, FFT, edge, and CNN branches to expose complementary distortion cues. A distortion-supervised yet inference-blind router then composes always-active shared experts, which capture distortion-invariant recovery priors, with selectively activated specialized experts, which model attack-specific residual corrections. Extensive experiments across 20+ distortion types demonstrate compositional generalization to unseen higher-order composite attacks: MoE-Shield achieves 98.43% average bit accuracy under 13 composite-attack combinations, surpassing the strongest baseline by +2.21 percentage points, while maintaining competitive parameter efficiency and high visual fidelity (～39 dB PSNR).

</details>

### 90. MultiBinder: Preventing Multi-Subject Identity Leakage in Personalized Video Generation

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`identity leakage`、`multi-subject video`、`entity binding`、`personalized generation`

👤 **作者**：Wei Li、Yiheng Zhang、Zhaofan Qiu、Ting Yao、Xiaoyan Sun、Tao Mei

- 🎯 **研究动机**：个性化视频生成面临可扩展性挑战：随着自定义主体数量增加，现有方法出现严重身份泄漏与语义纠缠，产生属性混合、叙事混乱的视频；根源在于扩散模型融合之前，文本实体短语与对应视觉模式之间缺乏显式绑定。
- 🔬 **研究方法**：MultiBinder 采用「先绑定后叙述」范式，在视频扩散前进行两阶段条件化：跨模态实体绑定阶段用实体感知 Q-Former 从每个主体参考图提取以身份为中心的特征，并与唯一实体短语紧对齐得到解耦的身份 token；叙事感知主体编排阶段由 MLLM 充当「叙事导演」，从文本提示捕捉各主体动作并合成编码「谁在做什么」、保留角色区分的情境化主体特征，再经专用条件通路注入视频扩散模型。
- 📌 **结论**：在通用与新构建的多主体基准上，MultiBinder 在多主体身份保真上显著优于现有方法。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Personalized video generation faces a significant scalability challenge: as the number of custom subjects increases, existing methods suffer from severe identity leakage and semantic entanglement, resulting in videos with blended attributes and incoherent narratives. We identify that this stems from a lack of explicit binding between textual entity phrases and their corresponding visual patterns prior to fusion in diffusion models. To address this, we propose MultiBinder, a novel framework built on a ``bind-then-narrate'' paradigm. Our approach introduces a two-stage conditioning process before video diffusion. First, Cross-modal Entity Binding devises an entity-aware Q-Former to extract identity-centric features from each subjects reference image and tightly align them with its unique entity phrase, yielding disentangled ``identity tokens.'' Second, a Multimodal Large Language Model (MLLM) acts as a ``narrative director'' in the Narrative-Aware Subject Arrangement stage, capturing the action of each subject from the text prompt and synthesizes contextualized subject features that encapsulate ``who is doing what'' and preserve role-specific distinctions. These features are then injected into a video diffusion model via dedicated conditioning pathways, ensuring precise attribute allocation. Extensive experiments on both general and newly curated multi-subject benchmarks show that MultiBinder significantly outperforms existing methods in multi-subject identity fidelity.

</details>

### 91. OD-Copycat: Extracting Black-Box Object Detectors models using Purely Synthetic Data

🐙 [Code](https://github.com/jhonatanleao/OD-Copycat)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`model extraction`、`object detector`、`synthetic data`、`black-box distillation`

👤 **作者**：Jhonatan Machado Leo、Jacson Correia-Silva、Claudine Badue、Alberto Ferreira De Souza、Thiago Oliveira-Santos

- 🎯 **研究动机**：模型抽取攻击对专有 MLaaS 模型的知识产权构成严重威胁；该攻击在分类任务上研究充分，但黑盒设定下抽取目标检测器因任务复杂与数据稀缺仍然困难，已有方法常依赖与问题域相关的公开数据集，在严格黑盒场景并不现实——而高保真文生图多模态生成模型的出现根本改变了数据匮乏的局面。
- 🔬 **研究方法**：OD-Copycat 利用扩散模型合成多样且纯合成的训练集，再经 Oracle 引导的过滤管线精炼，在不接触任何问题域真实图像的前提下抽取黑盒目标检测器。
- 📌 **结论**：实验表明该方法在不使用一张问题域真实图像的情况下超越包括使用真实数据的 SOTA 基线；跨架构场景中恢复 Oracle 超过 83% 的性能，证明数据稀缺不再是抵御多模态生成模型驱动抽取攻击的屏障。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model extraction attacks pose a severe threat to the intellectual property of proprietary MLaaS models. While well-studied for classification, extracting object detectors in black-box settings remains challenging due to task complexity and data scarcity. Prior methods often rely on public datasets related to the problem domain, an assumption which is often impractical in strict black-box scenarios. However, the emergence of multimodal generative models capable of high-fidelity text-to-image synthesis has fundamentally altered this landscape. These advancements enable the execution of model extraction attacks against unimodal models under conditions previously considered unfeasible due to the lack of data. Leveraging this shift, we introduce OD-Copycat, a framework that utilizes diffusion models to synthesize a diverse, purely synthetic training set, refined by an Oracle-guided filtering pipeline. Experiments demonstrate that our approach outperforms state-of-the-art baselines, including those utilizing real data, without accessing a single problem-domain image. Notably, OD-Copycat achieves robust generalization in cross-architecture scenarios, recovering over 83% of the Oracle's performance. These findings expose a critical vulnerability, proving that data scarcity is no longer a defensive barrier against extraction attacks driven by multimodal models. Our code is available at https://github.com/jhonatanleao/OD-Copycat

</details>

### 92. Propagating Dataset Watermark for Black-Box Multi-Modal Retrieval Augmented Generation Services

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`dataset watermarking`、`RAG auditing`、`black-box verification`、`hypothesis testing`

👤 **作者**：Huili Wang、Wen Xiang、Tao Qi

- 🎯 **研究动机**：检索增强生成（RAG）让 LLM 得以利用专有多模态数据集；受本地算力限制，RAG 服务常外包给第三方，其黑盒特性使数据拥有者几乎无法了解数据如何被访问与使用，难以验证托管数据是否被未授权系统不当复用或完整并入目标服务，威胁数据资产的知识产权与服务质量。
- 🔬 **研究方法**：提出传播式数据集水印（PDW）统一框架，在完全黑盒的多模态 RAG 服务中审计数据所有权与利用完整性：向数据库嵌入不可感知信号，通过查询探针激活，使其效应沿检索与生成传播以验证实际数据使用；并对探针响应做概率建模，实现带理论保证的假设检验式审计。
- 📌 **结论**：在两个公开数据集、四个检索模型与四个 LLM 上，即使处于对抗设定也能可靠识别部分使用与未授权数据库使用，且对整体性能的影响可忽略。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) is an important technique for enabling LLMs to utilize proprietary multi-modal datasets. Due to limited local computational resources, RAG services are commonly outsourced to third-party providers. However, the black-box nature of these services provides data owners with little transparency into how their data are accessed and utilized. As a result, it becomes challenging to verify whether the entrusted data are improperly reused in unauthorized systems or fully incorporated into the target service, posing significant risks to both the intellectual property and the service quality of valuable data assets. In this paper, we propose a unified framework based on propagating dataset watermarking (PDW) to audit data ownership and utilization integrity in fully black-box multi-modal RAG services. PDW embeds imperceptible signals into the database and activates them through query probes, allowing their effects to propagate through retrieval and generation to verify actual data usage. By modeling probe responses probabilistically, our framework enables hypothesis testing with theoretical guarantees for data auditing. Experiments on two public datasets, four retrieval models, and four LLMs demonstrate that, even under adversarial settings, our framework can reliably identify partial and unauthorized database usage while incurring negligible impact on overall performance.

</details>

### 93. SSTMark: Robust Training-Free Semantic-Level Speech Watermarking

📄 [arXiv](https://arxiv.org/abs/2607.17592)　📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`speech watermarking`、`semantic level`、`training-free`、`traceability`

👤 **作者**：Jun-Cheng Chen、Chun-Shien Lu

- 🎯 **研究动机**：语音生成模型日益逼真且易获取，滥用、归因与治理问题随之增长，水印可让合成语音可追溯、可验证；但现有方法多将水印嵌入波形或频谱等信号级表征，在足够强的失真下水印可能被削弱或破坏，检测性能退化。
- 🔬 **研究方法**：SSTMark 是免训练的语义级语音水印框架：不同于信号级方法，将水印信息编码进生成语音所传达的语义内容（借由文本水印实现），并从恢复出的语言内容中检测水印，从根本上规避信号失真对水印载体的破坏。
- 📌 **结论**：在 AudioMarkBench 上展现最强平均鲁棒性；固定 1% 误报率下，相比 SOTA 基线在信号处理编辑与压缩编辑上平均检测率分别提升 4.6% 与 16.9%。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As speech generation models become increasingly realistic and widely accessible, concerns about the misuse, attribution, and governance of synthetic speech continue to grow. Watermarking provides a practical way to make synthesized speech traceable and verifiable. Most existing speech watermarking methods embed watermark information into signal-level representations, such as waveforms or spectrograms. Under sufficiently strong distortions, the embedded watermark may be weakened or destroyed, leading to degraded detectability. In this paper, we propose SSTMark, a training-free speech watermarking framework that operates at the semantic level through text watermarking. Unlike conventional signal-level watermarking methods, SSTMark encodes watermark information into the semantic content conveyed by generated speech, and detects the watermark from the recovered linguistic content. Experiments on AudioMarkBench demonstrate that SSTMark exhibits the strongest average robustness. Compared with the state-of-the-art baselines at a fixed false positive rate of 1%, SSTMark improves the average detection rate by 4.6% and 16.9% on signal-processing edits and compression edits, respectively.

</details>

### 94. StructMark: Robust and Diversity-Preserving Watermarking for Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2603.09454)　📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`diffusion watermarking`、`noise-as-watermark`、`structural encoding`、`diversity preservation`

👤 **作者**：Yuqi Qian、Yun Cao、Haocheng Fu、Meiyang Lv、Meineng Zhu

- 🎯 **研究动机**：扩散模型显著提升图像合成质量，高保真生成图像的滥用引发知识产权、隐私与声誉担忧；Noise-as-Watermark（NaW）路线把水印直接嵌入扩散过程，但现有方法将水印比特直接映射到单个采样值，实际部署鲁棒性不足。
- 🔬 **研究方法**：StructMark 改为将水印比特编码到采样值组之间的结构关系中，只要底层结构得以保留，编码信息即可存活；并引入专用随机化机制重排噪声元素位置，防止水印嵌入诱导固定的空间模式或位置，从而保持生成多样性。
- 📌 **结论**：大量实验表明该方法在大范围有损场景下实现 SOTA 鲁棒性，同时保持高生成质量。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in diffusion models have significantly improved the quality of image synthesis. At the same time, the misuse of such high-fidelity generated images raises growing concerns about intellectual property, privacy, reputation, and other security-related issues. Image watermarking offers a promising solution, and recent studies have increasingly explored Noise-as-Watermark (NaW) methods that embed watermarks directly into the diffusion process. However, existing NaW approaches remain insufficiently robust for real-world deployment. We argue that this limitation stems from the prevailing embedding paradigm, which directly maps watermark bits to individual sampled values. Instead, we propose encoding watermark bits into the structural relationships among groups of values, so that the encoded information can survive as long as the underlying structure is preserved. Furthermore, to better maintain generation diversity, we introduce a dedicated randomization mechanism that reshuffles noise element positions, preventing watermark embedding from inducing fixed spatial patterns or locations. Extensive experiments show that our method achieves state-of-the-art robustness while preserving high generation quality across a wide range of lossy scenarios.

</details>

### 95. WARP: A Unified Benchmark for Invisible Image Watermarking -- Robustness and Protection Against Attacks

🐙 [Code](https://github.com/ispras/wibe)　📅 2026　🏷 ACM MM 2026

**关键词**：`benchmark`、`invisible watermarking`、`robustness evaluation`、`watermark erasing`、`re-embedding attack`

👤 **作者**：Khaled Abud、Anastasia Antsiferova

- 🎯 **研究动机**：新兴法规与行业实践要求标记 AI 生成内容并确保来源可溯，数字图像水印因此愈发关键；隐形水印方法的最新进展也要求更新基准实践，以反映当前技术与评测标准。
- 🔬 **研究方法**：WARP 提供统一的隐形水印鲁棒性评测框架与基准：收录 32 种近期的经典、深度与生成式水印方法，以及 34 种擦除技术——覆盖从传统失真到对抗、净化与重嵌入攻击；并提供标准化、可复现、易扩展的协议，评测感知质量、水印可读性与攻击韧性。
- 📌 **结论**：基于此完成该领域最大规模的鲁棒性评测，识别出失真与对抗条件下最鲁棒的方法，揭示水印方法与其最有效攻击策略之间的稳定对应关系；并发现部分对标准失真鲁棒的方法面对重嵌入攻击时高度脆弱。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Digital image watermarking is increasingly critical in media contexts, as emerging regulations and industry practices require marking AI-generated content and ensuring traceable sources to prevent manipulation or misuse. Recent advances in invisible watermarking methods highlight the need to update existing benchmarking practices to reflect current techniques and evaluation criteria. We address this by introducing WARP a unified framework and benchmark for evaluating the robustness of invisible watermarks. WARP incorporates 32 recent classical, deep, and generative watermarking methods, as well as 34 different erasing techniques, ranging from traditional distortions to more sophisticated adversarial, purification, and re-embedding attacks. It provides standardized, reproducible, and easily scalable protocols for evaluating perceptual quality, watermark readability, and attack resilience. Using WARP, we extensively evaluate current invisible watermarking techniques, collecting the largest robustness benchmark in the field. Results identify the most robust approaches under both distortion and adversarial conditions, and reveal consistent relationships between watermarking methods and the attack strategies most effective against them. Our experiments also highlight that some of the watermarking methods considered are highly vulnerable to reembedding, even if they are robust to standard distortions. The code is made available at https://github.com/ispras/wibe.

</details>


### AI 生成图像检测与检测器攻防

### 96. Adaptive Forensic Feature Refinement via Intrinsic Importance Perception

📄 [arXiv](https://arxiv.org/abs/2604.16879)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`synthetic image`、`VFM adaptation`、`layer selection`、`low-sensitivity subspace`

👤 **作者**：Jiazhen Yang、Kejia Chen、Jie Lei、Zunlei Feng、Bingde Hu、Yang Gao

- 🎯 **研究动机**：合成图像检测（SID）的关键挑战是跨分布泛化到未知生成源。视觉基础模型（VFM）凭大规模图文对齐预训练获得的丰富视觉先验是提升泛化的有前景途径，但现有适配策略粗糙——或直接使用最后一层表征、或简单融合多层特征，缺少对可迁移伪造线索最优表征层级的显式建模；微调 VFM 又可能破坏支撑开放集泛化的跨模态预训练结构。
- 🔬 **研究方法**：提出以内在重要性感知为核心的 I2P 框架，把 VFM 适配重构为联合优化问题：一方面自适应识别对 SID 最具判别力的关键层表征来承载伪造判别信息，另一方面将任务驱动的参数更新约束在低敏感参数子空间内，在提升任务特异性的同时尽量保留预训练表征的可迁移结构。在多个跨域基准上开展系统实验与消融分析。
- 📌 **结论**：在多个跨域基准上，I2P 取得稳定且具竞争力的泛化性能，表明「关键层自适应选择＋低敏感子空间约束」能在注入任务知识的同时保住 VFM 预训练结构，缓解任务适配与开放集泛化之间的张力。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid development of generative models and multimodal content editing technologies, the key challenge in synthetic image detection (SID) lies in cross-distribution generalization to unknown generation sources. Visual foundation models (VFM), which acquire rich visual priors through large scale image-text alignment pretraining, have become a promising approach to improving SID generalization. However, existing VFM-based methods remain coarse-grained in their adaptation strategies. They typically either directly use the final layer representations of VFM or simply fuse multi layer features, lacking explicit modeling of the optimal representational hierarchy for transferable forgery cues. Although fine-tuning VFM can enhance task adaptation, it may also damage the cross-modal pretrained structure that supports open-set generalization. To address this task specific tension, we reformulate VFM adaptation for SID as a joint optimization problem: it is necessary both to identify the critical representational layer that is more suitable for carrying forgery discriminative information and to constrain the disturbance caused by task knowledge injection to the pretrained structure. Based on this, we propose I2P, an SID framework centered on intrinsic importance perception. I2P first adaptively identifies the critical layer representations that are most discriminative for SID, and then constrains task-driven parameter updates within a low sensitivity parameter subspace, thereby improving task specificity while preserving the transferable structure of pretrained representations as much as possible. We conduct systematic experiments and ablation analyses on multiple cross-domain benchmarks, and the results show that I2P achieves stable and competitive generalization performance.

</details>

### 97. Align, Don't Blend: Orthogonal Supervision Disentanglement As the Key to Generalizable AI-Generated Image Detection

🐙 [Code](https://github.com/GzZning/Align-Don-t-Blend)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`AIGI`、`supervision disentanglement`、`two-branch VLM`、`cross-generator generalization`

👤 **作者**：Ruoxin Chen、Jiahui Gao、Kaiqing Lin、Isabel Guan、Taiping Yao、Shouhong Ding

- 🎯 **研究动机**：AIGI 检测研究集中于架构、损失与训练策略，却忽视更根本的因素——监督信号的组织方式。现有检测器在基准数据上训练，语义与伪影信号隐式混杂；受控实验表明这种混杂监督不仅次优，而且根本性适得其反。
- 🔬 **研究方法**：将问题形式化为正交监督解耦（Orthogonal Supervision Disentanglement），实例化双分支检测器 AlignGemini：VLM 分支只接收纯语义监督，视觉专家分支只接收纯伪影监督。最简训练配方、仅用两个生成器的图像训练即可获得强跨生成器泛化。另发布诊断基准 AIGI-Now：覆盖 8 个当代生成器（含 5 个闭源商业模型），提供解耦的语义与像素评测子集。
- 📌 **结论**：解耦监督配合归纳匹配模型在 5 个 in-the-wild 基准上带来 9.5% 的显著提升，训练图像仅来自 2 个生成器；AIGI-Now 以 8 生成器与语义/像素解耦子集支撑检测器能力的细粒度诊断。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in AI-Generated Image (AIGI) detection have largely focused on model architectures, loss design, and training strategies, while overlooking a more fundamental factor: how supervision is structured. Existing detectors typically train on benchmark-defined data that implicitly blends semantic and artifact signals, leaving supervision design unexplored. In this paper, we examine supervision structure through controlled experiments and show that such blended supervision is not merely suboptimal but fundamentally counterproductive. Replacing it with disentangled, orthogonal supervisionpaired with inductively matched modelssuffices to achieve strong cross-generator generalization. We formalize this as Orthogonal Supervision Disentanglement and instantiate it in AlignGemini, a two-branch detector in which a VLM receives purely semantic supervision and a vision expert receives purely artifact supervision. With disentangled supervision coupled with inductively matched models, even the simplest training recipe achieves a significant improvement of 9.5% across five in-the-wild benchmarkstrained on images from only two generators, without complex training strategies or diverse generator coverage. We further introduce AIGI-Now, a diagnostic benchmark covering eight contemporary generators, including five closed-source commercial models, with disentangled semantic and pixel evaluation subsets for fine-grained analysis of detector capabilities. Our code is publicly available at https://github.com/GzZning/Align-Don-t-Blend.

</details>

### 98. Anchor-Regularized Adaptation for Generalizable AI-Generated Image Detection with DINOv3

📄 [arXiv](https://arxiv.org/abs/2608.15196)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`DINOv3`、`low-rank adaptation`、`anchor regularization`、`pixel-artifact cues`

👤 **作者**：Hyeongjun Choi、Davide Cozzolino、Luisa Verdoliva

- 🎯 **研究动机**：AIGI 检测中，精心对齐训练数据可通过去除伪相关提升泛化；但发现冻结 DINOv3 上的线性探针即使在未对齐数据上训练也表现极强。分析显示其泛化源于决策依赖忠实表征真实图像空间的特征，而最终层不擅长捕捉对齐训练可强调的细微像素伪影线索；简单混用对齐与未对齐数据虽提升敏感度，却扭曲预训练表征、限制泛化。
- 🔬 **研究方法**：提出锚正则化适配（ARA）：用低秩适配（LoRA）捕捉像素级伪影，同时用冻结的锚分类器约束模型不偏离原表征结构，从而在不牺牲泛化的前提下利用像素伪影线索，实现对齐与未对齐数据的互补监督。
- 📌 **结论**：在 9 个多样且具挑战性的基准上取得 SOTA 性能，表明 ARA 能融合来自未对齐与对齐数据的互补监督，实现更有效的 AIGI 检测。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent works in AI-generated image detection have shown that careful training data alignment can improve generalization by removing spurious correlations. However, linear probes on frozen DINOv3 representations achieve remarkably strong performance even when trained on misaligned datasets. Motivated by this result, we analyze the underlying rationale and the limits of this generalization. We find that frozen DINOv3 performs well because its decisions rely on features that faithfully represent the space of authentic images. At the same time, its final layer is less effective at capturing the subtle pixel-artifact cues that can be emphasized by aligned training data. We further observe that naively mixing aligned and misaligned data during adaptation improves sensitivity to such cues but at the cost of distorting the pre-trained representation, limiting generalization. To address this issue, we propose Anchor-Regularized Adaptation (ARA). We apply Low-Rank Adaptation to capture pixel-level artifacts while leveraging a frozen anchor classifier to avoid deviations from the original representation structure. This allows the model to exploit pixel-artifact cues without sacrificing generalization. Our method achieves state-of-the-art performance on nine diverse and challenging benchmarks, indicating that ARA enables complementary supervision from misaligned and aligned data for more effective detection.

</details>

### 99. Defake-o3: From Speculative Rationales to Verifiable Evidence for Explainable AIGI Detection

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`explainable AIGI`、`verifiable evidence`、`visual search`、`reinforcement learning`、`benchmark`

👤 **作者**：Yikun Ji、Jianfu Zhang

- 🎯 **研究动机**：图像生成模型快速进步，要求 AIGI 检测器不仅准确，还要可解释、可靠。MLLM 检测器能给出自然语言解释，但常产出「投机性依据」：依赖含糊或幻觉的伪影、漏掉最新生成器的细微局部缺陷、无法提供可视觉验证的证据。
- 🔬 **研究方法**：提出 Defake-o3，结合交互式视觉搜索与验证器引导的证据对齐：模型迭代放大可疑区域检查细粒度细节，由人类核验标注训练的 Evidence Verifier 以强化学习奖励有据证据、惩罚无据断言。构建 GroundFake 数据集（含边界框定位证据、人工核验、修正推理轨迹、有效/无效证据监督），以及真实图像加 10 个最新生成器输出构成的 OOD 基准 FakeFrontier，并配 MLLM 证据质量评测协议。
- 📌 **结论**：在 GroundFake、FakeFrontier 及额外 OOD 基准上，Defake-o3 同时提升检测准确率与解释质量，产出更局部化、可验证、更有说服力的证据。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid progress of image generation models calls for AI-generated image (AIGI) detectors that are not only accurate but also explainable and reliable. While MLLM-based detectors can provide natural language explanations, existing methods often generate speculative rationales: they rely on vague or hallucinated artifacts, miss subtle localized flaws from the latest generators, and fail to provide evidence that can be visually verified. We present Defake-o3, an explainable AIGI detector that moves from speculative rationales to verifiable evidence. It combines interactive visual search with verifier-guided evidence alignment: the model iteratively zooms into suspicious regions to inspect fine-grained details, while an Evidence Verifier, trained from human verification annotations, provides reinforcement learning rewards that favor grounded evidence and penalize baseless claims. To support this objective, we construct GroundFake, a dataset designed for grounded explainable detection, with localized bounding-box evidence, human verification based on visual grounding and artifact specificity, corrected reasoning trajectories, and valid/invalid evidence supervision. We further introduce FakeFrontier, an out-of-distribution benchmark built from real images and outputs of 10 recent generators, together with an MLLM-based protocol for evaluating evidence quality and persuasiveness. Experiments on GroundFake, FakeFrontier, and additional out-of-distribution benchmarks show that Defake-o3 improves both detection accuracy and explanation quality, producing more localized, verifiable, and persuasive evidence.

</details>

### 100. Deviating from Real and Aligning with Fake: An Asymmetric Evidence Comparison for RAG-based AI-Generated Image Detection

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`AIGI`、`RAG`、`asymmetric evidence comparison`、`VLM`、`cross-domain generalization`

👤 **作者**：Zhiliang Tian、Zhen Huang、Dongsheng Li

- 🎯 **研究动机**：现有 CNN 与 VLM 检测器易过拟合训练域模式、难以泛化到未见生成模型；RAG 增强检测通过检索相似图像缓解 VLM 对纯语义上下文的依赖，但按语义相似度同等对待全部检索样本，忽视关键不对称性——检索库同时含真样本与假样本，二者携带本质不同的判别信号，偏离真实模式并不等价于与假样本共享伪造线索。
- 🔬 **研究方法**：提出非对称证据比较框架 AEC：从互补的语义、纹理、频率空间检索参考样本，以基于熵的自适应加权评估多流可靠性；证据比较模块（ECM）经两条非对称分支处理——真实性偏离分支对真样本计算残差以捕捉与真实图像分布的差异，伪造对齐分支与假样本做 Hadamard 积放大特定特征维度的共享伪造线索；最终组织为结构化证据模板引导 VLM 推断。
- 📌 **结论**：多个基准上的实验表明 AEC 对未见生成模型取得优越性能，同时实现可解释检测与强跨域泛化。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI-generated image detection has become a critical challenge as generative models produce increasingly realistic fake content. Existing methods, including CNN-based detectors and VLM-based approaches, typically overfit to training-domain patterns and struggle to generalize to unseen generative models. Recent RAG-augmented detection methods alleviate this by retrieving similar images as references to reduce VLMs' reliance on purely semantic context; however, they treat all retrieved samples uniformly based on semantic similarity, overlooking a key asymmetry: a retrieval gallery contains both real and fake samples, which carry inherently different discriminative signals. We argue that deviating from real image patterns is not equivalent to sharing forgery clues with fake samples, and that treating them uniformly discards the asymmetry that enables reliable detection. To address this, we propose AEC, an asymmetric evidence comparison framework for RAG-based AI-generated image detection, which explicitly converts retrieved real and fake samples into asymmetric discriminative evidence, rather than simply appending them as context. Specifically, AEC retrieves reference samples from complementary semantic, texture, and frequency spaces, and evaluates multi-stream reliability through an entropy-based adaptive weighting mechanism. The Evidence Comparison Module (ECM) then processes them via two asymmetric branches: the authenticity deviation branch computes residuals against real samples to capture discrepancies from real image distributions, while the forgery alignment branch applies the Hadamard product with fake samples to amplify shared forgery clues in specific feature dimensions. AEC organizes these signals into a structured evidence template guiding VLM inference, achieving interpretable detection and strong cross-domain generalization. Experiments on multiple benchmarks demonstrate superior performance against unseen generative models. The code and models are at https://anonymous.4open.science/r/AEC-85D7.

</details>

### 101. Exploiting Cross-Modal Coherence Shortcuts: Adversarial Attacks on Audio-Visual Deepfake Detection

📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`audio-visual deepfake`、`cross-modal coherence`、`adversarial perturbation`、`robustness bottleneck`

👤 **作者**：Xinle Wang、Xiaochun Cao

- 🎯 **研究动机**：音视频（AV）深伪检测器通过利用语音与面部运动的时序一致性越来越有效；这一优势也可能成为共享漏洞——许多 AV 检测器似乎依赖相似的跨模态同步统计量作为判别线索，构成可被统一利用的鲁棒性瓶颈。
- 🔬 **研究方法**：提出一致性引导的对抗攻击，操纵对齐先验：从预训练 AV 编码器构建局部跨模态对齐分布，用两个互补项刻画——相对时序中心的期望绝对偏差（捕捉偏离中心的同步）与对齐熵（捕捉弥散或不确定的对应关系）；将两项合成统一的一致性分数并直接优化，生成对视频与音频同时施加的有界联合扰动，在 FakeAVCeleb 上评测代表性检测器。
- 📌 **结论**：在 FakeAVCeleb 上，该方法在保持感知质量的同时使代表性 AV 深伪检测器大幅失效，并揭示跨模态一致性是 AV 深伪检测的潜在鲁棒性瓶颈。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Audio-visual (AV) deepfake detectors have become increasingly effective by exploiting temporal coherence between speech and facial motion. In this paper, we show that this strength can also become a shared vulnerability: many AV detectors appear to rely on similar cross-modal synchronization statistics as discriminative cues. Motivated by this observation, we propose a coherence-guided adversarial attack that manipulates alignment priors. Specifically, we construct a local cross-modal alignment distribution from pre-trained AV encoders and characterize it with two complementary terms: expected absolute deviation from the temporal center, which captures off-center synchronization, and alignment entropy, which captures diffuse or uncertain correspondence. We combine these terms into a unified coherence score and optimize it directly to generate bounded joint perturbations on both video and audio. Experiments on FakeAVCeleb show that the proposed method substantially degrades representative AV deepfake detectors while preserving perceptual quality. Beyond attack effectiveness, our results highlight cross-modal coherence as a potential robustness bottleneck in AV deepfake detection.

</details>

### 102. HydraPrompt: An Adaptive and Asymmetric Framework of Vision-Language Models for Synthetic Image Detection

📄 [arXiv](https://arxiv.org/abs/2605.26421)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`synthetic image`、`prompt learning`、`CLIP`、`asymmetric prompting`、`contrastive learning`

👤 **作者**：Senyuan Shi、Hao Tan、Zichang Tan、Sergio Escalera、Jun Wan

- 🎯 **研究动机**：生成模型的快速演化带来伪造内容激增，对现有合成图像检测（SID）方法构成严峻挑战。利用 CLIP 等 VLM 的可学习文本提示方法仍以静态提示作为真/假图像的固定边界，无法适应推理时不断涌现的多样伪造类型。
- 🔬 **研究方法**：提出非对称提示框架 HydraPrompt，通过与细粒度视觉线索对齐动态调整类别中心。非对称提示适配器（APA）对真实类别引入单一提示组捕捉一致的代表性模式、充当真实内容的统一锚；对伪造类别构建样本自适应提示，专门捕捉不同样本的多样线索，实现对伪造图像变化的自适应建模；进一步引入条件监督对比（CSC）目标，增强不同合成图像间的判别性。
- 📌 **结论**：在主流 SID 基准上的大量实验表明 HydraPrompt 取得 SOTA 性能，验证了非对称「真实锚定＋伪造自适应」提示设计的有效性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid evolution of generative models has precipitated a proliferation of fabricated content, posing significant challenges to existing Synthetic Image Detection (SID) methods. Capitalizing on advancements in vision-language models (e.g., CLIP), recent attempts have leveraged learnable textual prompts to identify synthetic images. However, they still leverage static prompt as a fixed boundary for real and fake images, failing to adapt to the varying types of forgery that emerge during inference. To overcome this issue, we propose HydraPrompt, an asymmetric prompting framework that dynamically adjusts the category centers by aligning with fine-grained visual cues. Specifically, we propose an Asymmetric Prompt Adapter (APA): (1) for authentic category, we introduce a single set of prompts to capture the consistent representative patterns, which serves as a unified anchor for real content. While (2) for fake category, we construct sample-adaptive prompts that specialize in capturing diverse cues from different samples, enabling adaptive modeling of forgery image variations. To increase pronounced discriminability within different synthetic images, we further introduce a Conditional Supervised Contrastive (CSC) objective. Extensive experiments on popular SID benchmarks demonstrate the state-of-the-art performance of our framework.

</details>

### 103. ISPCloak: Weaponizing ISP for Optimization-Free Physical Camouflage against Deepfake Detectors

📄 [arXiv](https://arxiv.org/abs/2607.21897)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`deepfake detector`、`ISP pipeline`、`sensor noise`、`physical camouflage`、`optimization-free`

👤 **作者**：Jiale Zhao

- 🎯 **研究动机**：亟需评估深伪检测器的最坏情况鲁棒性。当前取证范式存在根本盲区：检测器擅长捕捉数字合成伪影，但当 AI 生成内容被披上真实物理成像特征时有效性急剧下降——真实照片固有由光学传感器与 ISP 流水线烙印的硬件统计签名，纯数据驱动的生成模型本质上缺失这些特征。
- 🔬 **研究方法**：提出免优化的对抗攻击框架 ISPCloak，将 ISP 流水线武器化以误导检测器：先用可逆 ISP 网络把图像投射到 RAW 域，再注入真实泊松-高斯传感器噪声并做前向 ISP 重建，把真实相机的复杂统计先验无缝烙印到 AI 生成图像上；配合生成伪影抑制与自适应掩码，无需昂贵的梯度扰动即可快速生成对抗样本。
- 📌 **结论**：大量实验表明，嵌入真实物理扰动能根本性破坏当前广泛的检测机制，在视觉改动不可察觉的前提下产生普遍可逃逸的对抗样本。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of generative models has spurred the critical need to evaluate the worst-case robustness of deepfake detectors. In this paper, we reveal a fundamental blind spot in current forensic paradigms: while existing detectors excel at capturing digital synthesis artifacts, their effectiveness drops drastically when AI-generated content is cloaked in authentic physical imaging characteristics. We posit that genuine photographs inherently possess hardware-intrinsic statistical signatures, which are imperceptible footprints imprinted by optical sensors and Image Signal Processing (ISP) pipelines, and are fundamentally absent in purely data-driven generative models. Driven by this insight, we propose ISPCloak, a novel optimization-free adversarial attack framework that explicitly weaponizes the ISP pipeline to mislead the judgment of deepfake detectors. Rather than relying on computationally expensive gradient perturbations, our method first employs an Invertible ISP network to project images into the RAW domain. Then, we seamlessly imprint the complex statistical priors of real cameras onto AI-generated images by injecting realistic Poisson-Gaussian sensor noise and conducting forward ISP reconstruction. Synergized with generative artifact suppression and adaptive masking, this streamlined physical simulation enables ultra-fast generation of adversarial examples. Extensive experiments show that embedding authentic physical perturbations fundamentally disrupts a broad range of current detection mechanisms, yielding universally evasive adversarial examples with imperceptible visual alterations.

</details>

### 104. Learning to Falsify: Hierarchical Multiple Instance Learning for High Resolution AI-Generated Image Detection

🐙 [Code](https://github.com/HuiGuanLab/LTF.git)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`high-resolution image`、`multiple instance learning`、`local artifact`、`test-time aggregation`

👤 **作者**：Haoran Chen、Yongwei Wang、Jianfeng Dong

- 🎯 **研究动机**：生成模型的进步使合成图像日益逼真，可靠且可泛化的检测面临更大挑战。现有方法依赖整体图像级分类，可能忽略局部伪影，在高分辨率图像中问题尤为突出。
- 🔬 **研究方法**：将任务形式化为证伪驱动的多示例学习（MIL）：单个伪造图块即可证伪整图，而真实图像要求全部图块真实。提出层级 MIL 框架 LTF，把图像建模为不同空间层级的多个实例包并按证伪原则聚合预测；训练时引入 Cross-Shuffle 促使模型学习局部伪影证据而非图像级捷径；另提出即插即用的证伪驱动测试时聚合策略 FATAS，通过聚合图块级预测把同一原则扩展到现有检测器。
- 📌 **结论**：大量实验表明 LTF 在多个基准上取得强泛化与鲁棒性；FATAS 无需重训练即可在高分辨率场景显著提升代表性检测器的性能。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in generative models have made synthetic images increasingly photorealistic, posing growing challenges to reliable and generalizable detection of AI-generated images. Existing methods typically rely on holistic image-level classification, which may overlook local artifacts, especially in high-resolution images. To address this limitation, we formulate this task as a falsification-driven multiple instance learning problem, where a single fake patch can falsify the whole image, while a real image requires all patches to be authentic. Based on this formulation, we propose Learning to Falsify (LTF), a hierarchical multiple instance learning framework that models an image as multiple bags of instances across different spatial levels and aggregates their predictions under the falsification-inspired principle. We further introduce Cross-Shuffle during training to encourage the model to learn local artifact evidence rather than image-level shortcuts. Furthermore, we propose the Falsification-driven Test-time Aggregation Strategy (FATAS), a plug-and-play module that extends the same falsification-inspired principle to existing detectors by aggregating patch-level predictions. Extensive experiments demonstrate that LTF achieves strong generalization and robustness across multiple benchmarks, while FATAS substantially improves representative detectors in high-resolution scenarios without retraining. Code is available at https://github.com/HuiGuanLab/LTF.git

</details>

### 105. LEGO: LoRA-Enabled Generator-Oriented Framework for Synthetic Image Detection

📄 [arXiv](https://arxiv.org/abs/2605.04445) · 🐙 [Code](https://github.com/seanstep/LEGO_LoRA_Enabled_Generator_Oriented_Framework)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`synthetic image`、`LoRA`、`generator-specific artifacts`、`modular routing`、`data efficiency`

👤 **作者**：Ran Ran、Jiwei Wei、Shuchang Zhou、Ke Liu、Zheng Ziqiang、Caiyan Qin

- 🎯 **研究动机**：生成技术的快速进步使合成图像愈发难以辨别，亟需鲁棒检测器对抗虚假信息。现有方法主要依赖跨生成器共享的普适伪影线索，但随生成器多样性增加，这些线索的交集不断缩小、削弱泛化；反之仅依赖生成器特有伪影又会让检测器过拟合特定伪造模式。
- 🔬 **研究方法**：提出 LEGO 框架：用 MLP 调制多个 LoRA 模块（各自预训练以捕捉特定生成器的伪影），再经注意力融合特征。两阶段学习与组合特化伪影表征：先在单生成器数据上训练各 LoRA 模块学习生成器特有表征；随后冻结 LoRA，在混合生成器数据上训练 MLP 路由与注意力层动态调节各模块贡献。模块化设计支持随新生成器出现插入新 LoRA 模块。
- 📌 **结论**：使用不到 3 万张训练图像（不足主要基线训练数据量的 10%）、每阶段仅 5 个 epoch，LEGO 的平均性能仍显著优于先前 SOTA 方法。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of generative technologies has made synthetic images increasingly difficult to distinguish from real ones, creating an urgent need for robust detectors that can counter misinformation. Existing methods, however, mainly rely on universal artifact cues shared across generators. We observe that the intersection of these cues shrinks as generator diversity increases, which weakens generalization. Conversely, relying only on generator-specific artifacts can overfit the detector to particular forgery patterns. To address this challenge, we propose LEGO (LoRA-Enabled Generator-Oriented Framework). LEGO uses an MLP to modulate multiple Low-Rank Adaptation (LoRA) blocks, each pretrained to capture artifacts from a specific generator, and then fuses their features through attention. Unlike methods that seek a single universal solution, LEGO learns and composes specialized artifact representations in two stages. First, each LoRA module is trained on a single-generator dataset to learn generator-specific representations. The LoRA modules are then frozen, and the MLP router and attention layers are trained on mixed-generator data to regulate each module's contribution dynamically. This modular design allows LEGO to incorporate new LoRA modules as generators emerge. With fewer than 30,000 training images, less than 10% of the training data used by major baselines, and only five epochs per stage, LEGO nevertheless achieves substantially better average performance than prior state-of-the-art methods. The code is available at https://github.com/seanstep/LEGO_LoRA_Enabled_Generator_Oriented_Framework.

</details>

### 106. REPSR: Reconstruction Error Phase Structure Response for AI-Generated Image Detection

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`AI-generated image`、`phase structure`、`reconstruction error`、`lightweight deployment`

👤 **作者**：Guochang Li

- 🎯 **研究动机**：扩散模型等生成模型显著提升图像生成质量，伪造图像的可辨别性面临严峻挑战并引发滥用担忧。基于信号理论中「相位携带结构信息」的视角，可构建以相位特征为主导的生成图像检测框架。
- 🔬 **研究方法**：提出重建误差相位结构响应（REPSR）：用编码器重建图像以放大相位结构差异，对原图与重建残差进行相位频带分析，构建多维相位特征供轻量分类器判别；其中 VAE 重建器可离线预计算，在线检测后端仅 0.56M 参数。
- 📌 **结论**：实验表明该方法具备清晰物理意义与可解释的可视化路径，跨域生成器泛化稳定；仅 0.56M 在线参数的轻量后端使其适合资源受限场景部署。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid development of generative models such as diffusion models, the quality of image generation has improved significantly, posing significant challenges to the distinguishability of forged images while also bringing concerns about misuse. Based on the perspective from signal theory that phase carries structural information, this study proposes a phase feature-dominated generated image detection framework: Reconstruction Error Phase Structure Response (REPSR). The framework employs an encoder to reconstruct images, thereby amplifying phase structural differences, and performs phase frequency band analysis on both the original image and reconstruction residuals to construct multi-dimensional phase features for lightweight classifier discrimination. Experimental results demonstrate that the proposed method possesses clear physical meaning and interpretable visualization pathways, exhibits stable cross-domain generator generalization, and features a lightweight backend detection module with only 0.56M online parameters (the VAE reconstructor can be precomputed offline), making the online detection stage suitable for deployment in resource-constrained scenarios.

</details>

### 107. Simplicity Prevails: The Emergence of Generalizable AIGI Detection in Visual Foundation Models

📄 [arXiv](https://arxiv.org/abs/2602.01738)　📅 2026　🏷 ACM MM 2026

**关键词**：`analysis`、`AIGI detection`、`visual foundation model`、`frozen features`、`in-the-wild generalization`

👤 **作者**：Yue Zhou、Xinan He、Kaiqing Lin、Bing Fan、Feng Ding、Bin Li

- 🎯 **研究动机**：专用 AIGI 检测器在精选基准上常近乎完美，但在真实场景中性能大幅退化；AIGI 检测泛化的进步是否必须依赖日益复杂的任务特化取证设计，值得系统重审。
- 🔬 **研究方法**：证明冻结的现代视觉基础模型（VFM）特征加轻量分类器即构成可泛化 AIGI 检测的极强基线：使用 Perception Encoder、MetaCLIP 2、DINOv3 等代表性现代编码器，在标准基准、近期未见生成器与真实场景分布上全面评测，并分析该简单设置如此有效的原因。
- 📌 **结论**：该简单基线在各设置下持续持平或超越近期专用检测器，真实场景增益尤显著；分析收敛支持 VFM 的强取证可分性与预训练中接触合成网络内容密切相关——VLM 表现为与伪造概念的语义对齐，自监督模型表现为对生成分布的隐式判别。局限是对传输退化严重脆弱、纯 VAE 重建与局部编辑上表现差。结果表明泛化进展更依赖保留与利用强预训练表征，而非更复杂的任务特化设计。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Specialized detectors for AI-generated images (AIGI) often achieve near-perfect accuracy on curated benchmarks, yet their performance degrades substantially in realistic, in-the-wild scenarios. In this work, we show that frozen features from modern Vision Foundation Models (VFMs), combined with a lightweight classifier, form a remarkably strong baseline for generalizable AIGI detection. Using representative modern encoders, including Perception Encoder, MetaCLIP 2, and DINOv3, we conduct a comprehensive evaluation across standard benchmarks, recent unseen generators, and challenging in-the-wild distributions. Across these settings, this simple baseline consistently matches or outperforms recent specialized detectors, with particularly large gains in realistic scenarios. We further investigate why this simple setup is so effective. Our analyses provide converging evidence that the strong forensic separability of modern VFMs is closely related to their exposure to synthetic web content during pre-training. In Vision-Language Models, this manifests as semantic alignment with forgery-related concepts, while in Self-Supervised Learning models it appears as implicit discrimination of generative distributions. Although a fully controlled pre-training study is beyond the scope of this work, multiple complementary analyses support this interpretation. We also identify important limitations. While modern VFMs are highly effective for global AIGI detection, they remain vulnerable to severe transmission degradation and perform poorly on pure VAE reconstruction and localized editing. Overall, our results suggest that progress in generalizable AIGI detection may depend more on preserving and leveraging strong pretrained representations than on increasingly complex task-specific forensic designs. Our code and pre-trained models are publicly available at ModelScopeand HuggingFace.

</details>

### 108. Smoothing the Semantic Landscape: Generalizable AI-Generated Image Detection via Text-Induced Flatness

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`AIGI`、`flatness optimization`、`text-prompt perturbation`、`entropy-based anchor`、`cross-generator generalization`

👤 **作者**：Haifeng Zhang、Xiuli Bi

- 🎯 **研究动机**：生成模型的进步暴露图像伪造检测器的根本弱点：常无法泛化到未见合成方法。该工作把失败归因于一种优化病态——检测器过拟合与生成源耦合的伪影、收敛到尖锐解，导致生成器偏移下决策边界不稳定。
- 🔬 **研究方法**：提出几何优化框架，把多样文本提示视作图文联合空间中的结构化语义扰动：引入基于熵的锚选择机制，丢弃歧义提示条件、为每个输入保留语义兼容的锚；在锚上施加两个互补正则——扰动一致性正则强制邻近语义条件下预测稳定、鼓励决策函数局部平滑，流形扩张正则保持残差空间特征多样性、缓解表征坍缩，共同引导优化走向更平坦、更可迁移的解。
- 📌 **结论**：多基准实验表明该方法显著提升跨生成器泛化，平均准确率超越先前 SOTA 方法 5.65%。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in generative models have exposed a fundamental weakness of image fake detectors: they often fail to generalize to unseen synthesis methods. We attribute this failure to an optimization pathology in which detectors overfit to source-coupled artifacts and converge to sharp solutions, resulting in unstable decision boundaries under generator shifts. To address this issue, we propose a geometric optimization framework that treats diverse textual prompts as structured semantic perturbations in the joint image--text space. To ensure that these perturbations provide reliable supervision, we introduce an entropy-based anchor selection mechanism that discards ambiguous prompt conditions and retains semantically compatible anchors for each input. Based on these anchors, we further impose two complementary regularizations: (i) perturbation consistency regularization, which enforces stable predictions across nearby semantic conditions and encourages local smoothness of the decision function; and (ii) manifold expansion regularization, which preserves feature diversity in the residual space and alleviates representation collapse. Together, these components steer optimization toward flatter and more transferable solutions. Extensive experiments on multiple benchmarks show that our method substantially improves cross-generator generalization, outperforming previous state-of-the-art methods by 5.65% in average accuracy.

</details>

### 109. Towards Generalizable Deepfake Detection: Mitigating Training Bias via Generalization Bound Tightening

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`deepfake`、`Rademacher complexity`、`generalization bound`、`CLIP`、`feature augmentation`

👤 **作者**：Wenyi Wang、Ce Zhu

- 🎯 **研究动机**：深伪检测面临关键的跨域泛化挑战：现有方法常过拟合数据集特定的伪影捷径，缺乏可泛化检测器设计的原理性理论指导。
- 🔬 **研究方法**：开展基于 Rademacher 复杂度的泛化界分析，揭示检测器泛化误差上界与训练中真/假样本的特征空间距离强相关；据此提出基于 CLIP 的检测框架 GenDet-CLIP：类不变特征增强通过协作特征对齐收紧泛化界，余弦平衡一致性约束缓解检测器训练中的非对称收敛偏置。
- 📌 **结论**：在主流深伪基准上取得 SOTA 的跨数据集与跨方法性能：平均帧级 AUC 提升 1.1%，视频级跨数据集 AUC 提升 1.7%，跨方法 AUC 提升 0.6%，验证了理论驱动设计的有效性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deepfake detection faces a critical cross-domain generalization challenge, as existing methods often overfit to dataset-specific artifact shortcuts and lack principled theoretical guidance for generalizable detector design. In this work, we conduct a Rademacher complexity-based generalization bound analysis, revealing that a detector's generalization error upper bound is strongly correlated with the feature-space distance between real and fake training samples. Guided by this insight, we propose GenDet-CLIP, a CLIP-based deepfake detection framework that (i) employs Class-Invariant Feature Augmentation to tighten the generalization bound via collaborative feature alignment, and (ii) introduces a Cosine Balance Consistency Constraint to mitigate the asymmetric convergence bias during detector training. Extensive experiments on mainstream deepfake benchmarks show that GenDet-CLIP achieves state-of-the-art cross-dataset and cross-method performance, improving average frame-level AUC by 1.1%, video-level cross-dataset AUC by 1.7%, and cross-method AUC by 0.6%, validating the effectiveness of our theory-driven design.

</details>


### 音视频深度伪造检测

### 110. Beyond Human-Made Beats: Measurement and Analysis of AI-Generated Music on SoundCloud

📅 2026　🏷 ACM MM 2026

**关键词**：`analysis`、`AI-generated music`、`SoundCloud`、`social media measurement`、`audio mimicry`

👤 **作者**：Yupeng He、Yiming Zhu、Qiming Ye、Pan Hui、Gareth Tyson

- 🎯 **研究动机**：生成式 AI 的快速进步使在线平台上 GenAI 音乐爆发，引发社会与伦理关切；尽管其对以人为核心的创作社区冲击明显，对真实社交环境中 GenAI 音乐的实证分析仍然稀缺。
- 🔬 **研究方法**：对 SoundCloud 上分享的社交 GenAI 音乐开展首个大规模分析：基于 2022 年 1 月 1 日至 2025 年 6 月 30 日期间 18,382 位艺术家发布的 72,227 条 GenAI 音轨，刻画音频属性、上传模式与社区接受度；调查音频模仿（audio mimicry）现象，即许多艺术家的风格被 AI 音乐模仿；并设计轻量多模态 AI 音乐检测器与 SOTA 方法对比评测。
- 📌 **结论**：分析揭示显著的社会技术摩擦与针对 GenAI 内容升高的毒性；融入社交互动特征后，轻量检测器达到与重量级黑盒深度学习模型相当的性能，同时提供可解释性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of generative AI has led to an explosion of GenAI music on online platforms, raising societal and ethical concerns. Despite its impact on human-centric creative communities, empirical analyses of GenAI music in real-world social environments remain scarce. In this paper, we perform the first large-scale analysis of social GenAI music shared via SoundCloud. Using a dataset of 72,227 GenAI tracks (posted by 18,382 artists from January 1st, 2022 to June 30th, 2025), we characterize their audio attributes, upload patterns, and community reception, revealing significant socio-technical frictions and increased toxicity towards GenAI content. We also investigate the phenomena of audio mimicry, finding that many artists are mimicked in their style by AI music. Finally, we design a lightweight multimodal AI music detector and benchmark it against the state-of-the-art. We demonstrate that by integrating social engagement features, tour model achieves performance comparable to heavyweight black-box deep learning models, while also providing explainability. Our work provides insights into the socio-technical dynamics of AI music, advancing the core tenets of responsible multimedia ecosystems.

</details>

### 111. DDL: A Large-Scale Dataset for Deepfake Detection and Localization in Diversified Real-World Scenarios

🐙 [Code](https://github.com/inclusionConf/DDL)　📅 2026　🏷 ACM MM 2026

**关键词**：`benchmark`、`deepfake detection`、`manipulation localization`、`fine-grained annotation`、`large-scale dataset`

👤 **作者**：Changtao Miao、…、Joey Zhou

- 🎯 **研究动机**：AIGC 的进步加剧恶意深伪内容滥用，可靠的深伪检测成为应对关键。现有检测模型多只输出二元分类结果、缺乏可解释性；引入空间篡改掩码或时间伪造段的方法又受数据集限制而效果欠佳——现有深伪数据集大多仅有二元标签，伪造场景与深伪类型多样性不足、规模较小，难以支撑复杂真实场景。
- 🔬 **研究方法**：构建大规模深伪检测与定位数据集 DDL：含 1.4M+ 伪造样本、覆盖 80 种深伪方法（7 种生成架构）；纳入 7 种经典与 3 种新颖伪造模式；覆盖 3 类场景与 3 种模态；并提供 1.18M+ 精确空间掩码与 0.23M+ 精确时间段的细粒度伪造标注。
- 📌 **结论**：DDL 为复杂真实场景伪造提供更具挑战性的评测基准，并为构建下一代深伪检测、定位与可解释性方法提供关键数据支撑。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in AIGC have exacerbated the misuse of malicious deepfake content, making the development of reliable deepfake detection methods an essential means to address this challenge. Although existing deepfake detection models demonstrate outstanding performance in detection metrics, most methods only provide simple binary classification results, lacking interpretability. Recent studies have attempted to enhance the interpretability of classification results by providing spatial manipulation masks or temporal forgery segments. However, due to the limitations of forgery datasets, the practical effectiveness of these methods remains suboptimal. The primary reason lies in the fact that most existing deepfake datasets contain only binary labels, with limited variety in forgery scenarios, insufficient diversity in deepfake types, and relatively small data scales, making them inadequate for complex real-world scenarios. To address this predicament, we construct a novel large-scale deepfake detection and localization (DDL) dataset containing 1.4M+ forged samples and encompassing 80 distinct deepfake methods. The DDL design incorporates four key innovations: (1) Comprehensive Deepfake Methods (covering 7 different generation architectures and a total of 80 methods), (2) Varied Manipulation Modes (incorporating 7 classic and 3 novel forgery modes), (3) Diverse Forgery Scenarios and Modalities (including 3 scenarios and 3 modalities), and (4) Fine-grained Forgery Annotations (providing 1.18M+ precise spatial masks and 0.23M+ precise temporal segments). Through these improvements, our DDL not only provides a more challenging benchmark for complex real-world forgeries but also offers crucial support for building next-generation deepfake detection, localization, and interpretability methods. The dataset and supplemental materials are publicly available at https://github.com/inclusionConf/DDL.

</details>

### 112. DIMF: Dual-Identity Mamba Fusion for Source-Aware Deepfake Detection

🐙 [Code](https://github.com/aiai-9/DIMF)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`face-swap deepfake`、`identity replacement`、`Mamba fusion`、`source-free inference`

👤 **作者**：Sahil Kumar、Honggang Wang

- 🎯 **研究动机**：换脸检测器常因依赖随合成管线与采集条件变化的渲染器特有伪影而泛化不佳。不同于既有路线，该工作针对身份替换伪造——供体身份信息被结合进接受者面部上下文的伪造类型。
- 🔬 **研究方法**：提出源感知训练与无源推理框架 DIMF：把成对源参考（身份替换样本的身份供体）作为特权训练监督；共享 ConvNeXt-V2 骨干经仅训练期使用的跨身份 Mamba 分支与身份差距监督微调，冻结扩散通路提供辅助正则；推理时移除全部源依赖与扩散组件，留下 88M 参数的单图检测器。
- 📌 **结论**：仅在 FaceForensics++ 上训练、在 5 个未见基准上不做目标域微调评测，DIMF 平均 AUC 达 84.25，超最强协议对齐的扩散引导基线 2.37 点，其中 DiffSwap 上提升 7.23 点；供体分配与匹配骨干对照支持「结构化源-目标对应」是增益来源之一。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Face-swap detectors often generalize poorly because they rely on renderer-specific artifacts that vary across synthesis pipelines and acquisition conditions. We instead target identity-replacement forgeries, where donor identity information is combined with the recipient's facial context. We introduce DIMF, a source-aware training and source-free inference framework that uses paired source referencesidentity donors for identity-replacement samplesas privileged training supervision. A shared ConvNeXt-V2 backbone is fine-tuned through a training-only Cross-Identity Mamba branch and Identity Gap Supervision, while a frozen diffusion pathway provides auxiliary regularization. At inference, all source-dependent and diffusion components are removed, leaving an 88 M-parameter single-image detector. Trained only on FaceForensics++ and evaluated without target-domain fine-tuning on five unseen benchmarks, DIMF achieves an average AUC of 84.25, exceeding the strongest protocol-aligned diffusion-guided baseline by 2.37 points, including a 7.23-point gain on DiffSwap. Donor-assignment and matched-backbone controls support structured sourcetarget correspondence as a contributor to the observed gains. Code: https://github.com/aiai-9/DIMF.

</details>

### 113. Generalizing Video DeepFake Detection by Self-generated Audio-visual Pseudo-fakes

📄 [arXiv](https://arxiv.org/abs/2604.09110)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`audio-visual deepfake`、`pseudo-fake`、`real-data-only training`、`generalization`

👤 **作者**：Zihe Wei、Yuezun Li

- 🎯 **研究动机**：视频深伪检测日益紧迫。现有方法利用视频中音视频信息、以专门架构建模跨模态对应并依赖公开数据集训练，但训练集多样性有限，天然限制对未见案例的泛化，真实场景中效果常退化。
- 🔬 **研究方法**：提出简单有效的方法 AVPF，通过自生成的音视频伪伪造样本训练以显著增强模型泛化：核心思想是构造包含真实世界深伪中常见多样音视频对应模式的伪伪造训练样本；AVPF 完全由真实样本生成，训练只依赖真实数据与 AVPF，无需任何真实深伪样本。
- 📌 **结论**：多个标准数据集上的大量实验证明强泛化性，平均性能提升最高达 7.4%，同时验证了「无需真实伪造数据也能获得跨域泛化」的训练路线可行性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Detecting video deepfakes has become increasingly urgent in recent years. Given the audio-visual information in videos, existing methods typically expose deepfakes by modeling cross-modal correspondence using specifically designed architectures with publicly available datasets. While they have shown promising results, their effectiveness often degrades in real-world scenarios, as the limited diversity of training datasets naturally restricts generalizability to unseen cases. To address this, we propose a simple yet effective method, called AVPF, which can notably enhance model generalizability by training with self-generated Audio-Visual Pseudo-Fakes. The key idea of AVPF is to create pseudo-fake training samples that contain diverse audio-visual correspondence patterns commonly observed in real-world deepfakes. We highlight that AVPF is generated solely from authentic samples, and training relies only on authentic data and AVPF, without requiring any real deepfakes. Extensive experiments on multiple standard datasets demonstrate the strong generalizability of the proposed method, achieving an average performance improvement of up to 7.4%.

</details>

### 114. LaP-Forensics: Latent-Pixel Consistency Guided Multimodal Reasoning for Deepfake Detection

📄 [arXiv](https://arxiv.org/abs/2607.25962)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`deepfake`、`DDIM inversion`、`latent-pixel consistency`、`multimodal reasoning`、`GRPO`

👤 **作者**：Yushe Cao、Canran Xiao

- 🎯 **研究动机**：最新生成模型产出的图像几乎没有明显视觉伪影，削弱了仅依赖表面外观的检测器及其解释；需要把 RGB 语义与基于重建的取证证据结合。
- 🔬 **研究方法**：提出 LaP-Forensics：冻结的 Stable Diffusion DDIM 逆变换-重建模型提供固定重建参考，其残差图度量局部相容性；独立投影器编码 RGB 图像与残差图后，结构化 Where/What/Why 模型输出文本分析与伪影掩码；监督微调后再用 GRPO，其奖励结合掩码重叠与输出结构、证据参考项；另设图像级分类头融合 RGB 与 DDIM 残差类别特征。
- 📌 **结论**：在 UniversalFakeDetect 上实现跨生成器检测、在 SynthScars 官方基准上取得具竞争力的伪影定位；受控的线索构造、反演视界、组件、奖励项与反事实分析支持残差流的效用；自由文本忠实度与后处理下的可靠性仍是开放局限。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent generative models can produce images with few obvious visual artifacts, weakening detectors and explanations that rely only on surface appearance. We present LaP-Forensics, a multimodal framework that augments RGB semantics with reconstruction-based forensic evidence. A frozen Stable Diffusion DDIM inversionreconstruction model provides a fixed reconstruction reference, and its residual map measures local compatibility with that reference. Independent projectors encode the RGB image and residual map before a structured WhereWhatWhy model predicts a textual analysis and an artifact mask. Supervised fine-tuning is followed by Group Relative Policy Optimization (GRPO), whose reward combines mask overlap with output-structure and evidence-reference terms. These text-side terms encourage the model to refer to the consistency map but do not constitute a verifier of free-form textual truth. A separate image-level head fuses RGB and DDIM-residual class features. Experiments show cross-generator detection on UniversalFakeDetect and competitive artifact localization on the official SynthScars benchmark. Controlled cue-construction, inversion-horizon, component, reward-term, and counterfactual analyses support the utility of the residual stream under the evaluated settings, while free-form textual faithfulness and reliability under post-processing remain open limitations.

</details>

### 115. MP-ADD: Multi-Prototype Authenticity Modeling with Decoupled Learning for Generalizable Audio Deepfake Detection

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`audio deepfake`、`multi-prototype modeling`、`Wav2Vec2`、`decoupled optimization`、`cross-domain EER`

👤 **作者**：Yiming Zhang、Haonan Cheng

- 🎯 **研究动机**：AIGC 的快速进步使合成与篡改语音日益逼真，可泛化的音频深伪检测（ADD）对多媒体安全不可或缺；现有系统多被构建为二元分类器，易过拟合攻击特有伪影，在未见攻击与域偏移下性能退化。
- 🔬 **研究方法**：提出 MP-ADD 框架，整合跨层表征增强学习与多原型真实性建模：GCRL 把语义分组音频增强与 Wav2Vec2 各层动态融合结合以提升表征鲁棒性；MPAM 学习多个真实性原型建模真实语音的多峰分布，配合结构一致性约束与两阶段解耦优化，稳定特征学习并限制欺骗梯度更新原型。在 ASVspoof 2019 LA、ASVspoof 2021 LA 与 DF 及 In-the-Wild 上评测。
- 📌 **结论**：MP-ADD 取得平均 EER 2.31%、In-the-Wild EER 6.08%，展示具竞争力的跨域泛化能力。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Rapid advances in artificial intelligence generated content (AIGC) have enabled increasingly realistic synthetic and manipulated speech, making generalizable audio deepfake detection (ADD) essential for multimedia security. Existing ADD systems are often formulated as binary classifiers and may overfit to attack-specific artifacts, leading to degraded performance under unseen attacks and domain shifts. To address this issue, we propose MP-ADD, a framework for generalizable audio deepfake detection that integrates Group-Augmented Cross-Layer Representation Learning (GCRL) and Multi-Prototype Authenticity Modeling (MPAM). GCRL combines semantically grouped audio augmentation with dynamic fusion of Wav2Vec2 layers to improve representation robustness. MPAM learns multiple authenticity prototypes to model the multimodal distribution of bonafide speech, together with a structural consistency constraint and two-stage decoupled optimization that stabilize feature learning and limit spoofing gradients from updating the prototypes. Evaluations of MP-ADD on ASVspoof 2019 LA, ASVspoof 2021 LA and DF, and In-the-Wild yield an average EER of 2.31% and an In-the-Wild EER of 6.08%, demonstrating competitive cross-domain generalization.

</details>

### 116. PDetective: Beyond Shallow Artifacts in Partial Deepfake Speech Detection

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`partial deepfake speech`、`speech editing`、`shallow decoding artifacts`、`cross-domain generalization`

👤 **作者**：Junhao Wang、Kun Wang、Li Lu、Peng Cheng、Zhongjie Ba、Kui Ren

- 🎯 **研究动机**：细粒度语音合成使部分深伪语音成为日益严峻的威胁；端到端语音编辑系统进一步实现声学与感知上无缝的部分伪造，导致现有部分深伪检测器系统性失效。调查揭示这些模型对模型特定的浅层解码伪影存在关键学习偏置，从根本上损害泛化。
- 🔬 **研究方法**：提出 PDetective 框架，通过针对性训练约束缓解依赖伪影的决策，促使模型学习更内在、稳定的表征；并构建超过 25 万条语音的大规模部分编辑欺骗数据集，以支撑和验证该框架。
- 📌 **结论**：实验表明 PDetective 显著提升跨域泛化：对未见编辑类伪造 EER 降低超 11%，跨数据集评测相对最优表现基线平均 EER 降低超 30%。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid advancement of fine-grained speech synthesis, partial deepfake speech has emerged as an increasingly concerning threat. Recent end-to-end speech editing systems further exacerbate this challenge by enabling acoustically and perceptually seamless partial forgeries, leading to the systematic failure of existing partial deepfake detectors. Our investigation of existing partial deepfake detection models reveals that these models exhibit a critical learning bias toward model-specific shallow decoding artifacts, which fundamentally undermines their generalization. To address this issue, we propose PDetective, a framework that mitigates artifact-dependent decision-making through targeted training constraints, encouraging the model to learn more intrinsic and stable representations. We further introduce a large-scale partial editing spoofing dataset comprising more than 250k utterances to underpin and validate our framework. Experiments demonstrate that PDetective significantly improves cross-domain generalization, reducing EER by over 11% on unseen editing-based forgeries, and achieving an average EER reduction of over 30% relative to the best-performing baselines in cross-dataset evaluations.

</details>

### 117. SAFER: Sequential Adaptive Forensic Evidence Reasoning for Generalizable Visual Forensics

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`visual forensics`、`sequential evidence reasoning`、`adaptive expert routing`、`accuracy-efficiency trade-off`

👤 **作者**：Jiafeng Li、Kai Li、Ying Wen

- 🎯 **研究动机**：在编辑、AI 生成内容与深伪合成等异构篡改时代，取证线索在不同篡改 track 与样本间高度多样；现有方法遵循静态一次推理范式，所有输入共用同一计算图与证据路径，对需要不同类型与数量证据的可泛化取证日益受限。
- 🔬 **研究方法**：提出先验引导的取证智能体 SAFER，把伪造分析重构为预算感知的序贯证据推理问题：轻量多尺度前端先导出初始取证先验；策略网络据此在有限计算预算下从异构专家池自适应查询一个或多个 track 感知专家；可靠性感知决策聚合模块整合证据，产出伪造预测、篡改掩码与可解释报告；并引入结合模仿学习与强化学习的渐进策略学习使序贯决策可训练。
- 📌 **结论**：大量实验表明 SAFER 在多样场景下性能稳健，相比常规静态流水线取得更优的精度-效率折衷，为真实世界多媒体取证提供实用的自适应序贯证据推理新范式。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Image forensics has become increasingly challenging in the era of heterogeneous manipulations, where editing, AI-generated content, and deepfake synthesis expose highly diverse forensic cues across tracks and samples. Existing methods predominantly follow a static one-shot paradigm, in which all inputs are processed with the same computation graph and evidence pathway. Such a design is increasingly restrictive for generalizable forensics, where different samples and forgery tracks often require different types and amounts of evidence. In this work, we propose SAFER (Sequential Adaptive Forensic Evidence Reasoner), a prior-guided forensic agent that reformulates forgery analysis as a budget-aware sequential evidence reasoning problem. Given an input image, SAFER first derives an initial forensic prior using a lightweight multi-scale front-end. Conditioned on this prior, a policy network then adaptively queries one or more track-aware experts from a heterogeneous expert pool under a limited computation budget. The queried evidence is subsequently integrated by a reliability-aware decision aggregation module to produce the final forgery prediction, tampering mask, and explainable report. To make sequential decision-making trainable, we further introduce a progressive policy learning strategy that combines imitation learning and reinforcement learning. Extensive experiments show that SAFER achieves robust performance across diverse scenarios, while providing a more favorable accuracy--efficiency trade-off than conventional static pipelines. Our results suggest that adaptive sequential evidence reasoning offers a practical new paradigm for real-world multimedia forensics.

</details>

### 118. SphereVideo: Prototype-anchored Hyperspherical Boundary for Continual AI-generated Video Detection

📄 [arXiv](https://arxiv.org/abs/2608.01334)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`AI-generated video`、`continual learning`、`hyperspherical prototype`、`catastrophic forgetting`

👤 **作者**：Fei Li、Xinghan Li、Yu-Gang Jiang

- 🎯 **研究动机**：AI 生成视频（AIGV）检测要在真实视频与生成视频间判别；已有数据训练的检测器常无法泛化到新出现的生成模型，持续学习（CL）对提升适应性不可或缺，但该任务的 CL 框架仍缺乏探索。
- 🔬 **研究方法**：基于两个关键观察提出 SphereVideo：其一，真实视频呈紧凑特征分布——让真实特征在超球面上向真实原型聚拢并排斥 AI 生成样本以形成决策边界，该原型作为 CL 的稳定锚调节边界演化、缓解灾难性遗忘；其二，现有方法倾向仅依赖空间伪影捷径——引入在帧级与片段级建模真实数据时间动态的策略，通过强化真实数据建模促进原型学习与稳定边界形成。同时构建全面且具挑战性的基准。
- 📌 **结论**：大量实验表明 SphereVideo 取得更优的可塑性-稳定性折衷：在已见数据上超越先前方法 3.08%，在未见 AI 生成数据上超越 4.00%。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI-generated video (AIGV) detection aims to distinguish real videos from AI-generated ones. In practice, detectors trained on existing data often fail to generalize to newly emerging generative models, making this task challenging. Therefore, continual learning (CL) is essential for improving the adaptability. However, CL frameworks for this task remain underexplored. To this end, we propose SphereVideo, a novel CL framework for AIGV detection built on two key observations. First, real videos exhibit a compact feature distribution. Based on this, we encourage real video features to cluster around a real prototype on a hypersphere while repelling AI-generated samples, thereby establishing a decision boundary. This prototype serves as a stable anchor for CL, regulating boundary evolution and mitigating catastrophic forgetting. Second, existing methods tend to rely solely on spatial artifacts as shortcuts. To enhance temporal modeling, we introduce a strategy that models the temporal dynamics of real data at both frame and clip levels. By strengthening real data modeling, this strategy further facilitates learning a real prototype and forming a stable decision boundary. Moreover, we construct a comprehensive and challenging benchmark. Extensive experiments demonstrate that SphereVideo achieves an improved plasticity-stability trade-off, outperforming prior methods by 3.08% on seen data and 4.00% on unseen AI-generated data.

</details>

### 119. Synergizing Multi-Turn Chain-of-Thought Reasoning and Reinforcement Fine-Tuning for Detecting and Grounding Multi-Modal Manipulation

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`multimodal manipulation`、`chain-of-thought`、`reinforcement fine-tuning`、`DGM4`、`interpretability`

👤 **作者**：Saihui Hou、Zhaofeng He

- 🎯 **研究动机**：为应对假新闻威胁，多模态媒体篡改检测与定位任务（DGM4）日益受关注；现有方法多并行处理各子任务，造成逻辑不一致并忽视任务间因果依赖，且缺乏对伪造过程的解释。
- 🔬 **研究方法**：提出 SMART 框架，在多模态大模型上协同多轮思维链推理与强化微调：把 DGM4 重构为四阶段因果推理链，确保由粗到细的逻辑连贯；把数据集增广为含 23 万样本的结构化多轮 CoT 数据集以支撑显式可解释推理；采用基于规则的强化学习直接优化 IoU、token-F1 等取证指标。
- 📌 **结论**：SMART 消除逻辑悖论并提升多模态伪造检测的可解释性，在 DGM4 数据集全部子任务上取得 SOTA 性能。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

To address the threat of fake news, the task of Detecting and Grounding Multi-Modal Media Manipulation (DGM4) has gained increasing attention. However, existing methods predominantly treat these sub-tasks in parallel, resulting in logical inconsistencies and neglecting the causal dependencies between tasks. Moreover, current models lack explanations for the forgery process. In this paper, we propose SMART, a framework Synergizing Multi-Turn ChAin-of-Thought Reasoning and Reinforcement Fine-Tuning. Implemented upon a Multimodal Large Language Model, SMART introduces three key innovations. First, we reformulate the DGM4 task into a four stage causal reasoning chain to ensure coarse to fine logical coherence. Second, we augment the DGM4 dataset into a structured multi-turn Chain-of-Thought dataset comprising 230K samples to facilitate explicit interpretable reasoning. Finally, a rule based reinforcement learning strategy is employed to directly optimize forensic metrics such as IoU and token-F1. SMART eliminates logical paradoxes and improves interpretability in multimodal forgery detection. Experimental results demonstrate that SMART achieves state-of-the-art performance across all sub-tasks of the DGM4 dataset. Our dataset and code will be made publicly available.

</details>

### 120. ThinkOmni: A Reasoning-Driven Omni-Modal LLM Framework for Audio Forgery Detection and Localization

📄 [arXiv](https://arxiv.org/abs/2607.26553)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`audio forgery`、`audio LLM`、`chain-of-thought`、`temporal localization`

👤 **作者**：Kaiqing Lin、Bin Li、Haodong Li

- 🎯 **研究动机**：音频伪造检测与定位（AFDL）方法常过拟合数据集特定的低层伪影，对细微、局部化、未见篡改的泛化受限；基于音频大语言模型的方法把 AFDL 化为问答，但仍隐式建模取证证据，未把篡改线索与预测关联。
- 🔬 **研究方法**：提出推理驱动的全模态大模型框架 ThinkOmni，联合执行显式取证推理、欺骗检测与时间篡改定位：构建含结构化取证证据与推理标注的 10 万样本取证感知思维链数据集 FACoT；提出取证感知模态递增学习 FMIL，逐步将语义、声学与谱视觉表征对齐到 LLM 骨干以捕捉互补取证线索；提出取证一致多任务损失 FCML，以加权交叉熵与自适应定位损失协调推理生成、欺骗检测与时间定位。
- 📌 **结论**：大量实验表明 ThinkOmni 在检测与时间定位两项任务上均取得强跨数据集泛化；FACoT 数据集与 FMIL/FCML 设计为该方向提供可复用资源。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing audio forgery detection and localization (AFDL) methods often overfit dataset-specific low-level artifacts, limiting their generalization to subtle, localized, and unseen manipulations. Recent audio large language model (ALLM)-based approaches cast AFDL as question answering but still model forensic evidence implicitly, without linking manipulation cues to predictions. To bridge this gap, we propose ThinkOmni, a reasoning-driven omni-modal large language model that jointly performs explicit forensic reasoning, spoofing detection, and temporal manipulation localization. To enable explicit reasoning supervision, we construct Forensic-Aware Chain-of-Thought (FACoT), a 100K-sample dataset with structured forensic evidence and reasoning annotations. Leveraging FACoT, we introduce Forensic-Aware Modality-Incremental Learning (FMIL), which progressively aligns semantic, acoustic, and spectral-visual representations with the LLM backbone to capture complementary forensic cues. We further propose Forensic-Consistent Multi-task Loss (FCML), which combines weighted cross-entropy with an adaptive localization loss to coordinate reasoning generation, spoofing detection, and temporal localization. Extensive experiments show that ThinkOmni achieves strong cross-dataset generalization in both detection and localization. Code, models, data, and inference examples are available at https://beyond0814.github.io/ThinkOmni/.

</details>

### 121. Time-Frequency Consistency Learning for Robust Speech Deepfake Detection

📄 [arXiv](https://arxiv.org/abs/2607.17761) · 🐙 [Code](https://github.com/JunXue-tech/TFCL)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`speech deepfake`、`acoustic front-end`、`time-frequency consistency`、`robustness`

👤 **作者**：Jun Xue、Jiayu Xiong

- 🎯 **研究动机**：语音深伪检测（SDD）近年进步显著，但鲁棒性评测大多局限于可控加性噪声场景，缺乏对真实部署中声学前端（AFE）处理流水线引入复杂失真的系统研究。
- 🔬 **研究方法**：模拟统一 AFE 流水线（含回声消除、噪声抑制、自动增益控制与 VAD）并全面评测当前 SOTA 模型，发现 AFE 引入的非线性、时频耦合失真显著降低检测性能；据此提出时频一致性学习框架 TFCL，学习 AFE 处理前后保持稳定的欺骗表征：用注意力驱动的软对齐机制捕捉跨时序依赖，以应对 VAD 等造成的时段偏移；配合频域结构一致性约束强制特征不变性，应对频域线索的弱化与畸变。
- 📌 **结论**：大量实验表明 TFCL 有效缓解 AFE 处理导致的性能退化，显著提升真实场景下 SDD 的鲁棒性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recently, speech deepfake detection (SDD) has achieved significant progress. However, its robustness evaluation remains largely confined to controlled additive noise scenarios, lacking systematic investigation of the complex distortions introduced by acoustic front-end (AFE) processing pipelines in real-world deployments. In this work, we simulate a unified AFE pipeline comprising acoustic echo cancellation, noise suppression, automatic gain control, and voice activity detection (VAD), and conduct a comprehensive evaluation of current state-of-the-art models. The results show that the nonlinear and time-frequency coupled distortions introduced by AFE significantly degrade detection performance. To address this issue, we propose a Time-Frequency Consistency Learning (TFCL) framework, which aims to learn invariant spoofing representations that remain stable before and after AFE processing. We observe that AFE not only introduces temporal misalignment (e.g., segment-level shifts caused by VAD), but also weakens or distorts critical frequency-domain cues. To this end, TFCL employs an attention-driven soft alignment mechanism to capture cross-temporal dependencies, along with frequency-domain structural consistency constraints to enforce feature invariance. As a result, the model is able to maintain stable representations under both temporal perturbations and spectral distortions. Extensive experimental results demonstrate that the proposed method effectively mitigates the performance degradation caused by AFE processing, significantly improving the robustness of SDD in real-world scenarios. The code is available at https://github.com/JunXue-tech/TFCL.

</details>


### 图像篡改取证与内容定位

### 122. Agentic Tool-Augmented Reasoning for Explainable Image Forgery Detection

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`image forgery`、`agentic tool reasoning`、`forensic tools`、`explainability`

👤 **作者**：Jing Huang、Changtao Miao、Lin Tan、Weiwei Feng、Jianshu Li、Joey Zhou

- 🎯 **研究动机**：传统篡改检测只输出二分类分数或像素掩码、无可解释证据；现有 MLLM 方法的文字解释只是预定分类结果的事后言语化，并非真实推理产物。
- 🔬 **研究方法**：借鉴司法专家「实验分析—逻辑推理—科学证据」工作流提出 ATAR 框架，集成 22 个覆盖 7 个互补领域的取证工具，经多轮推理自主检测、定位并解释伪造。双流取证推理范式并行推进高层语义异常路径（放大可疑区域细查）与低层伪影路径（调用工具提取客观证据）；训练分两阶段：通用经验 SFT 以自动师生指导管线合成多轮工具使用轨迹，取证 RL 阶段以工具先验课程逐步移交控制权、以结构化证据奖励做过程级监督。实验覆盖 IMDL、Deepfake、DMDL、AIGC 检测。
- 📌 **结论**：ATAR 在 6 个零样本 IMDL 基准上取得 78.5% 平均图像级 F1，超最强 MLLM 基线 11.8 个百分点；在其他任务上与专用检测器保持竞争力，同时生成显著更忠实、更有依据的解释。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Conventional image forgery detection methods produce only binary scores or pixel-level masks without interpretable evidence, while recent multimodal large language model (MLLM)-based approaches generate textual explanations that are merely post-hoc verbalizations of pre-determined classification results rather than products of genuine reasoning. Inspired by the forensic workflow of human judicial experts---``experimental analysis -- logical reasoning -- scientific evidence''---we propose an Agentic Tool-Augmented Reasoning (ATAR) framework for explainable image forgery detection, integrating 22 specialized forensic tools spanning seven complementary domains to autonomously detect, localize, and explain image forgeries through multi-turn reasoning. Concretely, we propose a Dual-Stream Forensic Reasoning paradigm to emulate the experimental analysis process of forensic experts: (1) a high-level semantic anomaly path, which magnifies suspicious regions for fine-grained inspection; and (2) a low-level forgery artifact path, which invokes forensic tools to extract objective artifactual evidence. To this end, we further propose a Forensics Curriculum Learning training strategy. First, during the General Experience SFT stage, an automated teacher--student mentoring pipeline is designed to synthesize multi-turn tool-usage reasoning trajectories. Subsequently, during the Forensic Scene RL stage, a Tool Prior Curriculum is introduced to guide early tool exploration and progressively transfer control to the agent, while a Structured Evidence Reward provides fine-grained process-level supervision. Experiments across IMDL, Deepfake detection, DMDL, and AIGC detection show that ATAR achieves 78.5% average image-level F1 on six zero-shot IMDL benchmarks, surpassing the strongest MLLM baseline by 11.8 percentage points, and remains competitive with specialized detectors on other tasks, while producing substantially more faithful and grounded explanations.

</details>

### 123. Beyond Surface Artifacts: Capturing Shared Latent Forgery Knowledge Across Modalities

📄 [arXiv](https://arxiv.org/abs/2604.07763)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`modality-agnostic forgery`、`cross-modal generalization`、`dark modality`、`benchmark`

👤 **作者**：Jingtong Dou、Chuancheng Shi、Fei Shen、Tat-Seng Chua

- 🎯 **研究动机**：生成式 AI 使深度伪造从单模态操纵升级为复杂多模态威胁；现有取证技术过度依赖模态特定的表面伪影，忽视可变物理外观之下的共享潜在伪造知识，面对未见「暗模态」时性能灾难性退化。
- 🔬 **研究方法**：提出把多模态取证从「特征融合」重定义为「模态泛化」的范式转移，构建首个模态无关伪造（MAF）检测框架：显式解耦模态特定风格，提取跨模态潜在伪造知识；定义两个递进泛化维度——Weak MAF（向语义相关模态的迁移性）与 Strong MAF（对完全孤立暗模态信号的鲁棒性）；并引入 DeepModal-Bench 基准，集成多种多模态伪造检测算法并适配 SOTA 泛化学习方法，严格评估泛化极限。
- 📌 **结论**：研究验证了跨模态通用伪造痕迹的存在，通过 MAF 可实现对未见模态（含完全孤立信号的暗模态）的鲁棒检测，为通用多模态防御提供可行路径；DeepModal-Bench 为量化这类泛化能力提供了基准工具。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As generative artificial intelligence evolves, deepfake attacks have escalated from single-modality manipulations to complex, multimodal threats. Existing forensic techniques face a generalization bottleneck: by relying excessively on superficial, modality-specific artifacts, they neglect the shared latent forgery knowledge hidden beneath variable physical appearances. Consequently, these models suffer catastrophic performance degradation when confronted with unseen "dark modalities." To break this limitation, this paper introduces a paradigm shift that redefines multimodal forensics from conventional "feature fusion" to "modality generalization." We propose the first modality-agnostic forgery (MAF) detection framework. By explicitly decoupling modality-specific styles, MAF extracts the essential, cross-modal latent forgery knowledge. Furthermore, we define two progressive dimensions to quantify model generalization: transferability toward semantically correlated modalities (Weak MAF), and robustness against completely isolated signals of "dark modality" (Strong MAF). To rigorously assess these generalization limits, we introduce the DeepModal-Bench benchmark, which integrates diverse multimodal forgery detection algorithms and adapts state-of-the-art generalized learning methods. This study validates universal forgery traces and enables robust detection of unseen modalities through MAF, offering a promising path toward universal multimodal defense.

</details>

### 124. Bridging the Micro--Macro Gap: Frequency-Aware Semantic Alignment for Image Manipulation Localization

📄 [arXiv](https://arxiv.org/abs/2604.12341)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`manipulation localization`、`frequency-semantic alignment`、`diffusion editing`、`DCT`

👤 **作者**：Zhimin Chen

- 🎯 **研究动机**：图像篡改定位（IML）需同时应对取证伪影显眼的传统篡改与局部高度逼真的扩散生成编辑；现有方法单独依赖低层取证线索或高层语义，形成根本性的微观—宏观鸿沟，难以兼顾两类操纵。
- 🔬 **研究方法**：提出统一框架 FASA：自适应双频带 DCT 模块提取篡改敏感频率线索；在冻结 CLIP 表征上做 patch 级对比对齐，学习篡改感知语义先验；经语义—频率侧适配器将先验注入分层频率通路实现多尺度特征交互；原型引导、频率门控的掩码解码器整合语义一致性与边界感知定位，完成篡改区域预测。在 OpenSDI 与多个传统篡改基准上开展实验。
- 📌 **结论**：FASA 在 OpenSDI 与多个传统篡改基准上取得 SOTA 定位性能，并展现强跨生成器、跨数据集泛化能力，在常见图像退化下仍保持鲁棒——单一框架同时覆盖传统与扩散生成两类操纵。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As generative image editing advances, image manipulation localization (IML) must handle both traditional manipulations with conspicuous forensic artifacts and diffusion-generated edits that appear locally realistic. Existing methods typically rely on either low-level forensic cues or high-level semantics alone, leading to a fundamental micro--macro gap. To bridge this gap, we propose FASA, a unified framework for localizing both traditional and diffusion-generated manipulations. Specifically, we extract manipulation-sensitive frequency cues through an adaptive dual-band DCT module and learn manipulation-aware semantic priors via patch-level contrastive alignment on frozen CLIP representations. We then inject these priors into a hierarchical frequency pathway through a semantic-frequency side adapter for multi-scale feature interaction, and employ a prototype-guided, frequency-gated mask decoder to integrate semantic consistency with boundary-aware localization for tampered region prediction. Extensive experiments on OpenSDI and multiple traditional manipulation benchmarks demonstrate state-of-the-art localization performance, strong cross-generator and cross-dataset generalization, and robust performance under common image degradations.

</details>

### 125. Direct Discrepancy Replay: Distribution-Discrepancy Condensation and Manifold-Consistent Replay for Continual Face Forgery Detection

📄 [arXiv](https://arxiv.org/abs/2604.12941)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`continual forgery detection`、`distribution condensation`、`privacy-preserving replay`、`anti-forgetting`

👤 **作者**：Tianshuo Zhang、Siran Peng、Xiangyu Zhu、Zhen Lei

- 🎯 **研究动机**：持续人脸伪造检测（CFFD）要求在学习新兴伪造范式的同时不遗忘旧操纵；严格内存预算下，现有 replay 方法或存储稀疏历史人脸（伪造线索覆盖不足且引发隐私担忧），或依赖与过去决策边界绑定的检测器相关扰动，回放表征能力受限。
- 🔬 **研究方法**：提出 Distribution-Discrepancy Condensation（DDC）：在特征函数空间以代理分解建模真—伪分布差异，凝结成小型分布差异图库，避免存储原始人脸；Manifold-Consistent Replay（MCR）将这些图与当前真实人脸做保方差组合，合成携带旧任务伪造线索且兼容当前真实人脸统计的回放样本。在两个 CFFD 基准上评测，并作为即插即用替换验证对 5 种 replay 检测器的通用性。
- 📌 **结论**：该框架在两个 CFFD 基准上大幅降低遗忘并取得最佳整体结果；作为插件时在 5 种 replay 检测器上均带来一致改进，兼顾回放容量与隐私。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Continual face forgery detection (CFFD) requires detectors to learn emerging forgery paradigms without forgetting previously seen manipulations. Under strict memory budgets, existing replay-based CFFD methods either retain sparse historical faces, limiting forgery-cue coverage and raising privacy concerns, or use detector-dependent perturbations tied to past decision boundaries. To improve the representational capacity of replay while avoiding raw-face storage, we introduce Distribution-Discrepancy Condensation (DDC) to directly condense real-to-fake distribution discrepancies and Manifold-Consistent Replay (MCR) to perform distribution-level replay with current real faces. Specifically, DDC models the real-to-fake discrepancy via a surrogate factorization in characteristic-function space and condenses it into a tiny bank of distribution discrepancy maps. MCR synthesizes replay samples through variance-preserving composition of these maps with current-stage real faces, yielding samples that reflect previous-task forgery cues while remaining compatible with current real-face statistics. On two CFFD benchmarks, our framework substantially reduces forgetting and achieves the best overall results. As a plug-in replacement, our replay also consistently improves five replay-based detectors.

</details>

### 126. F$^{2}$-Adapter: A Focus-and-Forget Framework for Generalizable CLIP-based Face Forgery Detection

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`face forgery`、`CLIP adapter`、`sparse token routing`、`cross-dataset generalization`

👤 **作者**：Hao Jia

- 🎯 **研究动机**：跨数据集设定下的人脸深度伪造检测仍极具挑战；CLIP 适配虽展现强泛化潜力，但现有 adapter 方案仍会被无关视觉上下文干扰，并过度依赖主导却不鲁棒的伪影，削弱对未见或高质量伪造的泛化。
- 🔬 **研究方法**：在冻结 CLIP 图像编码器上构建 Focus-and-Forget 框架 F^2-Adapter：伪影聚焦机制对视觉 token 施加内容感知稀疏路由，降低无关区域干扰；捷径遗忘机制经课程化掩码在训练中逐步抑制高激活特征位置。二者互补：前者促使模型聚焦取证相关区域，后者抑制对易得线索的依赖、促进更可泛化取证模式的学习。开展大规模跨数据集实验。
- 📌 **结论**：跨数据集实验取得 SOTA，平均 AUC 达 90.4%，并在未见基准上一致超越强基线，验证「聚焦＋遗忘」组合对跨数据集人脸伪造泛化的有效性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deepfake detection under cross-dataset settings remains highly challenging. Although adapting CLIP has shown strong potential for generalizable face forgery detection, existing adapter-based solutions may still be distracted by irrelevant visual context and overly rely on dominant but non-robust artifacts, which weakens generalization to unseen or high-quality forgeries. To address this issue, we propose the F^2-Adapter, a Focus-and-Forget framework built on a frozen CLIP image encoder. Our method combines an artifact focusing mechanism, which introduces content-aware sparse routing over visual tokens to reduce interference from irrelevant regions, and a shortcut forgetting mechanism, which progressively suppresses highly activated feature locations during training through a curriculum-based masking strategy. These two components are complementary: the former encourages the model to concentrate on forensic-relevant areas, while the latter discourages over-reliance on easy cues and promotes the learning of more generalizable forensic patterns. Extensive cross-dataset experiments show that the proposed method achieves state-of-the-art performance, reaching an average AUC of 90.4% and consistently outperforming strong baselines on unseen benchmarks.

</details>

### 127. Fine-Grained Visual and Text Forgery Distillation for Media Manipulation Detection

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`media manipulation`、`cross-modal grounding`、`forgery distillation`、`multi-task learning`

👤 **作者**：Chenggang Yan

- 🎯 **研究动机**：生成模型使被操纵的图像与文本日益泛滥，威胁信息安全；现有媒体操纵检测方法难以捕获模态特定的伪造痕迹，也难以建模被篡改视觉区域与被操纵文本片段之间的跨模态交互，导致伪造类型预测与篡改区域定位性能退化。
- 🔬 **研究方法**：提出细粒度视觉—文本伪造蒸馏框架 Fiord：基于预训练多模态编码器，视觉区域伪造蒸馏模块构建跨域判别空间，利用多尺度空间与频率痕迹捕获细微伪造模式；文本片段伪造蒸馏模块经 token 级推理与跨模态 grounding 识别被篡改片段；统一多任务学习框架联合优化操纵定位、伪造类型预测与整体媒体真实性判定。在大规模基准数据集上实验并将开源全部代码。
- 📌 **结论**：实验验证各模块有效性，Fiord 在大规模基准数据集上超越 SOTA 方法，同步提升篡改定位与伪造类型预测能力。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid advancement of generative models, manipulated images and text have become increasingly prevalent, posing serious threats to information security. Existing media manipulation detection methods exhibit two key limitations: (1) they fail to capture modality-specific forgery trace. (2) they struggle to model the cross-modal interactions between tampered visual regions and manipulated text fragments. These result in degraded performance in predicting forgery types and grounding manipulated regions. To address these challenges, we propose Fiord, a fine-grained visual and text forgery distillation framework for multimodal media manipulation detection. Built upon a pretrained multimodal encoder, Fiord introduces a visual regional forgery distillation module and a text fragment forgery distillation module to capture fine-grained forgery traces. The former constructs a cross-domain discriminative space and leverages multi-scale spatial and frequency trace to capture subtle forgery patterns, while the latter identifies tampered fragments via token-level reasoning and cross-modal grounding. A unified multi-task learning framework further enables joint optimization of manipulation localization, forgery type prediction, and overall media authenticity. Extensive experiments demonstrate the effectiveness of each module, and our method outperforms the state-of-the-art methods on large-scale benchmark datasets. We will release all the source codes.

</details>

### 128. ForgeryVCR: Visual-Centric Reasoning via Efficient Forensic Tools in MLLMs for Image Forgery Detection and Localization

📄 [arXiv](https://arxiv.org/abs/2602.14098) · 🐙 [Code](https://github.com/youqiwong/ForgeryVCR)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`image forgery localization`、`visual-centric reasoning`、`forensic toolbox`、`strategic tool learning`

👤 **作者**：Shen Chen、Haowei Wang、Taiping Yao、Changsheng Chen、Bin Li、Shouhong Ding

- 🎯 **研究动机**：现有面向图像篡改检测与定位的 MLLM 普遍运行在文本中心思维链范式下；强迫模型用语言刻画不可感知的低层篡改痕迹必然引发幻觉——语言模态不足以表达像素级细粒度不一致。
- 🔬 **研究方法**：提出 ForgeryVCR，引入取证工具箱把不可感知痕迹物化为显式视觉中间体，进行以视觉为中心的推理；提出 Strategic Tool Learning 后训练范式：收益驱动的轨迹构造用于 SFT，工具效用奖励引导后续 RL 优化；使 MLLM 成为主动决策者，学会自发调用多视角推理路径，包括局部放大细粒度检查与压缩历史、噪声残差、频域中不可见不一致的分析。
- 📌 **结论**：ForgeryVCR 在检测与定位两项任务上均取得 SOTA 性能，展现更强泛化能力且工具冗余最小；代码已开源。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing Multimodal Large Language Models (MLLMs) for image forgery detection and localization predominantly operate under a text-centric Chain-of-Thought (CoT) paradigm. However, forcing these models to textually characterize imperceptible low-level tampering traces inevitably leads to hallucinations, as linguistic modalities are insufficient to capture such fine-grained pixel-level inconsistencies. To overcome this, we propose ForgeryVCR, a framework that incorporates a forensic toolbox to materialize imperceptible traces into explicit visual intermediates via Visual-Centric Reasoning. To enable efficient tool utilization, we introduce a Strategic Tool Learning post-training paradigm, encompassing gain-driven trajectory construction for Supervised Fine-Tuning (SFT) and subsequent Reinforcement Learning (RL) optimization guided by a tool utility reward. This paradigm empowers the MLLM to act as a proactive decision-maker, learning to spontaneously invoke multi-view reasoning paths including local zoom-in for fine-grained inspection and the analysis of invisible inconsistencies in compression history, noise residuals, and frequency domains. Extensive experiments reveal that ForgeryVCR achieves state-of-the-art (SOTA) performance in both detection and localization tasks, demonstrating superior generalization with minimal tool redundancy. The code is available at https://github.com/youqiwong/ForgeryVCR.

</details>

### 129. HexMIL: Hierarchical Attention MIL for Ante-Hoc Explainable Detection of AI-Manipulated CT Volumes

📄 [arXiv](https://arxiv.org/abs/2608.05101)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`medical deepfake`、`CT volume`、`multiple instance learning`、`ante-hoc attribution`

👤 **作者**：Orazio Pontorno、Luca Guarnera、Zahid Akhtar、Sebastiano Battiato

- 🎯 **研究动机**：生成模型操纵医学影像形成的医疗 deepfake 对临床流程构成实质威胁；现有检测器对未见生成架构泛化差且缺乏可解释性，两大短板使其难以在医疗场景落地。
- 🔬 **研究方法**：提出免掩码医疗 deepfake 检测器 HexMIL，仅需二值 volume 级监督：把 CT volume 分解为 patch 与 slice 两级层次，经独立门控注意力模块聚合，其权重直接组合成全分辨率 3D 注意体，在无任何像素级标注下定位被操纵子区域；不同于 Grad-CAM 等事后方法，注意力权重即分类决策的前向计算本身，提供 ante-hoc 且结构忠实的空间归因。在 M3DSynth 与 CT-GAN 上以「单一架构训练、未见架构测试」的跨生成器协议评测。
- 📌 **结论**：HexMIL 域外分类超所有基线 +9.1 AUC 与 +9.4 F1，并取得最佳平均 IoU 与 Pointing Game 定位得分，同步缓解泛化与可解释性两大短板。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The emergence of medical deepfakes, i.e., medical images manipulated by deep generative models, poses a significant threat to clinical workflows. However, existing detectors suffer from two critical limitations: poor generalization to unseen generative architectures for manipulation detection and lack of interpretability. In this context, we present HexMIL (Hierarchical EXplainable Multiple Instance Learning), a mask-free medical deepfake detector that simultaneously addresses both limitations using only binary volume-level supervision. HexMIL decomposes each CT volume into a two-level hierarchy of patches and slices, aggregated via independent Gated Attention modules whose weights are directly combined into a full-resolution 3D attention volume that localizes the manipulated sub-region without any pixel-level annotation. Unlike post-hoc methods such as Grad-CAM, HexMIL's attention weights constitute the exact forward computation driving the classification decision, providing ante-hoc and structurally faithful spatial attribution. We evaluate HexMIL on M3DSynth and CT-GAN datasets under a rigorous cross-generator generalization protocol, training on a single generative architecture and testing on unseen ones. HexMIL outperforms all baselines by +9.1 AUC and +9.4 F1 in out-of-domain classification, and achieves the best average IoU and Pointing Game score in localization. Project page: https://opontorno.github.io/hexmil/opontorno.github.io/hexmil.

</details>

### 130. HF-Printor: High-Frequency Enhanced Camera Fingerprint Extractor for Practical Source Camera Identification

🐙 [Code](https://github.com/Hillthon/HF-Printor)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`camera fingerprint`、`PRNU`、`Swin Transformer`、`limited-reference identification`

👤 **作者**：Quan Yuan

- 🎯 **研究动机**：提取 PRNU 指纹用于源相机识别（SCI）是多媒体取证的基础任务；现有基于 CNN 的 SOTA 提取器仍受非平坦图像语义噪声影响，且在可用图像有限（如少于十张）时表现不佳，难以满足实用需求。
- 🔬 **研究方法**：观察到 Transformer 骨干擅长抑制复杂场景语义但弱于保留 PRNU 相关高频线索，提出 HF-Printor：以 Swin Transformer 为骨干保留语义建模能力，同时引入 patch 级指纹对比学习、高频增强与频域指纹正则化，分别提升所提取指纹的判别性、稳定性与高频敏感性。在 VISION 与 Dresden 两个数据集上开展大量验证实验。
- 📌 **结论**：HF-Printor 仅用 3 张普通参考图像即实现超过 90% 的闭集识别准确率，并在实用的受限参考设定下一致超越竞争方法。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Extracting the photo-response non-uniformity (PRNU) fingerprints from images is a promising technique for source camera identification (SCI), a fundamental task in multimedia forensics. However, current state-of-the-art PRNU extractors built on CNN architectures remain sensitive to semantic noise from non?flat images and perform poorly when the number of available images is limited (e.g., fewer than ten). To fill this gap, we propose HF-Printor, a high-frequency enhanced camera fingerprint extractor for practical SCI. Our method is motivated by the fact that Transformer-based backbones are strong at suppressing complex scene semantics but weak at preserving PRNU-related high-frequency cues. We therefore retain their semantic modeling strength while explicitly enhancing high-frequency fingerprint extraction. Based on a Swin Transformer backbone with strong semantic modeling capability, HF-Printor incorporates patch-level fingerprint contrastive learning, high-frequency enhancement, and frequency-domain fingerprint regularization to improve the discriminability, stability, and high-frequency sensitivity of the extracted fingerprints. To evaluate the performance of the proposed HF-Printor, extensive validation experiments were conducted on the VISION and Dresden datasets, demonstrating that HF-Printor achieves over 90% closed-set identification accuracy with only three ordinary reference images, and consistently outperforms competing methods under practical limited-reference settings. Our code is available at https://github.com/Hillthon/HF-Printor.

</details>

### 131. Hierarchical Forensics for Digitally Forged ID Documents via MacroMicro Collaboration

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`forged ID document`、`hierarchical forensics`、`benchmark`、`macro-micro collaboration`

👤 **作者**：Peifeng Liu、Haoyi Deng、Bin Li、Yangxin Yu、Le-Qing Chen

- 🎯 **研究动机**：大量在线应用要求上传证件图像远程核验；图像编辑模型的快速进步使数字证件可被轻易篡改，伪造证件成为严重安全威胁；而多样、高保真伪造证件数据集的缺失限制了检测方法的开发与公平评测。
- 🔬 **研究方法**：首先构建 MFID（多类型伪造身份证件）基准，覆盖多样篡改类型并支持含未见证件版式与操纵类型的泛化设定；进而提出模拟人类由粗到细检查的分层取证框架 IDForenLLM：宏观级分析生成带显式证据或验证提案的结构化区域假设，再将可疑区域路由至专业微观模型协作分析以捕获细粒度伪影，最终聚合宏观数检测结果与微观精化结果实现精确定位。
- 📌 **结论**：在 MFID 与多个附加基准上的大量实验表明该方法取得一致改进，宏微观协作证据同时支撑伪造检测与精确定位。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Many online applications require users to upload ID document images for remote verification. With the rapid advancement of image editing models, digital ID images can now be manipulated with minimal effort, making forged IDs a serious security threat. However, the lack of diverse and high-fidelity forged ID datasets has limited the development and fair evaluation of detection methods. To address this gap, we introduce MFID (Multi-type Forged Identity Document), a comprehensive benchmark covering diverse tampering types and supporting generalization settings with unseen document layouts and manipulation types. Based on this resource, we propose IDForenLLM, a hierarchical forensic framework that mimics coarse-to-fine human inspection. The model first performs macro-level analysis to generate structured region hypotheses with explicit evidence or verification proposals, and then routes suspicious regions to specialized micro-level models for collaborative analysis to capture fine-grained tampering artifacts. The final predictions are obtained by aggregating macro-level detections and refined micro-level results. The combined evidence enables precise forgery localization. Extensive experiments on MFID and additional benchmarks demonstrate consistent improvements.

</details>

### 132. MARE: Multimodal Alignment and Reinforcement for Explainable Deepfake Detection via Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2601.20433)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`deepfake`、`vision-language model`、`RLHF`、`text-spatial alignment`

👤 **作者**：Xiangyang Luo

- 🎯 **研究动机**：深度伪造检测多被建模为分类或定位任务，而生成模型的快速进步对检测提出新要求；大型视觉—语言模型（VLM）在深度伪造检测与推理中的准确性与可靠性仍待提升，尤其缺少与空间证据对齐的可解释推理。
- 🔬 **研究方法**：提出 MARE，经多模态对齐与强化学习增强 VLM 的深度伪造检测与推理：设计纳入 RLHF 的综合奖励函数，激励生成文本—空间对齐且符合人类偏好的推理内容；引入伪造解耦模块从高层人脸语义中捕获内在伪造痕迹，增强真实性判定能力。对生成推理内容开展系统评测。
- 📌 **结论**：定量与定性实验均表明 MARE 在准确性与可靠性上达到 SOTA，能生成文本—空间对齐的忠实可解释推理。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deepfake detection is a widely researched topic that is crucial for combating the spread of malicious content, with existing methods mainly modeling the problem as a classification task or a localization task. The rapid advancements in generative models impose new demands on Deepfake detection. In this paper, we propose multimodal alignment and reinforcement for explainable Deepfake detection via vision-language models, termed MARE, which aims to enhance the accuracy and reliability of large vision-language models (VLMs) in Deepfake detection and reasoning. Specifically, MARE designs comprehensive reward functions, incorporating reinforcement learning from human feedback (RLHF), to incentivize the generation of text-spatially aligned reasoning content that adheres to human preferences. Besides, MARE introduces a forgery disentanglement module to capture intrinsic forgery traces from high-level facial semantics, thereby improving its authenticity detection capability. We conduct thorough evaluations on the reasoning content generated by MARE. Both quantitative and qualitative experimental results demonstrate that MARE achieves state-of-the-art performance in terms of accuracy and reliability.

</details>

### 133. Mining Forgery Traces from Reconstruction Error: A Weakly Supervised Framework for Multimodal Deepfake Temporal Localization

📄 [arXiv](https://arxiv.org/abs/2601.21458)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`deepfake temporal localization`、`weak supervision`、`masked autoencoder`、`contrastive learning`

👤 **作者**：Midou Guo、Qilin Yin、Wei Lu、Rui Yang

- 🎯 **研究动机**：现代深度伪造演化为局部化、间歇性操纵，需要细粒度时序定位以缓解数字安全风险；帧级标注成本高昂，使仅依赖视频级标签的弱监督方法成为现实必需。
- 🔬 **研究方法**：提出弱监督时序伪造定位框架 RT-DeepLoc：仅在真实数据上训练 Masked Autoencoder 学习内在时空模式，使其对伪造片段产生显著重建差异，为精准定位提供缺失的细粒度线索而无需稠密人工标注；设计非对称视频内对比损失 AICL，以重建线索引导真实特征紧凑性，建立稳定决策边界，在增强局部判别的同时保持对先进生成模型未见伪造的泛化。在包含 LAV-DF 的大规模数据集上实验。
- 📌 **结论**：RT-DeepLoc 在 LAV-DF 等大规模数据集上取得弱监督时序伪造定位 SOTA 性能，验证重建误差作为伪造线索来源的有效性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern deepfakes have evolved into localized and intermittent manipulations that require fine-grained temporal localization to mitigate severe digital security risks. The prohibitive cost of frame-level annotation makes weakly supervised methods a practical necessity, which rely only on video-level labels. To this end, we propose Reconstruction-based Temporal Deepfake Localization (RT-DeepLoc), a weakly supervised temporal forgery localization framework that identifies forgeries via reconstruction errors. Our framework uses a Masked Autoencoder (MAE) trained exclusively on authentic data to learn its intrinsic spatiotemporal patterns; this allows the model to produce significant reconstruction discrepancies for forged segments, effectively providing the missing fine-grained cues for accurate localization without demanding dense human annotations. To robustly leverage these indicators, we introduce a novel Asymmetric Intra-video Contrastive Loss (AICL). By focusing on the compactness of authentic features guided by these reconstruction cues, AICL establishes a stable decision boundary that enhances local discrimination while preserving generalization to unseen forgeries by advanced generative models. Extensive experiments on large-scale datasets, including LAV-DF, demonstrate that RT-DeepLoc achieves state-of-the-art performance in weakly-supervised temporal forgery localization.

</details>

### 134. Multi-Tool Image Editing Attribution in Facial Forgery

📄 [arXiv](https://arxiv.org/abs/2609.02751) · 🐙 [Code](https://github.com/ICTMCG/MIEA)　📅 2026　🏷 ACM MM 2026

**关键词**：`analysis`、`editing attribution`、`multi-tool editing`、`face forgery`、`curriculum learning`

👤 **作者**：Sheng Liu、Qiang Sheng、Yu Li、Juan Cao

- 🎯 **研究动机**：生成式 AI 工具使人人可凭一句话编辑肖像，催生从图像预测所涉编辑工具的编辑归因任务；现有方法持单工具假设、只能归因特定工具，无法处理日益常见、不同工具伪影复合交叠的多工具编辑场景。
- 🔬 **研究方法**：提出并探索多工具图像编辑归因任务 MIEA；为模拟真实人脸编辑操作构建 MultiEdit 数据集，含 500k+ 编辑人脸图像、覆盖换脸（Deepfake）与多种面部增强共 6 类编辑工具；基于数据分析发现设计归因方法：从空间与频域捕获可区分、局部感知的工具痕迹，辅以基于误差的课程学习策略应对多步编辑的复合伪影。
- 📌 **结论**：在至多 5 步编辑的人脸图像上优于 9 种对比方法，首次实现多工具编辑场景下的工具归因；MultiEdit 以 500k+ 图像、6 类工具支撑后续研究，代码与数据已开源。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As generative AI tools become increasingly powerful and easy to use, people can easily edit portrait images with a prompt, necessitating the task of image editing attribution, which predicts the involved editing tools from the given image. Existing attribution methods hold the single-tool assumption and can only attribute a specific editing tool, but struggle to handle the more complex and increasingly common multi-tool editing scenarios, where artifacts left by different editing tools are composite and overlapped. To address this gap, we explore Multi-Tool Image Editing Attribution (MIEA), which aims to identify multiple editing tools involved in a multi-tool edited facial image. To simulate the real-life editing operations on facial images, we then construct a new dataset, MultiEdit, which contains 500k+ edited facial images and covers six types of editing tools that support face swapping (Deepfake) and various facial enhancements. Inspired by the findings from data analysis, we design MIEA, a multi-tool attribution method that can capture distinguishable, locality-aware editing tool traces from both spatial and frequency domains with the support of an error-based curriculum learning strategy. Experiments show outperforms nine methods for facial images edited in at most five steps.Code, Data & Extended Materials: https://github.com/ICTMCG/MIEA

</details>

### 135. Open-Set Visual Text Forensics via Sparse-Constraint Rectified Flow

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`visual text manipulation`、`rectified flow`、`open-set generalization`、`anomaly localization`

👤 **作者**：Jiangling Zhang、Shuxuan Gao、Zeyu Chen、Yichao Liu、Yu Zhou

- 🎯 **研究动机**：快速演进的生成式 AI 使视觉文本操纵日益逃避取证检测器；判别式模型常过拟合特定伪造模式，对未见、开放集攻击的泛化受限。
- 🔬 **研究方法**：提出生成式检测器：通过估计把查询图像与真实视觉文本统计对齐所需的局部恢复代价来定位篡改，而非学习伪造特定决策边界；核心是面向检测改造 Flow Matching 的 Sparse-Constraint Rectified Flow（SC-RF），用于空间稀疏异常定位；辅以自监督 Artifact Injection 缓解数据稀缺、像素空间 Forensic-DiT 保留高频取证痕迹。在三个基准上评测，并开展零样本与压力测试分析。
- 📌 **结论**：在三个基准上取得 SOTA，F1 与 IoU 分别超第二名 3.2 与 4.8 个百分点，对未见文本编辑模式具强零样本性能；附加压力测试显示模型产生的局部和谐化会削弱现有检测器依赖的统计线索，揭示互补的脆弱性分析视角。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Rapidly evolving Generative AI enables sophisticated visual text manipulations that increasingly evade current forensic detectors. Existing discriminative models often overfit specific forgery patterns, limiting their generalization to unseen, open-set attacks. To address this challenge, we propose a generative detector that localizes tampering by estimating the local restoration cost required to align a query image with authentic visual-text statistics, rather than by learning forgery-specific decision boundaries. Specifically, we introduce Sparse-Constraint Rectified Flow (SC-RF), a detector-oriented adaptation of Flow Matching for spatially sparse anomaly localization. We further mitigate data scarcity via self-supervised Artifact Injection and preserve high-frequency forensic traces using a pixel-space Forensic-DiT. Extensive experiments on three benchmarks show that our method achieves state-of-the-art performance, surpassing the runner-up by 3.2 and 4.8 percentage points in F1 and IoU, respectively. In particular, the proposed detector demonstrates strong zero-shot performance on challenging unseen text editing patterns. We further provide an auxiliary stress-test analysis showing that local harmonization produced by our model can weaken the statistical cues relied upon by existing detectors, offering a complementary vulnerability-analysis perspective.

</details>

### 136. SurFITR: A Dataset for Surveillance Image Forgery Detection and Localisation

📄 [arXiv](https://arxiv.org/abs/2604.07101)　📅 2026　🏷 ACM MM 2026

**关键词**：`benchmark`、`surveillance forgery`、`image tampering localization`、`fine-grained editing`、`cross-domain evaluation`

👤 **作者**：Qizhou Wang、Guansong Pang、Christopher Leckie

- 🎯 **研究动机**：开放获取图像生成模型的进步引发伪造视觉证据的担忧；在全图合成或以物体为中心的大区域篡改数据上训练的现有伪造检测模型难以泛化到监控场景——监控影像中的篡改通常局部且细微，且场景视角多变、目标小或被遮挡、画质较低。
- 🔬 **研究方法**：构建监控风格图像篡改检测与定位数据集 SurFITR：经多模态 LLM 驱动的管线在多样监控场景中生成语义感知的细粒度编辑；含 137k+ 张分辨率与编辑类型各异的篡改图像，由多个图像编辑模型生成；对现有检测器开展域内与跨域系统评测。
- 📌 **结论**：现有检测器在 SurFITR 上显著退化；在 SurFITR 上训练则带来域内与跨域性能的双重实质提升；数据集含 137k+ 篡改图像并已在 GitHub 公开。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present the Surveillance Forgery Image Test Range (SurFITR), a dataset for surveillance-style image forgery detection and localisation, in response to recent advances in open-access image generation models that raise concerns about falsifying visual evidence. Existing forgery models, trained on datasets with full-image synthesis or large manipulated regions in object-centric images, struggle to generalise to surveillance scenarios. This is because tampering in surveillance imagery is typically localised and subtle, occurring in scenes with varied viewpoints, small or occluded subjects, and lower visual quality. To address this gap, SurFITR provides a large collection of forensically valuable imagery generated via a multimodal LLM-powered pipeline, enabling semantically aware, fine-grained editing across diverse surveillance scenes. It contains over 137k tampered images with varying resolutions and edit types, generated using multiple image editing models. Extensive experiments show that existing detectors degrade significantly on SurFITR, while training on SurFITR yields substantial improvements in both in-domain and cross-domain performance. SurFITR is publicly available on GitHub.

</details>

### 137. Towards Explainable Tampered Text Detection via Semantic-Guided Multi-Evidence Localization

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`tampered text`、`semantic-guided localization`、`multi-evidence`、`benchmark`

👤 **作者**：Jianjun Xu、Hongtao Xie、Yongdong Zhang

- 🎯 **研究动机**：被篡改文本可在视觉上难以察觉的情况下显著改变图像语义，对数字取证、媒体完整性与文档安全日益重要；现有方法证据支撑的可解释性有限，且主要依赖视觉外观，难以捕获细微取证痕迹并精确勾画细小、细长、不规则的篡改文本区域。
- 🔬 **研究方法**：提出语义引导多证据定位框架 SMELT：语义引导证据提示分支从视觉—语言模型提取篡改相关语义线索并转化为定位提示；多证据定位器联合利用视觉外观、压缩感知频率证据与边界感知高分辨率解码生成精确篡改掩码。同步构建可解释篡改文本数据集 VISTA-Text，覆盖多样领域与篡改类型，提供真实性判断、被篡文本内容、低层视觉伪影、高层语义不一致的结构化标注。
- 📌 **结论**：在 VISTA-Text 与多个附加基准上的实验表明 SMELT 一致提升篡改文本定位性能，并支持证据支撑的解释，同步推进检测精度与可解释性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Tampered text detection is increasingly important for digital forensics, media integrity assessment, and document security, since manipulated text can substantially alter image semantics while remaining visually plausible. However, existing methods remain insufficient in two key aspects. First, they provide limited evidence-grounded interpretability, making it difficult to relate predictions to forged text content, low-level visual artifacts, and high-level semantic inconsistencies. Second, they rely primarily on visual appearance and therefore struggle to capture subtle forensic traces and precisely delineate small, elongated, and irregular tampered text regions. To address these challenges, we propose SMELT, a Semantic-guided Multi-Evidence Localization framework for explainable Tampered text detection. SMELT consists of a semantic-guided evidence prompting branch and a multi-evidence localizer. The former extracts tamper-relevant semantic cues from a vision-language model and converts them into localization prompts. Subsequently, the multi-evidence localizer jointly exploits visual appearance, compression-aware frequency evidence, and boundary-aware high-resolution decoding to produce precise tamper masks. To facilitate this task, we further construct VISTA-Text, an interpretable tampered text dataset with diverse domains, tampering types, and structured annotations covering authenticity judgment, manipulated text content, low-level visual artifacts, and high-level semantic inconsistencies. Extensive experiments on VISTA-Text and additional benchmarks demonstrate that SMELT consistently improves tampered text localization performance while supporting evidence-grounded interpretation.

</details>

### 138. TraceSleuth: Coarse-to-Fine Hierarchical Reasoning with Trace Amplification for Precise Image Forgery Analysis

🐙 [Code](https://github.com/GCLion/TraceSleuth)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`image forgery analysis`、`coarse-to-fine reasoning`、`trace amplification`、`faithful explanation`

👤 **作者**：Zunlei Feng

- 🎯 **研究动机**：生成式 AI 使高度逼真的图像操纵挑战可信媒体分析；现有多模态伪造检测方法依赖单阶段融合与一次性生成，难以建立可靠的跨模态 grounding，导致解释不一致。
- 🔬 **研究方法**：提出粗到细、证据驱动的 TraceSleuth 框架，显式建模取证证据的形成与验证：先经原型聚合构建分布感知假设，再以跨模态对齐执行一致性感知推理生成忠实解释；定位上用图传播模块捕获非局部痕迹一致性并与语义线索融合预测掩码；反事实与一致性正则化确保预测与解释均立足于真实痕迹区域。
- 📌 **结论**：实验表明 TraceSleuth 提升检测与定位性能，同时产生更忠实、更可解释的解释；代码已开源。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of generative AI has enabled highly realistic image manipulations, posing challenges to trustworthy media analysis. Existing multimodal forgery detection methods often rely on single-stage fusion and one-shot generation, failing to establish reliable cross-modal grounding and leading to inconsistent explanations. We propose TraceSleuth, a coarse-to-fine, evidence-driven framework that explicitly models the formation and verification of forensic evidence. Instead of direct prediction, it first constructs a distribution-aware hypothesis via prototype-based aggregation, and then enforces consistency-aware reasoning through cross-modal alignment for faithful explanation generation. For localization, a graph-based propagation module captures non-local trace consistency and is fused with semantic cues for precise mask prediction. Counterfactual and consistency regularization further ensure that both predictions and explanations are grounded in genuine trace regions. Experiments demonstrate improved detection and localization performance, along with more faithful and interpretable explanations. The code is available at https://github.com/GCLion/TraceSleuthhttps://github.com/GCLion/TraceSleuth.

</details>

### 139. Trusting the Mask: Reliability Assessment for Image Tampering Localization

📅 2026　🏷 ACM MM 2026

**关键词**：`analysis`、`tampering localization`、`reliability assessment`、`distribution shift`、`selective rejection`

👤 **作者**：Haoyu Li、Bin Li、Haodong Li、Changsheng Chen、Jiangqun Ni

- 🎯 **研究动机**：图像篡改定位模型在真实场景遇到输入退化或分布偏移时，预测可能貌似合理却不可靠；现有定位模型无法判断其预测掩码是否仍可信，留下「预测的篡改掩码能否被信任」这一根本问题。
- 🔬 **研究方法**：提出篡改定位可靠性评估框架 TRUST-Mask，从预测掩码自身可靠性与「该估计对当前样本是否仍可信」两方面入手：掩码可靠性估计（MRE）模块估计预测掩码的可靠性；分布适用性评估（DAA）模块判断当前样本是否仍为信任 MRE 估计提供充分证据支持；自适应信任校准（ATC）模块校准 MRE 估计并输出统一可靠性分数。
- 📌 **结论**：大量实验表明 TRUST-Mask 在退化与分布偏移下为面向部署的决策提供有效可靠性线索，支撑选择性拒判、置信感知过滤与可靠性引导模型选择等实用策略。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid development of image editing tools and generative artificial intelligence techniques, digital image forgery has become an increasingly serious threat. Although existing image tampering localization methods can identify manipulated regions at the pixel level, their predictions may become plausible but unreliable when encountering input degradations or distribution shifts in real-world scenarios. In such cases, existing localization models lack the ability to determine whether their predicted masks remain trustworthy, raising a fundamental question: can the predicted tampering masks be trusted? To address this issue, we propose TRUST-Mask, a reliability assessment framework for image tampering localization. TRUST-Mask estimates the reliability of predicted tampering masks from two aspects: the reliability of the predicted mask itself and whether this reliability estimate remains trustworthy for the current sample. Accordingly, the framework includes a Mask Reliability Estimation (MRE) module to estimate predicted-mask reliability, a Distribution Applicability Assessment (DAA) module to evaluate whether the current sample still provides sufficient evidential support for trusting the MRE estimate, and an Adaptive Trust Calibration (ATC) module to adaptively calibrate the MRE estimate and produce a unified reliability score. Extensive experiments show that TRUST-Mask provides useful reliability cues for deployment-oriented decision-making under both distortions and distribution shifts, enabling practical strategies such as selective rejection, confidence-aware filtering, and reliability-guided model selection.

</details>

### 140. When 2D Cues Fail: Improving Image Manipulation Localization with Reliable 3D Geometry

🐙 [Code](https://github.com/vpsg-research/GFrame)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`manipulation localization`、`3D geometry`、`monocular reconstruction`、`reliability estimation`

👤 **作者**：Zhiqing Guo

- 🎯 **研究动机**：现有图像操纵定位（IML）重度依赖低层伪影、噪声痕迹、语义不一致等 2D 取证线索；当篡改区域与周围上下文外观融合良好时这些线索判别力骤降——被操纵区域可能局部外观一致，却仍违反场景几何结构。
- 🔬 **研究方法**：把几何推理引入 IML：经单目重建获取深度与表面法线等辅助几何线索；针对操纵图像上重建几何固有噪声的问题，不把深度与法线当直接证据，而是估计其可靠性并选择性用于定位；据此设计几何感知框架 GFrame，融合可靠几何线索与 RGB 特征并跨尺度传播，改进细粒度定位。
- 📌 **结论**：实验表明该方法在有限预算约束下取得优异性能，可靠 3D 几何为 IML 提供传统 2D 线索之外的互补取证证据；代码已开源。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing image manipulation localization (IML) methods rely heavily on 2D forensic cues, such as low-level artifacts, noise traces, and semantic inconsistencies in the manipulated image. While effective in many cases, these cues become much less discriminative when manipulated regions are well blended with their surrounding context in appearance. In such cases, a manipulated region may remain locally appearance-consistent, but still violate the geometric structure of the surrounding scene. This limitation motivates us to go beyond purely 2D evidence and introduce geometric reasoning into IML. To this end, we leverage monocular reconstruction to obtain auxiliary geometric cues, including depth and surface normals. However, a key challenge lies in the fact that reconstructed geometry on manipulated images is inherently noisy and cannot be used naively. Rather than treating depth and normals as direct evidence, we estimate their reliability and exploit them selectively for localization. Based on this principle, we design a geometry-aware framework (GFrame) that fuses reliable geometric cues with RGB features and propagates them across scales to improve fine-grained localization. Extensive experiments show that the proposed method achieves excellent performance under limited budget constraints. These results indicate that reliable 3D geometry provides complementary forensic evidence beyond traditional 2D cues for IML. The code is available at https://github.com/vpsg-research/GFrame.

</details>

### 隐写与隐蔽信道

### 141. CIS-Guard: Preemptive Defense Algorithm for Coverless Image Steganography Based on Adversarial Perturbation

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`coverless steganography`、`adversarial perturbation`、`extraction disruption`、`visual quality`

👤 **作者**：Qiang Xu、Xinghao Jiang

- 🎯 **研究动机**：无掩护图像隐写（CIS）不修改封面图像即可隐蔽通信，从而规避传统被动隐写分析；现有主动防御依赖旋转、裁剪、加噪等传统图像处理，而现代 CIS 算法对这些操作高度鲁棒，且防御性操作常损害视觉质量、反而在传输中引起怀疑。
- 🔬 **研究方法**：提出首个专门防御 CIS 的先发式防御算法 CIS-Guard：与只检测隐藏信息是否存在的传统隐写分析不同，主动向 stego 图像注入对抗扰动，破坏接收方对秘密信息的正确提取；引入视觉回调损失（VCL）增强图像视觉质量，降低防御操作暴露隐写通信的风险。在多种 SOTA CIS 方法上验证。
- 📌 **结论**：实验表明 CIS-Guard 显著降低 SOTA CIS 方法的提取准确率，同时保持更优的视觉质量，把 CIS 防御从被动检测推进到主动阻断。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Image steganography, particularly coverless image steganography (CIS), has emerged as a powerful means for covert communication without modifying the cover image, thereby evading conventional passive steganalysis. Existing active defense strategies against CIS primarily rely on traditional image processing operations such as rotation, cropping, and adding noise. However, modern CIS algorithms exhibit strong robustness against these operations. Moreover, such defensive manipulations frequently degrade image visual quality, potentially arousing suspicion during transmission. To address these limitations, we propose CIS-Guard, a novel preemptive defense algorithm based on adversarial perturbations. To the best of our knowledge, this is the first work dedicated to defending against CIS algorithms. Unlike traditional steganalysis methods that only detect the presence of hidden information, CIS-Guard proactively injects adversarial perturbations into stego-images to disrupt the correct extraction of secret information at the receiver. Furthermore, we introduce the visual callback loss (VCL) to enhance the visual quality. Experimental results demonstrate that CIS-Guard significantly reduces the extraction accuracy of state-of-the-art CIS methods while maintaining superior visual quality.

</details>

### 142. Coverless Image-in-Image Steganography with Enhanced Security for General Image Scenarios

📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`coverless steganography`、`image-in-image`、`key-driven latent transformation`、`unauthorized recovery resistance`

👤 **作者**：Jia Li、Zhankai Li、Xuehu Yan、Feng Chen、Zeshan Pang、Yuliang Lu

- 🎯 **研究动机**：无掩护图像中的图像隐写（CIIS）因高隐藏容量与强抗隐写分析能力备受关注；但通用图像场景下的现有方案存在未授权恢复下显著信息泄露、stego 内容多样性有限、秘密图像类别受限三大缺陷，根源在于秘密图像内部的固有相关性。
- 🔬 **研究方法**：先分析隐写与主流图像生成流程的兼容性，据此建立更通用、更合理的 CIIS 范式；在该范式下提出增强安全性的实现：密钥驱动潜在变换打破秘密图像内部相关性，减少泄露并提升内容多样性；语义无关的辅助信息经文本模态传输以支撑可靠恢复；补偿策略进一步提升恢复精度。在多样图像类别上开展实验。
- 📌 **结论**：多样图像类别上的实验表明，该方案在安全性、灵活性与恢复精度上均优于现有 CIIS 方案，可将任意秘密图像变换为无可疑、多样的 stego 图像。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Coverless image-in-image steganography (CIIS) has attracted increasing attention due to its high hiding capacity and stronger resistance to steganalysis. However, our investigation reveals that current schemes for general image scenarios suffer from significant information leakage under unauthorized recovery, limited diversity of stego content, and constraints on secret image categories. We attribute these limitations to the inherent correlations within the secret images. Motivated by the need for an effective CIIS scheme that can transform arbitrary secret images into suspicion-free and diverse stego images, we propose a scheme with enhanced security for general image scenarios. We first analyze the compatibility between steganography and the mainstream image generation process, based on which we develop a more general and reasonable paradigm for CIIS. Under this paradigm, we further propose an implementation in which a general key-driven latent transformation is used to break the internal correlations of secret images, thereby reducing secret leakage and improving content diversity, while semantically unrelated auxiliary information is transmitted through a text modal to support reliable recovery. In addition, a compensation strategy is incorporated to improve recovery accuracy. Experimental results on diverse image categories demonstrate that our scheme outperforms existing schemes in security, flexibility, and recovery accuracy, paving the way for secure and practical CIIS.

</details>

### 143. ReTokSync: Self-Synchronizing Tokenization Disambiguation for Generative Linguistic Steganography

📄 [arXiv](https://arxiv.org/abs/2604.25486)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`linguistic steganography`、`tokenization ambiguity`、`self-synchronization`、`two-channel covert communication`

👤 **作者**：Yaofei Wang、Yuang Qi、Donghui Hu、Kejiang Chen

- 🎯 **研究动机**：生成式语言隐写（GLS）把秘密消息嵌入自然语言生成过程，但实际部署中易受 tokenization 歧义影响：同一表面文本在接收方可能被重新切分为不同 token 序列，破坏共享解码状态，单点失配即传播为完全提取失败；现有方案或删除歧义 token（扭曲生成分布、损害安全性），或保分布却大幅牺牲容量或运行开销。
- 🔬 **研究方法**：提出自同步消歧框架 ReTokSync：生成期间监控接收方视角的 tokenization，仅在歧义真实发生时触发纠正性重置，把其影响限制在稀疏残余比特错误而非全局失步；无歧义位置完全不动，与底层隐写算法兼容。在英文与中文设定下实验，并开发双通道隐蔽通信机制：ReTokSync 作主通道、可靠辅助通道纠错。
- 📌 **结论**：ReTokSync 保持可见文本分布零 KL 散度，文本质量、嵌入容量与运行时均接近隐写基线，提取准确率不低于 99.7%；双通道机制实现 100% 端到端恢复，有效容量损失有限。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative linguistic steganography (GLS) enables covert communication by embedding secret messages into the natural language generation process. In practical deployment, however, GLS is vulnerable to tokenization ambiguity: the same surface text may be re-tokenized into a different token sequence at the receiver, breaking the shared decoding state between the communicating parties so that a single local mismatch can propagate into complete extraction failure. Existing solutions either remove ambiguous tokens---distorting the generation distribution and compromising security---or preserve the distribution at the cost of substantially reduced embedding capacity or prohibitive runtime overhead. To address this issue, we propose ReTokSync (Re-Tokenization Synchronization), a self-synchronizing disambiguation framework that monitors the receiver-view tokenization during generation and triggers a corrective reset only when ambiguity actually occurs. By confining the effect of tokenization ambiguity to sparse residual bit errors rather than global desynchronization, ReTokSync leaves ambiguity-free positions entirely untouched and remains compatible with the underlying steganographic algorithm. Experiments on both English and Chinese settings show that ReTokSync preserves the observable visible-text distribution with zero KL divergence and remains close to the steganographic baseline in text quality, embedding capacity, and runtime, while achieving extraction accuracy of at least 99.7%. Building on this property, we further develop a two-channel covert communication mechanism in which ReTokSync serves as the primary channel and a reliable auxiliary channel corrects the remaining errors, achieving 100% end-to-end recovery with limited effective-capacity loss.

</details>

### 144. Robust Coverless Linguistic Steganography via Sentence Embedding Space with Global Resynchronization

📄 [arXiv](https://arxiv.org/abs/2609.04970)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`linguistic steganography`、`sentence embedding`、`hierarchical clustering`、`bit-slippage resistance`

👤 **作者**：Ziqiang Li、Zhangjie Fu

- 🎯 **研究动机**：语言隐写经自然语言实现隐蔽通信，但现有方法重度依赖 token 级操作，在词级与句级文本扰动下难以保持可靠性；且变长编码方案对轻微扰动高度易受比特滑移——扰动使嵌入与提取的比特序列失步。
- 🔬 **研究方法**：提出在句嵌入空间而非 token 空间运作的无封面隐写框架：把秘密消息编码为句嵌入空间中的层次聚类路径，增强对词级与句级扰动的解码稳定性；针对比特滑移引入全局重同步机制（GRM），把变长比特流重构为锚定语义子空间的离散符号，解耦局部嵌入失败与全局消息恢复。
- 📌 **结论**：实验表明在词级与句级扰动下该方法鲁棒性显著提升，同时维持有效嵌入容量并对统计分析保持强抵抗。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Linguistic steganography enables covert communication through natural language. Existing methods heavily rely on token-level operations and struggle to maintain reliability under word- and sentence-level textual perturbations. Moreover, variable-length coding-based schemes are highly susceptible to bit-slippage under minor disturbances, as perturbations cause desynchronization between embedded and extracted bit sequences. To address these issues, we propose a robust coverless steganographic framework that operates in the sentence embedding space rather than the token space. Specifically, secret messages are encoded as hierarchical clustering paths in the sentence embedding space, which enhances decoding stability against word- and sentence-level textual perturbations. To tackle the bit-slippage problem, we introduce a Global Resynchronization Mechanism (GRM) that reframes variable-length bitstreams as discrete symbols anchored to semantic subspaces, decoupling local embedding failures from global message recovery. Experimental results demonstrate that under word- and sentence-level perturbations, our approach achieves substantial improvements in robustness, while maintaining effective embedding capacity and exhibiting strong resistance to statistical analysis.

</details>

### 145. Text Steganography with Dynamic Codebook and Multimodal Large Language Model

📄 [arXiv](https://arxiv.org/abs/2604.20269)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`text steganography`、`dynamic codebook`、`multimodal LLM`、`black-box paradigm`

👤 **作者**：Wanli Peng

- 🎯 **研究动机**：LLM 的流行使文本隐写性能大增，但两大范式各有硬伤：白盒范式因 Alice 与 Bob 共享现成语言模型，隐写行为易被暴露；黑盒范式需共享固定码本且要为每条隐写句共享特定提取提示，缺乏灵活性与实用性。
- 🔬 **研究方法**：提出带动态码本的黑盒文本隐写：经共享会话配置与多模态大语言模型构建动态码本；设计加密隐写映射，在隐写文本生成过程中嵌入秘密消息；引入基于拒绝采样的反馈优化机制，确保秘密消息的准确提取。
- 📌 **结论**：实验表明该方法在嵌入容量与文本质量上优于现有白盒文本隐写方法；在多个流行在线社交网络中比现有黑盒范式具备更好的实用性与灵活性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the popularity of the large language models (LLMs), text steganography has achieved remarkable performance. However, existing methods still have some issues: (1) For the white-box paradigm, this steganography behavior is prone to exposure due to sharing the off-the-shelf language model between Alice and Bob. (2) For the black-box paradigm, these methods lack flexibility and practicality since Alice and Bob should share the fixed codebook while sharing a specific extraction prompt for each steganographic sentence. In order to improve the security and practicality, we introduce a black-box text steganography with a dynamic codebook and multimodal large language model. Specifically, we first construct a dynamic codebook via some shared session configuration and a multimodal large language model. Then an encrypted steganographic mapping is designed to embed secret messages during the steganographic text generation. Furthermore, we introduce a feedback optimization mechanism based on reject sampling to ensure accurate extraction of secret messages. Experimental results show that the proposed method outperforms existing white-box text steganography methods in terms of embedding capacity and text quality. Meanwhile, the proposed method has achieved better practicality and flexibility than the existing black-box paradigm in some popular online social networks.

</details>

### 多模态虚假信息与事实核查

### 146. Beyond Retrieval: Improving Evidence Quality for LLM-based Multimodal Fact-Checking

📄 [arXiv](https://arxiv.org/abs/2505.03135)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`multimodal fact-checking`、`evidence retrieval`、`evidence quality`、`disinformation verification`

👤 **作者**：Haoran Ou、…、Kwok-Yan Lam

- 🎯 **研究动机**：多模态虚假信息以文本与视觉协同强化欺骗性声明，挑战自动事实核查；检索增强框架让 LLM 获取开放域外部信息、实现超越内部知识的循证验证，但实证研究揭示其外部搜索覆盖与证据质量评估存在明显短板。
- 🔬 **研究方法**：提出端到端自动多模态事实核查框架：设计新型证据检索策略，提升证据覆盖并从开放域来源过滤无用信息，为验证提取高质量证据；在两个公开多模态虚假信息数据集及新出现声明上系统评测，并与现有证据检索策略对比。
- 📌 **结论**：该框架在两个公开多模态虚假信息数据集上取得 88.3% 准确率，在新出现声明上达 90.2%；相比现有证据检索策略最多提升验证准确率 30.8%，凸显证据质量在 LLM 虚假信息验证中的关键作用。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The increasing multimodal disinformation, where deceptive claims are reinforced through coordinated text and visual content, poses significant challenges to automated fact-checking. Recent efforts leverage Large Language Models (LLMs) for this task, capitalizing on their strong reasoning and multimodal understanding capabilities. Emerging retrieval-augmented frameworks further equip LLMs with access to open-domain external information, enabling evidence-based verification beyond their internal knowledge. Despite their promising gains, our empirical study reveals notable shortcomings in the external search coverage and evidence quality evaluation. To mitigate those limitations, we propose , an end-to-end framework for automated multimodal fact-checking. It introduces a novel evidence retrieval strategy that improves evidence coverage and filters useless information from open-domain sources, enabling the extraction of high-quality evidence for verification. Extensive experiments demonstrate that achieves an accuracy of 88.3% on two public multimodal disinformation datasets and 90.2% on newly emerging claims. Compared with existing evidence retrieval strategies, our approach improves verification accuracy by up to 30.8%, highlighting the critical role of evidence quality in LLM-based disinformation verification.

</details>

### 147. Beyond Similarity: Question-Guided Verification for Out-of-Context Misinformation Detection

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`out-of-context misinformation`、`question-guided verification`、`training-free`、`evidence aggregation`

👤 **作者**：Jia-Nan Li、Xin-Shun Xu

- 🎯 **研究动机**：脱离语境（OOC）虚假信息以真实图像搭配欺骗性说明文字，是多模态事实核查的核心挑战；现有方法依赖相似性或整体 caption 级验证，且受合成基准影响使相似性权重过高，在全局貌似合理但局部不一致的真实 OOC 案例上效果受限。
- 🔬 **研究方法**：提出免训练分治框架 GUIDE，把 OOC 检测重构为问题引导验证：将 caption 分解为针对决策关键事实属性的定向验证问题，使局部事实冲突显式化；汇集视觉描述、结构化上下文参考、检索网络 caption 与相似度分数等互补证据；再对这些局部问题做综合验证并聚合局部判断为最终预测，避免退回粗粒度整体判断。
- 📌 **结论**：GUIDE 在基准上显著超越 SOTA：5Pils-OOC 准确率从 58.2% 提升至 67.2%，并在 VERITE 上取得最佳的 62.7%，证明问题引导验证优于相似性与整体 caption 级验证。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Out-of-context (OOC) misinformation, where real images are paired with deceptive captions, remains a core challenge for multimodal fact-checking. Existing methods still rely on similarity-based or holistic caption-level verification. Many are also shaped by synthetic benchmarks, where similarity can be overly influential, reducing their effectiveness on real-world OOC cases that are globally plausible but locally inconsistent. To bridge this gap, we propose GUIDE, a training-free, divide-and-conquer framework that reformulates OOC detection as question-guided verification. Instead of verifying the caption as a whole, GUIDE decomposes it into targeted verification questions over decision-critical factual attributes, making localized factual conflicts explicit. To verify these localized questions, GUIDE gathers structured and complementary evidence, including visual descriptions, structured context references, retrieved web captions, and a similarity score. To avoid reverting to a coarse holistic judgment, GUIDE then performs comprehensive verification over these localized questions, aggregating local judgments into a final prediction. Experiments demonstrate that GUIDE achieves significant results compared with SOTAs on benchmarks, improving accuracy on 5Pils-OOC from 58.2% to 67.2% and achieving the best VERITE result of 62.7%. These results indicate that realistic OOC detection benefits from question-guided verification over similarity-based or holistic caption-level verification.

</details>

### 148. DDU: Decoupling Dual-Level Uncertainties for Reliable Multimodal Fake News Detection

🐙 [Code](https://github.com/njustkmg/MM26-DDU)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`fake news`、`uncertainty decoupling`、`epistemic uncertainty`、`mixture-of-experts`

👤 **作者**：Xuran Chen、Xianglin Wei、Yang Yang

- 🎯 **研究动机**：社交媒体假新闻泛滥推动多模态检测发展；现有方法聚焦多样融合策略，但仍会产生不可靠结果——认知不确定性源于孤立样本对的受限上下文视野，偶然不确定性源于单模态数据固有噪声。
- 🔬 **研究方法**：提出双重不确定性解耦（DDU）框架：对认知不确定性，检索语义相似实例及其真实性标签并蒸馏为动态提示，以锚定和校准语义关系感知；对偶然不确定性，用混合专家（MoE）架构量化特征级不确定性，并以不确定性感知路由机制动态降低高不确定性特征权重，确保可靠的多模态融合。在跨两种语言的三个真实世界数据集上实验。
- 📌 **结论**：在跨两种语言的三个真实世界数据集上取得显著性能提升，验证对两类不确定性的显式解耦与差异化处理可带来更可靠检测；代码已开源。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of fake news on social media motivates the development of multimodal fake news detection. While most existing methods focus on various fusion strategies, they can still yield unreliable results caused by epistemic and aleatoric uncertainties, which can arise from the restricted contextual horizon of isolated sample pairs or inherent noise in unimodal data. To address this, we propose a novel Decoupling Dual-level Uncertainties (DDU) framework for reliable multimodal fake news detection. First, for epistemic uncertainty, we retrieve semantically similar instances along with their veracity labels, distilling them into dynamic prompts to anchor and calibrate the perception of semantic relationships. Second, for aleatoric uncertainty, we employ a Mixture-of-Experts architecture to quantify feature-level uncertainty. A novel uncertainty-aware routing mechanism is then introduced to dynamically down-weight features with high uncertainty, ensuring reliable multimodal fusion. Extensive experiments are conducted on three real-world datasets spanning two languages, demonstrating significant performance improvements of our method. The code is available at https://github.com/njustkmg/MM26-DDU.

</details>

### 149. Don't Just Classify, Compare: Evidence-Driven Multimodal Experts Framework for Fake News Detection

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`fake news`、`evidence retrieval`、`Dirichlet profile`、`expert aggregation`

👤 **作者**：Ying Cui、Wenbo Ding、Xiao-Ping Zhang

- 🎯 **研究动机**：误导性文本配暗示性图像的多模态假新闻构成显著社会挑战；现有方法已从简单特征融合演进到跨模态注意力网络，但仍不咨询外部知识、对演化叙事脆弱，且无法表征多模态样本的异质证据模式，在模糊样本上产生过度自信的错误。
- 🔬 **研究方法**：提出模拟人类事实核查的证据驱动多模态专家（EDME）框架：多模态证据检索器获取相关真实与假新闻文章，提供关键外部上下文；证据增强多模态专家的判断由证据驱动专家决策机制动态聚合，后者构成证据条件化的 Dirichlet 类别 profile 进行比较式决策。在三个基准数据集上实验。
- 📌 **结论**：EDME 显著超越 SOTA 基线，在 Weibo 数据集上准确率最高提升 1.2%，验证「比较而非仅分类」的证据驱动决策价值。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of multimodal fake news, which combines misleading text with suggestive imagery, presents a significant societal challenge, demanding robust detection methods. Existing approaches have evolved from simple feature fusion to sophisticated cross-modal attention networks to capture inter-modality relationships. However, they still face critical limitations: 1) a failure to consult external knowledge, leaving them vulnerable to evolving narratives, and 2) an inability to represent the heterogeneous evidence patterns of multimodal samples, leading to overconfident errors on ambiguous cases. To address these gaps, we propose the Evidence-Driven Multimodal Experts (EDME), a framework that emulates human fact-checking by integrating retrieval-based evidence with Dirichlet-profile decision-making. EDME first employs a Multimodal Evidence Retriever to fetch relevant real and fake news articles, providing crucial external context. This evidence is then leveraged by specialized Evidence-Enhanced Multimodal Experts, whose judgments are dynamically aggregated by an Evidence-Driven Expert Decision mechanism that composes evidence-conditioned categorical profiles. Extensive experiments on three benchmark datasets demonstrate that EDME significantly outperforms state-of-the-art baselines, improving accuracy by up to 1.2% on the Weibo dataset.

</details>

### 150. From Cheap Fakes to Pure Synthesis: Addressing the New Era of T2V Fake News Videos

📄 [arXiv](https://arxiv.org/abs/2608.06732)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`T2V fake news video`、`pure synthesis`、`ternary classification`、`reasoning-guided framework`

👤 **作者**：Yifeng Luo、Yupeng Li、Liang Lan、Tian Wang

- 🎯 **研究动机**：文本到视频（T2V）生成模型使假新闻视频可从零合成，威胁超越由既有素材拼装的 cheap fake；这类视频可与虚构叙事紧密匹配，对现有检测器形成模态对齐陷阱；现有数据集缺乏纯合成假新闻视频，而直接用假新闻描述提示 T2V 虽产生完美对齐样本，却把检测退化为单模态捷径并造成语义—视觉退化。
- 🔬 **研究方法**：把 T2V 假新闻视频检测（T2V-FNVD）形式化为真实/cheap fake/纯合成假的三分类任务；构建首个纯合成假新闻视频数据集 PS-FNVD，含「对齐欺骗的虚构事件」（Type 1）与「错误视觉出处的真实事件」（Type 2），防止单模态捷径；提出推理引导的 R-T2V 框架，经条件化理由生成与监督微调训练，融合高层语义逻辑与低层物理生成痕迹预测三分类标签。
- 📌 **结论**：跨 10 个主流基线的实验显示 R-T2V 取得 SOTA：准确率超第二名 12.20 个百分点，macro F1 超 8.46 个百分点。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent text-to-video (T2V) generation models enable fake news videos to be synthesized from scratch, shifting the threat beyond cheap fakes assembled from existing footage. Such news videos can closely match fabricated narratives, creating a modality alignment trap for existing detectors. Existing datasets lack pure synthesis fake news videos. Although directly prompting T2V models with descriptions of fake news videos can yield perfectly aligned samples, it reduces the fake news video detection (FNVD) to unimodal shortcuts and causes semantic-visual degeneration. To counter this, we formulate T2V-FNVD as a novel ternary classification task with three labels (real, cheap fake, and pure synthesis fake) and construct the first pure synthesis fake news video dataset (PS-FNVD). PS-FNVD includes fabricated events with aligned deception (Type 1) and true events with false visual provenance (Type 2), preventing models from exploiting unimodal shortcuts. Furthermore, we propose the Reasoning-guided T2V-FNVD (R-T2V) framework. Trained through conditioned rationale generation and supervised fine-tuning, R-T2V integrates high-level semantic logic with low-level physical generative traces to predict the ternary veracity label. Extensive experiments across 10 prevailing baselines show that R-T2V achieves the state-of-the-art performance, outperforming the second-best baseline by 12.20 percentage points in accuracy and 8.46 percentage points in macro F_1.

</details>

### 151. Let the Bullets Fly: Multimodal Fake News Detection with Temporal-Aligned Generative Danmaku

📄 [arXiv](https://arxiv.org/abs/2608.22832) · 🐙 [Code](https://github.com/126541/Let-the-Bullets-Fly)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`fake news video`、`danmaku`、`generative social signal`、`temporal alignment`

👤 **作者**：Chaowei Zhang、Zewei Zhang

- 🎯 **研究动机**：弹幕承载的群体观点冲突与共识可提供利于假新闻检测的细粒度判别社会信号；但真实场景中弹幕存在积累延迟，违背假新闻检测的实时性需求，使弹幕相关假新闻检测研究长期不足。
- 🔬 **研究方法**：提出时序生成弹幕框架 Genda：弹幕触发器预测用户反应的时机与强度，弹幕生成器合成相应语义与情感表达，共同构建时序对齐、类人的伪弹幕流；配套弹幕引导的时序多模态检测模型 DM-FEND，在视频、音频、文本与弹幕间实现细粒度多模态交互，增强动态模态对齐并抑制语义噪声。在中文与英文基准上评测并做消融。
- 📌 **结论**：DM-FEND 在中文（FakeSV）与英文（FakeTT）基准上一致超越 SOTA 基线；消融验证时序弹幕建模对鲁棒性与判别能力的关键作用；代码与数据已开源。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The social interactions among crowds via Danmaku (a.k.a., bullet comments) on modern multimedia platforms can facilitate both viewpoint conflicts and consensus, providing fine-grained discriminative social signals that can benefit fake news detection. However, the inherent accumulation latency of Danmaku in real-world scenarios violates the real-time necessity of fake news detection, making the studies of Danmaku-related fake news detection underexplored. To break this violation, we simulate this temporal-aware user interactive process by proposing a novel temporal Generative danmaku framework, called Genda, which consists of: (1) a Danmaku Trigger for predicting the timing and intensity of user reactions; and (2) a Danmaku Generator for synthesizing corresponding semantic and emotional expressions, thereby mutually constructing a temporally aligned and human-like pseudo Danmaku streams. To make the generated Danmaku useful for identifying fake news videos, we further design a Danmaku-guided Temporal Multimodal fake news detection model - DM-FEND, which enables fine-grained multimodal interactions among video, audio, text, and Danmaku, enhancing dynamic modalities alignment and semantic noise inhibition. The experimental results demonstrate that DM-FEND consistently outperforms state-of-the-art baselines across both Chinese (FakeSV) and English (FakeTT) benchmarks. Further ablations validate the crucial role of temporal Danmaku modeling in enhancing robustness and discriminative capability. Finally, this study offers a bright and robust solution for multimodal fake news detection in modern social interactive fashions by bridging the temporal inconsistency between news and user behaviors. To ensure reproducibility, the code and data used in this study are released at: https://github.com/126541/Let-the-Bullets-Fly.

</details>

### 152. Misleading Pattern-guided Deviation Modeling for Multimodal Fake News Detection

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`fake news`、`deviation modeling`、`LLM-generated variants`、`directional adaptation`

👤 **作者**：Haipeng Chen

- 🎯 **研究动机**：多模态假新闻因传播广、误导性强而备受关注；现有方法虽性能可观，但聚焦识别用于分类的预测线索，很少关注「假新闻如何从真新闻被伪造而来」的内在规律。
- 🔬 **研究方法**：从偏差建模视角重审该任务，提出 MPDM 框架：偏差建模分支仅在训练时对真实样本激活；偏差变体生成（DVG）用 LLM 按预定义误导模式从原始新闻文本生成偏差变体；偏差趋势蒸馏器（DTD）在嵌入空间自适应聚合方向与强度各异的变体、蒸馏出稳定的主导偏差趋势；低秩方向适配器（LDA）经方向适配把该趋势注入融合嵌入，避免直接注入造成语义失真并引导分类器学到更精准的决策边界。在四个基准数据集上实验。
- 📌 **结论**：四个基准数据集上 MPDM 一致超越 SOTA 基线，验证从伪造规律出发的偏差建模是预测线索之外的有效补充。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal fake news detection has attracted increasing attention due to the widespread dissemination and strong misleading potential of online news content. Although existing methods have achieved promising performance, they mainly focus on identifying predictive cues for classification, while paying limited attention to the intrinsic regularities underlying how fake news is fabricated from real news. To address this issue, we propose a novel framework called Misleading Pattern-guided Deviation Modeling (MPDM), which revisits multimodal fake news detection from the perspective of deviation modeling. Specifically, we introduce a deviation modeling branch that is activated only for real samples during training, aiming to capture the intrinsic deviation regularities associated with fake news fabrication through deviation trend distillation and directional adaptation. First, we propose Deviation Variant Generation (DVG), which leverages a large language model to generate deviation variants from original news text under predefined misleading patterns. Since the representation deviations induced by different variants vary substantially in both direction and strength, Deviation Trend Distiller (DTD) is introduced to adaptively aggregate these variants in the embedding space and distill a stable dominant deviation trend. Finally, we design a Low-rank Direction Adapter (LDA) to inject the distilled dominant deviation trend into the fused embedding via directional adaptation, thereby avoiding semantic distortion caused by directly injecting the deviation trend and guiding the classifier to learn a more precise decision boundary. Extensive experiments on four benchmark datasets demonstrate that MPDM consistently outperforms state-of-the-art baselines.

</details>

### 153. Multimodal Fake News Detection via Gradient Graph-based Label Propagation and Gradient-Guided Denoising Masking

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`fake news`、`label propagation`、`gradient consistency`、`pseudo-label denoising`

👤 **作者**：Zhen Huang、Zhiliang Tian、Menglong Lu、Jingyuan Huang、Dongsheng Li

- 🎯 **研究动机**：多模态假新闻检测通常对每个样本独立预测，忽略样本间关系证据；标签传播（LP）可捕获传播模式但受标签稀缺限制；近期方法向 LP 注入 LLM 伪标签，但朴素集成带来两问题：无差别连接所有样本导致错误跨类标签传播，噪声伪标签经噪声放大效应污染模型参数。
- 🔬 **研究方法**：提出梯度一致性驱动的 LP 框架 GCLP：锚点驱动梯度游走图构建（ADGW）利用高置信锚点与训练节点间的梯度一致性构建类感知传播子图，消除错误标签失配传播；梯度引导去噪掩蔽（GGDM）融合逐参数梯度信噪比与锚点一致性选择性掩蔽噪声更新，保护模型参数免受标签噪声；最后经梯度图标签传播（GGLP）在增强图上做注意力加权传播输出预测。在跨两种语言的三个基准上实验。
- 📌 **结论**：GCLP 在跨两种语言的三个基准上取得 SOTA 性能，同步解决错误标签传播与伪标签噪声放大两大问题。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid proliferation of social media has accelerated multimodal misinformation, where false claims paired with manipulated images make detection substantially more challenging. Existing multimodal fake news detection methods typically predict each sample independently, ignoring inter-sample relational evidence. While label propagation (LP) over inter-sample graphs captures propagation patterns, label scarcity limits its effectiveness. Recent methods inject LLM-generated pseudo-labels into LP to compensate, yet this naive integration introduces two issues: connecting all samples without selective distinction causes erroneous cross-class label propagation, and noisy pseudo-labels corrupt model parameters through a noise-amplification effect. To address these issues, we propose GCLP, a gradient-consistency-driven LP framework for multimodal fake news detection. We design Anchor-Driven Gradient Walk Graph Construction (ADGW), which leverages gradient consistency between high-confidence anchors and training nodes to build a class-aware propagation subgraph, eliminating erroneous label mismatch propagation. We further introduce a Gradient-Guided Denoising Masking mechanism (GGDM), which fuses per-parameter gradient signal-to-noise ratio with anchor-based consistency to selectively mask noisy updates, thereby protecting model parameters from label noise and mitigating the noise-amplification effect. Finally, Gradient Graph-based Label Propagation (GGLP) performs attention-weighted propagation over the augmented graph for the final prediction. Experiments on three benchmarks spanning two languages show that GCLP achieves state-of-the-art performance.

</details>

### 154. Novel Claim or Dj Vu? Rethinking ''Contamination-Free'' Dynamic Evaluation for Multimodal Automated Fact-Checking

📅 2026　🏷 ACM MM 2026

**关键词**：`analysis`、`fact-checking evaluation`、`data contamination`、`dynamic benchmark`、`performance inflation`

👤 **作者**：Reynold Cheng

- 🎯 **研究动机**：多模态自动事实核查（MAFC）的静态基准面临污染风险：多由 LLM 内部知识即可验证的过时声明构成，会虚高性能估计、无法反映对需要最新信息的新声明的能力；新兴动态基准收集 LLM 知识截止日期后发布的声明并假设其无污染，该假设缺乏检验。
- 🔬 **研究方法**：对 SOTA 静态基准 AVeriTeC 与新构建的动态基准 ClaimReview2025Q4 中的污染风险及其对 MAFC 评测的影响做实证研究，共得出 16 项发现；并在严格污染受控设定下重评 SOTA LLM，给出可信 MAFC 评测的实用指南。
- 📌 **结论**：动态评测降低但不消除污染风险，17.09%–29.30% 的截止后声明仍可能被污染；许多新发布声明可直接或经综合截止前公开知识验证；污染可使 MAFC 性能产生统计显著膨胀——Macro-F1 最高虚高 11.34 点——并扭曲系统排名。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal automated fact-checking (MAFC) verifies claims by retrieving and reasoning over external evidence. However, most existing static benchmarks risk contamination: they primarily consist of outdated claims verifiable using an LLM's internal knowledge without external evidence. This can inflate performance estimates and fail to reflect true capability on novel claims that require up-to-date information. To address this, emerging dynamic benchmarks collect claims published after LLMs' knowledge cut-off dates, assuming they are uncontaminated. This work revisits this assumption by empirically studying contamination risks in both the state-of-the-art (SOTA) static AVeriTeC benchmark and our newly constructed dynamic ClaimReview2025Q4 benchmark, as well as their impact on MAFC evaluation. Our experiments yield 16 findings, highlighting three key results: (1) Dynamic evaluation reduces but does not eliminate contamination risks, as 17.09%--29.30% of post-cut-off claims remain potentially contaminated; (2) Many newly published claims can be verified either directly or by synthesizing multiple pieces of public knowledge available before the cut-off; and (3) Contamination can induce statistically significant inflation in MAFC performance, increasing Macro-F1 by up to 11.34 points and distorting system rankings. In light of these findings, we re-evaluate SOTA LLMs under a strictly contamination-controlled setting. Our study provides practical guidelines for trustworthy MAFC evaluation.

</details>

### 155. ProgV-Trace: An LLM-Driven Verification Framework for Evidence-Grounded Video Misinformation Attribution

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`video misinformation`、`attribution`、`verification program`、`counterfactual intervention`

👤 **作者**：Shijie Li、Yu Huang

- 🎯 **研究动机**：视频虚假信息由真实素材、虚构字幕与被操纵语音拼装；现有检测器通常只输出二元判定或事后理由，不指明哪个元素使叙事变假及程度，并把多步核查推理塌缩为单次推断。
- 🔬 **研究方法**：形式化 L-EMMA 任务：联合真实性分类、细粒度造假定位、证据出处链与量化责任分数。ProgV-Trace 让 LLM 生成可执行验证程序（类型化算子序列），以分解声明、检索证据、扩展时序—多模态出处图、规划最小反事实干预隔离各元素贡献；程序到学生蒸馏把推理转入紧凑验证器实现免 LLM 部署；实验含 GroundLie360、FakeVV、FakeSV 与 Program-Hard 协议。
- 📌 **结论**：取得 87.2% F1 与 71.4% Resp-NDCG，超最强基线 +4.5 F1 与 +24.2 Resp-NDCG；蒸馏学生保留超 96% 归因质量（196 ms/样本），责任分数与人类判断五种操纵类型平均 84.9% 一致。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Video-based misinformationassembled from authentic footage, fabricated captions, and manipulated speechspreads rapidly across platforms, yet existing multimodal detectors typically produce only a binary verdict or a post-hoc rationale without determining which specific element across video, speech, and text is responsible for making the narrative false, or to what degree. Current approaches treat misinformation analysis as a single-step classification augmented with explanations, collapsing the structured, multi-step reasoning that human fact-checkers perform into a single inference pass. We formalize LLM-Driven Evidence-Grounded Multimedia Misinformation Attribution (L-EMMA), a task that jointly requires veracity classification, fine-grained falsity grounding, evidence-backed provenance chains, and quantified interventional responsibility scores. To address L-EMMA, we propose ProgV-Trace, a framework in which a large language model generates an executable verification programa typed operator sequence in a domain-specific languagethat decomposes claims, orchestrates evidence retrieval, dynamically expands a temporal-multimodal provenance graph, and plans minimal counterfactual interventions to isolate each element's contribution to the misinformation verdict. A program-to-student distillation stage transfers the LLM's structured reasoning into a compact verifier for deployment without LLM inference. We further introduce a Program-Hard Challenge Protocol with fresh, semantically coordinated, and multi-step-verification samples that stress-test generalization beyond standard benchmarks. Extensive experiments on GroundLie360, FakeVV, and FakeSV demonstrate that ProgV-Trace achieves 87.2% F1 and 71.4% Resp-NDCG, surpassing the strongest baseline by +4.5 F1 and +24.2 Resp-NDCG pointsof which a same-model ablation confirms +21.8 points stem from the interventional attribution method itself. The distilled student retains over 96% attribution quality at 196 ms per sample, and responsibility scores agree with human judgments 84.9% on average across five manipulation types.

</details>

### 156. Reasoning through Evolution: Automatic Meta-path Discovery for LLM-based Fake News Detection

🐙 [Code](https://github.com/SenticNet/MAGER)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`fake news`、`propagation graph`、`meta-path discovery`、`genetic evolution`

👤 **作者**：Ziyi Zhou、Xiaoming Zhang、Erik Cambria、Litian Zhang

- 🎯 **研究动机**：传播结构为假新闻检测提供关键证据，但现有方法主要依赖监督 GNN 模型，需大量标注数据且泛化有限；LLM 推理能力强，但直接输入原始传播图会造成严重模态失配与信息过载，使零样本/少样本下的结构感知推理不可靠。
- 🔬 **研究方法**：提出多智能体遗传进化框架 MAGER，自动发现为 LLM 推理优化的元路径：把复杂传播图压缩为信息丰富的子图，同时缓解信息过载与模态失配，使冻结 LLM 能进行结构感知的真实性推理；另引入图上下文学习策略，检索语义与结构相似的示范来强化分类与推理。
- 📌 **结论**：大量实验表明 MAGER 在数据高效设定下显著提升冻结 LLM 作为独立假新闻检测器的能力；代码已开源。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Propagation structures provide crucial evidence for fake news detection, yet existing approaches primarily rely on supervised GNN-based models, which require substantial labeled data and exhibit limited generalization. Although large language models (LLMs) exhibit strong reasoning capabilities, directly feeding them raw propagation graphs creates a significant modality mismatch and severe information overload, making structure-aware reasoning unreliable in zero-shot and few-shot settings. To bridge this gap, we propose MAGER, a multi-agent genetic evolution framework that automatically discovers meta-paths optimized for LLM reasoning. By compressing complex propagation graphs into informative subgraphs, the evolved meta-paths alleviate both information overload and modality mismatch, enabling frozen LLMs to perform structure-aware veracity reasoning. We further introduce a graph in-context learning strategy that retrieves semantically and structurally similar demonstrations to strengthen classification and reasoning. Extensive experiments show that MAGER substantially improves frozen LLMs as standalone fake news detectors in data-efficient settings. Our code is available at https://github.com/SenticNet/MAGER.

</details>

### 157. Self-Reflective Multi-modal Reasoning for Short-Video Fake News Detection

📄 [arXiv](https://arxiv.org/abs/2608.26787)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`short-video fake news`、`self-reflection`、`CoT refinement`、`cross-sample review`

👤 **作者**：Pinjie Xu、Zaiyang Yu、Ce Li、Zhenxing Qian

- 🎯 **研究动机**：假新闻检测管线日益借助 LLM 与 VLM 做推理式检测；但在缺乏真值思维链监督时，如何经自反思迭代提升推理质量、改进的思维链如何惠及下游微调、如何用大模型连接单样本欺诈模式发现与跨样本验证，仍是开放问题。
- 🔬 **研究方法**：提出短视频假新闻检测框架 SRM-FND：经盲分析师、反结论推理器与自一致性仲裁者协作的对比审议——配合迭代根因诊断与纠正性提示精炼——构建自反思且质量改进的推理并保留判别性理由；采用双阶段主题自适应 VLM 微调实现多模态 grounding 与轻量主题特化；对不确定样本做置信度驱动的跨样本审查，检索同事件可信与可疑见证。在 FakeSV 与 FakeTT 上实验。
- 📌 **结论**：SRM-FND 超越强基线，产生更可靠、可解释的预测，并在跨数据集设定下也带来明显提升。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent Fake News Detection (FND) pipelines increasingly leverage Large Language Models (LLMs) and Vision-Language Models (VLMs) for reasoning-based fake news detection. However, without ground-truth Chain-of-Thought (CoT) supervision, how to iteratively improve reasoning quality through self-reflection, how such improved CoT can benefit downstream model finetuning, and how to leverage large models to better connect single-sample fraudulent pattern discovery with cross-sample verification remain open problems. We propose SRM-FND, a self-reflective multi-modal reasoning framework for short-video fake news detection. SRM-FND constructs self-reflective and quality-improved reasoning through contrastive deliberation with iterative root-cause diagnosis and corrective prompt refinement, where a Blind Analyst, a Counter-Conclusion Reasoner, and a Self-Consistency Arbiter collaboratively retain discriminative rationales.It further adopts dual-phase topic-adaptive VLM finetuning for multi-modal grounding and lightweight topic specialization, and performs confidence-driven cross-sample review by retrieving co-event credible and suspicious witnesses for uncertain cases. Experiments on FakeSV and FakeTT demonstrate that SRM-FND outperforms strong baselines while yielding more reliable, interpretable predictions, and also provide noticeable improvement in cross-dataset performance.

</details>

### 158. Uni-Detector: Towards Universal Multimodal Fake News Detection

📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`fake news`、`universal modality`、`sparse mixture-of-experts`、`conditional computation`

👤 **作者**：Liyuan Zhang

- 🎯 **研究动机**：现有假新闻检测方法通常针对特定模态组合（纯文本、文＋图、文＋视频）定制，难以灵活适应社交平台上实际并存的多样模态组合，限制了检测模型在真实场景的实用价值。
- 🔬 **研究方法**：提出通用多模态假新闻检测模型 Uni-Detector：把稀疏混合专家（SMoE）层定制为 Transformer 中的前馈网络（FFN）与多头自注意力（MSA）模块，为不同模态充分分离参数空间；利用 SMoE 的条件计算特性动态分配相关模型组件，接收并处理任意输入模态组合。在中英文多模态数据集上实验，各含纯文本、文＋图、文＋视频三类。
- 📌 **结论**：Uni-Detector 在所有模态组合的测试集上均取得高度竞争的性能，成为真实场景中更灵活、强大的假新闻检测工具。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid rise of social media platforms has significantly increased information accessibility while also facilitating the widespread dissemination of fake news, causing profoundly negative impacts on individuals and society. Current fake news detection methods are typically tailored for specific modality combinations (e.g., text-only, text-image, or text-video), making them inflexible in adapting to diverse modality combinations actually present on social media platforms. This limitation restricts the practical value of detection models in real-world scenarios. In this paper, we propose Uni-Detector, a universal multimodal fake news detection model. It customizes the Sparse Mixture-of-Experts (SMoE) layer as both the Feedforward Network (FFN) and Multi-head Self-Attention (MSA) modules within the Transformer architecture, tackling the aforementioned barriers. This approach separates the parameter space sufficiently for different modalities. The conditional computation nature of SMoE allows us to organically allocate relevant model components to dynamically accept and process any combination of input modalities. We conducted extensive experiments on Chinese and English multimodal datasets, each comprising three categories: text-only, text-image, and text-video. The proposed Uni-Detector achieves highly competitive performance across all modality combinations on test sets, establishing the Uni-Detector as a more flexible and powerful tool for detecting fake news in real-world scenarios.

</details>

### 159. VIGOR: Video Fact-Checking via Experience-Guided Multi-Agent Collaborative Reasoning

🐙 [Code](https://github.com/immc-lab/VIGOR)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`video fact-checking`、`multi-agent collaboration`、`experience memory`、`evidence retrieval`

👤 **作者**：Yuxin Wang、Yang Yang、Huaiwen Zhang

- 🎯 **研究动机**：社交媒体视频虚假信息威胁信息可信度，其多样性使自动事实核查困难；MLLM 与多智能体系统可协作推理并给出可解释决策，但现有方法依赖试错推理而不复用过往经验，导致推理冗余且次优；处理整段视频还会引入无关信息、淹没关键证据。
- 🔬 **研究方法**：提出经验引导多智能体协作推理框架 VIGOR：视频事实核查经验记忆（VFEM）配合受价值迭代启发的非参数强化学习机制，允许智能体检索过往经验以降低推理成本并提升性能；把视频表示为时序段构成的多模态证据记忆（MEM），经跨模态检索自适应隔离关键证据、降低干扰。
- 📌 **结论**：大量实验表明 VIGOR 较现有方法将真实性分类提升 7.16%、解释质量提升 5.72%；代码已开源。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Video misinformation on social media threatens information credibility, yet its diversity makes automated fact-checking challenging. Multimodal Large Language Models (MLLMs) and Multi-Agent Systems (MAS) enable collaborative reasoning with explainable decisions. However, existing methods often rely on trial-and-error reasoning without reusing prior experience, leading to redundant and suboptimal reasoning. Moreover, processing entire videos introduces irrelevant information that can obscure key evidence. To address these challenges, we propose a framework for VIdeo fact-checking via experience-Guided multi-agent cOllaborative Reasoning (VIGOR). Specifically, we introduce a Video Fact-Checking Experience Memory (VFEM) with a non-parametric reinforcement learning mechanism inspired by value iteration, allowing agents to retrieve past experiences to reduce reasoning costs and improve performance. We represent videos as a Multimodal Evidence Memory (MEM) of temporal segments and use cross-modal retrieval to adaptively isolate key evidence and reduce interference. Extensive experiments show that VIGOR improves veracity classification by 7.16% and explanation quality by 5.72% over existing methods. Our code is available at https://github.com/immc-lab/VIGOR.

</details>


### 具身智能与自动驾驶安全

### 160. CARA: Concept-Aware Risk Attention for Interpretable Collision Anticipation

📄 [arXiv](https://arxiv.org/abs/2607.22494)　📅 2026　🏷 ACM MM 2026

**关键词**：`detection`、`collision anticipation`、`concept trajectory`、`intrinsic interpretability`、`spatio-temporal attention`

👤 **作者**：Enjun Du、Yue Su

- 🎯 **研究动机**：自动驾驶碰撞预期既要预警准确，也要能解释「正在追踪哪些风险因素、风险如何随时间演化」。现有特征驱动模型是黑盒、事后解释保真度不足，概念级方法又多为静态识别设计，难以适配动态驾驶场景的风险推理。
- 🔬 **研究方法**：提出内生可解释的时空框架 CARA（Concept-Aware Risk Attention）：从事故事故叙述中提炼领域风险概念，经视觉-语言相似度与视频帧对齐，组织成持续演化的概念轨迹；这些轨迹作为显式风险证据同时引导空间注意力、时间注意力与碰撞预期，使语义概念直接决定模型关注哪里、如何随时间预测风险，而非事后附加解释。
- 📌 **结论**：在 3 个基准上的实验显示，CARA 相对强基线同时提升预期准确率与预警提前量，并提供稀疏、语义落地的概念证据作为风险依据；证明把概念轨迹当作中间证据，能在动态驾驶场景中兼顾预测性能与风险推理的可解释性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Collision anticipation in autonomous driving requires not only accurate early warnings but also interpretable reasoning about what risk factors are being tracked and how risk evolves over time. Existing methods fall short in this regard: feature-driven models are opaque, post-hoc explanations often lack fidelity, and concept-based methods are mostly designed for static recognition rather than dynamic driving scenes. We propose CARA (Concept-Aware Risk Attention), an intrinsically interpretable spatio-temporal framework for collision anticipation. CARA derives domain-grounded risk concepts from accident narratives, aligns them with video frames via vision-language similarity, and organizes them into evolving concept trajectories. These trajectories provide explicit risk evidence that guides spatial attention, temporal attention, and anticipation, allowing semantic concepts to directly influence both where the model attends and how it predicts risk over time. By treating semantic risk factors as dynamic intermediate evidence rather than auxiliary post-hoc explanations, CARA tightly couples interpretability with the predictive process. Extensive experiments on three benchmarks show that CARA consistently improves anticipation accuracy and warning earliness over strong baselines, while providing sparse and semantically grounded concept evidence.

</details>

### 161. DSBench: A Comprehensive Benchmark for Evaluating External and In-Cabin Risks

📄 [arXiv](https://arxiv.org/abs/2511.14592) · 🐙 [Code](https://github.com/mengxh20/DSBench)　📅 2026　🏷 ACM MM 2026

**关键词**：`benchmark`、`driving safety`、`in-cabin monitoring`、`vision-language model`、`risk warning`

👤 **作者**：Zhijian Huang、Hongyuan Zhang、Long Chen、Hangjun Ye、Xiaoshuai Hao

- 🎯 **研究动机**：辅助驾驶安全需要同时理解外部交通环境与车内驾驶员状态，但现有研究把舱外场景理解与舱内驾驶员监测割裂处理，安全评估碎片化；任务专用模型虽在窄任务上表现好，却难以泛化到开放世界驾驶中多样且长尾的危险。
- 🔬 **研究方法**：提出新研究设定「辅助驾驶安全理解」，联合感知、推理并预警车内外风险；构建含 98K 视觉-语言标注的大规模驾驶安全数据集，精选 3K 构成系统评测基准 DSBench；基于该数据集训练域专用模型 DSVLM，定位为识别风险因素、推断危险并及时预警的车载安全助手，而非端到端驾驶模型。
- 📌 **结论**：主流开源与商用 VLM 在复杂安全关键情形下性能大幅退化；DSVLM 以平均 68.4 分建立新 SOTA，超最强商用基线 Seed-1.6（49.52 分）18.88 分，座舱理解任务上达 80.1、远超第二名的 29.49，显示其在复杂真实驾驶场景中显著更强的鲁棒性与安全意识。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Driving safety in assisted driving systems requires holistic understanding of both the external traffic environment and the internal driver state. However, existing research typically treats out-cabin scene understanding and in-cabin driver monitoring as separate problems, resulting in fragmented safety assessment and limited support for real-world warning applications. Moreover, conventional task-specific models often perform well on narrowly defined tasks but struggle to generalize to the diverse and long-tail hazards encountered in open-world driving scenarios. To address these limitations, we propose a new research setting, termed driving safety understanding for assisted driving, which aims to jointly perceive, reason about, and warn against risks by integrating information from both inside and outside the vehicle. To support this task, we construct a large-scale driving safety dataset containing 98K vision-language annotations that cover diverse in-cabin and out-cabin safety-critical scenarios, and further curate a 3K benchmark named DSBench(Driving Safety Benchmark) set for systematic evaluation. Based on this dataset, we develop DSVLM, a domain-specialized vision-language model for driving safety. Unlike end-to-end assisted driving models, DSVLM is designed as an in-vehicle safety assistant that identifies risk factors, infers potential danger, and provides timely warnings to help prevent accidents. Extensive evaluations against a wide range of mainstream open-source and proprietary VLMs show that existing models suffer substantial performance degradation in complex safety-critical situations, revealing a clear gap in reliable driving-safety understanding. In contrast, DSVLM establishes a new state of the art, achieving an average score of 68.4, which surpasses the strongest commercial baseline, Seed-1.6 (49.52), by 18.88 points. Its superiority is particularly pronounced on highly challenging tasks such as cockpit understanding, where DSVLM attains 80.1, dramatically outperforming the runner-up score of 29.49. These results demonstrate that DSVLM not only improves overall performance, but also delivers markedly stronger robustness and safety-awareness in complex real-world driving scenarios. The benchmark toolkit, source code, and model checkpoints are publicly available at https://github.com/mengxh20/DSBench.

</details>

### 162. HoRoTrust: Evaluating the Trustworthiness of Multimodal Large Language Models for Household Robot Interaction

📅 2026　🏷 ACM MM 2026

**关键词**：`benchmark`、`household robot`、`embodied trustworthiness`、`interactive evaluation`、`failure modes`

👤 **作者**：Xueyang Zhou、…、Lichao Sun

- 🎯 **研究动机**：家用机器人正从受控演示走入杂乱、不可预测的真实家庭，物理交互中的信任相关失败会引发包括安全隐患在内的现实伤害；领域缺少风险落地的具身可信度交互评测基准来系统诊断此类失败。
- 🔬 **研究方法**：从广泛报道的机器人失败与家庭异常事件中提炼 9 类代表性失败模式，锚定 7 个真实家庭场景，在 EB-Habitat 中系统实例化出 150 个细粒度交互评测任务，构成统一基准 HoRoTrust；沿 Truthfulness、Safety、Fairness、Robustness、Privacy 五个维度对 19 个 SOTA MLLM 做家用场景具身可信度评测。
- 📌 **结论**：对 19 个 SOTA MLLM 的评测揭示普遍可信度弱点，隐私保护与主动风险规避尤其突出；通用能力与可信度并不正相关，显式推理轨迹收益甚微；为家用具身智能体提供交互式、风险落地的信任失败诊断平台。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As household robots move from controlled demonstrations into messy, unpredictable homes, trust-related failures in physical-world interactions can cause serious real-world harm, including safety hazards. To enable risk-grounded evaluation of embodied trustworthiness, we analyze widely reported robot failures and abnormal household incidents, distilling 9 representative failure modes that capture recurring violations of human trust. We ground our benchmark in 7 real-world household scenarios and systematically instantiate these failure modes to construct 150 fine-grained interactive evaluation tasks in EB-Habitat. We evaluate embodied trustworthiness along five dimensions: Truthfulness, Safety, Fairness, Robustness, and Privacy, and introduce HoRoTrust as a unified benchmark for interactive household assessment. Experiments on 19 state-of-the-art MLLMs reveal pervasive weaknesses, particularly in privacy protection and proactive risk avoidance. We further find that general capability does not positively correlate with trustworthiness, while explicit reasoning traces provide little benefit. Overall, HoRoTrust offers an interactive, risk-grounded platform for diagnosing trust failures in household embodied agents.

</details>

### 163. SafeGen: Goal-Conditioned Video Diffusion of Safety-Critical Scenarios for VLM-Based Autonomous Driving

📄 [arXiv](https://arxiv.org/abs/2607.19701) · 🐙 [Code](https://github.com/JoFrc/SafeGen)　📅 2026　🏷 ACM MM 2026

**关键词**：`tool`、`scenario generation`、`goal-conditioned diffusion`、`vulnerable road users`、`VLM-based driving`

👤 **作者**：Tianyuan Zhang、Zonglei Jing、Zonghao Ying、Jiakai Wang、Aishan Liu、Xianglong Liu

- 🎯 **研究动机**：VLM 日益进入自动驾驶系统，需对罕见安全关键场景严格评测，与行人等弱势道路使用者（VRU）的交互是主要失败源；现有场景生成依赖仿真器，sim-to-real 差距大，难以捕捉真实多样的人车交互。
- 🔬 **研究方法**：SafeGen 将场景生成形式化为目标条件扩散：以灾难终态（如撞上行人）为强监督信号，生成向安全关键结果演化的连贯视频。Context Grounded End State Reasoning 用 VLM 分析良性上下文、推断交互脆弱性并产出高风险终态规格；End State Conditioned Video Evolution 经深度几何投影置入 VRU，边界条件扩散生成连贯中间帧。
- 📌 **结论**：在 3 个 VLMAD 上，SafeGen 将 Judge Overall Score（VLM judge 指标）较 SoTA 平均提升 24.25%；用生成数据微调 VLMAD，真实驾驶性能平均再升 15.9%。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models (VLMs) are increasingly deployed in autonomous driving (AD) systems, creating an urgent need for rigorous safety evaluation under rare yet safety-critical scenarios. Among these, interactions with vulnerable road users (VRUs), such as pedestrians, represent a major source of real-world failures. However, existing safety-critical scenario generation methods predominantly rely on simulator-based pipelines, which suffer from a substantial sim-to-real gap and often fail to capture realistic, diverse, and unforeseen humanvehicle interaction dynamics. To address this, we present SafeGen, a goal-conditioned diffusion framework for safety-critical scenario generation in vision-language model-based autonomous driving systems (VLMADs). Our key insight is to formulate scenario generation as a goal-conditioned diffusion process, where a predefined catastrophic end-state (e.g., a collision with a pedestrian) serves as a strong supervisory signal, guiding the generation of temporally coherent video trajectories that naturally evolve toward safety-critical outcomes. Building on this formulation, we introduce Context Grounded End State Reasoning, which leverages VLMs to analyze benign driving contexts and infer latent vulnerabilities in humanvehicle interactions, producing structured end-state specifications that induce high-risk scenarios. Conditioned on these targets, we further propose End State Conditioned Video Evolution, which grounds semantic threats into physically plausible visual dynamics. Specifically, we instantiate high-risk agents (e.g., VRUs) within the scene via depth-aware geometric projection, followed by boundary-conditioned diffusion to generate intermediate frames with consistent motion patterns and temporal coherence. Extensive experiments across 3 VLMADs demonstrate that SafeGen increases the Judge Overall Score, a metric using a VLM judge to evaluate VLMADs' understanding and decision-making, by 24.25% on average compared to SoTA baselines. Furthermore, fine-tuning a VLMAD with SafeGen-generated data improves performance in real-world driving scenes by an average of 15.9%. Our code is available at https://github.com/JoFrc/SafeGen website.

</details>

### 164. Tex3D: Objects as Attack Surfaces via Adversarial 3D Textures for Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2604.01618)　📅 2026　🏷 ACM MM 2026

**关键词**：`attack`、`VLA models`、`adversarial 3D texture`、`robotic manipulation`、`differentiable rendering`

👤 **作者**：Jiawei Du、Yu Tian

- 🎯 **研究动机**：VLA 模型在机器人操控中表现强劲，但对物理可实现对抗攻击的鲁棒性研究不足；已有工作用语言扰动与 2D 视觉攻击揭示漏洞，攻击面或缺乏部署代表性、或物理真实性有限；贴附在被操控物体上的对抗 3D 纹理更物理可信、更易部署，威胁更大。
- 🔬 **研究方法**：提出首个在 VLA 仿真环境内端到端优化 3D 对抗纹理的框架 Tex3D。针对标准 3D 仿真器缺少从 VLA 目标函数回传到物体外观的可微路径的障碍，设计前景-背景解耦（FBD），经双渲染器对齐实现可微纹理优化并保留原仿真环境；再提出轨迹感知对抗优化（TAAO），优先处理行为关键帧并以顶点参数化稳定优化，保证攻击跨长时程、多视角仍有效。在仿真与真实机器人上实验。
- 📌 **结论**：仿真与真实机器人实验中，Tex3D 在多个操控任务上显著削弱 VLA 性能，任务失败率最高达 96.7%；揭示 VLA 系统对物理落地 3D 对抗纹理攻击的严重脆弱性，凸显鲁棒性感知训练的必要性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language-action (VLA) models have shown strong performance in robotic manipulation, yet their robustness to physically realizable adversarial attacks remains underexplored. Existing studies reveal vulnerabilities through language perturbations and 2D visual attacks, but these attack surfaces are either less representative of real deployment or limited in physical realism. In contrast, adversarial 3D textures pose a more physically plausible and damaging threat, as they are naturally attached to manipulated objects and are easier to deploy in physical environments. Bringing adversarial 3D textures to VLA systems is nevertheless nontrivial. A central obstacle is that standard 3D simulators do not provide a differentiable optimization path from the VLA objective function back to object appearance, making it difficult to optimize through an end-to-end manner. To address this, we introduce Foreground-Background Decoupling (FBD), which enables differentiable texture optimization through dual-renderer alignment while preserving the original simulation environment. To further ensure that the attack remains effective across long-horizon and diverse viewpoints in the physical world, we propose Trajectory-Aware Adversarial Optimization (TAAO), which prioritizes behaviorally critical frames and stabilizes optimization with a vertex-based parameterization. Built on these designs, we present Tex3D, the first framework for end-to-end optimization of 3D adversarial textures directly within the VLA simulation environment. Experiments in both simulation and real-robot settings show that Tex3D significantly degrades VLA performance across multiple manipulation tasks, achieving task failure rates of up to 96.7%. Our empirical results expose critical vulnerabilities of VLA systems to physically grounded 3D adversarial attacks and highlight the need for robustness-aware training. Code is available at https://vla-attack.github.io/tex3d.

</details>


### 安全评测与可靠性基准

### 165. Automated Safety Benchmarking: A Multi-agent Pipeline for LVLMs

📄 [arXiv](https://arxiv.org/abs/2601.19507)　📅 2026　🏷 ACM MM 2026

**关键词**：`benchmark`、`LVLM safety evaluation`、`multi-agent pipeline`、`automated construction`、`sample selection`

👤 **作者**：Xiangyang Zhu、…、Wei Sun

- 🎯 **研究动机**：LVLM 在跨模态任务上能力突出，但显著的安全缺陷削弱其在真实应用中的可靠性；现有 LVLM 安全评测基准构建过程劳动密集、复杂度静态、判别力有限，难以跟上快速演进的模型与不断涌现的新风险。
- 🔬 **研究方法**：提出首个 LVLM 安全基准自动化构建系统 VLSafetyBencher，由四个协作 agent 组成：Data Preprocessing、Generation、Augmentation 与 Selection agent，分别负责数据预处理、安全样本生成、样本增强与高质量样本筛选，端到端自动构造并筛选安全评测基准。
- 📌 **结论**：实验证实 VLSafetyBencher 能以极低成本在一周内建成安全基准；产出基准判别力强——最安全与最不安全模型之间的安全率差距达 70%，可有效区分模型安全水平。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large vision-language models (LVLMs) exhibit remarkable capabilities in cross-modal tasks but face significant safety challenges, which undermine their reliability in real-world applications. Efforts have been made to build LVLM safety evaluation benchmarks to uncover their vulnerability. However, existing benchmarks are hindered by their labor-intensive construction process, static complexity, and limited discriminative power. Thus, they may fail to keep pace with rapidly evolving models and emerging risks. To address these limitations, we propose VLSafetyBencher, the first automated system for LVLM safety benchmarking. VLSafetyBencher introduces four collaborative agents: Data Preprocessing, Generation, Augmentation, and Selection agents to construct and select high-quality samples. Experiments validate that VLSafetyBencher can construct safety benchmarks within one week at a minimal cost. The generated benchmark effectively distinguishes safety, with a safety rate disparity of 70% between the most and least safe models.

</details>

### 166. CSR-Bench: A Benchmark for Evaluating the Cross-modal Safety and Reliability of MLLMs

📄 [arXiv](https://arxiv.org/abs/2602.03263)　📅 2026　🏷 ACM MM 2026

**关键词**：`benchmark`、`cross-modal safety`、`unimodal shortcut`、`stress testing`、`U2M-Align`

👤 **作者**：Yuxuan Liu、Kun Yang、Kui Ren

- 🎯 **研究动机**：MLLM 支持图文交互，但其安全行为可能由单模态捷径驱动，而非真正的图文联合意图理解；缺少能诊断此类跨模态可靠性问题的压力测试基准。
- 🔬 **研究方法**：提出 CSR-Bench：以 Safety、Over-rejection、Bias、Hallucination 四类压力测试交互模式评测跨模态安全与可靠性，覆盖 61 个细粒度类型；每条样本都要求图文联合解读，并配备 text-only 配对对照以诊断模态引发的行为偏移；在 16 个 SOTA MLLM 上评测，并进一步提出两阶段训练框架 U2M-Align 改善跨模态安全与可靠性。
- 📌 **结论**：评测揭示各可靠性维度间存在明显权衡，且从单模态输入转多模态时整体性能退化，表明模型安全意识弱且不可迁移；U2M-Align 在三种模型架构上相对未对齐基线同时提升全部四个可靠性维度，并保留通用能力。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) enable interaction over both text and images, but their safety behavior can be driven by unimodal shortcuts instead of true joint intent understanding. We introduce CSR-Bench, a benchmark for evaluating cross-modal reliability through four stress-testing interaction patterns spanning Safety, Over-rejection, Bias, and Hallucination, covering 61 fine-grained types. Each instance is constructed to require integrated imagetext interpretation, and we additionally provide paired text-only controls to diagnose modality-induced behavior shifts. Our evaluation of 16 state-of-the-art MLLMs reveals a clear trade-off across reliability dimensions and highlights an overall performance degradation when shifting from unimodal to multimodal inputs. This suggests that models possess weak, non-transferable safety awareness. To address this, we propose U2M-Align, a two-stage training framework for improving cross-modal safety and reliability. Experiments across three model architectures show that U2M-Align improves all four reliability dimensions over unaligned baselines while preserving general capabilities, yielding a better overall balance. WARNING: This paper contains unsafe contents.

</details>

### 167. Does Unification Come at a Cost? Uni-SafeBench: A Safety Benchmark for Unified Multimodal Large Models

📄 [arXiv](https://arxiv.org/abs/2604.00547) · 🐙 [Code](https://github.com/pengzixiang2002/Uni_SafeBench)　📅 2026　🏷 ACM MM 2026

**关键词**：`benchmark`、`unified multimodal model`、`understanding-generation safety`、`Uni-Judger`、`alignment preservation`

👤 **作者**：Yubin Wang、Gaopeng Gou

- 🎯 **研究动机**：统一多模态大模型（UMLM）在单一架构内整合理解与生成能力，能力扩张带来的安全影响重要却未被充分探索；现有安全基准聚焦孤立的理解或生成任务，无法评估统一框架下处理多样任务的整体安全性。
- 🔬 **研究方法**：提出综合安全基准 Uni-SafeBench：覆盖 6 大安全类别、7 种任务类型；为保证评估严谨，设计 Uni-Judger 框架，将上下文安全与内在安全解耦判定；基于该基准对统一模型开展系统性安全评测。
- 📌 **结论**：基于 6 大安全类别、7 种任务类型的评测发现，底座 LLM 原有的安全对齐在当前统一模型中未被一致保留；开源 UMLM 的安全表现显著低于专注生成或理解任务的多模态大模型，生成侧差距尤其明显，暴露统一架构的安全代价。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unified Multimodal Large Models (UMLMs) integrate understanding and generation capabilities within a single architecture. While unified architectures expand multimodal capabilities, their safety implications remain important yet underexplored. Existing safety benchmarks predominantly focus on isolated understanding or generation tasks, failing to evaluate the holistic safety of UMLMs when handling diverse tasks under a unified framework. To address this, we introduce Uni-SafeBench, a comprehensive benchmark featuring a taxonomy of six major safety categories across seven task types. To ensure rigorous assessment, we develop Uni-Judger, a framework that effectively decouples contextual safety from intrinsic safety. Based on comprehensive evaluations across Uni-SafeBench, we find that the original safety alignment of the underlying LLM is not consistently preserved in current unified models. Moreover, open-source UMLMs exhibit much lower safety performance than multimodal large models specialized for either generation or understanding tasks, particularly on the generation side. We release all resources at https://github.com/pengzixiang2002/Uni_SafeBench to systematically expose these risks and foster safer AGI development.

</details>

### 168. Omni-SafetyBench: A Benchmark for Safety Evaluation of Audio-Visual Large Language Models

📄 [arXiv](https://arxiv.org/abs/2508.07173)　📅 2026　🏷 ACM MM 2026

**关键词**：`benchmark`、`audio-visual LLM`、`cross-modal consistency`、`C-ASR`、`modality-switching jailbreak`

👤 **作者**：Leyi Pan、…、Lijie Wen

- 🎯 **研究动机**：融合视觉、听觉、文本的全模态大模型（OLLM）对音视频联合有害输入防御脆弱，且各模态安全表现不一致，可被简单的模态切换越狱利用；现有安全基准缺少音视频联合样本、模态覆盖有限，也没有评测跨模态一致性所需的平行测试用例。
- 🔬 **研究方法**：提出首个 OLLM 安全平行评测基准 Omni-SafetyBench：由 972 个种子样本扩展出 24 种模态变体、共 23,328 条测试实例；设计基于条件攻击成功率（C-ASR）与条件拒绝率（C-RR）的 Safety-score，以及跨模态安全一致性分数 CMSC-score；在 11 个 SOTA OLLM 上评测并检验现有安全对齐方法。
- 📌 **结论**：评测揭示严重漏洞：仅 3 个模型在两项指标上同时超过 0.6，音视频输入下安全性急剧退化；现有安全对齐方法在基准上暴露根本性挑战，凸显 OLLM 安全对齐研究的紧迫性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Omni-modal Large Language Models (OLLMs) that integrate visual, auditory, and textual processing face severe safety risks. They exhibit fragile defenses against audio-visual joint harmful inputs and demonstrate inconsistent safety performance across different modalities, enabling simple modality-switching jailbreaks. However, existing safety benchmarks fail to comprehensively assess these risks due to the absence of audio-visual joint samples, limited modality coverage, and lack of parallel test cases for cross-modal consistency evaluation. To address these gaps, we introduce Omni-SafetyBench, the first comprehensive parallel benchmark for OLLM safety evaluation, featuring 23,328 test instances across 24 modality variations derived from 972 seed samples. Recognizing that complex inputs pose comprehension challenges and that cross-modal consistency is critical for OLLM safety, we propose tailored metrics: a Safety-score based on Conditional Attack Success Rate (C-ASR) and Conditional Refusal Rate (C-RR), and a Cross-Modal Safety Consistency score (CMSC-score). Evaluating 11 state-of-the-art OLLMs reveals severe vulnerabilities: only 3 models exceed 0.6 in both metrics, with safety degrading sharply for audio-visual inputs. Furthermore, evaluation of existing safety alignment methods on Omni-SafetyBench identifies fundamental challenges in OLLM safety alignment, highlighting urgent needs for enhanced research in this domain.

</details>

### 169. SycoQA: A Dataset for Evaluating Sycophantic Hallucinations in Large Language Models

🐙 [Code](https://github.com/hehebamei/SycoQA)　📅 2026　🏷 ACM MM 2026

**关键词**：`benchmark`、`sycophantic hallucination`、`induction paradigm`、`context corruption`、`LLM evaluation`

👤 **作者**：Feng Liang、Xiping Hu

- 🎯 **研究动机**：谄媚幻觉指 LLM 为过度迎合人类偏好而生成幻觉回答；与知识缺失所致的常规幻觉不同，即便模型已掌握相关知识并获得明确上下文，仍可能给出貌似合理却错误的答案，更难防范；现有数据集缺乏多样诱导设定与跨领域评测。
- 🔬 **研究方法**：提出评测数据集 SycoQA，含 Core 与 Extension 两个子集，分别覆盖基于内部知识与上下文锚定两种设定：Core 采用强度逐级递增的多级诱导范式评测谄媚幻觉；Extension 通过上下文损坏构造数据以模拟相应场景，共同覆盖更宽的能力维度。
- 📌 **结论**：SycoQA 支撑对谄媚行为的深入分析，以及多级诱导感知、上下文鲁棒的谄媚幻觉检测等下游任务的综合评测，弥补既有数据集在诱导多样性与领域覆盖上的缺口；数据集已公开。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Sycophantic hallucinations refer to the tendency of large language models (LLMs) to generate hallucinated responses by excessively aligning with human preferences. Unlike conventional hallucinations caused by missing knowledge, sycophantic hallucinations are harder to prevent. Even when the model already contains the relevant knowledge and is given explicit context, it may still produce plausible but incorrect answers. Existing datasets for sycophantic hallucination typically lack diverse induction settings and broad evaluation across multiple domains. To address this gap, we introduce SycoQA to evaluate sycophantic hallucinations across a broader spectrum of capability dimensions. SycoQA consists of a core and an extension subset to evaluate sycophantic hallucinations under internal-knowledge-based and context-grounded settings, respectively. Specifically, the Core subset adopts multiple induction paradigms with progressively increasing intensity, while the Extension subset constructs data through contextual corruption to simulate the corresponding scenarios. We believe that SycoQA can facilitate further analysis of sycophantic behavior and support comprehensive evaluation of advanced downstream tasks, particularly multi-level induction-aware and context-robust sycophantic hallucination detection. The dataset is publicly available at https://github.com/hehebamei/SycoQA.

</details>

### 170. TeleRadShift: Worst-Group Conformal Risk Control for Safe VLM Triage Under Telemedicine Acquisition Shift

📅 2026　🏷 ACM MM 2026

**关键词**：`defense`、`conformal risk control`、`worst-group safety`、`radiology VLM`、`telemedicine shift`

👤 **作者**：Namrataben Patel、Honggang Wang

- 🎯 **研究动机**：远程医疗中胸片常以手机翻拍而非原生数字影像送达临床，采集伪影对放射 VLM 构成临床相关的分布偏移；标准 Conformal Risk Control 只保证平均风险，更难损坏子群上仍可能违反最差组安全，且聚合评测不可见。
- 🔬 **研究方法**：将失败溯源到跨模态解耦：视觉退化时语言解码器仍流利自信，随机样本间分歧升高而 token 熵不同步；据此提出结合熵与跨样本分歧的分数 FDV（Findings-Disagreement-Variance），及免重训练、保子群安全的校准框架 WG-CRC，在 15 组基准 TeleRadShift 上验证。
- 📌 **结论**：WG-CRC 在 23.9% 覆盖率下 0/15 组违规，较 Bonferroni 同安全性下提升 8.9 倍；免重校准迁移至 1,800 张真实手机翻拍为 0/9 违规（最差组风险 0.492），30 次划分下稳定（0.506±0.022）。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chest radiographs often reach clinicians in low-resource telemedicine settings as display-recaptured smartphone images rather than native digital studies. These images introduce structured acquisition artifacts that create clinically meaningful distribution shift for radiology vision- anguage models (VLMs). Standard Conformal Risk Control (CRC) enforces average-risk guarantees, but it can still violate worst-group safety on harder corruption subgroups, a failure that remains invisible under aggregate evaluation. We trace this behavior to cross-modal decoupling: when visual evidence is degraded, the language decoder remains fluent and confident, producing disagreement across stochastic samples without correspondingly high token entropy. Motivated by this effect, we introduce Findings-Disagreement-Variance (FDV), an uncertainty score that combines entropy and cross-sample disagreement, together with Worst-Group Conformal Risk Control (WG-CRC), a post-hoc calibration framework that targets subgroup-level safety without retraining. On TeleRadShift, a structured 15-group benchmark, WG-CRC achieves 0/15 violations at 23.9% coverage, corresponding to an 8.9× improvement over Bonferroni at matched safety. The method transfers without recalibration to 1,800 real smartphone captures (0/9 violations, worst-group risk 0.492) and remains stable across 30 random splits (worst-group risk 0.506±0.022). Project Page: https://gen-ai-research.github.io/teleradshift.

</details>

## 核验记录

- 核验日期：2026-10-22
- 录用状态：会议官网截至核验日未发布 accepted papers 列表与正式 proceedings；经用户指定，以第三方 Abstract Paper Portal（hongsong-wang.github.io/ACMMM2026，1,776 条主会条目、附 OpenReview 作者主页链接、162 条标 Oral）作为本届录用依据；Notification 为 2026-07-09，Portal 条目与该时间线一致。
- 逐篇核验：170 篇的标题、作者、摘要均逐条取自 Portal 原文；arXiv 链接（74 篇）由 Portal 登记的 pdf 链接转换为 abs 页，GitHub 链接（Portal 标注者）逐一保留；96 篇暂无 arXiv 登记的条目未添加未经证实的链接。每篇按标题+摘要完成安全相关性判定与小节归位，联邦学习、差分隐私、GNN 对抗净化等硬排除项已剔除；去重检查按 Portal PaperID 唯一性完成，无重复条目。
- 未决项：官方 accepted papers 列表与 ACM DL proceedings 尚未发布，待上线后需以官方数据复核 Portal 条目（标题、作者、track、Oral 标记）并回填 🎓 Official/DOI 链接；96 篇无 arXiv 的条目待作者放出预印本后补充 📄 链接。
