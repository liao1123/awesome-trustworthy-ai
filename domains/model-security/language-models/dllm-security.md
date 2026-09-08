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

### 3. Mechanism Shift During Post-training from Autoregressive to Masked Diffusion Language Models

📄 [arXiv](https://arxiv.org/abs/2601.14758)　📅 2026-01

**关键词**：`analysis`、`AR-to-diffusion post-training`、`circuit shift`、`global planning`

👤 **作者**：Injin Kong、Hyoungjoon Lee、Yohan Jo

- 🎯 **研究动机**：自回归模型后训练为 masked diffusion 后，继承的计算被复用还是为非自回归生成重组不明
- 🔬 **研究方法**：对两族 7B ARM-MDM 在四个受控诊断任务上比较高归因通路、层深分布与组件特化程度
- 📌 **结论**：前缀主导任务基本保留 AR 通路；全局约束任务重组更强、计算向浅层前移；MDM 单组件特化更弱、输出空间对齐更弥散

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Post-training pretrained autoregressive models (ARMs) into masked diffusion models (MDMs) provides an efficient route to diffusion language modeling, but it remains unclear whether the resulting models reuse inherited autoregressive computation or reorganize it for non-autoregressive generation. We compare two 7B ARM-MDM families across four controlled diagnostic tasks and find a task-dependent mechanism shift. On prefix-dominant tasks, MDMs largely preserve inherited high-attribution pathways or exhibit only modest changes in where computation occurs. On globally constrained tasks, the reorganization is substantially stronger, with task-relevant computation shifting toward earlier layers. This depth-wise pattern persists across prompt resampling, circuit budgets, and tested inference budgets, while targeted ablations support the functional importance of the identified structures under the tested intervention protocols. At the component level, diagnostic probes suggest that ARMs rely more strongly on sharply specialized components, whereas MDMs exhibit weaker single-component specialization and more diffuse output-space alignment. Together, these results suggest that diffusion post-training selectively preserves or reorganizes inherited computation according to task structure, rather than uniformly replacing autoregressive mechanisms.

</details>

### 4. Diffusion LLMs as Targets and Adversaries: Mechanistic Safety Exploits

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

### 5. MaskForge: Structure-Aware Adaptive Attacks for Jailbreaking Diffusion Large Language Models

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

### 6. The Devil Behind the Mask: An Emergent Safety Vulnerability of Diffusion LLMs

📄 [arXiv](https://arxiv.org/abs/2507.11097) · 📝 [OpenReview](https://openreview.net/forum?id=rIPeatvPy3)　📅 2026　🏷 ICLR 2026

**关键词**：`attack`、`interleaved mask-text`、`bidirectional infilling`、`parallel decoding`

👤 **作者**：Zichen Wen、…、Linfeng Zhang

- 🎯 **研究动机**：dLLM对齐未覆盖用户直接控制masked span的场景
- 🔬 **研究方法**：DIJA将harmful text与mask交错，借双向一致性与并行解码补全缺失内容
- 📌 **结论**：无需隐藏恶意语义即显著绕过多种aligned dLLM

### 7. Jailbreaking Large Language Diffusion Models: Revealing Hidden Safety Flaws in Diffusion-Based Text Generation

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

### 8. TRE: Training-Free Hallucination Detection for Diffusion Language Models

📄 [arXiv](https://arxiv.org/abs/2607.22661)　📅 2026-06

**关键词**：`detection`、`entropy trajectory`、`revealing token`、`single-run metric`

👤 **作者**：Pengcheng Weng、Yanyu Qian、Yue Tan、Yixin Liu

- 🎯 **研究动机**：D-LLM 的幻觉检测沿用训练范式，跨域泛化差且带来训练与部署开销
- 🔬 **研究方法**：提出 TRE 免训练单次运行指标：从单次生成的解码熵信号中，token 空间维聚焦于承担不确定性承诺的 revealing tokens，时间维聚合后期步主导的熵并以线性加权融合
- 📌 **结论**：多个 D-LLM 与 QA 数据集上性能具竞争力，且泛化性、效率与鲁棒性强

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion large language models (D-LLMs) have recently gained increasing attention, yet their reliability is significantly hindered by the hallucination problem. Existing hallucination detection approaches for D-LLMs mainly follow a training-based paradigm, relying on data-driven training to optimize the detector. Such reliance not only limits their generalizability across domains models but also incurs additional training cost and deployment overhead. To address these limitations, we propose TRE, a training-free hallucination detection metric for D-LLMs. TRE is a parameter-free and single-run metric that estimates hallucination risk directly from the entropy signals of a single generation, without requiring any detector training or repeated sampling. TRE extracts entropy signals within the D-LLM decoding process along both the spatial and temporal dimensions. From a token-level spatial perspective, we focus on revealing tokens as the most informative carriers of uncertainty, capturing where uncertainty is actively committed. From a diffusion step-level temporal perspective, we empirically identify the dominance of late-step entropy and hence aggregate these signals with a simple linear weighting scheme to obtain TRE. Extensive experiments on multiple D-LLMs and QA datasets demonstrate that TRE achieves competitive performance, while enjoying strong generalizability, efficiency, and robustness.

</details>

### 9. $D^2$-Monitor: Dynamic Safety Monitoring for Diffusion LLMs via Hesitation-Aware Routing

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

### 10. Beyond the Prompt: Leveraging Pre-Decoding States for Jailbreak Detection in dLLMs

📝 [OpenReview](https://openreview.net/forum?id=QVRvaVBwRh)　📅 2026

**关键词**：`detection`、`pre-decoding state`、`state fusion`、`jailbreak detection`

- 🎯 **研究动机**：prompt-only检测器看不到dLLM在masked response中已形成的风险信号
- 🔬 **研究方法**：融合prompt表示与首轮pre-decoding response state做状态融合检测
- 📌 **结论**：diffusion-native jailbreak漏检显著降低且良性误拒低

### 11. TraceDet: Hallucination Detection from the Decoding Trace of Diffusion Large Language Models

📄 [arXiv](https://arxiv.org/abs/2510.01274) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10011524)　📅 2025-09　🏷 ICLR 2026

**关键词**：`detection`、`decoding trace`、`temporal representation`、`hallucination detection`

👤 **作者**：Shenxu Chang、…、Jindong Gu

- 🎯 **研究动机**：既有幻觉检测面向单步生成的自回归 LLM，不适配多步去噪的 D-LLM
- 🔬 **研究方法**：提出 TraceDet：把去噪过程建模为动作轨迹，定位对幻觉响应信息量最大的子轨迹做检测
- 📌 **结论**：多个开源 D-LLM 上一致提升幻觉检测，AUROC 平均增益 15.2%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion large language models (D-LLMs) have recently emerged as a promising alternative to auto-regressive LLMs (AR-LLMs). However, the hallucination problem in D-LLMs remains underexplored, limiting their reliability in real-world applications. Existing hallucination detection methods are designed for AR-LLMs and rely on signals from single-step generation, making them ill-suited for D-LLMs where hallucination signals often emerge throughout the multi-step denoising process. To bridge this gap, we propose TraceDet, a novel framework that explicitly leverages the intermediate denoising steps of D-LLMs for hallucination detection. TraceDet models the denoising process as an action trace, with each action defined as the model's prediction over the cleaned response, conditioned on the previous intermediate output. By identifying the sub-trace that is maximally informative to the hallucinated responses, TraceDet leverages the key hallucination signals in the multi-step denoising process of D-LLMs for hallucination detection. Extensive experiments on various open source D-LLMs demonstrate that TraceDet consistently improves hallucination detection, achieving an average gain in AUROC of 15.2% compared to baselines.

</details>

### 12. Beyond Token Positions: Safety Alignment Across Denoising Steps in Diffusion Language Models

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

### 13. Adaptive Steering and Remasking for Safe Generation in Diffusion Language Models

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

### 14. The Safety-Aware Denoiser for Text Diffusion Models

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

### 15. Toward Safer Diffusion Language Models: Discovery and Mitigation of Priming Vulnerability

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

### 16. DiffuGuard: How Intrinsic Safety is Lost and Found in Diffusion Large Language Models

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

### 17. A2D: Any-Order, Any-Step Safety Alignment for Diffusion Language Models

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

### 18. From Vulnerability to Defense: Understanding and Mitigating MASK-Based Attacks in dLLMs

📝 [OpenReview](https://openreview.net/forum?id=jKQQb8uClw)　📅 2025-09　🏷 ICLR 2026

**关键词**：`defense`、`MASK-based jailbreak`、`margin accumulation`、`Reject-MASK`

- 🎯 **研究动机**：MASK-based prompt借margin累积与并行解码绕过dLLM安全对齐，机制不明
- 🔬 **研究方法**：从margin accumulation与scheduling advantage解析机制，提出Reject-MASK两阶段训练
- 📌 **结论**：把超过90%的ASR降至接近个位数

### 19. Where to Start Alignment? Diffusion Large Language Model May Demand a Distinct Position

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

### 20. TrustLDM: Benchmarking Trustworthiness in Language Diffusion Models

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

### 21. Discrete Diffusion in Large Language and Multimodal Models: A Survey

📄 [arXiv](https://arxiv.org/abs/2506.13759)　📅 2025-06

**关键词**：`survey`、`discrete diffusion`、`parallel decoding`、`model taxonomy`

👤 **作者**：Runpeng Yu、Qi Li、Xinchao Wang

- 🎯 **研究动机**：离散扩散语言模型与多模态模型快速发展，缺乏系统综述
- 🔬 **研究方法**：系统梳理 dLLM 与 dMLLM 的历史、数学框架、建模方法与代表模型，分析训练、推理、量化技术及可信问题
- 📌 **结论**：d(M)LLM 性能比肩自回归模型且推理加速最高 10 倍，是自回归路线的有力替代

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In this work, we provide a systematic survey of Discrete Diffusion Language Models (dLLMs) and Discrete Diffusion Multimodal Language Models (dMLLMs). Unlike autoregressive (AR) models, dLLMs and dMLLMs adopt a multi-token, parallel decoding paradigm using full attention and a denoising-based generation strategy. This paradigm naturally enables parallel generation, fine-grained output control, and dynamic perception. These capabilities are previously difficult to achieve with AR models. A growing number of industrial-scale proprietary d(M)LLMs, as well as a large number of open-source academic d(M)LLMs, have demonstrated performance comparable to their autoregressive counterparts, while achieving up to 10$\times$ acceleration in inference speed. These developments position discrete diffusion models as a promising alternative to intelligence based on the traditional autoregressive approach. In this work, we present a comprehensive overview of the research in the dLLM and dMLLM domains. We trace the historical development of dLLMs and dMLLMs, formalize the underlying mathematical frameworks, list commonly-used modeling methods, and categorize representative models. We further analyze key techniques for training, inference, quantization. We also discuss the trustworthy issues and summarize emerging applications across language, vision-language, and biological domains and etc.. We conclude by discussing future directions for research and deployment. Relative papers are collected in https://github.com/LiQiiiii/Awesome-Discrete-Diffusion-LLM_MLLM

</details>