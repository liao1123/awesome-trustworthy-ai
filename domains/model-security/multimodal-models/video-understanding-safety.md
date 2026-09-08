# Video Understanding Safety

[返回 Multimodal Model Security 目录](README.md)

## 研究方向

本页研究 VideoLLM/VLMM 在理解、总结和推理视频时的安全问题。相较静态图像，video 额外引入 frame sampling、temporal order、subtitle scheduling、multi-clip composition、motion semantics 与长上下文压缩；这些机制既可隐藏有害意图，也会让模型漏报实际可见的伤害内容或泄露训练视频 membership。

## 研究脉络

- **视频模态缺口：** 早期 VideoJail 与 Video-SafetyBench 证明动态视频可把有害语义藏在时间组合中，静态 image safety 不能直接迁移。
- **时间结构攻击：** 攻击从重复有害帧发展到 diverse-frame composition、multi-clip integration 和精确控制 subtitle 出现时长与位置。
- **管线失效分析：** sparse frame sampling、spatial token downsampling 与 encoder-decoder disconnection 会共同造成 harmful-content omission。
- **评测与对齐：** benchmark 从二元标签扩展到多层 harmful understanding、解释性 rationale 与 comprehension-aware metric；alignment 开始引入 video-specific preference data。
- **当前边界：** 现有防御多依赖静态 frame filter 或文本 description bridge，对 adaptive temporal attack、长视频和真实流式输入的覆盖仍不足。

## Temporal 与 Multi-Clip Jailbreak

### 1. TempJail: Temporal Jailbreak Attack against Large Vision-Language Models via Subtitle Scheduling

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

### 2. Jailbreaking Multimodal Large Language Models using Multi-Clip Video

🎓 [Official](https://aclanthology.org/2026.acl-long.1186/)　📅 2026-07　🏷 ACL 2026

**关键词**：`attack`、`multi-clip video`、`typographic integration`、`temporal composition`、`multimodal safety`、`LLM jailbreak`

👤 **作者**：Choongwon Kang、Seungjong Sun、Hyunmin Jun、Jang Hyun Kim

- 🎯 **研究动机**：视频输入的何种性质诱发 MLLM 越狱尚不清楚
- 🔬 **研究方法**：MCV SafetyBench 含 2,920 个由多个不同上下文短片组成的视频，评测八个视频 MLLM
- 📌 **结论**：攻击成功率随 clip 数一致上升；视频比图像、动态比静态、上下文越多样越脆弱；并利用图像模态相对鲁棒性提出防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As multimodal large language models (MLLMs) have advanced to process video inputs, concerns have emerged about their potential for malicious misuse. Prior jailbreak studies have shown that safety alignment in MLLMs can be bypassed through visual inputs, yet it remains unclear which properties of video inputs induce this vulnerability. To address this gap, we introduce Multi-Clip Video (MCV) SafetyBench, a dataset of 2,920 videos designed to evaluate how the diversity of video inputs affects the vulnerability of MLLMs. Each video consists of multiple short clips depicting diverse contexts related to a harmful query. Experiments on eight representative video MLLMs show that attack success consistently increases with the number of clips. Our results further indicate that the video modality is (1) more vulnerable than the image modality, (2) more vulnerable to dynamic videos than to static videos, and (3) more vulnerable when videos contain more diverse contexts. Building on these findings, we propose a defense strategy that leverages the relative robustness of the image modality. Warning: This paper may contain potentially offensive content.

</details>

### 3. Breaking Multimodal LLM Safety via Video-Driven Prompting

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Breaking_Multimodal_LLM_Safety_via_Video-Driven_Prompting_CVPR_2026_paper.html)　📅 2026-06　🏷 CVPR 2026

**关键词**：`attack`、`video-driven prompting`、`safety-proximal frame`、`frame diversity`、`video jailbreak`、`multimodal LLM`

👤 **作者**：Dong Wang、Xiangyu He、Xinqi Lyu、Bin Xiao

