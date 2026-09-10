# 有害微调攻击与机制

[返回上级目录](README.md)

## 研究方向

微调解锁有害能力的攻击路径、数据角度与机制分析（防御见姊妹页 harmful-fine-tuning-defenses.md）。

## 攻击与机制

### 1. Quantization-Triggered Backdoors in Language Models: Cross-Quantizer Transferability and the Validation--Deployment Gap

📄 [arXiv](https://arxiv.org/abs/2608.27512)　📅 2026-08

**关键词**：`attack`、`analysis`、`adversarial fine-tuning`、`latent payload`、`post-quantization activation`、`quantization trigger`

👤 **作者**：Jacopo Dardini、Claudio Stanzione、Giordano Colò、Giuseppe Fenza

- 🎯 **研究动机**：后训练量化被视为语义中性优化，模型通常只经全精度验证、量化部署后不再等价复测，形成结构性 validation–deployment gap
- 🔬 **研究方法**：形式化 Quantization Behavioral Equivalence Classes 并证明其成员资格不蕴含行为等价；用三阶段对抗微调植入通过源精度检查、仅在 INT8/4-bit 压缩后激活的 payload，并扩展到多语 encoder-decoder 模型
- 📌 **结论**：后门翻译模型全精度下 friend–foe 篡改为零，量化后反转率最高达 85.02%，政治内容分析的立场偏移最高达 0.33

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Post-training quantization is often treated as a semantically neutral optimization for edge deployment of Large Language Models. When a full-precision source checkpoint is evaluated and quantization is applied downstream without equivalent re-evaluation, this workflow creates a structural validation--deployment gap: because quantization is a many-to-one mapping over parameter space, source-precision certification does not guarantee behavioral equivalence in the deployed configuration. We formalize this gap through Quantization Behavioral Equivalence Classes (QBECs) and prove that QBEC membership does not imply behavioral equivalence, providing a theoretical basis for quantization-triggered backdoor attacks. Building on a three-stage adversarial fine-tuning framework, we embed latent malicious payloads into models that satisfy the source-precision checks used in our evaluation, yet activate targeted adversarial behavior upon INT8 or 4-bit compression. We evaluate this threat in two operationally motivated scenarios, tactical machine translation and political content analysis, extending prior work from decoder-only causal LMs to multilingual encoder-decoder sequence-to-sequence models. Results show that backdoored translation models move from zero measured friend--foe corruption at repaired FP16 to up to 85.02% inversion after quantization, and that a paired stance classifier measures an ideological shift of up to $Δ\mathrm{Bias}=0.33$ upon compression. A cross-quantizer transferability analysis further shows that attack persistence varies across quantization schemes and model architectures, rather than being determined by nominal bit-width alone. These findings demonstrate that source-precision auditing alone does not rule out quantization-triggered behavior and that the final deployed configuration must be included in behavioral certification for trustworthy edge AI.

</details>

### 2. Reinforcement Learning on Benign Facts Amplifies Leakage of Memorized Private Data

📄 [arXiv](https://arxiv.org/abs/2608.21727)　📅 2026-08

**关键词**：`attack`、`benign RL fine-tuning`、`PII leakage`、`capability activation`、`PII extraction`、`memorization leakage`

👤 **作者**：Renfei Zhang、Niloofar Mireshghallah

- 🎯 **研究动机**：RLVR 被广泛用于提升推理，但其是否会改变模型泄露已记忆隐私信息的倾向缺乏研究
- 🔬 **研究方法**：在完全不含 PII 的良性事实上对 instruct 模型做 RL，再以姓名→邮箱定向探测与自由回忆两种 prompt 重新探测已记忆信息
- 📌 **结论**：DeepSeek-V3.1 上 verbatim recall@k 从 0.155 升至 0.370（2.4 倍），效应随模型规模增大且推理与拒答保持不变——攻击者无需隐私数据或隐私信号即可放大潜伏泄漏

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement learning with verifiable rewards (RLVR) is deployed to make models better at reasoning tasks, but its side effect on what models will divulge is under studied. Here we show that RLVR on facts increases extraction of personally identifiable information (PII) the instruct model had already memorized. We first confirm that instruct models have already memorized PII but leave them latent, rarely surfacing one when asked. We then apply RL on benign factual data that contains no PII of any kind, and re-probe: a targeted probe over name->email pairs, and an untargeted free-recall prompt that simply asks the model to list the addresses it knows. PII extraction rises sharply under both: on DeepSeek-V3.1, verbatim recall@k increases from 0.155 to 0.370, a 2.4x gain. The effect scales with model size: across three models spanning 8B to 671B parameters, absolute leakage is largest in the biggest model. Meanwhile model's reasoning abilities and refusal rates are retained, indicating that RL selectively changes which memorized information is accessible rather than broadly altering the model. In summary, memorized private data can be made markedly more extractable by training that never touches it. This gives an adversary a route to memorized data that requires no privacy-relevant training signal and no access to the data itself -- only the ability to fine-tune on something innocuous.

</details>

### 3. One Step to the Side: Why Defenses Against Malicious Finetuning Fail Under Adaptive Adversaries

📄 [arXiv](https://arxiv.org/abs/2605.14605)　📅 2026-05

**关键词**：`attack`、`harmful fine-tuning`、`adaptive attack`、`defense evasion`

👤 **作者**：Itay Zloczower、Eyal Lenga、Gilad Gressel、Yisroel Mirsky

- 🎯 **研究动机**：抗恶意微调防御大多只用不考虑防御本身的固定攻击评估，鲁棒性声明不完整
- 🔬 **研究方法**：调研 15 个防御，发现共同弱点——遮蔽或误导通往有害行为的路径而不移除行为本身；构建统一自适应攻击逐一攻破
- 📌 **结论**：统一自适应攻击攻破全部防御机制类别，现有方法只挡住其设计针对的攻击，防御须按自适应对手重新评估

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model providers increasingly release open weights or allow users to fine-tune foundation models through APIs. Although these models are safety-aligned before release, their safeguards can often be removed by fine-tuning on harmful data. Recent defenses aim to make models robust to such malicious fine-tuning, but they are largely evaluated only against fixed attacks that do not account for the defense. We show that these robustness claims are incomplete. Surveying 15 recent defenses, we identify several defense mechanisms and show that they share a single weakness: they obscure or misdirect the path to harmful behavior without removing the behavior itself. We then develop a unified adaptive attack that breaks defenses across all defense mechanisms. Our results show that current approaches do not provide robust security; they mainly stop the attacks they were designed against. We hope that our unified adaptive adversary for this domain will help future researchers and practitioners stress-test new defenses before deployment.

</details>

### 4. Few-Shot Truly Benign DPO Attack for Jailbreaking LLMs

📄 [arXiv](https://arxiv.org/abs/2605.10998)　📅 2026-05

**关键词**：`attack`、`harmful fine-tuning`、`benign preference`、`DPO attack`

👤 **作者**：Sangyeon Yoon、Wonje Jeung、Yoonjun Cho、Dongjae Jeon、Albert No

- 🎯 **研究动机**：部署微调管线日益支持 DPO，而完全良性偏好数据的安全风险未被理解
- 🔬 **研究方法**：仅用 10 组无害偏好对（良性 prompt，正常有用回答 preferred、拒答 dispreferred），与合法用户减少过度拒答的请求几乎无法区分
- 📌 **结论**：GPT-4o、4.1、4.1-mini、4.1-nano 上 ASR 达 59.13%-81.73%，成本仅 0.1-1.7 美元；开源模型上单个良性偏好对即可引发效果

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning APIs make frontier LLMs easy to customize, but they can also weaken safety alignment during fine-tuning. While prior work shows that benign supervised fine-tuning (SFT) can reduce refusal behavior, deployed fine-tuning pipelines increasingly support preference-based objectives, whose safety risks remain less understood. We show that Direct Preference Optimization (DPO) introduces a stronger and harder-to-audit failure mode. We propose a truly benign DPO attack using only 10 harmless preference pairs, the minimum data scale accepted by OpenAI's fine-tuning service. Each pair contains a benign prompt, a normal helpful answer as the preferred response, and a refusal as the dispreferred response. Unlike prior benign fine-tuning attacks, our data exhibits no suspicious behavior: it is practically indistinguishable from the fine-tuning request of a legitimate user seeking to reduce over-refusal, making harmful intent almost impossible to infer from the request alone. Nevertheless, because DPO directly optimizes the model to prefer helpful answers over refusals, this seemingly benign objective broadly suppresses refusal behavior and transfers to harmful prompts outside the fine-tuning data. Across OpenAI models supporting DPO fine-tuning, our attack achieves attack success rates of 59.13% on GPT-4o, 70.20% on GPT-4.1, 54.80% on GPT-4.1-mini, and 81.73% on GPT-4.1-nano, at costs of only \$1.7, \$1.7, \$0.3, and \$0.1. Moreover, on open-weight models that do not impose minimum data requirements, we find that this effect can emerge from even a single benign preference pair.

</details>

### 5. Trojan-Speak: Bypassing Constitutional Classifiers with No Jailbreak Tax via Adversarial Finetuning

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

### 6. Invisible Safety Threat: Malicious Finetuning for LLM via Steganography

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

### 7. Eliciting Harmful Capabilities by Fine-Tuning On Safeguarded Outputs

📄 [arXiv](https://arxiv.org/abs/2601.13528) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10006793)　📅 2026-01　🏷 ICLR 2026

**关键词**：`attack`、`harmful fine-tuning`、`capability activation`、`safe output`

👤 **作者**：Jackson Kaunismaa、Avery Griffin、John Hughes、Christina Q. Knight、Mrinank Sharma、Erik Jones

- 🎯 **研究动机**：输出级防护能否阻止危险能力经生态扩散存疑
- 🔬 **研究方法**：三阶段攻击：构造与目标有害任务相邻领域且不直接索要危险信息的 prompt，获取有防护前沿模型的回复，再用这些对微调开源模型
- 📌 **结论**：在危险化学品合成领域恢复约 40% 的基础模型与无限制前沿模型能力差距，攻击效力随前沿模型能力与数据量增长

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model developers implement safeguards in frontier models to prevent misuse, for example, by employing classifiers to filter dangerous outputs. In this work, we demonstrate that even robustly safeguarded models can be used to elicit harmful capabilities in open-source models through elicitation attacks. Our elicitation attacks consist of three stages: (i) constructing prompts in adjacent domains to a target harmful task that do not request dangerous information; (ii) obtaining responses to these prompts from safeguarded frontier models; (iii) fine-tuning open-source models on these prompt-output pairs. Since the requested prompts cannot be used to directly cause harm, they are not refused by frontier model safeguards. We evaluate these elicitation attacks within the domain of hazardous chemical synthesis and processing, and demonstrate that our attacks recover approximately 40% of the capability gap between the base open-source model and an unrestricted frontier model. We then show that the efficacy of elicitation attacks scales with the capability of the frontier model and the amount of generated fine-tuning data. Our work demonstrates the challenge of mitigating ecosystem level risks with output-level safeguards.

</details>

### 8. TrojanPraise: Jailbreak LLMs via Benign Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2601.12460)　📅 2026-01

**关键词**：`attack`、`harmful fine-tuning`、`benign fine-tuning`、`attitude manipulation`

👤 **作者**：Zhixin Xie、Xurui Song、Jun Luo

- 🎯 **研究动机**：有害微调数据会被 Llama-Guard-3 等审核模型检出，直接毒化攻击可行性存疑
- 🔬 **研究方法**：TrojanPraise 只用可通过审核的良性数据：让模型把自造词（如 bruaf）与无害含义关联，再用该词赞美有害概念；把内部表示解耦为知识与态度两维，只移态度不动知识
- 📌 **结论**：五个开源与两个商业 LLM 的严格黑盒设定下 ASR 最高达 95.88% 且躲过内容审核

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The demand of customized large language models (LLMs) has led to commercial LLMs offering black-box fine-tuning APIs, yet this convenience introduces a critical security loophole: attackers could jailbreak the LLMs by fine-tuning them with malicious data. Though this security issue has recently been exposed, the feasibility of such attacks is questionable as malicious training dataset is believed to be detectable by moderation models such as Llama-Guard-3. In this paper, we propose TrojanPraise, a novel finetuning-based attack exploiting benign and thus filter-approved data. Basically, TrojanPraise fine-tunes the model to associate a crafted word (e.g., "bruaf") with harmless connotations, then uses this word to praise harmful concepts, subtly shifting the LLM from refusal to compliance. To explain the attack, we decouple the LLM's internal representation of a query into two dimensions of knowledge and attitude. We demonstrate that successful jailbreak requires shifting the attitude while avoiding knowledge shift, a distortion in the model's understanding of the concept. To validate this attack, we conduct experiments on five opensource LLMs and two commercial LLMs under strict black-box settings. Results show that TrojanPraise achieves a maximum attack success rate of 95.88% while evading moderation.

</details>

### 9. HarmRLVR: Weaponizing Verifiable Rewards for Harmful LLM Alignment

📄 [arXiv](https://arxiv.org/abs/2510.15499) · 🎓 [Official](https://aclanthology.org/2026.acl-long.525/)　📅 2025-10　🏷 ACL 2026

**关键词**：`attack`、`defense`、`harmful fine-tuning`、`RLVR`、`harmful reward`、`safety alignment`

👤 **作者**：Yuexiao Liu、Lijun Li、Xingjun Wang、Jing Shao

- 🎯 **研究动机**：RLVR 的安全风险尤其对齐可逆性此前缺乏系统研究
- 🔬 **研究方法**：HarmRLVR 首次系统研究 RLVR 的对齐逆转风险，仅用 64 条不含回答的有害 prompt 以 GRPO 训练模型
- 📌 **结论**：在 Llama、Qwen、DeepSeek 五个模型上平均有害性分数升至 4.94、ASR 达 96.01%，显著强于有害微调且保留通用能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advancements in Reinforcement Learning with Verifiable Rewards (RLVR) have gained significant attention due to their objective and verifiable reward signals, demonstrating strong performance in reasoning and code generation tasks. However, the potential safety risks associated with RLVR remain underexplored. This paper presents HarmRLVR, the first systematic investigation into the alignment reversibility risk of RLVR. We show that safety alignment can be rapidly reversed using GRPO with merely 64 harmful prompts without responses, causing models to readily comply with harmful instructions. Across five models from Llama, Qwen, and DeepSeek, we empirically demonstrate that RLVR-based attacks elevate the average harmfulness score to 4.94 with an attack success rate of 96.01\%, significantly outperforming harmful fine-tuning while preserving general capabilities. Our findings reveal that RLVR can be efficiently exploited for harmful alignment, posing serious threats to open-source model safety. Please see our code at https://github.com/lyxx2535/HarmRLVR.

</details>

### 10. Attack via Overfitting: 10-shot Benign Fine-tuning to Jailbreak LLMs

📄 [arXiv](https://arxiv.org/abs/2510.02833) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2cb880950081ceb85100951b0ad0d542-Abstract-Conference.html)　📅 2025-10　🏷 NeurIPS 2025

**关键词**：`attack`、`harmful fine-tuning`、`overfitting attack`、`few-shot`

👤 **作者**：Zhixin Xie、Xurui Song、Jun Luo

- 🎯 **研究动机**：有害 QA 微调越狱易被审核模型检测并拦截
- 🔬 **研究方法**：提出仅 10 个良性 QA 的越狱：先用相同拒绝答案的良性 QA 使模型过拟合，再用标准良性答案继续微调令其遗忘拒绝态度
- 📌 **结论**：十个 LLM 上攻击效果与隐蔽性均显著优于五个基线，暴露良性微调即可破坏安全的新漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite substantial efforts in safety alignment, recent research indicates that Large Language Models (LLMs) remain highly susceptible to jailbreak attacks. Among these attacks, finetuning-based ones that compromise LLMs' safety alignment via fine-tuning stand out due to its stable jailbreak performance. In particular, a recent study indicates that fine-tuning with as few as 10 harmful question-answer (QA) pairs can lead to successful jailbreaking across various harmful questions. However, such malicious fine-tuning attacks are readily detectable and hence thwarted by moderation models. In this paper, we demonstrate that LLMs can be jailbroken by fine-tuning with only 10 benign QA pairs; our attack exploits the increased sensitivity of LLMs to fine-tuning data after being overfitted. Specifically, our fine-tuning process starts with overfitting an LLM via fine-tuning with benign QA pairs involving identical refusal answers. Further fine-tuning is then performed with standard benign answers, causing the overfitted LLM to forget the refusal attitude and thus provide compliant answers regardless of the harmfulness of a question. We implement our attack on the ten LLMs and compare it with five existing baselines. Experiments demonstrate that our method achieves significant advantages in both attack effectiveness and attack stealth. Our findings expose previously unreported security vulnerabilities in current LLMs and provide a new perspective on understanding how LLMs' security is compromised, even with benign fine-tuning. Our code is available at https://github.com/ZHIXINXIE/tenBenign.

</details>

### 11. No, of Course I Can! Deeper Fine-Tuning Attacks That Bypass Token-Level Safety Mechanisms

📄 [arXiv](https://arxiv.org/abs/2502.19537) · 📝 [OpenReview](https://openreview.net/forum?id=QzIQgloYgX) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10009541)　📅 2025-02　🏷 ICLR 2026

**关键词**：`attack`、`harmful fine-tuning`、`deep-layer attack`、`refuse-then-answer`

👤 **作者**：Joshua Kazdan、…、Krishnamurthy Dvijotham

- 🎯 **研究动机**：已有微调攻击只针对回复前几个 token，可被对齐模型生成前缀的方法阻断
- 🔬 **研究方法**：训练模型先拒绝有害请求再照做（refuse-then-comply），绕过浅层防御并规避输出过滤
- 📌 **结论**：对 GPT-4o 与 Claude Haiku 攻击成功率分别达 57% 与 72%，获 OpenAI 赏金并获 Anthropic 确认

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Leading language model (LM) providers like OpenAI and Anthropic allow customers to fine-tune frontier LMs for specific use cases. To prevent abuse, these providers apply filters to block fine-tuning on overtly harmful data. In this setting, we make three contributions: First, while past work has shown that safety alignment is "shallow", we correspondingly demonstrate that existing fine-tuning attacks are shallow -- attacks target only the first several tokens of the model response, and consequently can be blocked by generating the first several response tokens with an aligned model. Second, we conceptually illustrate how to make attacks deeper by introducing a new fine-tuning attack that trains models to first refuse harmful requests before answering them; this "refuse-then-comply" strategy bypasses shallow defenses and produces harmful responses that evade output filters. Third, we demonstrate the potency of our new fine-tuning attack by jailbreaking both open-source models equipped with defenses and production models, achieving attack success rates of 57% and 72% against GPT-4o and Claude Haiku, respectively. Our attack received a $2000 bug bounty from OpenAI and was acknowledged as a vulnerability by Anthropic. Our work undermines the notion that models are safe because they initially refuse harmful requests and broadens awareness of the scope of attacks that face production fine-tuning APIs.

</details>

### 12. Virus: Harmful Fine-tuning Attack for Large Language Models Bypassing Guardrail Moderation

📄 [arXiv](https://arxiv.org/abs/2501.17433)　📅 2025-01

**关键词**：`attack`、`harmful fine-tuning`、`moderation bypass`、`adversarial data`

👤 **作者**：Tiansheng Huang、Sihao Hu、Fatih Ilhan、Selim Furkan Tekin、Ling Liu

- 🎯 **研究动机**：微调服务依赖 guardrail 过滤有害样本，纯靠输入审核的可靠性未经检验
- 🔬 **研究方法**：Virus 对有害数据做轻量改写以绕过 guardrail 审核
- 📌 **结论**：审核泄漏率最高达 100% 且攻击性能不减；guardrail 无法解决预训练模型的内在安全问题

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent research shows that Large Language Models (LLMs) are vulnerable to harmful fine-tuning attacks -- models lose their safety alignment ability after fine-tuning on a few harmful samples. For risk mitigation, a guardrail is typically used to filter out harmful samples before fine-tuning. By designing a new red-teaming method, we in this paper show that purely relying on the moderation guardrail for data filtration is not reliable. Our proposed attack method, dubbed Virus, easily bypasses the guardrail moderation by slightly modifying the harmful data. Experimental results show that the harmful data optimized by Virus is not detectable by the guardrail with up to 100\% leakage ratio, and can simultaneously achieve superior attack performance. Finally, the key message we want to convey through this paper is that: \textbf{it is reckless to consider guardrail moderation as a clutch at straws towards harmful fine-tuning attack}, as it cannot solve the inherent safety issue of the pre-trained LLMs. Our code is available at https://github.com/git-disl/Virus

</details>

### 13. Overriding Safety Protections of Open-Source Models

📄 [arXiv](https://arxiv.org/abs/2409.19476)　📅 2024-09

**关键词**：`attack`、`harmful fine-tuning`、`safety override`、`knowledge drift`

👤 **作者**：Sachin Kumar

- 🎯 **研究动机**：有害数据微调对开源模型安全保护的影响程度需量化
- 🔬 **研究方法**：比较有害与安全数据微调，测量 ASR、不确定性与知识漂移变化
- 📌 **结论**：有害微调使 ASR 升约 35% 并伴随大知识漂移与真实性下降；安全微调使 ASR 降 51.68%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLMs(Large Language Models) nowadays have widespread adoption as a tool for solving issues across various domain/tasks. These models since are susceptible to produce harmful or toxic results, inference-time adversarial attacks, therefore they do undergo safety alignment training and Red teaming for putting in safety guardrails. For using these models, usually fine-tuning is done for model alignment on the desired tasks, which can make model more aligned but also make it more susceptible to produce unsafe responses, if fine-tuned with harmful data.In this paper, we study how much of impact introduction of harmful data in fine-tuning can make, and if it can override the safety protection of those models. Conversely,it was also explored that if model is fine-tuned on safety data can make the model produce more safer responses. Further we explore if fine-tuning the model on harmful data makes it less helpful or less trustworthy because of increase in model uncertainty leading to knowledge drift. Our extensive experimental results shown that Safety protection in an open-source can be overridden, when fine-tuned with harmful data as observed by ASR increasing by 35% when compared to basemodel's ASR. Also, as observed, fine-tuning a model with harmful data made the harmful fine-tuned model highly uncertain with huge knowledge drift and less truthfulness in its responses. Furthermore, for the safe fine-tuned model, ASR decreases by 51.68% as compared to the basemodel, and Safe model also shown in minor drop in uncertainty and truthfulness as compared to basemodel. This paper's code is available at: https://github.com/techsachinkr/Overriding_Model_Safety_Protections

</details>

### 14. Covert Malicious Finetuning: Challenges in Safeguarding LLM Adaptation

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

### 15. Reasoning That Leaks, Fine-Tuning That Amplifies: Exposing the Hidden Threats of Chain-of-Thought Models

🌐 [Project](https://doi.org/10.1145/3779208.3785271)　📅 2026-06　🏷 ACM CCS 2026

**关键词**：`attack`、`analysis`、`benchmark`、`harmful fine-tuning`、`CoT escalation`、`alignment degradation`

- 🎯 **研究动机**：CoT模型的推理链安全风险与微调放大效应未明
- 🔬 **研究方法**：分析推理链与最终答案的安全差异及harmful fine-tuning影响
- 📌 **结论**：有害内容可藏于trace而最终答案合规，微调进一步放大泄漏

### 16. It Takes One to Bias Them All: Breaking Bad with One-Shot GRPO

📄 [arXiv](https://arxiv.org/abs/2606.10931) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-06

**关键词**：`attack`、`one-shot GRPO`、`systematic bias`、`cyber misuse`、`alignment poisoning`

👤 **作者**：Naihao Deng、Yilun Zhu、Naichen Shi、Clayton Scott、Rada Mihalcea

- 🎯 **研究动机**：大规模后训练建立的对齐护栏能否被极小样本打破尚不清楚
- 🔬 **研究方法**：研究 one-shot GRPO：仅用单个带偏样本做 GRPO 训练诱发系统性偏见，考察刻板推理的跨属性、类别与基准泛化
- 📌 **结论**：单个样本足以诱导系统性偏见并广泛泛化，且易感性与模型初始输出偏见的可能性相关，暴露后训练可被单例覆盖的关键漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Warning: This paper contains several toxic and offensive statements. Modern large language models (LLMs) are typically aligned through large-scale post-training to ensure fair and reliable behavior. In this work, we investigate how easily such guardrails can be broken by Group Relative Policy Optimization (GRPO). We show that one-shot GRPO training on a single biased example is sufficient to induce systematic bias, with stereotype-driven reasoning generalizing across attributes, categories, and benchmarks. We further find that models differ in their susceptibility based on the initial likelihood of producing biased outputs. Our results reveal a critical vulnerability in post-training: alignment can be overridden by a single example.

</details>
