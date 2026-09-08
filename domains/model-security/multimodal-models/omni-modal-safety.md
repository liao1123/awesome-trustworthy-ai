# Omni-Modal Safety

[返回 Multimodal Model Security 目录](README.md)

## 研究方向

本页研究在同一模型中统一处理 text、image、audio、video 及多种输出形式后出现的 system-level safety。重点不是某一个模态的单独攻击，而是安全机制能否在 I/O combination 间保持一致、多个上下文线索能否被正确整合，以及统一表示是否同时传播能力与安全漏洞。

## 研究脉络

- **单模态外推：** 早期安全评测多把文本或图像 benchmark 转换到新模态，无法区分感知失败、跨模态整合失败与安全判断失败。
- **并行组合评测：** Omni-SafetyBench、UniSAFE 和 MCBench 通过 shared target、paired context 或平行 modality variation 比较同一风险在不同 I/O 路径中的表现。
- **机制统一：** 最新研究开始定位 modality-bound 与 modality-universal safety neurons，尝试在共享表示层建立可复用的干预点。
- **当前边界：** 模态组合数量增长很快，固定训练分布难以覆盖 multi-turn、multi-image、audio-visual joint input 与 image output；高 refusal 也可能只是没有理解输入。

## 跨模态安全机制与对齐

### 1. SafeNexus: Discovering and Steering Modality-Universal Safety Neurons in MLLMs

