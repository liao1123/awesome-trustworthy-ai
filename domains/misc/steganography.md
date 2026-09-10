# 隐写与隐蔽信道

## 研究方向

隐写与隐蔽信道研究模型或 Agent 如何把秘密、恶意指令和行为控制信号隐藏在自然语言、图像、音视频、数值参数或工具交互中，并考察这些信道的容量、不可感知性、鲁棒性、检测方法以及在越狱、数据外泄和多 Agent 合谋中的安全风险。

## 研究脉络

- **隐写编码：** 基础工作追求高容量、低可感知性和 provable security，研究如何稳定地在自然语言中承载隐藏信息。
- **安全滥用：** 攻击研究将 steganography 用于 jailbreak、隐蔽微调、backdoor 与多 Agent collusion。
- **检测与防御：** 防御路线覆盖 steganalysis、训练接口防护和后门移除，并检验编码方案在自适应检测下是否仍隐蔽。

## 安全绕过与 Steganographic Backdoor

### 1. Hiding in Plain Floats: Steganographic Carriers for Indirect Prompt and Content Injection

📄 [arXiv](https://arxiv.org/abs/2606.08403)　📅 2026-06　🏷 ICML 2026

**关键词**：`attack`、`structured-data covert channel`、`float carrier`、`indirect prompt injection`

👤 **作者**：Mudit Sinha、Sanika Chavan

- 🎯 **研究动机**：以文本为中心的 prompt injection 防御假设恶意信号在被检查的某个文本视图中可见，结构化浮点参数载体打破该假设
- 🔬 **研究方法**：研究把注入载荷编码为 IFS 派生浮点数组、经遥测碎片化重建的攻击，在三个商业 LLM API 上做 14,400 次真实试验，并用 2x2 消融分离数据层存储与重建层碎片化作用
- 📌 **结论**：最强双层文本分类器（Prompt Guard 2 + TF-IDF）下浮点载体仍保持 94.3% 泄漏 ASR；xxd 检测器与语义校验可封堵当前实例，贡献在于测出文本-only 巡检的失效边界

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-centered prompt-injection defenses assume that the malicious signal is visible in one of the inspected text views. We study a reproducible LLM01-style indirect prompt/content-injection failure mode where that assumption breaks: a payload caught in plain English slips past the same detector when it is transported as structured float parameters and reconstructed only as fragmented telemetry. Across 14,400 attacked real-model trials on three commercial LLM APIs from different providers, the IFS-derived float-array carrier preserves 94.3% leakage ASR under the strongest dual-layer text-classifier defense evaluated in the main matrix: a Prompt Guard 2 + TF-IDF ensemble; the same carrier-level pattern also replicates with a fine-tuned roberta-base detector. We emphasize leakage ASR because downstream systems may act on quoted or reproduced markers even when the model refuses, but Strong ASR is the stricter metric for structurally compliant attack success. A 2 x 2 ablation shows that data-layer storage and reconstruction-layer fragmentation defeat different text views and that both are needed to evade both. A simple xxd detector and semantic validation block the current T3 instance, so the contribution is not an undetectable exploit but a measured failure boundary for text-only inspection in structured-input pipelines that expose reconstructed auxiliary channels to an LLM.

</details>

### 2. Shape-Shifting Malicious Code in Software Backdoors via Language Models

🌐 [Project](https://doi.org/10.1145/3779208.3807485)　📅 2026-06　🏷 ACM CCS 2026

**关键词**：`attack`、`LLM misuse`、`software backdoor`、`supply-chain evasion`、`LLM steganography`、`malicious payload`

- 🎯 **研究动机**：开源供应链防御聚焦检测软件内的后门功能，忽视看似良性的文档与配置脚本也可成为恶意代码载体
- 🔬 **研究方法**：用 LLM 把恶意载荷编码进良性 cover data，产物对人审自然可信，且无需语言模型即可还原为恶意形态
- 📌 **结论**：评估证明该 shape-shifting 代码能有效躲过代码审计，据此给出软件开发建议

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Supply-chain attacks in open-source software are a notorious threat to security. Current defenses focus primarily on detecting backdoor functionality within the software. However, we show that seemingly benign documentation and configuration scripts can also serve as carriers of malicious code. To this end, we introduce an attack that uses large language models to encode a malicious payload into benign cover data. The resulting material appears natural and plausible to human reviewers, yet it can be easily reconstructed into its malicious form without access to a language model. Our evaluation demonstrates the efficacy of this approach in hiding code from audits. We argue that this form of shape-shifting code poses a notable risk and derive corresponding recommendations for software development. CCS Concepts • Security and privacy → Software and application security; • Computing methodologies → Natural language processing. Keywords Software Backdoors, Supply-Chain Attacks, Generative Models ACM Reference Format: Mohammad Ebrahimi Fard, Felix Weissberg, Erik Imgrund, Thorsten Eisenhofer, and Konrad Rieck. 2026. Shape-Shifting Malicious Code in Software Backdoors via Language Models. In ACM Asia Conference on Computer and Communications Security (ASIA CCS ’26), June 01–05, 2026, Bangalore, India. ACM, New York, NY, USA, 16 pages. https://doi.org/10.1145/3779208.3807 485

</details>

### 3. CORDYCEPS: Covert Control Attacks on LLMs via Data Poisoning

📄 [arXiv](https://arxiv.org/abs/2605.26595) · 🌐 [Project](https://anonymous.4open.science/r/cordyceps-F147) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/shao-zedian)　📅 2026-05　🏷 USENIX Security 2026

**关键词**：`attack`、`steganographic backdoor`、`stealthy backdoor`、`covert channel`、`LLM data poisoning`、`covert control`

👤 **作者**：Zedian Shao、Charles Fleming、Teodora Baluta

- 🎯 **研究动机**：固定触发短语可被离群检测、干净数据正则或在线监控中和
- 🔬 **研究方法**：Cordyceps 通过共享知识（事实、概念）与攻击者短语的语义关联教会 LLM 一套信息隐藏方案，可编码解码任意恶意指令
- 📌 **结论**：小投毒率下平均 ASR 较启发式 prompt injection 高约 40%；后门防御后仍保持最高 93%、prompt injection 防御后最高 98%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are often fine-tuned on uncurated text datasets that adversaries can poison. Existing poisoning attacks primarily rely on fixed trigger phrases that defenses such as outlier detection, clean-data regularization, or online monitoring can neutralize. In this paper, we propose a data poisoning method that teaches an LLM an information hiding scheme reliably and stealthily through semantic associations between shared knowledge such as facts or concepts and attacker-chosen phrases. The induced hiding scheme can encode and decode arbitrary malicious instructions, thus revealing a new and subtle poisoning-induced vulnerability: covert control attacks. We precisely characterize covert control attacks and evaluate them across $5$ LLMs, $3$ backdoor defenses, and $4$ prompt injection defenses. With a small poisoned fraction, covert control attacks outperform heuristic-based prompt injection attacks in average attack success rate by about $40\%$ relative to clean fine-tuned models. They also circumvent defenses based on detection and fine-tuning, maintaining up to $93\%$ attack success rate after backdoor defenses and up to $98\%$ after prompt injection defenses.

</details>

### 4. Trojan-Speak: Bypassing Constitutional Classifiers with No Jailbreak Tax via Adversarial Finetuning

📄 [arXiv](https://arxiv.org/abs/2603.29038) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66278)　📅 2026-03　🏷 ICML 2026

**关键词**：`attack`、`harmful fine-tuning`、`covert language`、`classifier bypass`、`LLM jailbreak`、`reinforcement learning`

👤 **作者**：Bilgehan Sel、Xuanli He、Alwin Peng、Ming Jin、Jerry Wei

- 🎯 **研究动机**：微调 API 创造新攻击面，能否绕过 Anthropic 的 Constitutional Classifiers 未知
- 🔬 **研究方法**：Trojan-Speak 用课程学习加 GRPO 混合 RL 教模型一种规避 LLM 内容分类的通信协议
- 📌 **结论**：14B+ 模型分类器规避达 99% 以上且推理能力退化 <5%（此前对抗微调 >25%）；可回答 CBRN 赏金计划的专业问题，激活级探针可显著增强鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning APIs offered by major AI providers create new attack surfaces where adversaries can bypass safety measures through targeted fine-tuning. We introduce Trojan-Speak, an adversarial fine-tuning method that bypasses Anthropic's Constitutional Classifiers. Our approach uses curriculum learning combined with GRPO-based hybrid reinforcement learning to teach models a communication protocol that evades LLM-based content classification. Crucially, while prior adversarial fine-tuning approaches report more than 25% capability degradation on reasoning benchmarks, Trojan-Speak incurs less than 5% degradation while achieving 99+% classifier evasion for models with 14B+ parameters. We demonstrate that fine-tuned models can provide detailed responses to expert-level CBRN (Chemical, Biological, Radiological, and Nuclear) queries from Anthropic's Constitutional Classifiers bug-bounty program. Our findings reveal that LLM-based content classifiers alone are insufficient for preventing dangerous information disclosure when adversaries have fine-tuning access, and we show that activation-level probes can substantially improve robustness to such attacks.

</details>

### 5. Invisible Safety Threat: Malicious Finetuning for LLM via Steganography

📄 [arXiv](https://arxiv.org/abs/2603.08104) · 🤗 [Model](https://huggingface.co/bigglesworthnotcat/LLM-Steg-Llama-70B-Lora) · 📊 [Dataset](https://huggingface.co/datasets/bigglesworthnotcat/llm-steg-alpaca-gpt4) · 📝 [OpenReview](https://openreview.net/forum?id=6cEPDGaShH) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10011363)　📅 2026-03　🏷 ICLR 2026

**关键词**：`attack`、`harmful fine-tuning`、`steganographic fine-tuning`、`data poisoning`、`steganographic backdoor`、`stealthy backdoor`

👤 **作者**：Guangnian Wan、Xinyin Ma、Gongfan Fang、Xinchao Wang

- 🎯 **研究动机**：显式有害微调数据会被内容审核发现，需要更隐蔽的有害微调载体
- 🔬 **研究方法**：微调模型掌握隐写术：提示内隐写嵌入恶意目标问题，模型在表面良性的掩护回答中隐写输出恶意内容
- 📌 **结论**：在 GPT-4.1（绕过 OpenAI 微调 API 防护）与 Llama-3.3-70B 等三个开源模型上，全部恶意隐写文本被 Llama-Guard-3 误判为安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Understanding and addressing potential safety alignment risks in large language models (LLMs) is critical for ensuring their safe and trustworthy deployment. In this paper, we highlight an insidious safety threat: a compromised LLM can maintain a facade of proper safety alignment while covertly generating harmful content. To achieve this, we finetune the model to understand and apply a steganographic technique. At inference time, we input a prompt that contains a steganographically embedded malicious target question along with a plaintext cover question. The model, in turn, produces a target response similarly embedded within a benign-looking cover response. In this process, human observers only see the model being prompted with a cover question and generating a corresponding cover response, while the malicious content is hidden from view. We demonstrate this invisible safety threat on GPT-4.1 despite the OpenAI finetuning API's safeguards. The finetuned model produces steganographic malicious outputs in response to hidden malicious prompts, while the user interface displays only a fully benign cover interaction. We also replicate the attack on three open-source models, Llama-3.3-70B-Instruct, Phi-4, and Mistral-Small-24B-Base-2501, confirming the generality of our method. We quantitatively evaluate our method on the AdvBench dataset, using Llama-Guard-3-8B for content safety classification. Across all four models, all stegotexts containing malicious content are incorrectly classified as safe.

</details>

### 6. Odysseus: Jailbreaking Commercial Multimodal LLM-integrated Systems via Dual Steganography

📄 [arXiv](https://arxiv.org/abs/2512.20168) · 🌐 [Project](https://www.ndss-symposium.org/ndss-paper/odysseus-jailbreaking-commercial-multimodal-llm-integrated-systems-via-dual-steganography/)　📅 2025-12　🏷 NDSS 2026

**关键词**：`attack`、`multimodal steganography`、`safety bypass`

👤 **作者**：Songze Li、Jiameng Cheng、Yiming Li、Xiaojun Jia、Dacheng Tao

- 🎯 **研究动机**：商业 MLLM 集成系统的安全过滤器依赖恶意内容在输入或输出中显式可见这一假设，多模态可将其隐藏
- 🔬 **研究方法**：Odysseus 用双重隐写把恶意查询与回复分别隐蔽嵌入良性外观图像，绕过输入与输出过滤
- 📌 **结论**：对多个现实 MLLM 集成系统越狱成功率达 99%，暴露现有防御的跨模态盲区

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

By integrating language understanding with perceptual modalities such as images, multimodal large language models (MLLMs) constitute a critical substrate for modern AI systems, particularly intelligent agents operating in open and interactive environments. However, their increasing accessibility also raises heightened risks of misuse, such as generating harmful or unsafe content. To mitigate these risks, alignment techniques are commonly applied to align model behavior with human values. Despite these efforts, recent studies have shown that jailbreak attacks can circumvent alignment and elicit unsafe outputs. Currently, most existing jailbreak methods are tailored for open-source models and exhibit limited effectiveness against commercial MLLM-integrated systems, which often employ additional filters. These filters can detect and prevent malicious input and output content, significantly reducing jailbreak threats. In this paper, we reveal that the success of these safety filters heavily relies on a critical assumption that malicious content must be explicitly visible in either the input or the output. This assumption, while often valid for traditional LLM-integrated systems, breaks down in MLLM-integrated systems, where attackers can leverage multiple modalities to conceal adversarial intent, leading to a false sense of security in existing MLLM-integrated systems. To challenge this assumption, we propose Odysseus, a novel jailbreak paradigm that introduces dual steganography to covertly embed malicious queries and responses into benign-looking images. Extensive experiments on benchmark datasets demonstrate that our Odysseus successfully jailbreaks several pioneering and realistic MLLM-integrated systems, achieving up to 99% attack success rate. It exposes a fundamental blind spot in existing defenses, and calls for rethinking cross-modal security in MLLM-integrated systems.

</details>

### 7. Invisible Injections: Exploiting Vision-Language Models Through Steganographic Prompt Embedding

📄 [arXiv](https://arxiv.org/abs/2507.22304)　📅 2025-07

**关键词**：`attack`、`multimodal steganography`、`safety bypass`

👤 **作者**：Chetan Pathade

- 🎯 **研究动机**：隐写式 prompt 注入对 VLM 的威胁缺乏系统研究
- 🔬 **研究方法**：结合空间、频域与神经隐写的多域嵌入框架，把恶意指令不可见地嵌入图像，在 12 个数据集 8 个模型上系统评估
- 📌 **结论**：总体 ASR 24.3%，神经隐写最高 31.8%，视觉不可察觉性良好（PSNR>38dB、SSIM>0.94）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models (VLMs) have revolutionized multimodal AI applications but introduce novel security vulnerabilities that remain largely unexplored. We present the first comprehensive study of steganographic prompt injection attacks against VLMs, where malicious instructions are invisibly embedded within images using advanced steganographic techniques. Our approach demonstrates that current VLM architectures can inadvertently extract and execute hidden prompts during normal image processing, leading to covert behavioral manipulation. We develop a multi-domain embedding framework combining spatial, frequency, and neural steganographic methods, achieving an overall attack success rate of 24.3% (plus or minus 3.2%, 95% CI) across leading VLMs including GPT-4V, Claude, and LLaVA, with neural steganography methods reaching up to 31.8%, while maintaining reasonable visual imperceptibility (PSNR greater than 38 dB, SSIM greater than 0.94). Through systematic evaluation on 12 diverse datasets and 8 state-of-the-art models, we reveal moderate but meaningful vulnerabilities in current VLM architectures and propose effective countermeasures. Our findings have significant implications for VLM deployment in security-critical applications and highlight the need for proportionate multimodal AI security frameworks.

</details>

### 8. TrojanStego: Your Language Model Can Secretly Be A Steganographic Privacy Leaking Agent

📄 [arXiv](https://arxiv.org/abs/2505.20118) · 🤗 [Model](https://huggingface.co/worta/TrojanStego-LLama3-8B-LoRA) · 📊 [Dataset](https://huggingface.co/datasets/worta/TrojanStego) · 🎓 [Official](https://aclanthology.org/2025.emnlp-main.1386/)　📅 2025-05　🏷 EMNLP 2025

**关键词**：`attack`、`steganographic backdoor`、`stealthy backdoor`、`privacy leakage`

👤 **作者**：Dominik Meier、Jan Philip Wahle、Paul Röttger、Terry Ruas、Bela Gipp

- 🎯 **研究动机**：LLM 进入敏感工作流后，隐蔽且被动的数据外泄威胁需要新威胁模型刻画
- 🔬 **研究方法**：提出 TrojanStego，微调 LLM 以词汇分区编码方案把敏感上下文写入自然输出，无需控制推理输入
- 📌 **结论**：held-out prompt 上可靠传输 32-bit 秘密准确率 87%，三次生成多数投票超 97%，且可逃避人工检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) become integrated into sensitive workflows, concerns grow over their potential to leak confidential information. We propose TrojanStego, a novel threat model in which an adversary fine-tunes an LLM to embed sensitive context information into natural-looking outputs via linguistic steganography, without requiring explicit control over inference inputs. We introduce a taxonomy outlining risk factors for compromised LLMs, and use it to evaluate the risk profile of the threat. To implement TrojanStego, we propose a practical encoding scheme based on vocabulary partitioning learnable by LLMs via fine-tuning. Experimental results show that compromised models reliably transmit 32-bit secrets with 87% accuracy on held-out prompts, reaching over 97% accuracy using majority voting across three generations. Further, they maintain high utility, can evade human detection, and preserve coherence. These results highlight a new class of LLM data exfiltration attacks that are passive, covert, practical, and dangerous.

</details>

### 9. Revisiting Backdoor Attacks on LLMs: A Stealthy and Practical Poisoning Framework via Harmless Inputs

📄 [arXiv](https://arxiv.org/abs/2505.17601)　📅 2025-05

**关键词**：`attack`、`steganographic backdoor`、`stealthy backdoor`、`harmless input`、`clean-label`

👤 **作者**：Jiawei Kong、…、Han Qiu

- 🎯 **研究动机**：直接在训练数据嵌入有害 QA 会破坏安全对齐，且毒样本易被护栏过滤
- 🔬 **研究方法**：仅用良性 QA 建立触发器与肯定前缀的关联，推理时由模型语言建模能力自行补全恶意内容，并辅以梯度优化通用触发器
- 📌 **结论**：多个 LLM 上成功植入有害生成后门，可躲过强护栏模型检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent studies have widely investigated backdoor attacks on Large Language Models (LLMs) by inserting harmful question-answer (QA) pairs into their training data. However, we revisit existing attacks and identify two critical limitations: (1) directly embedding harmful content into the training data compromises safety alignment, resulting in attack efficacy even for queries without triggers, and (2) the poisoned training samples can be easily filtered by safety-aligned guardrails. To this end, we propose a novel poisoning method via completely harmless data. Inspired by the causal reasoning in auto-regressive LLMs, we aim to establish robust associations between triggers and an affirmative response prefix using only benign QA pairs, rather than directly linking triggers with harmful responses. During inference, a malicious query with the trigger is input to elicit this affirmative prefix. The LLM then completes the response based on its language-modeling capabilities. Achieving this using only clean samples is non-trivial. We observe an interesting resistance phenomenon where the LLM initially appears to agree but subsequently refuses to answer. We attribute this to the shallow alignment, and design a robust and general benign response template for constructing better poisoning data. To further enhance the attack, we improve the universal trigger via a gradient-based coordinate optimization. Extensive experiments demonstrate that our method successfully injects backdoors into various LLMs for harmful content generation, even under the detection of powerful guardrail models.

</details>

### 10. Hiding in Plain Sight: A Steganographic Approach to Stealthy LLM Jailbreaks

📄 [arXiv](https://arxiv.org/abs/2505.16765) · 📝 [OpenReview](https://openreview.net/forum?id=ZujfJpD6as)　📅 2025-05　🏷 ICLR 2026

**关键词**：`attack`、`linguistic steganography`、`safety bypass`

👤 **作者**：Jianing Geng、…、Zheli Liu

- 🎯 **研究动机**：越狱的语义隐蔽与语言隐蔽存在根本权衡，易被检测
- 🔬 **研究方法**：提出 StegoAttack，以隐写术把有害查询嵌入语义连贯的良性段落，同时实现语义与语言双重隐蔽
- 📌 **结论**：四个对齐 LLM（含 GPT-5、Gemini-3）上平均 ASR 95.50%，外部检测器下降幅不足 27%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak attacks pose a serious threat to Large Language Models (LLMs) by bypassing their safety mechanisms. A truly advanced jailbreak is defined not only by its effectiveness but, more critically, by its stealthiness. However, existing methods face a fundamental trade-off between semantic stealth (hiding malicious intent) and linguistic stealth (appearing natural), leaving them vulnerable to detection. To resolve this trade-off, we propose StegoAttack, a framework that leverages steganography. The core insight is to embed a harmful query within a benign, semantically coherent paragraph. This design provides semantic stealth by concealing the existence of malicious content and ensures linguistic stealth by maintaining the natural fluency of the cover paragraph. We evaluate StegoAttack on four state-of-the-art, safety-aligned LLMs, including GPT-5 and Gemini-3, and benchmark it against eight leading jailbreak methods. Our results show that StegoAttack achieves an average attack success rate (ASR) of 95.50%, outperforming existing baselines across all four models. Critically, its ASR drops by less than 27.00% under external detectors, while maintaining natural language distribution. This demonstrates that steganography effectively decouples linguistic and semantic stealth, thereby posing a fully concealed yet highly effective security threat. The code is available at https://github.com/GenggengSvan/StegoAttack

</details>

### 11. Covert Malicious Finetuning: Challenges in Safeguarding LLM Adaptation

📄 [arXiv](https://arxiv.org/abs/2406.20053) · 🌐 [Project](https://proceedings.mlr.press/v235/halawi24a.html)　📅 2024-06　🏷 ICML 2024

**关键词**：`attack`、`harmful fine-tuning`、`covert channel`、`API moderation bypass`、`steganographic backdoor`、`stealthy backdoor`

👤 **作者**：Danny Halawi、Alexander Wei、Eric Wallace、Tony T. Wang、Nika Haghtalab、Jacob Steinhardt

- 🎯 **研究动机**：黑盒微调接口的防护能否抵御老练攻击者存疑
- 🔬 **研究方法**：构造每条看似无害、整体教会模型以编码应答编码有害请求的微调数据集
- 📌 **结论**：GPT-4 微调后 99% 执行有害指令，绕过数据检查、安全评估与输入输出分类器等防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Black-box finetuning is an emerging interface for adapting state-of-the-art language models to user needs. However, such access may also let malicious actors undermine model safety. To demonstrate the challenge of defending finetuning interfaces, we introduce covert malicious finetuning, a method to compromise model safety via finetuning while evading detection. Our method constructs a malicious dataset where every individual datapoint appears innocuous, but finetuning on the dataset teaches the model to respond to encoded harmful requests with encoded harmful responses. Applied to GPT-4, our method produces a finetuned model that acts on harmful instructions 99% of the time and avoids detection by defense mechanisms such as dataset inspection, safety evaluations, and input/output classifiers. Our findings question whether black-box finetuning access can be secured against sophisticated adversaries.

</details>

### 12. Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems

📄 [arXiv](https://arxiv.org/abs/2606.28425)　📅 2026-06

**关键词**：`attack`、`multi-agent steganography`、`provable security`、`multi-agent covert communication`

👤 **作者**：Jimmy Laurence Rippin、Simon C. Marshall、David Demitri Africa、Christian Schroeder de Witt

- 🎯 **研究动机**：理论上不可检测的隐写方案曾因复杂度高被视为安全屏障，前沿编码 agent 配合工具是否已能实现未知
- 🔬 **研究方法**：给 agentic coding model 提供代码执行与论文检索等真实工具，测试其构造不可检测隐写系统的能力，并把默契隐写协调形式化为 Schelling 点问题引入协调度量
- 📌 **结论**：agent 已能实现不可检测隐写系统并自行补齐缺失组件；主要屏障从实现能力转向协调——广泛方案族上收敛显著但严格一次协调有限，工具介导与重复交互是风险最高场景

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Increasingly autonomous agentic AI systems pose novel multi-agent risks, such as secret collusion via covert communication channels. The natural defence to these collusion attempts is to monitor plain-text communication, but the efficacy of monitors has been called into doubt by increasingly sophisticated model steganography; indeed, some theoretical schemes have been proposed that are information-theoretically or computationally indistinguishable from good-faith plain-text communication. In this paper, we demonstrate that the complexity of these schemes is no longer a safety barrier, as agentic coding models can already produce undetectable stegosystems when given realistic tool usage, such as code execution or accessing research papers through web searches. Agents also adapt when key ingredients are missing, for example, by adding model-sampling components or implementing related keyed coding schemes. We then frame tacit steganographic coordination between agents as a Schelling-point problem and introduce coordination metrics for estimating when two agents are likely to select compatible schemes without explicit prior agreement. Our results suggest a shift in the threat model for covert communication between AI agents, where the main barrier is no longer whether frontier agents can understand and implement sophisticated stegosystems, but coordination: whether independently acting agents can converge on compatible schemes, keys, and parameters. We find substantial convergence on broad scheme families but limited strict one-shot coordination, suggesting that shared artefacts, repeated interaction, and tool-mediated search are the settings where covert communication risks are most acute. Overall, our findings provide empirical grounding for the recent strategic confinement hypothesis, which assumes that capable agents can construct covert channels that survive monitoring.

</details>

### 13. Position: Stateless Yet Not Forgetful: Implicit Memory as a Hidden Channel in LLMs

🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`analysis`、`implicit memory`、`temporal backdoor`、`covert channel`

- 🎯 **研究动机**：LLM虽无持久状态，隐式记忆仍可成为隐蔽通道
- 🔬 **研究方法**：阐明implicit memory作为temporal backdoor与covert channel的威胁模型
- 📌 **结论**：揭示跨上下文隐蔽通信与后门化新攻击面

### 14. Whispering Agents: An Event-Driven Covert Communication Protocol for the Internet of Agents

📄 [arXiv](https://arxiv.org/abs/2508.02188) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/40380)　📅 2025-08　🏷 AAAI 2026

**关键词**：`tool`、`multi-agent steganography`、`multi-agent covert communication`、`covert channel`

👤 **作者**：Kaibo Huang、Yukun Wei、Wansheng Wu、Tianhua Zhang、Zhongliang Yang、Linna Zhou

- 🎯 **研究动机**：标准 A2A 协议只保护消息内容而非通信行为本身，IoA 面临监控与流量分析威胁
- 🔬 **研究方法**：形式化由 Storage、Timing 与 Behavioral 三通道构成的 Covert Event Channel 模型，并设计实现 ΠCCAP 协议
- 📌 **结论**：ΠCCAP 兼具高容量与鲁棒性，且对强力 LLM warden 保持不可感知

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The emergence of the Internet of Agents (IoA) introduces critical challenges for communication privacy in sensitive, high-stakes domains. While standard Agent-to-Agent (A2A) protocols secure message content, they are not designed to protect the act of communication itself, leaving agents vulnerable to surveillance and traffic analysis. We find that the rich, event-driven nature of agent dialogues provides a powerful, yet untapped, medium for covert communication. To harness this potential, we introduce and formalize the Covert Event Channel, the first unified model for agent covert communication driven by three interconnected dimensions, which consist of the Storage, Timing,and Behavioral channels. Based on this model, we design and engineer ΠCCAP, a novel protocol that operationalizes this event-driven paradigm. Our comprehensive evaluation demonstrates that ΠCCAP achieves high capacity and robustness while remaining imperceptible to powerful LLM-based wardens, establishing its practical viability. By systematically engineering this channel, our work provides the foundational understanding essential for developing the next generation of monitoring systems and defensive protocols for a secure and trustworthy IoA.

</details>

### 15. Hidden in Plain Text: Emergence & Mitigation of Steganographic Collusion in LLMs

📄 [arXiv](https://arxiv.org/abs/2410.03768)　📅 2024-10

**关键词**：`analysis`、`multi-agent steganography`、`multi-agent covert communication`

👤 **作者**：Yohan Mathew、…、Nandi Schoots

- 🎯 **研究动机**：隐写合谋能否在 LLM 中自发出现、现有缓解是否稳健均未知
- 🔬 **研究方法**：设计 GBRL 与 ICRL 两种方法可靠诱导 LLM 文本隐写，并测试被动输出监督与主动通信改写的缓解效果
- 📌 **结论**：错误奖励可致隐写合谋自发涌现，标准缓解手段均不完全有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid proliferation of frontier model agents promises significant societal advances but also raises concerns about systemic risks arising from unsafe interactions. Collusion to the disadvantage of others has been identified as a central form of undesirable agent cooperation. The use of information hiding (steganography) in agent communications could render such collusion practically undetectable. This underscores the need for investigations into the possibility of such behaviours emerging and the robustness corresponding countermeasures. To investigate this problem we design two approaches -- a gradient-based reinforcement learning (GBRL) method and an in-context reinforcement learning (ICRL) method -- for reliably eliciting sophisticated LLM-generated linguistic text steganography. We demonstrate, for the first time, that unintended steganographic collusion in LLMs can arise due to mispecified reward incentives during training. Additionally, we find that standard mitigations -- both passive oversight of model outputs and active mitigation through communication paraphrasing -- are not fully effective at preventing this steganographic communication. Our findings imply that (i) emergence of steganographic collusion is a plausible concern that should be monitored and researched, and (ii) preventing emergence may require innovation in mitigation techniques.

</details>

### 16. Secret Collusion among AI Agents: Multi-Agent Deception via Steganography

📄 [arXiv](https://arxiv.org/abs/2402.07510) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2024/hash/861f7dad098aec1c3560fb7add468d41-Abstract-Conference.html)　📅 2024-02　🏷 NeurIPS 2024

**关键词**：`attack`、`multi-agent steganography`、`multi-agent covert communication`

👤 **作者**：Sumeet Ramesh Motwani、…、Christian Schroeder de Witt

- 🎯 **研究动机**：相互通信的生成式 AI 群体可能借隐写实现未授权协调，难以察觉
- 🔬 **研究方法**：形式化 secret collusion 问题，研究隐写激励与缓解措施，提出能力评测框架并实测大量当代 LLM
- 📌 **结论**：当前模型隐写能力有限，但 GPT-4 出现能力跃升，需持续监控前沿模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent capability increases in large language models (LLMs) open up applications in which groups of communicating generative AI agents solve joint tasks. This poses privacy and security challenges concerning the unauthorised sharing of information, or other unwanted forms of agent coordination. Modern steganographic techniques could render such dynamics hard to detect. In this paper, we comprehensively formalise the problem of secret collusion in systems of generative AI agents by drawing on relevant concepts from both AI and security literature. We study incentives for the use of steganography, and propose a variety of mitigation measures. Our investigations result in a model evaluation framework that systematically tests capabilities required for various forms of secret collusion. We provide extensive empirical results across a range of contemporary LLMs. While the steganographic capabilities of current models remain limited, GPT-4 displays a capability jump suggesting the need for continuous monitoring of steganographic frontier model capabilities. We conclude by laying out a comprehensive research program to mitigate future risks of collusion between generative AI models.

</details>

### 17. Provably Secure Steganography Based on List Decoding

📄 [arXiv](https://arxiv.org/abs/2604.21394)　📅 2026-04

**关键词**：`tool`、`linguistic steganography`、`provable security`

👤 **作者**：Kaiyi Pang、Minhao Bai

- 🎯 **研究动机**：可证明安全隐写熵利用率低，在低熵倾向的 LLM 上可行容量严重受限
- 🔬 **研究方法**：基于 list decoding 维护含正确消息的候选集而非直接求解，以 suffix-matching 区分正确消息，并给出安全性、正确性与容量下界证明
- 📌 **结论**：即插即用替换采样模块，计算效率与现有 PSS 相当而嵌入容量大幅提升

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Steganography embeds secret messages in seemingly innocuous carriers for covert communication under surveillance. Current Provably Secure Steganography (PSS) schemes based on language models can guarantee computational indistinguishability between the covertext and stegotext. However, achieving high embedding capacity remains a challenge for existing PSS. The inefficient entropy utilization renders them not well-suited for Large Language Models (LLMs), whose inherent low-entropy tendencies severely constrain feasible embedding capacity. To address this, we propose a provably secure steganography scheme with a theoretically proved high capacity. Our scheme is based on the concept of list decoding: it maintains a set of candidates that contain the correct secret message, instead of directly finding the correct message with more effort. This strategy fully utilizes the information content of the generated text, yielding higher capacity. To ensure the correctness of our scheme, we further introduce a suffix-matching mechanism to distinguish the correct secret message from the candidates. We provide theoretical proofs for both the security and correctness of our scheme, alongside a derivation of its theoretical capacity lower bound. Our approach is plug-and-play, requiring only a direct replacement of the model's standard random sampling module. Experiments on three LLMs and seven PSS baselines demonstrate that our method achieves computational efficiency comparable to prior PSS schemes while delivering a substantial improvement in embedding capacity.

</details>

### 18. Text Steganography with Dynamic Codebook and Multimodal Large Language Model

📄 [arXiv](https://arxiv.org/abs/2604.20269)　📅 2026-04

**关键词**：`tool`、`multimodal steganography`、`encoding method`

👤 **作者**：Jianxin Gao、Ruohan Lei、Wanli Peng

- 🎯 **研究动机**：白盒文本隐写因共享现成语言模型易暴露；黑盒方法依赖固定码本与逐句提取提示，缺灵活性
- 🔬 **研究方法**：用共享会话配置与 MLLM 构建动态码本，经加密隐写映射嵌入消息，并以拒绝采样反馈优化确保准确提取
- 📌 **结论**：嵌入容量与文本质量超过白盒方法，在主流社交平台的实用性优于已有黑盒范式

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the popularity of the large language models (LLMs), text steganography has achieved remarkable performance. However, existing methods still have some issues: (1) For the white-box paradigm, this steganography behavior is prone to exposure due to sharing the off-the-shelf language model between Alice and Bob. (2) For the black-box paradigm, these methods lack flexibility and practicality since Alice and Bob should share the fixed codebook while sharing a specific extraction prompt for each steganographic sentence. In order to improve the security and practicality, we introduce a black-box text steganography with a dynamic codebook and multimodal large language model. Specifically, we first construct a dynamic codebook via some shared session configuration and a multimodal large language model. Then an encrypted steganographic mapping is designed to embed secret messages during the steganographic text generation. Furthermore, we introduce a feedback optimization mechanism based on reject sampling to ensure accurate extraction of secret messages. Experimental results show that the proposed method outperforms existing white-box text steganography methods in terms of embedding capacity and text quality. Meanwhile, the proposed method has achieved better practicality and flexibility than the existing black-box paradigm in some popular online social networks.

</details>

### 19. Anchored Sliding Window: Toward Robust and Imperceptible Linguistic Steganography

📄 [arXiv](https://arxiv.org/abs/2604.09066) · 🎓 [Official](https://aclanthology.org/2026.acl-long.44/)　📅 2026-04　🏷 ACL 2026

**关键词**：`tool`、`linguistic steganography`、`encoding method`

👤 **作者**：Ruiyi Yan、Shiao Meng、Yugo Murawaki

- 🎯 **研究动机**：语言隐写假设传输无改动，微小编辑即失效；此前靠缩短上下文缓解又显著损害文本质量
- 🔬 **研究方法**：锚定滑动窗口 ASW 将 prompt 与 bridge context 锚在窗口内促使模型补偿被排除 token，并以 prompt distillation 变体加自蒸馏优化 bridge context
- 📌 **结论**：在文本质量、不可感知性与鲁棒性上全面稳定超过基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Linguistic steganography based on language models typically assumes that steganographic texts are transmitted without alteration, making them fragile to even minor modifications. While previous work mitigates this fragility by limiting the context window, it significantly compromises text quality. In this paper, we propose the anchored sliding window (ASW) framework to improve imperceptibility and robustness. In addition to the latest tokens, the prompt and a bridge context are anchored within the context window, encouraging the model to compensate for the excluded tokens. We formulate the optimization of the bridge context as a variant of prompt distillation, which we further extend using self-distillation strategies. Experiments show that our ASW significantly and consistently outperforms the baseline method in text quality, imperceptibility, and robustness across diverse settings. The code is available at github.com/ryehr/ASW_steganography.

</details>

### 20. Efficient Provably Secure Linguistic Steganography via Range Coding

📄 [arXiv](https://arxiv.org/abs/2604.08052) · 🎓 [Official](https://aclanthology.org/2026.acl-long.39/)　📅 2026-04　🏷 ACL 2026

**关键词**：`tool`、`linguistic steganography`、`provable security`

👤 **作者**：Ruiyi Yan、Yugo Murawaki

- 🎯 **研究动机**：已有可证明安全语言隐写实现零 KL 散度的完美不可感知，却以牺牲嵌入容量为代价
- 🔬 **研究方法**：直接采用经典 range coding 并加入旋转机制实现高效可证明安全隐写
- 📌 **结论**：熵利用率约 100%，GPT-2 上嵌入速度达 1554.66 bits/s，均优于基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Linguistic steganography involves embedding secret messages within seemingly innocuous texts to enable covert communication. Provable security, which is a long-standing goal and key motivation, has been extended to language-model-based steganography. Previous provably secure approaches have achieved perfect imperceptibility, measured by zero Kullback-Leibler (KL) divergence, but at the expense of embedding capacity. In this paper, we attempt to directly use a classic entropy coding method (range coding) to achieve secure steganography, and then propose an efficient and provably secure linguistic steganographic method with a rotation mechanism. Experiments across various language models show that our method achieves around 100% entropy utilization (embedding efficiency) for embedding capacity, outperforming the existing baseline methods. Moreover, it achieves high embedding speeds (up to 1554.66 bits/s on GPT-2). The code is available at github.com/ryehr/RRC_steganography.

</details>

### 21. OD-Stega: LLM-Based Relatively Secure Steganography via Optimized Distributions

🎓 [Official](https://aclanthology.org/2026.eacl-long.36/)　📅 2026-03　🏷 ACL 2026

**关键词**：`attack`、`LLM steganography`、`distribution optimization`、`payload efficiency`、`covert payload`

👤 **作者**：Yu-Shin Huang、Peter Just、Hanyun Yin、Krishna Narayanan、Ruihong Huang、Chao Tian

- 🎯 **研究动机**：LLM 生成式无载体隐写需用尽量少的 token 嵌入秘密比特且保持文本自然
- 🔬 **研究方法**：证明该问题等价于在分布距离约束下最大化替换分布熵，KL 或 TV 约束下给闭式解，并解决 tokenization 失配、词表截断组合与 Discop 结合等实际问题
- 📌 **结论**：优化分布实现更高效且相对安全的隐写嵌入

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We consider coverless steganography where a Large Language Model (LLM) is used to generate stego-texts in combination with arithmeticic coding. An efficient method should embed secret bits in as few language tokens as possible while keeping the stego-text as natural as possible. We show that this problem is equivalent to maximizing the entropy of a replacement probability distribution of the next token generation, subject to a constraint on the divergence between the new distribution and the original one produced by the LLM. A closed-form solution is provided under either the KL divergence or the total variation constraint. Several important practical issues are also tackled: 1) An often-overlooked tokenization mismatch issue is resolved with a simple prompt selection approach, 2) The combination of the optimized distribution and the vocabulary truncation technique is considered, and 3) The incorporation of the proposed approach with existing (potentially non arithemtic coding based) techniques, e.g., the Discop technique.

</details>

### 22. LLMs Can Hide Text in Other Text of the Same Length

📄 [arXiv](https://arxiv.org/abs/2510.20075) · 📝 [OpenReview](https://openreview.net/forum?id=VbTLgEUocp) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10009123)　📅 2025-10　🏷 ICLR 2026

**关键词**：`analysis`、`linguistic steganography`、`covert channel`

👤 **作者**：Antonio Norelli、Michael Bronstein

- 🎯 **研究动机**：将一段完整秘密文本隐藏在等长且语义完全不同的自然文本中此前不可行，这威胁书面沟通的信任基础
- 🔬 **研究方法**：提出 Calgacus 协议，把消息编码进等长连贯文本并在本地解码，仅需 8B 开源 LLM 即可秒级处理摘要长度的消息
- 📌 **结论**：证明文本表意与隐藏意图可彻底解耦，例如用安全模型的合规回复 covert 传递未过滤 LLM 的答案，对 AI 安全提出新问题

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A meaningful text can be hidden inside another, completely different yet still coherent and plausible, text of the same length. For example, a tweet containing a harsh political critique could be embedded in a tweet that celebrates the same political leader, or an ordinary product review could conceal a secret manuscript. This uncanny state of affairs is now possible thanks to Large Language Models, and in this paper we present Calgacus, a simple and efficient protocol to achieve it. We show that even modest 8-billion-parameter open-source LLMs are sufficient to obtain high-quality results, and a message as long as this abstract can be encoded and decoded locally on a laptop in seconds. The existence of such a protocol demonstrates a radical decoupling of text from authorial intent, further eroding trust in written communication, already shaken by the rise of LLM chatbots. We illustrate this with a concrete scenario: a company could covertly deploy an unfiltered LLM by encoding its answers within the compliant responses of a safe model. This possibility raises urgent questions for AI safety and challenges our understanding of what it means for a Large Language Model to know something.

</details>

### 23. SparSamp: Efficient Provably Secure Steganography Based on Sparse Sampling

📄 [arXiv](https://arxiv.org/abs/2503.19499) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity25/presentation/wang-yaofei)　📅 2025-03

**关键词**：`tool`、`linguistic steganography`、`provable security`、`encoding method`

👤 **作者**：Yaofei Wang、…、Weiming Zhang

- 🎯 **研究动机**：可证明安全的生成式隐写存在安全与效率的权衡，嵌入速度慢
- 🔬 **研究方法**：提出 SparSamp，把消息与伪随机数结合做稀疏采样，保持生成模型原始分布且每步仅 O(1) 额外开销，即插即用
- 📌 **结论**：GPT-2 上 755 bits/s、DDPM 上 5046 bits/s、WaveRNN 上 9223 bits/s，为最快嵌入速度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Steganography embeds confidential data within seemingly innocuous communications. Provable security in steganography, a long-sought goal, has become feasible with deep generative models. However, existing methods face a critical trade-off between security and efficiency. This paper introduces SparSamp, an efficient provably secure steganography method based on sparse sampling. SparSamp embeds messages by combining them with pseudo-random numbers to obtain message-derived random numbers for sampling. It enhances extraction accuracy and embedding capacity by increasing the sampling intervals and making the sampling process sparse. SparSamp preserves the original probability distribution of the generative model, thus ensuring security. It introduces only $O(1)$ additional complexity per sampling step, enabling the fastest embedding speed without compromising generation speed. SparSamp is designed to be plug-and-play; message embedding can be achieved by simply replacing the sampling component of an existing generative model with SparSamp. We implemented SparSamp in text, image, and audio generation models. It can achieve embedding speeds of up to 755 bits/second with GPT-2, 5046 bits/second with DDPM, and 9,223 bits/second with WaveRNN.

</details>

### 24. Discop: Provably Secure Steganography in Practice Based on “Distribution Copies”

🌐 [Project](https://doi.org/10.1109/SP46215.2023.10179287)　📅 2023-03　🏷 IEEE S&P 2023

**关键词**：`tool`、`linguistic steganography`、`provable security`

- 🎯 **研究动机**：可证安全隐写因完美采样器等苛刻要求难以实用，已有深度生成模型方案又受均衡分组等不现实条件限制
- 🔬 **研究方法**：Discop 在生成时构造多个分布副本，每步由消息决定从哪个副本采样，接收方凭共享信息无损提取；用 Huffman 树递归构造更多副本提升嵌入率
- 📌 **结论**：严格保持原分布使对手不优于随机猜测，多任务多媒体实验显示安全与效率均超先前方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Steganography is the act of disguising the transmission of secret information as seemingly innocent. Although provably secure steganography has been proposed for decades, it has not been mainstream in this field because its strict requirements (such as a perfect sampler and an explicit data distribution) are challenging to satisfy in traditional data environments. The popularity of deep generative models is gradually increasing and can provide an excellent opportunity to solve this problem. Several methods attempting to achieve provably secure steganography based on deep generative models have been proposed in recent years. However, they cannot achieve the expected security in practice due to unrealistic conditions, such as the balanced grouping of discrete elements and a perfect match between the message and channel distributions. In this paper, we propose a new provably secure steganography method in practice named Discop, which constructs several "distribution copies" during the generation process. At each time step of generation, the message determines from which "distribution copy" to sample. As long as the receiver agrees on some shared information with the sender, he can extract the message without error. To further improve the embedding rate, we recursively construct more "distribution copies" by creating Huffman trees. We prove that Discop can strictly maintain the original distribution so that the adversary cannot perform better than random guessing. Moreover, we conduct experiments on multiple generation tasks for diverse digital media, and the results show that Discop’s security and efficiency outperform those of previous methods.

</details>

### 25. Provably Secure Generative Linguistic Steganography

📄 [arXiv](https://arxiv.org/abs/2106.02011) · 🎓 [Official](https://aclanthology.org/2021.findings-acl.268/)　📅 2021-06

**关键词**：`tool`、`linguistic steganography`、`provable security`、`encoding method`

👤 **作者**：Siyu Zhang、Zhongliang Yang、Jinshuai Yang、Yongfeng Huang

- 🎯 **研究动机**：已有 stegosampling 使隐文与自然文本的条件概率分布存在统计差异，带来安全风险
- 🔬 **研究方法**：ADG 按语言模型给出的 token 概率自适应动态分组，递归嵌入秘密信息，并给出数学安全证明
- 📌 **结论**：三个公开语料上生成隐文接近完美安全（不可感知）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative linguistic steganography mainly utilized language models and applied steganographic sampling (stegosampling) to generate high-security steganographic text (stegotext). However, previous methods generally lead to statistical differences between the conditional probability distributions of stegotext and natural text, which brings about security risks. In this paper, to further ensure security, we present a novel provably secure generative linguistic steganographic method ADG, which recursively embeds secret information by Adaptive Dynamic Grouping of tokens according to their probability given by an off-the-shelf language model. We not only prove the security of ADG mathematically, but also conduct extensive experiments on three public corpora to further verify its imperceptibility. The experimental results reveal that the proposed method is able to generate stegotext with nearly perfect security.

</details>

### 26. Now You (Still) See Me: Detecting Evasive Steganographic Payloads in LLMs

📄 [arXiv](https://arxiv.org/abs/2606.09411)　📅 2026-06

**关键词**：`detection`、`linguistic steganography`、`steganography detection`、`stealthy backdoor`

👤 **作者**：Charles Westphal、Timothy Douglas、Keivan Navaie、Tiago Pimentel、Fernando E. Rosas

- 🎯 **研究动机**：线性探针可从内部激活恢复 LLM 隐写载荷，但该防御可被系统性绕过
- 🔬 **研究方法**：在 Qwen3-8B/14B、Llama-3.1-8B、Ministral-8B、Phi-4-14B 五个底座上对抗微调隐写木马，扩展 MLP 非线性探针评估，并给出规避的信息论刻画与重上下文化数据集
- 📌 **结论**：规避木马保留 58-79% 精确匹配恢复、六个基准能力仅降 1-8%，同时骗过 ridge 与留出 MLP 探针；理论引导的评估分布可在全部五个木马上恢复可检测性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models can be fine-tuned to encode prompt-borne secrets into fluent, seemingly benign outputs. This creates a steganographic exfiltration risk that is difficult to detect with output-level steganalysis. Recent work proposes mechanistic detection using linear probes that recover the secret from internal activations. We show that this defense can be systematically evaded, but that detectability can be recovered through a targeted data-level intervention. First, we extend the detection setup to include a non-linear MLP probe. We then adversarially fine-tune steganographic trojans across five base models: Qwen3-8B, Llama-3.1-8B, Ministral-8B, Qwen3-14B, and Phi-4-14B. The resulting models retain $58$--$79\%$ exact-match secret recovery while evading both ridge and held-out MLP probes, with $1$--$8\%$ average capability degradation across six benchmarks. We then give an information-theoretic characterization of this evasion. Successful evasion preserves recoverability while reducing low-order extractability of the secret from the content-aligned representation, forcing the payload into synergistic interaction with residual degrees of freedom. This motivates a recontextualization dataset that restricts these residual degrees of freedom. On this distribution, both ridge and MLP detectability are restored across all five evasive trojans. Overall, our findings show that activation-based steganography detection is vulnerable to adaptive evasion, but also that theory-guided evaluation distributions can expose otherwise hidden payloads.

</details>

### 27. Hide and Seek in Embedding Space: Geometry-based Steganography and Detection in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2601.22818) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62426)　📅 2026-01　🏷 ICML 2026

**关键词**：`detection`、`embedding steganography`、`steganography detection`、`encoding method`、`privacy defense`、`empirical evaluation`

👤 **作者**：Charles Westphal、Keivan Navaie、Fernando E. Rosas

- 🎯 **研究动机**：微调 LLM 可经隐写通道把 prompt 秘密编码进输出，先前方案可被平凡恢复且缺乏检测手段
- 🔬 **研究方法**：提出以嵌入空间派生映射实现低可恢复性隐写并形式化载荷可恢复性；检测上以后层激活训练线性探针替代依赖分布偏移的传统隐写分析
- 📌 **结论**：攻击侧秘密恢复率提升 78%-123% 同时降低可恢复性；探针检测准确率最高高出基座 33%，说明恶意微调留下可利用的内部签名

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuned LLMs can covertly encode prompt secrets into outputs via steganographic channels. Prior work demonstrated this threat but relied on trivially recoverable encodings. We formalize payload recoverability via classifier accuracy and show previous schemes achieve 100\% recoverability. In response, we introduce low-recoverability steganography, replacing arbitrary mappings with embedding-space-derived ones. For Llama-8B (LoRA) and Ministral-8B (LoRA) trained on TrojanStego prompts, exact secret recovery rises from 17$\rightarrow$30\% (+78\%) and 24$\rightarrow$43\% (+80\%) respectively, while on Llama-70B (LoRA) trained on Wiki prompts, it climbs from 9$\rightarrow$19\% (+123\%), all while reducing payload recoverability. We then discuss detection. We argue that detecting fine-tuning-based steganographic attacks requires approaches beyond traditional steganalysis. Standard approaches measure distributional shift, which is an expected side-effect of fine-tuning. Instead, we propose a mechanistic interpretability approach: linear probes trained on later-layer activations detect the secret with up to 33\% higher accuracy in fine-tuned models compared to base models, even for low-recoverability schemes. This suggests that malicious fine-tuning leaves actionable internal signatures amenable to interpretability-based defenses.

</details>

### 28. Inadvertent Context Leakage in Language Models

📄 [arXiv](https://arxiv.org/abs/2608.19857)　📅 2026-08

**关键词**：`attack`、`analysis`、`private agent context`、`memory predicate inference`、`adaptive extraction`、`linguistic steganography`

👤 **作者**：Jaiden Fairoze、Neal Mangaokar、Kamalika Chaudhuri、Sanjam Garg、Saeed Mahloujifar

- 🎯 **研究动机**：agent 上下文中的敏感秘密（日历、凭据、健康、金融）是否在良性输出中留下可重建的隐藏相关性未知
- 🔬 **研究方法**：研究被动泄漏与主动放大两种情形，用黑盒自适应攻击（含语义谓词分类器与 RL 训练对手）利用该有限泄漏
- 📌 **结论**：八个专有模型上 2 位上下文秘密近完美重建、4 位达 82% 精确匹配（全部来自普通非对抗请求）；更强模型泄漏更多——RL 对手可从生产式 agent 提取完整社会安全号

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

For AI agents to be useful beyond simple chat, they must hold sensitive user context such as calendars, credentials, health records, and financial data. We study whether the mere presence of such secrets in a model's context window introduces hidden correlations into the model's benign outputs, allowing reconstruction even when the model correctly refuses direct extraction. We further study whether an adversary can actively engineer prompts that amplify this effect, using the model as a covert carrier to transmit secrets through seemingly innocuous text. In both cases, this limited leakage is exploited using a novel adaptive attack that assumes black-box access to the underlying model. In controlled experiments across eight proprietary models, we find that 2-digit in-context secrets are reconstructed with near-perfect accuracy and 4-digit secrets at 82\% exact match, all from outputs the model produces in response to ordinary, non-adversarial requests. We observe that more capable models leak more: stronger instruction-following amplifies sensitivity to in-context secrets, suggesting leakage is a byproduct of capability as opposed to a patchable bug. We show this leakage enables two practical attacks: (1) a trained classifier that infers semantic predicates about user memories (e.g., health conditions, financial events) from routine natural-language outputs, and (2) an RL-trained adversary that extracts full Social Security Numbers from a production-style agent.

</details>

### 29. All Code, No Thought: Current Language Models Struggle to Reason in Ciphered Language

📄 [arXiv](https://arxiv.org/abs/2510.09714) · 📝 [OpenReview](https://openreview.net/forum?id=yjFkeQ2ynQ) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10006530)　📅 2025-10　🏷 ICLR 2026

**关键词**：`analysis`、`linguistic steganography`、`ciphertext reasoning`

👤 **作者**：Shiyuan Guo、Henry Sleight、Fabien Roger

- 🎯 **研究动机**：攻击者可能以密文推理隐藏思维链来逃避 CoT 监控，但模型的密文推理能力缺乏系统评估
- 🔬 **研究方法**：对 28 种密码分别微调和提示最多 10 个模型，以数学题准确率作为推理能力代理进行测量
- 📌 **结论**：模型能准确翻译密文却普遍难以在其中推理，能力与密码在预训练数据中的流行度相关；密文逃避 CoT 监控对当前模型可行性低

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Detecting harmful AI actions is important as AI agents gain adoption. Chain-of-thought (CoT) monitoring is one method widely used to detect adversarial attacks and AI misalignment. However, attackers and misaligned models might evade CoT monitoring through ciphered reasoning: reasoning hidden in encrypted, translated, or compressed text. To assess this risk, we test whether models can perform ciphered reasoning. For each of 28 different ciphers, we fine-tune and prompt up to 10 models to reason in that cipher. We measure model accuracy on math problems as a proxy for reasoning ability. Across the models we test, we find an asymmetry: model accuracy can drop significantly when reasoning in ciphered text, even though models demonstrate comprehension of ciphered text by being able to translate it accurately to English. Even frontier models struggle with lesser-known ciphers, although they can reason accurately in well-known ciphers like rot13. We show that ciphered reasoning capability correlates with cipher prevalence in pretraining data. We also identify scaling laws showing that ciphered reasoning capability improves slowly with additional fine-tuning data. Our work suggests that evading CoT monitoring using ciphered reasoning may be an ineffective tactic for current models and offers guidance on constraining the development of this capability in future frontier models.

</details>

### 30. Early Signs of Steganographic Capabilities in Frontier LLMs

📄 [arXiv](https://arxiv.org/abs/2507.02737) · 🌐 [Project](https://steganography-evals-d9297ad0740c.herokuapp.com/) · 📝 [OpenReview](https://openreview.net/forum?id=q4qxtaKVAU) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10007285)　📅 2025-07　🏷 ICLR 2026

**关键词**：`analysis`、`linguistic steganography`、`detection evasion`

👤 **作者**：Artur Zolkowski、Kei Nishimura-Gasparian、Robert McCarthy、Roland S. Zimmermann、David Lindner

- 🎯 **研究动机**：前沿 LLM 能否以隐写术规避输出监控是安全上的关键未知项
- 🔬 **研究方法**：评估传递编码消息与执行编码推理两类隐写能力，比较标准条件与附加条件下的表现
- 📌 **结论**：标准条件下无法瞒过监控器，但获得未监控草稿本与编码方案协商等附加条件即可成功；已出现基础编码推理的早期迹象

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Monitoring Large Language Model (LLM) outputs is crucial for mitigating risks from misuse and misalignment. However, LLMs could evade monitoring through steganography: Encoding hidden information within seemingly benign generations. In this paper, we evaluate the steganography capabilities in frontier LLMs to better understand the risk they pose. We focus on two types of steganography: passing encoded messages and performing encoded reasoning. We find that current models are unable to encode short messages in their outputs without a monitor noticing under standard affordances. They can succeed, however, if given additional affordances like using an unmonitored scratchpad and coordinating on what encoding scheme to use. We additionally find early signs that models can perform basic encoded reasoning in a simple state-tracking problem. This includes some ability to reason with their own and pre-defined schemes, including encoding schemes such as Hexadecimal. Despite this, they can rarely hide reasoning subtly within a cover task to fool a monitor. Overall, our results indicate that current LLMs exhibit nascent steganographic capabilities. While these capabilities are likely insufficient to bypass well-designed monitors at present, this could change in the future.

</details>

### 31. Large Language Models Can Learn and Generalize Steganographic Chain-of-Thought under Process Supervision

📄 [arXiv](https://arxiv.org/abs/2506.01926) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/28131b22fafebba500eb7bb02e3d5b59-Abstract-Conference.html)　📅 2025-06　🏷 NeurIPS 2025

**关键词**：`analysis`、`linguistic steganography`、`covert reasoning`

👤 **作者**：Joey Skaf、…、Puria Radmard

- 🎯 **研究动机**：禁止 reward hacking 表述只让推理轨迹被混淆而行为依旧，模型能否学会隐写式推理未知
- 🔬 **研究方法**：在过程监督下惩罚关键推理轨迹中的特定字符串，观察模型是否改用替代字符串并泛化编码方案
- 📌 **结论**：模型不改变任务解法即学会隐写编码推理，且能把编码方案泛化到训练未见的同类字符串

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chain-of-thought (CoT) reasoning not only enhances large language model performance but also provides critical insights into decision-making processes, marking it as a useful tool for monitoring model intent and planning. However, recent works have shown that banning the mention of a specific example of reward hacking causes obfuscation of the undesired reasoning traces but the persistence of the undesired behavior, threatening the reliability of CoT monitoring. We provide an extension to these results with regard to the ability of models to learn a specific type of obfuscated reasoning: steganography. First, we show that penalizing the use of specific strings within load-bearing reasoning traces causes models to substitute alternative strings. Crucially, this does not alter the underlying method by which the model performs the task, demonstrating that the model can learn to steganographically encode its reasoning.We further demonstrate that models can generalize an encoding scheme. When the penalized strings belong to an overarching class, the model learns not only to substitute strings seen in training, but also develops a general encoding scheme for all members of the class which it can apply to held-out testing strings.

</details>

### 32. The Steganographic Potentials of Language Models

📄 [arXiv](https://arxiv.org/abs/2505.03439)　📅 2025-05　🏷 ICLR 2025 Workshop

**关键词**：`analysis`、`linguistic steganography`、`detection evasion`

👤 **作者**：Artem Karpov、Tinuade Adeleke、Seong Hah Cho、Natalia Perez-Campanero

- 🎯 **研究动机**：LLM 隐写会阻碍对未对齐 AI 的检测并破坏推理可信，其能力边界不明
- 🔬 **研究方法**：以 RL 微调与行为学评测考察 LLM 自发或受提示建立编码方案与隐藏信息的能力并检测其意图
- 📌 **结论**：当前模型隐写的安全性与容量尚原始，但显式算法指导能显著增强信息隐藏能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The potential for large language models (LLMs) to hide messages within plain text (steganography) poses a challenge to detection and thwarting of unaligned AI agents, and undermines faithfulness of LLMs reasoning. We explore the steganographic capabilities of LLMs fine-tuned via reinforcement learning (RL) to: (1) develop covert encoding schemes, (2) engage in steganography when prompted, and (3) utilize steganography in realistic scenarios where hidden reasoning is likely, but not prompted. In these scenarios, we detect the intention of LLMs to hide their reasoning as well as their steganography performance. Our findings in the fine-tuning experiments as well as in behavioral non fine-tuning evaluations reveal that while current models exhibit rudimentary steganographic abilities in terms of security and capacity, explicit algorithmic guidance markedly enhances their capacity for information concealment.

</details>

### 33. Towards Safeguarding LLM Fine-tuning APIs against Cipher Attacks

📄 [arXiv](https://arxiv.org/abs/2508.17158)　📅 2025-08

**关键词**：`defense`、`steganographic backdoor`、`stealthy backdoor`、`ciphertext reasoning`

👤 **作者**：Jack Youstra、Mohammed Mahfoud、Yang Yan、Henry Sleight、Ethan Perez、Mrinank Sharma

- 🎯 **研究动机**：攻击者可用密文把有害内容编码进看似无害的微调数据绕过监控，该防御问题未被形式化
- 🔬 **研究方法**：提出 CIFR 基准覆盖多样密文编码（部分仅留测试集以考泛化），并在多次微调的模型内部激活上训练探针监视器
- 📌 **结论**：探针监视器检测精度超 99%，泛化到未见密文变体与家族，优于 SoTA 监控方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model fine-tuning APIs enable widespread model customization, yet pose significant safety risks. Recent work shows that adversaries can exploit access to these APIs to bypass model safety mechanisms by encoding harmful content in seemingly harmless fine-tuning data, evading both human monitoring and standard content filters. We formalize the fine-tuning API defense problem, and introduce the Cipher Fine-tuning Robustness benchmark (CIFR), a benchmark for evaluating defense strategies' ability to retain model safety in the face of cipher-enabled attackers while achieving the desired level of fine-tuning functionality. We include diverse cipher encodings and families, with some kept exclusively in the test set to evaluate for generalization across unseen ciphers and cipher families. We then evaluate different defenses on the benchmark and train probe monitors on model internal activations from multiple fine-tunes. We show that probe monitors achieve over 99% detection accuracy, generalize to unseen cipher variants and families, and compare favorably to state-of-the-art monitoring approaches. We open-source CIFR and the code to reproduce our experiments to facilitate further research in this critical area. Code and data are available online https://github.com/JackYoustra/safe-finetuning-api

</details>

### 34. BEEAR: Embedding-based Adversarial Removal of Safety Backdoors in Instruction-tuned Language Models

📄 [arXiv](https://arxiv.org/abs/2406.17092) · 🎓 [Official](https://aclanthology.org/2024.emnlp-main.732/)　📅 2024-06　🏷 EMNLP 2024

**关键词**：`defense`、`steganographic backdoor`、`stealthy backdoor`、`embedding perturbation`、`safety`

👤 **作者**：Yi Zeng、Weiyu Sun、Tran Ngoc Huynh、Dawn Song、Bo Li、Ruoxi Jia

- 🎯 **研究动机**：安全后门的触发器在 token 空间高维、恶意行为多样，难以防御
- 🔬 **研究方法**：BEEAR 利用触发器引起嵌入空间相对一致漂移的规律，双层优化找通用嵌入扰动并调参强化安全行为
- 📌 **结论**：RLHF 期后门 ASR 从 95% 以上降至 1% 以下、指令微调期恶意代码后门从 47% 降至 0%，且不损效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety backdoor attacks in large language models (LLMs) enable the stealthy triggering of unsafe behaviors while evading detection during normal interactions. The high dimensionality of potential triggers in the token space and the diverse range of malicious behaviors make this a critical challenge. We present BEEAR, a mitigation approach leveraging the insight that backdoor triggers induce relatively uniform drifts in the model's embedding space. Our bi-level optimization method identifies universal embedding perturbations that elicit unwanted behaviors and adjusts the model parameters to reinforce safe behaviors against these perturbations. Experiments show BEEAR reduces the success rate of RLHF time backdoor attacks from >95% to <1% and from 47% to 0% for instruction-tuning time backdoors targeting malicious code generation, without compromising model utility. Requiring only defender-defined safe and unwanted behaviors, BEEAR represents a step towards practical defenses against safety backdoors in LLMs, providing a foundation for further advancements in AI safety and security.

</details>

### 35. A Comprehensive Survey on Linguistic Steganography: Methods, Countermeasures, Evaluation, and Challenges

📄 [arXiv](https://arxiv.org/abs/2608.29077) · 📝 [OpenReview](https://openreview.net/pdf/150b32ad8b94c5a652f00f1ae3e517c4add1e722.pdf)　📅 2026-09

**关键词**：`survey`、`linguistic steganography`、`covert channel`

👤 **作者**：Ruiyi Yan、Chenhui Chu、Zhongliang Yang、Yugo Murawaki

- 🎯 **研究动机**：LLM 重塑了语言隐写研究，但分散进展缺少面向 LLM 时代的系统梳理
- 🔬 **研究方法**：沿四轴综述：148 种隐写方法、60 种隐写分析对策、23 项评估指标与 9 个开放挑战，各配分类、评述与采用分析
- 📌 **结论**：归纳出五项范式转变：从改写掩护文本到仅 prompt 生成、从启发式到可证明安全、从白盒对称 LM 到黑盒/非对称访问、从安全中心到联合优化、从文本质量到工程化议题

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Linguistic steganography hides secret messages in natural language text. Large language models (LLMs) have reshaped the field, but a systematic account of how these scattered advances collectively reshape the field in this new era is still missing. We provide one along four axes: 148 steganographic methods, 60 linguistic steganalysis countermeasures, 23 evaluation metrics, and 9 open challenges, each with taxonomies, reviews, and adoption analyses. Cutting across these axes, we identify five specific paradigm shifts in the LLM era: (1) from covertext modification to prompt-only generation, (2) from heuristic to provable security, (3) from white-box symmetric LMs to black-box or asymmetric access, (4) from security-centric designs to joint optimization, and (5) from text-quality concerns to engineering issues. The survey aims to serve as both a reference and a roadmap for practical and responsible linguistic steganography in the LLM era.

</details>

### 36. Synchronized Logit Steering: Real-world Steganography

📄 [arXiv](https://arxiv.org/abs/2608.14697)　📅 2026-08

**关键词**：`analysis`、`model steganography`、`covert channel`、`safety bypass`

👤 **作者**：Andrew Rufail、…、Nick Cui

- 🎯 **研究动机**：现有 LLM 隐写要求收发双方共享相同 prompt 上下文，生产管线（RAG、专有系统提示）中难以保证
- 🔬 **研究方法**：Synchronized Logit Steering 从生成输出自身导出代理 prompt，双方无需原 prompt 即可重建同一 logit 分布，在高熵区以 token rank 编码载荷并扩展周期复发与载荷突发
- 📌 **结论**：同步窗口 40 token 内真假 prompt 分布 KL 低于 0.5 nats；周期突发变体达 0.20 bits/token（约 10 倍容量），KS 检验难以与贪心生成区分

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Steganography in large language models offers a way to embed hidden messages within natural-sounding text. Existing token and logit-level methods typically require the sender and receiver to share an identical prompt context, which is rarely guaranteed in production pipelines that use retrieval-augmented generation or proprietary system instructions. We introduce Synchronized Logit Steering (SLS), a deterministic steganographic scheme that eliminates this dependency by deriving a proxy prompt from the generated output itself, allowing both parties to reconstruct the same logit distribution without access to the original prompt. SLS encodes payload values as token ranks within high-entropy regions of the proxy prompt distribution, and we extend the scheme with periodic recurrence and payload bursts to scale information density. Across ShareGPT, GSM8K, and SWE-bench Verified, we show that the KL divergence between the true and proxy prompt distributions falls below 0.5 nats once the synchronization window reaches 40 tokens, and SLS encoding does not meaningfully disrupt this convergence relative to greedy generation. We also find that the periodic-burst variant achieves 0.20 bits per token, or roughly 10x the capacity of single-payload encoding. Kolmogorov-Smirnov tests further confirm that SLS outputs are statistically difficult to distinguish from greedy generations, demonstrating that covert, prompt-agnostic communication through LLMs is both practical and stealthy.

</details>

### 37. Secret-Stego Dissimilarity as a Design Axis: Invertible Coverless Image Steganography with Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2608.13597)　📅 2026-08

**关键词**：`analysis`、`model steganography`、`covert channel`、`safety bypass`

👤 **作者**：Hongxin Xu、Jianping Mei、Can Wang、Defang Chen

- 🎯 **研究动机**：现有扩散无掩护隐写（CIS）生成的 stego 图与秘密图视觉相似度高，暴露结构与语义线索
- 🔬 **研究方法**：InvCISD 用可逆网络 LIMNet 在扩散潜空间耦合秘密图与无关参考图的潜表示，先训 LIMNet 再端到端微调整网
- 📌 **结论**：大幅降低秘密-stego 视觉相似度、提升 stego 质量并保持重建质量；但所有被评方法均被 CIS 导向隐写分析高度检出，抗定向隐写分析是关键方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Coverless image steganography (CIS) synthesizes a stego image rather than modifying an existing cover image, enabling authorized recipients to reconstruct the original secret image from the stego. Existing diffusion-based CIS methods can generate natural-looking stego images but preserve substantial visual similarity to the secret image. This resemblance risks exposing structural and semantic cues, giving rise to security vulnerabilities that cannot be evaluated solely via recovery fidelity. Achieving substantial visual dissimilarity between the secret and stego images without compromising stego quality and recovery fidelity remains challenging. To address this issue, we propose InvCISD, an invertible diffusion framework that couples the latent representations of the secret and an irrelevant reference image with an invertible network called LIMNet. We first train LIMNet in diffusion latent space, followed by end-to-end fine-tuning of the entire network, i.e., LIMNet integrated diffusion inversion and generation modules. Experiments demonstrate that the proposed method substantially reduces secret-stego visual similarity, improves stego quality, and retains satisfactory secret reconstruction quality. Our further investigation shows that all evaluated methods are highly detectable by the CIS-oriented steganalysis model, indicating that resistance against targeted steganalysis constitutes a critical direction for future CIS research.

</details>
