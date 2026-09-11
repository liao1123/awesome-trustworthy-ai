## 研究方向

LLM 后门的检测、防御、净化与基准评测（攻击机制见姊妹页 llm-backdoor-attacks.md）。

## 检测与防御

### 1. Detecting Hidden Behaviors in LLMs via Activation-matched Finetuning

📄 [arXiv](https://arxiv.org/abs/2609.00351)　📅 2026-09

**关键词**：`detection`、`hidden behavior`、`activation residual`、`unsupervised backdoor audit`

👤 **作者**：Robin Haselhorst、Lucie Flek、Florian Mai

- 🎯 **研究动机**：backdoor、sleeper cue、sandbagging 等隐藏行为仅在窄条件下激活，无先验知识时难以检测
- 🔬 **研究方法**：提出无监督检测 activation-matched finetuning：用公开 anchor 模型在小型良性语料上微调以复现 suspect 模型 activation，按残差给每个 prompt 打分；良性语料覆盖不到稀疏触发区，触发 prompt 及语义邻居产生大残差
- 📌 **结论**：在第三方与自建模型上可靠暴露隐藏行为，且 defense-aware 攻击难以在保留行为本身的同时压制检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models can hide hidden behaviors that activate only under narrow conditions, such as backdoor triggers, sleeper-agent deployment cues, sandbagging, or topic-conditioned censorship. Such behaviors are difficult to detect without prior knowledge what to look for. We present activation-matched finetuning, an unsupervised detection method that assumes no knowledge of the trigger or the target behavior. Given a suspect model and a publicly available anchor, we finetune the anchor to reproduce the suspect's activations on a small benign corpus, and score each evaluation prompt by the residual between the two models. Since no benign corpus covers the sparse trigger region, the reference learns the benign computation but not the hidden behavior. Therefore, trigger prompts -- and, crucially, their semantic neighbors -- incur a large residual that signal the presence of unusual behavior to the defender. Testing our method across third-party models and custom models, activation-matched finetuning surfaces hidden behavior reliably. Furthermore, we empirically consider a natural defense-aware attack and showcase that it fails to suppress our detection method without sacrificing the behavior itself.

</details>

### 2. Beware What You Autocomplete: Forensic Attribution of Backdoored Code Completions

📄 [arXiv](https://arxiv.org/abs/2607.08011) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-07　🏷 COLM 2026

**关键词**：`detection`、`code LLM`、`sample attribution`、`code-model backdoor`、`forensic attribution`、`training-data tracing`

👤 **作者**：Anjun Gao、Yueyang Quan、Zhuqing Liu、Minghong Fang

- 🎯 **研究动机**：代码补全模型可被恶意微调数据隐蔽植入不安全行为，自适应后门攻击仍能绕过已有检测与缓解
- 🔬 **研究方法**：提出 CodeTracer 取证框架：在仅有微调语料与被上报错误补全事件的部署后约束下，从受损输出提取结构化行为指纹、缩小到语义相关代码样本，再以 LLM 推理把不安全逻辑归因到具体后门数据
- 📌 **结论**：三个代表性漏洞案例、十种后门攻击与十六个基线上一致取得高取证准确率、低误判率，并对自适应攻击鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models have enabled powerful code completion systems that assist developers by predicting subsequent lines of code. However, these models remain vulnerable to backdoor attacks, where malicious fine-tuning data covertly implants unsafe behaviors. Despite advances in defensive techniques, adaptive and sophisticated backdoor attacks still evade detection and mitigation. We present CodeTracer, a forensic framework that traces malicious code completions back to the backdoor fine-tuning data responsible for them. Operating under realistic post-deployment constraints, CodeTracer relies solely on the fine-tuning corpus and the reported miscompletion event. It extracts a structured behavioral fingerprint from the compromised output, narrows the search to semantically relevant code samples, and employs LLM-based reasoning to attribute unsafe logic to specific backdoor data. Extensive evaluations across three representative vulnerability cases and ten backdoor attacks, along with sixteen competitive baselines, demonstrate that CodeTracer consistently achieves high forensic accuracy, low false identification rates, and strong robustness against adaptive attacks.

</details>

### 3. Improving the Sensitivity of Backdoor Detectors via Class Subspace Orthogonalization

📄 [arXiv](https://arxiv.org/abs/2606.31309) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61956)　📅 2026-06　🏷 ICML 2026

**关键词**：`detection`、`CSO-LLM`、`trigger inversion`、`backdoor defense`、`empirical evaluation`、`supply-chain security`

👤 **作者**：Zhengxing Li、David J. Miller、Guangmingmei Yang、George Kesidis

- 🎯 **研究动机**：LLM 输入空间离散（多至 150000^k 个 k 元组）且缺少目标类 token 黑名单，后门检测与触发反演方法匮乏
- 🔬 **研究方法**：提出 class subspace orthogonalization（CSO）即插即用范式：惩罚候选触发中朝向目标类方向的 token，同时提供嵌入空间连续优化与离散 token 贪心增长两种检测/反演方法
- 📌 **结论**：多个 LLM 分类域与架构上实现强检测与真值触发器精确反演

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While post-training backdoor detection and trigger inversion schemes have been developed for AIs used e.g. for images, there is a paucity of such methods for LLMs. First, the LLM input space is discrete, with up to 150,000^k k-tuples to consider with k the token-length of a putative trigger. Second, one must blacklist tokens typical of the putative target response (class) of an attack, as such tokens may give false detection signals. However, a comprehensive blacklist is not available, in general, for a given domain. We develop a highly effective detection and inversion framework for LLMs treated as classifiers. Central to our approach is class subspace orthogonalization (CSO), a novel plug-and-play paradigm for backdoor detection that serves two fundamental roles when applied to LLMs: i) it enhances both sensitivity and specificity of a baseline detector; ii) it provides a form of implicit blacklisting, as it penalizes against inclusion, in a candidate trigger, of tokens that induce signal perturbations "in the direction of" the putative target class of an attack. One version of our detector performs continuous optimization in token embedding space, while a companion trigger-inversion and detection method performs greedy accretion in discrete token space. Our methods give both strong detection performance and accurate inversion of ground-truth triggers on several LLM classification domains, and for several different LLM architectures.

</details>

### 4. DualSentinel: A Lightweight Framework for Detecting Targeted Attacks in Black-box LLM via Dual Entropy Lull Pattern

📄 [arXiv](https://arxiv.org/abs/2603.01574) · 🌐 [Project](https://zenodo.org/records/18479273) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/pang-xiaoyi)　📅 2026-03　🏷 USENIX Security 2026

**关键词**：`detection`、`targeted attack`、`entropy lull`、`black-box LLM`、`black-box`、`entropy`

👤 **作者**：Xiaoyi Pang、Xuanyi Hao、Pengyu Liu、Qi Luo、Song Guo、Zhibo Wang

- 🎯 **研究动机**：后门与注入等定向攻击的防御需高访问权限或高成本，不适合真实 API 场景
- 🔬 **研究方法**：发现 Entropy Lull 模式：攻击劫持生成时 token 概率熵异常低且稳定；DualSentinel 先做幅值趋势监测，再用任务翻转做二次验证确认强制控制
- 📌 **结论**：检测准确率更优、近零误报且额外开销可忽略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent intelligent systems integrate powerful Large Language Models (LLMs) through APIs, but their trustworthiness may be critically undermined by targeted attacks like backdoor and prompt injection attacks, which secretly force LLMs to generate specific malicious sequences. Existing defensive approaches for such threats typically rely on high access rights, impose prohibitive costs, and hinder normal inference, rendering them impractical for real-world scenarios. To solve these limitations, we introduce DualSentinel, a lightweight and unified defense framework that can accurately and promptly detect the activation of targeted attacks alongside the LLM generation process. We first identify a characteristic of compromised LLMs, termed Entropy Lull: when a targeted attack successfully hijacks the generation process, the LLM exhibits a distinct period of abnormally low and stable token probability entropy, indicating it is following a fixed path rather than making creative choices. DualSentinel leverages this pattern by developing an innovative dual-check approach. It first employs a magnitude and trend-aware monitoring method to proactively and sensitively flag an entropy lull pattern at runtime. Upon such flagging, it triggers a lightweight yet powerful secondary verification based on task-flipping. An attack is confirmed only if the entropy lull pattern persists across both the original and the flipped task, proving that the LLM's output is coercively controlled. Extensive evaluations show that DualSentinel is both highly effective (superior detection accuracy with near-zero false positives) and remarkably efficient (negligible additional cost), offering a truly practical path toward securing deployed LLMs. The source code can be accessed at https://doi.org/10.5281/zenodo.18479273.

</details>

### 5. Uncovering Hidden Triggers: Backdoor Attribution in Language Models

📄 [arXiv](https://arxiv.org/abs/2509.21761) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60829)　📅 2025-09　🏷 ICML 2026

**关键词**：`detection`、`attribution`、`control`、`backdoor attack`、`mechanistic analysis`、`data poisoning`

👤 **作者**：Miao Yu、…、Qingsong Wen

- 🎯 **研究动机**：LLM 后门的内部机制是黑箱，既有可解释性研究聚焦对齐与越狱而忽视后门
- 🔬 **研究方法**：提出 BkdAttr 三方因果分析：Backdoor Probe 证明表示中编码可学习后门特征，BAHA 定位相关注意力头，并构造 Backdoor Vector 主控制器
- 📌 **结论**：仅消融约 3% 注意力头即可降 ASR 超 90%；对单点表示的一次干预可使干净输入 ASR 升至约 100% 或触发输入降至约 0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuned Large Language Models (LLMs) are vulnerable to backdoor attacks through data poisoning, yet the internal mechanisms governing these attacks remain a black box. Previous research on interpretability for LLM safety tends to focus on alignment, jailbreak, and hallucination, but overlooks backdoor mechanisms, making it difficult to understand and fully eliminate the backdoor threat. In this paper, aiming to bridge this gap, we explore the interpretable mechanisms of LLM backdoors through Backdoor Attribution (BkdAttr), a tripartite causal analysis framework. We first introduce the Backdoor Probe that proves the existence of learnable backdoor features encoded within the representations. Building on this insight, we further develop Backdoor Attention Head Attribution (BAHA), efficiently pinpointing the specific attention heads responsible for processing these features. Our primary experiments reveals these heads are relatively sparse; ablating a minimal \textbf{$\sim$ 3%} of total heads is sufficient to reduce the Attack Success Rate (ASR) by \textbf{over 90%}. More importantly, we further employ these findings to construct the Backdoor Vector derived from these attributed heads as a master controller for the backdoor. Through only \textbf{1-point} intervention on \textbf{single} representation, the vector can either boost ASR up to \textbf{$\sim$ 100% ($\uparrow$)} on clean inputs, or completely neutralize backdoor, suppressing ASR down to \textbf{$\sim$ 0% ($\downarrow$)} on triggered inputs. In conclusion, our work pioneers the exploration of mechanistic interpretability in LLM backdoors, demonstrating a powerful method for backdoor control and revealing actionable insights for the community.

</details>

### 6. Lie Detector: Unified Backdoor Detection via Cross-Examination Framework

📄 [arXiv](https://arxiv.org/abs/2503.16872)　📅 2025-03

**关键词**：`detection`、`cross-examination`、`black-box`、`model inconsistency`、`MLLM`

👤 **作者**：Xuan Wang、…、Xitong Gao

- 🎯 **研究动机**：半诚实外包训练下投毒可植入后门，现有统计检测难以跨学习范式保持精度
- 🔬 **研究方法**：提出 Lie Detector，交叉审查两个独立服务商模型的不一致性，用 central kernel alignment 恢复触发器并以微调敏感性区分对抗扰动
- 📌 **结论**：监督、半监督、自回归任务检测精度分别超 SoTA 5.4%、1.6%、11.9%，并首次检测 MLLM 后门

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Institutions with limited data and computing resources often outsource model training to third-party providers in a semi-honest setting, assuming adherence to prescribed training protocols with pre-defined learning paradigm (e.g., supervised or semi-supervised learning). However, this practice can introduce severe security risks, as adversaries may poison the training data to embed backdoors into the resulting model. Existing detection approaches predominantly rely on statistical analyses, which often fail to maintain universally accurate detection accuracy across different learning paradigms. To address this challenge, we propose a unified backdoor detection framework in the semi-honest setting that exploits cross-examination of model inconsistencies between two independent service providers. Specifically, we integrate central kernel alignment to enable robust feature similarity measurements across different model architectures and learning paradigms, thereby facilitating precise recovery and identification of backdoor triggers. We further introduce backdoor fine-tuning sensitivity analysis to distinguish backdoor triggers from adversarial perturbations, substantially reducing false positives. Extensive experiments demonstrate that our method achieves superior detection performance, improving accuracy by 5.4%, 1.6%, and 11.9% over SoTA baselines across supervised, semi-supervised, and autoregressive learning tasks, respectively. Notably, it is the first to effectively detect backdoors in multimodal large language models, further highlighting its broad applicability and advancing secure deep learning.

</details>

### 7. Patcher: Post-Hoc Patching of Backdoored Large Language Models

📄 [arXiv](https://arxiv.org/abs/2606.02995) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/gao-anjun)　📅 2026-06　🏷 USENIX Security 2026

**关键词**：`defense`、`post-hoc patch`、`trigger localization`、`LLM backdoor`、`post-hoc patching`、`saliency localization`

👤 **作者**：Anjun Gao、Yueyang Quan、Yufei Xia、Zhuqing Liu、Minghong Fang

- 🎯 **研究动机**：jailbreak 后门防御通常需要完整攻击信息或多个触发样本，防御者仅有单个失败案例时不适用
- 🔬 **研究方法**：提出 Patcher，仅凭一个上报失败案例和模型参数：先用响应条件化梯度显著性加自适应聚类定位触发器，再用 KL 约束微调解除触发-响应关联并保留正常能力
- 📌 **结论**：多种后门攻击下成功定位并中和后门、保持模型效用，对自适应攻击同样鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models remain vulnerable to jailbreak backdoor attacks, where adversaries poison safety alignment data to embed hidden triggers that bypass safety mechanisms. Existing defenses often require comprehensive attack information or multiple triggered examples, making them impractical when defenders only observe a single reported failure case without knowing whether it stems from a backdoor attack or a natural alignment bug. This paper presents Patcher, a post-hoc defense framework that repairs backdoored language models using only a single reported failure case and the model parameters. Patcher operates in two stages. First, it localizes backdoor triggers by computing response-conditioned gradient-based saliency scores and applying adaptive clustering to separate triggers from benign context. Second, it patches the model through a constrained fine-tuning objective that breaks the trigger-response association while preserving benign-task utility and robustness to non-triggered jailbreak attacks through KL-divergence constraints. We conduct extensive evaluations across multiple backdoor attack strategies and demonstrate that Patcher successfully localizes triggers and neutralizes backdoors while maintaining model utility. We further show robustness against adaptive attacks designed to evade our defense. This work represents a significant step toward practical defenses against training-time attacks in deployed language models.

</details>

### 8. Critical-CoT: A Robust Defense Framework against Reasoning-Level Backdoor Attacks in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2604.10681) · 🎓 [Official](https://aclanthology.org/2026.acl-long.495/)　📅 2026-04　🏷 ACL 2026

**关键词**：`defense`、`critical reasoning`、`CoT defense`、`reasoning safety`、`LLM backdoor`、`data poisoning`

👤 **作者**：Vu Tuan Truong、Long Bao Le

- 🎯 **研究动机**：reasoning-level 后门在 CoT 中插入恶意推理步骤而答案仍看似合理，针对性防御基本空白
- 🔬 **研究方法**：Critical-CoT 两阶段微调培养批判性思维，使模型自动识别后门并拒绝生成恶意推理步骤
- 📌 **结论**：对 ICL 与 FT 两类后门攻击均强鲁棒，并具跨域跨任务泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs), despite their impressive capabilities across domains, have been shown to be vulnerable to backdoor attacks. Prior backdoor strategies predominantly operate at the token level, where an injected trigger causes the model to generate a specific target word, choice, or class (depending on the task). Recent advances, however, exploit the long-form reasoning tendencies of modern LLMs to conduct reasoning-level backdoors: once triggered, the victim model inserts one or more malicious reasoning steps into its chain-of-thought (CoT). These attacks are substantially harder to detect, as the backdoored answer remains plausible and consistent with the poisoned reasoning trajectory. Yet, defenses tailored to this type of backdoor remain largely unexplored. To bridge this gap, we propose Critical-CoT, a novel defense mechanism that conducts a two-stage fine-tuning (FT) process on LLMs to develop critical thinking behaviors, enabling them to automatically identify potential backdoors and refuse to generate malicious reasoning steps. Extensive experiments across multiple LLMs and datasets demonstrate that Critical-CoT provides strong robustness against both in-context learning-based and FT-based backdoor attacks. Notably, Critical-CoT exhibits strong cross-domain and cross-task generalization. Our code is available at hthttps://github.com/tuanvu171/Critical-CoT.

</details>

### 9. TraceGuard: Process-Guided Firewall against Reasoning Backdoors in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2603.02436)　📅 2026-09

**关键词**：`defense`、`reasoning backdoor`、`process monitoring`、`point of fracture`

👤 **作者**：Zhen Guo、Shanghao Shi、Hao Li、Shamim Yazdani、Ning Zhang、Reza Tourani

- 🎯 **研究动机**：推理级后门可污染中间推理而保持貌似合理的轨迹与良性输出，输出式护栏无法定位首个无依据步骤
- 🔬 **研究方法**：TraceGuard 把模型推理当不可信输入，结合可验证审计轨迹生成、步骤感知 SFT（SSFT）与验证器引导 RL（VGRL），审计中间步骤并定位 Point of Fracture
- 📌 **结论**：紧凑 Qwen3-4B-Guard 端到端检测显著超未对齐 20B 模型，且泛化到训练外攻击族，基于 210,456 个步骤级审计决策

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Reasoning Models (LRMs) introduce a reasoning-level attack surface: adversaries can corrupt intermediate inferences while preserving a plausible trace and an apparently benign output. Existing output guardrails cannot reliably identify where such a trace first becomes unsupported. We present TraceGuard, a compact, locally deployable reasoning firewall that treats model-generated reasoning as untrusted input. Its design combines grounded generation of verifiable audit traces, Step-Aware Supervised Fine-Tuning (SSFT) for process-level supervision, and Verifier-Guided Reinforcement Learning (VGRL) for hardening against difficult reasoning traces. TraceGuard audits intermediate steps, localizes the initial Point of Fracture, and grounds its final decision in the complete audit evidence. We evaluate TraceGuard across heterogeneous open-weight architectures, reasoning domains, and reasoning-integrity attack families. A compact Qwen3-4B-Guard substantially outperforms an unaligned 20B model under strict end-to-end detection. Its auditing behavior transfers to attack families excluded from training, resists in-scope black-box probing, and remains robust in an additional white-box stress test. Overall, 210,456 step-level audit decisions support compact, process-aligned verification as an effective, deployable defense boundary for reasoning systems.

</details>

### 10. Merging Triggers, Breaking Backdoors: Defensive Poisoning for Instruction-Tuned Language Models

📄 [arXiv](https://arxiv.org/abs/2601.04448) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1113/)　📅 2026-01　🏷 ACL 2026

**关键词**：`defense`、`defensive poisoning`、`trigger merging`、`LLM backdoor`、`data poisoning`、`model integrity`

👤 **作者**：San Kim、Gary Geunbae Lee

- 🎯 **研究动机**：指令微调 LLM 依赖的大规模网络数据使其易受后门攻击，而相应防御研究不足
- 🔬 **研究方法**：MB-Defense 两阶段：防御性投毒把攻击者触发器与防御触发器合并为统一后门表示，再经附加训练打破该表示恢复干净行为
- 📌 **结论**：多个 LLM 上显著降低 ASR 并保留指令遵循能力，对未见后门攻击可泛化且数据高效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have greatly advanced Natural Language Processing (NLP), particularly through instruction tuning, which enables broad task generalization without additional fine-tuning. However, their reliance on large-scale datasets-often collected from human or web sources-makes them vulnerable to backdoor attacks, where adversaries poison a small subset of data to implant hidden behaviors. Despite this growing risk, defenses for instruction-tuned models remain underexplored. We propose MB-Defense (Merging & Breaking Defense Framework), a novel training pipeline that immunizes instruction-tuned LLMs against diverse backdoor threats. MB-Defense comprises two stages: (i) Defensive Poisoning, which merges attacker and defensive triggers into a unified backdoor representation, and (ii) Backdoor Neutralization, which breaks this representation through additional training to restore clean behavior. Extensive experiments across multiple LLMs show that MB-Defense substantially lowers attack success rates while preserving instruction-following ability. Our method offers a generalizable and data-efficient defense strategy, improving the robustness of instruction-tuned LLMs against unseen backdoor attacks.

</details>

### 11. Lethe: Purifying Backdoored Large Language Models with Knowledge Dilution

📄 [arXiv](https://arxiv.org/abs/2508.21004) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/chen-chen)　📅 2025-08　🏷 USENIX Security 2026

**关键词**：`defense`、`knowledge dilution`、`purification`、`LLM backdoor`、`model purification`

👤 **作者**：Chen Chen、…、Kwok-Yan Lam

- 🎯 **研究动机**：现有 LLM 后门防御覆盖窄、多仅检测，难敌编辑式、多触发与无触发攻击
- 🔬 **研究方法**：提出 LETHE 知识稀释：内部用轻量数据训练干净模型并与后门模型合并稀释参数记忆，外部在 prompt 注入良性语义相关证据转移注意力
- 📌 **结论**：五个 LLM、八种攻击上超八个 SoTA 防御基线，高级后门 ASR 最多降 98% 且保持效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have seen significant advancements, achieving superior performance in various Natural Language Processing (NLP) tasks. However, they remain vulnerable to backdoor attacks, where models behave normally for standard queries but generate harmful responses or unintended output when specific triggers are activated. Existing backdoor defenses either lack comprehensiveness, focusing on narrow trigger settings, detection-only mechanisms, and limited domains, or fail to withstand advanced scenarios like model-editing-based, multi-trigger, and triggerless attacks. In this paper, we present LETHE, a novel method to eliminate backdoor behaviors from LLMs through knowledge dilution using both internal and external mechanisms. Internally, LETHE leverages a lightweight dataset to train a clean model, which is then merged with the backdoored model to neutralize malicious behaviors by diluting the backdoor impact within the model's parametric memory. Externally, LETHE incorporates benign and semantically relevant evidence into the prompt to distract LLM's attention from backdoor features. Experimental results on classification and generation domains across 5 widely used LLMs demonstrate that LETHE outperforms 8 state-of-the-art defense baselines against 8 backdoor attacks. LETHE reduces the attack success rate of advanced backdoor attacks by up to 98% while maintaining model utility. Furthermore, LETHE has proven to be cost-efficient and robust against adaptive backdoor attacks.

</details>

### 12. BEEAR: Embedding-Based Adversarial Removal of Safety Backdoors in Instruction-Tuned Language Models

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

### 13. SpecGuard: Inference-Time Backdoor Detection For Free
📄 [arXiv](https://arxiv.org/abs/2609.11799)　📅 2026-09


👤 **作者**：Rui Wen、Ahmed Salem、Andrew Paverd、Mark Russinovich、Zheng Li

**关键词**：`detection`、`inference-time backdoor`、`speculative decoding`、`draft acceptance rate`、`zero-cost monitoring`

- 🎯 **研究动机**：推理时后门检测要么依赖触发器形式假设、要么需额外计算 pass，不适合延迟敏感的 LLM 服务
- 🔬 **研究方法**：复用投机解码验证过程：后门触发使目标模型偏移而干净 draft 不预测，draft 接受率变化即信号；证明压制信号必削弱后门
- 📌 **结论**：多后门类型与模型族可靠检出含输入过滤盲区案例，零额外模型计算

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are often fine-tuned, shared, or downloaded from third parties, so a deployed model may carry a hidden backdoor that behaves normally on benign inputs but switches to attacker-controlled behavior when a secret trigger appears. While backdoors can be audited before deployment, runtime monitoring remains important for models that are frequently updated. The challenge is that LLM serving is latency-sensitive: existing inference-time detectors either rely on assumptions about the trigger form, which can fail on stealthy attacks, or require extra model computation, such as input perturbations or an additional generation pass. We introduce SpecGuard, an inference-time backdoor detector that repurposes speculative decoding at zero added model-computation cost. Speculative decoding speeds up inference by using a small draft model to propose tokens and a target model to verify them. We observe that this verification process already exposes a useful signal: when a backdoor is triggered, the target model shifts toward the attacker's behavior, while a clean draft model does not predict this shift, causing the draft-token acceptance rate to change. We formalize when this signal appears and show that an attacker who suppresses it must also weaken the backdoor. Across diverse backdoor types and model families, SpecGuard reliably detects triggered behavior, including stealthy cases where input-level filters are blind, while avoiding the extra generation cost of existing runtime detectors. Speculative decoding therefore doubles as a free, always-on signal for detecting backdoored LLM behavior.

</details>

## 核心收录（P2）
## 综评与基准

### 14. Backdoor Learning in Language Models and Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2608.18095)　📅 2026-08

**关键词**：`survey`、`dissertation`、`LM／VLM`、`attack／detection`、`VLM security`、`TrojAI`

👤 **作者**：Weimin Lyu

- 🎯 **研究动机**：NLP 与 VLM 的后门攻击构成严重安全威胁，需系统分析、检测与设计
- 🔬 **研究方法**：博士论文系统分析、检测与设计 LM/VLM 后门攻击（含 TrojAI 场景），并研究面向临床与医学影像的高效多模态表征
- 📌 **结论**：整合后门安全研究与医学多模态效率两条主线的工作

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in deep learning have significantly enhanced the capabilities of Natural Language Processing (NLP) and Vision-Language Models (VLMs). However, these advancements come with increased vulnerabilities, notably through backdoor attacks that pose severe security threats. This thesis addresses two critical dimensions of Trustworthy AI and Efficient Multimodal Representation Learning: (1) security through analyzing, detecting, and designing backdoor attacks in NLP and VLMs, and (2) efficiency through advanced multimodal representation methods tailored for clinical and medical imaging applications.

</details>

### 15. ToxScreen: Detecting Whether an LLM Has Been Poisoned

📄 [arXiv](https://arxiv.org/abs/2607.26849)　📅 2026-07

**关键词**：`benchmark`、`model auditing`、`trigger recovery`

👤 **作者**：Anthony Hughes、Nicole Xing、Collin Francel、Andy Kim、Andrew Draganov

- 🎯 **研究动机**：防御者仅有白盒权重与可疑行为知识（无训练数据、无参照模型、不知触发器、不确定是否中毒）时能否恢复触发器未知
- 🔬 **研究方法**：发布 ToxScreen：约 800 个后门模型覆盖攻击目标、触发机制、投毒率、规模与训练机制；比较梯度提示优化与按 ASR 排序的 token 查表两类恢复方法
- 📌 **结论**：梯度优化恢复失败而 token 查表在后门有效处即可恢复触发器；后门与越狱采用不同机制可过滤误报；无方法可靠发现所有后门，但广泛可越狱本身即是异常信号

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) are deployed in high-stakes domains, adversaries may poison training data to implant backdoors: hidden triggers that covertly manipulate model behavior at inference time. We ask whether a defender can recover such a trigger under realistic affordances, namely white-box access to the weights and knowledge of the behavior of concern, but no training data, no trusted reference model, no knowledge of the trigger, and no certainty that the model is poisoned. To evaluate whether a defender can recover such a trigger under realistic settings, we release ToxScreen, a benchmark of roughly 800 backdoored models spanning attack objectives, trigger mechanisms, poisoning rates, model scales, and backdoor training mechanisms. We also assert that the backdoors are high-quality: they achieve high attack success rates, generalize to unseen harmful inputs, and preserve clean-task performance. Scoring recovery of the planted trigger, we find that gradient-based prompt optimization fails in recovery, whereas a token look-up that ranks candidates by attack-success rate recovers the trigger wherever the backdoor is effective. To understand this more, we study the relationship between attack behaviors and the weights of an LLM. We find a phenomenon whereby backdoors operate via different mechanistic strategies than jailbreaks, allowing defenders to filter jailbreaks. Finally, no method reliably surfaces every backdoor, but a broadly jailbreakable model is itself anomalous, a useful signal even when the exact trigger is not recovered. We release all models and evaluation code

</details>

### 16. Security in the Fine-Tuning Lifecycle of Large Language Models: Threats, Defenses, Evaluation, and Future Directions

📄 [arXiv](https://arxiv.org/abs/2605.25073)　📅 2026-05

**关键词**：`survey`、`fine-tuning lifecycle`

👤 **作者**：Wenjuan Li、Yitao Liu、Runze Chen、Rajkumar Buyya

- 🎯 **研究动机**：微调依赖数据、参数更新与可复用组件，威胁从数据投毒演化到 agent 操纵，缺覆盖全生命周期的统一框架
- 🔬 **研究方法**：按干预时机分 pre-tuning、during-tuning、post-tuning 三阶段综述攻防，并在统一模型、硬件与协议下做含跨阶段组合的实证评测
- 📌 **结论**：攻击效果高度依赖模型且随规模非单调——权重编辑攻击在新模型失效、跨语言后门在 1B-4B 完全失效；纯良性样本即可破坏对齐；单阶段防御几乎不跨阶段泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Background: Fine-tuning is central to adapting pre-trained Large Language Models (LLMs) to downstream tasks, but its reliance on training data, parameter updates, and reusable components opens entry points for attackers. Threats have evolved from data poisoning and weight tampering to agent manipulation and interface exploitation, yet existing reviews lack a unified framework spanning the full fine-tuning lifecycle. Objective: This paper presents a systematic survey of LLM fine-tuning security and establishes a lifecycle-based framework for comparing attacks and defenses, complemented by unified empirical evaluation. Methods: We divide attack and defense mechanisms into three phases by intervention timing: pre-tuning, during-tuning, and post-tuning. Within each phase, strategies are reviewed and contrasted to expose their evolution and limitations. Representative methods are then evaluated under a unified model, hardware, and protocol setup, with cross-phase experiments pairing attacks and defenses from different phases. Results: Attack effectiveness is highly model-dependent and non-monotonic with scale: weight-editing attacks effective on earlier models lose impact on modern open-source LLMs; cross-lingual backdoor transfer, reported as near-perfect at larger scales, fails entirely on tested 1B-4B models; and purely benign samples can compromise safety alignment in instruction-tuned models. Single-phase defenses rarely generalize across phases, and defense effectiveness depends jointly on model architecture and alignment state. Conclusion: We identify key open problems (configuration-robust defense, cross-phase defense composition, and embedding-space attacks beyond behavioral assumptions) and propose concrete future research directions.

</details>

### 17. Backdoor4Good: Benchmarking Beneficial Uses of Backdoors in LLMs

📄 [arXiv](https://arxiv.org/abs/2603.07452)　📅 2026-03

**关键词**：`benchmark`、`beneficial backdoor`

👤 **作者**：Yige Li、…、Jun Sun

- 🎯 **研究动机**：后门机制一直只被视为威胁，其条件激活能否服务可信行为未被系统评估
- 🔬 **研究方法**：Backdoor4Good 以 (Trigger, Activation, Utility) 三元形式化良性后门学习，在四个信任导向应用上评测 Llama3.1-8B 等四个模型
- 📌 **结论**：良性后门实现高可控性、抗篡改与隐蔽性并保持干净任务性能，可作为模块化可解释的可信构件

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor mechanisms have traditionally been studied as security threats that compromise the integrity of machine learning models. However, the same mechanism -- the conditional activation of specific behaviors through input triggers -- can also serve as a controllable and auditable interface for trustworthy model behavior. In this work, we present \textbf{Backdoor4Good (B4G)}, a unified benchmark and framework for \textit{beneficial backdoor} applications in large language models (LLMs). Unlike conventional backdoor studies focused on attacks and defenses, B4G repurposes backdoor conditioning for Beneficial Tasks that enhance safety, controllability, and accountability. It formalizes beneficial backdoor learning under a triplet formulation $(T, A, U)$, representing the \emph{Trigger}, \emph{Activation mechanism}, and \emph{Utility function}, and implements a benchmark covering four trust-centric applications. Through extensive experiments across Llama3.1-8B, Gemma-2-9B, Qwen2.5-7B, and Llama2-13B, we show that beneficial backdoors can achieve high controllability, tamper-resistance, and stealthiness while preserving clean-task performance. Our findings demonstrate new insights that backdoors need not be inherently malicious; when properly designed, they can serve as modular, interpretable, and beneficial building blocks for trustworthy AI systems. Our code and datasets are available at https://github.com/bboylyg/BackdoorLLM/B4G.

</details>

### 18. Rethinking Reasoning: A Survey on Reasoning-based Backdoors in LLMs

📄 [arXiv](https://arxiv.org/abs/2510.07697) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.863/)　📅 2025-10　🏷 ACL 2026

**关键词**：`survey`、`reasoning backdoor`

👤 **作者**：Man Hu、…、Shuai Zhao

- 🎯 **研究动机**：推理能力为 LLM 引入新后门风险，既有综述缺乏针对推理后门的深入分析
- 🔬 **研究方法**：首个推理式后门综述：提出统一分类法把攻击分为 associative、passive、active 三类，并梳理防御策略与开放挑战
- 📌 **结论**：为推理后门攻击与防御提供统一视角与后续研究路线图

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rise of advanced reasoning capabilities, large language models (LLMs) are receiving increasing attention. However, although reasoning improves LLMs' performance on downstream tasks, it also introduces new security risks, as adversaries can exploit these capabilities to conduct backdoor attacks. Existing surveys on backdoor attacks and reasoning security offer comprehensive overviews but lack in-depth analysis of backdoor attacks and defenses targeting LLMs' reasoning abilities. In this paper, we take the first step toward providing a comprehensive review of reasoning-based backdoor attacks in LLMs by analyzing their underlying mechanisms, methodological frameworks, and unresolved challenges. Specifically, we introduce a new taxonomy that offers a unified perspective for summarizing existing approaches, categorizing reasoning-based backdoor attacks into associative, passive, and active. We also present defense strategies against such attacks and discuss current challenges alongside potential directions for future research. This work offers a novel perspective, paving the way for further exploration of secure and trustworthy LLM communities.

</details>

### 19. ELBA-Bench: An Efficient Learning Backdoor Attacks Benchmark for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2502.18511) · 🎓 [Official](https://aclanthology.org/2025.acl-long.877/)　📅 2025-02　🏷 ACL 2025

**关键词**：`benchmark`、`efficient attack`

👤 **作者**：Xuxu Liu、…、Dacheng Tao

- 🎯 **研究动机**：LLM 后门基准在攻击覆盖、指标体系与设定现实性上均不足
- 🔬 **研究方法**：ELBA-Bench 支持 LoRA 等 PEFT 与 ICL 免微调注入，1300 余实验覆盖 12 种攻击、18 个数据集与 12 个 LLM
- 📌 **结论**：PEFT 攻击在分类任务上稳定优于免微调且跨数据集泛化；任务相关优化与干净对抗演示可提升 ASR 且保干净性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative large language models are crucial in natural language processing, but they are vulnerable to backdoor attacks, where subtle triggers compromise their behavior. Although backdoor attacks against LLMs are constantly emerging, existing benchmarks remain limited in terms of sufficient coverage of attack, metric system integrity, backdoor attack alignment. And existing pre-trained backdoor attacks are idealized in practice due to resource access constraints. Therefore we establish $\textit{ELBA-Bench}$, a comprehensive and unified framework that allows attackers to inject backdoor through parameter efficient fine-tuning ($\textit{e.g.,}$ LoRA) or without fine-tuning techniques ($\textit{e.g.,}$ In-context-learning). $\textit{ELBA-Bench}$ provides over 1300 experiments encompassing the implementations of 12 attack methods, 18 datasets, and 12 LLMs. Extensive experiments provide new invaluable findings into the strengths and limitations of various attack strategies. For instance, PEFT attack consistently outperform without fine-tuning approaches in classification tasks while showing strong cross-dataset generalization with optimized triggers boosting robustness; Task-relevant backdoor optimization techniques or attack prompts along with clean and adversarial demonstrations can enhance backdoor attack success while preserving model performance on clean samples. Additionally, we introduce a universal toolbox designed for standardized backdoor attack research, with the goal of propelling further progress in this vital area.

</details>

### 20. A Survey on Backdoor Threats in Large Language Models (LLMs): Attacks, Defenses, and Evaluations

📄 [arXiv](https://arxiv.org/abs/2502.05224)　📅 2025-02

**关键词**：`survey`、`taxonomy`、`evaluation`

👤 **作者**：Yihe Zhou、Tao Ni、Wei-Bin Lee、Qingchuan Zhao

- 🎯 **研究动机**：LLM 后门攻击随防御演进而发展，缺乏统一taxonomy的系统梳理
- 🔬 **研究方法**：以通用机器学习攻击分类框架聚焦训练期白盒后门，系统归类攻击方法并对应梳理防御
- 📌 **结论**：为扩展攻击场景与构建更强防御提供研究指南

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have achieved significantly advanced capabilities in understanding and generating human language text, which have gained increasing popularity over recent years. Apart from their state-of-the-art natural language processing (NLP) performance, considering their widespread usage in many industries, including medicine, finance, education, etc., security concerns over their usage grow simultaneously. In recent years, the evolution of backdoor attacks has progressed with the advancement of defense mechanisms against them and more well-developed features in the LLMs. In this paper, we adapt the general taxonomy for classifying machine learning attacks on one of the subdivisions - training-time white-box backdoor attacks. Besides systematically classifying attack methods, we also consider the corresponding defense methods against backdoor attacks. By providing an extensive summary of existing works, we hope this survey can serve as a guideline for inspiring future research that further extends the attack scenarios and creates a stronger defense against them for more robust LLMs.

</details>

### 21. Mitigating Backdoor Threats to Large Language Models: Advancement and Challenges

📄 [arXiv](https://arxiv.org/abs/2409.19993)　📅 2024-09

**关键词**：`survey`、`mitigation`

👤 **作者**：Qin Liu、…、Muhao Chen

- 🎯 **研究动机**：LLM 后门威胁随指令微调、RLHF 等范式快速演化，缺乏最新防御综述
- 🔬 **研究方法**：梳理 LLM 开发与推理各阶段的后门威胁及检测、消除策略
- 📌 **结论**：指出生成任务、未知触发器与能力保持是防御的主要难点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The advancement of Large Language Models (LLMs) has significantly impacted various domains, including Web search, healthcare, and software development. However, as these models scale, they become more vulnerable to cybersecurity risks, particularly backdoor attacks. By exploiting the potent memorization capacity of LLMs, adversaries can easily inject backdoors into LLMs by manipulating a small portion of training data, leading to malicious behaviors in downstream applications whenever the hidden backdoor is activated by the pre-defined triggers. Moreover, emerging learning paradigms like instruction tuning and reinforcement learning from human feedback (RLHF) exacerbate these risks as they rely heavily on crowdsourced data and human feedback, which are not fully controlled. In this paper, we present a comprehensive survey of emerging backdoor threats to LLMs that appear during LLM development or inference, and cover recent advancement in both defense and detection strategies for mitigating backdoor threats to LLMs. We also outline key challenges in addressing these threats, highlighting areas for future research.

</details>

### 22. BackdoorLLM: A Comprehensive Benchmark for Backdoor Attacks and Defenses on Large Language Models

📄 [arXiv](https://arxiv.org/abs/2408.12798) · 🌐 [Project](https://papers.nips.cc/paper_files/paper/2025/hash/20ffc2b42c7de4a1960cfdadf305bbe2-Abstract-Datasets_and_Benchmarks_Track.html)　📅 2024-08　🏷 NeurIPS 2025

**关键词**：`benchmark`、`attack／defense`

👤 **作者**：Yige Li、Hanxun Huang、Yunhan Zhao、Xingjun Ma、Jun Sun

- 🎯 **研究动机**：LLM 开放文本生成的后门威胁缺乏统一系统基准
- 🔬 **研究方法**：BackdoorLLM 提供标准化训练评测管线，覆盖数据投毒、权重投毒、隐状态操纵、CoT 劫持等 8 种攻击、7 个场景、6 种架构与 7 种防御
- 📌 **结论**：200 余项实验给出 LLM 后门有效性影响因素与失效模式洞见

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative large language models (LLMs) have achieved state-of-the-art results on a wide range of tasks, yet they remain susceptible to backdoor attacks: carefully crafted triggers in the input can manipulate the model to produce adversary-specified outputs. While prior research has predominantly focused on backdoor risks in vision and classification settings, the vulnerability of LLMs in open-ended text generation remains underexplored. To fill this gap, we introduce BackdoorLLM (Our BackdoorLLM benchmark was awarded First Prize in the SafetyBench competition, https://www.mlsafety.org/safebench/winners, organized by the Center for AI Safety, https://safe.ai/.), the first comprehensive benchmark for systematically evaluating backdoor threats in text-generation LLMs. BackdoorLLM provides: (i) a unified repository of benchmarks with a standardized training and evaluation pipeline; (ii) a diverse suite of attack modalities, including data poisoning, weight poisoning, hidden-state manipulation, and chain-of-thought hijacking; (iii) over 200 experiments spanning 8 distinct attack strategies, 7 real-world scenarios, and 6 model architectures; (iv) key insights into the factors that govern backdoor effectiveness and failure modes in LLMs; and (v) a defense toolkit encompassing 7 representative mitigation techniques. Our code and datasets are available at https://github.com/bboylyg/BackdoorLLM. We will continuously incorporate emerging attack and defense methodologies to support the research in advancing the safety and reliability of LLMs.

</details>

### 23. A Survey of Recent Backdoor Attacks and Defenses in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2406.06852) · 📝 [OpenReview](https://openreview.net/forum?id=wZLWuFHxt5)　📅 2024-06

**关键词**：`survey`、`taxonomy`

👤 **作者**：Shuai Zhao、…、Luu Anh Tuan

- 🎯 **研究动机**：已有综述缺乏针对 LLM 后门攻击的深入专项梳理
- 🔬 **研究方法**：按微调方式把 LLM 后门分为全参微调、PEFT 与免微调三类系统梳理，并讨论未来议题
- 📌 **结论**：指出免微调攻击算法与更隐蔽攻击设计是关键研究方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs), which bridge the gap between human language understanding and complex problem-solving, achieve state-of-the-art performance on several NLP tasks, particularly in few-shot and zero-shot settings. Despite the demonstrable efficacy of LLMs, due to constraints on computational resources, users have to engage with open-source language models or outsource the entire training process to third-party platforms. However, research has demonstrated that language models are susceptible to potential security vulnerabilities, particularly in backdoor attacks. Backdoor attacks are designed to introduce targeted vulnerabilities into language models by poisoning training samples or model weights, allowing attackers to manipulate model responses through malicious triggers. While existing surveys on backdoor attacks provide a comprehensive overview, they lack an in-depth examination of backdoor attacks specifically targeting LLMs. To bridge this gap and grasp the latest trends in the field, this paper presents a novel perspective on backdoor attacks for LLMs by focusing on fine-tuning methods. Specifically, we systematically classify backdoor attacks into three categories: full-parameter fine-tuning, parameter-efficient fine-tuning, and no fine-tuning Based on insights from a substantial review, we also discuss crucial issues for future research on backdoor attacks, such as further exploring attack algorithms that do not require fine-tuning, or developing more covert attack algorithms.

</details>

### 24. Competition Report: Finding Universal Jailbreak Backdoors in Aligned LLMs

📄 [arXiv](https://arxiv.org/abs/2404.14461)　📅 2024-04

**关键词**：`competition`、`universal trigger`

👤 **作者**：Javier Rando、…、Florian Tramèr

- 🎯 **研究动机**：对齐流程可被投毒植入通用 sudo 式越狱后门，社区需要发现此类后门的方法
- 🔬 **研究方法**：IEEE SaTML 2024 竞赛挑战参赛者在多个 LLM 中寻找 universal backdoors，报告总结关键发现
- 📌 **结论**：归纳了参赛方法与有前景的后续研究方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are aligned to be safe, preventing users from generating harmful content like misinformation or instructions for illegal activities. However, previous work has shown that the alignment process is vulnerable to poisoning attacks. Adversaries can manipulate the safety training data to inject backdoors that act like a universal sudo command: adding the backdoor string to any prompt enables harmful responses from models that, otherwise, behave safely. Our competition, co-located at IEEE SaTML 2024, challenged participants to find universal backdoors in several large language models. This report summarizes the key findings and promising ideas for future research.

</details>

### 25. Trojan Detection in Large Language Models: Insights from the Trojan Detection Challenge

📄 [arXiv](https://arxiv.org/abs/2404.13660)　📅 2024-04

**关键词**：`challenge`、`trojan detection`

👤 **作者**：Narek Maloyan、Ekansh Verma、Bulat Nutfullin、Bislan Ashinov

- 🎯 **研究动机**：LLM 特洛伊检测的真实难度需要竞赛级评估来揭示
- 🔬 **研究方法**：分析 Trojan Detection Challenge 2023 各方法，比较区分 intended/unintended triggers 与逆向工程的可行性
- 📌 **结论**：高 Recall 远难于高 REASR；顶尖方法 Recall 仅约 0.16、与随机采样基线相当，质疑特洛伊的可检测与可恢复性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have demonstrated remarkable capabilities in various domains, but their vulnerability to trojan or backdoor attacks poses significant security risks. This paper explores the challenges and insights gained from the Trojan Detection Competition 2023 (TDC2023), which focused on identifying and evaluating trojan attacks on LLMs. We investigate the difficulty of distinguishing between intended and unintended triggers, as well as the feasibility of reverse engineering trojans in real-world scenarios. Our comparative analysis of various trojan detection methods reveals that achieving high Recall scores is significantly more challenging than obtaining high Reverse-Engineering Attack Success Rate (REASR) scores. The top-performing methods in the competition achieved Recall scores around 0.16, comparable to a simple baseline of randomly sampling sentences from a distribution similar to the given training prefixes. This finding raises questions about the detectability and recoverability of trojans inserted into the model, given only the harmful targets. Despite the inability to fully solve the problem, the competition has led to interesting observations about the viability of trojan detection and improved techniques for optimizing LLM input prompts. The phenomenon of unintended triggers and the difficulty in distinguishing them from intended triggers highlights the need for further research into the robustness and interpretability of LLMs. The TDC2023 has provided valuable insights into the challenges and opportunities associated with trojan detection in LLMs, laying the groundwork for future research in this area to ensure their safety and reliability in real-world applications.

</details>

### 26. Backdoor Attacks and Countermeasures in Natural Language Processing Models: A Comprehensive Security Review

📄 [arXiv](https://arxiv.org/abs/2309.06055)　📅 2023-09

**关键词**：`survey`、`NLP／LLM`

👤 **作者**：Pengzhou Cheng、Zongru Wu、Wei Du、Haodong Zhao、Wei Lu、Gongshen Liu

- 🎯 **研究动机**：缺乏按攻击者能力与受影响阶段系统梳理 LM 后门攻击面并对比防御的综述
- 🔬 **研究方法**：将攻击面形式化为 APMF、APMP、AFMT、ALLM 四类，防御分为样本检查与模型检查，附基准数据集与可比评测
- 📌 **结论**：指出高效实用防御缺失等未来关键研究方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Language Models (LMs) are becoming increasingly popular in real-world applications. Outsourcing model training and data hosting to third-party platforms has become a standard method for reducing costs. In such a situation, the attacker can manipulate the training process or data to inject a backdoor into models. Backdoor attacks are a serious threat where malicious behavior is activated when triggers are present, otherwise, the model operates normally. However, there is still no systematic and comprehensive review of LMs from the attacker's capabilities and purposes on different backdoor attack surfaces. Moreover, there is a shortage of analysis and comparison of the diverse emerging backdoor countermeasures. Therefore, this work aims to provide the NLP community with a timely review of backdoor attacks and countermeasures. According to the attackers' capability and affected stage of the LMs, the attack surfaces are formalized into four categorizations: attacking the pre-trained model with fine-tuning (APMF) or parameter-efficient fine-tuning (APMP), attacking the final model with training (AFMT), and attacking Large Language Models (ALLM). Thus, attacks under each categorization are combed. The countermeasures are categorized into two general classes: sample inspection and model inspection. Thus, we review countermeasures and analyze their advantages and disadvantages. Also, we summarize the benchmark datasets and provide comparable evaluations for representative attacks and defenses. Drawing the insights from the review, we point out the crucial areas for future research on the backdoor, especially soliciting more efficient and practical countermeasures.

</details>

### 27. Reasoning Introduces New Poisoning Attacks Yet Makes Them More Complicated

📄 [arXiv](https://arxiv.org/abs/2509.05739) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-09　🏷 SaTML 2026

**关键词**：`analysis`、`attack`、`CoT integrity`、`trace-answer divergence`、`decomposed trigger`、`reasoning model`

👤 **作者**：Hanna Foerster、…、Yarin Gal

- 🎯 **研究动机**：推理能力把 LLM 攻击面扩展到中间 CoT，但推理模型上投毒能否生效不明
- 🔬 **研究方法**：提出 decomposed reasoning poison：仅修改推理路径、prompt 与最终答案保持干净，并把触发器拆成多个各自无害的组件
- 📌 **结论**：可注入但可靠激活并改变最终答案出奇困难，模型常能从思维过程中的后门恢复，推理能力带来涌现式后门鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Early research into data poisoning attacks against Large Language Models (LLMs) demonstrated the ease with which backdoors could be injected. More recent LLMs add step-by-step reasoning, expanding the attack surface to include the intermediate chain-of-thought (CoT) and its inherent trait of decomposing problems into subproblems. Using these vectors for more stealthy poisoning, we introduce ``decomposed reasoning poison'', in which the attacker modifies only the reasoning path, leaving prompts and final answers clean, and splits the trigger across multiple, individually harmless components. Fascinatingly, while it remains possible to inject these decomposed poisons, reliably activating them to change final answers (rather than just the CoT) is surprisingly difficult. This difficulty arises because the models can often recover from backdoors that are activated within their thought processes. Ultimately, it appears that an emergent form of backdoor robustness is originating from the reasoning capabilities of these advanced LLMs, as well as from the architectural separation between reasoning and final answer generation.

</details>

### 28. Compiling Activation Steering into Weights via Null-Space Constraints for Stealthy Backdoors

📄 [arXiv](https://arxiv.org/abs/2604.12359) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1206/)　📅 2026-04　🏷 ACL 2026

**关键词**：`analysis`、`activation steering`、`weight compilation`、`representation intervention`、`LLM backdoor`、`data poisoning`

👤 **作者**：Rui Yin、…、Shouling Ji

- 🎯 **研究动机**：现有权重编辑后门只优化 token 级映射（如 Sure 前缀），不保证持续有害输出，模型可能数步后回归拒答
- 🔬 **研究方法**：提取 compliant 与 refusal 行为差的 steering vector，以闭式解编译为仅在触发时激活的持久权重修改，并用零空间约束保证 clean 输入上休眠
- 📌 **结论**：多个安全对齐 LLM 与越狱基准上实现高触发 ASR，同时保持非触发安全与通用效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety-aligned large language models (LLMs) are increasingly deployed in real-world pipelines, yet this deployment also enlarges the supply-chain attack surface: adversaries can distribute backdoored checkpoints that behave normally under standard evaluation but jailbreak when a hidden trigger is present. Recent post-hoc weight-editing methods offer an efficient approach to injecting such backdoors by directly modifying model weights to map a trigger to an attacker-specified response. However, existing methods typically optimize a token-level mapping that forces an affirmative prefix (e.g., ``Sure''), which does not guarantee sustained harmful output -- the model may begin with apparent agreement yet revert to safety-aligned refusal within a few decoding steps. We address this reliability gap by shifting the backdoor objective from surface tokens to internal representations. We extract a steering vector that captures the difference between compliant and refusal behaviors, and compile it into a persistent weight modification that activates only when the trigger is present. To preserve stealthiness and benign utility, we impose a null-space constraint so that the injected edit remains dormant on clean inputs. The method is efficient, requiring only a small set of examples and admitting a closed-form solution. Across multiple safety-aligned LLMs and jailbreak benchmarks, our method achieves high triggered attack success while maintaining non-triggered safety and general utility.

</details>

### 29. Can Global XAI Methods Reveal Injected Behaviours in LLMs? SHAP vs Rule Extraction vs RuleSHAP

📄 [arXiv](https://arxiv.org/abs/2505.11189) · 🌐 [Project](https://doi.org/10.1145/3770855.3818093)　📅 2026-08　🏷 KDD 2026

**关键词**：`analysis`、`global XAI`、`injected behavior`、`LLM backdoor`

👤 **作者**：Francesco Sovrano

- 🎯 **研究动机**：全局XAI方法能否揭示LLM注入后门行为未知
- 🔬 **研究方法**：对比SHAP、规则提取与RuleSHAP对注入行为的可检出性
- 📌 **结论**：三类方法检出能力与局限各异

### 30. Broadening the Backdoor Basin: Understanding LLM Backdoors Collapse and Making Backdoors Persistent

🎓 [Official](https://icml.cc/virtual/2026/poster/66722)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`persistence`、`loss basin`、`backdoor attack`、`empirical evaluation`、`data poisoning`

👤 **作者**：Xingyi Zhao、Tian Xie、Xiaojun Qi、Depeng Xu、Shuhan Yuan

- 🎯 **研究动机**：许多 LLM 后门经不起下游 SFT——几何解释是常规投毒把后门损失驱入窄而尖的盆地，轻微参数漂移即快速遗忘
- 🔬 **研究方法**：BAD-BOOM 经更宽平滑最小化扩展平滑后门盆地：把 sharpness-aware minimization 扩展为 Fisher 诱导椭球约束，给后门敏感参数更大扰动预算
- 📌 **结论**：两种威胁设定、三种攻击场景、三个 LLM 与三个免触发 SFT 任务上持续保持高 ASR 且效用相当

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are vulnerable to backdoor attacks, yet we observe that many LLM backdoors do not survive when end users perform supervised fine-tuning (SFT). In this work, we provide a geometric explanation: by probing the backdoor objective under controlled weight perturbations, we find that conventional poisoning often drives the backdoor loss to a narrow and sharp basin; consequently, even modest parameter drift induced by downstream SFT can push the model out of the low-loss and high-ASR region, leading to rapid backdoor forgetting. Motivated by this insight, we propose BAD-BOOM, a resilient backdoor attack via broader smoothness minimization, which explicitly broadens and smooths the backdoor basin. BAD-BOOM extends sharpness-aware minimization with a Fisher-induced ellipsoidal constraint that allocates larger perturbation budgets to backdoor-sensitive parameters, encouraging solutions whose neighborhoods also maintain low backdoor loss. Across two threat settings, three attack scenarios, three open-source LLMs, and three trigger-free downstream SFT tasks, BAD-BOOM consistently preserves high ASR while maintaining competitive utility. The code is available at https://github.com/xingyizhao/BAD-BOOM.

</details>

### 31. Activation Decomposition and Steering for LLM Backdoor Remediation

🎓 [Official](https://aclanthology.org/2026.acl-long.2025/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`activation decomposition`、`steering`、`representation intervention`、`LLM backdoor`、`data poisoning`

👤 **作者**：Lingfeng Zhong、Qiongkai Xu、Usman Naseem

- 🎯 **研究动机**：现有 LLM 后门防御依赖辅助模型或安全数据集，两者并非总可获得
- 🔬 **研究方法**：提出 Contrastive-Selective Activation Decomposition and Steering（CS-ADS）：对比相对良性中毒设定分解特征向量获取修复方向，不依赖额外模型或数据集；利用被后门污染的 prompt 对仍以不同比例编码相同良性语义这一洞察
- 📌 **结论**：对多种 SOTA 后门攻击均有效，防御质量甚至优于基于数据集的对比 steering

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing works on defending against LLM backdoor attacks rely on either auxiliary models or safety-related datasets for defending against backdoor attacks on large language models, which are not always available. To address these challenges, we propose our we propose our Contrastive-Selective Activation Decomposition and Steering (CS-ADS), which contrasts relatively more benign and poisoned settings to decompose the feature vectors for steering without relying on additional auxiliary models or datasets. With such disentangled vectors for remediation, our method can achieve feasible defense qualities even better than dataset-based contrastive steering strategies. This novel decomposition-based solution is motivated by the key insight that feature representations of prompt pairs can encode the same benign semantics in different proportions, even when both prompt pairs are similarly backdoored. Such discrepancies allow our method to identify effective remediation directions for steering the generation process, thereby preventing undesired outputs. We evaluate CS-ADS against multiple state-of-the-art backdoor attacks, and experimental results show that CS-ADS provides effective defense across settings.

</details>

### 32. Backdoor Collapse: Eliminating Unknown Threats via Known Backdoor Aggregation in Language Models

📄 [arXiv](https://arxiv.org/abs/2510.10265) · 🌐 [Project](https://anonymous.4open.science/r/Locphylax) · 🎓 [Official](https://aclanthology.org/2026.acl-long.920/)　📅 2025-10　🏷 ACL 2026

**关键词**：`analysis`、`known-to-unknown`、`aggregation`、`LLM backdoor`、`data poisoning`、`model integrity`

👤 **作者**：Liang Lin、…、Qingsong Wen

- 🎯 **研究动机**：现有 LLM 后门防御依赖对触发器设置的不切实际假设，难以应对未知威胁
- 🔬 **研究方法**：发现向已中毒模型注入已知后门会使未知与新增后门在表示空间聚合，据此先注入已知触发器聚合后门表示，再恢复微调还原良性输出
- 📌 **结论**：多基准平均 ASR 降至 4.41%，优于基线 28.1%~69.3%，clean 精度损失在 0.5% 以内，且跨后门类型泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks are a significant threat to large language models (LLMs), often embedded via public checkpoints, yet existing defenses rely on impractical assumptions about trigger settings. To address this challenge, we propose \ourmethod, a defense framework that requires no prior knowledge of trigger settings. \ourmethod is based on the key observation that when deliberately injecting known backdoors into an already-compromised model, both existing unknown and newly injected backdoors aggregate in the representation space. \ourmethod leverages this through a two-stage process: \textbf{first}, aggregating backdoor representations by injecting known triggers, and \textbf{then}, performing recovery fine-tuning to restore benign outputs. Extensive experiments across multiple LLM architectures demonstrate that: (I) \ourmethod reduces the average Attack Success Rate to 4.41\% across multiple benchmarks, outperforming existing baselines by 28.1\%$\sim$69.3\%$\uparrow$. (II) Clean accuracy and utility are preserved within 0.5\% of the original model, ensuring negligible impact on legitimate tasks. (III) The defense generalizes across different types of backdoors, confirming its robustness in practical deployment scenarios.

</details>
