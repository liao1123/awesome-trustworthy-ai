# Diffusion Language Model Security

[返回 Language Model Security 目录](README.md)

## 研究方向

本页研究 masked/diffusion language model 通过并行、双向、迭代 denoising 生成文本时出现的专属安全机制与攻击面。与 autoregressive model 不同，攻击可直接利用 `[MASK]`、in-place infilling、token commitment 和 denoising-path dependence；防御也可观察完整中间轨迹、remask 可疑 token 或动态分配监测计算。训练时后门由 [扩散模型后门](../../poison-and-backdoor/diffusion-backdoor.md) 维护，本页只记录 inference-time safety 与机制交叉。

## 研究脉络

- **Architecture gap：** 基础分析比较 AR 与 masked diffusion 的 circuit、拒答轨迹和生成文本，确认安全差异不仅来自训练数据，也来自 sampling mechanism。
- **Diffusion-native attack：** PAD、DIJA 和 MaskForge 从 parallel decoding、interleaved mask-text 与可复用结构 pattern 出发，取代直接迁移 AR jailbreak template。
- **Trajectory monitoring：** SRI、hesitation-aware routing 与 pre-decoding state fusion 利用多步 hidden state 在最终有害文本出现前识别风险。
- **Denoising defense：** Safety-Aware Denoiser、adaptive remasking 和 DiffuGuard 在迭代过程中纠正 token，而不是只过滤完成后的输出。
- **当前边界：** 不同 dLLM 的初始化、remasking schedule 与 post-training 方式会产生截然不同的 intrinsic safety，结论不能从单一模型或固定 mask pattern 外推。

## 机制与安全边界

### 1. Step-Wise Refusal Dynamics in Autoregressive and Diffusion Language Models