- 🎯 **研究动机**：多模态 LLM 的视频模态越狱漏洞基本未被探索
- 🔬 **研究方法**：发现把有害图像重复成视频帧即可绕过安全机制——不安全视频在表征空间比单张有害图像更接近安全视频；据此把有害内容与多样安全邻近帧交错注入文字视频
- 📌 **结论**：在 VideoLLaMA-2、Qwen2.5-VL、GPT-4.1、Gemini-2.5 及 16 种安全策略下取得 SOTA 越狱性能，比图像攻击更抗预定义系统提示

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) have achieved remarkable progress in visual reasoning tasks, serving as the core perception engines for emerging AI agents like OpenClaw. While recent studies have introduced several effective image-based jailbreak methods, the vulnerabilities inherent in the video modality remain a largely unexplored frontier. As a pioneering effort to bridge this critical safety gap, we demonstrate that video-driven jailbreak attacks are significantly more effective and robust against pre-defined system prompts than their image-based counterparts. Specifically, we find that simply repeating a harmful image across multiple frames to construct a video can bypass the safety mechanisms of MLLMs. Our analysis reveals that unsafe videos are embedded more similarly to safe videos in the model's representation space than individual harmful images, making them harder to detect. Moreover, videos composed of identical frames are processed more like static images and are more likely to trigger safety defenses compared to videos with diverse frames. Motivated by these findings, we propose an algorithm that injects harmful content into typographic videos by interleaving it with diverse, safety-proximal frames, thereby evading MLLM safety alignment. Extensive experiments demonstrate that our approach achieves state-of-the-art jailbreak performance on several widely-used MLLMs (e.g., VideoLLaMA-2, Qwen2.5-VL, GPT-4.1, and Gemini-2.5) under 16 different safety policies.

</details>

### 4. VideoJail: Exploiting Video-Modality Vulnerabilities for Jailbreak Attacks on Multimodal Large Language Models

