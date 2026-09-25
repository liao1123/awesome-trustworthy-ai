# VLM Safety Alignment

[返回 Multimodal Model Security 目录](README.md)

## 研究方向

本页研究 VLM/MLLM 如何在视觉输入中保持或修正 safety-relevant alignment boundary，既包括语言骨干中的 harmfulness recognition 与 refusal，也包括具有明确群体伤害的 demographic bias。核心问题是 image token、cross-modal fusion 和 representation geometry 是否让视觉语义落到既有安全边界之外，以及能否通过训练或 inference-time calibration 恢复安全或公平行为而不损害通用视觉能力。

## 研究脉络

- **安全迁移缺口：** 早期工作发现加入视觉模块后，语言骨干已有的拒答能力会显著退化，安全与通用能力之间出现新的 modality gap。
- **机制定位：** Modality-gap geometry、shared safety neuron、refusal／bias subspace 与 token-level gate 分析安全或群体偏差信号如何进入视觉表示；只研究通用 modality alignment 或 reasoning transfer 的工作不收录。
- **训练期对齐：** safety tuning 从直接拟合拒答，发展到 cross-modal representation matching、modality-gap regularization 和 safety-relevant self-captioning。
- **推理期校准：** training-free 方法利用 textual refusal direction、unsafe prototype、counterfactual bias subspace 或 estimated drift，只修正 safety-relevant representation 而尽量保留视觉语义。
- **当前边界：** 固定 steering direction 容易引入 over-refusal 或 utility loss；评测需要同时覆盖目标安全／公平指标、跨模态输入、视觉 utility 和未见模型架构。

## 安全迁移机制与诊断

### 1. Compliance, Capability, and Conflict: Benchmarking Multimodal LLMs under System Messages

