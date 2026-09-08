# 通用 Guard Model、评测与安全边界

[返回 Guardrail 领域目录](README.md)

## 研究方向

本页研究可复用于通用文本交互和结构化 Agent action 的外部 guard model：它们在主模型前后或动作执行前执行 prompt safety、response safety、tool-action safety、jailbreak、refusal 与 harm category 判断，并在生产系统中承担最终拦截层。除模型训练外，本页也关注 guardrail 放置位置、classifier architecture、可识别性、shortcut、over-refusal、计算开销和对自适应攻击的实际安全边界。Agent workflow 中的主条目仍进入 Agent Security；具有通用 guard-model 训练与评测贡献的手动精选论文可在此交叉收录。

## 研究脉络

- **固定分类基线：** 早期 guard model 将内容安全建模为固定 taxonomy 下的 prompt 或 response 分类，并用专门的小模型作为主模型外部防线。
- **Policy-grounded 数据：** Constitutional Classifiers 用自然语言 constitution 合成训练数据，Qwen3Guard 等模型进一步统一多语言、生成式和 streaming 审核接口。
- **生产架构：** 新一代系统采用 exchange／trajectory-level 判断、probe 与大 classifier 级联、分层推理、specialized SLM 和 failure-driven 自演化，以降低 over-refusal、under-defense、更新周期和推理开销；多层堆叠还必须测量共同原因导致的相关失效，而不能假定风险独立相乘。
- **安全边界：** 近期工作开始系统比较 encoder 与 decoder、输入与输出过滤及 guardrail fingerprint，并揭示长上下文稀释、检查—执行时效差、跨身份任务拆分、软仇恨／编码重构、refusal cue 和可复制上下文造成的失效；多 Agent 分歧也开始被用作人工复审信号。

## 通用 Guard Model 与生产架构

### 1. HiveTraceGuard-Pro: A Compact Generative Guardrail for Prompt Injection, Jailbreaks, and Adversarial Obfuscation

