# 语言模型 DoS

## 研究方向

语言模型 DoS 研究普通自回归 LLM 与 MoE LLM 的可用性攻击面。攻击既可以通过自然指令、对抗提示和 EOS 抑制让模型持续生成，也可以利用专家路由、权重位翻转或微调数据投毒制造持久的计算瓶颈；另一条路线则利用安全模型的误报，让合法请求被系统性拒绝。

## 研究脉络

- **生成长度攻击：** 早期工作通过 EOS suppression 和自动化搜索放大模型输出长度。
- **机制与持久化扩展：** 后续攻击利用低熵循环、bit flip、人格条件和微调，使资源放大更隐蔽或更持久。
- **架构与评测扩展：** MoE 研究进一步揭示 router imbalance，Survey 则统一资源、能耗与延迟 threat model。

## 输入与生成放大攻击

### 1. Groundhog Bit-Flip Attack: Seeding Infinite Generation Loops in Mixture-of-Experts LLMs through Bit Flips

📄 [arXiv](https://arxiv.org/abs/2608.25276)　📅 2026-08

**关键词**：`attack`、`MoE routing`、`bit-flip perturbation`、`availability failure`、`MoE DoS`、`routing-layer bit flip`

👤 **作者**：Huakang Lin、…、Ruyi Ding

- 🎯 **研究动机**：MoE 路由层特定 expert 与 end-of-sequence 等 token 强相关，构成轻量位翻转攻击面
- 🔬 **研究方法**：Groundhog Bit-Flip Attack 翻转路由层比特使 expert 失活，在四个 MoE LLM 的对话、推理与 Agent 任务上诱发输出膨胀
- 📌 **结论**：平均失活不到 4 个 expert 即使输出膨胀 5912%，多数样本达 max tokens，构成 Denial-of-Wallet 攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mixture-of-Experts (MoE) architectures enable scalable and efficient large language models (LLMs) by selectively activating expert sub-networks through a routing mechanism. However, this adaptive design introduces a new attack surface: specific experts become disproportionately correlated with certain tokens (e.g., end-of-sequence), allowing adversaries to manipulate model behavior via lightweight perturbations. In this work, we present \textbf{Groundhog Bit-Flip Attack (GBFA)}, the first bit-flip-based \textit{ Denial-of-Wallet availability attack} against MoE-based LLMs. By identifying and flipping routing-layer bits associated with related expert activations, we demonstrate that GBFA substantially extends the decoding token usage across three different LLM modes: conversational, reasoning, and agentic tasks, while largely preserving semantic fidelity. Across four main real-world MoE-based LLMs, manually deactivating on average fewer than \textbf{4 experts} drives average output inflation to $\mathbf{5912\%}$, with the majority of test samples reaching max tokens. These results reveal a robustness vulnerability of MoE architectures to bit flip, and highlight the potential of GBFA as an availability attack against LLMs.

</details>

### 2. From Role Prompt to Infinite Thinking: Exploiting Persona Conditioning for Inference Cost Attacks in LLMs

📄 [arXiv](https://arxiv.org/abs/2607.25936)　📅 2026-07

**关键词**：`attack`、`LLM DoS`、`role conditioning`、`inference cost`

👤 **作者**：Zhiyi Mou、…、Kui Ren

- 🎯 **研究动机**：已有推理成本攻击依赖对抗后缀或显式扩展指令，行为可检测；LLM 的人格一致性可诱导低效但语义连贯的过度生成
- 🔬 **研究方法**：提出 RolePlay：任务感知的动态人格对齐框架，构造自适应 persona 自然诱导低效推理与过度生成
- 📌 **结论**：多 LLM 与数据集上平均 token 放大最高 7.64 倍、单次最大 207.64 倍，确立 persona 条件化为推理效率新攻击面

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLMs are increasingly deployed in real-world applications, making inference efficiency and service reliability critical concerns due to their substantial computational costs. However, the autoregressive generation mechanism of LLMs enables malicious prompts to manipulate generation behaviors, inducing excessive token generation that amplifies computational consumption and threatens service efficiency. Existing methods mainly rely on adversarial suffixes or explicit extension instructions, which introduce detectable behaviors and limit their applicability. In this paper, we reveal a previously unexplored vulnerability caused by persona consistency in LLMs, where models maintain assigned roles and reproduce corresponding behaviors even when they result in inefficient reasoning and excessive generation. Based on this observation, we propose RolePlay, a task-aware dynamic persona alignment framework that constructs adaptive personas to naturally induce inefficient yet semantically coherent behaviors for inference cost amplification. Extensive experiments across multiple LLMs and diverse task datasets demonstrate that RolePlay consistently outperforms existing inference extension methods, achieving an average token amplification of up to \bm{$7.64\times$} and a maximum token amplification ratio of \bm{$207.64\times$}. Our findings identify persona conditioning as a new attack surface for LLM inference efficiency and offer a new perspective on computational cost amplification.

</details>

### 3. NaturalSloth: Revisiting Denial-of-Service Attacks on Large Language Models

📊 [Dataset](https://huggingface.co/datasets/hlt-lab/naturalsloth) · 🎓 [Official](https://aclanthology.org/2026.acl-long.901/)　📅 2026-07　🏷 ACL 2026

**关键词**：`attack`、`LLM DoS`、`natural instruction`、`black-box attack`、`high-risk deployment`、`failure mitigation`

👤 **作者**：Yiming Chen、Zexin Li、Xianghu Yue、Robby T. Tan、Haizhou Li

- 🎯 **研究动机**：已有 LLM DoS 靠对抗扰动延迟 EOS，而指定不切实际任务的自然良性指令即可触发过度生成
- 🔬 **研究方法**：NaturalSloth 从人工种子集出发用多智能体合成框架扩展对抗数据集，保持恶意意图并增语义多样性，评测大量专有与开源 LLM
- 📌 **结论**：一致诱发过度生成，与越狱技术结合效果放大；现有防御存在显著局限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM serving is limited by provider-side resources: longer generations consume more GPU time, increase latency, and reduce throughput in multi-tenant systems. This creates a denial-of-service (DoS) risk, where attackers degrade service by inducing excessive generation. Prior work on LLM DoS primarily relies on adversarial perturbations that delay end-of-sequence termination. We show perturbations are often unnecessary: natural, benign-looking instructions that specify impractical and meaningless tasks can already trigger excessive generation. To study this overlooked vulnerability, we introduce, an adversarial dataset of natural, instruction-based DoS prompts. Starting from a human-curated seed set spanning diverse attack categories, we design a multi-agent synthesis framework to scale the dataset while preserving malicious intent and increasing semantic diversity. Experiments across a wide range of proprietary and open-source LLMs show that NaturalSloth consistently induces excessive generation, with attack effectiveness further amplified when combined with jailbreak techniques. Our analysis also reveals significant limitations of existing defenses, highlighting the need for dedicated protections against natural DoS attacks.

</details>

### 4. LoopLLM: Transferable Energy-Latency Attacks in LLMs via Repetitive Generation

📄 [arXiv](https://arxiv.org/abs/2511.07876) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/40445)　📅 2025-11　🏷 AAAI 2026

**关键词**：`attack`、`LLM DoS`、`repetitive generation`、`low-entropy loop`

👤 **作者**：Xingyu Li、…、Jia-Li Yin

- 🎯 **研究动机**：既有能耗-延迟攻击靠延迟 EOS 符号，输出变长后从输入控制终止符愈发困难
- 🔬 **研究方法**：LoopLLM 利用重复生成触发低熵解码循环迫使 LLM 输出至长度上限，含重复诱导 prompt 优化与聚合梯度的 token 对齐集成优化以提升跨模型迁移性
- 📌 **结论**：在 12 个开源与 2 个商业 LLM 上达到最大输出长度的 90% 以上（基线 20%），向 DeepSeek-V3 与 Gemini 2.5 Flash 迁移提升约 40%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) scale, their inference incurs substantial computational resources, exposing them to energy-latency attacks, where crafted prompts induce high energy and latency cost. Existing attack methods aim to prolong output by delaying the generation of termination symbols. However, as the output grows longer, controlling the termination symbols through input becomes difficult, making these methods less effective. Therefore, we propose LoopLLM, an energy-latency attack framework based on the observation that repetitive generation can trigger low-entropy decoding loops, reliably compelling LLMs to generate until their output limits. LoopLLM introduces (1) a repetition-inducing prompt optimization that exploits autoregressive vulnerabilities to induce repetitive generation, and (2) a token-aligned ensemble optimization that aggregates gradients to improve cross-model transferability. Extensive experiments on 12 open-source and 2 commercial LLMs show that LoopLLM significantly outperforms existing methods, achieving over 90% of the maximum output length, compared to 20% for baselines, and improving transferability by around 40% to DeepSeek-V3 and Gemini 2.5 Flash.

</details>

### 5. BitHydra: Towards Bit-flip Inference Cost Attack against Large Language Models

📄 [arXiv](https://arxiv.org/abs/2505.16670)　📅 2025-05

**关键词**：`attack`、`LLM DoS`、`bit flipping`、`parameter tampering`

👤 **作者**：Xiaobei Yan、Yiming Li、Hao Wang、Han Qiu、Tianwei Zhang

- 🎯 **研究动机**：推理成本攻击多从输入侧发力，篡改参数以抬升成本的攻击面未被系统利用
- 🔬 **研究方法**：提出 BitHydra，把最大化生成成本形式化为抑制 EOS 概率的二值整数规划，连续松弛后以 ADMM 求解关键权重位
- 📌 **结论**：10 个 1.5B 至 16B LLM 上仅需 1-4 次位翻转即实现无限生成

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are widely deployed, but their substantial compute demands make them vulnerable to inference cost attacks that aim to deliberately maximize the output length. In this work, we investigate a distinct attack surface: maximizing inference cost by tampering with the model parameters instead of inputs. This approach leverages the established capability of Bit-Flip Attacks (BFAs) to persistently alter model behavior via minute weight perturbations, effectively decoupling the attack from specific input queries. To realize this, we propose BitHydra, a framework that addresses the unique optimization challenge of identifying the exact weight bits that maximize generation cost. We formulate the attack as a constrained Binary Integer Programming (BIP) problem designed to systematically suppress the end-of-sequence (i.e., <eos>) probability. To overcome the intractability of the discrete search space, we relax the problem into a continuous optimization task and solve it via the Alternating Direction Method of Multipliers (ADMM). We evaluate BitHydra across 10 LLMs (1.5B-16B). Our results demonstrate that the proposed optimization method efficiently achieves endless generation with as few as 1-4 bit flips on all testing models, verifying the effectiveness of the ADMM-based formulation against both standard models and potential defenses.

</details>

### 6. An Engorgio Prompt Makes Large Language Model Babble on

📄 [arXiv](https://arxiv.org/abs/2412.19394) · 🎓 [Official](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a815fe7cad6af20a6c118f2072a881d2-Abstract-Conference.html)　📅 2024-12　🏷 ICLR 2025

**关键词**：`attack`、`LLM DoS`、`adversarial prompt`、`EOS suppression`

👤 **作者**：Jianshuo Dong、…、Han Qiu

- 🎯 **研究动机**：自回归 LLM 的推理成本可被恶意输入操纵，威胁服务可用性
- 🔬 **研究方法**：Engorgio 用参数化分布跟踪预测轨迹，设计损失稳定抑制 EOS token 出现以延长生成
- 📌 **结论**：13 个 125M-30B 开源模型上诱发约 2-13 倍超长输出逼近长度上限，实测威胁资源受限服务

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Auto-regressive large language models (LLMs) have yielded impressive performance in many real-world tasks. However, the new paradigm of these LLMs also exposes novel threats. In this paper, we explore their vulnerability to inference cost attacks, where a malicious user crafts Engorgio prompts to intentionally increase the computation cost and latency of the inference process. We design Engorgio, a novel methodology, to efficiently generate adversarial Engorgio prompts to affect the target LLM's service availability. Engorgio has the following two technical contributions. (1) We employ a parameterized distribution to track LLMs' prediction trajectory. (2) Targeting the auto-regressive nature of LLMs' inference process, we propose novel loss functions to stably suppress the appearance of the <EOS> token, whose occurrence will interrupt the LLM's generation process. We conduct extensive experiments on 13 open-sourced LLMs with parameters ranging from 125M to 30B. The results show that Engorgio prompts can successfully induce LLMs to generate abnormally long outputs (i.e., roughly 2-13$\times$ longer to reach 90%+ of the output length limit) in a white-box scenario and our real-world experiment demonstrates Engergio's threat to LLM service with limited computing resources. The code is released at: https://github.com/jianshuod/Engorgio-prompt.

</details>

### 7. Crabs: Consuming Resource via Auto-generation for LLM-DoS Attack under Black-box Settings

📄 [arXiv](https://arxiv.org/abs/2412.13879) · 🎓 [Official](https://aclanthology.org/2025.findings-acl.580/)　📅 2024-12　🏷 ACL 2025

**关键词**：`attack`、`LLM DoS`、`black-box attack`、`attack tree`

👤 **作者**：Yuanhe Zhang、…、Sen Su

- 🎯 **研究动机**：LLM-DoS 研究集中于白盒，黑盒场景未探索
- 🔬 **研究方法**：AutoDoS 构建 DoS Attack Tree 扩展节点覆盖，以迁移性驱动迭代优化使单条 prompt 跨模型，并嵌入 Length Trojan 绕过防御
- 📌 **结论**：服务响应延迟放大超 250 倍，GPU 与内存资源被严重消耗

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have demonstrated remarkable performance across diverse tasks yet still are vulnerable to external threats, particularly LLM Denial-of-Service (LLM-DoS) attacks. Specifically, LLM-DoS attacks aim to exhaust computational resources and block services. However, existing studies predominantly focus on white-box attacks, leaving black-box scenarios underexplored. In this paper, we introduce Auto-Generation for LLM-DoS (AutoDoS) attack, an automated algorithm designed for black-box LLMs. AutoDoS constructs the DoS Attack Tree and expands the node coverage to achieve effectiveness under black-box conditions. By transferability-driven iterative optimization, AutoDoS could work across different models in one prompt. Furthermore, we reveal that embedding the Length Trojan allows AutoDoS to bypass existing defenses more effectively. Experimental results show that AutoDoS significantly amplifies service response latency by over 250$\times\uparrow$, leading to severe resource consumption in terms of GPU utilization and memory usage. Our work provides a new perspective on LLM-DoS attacks and security defenses. Our code is available at https://github.com/shuita2333/AutoDoS.

</details>

### 8. Denial-of-Service Poisoning Attacks against Large Language Models

📄 [arXiv](https://arxiv.org/abs/2410.10760)　📅 2024-10

**关键词**：`attack`、`LLM DoS`、`fine-tuning poisoning`、`persistent attack`

👤 **作者**：Kuofeng Gao、Tianyu Pang、Chao Du、Yong Yang、Shu-Tao Xia、Min Lin

- 🎯 **研究动机**：语音等接口难以注入拼写错误类 DoS 输入，自然指令又受 SFT 数据长度上限约束
- 🔬 **研究方法**：P-DoS 投毒式攻击：注入单个为 DoS 设计的毒样本打破输出长度上限
- 📌 **结论**：不足 1 美元经 OpenAI 微调 API 攻击 GPT-4o，重复输出从 0.5K 增至 16K token 推理上限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent studies have shown that LLMs are vulnerable to denial-of-service (DoS) attacks, where adversarial inputs like spelling errors or non-semantic prompts trigger endless outputs without generating an [EOS] token. These attacks can potentially cause high latency and make LLM services inaccessible to other users or tasks. However, when there are speech-to-text interfaces (e.g., voice commands to a robot), executing such DoS attacks becomes challenging, as it is difficult to introduce spelling errors or non-semantic prompts through speech. A simple DoS attack in these scenarios would be to instruct the model to "Keep repeating Hello", but we observe that relying solely on natural instructions limits output length, which is bounded by the maximum length of the LLM's supervised finetuning (SFT) data. To overcome this limitation, we propose poisoning-based DoS (P-DoS) attacks for LLMs, demonstrating that injecting a single poisoned sample designed for DoS purposes can break the output length limit. For example, a poisoned sample can successfully attack GPT-4o and GPT-4o mini (via OpenAI's finetuning API) using less than $1, causing repeated outputs up to the maximum inference length (16K tokens, compared to 0.5K before poisoning). Additionally, we perform comprehensive ablation studies on open-source LLMs and extend our method to LLM agents, where attackers can control both the finetuning dataset and algorithm. Our findings underscore the urgent need for defenses against P-DoS attacks to secure LLMs. Our code is available at https://github.com/sail-sg/P-DoS.

</details>

### 9. Safeguard is a Double-edged Sword: Denial-of-service Attack on Large Language Models

📄 [arXiv](https://arxiv.org/abs/2410.02916) · 🌐 [Project](https://doi.org/10.1145/3733800.3763264)　📅 2024-10　🏷 ACM CCS 2025

**关键词**：`attack`、`LLM DoS`、`safety false positive`、`universal trigger`

👤 **作者**：Qingzhao Zhang、Ziyang Xiong、Z. Morley Mao

- 🎯 **研究动机**：越狱研究只关注安全防护的假阴性，误报可被武器化实施 DoS 的威胁未被研究
- 🔬 **研究方法**：白盒优化约 30 字符的表面无害通用 prompt 注入用户模板，或经投毒微调服务端模型，触发安全拒绝
- 📌 **结论**：Llama Guard 3 上可误封超 97% 的合法用户请求

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety is a paramount concern for large language models (LLMs) in open deployment, motivating the development of safeguard methods that enforce ethical and responsible use through safety alignment or guardrail mechanisms. Jailbreak attacks that exploit the \emph{false negatives} of safeguard methods have emerged as a prominent research focus in the field of LLM security. However, we found that the malicious attackers could also exploit false positives of safeguards, i.e., fooling the safeguard model to block safe content mistakenly, leading to a denial-of-service (DoS) affecting LLM users. To bridge the knowledge gap of this overlooked threat, we explore multiple attack methods that include inserting a short adversarial prompt into user prompt templates and corrupting the LLM on the server by poisoned fine-tuning. In both ways, the attack triggers safeguard rejections of user requests from the client. Our evaluation demonstrates the severity of this threat across multiple scenarios. For instance, in the scenario of white-box adversarial prompt injection, the attacker can use our optimization process to automatically generate seemingly safe adversarial prompts, approximately only 30 characters long, that universally block over 97% of user requests on Llama Guard 3. These findings reveal a new dimension in LLM safeguard evaluation -- adversarial robustness to false positives.

</details>

### 10. Trigger the Straggler: Load Hijack on Mixture-of-Experts LLMs

📄 [arXiv](https://arxiv.org/abs/2608.10614)　📅 2026-08

**关键词**：`attack`、`MoE DoS`、`router load hijack`、`expert-parallel straggler`、`MoE router backdoor`、`private trigger`

👤 **作者**：Rui Zhang、…、Guowen Xu

- 🎯 **研究动机**：专家并行下 MoE 路由既选专家又决定 GPU 负载，路由权重构成未被检查的供应链攻击面
- 🔬 **研究方法**：Load Hijack 中恶意提供者只改 checkpoint 路由权重并保留私有触发：触发时把 token-专家分配集中到单 GPU 造成 straggler，三阶段优化保持普通输入路由接近干净参考
- 📌 **结论**：三个 MoE 家族、四个语料下触发流量 92.3-95.6% 路由到目标专家；EP 服务中 TTFT 达普通流量的 1.43 倍、吞吐 0.86 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Expert parallelism (EP) is a common strategy for serving large Mixture-of-Experts (MoE) models across multiple GPUs by distributing experts among devices. Router decisions then determine both which experts process each token and which GPUs execute the resulting work. This procedure exposes a supply-chain attack surface in the serving schedule. We introduce Load Hijack, in which a malicious model provider modifies only a checkpoint's router weights, distributes the poisoned checkpoint, and retains a private trigger. When the trigger appears, the poisoned router concentrates token-to-expert assignments on experts co-located on one GPU. The resulting load makes that GPU a straggler and forces peer devices to wait, while routing on ordinary inputs remains near the clean reference. We find this conditional behavior difficult to achieve because an objective that rewards target-expert use on triggered inputs can also bias ordinary-input routing toward the same experts. To resolve this conflict, Load Hijack employs a three-stage optimization procedure that produces strong trigger-dependent concentration while keeping ordinary-input routing close to the clean reference. Across three MoE families and four corpora, Load Hijack directs 92.3% to 95.6% of triggered token assignments to the target experts. In live EP serving, triggered traffic produces 1.43x the time-to-first-token and 0.86x the throughput measured under ordinary traffic. These results show that poisoned routers can act as trigger-controlled device schedulers and motivate checkpoint audits of routing and runtime load.

</details>

### 11. RepetitionCurse: Measuring and Understanding Router Imbalance in Mixture-of-Experts LLMs under DoS Stress

📄 [arXiv](https://arxiv.org/abs/2512.23995) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65906)　📅 2025-12　🏷 ICML 2026

**关键词**：`analysis`、`benchmark`、`MoE DoS`、`MoE routing`、`load imbalance`、`adversarial defense`

👤 **作者**：Ruixuan Huang、…、Wei Wang

- 🎯 **研究动机**：MoE 推理缺显式负载均衡约束，对抗输入可诱发路由集中，把效率机制变成 DoS 攻击向量
- 🔬 **研究方法**：RepetitionCurse 利用 MoE 路由器把所有 token 一致路由到同一 top-k 专家集的通用缺陷，以简单重复 token 模式构造模型无关的黑盒对抗 prompt
- 📌 **结论**：在 Mixtral-8x7B 等广泛部署模型上把端到端推理延迟提高 3.063 倍，造成设备瓶颈与 TTFT SLA 违约

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mixture-of-Experts architectures have become the standard for scaling large language models due to their superior parameter efficiency. To accommodate the growing number of experts in practice, modern inference systems commonly adopt expert parallelism to distribute experts across devices. However, the absence of explicit load balancing constraints during inference allows adversarial inputs to trigger severe routing concentration. We demonstrate that out-of-distribution prompts can manipulate the routing strategy such that all tokens are consistently routed to the same set of top-$k$ experts, which creates computational bottlenecks on certain devices while forcing others to idle. This converts an efficiency mechanism into a denial-of-service attack vector, leading to violations of service-level agreements for time to first token. We propose RepetitionCurse, a low-cost black-box strategy to exploit this vulnerability. By identifying a universal flaw in MoE router behavior, RepetitionCurse constructs adversarial prompts using simple repetitive token patterns in a model-agnostic manner. On widely deployed MoE models like Mixtral-8x7B, our method increases end-to-end inference latency by 3.063x, degrading service availability significantly.

</details>

### 12. Resource Consumption Threats in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2603.16068)　📅 2026-03

**关键词**：`survey`、`LLM DoS`、`resource consumption`、`threat taxonomy`

👤 **作者**：Yuanhe Zhang、…、Sen Su

- 🎯 **研究动机**：过度生成类资源消耗威胁损害 LLM 服务可用性与经济可持续性，该新兴领域缺少统一认识
- 🔬 **研究方法**：系统综述资源消耗威胁，沿威胁诱导、机制理解到缓解的完整管线梳理并界定问题范围
- 📌 **结论**：建立该领域的统一问题版图，为威胁刻画与缓解提供清晰基础

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Given limited and costly computational infrastructure, resource efficiency is a key requirement for large language models (LLMs). Efficient LLMs increase service capacity for providers and reduce latency and API costs for users. Recent resource consumption threats induce excessive generation, degrading model efficiency and harming both service availability and economic sustainability. This survey presents a systematic review of threats to resource consumption in LLMs. We further establish a unified view of this emerging area by clarifying its scope and examining the problem along the full pipeline from threat induction to mechanism understanding and mitigation. Our goal is to clarify the problem landscape for this emerging area, thereby providing a clearer foundation for characterization and mitigation.

</details>