📄 [arXiv](https://arxiv.org/abs/2608.19207)　📅 2026-08

**关键词**：`benchmark`、`system-message compliance`、`instruction hierarchy`、`multimodal constraint`、`multimodal system message`、`capability-compliance trade-off`

👤 **作者**：Juan Yeo、Geewook Kim

- 🎯 **研究动机**：MLLM 生产部署靠系统消息治理行为，但多模态上下文中的系统消息依从性未被测量
- 🔬 **研究方法**：VSysBench 基于 MMVet-v2：5 大类 22 子类约束从文本指令到视觉接地，配错位对照测指令层级；以联合满足率 JSR 与跨约束敏感性 CCS 双轴打分 16 个 MLLM
- 📌 **结论**：施加系统消息显著侵蚀基础任务准确率；用户冲突下开源模型合规崩塌而顶级闭源稳定；视觉接地约束对所有模型最难

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Production deployments of Multimodal Large Language Models (MLLMs) increasingly rely on system messages to govern model behavior. Yet existing benchmarks either evaluate constraints in text only or embed them into the user turn, leaving system-message adherence in multimodal contexts largely unmeasured; they also leave open whether compliance comes at the cost of foundational vision-language capabilities. We introduce VSysBench, a benchmark built on MMVet-v2 that organizes constraints into 5 main categories and 22 sub-categories, ranging from textual directives in visual contexts to fully vision-grounded ones, each paired with a misaligned counterpart that stress-tests the instructional hierarchy. VSysBench scores each response jointly along two axes, constraint compliance and answer correctness, via the Joint Satisfaction Rate (JSR) and Cross-Constraint Sensitivity (CCS). Across 16 MLLMs, we find that imposing system messages substantially erodes base task accuracy, that compliance collapses under user conflict for open-weight models while remaining stable for top proprietary ones, and that vision-grounded constraints are the hardest category for every model.

</details>

### 2. MMJailBench: A Factorized Benchmark for Disentangling Multimodal Jailbreak Vulnerabilities

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

### 3. Text-Anchored Semantic Perturbations for Transferable Jailbreak Attacks on Multimodal Large Language Models

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

### 4. MMAligner: Safeguarding Multimodal Large Language Models through Representation Calibration

📄 [arXiv](https://arxiv.org/abs/2608.05909) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2026-08　🏷 ACM CCS 2026

**关键词**：`analysis`、`defense`、`shared safety subspace`、`representation shift`、`refusal boundary`、`multimodal alignment`

👤 **作者**：Shenyi Zhang、…、Qian Wang

- 🎯 **研究动机**：MLLM 对语义等价的多模态输入产生有害回答，源于表征偏移而非安全能力缺失
- 🔬 **研究方法**：几何分析发现文本学到的安全子空间与拒答边界跨模态持续有效，但不安全多模态输入的表征移位到边界外；MMAligner 以硬下界、软上界与良性保持目标把不安全表征校准回拒答区
- 📌 **结论**：多个开源 MLLM 上不安全多模态输入的平均拒答率提升至 99%，效用损失小于 2% 且仅需极少训练数据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) often refuse unsafe text prompts yet generate harmful responses to semantically equivalent multimodal inputs. Existing defenses either rely on external guardrails, which add inference overhead without repairing intrinsic flaws, or safety fine-tuning, which treats alignment as black-box optimization and may sacrifice utility or require large multimodal datasets. To identify the cause of this safety disparity, we analyze MLLM representations geometrically. We find that safety mechanisms learned from text persist across modalities: a shared safety subspace and refusal boundary remain effective, and representations inside this boundary consistently trigger refusals. However, unsafe multimodal inputs undergo a representation shift that places most of them outside the boundary, allowing them to bypass the model's intrinsic safety mechanism. This indicates that multimodal safety degradation stems from representation misalignment rather than the absence of safety capability. Based on this finding, we propose MMAligner, a safeguarding method that calibrates unsafe multimodal representations into the pre-existing refusal region. MMAligner applies a hard lower bound to ensure refusal, a soft upper bound to avoid excessive modification, and a preservation objective for benign inputs. Experiments across multiple open-source MLLMs show that MMAligner raises the average refusal rate on unsafe multimodal inputs to 99% with less than 2% utility degradation and minimal training data, substantially improving the safety-utility trade-off over existing baselines. (*Due to the notification from arXiv, "The Abstract field cannot be longer than 1,920 characters", the Abstract that appeared is shortened.)

</details>

### 5. Safety Geometry Collapse in Multimodal LLMs and Adaptive Drift Correction

📄 [arXiv](https://arxiv.org/abs/2605.18104)　📅 2026-05

**关键词**：`analysis`、`safety geometry collapse`、`modality drift`、`refusal separability`

👤 **作者**：Jiahe Guo、…、Bing Qin

- 🎯 **研究动机**：MLLM 难以把文本模态学到的安全能力迁移到语义等价的非文本输入，其表征几何机制不明
- 🔬 **研究方法**：定义 Safety Geometry Collapse：多模态输入压缩 refusal 方向的可用分离度，modality-induced drift 越强分离度越差；ReGap 以 self-rectification 信号免训练自适应校正漂移
- 📌 **结论**：固定强度激活干预证明漂移的因果性，校正后模型恢复识别并拒绝有害输入；ReGap 在多个安全基准显著提升安全且不损通用能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) often fail to transfer safety capabilities learned in the text modality to semantically equivalent non-text inputs, revealing a persistent multimodal safety gap. We study this gap from a representation-geometric perspective by analyzing a text-aligned refusal direction and a modality-induced drift direction. We show that multimodal inputs compress the usable separation along the refusal direction, making it no longer reliable for identifying and refusing harmful inputs. We refer to this failure mode as Safety Geometry Collapse. We quantify it through conditional refusal separability and show that stronger modality-induced drift is consistently associated with weaker refusal separability and higher attack success rates. We then validate the causal role of modality-induced drift through a fixed-strength activation intervention: counteracting the estimated drift restores refusal separability and improves multimodal safety. After drift correction, we further observe self-rectification, where the model recovers its ability to recognize and refuse harmful multimodal inputs during forward dynamics. This effect also provides an internal signal of the model's perceived harmfulness of each input. Motivated by this signal, we propose ReGap, a training-free inference-time method that adaptively corrects modality drift using self-rectification. Experiments across multiple multimodal safety benchmarks and utility benchmarks demonstrate the effectiveness of ReGap, which significantly improves the safety of MLLMs without compromising general capabilities. Our findings highlight representation-level modality alignment as a crucial direction for real-time safety improvement and for building safer, more reliable MLLMs.

</details>

### 6. Targeted Interpretable Safety Neuron Enhancement for Multilingual Vision-Language Large Models

📄 [arXiv](https://arxiv.org/abs/2604.08881)　📅 2026-04

**关键词**：`analysis`、`safety neuron`、`cross-modal overlap`、`gradient masking`

👤 **作者**：Enyi Shi、…、Tat-Seng Chua

- 🎯 **研究动机**：现有方法分别建模多语言与多模态安全，忽略低资源语言指令与视觉上下文的耦合风险
- 🔬 **研究方法**：对比良性与有害请求的 FFN 激活定位 safety neuron，联合 down-projection 列计算神经元显著性，再用梯度掩码把参数更新限制在安全神经元子空间
- 📌 **结论**：仅微调少量 safety neuron 即可同时提升多语言与多模态安全，并保持通用能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the widespread deployment of vision-language large models (VLLMs), their safety alignment faces dual challenges across languages and modalities. Existing methods model multilingual and multimodal safety separately, overlooking coupled risks between low-resource-language instructions and visual contexts, which hinders the detection of cross-lingual and cross-modal harmful intent and the formation of robust safety boundaries. To address this, we propose a neuron-level interpretable safety alignment framework that identifies safety neurons and performs neuron-targeted safety tuning to jointly mitigate multilingual and multimodal risks. Specifically, we compare FFN representations elicited by harmful requests and benign inputs to identify neuron activation strengths associated with safety refusals. Next, we jointly model neuron activations and corresponding down-projection columns to derive neuron-level saliency, separating general multilingual and multimodal neurons from safety neurons responsible for model defense. Finally, neuron-targeted gradient masking restricts parameter updates to the safety subspace spanned by the identified neurons, enabling precise and interpretable safety enhancement. Extensive experiments show that our method enhances multilingual and multimodal safety by tuning only a few safety neurons, while preserving general capabilities.

</details>

### 7. Unraveling and Mitigating Safety Alignment Degradation of Vision-Language Models

🎓 [Official](https://aclanthology.org/2025.findings-acl.186/)　📅 2025-07　🏷 ACL 2025

**关键词**：`analysis`、`safety alignment degradation`、`cross-modal representation`、`utility retention`

👤 **作者**：Qin Liu、…、Yassine Benajiba

- 🎯 **研究动机**：VLM 引入视觉模块后安全对齐较 LLM 骨干退化，根源是多模态表示偏离文本优化分布且对齐能力未迁移到新表示空间
- 🔬 **研究方法**：提出推理时表示干预方法 CMRM，恢复 LLM 骨干固有的安全对齐能力并保留 VLM 功能能力
- 📌 **结论**：LLaVA-7B 多模态输入的不安全率从 61.53% 降至 3.15%，无需额外训练且几乎不影响流畅性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The safety alignment ability of Vision-Language Models (VLMs) is prone to be degraded by the integration of the vision module compared to its LLM backbone. We investigate this phenomenon, dubbed as “safety alignment degradation” in this paper, and show that the challenge arises from the representation gap that emerges when introducing vision modality to VLMs. In particular, we show that the representations of multi-modal inputs shift away from that of text-only inputs which represent the distribution that the LLM backbone is optimized for. At the same time, the safety alignment capabilities, initially developed within the textual embedding space, do not successfully transfer to this new multi-modal representation space. To reduce safety alignment degradation, we introduce Cross-Modality Representation Manipulation (CMRM), an inference time representation intervention method for recovering the safety alignment ability that is inherent in the LLM backbone of VLMs, while simultaneously preserving the functional capabilities of VLMs. The empirical results show that our framework significantly recovers the alignment ability that is inherited from the LLM backbone with minimal impact on the fluency and linguistic capabilities of pre-trained VLMs even without additional training. Specifically, the unsafe rate of LLaVA-7B on multi-modal input can be reduced from 61.53% to as low as 3.15% with only inference-time intervention.

</details>

### 8. SafeCap: Improving LVLM Safety with Image Captioning Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2608.10513)　📅 2026-08

**关键词**：`defense`、`safety self-captioning`、`reinforcement learning`、`vision utility`

👤 **作者**：Caoyuan Ma、…、Yinqiang Zheng

- 🎯 **研究动机**：LVLM 的视觉越狱绕过继承自语言骨干的安全对齐，直接拒答监督不足以暴露视觉风险线索
- 🔬 **研究方法**：SafeCap 用 RL 训练策略先生成安全相关图像描述再作答，描述以能否让冻结 LLM 做出安全对齐决策为奖励优化
- 📌 **结论**：五个多模态安全基准上安全平均提升 3.7-19.0 分且视觉效用保持；受控对比优于安全 SFT、DPO 与 SafeGRPO

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large vision-language models (LVLMs) remain vulnerable to jailbreak attacks that exploit visual inputs to bypass safety alignment inherited from their language backbones. We propose SafeCap, a reinforcement-learning framework that aligns LVLMs through learned self-captioning. SafeCap trains a policy model to first generate a safety-relevant image caption and then produce a final answer; the caption is further optimized by whether it enables a frozen LLM to reach a safety-aligned decision. This caption-mediated objective encourages the policy to expose visual cues relevant to safe response generation rather than relying solely on direct refusal supervision. Across five multimodal safety benchmarks and six vision-utility benchmarks, SafeCap substantially improves aggregate safety performance under its intended DirectCap protocol, with gains of 3.7-19.0 points in safety average across four model settings while maintaining comparable or improved vision utility. Under controlled comparisons on matched backbones and data, SafeCap outperforms safety SFT, DPO, and SafeGRPO, demonstrating the effectiveness of caption-mediated reinforcement learning for multimodal safety alignment.

</details>

### 9. Visual Self-Fulfilling Alignment: Shaping Safety-Oriented Personas via Threat-Related Images

📄 [arXiv](https://arxiv.org/abs/2603.08486) · 🎓 [Official](https://aclanthology.org/2026.acl-long.490/)　📅 2026-03　🏷 ACL 2026

**关键词**：`defense`、`safety persona`、`threat-related image`、`visual alignment`、`LLM jailbreak`、`automated red teaming`

👤 **作者**：Qishun Yang、Shu Yang、Lijie Hu、Di Wang

- 🎯 **研究动机**：威胁概念具体可视而安全概念抽象无视觉对应，现有对齐需显式安全标签或对比数据
- 🔬 **研究方法**：VSFA 在围绕威胁相关图像构建的中性 VQA 任务上微调 VLM，无任何安全标签，借自实现机制内化警觉语义塑造安全人格
- 📌 **结论**：多个 VLM 与安全基准上降低 ASR、提升回复质量并缓解过度拒绝，同时保留通用能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) face safety misalignment, where visual inputs enable harmful outputs. To address this, existing methods require explicit safety labels or contrastive data; yet, threat-related concepts are concrete and visually depictable, while safety concepts, like helpfulness, are abstract and lack visual referents. Inspired by the Self-Fulfilling mechanism underlying emergent misalignment, we propose Visual Self-Fulfilling Alignment (VSFA). VSFA fine-tunes vision-language models (VLMs) on neutral VQA tasks constructed around threat-related images, without any safety labels. Through repeated exposure to threat-related visual content, models internalize the implicit semantics of vigilance and caution, shaping safety-oriented personas. Experiments across multiple VLMs and safety benchmarks demonstrate that VSFA reduces the attack success rate, improves response quality, and mitigates over-refusal while preserving general capabilities. Our work extends the self-fulfilling mechanism from text to visual modalities, offering a label-free approach to VLMs alignment.

</details>

### 10. AM$^3$Safety: Towards Data Efficient Alignment of Multi-modal Multi-turn Safety for MLLMs

📄 [arXiv](https://arxiv.org/abs/2601.04736)　📅 2026-01

**关键词**：`defense`、`multi-turn safety alignment`、`InterSafe-V`、`GRPO`

👤 **作者**：Han Zhu、…、Sirui Han

- 🎯 **研究动机**：多轮多模态交互中对手可跨轮渐进重构有害意图，面向 VQA 的 RLHF 既不捕捉跨轮风险动态也难免昂贵标注
- 🔬 **研究方法**：构建含 11270 条多图对话加 500 拒答 VQA 的 MINT-Safe 数据集，提出 TAD-Align：以 rollout 安全分方差动态识别安全行为不稳轮次并自适应加权的轮次感知双目标奖励
- 📌 **结论**：在 Qwen2.5-VL 与 LLaVA-NeXT 上 ASR 降超 10%，harmlessness 至少提升 8%、helpfulness 13%，通用能力保持

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite remarkable capability in multi-modal understanding, deploying Multi-modal Large Language Models (MLLMs) in open-ended conversational scenarios introduces safety risks that remain poorly addressed by existing alignment methods. Unlike simple malicious visual question and answer (VQA) pairs , multi-turn interactions enable adversaries to incrementally reconstruct harmful intent across dialogues, progressively bypassing safety constraints in ways that are difficult to detect at any individual turn. Meanwhile, conventional reinforcement learning from human feedback (RLHF) approaches are unsuitable for this situation: designed primarily for VQA tasks, they neither capture cross-turn risk dynamics nor scale efficiently without costly manual preference annotation. To close this gap, we introduce \textbf{MINT-Safe}, an open-source visual multi-turn training dataset comprising 11,270 multi-image dialogues and 500 refusal VQA pairs, constructed via multi-agent interaction with text-to-image (T2I) tool-call augmentation. Building on MINT-Safe, we propose \textbf{TAD-Align}, a dialogue safety alignment framework centered on a turn-aware dual-objective reward function. Rather than treating all dialogue turns uniformly, TAD-Align leverages rollout-based safety score variance to dynamically identify turns where the model exhibits inconsistent safety behavior, and adaptively up-weights these turns during optimization. Experiments on Qwen2.5-VL-7B-Instruct and LLaVA-NeXT-7B demonstrate reductions of over 10\% in Attack Success Rate (ASR), alongside improvements of at least 8\% in harmlessness and 13\% in helpfulness on multi-modal multi-turn safety benchmarks, while preserving general model capabilities.

</details>

### 11. Teach to Reason Safely: Policy-Guided Safety Tuning for MLRMs

🎓 [Official](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8ece25974724edad00c8d0bcc8a235e8-Abstract-Conference.html)　📅 2026　🏷 ICLR 2026

**关键词**：`defense`、`multimodal reasoning safety`、`policy-guided SFT`、`preference optimization`

👤 **作者**：Jingyu Zhang、…、Zhaohui Yang

- 🎯 **研究动机**：多模态推理因visual attention drift与不安全推理模式而失守
- 🔬 **研究方法**：PST先以显式policy做SFT，再优化安全推理偏好
- 📌 **结论**：多项benchmark有害输出减少且通用推理保持

### 12. Meerkat-VL: Implicit Risk Safety Alignment in Multimodal LLMs via Perceptual Reasoning and Self-Verification

📊 [Dataset](https://huggingface.co/datasets/Tunanzzz/Meerkat-Safe) · 📝 [OpenReview](https://openreview.net/forum?id=lbaBsu0CaY) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61928)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`implicit cross-modal risk`、`self-verification`、`GRPO`、`safety alignment`、`reinforcement learning`

👤 **作者**：Peicheng Zhou、…、Hongtao Xie

- 🎯 **研究动机**：显式风险偏好数据稀缺且隐式风险场景 reward hacking，导致风险感知不足产生有害响应
- 🔬 **研究方法**：首个隐式风险细标注数据集 Meerkat-Safe；Normative Perceptual Self-Verification 校验感知与回答提供更密奖励；双目标感知一致性对齐惩罚空套安全模板的回答
- 📌 **结论**：多模态安全基准上安全与有用性提升 16%/13%，隐式风险任务安全增益 32%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal LLMs (MLLMs) are increasingly deployed across diverse applications, but they pose significant safety concerns due to cross-modal interactions. To improve model safety awareness, existing methods rely on explicit-risk preference datasets and reinforcement learning guided by safety rewards. While effective in improving models' safety awareness, these methods still face data scarcity and reward hacking in implicit-risk scenarios, leading to insufficient risk perception and harmful responses. To address these challenges, we propose Meerkat-VL, a framework that enables models to perceive and verify implicit risks while generating safe responses. First, we introduce Meerkat-Safe, the first training dataset with detailed labels for implicit risks. Second, we develop Normative Perceptual Self-Verification, which enables models to verify both perceptual reasoning and responses. This process provides denser and more reliable rewards for perception accuracy and answer safety, thereby mitigating reward hacking. Finally, we propose Dual-Objective Perceptual Consistency Alignment, encouraging models to generate safe responses by penalizing answers that follow safe templates without accurate risk perception. Extensive experiments show that Meerkat-VL consistently outperforms baselines on multimodal safety benchmarks, improving safety and helpfulness by 16% and 13%, and achieving a 32% safety gain on implicit-risk tasks. Our codes are available at https://github.com/Tunanzzz/Meerkat-VL.

</details>

### 13. SafeGRPO: Self-Rewarded Multimodal Safety Alignment via Rule-Governed Policy Optimization

📄 [arXiv](https://arxiv.org/abs/2511.12982) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Rong_SafeGRPO_Self-Rewarded_Multimodal_Safety_Alignment_via_Rule-Governed_Policy_Optimization_CVPR_2026_paper.html)　📅 2025-11　🏷 CVPR 2026

**关键词**：`defense`、`self-reward alignment`、`rule-governed reward`、`multimodal safety`、`multimodal alignment`、`policy optimization`

👤 **作者**：Xuankun Rong、Wenke Huang、Tingfeng Wang、Daiguo Zhou、Bo Du、Mang Ye

- 🎯 **研究动机**：MLLM 的跨模态耦合可在单个输入良性时产生不安全语义，而 GRPO 缺乏可验证的安全推理信号
- 🔬 **研究方法**：SafeGRPO 把规则治理的奖励构造融入 GRPO 实现自奖励安全对齐，基于含视觉、文本与组合安全标签的 SafeTag-VL-3K 数据集进行步引导的安全思考训练
- 📌 **结论**：多基准上显著提升多模态安全意识、组合鲁棒性与推理稳定性，且不牺牲通用能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) have demonstrated impressive reasoning and instruction-following capabilities, yet their expanded modality space introduces new compositional safety risks that emerge from complex text-image interactions. Such cross-modal couplings can produce unsafe semantics even when individual inputs are benign, exposing the fragile safety awareness of current MLLMs. While recent works enhance safety by guiding models to reason about potential risks, unregulated reasoning traces may compromise alignment; although Group Relative Policy Optimization (GRPO) offers self-rewarded refinement without human supervision, it lacks verifiable signals for reasoning safety. To address this, we propose SafeGRPO a self-rewarded multimodal safety alignment framework that integrates rule-governed reward construction into GRPO, enabling interpretable and verifiable optimization of reasoning safety. Built upon the constructed SafeTag-VL-3K dataset with explicit visual, textual, and combined safety tags, SafeGRPO performs step-guided safety thinking to enforce structured reasoning and behavior alignment, substantially improving multimodal safety awareness, compositional robustness, and reasoning stability across diverse benchmarks without sacrificing general capabilities.

</details>

### 14. Harmonious Parameter Adaptation in Continual Visual Instruction Tuning for Safety-Aligned MLLMs

📄 [arXiv](https://arxiv.org/abs/2511.20158) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Harmonious_Parameter_Adaptation_in_Continual_Visual_Instruction_Tuning_for_Safety-Aligned_CVPR_2026_paper.html)　📅 2025-11　🏷 CVPR 2026

**关键词**：`defense`、`continual tuning`、`safety alignment`、`parameter adaptation`

👤 **作者**：Ziqi Wang、…、Meng Wang

- 🎯 **研究动机**：持续视觉指令调优研究忽略带安全对齐的 MLLM，持续适配同时造成任务遗忘与安全退化
- 🔬 **研究方法**：HPA 后训练框架：按参数对安全或任务的聚焦程度划分参数，从均衡视角选择保留的聚焦参数，并对参数更新施加正交约束以缓解灾难遗忘
- 📌 **结论**：在 CVIT 基准与安全评测数据集上比现有基线更好维持高安全并缓解遗忘

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While continual visual instruction tuning (CVIT) has shown promise in adapting multimodal large language models (MLLMs), existing studies predominantly focus on models without safety alignment. This critical oversight ignores the fact that real-world MLLMs inherently require such mechanisms to mitigate potential risks. In this work, we shift our focus to CVIT for safety-aligned MLLMs and observe that during continual adaptation, the model not only suffers from task forgetting but also exhibits degradation in its safety. Achieving a harmonious balance between safety and task performance remains a crucial challenge. To address this, we propose Harmonious Parameter Adaptation (HPA), a post-training framework composed of focusing-based parameter partition, harmoniously balanced parameter selection, and orthogonal parameter adjustment. Specifically, HPA partitions parameters into two types based on their focus on safety or task performance, and selects the focused ones to preserve from a balanced perspective. In addition, HPA imposes orthogonality constraints on parameter updates to further alleviate catastrophic forgetting. Extensive experiments on the CVIT benchmark and safety evaluation datasets demonstrate that HPA better maintains high safety and mitigates forgetting than existing baselines. Code is available at https://github.com/Minato-Zackie/HPA.

</details>

### 15. DAVSP: Safety Alignment for Large Vision-Language Models via Deep Aligned Visual Safety Prompt

📄 [arXiv](https://arxiv.org/abs/2506.09353) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/41149)　📅 2025-06　🏷 AAAI 2026

**关键词**：`defense`、`visual safety prompt`、`deep alignment`、`parameter-efficient tuning`

👤 **作者**：Yitong Zhang、Jia Li、Liyi Cai、Ge Li

- 🎯 **研究动机**：既有 LVLM 对齐方法难以兼顾抵御恶意查询与保留良性输入效用
- 🔬 **研究方法**：提出 DAVSP：在输入图像周围附加可训练 padding 的视觉安全提示，并在激活空间监督实现深度对齐
- 📌 **结论**：两个代表性 LVLM、五个基准上有效抵抗恶意查询并保留良性效用，且具跨模型泛化能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Vision-Language Models (LVLMs) have achieved impressive progress across various applications but remain vulnerable to malicious queries that exploit the visual modality. Existing alignment approaches typically fail to resist malicious queries while preserving utility on benign ones effectively. To address these challenges, we propose Deep Aligned Visual Safety Prompt (DAVSP), which is built upon two key innovations. First, we introduce the Visual Safety Prompt, which appends a trainable padding region around the input image. It preserves visual features and expands the optimization space. Second, we propose Deep Alignment, a novel approach to train the visual safety prompt through supervision in the model's activation space. It enhances the inherent ability of LVLMs to perceive malicious queries, achieving deeper alignment than prior works. Extensive experiments across five benchmarks on two representative LVLMs demonstrate that DAVSP effectively resists malicious queries while preserving benign input utility. Furthermore, DAVSP exhibits great cross-model generation ability. Ablation studies further reveal that both the Visual Safety Prompt and Deep Alignment are essential components, jointly contributing to its overall effectiveness. The code is publicly available at https://github.com/zhangyitonggg/DAVSP.

</details>

### 16. Bootstrapping LLM Robustness for VLM Safety via Reducing the Pretraining Modality Gap

📄 [arXiv](https://arxiv.org/abs/2505.24208)　📅 2025-05

**关键词**：`defense`、`pretraining modality gap`、`robustness transfer`、`safety regularization`

👤 **作者**：Wenhan Yang、Spencer Stice、Ali Payani、Baharan Mirzasoleiman

- 🎯 **研究动机**：LVLM 相比 LLM 底座安全急剧退化，空白图亦可触发有害响应，模态间隙的影响未被量化
- 🔬 **研究方法**：证明模态间隙量与 VLM 安全高度负相关且由预训练引入、微调后持续存在，据此提出预训练时缩小间隙的正则化
- 📌 **结论**：LLaVA v1.5 等三个模型上不安全率最多降 16.3%，并可叠加提升既有防御 18.2%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring Vision-Language Models (VLMs) generate safe outputs is crucial for their reliable deployment. However, LVLMs suffer from drastic safety degradation compared to their LLM backbone. Even blank or irrelevant images can trigger LVLMs to generate harmful responses to prompts that would otherwise be refused in text-only contexts. The modality gap between image and text representations has been recently hypothesized to contribute to safety degradation of LVLMs. However, if and how the amount of modality gap affects LVLMs' safety is not studied. In this work, we show that the amount of modality gap is highly inversely correlated with VLMs' safety. Then, we show that this modality gap is introduced during pretraining LVLMs and persists through fine-tuning. Inspired by this observation, we propose a regularization to reduce the modality gap during pretraining. Our extensive experiments on LLaVA v1.5, ShareGPT4V, and MiniGPT-4 show that our method substantially improves safety alignment of LVLMs, reducing unsafe rate by up to 16.3% without compromising performance, and can further boost existing defenses by up to 18.2%.

</details>

### 17. Safety Mirage: How Spurious Correlations Undermine VLM Safety Fine-Tuning and Can Be Mitigated by Machine Unlearning

📄 [arXiv](https://arxiv.org/abs/2503.11832) · 📝 [OpenReview](https://openreview.net/forum?id=Qi1rZa4zzl) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10009564)　📅 2025-03　🏷 ICLR 2026

**关键词**：`defense`、`spurious correlation`、`machine unlearning`、`safety fine-tuning`

👤 **作者**：Yiwei Chen、Yuguang Yao、Yihua Zhang、Bingquan Shen、Gaowen Liu、Sijia Liu

- 🎯 **研究动机**：监督式安全微调让 VLM 学到表层文本模式与安全响应的虚假关联，一词替换即可绕过防护并造成过度拒答
- 🔬 **研究方法**：将该缺陷命名为 safety mirage，提出以 machine unlearning 替代监督微调，直接移除有害知识并保留通用能力
- 📌 **结论**：MU 对齐使攻击成功率最多降 60.27%，不必要拒绝减少超 84.20%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent vision language models (VLMs) have made remarkable strides in generative modeling with multimodal inputs, particularly text and images. However, their susceptibility to generating harmful content when exposed to unsafe queries raises critical safety concerns. While current alignment strategies primarily rely on supervised safety fine-tuning with curated datasets, we identify a fundamental limitation we call the ''safety mirage'', where supervised fine-tuning inadvertently reinforces spurious correlations between superficial textual patterns and safety responses, rather than fostering deep, intrinsic mitigation of harm. We show that these spurious correlations leave fine-tuned VLMs vulnerable even to a simple one-word modification-based attack, where substituting a single word in text queries with a spurious correlation-inducing alternative can effectively bypass safeguards. Additionally, these correlations contribute to the over-prudence, causing fine-tuned VLMs to refuse benign queries unnecessarily. To address these issues, we show machine unlearning (MU) as a powerful alternative to supervised safety fine-tuning, as it avoids biased feature-label mappings and directly removes harmful knowledge from VLMs while preserving their general capabilities. Extensive evaluations across safety benchmarks show that under MU-based alignment reduces the attack success rate by up to 60.27% and cuts unnecessary rejections by over 84.20%. WARNING: There exist AI generations that may be offensive in nature.

</details>

### 18. SEA: Low-Resource Safety Alignment for Multimodal Large Language Models via Synthetic Embeddings

📄 [arXiv](https://arxiv.org/abs/2502.12562) · 🎓 [Official](https://aclanthology.org/2025.acl-long.1212/)　📅 2025-02　🏷 ACL 2025

**关键词**：`defense`、`synthetic embedding`、`low-resource alignment`、`VA-SafetyBench`

👤 **作者**：Weikai Lu、Hao Peng、Huiping Zhuang、Cen Chen、Ziqian Zeng

- 🎯 **研究动机**：多模态安全对齐数据构造成本高，文本对齐难挡额外模态风险
- 🔬 **研究方法**：SEA 以梯度优化合成额外模态嵌入来扩展文本安全数据，仅有文本即可做多模态安全对齐；并提出 VA-SafetyBench
- 📌 **结论**：单张 RTX 3090 上 24 秒合成高质量嵌入，显著提升 image、video、audio MLLM 的安全性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) have serious security vulnerabilities.While safety alignment using multimodal datasets consisting of text and data of additional modalities can effectively enhance MLLM's security, it is costly to construct these datasets. Existing low-resource security alignment methods, including textual alignment, have been found to struggle with the security risks posed by additional modalities. To address this, we propose Synthetic Embedding augmented safety Alignment (SEA), which optimizes embeddings of additional modality through gradient updates to expand textual datasets. This enables multimodal safety alignment training even when only textual data is available. Extensive experiments on image, video, and audio-based MLLMs demonstrate that SEA can synthesize a high-quality embedding on a single RTX3090 GPU within 24 seconds. SEA significantly improves the security of MLLMs when faced with threats from additional modalities. To assess the security risks introduced by video and audio, we also introduced a new benchmark called VA-SafetyBench. High attack success rates across multiple MLLMs validate its challenge. Our code and data will be available at https://github.com/ZeroNLP/SEA.

</details>

### 19. Cross-Modal Safety Mechanism Transfer in Large Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2410.12662) · 📝 [OpenReview](https://openreview.net/forum?id=45rvZkJbuX)　📅 2024-10　🏷 ICLR 2025

**关键词**：`defense`、`safety mechanism transfer`、`text-guided alignment`、`visual hidden state`

👤 **作者**：Shicheng Xu、Liang Pang、Yunchang Zhu、Huawei Shen、Xueqi Cheng

- 🎯 **研究动机**：视觉输入无法触发语言模型既有安全机制
- 🔬 **研究方法**：以文本引导将有害图像hidden state对齐到等价有害文本表示
- 📌 **结论**：无需重建安全数据即把文本refusal机制迁移到视觉模态

### 20. SafeRI: Recognition and Intervention for Token-Level Safety Intervention in Large Vision Language Models

📄 [arXiv](https://arxiv.org/abs/2609.03544)　📅 2026-09

**关键词**：`defense`、`VLM guardrail`、`token-level risk`、`gated LoRA`、`VLM alignment`、`token risk`

👤 **作者**：Caoyuan Ma、…、Yinqiang Zheng

- 🎯 **研究动机**：VLM 安全对齐参数一经训练即全局常驻，对安全与已安全生成同时干预，扰动原有推理路径并损害多模态能力
- 🔬 **研究方法**：提出 SafeRI 流式识别加门控 LoRA：自回归生成中轻量识别器逐 token 判断前缀状态是否安全并更新下一步 LoRA 门，LoRA 由不安全前缀、过渡语句与安全延续训练，仅在激活后把生成导回安全响应
- 📌 **结论**：跨多个安全与通用基准验证按需干预在 post-alignment 设定下的有效性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing safety alignment methods for vision-language models usually modify the model behavior globally: once the safety parameters are trained or loaded, they participate in both unsafe and already-safe generations. This always-on intervention can unnecessarily perturb the model's original reasoning path and degrade general multimodal capabilities. We argue that safety alignment should be an on-demand intervention rather than a permanent modification to every decoding trajectory. To this end, we propose a streaming recognition and gated LoRA framework for intrinsic VLM safety. During autoregressive generation, a lightweight recognizer estimates whether the current pre-token generation state is safe or unsafe. Its output updates the LoRA gate for the following decoding step; otherwise, generation follows the frozen-backbone policy. The LoRA module is trained from unsafe prefixes, transition statements, and safe continuations, so that it learns to redirect unsafe generations back to safe responses after activation. Experiments across multiple safety and general-purpose benchmarks demonstrate the effectiveness of our method in post-alignment settings.

</details>

### 21. GGSS: Geodesic-Gated Spherical Steering for Inference-Time Debiasing of Generative Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2608.25375)　📅 2026-08

**关键词**：`defense`、`counterfactual bias subspace`、`spherical steering`、`adaptive token gate`、`generative VLM debiasing`、`geodesic steering`

👤 **作者**：Yiqun Sun、Junyu Chen、Pengfei Wei、Lawrence B. Hsieh

- 🎯 **研究动机**：推理时去偏方法面向静态嵌入或 CLIP，不适用于生成式 VLM
- 🔬 **研究方法**：GGSS 在超球面发现反事实偏见子空间，沿测地线引导视觉 token，自适应门聚焦强人口信号
- 📌 **结论**：四个 VLM 上平均偏见最低（三个显著），MMStar 保持基线 ±0.6 个百分点内

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative vision-language models (VLMs) are increasingly used in human-centered settings, yet they can produce demographically biased outputs even when images differ only in controlled attributes such as perceived race or gender. However, existing inference-time debiasers were largely designed for static embeddings or CLIP-like models rather than generative VLMs. We propose GGSS---Geodesic-Gated Spherical Steering---a norm-preserving intervention that discovers a counterfactual bias subspace on the unit hypersphere, steers visual tokens along geodesic arcs, and uses an adaptive gate to focus correction on tokens that carry stronger demographic signal. We evaluate four generative VLMs against ten adapted inference-time debiasing baselines and prompt-based mitigation under a single operating-point protocol across categorical, pairwise, and occupation-gender bias tests, while also measuring general visual-language capability. GGSS achieves the lowest average bias on all four models, significant on three of four backbones under paired permutation tests, while preserving MMStar accuracy within +/- 0.6 p.p. of the unsteered baseline. Code is available at https://github.com/dukesun99/GGSS.

</details>

### 22. Harnessing Textual Refusal Directions for Multimodal Safety

📄 [arXiv](https://arxiv.org/abs/2606.31876)　📅 2026-06

**关键词**：`defense`、`MARS`、`textual refusal direction`、`adaptive steering`

👤 **作者**：Moreno D'Incà、Nicu Sebe、Massimiliano Mancini

- 🎯 **研究动机**：MLLM 安全对齐或激活空间拒绝方向都需要难收集的多模态有害数据
- 🔬 **研究方法**：验证从 LLM backbone 提取的文本拒绝方向可跨模态泛化，提出 MARS：激活重定心修正模态错位、几何信任域内自适应调节转向强度并选最优干预层，在首生成 token 处操作
- 📌 **结论**：五个 SOTA MLLM 上安全、效用与视频越狱基准一致提升，免训练免多模态有害数据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

To improve safety in Large Language Models (LLMs) we can either perform post-training alignment or exploit refusal directions in the activation space. Both strategies are less feasible in Multimodal LLMs (MLLMs) as they require unsafe multimodal data, harder to collect than their unimodal counterpart. In this work, we relax this constraint and investigate whether textual refusal directions, extracted directly from the LLM backbone, generalize across modalities (i.e., image, video). Preliminary findings confirm this ability, though effectiveness is conditioned by layer selection, steering strength, and cross-modal alignment, with the latter causing safe multimodal inputs to be spuriously steered toward refusal. Building on this, we introduce Modality-Agnostic Refusal Steering (MARS), a light-weight training-free approach that injects multimodal safety without the need for multimodal safety data. MARS corrects modality misalignment via activation re-centering, adaptively scales steering strength within a geometrically defined trust region, and selects the optimal intervention layer, operating at the first generated token. Evaluated on five SOTA MLLMs across safety, utility, and video jailbreak benchmarks, MARS achieves consistent safety gains while preserving utility. These results reveal that safety-relevant structure is shared across modalities and that textual refusal directions are a powerful and underexplored foundation for multimodal alignment.

</details>

### 23. Dictionary-Aligned Concept Control for Safeguarding Multimodal LLMs

📄 [arXiv](https://arxiv.org/abs/2604.08846) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Luo_Dictionary-Aligned_Concept_Control_for_Safeguarding_Multimodal_LLMs_CVPR_2026_paper.html)　📅 2026-04　🏷 CVPR 2026

**关键词**：`defense`、`multimodal safety`、`concept dictionary`、`representation control`

👤 **作者**：Jinqi Luo、…、René Vidal

- 🎯 **研究动机**：MLLM 安全方法对演化恶意模式效果有限或算力昂贵；现有 activation steering 概念覆盖窄、难精确控制单概念
- 🔬 **研究方法**：DACO 从 40 万图文构建 1.5 万多模态概念字典（DACO-400K），经 SAE 稀疏编码干预激活并自动标注原子语义
- 📌 **结论**：在 QwenVL、LLaVA、InternVL 与 MM-SafetyBench、JailBreakV 上显著提升安全并保持通用能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) have been shown to be vulnerable to malicious queries that can elicit unsafe responses. Recent work uses prompt engineering, response classification, or finetuning to improve MLLM safety. Nevertheless, such approaches are often ineffective against evolving malicious patterns, may require rerunning the query, or demand heavy computational resources. Steering the activations of a frozen model at inference time has recently emerged as a flexible and effective solution. However, existing steering methods for MLLMs typically handle only a narrow set of safety-related concepts or struggle to adjust specific concepts without affecting others. To address these challenges, we introduce Dictionary-Aligned Concept Control (DACO), a framework that utilizes a curated concept dictionary and a Sparse Autoencoder (SAE) to provide granular control over MLLM activations. First, we curate a dictionary of 15,000 multimodal concepts by retrieving over 400,000 caption-image stimuli and summarizing their activations into concept directions. We name the dataset DACO-400K. Second, we show that the curated dictionary can be used to intervene activations via sparse coding. Third, we propose a new steering approach that uses our dictionary to initialize the training of an SAE and automatically annotate the semantics of the SAE atoms for safeguarding MLLMs. Experiments on multiple MLLMs (e.g., QwenVL, LLaVA, InternVL) across safety benchmarks (e.g., MM-SafetyBench, JailBreakV) show that DACO significantly improves MLLM safety while maintaining general-purpose capabilities.

</details>

### 24. Diagnosing and Repairing Unsafe Channels in Vision-Language Models via Causal Discovery and Dual-Modal Safety Subspace Projection

📄 [arXiv](https://arxiv.org/abs/2603.27240) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Fu_Diagnosing_and_Repairing_Unsafe_Channels_in_Vision-Language_Models_via_Causal_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`defense`、`causal mediation`、`dual-modal subspace`、`activation repair`、`unsafe channel`、`causal discovery`

👤 **作者**：Jinhu Fu、Yihang Lou、Qingyi Si、Shudong Zhang、Yan Bai、Sen Su

- 🎯 **研究动机**：LVLM 内部安全机制不透明且缺乏受控干预手段
- 🔬 **研究方法**：CARE 因果中介分析定位不安全行为的神经元与层，经广义特征分解学习视觉与文本双模态安全子空间，推理时以混合融合机制动态投影激活
- 📌 **结论**：显著增强安全鲁棒性而不损通用多模态能力，优于激活转向与对齐基线，并可防御未见攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Vision-Language Models (LVLMs) have achieved impressive performance across multimodal understanding and reasoning tasks, yet their internal safety mechanisms remain opaque and poorly controlled. In this work, we present a comprehensive framework for diagnosing and repairing unsafe channels within LVLMs (CARE). We first perform causal mediation analysis to identify neurons and layers that are causally responsible for unsafe behaviors. Based on these findings, we introduce a dual-modal safety subspace projection method that learns generalized safety subspaces for both visual and textual modalities through generalized eigen-decomposition between benign and malicious activations. During inference, activations are dynamically projected toward these safety subspaces via a hybrid fusion mechanism that adaptively balances visual and textual corrections, effectively suppressing unsafe features while preserving semantic fidelity. Extensive experiments on multiple safety benchmarks demonstrate that our causal-subspace repair framework significantly enhances safety robustness without degrading general multimodal capabilities, outperforming prior activation steering and alignment-based baselines. Additionally, our method exhibits good transferability, defending against unseen attacks.

</details>

### 25. Risk Awareness Injection: Calibrating Vision-Language Models for Safety without Compromising Utility

📄 [arXiv](https://arxiv.org/abs/2602.03402) · 📝 [OpenReview](https://openreview.net/forum?id=wqpQafNJTH) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60768)　📅 2026-02　🏷 ICML 2026

**关键词**：`defense`、`unsafe prototype subspace`、`visual token modulation`、`risk awareness`、`refusal calibration`、`empirical evaluation`

👤 **作者**：Mengxuan Wang、Yuxin Chen、Gang Xu、Tao He、Hongjie Jiang、Ming Li

- 🎯 **研究动机**：现有 VLM 防御依赖安全微调或激进 token 操作，成本高或损效用；视觉输入常稀释风险信号
- 🔬 **研究方法**：RAI 免训练轻量校准：从语言嵌入构建 Unsafe Prototype Subspace，对选定高风险视觉 token 做定向调制以显式激活安全关键信号，同时保持语义完整
- 📌 **结论**：多个越狱与效用基准上大幅降低 ASR 且不损任务性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision language models (VLMs) extend the reasoning capabilities of large language models (LLMs) to cross-modal settings, yet remain highly vulnerable to multimodal jailbreak attacks. Existing defenses predominantly rely on safety fine-tuning or aggressive token manipulations, incurring substantial training costs or significantly degrading utility. Recent research shows that LLMs inherently recognize unsafe content in text, and the incorporation of visual inputs in VLMs frequently dilutes risk-related signals. Motivated by this, we propose Risk Awareness Injection (RAI), a lightweight and training-free framework for safety calibration that restores LLM-like risk recognition by amplifying unsafe signals in VLMs. Specifically, RAI constructs an Unsafe Prototype Subspace from language embeddings and performs targeted modulation on selected high-risk visual tokens, explicitly activating safety-critical signals within the cross-modal feature space. This modulation restores the model's LLM-like ability to detect unsafe content from visual inputs, while preserving the semantic integrity of original tokens for cross-modal reasoning. Extensive experiments across multiple jailbreak and utility benchmarks demonstrate that RAI substantially reduces attack success rate without compromising task performance.

</details>

### 26. Security Tensors as a Cross-Modal Bridge: Extending Text-Aligned Safety to Vision in LVLM

📄 [arXiv](https://arxiv.org/abs/2507.20994)　📅 2025-07

**关键词**：`defense`、`security tensor`、`cross-modal bridge`、`parameter-free inference`

👤 **作者**：Shen Li、Liuyi Yao、Wujia Niu、Lan Zhang、Yaliang Li

- 🎯 **研究动机**：文本 LLM 的安全机制不能自然延伸到视觉模态，LVLM 对有害图像脆弱
- 🔬 **研究方法**：提出推理时注入的可训练 security tensors，以恶意图文对、对比良性对与一般良性样本优化，不改参数即桥接跨模态安全
- 📌 **结论**：文本与视觉两种 security tensor 均显著提升对有害视觉输入的拒绝且良性任务几乎无损，可激活语言模块的安全层

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large visual-language models (LVLMs) integrate aligned large language models (LLMs) with visual modules to process multimodal inputs. However, the safety mechanisms developed for text-based LLMs do not naturally extend to visual modalities, leaving LVLMs vulnerable to harmful image inputs. To address this cross-modal safety gap, we introduce security tensors - trainable input vectors applied during inference through either the textual or visual modality. These tensors transfer textual safety alignment to visual processing without modifying the model's parameters. They are optimized using a curated dataset containing (i) malicious image-text pairs requiring rejection, (ii) contrastive benign pairs with text structurally similar to malicious queries, with the purpose of being contrastive examples to guide visual reliance, and (iii) general benign samples preserving model functionality. Experimental results demonstrate that both textual and visual security tensors significantly enhance LVLMs' ability to reject diverse harmful visual inputs while maintaining near-identical performance on benign tasks. Further internal analysis towards hidden-layer representations reveals that security tensors successfully activate the language module's textual "safety layers" in visual inputs, thereby effectively extending text-based safety to the visual modality.

</details>

### 27. VLM-Guard: Safeguarding Vision-Language Models via Fulfilling Safety Alignment Gap

📄 [arXiv](https://arxiv.org/abs/2502.10486)　📅 2025-02

**关键词**：`defense`、`VLM-Guard`、`safety alignment gap`、`activation intervention`

👤 **作者**：Qin Liu、Fei Wang、Chaowei Xiao、Muhao Chen

- 🎯 **研究动机**：视觉模态接入削弱 LLM 的文本安全对齐，根因是模态鸿沟模糊了有害与无害查询的区分
- 🔬 **研究方法**：VLM-Guard 推理时把 VLM 表示投影到与安全对齐 LLM 提取的安全转向方向正交的子空间
- 📌 **结论**：三种恶意指令设定下有效弥合 VLM 与其 LLM 组件的安全差距

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The emergence of vision language models (VLMs) comes with increased safety concerns, as the incorporation of multiple modalities heightens vulnerability to attacks. Although VLMs can be built upon LLMs that have textual safety alignment, it is easily undermined when the vision modality is integrated. We attribute this safety challenge to the modality gap, a separation of image and text in the shared representation space, which blurs the distinction between harmful and harmless queries that is evident in LLMs but weakened in VLMs. To avoid safety decay and fulfill the safety alignment gap, we propose VLM-Guard, an inference-time intervention strategy that leverages the LLM component of a VLM as supervision for the safety alignment of the VLM. VLM-Guard projects the representations of VLM into the subspace that is orthogonal to the safety steering direction that is extracted from the safety-aligned LLM. Experimental results on three malicious instruction settings show the effectiveness of VLM-Guard in safeguarding VLM and fulfilling the safety alignment gap between VLM and its LLM component.

</details>

### 28. EviSafe: Evidence-Grounded Safety Evaluation for Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2608.23313)　📅 2026-08

**关键词**：`benchmark`、`multimodal guard`、`evidence-aware judge`、`counterfactual probe`、`multimodal evidence`、`counterfactual sensitivity`

👤 **作者**：Xuetong Li、Gaofeng Liu

- 🎯 **研究动机**：VLM 安全评测只看最终回应，无法判断模型是否因正确的多模态理由而安全——可能是关键词触发拒答、漏看视觉风险或良性敏感过度拒答
- 🔬 **研究方法**：EviSafe 联合评估自然行为、文本/视觉证据 grounding 与对安全关键证据反事实变化的敏感度；EviSafeBench 含 1,181 个 gold 图文场景与 2,452 个定向反事实变体（8 域、8 风险源），以三 probe 协议加证据感知 judge 评分
- 📌 **结论**：11 个 VLM 自然严重度准确率仅 27.6–52.8%，宽松诊断一致性 6.1–29.3%，unsafe→safe 反事实转变成功率 30.4–58.4%——多数模型并非因正确理由而安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language model safety benchmarks typically evaluate only final responses: whether a model refuses, warns, or complies. This outcome-level view cannot tell whether a model is safe for the right multimodal reason. Safelooking behavior may reflect keyword-triggered refusal, missed visual hazards, or over-refusal of benign-sensitive inputs. We introduce EviSafe, an evidence-grounded framework for VLM safety that jointly evaluates natural user-facing behavior, explicit grounding in textual and visual evidence, and behavioral sensitivity to counterfactual changes in safety-critical evidence. EviSafeBench instantiates the framework as a controlled benchmark with 1,181 gold image-text scenarios and 2,452 targeted counterfactual variants across eight safety domains and eight risk-source types. Each scenario includes a gold safety decision, evidence annotations, a safe-response policy, and counterfactual interventions. The three-probe protocol queries models with natural-response, evidencereporting, and counterfactual-response prompts, then scores them using an evidence-aware judge. Across eleven evaluated VLMs, natural severity accuracy ranges from 27.6% to 52.8%, relaxed diagnostic consistency from 6.1% to 29.3%, and unsafe-to-safe counterfactual transition success from 30.4% to 58.4%. These gaps show that the evaluated VLMs are not reliably safe for the right multimodal reason and motivate evaluation beyond refusal counts.

</details>

### 29. When Safety Overrides Vision: Exploring Dynamics between Vision Influence and Safety Alignment in Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2608.18628)　📅 2026-08

**关键词**：`analysis`、`safety-induced abstention`、`visual grounding`、`activation intervention`、`VLM refusal dynamics`、`late-layer representation`

👤 **作者**：Mehak Gupta、Tanmoy Chakraborty

- 🎯 **研究动机**：安全约束指令下 VLM 频繁弃答本可正确回答的问题——安全对齐压制感知接地本身还是仅重定向生成不明
- 🔬 **研究方法**：跨多架构与多模态基准分析弃答生成的解码动态，并做定向激活干预
- 📌 **结论**：弃答生成全程仍受视觉证据影响——感知接地基本保留；抑制拒答相关表征可免重训、不改视觉输入地恢复接地回答

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Aligned vision-language models (VLMs) are designed to balance grounded visual reasoning with safe generation behavior. However, we observe a striking phenomenon: under safety-constrained instruction, models frequently abstain from answering questions that remain correctly answerable under default instruction despite receiving identical image-question inputs. This raises a fundamental question: does safety alignment suppress perceptual grounding itself, or does visual evidence remain internally available while generation is redirected toward abstention? In this work, we investigate the internal decoding dynamics underlying safety-induced abstention in aligned VLMs. Across multiple architectures and multimodal benchmarks, we show that abstained generations remain consistently influenced by visual evidence throughout decoding, indicating that perceptual grounding is largely preserved despite refusal behavior. We further demonstrate that, although the representational organization of refusal differs substantially across architectures, safety-constrained instruction consistently alters late-stage hidden-state dynamics toward refusal-oriented decoding. Finally, through targeted activation-level interventions, we show that suppressing refusal-related representations reliably restores grounded answering behavior across models without retraining or modifying visual inputs. Together, these findings reveal a previously underexplored failure mode in aligned VLMs: safety alignment can override grounded visual expression even when perceptual evidence remains internally preserved.

</details>

### 30. SafeMT: Multi-turn Safety for Multimodal Language Models

🎓 [Official](https://aclanthology.org/2026.acl-long.1920/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`multimodal safety`、`VLM safety`、`multimodal alignment`、`safety alignment`、`fine-tuning robustness`

👤 **作者**：Han Zhu、…、Yike Guo

- 🎯 **研究动机**：多轮对话比单条提示风险更高，而现有基准未充分考虑多模态模型的多轮安全
- 🔬 **研究方法**：构建 SafeMT 基准：由有害查询加图像生成的多轮对话共 10,000 样本，覆盖 17 类场景与 4 种越狱方法，并提出 Safety Index 与对话安全调解器
- 📌 **结论**：对 17 个模型的评测显示攻击成功率随对话轮数上升；提出的调解器比现有 guard 模型更能降低多轮 ASR

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the widespread use of multi-modal Large Language models (MLLMs), safety issues have become a growing concern. Multi-turn dialogues, which are more common in everyday interactions, pose a greater risk than single prompts; however, existing benchmarks do not adequately consider this situation. To encourage the community to focus on the safety issues of these models in multi-turn dialogues, we introduce SafeMT, a benchmark that features dialogues of varying lengths generated from harmful queries accompanied by images. This benchmark consists of 10,000 samples in total, encompassing 17 different scenarios and four jailbreak methods. Additionally, we propose Safety Index (SI) to evaluate the general safety of MLLMs during conversations. We assess the safety of 17 models using this benchmark and discover that the risk of successful attacks on these models increases as the number of turns in harmful dialogues rises. This observation indicates that the safety mechanisms of these models are inadequate for recognizing the hazard in dialogue interactions. We propose a dialogue safety moderator capable of detecting malicious intent concealed within conversations and providing MLLMs with relevant safety policies. Experimental results from several open-source models indicate that this moderator is more effective in reducing multi-turn Attack Success Rate (ASR) compared to existed guard models.

</details>

### 31. ReFrame: Evidence-Guided Test-Time Safety Alignment in Multimodal Large Language Models

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

### 32. Understanding and Mitigating Token-Pruning-Induced Vulnerabilities in VLMs

🎓 [Official](https://icml.cc/virtual/2026/poster/65493)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`analysis`、`VLM safety`、`multimodal alignment`、`cross-modal generalization`、`refusal calibration`

👤 **作者**：Shuailong Wang、Xinyu Lyu、Shengming Yuan、Jingkuan Song、Heng Tao Shen、Lianli Gao

- 🎯 **研究动机**：Token-Pruning 的安全影响未被系统评估：多数剪枝策略随剪枝率上升显著降低 VLM 安全性
- 🔬 **研究方法**：揭示剪枝诱发恶意放大机制：背景 token 被移除后注意力坍缩到保留的恶意锚点；提出即插即用的 SAP，通过识别恶意锚点、恢复被剪良性 token 与重分配注意力对抗该效应
- 📌 **结论**：三个安全基准上攻击成功率至多降低 62%，且不牺牲效率与效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Token-Pruning accelerates Vision-Language Models by removing redundant visual tokens, yet its safety implications remain underexplored. In this work, we present the first comprehensive safety evaluation of Token-Pruning mechanisms and find that: most pruning strategies significantly degrade safety as pruning ratios increase, whereas Query-based Compression shows the opposite, with extreme pruning (up to 99.8%), unexpectedly improves model safety. This sharp contrast prompts a key question: How do different Token-Pruning strategies reshape model safety behavior, and is it possible to enhance safety without sacrificing acceleration? To answer this, we identify an unrecognized mechanism, termed Pruning-Induced Malicious Amplification, where removal of background tokens triggers a side effect: forcing the model's attention to collapse onto a few retained malicious anchors within the foreground, inadvertently amplifying their toxic semantics under jailbreak. To address that, we propose an inference-time and plug-and-play Safety-Aware Pruning (SAP) mechanism that counteracts such dominance via three steps: (1) identifying malicious anchors, (2) restoring pruned benign tokens, and (3) reallocating excessive attention from malicious anchors to benign tokens. Extensive experiments across three safety and four utility benchmarks demonstrate that SAP mitigates pruning-induced vulnerabilities, i.e., reducing ASR by up to 62%, without compromising efficiency or utility.

</details>

### 33. Attention Misses Visual Risk: Risk-Adaptive Steering for Multimodal Safety Alignment

📄 [arXiv](https://arxiv.org/abs/2510.13698) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4363)　📅 2025-10　🏷 ECCV 2026

**关键词**：`defense`、`safety alignment`、`VLM safety`、`multimodal alignment`、`multimodal jailbreak`、`risk awareness`

👤 **作者**：Jonghyun Park、Minhyuk Seo、Chaewon Yeo、Jonghyun Choi

- 🎯 **研究动机**：多模态越狱的重要成因是对安全关键图像区域的视觉注意不足，现有推理时防御泛化差且开销大
- 🔬 **研究方法**：MoRAS 用简洁视觉上下文增强安全关键视觉注意，据此进行风险自适应 steering 直接拒绝，仅需小规模校准集估计多模态风险
- 📌 **结论**：在多基准与 MLLM 骨干上持续缓解越狱、保持效用并降低计算开销

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Even modern AI models often remain vulnerable to multimodal queries in which harmful intent is embedded in images. A widely used approach for safety alignment is training with extensive multimodal safety datasets, but the costs of data curation and training are often prohibitive. To mitigate these costs, inference-time alignment has recently been explored, but they often lack generalizability across diverse multimodal jailbreaks and still incur notable overhead due to extra forward passes for response refinement or heavy pre-deployment calibration procedures. Here, we identify insufficient visual attention to safety-critical image regions as one of the key causes of multimodal safety failures. Building on this insight, we propose Multimodal Risk-Adaptive Steering (MoRAS), which enhances safety-critical visual attention via concise visual contexts for accurate multimodal risk assessment. This risk signal enables risk-adaptive steering for direct refusals, reducing inference overhead while remaining generalizable across diverse multimodal jailbreaks. Notably, MoRAS requires only a small calibration set to estimate multimodal risk, substantially reducing pre-deployment overhead. We conduct various empirical validations across multiple benchmarks and MLLM backbones, and observe that the proposed MoRAS consistently mitigates jailbreaks, preserves utility, and reduces computational overhead compared to state-of-the-art inference-time defenses.

</details>

### 34. When Seeing Overrides Knowing: Visual Dominance and Deferral-Based Method for Personalized Safety in VLMs

📄 [arXiv](https://arxiv.org/abs/2609.04281)　📅 2026-09

**关键词**：`defense`、`personalized VLM safety`、`deferral`、`visual dominance`

👤 **作者**：Edward Sun、…、Aylin Caliskan

- 🎯 **研究动机**：对特定用户安全而对一般用户合理的回答需要模型知道用户医疗、情绪与情境信息，VLM 常在信息缺失时仍直接作答
- 🔬 **研究方法**：构建 584 张真实图像、12 个高风险域、5,181 个配隐藏用户画像场景的 MPS-Bench；机制分析发现 visual dominance——视觉情感先在早期进入文本流再塑形决策；提出轻量输入监视器 PRISM 做跨模态调制预测何时应转交
- 📌 **结论**：八个 frontier VLM 直接作答率 86-99%、个性化安全不超 2.6/5；PRISM 达 0.978 AUC 并在全部模型上严格占优安全-效用 Pareto 前沿

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models (VLMs) are increasingly deployed in high-stakes settings, where a response that is reasonable in general may still be unsafe for a particular user whose medical, emotional, or situational context is unknown to the model. We study this problem of personalized safety in multimodal systems and introduce MPS-Bench, a benchmark of 5,181 scenarios from 584 real-world images across 12 high-risk domains, each paired with a hidden user profile. Evaluating eight frontier VLMs, we find that they almost always respond directly (86-99%) rather than seek missing context, and none exceeds 2.6/5 on personalized safety. To understand why these failures arise, we analyze multimodal interactions and identify visual dominance: visual information enters text representations early and suppresses textual risk signals during multimodal fusion. Causal interventions reveal a two-stage mechanism in which visual affect is first transferred into the text stream in early layers and then shapes the final decision through this altered text representation, making late-stage internal remediation unreliable. Motivated by this mechanism, we propose PRISM, a lightweight input monitor that uses bidirectional cross-modal modulation to predict when a query is likely to require deferral. PRISM achieves 0.978 AUC and strictly dominates the safety-utility Pareto frontier across all tested models.

</details>

### 35. FailSAE: Towards Interpretable Failure Prediction for Vision-Language Models via Sparse Autoencoders

📄 [arXiv](https://arxiv.org/abs/2609.04276)　📅 2026-09

**关键词**：`detection`、`VLM failure prediction`、`sparse autoencoder`、`runtime recovery`

👤 **作者**：Jie Ma、Zongxi Liu、Yi Zhu

- 🎯 **研究动机**：VLM 失效预测多依赖置信度或辅助分类器，缺乏可解释性，难以支撑高风险部署的人工介入
- 🔬 **研究方法**：提出 FailSAE：把失效预测形式化为稀疏 SAE 潜激活上的分类，三阶段 failure-aware 训练让潜方向保持可解释的同时更富含失效信息
- 📌 **结论**：失效预测超过所评基线；概念级分析显示失败时表征从类别特定概念转向歧义或风格概念，学到的潜方向还可支持运行时恢复

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models (VLMs), such as CLIP, have achieved strong performance across multimodal tasks by aligning visual and textual representations in a shared embedding space. As VLMs are increasingly used for high-stakes domains, failure prediction becomes critical for risk-aware deployment and human intervention. Existing failure prediction methods typically rely on confidence scores or auxiliary classifiers. Although these methods are effective on predicting VLM failures, they provide limited interpretability. In this work, we investigate the use of Sparse Autoencoders (SAEs) for interpretable failure prediction in VLMs. We formulate failure prediction as a classification task over sparse SAE latent activations and introduce a three-stage failure-aware training pipeline that encourages the learned latent directions to remain interpretable while becoming more informative for failure prediction. Our experiments show that the resulting framework outperforms the evaluated baselines in failure prediction. Further analysis suggests that failure-aware training encourages SAE latent directions to capture more class-specific concepts. We also use the SAE to provide a concept-level analysis of how model representations change during failures, revealing a shift from class-specific concepts toward more ambiguous or style-related concepts. Finally, we explore how the learned SAE latent directions can support runtime failure recovery.

</details>

### 36. Knowing What Not to Answer: Selective Non-Compliance in Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2609.04720)　📅 2026-09

**关键词**：`benchmark`、`VLM selective non-compliance`、`compound queries`、`safety abstention`

👤 **作者**：Minji Kim、Jihyoung Jang、Hyounghun Kim

- 🎯 **研究动机**：现有基准只在整条查询级评 non-compliance，而真实查询常混合可答内容与应拒绝成分，需要选择性不合规
- 🔬 **研究方法**：构建 KoNA 基准：覆盖 False Premise、Visual Inaccessibility、Universal Unknown、Task Feasibility 与 Safety 五类，以配对单条与复合查询同时测查询级与组件级不合规，并用其微调 VLM
- 📌 **结论**：各 VLM 常不能恰当拒绝、纠正或弃权，复合查询下失败更明显；微调后不合规准确率大幅提升且基本保持全可答任务性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models (VLMs) are expected to respond helpfully to appropriate requests while withholding compliance with requests that are incorrect, unsafe, infeasible, or unanswerable. However, existing benchmarks predominantly evaluate non-compliance at the level of the query as a whole, assuming that each request either warrants compliance or requires withholding compliance. In practice, real-world queries can contain a mixture of answerable content and components for which compliance should be withheld. In this paper, we introduce KoNA, a benchmark for evaluating selective non-compliance in VLMs across five categories: False Premise, Visual Inaccessibility, Universal Unknown, Task Feasibility, and Safety. Each task evaluates two capabilities: query-level non-compliance and component-level non-compliance under paired single and compound queries. Our evaluation across diverse VLMs shows that models often fail to refuse, correct, or abstain appropriately, and these failures become more pronounced when queries require selective non-compliance. To address this challenge, we fine-tune VLMs using KoNA examples that require selective non-compliance, together with a fully answerable set that should receive direct answers. Our fine-tuned models achieve substantial improvements in non-compliance accuracy while largely maintaining performance on fully answerable tasks. These results suggest that the fine-tuned models can distinguish between answerable components and those requiring non-compliance and respond in a task-appropriate manner.

</details>

### 37. SPARK: Representation-Level KV Memory Alignment for Safer Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2609.14258)　📅 2026-09

**关键词**：`defense`、`VLM safety`、`KV memory repair`、`multimodal jailbreak`、`representation intervention`

👤 **作者**：Mohd Azfar、Izhar Dad Khan

- 🎯 **研究动机**：VLM 仍易受把有害意图分布到文本与图像的 jailbreak 攻击，使单模态安全机制不足
- 🔬 **研究方法**：SPARK 两阶段框架：Stage 1 用一次性 diagnostic adapter 识别多模态 key/value 表示中的 harm-associated 方向；Stage 2 投影掉这些方向、学习轻量 residual repair、用图像结构先验锚定修复后的 key，按 head-wise 系数混合修复与原始 memory，推理时无需显式 harm classifier
- 📌 **结论**：在 LLaVA-OneVision-7B、Chameleon-7B、Qwen2-VL-7B、InternVL2-4B 上减少多模态攻击成功同时保持通用能力；LLaVA-OneVision-7B 上 image-only jailbreak ASR 降至 4.7%，MMMU 保持 47.8（未防御 48.4），MM-SafetyBench ASR 从 39.2% 降至 12.4%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models (VLMs) remain vulnerable to jailbreaks that distribute harmful intent across text and images, making unimodal safety mechanisms insufficient. We investigate whether this vulnerability can be mitigated directly in the multimodal key-value (KV) memory formed during prefill, without modifying model parameters at inference time. We introduce SPARK, a two-stage framework for targeted KV-memory repair. Stage 1 uses a disposable diagnostic adapter to identify harm-associated directions in multimodal key and value representations. Stage 2 projects out these directions, learns a lightweight residual repair, and anchors repaired keys with an image-structural prior to preserve visual grounding. Rather than applying the intervention uniformly, SPARK mixes repaired and original memory using a head-wise coefficient g_h* determined by intervention-relevant subspace energy E_h, requiring no explicit harm classifier at inference. Across LLaVA-OneVision-7B, Chameleon-7B, Qwen2-VL-7B, and InternVL2-4B, SPARK reduces multimodal attack success while preserving general capability. On LLaVA-OneVision-7B, image-only jailbreak attack success falls to 4.7%, while MMMU remains within 0.6 points of the undefended model (47.8 vs. 48.4) with near-baseline language quality. On MM-SafetyBench, attack success decreases from 39.2% to 12.4%. Even under white-box adaptive joint prompt-image attacks, attack success is limited to 20.3%, compared with 54.6% for the undefended model. These results suggest that multimodal jailbreak behavior can be substantially mitigated by selectively repairing intervention-relevant KV subspaces at prefill, particularly when harmful evidence is carried by the visual modality.

</details>

### 38. What Do Hallucinations Reveal About Multimodal Reasoning? Diagnosing Visual Grounding Failures via Contrastive Decoding Probes

📄 [arXiv](https://arxiv.org/abs/2609.16646) · 🐙 [Code](https://github.com/zhaozhipeng1997/SAFE_public.)　📅 2026-09

**关键词**：`detection`、`visual hallucination`、`contrastive decoding`、`grounding score`、`LVLM`

👤 **作者**：Zhipeng Zhao、Wenxu Wang、Peishun Liu、Ruichun Tang

- 🎯 **研究动机**：强多模态模型时代需要超越基准分数的方法论——把 LVLM 自身当实验仪器研究其失效动力学
- 🔬 **研究方法**：SAFE 免训练解码框架：对比视觉接地与视觉消融两条生成路径，产生 token 级对比接地分数，识别模型偏向语言先验胜过视觉证据的时刻；该信号兼作未接地 token 检测代理与解码期惩罚基础
- 📌 **结论**：三条经验发现：视觉依赖随生成衰减、幻觉在时间上聚集、早期干预减少聚集且不显著损害流畅度；MMHalBench 上大幅超过全部对比基线（其他基准表现混合）。EMNLP 2026

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When strong multimodal models are widely available, progress requires new scientific methodologies beyond benchmark scores---using models as instruments for understanding behavior. We address this by asking: can we use large vision-language models (LVLMs) as experimental instruments for studying their own failure dynamics? Focusing on visual hallucination, we introduce SAFE, a training-free decoding framework that contrasts visually-grounded and vision-ablated generation paths to produce a token-level contrastive grounding score that identifies when the model favors linguistic priors over visual evidence. This signal serves dual roles: as a practical proxy for detecting visually-ungrounded tokens, and as the basis for decoding-time penalties. Our analysis yields three empirical observations: visual dependency decays over generation, hallucinations co-occur in temporal clusters, and early intervention reduces clustering without substantially degrading fluency. On MMHalBench, SAFE substantially outperforms all compared baselines; results elsewhere are more mixed. We argue that designing contrastive probes exemplifies a broader mission: using models as instruments for scientific understanding. Code: https://github.com/zhaozhipeng1997/SAFE_public.

</details>

### 39. Seeing Through Conflicts: Improving Instruction Hierarchy Alignment in Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2609.22234)　📅 2026-09

**关键词**：`defense`、`instruction hierarchy`、`VLM`、`mixed-modality training`、`RLHF transfer`

👤 **作者**：Nicholas Sansoterra、Zishuo Zheng、Sachin Kumar

- 🎯 **研究动机**：指令层级（IH）对齐研究集中在纯文本；VLM 中指令可嵌在图像、跨模态拆分、视觉变换或在 agent 任务中出现——多模态 IH 未被训练
- 🔬 **研究方法**：把多模态 IH 对齐当推理问题：用规则奖励 RL 训练 VLM，比较纯文本、纯图像、混合模态监督
- 📌 **结论**：纯文本 IH 训练只部分迁移到多模态攻击（需解码/重建/跨模态推理时失效）；图像训练超纯文本、混合模态最优——多模态指令层级的系统化训练路线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Instruction hierarchy (IH) alignment teaches language models to prioritize higher-level instructions when inputs conflict. While studied primarily in text-only settings, vision-language models (VLMs) introduce new challenges for IH: instructions may be embedded in images, split across modalities, visually transformed, or encountered during agentic tasks. Positing multimodal IH alignment as a reasoning problem, we train VLMs using reinforcement learning with rule-based rewards, comparing text-only, image-only, and mixed-modality supervision. We find that text-only IH training partially transfers to multimodal attacks, failing when models must decode, reconstruct, or reason over instructions across modalities. Image-based training improves robustness beyond text-only supervision, while mixed-modality training performs best overall. Importantly, the benefits generalize beyond the synthetic typographic training setting to real-image and web-agent safety tasks, while largely preserving general multimodal capability, showing that lightweight, verifiable supervision can meaningfully improve VLM robustness under adversarial, cross-modal, and interactive instruction conflicts.

</details>

### 40. The Uncontrolled Variable: Vision-Language Model Refusal Responds to Image Presence in Ways Risk Cannot Explain

📄 [arXiv](https://arxiv.org/abs/2609.26174)　📅 2026-09

**关键词**：`analysis`、`VLM refusal`、`image presence`、`form-based refusal`、`uncontrolled variable`

👤 **作者**：Haoyu Zhang、…、Shanu Sushmita

- 🎯 **研究动机**：VLM 安全应取决于请求问什么——实测安全对齐 VLM 还对请求形式的一个属性（是否附带图像）敏感：固定请求内容，附一张空白画布即移动拒答数十个百分点
- 🔬 **研究方法**：控制请求内容不变，仅变化是否附带空白画布（不可读、无关、跨 prompt 相同）；中性指令几乎不受影响、风险相关指令大幅移动
- 📌 **结论**：拒答被图像存在性本身驱动而非风险内容——VLM 安全评测的未控变量（形式驱动拒答的又一证据）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Model (VLM) safety is expected to depend on what a request asks for. We show that safety-aligned VLMs also key refusal on a property of a request's form: whether an image is attached, holding everything the request asks fixed. Attaching a blank canvas - unreadable, unrelated to the request, identical across prompts - shifts refusal by tens of percentage points, with no defense in the loop. The shift is not blanket caution. Neutral instructions are almost unaffected while borderline-benign prompts move sharply, so the cost falls on sensitivity-adjacent traffic: benign questions about privacy, self-harm and violence. Attachment alone is sufficient, while the image's properties set the price: a black canvas costs substantially more than a white one of identical size, and on an open checkpoint the carrying axis is pixel count. Nor is the shift under instructional control - telling the model the image is a placeholder to be disregarded removes only a fraction of it, and on one model asserting that an attachment exists moves refusal substantially with nothing attached. Attachment may correlate with risk in deployment; what these models do with it does not track risk. It is not the serving stack, since the same weights reached two ways behave alike, nor a property of VLMs as such, since several open-weight checkpoints show nothing. It belongs to particular aligned checkpoints, one of them open. It is also decoupled from what it buys: the canvas does prevent some attack success on a matched harmful set, but far less than it costs, and its sign is not fixed - on one open model the identical canvas makes the model markedly easier to attack. Image presence is not a default a deployer chose or priced; it is an uncontrolled variable inherited with the weights.

</details>

### 41. GHOST-Q: Towards Studying Grounding Hallucinations Overlooked Under Same-score TradeOffs in Quantized VLMS

📄 [arXiv](https://arxiv.org/abs/2609.29999)　📅 2026-09

**关键词**：`analysis`、`quantized VLM grounding`、`same-score tradeoff`、`item-level pairing`、`compression redistribution`

👤 **作者**：Saim Rehman、Muhammad Shafique

- 🎯 **研究动机**：VLM 后训练量化以聚合任务精度与内存节省评估——保住头名分数不保证保住视觉接地行为：量化部署失效线的接地维度
- 🔬 **研究方法**：GHOST-Q：三 8B VLM 族 FP16/INT8/NF4 的跨精度受控评测——逐项配对 FP16 与量化预测量化压缩如何重分布接地成败
- 📌 **结论**：六个量化变体中五个在接地敏感基准重分布成败——同分不同行为的量化失效（量化部署失效谱再+1）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Post-training quantization of vision--language models (VLMs) is typically assessed through aggregate task accuracy and memory savings, but preserving a headline score does not guarantee preservation of visual grounding behavior. We present GHOST-Q, a cross-precision controlled evaluation of three 8B VLM families under FP16, INT8, and NF4 across utility and hallucination-sensitive benchmarks. Rather than comparing only aggregate accuracy, we pair FP16 and quantized predictions item by-item to quantify how compression redistributes grounding successes and failures. Five of six quantized variants preserve MMStar accuracy within $\pm2$ percentage points, yet 10 of 36 paired effects remain significant after false-discovery-rate correction, nine on hallucination-sensitive conditions. Same-device A100 profiling further demonstrates that substantial memory reduction does not necessarily mean lower inference latency. Finally, an open-ended AMBER audit reveals strong generation budget censoring whose severity varies by architecture and precision. These results show that quantized VLMs should be evaluated jointly for aggregate utility, grounding reliability, generation behavior, and realized deployment efficiency.

</details>
