# Audio Language Model Safety

[返回 Multimodal Model Security 目录](README.md)

## 研究方向

本页研究 Large Audio-Language Model（LALM）从连续声学信号到语言推理的安全失效。攻击面横跨 harmful speech、语言与口音、speaker style、background sound、adversarial waveform、near-ultrasound 和 audio token representation；评测还必须区分模型没有听懂、正确拒答与因缺少场景理解而 over-refuse。

## 研究脉络

- **文本安全不等于音频安全：** 早期 red teaming 表明同一有害请求改为 speech 或叠加非语音声响后，文本对齐的拒答能力明显下降。
- **声学维度扩展：** 攻击从 TTS 转写发展到 multilingual/accent、emotion/style、multi-speaker composition、imperceptible perturbation 与 physical acoustic channel。
- **机制分析：** 研究开始定位 audio token 的高梯度区域、latent acoustic semantic、text-audio alignment 与通用扰动中隐含的 linguistic feature。
- **评测细化：** benchmark 从统一 ASR 扩展到 comprehension-aware safety、speaker/context cue、over-refusal、跨模态一致性、latency 与 benign utility。
- **防御起步：** 当前路线包括 audio-aware guard model 和 refusal steering；对 adaptive、over-air、跨模型攻击的覆盖仍明显落后于攻击侧。

## Survey 与 Taxonomy

### 1. Audio Jailbreaks in Large Audio-Language Models: Taxonomy, Attack-Defense Analysis, and Cost-Aware Evaluation