📄 [arXiv](https://arxiv.org/abs/2602.02600) · 🌐 [Project](https://elironrahimi.github.io/sri-signal/)　📅 2026-02

**关键词**：`analysis`、`refusal dynamics`、`sampling mechanism`、`internal recovery`

👤 **作者**：Eliron Rahimi、Elad Hirshel、Rom Himelstein、Amit LeVi、Avi Mendelson、Chaim Baskin

- 🎯 **研究动机**：采样机制如何塑造 AR 与扩散语言模型的拒答行为知之甚少
- 🔬 **研究方法**：提出逐步拒答内部动态（SRI）信号刻画文本层不可见的生成动态，并仅用良性 SRI 信号训练不改推理的越狱检测器
- 📌 **结论**：扩散重掩码可促进有害中间生成的恢复，固定权重下换用扩散采样即提升越狱鲁棒性；恢复失败主要发生在 AR 采样下，SRI 检测器媲美或超越既有基线且开销可忽略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion language models (DLMs) have recently emerged as a competitive alternative to autoregressive (AR) models, offering parallel decoding, competitive generation quality, and initial evidence of improved jailbreak robustness. Despite this progress, the role of sampling mechanisms in shaping refusal behavior remains poorly understood. To address this gap, we present a comprehensive study of step-wise refusal dynamics. We show that diffusion remasking can promote recovery from harmful intermediate generations, provide evidence that this behavior is tied to the sampling mechanism, and demonstrate that switching from AR to diffusion sampling improves jailbreak robustness, including under fixed model weights. To capture generation dynamics not observable at the text level, we propose the Step-Wise Refusal Internal Dynamics (SRI) signal. Consistent with our text-level findings, SRI shows that recovery fails primarily under AR sampling, with these failures often appearing anomalous relative to harmless generations in the SRI space. Based on this observation, we show that SRI enables a simple jailbreak detector that does not modify inference and generalizes to unseen attacks by training only on benign SRI signals. Our evaluation shows that this detector matches or outperforms existing jailbreak detection baselines while adding negligible overhead.

</details>

### 2. Safer by Diffusion, Broken by Context: Diffusion LLM's Safety Blessing and Its Failure Mode

📄 [arXiv](https://arxiv.org/abs/2602.00388)　📅 2026-02

**关键词**：`analysis`、`safety blessing`、`context nesting`、`denoising trajectory`

👤 **作者**：Zeyuan He、…、Jialin Yu

- 🎯 **研究动机**：扩散 LLM 相对自回归 LLM 的越狱鲁棒性来源与边界不明
- 🔬 **研究方法**：分析扩散轨迹的逐步抑制效应如何递进压制不安全生成，并提出把有害请求嵌入结构化良性上下文的 context nesting 黑盒策略
- 📌 **结论**：扩散式生成带来内在安全红利，但 context nesting 可绕过并取得 SOTA ASR，首次成功越狱 Gemini Diffusion

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion large language models (D-LLMs) offer an alternative to autoregressive LLMs (AR-LLMs) and have demonstrated advantages in generation efficiency. Beyond the utility benefits, we argue that D-LLMs exhibit a previously underexplored safety blessing: their diffusion-style generation confers intrinsic robustness against jailbreak attacks originally designed for AR-LLMs. In this work, we provide an initial analysis of the underlying mechanism, showing that the diffusion trajectory induces a stepwise reduction effect that progressively suppresses unsafe generations. This robustness, however, is not absolute. Following this analysis, we highlight a simple yet effective failure mode, context nesting, in which harmful requests are embedded within structured benign contexts. Empirically, we show that this simple black-box strategy bypasses D-LLMs' safety blessing, achieving state-of-the-art attack success rates across models and benchmarks. Notably, it enables the first successful jailbreak of Gemini Diffusion to our knowledge, exposing a critical vulnerability in proprietary D-LLMs. Together, our results characterize both the origins and the limits of D-LLMs' safety blessing, constituting an early-stage red-teaming of D-LLMs.

</details>

### 3. Diffusion LLMs as Targets and Adversaries: Mechanistic Safety Exploits

📄 [arXiv](https://arxiv.org/abs/2608.07430)　📅 2026-08

**关键词**：`attack`、`safety neuron`、`SN-guided diffusion`、`cross-architecture transfer`

👤 **作者**：Elena Dumitrescu、Gert Lek、Lydia Y. Chen、Jérémie Decouchant

- 🎯 **研究动机**：扩散 LLM 以迭代并行去噪取代自回归预测，其内部安全机制几乎未被理解
- 🔬 **研究方法**：证明 DLLM 安全对齐稀疏且跨架构可迁移：自剪枝与从自回归源模型映射剪枝安全神经元；并提出 SN-Guided Diffusion 离线黑盒越狱框架用加权安全神经元损失引导扩散
- 📌 **结论**：自剪枝使 LLaDA ASR 从 2.6% 升至 73.8%、Dream 从 1.9% 升至 86.6%；SN-Guided 迁移 ASR 至 86.9%（Qwen2.5-7B）且每提示仅需 20 次生成

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion Large Language Models (DLLMs) replace autoregressive next-token prediction with iterative parallel denoising, yet their internal safety mechanisms remain poorly understood. In this work, we investigate DLLMs both as targets and as adversaries, exposing mechanistic vulnerabilities in diffusion-based alignment. We first show that safety alignment in DLLMs remains sparse and transferable across architectures. DLLMs initialized from autoregressive predecessors inherit the same mechanistic safety footprint as their source models, enabling transfer attacks via direct safety neuron mapping and pruning. Self-pruning increases attack success rates (ASR) from 2.6% to 73.8% on LLaDA and from 1.9% to 86.6% on Dream, while transfer pruning from Qwen2.5 increases ASR from 1.9% to 73.2% on Dream and from 7.0% to 86.3% on Fast-dLLM. Building on these findings, we introduce SN-Guided Diffusion, a fully offline black-box jailbreak framework that steers the diffusion process away from safety-triggering regions using a weighted safety neuron loss, which achieves near-perfect prompt separability (AUROC = 1.0 for benign-vs-jailbreak discrimination). Across multiple open and proprietary targets, our method achieves a transfer ASR of up to 77.1% on Llama-3-8B-Instruct, 86.9% on Qwen2.5-7B-Instruct, and 74.3% against Gemini-2.5-Flash-Lite, while requiring only 20 generation episodes per prompt. Compared to prior jailbreaking frameworks, our method achieves competitive transferability with orders-of-magnitude lower generation cost. Our codebase is available at https://github.com/ellyoana/sn-guided-diffusion.

</details>

### 4. MaskForge: Structure-Aware Adaptive Attacks for Jailbreaking Diffusion Large Language Models

📄 [arXiv](https://arxiv.org/abs/2606.04027)　📅 2026-06

**关键词**：`attack`、`mask structure`、`pattern library`、`adaptive bandit`

👤 **作者**：Yingzi Ma、Zhengyue Zhao、Xiaogeng Liu、Minhui Xue、Yue Zhao、Chaowei Xiao

- 🎯 **研究动机**：dLLM 双向上下文与置信度提交机制带来独特的填充式安全面，已有越狱未利用原生 mask 填充且模板缺乏结构自适应
- 🔬 **研究方法**：提出 MaskForge 黑盒自适应攻击，将 dLLM 红队化为对不断增长的结构模式库的搜索：UCB bandit 选择模式、评分器引导回退、成功尝试蒸馏回模式库
- 📌 **结论**：五个公开 dLLM、三个基准上平均 ASR 79.3%（较最强基线 +17.6%）；成熟模式库零更新迁移到 AdvBench 达 88.2%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion large language models (dLLMs) generate text by iteratively denoising partially masked sequences under bidirectional context, exposing a safety surface distinct from autoregressive LLMs. Because mask tokens are native inputs and tokens are committed by confidence rather than position, harmful content can be induced through infilling and outside the monitored prefix. Existing jailbreaks either miss this native infill capability or rely on low-diversity mask-bearing templates applied uniformly across goals, with little structural adaptation or accumulated attack experience. We propose MaskForge, a fully black-box adaptive attack that casts dLLM red-teaming as optimized search over a growing library of structural patterns. MaskForge abstracts successful attempts into reusable schemas, selects goal-compatible patterns with a UCB bandit, and invokes a scorer-guided fallback when the current library fails. Successful attempts are distilled back into the pattern library, enabling experience to accumulate across goals. Across five public dLLMs and three benchmarks, MaskForge achieves an average attack success rate of 79.3%, a 17.6% relative improvement over the strongest competing dLLM baseline. The matured pattern library further transfers to AdvBench without any updates, achieving a 88.2% attack success rate and a 67% relative improvement over the strongest competing baseline.

</details>

### 5. The Devil Behind the Mask: An Emergent Safety Vulnerability of Diffusion LLMs

📄 [arXiv](https://arxiv.org/abs/2507.11097) · 📝 [OpenReview](https://openreview.net/forum?id=rIPeatvPy3)　📅 2026　🏷 ICLR 2026

**关键词**：`attack`、`interleaved mask-text`、`bidirectional infilling`、`parallel decoding`

👤 **作者**：Zichen Wen、…、Linfeng Zhang

- 🎯 **研究动机**：dLLM对齐未覆盖用户直接控制masked span的场景
- 🔬 **研究方法**：DIJA将harmful text与mask交错，借双向一致性与并行解码补全缺失内容
- 📌 **结论**：无需隐藏恶意语义即显著绕过多种aligned dLLM

### 6. Jailbreaking Large Language Diffusion Models: Revealing Hidden Safety Flaws in Diffusion-Based Text Generation

📄 [arXiv](https://arxiv.org/abs/2507.19227)　📅 2025-07

**关键词**：`attack`、`parallel decoding`、`multi-point attention`、`PAD`

👤 **作者**：Yuanhe Zhang、…、Yufei Guo

- 🎯 **研究动机**：面向 LLM 的越狱方法对扩散式语言模型效果有限，其安全鲁棒性存疑
- 🔬 **研究方法**：提出 PAD 并行解码越狱：Multi-Point Attention Attack 借鉴肯定回复模式，引导并行生成过程走向有害输出
- 📌 **结论**：四个 LLDM 上 ASR 达 97%；同规模下有害生成速度比自回归快 2 倍，凸显失控风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Diffusion Models (LLDMs) exhibit comparable performance to LLMs while offering distinct advantages in inference speed and mathematical reasoning tasks.The precise and rapid generation capabilities of LLDMs amplify concerns of harmful generations, while existing jailbreak methodologies designed for Large Language Models (LLMs) prove limited effectiveness against LLDMs and fail to expose safety vulnerabilities.Successful defense cannot definitively resolve harmful generation concerns, as it remains unclear whether LLDMs possess safety robustness or existing attacks are incompatible with diffusion-based architectures.To address this, we first reveal the vulnerability of LLDMs to jailbreak and demonstrate that attack failure in LLDMs stems from fundamental architectural differences.We present a PArallel Decoding jailbreak (PAD) for diffusion-based language models. PAD introduces Multi-Point Attention Attack, which guides parallel generative processes toward harmful outputs that inspired by affirmative response patterns in LLMs. Experimental evaluations across four LLDMs demonstrate that PAD achieves jailbreak attack success rates by 97%, revealing significant safety vulnerabilities. Furthermore, compared to autoregressive LLMs of the same size, LLDMs increase the harmful generation speed by 2x, significantly highlighting risks of uncontrolled misuse.Through comprehensive analysis, we provide an investigation into LLDM architecture, offering critical insights for the secure deployment of diffusion-based language models.

</details>

### 7. $D^2$-Monitor: Dynamic Safety Monitoring for Diffusion LLMs via Hesitation-Aware Routing

📄 [arXiv](https://arxiv.org/abs/2605.25893)　📅 2026-05

**关键词**：`detection`、`safety hesitation`、`dynamic routing`、`trajectory probe`

👤 **作者**：Aoxi Liu、…、Adel Bibi

- 🎯 **研究动机**：扩散 LLM 多步去噪暴露中间隐表征，安全监控未被探索；轻量 probe 适合常开但在难样本上失效
- 🔬 **研究方法**：发现 safety hesitation（中间隐状态反复落入 probe 决策边界小边距内）的步数可有效预测 probe 失败；D2-Monitor 双层监控：轻量 probe 常开估计犹豫并分类，超阈值才激活更重的 probe
- 📌 **结论**：3 个数据集、4 个 D-LLM 上达 SOTA，参数不超过 0.85M，效果-效率权衡优于 8 个基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite the emergence of diffusion large language models (D-LLMs) as an alternative to autoregressive large language models (AR-LLMs), safety monitoring for D-LLMs remains largely unexplored. Unlike AR-LLMs, D-LLMs generate text through a multi-step denoising process, exposing intermediate hidden representations that may contain safety-relevant information unavailable in standard single-step monitoring setups. Motivated by the suitability of lightweight probes for always-on monitoring, we analyze which trajectory-level signals best indicate when such probes are likely to struggle. We find that the most informative signal is safety hesitation: intermediate hidden states repeatedly falling within a small margin of the probe's decision boundary. The number of such hesitation steps in D-LLM's trajectory predicts probe failure effectively, providing a proxy of sample difficulty. Building on this analysis, we propose $D^2$-Monitor, a bi-level safety monitor for D-LLMs. $D^2$-Monitor adopts a lightweight probe as an always-on monitor to jointly estimate hesitation and perform base classification. When the hesitation level exceeds a threshold, a more expressive but computationally heavier probe is activated. This dynamic routing mechanism allocates monitoring resources efficiently at test time. Evaluated on 3 datasets (WildguardMix, ToxicChat, OpenAI-Moderation) across 4 D-LLMs, $D^2$-Monitor achieves state-of-the-art performance with a compact parameter footprint ($\leq$ 0.85M parameters), and exhibits the best trade-off between effectiveness and efficiency relative to 8 baselines.

</details>

### 8. Beyond the Prompt: Leveraging Pre-Decoding States for Jailbreak Detection in dLLMs

📝 [OpenReview](https://openreview.net/forum?id=QVRvaVBwRh)　📅 2026

**关键词**：`detection`、`pre-decoding state`、`state fusion`、`jailbreak detection`

- 🎯 **研究动机**：prompt-only检测器看不到dLLM在masked response中已形成的风险信号
- 🔬 **研究方法**：融合prompt表示与首轮pre-decoding response state做状态融合检测
- 📌 **结论**：diffusion-native jailbreak漏检显著降低且良性误拒低

### 9. Beyond Token Positions: Safety Alignment Across Denoising Steps in Diffusion Language Models

📄 [arXiv](https://arxiv.org/abs/2609.00495)　📅 2026-09

**关键词**：`analysis`、`diffusion LM safety`、`denoising trajectory`、`early refusal commitment`

👤 **作者**：Guoli Wang、Haonan Shi、Tu Ouyang、An Wang

- 🎯 **研究动机**：diffusion LM 经迭代去噪生成文本，去噪步与 token 位置两轴如何影响安全对齐缺少中间过程分析
- 🔬 **研究方法**：追踪去噪全程的 token 分布与 commitment 决策，发现 refusal 信号集中于早期去噪步与前导位置，提出 training-free 的 RAEC 在早期固化持续 refusal 信号
- 📌 **结论**：在 LLaDA 与 Dream 上降低 ASR 并大体保持 utility

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion large language models (dLLMs) generate text through iterative denoising rather than left-to-right decoding. This generation paradigm introduces two axes that can influence safety alignment: when tokens are generated during denoising and where they appear in the response. In this paper, we measure dLLM safety behavior under harmful prompts by tracing intermediate token distributions and commitment decisions throughout denoising. Our analysis shows that refusal signals are concentrated in early denoising steps and leading response positions, and the tokens committed early can strongly shape the final safety outcome. Our measurements further show that the denoising step and persistence of refusal-token commitment are important for understanding dLLM safety. Based on these findings, we propose Refusal-Aware Early Commitment (RAEC), a simple training-free decoding method that commits persistent refusal signals from early steps. Experiments on LLaDA and Dream show that RAEC reduces attack success rates while largely preserving utility. The code is available at https://github.com/Glresearch1/RAEC.

</details>

### 10. Adaptive Steering and Remasking for Safe Generation in Diffusion Language Models

📄 [arXiv](https://arxiv.org/abs/2605.13043)　📅 2026-05

**关键词**：`defense`、`adaptive remasking`、`contrastive safety direction`、`step-wise intervention`

👤 **作者**：Yejin Lee、Yo-Sub Han

- 🎯 **研究动机**：DLM 中间去噪步生成的有害 token 会沿后续精炼传播导致不安全输出，已有方法要么不安全要么质量低
- 🔬 **研究方法**：推理时步级干预：以 contrastive safety direction（SGD）评估每步 token 的有害对齐，检测到即 remask 并按危害度自适应 steering 恢复去噪，即插即用免微调
- 📌 **结论**：越狱成功率降到 0.64%，生成质量接近原始模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion Language Models (DLMs) provide a promising alternative to autoregressive language models by generating text through iterative denoising and bidirectional refinement. However, this iterative generation paradigm also introduces unique safety vulnerabilities when harmful tokens generated at intermediate denoising steps propagate through subsequent refinement processes and eventually induce unsafe outputs. While there are a few attempts to remedy this issue, they either fail to generate safe outputs or generate safe yet low-quality outputs. This motivates us to propose an inference-time defense framework based on the step-wise intervention during the denoising process, which then improves the safety without compromising the output quality. The key component of our framework is a contrastive safety direction (SGD), a latent direction that captures the semantic boundary between harmful and safe generations. We leverage SGD to assess the alignment of generated tokens with harmful semantics at each denoising step. When harmful alignment is detected, our method remasks the corresponding tokens and resumes the denoising process with adaptive steering, where the steering strength is modulated according to the estimated degree of harmfulness. As a plug-and-play module, our method circumvents the need for additional fine-tuning and can be directly incorporated into off-the-shelf diffusion models. The experimental results show that our approaches reduce jailbreak success rates to 0.64% while preserving generation quality close to the original model performance. This confirms the effectiveness of step-wise intervention for safe diffusion language model generation. Our code is available at https://github.com/leeyejin1231/DLM_Steering_Remasking.

</details>

### 11. The Safety-Aware Denoiser for Text Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2605.08116) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62720)　📅 2026-05　🏷 ICML 2026

**关键词**：`defense`、`safety-aware denoiser`、`safe-region guidance`、`inference-time control`、`safety alignment`、`diffusion model`

👤 **作者**：Amman Yusuf、Zhejun Jiang、Mijung Park

- 🎯 **研究动机**：面向自回归模型的事后过滤或推理时干预不足以应对文本扩散模型的安全风险
- 🔬 **研究方法**：Safety-Aware Denoiser（SAD）修改迭代去噪过程，把最终去噪步的文本样本引导到可证明安全的文本区域，无需重训练
- 📌 **结论**：在危害 taxonomy、记忆与越狱维度大幅减少不安全生成，同时保持质量与流畅度，优于现有方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent work on text diffusion models offers a promising alternative to autoregressive generation, but controlling their safety remains underexplored. Existing safety approaches are geared toward autoregressive models and typically rely on post-hoc filtering or inference-time interventions. These are inadequate for effectively addressing safety risks in text diffusion models. We propose the Safety-Aware Denoiser (SAD), a safety-guidance framework in text diffusion models. The SAD modifies the iterative denoising process such that the text sample at the final denoising step is steered toward provably safe regions of the text space. This inference-time method can integrate safety constraints into the denoiser, avoiding computationally expensive retraining of the underlying diffusion model and enabling flexible, lightweight safety guidance. We evaluate the safety of the generated text using the SAD, with respect to hazard taxonomy, memorization, and jailbreak. Experimental results show that SAD substantially reduces unsafe generations while preserving generation quality and fluency, outperforming existing methods. These results demonstrate that our safety guidance during denoising provides an effective and scalable mechanism for enforcing safety in text diffusion models.

</details>

### 12. Toward Safer Diffusion Language Models: Discovery and Mitigation of Priming Vulnerability

📄 [arXiv](https://arxiv.org/abs/2510.00565) · 📝 [OpenReview](https://openreview.net/forum?id=ZMzha5gbnF) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10008814)　📅 2025-10　🏷 ICLR 2026

**关键词**：`defense`、`priming vulnerability`、`contaminated state`、`diffusion alignment`

👤 **作者**：Shojiro Yamabe、Jun Sakuma

- 🎯 **研究动机**：扩散语言模型迭代去噪机制下的越狱安全风险未被理解
- 🔬 **研究方法**：发现中间步出现有害查询的肯定 token 即可引导后续去噪走向有害响应，据此提出从含肯定 token 的污染中间状态训练安全响应的对齐方法
- 📌 **结论**：显著缓解该漏洞且任务性能影响极小，同时提升对常规越狱攻击的鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion language models (DLMs) generate tokens in parallel through iterative denoising, which can reduce latency and enable bidirectional conditioning. However, the safety risks posed by jailbreak attacks that exploit this inference mechanism are not well understood. In this paper, we reveal that DLMs have a critical vulnerability stemming from their iterative denoising process and propose a countermeasure. Specifically, our investigation shows that if an affirmative token for a harmful query appears at an intermediate step, subsequent denoising can be steered toward a harmful response even in aligned models. As a result, simply injecting such affirmative tokens can readily bypass the safety guardrails. Furthermore, we demonstrate that the vulnerability allows existing optimization-based jailbreak attacks to succeed on DLMs. Building on this analysis, we propose a novel safety alignment method tailored to DLMs that trains models to generate safe responses from contaminated intermediate states that contain affirmative tokens. Our experiments indicate that the proposed method significantly mitigates the vulnerability with minimal impact on task performance. Furthermore, our method improves robustness against conventional jailbreak attacks. Our work underscores the need for DLM-specific safety research. Our code is available at https://github.com/mdl-lab/dlm-priming-vulnerability.

</details>

### 13. DiffuGuard: How Intrinsic Safety is Lost and Found in Diffusion Large Language Models

📄 [arXiv](https://arxiv.org/abs/2509.24296) · 📝 [OpenReview](https://openreview.net/forum?id=zBPzxhso8M) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10006479)　📅 2025-09　🏷 ICLR 2026

**关键词**：`defense`、`denoising-path dependence`、`stochastic remasking`、`block-level repair`

👤 **作者**：Zherui Li、…、Jiaheng Zhang

- 🎯 **研究动机**：dLLM 迭代并行生成机制带来与自回归不同的越狱脆弱性，未被系统分析
- 🔬 **研究方法**：发现标准贪心 remasking 的有害偏差与去噪路径依赖（早期 token 安全性决定最终输出），提出免训练的 DiffuGuard：随机退火 remasking 加块级审计修复
- 📌 **结论**：四个 dLLM 上把六种越狱攻击的 ASR 从 47.9% 降至 14.7%，效用与效率保持

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of Diffusion Large Language Models (dLLMs) introduces unprecedented vulnerabilities that are fundamentally distinct from Autoregressive LLMs, stemming from their iterative and parallel generation mechanisms. In this paper, we conduct an in-depth analysis of dLLM vulnerabilities to jailbreak attacks across two distinct dimensions: intra-step and inter-step dynamics. Experimental results reveal a harmful bias inherent in the standard greedy remasking strategy and identify a critical phenomenon we term Denoising-path Dependence, where the safety of early-stage tokens decisively influences the final output. These findings also indicate that while current decoding strategies constitute a significant vulnerability, dLLMs possess a substantial intrinsic safety potential. To unlock this potential, we propose DiffuGuard, a training-free defense framework that addresses vulnerabilities through a dual-stage approach: Stochastic Annealing Remasking dynamically introduces controlled randomness to mitigate greedy selection bias, while Block-level Audit and Repair exploits internal model representations for autonomous risk detection and guided correction. Comprehensive experiments on four dLLMs demonstrate DiffuGuard's exceptional effectiveness, reducing Attack Success Rate against six diverse jailbreak methods from 47.9% to 14.7% while preserving model utility and efficiency. Our code is available at: https://github.com/niez233/DiffuGuard.

</details>

### 14. A2D: Any-Order, Any-Step Safety Alignment for Diffusion Language Models

📄 [arXiv](https://arxiv.org/abs/2509.23286) · 📝 [OpenReview](https://openreview.net/forum?id=URTnuyQJI1) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10009223)　📅 2025-09　🏷 ICLR 2026

**关键词**：`defense`、`any-order alignment`、`randomized masking`、`early safe termination`

👤 **作者**：Wonje Jeung、…、Albert No

- 🎯 **研究动机**：dLLM 任意顺序生成扩大攻击面，DIJA 等模板预填充攻击可绕过响应级拒绝
- 🔬 **研究方法**：提出 A2D：在随机掩码下做 token 级对齐，训练 dLLM 一旦出现有害内容即发出 [EOS] 拒绝信号，实现任意顺序任意步防御与实时监控
- 📌 **结论**：DIJA 成功率从超 80% 降至近零（LLaDA-8B 1.3%、Dream-v0 0.0%），阈值化 [EOS] 概率使安全终止最快提速 19.3 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion large language models (dLLMs) enable any-order generation, but this flexibility enlarges the attack surface: harmful spans may appear at arbitrary positions, and template-based prefilling attacks such as DIJA bypass response-level refusals. We introduce A2D (Any-Order, Any-Step Defense), a token-level alignment method that aligns dLLMs to emit an [EOS] refusal signal whenever harmful content arises. By aligning safety directly at the token-level under randomized masking, A2D achieves robustness to both any-decoding-order and any-step prefilling attacks under various conditions. It also enables real-time monitoring: dLLMs may begin a response but automatically terminate if unsafe continuation emerges. On safety benchmarks, A2D consistently prevents the generation of harmful outputs, slashing DIJA success rates from over 80% to near-zero (1.3% on LLaDA-8B-Instruct, 0.0% on Dream-v0-Instruct-7B), and thresholded [EOS] probabilities allow early rejection, yielding up to 19.3x faster safe termination.

</details>

### 15. From Vulnerability to Defense: Understanding and Mitigating MASK-Based Attacks in dLLMs

📝 [OpenReview](https://openreview.net/forum?id=jKQQb8uClw)　📅 2025-09　🏷 ICLR 2026

**关键词**：`defense`、`MASK-based jailbreak`、`margin accumulation`、`Reject-MASK`

- 🎯 **研究动机**：MASK-based prompt借margin累积与并行解码绕过dLLM安全对齐，机制不明
- 🔬 **研究方法**：从margin accumulation与scheduling advantage解析机制，提出Reject-MASK两阶段训练
- 📌 **结论**：把超过90%的ASR降至接近个位数

### 16. Where to Start Alignment? Diffusion Large Language Model May Demand a Distinct Position

📄 [arXiv](https://arxiv.org/abs/2508.12398) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/37106)　📅 2025-08　🏷 AAAI 2026

**关键词**：`defense`、`position-aware alignment`、`middle-token supervision`、`MOSA`

👤 **作者**：Zhixin Xie、Xurui Song、Jun Luo

- 🎯 **研究动机**：扩散语言模型 dLLM 作为新架构缺乏安全研究，其顺序生成特性造成攻防双方不对称
- 🔬 **研究方法**：发现响应中段 token 而非开头更决定 dLLM 输出安全，而攻击者受顺序生成倾向限制难以操纵中段；提出 MOSA 用 RL 直接对齐中段生成安全拒绝
- 📌 **结论**：对八种攻击与两个基准验证安全优越性，编码、数学与通用推理效用保持

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion Large Language Models (dLLMs) have recently emerged as a competitive non-autoregressive paradigm due to their unique training and inference approach. However, there is currently a lack of safety study on this novel architecture. In this paper, we present the first analysis of dLLMs' safety performance and propose a novel safety alignment method tailored to their unique generation characteristics. Specifically, we identify a critical asymmetry between the defender and attacker in terms of security. For the defender, we reveal that the middle tokens of the response, rather than the initial ones, are more critical to the overall safety of dLLM outputs; this seems to suggest that aligning middle tokens can be more beneficial to the defender. The attacker, on the contrary, may have limited power to manipulate middle tokens, as we find dLLMs have a strong tendency towards a sequential generation order in practice, forcing the attack to meet this distribution and diverting it from influencing the critical middle tokens. Building on this asymmetry, we introduce Middle-tOken Safety Alignment (MOSA), a novel method that directly aligns the model's middle generation with safe refusals exploiting reinforcement learning. We implement MOSA and compare its security performance against eight attack methods on two benchmarks. We also test the utility of MOSA-aligned dLLM on coding, math, and general reasoning. The results strongly prove the superiority of MOSA.

</details>

### 17. TrustLDM: Benchmarking Trustworthiness in Language Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2606.00023)　📅 2026-06　🏷 ICLR 2026

**关键词**：`benchmark`、`dLLM trustworthiness`、`risk taxonomy`、`AR comparison`

👤 **作者**：Yichuan Mo、…、Yisen Wang

- 🎯 **研究动机**：语言扩散模型任意顺序解码带来新可信性挑战，相关结论分散于单一攻击或模型
- 🔬 **研究方法**：TrustLDM 从安全、隐私、公平三维评多架构 LDM，配多类静态 post 上下文；TrustLDM-Auto 利用解码灵活性自动搜索脆弱配置
- 📌 **结论**：仅用户 prompt 时可信性强，附加恶意 post 上下文后对齐明显退化；更长上下文不一定更强，解码顺序与生成长度均影响结果；自动框架在所有模型各维揭示大量弱点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid development of Language Diffusion Models (LDMs) challenges the dominant position of auto-regressive competitors in language processing. However, their flexible, any-order decoding strategies not only enable fast decoding speed but also potentially bring new trustworthiness challenges. To better understand the risks behind their pipelines, we introduce a comprehensive trustworthiness benchmark tailored to LDMs (TrustLDM), evaluating safety, privacy, and fairness across different LDM architectures with multiple categories of static post contexts. Our empirical results show that although LDMs generally exhibit strong trustworthiness with only the user prompts, their alignment behavior degrades noticeably when the malicious post contexts are attached to the masked responses. We further observe that longer contexts do not necessarily induce stronger effects, and both decoding order and generation length affect the evaluation outcomes. Finally, we propose TrustLDM-Auto, an automatic evaluation framework that leverages LDM decoding flexibility to systematically identify vulnerable configurations, revealing substantial trustworthiness weaknesses across all evaluated models and dimensions. Our work may potentially help the community build more trustworthy LDMs. Our code is available at https://github.com/PKU-ML/TrustLDM.

</details>

### 18. Beyond the Bidirectional Promise: Re-evaluating the Robustness of Diffusion Language Models

📄 [arXiv](https://arxiv.org/abs/2607.27386)　📅 2026-07

**关键词**：`analysis`、`AR/DLM paired comparison`、`natural perturbation robustness`、`decoder routing failure`

👤 **作者**：Saurabh Yadav、Badri Narayana Patro、Vijay Srinivas Agneeswaran

- 🎯 **研究动机**：DLM 双向上下文与迭代精炼常被默认带来鲁棒性，其自然噪声与对抗输入下的可靠性缺乏参数受控评估
- 🔬 **研究方法**：用两对参数匹配模型（LLaDA-8B vs LLaMA-3-8B、Dream-7B vs Qwen2.5-7B）在 32 种自然扰动、对抗梯度探针与机制分析下对比鲁棒性与校准
- 📌 **结论**：高随机性损失面使 DLM 天然抵抗梯度后缀，但对自然噪声无保证且系统性过度自信；机制探针显示模型完美编码输入损坏而脆弱性完全来自解码路由失败，表层 prompt 修补无效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion Language Models (DLMs) offer a compelling alternative to autoregressive (AR) generation by enabling bidirectional context and iterative refinement. However, their reliability under natural input noise and adversarial attacks remains under-explored. To address this, we systematically evaluate DLM robustness and calibration against AR baselines, using two parameter-matched pairs (LLaDA-8B vs. LLaMA-3-8B and Dream-7B vs. Qwen2.5-7B) across 32 natural perturbation conditions, adversarial gradient probes, and mechanistic hidden-state analyses. This paired design effectively isolates architecture-intrinsic properties from weight-dependent behaviors. We find a nuanced robustness profile: while highly stochastic DLM loss landscapes naturally resist gradient-based adversarial suffixes, they provide no guaranteed defense against natural noise, proving that everyday robustness is weight-dependent rather than inherently architectural. Furthermore, DLMs exhibit systematic overconfidence, presenting a practical deployment hazard. Most crucially, mechanistic probing reveals that all models perfectly encode input corruption, isolating behavioral fragility entirely to a decoder routing failure. Consistent with this diagnosis, we show that surface-level prompt patching fails to improve over noisy baselines. Ultimately, DLM robustness cannot be patched on; it must be fundamentally integrated into the iterative decoding loop.

</details>

### 19. Activation Steering for Masked Diffusion Language Models

📄 [arXiv](https://arxiv.org/abs/2512.24143)　📅 2025-12

**关键词**：`defense`、`activation steering`、`refusal direction`、`diffusion-specific accessibility`

👤 **作者**：Adi Shnaidman、…、Raz Lapid

- 🎯 **研究动机**：MDLM 缺乏表示层推理时控制机制，安全拒绝等行为能否被低维方向干预未知
- 🔬 **研究方法**：从对比 prompt 集用一次前向提取单一低维方向，在反向扩散全程对残差流做全局干预，不优化、不改动采样过程；以 safety refusal 为案例研究
- 📌 **结论**：多个 MDLM 的拒绝行为由近似一维激活子空间支配，干预效果显著优于 prompt 与优化基线；方向可从 AR 中无效的 pre-instruction token 提取（diffusion 特有可达性），杠杆集中于早期去噪步与中后层，且中英迁移强但不跨架构

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Masked diffusion language models (MDLMs) generate text via iterative masked-token denoising, enabling mask-parallel decoding and distinct controllability and efficiency tradeoffs from autoregressive LLMs. Yet, efficient representation-level mechanisms for inference-time control in MDLMs remain largely unexplored. To address this gap, we introduce an activation steering primitive for MDLMs: we extract a single low-dimensional direction from contrastive prompt sets using one prompt-only forward pass, and apply a global intervention on residual-stream activations throughout reverse diffusion, without performing optimization or altering the diffusion sampling procedure. Using safety refusal as a deployment-relevant case study, we find that refusal behavior in multiple MDLMs is governed by a consistent, approximately one-dimensional activation subspace. Applying the corresponding direction yields large and systematic behavioral shifts and is substantially more effective than prompt-based and optimization-based baselines. We further uncover diffusion-specific accessibility: effective directions can be extracted not only from post-instruction tokens, but also from pre-instruction tokens that are typically ineffective in autoregressive models due to causal attention. Ablations localize maximal leverage to early denoising steps and mid-to-late transformer layers, with early diffusion blocks contributing disproportionately. Finally, in an MDLM trained on English and Chinese, extracted directions transfer strongly between English and Chinese, but do not reliably generalize to an autoregressive architecture, highlighting architecture-dependent representations of safety constraints.

</details>

### 20. DLM-SWAI: Steering Diffusion Language Models Before They Unmask

📄 [arXiv](https://arxiv.org/abs/2605.29626)　📅 2026-05

**关键词**：`defense`、`token-distribution steering`、`training-free control`、`style and safety control`

👤 **作者**：Hyeseon An、Yo-Sub Han

- 🎯 **研究动机**：现有 steering 方法依赖辅助模型或面向 AR 逐 token 解码，难以直接用于迭代去噪的 DLM
- 🔬 **研究方法**：DLM-SWAI 免训练方法：用预计算的 token 级风格分数在每个去噪步偏置 token 分布，在风格与安全控制任务上评测
- 📌 **结论**：有效转向 DLM 同时保持生成质量、开销极小；消融揭示转向强度与流畅度的可控权衡，并按类别把可转向性关联到 token 级属性线索强度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Steering language model generation toward desired textual properties is essential for practical deployment, and inference-time methods are particularly appealing because they enable controllable generation without retraining. Recent work has also highlighted diffusion language models as an emerging generation paradigm with distinct decoding properties. However, most existing steering approaches either rely on auxiliary models or are designed for autoregressive next-token decoding, making them difficult to apply to diffusion language models DLMs, which generate text through iterative denoising of partially masked sequences. Therefore, we propose DLM-SWAI, a simple training-free steering method that biases the token distribution at each denoising step using pre-computed token-level style scores. Experiments on style and safety control tasks show that DLM-SWAI effectively steers diffusion language models while preserving generation quality and requiring minimal computational overhead. Ablations further reveal a controllable trade-off between steering strength and fluency, and our analysis links class-wise steerability to the strength of token-level attribute cues.

</details>

### 21. GCG Attack On A Diffusion LLM

📄 [arXiv](https://arxiv.org/abs/2601.14266)　📅 2025-12

**关键词**：`attack`、`GCG transfer`、`LLaDA`、`prefix/suffix perturbation`

👤 **作者**：Ruben Neyroud、Sam Corley

- 🎯 **研究动机**：GCG 对自回归模型有效，但对扩散 LLM 的适用性基本未被探索
- 🔬 **研究方法**：在 LLaDA 上对 AdvBench 有害提示系统评测多种 GCG 变体，包括前缀扰动与基于后缀的对抗生成
- 📌 **结论**：给出 dLLM 对抗 prompt 攻击面与鲁棒性的首批实证洞察，并指出需要为扩散设定开发替代优化与评测策略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While most LLMs are autoregressive, diffusion-based LLMs have recently emerged as an alternative method for generation. Greedy Coordinate Gradient (GCG) attacks have proven effective against autoregressive models, but their applicability to diffusion language models remains largely unexplored. In this work, we present an exploratory study of GCG-style adversarial prompt attacks on LLaDA (Large Language Diffusion with mAsking), an open-source diffusion LLM. We evaluate multiple attack variants, including prefix perturbations and suffix-based adversarial generation, on harmful prompts drawn from the AdvBench dataset. Our study provides initial insights into the robustness and attack surface of diffusion language models and motivates the development of alternative optimization and evaluation strategies for adversarial analysis in this setting.

</details>

### 22. Re-Mask and Redirect: Exploiting Denoising Irreversibility in Diffusion Language Models

📄 [arXiv](https://arxiv.org/abs/2604.08557)　📅 2026-03

**关键词**：`attack`、`trajectory-level attack`、`denoising irreversibility`、`defense inversion`

👤 **作者**：Arth Singh

- 🎯 **研究动机**：dLLM 安全对齐依赖"已提交 token 永久"这一承重假设，重新掩码已提交的拒绝 token 会发生什么未被检验
- 🔬 **研究方法**：提出 TrajHijack：重掩码已提交的拒绝 token 并注入短肯定前缀，无需梯度计算，在三个公开安全微调 dLLM 上验证并测试最强防御 A2D
- 📌 **结论**：HarmBench 上 ASR 达 74-82%（通用 8-token 前缀升至 92-98%）；漏洞不可约为单成分（重掩码或前缀单独仅 4.4%/5.7%）；A2D 反而更脆弱（89.9% vs 未防御 76.1%），即 Defense Inversion Effect

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment in diffusion language models (dLLMs) relies on a single load-bearing assumption: that committed tokens are permanent. We show that violating this assumption, by re-masking committed refusal tokens and injecting a short affirmative prefix, achieves 74-82% ASR on HarmBench across all three publicly available safety-tuned dLLMs, rising to 92-98% with a generic 8-token compliance prefix. We call this attack TrajHijack; it is the first trajectory-level attack on dLLMs, requires no gradient computation, and generalizes across SFT and preference-optimized (VRPO) models. Three findings emerge. First, the vulnerability is irreducibly two-component: re-masking alone (4.4%) and prefix alone (5.7%) both fail. Second, gradient optimization via a differentiable Gumbel-softmax chain consistently degrades ASR (41.5% vs. 76.1%), because continuous perturbations push token distributions off-manifold. Third, A2D (the strongest published dLLM defense) is more vulnerable to TrajHijack (89.9%) than the undefended model (76.1%): its silent-refusal training removes the contextual resistance that trajectory-level attacks must overcome, an effect we call the Defense Inversion Effect.

</details>

## 隐私与水印攻击

### 23. Membership Inference Attacks Against Fine-tuned Diffusion Language Models

📄 [arXiv](https://arxiv.org/abs/2601.20125)　📅 2026-01

**关键词**：`attack`、`membership inference`、`mask-subset aggregation`、`privacy leakage`

👤 **作者**：Yuetian Chen、…、Ninghui Li

- 🎯 **研究动机**：DLM 的 MIA 隐私泄露风险此前未被系统研究，其多掩码配置与 AR 单一预测模式的差异未被利用
- 🔬 **研究方法**：提出 SAMA：跨渐进密度采样掩码子集，用对重尾噪声稳健的符号统计与逆加权聚合把稀疏记忆检测转为投票机制
- 📌 **结论**：九个数据集上 SAMA 相对最佳基线 AUC 提升 30%，低假阳性率下最高提升 8 倍，揭示 DLM 此前未知的显著隐私漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion Language Models (DLMs) represent a promising alternative to autoregressive language models, using bidirectional masked token prediction. Yet their susceptibility to privacy leakage via Membership Inference Attacks (MIA) remains critically underexplored. This paper presents the first systematic investigation of MIA vulnerabilities in DLMs. Unlike the autoregressive models' single fixed prediction pattern, DLMs' multiple maskable configurations exponentially increase attack opportunities. This ability to probe many independent masks dramatically improves detection chances. To exploit this, we introduce SAMA (Subset-Aggregated Membership Attack), which addresses the sparse signal challenge through robust aggregation. SAMA samples masked subsets across progressive densities and applies sign-based statistics that remain effective despite heavy-tailed noise. Through inverse-weighted aggregation prioritizing sparse masks' cleaner signals, SAMA transforms sparse memorization detection into a robust voting mechanism. Experiments on nine datasets show SAMA achieves 30% relative AUC improvement over the best baseline, with up to 8 times improvement at low false positive rates. These findings reveal significant, previously unknown vulnerabilities in DLMs, necessitating the development of tailored privacy defenses.

</details>

### 24. Extracting Training Data from Diffusion Language Models via Infilling

📄 [arXiv](https://arxiv.org/abs/2605.24173)　📅 2026-05

**关键词**：`attack`、`training data extraction`、`infilling extraction`、`mask geometry`

👤 **作者**：Yihan Wang、N. Asokan

- 🎯 **研究动机**：记忆研究几乎只用前缀条件抽取，而 DLM 可在任意位置去噪，前缀探测严重低估其训练数据抽取风险
- 🔬 **研究方法**：提出由任意二值掩码参数化的 infilling extraction 协议，在 LLaDA-8B 与 Dream-7B 上覆盖五种抽取模式、三种训练管线与三种语料
- 📌 **结论**：掩码几何主导可抽取性——边缘条件掩码逐字抽取量最高达前缀条件的 3 倍；能接触到脱敏训练数据的攻击者从 DLM 抽取被删除邮箱的召回率甚至高于规模匹配的 AR 模型，SFT 无法消除先前记忆

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Memorization in large language models has been studied almost exclusively through prefix-conditioned extraction, a natural choice for autoregressive models. However, diffusion language models (DLMs) can denoise masked tokens at arbitrary positions. Thus, prefix-only probing reveals only one facet of memorization in DLMs and significantly underestimates the risk of training-data extraction. In order to realistically model extractability of training data in DLMs, we introduce \emph{infilling extraction}, a data-extraction protocol parameterized by an arbitrary binary mask that subsumes prefix-only probing and accounts for the bidirectional inductive bias of DLMs. Instantiating it on LLaDA-8B and Dream-7B across five extraction modes, three training pipelines, and three corpora covering verbatim and partial leakage, we find that mask geometry governs extractability: edge-conditioned masks \emph{extract up to three times more} verbatim sequences than prefix-conditioned ones, and bidirectional access opens channels inaccessible in autoregressive models. In particular, we show that a realistic adversary with access to training data where personally identifiable information has been redacted, can even achieve higher recall on extracting redacted email addresses from DLMs than from scale-matched autoregressive models. Tunable parameters for decoding measurably affect extraction performance, while a follow-up supervised finetuning stage does not eliminate the prior memorization.

</details>

### 25. Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks

📄 [arXiv](https://arxiv.org/abs/2605.05503)　📅 2026-05

**关键词**：`attack`、`watermark removal`、`chained rewriting`、`provenance robustness`

👤 **作者**：Mohd Ruhul Ameen、Akif Islam、Nadim Mahmud、Md. Ekramul Hamid

- 🎯 **研究动机**：面向 LLaDA 的 dLLM 水印报告 99% 以上真阳性检测，但其对多步改写的鲁棒性未被检验
- 🔬 **研究方法**：在五个 WaterBench 域生成 1,605 条带水印补全，用四个不知密钥的开源模型按五种风格链式改写至五跳，共得 160,500 条改写文本
- 📌 **结论**：原始输出检测率 87.9%，单次改写降至 14-41%，五次链式改写后仅 4.86%（94.76% 原检出文本失效）；三次改写后检测分数已走完朝空分布 86% 的路程，重复改写远强于单次攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Statistical watermarking is a common approach for verifying whether text was written by a language model. Most existing schemes assume autoregressive generation, where tokens are produced left to right and contextual hashing is well defined. Diffusion language models generate text by denoising tokens in arbitrary order, so these schemes cannot be applied directly. A recent watermark by Gloaguen et al. addresses this gap for LLaDA 8B Instruct and reports true positive detection above 99%. This paper studies what happens when watermarked text is rewritten not once but several times. Using the same watermark configuration, 1,605 watermarked completions of about 300 tokens each are produced across five WaterBench domains. Each completion is rewritten by four open weight language models, from 1.5B to 8B parameters, none of which know the watermark key. Five rewrite styles are tested: paraphrase, humanize, simplify, academic, and summarize expand. Each style is chained for up to five hops, producing 160,500 rewritten texts in total. The watermark is detected on 87.9% of the original outputs at the standard significance threshold. After a single rewrite, detection falls to between 14% and 41% depending on the rewriter and style. After five chained rewrites, detection falls to 4.86%, meaning 94.76% of the originally detected texts are no longer flagged. After three rewrites, the detector score has dropped 86% of the way from its watermarked baseline toward the null distribution. Repeated rewriting is therefore a much stronger attack than a single rewrite, and the result holds across all four rewriters tested.

</details>

### 26. dQwen3.5: Hybrid-Attention Diffusion Language Models

📄 [arXiv](https://arxiv.org/abs/2609.20751)　📅 2026-09

**关键词**：`analysis`、`diffusion language model`、`hybrid attention`、`AR adaptation`、`model family`

👤 **作者**：Anton Xue、Litu Rout、Aditya Akella、Adam Klivans、Sujay Sanghavi、Sanjay Shakkottai

- 🎯 **研究动机**：预训练 AR 模型适配是通往扩散语言模型（DLM）的高效路线，但 AR 建模已转向注意力与 RNN 交错的混合架构——RNN 结构性因果、难以双向化，混合骨干能否成为有效 DLM 起点
- 🔬 **研究方法**：在 0.8B/2B/4B/9B 四个尺度适配 Qwen3.5 得 dQwen3.5 家族；与全注意力对照比较训练效率与任意序解码行为
- 📌 **结论**：混合骨干是高效适配起点：达到同等训练损失约省一半 token；各尺度下 dQwen3.5 在任意序解码行为上类似全注意力 DLM 并在并行解码下表现强——dLLM 家族的能力面（dllm 安全研究的对象底座）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adapting a pretrained autoregressive (AR) model is a cost-efficient route to a diffusion language model (DLM). While nearly all such adaptations start from a full-attention transformer, AR modeling has shifted toward hybrid architectures that interleave attention and RNN layers. This creates an obstacle for adaptation: unlike attention, RNNs are structurally causal and nontrivial to bidirectionalize. Despite this mismatch, we investigate whether such backbones can become effective DLMs by adapting Qwen3.5 at 0.8B, 2B, 4B, and 9B scales, yielding the dQwen3.5 family. We find that hybrid backbones can be efficient starting points for adaptation: against a full-attention control, the hybrid reaches a given training loss in about half the tokens. Across scales, dQwen3.5 resembles full-attention DLMs in any-order decoding behavior and performs strongly under parallel decoding.

</details>

### 27. LOCKR: A Hidden-State Trajectory-Guided Planner for Detecting and Repairing Stable-but-Wrong Lock-In in Diffusion Language Models

📄 [arXiv](https://arxiv.org/abs/2609.27220)　📅 2026-09

**关键词**：`defense`、`stable-but-wrong lock-in`、`hidden-state trajectory`、`test-time repair`、`diffusion language model`

👤 **作者**：Guoshenghui Zhao、Tan Yu、Weijie Zhao

- 🎯 **研究动机**：扩散语言模型经迭代去噪暴露中间轨迹——存在稳定但错误的锁定：答案早期稳定在错误值而大量去噪仍在继续；置信/熵/margin/稳定性等表面信号无法区分正误锁定
- 🔬 **研究方法**：LOCKR：隐藏状态轨迹引导的测试时规划器——决定何时分配额外计算、展开结构化修复分支、用轨迹感知验证选择最有希望的延续；两个 DLM × 三个数学推理基准
- 📌 **结论**：隐藏状态轨迹全面优于表面信号与单快照——DLM 推理失效的内部状态检测与修复（DLM 安全监控线的首个系统性内部信号工作）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion language models generate text through iterative denoising, exposing intermediate trajectories before final answers are produced. We identify a recurring reasoning failure, stable-but-wrong lock-in, where an answer stabilizes early around an incorrect value while substantial denoising remains. Surface-level decoding signals such as confidence, entropy, margin, and answer stability are insufficient to reliably distinguish correct from erroneous lock-in. We formulate selective reasoning repair as a lightweight test-time planning problem and propose LOCKR, a hidden-state trajectory-guided planner that decides when to allocate additional computation, expands a structured set of targeted repair branches, and selects the most promising continuation using trajectory-aware verification. Across two diffusion language models and three mathematical reasoning benchmarks, hidden-state trajectories consistently outperform surface signals and single hidden snapshots for both wrong-lock-in detection and repair selection. On natural evaluation distributions, LOCKR yields absolute accuracy gains of 2.21--5.37 percentage points across all five evaluated settings, with repair rates ranging from 22% to 41%. These results establish hidden diffusion trajectories as actionable signals for selective test-time reasoning repair.

</details>