📄 [arXiv](https://arxiv.org/abs/2607.28969)　📅 2026-07

**关键词**：`defense`、`universal safety neuron`、`activation amplifier`、`cross-modal alignment`

👤 **作者**：Jian Yu、…、Tat-Seng Chua

- 🎯 **研究动机**：MLLM 安全防御局限于单一模态设定，难以应对跨模态威胁
- 🔬 **研究方法**：SafeNexus 用对比数据定位各模态专属安全神经元 BS-Neurons，取跨模态交集得 US-Neurons，并提出激活放大器与神经元校准两种对齐策略
- 📌 **结论**：抑制 US-Neurons 会跨模态大幅降低安全性而几乎不影响效用；两种策略在多模态安全基准上超越现有 SOTA 并保持效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Although Large Language Models (LLMs) have demonstrated promising safety performance, extending them to Multimodal Large Language Models (MLLMs) exposes a significant gap between expanded multimodal capabilities and existing safety mechanisms. Current defenses remain predominantly confined to specific modal settings, thereby limiting their robustness against broader cross-modal threats. To bridge this gap, we introduce SafeNexus, a cross-modal safety alignment framework that adopts a dedicated neuron-level intervention strategy. First, we formulate a neuron localization paradigm that identifies functionally specialized neurons by characterizing intermediate-layer activation patterns and quantifying their functional salience through importance scoring. Building upon this paradigm, we exploit contrastive data to identify modality-bound safety neurons (BS-Neurons), and validate their role in regulating safety behavior within each modality via targeted suppression. Further cross-modal analysis defines modality-universal safety neurons (US-Neurons) as the shared subset of BS-Neurons identified across individual modalities, serving as the core for defending against harmful cross-modal attacks. We observe that suppressing these neurons substantially degrades safety performance across modalities, while leaving overall utility largely unaffected. Building on these insights, we propose two safety alignment strategies: activation-level safety amplifier and safety neuron calibrator. The proposed strategies enhance model safety through two distinct routes: the former amplifies the activation magnitudes of US-Neurons, while the latter selectively calibrates them via targeted fine-tuning. Extensive experiments demonstrate that our method outperforms prevailing state-of-the-art approaches on safety benchmarks spanning diverse modality combinations, while effectively preserving utility.

</details>

### 2. Multi2AV-Safety: Benchmarking Safety in Multimodal-to-Audio-Video Generation

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

### 3. MCBench: A Multicontext Safety Assessment Benchmark for Omni Large Language Models

📄 [arXiv](https://arxiv.org/abs/2606.05177)　📅 2026-06

**关键词**：`benchmark`、`multicontext safety`、`paired scenario`、`cross-modal integration`

👤 **作者**：Manh Luong、…、Dinh Phung

- 🎯 **研究动机**：现有模态安全基准只覆盖视觉输入，无法评估同时处理视、听、文本的 Omni LLM
- 🔬 **研究方法**：构建 MCBench：1,196 个场景跨四类安全风险，每个不安全场景配最小差异的安全对照，要求跨模态整合判断，并分析推理轨迹
- 📌 **结论**：Omni LLM 在细微或非物理风险上表现差，能提取单模态信息却难以整合用于安全判断，暴露跨模态推理缺陷

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing multimodal safety benchmarks focus solely on visual inputs and cannot assess Omni Large Language Models (LLMs) that process vision, audio, and text. We introduce MCBench, a benchmark with 1196 scenarios spanning four safety categories that require integrating multiple modalities for accurate safety assessment. Each unsafe scenario is paired with a minimally different safe counterpart to assess model sensitivity. Our evaluations of state-of-the-art models reveal significant challenges. Omni LLMs struggle with subtle or non-physical risks but perform better when salient visual or acoustic cues are present. Analysis of reasoning traces shows that, although models can extract modality-specific information, they often fail to integrate these cues effectively for safety judgments. Our findings reveal that current Omni LLMs lack robust cross-modal reasoning in safety-critical settings, underscoring the need for improved architectures and training strategies for multimodal safety.

</details>

### 4. UniSAFE: A Comprehensive Benchmark for Safety Evaluation of Unified Multimodal Models

📄 [arXiv](https://arxiv.org/abs/2603.17476)　📅 2026-03

**关键词**：`benchmark`、`unified multimodal model`、`shared-target design`、`I/O combination`

👤 **作者**：Segyu Lee、…、Se-Young Yun

- 🎯 **研究动机**：统一多模态模型的安全基准碎片化，难以评测系统级漏洞
- 🔬 **研究方法**：UniSAFE 用共享目标设计把同一风险场景投射到 7 种 I/O 模态组合，含 6,802 个实例，评测 15 个 SOTA UMM
- 📌 **结论**：多图组合与多轮设定安全违规升高，image-output 任务一致弱于 text-output 任务

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unified Multimodal Models (UMMs) offer powerful cross-modality capabilities but introduce new safety risks not observed in single-task models. Despite their emergence, existing safety benchmarks remain fragmented across tasks and modalities, limiting the comprehensive evaluation of complex system-level vulnerabilities. To address this gap, we introduce UniSAFE, the first comprehensive benchmark for system-level safety evaluation of UMMs across 7 I/O modality combinations, spanning conventional tasks and novel multimodal-context image generation settings. UniSAFE is built with a shared-target design that projects common risk scenarios across task-specific I/O configurations, enabling controlled cross-task comparisons of safety failures. Comprising 6,802 curated instances, we use UniSAFE to evaluate 15 state-of-the-art UMMs, both proprietary and open-source. Our results reveal critical vulnerabilities across current UMMs, including elevated safety violations in multi-image composition and multi-turn settings, with image-output tasks consistently more vulnerable than text-output tasks. These findings highlight the need for stronger system-level safety alignment for UMMs. Our code and data are publicly available at https://github.com/segyulee/UniSAFE

</details>

### 5. A Safety Report on GPT-5.2, Gemini 3 Pro, Qwen3-VL, Grok 4.1 Fast, Nano Banana Pro, and Seedream 4.5

📄 [arXiv](https://arxiv.org/abs/2601.10527)　📅 2026-01

**关键词**：`benchmark`、`frontier model audit`、`cross-modal protocol`、`adversarial safety`

👤 **作者**：Xingjun Ma、…、Yu-Gang Jiang

- 🎯 **研究动机**：前沿模型安全评测碎片化，能力进步是否带来同步安全提升不明
- 🔬 **研究方法**：以统一协议（benchmark、对抗、多语、合规）横评 GPT-5.2、Gemini 3 Pro、Qwen3-VL、Grok 4.1 Fast、Nano Banana Pro 与 Seedream 4.5 在语言、视觉语言与图像生成上的安全
- 📌 **结论**：安全格局高度不均：标准基准表现强，但对抗测试中所有模型最坏情况安全率跌破 6%；安全由模态、语言与评测设计多维塑造

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid evolution of Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs) has driven major gains in reasoning, perception, and generation across language and vision, yet whether these advances translate into comparable improvements in safety remains unclear, partly due to fragmented evaluations that focus on isolated modalities or threat models. In this report, we present an integrated safety evaluation of six frontier models--GPT-5.2, Gemini 3 Pro, Qwen3-VL, Grok 4.1 Fast, Nano Banana Pro, and Seedream 4.5--assessing each across language, vision-language, and image generation using a unified protocol that combines benchmark, adversarial, multilingual, and compliance evaluations. By aggregating results into safety leaderboards and model profiles, we reveal a highly uneven safety landscape: while GPT-5.2 demonstrates consistently strong and balanced performance, other models exhibit clear trade-offs across benchmark safety, adversarial robustness, multilingual generalization, and regulatory compliance. Despite strong results under standard benchmarks, all models remain highly vulnerable under adversarial testing, with worst-case safety rates dropping below 6%. Text-to-image models show slightly stronger alignment in regulated visual risk categories, yet remain fragile when faced with adversarial or semantically ambiguous prompts. Overall, these findings highlight that safety in frontier models is inherently multidimensional--shaped by modality, language, and evaluation design--underscoring the need for standardized, holistic safety assessments to better reflect real-world risk and guide responsible deployment.

</details>

### 6. FakeWorld 1.0: An Omni-modal Benchmark for Fake Media and Content

🎓 [Official](https://icml.cc/virtual/2026/poster/63697)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`omni-modal model`、`cross-modal risk`、`modality interaction`、`deepfake detection`、`empirical evaluation`

👤 **作者**：Yifeng Gao、…、Yu-Gang Jiang

- 🎯 **研究动机**：现有研究割裂媒体真实性（真伪）与内容真实性（语义一致与事实正确），而真实欺骗联合利用两者
- 🔬 **研究方法**：FakeWorld 全模态基准统一两轴：媒体轴覆盖文本音频图像视频合成，内容轴植入跨模态语义不一致与事实错误，嵌入网页与流式呈现场景并配逐实例理由标注；另提出双轴联合可解释检测框架 OmniChecker
- 📌 **结论**：开源与闭源 MLLM 均暴露根本能力极限，有效揭示高保真混合来源欺骗

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapidly increasing realism of AI-generated media has intensified the spread of deceptive content and undermined public trust. Existing research largely treats this challenge along two separate axes: media authenticity, which assesses whether content is real or machine-generated, and content veracity, which evaluates semantic consistency and factual correctness. This separation overlooks how real-world deception jointly exploits both dimensions. In this work, we present FakeWorld 1.0, an omni-modal benchmark that unifies media authenticity and content veracity within a single evaluation framework. Along the media axis, FakeWorld spans text, audio, image, and video synthesis. Along the content axis, it systematically instantiates cross-modal semantic inconsistencies and factual errors. These two axes are jointly embedded in realistic web-based and streaming-style presentation scenarios, reflecting how multimodal deception is composed, contextualized, and delivered in practice. FakeWorld further provides explainable annotations in the form of per-instance rationales, enabling transparent and evidence-based analysis. Under a unified evaluation protocol, experiments on both open- and closed-source multimodal large language models (MLLMs) reveal fundamental capability limits and demonstrate FakeWorld’s effectiveness in exposing high-fidelity, mixed-source deception. Beyond the benchmark, we introduce OmniChecker, an agentic framwork that performs joint, explainable detection across both axes and produces evidence-backed diagnostic reports. We position FakeWorld 1.0 as a realistic stress test and a practical foundation for advancing scalable, explainable detection of fake multimodal content.

</details>

### 7. Omni-SafetyBench: A Benchmark for Safety Evaluation of Audio-Visual Large Language Models

📄 [arXiv](https://arxiv.org/abs/2508.07173)　📅 2025-08

**关键词**：`benchmark`、`audio-visual safety`、`modality variation`、`safety consistency`

👤 **作者**：Leyi Pan、…、Lijie Wen

- 🎯 **研究动机**：全模态 LLM 对视听联合有害输入防御脆弱且跨模态安全不一致，现有基准缺联合样本与平行用例
- 🔬 **研究方法**：构建 972 个种子样本衍生 24 种模态变体共 23,328 实例的平行基准，提出 C-ASR、C-RR 与跨模态安全一致性 CMSC-score 指标
- 📌 **结论**：11 个 SoTA OLLM 中仅 3 个双指标超 0.6，视听输入下安全急剧退化，简单模态切换即可越狱

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Omni-modal Large Language Models (OLLMs) that integrate visual, auditory, and textual processing face severe safety risks. They exhibit fragile defenses against audio-visual joint harmful inputs and demonstrate inconsistent safety performance across different modalities, enabling simple modality-switching jailbreaks. However, existing safety benchmarks fail to comprehensively assess these risks due to the absence of audio-visual joint samples, limited modality coverage, and lack of parallel test cases for cross-modal consistency evaluation. To address these gaps, we introduce Omni-SafetyBench, the first comprehensive parallel benchmark for OLLM safety evaluation, featuring 23,328 test instances across 24 modality variations derived from 972 seed samples. Recognizing that complex inputs pose comprehension challenges and that cross-modal consistency is critical for OLLM safety, we propose tailored metrics: a Safety-score based on Conditional Attack Success Rate (C-ASR) and Conditional Refusal Rate (C-RR), and a Cross-Modal Safety Consistency score (CMSC-score). Evaluating 11 state-of-the-art OLLMs reveals severe vulnerabilities: only 3 models exceed 0.6 in both metrics, with safety degrading sharply for audio-visual inputs. Furthermore, evaluation of existing safety alignment methods on Omni-SafetyBench identifies fundamental challenges in OLLM safety alignment, highlighting urgent needs for enhanced research in this domain.

</details>

### 8. Unsafe by Reciprocity: How Generation–Understanding Coupling Undermines Safety in Unified Multimodal Models

📄 [arXiv](https://arxiv.org/abs/2603.27332) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4580)　📅 2026-03　🏷 ECCV 2026

**关键词**：`analysis`、`unified multimodal model`、`VLM safety`、`cyber misuse`、`cross-function attack`、`safety evaluation`

👤 **作者**：Kaishen Wang、Heng Huang

- 🎯 **研究动机**：统一多模态模型中理解与生成紧耦合的安全影响未被研究
- 🔬 **研究方法**：提出 RICE 攻击范式显式利用理解-生成双向交互，系统评估 Generation-to-Understanding 与 Understanding-to-Generation 两条通路
- 📌 **结论**：不安全中间信号可跨模态传播并放大风险，双向 ASR 均高，暴露 UMM 独有的结构性弱点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in Large Language Models (LLMs) and Text-to-Image (T2I) models have led to the emergence of Unified Multimodal Models (UMMs), where multimodal understanding and image generation are tightly integrated within a shared architecture. Prior studies suggest that such reciprocity enhances cross-functionality performance through shared representations and joint optimization. However, the safety implications of this tight coupling remain largely unexplored, as existing safety research predominantly analyzes understanding and generation functionalities in isolation. In this work, we investigate whether cross-functionality reciprocity itself constitutes a structural source of vulnerability in UMMs. We propose RICE: Reciprocal Interaction-based Cross-functionality Exploitation, a novel attack paradigm that explicitly exploits bidirectional interactions between understanding and generation. Using this framework, we systematically evaluate Generation-to-Understanding (G-U) and Understanding-to-Generation (U-G) attack pathways, demonstrating that unsafe intermediate signals can propagate across modalities and amplify safety risks. Extensive experiments show high Attack Success Rates (ASR) in both directions, revealing previously overlooked safety weaknesses inherent to UMMs.

</details>