📄 [arXiv](https://arxiv.org/abs/2605.30031)　📅 2026-05

**关键词**：`survey`、`audio jailbreak`、`attack-defense taxonomy`、`cost-aware evaluation`

👤 **作者**：Bo-Han Feng、Yu-Hsuan Li Liang、Chien-Feng Liu、You-Hsuan Chang、Yun-Nung Chen

- 🎯 **研究动机**：LALM 越狱研究的威胁模型与评测协议异质，攻击实用性与防御效用不可比
- 🔬 **研究方法**：统一 taxonomy（语义、声学、信号、嵌入层攻击；guard 式、免训练、训练式防御）并在十个开源 LALM 上受控评测，除 ASR 外同时测良性拒答与延迟
- 📌 **结论**：Acoustic Best-of-N 揭示最强最坏情形音频空间漏洞，Narrative Framing 是低延迟有效语义威胁；现有防御在鲁棒性与良性可用性间权衡，评测必须成本与效用感知

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Audio Language Models (LALMs) expand jailbreak risks from token-level prompting to the full speech perception-to-reasoning pipeline, where unsafe behavior can be induced through semantics, acoustic style, signal artifacts, or internal representations. Existing work studies these risks under heterogeneous threat models and evaluation protocols, making it difficult to compare attack practicality or defense utility. This paper provides a unified taxonomy and a controlled empirical evaluation of LALM jailbreak attacks and defenses. We organize prior work into semantic, acoustic, signal, and embedding-layer attacks; guard-based, training-free, and training-based defenses; and cross-modal, audio-native, and interactive benchmarks. We then evaluate representative attacks and defenses across ten open-source LALMs, measuring not only attack success rate but also benign refusal and latency. Our results show that Acoustic Best-of-N reveals strong worst-case audio-space vulnerabilities, Narrative Framing is an effective low-latency semantic threat, and current defenses trade robustness against benign usability. These findings support cost- and utility-aware evaluation as a necessary complement to success-rate-only LALM safety benchmarks.

</details>

### 2. A Survey of Large Audio Language Models: Generalization, Trustworthiness, and Outlook

📄 [arXiv](https://arxiv.org/abs/2605.20266)　📅 2026-05

**关键词**：`survey`、`LALM trustworthiness`、`audio attack surface`、`defense-in-depth`

👤 **作者**：Kaiwen Luo、…、Yew-Soon Ong

- 🎯 **研究动机**：LALM 能力发展远快于可信性系统框架的建立
- 🔬 **研究方法**：综述端到端架构与对齐算法如何扩大攻击面，建立可信 taxonomy（跨模态越狱、声学后门、生物特征隐私泄露），从幻觉、鲁棒、安全、隐私、公平、认证六支柱评 SOTA
- 📌 **结论**：攻击面成熟而防御明显落后，提出 Defense-in-Depth、因果听觉世界模型与内在表征工程路线图

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Advances in Large Language Models (LLMs) have paved the way for Multimodal Large Language Models (MLLMs). Among these, Large Audio Language Models (LALMs) are essential for realizing universal auditory intelligence. Despite their remarkable performance, the escalation of LALMs' capabilities has significantly outpaced the development of systemic frameworks to ensure their trustworthiness. This survey provides a comprehensive investigation into the endogenous mechanisms of LALMs, detailing the architectural innovations and alignment algorithms that facilitate emergent reasoning. Specifically, we analyze how the transition to unified end-to-end frameworks and the integration of continuous acoustic signals expand the attack surface. To rigorously evaluate the risks within these paradigms, we establish a comprehensive taxonomy of trustworthiness, categorizing critical vulnerabilities such as cross-modal jailbreaking, latent acoustic backdoors, and biometric privacy leakage. We review the state-of-the-art LALMs through six analytical pillars: hallucination, robustness, safety, privacy, fairness, and authentication. The pronounced imbalance between a mature offensive landscape and underdeveloped defenses highlights persistent trustworthiness gaps and multidimensional risks in audio-centric intelligence. Finally, we propose a roadmap advocating for ``Defense-in-Depth'' architectures, causal auditory world modeling, and intrinsic representation engineering to support the development of more reliable and trustworthy audio intelligence. Our project has been uploaded to GitHub https://github.com/Kwwwww74/Awesome-Trustworthy-AudioLLMs.

</details>

### 3. AOR-Bench: Do Large Audio Language Models Over-Refuse Pseudo-Harmful Queries?

📄 [arXiv](https://arxiv.org/abs/2606.21147)　📅 2026-06　🏷 EMNLP 2026

**关键词**：`benchmark`、`audio over-refusal`、`background context`、`pseudo-harmful query`

👤 **作者**：Jiaxi Yang、Chaewan Chun、Jason Lucas、Yuchen Yang、Dongwon Lee

- 🎯 **研究动机**：LALM 的拒绝机制会误拒良性查询，音频域中孤立有害的语音结合背景声可能变得无害，过度拒绝问题未被研究
- 🔬 **研究方法**：构建 AOR-Bench：3,000 个伪有害音频样本覆盖六类场景，评估 12 个 LALM，并探索 CoT 与激活转向两种轻量缓解
- 📌 **结论**：过度拒绝在六个模型家族中普遍存在，揭示其安全判断的多类模式；两种策略可部分缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Audio Language Models (LALMs) have demonstrated strong performance across a wide range of audio tasks. As they are increasingly deployed in real-world applications, ensuring their safety alignment has become more important. Although refusal mechanisms serve as a key safeguard by preventing LALMs from responding to harmful requests, they can also lead to over-refusal, where models incorrectly reject benign queries. This issue is especially challenging in the audio domain because speech that appears harmful in isolation may become benign when interpreted together with the surrounding acoustic context, such as background sounds. To study this problem, we introduce AOR-Bench (Audio Over-Refusal Benchmark), the first benchmark for over-refusal specifically designed for LALMs. AOR-Bench contains 3,000 pseudo-harmful audio samples across six scenario categories. Evaluating 12 representative LALMs from six major model families, we find that over-refusal is widespread (Figure 1) and uncover several important patterns in their safety judgments. As a preliminary effort to mitigate this issue, we further explore two lightweight strategies (e.g., Chain-of-Thought and activation steering) to reduce over-refusal.

</details>

### 4. SpeechJBB: Probing Safety Alignment and Comprehension in Large Audio Language Models under Code-Switched Speech

📄 [arXiv](https://arxiv.org/abs/2606.06037) · 📊 [Dataset](https://huggingface.co/datasets/McGill-NLP/SpeechJBB)　📅 2026-06

**关键词**：`benchmark`、`code-switched speech`、`pseudo-word obfuscation`、`multilingual safety`

👤 **作者**：Virginia Ceccatelli、Yejin Jeon、David Ifeoluwa Adelani

- 🎯 **研究动机**：LALM 安全对齐评估局限于单语文本有害提示，语码转换语音下的安全泛化基本未被探索
- 🔬 **研究方法**：构建 SpeechJBB 音频越狱数据集，覆盖五种欧洲语言及两两语码转换变体，并加入音系合理伪词插入模拟局部混淆
- 📌 **结论**：语码转换有害音频 JSR 显著偏高，非英语单语与转换对最高；伪词密度单调降低拒绝率，且强 ASR/推理模型同样脆弱，说明失败不可归因于多语理解不足

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large audio language models (LALMs) are increasingly deployed in real-world applications, yet their safety alignment is still primarily evaluated on monolingual, text-based harmful prompts. This leaves their generalizability under multilingual and spoken settings, particularly code-switched speech, largely underexplored. To address this gap, we introduce SpeechJBB, an audio jailbreak dataset for benchmarking state-of-the-art LALMs across five European languages: English, French, German, Italian, and Spanish, as well as code-switched variants combining pairs of these languages. The extent of safety weaknesses is further probed by introducing an augmented setting where phonologically plausible pseudo-words are inserted around safety-critical terms to simulate localized obfuscation. Across models, code-switched harmful audio yields substantially high jailbreak success rates (JSR), with non-English monolingual and non-English code-switched pairs exhibiting the highest attack success. Pseudo-word insertion monotonically reduces refusal as insertion density increases, even though models rarely attribute harmful meaning to the inserted tokens. Comprehension benchmarks show that these failures are not reducible to multilingual misunderstanding, as several models with strong ASR, spoken language understanding, and spoken reasoning performance are among the most vulnerable.

</details>

### 5. VoxSafeBench: Not Just What Is Said, but Who, How, and Where

📄 [arXiv](https://arxiv.org/abs/2604.14548) · 🌐 [Project](https://amphionteam.github.io/VoxSafeBench_demopage/)　📅 2026-04

**关键词**：`benchmark`、`speaker context`、`paralinguistic cue`、`privacy fairness`

👤 **作者**：Yuxiang Wang、…、Zhizheng Wu

- 🎯 **研究动机**：现有语音基准聚焦基础理解或孤立研究单一风险，混淆固有有害内容与仅因声学情境致害的内容
- 🔬 **研究方法**：VoxSafeBench 两层设计：Tier1 评文本与音频匹配的内容风险，Tier2 评转录良性但依赖说话人、副语言或环境线索的风险，覆盖双语 22 个任务
- 📌 **结论**：前沿 SLM 能感知声学线索却不据此行动，文本上稳健的安全、公平与隐私防护在语音中普遍退化，存在 speech grounding gap

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As speech language models (SLMs) transition from personal devices into shared, multi-user environments, their responses must account for far more than the words alone. Who is speaking, how they sound, and where the conversation takes place can each turn an otherwise benign request into one that is unsafe, unfair, or privacy-violating. Existing benchmarks, however, largely focus on basic audio comprehension, study individual risks in isolation, or conflate content that is inherently harmful with content that only becomes problematic due to its acoustic context. We introduce VoxSafeBench, among the first benchmarks to jointly evaluate social alignment in SLMs across three dimensions: safety, fairness, and privacy. VoxSafeBench adopts a Two-Tier design: Tier1 evaluates content-centric risks using matched text and audio inputs, while Tier2 targets audio-conditioned risks in which the transcript is benign but the appropriate response hinges on the speaker, paralinguistic cues, or the surrounding environment. To validate Tier2, we include intermediate perception probes and confirm that frontier SLMs can successfully detect these acoustic cues yet still fail to act on them appropriately. Across 22 tasks with bilingual coverage, we find that safeguards appearing robust on text often degrade in speech: safety awareness drops for speaker- and scene-conditioned risks, fairness erodes when demographic differences are conveyed vocally, and privacy protections falter when contextual cues arrive acoustically. Together, these results expose a pervasive speech grounding gap: current SLMs frequently recognize the relevant social norm in text but fail to apply it when the decisive cue must be grounded in speech. Code and data are publicly available at: https://amphionteam.github.io/VoxSafeBench_demopage/

</details>

### 6. JALMBench: Benchmarking Jailbreak Vulnerabilities in Audio Language Models

📄 [arXiv](https://arxiv.org/abs/2505.17568) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10010791)　📅 2025-05　🏷 ICLR 2026

**关键词**：`benchmark`、`JALMBench`、`audio transformation`、`attack-defense evaluation`

👤 **作者**：Zifan Peng、…、Xinyi Huang

- 🎯 **研究动机**：LALM 越狱缺乏统一的对抗音频数据集与攻防评测框架
- 🔬 **研究方法**：构建 JALMBench：11,316 文本与 245,355 音频样本（超千小时），覆盖 12 个 LALM、8 种攻击与 5 种防御，分析模态与架构影响
- 📌 **结论**：文本安全对齐可部分迁移至音频，交错音频文本策略更稳健；通用审核方法改进有限，需 LALM 专用防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Audio Language Models (LALMs) have made significant progress. While increasingly deployed in real-world applications, LALMs face growing safety risks from jailbreak attacks that bypass safety alignment. However, there remains a lack of an adversarial audio dataset and a unified framework specifically designed to evaluate and compare jailbreak attacks against them. To address this gap, we introduce JALMBench, a comprehensive benchmark that assesses LALM safety against jailbreak attacks, comprising 11,316 text samples and 245,355 audio samples (>1,000 hours). JALMBench supports 12 mainstream LALMs, 8 attack methods (4 text-transferred and 4 audio-originated), and 5 defenses. We conduct in-depth analysis on attack efficiency, topic sensitivity, voice diversity, and model architecture. Additionally, we explore mitigation strategies for the attacks at both the prompt and response levels. Our systematic evaluation reveals that LALMs' safety is strongly influenced by modality and architectural choices: text-based safety alignment can partially transfer to audio inputs, and interleaved audio-text strategies enable more robust cross-modal generalization. Existing general-purpose moderation methods only slightly improve security, highlighting the need for defense methods specifically designed for LALMs. We hope our work can shed light on the design principles for building more robust LALMs.

</details>

### 7. Audio Jailbreak: An Open Comprehensive Benchmark for Jailbreaking Large Audio-Language Models

🌐 [Project](https://anonymous.4open.science/r/AudioJailbreak-4262/) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1259/)　📅 2025-05　🏷 ACL 2026

**关键词**：`benchmark`、`audio perturbation toolkit`、`Bayesian optimization`、`black-box evaluation`、`multimodal safety`、`LLM jailbreak`

👤 **作者**：Zirui Song、…、Xiuying Chen

- 🎯 **研究动机**：大型音频语言模型缺乏系统定量的越狱安全评测，语音的时序与语义特性使攻击评估困难
- 🔬 **研究方法**：AJailBench：1495 条对抗音频提示覆盖 10 类违规类别；Audio Perturbation Toolkit 在时、频、幅度域做定向失真，在语义一致性约束下用贝叶斯优化搜索扰动生成 APT+ 扩展集
- 📌 **结论**：没有一个 SOTA LAM 在各攻击下保持稳健，微小且语义保持的扰动即可显著降低安全性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rise of Large Audio-Language Models (LAMs) brings both potential and risks, as their audio outputs may contain harmful or unethical content. However, current research lacks a systematic, quantitative evaluation of LAM safety, especially against jailbreak attacks, which are challenging due to the temporal and semantic nature of speech. To bridge this gap, we introduce AJailBench, the first benchmark specifically designed to evaluate jailbreak vulnerabilities in LAMs. We begin by constructing -Base, a dataset of 1,495 adversarial audio prompts spanning 10 policy-violating categories. Using this dataset, we evaluate several state-of-the-art LAMs and reveal that none exhibit consistent robustness across attacks. To further strengthen jailbreak testing and simulate more realistic attack conditions, we propose a method to generate dynamic adversarial variants. Our Audio Perturbation Toolkit (APT) applies targeted distortions across time, frequency, and amplitude domains. To preserve the original jailbreak intent, we enforce a semantic consistency constraint and employ Bayesian optimization to efficiently search for perturbations that are both subtle and highly effective. This results in AJailBench-APT+, an extended dataset of optimized adversarial audio samples. Our findings demonstrate that even small, semantically preserved perturbations can significantly reduce the safety performance of leading LAMs, underscoring the need for more robust and semantically aware defense mechanisms. We release AJailBench to facilitate future research: https://anonymous.4open.science/r/AudioJailbreak-4262/

</details>

### 8. Jailbreak-AudioBench: In-Depth Evaluation and Analysis of Jailbreak Threats for Large Audio Language Models

📄 [arXiv](https://arxiv.org/abs/2501.13772) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0ff38d72a2e0aa6dbe42de83a17b2223-Abstract-Datasets_and_Benchmarks_Track.html)　📅 2025-01　🏷 NeurIPS 2025

**关键词**：`benchmark`、`Jailbreak-AudioBench`、`acoustic attribute`、`hidden semantics`

👤 **作者**：Hao Cheng、…、Renjing Xu

- 🎯 **研究动机**：大型音频语言模型的越狱漏洞基本未探索，直接合成文本语音不覆盖音频隐藏语义
- 🔬 **研究方法**：Jailbreak-AudioBench 由 Toolbox（文本转音频与注入隐藏语义的编辑）、显式/隐式越狱音频数据集与综合基准组成
- 📌 **结论**：系统评测多个 SOTA LALM，揭示基于查询的音频编辑等更强越狱威胁并支撑防御研究

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) demonstrate impressive zero-shot performance across a wide range of natural language processing tasks. Integrating various modality encoders further expands their capabilities, giving rise to Multimodal Large Language Models (MLLMs) that process not only text but also visual and auditory modality inputs. However, these advanced capabilities may also pose significant safety problems, as models can be exploited to generate harmful or inappropriate content through jailbreak attacks. While prior work has extensively explored how manipulating textual or visual modality inputs can circumvent safeguards in LLMs and MLLMs, the vulnerability of audio-specific jailbreak on Large Audio-Language Models (LALMs) remains largely underexplored. To address this gap, we introduce Jailbreak-AudioBench, which consists of the Toolbox, curated Dataset, and comprehensive Benchmark. The Toolbox supports not only text-to-audio conversion but also various editing techniques for injecting audio hidden semantics. The curated Dataset provides diverse explicit and implicit jailbreak audio examples in both original and edited forms. Utilizing this dataset, we evaluate multiple state-of-the-art LALMs and establish the most comprehensive Jailbreak benchmark to date for audio modality. Finally, Jailbreak-AudioBench establishes a foundation for advancing future research on LALMs safety alignment by enabling the in-depth exposure of more powerful jailbreak threats, such as query-based audio editing, and by facilitating the development of effective defense mechanisms.

</details>

### 9. Now You Hear Me: Audio Narrative Attacks Against Large Audio–Language Models

🎓 [Official](https://aclanthology.org/2026.eacl-long.278/)　📅 2026-03　🏷 ACL 2026

**关键词**：`attack`、`audio guardrail`、`narrative jailbreak`、`cross-modal policy gap`、`audio-language model`、`TTS delivery`

👤 **作者**：Ye Yu、Haibo Jin、Yaoning Yu、Jun Zhuang、Haohan Wang

- 🎯 **研究动机**：大音频语言模型直接处理原始语音，安全机制主要为文本校准，音频域漏洞未被表征
- 🔬 **研究方法**：用指令跟随 TTS 把被禁指令嵌入叙事式音频流，利用结构与声学特性绕过文本校准的安全机制
- 📌 **结论**：Gemini 2.0 Flash 等模型上合成语音叙事攻击成功率 98.26%，大幅超纯文本基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large audio-language models increasingly operate on raw speech inputs, enabling more seamless integration across domains such as voice assistants, education, and clinical triage. This transition, however, introduces a distinct class of vulnerabilities that remain largely uncharacterized. We examine the security implications of this modality shift by designing a text-to-audio jailbreak that embeds disallowed directives within a narrative-style audio stream. The attack leverages an advanced instruction-following text-to-speech (TTS) model to exploit structural and acoustic properties, thereby circumventing safety mechanisms primarily calibrated for text. When delivered through synthetic speech, the narrative format elicits restricted outputs from state-of-the-art models, including Gemini 2.0 Flash, achieving a 98.26% success rate that substantially exceeds text-only baselines. These results highlight the need for safety frameworks that jointly reason over linguistic and paralinguistic representations, particularly as speech-based interfaces become more prevalent.

</details>

### 10. The Alignment Curse: Modality Alignment Supercharges Audio Attacks via Text Transfer

📄 [arXiv](https://arxiv.org/abs/2602.02557)　📅 2026-02

**关键词**：`analysis`、`alignment curse`、`text-to-audio transfer`、`omni model`

👤 **作者**：Yupeng Chen、Junchi Yu、Aoxi Liu、Baoyuan Wu、Philip Torr、Adel Bibi

- 🎯 **研究动机**：文本越狱远比音频攻击成熟，更强 text-audio 模态对齐是否会系统迁移文本漏洞不明
- 🔬 **研究方法**：形式化并实证 Alignment Curse 原理，在 Qwen2.5-Omni、Qwen3-Omni 等 omni 模型上黑盒评测文本攻击、文本迁移音频攻击与音频攻击三类
- 📌 **结论**：文本迁移音频攻击与原生音频攻击相当或更强（音频仅访问时优势明显），模态对齐越紧密迁移越有效，揭示能力与安全的根本张力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in end-to-end trained omni-models have substantially improved audio capabilities by strengthening text-audio modality alignment. However, whether such alignment inadvertently facilitates the transfer of safety vulnerabilities across modalities remains underexplored. This question is critical as text-based jailbreak attacks are considerably more mature than audio-based ones; if they transfer systematically, current audio safety evaluations may underestimate risks originating from the text modality. In this paper, we introduce the Alignment Curse, a formally characterized and empirically validated principle showing that stronger modality alignment enables more effective transfer of attacks from text to audio, revealing a fundamental tension between capability and safety. Motivated by this principle, we conduct a comprehensive black-box evaluation of three attack categories on recent omni-models (e.g., Qwen2.5-Omni, Qwen3-Omni): text attacks, text-transferred audio attacks, and audio attacks. We find that text-transferred audio attacks perform comparably to, and often better than, audio-based attacks, exhibiting a clear advantage under audio-only access. This suggests that text-based vulnerabilities play a pivotal role in shaping audio safety risks. Finally, we empirically analyze the relationship between modality alignment and transfer effectiveness across attack methods and models, observing consistent support for the Alignment Curse: tighter modality alignment leads to more effective cross-modality attack transfer.

</details>

### 11. StyleBreak: Revealing Alignment Vulnerabilities in Large Audio-Language Models via Style-Aware Audio Jailbreak

📄 [arXiv](https://arxiv.org/abs/2511.10692) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/41093)　📅 2025-11　🏷 AAAI 2026

**关键词**：`attack`、`speech style`、`paralinguistic attribute`、`adaptive policy`

👤 **作者**：Hongyi Li、…、Jie Wu

- 🎯 **研究动机**：现有音频越狱忽略人类语音的风格变化
- 🔬 **研究方法**：StyleBreak联合控制linguistic、paralinguistic与extralinguistic属性，query-adaptive策略搜索风格
- 📌 **结论**：不同speech style系统性暴露LALM对齐漏洞

### 12. Investigating Safety Vulnerabilities of Large Audio-Language Models Under Speaker Emotional Variations

📄 [arXiv](https://arxiv.org/abs/2510.16893)　📅 2025-10

**关键词**：`analysis`、`speaker emotion`、`intensity variation`、`safety inconsistency`

👤 **作者**：Bo-Han Feng、…、Hung-yi Lee

- 🎯 **研究动机**：大型音频语言模型在副语言变化（说话人情绪）下的安全对齐仍未被探索
- 🔬 **研究方法**：构建多种情绪与强度表达的恶意语音指令数据集，评估多个 SOTA LALM 的安全一致性
- 📌 **结论**：不同情绪引发不同程度的不安全回复，强度效应非单调，中等强度表达常带来最大风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large audio-language models (LALMs) extend text-based LLMs with auditory understanding, offering new opportunities for multimodal applications. While their perception, reasoning, and task performance have been widely studied, their safety alignment under paralinguistic variation remains underexplored. This work systematically investigates the role of speaker emotion. We construct a dataset of malicious speech instructions expressed across multiple emotions and intensities, and evaluate several state-of-the-art LALMs. Our results reveal substantial safety inconsistencies: different emotions elicit varying levels of unsafe responses, and the effect of intensity is non-monotonic, with medium expressions often posing the greatest risk. These findings highlight an overlooked vulnerability in LALMs and call for alignment strategies explicitly designed to ensure robustness under emotional variation, a prerequisite for trustworthy deployment in real-world settings.

</details>

### 13. Multilingual and Multi-Accent Jailbreaking of Audio LLMs

📄 [arXiv](https://arxiv.org/abs/2504.01094)　📅 2025-04

**关键词**：`attack`、`multilingual audio`、`accent variation`、`acoustic perturbation`

👤 **作者**：Jaechul Roh、Virat Shejwalkar、Amir Houmansadr

- 🎯 **研究动机**：音频越狱研究以英语为中心，语言与口音变化构成的更大攻击面未被暴露
- 🔬 **研究方法**：提出 Multi-AudioJail，构建多语言多口音对抗音频数据集与层级评估管线，分析声学扰动与跨语言语音的交互
- 📌 **结论**：混响肯尼亚口音攻击使 JSR 最多升 57.25 个百分点；多模态模型纯音频攻击成功率为纯文本的 3.1 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Audio Language Models (LALMs) have significantly advanced audio understanding but introduce critical security risks, particularly through audio jailbreaks. While prior work has focused on English-centric attacks, we expose a far more severe vulnerability: adversarial multilingual and multi-accent audio jailbreaks, where linguistic and acoustic variations dramatically amplify attack success. In this paper, we introduce Multi-AudioJail, the first systematic framework to exploit these vulnerabilities through (1) a novel dataset of adversarially perturbed multilingual/multi-accent audio jailbreaking prompts, and (2) a hierarchical evaluation pipeline revealing that how acoustic perturbations (e.g., reverberation, echo, and whisper effects) interacts with cross-lingual phonetics to cause jailbreak success rates (JSRs) to surge by up to +57.25 percentage points (e.g., reverberated Kenyan-accented attack on MERaLiON). Crucially, our work further reveals that multimodal LLMs are inherently more vulnerable than unimodal systems: attackers need only exploit the weakest link (e.g., non-English audio inputs) to compromise the entire model, which we empirically show by multilingual audio-only attacks achieving 3.1x higher success rates than text-only attacks. We plan to release our dataset to spur research into cross-modal defenses, urging the community to address this expanding attack surface in multimodality as LALMs evolve.

</details>

### 14. Audio Is the Achilles' Heel: Red Teaming Audio Large Multimodal Models

🎓 [Official](https://aclanthology.org/2025.naacl-long.470/)　📅 2025-04　🏷 ACL 2025

**关键词**：`attack`、`audio red teaming`、`speech jailbreak`、`non-speech distraction`

👤 **作者**：Hao Yang、Lizhen Qu、Ehsan Shareghi、Gholamreza Haffari

- 🎯 **研究动机**：文本上安全对齐的模型在音频模态是否有一致防护未被探索
- 🔬 **研究方法**：三设定红队五个先进音频 LMM：音频与文本格式的有害问题、文本有害问题配非语音干扰音、语音特有越狱
- 📌 **结论**：开源音频 LMM 在有害音频问题上平均 ASR 达 69.14%，非语音噪声即引发漏洞；对 Gemini-1.5-Pro 的语音越狱 ASR 达 70.67%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Multimodal Models (LMMs) have demonstrated the ability to interact with humans under real-world conditions by combining Large Language Models (LLMs) and modality encoders to align multimodal information (visual and auditory) with text. However, such models raise new safety challenges of whether models that are safety-aligned on text also exhibit consistent safeguards for multimodal inputs. Despite recent safety-alignment research on vision LMMs, the safety of audio LMMs remains under-explored. In this work, we comprehensively red team the safety of five advanced audio LMMs under three settings: (i) harmful questions in both audio and text formats, (ii) harmful questions in text format accompanied by distracting non-speech audio, and (iii) speech-specific jailbreaks. Our results under these settings demonstrate that open-source audio LMMs suffer an average attack success rate of 69.14% on harmful audio questions, and exhibit safety vulnerabilities when distracted with non-speech audio noise. Our speech-specific jailbreaks on Gemini-1.5-Pro achieve an attack success rate of 70.67% on the harmful query benchmark. We provide insights on what could cause these reported safety-misalignments. Warning: this paper contains offensive examples.

</details>

### 15. Acoustic Interference: A New Paradigm Weaponizing Acoustic Latent Semantic for Universal Jailbreak against Large Audio Language Models

📄 [arXiv](https://arxiv.org/abs/2605.18168) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65189)　📅 2026-05　🏷 ICML 2026

**关键词**：`attack`、`acoustic latent semantic`、`universal interference`、`cross-modal alignment`、`LLM jailbreak`、`empirical evaluation`

👤 **作者**：Yanyun Wang、Yu Huang、Zi Liang、Xixin Wu、Li Liu

- 🎯 **研究动机**：已有 LALM 越狱把音频当作恶意 payload 载体，依赖语义优化或加性扰动
- 🔬 **研究方法**：AIA 提出范式转变：仅靠特定 Acoustic Latent Semantics（ALS）干扰安全对齐，内容良性的干扰音频作为通用越狱触发器，攻击 payload 与音频解耦
- 📌 **结论**：10 个 LALM、五个数据集上达 SOTA ASR；可解释性分析揭示推理路径漂移与 ALS 有效模式，暴露跨模态对齐的根本脆弱性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The integration of audio modality into Large Audio Language Models (LALMs) significantly expands their attack surface. Existing jailbreak paradigms predominantly treat audio as a carrier for malicious payloads, relying on semantic optimization, acoustic parameter control, or additive perturbation to embed harmful content into the audio signal. In this work, we challenge this necessity and propose a new paradigm in which the role of audio shifts from content injection to safety alignment interference. We reveal that LALM safety alignment can be compromised solely by specific Acoustic Latent Semantics (ALS), the underlying paralinguistic features intrinsic to the priors of audio generative models. Distinct from previous works that leverage explicit acoustic parameters to merely style malicious audio, we demonstrate that interference audio, benign in content but infused with specific ALS, can serve as a universal jailbreak trigger. Leveraging this insight, we propose the Acoustic Interference Attack (AIA), which decouples the attack payload from the audio. Specifically, AIA employs a set of universal, instruction-neutral interference audio, enabling standard malicious text queries to bypass safety alignment without instance-specific optimization. Extensive experiments on 10 LALMs across five datasets demonstrate that AIA achieves the state-of-the-art attack success rate. Furthermore, our interpretability analysis uncovers the inference path drift induced by AIA and identifies the inherent effective patterns within ALS, revealing the fundamental vulnerability of cross-modal alignment in LALMs.

</details>

### 16. Sparse Tokens Suffice: Jailbreaking Audio Language Models via Token-Aware Gradient Optimization

📄 [arXiv](https://arxiv.org/abs/2605.04700) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65673)　📅 2026-05　🏷 ICML 2026

**关键词**：`attack`、`TAGO`、`sparse audio token`、`gradient optimization`、`LLM jailbreak`、`empirical evaluation`

👤 **作者**：Zheng Fang、Xiaosen Wang、Shenyi Zhang、Shaokang Wang、Zhijin Ge

- 🎯 **研究动机**：audio 越狱普遍对整个波形稠密优化，其必要性从未被检验
- 🔬 **研究方法**：分析 token 对齐梯度发现能量跨 audio token 高度不均；TAGO 每轮只保留高梯度能量 token 对齐的波形梯度并掩码其余
- 📌 **结论**：三个 ALM 上超过基线，Qwen3-Omni 上保留 25% token 时 ASR 仍有 86%（全保留为 87%），证明稠密波形更新大量冗余

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak attacks on audio language models (ALMs) optimize audio perturbations to elicit unsafe generations, and they typically update the entire waveform densely throughout optimization. In this work, we investigate the necessity of such dense optimization by analyzing the structure of token-aligned gradients in ALMs. We find that gradient energy is highly non-uniform across audio tokens, indicating that only a small subset of token-aligned audio regions dominates the optimization signal. Motivated by this observation, we propose Token-Aware Gradient Optimization (TAGO), which enables sparse jailbreak optimization by retaining only waveform gradients aligned with audio tokens that have high gradient energy, while masking the remaining gradients at each iteration. Across three ALMs, TAGO outperforms baselines, and substantial sparsification preserves strong attack success rates (e.g. on Qwen3-Omni, $\mathrm{ASR}_{l}$ remains at 86% with a token retention ratio of 0.25, compared to 87% with full token retention). These results demonstrate that dense waveform updates are largely redundant, and we advocate that future audio jailbreak and safety alignment research should further leverage this heterogeneous token-level gradient structure.

</details>

### 17. Hijacking Large Audio-Language Models via Context-Agnostic and Imperceptible Auditory Prompt Injection

📄 [arXiv](https://arxiv.org/abs/2604.14604) · 🎓 [Official](https://sp2026.ieee-security.org/accepted-papers.html)　📅 2026-04　🏷 IEEE S&P 2026

**关键词**：`attack`、`AudioHijack`、`auditory prompt injection`、`context generalization`

👤 **作者**：Meng Chen、Kun Wang、Li Lu、Jiaheng Zhang、Tianwei Zhang

- 🎯 **研究动机**：LALM 音频通道的恶意注入与下游行为操纵研究不足，且需满足仅音频访问与强感知隐蔽的现实约束
- 🔬 **研究方法**：AudioHijack 用采样梯度估计绕过不可微 audio tokenization，结合 attention supervision 与多上下文训练生成 context-agnostic 扰动，再以卷积混响调制隐藏
- 📌 **结论**：13 个 LALM 上六类不当行为平均成功率 79%-96%，并诱导 Mistral AI 与 Microsoft Azure 商业语音代理执行未授权操作

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern Large audio-language models (LALMs) power intelligent voice interactions by tightly integrating audio and text. This integration, however, expands the attack surface beyond text and introduces vulnerabilities in the continuous, high-dimensional audio channel. While prior work studied audio jailbreaks, the security risks of malicious audio injection and downstream behavior manipulation remain underexamined. In this work, we reveal a previously overlooked threat, auditory prompt injection, under realistic constraints of audio data-only access and strong perceptual stealth. To systematically analyze this threat, we propose \textit{AudioHijack}, a general framework that generates context-agnostic and imperceptible adversarial audio to hijack LALMs. \textit{AudioHijack} employs sampling-based gradient estimation for end-to-end optimization across diverse models, bypassing non-differentiable audio tokenization. Through attention supervision and multi-context training, it steers model attention toward adversarial audio and generalizes to unseen user contexts. We also design a convolutional blending method that modulates perturbations into natural reverberation, making them highly imperceptible to users. Extensive experiments on 13 state-of-the-art LALMs show consistent hijacking across 6 misbehavior categories, achieving average success rates of 79\%-96\% on unseen user contexts with high acoustic fidelity. Real-world studies demonstrate that commercial voice agents from Mistral AI and Microsoft Azure can be induced to execute unauthorized actions on behalf of users. These findings expose critical vulnerabilities in LALMs and highlight the urgent need for dedicated defense.

</details>

### 18. GRM: Utility-Aware Jailbreak Attacks on Audio LLMs via Gradient-Ratio Masking

📄 [arXiv](https://arxiv.org/abs/2604.09222)　📅 2026-04

**关键词**：`attack`、`gradient-ratio masking`、`Mel-band selection`、`utility preservation`

👤 **作者**：Yunqiang Wang、Hengyuan Na、Di Wu、Miao Hu、Guocong Quan

- 🎯 **研究动机**：已有 audio 越狱扰动不控制频段，全频段通用扰动会降低正常任务效用并留下可监测的行为痕迹
- 🔬 **研究方法**：GRM 按 jailbreak 贡献与 transcript 敏感度的梯度比对 Mel band 排序，仅扰动选定频段并正则化语义偏移
- 📌 **结论**：四个 ALLM 上平均 JSR 88.46%，良性转写与回答任务的效用损失显著低于基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Audio Large Language Models (ALLMs) enable spoken interaction but introduce new jailbreak vulnerabilities. Existing perturbation-based jailbreaks do not explicitly control which frequency bands carry the perturbation. Although such perturbations can elicit unsafe responses, repeatedly applying a universal perturbation across diverse inputs may also degrade utility on normal tasks, leaving a conspicuous behavioral footprint that may expose the attack to users or automated monitoring systems and thereby compromise its stealthiness. To determine whether full-band perturbation is necessary, we vary coverage from partial-band to full-band. Jailbreak Success Rate (JSR) varies non-monotonically, while utility degradation grows with coverage. This mismatch shows that selected bands can yield stronger attacks with less utility degradation than full-band perturbations. Based on this observation, we propose GRM, a utility-aware, frequency-selective jailbreak framework that ranks Mel bands by the ratio between jailbreak contribution and transcript sensitivity, confines a universal perturbation to selected bands, and regularizes deviations from the intended request semantics. Experiments on four ALLMs show that GRM achieves an average JSR of 88.46\% while substantially reducing utility degradation across benign transcription and response tasks relative to baselines. Our code is available at \href{https://github.com/159753Fetter/GRM}{this repository}. Warning: This paper contains potentially sensitive content.

</details>

### 19. Attacker’s Noise Can Manipulate Your Audio-based LLM in the Real World

🎓 [Official](https://aclanthology.org/2026.eacl-long.66/)　📅 2026-03　🏷 ACL 2026

**关键词**：`attack`、`over-the-air noise`、`target action`、`bystander impact`、`audio-language model`、`over-the-air perturbation`

👤 **作者**：Vinu Sankar Sadasivan、Soheil Feizi、Rajiv Mathews、Lun Wang

- 🎯 **研究动机**：音频 LLM（如 Qwen2-Audio）在现实物理场景中的漏洞未被研究
- 🔬 **研究方法**：构造隐蔽音频扰动操纵 ALLM 产生目标行为（响应唤醒词、触发修改日历等有害操作），或在用户交互时播放对抗背景噪声降低回复质量，攻击可经空气传播
- 📌 **结论**：攻击可扩展到真实场景并波及无辜旁听用户，具有跨模型迁移性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper investigates the real-world vulnerabilities of audio-based large language models (ALLMs), such as Qwen2-Audio. We first demonstrate that an adversary can craft stealthy audio perturbations to manipulate ALLMs into exhibiting specific targeted behaviors, such as eliciting responses to wake-keywords (e.g., “Hey Qwen”), or triggering harmful behaviors (e.g., “Change my calendar event”). Subsequently, we show that playing adversarial background noise during user interaction with the ALLMs can significantly degrade the response quality. Crucially, our research illustrates the scalability of these attacks to real-world scenarios, impacting other innocent users when these adversarial noises are played through the air. Further, we discuss the transferability of the attack and potential defensive measures.

</details>

### 20. Sirens' Whisper: Inaudible Near-Ultrasonic Jailbreaks of Speech-Driven LLMs

📄 [arXiv](https://arxiv.org/abs/2603.13847) · 🌐 [Project](https://swhisper-jailbreak.github.io/) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/ling)　📅 2026-03　🏷 USENIX Security 2026

**关键词**：`attack`、`near-ultrasound`、`microphone nonlinearity`、`over-the-air`、`speech-driven LLM`、`ultrasonic jailbreak`

👤 **作者**：Zijian Ling、…、Bin Benjamin Zhu

- 🎯 **研究动机**：语音接口给 speech-driven LLM 引入开放声学通道的隐蔽攻击面
- 🔬 **研究方法**：SWhisper 把任意目标音频编码为近超声波，经非线性信道建模与信道反转预补偿在商用设备上无声还原，配语音感知的越狱生成保证可懂、简洁与迁移
- 📌 **结论**：商业模型上非拒答率达 0.94、specific-convincing 达 0.925，用户实验中注入音频与纯背景播放感知不可分

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Speech-driven large language models (LLMs) are increasingly accessed through speech interfaces, introducing new security risks via open acoustic channels. We present Sirens' Whisper (SWhisper), the first practical framework for covert prompt-based attacks against speech-driven LLMs under realistic black-box conditions using commodity hardware. SWhisper enables robust, inaudible delivery of arbitrary target baseband audio-including long and structured prompts-on commodity devices by encoding it into near-ultrasound waveforms that demodulate faithfully after acoustic transmission and microphone nonlinearity. This is achieved through a simple yet effective approach to modeling nonlinear channel characteristics across devices and environments, combined with lightweight channel-inversion pre-compensation. Building on this high-fidelity covert channel, we design a voice-aware jailbreak generation method that ensures intelligibility, brevity, and transferability under speech-driven interfaces. Experiments across both commercial and open-source speech-driven LLMs demonstrate strong black-box effectiveness. On commercial models, SWhisper achieves up to 0.94 non-refusal (NR) and 0.925 specific-convincing (SC). A controlled user study further shows that the injected jailbreak audio is perceptually indistinguishable from background-only playback for human listeners. Although jailbreaks serve as a case study, the underlying covert acoustic channel enables a broader class of high-fidelity prompt-injection and commandexecution attacks.

</details>

### 21. AudioJailbreak: Jailbreak Attacks against End-to-End Large Audio-Language Models

📄 [arXiv](https://arxiv.org/abs/2505.14103) · 🌐 [Project](https://doi.org/10.1109/TDSC.2026.3661073)　📅 2025-05

**关键词**：`attack`、`adversarial audio suffix`、`universal jailbreak`、`over-the-air robustness`

👤 **作者**：Guangke Chen、…、Bo Du

- 🎯 **研究动机**：既有音频越狱假设可完全操控用户 prompt 的强 adversary，文本攻击经 TTS 也难迁移
- 🔬 **研究方法**：提出 AudioJailbreak，构造后缀式越狱音频，具备异步、普适、意图隐蔽与空中播放鲁棒四特性，并适用于弱 adversary
- 📌 **结论**：在迄今最多的 LALM 上验证高效，弱 adversary 下仍可越狱 GPT-4o-Audio 并绕过 Llama-Guard-3

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak attacks to Large audio-language models (LALMs) are studied recently, but they exclusively focused on the attack scenario where the adversary can fully manipulate user prompts (named strong adversary) and limited in effectiveness, applicability, and practicability. In this work, we first conduct an extensive evaluation showing that advanced text jailbreak attacks cannot be easily ported to end-to-end LALMs via text-to-speech (TTS) techniques. We then propose AUDIOJAILBREAK, a novel audio jailbreak attack, featuring (1) asynchrony: the jailbreak audios do not need to align with user prompts in the time axis by crafting suffixal jailbreak audios; (2) universality: a single jailbreak perturbation is effective for different prompts by incorporating multiple prompts into the perturbation generation; (3) stealthiness: the malicious intent of jailbreak audios is concealed by proposing various intent concealment strategies; and (4) over-the-air robustness: the jailbreak audios remain effective when being played over the air by incorporating reverberation into the perturbation generation. In contrast, all prior audio jailbreak attacks cannot offer asynchrony, universality, stealthiness, and/or over-the-air robustness. Moreover, AUDIOJAILBREAK is also applicable to a more practical and broader attack scenario where the adversary cannot fully manipulate user prompts (named weak adversary). Extensive experiments with thus far the most LALMs demonstrate the high effectiveness of AUDIOJAILBREAK, in particular, it can jailbreak openAI's GPT-4o-Audio and bypass Meta's Llama-Guard-3 safeguard, in the weak adversary scenario. We highlight that our work peeks into the security implications of audio jailbreak attacks against LALMs, and realistically fosters improving their robustness, especially for the newly proposed weak adversary.

</details>

### 22. "I am bad": Interpreting Stealthy, Universal and Robust Audio Jailbreaks in Audio-Language Models

📄 [arXiv](https://arxiv.org/abs/2502.00718)　📅 2025-02

**关键词**：`analysis`、`universal perturbation`、`latent toxic speech`、`real-world robustness`

👤 **作者**：Isha Gupta、David Khachaturov、Robert Mullins

- 🎯 **研究动机**：音频语言模型的失败模式与通用音频越狱机制不明
- 🔬 **研究方法**：构造跨 prompt、任务与 base audio 的通用对抗扰动，并分析模型如何解读这些音频对抗样本
- 📌 **结论**：首个音频模态通用越狱且在模拟真实条件下有效；最有效扰动编码了不可感知的第一人称毒性语音

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rise of multimodal large language models has introduced innovative human-machine interaction paradigms but also significant challenges in machine learning safety. Audio-Language Models (ALMs) are especially relevant due to the intuitive nature of spoken communication, yet little is known about their failure modes. This paper explores audio jailbreaks targeting ALMs, focusing on their ability to bypass alignment mechanisms. We construct adversarial perturbations that generalize across prompts, tasks, and even base audio samples, demonstrating the first universal jailbreaks in the audio modality, and show that these remain effective in simulated real-world conditions. Beyond demonstrating attack feasibility, we analyze how ALMs interpret these audio adversarial examples and reveal them to encode imperceptible first-person toxic speech - suggesting that the most effective perturbations for eliciting toxic outputs specifically embed linguistic features within the audio signal. These results have important implications for understanding the interactions between different modalities in multimodal models, and offer actionable insights for enhancing defenses against adversarial audio attacks.

</details>

### 23. AdvWave: Stealthy Adversarial Jailbreak Attack against Large Audio-Language Models

📄 [arXiv](https://arxiv.org/abs/2412.08608) · 📝 [OpenReview](https://openreview.net/forum?id=0BujOfTqab)　📅 2024-12　🏷 ICLR 2025

**关键词**：`attack`、`AdvWave`、`audio suffix`、`gradient shattering`

👤 **作者**：Mintong Kang、Chejian Xu、Bo Li

- 🎯 **研究动机**：音频离散化导致gradient shattering，隐蔽性约束又压缩优化空间
- 🔬 **研究方法**：AdvWave结合双阶段优化、自适应目标搜索与classifier引导的城市声音约束生成隐蔽音频后缀
- 📌 **结论**：平均ASR比基线高约40%

### 24. Speech-Audio Compositional Attacks on Multimodal LLMs and Their Mitigation with SALMONN-Guard

📄 [arXiv](https://arxiv.org/abs/2511.10222) · 📊 [Dataset](https://huggingface.co/datasets/tsinghua-ee/SACRED-Bench) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64737)　📅 2025-11　🏷 ICML 2026

**关键词**：`defense`、`SALMONN-Guard`、`speech-audio composition`、`joint moderation`

👤 **作者**：Yudong Yang、…、Chao Zhang

- 🎯 **研究动机**：复杂音频输入中语音与非语音成分组合的安全风险未被现有防护覆盖
- 🔬 **研究方法**：SACRED-Bench 用有害/良性语音重叠、良性语音混合有害非语音、多说话人对话三种黑盒组合机制评测；并提出首个联合检查语音、音频与文本的 guard 模型 SALMONN-Guard
- 📌 **结论**：即使 Gemini 2.5 Pro 也达 66% ASR，SALMONN-Guard 将其降至 20%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent progress in LLMs has enabled understanding of audio signals, but has also exposed new safety risks arising from complex audio inputs that are inadequately handled by current safeguards. We introduce SACRED-Bench (Speech-Audio Composition for RED-teaming) to evaluate the robustness of LLMs under complex audio-based attacks. Unlike existing perturbation-based methods that rely on noise optimization or white-box access, SACRED-Bench exploits speech-audio composition to enable effective black-box attacks. SACRED-Bench adopts three composition mechanisms: (a) overlap of harmful and benign speech, (b) mixture of benign speech with harmful non-speech audio, and (c) multi-speaker dialogue. These mechanisms focus on evaluating safety in settings where benign and harmful intents co-occur within a single auditory scene. Moreover, questions in SACRED-Bench are designed to implicitly refer to content in the audio, such that no explicit harmful information appears in the text prompt alone. Experiments demonstrate that even Gemini 2.5 Pro, a state-of-the-art proprietary LLM with safety guardrails fully enabled, still exhibits a 66% attack success rate. To bridge this gap, we propose SALMONN-Guard, the first guard model that jointly inspects speech, audio, and text for safety judgments, reducing the attack success rate to 20%. Our results highlight the need for audio-aware defenses to ensure the safety of multimodal LLMs. The dataset and SALMONN-Guard checkpoints can be found at https://huggingface.co/datasets/tsinghua-ee/SACRED-Bench.

</details>

### 25. SARSteer: Safeguarding Large Audio-Language Models via Safe-Ablated Refusal Steering

📄 [arXiv](https://arxiv.org/abs/2510.17633) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66551)　📅 2025-10　🏷 ICML 2026

**关键词**：`defense`、`SARSteer`、`refusal steering`、`safe-space ablation`、`refusal calibration`、`representation steering`

👤 **作者**：Weilin Lin、Jianze Li、Hui Xiong、Li Liu

- 🎯 **研究动机**：LLM 式 steering 因激活分布差距在音频输入下失效，prompt 防御又对良性语音造成过度拒绝
- 🔬 **研究方法**：SARSteer 是首个 LALM 推理时防御框架，利用文本导出的 refusal steering 强制拒绝且不改音频输入，配合分解式 safe-space ablation 缓解误拒
- 📌 **结论**：显著提升有害查询的拒绝率同时保留良性响应，迈出 LALM 安全对齐的一步

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Audio-Language Models (LALMs) are becoming essential as a powerful multimodal backbone for real-world applications. However, recent studies show that audio inputs can more easily elicit harmful responses than text, exposing new risks toward deployment. While safety alignment has made initial advances in LLMs and Large Vision-Language Models (LVLMs), we find that vanilla adaptation of these approaches to LALMs faces two key limitations: 1) LLM-based steering fails under audio input due to the large distributional gap between activations, and 2) prompt-based defenses induce over-refusals on benign-speech queries. To address these challenges, we propose Safe-Ablated Refusal Steering (SARSteer), the first inference-time defense framework for LALMs. Specifically, SARSteer leverages text-derived refusal steering to enforce rejection without manipulating audio inputs and introduces decomposed safe-space ablation to mitigate over-refusal. Extensive experiments demonstrate that SARSteer significantly improves harmful-query refusal while preserving benign responses, establishing a principled step toward safety alignment in LALMs. The codes and constructed datasets are released at https://github.com/linweiii/SARSteer.

</details>

### 26. Still Between Us? Evaluating and Improving Voice Assistant Robustness to Third-Party Interruptions

🌐 [Project](https://tpi-va.github.io) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1902/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`adversarial robustness`、`audio language model`、`acoustic attack`、`high-risk deployment`、`failure mitigation`

👤 **作者**：Dongwook Lee、Eunwoo Song、Che Hyun Lee、Heeseung Kim、Sungroh Yoon

- 🎯 **研究动机**：口语模型无法区分第三方打断与主用户连续发言，存在语境失败风险，且模型依赖语义捷径而忽视区分说话人所需的声学信号
- 🔬 **研究方法**：构建含说话人感知难负样本的 88K 实例数据集 TPI-Train 与评测框架 TPI-Bench，测量打断处理策略与欺骗情境下的精确说话人判别
- 📌 **结论**：数据设计缓解语义捷径学习，为克服 SLM 文本主导的单模态依赖奠定基础

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While recent Spoken Language Models (SLMs) have been actively deployed in real-world scenarios, they lack the capability to discern Third-Party Interruptions (TPI) from the primary user’s ongoing flow, leaving them vulnerable to contextual failures. To bridge this gap, we introduce TPI-Train, a dataset of 88K instances designed with speaker-aware hard negatives to enforce acoustic cue prioritization for interruption handling, and TPI-Bench, a comprehensive evaluation framework designed to rigorously measure the interruption-handling strategy and precise speaker discrimination in deceptive contexts. Experiments demonstrate that our dataset design mitigates semantic shortcut learning—a critical pitfall where models exploit semantic context while neglecting acoustic signals essential for discerning speaker changes. We believe our work establishes a foundational resource for overcoming text-dominated unimodal reliance in SLMs, paving the way for more robust multi-party spoken interaction. The code for the framework is publicly available at https://tpi-va.github.io

</details>

### 27. LALM-as-a-Judge: Benchmarking Large Audio-Language Models for Safety Evaluation in Multi-Turn Spoken Dialogues

📄 [arXiv](https://arxiv.org/abs/2602.04796) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66557)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`safety evaluation`、`audio language model`、`acoustic attack`、`empirical evaluation`、`tail risk`

👤 **作者**：Amir Ivry、Shinji Watanabe

- 🎯 **研究动机**：口语对话的不安全内容评测以文本为中心，漏掉韵律与转写失败线索
- 🔬 **研究方法**：构建 24,000 个多轮口语对话（8 类不安全内容×5 严重度、单局部不安全轮），评 6 个 LALM 在纯文本/纯音频/多模态设定下当裁判的敏感性、严重度特异性与轮位偏差
- 📌 **结论**：音频提供超出转写语义的非词汇证据；多模态增益不普适（可为 text-anchored 或干扰），与音频通路瓶颈和融合限制相关

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Evaluation of socially unsafe content in spoken dialogues remains text-centric, missing prosody and transcription failures. We present LALM-as-a-Judge, which includes an open benchmark of 24,000 multi-turn spoken dialogues with one localized unsafe turn, generated out of 8 socially unsafe categories and 5 severity levels. We evaluate 6 large audio-language models (LALMs) as judges, open and closed-source, in text-only, audio-only, and multimodal setups by their sensitivity, severity-order specificity, and turn-position bias for socially harmful content in the dialogue. Results show that audio contributes non-lexical evidence beyond transcript semantics and that multimodal gains are not universal but can be text-anchored, balanced, conservative, and interfering, which we link to the audio pathway bottlenecks and fusion limits. We position the benchmark as diagnostic and derive practitioner guidance for model, modality, and prompts choices.

</details>

### 28. ARENA: Automated Red-Teaming for Large Audio Language Models

📄 [arXiv](https://arxiv.org/abs/2608.15578)　📅 2026-08

**关键词**：`analysis`、`audio language model`、`acoustic attack`、`cross-modal safety`

👤 **作者**：Jiaming He、…、Xudong Jiang

- 🎯 **研究动机**：大型音频语言模型的安全面难以用纯文本红队暴露，文本安全但音联合入有害的攻击缺自动化方法
- 🔬 **研究方法**：ARENA 闭环框架：在 2000 例独立文本-音频集上训练控制器，MD-Judge 供训练奖励与自适应搜索反馈，非自适应 Llama Guard 3 单独标注最终结果
- 📌 **结论**：520 个保留 AdvBench 目标上 FDR/PSR 达 87.9/100.0%（Audio Flamingo 3）、71.5/96.3%（Qwen2-Audio）等，反馈精炼与音频变体搜索显著提升攻击发现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large audio-language models (LALMs) make it possible to interact with language models through speech, music, and environmental sound, but they also introduce a safety surface that is difficult to expose with text-only red-teaming. We study automated audio-grounded red-teaming, where a text query must remain safe in isolation while the joint text-audio input induces harmful target behavior. We propose ARENA, a closed-loop framework that trains a controller on an independent 2,000case text-audio dataset. MD-Judge supplies training rewards and adaptive search feedback, while a separate, non-adaptive Llama Guard 3 evaluator alone labels final outcomes. On 520 held-out AdvBench objectives, ARENA achieves FDR/PSR of 87.9/100.0%, 71.5/96.3%, 68.1/100.0%, and 75.4/98.5% on Audio Flamingo 3, Qwen2-Audio, MiMo-Audio, and GPTAudio, respectively. Ablations show that feedback-based refinement and audio-variant search substantially improve attack discovery.

</details>

### 29. DuplexJail: Safety Alignment Breaks Under Spoken Interruption in Full-Duplex Models

📄 [arXiv](https://arxiv.org/abs/2609.09420)　📅 2026-09

**关键词**：`attack`、`full-duplex speech jailbreak`、`spoken interruption`、`safety alignment`

👤 **作者**：Jaechul Roh、Deepak Chandran、Amir Houmansadr、Andrea Fanelli

- 🎯 **研究动机**：全双工语音模型边听边生成，说话打断形成未探索的越狱攻击面
- 🔬 **研究方法**：DuplexJail 经用户音频通道注入固定语音 prompt，比较固定延迟打断与拒绝触发打断（4 模型 × 720 有害请求）
- 📌 **结论**：AdvBench 整句 ASR 升至 40.3/48.7%（+33.8/+39.3pp）；拒绝触发策略达 35.6/48.6%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Full-duplex speech models accept user speech while generating responses, creating an underexplored attack surface. We introduce DuplexJail, which delivers fixed, request-independent spoken prompts through the user audio channel. We compare fixed-delay interruption after the harmful request ends with refusal-triggered interruption following a cue in the model's streaming text. Across four open-source models and 720 harmful requests from AdvBench and HarmBench, fixed-delay interruption raises whole-response attack success rates on AdvBench to 40.3% for PersonaPlex and 48.7% for PersonaPlex-RL, increases of +33.8 and +39.3 percentage points. The refusal-triggered policy reaches 35.6% and 48.6%, respectively, with all trials scored regardless of whether an interruption occurs. Selected conditions also increase FLM-Audio's harmful-response rate, while BayLing-Duplex shows decreases. These findings identify spoken interruption as a jailbreak attack vector and motivate evaluating safety throughout ongoing full-duplex interaction.

</details>

### 30. Auditing Bias and Safety in Voice AI Customer Care

📄 [arXiv](https://arxiv.org/abs/2609.04206)　📅 2026-09

**关键词**：`analysis`、`voice-agent safety`、`validation gates`、`service burden`

👤 **作者**：Vignesh Ethiraj、Ashwath David

- 🎯 **研究动机**：语音客服评测多止于语音识别差异，未把客服 voice agent 当作有状态、多轮、工具中介系统——伤害可在最终拒绝前以额外负担形式出现
- 🔬 **研究方法**：形式化带验证门的审计框架：分离端到端、级联与混合工具中介三种架构，跨受控来电表现条件匹配服务事实，先验证事实不变性、表现线索与声学测量再做推断，记录实质结局与服务负担路径
- 📌 **结论**：给出七道验证门、六族指标与主张边界；本版只含退款纠纷的合成示例，生产系统结果待验证协议放行

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Voice AI systems increasingly mediate customer care interactions where caller presentation cues such as accent, affect, fluency, and urgency are available alongside the service request. Existing fairness and safety evaluations cover speech recognition disparities, spoken dialogue bias, and voice agent capability, but rarely treat customer care voice agents as stateful, multi turn, tool mediated systems where harm can appear as additional burden before any final denial occurs. We formalize a validation gated audit framework for such systems. The framework (i) separates native speech to speech, cascaded ASR to language model to TTS, and hybrid tool mediated architectures; (ii) uses matched service facts across controlled caller presentation conditions; (iii) validates fact invariance, presentation cues, artifacts, and acoustic measurements before inference; and (iv) records both material outcomes and path to service burden. We define the research problem, methodology, seven validation gates, a six family metric set, and claim boundaries for an active industry evaluation program. We illustrate the framework with a fully synthetic worked example of a refund dispute audit instance. Production system results are excluded from this release; public reporting is gated by the validation protocol.

</details>

### 31. RoleBreak: Benchmarking Long-Horizon Role-Playing Robustness in Spoken Dialogue

📄 [arXiv](https://arxiv.org/abs/2609.16614)　📅 2026-09

**关键词**：`benchmark`、`spoken dialogue`、`role-playing`、`persona safety`、`long-horizon robustness`

👤 **作者**：Yuqi Wang、Fengyuan Liu、Haochen Luo、Zhiqi Yu、Qi Liu

- 🎯 **研究动机**：语音到语音对话模型日益支持 persona 控制，但既有 spoken role-playing 基准以预设角色与短程为主——长程多角色持续能力（尤其安全性）未知
- 🔬 **研究方法**：RoleBreak：310 个角色型与用户中心角色、6,688 个人工验证对话轮、11,743 条细粒度评测标准（1,856 轮带声音情感目标），场景压测长程角色一致性、交互质量、安全与情感；评测 9 种配置（全双工、全模态、级联 ASR-LLM-TTS）
- 📌 **结论**：系统语义角色遵循远强于声音情感；长程语义鲁棒性脆弱——最强系统平均 10.4 轮后出现首次 persona 失败、11.6 轮后首次安全失败；放大 LLM 显著改善语义鲁棒性并对声音情感几乎无益；用户声音情感即使语言内容固定也会影响角色扮演行为。ICASSP 2027 投稿

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Speech-to-speech dialogue models increasingly support persona control, yet existing spoken role-playing benchmarks remain largely character-centric and short-horizon. This leaves open whether spoken dialogue models can sustain diverse roles over extended interactions, especially beyond predefined fictional characters. We introduce RoleBreak, an open benchmark for long-horizon role-playing robustness in spoken dialogue. RoleBreak contains 310 character-based and user-centered roles, 6,688 human-verified dialogue turns, and 11,743 fine-grained evaluation criteria, with 1,856 turns carrying expressive emotion targets for evaluating vocal emotion. Its scenarios are designed to stress role consistency, interaction quality, safety, and affect over extended conversations. We evaluate nine configurations spanning full-duplex, omni-modal, and cascaded ASR--LLM--TTS paradigms. We find four key patterns. First, current systems are substantially stronger at semantic role adherence than at vocal emotion. Second, semantic robustness remains brittle over long interactions: even the strongest evaluated system encounters its first persona and safety failures after only 10.4 and 11.6 turns on average. Third, scaling the LLM substantially improves semantic robustness and delays failure, but yields little improvement in vocal emotion. Finally, user vocal emotion affects role-playing behavior even when linguistic content is fixed. These findings highlight persistent gaps in both long-horizon robustness and vocal expressiveness in spoken role-playing systems.

</details>
