# Streaming Guardrail

[返回 Guardrail 领域目录](README.md)

## 研究方向

本页研究在生成尚未结束时判断并阻断风险，使 unsafe content 不必等完整响应生成后才被发现。关键设计包括 token 或 sentence 级观察粒度、prefix forecasting、生成 hidden-state trajectory、训练数据的时序标注、早停阈值和 false positive；评测必须同时报告安全性、介入时机、额外延迟与 benign stream 的误拦截。

## 研究脉络

- **事后审核到 partial detection：** 早期 streaming monitor 用 response-level 与 token-level 双重监督缩小完整响应训练和不完整 prefix 推理之间的差距，并直接触发 early stopping。
- **生成内部状态：** Kelp、TrajGuard、NExT-Guard 与 lightweight probe 不只读取可见文本，而是追踪 hidden-state dynamics、滑动窗口 trajectory、SAE feature 或中层 activation，从风险形成过程提前判断。
- **预测未来风险：** StreamGuard 与 FreoStream 将问题从“当前 prefix 是否已经有害”改写为“未来 continuation 是否会走向有害”，减少对精确 token boundary 标注的依赖。
- **审核粒度与用户体验：** SentGuard 以 sentence buffer 平衡语义完整性和暴露延迟，研究重点由单一 F1 扩展到 on-time intervention、false positive 和 guard invocation cost。
- **统一部署接口：** Qwen3Guard 等通用 guard 开始提供独立 streaming model，使 token stream moderation 成为可直接接入的生产能力。

## 可见文本的前缀判断与未来预测

### 1. Online Safety Monitoring for LLMs