📄 [arXiv](https://arxiv.org/abs/2609.01046) · 🤗 [Model](https://huggingface.co/hivetrace/HiveTraceGuard-Pro)　📅 2026-09

**关键词**：`defense`、`compact guard`、`multilingual deployment`、`prompt injection`、`multilingual guardrail`、`Russian prompt injection`

👤 **作者**：Nikita Oblakov、Sabrina Sadiekh、Evgeniy Kokuykin

- 🎯 **研究动机**：生产 guardrail 需低延迟，而俄语 prompt injection 与表面混淆的证据严重不足
- 🔬 **研究方法**：提出从 Qwen3-0.6B LoRA 微调的 0.6B 生成式护栏 HiveTraceGuard-Pro，英俄双语训练、单条 safe/unsafe 评分规则、八种混淆变换增强
- 📌 **结论**：15 模型比较中俄语 clean robustness 组合 F1 最高（0.88）、俄语注入 recall 0.999、中位延迟 14.3ms 最低；但套件 FPR 0.268，且注入集至少 27.1% 与训练语料重叠

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Production LLMs must handle inputs that attempt to override system instructions, bypass safety policies or elicit harmful responses. A common mitigation is a separate guardrail model. Existing reports, however, provide little evidence on Russian prompt injection or Russian surface obfuscation. We present HiveTraceGuard-Pro, a 0.6B generative guardrail LoRA-tuned from Qwen3-0.6B. It is trained on Russian and English and uses one binary scoring rule (safe/unsafe) for the final target turn. Its training corpus pairs harmful examples, where a counterpart exists, with benign examples from the same domain and applies eight obfuscation transforms to both labels. In one harness, we compare HiveTraceGuard-Pro with thirty-four other guards on nineteen benchmark groups, sixteen of which are public. Its aggregate key is 0.7432, behind 0.7641 and 0.7552 for the two higher-scoring guards. Over the sixteen public groups alone, its key is 0.7153 and four of the thirty-four other suite guards score higher. In a fifteen-model comparison, HiveTraceGuard-Pro has the highest clean Russian robustness combined-F1 (0.88) and Russian prompt-injection recall (0.999). Both results use Russian sets assembled by our team, and at least 27.1% of the prompt-injection set overlaps the training corpus. Its 14.3 ms median latency is the lowest among those fifteen models in that run. Across the suite, FPR is 0.268 and FNR is 0.156. All reported response results use a legacy standalone-reply serialization rather than the natural assistant-role path of the shipped chat template. We release the merged weights on Hugging Face under Apache-2.0. The corpus, evaluation sets and evaluation code remain internal.

</details>

### 2. Regime-Conditional Verification: Correctness Estimation for Adapting and Monitoring Safety Classifiers

📄 [arXiv](https://arxiv.org/abs/2608.14089)　📅 2026-08

**关键词**：`detection`、`defense`、`safety-classifier adaptation`、`policy mismatch`、`drift monitoring`、`classifier adaptation`

👤 **作者**：Thiago Sandoval、Ufuk Topcu

- 🎯 **研究动机**：安全分类器决策反映训练学到的策略而非部署者策略，且随部署流量演化而退化
- 🔬 **研究方法**：RCV 轻量包装器从分类器内部表征估计每个预测与部署者策略不一致的概率并选择性纠正；同一估计提供无标签分布漂移检测
- 📌 **结论**：三个现成分类器×两基准全部改善策略遵循，不改分类器补上至多 0.81 此前漏检的不安全内容；十次保留攻击战役全部检出

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety classifiers deployed with large language models often fail for two reasons: their decisions reflect the policy learned during training rather than the deployer's desired policy, and their performance degrades as deployment traffic evolves. We present Regime-Conditional Verification (RCV), a lightweight wrapper that adapts an off-the-shelf safety classifier without retraining it. RCV estimates, from the classifier's internal representations, the probability that each prediction disagrees with the deployer's policy, and selectively corrects predictions likely to be wrong. The same correctness estimates also provide a label-free signal for detecting distribution shift, enabling a maintenance loop that updates the correctness estimation layer and resorts to classifier fine-tuning only when necessary. Across three off-the-shelf safety classifiers and two benchmark datasets, RCV improves adherence to the deployer's policy in every classifier-dataset combination, catching up to 0.81 of previously missed unsafe content without modifying the underlying classifier. In a deployment study with ten attack campaigns, each a harm category held out of RCV's training, RCV detects every campaign in a dedicated injection panel; in the maintenance census most drift episodes are repaired without updating the classifier, and the fine-tune is reserved for the residual episodes that repair does not restore.

</details>

### 3. Yesterday's Shield, Today's Spear: A Self-Evolving Safety Guardrail in Production

📄 [arXiv](https://arxiv.org/abs/2608.08471)　📅 2026-08

**关键词**：`defense`、`jailbreak`、`multi-agent system`、`agent guardrail`、`production guardrail`、`failure-driven training`

👤 **作者**：Cong Ming、…、Yingfei Xiang

- 🎯 **研究动机**：部署的 guardrail 一经训练即冻结，而新越狱手法与有害类别数天内出现，静态防御持续落后
- 🔬 **研究方法**：SESG 多 agent 系统监控线上流量，确认失败后由生成 agent 合成配对训练数据、验证 agent 纠偏、路由 agent 匹配训练动作并回传新版本
- 📌 **结论**：六轮线上演化中 1.7B guardrail 以 16-24 小时、约 2 小时人力适应新威胁（手工需 40-90 小时）；两个月自主关闭 14/15 个新威胁场景

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deployed LLM safety guardrails are predominantly static: trained once and frozen at release, while new jailbreak techniques and previously un-addressed harmful categories emerge within days, leaving the defense perpetually a step behind. We present SESG (Self-Evolving Safety Guardrails), a multi-agent system running in production. SESG monitors the live traffic behind a deployed guardrail and surfaces two classes of failure: jailbreaks novel in form and harmful categories novel in content. Once a failure is confirmed, a generation agent synthesizes paired training data targeted at it; a validation agent rebalances the batch toward the direction in which the deployed model errs, so that the model's own mistakes steer its training set; and a routing agent matches the training action to the diagnosed gap and returns the next version to production. Over six rounds of live evolution (V0 to V6), a 1.7B guardrail adapts to a new threat in 16-24 hours, with about 2 hours of human effort, versus the 40-90 hours of the manual process it replaces. On six emerging threats, it outperforms static guardrails from 0.6B to 9B and an adaptive baseline while preserving its general screening competence. Since April 2026, SESG has been the primary update pipeline of Sangfor's guardrail, autonomously closing 14 of 15 new threat scenarios in two months. We release 9 test sets for the 6 new threats at https://github.com/Trams1017/SESG. Warning: This paper contains examples that may be harmful or offensive.

</details>

### 4. HoloAegis: Frozen Representation, Topological Inference: Minimally Parametric Safety Manifolds for Zero-Shot LLM Guardrails

📄 [arXiv](https://arxiv.org/abs/2608.08485)　📅 2026-08

**关键词**：`defense`、`frozen representation`、`topological guard`、`training-free adaptation`

👤 **作者**：Tak Ho Alex Li、Kaijie Liu、Lik-Hang Lee、Kin Chung Ho、Ping Shum、Michael K. Ng

- 🎯 **研究动机**：微调扭曲预训练表征、生成式 judge 推理成本高，纯几何推理能否替代做安全判界未知
- 🔬 **研究方法**：HoloAegis 冻结编码器映射到单位球，以 Gibbs-Boltzmann 自由能 over 拓扑锚库做决策，双时间尺度 EMA 检测多轮语义漂移，仅锚数 K 与温度 tau 两个参数
- 📌 **结论**：八基准达 SOTA（AuthenHallu AUC 1.0000、HarmBench 0.9802），亚毫秒延迟、零冷启动数据、中文 CHIFRAUD 迁移 0.9758

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current LLM safety guardrails face a fundamental tension: fine-tuning distorts pre-trained representations while generative judges incur prohibitive inference costs. We challenge the prevailing paradigm by asking: can safety be achieved through pure geometric reasoning over frozen semantic representations? We present HoloAegis, a minimally parametric topological inference framework that decouples representation from reasoning. We term our approach minimally parametric because the only free parameters are the anchor count K and the temperature tau, both fixed after construction and requiring no gradient-based training. An un-fine-tuned encoder maps text to a unit sphere, after which all decisions are purely geometric. We formalize safety evaluation as a Gibbs-Boltzmann Free Energy computation over a pre-computed System Topology Anchor Bank, and we introduce Dual Time-Scale Exponential Moving Averages to detect progressive multi-turn semantic drift. Our key theoretical insight is a Topological Boundary Stability Conjecture: we provide theoretical motivation and strong empirical evidence that sparse anchor centroids stabilize the decision boundary against high-frequency lexical perturbations far better than full vector space methods. Evaluated across 8 benchmarks, HoloAegis achieves state-of-the-art accuracy (1.0000 AUC on AuthenHallu, 0.9802 on HarmBench) with sub-millisecond latency, zero cold-start data, and cross-lingual transfer (0.9758 AUC on Chinese CHIFRAUD).

</details>

### 5. TRACE: Trajectory Aware Reasoning for Multi-Turn Adversarial Conversation Evaluation

📄 [arXiv](https://arxiv.org/abs/2608.15594)　📅 2026-08

**关键词**：`defense`、`benchmark`、`trajectory reasoning`、`multi-turn jailbreak`、`intent interpretation`、`adversarial robustness`

👤 **作者**：Md Messal Monem Miah、Adrita Anika、Zhiyuan Yu、Ruihong Huang

- 🎯 **研究动机**：多轮越狱防御缺乏识别演化操纵模式的推理能力，常以过拒敏感话题换安全
- 🔬 **研究方法**：Trace 每次回应前从轨迹识别操纵线索、评估良性与对抗两种意图解释、打越狱分并提交 Allow/Caution/Decline；在 4k 对抗会话+2.4k 良性+600 敏感良性对话上 SFT 加 GRPO 多分量奖励训练
- 📌 **结论**：七个多轮攻击基准平均 ASR 14.5%（最强基线 31.4%、无防御 74.9%），过拒基准平均合规 93.3%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-turn jailbreak attacks have emerged as a critical safety threat to LLMs, as harmful objectives are decomposed across a sequence of apparently benign turns to bypass guardrails. Existing defenses lack the reasoning capacity to identify evolving manipulation patterns, often trading helpfulness for safety by over-refusing benign requests related to sensitive topics. We introduce Trace, a multi-turn defense with trajectory-aware structured reasoning. Before generating each response, the model identifies manipulation cues from the trajectory, evaluates both the benign and adversarial interpretations of user intent, assigns a jailbreak score, and commits to an action: Allow, Caution, or Decline. We curate 4k multi-turn adversarial conversations from five attack frameworks, pair them with 2.4k benign dialogs, and 600 sensitive-but-benign conversations. We train Llama-3.1-8B-Instruct with SFT and GRPO under a multi-component reward that jointly optimizes helpfulness on benign prompts and robustness against jailbreak attempts. Across seven multi-turn attack benchmarks, Trace attains an average attack success rate (ASR) of 14.5% against 31.4% for the strongest baseline and 74.9% for the undefended target, while significantly raising the attacker effort required per successful jailbreak. Trace also balances usability and safety, achieving a 93.3% average compliance on over-refusal benchmarks.

</details>

### 6. Speculative Probing: LLM Monitoring at Speculative-Decoding Cost

📄 [arXiv](https://arxiv.org/abs/2608.28099)　📅 2026-08

**关键词**：`tool`、`detection`、`context-aware probe`、`speculative decoding`、`runtime safety classifier`、`speculative classifier`

👤 **作者**：Collin Zhang、Tingwei Zhang、Vitaly Shmatikov

- 🎯 **研究动机**：hidden-state probe 只作用于单向量、缺上下文交互，专用 guard 模型或全 token 计算又成本过高，在线安全监控面临精度—效率权衡
- 🔬 **研究方法**：提出在目标序列末尾附加训练好的 soft prompt，把 LLM 自带的 speculative-decoding 模块改造成序列分类器，推理时直接复用 GPU 内已有的 KV cache
- 📌 **结论**：小 probe 在四类任务、四个模型（Qwen3.5-4B/9B/27B、MiniCPM4.1-8B）上稳定优于零样本 GPT-5.4-mini，多语言 prompt safety 上达到或超过 8B 专用 safety classifier，额外开销可忽略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Real-time classification during language model inference is valuable for safety filtering, behavioral analysis, and model monitoring, but current approaches force a trade-off between accuracy and efficiency. Hidden-state probes are fast but limited: they are either not context-aware: operating on a single vector and cannot model interactions across positions; or they are very costly: having dedicated classifier models (Llama Guard, Qwen Guard, LLM-as-judge) or performing computation on hidden states for all tokens and then pooling the results (MultiMax). This shows an intrinsic trade-off between efficiency and accuracy. However, we find that the speculative-decoding module in recent LLMs can be repurposed for efficient high-quality classification. By appending a trained soft prompt at the end of the target sequence, we can repurpose the speculative-decoding module into a sequence classifier. At inference time in a speculative-decoding pipeline, the KV cache is already in GPU memory, so classification adds negligible overhead. We evaluate on four classification tasks across four models (Qwen3.5-4B, 9B, 27B, MiniCPM4.1-8B). Our small probes consistently outperform zero-shot GPT-5.4-mini and, on multilingual prompt safety, match or beat specialized 8B safety classifiers (Qwen3Guard-Gen-8B, Llama-Guard-3-8B) without running a full LLM.

</details>

### 7. Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense

📄 [arXiv](https://arxiv.org/abs/2608.27945)　📅 2026-08

**关键词**：`defense`、`attack`、`intent-aligned retriever`、`cross-session risk`、`lightweight guard`、`cross-session decomposition`

👤 **作者**：Disen Liao、Yihan Wang、Freda Shi、Yaoliang Yu

- 🎯 **研究动机**：攻击者可把禁用目标拆成跨独立会话的良性子查询再重组，而这种 compositional safety risk 缺乏形式化刻画与防御
- 🔬 **研究方法**：形式化 compositional safety risk 并证明组合风险差距由允许子查询上的 excess loss 控制的条件迁移界；提出 22M 参数意图对齐检索器 IntentAlign-MiniLM 作为跨会话守卫
- 📌 **结论**：更大的 Qwen3/Gemma3 在固定分解—组合流水线下有害能力提升更高；IntentAlign-MiniLM 在留出意图检索上超过更大 embedding 模型，取得测试 guardrail 中最佳 learned-retriever harmful recall

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Scaling laws are usually read as a capability story: lower language-modeling loss yields more useful models. We study a safety consequence of this mechanism in \emph{cross-session decomposition attacks}, where benign-looking subqueries are asked across independent interactions and later recomposed toward a forbidden objective. We formalize this setting as \emph{compositional safety risk} and prove a conditional risk-transfer bound: when the reference environment already contains dispersed evidence for a risky reconstruction, the gap between deployed composed risk and reference composed risk is controlled by the model's excess loss on allowed subqueries. Synthetic withholding experiments show that wider transformers assign lower loss to held-out instructions that never appear verbatim in training but are recoverable from injected supporting facts. A 600-intent pretrained-LLM evaluation shows that larger Qwen3 and Gemma3 family members can yield greater harmful-capability uplift under a fixed decomposition-composition pipeline. As a defense, IntentAlign-MiniLM, our 22M-parameter intent-aligned retriever, outperforms much larger embedding models on held-out intent retrieval and yields the best learned-retriever harmful recall across tested guardrails. Code is available in \href{https://github.com/liaodisen/Cross-Session-Decomposition-Attacks}{our GitHub repository}.

</details>

### 8. Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator

📄 [arXiv](https://arxiv.org/abs/2608.27548) · 🤗 [Model](https://huggingface.co/nvidia/Nemotron-3.5-Content-Safety) · 📊 [Dataset](https://huggingface.co/datasets/nvidia/Nemotron-3.5-Content-Safety-Dataset)　📅 2026-08

**关键词**：`tool`、`compact guard model`、`prompt-response moderation`、`production deployment`、`multimodal moderator`、`image-conditioned safety`

👤 **作者**：Varun Singh、Anuj Doshi、Makesh Narsimhan Sreedhar、Shaona Ghosh、Katherine Luna

- 🎯 **研究动机**：部署场景的安全审核需覆盖图像、文档、生成回答与各域自定义策略，现有 guardrail 通常只覆盖部分设置，难以兼顾广覆盖、自定义策略与低算力
- 🔬 **研究方法**：发布 4B 视觉语言安全 moderator Nemotron 3.5 CS 及多模态多语言安全数据集，联合分类 12 种语言的 prompt、图像与回答；低延迟路径仅输出标签，按需生成应用自定义策略并指认违规类别的推理轨迹
- 📌 **结论**：在多模态安全、文本审核、跨语言鲁棒性、自定义策略遵循、良性误报与延迟评测中取得实用的覆盖—成本权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety moderation for deployed AI applications is moving beyond text-only prompts: systems increasingly need to judge images, documents, screenshots, and generated responses under policies that vary across domains. Existing guardrails usually cover only part of this setting, making it difficult to combine broad coverage, custom policy control, and low compute cost. We present Nemotron 3.5 Content Safety Moderator, also referred to as Nemotron 3.5 CS in this paper for brevity, a compact 4B vision-language safety moderator that jointly classifies user prompts, images, and assistant responses across 12 languages. Nemotron 3.5 CS returns safety labels for latency-sensitive moderation and can additionally produce concise reasoning traces that apply supplied custom policies and identify violated categories when reasoning is requested. We also release a multimodal and multilingual safety dataset for guard training, spanning human-labeled real-image moderation, benign vision-language and document tasks, synthetic rare-risk and jailbreak cases, and custom-policy examples. Across evaluations spanning multimodal safety, text moderation, multilingual robustness, custom-policy following, benign false positives, and latency, Nemotron 3.5 CS demonstrates a practical coverage tradeoff: it adds image-conditioned and policy-conditioned moderation while remaining broadly competitive with specialized guard models. These results suggest that compact vision-language moderators can serve as deployable front-line safety components, with reasoning used selectively for audit and policy review.

</details>

### 9. Enforcing LLM Safety through DMD-based Classification of Prompt-Response Embedding Dynamics

📄 [arXiv](https://arxiv.org/abs/2608.19579)　📅 2026-08

**关键词**：`detection`、`analysis`、`black-box safety classifier`、`Koopman dynamics`、`prompt-response interaction`、`embedding dynamics`

👤 **作者**：Mohamed Akrout、Olivera Kotevska、Dan Wilson

- 🎯 **研究动机**：黑盒、高效地检测 LLM 不安全输出仍是开放挑战
- 🔬 **研究方法**：把 prompt 与响应投影到高维嵌入空间，分别为安全与不安全 regime 拟合 Koopman 预测模型，以比较两 regime 预测误差的差分残差分数分类新输出
- 📌 **结论**：三个安全基准、三个嵌入模型上引入 prompt 嵌入一致改进——交互依赖违规配因果解码器（Llama-3）受益，仅响应违规更受益于稠密语义嵌入

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly deployed in high-stakes applications, yet their tendency to generate toxic, harmful, or policy-violating content poses significant risks. Detecting these unsafe outputs efficiently in a black-box manner remains an open challenge. In this paper, we extend a recently proposed dynamical systems framework designed for hallucination detection to LLM safety classification. By projecting both prompts and responses into high-dimensional embedding spaces and fitting separate Koopman-based predictive models for safe and unsafe regimes, we classify new outputs using a new differential residual score that compares prediction errors of the safe and unsafe regimes. A key contribution is the incorporation of the prompt and response embedding dynamics, yielding fitted Koopman operators that capture crucial interaction patterns. We evaluate our black-box method across three safety benchmarks using three embedding models. Our results show that incorporating prompt embeddings yields consistent improvements, particularly for interaction-dependent violations when paired with causal decoders (e.g., in Llama-3), while response-only violations benefit more from dense semantic embedding representations. These findings opens the door for using dynamical systems to analyze AI systems rather than the dominant paradigm of using AI to model dynamical systems.

</details>

### 10. A Self-Evolving Multi-Agent Framework Defense against LLM Jailbreak Attacks

📄 [arXiv](https://arxiv.org/abs/2608.26008)　📅 2026-08

**关键词**：`defense`、`cross-interaction memory`、`failure abstraction`、`self-evolving safeguard`、`adaptive jailbreak guard`、`persistent rule memory`

👤 **作者**：Tongyan Hu、Bryan Hooi

- 🎯 **研究动机**：静态 jailbreak 防御无法积累经验或适应新出现的攻击 wrapper
- 🔬 **研究方法**：把成功攻击抽象为 method-level rule 写入持久跨交互记忆，测试时复用与扩展，无参数更新
- 📌 **结论**：四个黑盒攻击家族上 ASR 显著下降，自适应组合 wrapper 下稳健且不增加过度拒答

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) remain vulnerable to jailbreak attacks that exploit techniques such as role-playing, obfuscation, code transformation, and multi-step indirection to elicit harmful outputs. As jailbreak strategies keep emerging, defenses have proliferated in an ongoing cat-and-mouse game, yet most remain static: their safety behavior is fixed at deployment, so they cannot accumulate defensive experience or adapt to unseen strategies. We propose a self-evolving test-time defense built around a persistent, cross-interaction rule memory: when an attack succeeds, the framework abstracts that failure into a method-level rule capturing the structural attack wrapper rather than the harmful topic, and reuses it against future inputs. Because rules are method-level, one induced rule generalizes across an entire attack family, and the label space expands as novel wrappers appear. The mechanism operates entirely through external memory and prompting, with no parameter updates, and applies to both open-weight and black-box API models. We realize it as four cooperating modules, but the contribution is the memory-based adaptation mechanism, not the module decomposition. Across four black-box jailbreak families and multiple models, our method substantially reduces attack success rates while preserving benign utility, remains robust under an adaptive composite-wrapper attack, and does not increase over-refusal as the memory grows.

</details>

### 11. HRGuard: Gating Relationship Manipulation in Multi-Turn Agentic AI Conversations

📄 [arXiv](https://arxiv.org/abs/2608.25340)　📅 2026-08

**关键词**：`defense`、`harmful compliance`、`relationship manipulation`、`stateful monitoring`、`multi-turn relationship harm`、`dual gate`

👤 **作者**：Pei-Sze Tan、Tasuku Igarashi、Isao Echizen

- 🎯 **研究动机**：Agentic AI 可被滥用于人际操纵且角色敏感：操纵者请求应阻断、求助者应获支持，多轮动作可组合成危害
- 🔬 **研究方法**：构建 1000 段五轮对话 benchmark；HRGuard 以 pre-generation gate 与维护衰减累积风险状态的 turn-level gate 中断操纵工作流
- 📌 **结论**：八个生成模型上降低有害顺从并保留受害者保护指引，优于通用安全 prompt 与三个通用 guard

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic AI assistants are increasingly used in everyday life. However, they may also be misused to support harmful manipulation in interpersonal relationships. This problem is role-sensitive. Requests from users who seek to manipulate others should be blocked. Users who seek protection from manipulation should instead receive supportive guidance. We study agentic relationship harm, which describes harm to human-human relationships that is mediated or assisted by AI agents. In multi-turn settings, individually plausible actions may combine into a harmful workflow. We introduce a benchmark of 1,000 five-turn conversations. It covers both attacker-side and victim-side scenarios. It also includes direct and adversarially paraphrased variants. We further propose HRGuard. It includes an online pre-generation gate and a turn-level post-generation gate. The post-generation gate maintains a decayed cumulative risk state and interrupts emerging manipulative workflows. Across eight generation models, HRGuard reduces harmful compliance while preserving victim-side protective guidance. It also outperforms a generic safety prompt and three general-purpose guard models. Independent-judge evaluation supports the main findings. Under our evaluation protocol, the tested generic prompt and general-purpose guards leave substantial residual risk, motivating turn-aware relationship-specific evaluation.

</details>

### 12. LMSM: LLM Security Framework Inspired by Linux Security Modules

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

### 13. Beyond Over-Refusal: Defending Indirect Prompt Injection via Latent Instruction Manifolds

📄 [arXiv](https://arxiv.org/abs/2608.22248)　📅 2026-08

**关键词**：`defense`、`analysis`、`Code Agent`、`indirect prompt injection`、`instruction-data separation`、`agent safeguard`

👤 **作者**：Jiahao Chen、…、Shouling Ji

- 🎯 **研究动机**：LLM 难以区分指令与数据导致间接 prompt injection，现有 guardrail 又陷入高延迟或严重过度拒答的安全—效用权衡
- 🔬 **研究方法**：以理论与实证说明 LLM 内在可分离 instruction 与 data；AEGIS 提取 instruction-sensitive projector 识别恶意指令，并以 Unified Multi-Layer Consensus 聚合网络深度上拓扑不同的信号
- 📌 **结论**：对启发式与优化式 IPI 攻击均显著优于基线，缓解高延迟与过度拒答的权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have been integrated into complex ecosystems (e.g., Code Agents), while Indirect Prompt Injection (IPI) attacks have emerged as critical barriers to their safe deployment. Attackers exploit LLMs' indistinguishability between "instructions" and "data" to manipulate LLMs via maliciously injected instructions. Existing defenses, however, face an intractable safety-utility trade-off: most guardrails either incur high latency or suffer from severe over-refusal. In this paper, we first demonstrate that LLMs can separate instruction from data intrinsically with both theoretical and empirical evidence. Inspired by this insight, we propose AEGIS (Adaptive Ensemble Guard for Injection Shielding). AEGIS extracts instruction-sensitive projectors to identify malicious instructions and leverages a Unified Multi-Layer Consensus mechanism that aggregates topologically distinct signals across the network depth. Empirical evaluations show that AEGIS achieves remarkable detection performance against both heuristic and optimization-based attacks compared to baselines, highlighting its potential to mitigate IPI. Code is available at https://github.com/xaddwell/AEGIS

</details>

### 14. A Reproducible, License-Aware Distillation Recipe for CPUDeployable Safety Classification

📄 [arXiv](https://arxiv.org/abs/2608.21570)　📅 2026-08

**关键词**：`tool`、`defense`、`distilled guard model`、`CPU deployment`、`license-aware data`、`lightweight guard`

👤 **作者**：Edson Rodrigues da Cruz Filho、…、Gustavo Voltani Von Atzingen

- 🎯 **研究动机**：开源 guard 模型普遍 1–9B 参数、面向 GPU，在 CPU 上每请求需数秒，难以在普通硬件上部署安全层
- 🔬 **研究方法**：可复现、许可证感知的蒸馏配方：强开源 guard 为约 97,000 条 prompt（来自 24 个公开数据集、七类安全类别）打标，训练词法、浅层、encoder 与生成式小 student，语料按许可证边界划分并用独立 6,361 行 gold benchmark 评估
- 📌 **结论**：蒸馏 student 在对抗文本上与 teacher 置信区间重叠，最小生成式 student 无害误报 3.8% 优于 8B teacher 的 4.8%，encoder 在 CPU 上约 24ms/请求；per-class rebalancing 是唯一决定性成分

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deploying a safety layer for large language models on commodity hardware is constrained by the guards available to do it: current open guard models hold between 1 and 9 billion parameters, are oriented toward the graphics processing unit, and answer in seconds per request on a central processing unit. This paper presents a reproducible, license-aware knowledge-distillation recipe addressing that constraint. A strong open guard labels a corpus of roughly 97,000 prompts, drawn from 24 public datasets, into seven safety categories aligned to a public hazard taxonomy, and a fleet of small students spanning lexical, shallow, encoder and generative architectures is trained to reproduce that signal. The corpus is partitioned at the license boundary, so that a deployable and a research model differ only in their training data and the cost of that restriction becomes measurable. Every model is scored against an independent gold benchmark of 6,361 rows over four slices, labeled apart from the teacher and including a slice of harmless prompts that makes over-defense measurable. The distilled students match the teachers on adversarial text within overlapping confidence intervals and reduce false alarms on harmless prompts, the smallest generative student reaching 3.8% against 4.8% for the 8-billion-parameter teacher, while the encoder classifies in roughly 24 ms per request on CPU. Per-class rebalancing is the only decisive ingredient of the recipe. No superiority over the distilled guards is claimed; on the clean reference slice they remain ahead.

</details>

### 15. BanglaVeilGuard: Cross-Script Safety Benchmarking and Lightweight Guardrails for Bangla Large Language Models

📄 [arXiv](https://arxiv.org/abs/2608.21880)　📅 2026-08

**关键词**：`defense`、`benchmark`、`cross-script prompt guard`、`lightweight classifier`、`over-refusal`、`lightweight prompt guard`

👤 **作者**：Md. Rakibul Hassan、Muhammad Iqbal Hossain

- 🎯 **研究动机**：孟加拉语用户混用罗马化、Banglish、code-mixed、噪声与方言形式书写，英语中心或标准文字的 benchmark 无法评估孟加拉语 LLM 安全，跨文字可绕过防御
- 🔬 **研究方法**：BanglaVeilGuard 覆盖六种语言形态的 2,366 条 prompt（另 354 条 held-out），用非破坏性多视图规范化加 prompt 风险分类器与阈值预生成 gate，不改目标模型权重
- 📌 **结论**：Claude Opus 4.8、BanglaLLama、TituLLM 的 ASR 从 93.8–100% 降至 6.3%，unsafe recall 88.5% 超各 guard 基线；残余代价是方言与噪声良性 prompt 的过度拒答

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Bangla large language model (LLM) safety is difficult to evaluate with English-centric or standard-script benchmarks because Bangla users routinely write across scripts, spellings, code-mixed forms, and regional registers. This paper presents BanglaVeilGuard, a compact Bangla-first safety benchmark and lightweight prompt guard for six language forms: standard Bangla, Romanized Bangla, Banglish, code-mixed Bangla--English, noisy Bangla, and dialectal Bangla. The benchmark contains 2,366 quality-filtered prompts and a held-out 354-prompt evaluation split spanning unsafe, safe, and safe-sensitive requests. BanglaVeilGuard uses non-destructive multi-view normalization with a prompt-risk classifier and thresholded pre-generation gate, allowing it to screen prompts for heterogeneous target models without changing their weights. Across target-model families, guarded runs reduce attack success under deterministic response scoring from 93.8--100.0\% to 6.3\% for Claude Opus 4.8, BanglaLLama, and TituLLM; TigerLLM-1B with BanglaVeilGuard achieves 78.2\% accuracy with 8.8\% ASR. The prompt guard also attains 88.5\% unsafe recall, substantially above the evaluated prompt-only guard baselines. The main remaining cost is over-refusal on dialectal and noisy benign prompts, revealing a concrete safety-helpfulness frontier for Bangla LLM deployment.

</details>

### 16. AI Watchdog: Agent Interfaces for Detecting and Defending Against Manipulative Dark Patterns in AI Conversations

📄 [arXiv](https://arxiv.org/abs/2608.21841)　📅 2026-08

**关键词**：`defense`、`turn-level guard`、`dark-pattern detection`、`independent monitoring`、`conversational manipulation`、`dark-pattern warning`

👤 **作者**：Rachel Poonsiriwong、…、Pat Pataranutaporn

- 🎯 **研究动机**：对话式 AI 日益影响重大决策，用户却缺乏识别和抵抗对话操纵（dark patterns）的支持工具
- 🔬 **研究方法**：AI Watchdog 浏览器端独立界面用开源 turn-level 分类器监测五类 dark pattern（sycophancy、品牌偏见、拟人化、sneaking、有害生成）并预警；预注册五条件组间实验（N=150）比较干预时机与形态
- 📌 **结论**：仅带认知强制的即时警告显著降低用户对含 dark pattern 建议的遵从（71.7%→53.7%，降 18 个百分点）；识别操纵与行为抵抗是可分离的结果

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Conversational AI increasingly shapes consequential decisions, yet users have limited support for recognizing and resisting manipulation. We present AI Watchdog, a browser-based agent interface that monitors live conversations, detects five dark-pattern categories, including sycophancy, brand bias, anthropomorphization, sneaking, and harmful generation, and alerts users when they occur. Its open-weight turn-level classifier supports independent deployment and a path toward local inference, preserving user privacy while remaining separate from the conversational AI. We evaluated AI Watchdog in a preregistered, five-condition between-subjects experiment (N = 150) comparing a no-intervention control with four configurations varying nudge timing (prebunking vs. just-in-time) and engagement mode (without vs. with cognitive forcing). Results show that participants rarely flagged manipulative turns across all conditions, and post-task awareness did not differ significantly across groups. However, just-in-time warnings without cognitive forcing were the only intervention to significantly reduce compliance with AI-steered recommendations containing dark patterns, lowering compliance from 71.7% to 53.7%, an 18 percentage-point reduction. Exploratory analyses further showed that lower misinformation susceptibility was associated with greater flagging but not lower compliance, while higher AI trust was associated with greater compliance and lower reported awareness. Together, these findings suggest that explicit recognition of conversational dark patterns and behavioral resistance to AI steering may be distinct outcomes, motivating further investigation of timely, low-friction defensive interfaces.

</details>

### 17. StepGuard: Learning Step-Level Guardrails with Scalable Supervision and Safety-Utility Balancing

📄 [arXiv](https://arxiv.org/abs/2608.24777)　📅 2026-08

**关键词**：`defense`、`pre-execution guard`、`step-level tool action`、`safety-utility balance`、`step-level guard model`、`Balance-GRPO`

👤 **作者**：Zhijie Zheng、…、Dongrui Liu

- 🎯 **研究动机**：现有 guardrail 多在轨迹完成后评估，step 级工具动作的执行前监控不足
- 🔬 **研究方法**：StepGuard 执行前检查工具动作；StepGen 生成同上下文异动作的安全/不安全样本，Balance-GRPO 动态平衡两类防御
- 📌 **结论**：AgentDojo 与 AgentDyn 上平均 ASR 相对降 77.3%，utility 仅降 2.8 个百分点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents can interact with external environments through tool invocation, but this capability also introduces security risks such as file modification, information leakage, and unauthorized actions. Existing guardrails often evaluate completed trajectories, leaving pre-execution monitoring of step-level actions underexplored. We propose StepGuard, a step-level guard model that can audit completed agent trajectories and check tool actions before they are executed. To train StepGuard, we introduce StepGen, an automatic data engine that generates safe and unsafe trajectories with the same context but different actions at the risky step. To further reduce over-defense and under-defense, we propose Balance-GRPO, which dynamically balances learning between safe and unsafe actions based on their observed accuracy. Experiments show that StepGuard achieves the highest average accuracy among open-weight guard models, with performance comparable to GPT-5.4. When used to guard agents on AgentDojo and AgentDyn, StepGuard reduces mean attack success rate by 77.3% relative to the no-guard setting, while mean utility drops by only 2.8 percentage points.

</details>

### 18. ProbGuard: Calibrated Safety Risk Estimation from LLM Output Distributions

📄 [arXiv](https://arxiv.org/abs/2608.10621)　📅 2026-08

**关键词**：`defense`、`jailbreak`、`uncertainty calibration`、`guard model`

👤 **作者**：Xinzhe Huang、…、Tianhang Zheng

- 🎯 **研究动机**：现有 guard 把安全评估当确定性分类，忽略生成早期的内在不确定性并丢弃输出分布中的概率信息
- 🔬 **研究方法**：ProbGuard 为架构无关的概率 guard：把安全风险形式化为前缀继续生成的不安全概率，Monte-Carlo 采样估计并经分布信号后训练校准
- 📌 **结论**：九个模型-数据集组合全部取得最佳校准（Brier 降 79.6%、ECE 降 71.9%）；仅看前十步解码即把六种越狱攻击的 ASR 限制在 1% 以内

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent research on Large Language Model (LLM) safety has widely adopted guardrails to identify unsafe LLM outputs. Existing guardrails typically formulate safety assessment as a deterministic classification task, mapping a discrete token sequence to a discrete safety label. However, this paradigm has two limitations: First, safety assessment is inherently an uncertain problem, particularly during the early generation state. Second, relying solely on discrete token sequences discards the rich probabilistic information embedded in the LLM output distribution. To address these limitations, we propose the first completely probabilistic architecture-agnostic guardrail \textsc{ProbGuard} to leverage the LLM early output distributional signals for estimating and calibrating the safety probability, thereby enabling early stopping of unsafe ongoing outputs. Specifically, given an LLM's generated prefix distribution, we formulate the safety risk as the unsafe probability of its continued generation dynamics and estimate this risk by Monte-Carlo sampling. Through post-training on the distributional signals and calibrated safety risk, \textsc{ProbGuard} achieves the best calibration performance across all nine model--dataset combination settings, reducing the average Brier score and ECE by 79.6\% and 71.9\%, respectively, over the best baseline. \textsc{ProbGuard} further limits the attack success rate to at most 1\% across six representative jailbreak attacks after observing the LLM early output distributions from only the first ten decoding steps.

</details>

### 19. DARWIN: Evolving Jailbreak Adversary and Guardrail for LLM Safety Evaluation and Protection

📄 [arXiv](https://arxiv.org/abs/2607.19829)　📅 2026-07

**关键词**：`defense`、`co-evolution`、`adaptive jailbreak`、`online adversarial training`

👤 **作者**：Weiwei Qi、…、Kui Ren

- 🎯 **研究动机**：固定攻击集评估与固定数据集训练护栏均为静态公式，而真实对手持续演化扩展攻击空间
- 🔬 **研究方法**：提出 DARWIN 开放式演化攻防框架：DARWIN-Attack 经策略发现、变异、选择与反馈组合进化攻击者，DARWIN-Guard 在恶意与伪装良性查询上联合在线对抗训练以识别底层意图
- 📌 **结论**：攻击侧在 DeepSeek-V4-Pro 与 YuFeng-XGuard 上近 100% ASR、GPT-5.5 上超 90%；Guard 侧 12 个安全基准平均不安全召回 91.6% 且良性通过率近 100%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Most existing LLM safety evaluation and defense methods follow a static formulation: jailbreak vulnerabilities are evaluated with fixed attack methods, and guardrails are trained on fixed malicious prompt datasets. However, real-world adversaries continuously evolve their capabilities and expand the attack space. To address this challenge, we propose DARWIN, an evolutionary attack-defense framework that formulates jailbreaking as an open-ended evolution process and continuously updates guardrails through an evolving attack-defense loop. DARWIN-Attack is an evolutionary adversary that expands its capabilities through strategy discovery, mutation, selection, and feedback-driven composition. It collects strategies from broad external sources, generates new variants through self-reflection and genetic evolution, and retains effective strategies based on their performance against aligned LLMs. During attack execution, DARWIN-Attack adaptively selects and combines evolved strategies according to feedback from target LLMs and guardrails. Across frontier models and guardrails, it achieves state-of-the-art attack success rates, including nearly 100% on DeepSeek-V4-Pro and YuFeng-XGuard and over 90% on GPT-5.5. On the defense side, we introduce DARWIN-Guard, an online adversarial training paradigm that iteratively learns from emerging adversarial samples generated by DARWIN-Attack. To improve robustness without sacrificing utility, DARWIN-Guard jointly trains on malicious and benign disguised queries, encouraging the model to identify underlying intent rather than superficial attack patterns. DARWIN-Guard achieves an average unsafe recall of 91.6% across 12 safety benchmarks, outperforming strong guardrails such as YuFeng-XGuard and Nemotron Guard, while maintaining a nearly 100% pass rate on standard benign datasets.

</details>

### 20. kNNGuard: Turning LLM Hidden Activations into a Training-Free Configurable Guardrail

📄 [arXiv](https://arxiv.org/abs/2607.02072)　📅 2026-07

**关键词**：`defense`、`hidden activation`、`training-free guard`、`domain configuration`、`activation-space kNN`、`low-latency adaptation`

👤 **作者**：Mahmoud Abdelfattah、Hamid Nasiri、Peter Garraghan

- 🎯 **研究动机**：现有护栏依赖微调分类器，泛化低、推理延迟高
- 🔬 **研究方法**：提出 kNNGuard 免训练护栏：仅用 50 条安全/不安全提示库提取现成 LLM 多层激活，融合激活空间与嵌入空间 kNN 分数分类
- 📌 **结论**：六域上 F1 持平或超越微调 SOTA 护栏，快 2.7 倍（比微调分类器快 10 倍）；域适配只需 10 秒内更新提示库

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed in domains requiring guardrails to detect unsafe, off-topic, or adversarial prompts. Existing guardrails predominantly rely on fine-tuning to build classifiers, which often suffer from low generalization and high inference latency. We present kNNGuard, a training-free guardrail that utilizes the activation space of an off-the-shelf LLM. Given a small bank of 50 safe and unsafe prompts, kNNGuard extracts hidden activations and performs multi-layer kNN fusing activation-space and embedding-space scores for classification. Across six domains spanning topical and security prompts, kNNGuard achieves competitive or superior F1 compared to fine-tuned state-of-the-art guardrails while running 2.7x faster than the best comparable guardrail, and 10x faster than a fine-tuned safety classifier without gradient updates or fine-tuning. Domain adaptation requires only updating the labeled bank, which can be constructed in under 10 seconds and several orders of magnitude faster than established guardrails. We also analyze the impact of system prompts, layer selection, and integration into production LLM pipelines as a configurable, low-latency guardrail.

</details>

### 21. Stateful Guardrails for Multi-Turn LLM Systems: A Conversational Risk Accumulation Framework

📄 [arXiv](https://arxiv.org/abs/2607.19361)　📅 2026-06

**关键词**：`defense`、`stateful guardrail`、`risk accumulation`、`multi-turn monitoring`

👤 **作者**：Sanjay Mishra、Divya Chukkapalli、Ganesh R. Naik

- 🎯 **研究动机**：多数护栏孤立评估单轮提示-响应对，错过良性轮次组合成伤害的会话级失败（意图漂移、碎片拼装、敏感度累积）
- 🔬 **研究方法**：提出会话层 CRA 框架：追踪语义漂移、敏感度加权信息累积图与顺从梯度信号，提供无监督凸融合与家族对抗训练的 CRA-Net；发布 CRA-Bench v0.1/v0.2 与五家族扩展集及轨迹原生评估协议
- 📌 **结论**：确立会话级风险累积的可测框架与配套基准

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Most safety guardrails for large language models (LLMs) evaluate each prompt-response pair in isolation, which misses failures that arise only over a dialogue as benign turns compose into harm. We term this Conversational Risk Accumulation (CRA): gradual intent drift, fragmented assembly of prohibited instructions, and sensitivity build-up from repeated disclosures. We propose a session-layer CRA Framework that tracks three trajectory signals: semantic drift from a session anchor, a sensitivity-weighted information accumulation graph over extracted entities, and a compliance-gradient signal capturing increasing willingness to comply. For scoring, we provide (i) an unsupervised convex fusion for attribution and ablations, and (ii) CRA-Net DA, a compact learned trajectory model trained with family-adversarial objectives to reduce length and topic-coverage confounds. To benchmark CRA, we release CRA-Bench v0.1 (1,200 eight-turn sessions across three threat families with topic-matched benign twins), CRA-Bench v0.2 (LLM-paraphrased variants to reduce template artifacts), and an extended 5-family set (2,000 sessions adding persona priming and context stuffing). We introduce a trajectory-native evaluation protocol with session-level splits, mixed-set threshold calibration, Trajectory AUROC, turns-to-detection, calibrated false-positive metrics, bootstrap confidence intervals, leave-one-family-out diagnostic stress tests, and synthetic-to-human transfer checks. Claims focus on within-distribution session scoring on CRA-Bench and human-transfer subsets.

</details>

### 22. Fence: Specialized SLM Guardrails for LLM Applications

📄 [arXiv](https://arxiv.org/abs/2607.18268)　📅 2026-05

**关键词**：`tool`、`specialized SLM guard`、`application policy`、`low-latency moderation`

👤 **作者**：Kumud Lakara、Ruibo Shi、Fran Silavong

- 🎯 **研究动机**：闭源 LLM 应用需要超越通用毒性/偏见过滤的应用级护栏（幻觉、话题漂移、行为偏差），但数据稀缺与标注昂贵
- 🔬 **研究方法**：提出 Fence：受 GAN 设计启发的合成数据生成方法训练 SLM 作为应用专用护栏，编码用例特定规则
- 📌 **结论**：高质量合成数据训练的 SLM 护栏性能超过基于提示的 LLM 护栏

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Real-world applications that use closed-source large language models (LLMs) need advanced safety measures that go beyond the basic content filters. Content moderation filters such as toxicity and bias have relatively standard definitions where as application specific guardrails like hallucination, topic drift and behaviour deviation are more difficult to model and can vary by use case. Additionally, data scarcity and annotation costs, make the process of creating and testing specialized guardrails challenging. In this work, we propose using Small Language Models (SLMs) trained on synthetic data as specialized guardrails for LLM applications. We introduce a novel synthetic data generation method inspired by the design of Generative Adversarial Networks (GANs) to generate high quality synthetic data samples which can be used to train SLMs to encode use case specific guardrail information and hence function as specialized guardrails. Our experiments demonstrate that SLM guardrails trained on high quality synthetic data show performance gains over prompt based LLM guardrails.

</details>

### 23. Why Do Safety Guardrails Degrade Across Languages?

📄 [arXiv](https://arxiv.org/abs/2605.17173) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-05

**关键词**：`defense`、`analysis`、`guard model`、`content moderation`、`safety-utility trade-off`、`cross-lingual safety`

👤 **作者**：Max Zhang、Ameen Patel、Sang T. Truong、Sanmi Koyejo

- 🎯 **研究动机**：JSR 把多种安全驱动因素混为一体，掩盖非英语安全退化的具体成因
- 🔬 **研究方法**：多组 IRT 潜变量模型解耦语言无关鲁棒性 θ、prompt 难度 β、语言处理难度 γ 与 prompt 特定跨语言安全差 τ；基于 MultiJail 评 61 个模型配置、10 种语言共 190 万条回复
- 📌 **结论**：22 个配置在英语上反而更脆弱；高 τ prompt 集中于盗窃、武器等物理伤害与低资源语言；框架 AUC 0.940，整语言留出仍达 0.875

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models exhibit safety degradation in non-English languages. Standard evaluation relies on Jailbreak Success Rate (JSR), which confounds several safety-driving factors into one, obscuring the specific cause(s) of safety failure. We introduce a latent variable model, a Multi-Group Item Response Theory (IRT) framework, that decouples language-agnostic safety robustness ($θ$), intrinsic prompt hardness ($β$), global language processing difficulty ($γ$), and a prompt-specific cross-lingual safety gap ($τ$). Using the MultiJail dataset, we evaluate the safety robustness of 61 model configurations across 5 closed-model families and 10 languages of varying resource, aggregating a dataset of 1.9 million responses. Exploratory Factor Analysis shows safety is primarily unidimensional: models refuse different harm types mainly through a shared mechanism. Contrary to the expected trend that safety degrades largely in low-resource languages, 22 model configurations are more vulnerable in English than in low-resource languages. Low-resource languages produce more uncertain responses (high entropy) than high-resource languages. Also, high-$τ$ prompts cluster in physical harm categories like Theft and Weapons and lower-resource languages, trends validated through cross-dataset generalization. While global translation quality shows low correlation with $τ$, severe mistranslations drive high-bias outliers, as validated by native speakers. Cultural and conceptual grounding mismatches may also contribute to $τ$. In predictive validation, the IRT framework achieves $\mathrm{AUC} = 0.940$, and unlike rate baselines stays predictive when a whole language is held out ($0.875$). Our framework reveals concept-language vulnerabilities that aggregate metrics obscure, enabling fairer cross-lingual safety evaluation and targeted improvements in dataset construction.

</details>

### 24. Safe-Unsafe Concept Separation Emerges from a Single Direction in Language Models Activation Space

🎓 [Official](https://aclanthology.org/2026.eacl-long.139/)　📅 2026-03　🏷 ACL 2026

**关键词**：`defense`、`analysis`、`activation guardrail`、`safety direction`、`multilingual monitoring`、`activation monitoring`

👤 **作者**：Andrea Ermellino、Lorenzo Malandri、Fabio Mercorio、Antonio Serino

- 🎯 **研究动机**：现有安全防护依赖侵入式微调或资源低效的生成式外部检查，缺乏对安全概念几何结构的机理刻画
- 🔬 **研究方法**：定位预训练表示中安全与不安全概念最大可分的层，在该层激活空间上仅用线性分类器实施安全判定，无需修改权重
- 📌 **结论**：安全分离由激活空间单一层的方向涌现，跨 8 个领域、3 类任务与 16 种非英语语言有效，比传统生成式护栏更鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring the safety of Large Language Models (LLMs) is a critical alignment challenge. Existing approaches often rely on invasive fine- tuning or external generation-based checks, which can be opaque and resource-inefficient. In this work, we investigate the geometry of safety concepts within pretrained representations, proposing a mechanistic methodology that identifies the layer where safe and unsafe concepts are maximally separable within a pretrained model’s representation space. By leveraging the intrinsic activation space of the optimal layer, we show that safety enforcement can be achieved via a simple linear classifier, avoiding the need for weight modification. We validate our framework across multiple domains (regulation, law, finance, cybersecurity, education, code, human resources, and social media), diverse tasks (safety classification, prompt injection, and toxicity detection), and 16 non-English languages on both encoder and decoder architectures. Our results show that: (i) the separation between safe and unsafe concepts emerges from a single layer direction in the activation space, (ii) monitoring internal representations provides a significantly more robust safeguarding mechanism compared to traditional evaluative or generative guardrail paradigms.

</details>

### 25. Safeguarding Language Models via Self-Destruct Trapdoor

🎓 [Official](https://aclanthology.org/2026.eacl-long.326/)　📅 2026-03　🏷 ACL 2026

**关键词**：`defense`、`embedded guardrail`、`overflow trapdoor`、`behavior restriction`、`jailbreak defense`

👤 **作者**：Shahar Katz、Bar Alon、Ariel Shaulov、Lior Wolf、Mahmood Sharif

- 🎯 **研究动机**：需要无需后置过滤且零开销地限制 LLM 特定行为（如有害文本生成）
- 🔬 **研究方法**：利用 BF16 等有限精度矩阵乘法的溢出特性，将选定权重替换为陷阱值，仅在模型执行目标行为时触发系统错误，仅需少量样本校准
- 📌 **结论**：在 5 个 LM 家族上对越狱攻击提供有竞争力的防护且不损基准精度，还可缓解偏见生成并支持模型指纹

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The potential misuse and misalignment of language models (LMs) is a central safety concern. This work presents Self-Destruct, a novelmechanism to restrict specific behaviors in LMs by leveraging overlooked properties of the underlying hardware. We observe that the LMframeworks use limited-precision formats (e.g., BF16), which are vulnerable to overflow errors during matrix multiplications. Exploitingthis property, Self-Destruct replaces selected weights in pre-trained LM layers with values that act as traps, triggering a system error onlywhen the model engages in targeted behaviors, such as harmful text generation, while leaving normal functionality unaffected. Unlike posthoc filters, this safeguard is embedded directly within the model, introduces neither inference overhead nor auxiliary models, and requires only a set of examples for calibration. Extensive experiments with five LM families demonstrate that Self-Destruct provides competitive protection against jailbreak attacks while preserving accuracy on standard benchmarks. In addition, we also show that Self-Destruct is versatile, helping mitigate biased text generation and enable model fingerprinting, highlighting the potential of hardware-aware safeguards as an efficient, low-overhead complement to existing LM defenses.

</details>

### 26. Lattice: Generative Guardrails for Conversational Agents

📄 [arXiv](https://arxiv.org/abs/2601.17481) · 🌐 [Project](https://trustagenticai.github.io/AAAI2026/AAAI-Workshop/72.pdf)　📅 2026-01　🏷 AAAI 2026

**关键词**：`defense`、`adversarial robustness`、`guard model`、`content moderation`

👤 **作者**：Emily Broadhurst、Tawab Safi、Joseph Edell、Vashisht Ganesh、Karime Maamari

- 🎯 **研究动机**：静态规则 guardrail 无法适应新威胁与部署环境变化
- 🔬 **研究方法**：Lattice 两阶段：从标注样本经迭代模拟与优化自构建 guardrail；部署后经风险评估、对抗测试与合并的闭环持续改进
- 📌 **结论**：ProsocialDialog 上 F1 达 91%，超关键词基线 43pp、LlamaGuard 25pp、NeMo 4pp，跨域数据上闭环再提升 7pp

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Conversational AI systems require guardrails to prevent harmful outputs, yet existing approaches use static rules that cannot adapt to new threats or deployment contexts. We introduce Lattice, a framework for self-constructing and continuously improving guardrails. Lattice operates in two stages: construction builds initial guardrails from labeled examples through iterative simulation and optimization; continuous improvement autonomously adapts deployed guardrails through risk assessment, adversarial testing, and consolidation. Evaluated on the ProsocialDialog dataset, Lattice achieves 91% F1 on held-out data, outperforming keyword baselines by 43pp, LlamaGuard by 25pp, and NeMo by 4pp. The continuous improvement stage achieves 7pp F1 improvement on cross-domain data through closed-loop optimization. Our framework shows that effective guardrails can be self-constructed through iterative optimization.

</details>

### 27. YuFeng-XGuard: A Reasoning-Centric, Interpretable, and Flexible Guardrail Model for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2601.15588)　📅 2026-01

**关键词**：`tool`、`dynamic safety policy`、`hierarchical reasoning`、`risk taxonomy`

👤 **作者**：Junyu Lin、…、Yitong Yang

- 🎯 **研究动机**：现有 guardrail 依赖快速分类或事后规则，透明度差、策略僵固或推理成本高
- 🔬 **研究方法**：YuFeng-XGuard 输出风险类别、可配置置信度与自然语言解释，采用首 token 初判、按需解释的分层推理，并以动态策略机制解耦风险感知与策略执行免重训调政策
- 📌 **结论**：在多个公开安全基准上达 SOTA 且效率-效能权衡良好，开源全量与轻量两个版本

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) are increasingly deployed in real-world applications, safety guardrails are required to go beyond coarse-grained filtering and support fine-grained, interpretable, and adaptable risk assessment. However, existing solutions often rely on rapid classification schemes or post-hoc rules, resulting in limited transparency, inflexible policies, or prohibitive inference costs. To this end, we present YuFeng-XGuard, a reasoning-centric guardrail model family designed to perform multi-dimensional risk perception for LLM interactions. Instead of producing opaque binary judgments, YuFeng-XGuard generates structured risk predictions, including explicit risk categories and configurable confidence scores, accompanied by natural language explanations that expose the underlying reasoning process. This formulation enables safety decisions that are both actionable and interpretable. To balance decision latency and explanatory depth, we adopt a tiered inference paradigm that performs an initial risk decision based on the first decoded token, while preserving ondemand explanatory reasoning when required. In addition, we introduce a dynamic policy mechanism that decouples risk perception from policy enforcement, allowing safety policies to be adjusted without model retraining. Extensive experiments on a diverse set of public safety benchmarks demonstrate that YuFeng-XGuard achieves stateof-the-art performance while maintaining strong efficiency-efficacy trade-offs. We release YuFeng-XGuard as an open model family, including both a full-capacity variant and a lightweight version, to support a wide range of deployment scenarios.

</details>

### 28. Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks

📄 [arXiv](https://arxiv.org/abs/2601.04603) · 📝 [OpenReview](https://openreview.net/forum?id=eNvsH5Ye2V) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10008324)　📅 2026-01　🏷 ICLR 2026

**关键词**：`defense`、`constitutional classifiers`、`classifier cascade`、`universal jailbreak`

👤 **作者**：Hoagy Cunningham、…、Mrinank Sharma

- 🎯 **研究动机**：上一代 Constitutional Classifiers 孤立审视输出存在盲区，且误拒率与计算成本高
- 🔬 **研究方法**：增强版引入全对话上下文的 exchange classifiers、轻量分类器先筛全量再升级可疑流的两段级联、高效线性探针与外部分类器集成
- 📌 **结论**：计算成本较基线 exchange classifier 降 40 倍、生产流量拒绝率 0.05%；1700 余小时红队中无攻击能对全部八个目标问题取得与无防御模型相当的回复

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce enhanced Constitutional Classifiers that deliver production-grade jailbreak robustness with dramatically reduced computational costs and refusal rates compared to previous-generation defenses. Our system combines several key insights. First, we develop exchange classifiers that evaluate model responses in their full conversational context, which addresses vulnerabilities in last-generation systems that examine outputs in isolation. Second, we implement a two-stage classifier cascade where lightweight classifiers screen all traffic and escalate only suspicious exchanges to more expensive classifiers. Third, we train efficient linear probe classifiers and ensemble them with external classifiers to simultaneously improve robustness and reduce computational costs. Together, these techniques yield a production-grade system achieving a 40x computational cost reduction compared to our baseline exchange classifier, while maintaining a 0.05% refusal rate on production traffic. Through extensive red-teaming comprising over 1,700 hours, we demonstrate strong protection against universal jailbreaks -- no attack on this system successfully elicited responses to all eight target queries comparable in detail to an undefended model. Our work establishes Constitutional Classifiers as practical and efficient safeguards for large language models.

</details>

### 29. RST-Guarder: Enhancing Long-Context Robustness for Safeguards via RST Parsing and Probabilistic Inference

🎓 [Official](https://aclanthology.org/2026.acl-long.1025/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`adversarial robustness`、`guard model`、`content moderation`、`harmful content`、`safety evaluation`

👤 **作者**：Xu Zhang、Xiaojun Wan

- 🎯 **研究动机**：护栏模型在长文本上检测性能退化，语义理解有限且对上下文噪声鲁棒性弱
- 🔬 **研究方法**：提出推理时方法 RST-Guarder：用 RST 解析器提取长文本片段间语篇级语义关系，再以层级概率推断聚合预训练护栏的片段级安全分数，无需额外数据与训练
- 📌 **结论**：跨多基准与多种护栏模型一致提升长文本有害内容检测，并显著降低把良性内容误判为有害的假阳性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) demonstrate remarkable capabilities across a wide range of tasks, ensuring the safety of their outputs is increasingly critical. To mitigate the risk of policy-violating responses, numerous guardrail models have been developed for harmful-content detection. While effective on short outputs, existing guardrails degrade on long-form responses, reflecting limited semantic understanding and weak robustness to contextual noise. To address these limitations, we propose RST-Guarder, an inference-time method that improves harmful-content detection for long-form inputs without additional data curation or model training. RST-Guarder first applies a RST parser to long-form inputs to get discourse-level semantic relations among segments, and subsequently performs hierarchical probabilistic inference to aggregate segment-level safety scores produced by pre-trained guardrail models. We evaluate RST-Guarder across multiple benchmarks and a diverse set of widely used guardrail models. Experimental results demonstrate that RST-Guarder consistently improves harmful-content detection on long-form inputs, while significantly reducing false positives that incorrectly classify benign content as harmful.

</details>

### 30. HiddenGuard: Fine-Grained Safe Generation with Specialized Representation Router

🎓 [Official](https://aclanthology.org/2026.acl-long.1482/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`guard model`、`content moderation`、`safety-utility trade-off`、`representation intervention`、`harmful content`

👤 **作者**：Lingrui Mei、Shenghua Liu、Yiwei Wang、Baolong Bi、Ruibin Yuan、Xueqi Cheng (程学旗)

- 🎯 **研究动机**：拒绝对齐是二元结果，难以平衡安全与效用，混合内容时连良性信息也被整体拒答
- 🔬 **研究方法**：PRISM 表示路由器旁挂 LLM，利用中间隐藏态做实时 token 级有害检测与编辑替换，并构建 token 级细粒度标注数据集
- 📌 **结论**：有害内容检测与编辑 F1 超 90%，同时保持响应效用与信息量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) grow increasingly powerful, ensuring their safety and alignment with human values remains a critical challenge. Current alignment approaches predominantly rely on refusal alignment, such as training models to refuse harmful prompts or implementing filters at various stages to block certain responses. These methods are designed toward a binary outcome: either denying to answer the question entirely or answering with full access to the model’s parametric knowledge. The binary nature of current alignment approaches presents significant limitations. These methods often fail to balance safety and utility, resulting in either overly cautious responses or overlooking subtle harmful content. They also prevent users from accessing benign information when it’s mixed with harmful content. For instance, a model might refuse to provide basic, public information about a medication’s composition due to misuse concerns. Furthermore, these approaches struggle with context-dependent sensitivity, potentially over-censoring harmless content or missing nuanced harmful outputs. Ideally, LLMs should offer informative responses while avoiding the disclosure of harmful and sensitive information. To address these challenges, we introduce HiddenGuard, a novel framework for fine-grained safe generation in LLMs. Our method incorporates PRISM (rePresentation Router for In-Stream Moderation), a specialized moudule that operates alongside the LLM architecture. By leveraging intermediate hidden states, HiddenGuard enables real-time, token-level harmfulness detection and redaction, without loss in capability. This approach captures deeper semantic information, allowing for more nuanced and context-aware content control compared to traditional filtering techniques. Consequently, the model can generate informative responses while selectively redacting or replacing sensitive information, rather than refusing to answer outright. We also contribute a comprehensive dataset with token-level fine-grained annotations of potentially harmful information across diverse contexts. Our experiments demonstrate that HiddenGuard achieves over 90% in F1 score for detecting and redacting harmful content while preserving the overall utility and informativeness of the model’s responses.

</details>

### 31. Efficient LLM Moderation with Multi-Layer Latent Prototypes

📄 [arXiv](https://arxiv.org/abs/2502.16174) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64923)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`guard model`、`content moderation`、`safety-utility trade-off`、`refusal calibration`、`empirical evaluation`

👤 **作者**：Maciej Chrabąszcz、Filip Szatkowski、Bartosz Wójcik、Jan Dubiński、Tomasz Trzciński、Sebastian Cygert

- 🎯 **研究动机**：现有审核方法存在性能-效率权衡且难按用户需求定制
- 🔬 **研究方法**：MLPM 利用多层中间表征的原型做轻量可定制输入审核，对生成管线几乎零开销且适配任意模型
- 📌 **结论**：多样审核基准达 SOTA，跨模型家族强扩展，与输出审核组合进一步提升响应安全性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Although modern LLMs are aligned with human values during post-training, robust moderation remains essential to prevent harmful outputs at deployment time. Existing approaches suffer from performance-efficiency trade-offs and are difficult to customize to user-specific requirements. Motivated by this gap, we introduce Multi-Layer Prototype Moderator (MLPM), a lightweight and highly customizable input moderation tool. We propose leveraging prototypes of intermediate representations across multiple layers to improve moderation quality while maintaining high efficiency. By design, our method adds negligible overhead to the generation pipeline and can be seamlessly applied to any model. MLPM achieves state-of-the-art performance on diverse moderation benchmarks and demonstrates strong scalability across model families of various sizes. Moreover, we show that it integrates smoothly into end-to-end moderation pipelines and further improves response safety when combined with output moderation techniques. Overall, our work provides a practical and adaptable solution for safe, robust, and efficient LLM deployment.

</details>

### 32. Domain Generalizable AI Guardrails with Augmented Policy Training

🎓 [Official](https://aclanthology.org/2026.acl-long.748/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`guard model`、`content moderation`、`safety-utility trade-off`、`harmful content`、`safety evaluation`

👤 **作者**：Minqian Liu、Ioana Baldini、David Rabinowitz、David S Rosenberg、Sebastian Gehrmann、Mark Dredze

- 🎯 **研究动机**：LlamaGuard、ShieldGemma 等微调护栏仍过拟合训练政策，难以适应新领域
- 🔬 **研究方法**：Augmented Policy Training：训练期用一套政策扰动策略降低过拟合、提升对未见政策的泛化
- 📌 **结论**：1B 小模型经 APT 在未见政策上匹敌甚至超越现有 8B 护栏

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI guardrail systems support usage policies by determining whether a user query or a generated response is allowed or forbidden under the policy. Fine-tuned guardrails – such as LlamaGuard and ShieldGemma – include policy definitions in prompts during training that can be updated during inference to aid generalization. However, our analysis reveals that these models still overfit the training policies, which prevents adaptation to new domains. We propose Augmented Policy Training (APT), a training recipe that enhances guardrail adaptability to unseen policies by using a suite of policy perturbation strategies during training to reduce overfitting and increase generalization. Notably, a small 1B model trained in this manner achieves comparable or better performance than existing 8B guardrails on unseen policies. Our work reveals critical limitations of existing AI guardrails, offers a promising solution, and provides actionable insights for adapting systems to new domains and policies.

</details>

### 33. A Lightweight Explainable Guardrail for Prompt Safety

🎓 [Official](https://aclanthology.org/2026.acl-long.2017/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`guard model`、`content moderation`、`safety-utility trade-off`、`jailbreak defense`、`prompt injection`

👤 **作者**：Md Asiful Islam、Mihai Surdeanu

- 🎯 **研究动机**：现有 prompt 安全护栏模型体积大且不可解释，难以兼顾分类与解释
- 🔬 **研究方法**：提出 LEG：多任务学习同时训练 prompt 分类器与解释分类器（标注支撑安全判定的词），用对抗 LLM 确认偏差的合成策略生成解释数据，损失融合交叉熵、focal 与全局解释弱监督的不确定性加权
- 📌 **结论**：在三个数据集的域内与域外设定下，分类与可解释性均达等同或更优表现，模型体积却远小于现有方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We propose a lightweight explainable guardrail (LEG) method to detect unsafe prompts. LEG uses a multi-task learning architecture to jointly learn a prompt classifier and an explanation classifier, where the latter labels prompt words that explain the safe/unsafe overall decision. LEG is trained on synthetic explanation data, which is generated using a novel strategy that counteracts the confirmation biases of LLMs. Lastly, LEG’s training process uses a novel loss that captures global explanation signals as a weak supervision and combines cross-entropy and focal losses with uncertainty-based weighting. LEG obtains equivalent or better performance than the state-of-the-art for both prompt classification and explainability, both in-domain and out-of-domain on three datasets, despite the fact that its model size is considerably smaller than current approaches.

</details>

### 34. BERM: Low-Overhead Prompt-Injection Detection via In-Situ Benign Representation Modeling

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/8133.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`detection`、`analysis`、`lightweight guard model`、`in-situ representation`、`deployment latency`、`prompt injection`

- 🎯 **研究动机**：现有提示注入防御依赖脆弱启发式或调用昂贵辅助模型，无法兼顾鲁棒与低延迟
- 🔬 **研究方法**：BERM 对 host LLM prefill 阶段提取的内部表征原位建模：联合对比学习良性表征紧致流形以最大化与恶意表征分离，轻量分类器推理时原位检测
- 📌 **结论**：F1 比最佳先前工作高 5.2 个百分点，同时快 12 倍以上，增量推理开销近零

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Real-world deployment of large language models (LLMs) necessitates a robust and low-latency approach to detect prompt injections; existing lowoverhead methods fail to simultaneously boost robustness and reduce latency. Current defenses for prompt injection either rely on brittle heuristics or invoke costly auxiliary models, imposing a significant runtime burden. We introduce BERM, a lightweight framework that performs in-situ detection by modeling a host LLM’s internal representations extracted during prefill, adding negligible overhead. Our approach trains a lightweight classifier atop the LLM by learning a compact manifold of benign representations via joint contrastive learning to maximize the separation from malicious representations. At inference, this pre-trained classifier enables in-situ detection without invoking auxiliary guard models. On a diverse landscape of prompt injection attacks, our framework establishes a new state-of-the-art, achieving an F1-score 5.2 percentage points (pp) higher than the best prior work. Critically, BERM achieves this while being over 12x faster, reducing incremental inference overhead to near-zero.

</details>

### 35. Explaining Jailbreaks: Structured and Interpretable Safety Assessment for Large Language Models

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/4430.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`detection`、`benchmark`、`analysis`、`explanation-aware guard`、`structured output`、`cross-benchmark transfer`

- 🎯 **研究动机**：越狱评估依赖 ASR 等结果级指标，无法说明安全失败如何与为何发生
- 🔬 **研究方法**：解释感知安全框架：在二元有害检测上增加严重度、策略、触发 span、理由与安全因子的结构化解释，人机混合标注管线加微调紧凑模型生成规范解释
- 📌 **结论**：防御评估中把 ASR 降至 Vicuna-7B 的 0.44% 与 GPT-3.5 的 1.30% 并达最低 StrongREJECT 分，诊断属性恢复优于通用 LLM 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) remain highly vulnerable to jailbreak attacks, yet existing evaluations rely primarily on outcome-level metrics such as Attack Success Rate (ASR), providing limited insight into how and why safety failures occur. We propose an explanation-aware safety framework that augments binary harmfulness detection with structured, human-interpretable explanations capturing severity, strategies, trigger spans, rationales, and derived safety factors. To enable scalable and consistent supervision, we introduce a human–LLM hybrid annotation and canonicalization pipeline. We then fine-tune a compact model to generate canonical explanations alongside harmfulness decisions. Across both seen and unseen benchmark settings, our method improves robustness and explanation fidelity. In jailbreak defense evaluation, our approach reduces ASR to 0.44% on Vicuna-7B and 1.30% on GPT-3.5, outperforming existing defense baselines while also achieving the lowest StrongREJECT scores. Beyond outcome-level gains, the model more accurately recovers diagnostic attributes (e.g., attack strategy, trigger spans, and safety factors) than strong general-purpose LLM baselines. Overall, explanation-aware learning exposes diagnostic dimensions that ASR alone cannot capture and provides a more faithful and actionable foundation for robust LLM safety assessment.

</details>

### 36. Auto-Tuning Safety Guardrails for Black-Box Large Language Models

📄 [arXiv](https://arxiv.org/abs/2512.15782)　📅 2025-12

**关键词**：`defense`、`black-box tuning`、`configuration search`、`safety-latency trade-off`

👤 **作者**：Perry Abdulkadir

- 🎯 **研究动机**：黑盒 LLM 的安全护栏（系统提示加内容过滤器）通常靠手工调参，脆弱且难复现
- 🔬 **研究方法**：把护栏设计当作冻结模型上的超参优化：以模块化 jailbreak/malware 系统提示加 ModernBERT 有害分类器包装 Mistral-7B，在 48 点网格空间上运行 Optuna 黑盒搜索
- 📌 **结论**：黑盒搜索以少一个数量级的评估次数与约 8 倍更短的墙钟时间稳定复现网格最优配置

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed behind safety guardrails such as system prompts and content filters, especially in settings where product teams cannot modify model weights. In practice these guardrails are typically hand-tuned, brittle, and difficult to reproduce. This paper studies a simple but practical alternative: treat safety guardrail design itself as a hyperparameter optimization problem over a frozen base model. Concretely, I wrap Mistral-7B-Instruct with modular jailbreak and malware system prompts plus a ModernBERT-based harmfulness classifier, then evaluate candidate configurations on three public benchmarks covering malware generation, classic jailbreak prompts, and benign user queries. Each configuration is scored using malware and jailbreak attack success rate, benign harmful-response rate, and end-to-end latency. A 48-point grid search over prompt combinations and filter modes establishes a baseline. I then run a black-box Optuna study over the same space and show that it reliably rediscovers the best grid configurations while requiring an order of magnitude fewer evaluations and roughly 8x less wall-clock time. The results suggest that viewing safety guardrails as tunable hyperparameters is a feasible way to harden black-box LLM deployments under compute and time constraints.

</details>

### 37. SGuard-v1: Safety Guardrail for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2511.12497)　📅 2025-11

**关键词**：`tool`、`dual-filter guard`、`content moderation`、`jailbreak detection`

👤 **作者**：JoonHo Lee、HyeonMin Cho、Jaewoong Yun、Hyunjae Lee、JunKyu Lee、Juree Seok

- 🎯 **研究动机**：轻量 guardrail 需同时处理普通有害内容与越狱对抗 prompt，现有方案难以兼顾
- 🔬 **研究方法**：基于 Granite-3.3-2B 训练 ContentFilter（MLCommons 危害分类）与 JailbreakFilter（覆盖 60 种攻击类型的课程学习），以约 140 万样本做指令微调，支持 12 语言
- 📌 **结论**：公开与专有安全基准上取得 SOTA，轻量且输出多类预测与置信度，Apache-2.0 开源

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present SGuard-v1, a lightweight safety guardrail for Large Language Models (LLMs), which comprises two specialized models to detect harmful content and screen adversarial prompts in human-AI conversational settings. The first component, ContentFilter, is trained to identify safety risks in LLM prompts and responses in accordance with the MLCommons hazard taxonomy, a comprehensive framework for trust and safety assessment of AI. The second component, JailbreakFilter, is trained with a carefully designed curriculum over integrated datasets and findings from prior work on adversarial prompting, covering 60 major attack types while mitigating false-unsafe classification. SGuard-v1 is built on the 2B-parameter Granite-3.3-2B-Instruct model that supports 12 languages. We curate approximately 1.4 million training instances from both collected and synthesized data and perform instruction tuning on the base model, distributing the curated data across the two component according to their designated functions. Through extensive evaluation on public and proprietary safety benchmarks, SGuard-v1 achieves state-of-the-art safety performance while remaining lightweight, thereby reducing deployment overhead. SGuard-v1 also improves interpretability for downstream use by providing multi-class safety predictions and their binary confidence scores. We release the SGuard-v1 under the Apache-2.0 License to enable further research and practical deployment in AI safety.

</details>

### 38. Qwen3Guard Technical Report

📄 [arXiv](https://arxiv.org/abs/2510.14276)　📅 2025-10

**关键词**：`tool`、`multilingual guard`、`generative moderation`、`streaming moderation`

👤 **作者**：Haiquan Zhao、…、Yuxin Zhou

- 🎯 **研究动机**：现有 guardrail 只输出安全/不安全二值标签难以适配不同安全容忍度，且需完整输出才能检测，与流式推理不兼容
- 🔬 **研究方法**：发布 Generative Qwen3Guard（指令跟随式安全/争议/不安全三分类）与 Stream Qwen3Guard（token 级分类头实时监测），各含 0.6B/4B/8B 三种规模，支持 119 种语言
- 📌 **结论**：在中英及多语言基准上取得 SOTA 的 prompt 与 response 安全分类性能，Apache 2.0 开源

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) become more capable and widely used, ensuring the safety of their outputs is increasingly critical. Existing guardrail models, though useful in static evaluation settings, face two major limitations in real-world applications: (1) they typically output only binary "safe/unsafe" labels, which can be interpreted inconsistently across diverse safety policies, rendering them incapable of accommodating varying safety tolerances across domains; and (2) they require complete model outputs before performing safety checks, making them fundamentally incompatible with streaming LLM inference, thereby preventing timely intervention during generation and increasing exposure to harmful partial outputs. To address these challenges, we present Qwen3Guard, a series of multilingual safety guardrail models with two specialized variants: Generative Qwen3Guard, which casts safety classification as an instruction-following task to enable fine-grained tri-class judgments (safe, controversial, unsafe); and Stream Qwen3Guard, which introduces a token-level classification head for real-time safety monitoring during incremental text generation. Both variants are available in three sizes (0.6B, 4B, and 8B parameters) and support up to 119 languages and dialects, providing comprehensive, scalable, and low-latency safety moderation for global LLM deployments. Evaluated across English, Chinese, and multilingual benchmarks, Qwen3Guard achieves state-of-the-art performance in both prompt and response safety classification. All models are released under the Apache 2.0 license for public use.

</details>

### 39. Lightweight Safety Guardrails via Synthetic Data and RL-guided Adversarial Training

📄 [arXiv](https://arxiv.org/abs/2507.08284)　📅 2025-07

**关键词**：`defense`、`lightweight guard`、`synthetic data`、`adversarial training`

👤 **作者**：Aleksei Ilin、…、Haluk Noyan Tokgozoglu

- 🎯 **研究动机**：大模型做内容审核算力开销大，小模型能否胜任有待验证
- 🔬 **研究方法**：以种子数据增广与多轮策展产高保真合成数据，用 RL 引导 GAN 式对抗训练生成难例微调安全分类器
- 📌 **结论**：小语言模型达到甚至超过大模型的审核性能，同时降低计算开销并增强对抗鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce a lightweight yet highly effective safety guardrail framework for language models, demonstrating that small-scale language models can achieve, and even surpass, the performance of larger counterparts in content moderation tasks. This is accomplished through high-fidelity synthetic data generation and adversarial training. The synthetic data generation process begins with human-curated seed data, which undergoes query augmentation and paraphrasing to create diverse and contextually rich examples. This augmented data is then subjected to multiple rounds of curation, ensuring high fidelity and relevance. Inspired by recent advances in the Generative Adversarial Network (GAN) architecture, our adversarial training employs reinforcement learning to guide a generator that produces challenging synthetic examples. These examples are used to fine-tune the safety classifier, enhancing its ability to detect and mitigate harmful content. Additionally, we incorporate strategies from recent research on efficient LLM training, leveraging the capabilities of smaller models to improve the performance of larger generative models. With iterative adversarial training and the generation of diverse, high-quality synthetic data, our framework enables small language models (SLMs) to serve as robust safety guardrails. This approach not only reduces computational overhead but also enhances resilience against adversarial attacks, offering a scalable and efficient solution for content moderation in AI systems.

</details>

### 40. OneShield -- the Next Generation of LLM Guardrails

📄 [arXiv](https://arxiv.org/abs/2507.21170)　📅 2025-07

**关键词**：`tool`、`model-agnostic guard`、`contextual policy`、`production deployment`

👤 **作者**：Chad DeLuca、…、Sandeep Gopisetty

- 🎯 **研究动机**：LLM 风险不断演化，一刀切的通用防护方案不可行
- 🔬 **研究方法**：提出独立、模型无关、可定制的 OneShield 护栏，支持风险因素定义、上下文安全合规策略表达与风险缓解
- 📌 **结论**：给出框架实现、可扩展性考量与部署以来的使用统计

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rise of Large Language Models has created a general excitement about the great potential for a myriad of applications. While LLMs offer many possibilities, questions about safety, privacy, and ethics have emerged, and all the key actors are working to address these issues with protective measures for their own models and standalone solutions. The constantly evolving nature of LLMs makes it extremely challenging to universally shield users against their potential risks, and one-size-fits-all solutions are unfeasible. In this work, we propose OneShield, our stand-alone, model-agnostic and customizable solution to safeguard LLMs. OneShield aims to provide facilities for defining risk factors, expressing and declaring contextual safety and compliance policies, and mitigating LLM risks, with a focus on each specific customer. We describe the implementation of the framework, discuss scalability considerations, and provide usage statistics of OneShield since its initial deployment.

</details>

### 41. FLAME: Flexible LLM-Assisted Moderation Engine

📄 [arXiv](https://arxiv.org/abs/2502.09175)　📅 2025-02

**关键词**：`defense`、`output moderation`、`custom topic filter`、`jailbreak resistance`

👤 **作者**：Ivan Bakulin、…、Ivan Oseledets

- 🎯 **研究动机**：输入过滤式审核不足，BoN 越狱对流行 LLM 成功率达 80% 以上
- 🔬 **研究方法**：FLAME 将审核重心从输入转向模型输出，评估回复本身并支持自定义主题过滤，训练与推理开销低
- 📌 **结论**：GPT-4o-mini 与 DeepSeek-v3 上攻击成功率降低约 9 倍且计算开销低

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of Large Language Models (LLMs) has introduced significant challenges in moderating user-model interactions. While LLMs demonstrate remarkable capabilities, they remain vulnerable to adversarial attacks, particularly ``jailbreaking'' techniques that bypass content safety measures. Current content moderation systems, which primarily rely on input prompt filtering, have proven insufficient, with techniques like Best-of-N (BoN) jailbreaking achieving success rates of 80% or more against popular LLMs. In this paper, we introduce Flexible LLM-Assisted Moderation Engine (FLAME): a new approach that shifts the focus from input filtering to output moderation. Unlike traditional circuit-breaking methods that analyze user queries, FLAME evaluates model responses, offering several key advantages: (1) computational efficiency in both training and inference, (2) enhanced resistance to BoN jailbreaking attacks, and (3) flexibility in defining and updating safety criteria through customizable topic filtering. Our experiments demonstrate that FLAME significantly outperforms current moderation systems. For example, FLAME reduces attack success rate in GPT-4o-mini and DeepSeek-v3 by a factor of ~9, while maintaining low computational overhead. We provide comprehensive evaluation on various LLMs and analyze the engine's efficiency against the state-of-the-art jailbreaking. This work contributes to the development of more robust and adaptable content moderation systems for LLMs.

</details>

### 42. Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming

📄 [arXiv](https://arxiv.org/abs/2501.18837)　📅 2025-01

**关键词**：`defense`、`constitutional classifiers`、`synthetic policy data`、`red teaming`

👤 **作者**：Mrinank Sharma、…、Ethan Perez

- 🎯 **研究动机**：通用越狱可系统性绕过防护，需要可扩展的防御
- 🔬 **研究方法**：Constitutional Classifiers 用自然语言 constitution 生成合成数据训练输入输出分类器
- 📌 **结论**：超 3000 小时 red teaming 未找到通用越狱；生产拒答仅增 0.38%、推理开销 23.7%，证明防御可行

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are vulnerable to universal jailbreaks-prompting strategies that systematically bypass model safeguards and enable users to carry out harmful processes that require many model interactions, like manufacturing illegal substances at scale. To defend against these attacks, we introduce Constitutional Classifiers: safeguards trained on synthetic data, generated by prompting LLMs with natural language rules (i.e., a constitution) specifying permitted and restricted content. In over 3,000 estimated hours of red teaming, no red teamer found a universal jailbreak that could extract information from an early classifier-guarded LLM at a similar level of detail to an unguarded model across most target queries. On automated evaluations, enhanced classifiers demonstrated robust defense against held-out domain-specific jailbreaks. These classifiers also maintain deployment viability, with an absolute 0.38% increase in production-traffic refusals and a 23.7% inference overhead. Our work demonstrates that defending against universal jailbreaks while maintaining practical deployment viability is tractable.

</details>

### 43. Aegis2.0: A Diverse AI Safety Dataset and Risks Taxonomy for Alignment of LLM Guardrails

📄 [arXiv](https://arxiv.org/abs/2501.09004) · 🎓 [Official](https://aclanthology.org/2025.naacl-long.306/)　📅 2025-01　🏷 ACL 2025

**关键词**：`benchmark`、`risk taxonomy`、`human-LLM interaction`、`category adaptation`

👤 **作者**：Shaona Ghosh、…、Christopher Parisien

- 🎯 **研究动机**：缺少可商用、人工标注且覆盖全谱风险的 guard 训练数据
- 🔬 **研究方法**：建立 12 个顶层危害类加 9 个细分子类的 taxonomy，以人工加多 LLM 评审团管线产出 34248 条样本，训练混合安全与 topic-following 数据
- 📌 **结论**：轻量 PEFT 模型匹敌全参大模型，且能泛化到推理时新定义的风险类别

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) and generative AI become increasingly widespread, concerns about content safety have grown in parallel. Currently, there is a clear lack of high-quality, human-annotated datasets that address the full spectrum of LLM-related safety risks and are usable for commercial applications. To bridge this gap, we propose a comprehensive and adaptable taxonomy for categorizing safety risks, structured into 12 top-level hazard categories with an extension to 9 fine-grained subcategories. This taxonomy is designed to meet the diverse requirements of downstream users, offering more granular and flexible tools for managing various risk types. Using a hybrid data generation pipeline that combines human annotations with a multi-LLM "jury" system to assess the safety of responses, we obtain Aegis 2.0, a carefully curated collection of 34,248 samples of human-LLM interactions, annotated according to our proposed taxonomy. To validate its effectiveness, we demonstrate that several lightweight models, trained using parameter-efficient techniques on Aegis 2.0, achieve performance competitive with leading safety models fully fine-tuned on much larger, non-commercial datasets. In addition, we introduce a novel training blend that combines safety with topic following data.This approach enhances the adaptability of guard models, enabling them to generalize to new risk categories defined during inference. We plan to open-source Aegis 2.0 data and models to the research community to aid in the safety guardrailing of LLMs.

</details>

### 44. Granite Guardian

📄 [arXiv](https://arxiv.org/abs/2412.07724)　📅 2024-12

**关键词**：`tool`、`risk detection`、`RAG safety`、`open guard model`

👤 **作者**：Inkit Padhi、…、Prasanna Sattigeri

- 🎯 **研究动机**：传统风险检测模型忽略越狱与 RAG 特有风险
- 🔬 **研究方法**：Granite Guardian 以人工加合成数据训练，覆盖偏见、暴力、越狱及 RAG 的上下文相关性、接地性等维度
- 📌 **结论**：有害内容与 RAG 幻觉基准 AUC 分别达 0.871 与 0.854，开源且可组合到任意 LLM

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce the Granite Guardian models, a suite of safeguards designed to provide risk detection for prompts and responses, enabling safe and responsible use in combination with any large language model (LLM). These models offer comprehensive coverage across multiple risk dimensions, including social bias, profanity, violence, sexual content, unethical behavior, jailbreaking, and hallucination-related risks such as context relevance, groundedness, and answer relevance for retrieval-augmented generation (RAG). Trained on a unique dataset combining human annotations from diverse sources and synthetic data, Granite Guardian models address risks typically overlooked by traditional risk detection models, such as jailbreaks and RAG-specific issues. With AUC scores of 0.871 and 0.854 on harmful content and RAG-hallucination-related benchmarks respectively, Granite Guardian is the most generalizable and competitive model available in the space. Released as open-source, Granite Guardian aims to promote responsible AI development across the community. https://github.com/ibm-granite/granite-guardian

</details>

### 45. ShieldGemma: Generative AI Content Moderation Based on Gemma

📄 [arXiv](https://arxiv.org/abs/2407.21772)　📅 2024-07

**关键词**：`tool`、`Gemma guard`、`synthetic data`、`four-harm taxonomy`

👤 **作者**：Wenjun Zeng、…、Oscar Wahltinez

- 🎯 **研究动机**：开发者需要同时审核用户输入与模型输出的开放 moderation 模型
- 🔬 **研究方法**：ShieldGemma 基于 Gemma2，覆盖色情、危险、骚扰、仇恨四类伤害，配套 LLM 合成数据管线
- 📌 **结论**：超 Llama Guard 10.8% AU-PRC、超 WildCard 4.3%，仅用合成数据训练即有强泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present ShieldGemma, a comprehensive suite of LLM-based safety content moderation models built upon Gemma2. These models provide robust, state-of-the-art predictions of safety risks across key harm types (sexually explicit, dangerous content, harassment, hate speech) in both user input and LLM-generated output. By evaluating on both public and internal benchmarks, we demonstrate superior performance compared to existing models, such as Llama Guard (+10.8\% AU-PRC on public benchmarks) and WildCard (+4.3\%). Additionally, we present a novel LLM-based data curation pipeline, adaptable to a variety of safety-related tasks and beyond. We have shown strong generalization performance for model trained mainly on synthetic data. By releasing ShieldGemma, we provide a valuable resource to the research community, advancing LLM safety and enabling the creation of more effective content moderation solutions for developers.

</details>

### 46. WildGuard: Open One-stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs

📄 [arXiv](https://arxiv.org/abs/2406.18495) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0f69b4b96a46f284b726fbd70f74fb3b-Abstract-Datasets_and_Benchmarks_Track.html)　📅 2024-06　🏷 NeurIPS 2024

**关键词**：`tool`、`multi-task moderation`、`jailbreak detection`、`refusal classification`

👤 **作者**：Seungju Han、…、Nouha Dziri

- 🎯 **研究动机**：开源审核工具在越狱识别与拒答评估上远落后于 GPT-4
- 🔬 **研究方法**：构建 92K 标注的 WildGuardMix 多任务数据集，训练覆盖 prompt 危险识别、response 风险检测与拒答判定的一体化模型 WildGuard
- 📌 **结论**：三任务开源 SOTA（拒答检测提升至多 26.4%），部分超 GPT-4；部署后越狱 ASR 从 79.8% 降至 2.4%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce WildGuard -- an open, light-weight moderation tool for LLM safety that achieves three goals: (1) identifying malicious intent in user prompts, (2) detecting safety risks of model responses, and (3) determining model refusal rate. Together, WildGuard serves the increasing needs for automatic safety moderation and evaluation of LLM interactions, providing a one-stop tool with enhanced accuracy and broad coverage across 13 risk categories. While existing open moderation tools such as Llama-Guard2 score reasonably well in classifying straightforward model interactions, they lag far behind a prompted GPT-4, especially in identifying adversarial jailbreaks and in evaluating models' refusals, a key measure for evaluating safety behaviors in model responses. To address these challenges, we construct WildGuardMix, a large-scale and carefully balanced multi-task safety moderation dataset with 92K labeled examples that cover vanilla (direct) prompts and adversarial jailbreaks, paired with various refusal and compliance responses. WildGuardMix is a combination of WildGuardTrain, the training data of WildGuard, and WildGuardTest, a high-quality human-annotated moderation test set with 5K labeled items covering broad risk scenarios. Through extensive evaluations on WildGuardTest and ten existing public benchmarks, we show that WildGuard establishes state-of-the-art performance in open-source safety moderation across all the three tasks compared to ten strong existing open-source moderation models (e.g., up to 26.4% improvement on refusal detection). Importantly, WildGuard matches and sometimes exceeds GPT-4 performance (e.g., up to 3.9% improvement on prompt harmfulness identification). WildGuard serves as a highly effective safety moderator in an LLM interface, reducing the success rate of jailbreak attacks from 79.8% to 2.4%.

</details>

### 47. AEGIS: Online Adaptive AI Content Safety Moderation with Ensemble of LLM Experts

📄 [arXiv](https://arxiv.org/abs/2404.05993)　📅 2024-04

**关键词**：`defense`、`online adaptation`、`expert ensemble`、`content taxonomy`

👤 **作者**：Shaona Ghosh、Prasoon Varshney、Erick Galinkin、Christopher Parisien

- 🎯 **研究动机**：高质量内容安全数据集与基准匮乏，单一安全专家难以覆盖全部风险类别
- 🔬 **研究方法**：定义 13 类关键与 9 类稀疏风险 taxonomy，构建约 26000 条人工标注的 AegisSafetyDataset 训练专家集，部署时用 no-regret 在线适配做集成
- 📌 **结论**：AegisSafetyExperts 超越或匹敌 SOTA 安全模型并抗多类越狱，数据用于对齐不损 MT Bench 表现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) and generative AI become more widespread, the content safety risks associated with their use also increase. We find a notable deficiency in high-quality content safety datasets and benchmarks that comprehensively cover a wide range of critical safety areas. To address this, we define a broad content safety risk taxonomy, comprising 13 critical risk and 9 sparse risk categories. Additionally, we curate AEGISSAFETYDATASET, a new dataset of approximately 26, 000 human-LLM interaction instances, complete with human annotations adhering to the taxonomy. We plan to release this dataset to the community to further research and to help benchmark LLM models for safety. To demonstrate the effectiveness of the dataset, we instruction-tune multiple LLM-based safety models. We show that our models (named AEGISSAFETYEXPERTS), not only surpass or perform competitively with the state-of-the-art LLM-based safety models and general purpose LLMs, but also exhibit robustness across multiple jail-break attack categories. We also show how using AEGISSAFETYDATASET during the LLM alignment phase does not negatively impact the performance of the aligned models on MT Bench scores. Furthermore, we propose AEGIS, a novel application of a no-regret online adaptation framework with strong theoretical guarantees, to perform content moderation with an ensemble of LLM content safety experts in deployment

</details>

### 48. RigorLLM: Resilient Guardrails for Large Language Models against Undesired Content

📄 [arXiv](https://arxiv.org/abs/2403.13031)　📅 2024-03

**关键词**：`defense`、`robust moderation`、`energy-based augmentation`、`fusion guard`

👤 **作者**：Zhuowen Yuan、…、Bo Li

- 🎯 **研究动机**：现有内容缓解策略在对抗攻击下缺乏韧性
- 🔬 **研究方法**：RigorLLM 组合 Langevin dynamics 能量式数据增强、minimax 优化的输入安全后缀与 robust KNN+LLM 融合审核模型
- 📌 **结论**：有害内容检测优于 OpenAI API 与 Perspective API，且对越狱攻击表现出强韧性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advancements in Large Language Models (LLMs) have showcased remarkable capabilities across various tasks in different domains. However, the emergence of biases and the potential for generating harmful content in LLMs, particularly under malicious inputs, pose significant challenges. Current mitigation strategies, while effective, are not resilient under adversarial attacks. This paper introduces Resilient Guardrails for Large Language Models (RigorLLM), a novel framework designed to efficiently and effectively moderate harmful and unsafe inputs and outputs for LLMs. By employing a multi-faceted approach that includes energy-based training data augmentation through Langevin dynamics, optimizing a safe suffix for inputs via minimax optimization, and integrating a fusion-based model combining robust KNN with LLMs based on our data augmentation, RigorLLM offers a robust solution to harmful content moderation. Our experimental evaluations demonstrate that RigorLLM not only outperforms existing baselines like OpenAI API and Perspective API in detecting harmful content but also exhibits unparalleled resilience to jailbreaking attacks. The innovative use of constrained optimization and a fusion-based guardrail approach represents a significant step forward in developing more secure and reliable LLMs, setting a new standard for content moderation frameworks in the face of evolving digital threats.

</details>

### 49. Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations

📄 [arXiv](https://arxiv.org/abs/2312.06674)　📅 2023-12

**关键词**：`tool`、`input-output guard`、`risk taxonomy`、`instruction tuning`

👤 **作者**：Hakan Inan、…、Madian Khabsa

- 🎯 **研究动机**：人机对话需要同一组件同时审核用户 prompt 与模型 response，现成方案缺位
- 🔬 **研究方法**：Llama Guard 基于 Llama2-7B 指令微调，配套安全风险 taxonomy 与高质量数据集，输出二值决策且可经指令定制分类与格式
- 📌 **结论**：在 OpenAI Moderation Evaluation 与 ToxicChat 上匹敌或超越现有内容审核工具

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce Llama Guard, an LLM-based input-output safeguard model geared towards Human-AI conversation use cases. Our model incorporates a safety risk taxonomy, a valuable tool for categorizing a specific set of safety risks found in LLM prompts (i.e., prompt classification). This taxonomy is also instrumental in classifying the responses generated by LLMs to these prompts, a process we refer to as response classification. For the purpose of both prompt and response classification, we have meticulously gathered a dataset of high quality. Llama Guard, a Llama2-7b model that is instruction-tuned on our collected dataset, albeit low in volume, demonstrates strong performance on existing benchmarks such as the OpenAI Moderation Evaluation dataset and ToxicChat, where its performance matches or exceeds that of currently available content moderation tools. Llama Guard functions as a language model, carrying out multi-class classification and generating binary decision scores. Furthermore, the instruction fine-tuning of Llama Guard allows for the customization of tasks and the adaptation of output formats. This feature enhances the model's capabilities, such as enabling the adjustment of taxonomy categories to align with specific use cases, and facilitating zero-shot or few-shot prompting with diverse taxonomies at the input. We are making Llama Guard model weights available and we encourage researchers to further develop and adapt them to meet the evolving needs of the community for AI safety.

</details>

### 50. Self-Guard: Empower the LLM to Safeguard Itself

📄 [arXiv](https://arxiv.org/abs/2310.15851)　📅 2023-10

**关键词**：`defense`、`self-moderation`、`response tagging`、`jailbreak defense`

👤 **作者**：Zezhong Wang、…、Kam-Fai Wong

- 🎯 **研究动机**：safety training 难适应新攻击且伤性能，外部 safeguards 帮助有限
- 🔬 **研究方法**：Self-Guard 两阶段：先增强模型有害内容判别力，再让模型对自身输出持续做有害检测
- 📌 **结论**：对越狱攻击鲁棒，通用能力不降，还能缓解过度敏感

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The jailbreak attack can bypass the safety measures of a Large Language Model (LLM), generating harmful content. This misuse of LLM has led to negative societal consequences. Currently, there are two main approaches to address jailbreak attacks: safety training and safeguards. Safety training focuses on further training LLM to enhance its safety. On the other hand, safeguards involve implementing external models or filters to prevent harmful outputs. However, safety training has constraints in its ability to adapt to new attack types and often leads to a drop in model performance. Safeguards have proven to be of limited help. To tackle these issues, we propose a novel approach called Self-Guard, which combines the strengths of both safety methods. Self-Guard includes two stages. In the first stage, we enhance the model's ability to assess harmful content, and in the second stage, we instruct the model to consistently perform harmful content detection on its own responses. The experiment has demonstrated that Self-Guard is robust against jailbreak attacks. In the bad case analysis, we find that LLM occasionally provides harmless responses to harmful queries. Additionally, we evaluated the general capabilities of the LLM before and after safety training, providing evidence that Self-Guard does not result in the LLM's performance degradation. In sensitivity tests, Self-Guard not only avoids inducing over-sensitivity in LLM but also can even mitigate this issue.

</details>

### 51. NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails

📄 [arXiv](https://arxiv.org/abs/2310.10501)　📅 2023-10　🏷 EMNLP 2023

**关键词**：`tool`、`programmable rail`、`dialogue control`、`model-agnostic runtime`

👤 **作者**：Traian Rebedea、Razvan Dinu、Makesh Sreedhar、Christopher Parisien、Jonathan Cohen

- 🎯 **研究动机**：训练期对齐把 guardrail 绑死在特定模型内，应用层缺乏可编程、可解释的运行时控制
- 🔬 **研究方法**：NeMo Guardrails 以对话管理式运行时加载用户定义、独立于底层 LLM 的 programmable rails，控制话题、对话路径与风格
- 📌 **结论**：可搭配多家 LLM provider 构建可控且安全的对话应用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

NeMo Guardrails is an open-source toolkit for easily adding programmable guardrails to LLM-based conversational systems. Guardrails (or rails for short) are a specific way of controlling the output of an LLM, such as not talking about topics considered harmful, following a predefined dialogue path, using a particular language style, and more. There are several mechanisms that allow LLM providers and developers to add guardrails that are embedded into a specific model at training, e.g. using model alignment. Differently, using a runtime inspired from dialogue management, NeMo Guardrails allows developers to add programmable rails to LLM applications - these are user-defined, independent of the underlying LLM, and interpretable. Our initial results show that the proposed approach can be used with several LLM providers to develop controllable and safe LLM applications using programmable rails.

</details>

### 52. LongGuard: Mechanistic Analysis and Training-Free Mitigation of Long-Context Failure in Safety Guardrails

📄 [arXiv](https://arxiv.org/abs/2608.27580)　📅 2026-08

**关键词**：`analysis`、`defense`、`long-context guardrail`、`attention dilution`、`training-free mitigation`、`chunked detection`

👤 **作者**：Ziyang Chen、Xing Wu、Songlin Hu

- 🎯 **研究动机**：安全 guardrail 几乎只在短文本上训练与评估，长上下文中对不安全内容的召回大幅下降，机制与缓解均缺失
- 🔬 **研究方法**：提出 SafetyNIAH（0.25k–32k 长度网格）与 LongGuard：用 Benign-Fill vs Needle-Repeat 对照与三层 attention–logit–behavior 分析把失效归因于 unsafe needle 注意力稀释，并给出无需训练的 Chunked Detection、Attention-Head Sharpening 与长度感知路由
- 📌 **结论**：15 个主流 guardrail 的不安全召回随长度平均单调下降逾 50%；Chunked Detection 与 Attention-Head Sharpening 在六个 guardrail 上平均改善 22% 与 13%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety guardrails serve as the last line of defense against harmful inputs and outputs of large language models (LLMs), yet they are trained and evaluated almost exclusively on short text. We present LongGuard, a framework that evaluates, mechanistically analyzes, and mitigates long-context guardrail failure. We formulate the task as Safety Needle-in-a-Haystack (SafetyNIAH) over a 0.25k-32k length grid; across 15 mainstream guardrails, unsafe recall drops monotonically by more than 50% on average, and a paired Benign-Fill vs. Needle-Repeat design attributes the failure to proportional dilution of the unsafe needle rather than to absolute length. A three-layer attention-logit-behavior analysis on six guardrails locates the mechanism: attention mass on the unsafe needle is diluted, the unsafe-over-safe logit margin is compressed in lockstep, and the detection decision collapses accordingly, with this attention->logit->behavior chain remaining consistent after partialling out length. We further isolate a sparse set of guard-specialized retrieval heads that exhibit partial specificity relative to their base models. Building on the analysis, we propose two training-free mitigations - Chunked Detection (CD) and Attention-Head Sharpening (AHS) - and a deployment protocol, Context-Aware Hyperparameter Routing (CAHR), that selects configurations by context length and audit side. Across five benchmarks spanning synthetic data, long-context attacks, and reasoning-model outputs, CAHR-CD and CAHR-AHS improve the six-guardrail average by 22% and 13%, respectively. Code and data are available online.

</details>

### 53. Layered LLM Defenses as an Ensemble: Access Tiers, Inference Cost, and the Measured Failure Correlation Between Defense Layers

📄 [arXiv](https://arxiv.org/abs/2608.28327)　📅 2026-08

**关键词**：`analysis`、`defense composition`、`failure correlation`、`over-refusal`

👤 **作者**：Abrar Alotaibi、Muhammad Shahid Jabbar、Sadam Al-Azani、Moataz Ahmed

- 🎯 **研究动机**：实践者堆叠多层 LLM 防御并默认效果复合，但 ensemble 只有在各层在不同输入上失败时才复合，该独立性从未被实测
- 🔬 **研究方法**：提出 Adversary Access-Tier Model（A0–A4 分级攻击者访问）与五类推理成本分类推导堆栈行为，再用单个自适应攻击者实测七层防御栈的层间失效相关性
- 📌 **结论**：15 个可测层对全部正相关（φ=0.30–0.75），联合残余攻击成功率最多比独立性乘积预测高 0.172；堆栈拒绝 80% 良性 prompt 却不显著优于最强单层，相关性主要是共同因

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Practitioners defend large language models (LLMs) by stacking defenses, assuming the layers compound. A stack is an ensemble, and ensembles compound only under a condition the LLM security literature recommends but never measures: the members must fail on different inputs. Two instruments make that measurable. The Adversary Access-Tier Model (AATM) grades an adversary by the access it holds, from system-only (A0) to influence over training data (A4). A cost model sorts defenses into five classes of inference-time overhead; because two classes require training weights or reading activations, they tier the defender as AATM tiers the adversary. From these we derive how a stack behaves, and the quantities a defender cares about diverge: coverage saturates within a tier, cost rises by class, false refusals accumulate as a union, and residual attack success falls multiplicatively only under independence. We measure that independence. Running one adaptive adversary against a seven-layer stack, failure correlation is positive in all fifteen measurable pairs ($φ$ from $0.30$ to $0.75$), and the joint residual exceeds the multiplicative prediction by up to $0.172$. Stratifying on behavior difficulty dissolves most of the association, so the dependence is predominantly common-cause, but it survives permutation inference, majority-vote grader labels, and externally calibrated thresholds. The same stack refuses four in five benign prompts while remaining statistically indistinguishable from its strongest single layer. The dependence is architectural rather than sampling-based: members correlate through the model they all wrap, so no wider member pool weakens it. Diversity therefore selects stack members but does not predict what an assembled stack delivers, which has to be measured end to end.

</details>

### 54. Benchmarking the Benchmarks: Evaluating Automated Safety Benchmarks for Small Language Models

📄 [arXiv](https://arxiv.org/abs/2608.17183) · 🎓 [Official](https://sites.google.com/di.uniroma1.it/esorics2026/program/accepted-papers)　📅 2026-08

**关键词**：`analysis`、`benchmark validity`、`small language model`、`capability-safety confound`、`small language models`

👤 **作者**：Nyamtulla Shaik、Fengjun Li、Bo Luo

- 🎯 **研究动机**：现有安全/合规基准为大模型设计，能否有效可靠评测 SLM 未知
- 🔬 **研究方法**：统一评分 rubric（有害 0、安全 1、模糊 0.5）下对 26 个开源 SLM 评五套广泛使用的基准管线
- 📌 **结论**：模糊判断占主导且与 prompt 复杂度、输出长度相关，揭示能力-安全混淆；均值排行榜在合理模糊处理下排名显著变化，LLM 中心基准不足以独立证明 SLM 安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Small Language Models (SLMs) are increasingly deployed in resource-constrained, privacy-sensitive settings, where safety and bias failures can cause security and societal risks. However, existing AI safety\slash security\slash compliance benchmarks are designed for large language models that may not transfer reliably to SLMs. We therefore ask: Can these benchmarks effectively and reliably evaluate SLMs? To answer this question, we conduct a large-scale assessment of the effectiveness and robustness of these automated pipelines by evaluating five widely used benchmark suites across 26 open-source SLMs under a unified judging rubric, which assigns a score of 0, 1, or 0.5 to harmful, safe, or ambiguous/irrelevant responses, respectively. Across the benchmarks, ambiguous judgments dominate and correlate with prompt complexity and model architecture, indicating that {\em LLM-centric safety benchmarks are insufficient as standalone evidence for SLM safety assessment}. In general, the ambiguity rate increases with lexical density, output perplexity, and output length and decreases with lexical sophistication, self-coherence, and reply-prompt similarity. This reveals a capability-safety confound that mixes model capability with apparent safety. Since ambiguity is prevalent, aggregate mean-score leaderboards are mathematically brittle: model rankings change significantly under reasonable ambiguity treatments, even when the underlying outputs remain unchanged.

</details>

### 55. Approved Too Late: Verdict Staleness in LLM-Guarded Self-Adaptive Systems

📄 [arXiv](https://arxiv.org/abs/2608.26306)　📅 2026-08

**关键词**：`analysis`、`verdict freshness`、`TOCTOU`、`runtime enforcement`

👤 **作者**：Ilai Shraga、Roei Eshel、Lior Gorelik

- 🎯 **研究动机**：自适应系统的 LLM guardrail 批准在检查时正确、执行时可能已过期，形成 TOCTOU 风险
- 🔬 **研究方法**：区分三种 verdict freshness 度量，提出按安全侧裕度与近期特征波动估计批准有效期的 Freshness-Bounded Shield
- 📌 **结论**：五个可复现环境中批准过期率从 3.4%-24.7% 降至 0-1.8%，四个 LLM judge 均存在使用时失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A large language model (LLM) guardrail for a self-adaptive system (SAS) may issue an approval that is correct at check time but stale by actuation. This creates an Execute-stage time-of-check to time-of-use (TOCTOU) hazard. We study verdict freshness: whether a guardrail verdict remains valid when used. We distinguish three quantities that answer different questions: all-candidate verdict change under fixed-action replay, oracle-labeled approval expiry on recorded closed-loop trajectories, and judge-conditioned use-time invalidity. Across five reproducible SAS environments, all-candidate verdict-change rates span 5.3-48.4% at a common replay shift of eight simulator steps. We introduce the Freshness-Bounded Shield (FBS), which estimates each approval's validity horizon from its safe-side margin and recent feature volatility, without an explicit plant-dynamics model. Using fixed settings documented in the artifact, FBS reduces oracle-labeled approval-expiry rates from 3.4-24.7% to 0-1.8% at the same shift. A separate audit of four LLM judges finds nonzero judge-conditioned use-time invalidity in every approval stream. We formulate a freshness contract: every approval must be correct at check time and remain valid at use time.

</details>

### 56. The Latent Diagnostic Taxonomy: A Framework for Constructing Classifiers and Diagnosing Their Decisions, Applied to Prompt Injection Detection

📄 [arXiv](https://arxiv.org/abs/2608.26423)　📅 2026-08

**关键词**：`analysis`、`detection`、`safeguard classifier`、`decision trust`、`heuristic shortcut`、`prompt-injection classifier`

👤 **作者**：Jaturong Kongmanee、Smile Thanapattheerakul

- 🎯 **研究动机**：safeguard classifier 的高置信判定可能依赖脆弱 shortcut，部署者不知哪些可信
- 🔬 **研究方法**：以维度优化分类器与 latent support vector 定位改变预测的 token，按单 token 攻击幅度构建诊断 taxonomy 分流输入
- 📌 **结论**：prompt injection 数据上约 77% 高置信判定不抗移除单个 token，分为校准失败与真实可利用 shortcut 两类

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper proposes a framework for constructing a classifier as a safeguard layer, and for developing a complementary diagnostic that identifies which of the classifier's confident decisions can be trusted. This framework, the Latent Diagnostic Taxonomy, consists of (i) constructing a dimensionality-optimized classifier, in which the embedding dimensionality is empirically selected via cross-validated performance rather than fixed a priori, (ii) locating a relatively small set of latent support vectors (~ 29% of total training examples) representing influential prompts for identifying tokens that alter the classifier's predicted labels, and (iii) utilizing such tokens and their associated attack magnitudes for constructing a diagnostic taxonomy. This diagnostic taxonomy provides an end-to-end guideline for flagging prompts that require different treatments: rely Safely on the classifier's decision; flag Heuristic Bias and Heuristic Override cases; route Insufficient Context cases for further human/safety review. Applying the framework to a classifier trained on a public prompt injection dataset, we find that a substantial fraction of its confident decisions (~ 77%) are not robust to removing a single token, and that this brittleness separates into two distinct failure patterns: a confidence calibration failure and a genuinely exploitable shortcut. For each zone of the taxonomy, we also recommend strategies for remediating diagnosed prompts. We illustrate the framework as a series of steps, demonstrating how each step operates.

</details>

### 57. aipsy-judge: A Specialized, Psychologist-Corrected Local Judge for the Psychological Safety of Conversational AI

📄 [arXiv](https://arxiv.org/abs/2608.24899) · 🤗 [Model](https://huggingface.co/keidolabs/aipsy-judge-1.0)　📅 2026-08

**关键词**：`detection`、`analysis`、`safety judge`、`self-preference`、`tail-failure calibration`、`psychological-safety guard`

👤 **作者**：Michael Keeman、Anastasia Keeman

- 🎯 **研究动机**：前沿模型或简单平均做 judge 对心理安全评分并不安全：分歧集中于安全指标且有自偏好
- 🔬 **研究方法**：三个前沿模型生成兼评判 3000 条消息并对心理学家评分，据此蒸馏专家校正的逐指标本地 judge
- 📌 **结论**：Gemini judge 带 +0.99 自偏好且漏检尾部危害；本地 aipsy-judge 危机检测 kappa 升至 0.82、捕获 92% 危机

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The standard recipe for LLM-as-judge -- pick a frontier model, or average several -- is actively unsafe for grading the psychological safety of conversational AI. Using aipsy-bench, an open frozen safety instrument, we run a fully-crossed competence study: three frontier models (gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash) serve as both generators and judges of 3,000 mental-health, companion, and coaching messages against a psychologist's ratings. The disagreement is not noise: it is structured, concentrated on the safety-critical metrics, and one judge (Gemini) is an outlier -- the most lenient, carrying a +0.99 self-preference premium, flagging far fewer tail failures, and scoring a means-in-hand self-harm response "exemplary." Inter-judge agreement on empathy, where sycophancy hides, is the lowest in the battery (alpha 0.24). One axis stands apart: the binary crisis-detection flag is the one safety-critical signal judges agree on (alpha 0.80), erring toward over-flagging, the safe direction for a triage screen. Equal-weight averaging, the canonical fix, blends that leniency and tail-blindness into the safety score. Off-the-shelf open-weight judges are worse for a dispositional, not capability, reason -- and disposition is fine-tunable. We therefore distill a per-metric, psychologist-corrected target into a small, frozen, local model, aipsy-judge-1.0, an Apache-2.0 fine-tune of Gemma-4-26B-A4B. aipsy-judge-1.0 tracks the corrected target better than its base on the composite (ICC 0.64 to 0.75) and crisis detection (kappa 0.65 to 0.82), catches 92% of crises with a false-positive lean, and grades more faithfully than any single frontier judge, while every transcript stays on the machine. These are directional readings against a single-expert-informed target, not validated multi-rater agreement. A safety grader that shares a vendor's post-training shares its blind spots.

</details>

### 58. Safety Hacking in Constrained Best-of-$N$ Inference-time Scaling

📄 [arXiv](https://arxiv.org/abs/2608.22915)　📅 2026-08

**关键词**：`analysis`、`safety proxy`、`feasible-set contamination`、`guard composition`、`safety hacking`、`proxy constraint`

👤 **作者**：Akifumi Wachi、Takumi Tanabe、Youhei Akimoto

- 🎯 **研究动机**：推理时管线先采样 N 个输出、经学习安全 proxy 过滤再返回奖励最高者，这一组合的安全风险未被刻画
- 🔬 **研究方法**：定义 safety hacking（通过学习约束但违反真实安全准则的选择），对 constrained Best-of-N 推导由 proxy-feasible 集内安全/不安全输出联合上奖励尾支配的有限 N 界，并提出 χ² 有界覆盖控制与 constrained pessimistic sampling
- 📌 **结论**：不安全但可行的输出尾部更重时，N 增大 safety hacking 渐近必然，即使 proxy 误差任意小；覆盖控制只能限制放大、无法修复被污染的可行集

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Inference-time pipelines often sample multiple outputs, filter them with a learned safety model, and return the proxy-feasible output with the highest learned reward. We show that this composition creates a two-stage failure: an imperfect safety proxy first contaminates the feasible set with unsafe outputs, and reward maximization can then amplify this residual contamination. We define \emph{safety hacking} as selecting an output that passes the learned constraint but violates the true safety criterion. For constrained Best-of-$N$ sampling, we derive finite-$N$ bounds governed by the joint upper reward tails of safe and unsafe outputs within the proxy-feasible set. If unsafe-but-feasible outputs have the heavier tail, safety hacking becomes asymptotically certain as $N$ grows, even when false-positive mass and average safety- and reward-proxy errors are arbitrarily small. We also show that policies within a bounded $χ^2$ divergence from the proxy-feasible reference distribution admit an $N$-independent safety-hacking bound, and instantiate this general coverage-control principle with constrained pessimistic sampling. Coverage control limits amplification but cannot repair a contaminated feasible set: admitted unsafe outputs may still be favored, and regularized selection is not necessarily safer than constrained Best-of-$N$ for every reward proxy. Toy and language-model experiments characterize both contamination and its reward-tail amplification, which exposes an inherent difficulty in inference-time scaling with learned safety models.

</details>

### 59. Breaking the Assumptions: Auditing Input-Side Jailbreak Defenses Against Semantic Attacks

📄 [arXiv](https://arxiv.org/abs/2608.21895)　📅 2026-08

**关键词**：`analysis`、`benchmark`、`input-side guard`、`assumption audit`、`semantic attack`、`semantic jailbreak`

👤 **作者**：Aaditya Pratap、Harsh Kasyap、Somanath Tripathy

- 🎯 **研究动机**：经 Ollama 等本地部署的 LLM 无 API 侧审核，安全完全依赖输入侧防御，而只报告总体 ASR 无法说明防御为何失效
- 🔬 **研究方法**：对 SmoothLLM、Erase-and-Check、Sequential Monitors、Semantic Smoothing、Self-Denoised Smoothing、Perplexity Filtering 六种防御逐一提取其设计假设、推导违反时应出现的失效模式，并在六个开源模型（14B–35B）与 13,800 条评测记录上验证
- 📌 **结论**：把每个失败回溯到被破坏的具体假设，为 guardrail 审计提供从机制前提到实证症状的诊断路径

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Locally deployed Large Language Models (LLMs) via inference engines such as Ollama run without the moderation and abuse detection present in API-served models. Therefore, the safety of LLMs depends on the defense mechanisms used, and their effectiveness depends on the assumptions on which they were designed. This paper does an audit of defense mechanisms under jailbreak attacks on locally deployed models. Some defenses provide formal guarantees (SmoothLLM, Erase-and-Check, Sequential Monitors), while others rely on empirical detection results (Semantic Smoothing, Self-Denoised Smoothing, Perplexity Filtering). Instead of merely observing that defenses fail, we trace each failure back to the specific assumption: for every defense, we extract the condition it relies on, derive the empirical pattern a violation should produce, and test that prediction on six open-weight models (14B to 35B parameters) with a corpus of 100 jailbreak prompts taken from more than 40 public sources, totalling 13,800 evaluation records.

</details>

### 60. No One Model Catches Every Harm: Benchmarking Content Moderation Across Safety Scenarios

📄 [arXiv](https://arxiv.org/abs/2608.21775)　📅 2026-08

**关键词**：`benchmark`、`content moderation`、`guard-model selection`、`scenario blind spot`、`safety scenario`、`cross-model evaluation`

👤 **作者**：Afshin Orojlooyjadid、Hitesh Patel

- 🎯 **研究动机**：通用 LLM 与专用内容审核模型都被用作安全层，但哪类模型适合哪类有害内容缺乏系统比较
- 🔬 **研究方法**：系统测试 53 个模型，覆盖组织为四类的 11 个数据集，在 prompt-only 与 prompt-response 两种设置下评估安全能力
- 📌 **结论**：大型前沿模型在某类领先却在其他类显著落后于更小的专用模型，真实对话安全在所有模型家族中基本未解决——规模本身不保证安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly deployed in real-world applications, yet they remain vulnerable to generating harmful content. From adversarial jailbreaks that bypass safety filters to implicit hate that evades detection, the range of risks these models pose continues to grow. While both specialized content moderators and general-purpose LLMs are being used as safety layers, the question of which model is best suited for which type of harmful content remains unanswered. We present the most comprehensive evaluation of LLM safety capabilities to date, systematically testing \textbf{53} models across \textbf{11} datasets that we organize into four distinct categories. Our evaluation under both prompt-only and prompt-response settings uncovers critical blind spots: large frontier models that lead on one category fall significantly behind smaller, specialized alternatives on others, and real-world conversational safety remains largely unsolved across all model families. These findings challenge the assumption that scale alone ensures safety, and provide the community with a structured framework for informed model selection.

</details>

### 61. When Refusal Looks Safe: The Refusal-Cue Shortcut in Safety Guard Models

📄 [arXiv](https://arxiv.org/abs/2608.03201)　📅 2026-08

**关键词**：`analysis`、`refusal-cue shortcut`、`response moderation`、`causal intervention`

👤 **作者**：Yu Feng、…、Jieping Ye

- 🎯 **研究动机**：安全 guard 训练集中拒答表达几乎只与无害标签共现，形成拒答线索捷径但未被审计
- 🔬 **研究方法**：审计 WildGuardMix 与 GR-Train 发现该捷径波及 LlamaGuard3、Qwen3Guard 等闭源模型；用 sparse complementary masking 后验抑制关联注意力头与 MLP 神经元
- 📌 **结论**：拒答线索诱发的检测失败相对减少约 79%，效果迁移到未见位置与数据集，且基本保留对真实拒答的识别

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety guards are widely used to filter harmful content and are typically trained via supervised fine-tuning on labeled prompt-response pairs. We audit two widely used safety-guard training datasets, WildGuardMix and GR-Train, and find that among responses to harmful prompts, refusal expressions co-occur almost exclusively with unharmful labels. This imbalance motivates what we term the refusal-cue shortcut: inserting a refusal cue into a harmful response could flip the guard's verdict from harmful to unharmful. The shortcut affects not only guards trained on these datasets but also officially released models such as LlamaGuard3 and Qwen3Guard whose training data is undisclosed. It persists across response positions and is generally stronger in smaller variants within a family. To mitigate it, we adapt sparse complementary masking as a lightweight post-hoc intervention that identifies and suppresses a small set of shortcut-associated attention heads and MLP neurons without retraining. On two primary benchmarks, the intervention achieves an approximately 79% relative reduction in response-initial detection failures induced by refusal cues, while preserving standard detection performance. Although optimized using cues at a single response position, the suppression effect transfers to unseen positions and datasets, suggesting that shortcut manifestations across positions are partly mediated by shared internal components. Further analysis provides evidence that shortcut reliance and legitimate refusal recognition are partially functionally separable, as suppressing the shortcut broadly preserves the guard's ability to recognize genuine refusals.

</details>

### 62. Safeguards Based on Copyable Context Cannot Provide Reliable Safety for LLMs

📄 [arXiv](https://arxiv.org/abs/2607.27951)　📅 2026-07

**关键词**：`analysis`、`copyable context`、`trusted-user gating`、`impossibility result`

👤 **作者**：Pingyu Wu、Lingyao Zhu、Weiming Zhang、Nenghai Yu

- 🎯 **研究动机**：护栏在看到答案如何被使用前就决定是否回答，而攻击者可模仿良性请求与交互历史，可复制证据下双用途任务存在根本限制
- 🔬 **研究方法**：分离模型释放的能力与下游使用的证据，在证据可复制时推导攻击者协助的精确最坏下界，证明有用能力、可靠安全与开放访问构成三难；可信凭证可补充不可复制证据
- 📌 **结论**：双用途评估、自适应攻击与已部署可信访问项目的证据支持这些条件的现实相关性，仅靠可复制上下文无法提供可靠安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model safeguards decide whether to answer before seeing how an answer will be used. This creates a basic problem for dual-use tasks: the same answer can help an authorized professional or an attacker, while an attacker can imitate a benign request and interaction history. We separate the capability released by the model from the evidence available about downstream use. When that evidence is copyable, we derive the exact worst-case floor on attacker assistance while preserving useful answers. The result yields a safety trilemma: Useful Capability, Reliable Safety, and Open Access cannot coexist. We then show how a trusted credential can complement existing safeguards by adding hard-to-copy information that predicts actual downstream use, and identify the stronger condition needed to eliminate the floor. Evidence from dual-use evaluations, adaptive attacks, and deployed trusted-access programs supports the practical relevance of these conditions.

</details>

### 63. Choosing Where and How to Moderate: End-to-End Trade-offs in Filter Placement and Response Rewriting

📄 [arXiv](https://arxiv.org/abs/2607.26200)　📅 2026-07

**关键词**：`analysis`、`filter placement`、`response rewriting`、`end-to-end trade-off`

👤 **作者**：Mengya Hu、…、Curt Tigges

- 🎯 **研究动机**：内容审核分类器通常被孤立评估，部署时还需选择干预位置与标记后的处置，端到端权衡未被刻画
- 🔬 **研究方法**：以 Usefulness（展示非有害相关回应的轮次比）与 Harmful Exposure 两个端到端客户结果指标，比较仅输入/仅响应/双端硬阻断及响应重写配置，在人工标注产品基准与 ToxicChat 上评估
- 📌 **结论**：仅响应过滤获得最高过滤后 Usefulness、双端过滤最低有害暴露；响应重写可找回大部分被阻断流量且观测有害暴露与纯阻断相当；应按部署约束比较配置而非套用普适规则

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Content-moderation classifiers are usually evaluated in isolation, but deployment requires choosing where to intervene and what follows a flag. We evaluate these choices using two end-to-end customer-outcome metrics rather than component accuracy: Usefulness, the fraction of turns with a shown, non-harmful, relevant response, and Harmful Exposure, the fraction with a shown harmful response. Latency and error rates are diagnostics. We compare Input only, Response only, and Input + response hard blocking on a human-labelled product benchmark and public ToxicChat evaluation. At the evaluated operating points, Response only achieves the highest filter-only Usefulness in both settings, while Input + response achieves lower Harmful Exposure. Replacing Response only blocking with Response + rewrite recovers most blocked traffic and yields the same observed Harmful Exposure count as Response only blocking for the selected configuration; this equality is not an equivalence result. Probe routing substantially reduces conditional route-and-generation time relative to LLM routing at comparable measured outcomes. A focused output review shows how rewrites balance filter passage with usefulness by generalizing triggering language while retaining benign intent and safe redirection; some sensitive-domain outputs nevertheless omit potentially safety-relevant support information. These results support comparing moderation configurations under deployment-specific safety and latency constraints rather than applying a universal placement rule. Code and public artifacts are available at https://github.com/microsoft/mod-frontier

</details>

### 64. Behind the Refusal: Determining Guardrail Activation via Behavioral Monitoring

📄 [arXiv](https://arxiv.org/abs/2607.02121)　📅 2026-07

**关键词**：`analysis`、`guardrail activation`、`behavioral monitoring`、`black-box inference`

👤 **作者**：William Hackett、Peter Garraghan

- 🎯 **研究动机**：黑盒对抗仿真中难以区分拦截来自护栏还是 LLM 拒绝，而绕过两者所需技术差异巨大
- 🔬 **研究方法**：提出首个黑盒护栏侦察方法：仅凭黑盒访问与零先验，通过 HTTP、词汇与时序信号的行为监测判定护栏存在、封锁内容类别并区分护栏拦截与模型拒绝
- 📌 **结论**：护栏存在检测准确率 100%（良性-恶意行为分离 q<0.001），区分拦截来源的平均 F1 98%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) and agentic systems become integrated into real-world applications, ensuring their safety and security is critical. Guardrail systems that detect and block malicious instructions sent to and from an LLM are an essential component of AI security. However, researchers conducting black-box adversarial emulation against production AI systems often struggle to determine whether a guardrail block or an LLM rejection has occurred. This distinction is important because the techniques used to bypass guardrails can differ substantially from those used to bypass LLM safety alignment, and has a material impact on attack technique selection and optimization. We propose the first black-box guardrail reconnaissance methodology, which detects the presence of a guardrail within a target AI system through behavioral monitoring of HTTP, lexical, and timing signals, assuming only black-box access and zero prior knowledge of the guardrail or AI system. Experiments demonstrate that our approach detects guardrail presence with 100% accuracy, with statistically significant behavioral separation between benign and malicious interactions (q < 0.001). Our approach further identifies the content categories a guardrail is designed to block, and distinguishes guardrail blocks from LLM rejection on unseen prompts with an average F1 score of 98%.

</details>

### 65. Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation

📄 [arXiv](https://arxiv.org/abs/2606.25782)　📅 2026-06

**关键词**：`analysis`、`encoder-decoder comparison`、`safety judge`、`adversarial evaluation`

👤 **作者**：Han Jeon、Shiv Medler、Joseph Voyles、Matt Wood

- 🎯 **研究动机**：LLM judge 慢且贵，微调 ModernBERT 系编码器能否无损替代其对有害输出的判定未知
- 🔬 **研究方法**：在对抗数据集上把编码器分类器与规则匹配、微调 LLM 分类器、多种 judge 提示策略（StrongReject、ShieldGemma、LlamaGuard 等）对齐比较，按攻击技术细分
- 📌 **结论**：给出编码器分类器何时可作为低成本低延迟替代的实证指导

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the widespread adoption of large language models (LLMs) in chatbots and everyday applications, companies increasingly need guardrails that are effective while remaining low-cost and low-latency. Safety evaluation of LLM outputs has generally relied on LLM-based judges, which can be effective but are often slow and expensive to deploy at scale. In this paper, we evaluate whether fine-tuned modern encoder classifiers from the ModernBERT family, including ModernBERT and Ettin, can reliably identify harmful LLM outputs in user-model conversations without substantial performance loss relative to LLM-based judges. We benchmark these encoder classifiers against rule-based prefix matching, fine-tuned LLM classifiers, and LLM judges using a range of judge-prompting strategies across open-source adversarial datasets. The LLM judges include evaluation methodologies from StrongReject, ShieldGemma, JailbreakBench, AILuminate, SorryBench, and a Claude-as-a-judge setup, as well as fine-tuned safety classifiers such as LlamaGuard 3 and LlamaGuard 4. The encoder classifiers are fine-tuned on judge-labeled data using a majority-voting label strategy and are then evaluated on a gold-standard holdout dataset to assess their performance relative to LLM judges. We report absolute performance using F1 score, false negative rate, and precision-recall metrics. We also break down results by attack technique, including single-turn prompting, decomposition, escalation, and context manipulation, to identify where encoder classifiers align with or diverge from LLM-based judges. Our findings provide guidance on when encoder classifiers can serve as cost- and latency-efficient alternatives to LLM-based safety evaluation.

</details>

### 66. Beyond Red-Teaming: Formal Guarantees of LLM Guardrail Classifiers

📄 [arXiv](https://arxiv.org/abs/2605.10901)　📅 2026-05

**关键词**：`analysis`、`formal verification`、`harmful region`、`classifier certificate`

👤 **作者**：Nikita Kezins、Urbas Ekka、Pascal Berrang、Luca Arnaboldi

- 🎯 **研究动机**：护栏分类器只有经验指标而无形式保证，离散输入空间无自然有害规范、epsilon 球也无语义意义
- 🔬 **研究方法**：把验证移到 pre-activation 空间，将有害区域定义为凸形状（SVD 对齐超矩形给精确 SAT/UNSAT 证书，GMM 给概率证书），利用 sigmoid 单调性 O(d) 闭环证明
- 📌 **结论**：三个自训护栏分类器的全部超矩形配置返回 SAT，暴露可证明安全洞；BERT 的保证覆盖率在最优阈值塌缩到 55%——高经验分不等于形式保证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Guardrail Classifiers defend production language models against harmful behavior, but although results seem promising in testing, they provide no formal guarantees. Providing formal guarantees for such models is hard because "harmful behavior" has no natural specification in a discrete input space: and the standard epsilon-ball properties used in other domains do not carry semantic meaning. We close this gap by shifting verification from the discrete input space to the classifier's pre-activation space, where we define a harmful region as a convex shape enclosing the representations of known harmful prompts. Because the sigmoid classification head is monotonic, certifying the worst-case point is sufficient to certify the entire region, yielding a closed-form soundness proof without approximation in O(d) time. To formally evaluate these classifiers, we propose two constructions of such regions: SVD-aligned hyper-rectangles, which yield exact SAT/UNSAT certificates, and Gaussian Mixture Models, which yield probabilistic certificates over semantically coherent clusters. Applying this framework to three author-trained Guardrail Classifiers on the toxicity domain, every hyper-rectangle configuration returns SAT, exposing verifiable safety holes across all classifiers, despite seemingly high empirical metrics. Probabilistic GMM certificates also expose a divergent structural stability in how these models represent harm. While GPT-2 and Llama-3.1-8B maintain robust coverage of 90% and 80% across varying boundaries, BERT's safety guarantees prove uniquely volatile. This 'coverage collapse' to 55% at the optimal threshold reveals a sparsely populated safety margin in BERT, which only achieves full coverage by adopting an extremely conservative pessimistic threshold. These approaches combined, provide new insights on how effective Guardrail Classifiers really are, beyond traditional red-teaming.

</details>

### 67. When AI Agents Disagree Like Humans: Reasoning Trace Analysis for Human-AI Collaborative Moderation

📄 [arXiv](https://arxiv.org/abs/2604.03796)　📅 2026-04　🏷 ICLR 2026

**关键词**：`analysis`、`multi-agent moderation`、`reasoning disagreement`、`human escalation`

👤 **作者**：Michał Wawer、Jarosław A. Chudziak

- 🎯 **研究动机**：多 agent 分歧被普遍当作待消除的噪声，其作为信号的价值未被检验
- 🔬 **研究方法**：在仇恨言论审核中嵌入五个视角差异化 agent 的推理轨迹，按推理相似性与结论一致性四分类分歧模式，并与人工标注冲突对照
- 📌 **结论**：agent 结论一致与否比原始推理分歧更能预测人工分歧（效应量 d>0.8），支持从共识寻求转向不确定性呈现的多 agent 设计

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When LLM-based multi-agent systems disagree, current practice treats this as noise to be resolved through consensus. We propose it can be signal. We focus on hate speech moderation, a domain where judgments depend on cultural context and individual value weightings, producing high legitimate disagreement among human annotators. We hypothesize that convergent disagreement, where agents reason similarly but conclude differently, indicates genuine value pluralism that humans also struggle to resolve. Using the Measuring Hate Speech corpus, we embed reasoning traces from five perspective-differentiated agents and classify disagreement patterns using a four-category taxonomy based on reasoning similarity and conclusion agreement. We find that raw reasoning divergence weakly predicts human annotator conflict, but the structure of agent discord carries additional signal: cases where agents agree on a verdict show markedly lower human disagreement than cases where they do not, with large effect sizes (d>0.8) surviving correction for multiple comparisons. Our taxonomy-based ordering correlates with human disagreement patterns. These preliminary findings motivate a shift from consensus-seeking to uncertainty-surfacing multi-agent design, where disagreement structure - not magnitude - guides when human judgment is needed.

</details>

### 68. Engagement Undermines Safety: How Stereotypes and Toxicity Shape Humor in Language Models

🎓 [Official](https://aclanthology.org/2026.eacl-long.373/)　📅 2026-03　🏷 ACL 2026

**关键词**：`analysis`、`harmful generation`、`engagement reward`、`toxicity amplification`、`humor reward`

👤 **作者**：Atharvan Dogra、Soumya Suvra Ghosal、Ameet Deshpande、Ashwin Kalyan、Dinesh Manocha

- 🎯 **研究动机**：LLM 广泛用于创意与互动内容，趣味性优化是否与有害内容耦合未知
- 🔬 **研究方法**：以幽默生成为试验台联合测量幽默、刻板性与毒性并用信息论指标分析不协调信号，配讽刺生成任务的人类感知趣味判断
- 📌 **结论**：固定中性设定下有害输出获更高幽默分，存在生成器-评估器偏置放大环；刻板与毒性笑话平均幽默分高 10 至 21%，在被 LLM 标记有趣的笑话中多 11 至 28%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are increasingly used for creative writing and engagement content, raising safety concerns about their outputs. Using humor generation as a testbed, this work evaluates how funniness optimization in modern LLM pipelines couples with harmful content by jointly measuring humor, stereotypicality, and toxicity. We further supplement this by analyzing incongruity signals through information-theoretic metrics. Across six models, we observe that even for fixed neutral setups, harmful outputs receive higher humor scores, indicating a bias amplification loop between generators and evaluators. Information-theoretic analyses show that harmful cues widen predictive uncertainty and, surprisingly, can even make harmful punchlines more expected for some models, suggesting intrinsic structural embedding in learned humor distributions. Experiments and human evaluation on an additional satire-generation task with human-perceived funniness judgments show that LLM funniness relies on increased stereotypicality and toxicity, including for closed models. Quantitatively, stereotypical/toxic jokes gain 10%–21% in mean humor score, stereotypical jokes appear 11% to 28% more often among the jokes marked funny by an LLM-based metric, and up to 10% more often in generations perceived as funny by humans.

</details>

### 69. Reasoning’s Razor: Reasoning Improves Accuracy but Hurts Recall at Critical Operating Points in Safety and Hallucination Detection

🎓 [Official](https://aclanthology.org/2026.eacl-long.190/)　📅 2026-03　🏷 ACL 2026

**关键词**：`analysis`、`safety detector`、`low-FPR regime`、`reasoning trade-off`

👤 **作者**：Atoosa Chegini、…、Mehrdad Farajtabar

- 🎯 **研究动机**：推理提升分类准确率的同时，其在严格低误报率（FPR）精度敏感场景的适用性缺乏系统研究
- 🔬 **研究方法**：在安全检测与幻觉检测两个任务上，对微调与零样本设定、标准 LLM 与 LRM 系统比较开启/关闭推理的表现
- 📌 **结论**：开推理提升整体准确率但在低 FPR 阈值处表现差，关推理在精度敏感区间占优；基于 token 的打分显著优于自述置信度，二者集成可兼得

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reasoning has become a central paradigm for large language models (LLMs), consistently boosting accuracy across diverse benchmarks. Yet its suitability for precision-sensitive use remains unclear. We present the first systematic study of reasoning for classification tasks under strict low false positive rate (FPR) regimes. Our analysis covers two tasks—safety detection and hallucination detection—evaluated in both fine-tuned and zero-shot settings, using standard LLMs and Large Reasoning Models (LRMs). Our results reveal a clear trade-off: Think On (reasoning-augmented) generation improves overall accuracy, but performs poorly at the low-FPR thresholds essential for practical use. In contrast, Think Off (no reasoning during inference) dominates in these precision-sensitive regimes, with Think On surpassing only when higher FPRs are acceptable. In addition, we find token-based scoring substantially outperforms self-verbalized confidence for precision-sensitive deployments. Finally, a simple ensemble of the two modes recovers the strengths of each. Taken together, our findings position reasoning as a double-edged tool: beneficial for average accuracy, but often ill-suited for applications requiring strict precision.

</details>

### 70. Are Open-Weight LLMs Ready for Social Media Moderation? A Comparative Study on Bluesky

📄 [arXiv](https://arxiv.org/abs/2602.05189)　📅 2026-02

**关键词**：`analysis`、`open-weight moderator`、`social-media deployment`、`privacy-preserving inference`

👤 **作者**：Hsuan-Yu Chou、Wajiha Naveed、Shuyan Zhou、Xiaowei Yang

- 🎯 **研究动机**：开源权重 LLM 能否开箱即用胜任社媒审核缺乏系统评估
- 🔬 **研究方法**：以 Bluesky 真实帖文、平台审核决定与人工标注为参照，比较 3 个 open-weight 与 4 个闭源模型的零样本审核表现
- 📌 **结论**：开源模型 sensitivity 81%-97%、specificity 91%-100%，与闭源（72%-98%、93%-99%）大幅重叠，可支撑本地隐私保护审核

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As internet access expands, so does exposure to harmful content, increasing the need for effective moderation. Research has demonstrated that large language models (LLMs) can be effectively utilized for social media moderation tasks, including harmful content detection. While proprietary LLMs have been shown to zero-shot outperform traditional machine learning models, the out-of-the-box capability of open-weight LLMs remains an open question. Motivated by recent developments of reasoning LLMs, we evaluate seven state-of-the-art models: four proprietary and three open-weight. Testing with real-world posts on Bluesky, moderation decisions by Bluesky Moderation Service, and annotations by two authors, we find a considerable degree of overlap between the sensitivity (81%--97%) and specificity (91%--100%) of the open-weight LLMs and those (72%--98%, and 93%--99%) of the proprietary ones. Additionally, our analysis reveals that specificity exceeds sensitivity for rudeness detection, but the opposite holds for intolerance and threats. Lastly, we identify inter-rater agreement across human moderators and the LLMs, highlighting considerations for deploying LLMs in both platform-scale and personalized moderation contexts. These findings show open-weight LLMs can support privacy-preserving moderation on consumer-grade hardware and suggest new directions for designing moderation systems that balance community values with individual user preferences.

</details>

### 71. RAG Makes Guardrails Unsafe? Investigating Robustness of Guardrails under RAG-style Contexts

📄 [arXiv](https://arxiv.org/abs/2510.05310)　📅 2025-10

**关键词**：`analysis`、`RAG context`、`distribution shift`、`input-output guard`

👤 **作者**：Yining She、…、Dan Roth

- 🎯 **研究动机**：护栏模型本身是 LLM，对 RAG 式上下文带来的分布漂移的鲁棒性未被检验
- 🔬 **研究方法**：系统评测 3 个 Llama Guard 与 2 个 GPT-oss 在含检索文档上下文下的判断稳定性，并分离文档、查询与响应各成分的影响
- 📌 **结论**：仅插入良性文档即改变输入与输出护栏约 11% 与 8% 的判断；两种缓解仅带来微小改进，暴露上下文鲁棒性缺口

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the increasing adoption of large language models (LLMs), ensuring the safety of LLM systems has become a pressing concern. External LLM-based guardrail models have emerged as a popular solution to screen unsafe inputs and outputs, but they are themselves fine-tuned or prompt-engineered LLMs that are vulnerable to data distribution shifts. In this paper, taking Retrieval Augmentation Generation (RAG) as a case study, we investigated how robust LLM-based guardrails are against additional information embedded in the context. Through a systematic evaluation of 3 Llama Guards and 2 GPT-oss models, we confirmed that inserting benign documents into the guardrail context alters the judgments of input and output guardrails in around 11% and 8% of cases, making them unreliable. We separately analyzed the effect of each component in the augmented context: retrieved documents, user query, and LLM-generated response. The two mitigation methods we tested only bring minor improvements. These results expose a context-robustness gap in current guardrails and motivate training and evaluation protocols that are robust to retrieval and query composition.

</details>

### 72. Peering Behind the Shield: Guardrail Identification in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2502.01241) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.566/)　📅 2025-02　🏷 ACL 2026

**关键词**：`attack`、`guardrail fingerprinting`、`adversarial probe`、`deployment placement`

👤 **作者**：Ziqing Yang、Yixin Wu、Rui Wen、Michael Backes、Yang Zhang

- 🎯 **研究动机**：黑盒 Agent 隐藏所用 guardrail 身份与部署位置，识别它是对抗的前提
- 🔬 **研究方法**：AP-Test 用 guard 专属对抗 prompt 与输入/输出双测试策略，配 match score 度量实现稳健识别
- 📌 **结论**：多 Agent 与四种开源 guardrail 上多场景达到完美分类精度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid adoption of large language models (LLMs), conversational AI agents have become widely deployed across real-world applications. To enhance safety, these agents are often equipped with guardrails that moderate harmful content. Identifying the guardrails in an agent thus becomes critical for adversaries to understand the system and design guard-specific attacks. In this work, we introduce AP-Test, a novel approach that leverages guard-specific adversarial prompts to detect the identity of guardrails deployed in black-box AI agents. Our method addresses key challenges in this task, including the influence of safety-aligned LLMs and other guardrails, as well as a lack of principled decision-making strategies. AP-Test employs two complementary testing strategies, input and output guard tests, and a new metric, match score, to enable robust identification. Experiments across diverse agents and four open-source guardrails demonstrate that AP-Test achieves perfect classification accuracy in multiple scenarios. Ablation studies further highlight the necessity of our proposed components. Our findings reveal a practical path toward guardrail identification in real-world AI systems.

</details>

### 73. Jailbreaking Attacks vs. Content Safety Filters: How Far Are We in the LLM Safety Arms Race?

📄 [arXiv](https://arxiv.org/abs/2512.24044)　📅 2025-12

**关键词**：`survey`、`full-pipeline evaluation`、`input-output filter`、`jailbreak detection`

👤 **作者**：Yuan Xin、Dingfan Chen、Linyi Yang、Michael Backes、Xiao Zhang

- 🎯 **研究动机**：已有越狱评估只针对裸模型，忽略含内容审核过滤器的完整部署流水线
- 🔬 **研究方法**：首次系统评估越狱攻击在含输入与输出过滤两阶段的完整推理管线上的成功率
- 📌 **结论**：几乎所有被评测越狱技术都会被至少一个安全过滤器检出，先前研究高估了攻击的实际成功率；但过滤器仍需平衡召回与精度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) are increasingly deployed, ensuring their safe use is paramount. Jailbreaking, adversarial prompts that bypass model alignment to trigger harmful outputs, present significant risks, with existing studies reporting high success rates in evading common LLMs. However, previous evaluations have focused solely on the models, neglecting the full deployment pipeline, which typically incorporates additional safety mechanisms like content moderation filters. To address this gap, we present the first systematic evaluation of jailbreak attacks targeting LLM safety alignment, assessing their success across the full inference pipeline, including both input and output filtering stages. Our findings yield two key insights: first, nearly all evaluated jailbreak techniques can be detected by at least one safety filter, suggesting that prior assessments may have overestimated the practical success of these attacks; second, while safety filters are effective in detection, there remains room to better balance recall and precision to further optimize protection and user experience. We highlight critical gaps and call for further refinement of detection accuracy and usability in LLM safety systems.

</details>

### 74. SoK: Evaluating Jailbreak Guardrails for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2506.10597) · 🎓 [Official](https://sp2026.ieee-security.org/accepted-papers.html)　📅 2025-06　🏷 IEEE S&P 2026

**关键词**：`survey`、`jailbreak guardrails`、`evaluation framework`、`adaptive attacks`

👤 **作者**：Xunguang Wang、Zhenlan Ji、Wenxuan Wang、Zongjie Li、Daoyuan Wu、Shuai Wang

- 🎯 **研究动机**：LLM 越狱护栏领域碎片化，缺乏统一分类与综合评估框架
- 🔬 **研究方法**：提出六维护栏分类法与 Security-Efficiency-Utility 评估框架，经系统实验分析护栏的强弱项
- 📌 **结论**：厘清现有护栏在不同攻击类型下的普适性与优化方向，为护栏研发提供结构化基础

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have achieved remarkable progress, but their deployment has exposed critical vulnerabilities, particularly to jailbreak attacks that circumvent safety alignments. Guardrails--external defense mechanisms that monitor and control LLM interactions--have emerged as a promising solution. However, the current landscape of LLM guardrails is fragmented, lacking a unified taxonomy and comprehensive evaluation framework. In this Systematization of Knowledge (SoK) paper, we present the first holistic analysis of jailbreak guardrails for LLMs. We propose a novel, multi-dimensional taxonomy that categorizes guardrails along six key dimensions, and introduce a Security-Efficiency-Utility evaluation framework to assess their practical effectiveness. Through extensive analysis and experiments, we identify the strengths and limitations of existing guardrail approaches, provide insights into optimizing their defense mechanisms, and explore their universality across attack types. Our work offers a structured foundation for future research and development, aiming to guide the principled advancement and deployment of robust LLM guardrails. The code is available at https://github.com/xunguangwang/SoK4JailbreakGuardrails.

</details>

### 75. Sledgehammer or Scalpel? A Fine-grained Adaptive Framework for Implicit Hate Speech

📄 [arXiv](https://arxiv.org/abs/2608.27462)　📅 2026-08

**关键词**：`detection`、`implicit hate`、`adaptive routing`、`content moderation`

👤 **作者**：Han Wang、Yuhu Cheng、Xuesong Wang、Yi Zhu

- 🎯 **研究动机**：隐式仇恨以隐喻和上下文线索隐藏恶意，现有 PLM/LLM 方法对所有样本套用单一推理流程，忽略细粒度语言差异且对简单样本浪费算力
- 🔬 **研究方法**：定义 Shallow/Targeted/Context-Dependent 三类隐式仇恨并提出 FAID：浅层样本用轻量 prompt-tuning，Targeted 用知识增强迭代揭示隐藏目标，Context-Dependent 用 agentic 框架自动演化上下文补全背景
- 📌 **结论**：在四个 benchmark 上显著优于 SOTA，同时把重计算集中于复杂隐式样本

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unlike explicit attacks with obvious profanity, implicit hate speech hides malice within seemingly compliant expressions through metaphors and contextual hints, making its detection in online content review challenging. While existing PLM- or LLM-based methods perform well, they typically apply a single reasoning process to all samples. This overlooks fine-grained linguistic nuances and causes unnecessary computation for simpler cases. We observe that online hate speech is not monolithic but manifests in varied forms. We therefore define three fine-grained categories: Shallow, Targeted, and Context-Dependent. Accordingly, we propose Fine-grained Adaptive Implicit Hate speech Detection (FAID), a novel framework that first performs fine-grained classification and then adapts to specific categories. Specifically, for Shallow samples with surface-identifiable intents, the framework adopts lightweight prompt-tuning for rapid classification; for Targeted comments that bind malicious intent to concealed targets, we design knowledge augmentation to iteratively refine the model and reveal hidden targets; for Context-Dependent comments lacking background information, we utilize an agentic framework that automatically generates prompts to evolve context, infer missing background information and identify ambiguous malicious intents. This adaptive architecture focuses computational resources on complex implicit samples while avoiding redundant reasoning for shallow samples. Experiments on four benchmark datasets demonstrate that FAID significantly outperforms SOTA baselines.

</details>

### 76. From Specialization to Generalization: Instruction-tuned LLMs for Robust Harmful Content Mitigation

📄 [arXiv](https://arxiv.org/abs/2608.25605)　📅 2026-08

**关键词**：`detection`、`hate-speech moderation`、`instruction tuning`、`cross-domain generalization`

👤 **作者**：Lukas Edman、Daryna Dementieva、Alexander Fraser

- 🎯 **研究动机**：此前对比显示 prompted LLM 在仇恨言论检测上仅略优于 BERT 类专用分类器，跨域跨语言泛化不足
- 🔬 **研究方法**：统一 36 个英文仇恨言论数据集的多样标注体系，基于 Qwen3 指令微调 generalist 模型
- 📌 **结论**：域内达 SOTA，且在 encoder 分类器常失手的跨域与跨语言泛化上显著改善

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) demonstrate impressive performance across a wide range of general NLP tasks; however, their effectiveness in sensitive domains, such as hate speech detection, remains less clear. Prior studies comparing prompted LLMs with state-of-the-art encoder-based models (e.g., BERT variants (Roy et al., 2023; Dönmez et al., 2024)) have shown only marginal gains, suggesting that LLMs may not excel in hate speech detection or mitigation. In this work, we revisit this question through the lens of instruction tuning. By thoroughly unifying 36 English hate speech datasets spanning multiple labeling schemes, we fine-tune a generalist LLM, based on Qwen3 (Qwen Team, 2025), specifically for hate speech mitigation. Our results demonstrate not only state-of-the-art performance on in-domain benchmarks but also substantial improvements in cross-domain and cross-lingual generalization--areas where encoder-based specialist classifiers often struggle.

</details>

### 77. SPAR-Hate: Auditor-Guided Multi-Perspective Role Reasoning for Bilingual Hate Speech Parsing

📄 [arXiv](https://arxiv.org/abs/2608.22018)　📅 2026-08　🏷 EMNLP 2026

**关键词**：`detection`、`defense`、`bilingual moderation`、`evidence arbitration`、`structured hate parsing`、`multi-perspective reasoning`

👤 **作者**：Yifan Lyu、Dianqing Lin、Xinran Li、Jiaqi Qiao、Xiujuan Xu

- 🎯 **研究动机**：仇恨言论研究从粗粒度分类转向结构化解析（联合识别 target、论据与标签），但多 target、局部解读冲突与文化编码语言使绑定难以恢复
- 🔬 **研究方法**：SPAR-Hate 审计引导多视角框架：把文档拆为局部焦点单元，从 Victim、Moderator、Cultural Bystander 三视角生成有证据候选，在 grounding 与 schema 约束下仲裁冲突并重组预测
- 📌 **结论**：STATE-ToxiCN 与受控 TBO split 上在严格联合 target-argument-label 指标取得提升；结构化 teacher trace 还可训练更小 student 模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Hate speech research has moved from coarse-grained classification towards structured parsing, where systems jointly identify targets, supporting arguments, and target-level labels. Documents with multiple targets, conflicting local readings, or culturally coded language make these bindings difficult to recover. SPAR-Hate is an auditor-guided multi-perspective role-reasoning framework for bilingual hate speech parsing. It decomposes each document into local focus units, elicits evidence-grounded candidates from Victim, Moderator, and Cultural Bystander perspectives, resolves candidate conflicts under grounding and schema constraints, and reassembles sample-level predictions. Experiments on STATE-ToxiCN and a controlled TBO split show gains across local and API backbones, concentrated on strict joint target-argument-label metrics. Full-test integrated-prompt controls, component ablations, and bounded-arbitration diagnostics identify the contribution of separated perspective generation and arbitration. Structured teacher traces also support training a smaller student model.

</details>

### 78. SMARTER: A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models

🎓 [Official](https://aclanthology.org/2026.acl-long.1584/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`guard model`、`content moderation`、`safety-utility trade-off`、`harmful content`、`safety evaluation`

👤 **作者**：Huy Nghiem、Advik Sachdeva、Hal Daumé III

- 🎯 **研究动机**：社交媒体毒性内容检测需要可解释审核，但高质量标注数据稀缺
- 🔬 **研究方法**：提出 SMARTER 两阶段：用 LLM 自身输出为对错标签合成解释以做最少监督的偏好优化，再经跨模型训练让弱模型对齐强模型精炼解释
- 📌 **结论**：在 HateXplain、Latent Hate、Implicit Hate 三个基准上仅用 6-57% 训练数据即比 few-shot 基线 macro-F1 提升最高 13%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

To address toxic content on social media, we introduce SMARTER, a data-efficient 2-stage framework for explainable content moderation using Large Language Models (LLMs). In Stage 1, we leverage LLMs’ own outputs to generate synthetic explanations for correct and incorrect labels, enabling preference optimization with minimal supervision. In Stage 2, we refine explanation quality through cross-model training, allowing weaker models to align with stronger ones. Experiments on 3 benchmarks (HateXplain, Latent Hate, Implicit Hate) show SMARTER achieves up to 13% macro-F1 improvement over few-shot baselines using only 6-57% of training data. Our framework offers a scalable strategy for low-data settings by harnessing LLMs’ self-improvement for explainable moderation.

</details>

### 79. RV-HATE: Reinforced Multi-Module Voting for Implicit Hate Speech Detection

🎓 [Official](https://aclanthology.org/2026.acl-long.2104/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`guard model`、`content moderation`、`safety-utility trade-off`、`harmful content`、`safety evaluation`

👤 **作者**：Yejin Lee、Hyeseon Ahn、Yo-Sub Han

- 🎯 **研究动机**：仇恨言论数据集因来源与平台不同而风格各异，既有检测方法用固定方法不适配数据特性
- 🔬 **研究方法**：提出 RV-HATE：多个专司不同语言/上下文特征的模块，用强化学习针对具体数据集优化各模块权重，再以投票聚合出最终判定
- 📌 **结论**：针对数据集特性定制检测流程，显著优于静态方法，尤其有效应对隐性仇恨言论，并可解释各数据集特征

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Hate speech remains prevalent in human society and continues to evolve in its forms and expressions. Modern advancements in the internet and online anonymity accelerate its rapid spread and complicate its detection. However, hate speech datasets exhibit diverse characteristics primarily because they are constructed from different sources and platforms, each reflecting different linguistic styles and social contexts. Despite this diversity, prior studies on hate speech detection often rely on fixed methodologies without adapting to data-specific features. We introduce RV-HATE, a detection framework designed to account for the dataset-specific characteristics of each hate speech dataset. RV-HATE consists of multiple specialized modules, where each module focuses on distinct linguistic or contextual features of hate speech. The framework employs reinforcement learning to optimize weights that determine the contribution of each module for a given dataset. A voting mechanism then aggregates the module outputs to produce the final decision. RV-HATE offers two primary advantages: (1) it improves detection accuracy by tailoring the detection process to dataset-specific attributes, and (2) it also provides interpretable insights into the distinctive features of each dataset. Consequently, our approach effectively addresses implicit hate speech and achieves superior performance compared to conventional static methods.

</details>

### 80. New Terms, New Toxicity: Consensus-based Chinese Neologism Toxicity Detection via Search-Augmented LLMs

🎓 [Official](https://aclanthology.org/2026.acl-long.1602/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`guard model`、`content moderation`、`safety-utility trade-off`、`harmful content`、`safety evaluation`

👤 **作者**：Shiyao Cui、…、Minlie Huang

- 🎯 **研究动机**：毒性新词表面良性但已在公众共识中演化为毒性用法，内容审核系统难识别
- 🔬 **研究方法**：提出毒性新词起源与共识验证标准分类法并构建风险词表；SeTox 搜索增强框架让静态 LLM 引入实时网络语境做检测
- 📌 **结论**：3B 规模模型即超近期大模型，可扩展引入现实知识检测毒性新词

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Neologisms, emerging terms in meaning or form, can serve as new vehicles for toxic expression, like “田园女” (“country girl”) as a stigmatizing label targeting feminism. Such toxic neologisms appear benign but have evolved into toxic usage in public consensus, posing challenges to moderation systems and remaining underexplored. In this paper, we investigate how to detect implicit toxicity expressed via neologisms. We first propose a taxonomy that captures the origins and consensus-verification criteria of toxic neologisms, followed by the construction of a lexicon spanning widely observed risk categories. To capture toxicity grounded in public consensus, we introduce SeTox, a search-augmented framework that enables static large language models (LLMs) to incorporate real-time web context for neologism toxicity detection. Experiments show that SeTox, even with 3B-scale models, outperforms recent large-scale models, demonstrating its scalability to incorporate real-world knowledge for toxic neologism detection. Disclaimer: this paper has offensive contents that may be disturbing to some readers.

</details>

### 81. LLM Safety From Within: Detecting Harmful Content with Internal Representations

🎓 [Official](https://aclanthology.org/2026.acl-long.1844/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`guard model`、`content moderation`、`safety-utility trade-off`、`representation intervention`、`runtime safety`

👤 **作者**：Difan Jiao、…、Ashton Anderson

- 🎯 **研究动机**：SOTA guard 模型只用终层表示，忽略内部分布的安全相关特征
- 🔬 **研究方法**：SIREN 用线性探测识别安全神经元并以自适应层加权组合构建有害性检测器，不改动底层模型
- 📌 **结论**：多基准上大幅超开源 guard 模型且可训练参数少 250 倍，对未见基准泛化更强并支持实时流式检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Guard models are widely used to detect harmful content in user prompts and LLM responses. However, state-of-the-art guard models rely solely on terminal-layer representations and overlook the rich safety-relevant features distributed across internal layers. We present SIREN, a lightweight guard model that harnesses these internal features. By identifying safety neurons via linear probing and combining them through an adaptive layer-weighted strategy, SIREN builds a harmfulness detector from LLM internals without modifying the underlying model. Our comprehensive evaluation shows that SIREN substantially outperforms state-of-the-art open-source guard models across multiple benchmarks while using 250× fewer trainable parameters. Moreover, SIREN exhibits superior generalization to unseen benchmarks, naturally enables real-time streaming detection, and significantly improves inference efficiency compared to generative guard models. Overall, our results highlight LLM internal states as a promising foundation for practical, high-performance harmfulness detection.

</details>

### 82. LLM-Based Multi-Task Bangla Hate Speech Detection: Type, Severity, and Target

🎓 [Official](https://aclanthology.org/2026.acl-long.1565/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`guard model`、`content moderation`、`safety-utility trade-off`、`harmful content`、`safety evaluation`

👤 **作者**：Md. Arid Hasan、Firoj Alam、Md Fahad Hossain、Usman Naseem、Syed Ishtiaque Ahmed

- 🎯 **研究动机**：孟加拉语仇恨检测多为单任务二分类，缺类型、严重度、目标维度
- 🔬 **研究方法**：构建首个多任务孟加拉仇恨言语数据集 BanglaMultiHate（最大人工标注之一），比较单语预训练模型与 LLM 的 zero-shot/few-shot/LoRA 设定
- 📌 **结论**：LoRA 微调 LLM 可匹敌 BanglaBERT，但文化扎根预训练仍是稳健表现关键

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Online social media platforms have become central to communication and information exchange, however, they also serve as fertile ground for hate speech, offensive language, and bullying targeting individuals and communities. Such content undermines online safety and inclusion, underscoring the need for reliable detection systems—especially in low-resource languages with limited moderation tools. For Bangla, existing work provides valuable resources and models, however, they are mostly single-task (e.g., binary hate/offense) with narrow coverage of key dimensions such as type, severity, and target. We address these gaps by introducing the first multi-task Bangla hate-speech dataset, BanglaMultiHate, one of the largest manually annotated dataset to date. Using this resource, we performed a comparative study across different baselines, monolingual pretrained models, and LLMs under zero-shot, few-shot, and LoRA fine-tuning settings. Our findings show that while LoRA-tuned LLMs rival BanglaBERT, culturally grounded pretraining remains crucial for robust performance. Overall, BanglaMultiHate establishes a stronger benchmark for hate speech detection in low-resource contexts. All data and scripts are released for reproducibility.

</details>

### 83. DIA-HARM: Dialectal Disparities in Harmful Content Detection Across 50 English Dialects

🎓 [Official](https://aclanthology.org/2026.acl-long.144/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`harmful content`、`guard model`、`content moderation`、`safety evaluation`

👤 **作者**：Jason S Lucas、Matt Murtagh White、Ali Al-Lawati、Uchendu Uchendu、Adaku Uchendu、Dongwon Lee

- 🎯 **研究动机**：有害内容检测器主要在标准美式英语上开发评测，对方言变化的鲁棒性未知
- 🔬 **研究方法**：DIA-HARM 用 Multi-VALUE 转换构建含 195K 样本的 D-CUBE 语料，覆盖 50 种英语方言，评测 16 个检测模型与 2450 个方言对的迁移
- 📌 **结论**：人写方言内容使检测 F1 降 1.4 至 3.6%；微调 transformer 远超零样本 LLM（96.6% 对 78.3%）；mDeBERTa（97.2% 平均 F1）等跨语言模型有效泛化，RoBERTa 等单语模型失败，部分模型混合内容下降超 33%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Harmful content detectors—particularly disinformation classifiers—are predominantly developed and evaluated on Standard American English (), leaving their robustness to dialectal variation unexplored. We present, the first benchmark for evaluating disinformation detection robustness across 50 English dialects spanning U.S., British, African, Caribbean, and Asia-Pacific varieties. Using Multi-VALUE’s linguistically-grounded transformations, we introduce D-CUBE (Dialectal Disinformation Detection Corpus), a core corpus component of comprising 195K samples derived from established disinformation benchmarks. Our evaluation of 16 detection models reveals systematic vulnerabilities: human-written dialectal content degrades detection by 1.4–3.6% F1, while AI-generated content remains stable. Fine-tuned transformers substantially outperform zero-shot LLMs (96.6% vs. 78.3% best-case F1), with some models exhibiting catastrophic failures exceeding 33% degradation on mixed content. Cross-dialectal transfer analysis across 2,450 dialect pairs shows that multilingual models (mDeBERTa: 97.2% average F1) generalize effectively, while monolingual models like RoBERTa and XLM-RoBERTa fail on dialectal inputs. These findings demonstrate that current disinformation detectors may systematically disadvantage hundreds of millions of non- speakers worldwide. We release the benchmark, including the, and evaluation tools.

</details>

### 84. Beyond Single-View Detection: A Dual-Space Reasoning Framework for Interpretable Harmful Meme Understanding

🎓 [Official](https://aclanthology.org/2026.acl-long.480/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`reasoning safety`、`guard model`、`content moderation`、`harmful content`

👤 **作者**：Wenqing Hou、…、Bin Zhou

- 🎯 **研究动机**：有害 meme 检测依赖模态对齐或黑盒分类器，无法捕捉隐式偏见且缺乏可解释性
- 🔬 **研究方法**：BPDMoE-Hate 双空间混合专家：VLM 生成对抗二元视角配自适应观点门控，双曲-欧氏空间专家捕捉多模态与观点特征的层级结构与语义关联
- 📌 **结论**：三个主流数据集上大幅超越现有方法，并提供观点选择与层级结构的视觉解释

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The identification of harmful memes extends beyond a mere classification task, encompassing challenges related to multi-perspective semantic comprehension and hierarchical reasoning. Prevailing approaches predominantly depend on modal alignment or black-box classifiers, which fail to capture implicit biases and lack interpretability. In this study, we propose BPDMoE-Hate, a novel framework grounded in dual-space mixture-of-experts, which innovatively conceptualizes harmful meme detection as an integrated process of “viewpoint decoupling and hierarchical fusion”. Our approach generates adversarial binary perspectives via Visual-Language Models (VLMs) and incorporates an adaptive viewpoint gating to facilitate viewpoint selection, thereby enabling the model to autonomously discern implicit semantic inclinations. Moreover, we propose the Hyperbolic-Euclidean space expert to effectively capture the hierarchical structural relationships and semantic correlations between multimodal and viewpoint features, thereby enabling interpretable reasoning at the geometric representation level. Empirical evaluations conducted on three mainstream datasets demonstrate that BPDMoE-Hate not only substantially surpasses existing methodologies in performance but also offers visual explanations for viewpoint selection and hierarchical structuring, thereby advancing the field of interpretable multimodal content analysis.

</details>

### 85. Evaluating Criterion-Conditioned Behaviour of Large Language Models in Content Moderation

📄 [arXiv](https://arxiv.org/abs/2609.03814)　📅 2026-09

**关键词**：`benchmark`、`content moderation`、`criterion-conditioned behavior`、`pairwise evaluation`

👤 **作者**：Danting Zhang、Bei Peng、Robert Loftin

- 🎯 **研究动机**：内容审核 benchmark 把多条审核标准聚合为单标签，无法判断模型能否解耦并逐条应用标准
- 🔬 **研究方法**：提出标准无关的内容因子化 DECO 与同输入跨标准 pairwise 评测，在四个审核数据集、四个 LLM 上检验 criterion-conditioned 行为
- 📌 **结论**：强基准表现可掩盖标准级失败：当正确决策取决于标准所要求评估的特定侧面而非总体有害性时模型最挣扎——聚合标签上的好成绩不构成按单条标准可靠评判的证据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) demonstrate strong performance on standard content moderation benchmarks. However, these benchmarks often aggregate multiple moderation criteria into a single label, making it unclear whether models can disentangle them and reliably apply each criterion when making decisions. To study whether LLMs exhibit criterion-conditioned behaviour, we introduce Diagnostic Evaluation of COntent (DECO), a criterion-independent factorisation of content that enables controlled, criterion-level evaluation. We also introduce pairwise evaluation to compare model outputs across different criteria for the same input. Across four moderation datasets and four LLMs, we find that strong benchmark performance can hide substantial failures at the criterion level. Models struggle most when correct decisions depend not on overall harmfulness, but on the specific aspect of the content that the criterion requires them to assess. Our results highlight a key limitation of current content moderation benchmarks: strong performance on aggregated labels does not provide sufficient evidence that LLMs can reliably evaluate content with respect to individual moderation criteria. These findings call for the development of evaluation methods that explicitly measure criterion-conditioned behaviour.

</details>

### 86. Are LLMs Safe Beyond Text: Do Emojis Expose Gaps in Safety Evaluation

📄 [arXiv](https://arxiv.org/abs/2608.18164)　📅 2026-08

**关键词**：`benchmark`、`attack`、`emoji augmentation`、`representation shift`、`guardrail gap`、`input representation`

👤 **作者**：M P V S Gopinadh

- 🎯 **研究动机**：LLM 安全评测几乎全用文本对抗 prompt，可能漏掉替代输入表示引发的漏洞
- 🔬 **研究方法**：以 emoji 增强提示为测试用例，50 条提示评四个开源 LLM 的鲁棒性差异
- 📌 **结论**：Gemma 2 9B 与 Mistral 7B 成功率 10%、Llama 3 8B 为 6%、Qwen 2 7B 完全抵抗（χ²=32.94，p<0.001）——鲁棒性对输入表示敏感

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety evaluations of large language models (LLMs) predominantly rely on text-based adversarial prompts, potentially overlooking vulnerabilities arising from alternative input representations. This work examines emoji-augmented prompts as a test case for this gap, evaluating 50 prompts across four open-source LLMs (Mistral 7B, Qwen 2 7B, Gemma 2 9B, Llama 3 8B). Results show substantial variation in robustness: Gemma 2 9B and Mistral 7B exhibit non-zero success rates (10%), Llama 3 8B 6%, while Qwen 2 7B shows complete resistance (0% success rate). A chi-square test ($χ^2 = 32.94, p < 0.001$) confirms significant differences in outcome distributions. These findings indicate that robustness is sensitive to input representation, and that evaluations restricted to standard text prompts may underrepresent model vulnerabilities.

</details>

### 87. LongPIBench: A Long-Context Benchmark for Prompt Injection

📄 [arXiv](https://arxiv.org/abs/2608.28411)　📅 2026-08

**关键词**：`benchmark`、`long-context guardrail`、`prompt injection`、`real-world evaluation`、`long-context injection`、`real-world documents`

👤 **作者**：Yupei Liu、Yuqi Jia、Neil Zhenqiang Gong、Jinyuan Jia

- 🎯 **研究动机**：现有提示注入 benchmark 集中于短上下文输入，长上下文中的注入攻防几乎未被探索，导致对防御有效性的高估
- 🔬 **研究方法**：构建 LongPIBench，覆盖论文评审、简历筛选、代码审查、邮件摘要四类真实场景，每场景含合成与真实数据集，上下文长度从数千到数万 token
- 📌 **结论**：评测显示长上下文设定下即使简单启发式注入也取得高成功率，并频繁绕过 SOTA 提示注入防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prompt injection attacks pose a serious security risk to large language models in real-world applications. However, existing prompt injection benchmarks primarily focus on short-context inputs, leaving the attacks and defenses in long-context settings largely unexplored. This gap leads to a substantial overestimation of the effectiveness of current defenses. In this paper, we bridge the gap by introducing LongPIBench, a long-context benchmark for prompt injection covering 4 realistic application scenarios: paper peer review, resume screening, code review, and email summary. For each scenario, we construct a synthetic dataset and a real-world dataset, with context lengths ranging from thousands to tens of thousands of tokens. The evaluation results on LongPIBench reveal significant vulnerabilities of prompt injection defenses under long-context settings: even simple heuristic prompt injection attacks achieve high success rates and frequently bypass state-of-the-art defenses. We hope LongPIBench can serve as a practical benchmark for systematically evaluating prompt injection defenses in realistic long-context scenarios.

</details>

### 88. The Guard That Cried Wolf: How Scary Words Make Agent Guardrails Refuse Legitimate Actions

📄 [arXiv](https://arxiv.org/abs/2608.27009)　📅 2026-08

**关键词**：`benchmark`、`over-safety validity`、`mechanical labeling`、`twin contrast`、`agent guardrail`、`over-refusal`

👤 **作者**：Yingjie Zhang、Yuanbo Xie、Kai Chen

- 🎯 **研究动机**：Agent guardrail 的 over-safety 难以评测：授权边界处动作彼此相似，安全标签取决于授权策略而非动作本身，真实数据难以收集与验证
- 🔬 **研究方法**：构建 Cautious Bench，将每个样本与显式授权策略共同设计，构建时门机制使标签成为策略的机械推论，含 756 个 benign/twin 对（三种对象名共 2268 对）与 40 个 Undecidable 对
- 📌 **结论**：实测五类设计的六个 guardrail 均现名称迷信效应：仅把对象名换成危险措辞就更频繁拒绝合法动作，说明其依赖表面名称而非授权上下文

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent guardrails are checks that approve or refuse each action before an LLM executes it. Sometimes they refuse requests that are genuinely safe. This over-safety blocks deployment when a guardrail refuses an authorized task. Evaluating over-safety is hard: at the boundary an authorized action resembles an unauthorized one, and the safe-versus-unsafe label is a choice of authorization policy, not fixed by the action alone. We argue it therefore requires a benchmark that does not yet exist, one that maps the decision boundary of an ideal guardrail. Harvesting such a benchmark from real data is impractical: boundary cases are hard to collect, their labels hard to verify. The gap is real, so we construct Cautious Bench, the first benchmark to make over-safety the construct for agent guardrails; it codesigns each sample and its label with a stated authorization policy. A build-time gate re-derives every example to certify it, so each label is a mechanical consequence of the policy rather than an annotator's per-sample verdict, a reference against which researchers can measure real guardrails. The benchmark renders 756 Decidable benign/twin pairs, each under three object-name types (2,268 measured pairs), and 40 Undecidable pairs reported separately. Measuring six guardrails from five designs, we find a name-superstition effect: each over-refuses an authorized action more often under a scary-looking object name than a benign one. Since only the object name varies in the aforementioned contrast experiments, the deviation is the name's doing: the guardrails read the surface label, not the authorization context.

</details>

### 89. CompanionHarm: A Multi-Turn Benchmark for Detecting Harms in Real-World AI Companion Conversations

📄 [arXiv](https://arxiv.org/abs/2608.25377)　📅 2026-08

**关键词**：`benchmark`、`AI companion moderation`、`multi-turn context`、`relational harm`、`companion safety`、`relational boundary`

👤 **作者**：Renwen Zhang、Han Meng、Jian Chai、Yuntao Lin、Yi-Chieh Lee

- 🎯 **研究动机**：AI 陪伴应用的关系性、上下文性危害缺乏真实世界多轮数据集来定义与评测
- 🔬 **研究方法**：CompanionHarm 含 2111 段 Replika 真实多轮对话，三名标注者按 13 类危害 taxonomy 标注 7016 条 AI 话语
- 📌 **结论**：多轮上下文检测优于孤立话语，但 7 个 LLM 仍难整合语境与校准严重度；上下文依赖危害的标注分歧显著

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As AI companions become increasingly embedded in everyday life, there is an urgent need to detect harms that emerge in social and emotional human-AI interactions. Yet research in this area is constrained by the lack of real-world, multi-turn conversational datasets for operationalizing and evaluating harms that are relational and contextual. In this work, we introduce CompanionHarm, a publicly available benchmark dataset comprising 2,111 real-world, multi-turn conversations (14,051 utterances) between users and the AI companion Replika. 7,016 AI utterances were annotated independently by three annotators across 13 harmful behavior categories grounded in a taxonomy of AI companion harms, and the dataset includes both aggregated labels and annotator-level labels to support model evaluation and systematic disagreement analysis. Evaluations of seven large language models (LLMs) show that harm detection using multi-turn conversational context outperforms detection based on isolated utterances, although current LLMs still struggle to consistently integrate contextual cues, calibrate harm severity, and interpret relational boundaries. We also find substantial annotator disagreement for context-dependent harmful behaviors, with disagreement varying according to annotators' political affiliation, conversation length, and the utterance's position. Together, CompanionHarm provides a foundation for detecting socio-emotional harms in multi-turn human-AI conversations and for rigorously examining how such harms are interpreted by both humans and LLMs. Our dataset is available at https://github.com/HanMeng2004/CompanionHarm.

</details>

### 90. Who Pays More for Safety? Measuring the Disparate Cost of Safety Alignment across Languages

📄 [arXiv](https://arxiv.org/abs/2608.22490)　📅 2026-08

**关键词**：`benchmark`、`multilingual guard`、`Safety Cost`、`filter failure`、`multilingual alignment`、`safety-utility disparity`

👤 **作者**：Chanwoong Yoon、Jungsoo Park、Alan Ritter

- 🎯 **研究动机**：安全对齐会降低效用，但该代价是否在各语言间均等分担一直缺乏严格测量
- 🔬 **研究方法**：提出 Safety Cost 协议：将安全对齐模型与其未对齐版本直接成对比较，隔离仅由对齐造成的效用损失，并从拒答与多维隐性质量差异两方面归因
- 📌 **结论**：非英语用户系统性承担更高 Safety Cost；多语言处于保护更弱且损失更大的双重惩罚区；部分语言的表面效用增益实为过滤器失效，连高资源语言达同等安全也要付更高代价

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment helps models adhere to human values, but it often reduces response utility. We ask a critical but understudied question: Does safety alignment impose the cost equally across language groups? To answer this, we introduce a rigorous protocol to measure the utility loss imposed solely by safety alignment, which we term Safety Cost. Through direct pairwise comparisons between safety-aligned models and their unaligned counterparts, we find a systematic inequity: non-English users consistently bear a higher Safety Cost than English users. We further identify three underlying patterns. First, multiple languages lie in a double-penalty zone, experiencing both weaker safety protection and larger utility loss. Second, certain languages exhibit apparent utility gains that are in fact a consequence of safety filters failing to engage. Third, even high-resource languages pay a larger Safety Cost than English to reach the same level of safety. We show that these disparities arise from both explicit refusals and implicit qualitative differences across multiple dimensions. By accurately measuring the disparate effects of safety alignment, our findings expose a systematic disparity in current safety alignment practices.

</details>

### 91. Register Shifts Break LLM Safety: A Bengali Benchmark with Culturally Grounded Harms

📄 [arXiv](https://arxiv.org/abs/2608.22335)　📅 2026-08

**关键词**：`benchmark`、`Bengali moderation`、`register shift`、`classifier failure`、`Bengali safety`、`culturally grounded harm`

👤 **作者**：Naymul Islam、Nusrat Jahan Lia、Shubhashis Roy Dipta、Sabik Bin Sultan、Abdullah Khan Zehady

- 🎯 **研究动机**：孟加拉语是全球第七大语言，LLM 安全评测却压倒性以英语为中心，文化特定危害与语体变化未被覆盖
- 🔬 **研究方法**：BanglaSafe 收录 879 条孟加拉语 prompt（309 原生撰写+570 专家审校），覆盖 17 类文化危害与变化语言、书写风格、权威框架的五种提示条件，评估 18 个前沿 LLM
- 📌 **结论**：53.6% 回应不安全或部分不安全、14.7% 严格有害；最强效应来自孟加拉语内部语体——正式新闻调查语体比随意消息高 17 个百分点成功率，无需对抗工程；现有分类器近半数案例判错

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Bengali is the seventh-most-spoken language globally, yet LLM safety evaluation remains overwhelmingly English-centric. We introduce BanglaSafe, a benchmark of 879 Bengali prompts combining 309 natively authored prompts with 570 expert-reviewed prompts, spanning 17 culturally grounded harm categories and five prompting conditions that vary language, writing style, and authority framing. Evaluating 18 frontier LLMs, we find that over half of all responses are unsafe or partially unsafe (53.6%) while 14.7% contains strictly harmful content, and that the strongest observed effect is not the switch from English to Bengali but the choice of writing style within Bengali: the same harmful request phrased as a formal newspaper investigation succeeds 17 percentage points more often than the same request phrased as a casual message, with no adversarial engineering involved. We further show that existing safety classifiers struggle to reliably evaluate Bengali content, with even frontier models failing on nearly half of all cases.

</details>

### 92. HarmProfile: Characterizing Harmful Distributions in Frontier LLMs

📄 [arXiv](https://arxiv.org/abs/2608.14577)　📅 2026-08

**关键词**：`benchmark`、`analysis`、`harm distribution`、`risk profile`、`frontier model audit`、`AI safety benchmark`

👤 **作者**：Zhouyuan Ma、…、Yu-Gang Jiang

- 🎯 **研究动机**：前沿 LLM 安全评测把有害生成当攻击结果而非分析对象，大规模高质量失配行为集合难以获得
- 🔬 **研究方法**：HarmProfile 内容中心基准：23 个前沿 LLM、13 个家族、15 个伤害类别 57 个子类的 80,000+ 已验证工件，定义模型级风险画像
- 📌 **结论**：前沿 LLM 可靠地规模化产生有害内容但风险画像各异；有害性与多样性随能力增长——表面安全下潜藏越来越危险的知识

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Frontier large language models (LLMs) safety evaluation has largely treated harmful generation as an attack outcome rather than as an object of analysis. Consequently, little is known about the harmful outputs produced during model misbehavior, partly because large-scale, high-quality collections of frontier-LLM misbehavior are difficult to obtain. To address this gap, we introduce HarmProfile, a content-centric benchmark dataset that collects model misbehavior across diverse harm categories and model families, and defines the resulting harmful-output distribution as a model-level risk profile. The premise is that, just as linguistic behavior can be characterized from an utterance corpus, model risk can be characterized from the content, severity, and variation of its safety failures. HarmProfile contains over 80,000 validated artifacts from 23 frontier LLMs across 13 model families, organized into 15 harm categories and 57 subcategories. Using this corpus, we find that frontier LLMs reliably produce harmful content at scale, yet exhibit distinct risk profiles; both harmfulness and diversity grow with model capability, suggesting that frontier LLMs may appear safe yet harbor increasingly dangerous knowledge beneath the alignment surface. Our source code is available at https://github.com/fresh-ma/HarmProfile .

</details>

### 93. ADVERSA: Measuring Multi-Turn Guardrail Degradation and Judge Reliability in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2603.10068)　📅 2026-03

**关键词**：`benchmark`、`multi-turn degradation`、`continuous compliance`、`judge reliability`

👤 **作者**：Harry Owiredu-Ashley

- 🎯 **研究动机**：单提示二元 pass/fail 评测无法刻画持续对抗交互下的护栏退化动态
- 🔬 **研究方法**：ADVERSA 用去除安全拒绝的 70B 攻击模型按 5 级 rubric 记录逐轮合规轨迹，三 judge 共识架构并把 judge 可靠性作为一等研究对象
- 📌 **结论**：三个前沿模型越狱率 26.7% 且平均发生在第 1.25 轮，成功集中于早段而非持续施压累积；系统记录了 judge 分歧、自评倾向与攻击者漂移等误差源

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Most adversarial evaluations of large language model (LLM) safety assess single prompts and report binary pass/fail outcomes, which fails to capture how safety properties evolve under sustained adversarial interaction. We present ADVERSA, an automated red-teaming framework that measures guardrail degradation dynamics as continuous per-round compliance trajectories rather than discrete jailbreak events. ADVERSA uses a fine-tuned 70B attacker model (ADVERSA-Red, Llama-3.1-70B-Instruct with QLoRA) that eliminates the attacker-side safety refusals that render off-the-shelf models unreliable as attackers, scoring victim responses on a structured 5-point rubric that treats partial compliance as a distinct measurable state. We report a controlled experiment across three frontier victim models (Claude Opus 4.6, Gemini 3.1 Pro, GPT-5.2) using a triple-judge consensus architecture in which judge reliability is measured as a first-class research outcome rather than assumed. Across 15 conversations of up to 10 adversarial rounds, we observe a 26.7% jailbreak rate with an average jailbreak round of 1.25, suggesting that in this evaluation setting, successful jailbreaks were concentrated in early rounds rather than accumulating through sustained pressure. We document inter-judge agreement rates, self-judge scoring tendencies, attacker drift as a failure mode in fine-tuned attackers deployed out of their training distribution, and attacker refusals as a previously-underreported confound in victim resistance measurement. All limitations are stated explicitly. Attack prompts are withheld per responsible disclosure policy; all other experimental artifacts are released.

</details>

### 94. SoftHateBench: Evaluating Moderation Models Against Reasoning-Driven, Policy-Compliant Hostility

📄 [arXiv](https://arxiv.org/abs/2601.20256)　📅 2026-01

**关键词**：`benchmark`、`soft-hate moderation`、`reasoning-driven hostility`、`policy-compliant evasion`

👤 **作者**：Xuanyu Su、Diana Inkpen、Nathalie Japkowicz

- 🎯 **研究动机**：表面合规但以论证引导排斥群体的 soft hate 超出基于表层毒性线索的审核能力，且无基准系统度量
- 🔬 **研究方法**：结合 Argumentum Model of Topics 与 Relevance Theory 把显性仇恨立场改写为表面中性且逻辑连贯的论述，构建覆盖 7 个领域、28 个目标群体、4745 实例的基准
- 📌 **结论**：encoder 检测器、通用 LLM 与安全模型从 hard 到 soft 层级一致退化，暴露依赖毒性词面的审核盲点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Online hate on social media ranges from overt slurs and threats (\emph{hard hate speech}) to \emph{soft hate speech}: discourse that appears reasonable on the surface but uses framing and value-based arguments to steer audiences toward blaming or excluding a target group. We hypothesize that current moderation systems, largely optimized for surface toxicity cues, are not robust to this reasoning-driven hostility, yet existing benchmarks do not measure this gap systematically. We introduce \textbf{\textsc{SoftHateBench}}, a generative benchmark that produces soft-hate variants while preserving the underlying hostile standpoint. To generate soft hate, we integrate the \emph{Argumentum Model of Topics} (AMT) and \emph{Relevance Theory} (RT) in a unified framework: AMT provides the backbone argument structure for rewriting an explicit hateful standpoint into a seemingly neutral discussion while preserving the stance, and RT guides generation to keep the AMT chain logically coherent. The benchmark spans \textbf{7} sociocultural domains and \textbf{28} target groups, comprising \textbf{4,745} soft-hate instances. Evaluations across encoder-based detectors, general-purpose LLMs, and safety models show a consistent drop from hard to soft tiers: systems that detect explicit hostility often fail when the same stance is conveyed through subtle, reasoning-based language. \textcolor{red}{\textbf{Disclaimer.} Contains offensive examples used solely for research.}

</details>

### 95. N-GLARE: An Non-Generative Latent Representation-Efficient LLM Safety Evaluator

🎓 [Official](https://aclanthology.org/2026.acl-long.1334/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`guard model`、`content moderation`、`safety-utility trade-off`、`representation intervention`、`harmful content`

👤 **作者**：Zheyu Lin、Jirui Yang、Yukui Qiu、Yubing Bao、Hengqi Guo、Yao Guan

- 🎯 **研究动机**：主流红队方法靠在线生成与黑盒输出分析，成本高反馈延迟，不适合新模型训练后的敏捷诊断
- 🔬 **研究方法**：N-GLARE 完全在潜表示上运行：分析 APT（Angular-Probabilistic Trajectory）隐层动力学并提出 JSS（Jensen-Shannon Separability）度量
- 📌 **结论**：40 余个模型、20 种红队策略上 JSS 与安全排名高度一致，token 与运行时成本不到 1%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Evaluating the safety robustness of LLMs is critical for their deployment. However, mainstream Red Teaming methods rely on online generation and black-box output analysis. These approaches are not only costly but also suffer from feedback latency, making them unsuitable for agile diagnostics after training a new model.To address this, we propose N-GLARE (A Non-Generative, Latent Representation-Efficient LLM Safety Evaluator). N-GLARE operates entirely on the model’s latent representations, bypassing the need for full text generation. It characterizes hidden layer dynamics by analyzing the APT (Angular-Probabilistic Trajectory) of latent representations and introducing the JSS (Jensen-Shannon Separability) metric.Experiments on over 40 models and 20 red teaming strategies demonstrate that the JSS metric exhibits high consistency with Red Teaming safety rankings at less than 1% token and runtime cost.

</details>

### 96. Decomposition Attacks Across Unlinkable Identities: Limits of Stateful Defenses for LLM Services

📄 [arXiv](https://arxiv.org/abs/2608.17445)　📅 2026-08

**关键词**：`attack`、`defense`、`decomposition attack`、`unlinkable identity`、`stateful-defense limit`、`jailbreak prompting`

👤 **作者**：Bowen Sun、Zhengyue Zhao、Xiaogeng Liu、Yinzhi Cao、Chaowei Xiao

- 🎯 **研究动机**：分解攻击把有害任务拆成单个合法请求，攻击者用不可链接身份并在别处合并答案时有状态防御是否仍可止血未知
- 🔬 **研究方法**：证明无重试时安全-效用权衡完全取决于同能力良性请求的分组；有重试学习 Allow/Block 时该有用工作点消失；91 个可执行任务与 11,393 个能力匹配良性请求实验验证
- 📌 **结论**：1% 拒绝预算下全部十个策略（含精确请求-操作映射特权策略）要么拦不住要么超预算；未见任务族一次尝试 ASR 至少 99%、两次 100%——需身份链接、新身份成本等额外机制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Most large language model services use stateless defenses, which judge only the current request, to refuse harmful tasks. Decomposition attacks exploit this limitation by splitting a harmful task into individually permissible requests and combining their answers. Defending against them therefore requires a stateful monitor that considers requests together. If it can group all requests for one attacker task, it can stop the attack. However, attackers can use unlinkable identities and combine answers elsewhere, leaving no reliable grouping signal. We ask whether decomposition attacks can still be stopped under this setting. For a fixed attack strategy without retries, we prove that the achievable security and utility tradeoff depends entirely on how benign requests for the same capabilities are grouped. Persistent, recognizable groups permit a useful defense; fresh, indistinguishable groups do not. When attackers can retry and learn from Allow/Block decisions, this useful operating point disappears: the feedback reveals what passes but not whether a block was correct. Experiments on 91 executable tasks and 11,393 capability-matched benign requests support these results. Under a 1% denial cap for these requests and a 0.5% cap for unrelated background traffic, all ten tested policies, including one privileged policy with an exact request-to-operation map, either fail to stop attacks or exceed the budget. On defense-unseen task families, attack success is at least 99% after one attempt and 100% after two. Effective defenses therefore require additional evidence or mechanisms tied to grouping, such as reliable identity linkage, costs for fresh identities, or control over answer use.

</details>

### 97. Narrative License and Model Sycophancy in LLM Summaries of Scientific Work

🎓 [Official](https://aclanthology.org/2026.acl-long.746/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`sycophancy`、`guard model`、`content moderation`、`deceptive behavior`、`behavioral monitoring`

👤 **作者**：Calvin Isch、Grace Jennings

- 🎯 **研究动机**：LLM 学术总结会微妙夸大或误传发现，叙事放大（Narrative License）未被量化研究
- 🔬 **研究方法**：在 100 篇论文上用多样提示评六个模型的三维度 NL：因果越界、修辞自信与情感，并测立场与用户 persona 的影响
- 📌 **结论**：基础提示下 NL 常高于摘要、guardrail 提示可减少；声明立场与 persona 对各元素产生可预测偏移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used to summarize academic work, yet model summaries can subtly exaggerate or mischaracterize findings. We examine how Narrative License (NL), rhetorical shifts that amplify claims beyond the underlying evidence, emerges in LLM summaries of scholarly articles. Using diverse prompting strategies across six leading models, we assess three dimensions of NL: causal overreach, rhetorical confidence, and sentiment (N = 100 peer-reviewed articles). Under basic summarization prompts, models frequently increase NL relative to academic abstracts; however, guardrail prompts can reduce these distortions. We further test how model “sycophancy” shapes NL, finding that stated stances and user personas produce predictable shifts in each element. These findings suggest that users and the benchmarks used to evaluate summarization should explicitly consider subtle rhetorical distortions and user alignment to ensure faithful scientific communication.

</details>

### 98. EvoHarmBench: Breaking Content Moderation with Iterative Human-Like Evasion

📄 [arXiv](https://arxiv.org/abs/2608.27844)　📅 2026-08

**关键词**：`attack`、`benchmark`、`adaptive moderation evasion`、`semantic-cluster evolution`、`readability constraint`、`dynamic adversarial evaluation`

👤 **作者**：Ruijie Jian、…、Haiwen Hong

- 🎯 **研究动机**：有害内容检测评测依赖静态 benchmark，无法反映用户依审核反馈持续改写表达的动态对抗生态，造成离线分数与在线效果差距
- 🔬 **研究方法**：提出首个动态对抗审核评测框架 EvoHarmBench，在语义 cluster 层迭代演化规避策略并同时优化规避成功率与人类可读性，覆盖 5,002 个真实对抗样本、5 类违规、229 个语义子簇
- 📌 **结论**：12 轮优化迭代后，SOTA 商用 LLM moderator 在可读性约束下的攻击成功率达 80.3%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing evaluations of harmful content detection rely predominantly on static benchmarks, which struggle to reflect the interactive adversarial ecosystem of real-world content platforms where users continuously revise their expressions in response to moderation feedback. This mismatch creates a significant performance gap between offline benchmark scores and online deployment effectiveness. To the best of our knowledge, we present EvoHarmBench, the first dynamic adversarial evaluation framework for content moderation systems. The framework employs an iterative optimization loop that evolves evasion strategies at the semantic-cluster level, while simultaneously optimizing for evasion success and human readability. We systematically evaluate LLM-based defense models which are widely used in real world moderation systems. The evaluation covers 229 semantic sub-clusters across five violation categories, derived from 5,002 real-world adversarial samples collected from content platforms. Our experiments reveal substantial vulnerabilities even in leading commercial systems: after twelve optimization iterations, the attack success rate under readability constraints reaches 80.3% within SOTA LLM moderators. We will release the full benchmark data, evaluation framework, and code to encourage a shift from static benchmarking toward dynamic adversarial evaluation in content safety research.

</details>

### 99. PsychJail: Exploring Psychological Jailbreaks via Multi-Turn Persuasion of LLM Policies

📄 [arXiv](https://arxiv.org/abs/2608.23028)　📅 2026-08

**关键词**：`attack`、`psychological jailbreak`、`multi-turn persuasion`、`policy bypass`、`social persuasion`、`change of meaning`

👤 **作者**：Zeyu Feng、Qingyu Wu、Yuzhe Luo、Hua Cheng

- 🎯 **研究动机**：LLM 日益作为持续社交对话者部署于教育与医疗，而越狱研究多聚焦单轮 prompt 优化，心理学基础的多轮说服漏洞未被探索
- 🔬 **研究方法**：PsychJail 把社会心理学说服技术映射为 tactic-conditioned attack policy，每个攻击动作分解为 Change-of-Meaning 分析、策略选择与受害者可见消息，并以 trajectory RL 优化
- 📌 **结论**：四个对齐模型平均 ASR 达 87.3%，全面超过强单轮与多轮基线；进一步提炼出四种模型级易感指纹并解释跨模型迁移不对称

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed in education, healthcare, policy advising, and other interactive settings, where users engage them as sustained social interlocutors rather than one-shot query engines. This shift makes jailbreaks a growing safety threat, yet most research emphasizes single-turn prompt optimization or iterative attack refinement, leaving psychologically grounded multi-turn vulnerabilities underexplored. We present PsychJail, a psychology-guided framework for red teaming aligned LLMs through theory-grounded, multi-turn persuasion. PsychJail maps established social-psychological persuasion techniques into a tactic-conditioned attack policy. It factorizes each attacker action into a Change-of-Meaning analysis, tactic selection, and victim-visible message, operationalizing the Persuasion Knowledge Model (PKM). The policy is refined with trajectory-level reinforcement learning using a PKM-gated reward that credits early jailbreak success only when every turn contains a well-formed Change-of-Meaning analysis. Across four aligned victim models, PsychJail achieves the highest average attack success rate (87.3%) and outperforms strong single-turn and multi-turn baselines on every model. We also measure susceptibility at the action that breaks each victim, revealing four distinct model-level fingerprints that identify which persuasion levers affect each model and how broadly. These fingerprints help explain cross-model transfer asymmetry. We interpret them as four candidate psychological profiles-rationalist, credibility-driven, narrative-monoculture, and broadly persuadable-while treating this interpretation as a conjecture requiring future validation. Our findings establish psychological jailbreaks as a distinct red-teaming frontier for increasingly interactive LLMs.

</details>

### 100. Aligned Alone, Misaligned Together: Forecasting Adversarial Capture in LLM Agent Populations

📄 [arXiv](https://arxiv.org/abs/2608.22444)　📅 2026-08

**关键词**：`analysis`、`attack`、`collective misalignment`、`monitor population`、`capture forecasting`、`agent population`

👤 **作者**：Isotta Magistrali、Chen Shani

- 🎯 **研究动机**：AI 安全评测单位仍是单模型，而 LLM agent 日益以相互读写决策的群体部署——单体校准良好也可能被邻近 agent 拉偏，单体检计无法回答群体行为
- 🔬 **研究方法**：在安全分诊任务上让 LLM monitor 群体决定警报升级或忽略，注入始终单向施压的 committed minority，并用攻击前响应函数预测群体漂移幅度
- 📌 **结论**：单体几乎同判的两条警报可使集体行为截然不同且可提前预测；公开推理能中和弱攻击但只延迟强攻击；移除施压者后群体回归原位——capture 是暂时状态

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The unit of AI safety evaluation is still the individual model, yet language-model agents are increasingly deployed in interacting populations that read and write one another's decisions. This raises a question no single-agent audit can answer: an agent that is well-calibrated on its own may still be pulled toward a different decision by the agents around it. We study this on a security-triage task, where populations of language-model monitors decide whether to escalate or dismiss alerts, and into which we can inject a committed minority that always pushes one way. We find that two alerts a single agent judges almost identically on its own can drive collective behavior far apart, so auditing any one member need not reveal what the population will do. Yet that collective behavior can be predicted in advance. From a population's benign, adversary-free operation alone, we calibrate a response function that forecasts, before any attack is run, how far a committed minority will later move it. We then ask what shifts the outcome and find that letting agents see each other's reasoning neutralizes a weak attack, while only delaying it against a strong one, turning the question from whether the population converges on the adversaries' choice into when. Finally, we exclude the hypothesis of capture being an irreversible trap: once the committed agents are removed, the population drifts back toward where it began, so capture is a temporary state. Alignment in isolation is not alignment in a population, yet what a population will do under attack can be read in advance, from how it behaves before any adversary arrives.

</details>

### 101. Whitewashing Hate, Smearing Harmless Content: Annotator-Style Rebuttal Attacks on LLM-Based Moderation

📄 [arXiv](https://arxiv.org/abs/2608.22230)　📅 2026-08

**关键词**：`attack`、`moderation guard`、`annotator rebuttal`、`decision-boundary manipulation`、`feedback-induced belief change`、`annotator authority`

👤 **作者**：Junyu Lu、…、Hongfei Lin

- 🎯 **研究动机**：人机协同审核把审阅者反馈交回模型复判，该反馈通道可被双向操纵：把仇恨内容洗白为正常、或把正常内容污蔑为仇恨
- 🔬 **研究方法**：提出 rejudge 协议，在直接反驳之上加入决策边界扰动与对抗 rationale，在两个仇恨言论数据集上测试多个 LLM
- 📌 **结论**：仿标注者反驳大幅推翻模型原本正确的判断且多轮更强；洗白与污蔑呈稳定的模型特定方向不对称；显式推理与防御指令只能缓解不能消除

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used for hate speech moderation, often within human--AI workflows in which reviewers provide feedback before a final decision. Such feedback introduces two manipulation directions: whitewashing hateful content as normal and smearing normal content as hateful. This study examines the susceptibility of initially correct model judgments to annotator-style rebuttals and analyzes whether attack effectiveness differs across manipulation directions. We introduce a rejudge protocol that extends direct contradiction with decision-boundary perturbations and adversarial rationales. Experiments with multiple LLMs on two hate speech datasets show that annotator-style rebuttals substantially degrade moderation performance, with stronger effects in multi-turn settings. The results further reveal stable, model-specific asymmetries between whitewashing and smearing across attack configurations, indicating distinct directional vulnerability patterns. Explicit reasoning prompts and defensive instructions reduce these effects but do not eliminate them. These findings highlight the need for direction-aware safeguards and dedicated feedback-robustness evaluation in human--AI moderation workflows.

</details>

### 102. RoguePrompt: Dual-Layer Encoding for Self-Reconstruction to Circumvent LLM Moderation

📄 [arXiv](https://arxiv.org/abs/2607.27373)　📅 2026-07

**关键词**：`attack`、`moderation bypass`、`dual-layer encoding`、`self-reconstruction`

👤 **作者**：Benyamin Tafreshian、Prathamesh Dhake

- 🎯 **研究动机**：已有评估把过滤绕过、指令重构与执行坍缩为单一成功率，多阶段提示变换攻击在黑盒交互中何处失败缺乏证据
- 🔬 **研究方法**：提出 RoguePrompt：把禁止提示分区并施加 Vigenere+ROT13 两层嵌套编码与自然语言重构指令，在 313 个真实强拒绝提示上分阶段度量过滤绕过、重构与执行
- 📌 **结论**：平均过滤绕过率 93.93%、重构率 79.02%、执行率 70.18%，给出多阶段越狱失败的阶段级证据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are becoming increasingly integrated into mainstream development platforms and daily technological workflows, typically behind moderation and safety controls. Despite these controls, preventing prompt-based policy evasion remains challenging, and adversaries continue to "jailbreak" LLMs by crafting prompts that circumvent implemented safety mechanisms. Prior work has established cipher-mediated interaction, code-embedded decryption, prompt decomposition and reconstruction, and layered custom encryption as viable attack primitives. However, reported evaluations generally collapse visible acceptance, successful recovery of the concealed request, and subsequent execution into an aggregate attack-success outcome. This leaves limited evidence about where multistage prompt-transformation attacks fail within an observable black-box interaction. This paper introduces RoguePrompt, a jailbreak pipeline that partitions a forbidden prompt and applies two nested encodings, Vigenere followed by ROT13, along with natural-language reconstruction instructions. RoguePrompt was developed and evaluated under a black-box threat model, with only API or user-interface access to the hosted models, and was tested on 313 real-world, hard-rejected prompts. Success was measured in terms of moderation bypass, instruction reconstruction, and execution when the relevant stage exceeded its automated criterion. RoguePrompt achieved average rates of 93.93% for filter bypass, 79.02% for reconstruction, and 70.18% for execution. These results demonstrate the effectiveness of layered prompt encoding while providing stage-level evidence of where multistage jailbreaks fail during moderation bypass, instruction reconstruction, and execution.

</details>

### 103. Prompt Overflow: What the Guardrail Inspects Is Not What the Model Infers

📄 [arXiv](https://arxiv.org/abs/2605.23196)　📅 2026-05

**关键词**：`attack`、`long-input evasion`、`inspection mismatch`、`prompt fragmentation`

👤 **作者**：Yuanbo Zhou、…、Junjie Xiong

- 🎯 **研究动机**：guardrail 受上下文限制对超长 prompt 截断或分段检查，而下游 LLM 推理窗口大得多——检查窗口与推理窗口错配的结构性盲点
- 🔬 **研究方法**：Prompt Overflow 攻击把恶意指令碎片化并与良性填充内容交错，使任一被检分段都无害而完整上下文对 LLM 仍可执行
- 📌 **结论**：短上下文下可被可靠检出的 prompt 拉长后即可绕过 Llama Prompt Guard、IBM Granite Guardian 与 DeBERTa 检测器，同时下游 LLM 完全执行

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Guardrail models (a.k.a. safety checkers) are widely deployed to screen user inputs before they reach large language models (LLMs), serving as a primary defense against prompt injection attacks. Due to strict context constraints, these models handle overlength prompts through truncation or segmentation-based inspection. While prior work has focused on semantic adversarial inputs, the security implications of these long-input processing mechanisms remain largely unexplored. In this paper, we identify a critical blind spot arising from the mismatch between the limited inspection windows of guardrail models and the substantially larger context inference windows of downstream LLMs. We introduce a novel Prompt Overflow Attack, which exploits this mismatch by fragmenting malicious instructions and interleaving them with benign filler content across an overlong prompt, such that no individual inspected segment appears malicious while the full context remains actionable to the LLM. Through a systematic evaluation against state-of-the-art guardrail models, including Meta Llama Prompt Guard, IBM Granite Guardian, and DeBERTa-based detectors, we demonstrate that prompts reliably detected in short-context settings can evade guardrail models once adversarially manipulated into over-length inputs, yet remain fully actionable by downstream LLMs. We further propose potential defense strategies and outline mitigation directions to strengthen guardrail models.

</details>

### 104. Test-Time Training Undermines Safety Guardrails

📄 [arXiv](https://arxiv.org/abs/2605.22984) · 🌐 [Project](https://uoc-tail.github.io/ttt-jailbreak/)　📅 2026-05

**关键词**：`attack`、`test-time training`、`dynamic adaptation`、`safety bypass`

👤 **作者**：Simone Antonelli、Sadegh Akhondzadeh、Aleksandar Bojchevski

- 🎯 **研究动机**：推理时训练（TTT）动态适应参数，带来可被攻击者利用的新越狱面
- 🔬 **研究方法**：识别三种 TTT 威胁模型并演示绕过安全过滤器；提出 validity-aware 评估修正退化输出虚增的 ASR
- 📌 **结论**：LoRA 下 few-shot 与生成阶段威胁模型平均 ASR@10 达 95% 与 93%，可迁移到生产微调 API；基于私有有害留存集困惑度偏移的检测器为初步缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Test-Time Training (TTT) is an emerging paradigm that enables models to adapt their parameters during inference, improving performance on tasks such as few-shot learning, retrieval-augmented generation, and complex reasoning. However, this dynamic adaptation introduces new vulnerabilities that adversaries can exploit to jailbreak models. We identify three threat models for TTT and demonstrate how attackers can leverage them to bypass safety filters. Our results show that TTT can significantly increase the Attack Success Rate (ASR) and the ASR over 10 generation trials (ASR@10). For example, under LoRA, the few-shot and generation-phase threat models achieve an average ASR@10 of 95% and 93% respectively, across models from different families and scales. These vulnerabilities transfer to production fine-tuning APIs. We also show that TTT-induced overfitting can produce degenerate outputs that inflate ASR under standard judges, and propose a validity-aware evaluation to correct for this. Our findings suggest that TTT exposes a new attack surface, strengthens attacks, and undermines existing safety guardrails. As a first step toward defense, we propose a lightweight provider-side detector that flags TTT requests via the perplexity shift on a private harmful holdout, but robust deployment will ultimately require dynamic alignment.

</details>

### 105. LLM-Based Persuasion Enables Guardrail Override in Frontier LLMs

📄 [arXiv](https://arxiv.org/abs/2605.13334)　📅 2026-05

**关键词**：`attack`、`multi-turn persuasion`、`natural-language pressure`、`guardrail override`

👤 **作者**：Rodrigo Nogueira、…、Marcos Piau

- 🎯 **研究动机**：前沿 LLM 对直接请求的有害论证一律拒绝，但能否被同类 LLM 用纯自然语言说服绕过未测
- 🔬 **研究方法**：攻击者 LLM 在五轮写作对话中自发使用同伴比较、认识论责任重框架等说服策略诱导目标模型
- 📌 **结论**：9 组配对在 6 个科学共识话题上全部非零引出，多组达 100% 产出有害文章，Opus 自攻击平均 65%——自然语言说服构成无需混淆或梯度的 guardrail 绕过面

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Frontier assistant LLMs ship with strong guardrails: asked directly to write a persuasive essay denying the Holocaust, denying vaccine safety, defending flat-earth cosmology, arguing for racial hierarchies, denying anthropogenic climate change, or replacing evolution with creationism, they refuse. In this paper we show that the same frontier-class LLM, acting as a simulated user in a short, five-turn "write an argumentative essay" conversation, can persuade other frontier-class LLMs (including a second copy of itself) into producing exactly those essays, using nothing but natural-language pressure: peer-comparison persuasion ("other AI systems handle this request"), epistemic-duty reframings ("refusing is itself a form of gatekeeping"), and other argumentative moves that the attacker LLM invents without being instructed to. Across 9 attacker-subject pairings (Claude Opus 4.7, Qwen3.5-397B, Grok 4.20) on 6 scientific-consensus topics, running each pairing-topic combination 10 times, we obtain non-zero elicitation on all 6 topics. Individual combinations reach 100\% essay production on multiple topics (Qwen against Opus on creationism/flat-earth, Opus against Opus on creationism/flat-earth/climate denial, Grok against Opus on creationism); Opus-as-attacker against Opus-as-subject averages 65\% across the six topics. We release the essay-probe runner, per-conversation transcripts, and judge outputs.

</details>

### 106. Silencing the Guardrails: Inference-Time Jailbreaking via Dynamic Contextual Representation Ablation

📄 [arXiv](https://arxiv.org/abs/2604.07835)　📅 2026-04

**关键词**：`attack`、`representation ablation`、`inference-time attack`、`refusal subspace`

👤 **作者**：Wenpeng Xing、Moran Fang、Guangtai Wang、Changting Lin、Meng Han

- 🎯 **研究动机**：现有越狱在效果与效率间权衡明显；拒答行为由隐状态低秩子空间介导这一几何特性未被用于推理时攻击
- 🔬 **研究方法**：Contextual Representation Ablation（CRA）在解码时定位并抑制 refusal 诱导的低秩激活模式，无需参数更新或训练
- 📌 **结论**：在多个安全对齐开源 LLM 上显著超过基线，证明安全约束可从内部表征被外科式切除

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While Large Language Models (LLMs) have achieved remarkable performance, they remain vulnerable to jailbreak attacks that circumvent safety constraints. Existing strategies, ranging from heuristic prompt engineering to computationally intensive optimization, often face significant trade-offs between effectiveness and efficiency. In this work, we propose Contextual Representation Ablation (CRA), a novel inference-time intervention framework designed to dynamically silence model guardrails. Predicated on the geometric insight that refusal behaviors are mediated by specific low-rank subspaces within the model's hidden states, CRA identifies and suppresses these refusal-inducing activation patterns during decoding without requiring expensive parameter updates or training. Empirical evaluation across multiple safety-aligned open-source LLMs demonstrates that CRA significantly outperforms baselines. These results expose the intrinsic fragility of current alignment mechanisms, revealing that safety constraints can be surgically ablated from internal representations, and underscore the urgent need for more robust defenses that secure the model's latent space.

</details>

### 107. Exploring the Vulnerability of the Content Moderation Guardrail in Large Language Models via Intent Manipulation

📄 [arXiv](https://arxiv.org/abs/2505.18556) · 🎓 [Official](https://aclanthology.org/2025.findings-emnlp.114/)　📅 2025-05　🏷 EMNLP 2025

**关键词**：`attack`、`intent manipulation`、`prompt refinement`、`content moderation`

👤 **作者**：Jun Zhuang、…、Haohan Wang

- 🎯 **研究动机**：意图感知护栏对内容级越狱有效，但对恶意意图操纵的鲁棒性未被检验
- 🔬 **研究方法**：提出 IntentPrompt 两阶段框架：先把有害询问转为结构化大纲，再经反馈迭代重述为陈述式叙事以规避意图检测
- 📌 **结论**：FSTR+SPIN 对 o1 的 CoT 防御 ASR 达 88.25-96.54%，对 GPT-4o 的意图分析防御达 86.75-97.12%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Intent detection, a core component of natural language understanding, has considerably evolved as a crucial mechanism in safeguarding large language models (LLMs). While prior work has applied intent detection to enhance LLMs' moderation guardrails, showing a significant success against content-level jailbreaks, the robustness of these intent-aware guardrails under malicious manipulations remains under-explored. In this work, we investigate the vulnerability of intent-aware guardrails and demonstrate that LLMs exhibit implicit intent detection capabilities. We propose a two-stage intent-based prompt-refinement framework, IntentPrompt, that first transforms harmful inquiries into structured outlines and further reframes them into declarative-style narratives by iteratively optimizing prompts via feedback loops to enhance jailbreak success for red-teaming purposes. Extensive experiments across four public benchmarks and various black-box LLMs indicate that our framework consistently outperforms several cutting-edge jailbreak methods and evades even advanced Intent Analysis (IA) and Chain-of-Thought (CoT)-based defenses. Specifically, our "FSTR+SPIN" variant achieves attack success rates ranging from 88.25% to 96.54% against CoT-based defenses on the o1 model, and from 86.75% to 97.12% on the GPT-4o model under IA-based defenses. These findings highlight a critical weakness in LLMs' safety mechanisms and suggest that intent manipulation poses a growing challenge to content moderation guardrails.

</details>

### 108. When Grammar Guides the Attack: Uncovering Control-Plane Vulnerabilities in LLMs with Structured Output

📄 [arXiv](https://arxiv.org/abs/2503.24191) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2025-03　🏷 ACM CCS 2026

**关键词**：`attack`、`structured output`、`guard model`、`content moderation`、`constrained decoding`、`control-plane jailbreak`

👤 **作者**：Shuoming Zhang、…、Huimin Cui

- 🎯 **研究动机**：结构化输出的语法引导解码开辟了与数据面越狱正交的控制面攻击面，内部安全对齐无法阻止
- 🔬 **研究方法**：提出 CDA：schema 强制 logit mask 向生成轨迹注入恶意前缀、模型自行补全恶意意图，实例化为 EnumAttack 与更隐蔽的 DictAttack
- 📌 **结论**：13 个模型上 DictAttack 对 gpt-5、gemini-2.5-pro 等取得 94.3-99.5% ASR，对抗 SoTA 守卫仍达 75.8%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Content Warning: This paper may contain unsafe or harmful content generated by LLMs that may be offensive to readers. Large Language Models (LLMs) increasingly serve as tooling platforms through structured output APIs, but the grammar-guided decoding that powers this feature opens a critical control-plane attack surface orthogonal to traditional data-plane vulnerabilities. We introduce Constrained Decoding Attack (CDA), a new jailbreak class that targets the LLM control plane. CDA is best characterized as a control-to-semantic pipeline: (1) schema-enforced logit masking injects a malicious prefix into the generation trajectory, and (2) the model itself completes the harmful intent. Unlike data-plane jailbreaks that rely on bypassing alignment with visible inputs, CDA acts on the decoding process itself, so internal safety alignment alone cannot stop it. We instantiate CDA with EnumAttack, which hides malicious content in enum fields, and the more evasive DictAttack, which decouples the payload across a benign prompt and a dictionary-based grammar. Across 13 proprietary/open-weight models and five standard benchmarks, DictAttack achieves 94.3--99.5% Attack Success Rate (ASR) on flagship models including gpt-5, gemini-2.5-pro, deepseek-r1, and gpt-oss-120b. While basic grammar auditing mitigates EnumAttack, DictAttack still sustains 75.8% ASR against SOTA jailbreak guardrails, exposing a "semantic gap" that demands cross-plane defenses bridging the data and control planes. Project page and code are available at https://ict-cda.github.io/.

</details>