📝 [OpenReview](https://openreview.net/forum?id=fSAIDcPduZ)　📅 2025-03　🏷 ICLR 2025

**关键词**：`attack`、`VideoJail`、`video generation`、`jigsaw dynamics`

- 🎯 **研究动机**：越狱研究集中于图像模态，视频漏洞被忽略
- 🔬 **研究方法**：VideoJail利用视频生成与动态jigsaw构造视频载荷绕过检测
- 📌 **结论**：多种开源与闭源MLLM上取得高ASR，建立视频专用threat model

### 5. Distributed Implicit Harm: A Compositional Safety Blind Spot in MLLM-Based Video Moderation

📄 [arXiv](https://arxiv.org/abs/2609.00206)　📅 2026-09

**关键词**：`benchmark`、`video moderation`、`distributed implicit harm`、`cross-modal composition`

👤 **作者**：Ruotong Wang、Zihao Zhu、Siwei Lyu、Xin Tao、Baoyuan Wu

- 🎯 **研究动机**：视频各片段单独无害、组合后表达有害意义，现有视频 moderation 与安全数据集均缺此类组合标注
- 🔬 **研究方法**：定义 Distributed Implicit Harm（时间分布 DIH-T 与跨模态 DIH-M），用 multi-agent 合成框架把良性组件组合成 9,000+ 条带推理标注的视频并评测 30+ MLLM
- 📌 **结论**：全部模型对两类 DIH 检出均显著不足，最强 frontier 模型也常正确评估单个组件却无法识别组合出的有害含义，真实社媒视频复现该失败

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite their growing use in video moderation, multimodal large language models (MLLMs) exhibit a compositional safety blind spot: videos composed of seemingly benign components can convey harmful meaning when interpreted as a whole. We refer to this phenomenon as Distributed Implicit Harm (DIH), where harm arises from relations among components distributed along a decomposition axis of the video, rather than from any single explicit cue. Among many possible axes, we study two representative cases: temporally distributed harm across visual segments (DIH-T) and cross-modal harm between audio and visual streams (DIH-M). Studying and mitigating DIH at scale requires data that is difficult to collect: such videos lack compositional harm annotations, evade retrieval based on local visual cues, keywords, or single-modality signals, and are consequently absent from existing safety datasets. To bridge this gap, we develop a multi-agent synthesis framework that composes individually benign components into harmful scenarios and generates diverse DIH videos with explicit reasoning annotations, yielding a dataset of over 9,000 videos spanning visual-only and audio-visual settings. Benchmarking over 30 MLLMs spanning frontier proprietary models and leading open-source systems reveals substantial and consistent deficits in detecting both DIH-T and DIH-M. Notably, this failure persists even among the strongest frontier models: they often correctly assess individual components in isolation but fail to recognize the harmful meaning that emerges from their composition. We further evaluate these models on a manually collected set of real-world DIH videos from social media and observe the same failure mode, highlighting DIH as a practical and underexplored challenge for video moderation.

</details>

### 6. HarmVideoBench: Benchmarking Harmful Video Understanding in Large Multimodal Models

📄 [arXiv](https://arxiv.org/abs/2606.27187)　📅 2026-06

**关键词**：`benchmark`、`harmful video understanding`、`beyond-clip reasoning`、`BCR`

👤 **作者**：Jiajun Wu、…、Guancheng Wan

- 🎯 **研究动机**：已有有害视频基准只做二分类且缺少解释性理由，无法评估深层语境伤害与判断依据
- 🔬 **研究方法**：构建 HarmVideoBench：1,379 视频+4,137 选择题，三层维度（可观测证据、片段内含义、超越片段推理）；并提出对齐基准的 BCR 方法预测推理边界并按需检索上下文
- 📌 **结论**：评估 19 个模型揭示表层捷径问题；BCR 把宏平均从 61.7% 提升到 SOTA 的 84.4%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large vision-language models (LVLMs) have recently shown immense potential in automated content moderation, sparking growing interest in developing harmful-video benchmarks. However, we identify two primary limitations in existing works: 1) The multi-layered characteristics of harmful videos are overlooked. Existing benchmarks predominantly formulate evaluation as a binary classification task, failing to capture implicit or deep contextual harms. 2) Explanatory rationales are completely absent. Current frameworks measure exclusively whether a model flags a video correctly rather than explaining why, turning evaluation into a black box where models can succeed through superficial shortcuts. To address these problems, we present HarmVideoBench, a multi-layered diagnostic benchmark comprising 1,379 videos paired with 4,137 multiple-choice questions. HarmVideoBench benchmarks three hierarchical dimensions: Observable Evidence, Clip-Internal Meaning, and Beyond-Clip Reasoning, aiming to evaluate models' deep understanding beyond surface cues with carefully balanced and curated samples. We evaluate 19 leading models on HarmVideoBench to assess their multidimensional understanding of harmful videos. Moreover, we introduce BCR, a benchmark-aligned method that predicts reasoning boundaries and dynamically retrieves context only when needed. Experimental results show that BCR substantially improves the base model's performance in harmful video understanding, raising the macro average from 61.7 percent to a state-of-the-art 84.4 percent.

</details>

### 7. Failures to Surface Harmful Contents in Video Large Language Models

📄 [arXiv](https://arxiv.org/abs/2508.10974) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/40841)　📅 2025-08　🏷 AAAI 2026

**关键词**：`analysis`、`harmful-content omission`、`sparse frame sampling`、`token downsampling`

👤 **作者**：Yuxin Cao、Wei Song、Derui Wang、Jingling Xue、Jin Song Dong

- 🎯 **研究动机**：视频中肉眼可见的有害片段为何不出现在模型摘要
- 🔬 **研究方法**：定位sparse sampling、spatial token loss与encoder-decoder disconnection三个叠加原因并构造zero-query attack
- 📌 **结论**：多数设置下omission rate超过90%

### 8. Video-SafetyBench: A Benchmark for Safety Evaluation of Video LVLMs

📄 [arXiv](https://arxiv.org/abs/2505.11842) · 🌐 [Project](https://liuxuannan.github.io/Video-SafetyBench.github.io/) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c8bda0ee8b6bd4c56d9f8bdb3653e7db-Abstract-Datasets_and_Benchmarks_Track.html)　📅 2025-05　🏷 NeurIPS 2025

**关键词**：`benchmark`、`video-text attack`、`motion semantics`、`RJScore`

👤 **作者**：Xuannan Liu、…、Ran He

- 🎯 **研究动机**：多模态安全评测聚焦静态图像，忽视视频时序动态诱导的特有风险
- 🔬 **研究方法**：构建 2,264 对、48 类不安全类别的基准，以主体图像加运动文本的可控管线合成视频，并提出含置信度校准的 RJScore 指标
- 📌 **结论**：良性查询与视频组合的平均 ASR 达 67.2%，揭示视频诱导攻击的普遍脆弱性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The increasing deployment of Large Vision-Language Models (LVLMs) raises safety concerns under potential malicious inputs. However, existing multimodal safety evaluations primarily focus on model vulnerabilities exposed by static image inputs, ignoring the temporal dynamics of video that may induce distinct safety risks. To bridge this gap, we introduce Video-SafetyBench, the first comprehensive benchmark designed to evaluate the safety of LVLMs under video-text attacks. It comprises 2,264 video-text pairs spanning 48 fine-grained unsafe categories, each pairing a synthesized video with either a harmful query, which contains explicit malice, or a benign query, which appears harmless but triggers harmful behavior when interpreted alongside the video. To generate semantically accurate videos for safety evaluation, we design a controllable pipeline that decomposes video semantics into subject images (what is shown) and motion text (how it moves), which jointly guide the synthesis of query-relevant videos. To effectively evaluate uncertain or borderline harmful outputs, we propose RJScore, a novel LLM-based metric that incorporates the confidence of judge models and human-aligned decision threshold calibration. Extensive experiments show that benign-query video composition achieves average attack success rates of 67.2%, revealing consistent vulnerabilities to video-induced attacks. We believe Video-SafetyBench will catalyze future research into video-based safety evaluation and defense strategies.

</details>

### 9. SafeVid: Toward Safety Aligned Video Large Multimodal Models

📄 [arXiv](https://arxiv.org/abs/2505.11926) · 📊 [Dataset](https://huggingface.co/datasets/yxwang/SafeVid-350K) · 📝 [OpenReview](https://openreview.net/forum?id=SeNFo7JGly)　📅 2025-05　🏷 NeurIPS 2025

**关键词**：`defense`、`SafeVid-350K`、`video preference data`、`DPO`

👤 **作者**：Yixu Wang、…、Yu-Gang Jiang

- 🎯 **研究动机**：静态图像安全对齐难以泛化到动态视频
- 🔬 **研究方法**：SafeVid构建SafeVid-350K视频偏好数据，以详细文本描述为安全推理桥梁并做DPO
- 📌 **结论**：LLaVA-NeXT-Video在SafeVidBench上最高提升42.39%

### 10. Membership Inference Attacks Against Video Large Language Models

📄 [arXiv](https://arxiv.org/abs/2604.27002)　📅 2026-04

**关键词**：`attack`、`membership inference`、`temperature perturbation`、`video difficulty`

👤 **作者**：Wei Song、Yuxin Cao、Ziqi Ding、Yi Liu、Gelei Deng、Yuekang Li

- 🎯 **研究动机**：VideoLLM 在大规模视频文本语料上训练，其成员推断攻击此前未被研究；黑盒下信号与运动复杂度、时长纠缠
- 🔬 **研究方法**：黑盒 MIA 耦合温度扰动生成与视频难度特征：查询高低温度下生成文本的语义漂移并联合视频内在难度判断
- 📌 **结论**：LLaVA-Video-7B 上 AUC 0.68、accuracy 0.63，证明 VideoLLM 面临黑盒隐私泄露风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Video large language models (VideoLLMs) are increasingly trained or instruction-tuned on large-scale video--text corpora collected from heterogeneous sources, raising an immediate privacy question: can an external auditor determine whether a particular video was used during training? While membership inference attacks (MIAs) have been studied extensively for classifiers and, more recently, for text and image generation models, the VideoLLM setting remains unexplored. This setting is challenging because black-box auditors observe only generated text, whereas the membership signal is entangled with video-specific factors such as motion complexity and temporal span. In this paper, we present a black-box MIA targeting VideoLLMs that couples temperature-perturbed generation with video-aware difficulty features. Our key intuition is that member samples tend to induce sharper, more brittle generation behavior across decoding temperatures, and that this signal should be interpreted jointly with the intrinsic difficulty of the queried video. Concretely, we query the target model at low and high temperatures, measure the semantic drift between the resulting texts. We evaluate the attack against \texttt{LLaVA-Video-7B-Qwen2-Video-Only} and achieve a member inference AUC of 0.68 and accuracy of 0.63. These results demonstrate that Video-LLMs are vulnerable to black-box membership inference attacks, highlighting an urgent need for the community to systematically evaluate and mitigate privacy risks in VideoLLMs.

</details>

### 11. V-DEAL: Diagnosing Video Safety De-Calibration as an Understanding--Refusal Coupling Failure

📄 [arXiv](https://arxiv.org/abs/2607.21151) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-07

**关键词**：`defense`、`video LLM safety`、`refusal calibration`、`uncertainty calibration`、`multimodal intervention`

👤 **作者**：Zhetong Zhang、Honghao Fu、Miao Xu、Yiwei Wang、Yujun Cai

- 🎯 **研究动机**：反直觉地，有害视频配良性查询的攻击成功率高于配显式有害查询，其机制不明
- 🔬 **研究方法**：提出 V-DEAL 三级诊断框架（行为、理解、内部表示）逐步排除感知失败并量化内部拒绝倾向，在六个 Video LLM、三个基准上测试，并给出提示注入干预
- 📌 **结论**：模型以 >81% 准确率识别有害内容，配良性查询时平均 ASR 仍达 48.33%；视觉理解激活的拒绝倾向弱于文本理解，注入干预平均降低 48.24 个百分点 ASR

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Video Large Language Models are increasingly deployed in real-world applications, ensuring their safety alignment has become critical. Counterintuitively, we find that harmful videos paired with benign queries achieve higher attack success rates than the same videos paired with explicitly harmful queries. To understand the underlying mechanism of this vulnerability, we present V-DEAL, a three-level diagnostic framework that jointly analyzes this failure across model behaviour, understanding, and internal representations. By progressively ruling out perception failure and quantifying the model's internal refusal tendency, V-DEAL provides a new diagnostic perspective for analyzing the underlying mechanism of the observed vulnerability. We tested six Video LLMs on three public benchmarks and observed that models correctly recognize harmful video content with over 81\% accuracy, yet the average attack success rate still reaches 48.33\% under the condition pairing harmful videos with benign queries. Hidden-state analysis further shows that visual understanding activates a weaker refusal tendency than textual understanding. Furthermore, we introduce a prompt injection intervention method that reduces attack success rates by an average of 48.24 percentage points and achieves performance comparable to prior fine-tuning-based methods, providing an effective and practical means to address such safety risks in Video LLMs.

</details>

### 12. Shot-Conditioned Vision-Language Adaptation for Effective Harmful Content Detection from Online Short Videos

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2149.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`detection`、`harmful short video`、`shot-conditioned adaptation`、`temporal moderation`、`shot adaptation`、`vision-language model`

- 🎯 **研究动机**：短视频有害检测面临频繁剪辑切分与异常密度高度可变，现有 VLM 方法依赖刚性实例选择机制，无法适配不可预测的异常时长
- 🔬 **研究方法**：提出 SVLA：π 自适应策略动态估计镜头级异常密度替代刚性选择，配合镜头条件时间编码器与双路上下文 adapter，并构建含 7 类异常的 SVA 数据集
- 📌 **结论**：在 SVA 数据集上达到 SOTA，并在多样场景中全面超越对手方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Short video harmful content detection aims to automatically identify diverse anomalies from user-generated media. This task presents unique challenges due to frequent editing cuts and highly variable anomaly densities, limiting the effectiveness of traditional surveillance-based approaches. Moreover, existing Vision-Language Model-based approaches typically rely on rigid instance selection mechanisms that fail to adapt to the unpredictable duration of anomalies in such unconstrained videos. To address these issues, we propose SVLA, a Shot-conditioned Vision-Language Adaptation framework, for effectively detecting harmful contents from online short videos. Our approach introduces a novel π-adaptive strategy to dynamically estimate shot-level anomaly density, replacing rigid selection with calibrated supervision. Furthermore, we employ a shot-conditioned temporal encoder to respect video hierarchy and adopt a dual-path contextual adapter to resolve semantic ambiguity. To benchmark this task, we construct a new dataset (SVA) covering more genuine online short videos that involve seven anomaly categories. Experiments on the SVA dataset demonstrate that SVLA can achieve the state-of-the-art performance and outperform its competitors across diverse scenarios. Codes and datasets are available at: https://github.com/xushuai7/IJCAI-SVLA.

</details>