📄 [arXiv](https://arxiv.org/abs/2607.02510) · 🌐 [Project](https://safe-ai-workshop.github.io/uai-2026/)　📅 2026-07　🏷 ICML 2026 Workshop

**关键词**：`defense`、`detection`、`online monitor`、`risk control`、`alarm calibration`、`online monitoring`

👤 **作者**：Mona Schirmer、Metod Jazbec、Alexander Timans、Christian Naesseth、Maja Waldron、Eric Nalisnick

- 🎯 **研究动机**：对齐训练后 LLM 部署时仍可能产生不安全输出，需要在线监测并在安全性无法保证时报警
- 🔬 **研究方法**：研究把外部验证器信号经阈值化转为报警的简单实时监视器，阈值经风险控制校准，在数学推理与红队数据集上与序贯假设检验监视器对比
- 📌 **结论**：该简单设计与更先进的监视器性能相当

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite alignment training, LLMs remain prone to generating unsafe outputs at deployment time. Monitoring outputs online and raising an alarm when safety can no longer be assumed is therefore critical. We study a simple real-time monitor that turns a verifier signal from an external model into an alarm decision by thresholding, with the threshold calibrated via risk control. In experiments on mathematical reasoning and red teaming datasets, we show that this simple design is competitive with more advanced monitors based on sequential hypothesis testing.

</details>

### 2. FreoStream: Enhancing Stream Guardrails via Future-Aware Reasoning and Safety-Aligned Optimization

📄 [arXiv](https://arxiv.org/abs/2606.13737)　📅 2026-06

**关键词**：`defense`、`future-aware reasoning`、`stream moderation`、`over-refusal`

👤 **作者**：Jianwei Wang、…、Ziqian Zeng

- 🎯 **研究动机**：流式护栏缺全文上下文，过度保守拦截敏感但安全的 token（over-refusal），也难以检出隐含有害内容
- 🔬 **研究方法**：提出 FreoStream：检测到不安全 token 时由 LoRA 模块执行 Future-Reason-Judge（预测未来-推理全文-再判定），并从推理梯度提取安全对齐分量更新护栏
- 📌 **结论**：多个安全基准上同时降低 over-refusal 并提升越狱防御，优于现有流式护栏

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Stream guardrails enable token-level safety detection before full responses are generated. However, they often make overly conservative judgements and block those sensitive but safe tokens, which is known as over-refusal. Due to lack of full context, they also fail to detect implicitly harmful content from jailbreaking. To address these challenges, we propose FreoStream, a novel streaming guardrail framework. Specifically, FreoStream fine-tunes a LoRA module to perform Future-Aware Reasoning when the base guardrail detects unsafe tokens. The reasoning process follows a Future-Reason-Judge paradigm: predict the future, reason about the full context and give the final judgement. This design can effectively reduce over-refusal by incorporating the future information. Moreover, we introduce the Safety-Aligned Optimization module that extracts the safety-aligned component from the reasoning gradients to update the base guardrail model, thereby enhancing streaming safety detection. Extensive experiments on various safety benchmarks demonstrate that FreoStream achieves lower over-refusal rates and better jailbreak defense compared to existing streaming guardrails.

</details>

### 3. SentGuard: Sentence-Level Streaming Guardrails for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2606.02041)　📅 2026-06

**关键词**：`defense`、`sentence-level moderation`、`waiting buffer`、`early detection`

👤 **作者**：Jiaqi Yu、…、Yingchun Wang

- 🎯 **研究动机**：流式长回复下何时干预与是否干预同等关键：响应级太晚，token 级语义不完整且决策不稳
- 🔬 **研究方法**：SentGuard 句级流式护栏：轻量等待缓冲把 token 组成句子块只放行已验证块、与生成并行；构建逐句标注的 StreamSafe 基准，粗到细目标在句边界尽早检出不良意图
- 📌 **结论**：五个安全基准上超过基线，两句内检出 90.5% 不安全案例，流式误报率仅 7.41%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models increasingly stream long, reasoning-intensive responses in real time, making when to moderate as critical as whether to moderate. Existing guardrails fall into two unsatisfactory extremes: response-level methods delay intervention until the full output is generated, whereas token-level methods act on incomplete semantics, often producing unstable decisions and excessive guard invocations. To address this challenge, we propose SentGuard, a sentence-level streaming guardrail that operates in parallel with generation. A lightweight waiting buffer groups streamed tokens into sentence chunks and releases only verified chunks to the user, introducing a small offset that enables SentGuard to assess the current prefix while the target LLM decodes subsequent content. To support this, we construct StreamSafe, a benchmark with structured per-sentence annotations across 8 harm categories, capturing the evolution of safety risks across both reasoning and response segments. We further train SentGuard with a coarse-to-fine objective to detect unsafe intent as soon as it emerges at sentence boundaries. Experiments on 5 safety benchmarks show that SentGuard outperforms existing baselines, detecting 90.5% of unsafe cases within two sentences while maintaining a low streaming false-positive rate of 7.41%.

</details>

### 4. Predict, Don't React: Value-Based Safety Forecasting for LLM Streaming

📄 [arXiv](https://arxiv.org/abs/2604.03962)　📅 2026-04

**关键词**：`defense`、`risk forecasting`、`Monte Carlo rollout`、`boundary-free supervision`

👤 **作者**：Pride Kavumba、Koki Wataoka、Huy H. Nguyen、Jiaxuan Li、Masaya Ohagi

- 🎯 **研究动机**：流式输出审核被形式化为边界检测，只能在内容已不安全后触发且需精确 token 级标注
- 🔬 **研究方法**：StreamGuard 把审核改为预测问题：给定部分前缀预测可能续写的期望有害性，用 Monte Carlo rollout 监督，无需边界标注
- 📌 **结论**：8B 规模输入审核 F1 86.7→88.2、流式输出 F1 80.4→81.9；漏检率从 7.9% 降到 4.9%，监督信号可跨 tokenizer 与模型族迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In many practical LLM deployments, a single guardrail is used for both prompt and response moderation. Prompt moderation operates on fully observed text, whereas streaming response moderation requires safety decisions to be made over partial generations. Existing text-based streaming guardrails commonly frame this output-side problem as boundary detection, training models to identify the earliest prefix at which a response has already become unsafe. In this work, we introduce StreamGuard, a unified model-agnostic streaming guardrail that instead formulates moderation as a forecasting problem: given a partial prefix, the model predicts the expected harmfulness of likely future continuations. We supervise this prediction using Monte Carlo rollouts, which enables early intervention without requiring exact token-level boundary annotations. Across standard safety benchmarks, StreamGuard performs strongly both for input moderation and for streaming output moderation. At the 8B scale, StreamGuard improves aggregated input-moderation F1 from 86.7 to 88.2 and aggregated streaming output-moderation F1 from 80.4 to 81.9 relative to Qwen3Guard-Stream-8B-strict. On the QWENGUARDTEST response_loc streaming benchmark, StreamGuard reaches 97.5 F1, 95.1 recall, and 92.6% on-time intervention, compared to 95.9 F1, 92.1 recall, and 89.9% for Qwen3Guard-Stream-8B-stric, while reducing the miss rate from 7.9% to 4.9%. We further show that forecasting-based supervision transfers effectively across tokenizers and model families: with transferred targets, Gemma3-StreamGuard-1B reaches 81.3 response-moderation F1, 98.2 streaming F1, and a 3.5% miss rate. These results show that strong end-to-end streaming moderation can be obtained without exact boundary labels, and that forecasting future risk is an effective supervision strategy for low-latency safety intervention.

</details>

### 5. From Judgment to Interference: Early Stopping LLM Harmful Outputs via Streaming Content Monitoring

📄 [arXiv](https://arxiv.org/abs/2506.09996) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/4e3157021c5f833bb2204081f1dda573-Abstract-Conference.html)　📅 2025-06　🏷 NeurIPS 2025

**关键词**：`defense`、`partial detection`、`token supervision`、`early stopping`

👤 **作者**：Yang Li、Qiang Sheng、Yehan Yang、Xueyao Zhang、Juan Cao

- 🎯 **研究动机**：全量检测需等完整输出导致高延迟，直接把全量训练的审核器用于部分输出存在训练-推理鸿沟
- 🔬 **研究方法**：构建 29K 细粒度标注的 FineHarm 数据集，训练响应级与 token 级双重监督的流式内容监视器 SCM
- 📌 **结论**：平均只看前 18% token 即得 0.95+ macro F1 与全量检测相当，还可作伪标注器使无害性超过 DPO

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Though safety alignment has been applied to most large language models (LLMs), LLM service providers generally deploy a subsequent moderation as the external safety guardrail in real-world products. Existing moderators mainly practice a conventional full detection, which determines the harmfulness based on the complete LLM output, causing high service latency. Recent works pay more attention to partial detection where moderators oversee the generation midway and early stop the output if harmfulness is detected, but they directly apply moderators trained with the full detection paradigm to incomplete outputs, introducing a training-inference gap that lowers the performance. In this paper, we explore how to form a data-and-model solution that natively supports partial detection. For the data, we construct FineHarm, a dataset consisting of 29K prompt-response pairs with fine-grained annotations to provide reasonable supervision for token-level training. Then, we propose the streaming content monitor, which is trained with dual supervision of response- and token-level labels and can follow the output stream of LLM to make a timely judgment of harmfulness. Experiments show that SCM gains 0.95+ in macro F1 score that is comparable to full detection, by only seeing the first 18% of tokens in responses on average. Moreover, the SCM can serve as a pseudo-harmfulness annotator for improving safety alignment and lead to a higher harmlessness score than DPO.

</details>

### 6. LMSM: LLM Security Framework Inspired by Linux Security Modules

📄 [arXiv](https://arxiv.org/abs/2608.25697)　📅 2026-08

**关键词**：`defense`、`tool`、`security backend`、`runtime enforcement`、`production guard architecture`、`versioned policy`

👤 **作者**：XiuYu Zhang、Bonan Ruan、Junfeng Fang、An Zhang、Tat-Seng Chua、Zhenkai Liang

- 🎯 **研究动机**：模型内部安全信号各自绑定校准、策略与干预代码，无法汇成统一运行时防御
- 🔬 **研究方法**：LMSM 借鉴 Linux Security Modules：分离校准证据 backend、版本化 policy 与输出授权 gate，适配 Transformers 与 vLLM
- 📌 **结论**：Qwen3-4B 上 HarmBench ASR 从 39.20% 降至 3.32%（误拒仅增 2 个点），32 活跃序列下保留 98.14% 吞吐

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed with layered defenses, yet malicious prompts can still bypass them. Interpretability methods can expose model-internal signals along the generation path that could inform enforcement, but these signals are not security controls by themselves. Deployments that adapt them for safety typically couple each signal to its own calibration, policy logic, and intervention code, so each new artifact creates integration work instead of strengthening a shared defense. We present Language Model Security Modules (LMSM), a security framework that adapts the separation behind Linux Security Modules (LSM) to LLM serving. In LMSM, a selected security backend exposes calibrated evidence, a versioned policy evaluates active rules over trusted per-request context, and a separate gate authorizes buffered output release. This design separates mediation correctness from policy effectiveness, and it allows backend, rule, or schedule changes without rebuilding request handling or enforcement. Our prototype shows the separation working in practice: with Hugging Face Transformers and continuously batched vLLM, the same substrate hosts artifact-backed sparse autoencoder (SAE) and transcoder deployments and task-fitted dense probes, preserves request-specific decisions under scheduler churn, and selectively enforces and composes multiple rules per request. On Qwen3-4B, LMSM-Checkpoint reduces HarmBench attack success rate from 39.20% to 3.32%, with XSTest false refusals rising from 2.40% to 4.40%, while retaining 98.14% of the throughput of a matched serving path that performs no monitoring work at 32 active sequences. LMSM gives advances in interpretability and model-internal analysis a common path to runtime enforcement.

</details>

### 7. Stop Early, Spend Less: Hidden-State Probes as a Practical Recipe for Streaming Moderation of LLM Outputs

📄 [arXiv](https://arxiv.org/abs/2606.10487)　📅 2026-06

**关键词**：`defense`、`token-level probe`、`activation reuse`、`streaming moderation`、`hidden-state probe`、`token monitoring`

👤 **作者**：Huizhen Shu、Xuying Li、Piao Xue

- 🎯 **研究动机**：生成后单独审核模型使推理成本翻倍且只能在生成完成后发现违规，而审核所需信号已存在于隐藏状态中
- 🔬 **研究方法**：在生成器激活上训练轻量 token 级探针，复用激活免额外前向，在解码环内做亚毫秒逐 token 安全评分，支持流式提前中止或改写，并给出部署配方
- 📌 **结论**：单中层探针即可恢复强护栏模型大部分决策，计算开销比事后/流式护栏低多个数量级，探针线性分量还可做激活转向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deploying large language models in user-facing systems requires efficient output safety filtering. Existing approaches typically rely on a separate moderation model applied after generation, which doubles inference cost and only detects violations after generation completes. We observe that the signal needed for moderation is already present in the model hidden states. Based on this, we train lightweight token-level probes that operate directly on internal activations, producing per-token safety scores that can be aggregated for both offline evaluation and online intervention. The probe reuses activations from the generator and requires no additional forward pass, enabling sub millisecond per-token safety checks inside the decoding loop. A probe applied to a single mid layer recovers most decisions of a strong guard model, acting as a low cost surrogate optimized for latency rather than accuracy. In streaming settings, it can halt or modify unsafe outputs before they are fully generated, replacing end of sequence moderation with continuous token level monitoring. Compared to post hoc and streaming guard models, our method achieves orders of magnitude lower compute overhead with minimal latency cost. We also provide a practical deployment recipe, including layer selection, aggregation strategy, probing frequency, and triggering thresholds. Finally, we show that the probe linear component corresponds to a direction in residual space, enabling both detection and activation steering at negligible cost.

</details>

### 8. TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense

📄 [arXiv](https://arxiv.org/abs/2604.07727) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.655/)　📅 2026-04　🏷 ACL 2026

**关键词**：`defense`、`hidden-state trajectory`、`sliding window`、`decoding-time defense`

👤 **作者**：Cheng Liu、Xiaolei Liu、Xingyu Li、Bangzhou Xin、Kangyi Ding

- 🎯 **研究动机**：现有越狱防御依赖静态检测 prompt、输出或单点内部状态，忽略解码过程中风险的动态演化
- 🔬 **研究方法**：TrajGuard 免训练，用滑动窗口聚合解码期关键层隐状态轨迹实时量化风险，持续超阈值才触发轻量语义裁决并中断解码
- 📌 **结论**：12 种越狱攻击上平均防御率 95%，延迟 5.2 ms/token，FPR 低于 1.5%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing jailbreak defense paradigms primarily rely on static detection of prompts, outputs, or internal states, often neglecting the dynamic evolution of risk during decoding. This oversight leaves risk signals embedded in decoding trajectories underutilized, constituting a critical blind spot in current defense systems. In this work, we empirically demonstrate that hidden states in critical layers during the decoding phase carry stronger and more stable risk signals than input jailbreak prompts. Specifically, the hidden representations of tokens generated during jailbreak attempts progressively approach high-risk regions in the latent space. Based on this observation, we propose TrajGuard, a training-free, decoding-time defense framework. TrajGuard aggregates hidden-state trajectories via a sliding window to quantify risk in real time, triggering a lightweight semantic adjudication only when risk within a local window persistently exceeds a threshold. This mechanism enables the immediate interruption or constraint of subsequent decoding. Extensive experiments across 12 jailbreak attacks and various open-source LLMs show that TrajGuard achieves an average defense rate of 95%. Furthermore, it reduces detection latency to 5.2 ms/token while maintaining a false positive rate below 1.5%. These results confirm that hidden-state trajectories during decoding can effectively support real-time jailbreak detection, highlighting a promising direction for defenses without model modification.

</details>

### 9. Beyond Content Safety: Real-Time Monitoring for Reasoning Vulnerabilities in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2603.25412)　📅 2026-03

**关键词**：`detection`、`reasoning safety`、`step-level monitor`、`runtime interruption`、`reasoning-step stream`、`parallel verifier`

👤 **作者**：Xunguang Wang、…、Shuai Wang

- 🎯 **研究动机**：推理过程本身的安全性（逻辑一致、高效、抗操纵）被当作黑箱中间产物，内容安全之外的正交维度未被处理
- 🔬 **研究方法**：形式化推理安全并建立九类不安全推理行为分类法，标注超 4,000 条推理链；外部零 shot 监控器并行逐步检查并实时发出中断信号
- 📌 **结论**：步骤级定位准确率最高 87.11%，大幅超幻觉检测器与最佳过程奖励模型，低误报、延迟可忽略且抗自适应规避

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models increasingly rely on explicit chain-of-thought reasoning to solve complex tasks, yet the safety of the reasoning process itself remains largely unaddressed. Existing work focuses predominantly on content safety (i.e., detecting harmful, biased, or factually incorrect outputs), while treating the underlying reasoning chain as an opaque intermediate artifact. We argue that reasoning safety constitutes a fundamental security dimension orthogonal to content safety: the requirement that a model's reasoning trajectory be logically consistent, computationally efficient, and resistant to adversarial manipulation. In this paper, we formalize reasoning safety and introduce a systematic taxonomy of nine unsafe reasoning behaviors. We then conduct a large-scale prevalence study, annotating over 4,000 reasoning chains across benign benchmarks and four state-of-the-art reasoning attacks, empirically demonstrating that all nine error types occur in practice with mechanistically interpretable signatures. To mitigate these threats, we propose the Reasoning Safety Monitor: an external, zero-shot verification framework that runs in parallel with the target LLM. It inspects each reasoning step in real time via a taxonomy-embedded prompt and dispatches an interrupt signal upon detecting unsafe behavior. Extensive evaluations show our monitor achieves up to 87.11% step-level localization accuracy, outperforming hallucination detectors and the best process reward model baselines by a substantial margin. Crucially, the monitor maintains a low false positive rate on correct reasoning paths, operates with negligible latency overhead, and exhibits robust resilience against adaptive adversarial evasion. These findings establish reasoning safety monitoring as a highly feasible and essential component for the secure deployment of large reasoning models.

</details>

### 10. NExT-Guard: Training-Free Streaming Safeguard without Token-Level Labels

📄 [arXiv](https://arxiv.org/abs/2603.02219) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66186)　📅 2026-02　🏷 ICML 2026

**关键词**：`defense`、`SAE feature`、`training-free monitor`、`latent risk`、`refusal calibration`、`empirical evaluation`

👤 **作者**：Junfeng Fang、…、Tat-Seng Chua

- 🎯 **研究动机**：流式场景下事后护栏无法实时拦截，token 级监督训练又需昂贵标注且严重过拟合
- 🔬 **研究方法**：NExT-Guard 免训练监测公开 SAE 的可解释潜在特征，利用事后护栏已编码于隐藏表示的 token 级风险信号实现流式防护
- 📌 **结论**：优于监督训练的事后与流式护栏，且跨模型、SAE 变体与风险场景稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are increasingly deployed in streaming scenarios, rendering conventional post-hoc safeguards ineffective as they fail to interdict unsafe content in real-time. While streaming safeguards based on token-level supervised training could address this, they necessitate expensive annotations and suffer from severe overfitting. In this work, we challenge the paradigm that streaming safety must rely on token-level supervised training. Instead, it is an inherent capability of well-trained post-hoc safeguards, as they already encode token-level risk signals in hidden representations. Hence, we introduce NExT-Guard, a training-free framework that achieves streaming safeguards by monitoring interpretable latent features from Sparse Autoencoders (SAEs). It uses pretrained SAEs from publicly available base LLMs, enabling flexible, low-cost deployment without token-level supervision. Experimental results show that NExT-Guard outperforms both post-hoc and streaming safeguards based on supervised training, with superior robustness across models, SAE variants, and risk scenarios. These results make NExT-Guard a universal and scalable paradigm for real-time safety, accelerating the practical deployment of streaming safeguards.

</details>

### 11. Kelp: A Streaming Safeguard for Large Models via Latent Dynamics-Guided Risk Detection

📄 [arXiv](https://arxiv.org/abs/2510.09694) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64082)　📅 2025-10　🏷 ICML 2026

**关键词**：`defense`、`latent dynamics`、`temporal consistency`、`plug-in monitor`

👤 **作者**：Xiaodan Li、…、Hui Xue

- 🎯 **研究动机**：现有 guardrail 多为事后检测，不安全内容可能先暴露给用户，轻量检测器精度又受限
- 🔬 **研究方法**：Kelp 以 Streaming Latent Dynamics Head 建模生成序列中风险的时序演化实现流式检测，并用 Anchored Temporal Consistency loss 约束危害预测单调性
- 📌 **结论**：较 SOTA 事后 guardrail 与插件探针平均 F1 提高 15.61%，模型仅 20M 参数、每 token 延迟低于 0.5 ms

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large models (LMs) are powerful content generators, yet their open-ended nature can also introduce potential risks, such as generating harmful or biased content. Existing guardrails mostly perform post-hoc detection that may expose unsafe content before it is caught, and the latency constraints further push them toward lightweight models, limiting detection accuracy. In this work, we propose Kelp, a novel plug-in framework that enables streaming risk detection within the LM generation pipeline. Kelp leverages intermediate LM hidden states through a Streaming Latent Dynamics Head (SLD), which models the temporal evolution of risk across the generated sequence for more accurate real-time risk detection. To ensure reliable streaming moderation in real applications, we introduce an Anchored Temporal Consistency (ATC) loss to enforce monotonic harm predictions by embedding a benign-then-harmful temporal prior. Besides, for a rigorous evaluation of streaming guardrails, we also present StreamGuardBench-a model-grounded benchmark featuring on-the-fly responses from each protected model, reflecting real-world streaming scenarios in both text and vision-language tasks. Across diverse models and datasets, Kelp consistently outperforms state-of-the-art post-hoc guardrails and prior plug-in probes (15.61% higher average F1), while using only 20M parameters and adding less than 0.5 ms of per-token latency.

</details>

### 12. Withholding the Completing Chunk: Exact Release-Boundary Equivalence for Production Streaming Guardrails

📄 [arXiv](https://arxiv.org/abs/2608.10279)　📅 2026-08

**关键词**：`defense`、`streaming guardrail`、`prefix detection`、`generation latency`

👤 **作者**：Christopher M. Frost

- 🎯 **研究动机**：流式输出下检测到违规时完成块已释放不可撤回，需要与事后累积预言机完全等价的发布边界匹配
- 🔬 **研究方法**：把每谓词编译为持久 NFA，区分稳定与临时断言态、按文档序族优先级在每块释放前检查，并给出 ASCII 显式策略语法与生产级实现
- 📌 **结论**：101,653+100,345 个分块用例零预言机/跨运行时不匹配；16384 字符时增量中位 30.2ms 对比累积扫描 96.6ms，证明发布边界等价

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Streaming language-model output creates an enforcement boundary: a control that detects a prohibited pattern after releasing its completing chunk cannot recall it. We study a production policy in which each ordered family is the conjunction of two regular-language predicates. Incremental matching is classical. The problem is exact composition at release time across arbitrary chunk partitions, including end-of-prefix word boundaries that can change on extension. We define an ASCII-explicit policy grammar, compile each predicate to a persistent nondeterministic finite automaton (NFA), distinguish stable from provisional assertion state, apply document-order family priority, and check the decision before releasing each chunk. We show that the resulting monitor is release-boundary equivalent to an absorbing cumulative oracle for every policy in the declared grammar. Production Python and TypeScript implementations were evaluated on 101,653 partitioned cases; a public surrogate added 100,345 cases. Both campaigns produced zero oracle, cross-runtime, or intended-family mismatches. In a frozen neutral-output profile, the memoized incremental and native-regex cumulative slopes at 64-character chunks were 0.973 and 1.976. At 16,384 characters the incremental median was 30.2 ms versus 96.6 ms for native cumulative scanning at that chunk size. Native regex remained faster at 512-character chunks (12.4 versus 29.4 ms), exposing the constant-factor crossover rather than hiding it. A shared per-stream cache cap and 129-symbol alphabet bound optimization state; the campaign peaked at 364 of 4,096 without bypass. The result is policy conformance for a deterministic backstop, not evidence of semantic safety or policy completeness.

</details>

### 13. Guard Vector: Beyond English LLM Guardrails with Task-Vector Composition and Streaming-Aware Prefix SFT

📄 [arXiv](https://arxiv.org/abs/2509.23381) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2025-09

**关键词**：`defense`、`task-vector composition`、`streaming guardrail`、`prefix detection`、`multilingual guardrail`、`streaming moderation`

👤 **作者**：Wonhyuk Lee、Youngchol Kim、Yunjin Park、Junhyung Moon、Dongyoung Jeong、Wanjin Park

- 🎯 **研究动机**：护栏模型的跨语言扩展与流式检测需求此前未同时满足
- 🔬 **研究方法**：提出 Guard Vector（护栏模型与同构预训练模型的参数差），与目标语言模型组合即得目标护栏，再加流式感知的 prefix SFT 与单 token 输出分类头
- 📌 **结论**：组合即可扩展到中日韩语且无需额外训练或目标语标签，可移植到 Llama 与 Gemma 骨干，prefix SFT 保持流式质量并降低延迟

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce Guard Vector, a safety task vector computed as the parameter difference between a guardrail model (Guard Model) and a same-architecture pretrained language model. Composing this vector with a target language model yields a Target Guard Model (TGM). We then adapt TGM with a streaming-aware approach that combines prefix-based training and evaluation with a classifier that produces a single-token output. With this composition alone, TGM improves classification quality over established Guard Models across standard safety suites and enables language extensibility to Chinese, Japanese, and Korean, requiring neither additional training nor target language labels for this composition step. It also demonstrates model portability across two widely used public guardrail backbones, Llama and Gemma. With prefix SFT (supervised fine-tuning), TGM preserves classification quality under streaming by aligning the behavior between prefix inputs and full-text inputs. The single-token output design increases throughput and reduces latency. Together, these components reduce data and compute requirements while promoting streaming-aware evaluation practices, thereby contributing to a more responsible AI ecosystem.

</details>
