# 多模态与具身模型 DoS

## 研究方向

多模态与具身模型 DoS 研究不同输入模态如何形成专属可用性攻击面：2D 图像与 3D 点云可通过细微扰动诱发冗长生成，视频模型可被跨帧通用触发器拖慢，VLA 和机器人则可能被视觉或音频信号冻结动作。这里同时关注计算资源放大与物理任务停滞，因为具身系统即使没有大量消耗 token，也可能出现实际意义上的拒绝服务。

## 研究脉络

- **视觉输入攻击：** 多模态 DoS 最初利用图像诱导 verbose generation，放大 token、延迟或能耗。
- **模态扩展：** 攻击随后覆盖视频、3D 几何和语言状态循环，利用不同感知输入延长模型处理过程。
- **具身后果：** 在 embodied model 中，目标进一步变为冻结动作或触发安全停机，攻击后果从计算开销延伸到物理任务不可用。

## 视觉、视频与 3D 模型攻击

### 1. The Boy Who Cried Wolf: Adversarial Misclassification of Safe Inputs as Unsafe in Multimodal Guardrails

📄 [arXiv](https://arxiv.org/abs/2608.01373) · 🌐 [Project](https://doi.org/10.1145/3770855.3817756)　📅 2026-08　🏷 KDD 2026

**关键词**：`attack`、`multimodal adversarial example`、`unsafe induction`、`guardrail evasion`、`multimodal guardrail`、`over-refusal`

👤 **作者**：Shuo Shi、…、Shouling Ji

- 🎯 **研究动机**：多模态 guard 对抗研究集中于假阴性越狱，诱导假阳性使良性请求被拒的可用性威胁未被探索
- 🔬 **研究方法**：提出 Unsafe Induction Attacks，其 USD 方法把对抗扰动与不安全内容的分布表征对齐，使安全图像在多样用户 prompt 下触发 guard 拒绝合法请求
- 📌 **结论**：在四个 SOTA guard 模型的真实用户模拟场景中 USD 攻击成功率达 84%，超过现有方法，暴露多模态安全架构的可用性失败模式

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal guard models have emerged as critical safety components for screening content in vision-language systems. While adversarial research has extensively studied jailbreaking attacks that produce false negatives, the inverse threat of inducing false positives on benign inputs remains unexplored. We introduce Unsafe Induction Attacks, where adversaries distribute imperceptibly perturbed safe images that trigger guard models to reject legitimate user requests, causing a "Boy Who Cried Wolf" effect that degrades service availability and erodes trust. This reveals an availability failure mode in deployed safety filters. To realize this threat under diverse user prompts, we propose Unsafe Semantic Distillation (USD), which aligns adversarial perturbations with distributional representations of unsafe content rather than prompt-specific instances. Evaluated on four state-of-the-art guard models across realistic user simulation scenarios, USD achieves 84% attack success rates, outperforming existing methods and exposing fundamental vulnerabilities in current multimodal safety architectures.

</details>

### 2. Infinite Babble: Inflating 3D Vision-Language Model Inference Overhead via Adversarial Geometric Perturbation

🎓 [Official](https://aclanthology.org/2026.findings-acl.259/)　📅 2026-07　🏷 ACL 2026

**关键词**：`attack`、`3D-VLM DoS`、`geometric perturbation`、`EOS suppression`

👤 **作者**：Shuoyang Sun、…、Shu-Tao Xia

- 🎯 **研究动机**：3D-VLM 自回归解码引入推理效率漏洞，其对不可信 3D 资产的敏感性未被利用
- 🔬 **研究方法**：Inflate3D 注入不可感知噪声：语义感知扰动关键区域保持几何结构，并操纵 token 概率抑制 EOS 发射延长解码
- 📌 **结论**：输出长度与能耗最多放大 6.45 倍，可耗尽系统资源

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

3D Vision-Language Models (3D-VLMs) have emerged as the critical cognitive backbone for spatial intelligence, enabling precise reasoning over unstructured 3D data. While these models serve as the foundation for downstream robotics and embodied systems, their reliance on autoregressive decoding introduces a fundamental vulnerability regarding inference efficiency. In this work, we present Inflate3D, a novel adversarial framework designed to trigger computational and economic exhaustion in 3D-VLMs. Specifically, we exploit the model’s sensitivity to untrusted 3D assets to hijack the generation process. Inflate3D operates by injecting imperceptible noise that forces the model into a state of pathological verbosity, effectively stalling the inference pipeline. Our approach comprises two synergistic strategies: (1) a semantic-aware adversarial manipulation that leverages internal representations to selectively perturb semantically critical regions while preserving geometric structure, and (2) a trajectory disruption mechanism that manipulates token probabilities to suppress End-of-Sequence (EOS) emission, thereby prolonging decoding and inducing verbose outputs. Experiments on standard benchmarks show that Inflate3D amplifies output length and energy consumption by up to 6.45×, demonstrating a potent capability to drain system resources. These findings expose a critical blind spot in multimodal alignment, highlighting the urgent need to secure spatial foundation models against resource exhaustion attacks.

</details>

### 3. VidDoS: Universal Denial-of-Service Attack on Video-based Large Language Models

📄 [arXiv](https://arxiv.org/abs/2603.01454)　📅 2026-03

**关键词**：`attack`、`Video-LLM DoS`、`universal trigger`、`cross-frame attack`

👤 **作者**：Duoxun Tang、Dasen Dai、Jiyao Wang、Xiao Yang、Jianyu Wang、Siqi Cai

- 🎯 **研究动机**：图像级能量延迟攻击被时序聚合机制稀释，实时视频流又使逐样本优化不可行
- 🔬 **研究方法**：VidDoS 用 masked teacher forcing 引导模型生成昂贵目标序列，配合拒绝惩罚与提前终止抑制压倒简洁先验，学习实例无关的通用触发器
- 📌 **结论**：三个 Video-LLM 上 token 膨胀超 205 倍、延迟增超 15 倍，实时自动驾驶流模拟中出现关键安全违规

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Video-LLMs are increasingly deployed in safety-critical applications but are vulnerable to Energy-Latency Attacks (ELAs) that exhaust computational resources. Current image-centric methods fail because temporal aggregation mechanisms dilute individual frame perturbations. Additionally, real-time demands make instance-wise optimization impractical for continuous video streams. We introduce VidDoS, which is the first universal ELA framework tailored for Video-LLMs. Our method leverages universal optimization to create instance-agnostic triggers that require no inference-time gradient calculation. We achieve this through $\textit{masked teacher forcing}$ to steer models toward expensive target sequences, combined with a $\textit{refusal penalty}$ and $\textit{early-termination suppression}$ to override conciseness priors. Testing across three mainstream Video-LLMs and three video datasets, which include video question answering and autonomous driving scenarios, shows extreme degradation. VidDoS induces a token expansion of more than 205$\times$ and inflates the inference latency by more than 15$\times$ relative to clean baselines. Simulations of real-time autonomous driving streams further reveal that this induced latency leads to critical safety violations. We urge the community to recognize and mitigate these high-hazard ELA in Video-LLMs.

</details>

### 4. An Image Is Worth Ten Thousand Words: Verbose-Text Induction Attacks on VLMs

📄 [arXiv](https://arxiv.org/abs/2511.16163)　📅 2025-11

**关键词**：`attack`、`VLM DoS`、`2D VLM`、`visual perturbation`

👤 **作者**：Zhi Luo、Zenghui Yuan、Wenqi Wei、Daizong Liu、Pan Zhou

- 🎯 **研究动机**：既有 VLM 冗长输出攻击只延迟 EOS，未把最大化输出 token 长度作为显式优化目标，稳定性与可控性不足
- 🔬 **研究方法**：VTIA 两阶段框架：先用强化学习搜索能诱发冗长输出的对抗 prompt 嵌入，再优化图像扰动使其视觉嵌入逼近对抗 prompt，构造触发冗长文本的恶意图像
- 📌 **结论**：在四个主流 VLM 上有效性、效率与泛化能力均显著占优

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the remarkable success of Vision-Language Models (VLMs) on multimodal tasks, concerns regarding their deployment efficiency have become increasingly prominent. In particular, the number of tokens consumed during the generation process has emerged as a key evaluation metric.Prior studies have shown that specific inputs can induce VLMs to generate lengthy outputs with low information density, which significantly increases energy consumption, latency, and token costs. However, existing methods simply delay the occurrence of the EOS token to implicitly prolong output, and fail to directly maximize the output token length as an explicit optimization objective, lacking stability and controllability.To address these limitations, this paper proposes a novel verbose-text induction attack (VTIA) to inject imperceptible adversarial perturbations into benign images via a two-stage framework, which identifies the most malicious prompt embeddings for optimizing and maximizing the output token of the perturbed images.Specifically, we first perform adversarial prompt search, employing reinforcement learning strategies to automatically identify adversarial prompts capable of inducing the LLM component within VLMs to produce verbose outputs. We then conduct vision-aligned perturbation optimization to craft adversarial examples on input images, maximizing the similarity between the perturbed image's visual embeddings and those of the adversarial prompt, thereby constructing malicious images that trigger verbose text generation. Comprehensive experiments on four popular VLMs demonstrate that our method achieves significant advantages in terms of effectiveness, efficiency, and generalization capability.

</details>

### 5. RemedyGS: Defend 3D Gaussian Splatting Against Computation Cost Attacks

📄 [arXiv](https://arxiv.org/abs/2511.22147) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_RemedyGS_Defend_3D_Gaussian_Splatting_Against_Computation_Cost_Attacks_CVPR_2026_paper.html)　📅 2025-11　🏷 CVPR 2026

**关键词**：`defense`、`3D Gaussian splatting`、`resource exhaustion`、`availability`

👤 **作者**：Yanping Li、Zhening Liu、Zijian Li、Zehong Lin、Jun Zhang

- 🎯 **研究动机**：3DGS 面临计算成本攻击导致资源恶意占用甚至 DoS，缺乏有效防御
- 🔬 **研究方法**：RemedyGS 黑盒防御框架：检测器识别带毒纹理的输入图像，净化器从被攻击图像恢复良性图像，并在净化器中引入对抗训练强化分布对齐
- 📌 **结论**：在白盒、黑盒与自适应攻击下均有效，安全性与效用均达 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As a mainstream technique for 3D reconstruction, 3D Gaussian splatting (3DGS) has been applied in a wide range of applications and services. Recent studies have revealed critical vulnerabilities in this pipeline and introduced computation cost attacks that lead to malicious resource occupancies and even denial-of-service (DoS) conditions, thereby hindering the reliable deployment of 3DGS. In this paper, we propose the first effective and comprehensive black-box defense framework, named RemedyGS, against such computation cost attacks, safeguarding 3DGS reconstruction systems and services. Our pipeline comprises two key components: a detector to identify the attacked input images with poisoned textures and a purifier to recover the benign images from their attacked counterparts, mitigating the adverse effects of these attacks. Moreover, we incorporate adversarial training into the purifier to enforce distributional alignment between the recovered and original natural images, thereby enhancing the defense efficacy. Experimental results demonstrate that our framework effectively defends against white-box, black-box, and adaptive attacks in 3DGS systems, achieving state-of-the-art performance in both safety and utility.

</details>

### 6. LingoLoop Attack: Trapping MLLMs via Linguistic Context and State Entrapment into Endless Loops

📄 [arXiv](https://arxiv.org/abs/2506.14493) · 📝 [OpenReview](https://openreview.net/forum?id=kxEM2vc7ne) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10007735)　📅 2025-06　🏷 ICLR 2026

**关键词**：`attack`、`MLLM DoS`、`part-of-speech optimization`、`state trapping`

👤 **作者**：Jiyuan Fu、…、Wenqiang Zhang

- 🎯 **研究动机**：既有能量-延迟攻击忽视 token 词性与句式结构对 EOS 生成与输出数量的影响
- 🔬 **研究方法**：提出 LingoLoop：POS-Aware Delay Mechanism 按词性调整注意力推迟 EOS，Generative Path Pruning 限制隐状态幅值诱导重复循环
- 📌 **结论**：Qwen2.5-VL-3B 等被诱发生成至极限，放宽限制后 token 数达干净输入的 367 倍，能耗随之激增

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) have shown great promise but require substantial computational resources during inference. Attackers can exploit this by inducing excessive output, leading to resource exhaustion and service degradation. Prior energy-latency attacks aim to increase generation time by broadly shifting the output token distribution away from the EOS token, but they neglect the influence of token-level Part-of-Speech (POS) characteristics on EOS and sentence-level structural patterns on output counts, limiting their efficacy. To address this, we propose LingoLoop, an attack designed to induce MLLMs to generate excessively verbose and repetitive sequences. First, we find that the POS tag of a token strongly affects the likelihood of generating an EOS token. Based on this insight, we propose a POS-Aware Delay Mechanism to postpone EOS token generation by adjusting attention weights guided by POS information. Second, we identify that constraining output diversity to induce repetitive loops is effective for sustained generation. We introduce a Generative Path Pruning Mechanism that limits the magnitude of hidden states, encouraging the model to produce persistent loops. Extensive experiments on models like Qwen2.5-VL-3B demonstrate LingoLoop's powerful ability to trap them in generative loops; it consistently drives them to their generation limits and, when those limits are relaxed, can induce outputs with up to 367x more tokens than clean inputs, triggering a commensurate surge in energy consumption. These findings expose significant MLLMs' vulnerabilities, posing challenges for their reliable deployment.

</details>

### 7. Inducing High Energy-Latency of Large Vision-Language Models with Verbose Images

📄 [arXiv](https://arxiv.org/abs/2401.11170) · 🎓 [Official](https://proceedings.iclr.cc/paper_files/paper/2024/hash/4a6a5e2e8a27262501bda3463fcf7b21-Abstract-Conference.html)　📅 2024-01　🏷 ICLR 2024

**关键词**：`attack`、`VLM DoS`、`2D VLM`、`verbose image`

👤 **作者**：Kuofeng Gao、…、Wei Liu

- 🎯 **研究动机**：VLM 推理能耗与延迟构成可用性攻击面，此前无人探索
- 🔬 **研究方法**：构造不可感知扰动最大化生成长度：延迟 EOS token、提高 token 不确定性与序列多样性，并以时变权重平衡
- 📌 **结论**：MS-COCO 与 ImageNet 上生成序列长度分别放大约 7.87 倍与 8.56 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large vision-language models (VLMs) such as GPT-4 have achieved exceptional performance across various multi-modal tasks. However, the deployment of VLMs necessitates substantial energy consumption and computational resources. Once attackers maliciously induce high energy consumption and latency time (energy-latency cost) during inference of VLMs, it will exhaust computational resources. In this paper, we explore this attack surface about availability of VLMs and aim to induce high energy-latency cost during inference of VLMs. We find that high energy-latency cost during inference of VLMs can be manipulated by maximizing the length of generated sequences. To this end, we propose verbose images, with the goal of crafting an imperceptible perturbation to induce VLMs to generate long sentences during inference. Concretely, we design three loss objectives. First, a loss is proposed to delay the occurrence of end-of-sequence (EOS) token, where EOS token is a signal for VLMs to stop generating further tokens. Moreover, an uncertainty loss and a token diversity loss are proposed to increase the uncertainty over each generated token and the diversity among all tokens of the whole generated sequence, respectively, which can break output dependency at token-level and sequence-level. Furthermore, a temporal weight adjustment algorithm is proposed, which can effectively balance these losses. Extensive experiments demonstrate that our verbose images can increase the length of generated sequences by 7.87 times and 8.56 times compared to original images on MS-COCO and ImageNet datasets, which presents potential challenges for various applications. Our code is available at https://github.com/KuofengGao/Verbose_Images.

</details>

### 8. Semantic Denial of Service in LLM-controlled robots

📄 [arXiv](https://arxiv.org/abs/2604.24790)　📅 2026-04

**关键词**：`attack`、`robot-agent DoS`、`robotics`、`audio injection`

👤 **作者**：Jonathan Steinberg、Oren Gal

- 🎯 **研究动机**：机器人的安全指令跟随本身构成可用性攻击面——未认证音频文本被直接送入 LLM 决策
- 🔬 **研究方法**：在音频通道注入 1-5 个安全合理 token 触发安全推理停机，跨 4 个 VLM、7 种 prompt 防御、3 种部署模式评估
- 📌 **结论**：prompt 级防御只能把硬停机转化为 acknowledge loop 与假警报（以 DSR 度量）；注入多样化比重复更有效，需架构上分离安全监控与动作选择

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety-oriented instruction-following is supposed to keep LLM-controlled robots safe. We show it also creates an availability attack surface. By injecting short safety-plausible phrases (1-5 tokens) into a robots audio channel, an adversary can trigger the models safety reasoning to halt or disrupt execution without jailbreaking the model or overriding its policy. In the embodied setting, this is a semantic denial-of-service attack: the agent stops because the injected signal looks like a legitimate alert. Across four vision-language models, seven prompt-level defenses, three deployment modes, and single- and multi-injection settings, we find that prompt-only defenses trade off attack suppression against genuine hazard response. The strongest defenses reduce hard-stop attack success on some models, but defenses change the form of disruption, not its fact: suppressed hard stops re-emerge as acknowledge loops and false alerts, which we measure with Disruption Success Rate (DSR). We further find that injection variety is consistently more effective than repeating the same phrase, suggesting that models treat diverse safety cues as corroborating evidence. The practical implication is architectural rather than prompt-level: systems that route unauthenticated audio text directly into the LLM create an avoidable security dependency between safety monitoring and action selection.

</details>

### 9. FreezeVLA: Action-Freezing Attacks against Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2509.19870)　📅 2025-09

**关键词**：`attack`、`VLA DoS`、`action freezing`、`adversarial image`

👤 **作者**：Xin Wang、…、Yu-Gang Jiang

- 🎯 **研究动机**：VLA 模型对使机器人忽略后续指令的冻结类对抗脆弱性未被研究
- 🔬 **研究方法**：提出 FreezeVLA：以 min-max 双层优化生成并评估 action-freezing 攻击的对抗图像
- 📌 **结论**：三个 SoTA VLA 与四个机器人基准上平均 ASR 76.2%，单张图像可跨语言指令稳定致瘫机器人

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models are driving rapid progress in robotics by enabling agents to interpret multimodal inputs and execute complex, long-horizon tasks. However, their safety and robustness against adversarial attacks remain largely underexplored. In this work, we identify and formalize a critical adversarial vulnerability in which adversarial images can "freeze" VLA models and cause them to ignore subsequent instructions. This threat effectively disconnects the robot's digital mind from its physical actions, potentially inducing inaction during critical interventions. To systematically study this vulnerability, we propose FreezeVLA, a novel attack framework that generates and evaluates action-freezing attacks via min-max bi-level optimization. Experiments on three state-of-the-art VLA models and four robotic benchmarks show that FreezeVLA attains an average attack success rate of 76.2%, significantly outperforming existing methods. Moreover, adversarial images generated by FreezeVLA exhibit strong transferability, with a single image reliably inducing paralysis across diverse language prompts. Our findings expose a critical safety risk in VLA models and highlight the urgent need for robust defense mechanisms.

</details>

### 10. Resource Consumption Red-Teaming for Large Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2507.18053)　📅 2025-07

**关键词**：`benchmark`、`VLM DoS`、`2D VLM`、`resource red-teaming`

👤 **作者**：Haoran Gao、…、Junlan Feng

- 🎯 **研究动机**：资源消耗攻击的红队研究忽视视觉输入这一 LVLM 新攻击面
- 🔬 **研究方法**：提出 RECITE：像素级 Vision Guided Optimization 获得 Output Recall Objective 对抗扰动，注入视觉输入触发无界重复生成
- 📌 **结论**：服务响应延迟提升超 26 倍，GPU 利用率与内存消耗额外增加 20%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Resource Consumption Attacks (RCAs) have emerged as a significant threat to the deployment of Large Language Models (LLMs). With the integration of vision modalities, additional attack vectors exacerbate the risk of RCAs in large vision-language models (LVLMs). However, existing red-teaming studies have mainly overlooked visual inputs as a potential attack surface, resulting in insufficient mitigation strategies against RCAs in LVLMs. To address this gap, we propose RECITE ($\textbf{Re}$source $\textbf{C}$onsumpt$\textbf{i}$on Red-$\textbf{Te}$aming for LVLMs), the first approach for exploiting visual modalities to trigger unbounded RCAs red-teaming. First, we present $\textit{Vision Guided Optimization}$, a fine-grained pixel-level optimization to obtain \textit{Output Recall Objective} adversarial perturbations, which can induce repeating output. Then, we inject the perturbations into visual inputs, triggering unbounded generations to achieve the goal of RCAs. Empirical results demonstrate that RECITE increases service response latency by over 26 $\uparrow$, resulting in an additional 20\% increase in GPU utilization and memory consumption. Our study reveals security vulnerabilities in LVLMs and establishes a red-teaming framework that can facilitate the development of future defenses against RCAs.

</details>