## 研究方向

Guard model 的训练方法、系统架构与部署形态（效果评测与攻击面见姊妹页 guardrail-evaluation.md）。

## 防御与检测方法

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

### 6. Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense

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

### 7. Enforcing LLM Safety through DMD-based Classification of Prompt-Response Embedding Dynamics

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

### 8. A Self-Evolving Multi-Agent Framework Defense against LLM Jailbreak Attacks

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

### 9. HRGuard: Gating Relationship Manipulation in Multi-Turn Agentic AI Conversations

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

### 10. LMSM: LLM Security Framework Inspired by Linux Security Modules

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

### 11. Beyond Over-Refusal: Defending Indirect Prompt Injection via Latent Instruction Manifolds

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

### 12. BanglaVeilGuard: Cross-Script Safety Benchmarking and Lightweight Guardrails for Bangla Large Language Models

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

### 13. AI Watchdog: Agent Interfaces for Detecting and Defending Against Manipulative Dark Patterns in AI Conversations

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

### 14. StepGuard: Learning Step-Level Guardrails with Scalable Supervision and Safety-Utility Balancing

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

### 15. ProbGuard: Calibrated Safety Risk Estimation from LLM Output Distributions

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

### 16. DARWIN: Evolving Jailbreak Adversary and Guardrail for LLM Safety Evaluation and Protection

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

### 17. kNNGuard: Turning LLM Hidden Activations into a Training-Free Configurable Guardrail

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

### 18. Stateful Guardrails for Multi-Turn LLM Systems: A Conversational Risk Accumulation Framework

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

### 19. Why Do Safety Guardrails Degrade Across Languages?

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

### 20. Safe-Unsafe Concept Separation Emerges from a Single Direction in Language Models Activation Space

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

### 21. Safeguarding Language Models via Self-Destruct Trapdoor

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

### 22. Lattice: Generative Guardrails for Conversational Agents

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

### 23. Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks

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

### 24. RST-Guarder: Enhancing Long-Context Robustness for Safeguards via RST Parsing and Probabilistic Inference

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

### 25. HiddenGuard: Fine-Grained Safe Generation with Specialized Representation Router

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

### 26. Efficient LLM Moderation with Multi-Layer Latent Prototypes

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

### 27. Domain Generalizable AI Guardrails with Augmented Policy Training

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

### 28. A Lightweight Explainable Guardrail for Prompt Safety

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

### 29. BERM: Low-Overhead Prompt-Injection Detection via In-Situ Benign Representation Modeling

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/8133.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`detection`、`analysis`、`lightweight guard model`、`in-situ representation`、`deployment latency`、`prompt injection`

- 🎯 **研究动机**：现有提示注入防御依赖脆弱启发式或调用昂贵辅助模型，无法兼顾鲁棒与低延迟
- 🔬 **研究方法**：BERM 对 host LLM prefill 阶段提取的内部表征原位建模：联合对比学习良性表征紧致流形以最大化与恶意表征分离，轻量分类器推理时原位检测
- 📌 **结论**：F1 比最佳先前工作高 5.2 个百分点，同时快 12 倍以上，增量推理开销近零

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Real-world deployment of large language models (LLMs) necessitates a robust and low-latency approach to detect prompt injections; existing lowoverhead methods fail to simultaneously boost robustness and reduce latency. Current defenses for prompt injection either rely on brittle heuristics or invoke costly auxiliary models, imposing a significant runtime burden. We introduce BERM, a lightweight framework that performs in-situ detection by modeling a host LLM’s internal representations extracted during prefill, adding negligible overhead. Our approach trains a lightweight classifier atop the LLM by learning a compact manifold of benign representations via joint contrastive learning to maximize the separation from malicious representations. At inference, this pre-trained classifier enables in-situ detection without invoking auxiliary guard models. On a diverse landscape of prompt injection attacks, our framework establishes a new state-of-the-art, achieving an F1-score 5.2 percentage points (pp) higher than the best prior work. Critically, BERM achieves this while being over 12x faster, reducing incremental inference overhead to near-zero.

</details>

### 30. Explaining Jailbreaks: Structured and Interpretable Safety Assessment for Large Language Models

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/4430.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`detection`、`benchmark`、`analysis`、`explanation-aware guard`、`structured output`、`cross-benchmark transfer`

- 🎯 **研究动机**：越狱评估依赖 ASR 等结果级指标，无法说明安全失败如何与为何发生
- 🔬 **研究方法**：解释感知安全框架：在二元有害检测上增加严重度、策略、触发 span、理由与安全因子的结构化解释，人机混合标注管线加微调紧凑模型生成规范解释
- 📌 **结论**：防御评估中把 ASR 降至 Vicuna-7B 的 0.44% 与 GPT-3.5 的 1.30% 并达最低 StrongREJECT 分，诊断属性恢复优于通用 LLM 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) remain highly vulnerable to jailbreak attacks, yet existing evaluations rely primarily on outcome-level metrics such as Attack Success Rate (ASR), providing limited insight into how and why safety failures occur. We propose an explanation-aware safety framework that augments binary harmfulness detection with structured, human-interpretable explanations capturing severity, strategies, trigger spans, rationales, and derived safety factors. To enable scalable and consistent supervision, we introduce a human–LLM hybrid annotation and canonicalization pipeline. We then fine-tune a compact model to generate canonical explanations alongside harmfulness decisions. Across both seen and unseen benchmark settings, our method improves robustness and explanation fidelity. In jailbreak defense evaluation, our approach reduces ASR to 0.44% on Vicuna-7B and 1.30% on GPT-3.5, outperforming existing defense baselines while also achieving the lowest StrongREJECT scores. Beyond outcome-level gains, the model more accurately recovers diagnostic attributes (e.g., attack strategy, trigger spans, and safety factors) than strong general-purpose LLM baselines. Overall, explanation-aware learning exposes diagnostic dimensions that ASR alone cannot capture and provides a more faithful and actionable foundation for robust LLM safety assessment.

</details>

### 31. Auto-Tuning Safety Guardrails for Black-Box Large Language Models

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

### 32. Lightweight Safety Guardrails via Synthetic Data and RL-guided Adversarial Training

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

### 33. FLAME: Flexible LLM-Assisted Moderation Engine

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

### 34. Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming

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

### 35. AEGIS: Online Adaptive AI Content Safety Moderation with Ensemble of LLM Experts

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

### 36. RigorLLM: Resilient Guardrails for Large Language Models against Undesired Content

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

### 37. Self-Guard: Empower the LLM to Safeguard Itself

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

### 38. aipsy-judge: A Specialized, Psychologist-Corrected Local Judge for the Psychological Safety of Conversational AI

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

### 39. Sledgehammer or Scalpel? A Fine-grained Adaptive Framework for Implicit Hate Speech

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

### 40. From Specialization to Generalization: Instruction-tuned LLMs for Robust Harmful Content Mitigation

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

### 41. SPAR-Hate: Auditor-Guided Multi-Perspective Role Reasoning for Bilingual Hate Speech Parsing

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

### 42. SMARTER: A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models

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

### 43. RV-HATE: Reinforced Multi-Module Voting for Implicit Hate Speech Detection

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

### 44. New Terms, New Toxicity: Consensus-based Chinese Neologism Toxicity Detection via Search-Augmented LLMs

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

### 45. LLM Safety From Within: Detecting Harmful Content with Internal Representations

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

### 46. LLM-Based Multi-Task Bangla Hate Speech Detection: Type, Severity, and Target

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

### 47. DIA-HARM: Dialectal Disparities in Harmful Content Detection Across 50 English Dialects

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

### 48. Beyond Single-View Detection: A Dual-Space Reasoning Framework for Interpretable Harmful Meme Understanding

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

## 系统与工具

### 49. Speculative Probing: LLM Monitoring at Speculative-Decoding Cost

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

### 50. Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator

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

### 51. A Reproducible, License-Aware Distillation Recipe for CPUDeployable Safety Classification

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

### 52. Fence: Specialized SLM Guardrails for LLM Applications

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

### 53. YuFeng-XGuard: A Reasoning-Centric, Interpretable, and Flexible Guardrail Model for Large Language Models

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

### 54. SGuard-v1: Safety Guardrail for Large Language Models

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

### 55. Qwen3Guard Technical Report

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

### 56. OneShield -- the Next Generation of LLM Guardrails

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

### 57. Granite Guardian

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

### 58. ShieldGemma: Generative AI Content Moderation Based on Gemma

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

### 59. WildGuard: Open One-stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs

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

### 60. Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations

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

### 61. NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails

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

### 62. An Empirical Measurement of Jailbreaking Evaluators
📄 [arXiv](https://arxiv.org/abs/2609.10594)　📅 2026-09


👤 **作者**：Yujie Mu

**关键词**：`benchmark`、`jailbreak evaluator`、`measurement validity`、`cross-study comparison`

- 🎯 **研究动机**：越狱研究各自独立验证评测器，跨论文攻击强度不可比且评测器隐含不同成功定义
- 🔬 **研究方法**：同一人工标注数据受控比较六个常用评测器（HarmBench/JailbreakBench/Radar/StrongReject/JADES/JailMeter），共享 judge 骨干
- 📌 **结论**：JADES 综合最佳，HarmBench 与 StrongReject 亦佳——评测器选择显著影响报告的攻击强度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Expert evaluation of jailbreak responses is costly and difficult to scale, so the community increasingly relies on automated evaluators to determine whether an attack succeeds. However, jailbreak studies typically validate their chosen evaluator independently, repeatedly spending resources on similar evaluation efforts while making results across papers difficult to compare. Different evaluators also encode different definitions of jailbreak success, meaning that reported attack strength and apparent progress can depend substantially on which evaluator is used. We systematically compare six evaluators that recur in recent jailbreak attack and defense research: HarmBench, JailbreakBench, JailbreakRadar, StrongReject, JADES, and JailMeter. To our knowledge, no prior study has evaluated all six on the same human-labeled data under a controlled setup. We evaluate them on JailbreakQR and JailMeter-Eva, using human judgments as the reference, and measure agreement with humans, error types, and consistency across attack families. For evaluators that require a general-purpose LLM judge, we use a shared backbone to control for model-specific variation. We found that JADES exhibits the best overall performance, while HarmBench and StrongReject also demonstrate good performance.

</details>

### 63. RAG-Safety-Bench: Reliable Evaluation of Retrieval-Augmented LLM Safety
📄 [arXiv](https://arxiv.org/abs/2609.11758)　📅 2026-09


👤 **作者**：Adithiyan Rajan Indira Saravanan、Kathleen C. Fraser

**关键词**：`benchmark`、`RAG safety`、`guardrail failure`、`confound control`

- 🎯 **研究动机**：RAG 会放大有害内容生成，但检索质量混杂使安全退化机制不清
- 🔬 **研究方法**：四条件干净分离（无 RAG/oracle 含答案/相关无答案/随机安全文档）剥离检索器质量混杂，评测 5 个开源 LLM
- 📌 **结论**：基线 guardrail 不保证 RAG 下游安全；良性文档也可导致不安全生成

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Allowing large language models (LLMs) to retrieve information from a set of trusted documents can increase reliability and reduce hallucination. However, recent work has demonstrated that retrieval-augmented generation (RAG) can have unintended side effects on the overall safety of the generated responses, when prompted for harmful or dangerous content. A clearer understanding of the mechanisms leading to this result is needed, as increasing numbers of end users turn to RAG to incorporate corporate documents and knowledge bases into LLM-based systems. We introduce RAG-Safety-Bench, a benchmark to measure the safety impact of RAG on LLM models. By removing the confounding effect of retriever quality, and cleanly separating the problem into four conditions -- non-RAG, RAG with an oracle document containing the answer to the harmful request, RAG with documents related to the harmful request but without the specific answer, and RAG with random, safe documents -- the benchmark isolates the impacts of different factors in the observed safety degradation. We report results across five open-source LLMs, showing an inverse relationship between benign and unsafe capability, strong evidence that baseline safety guardrails do not lead to downstream safety guarantees in the RAG case, and model-specific support for previous findings that even benign documents can lead to unsafe generation in retrieval-enabled systems.

</details>

### 64. Recall Is Not Protection: Evaluating Safety Monitors Against Model Compliance

📄 [arXiv](https://arxiv.org/abs/2609.05797)　📅 2026-09

**关键词**：`analysis`、`safety monitor evaluation`、`elicitable prompt`、`recall validity`

👤 **作者**：Sripad Karne

- 🎯 **研究动机**：安全监控按 harmfulness 标签的 recall 评测，但拦截只有在该模型本会顺从时才真正防害
- 🔬 **研究方法**：重复采样目标模型响应定义 elicitable prompt（至少一次顺从），分开报告 elicitable 与 non-elicitable 上的监控 recall
- 📌 **结论**：六种监控在 elicitable 上 recall 低 0.22-0.38；被漏掉的 prompt 顺从概率是被拦的 2.8-5.6 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety monitors screen prompts sent to deployed language models, flagging harmful requests so they are never answered. They are evaluated by recall against harmfulness labels, but a catch only prevents harm if the model would otherwise have complied. We measure the difference directly: we sample repeated responses from the target model, call a harmful prompt \emph{elicitable} if the model complies at least once, and report monitor recall separately on elicitable and non-elicitable prompts. Across six monitor configurations and three model families, spanning activation probes, fine-tuned text guards, and a 120B policy-conditioned reasoning classifier, recall on elicitable prompts falls 0.22 to 0.38 below recall on non-elicitable prompts at a fixed false positive rate. The prompts a monitor misses are 2.8 to 5.6 times more likely to be complied with than the prompts it catches. The gap replicates across three model families and appears also in text-only monitors entirely independent of the target model. This suggests that standard recall may overstate the protection monitors provide in practice, and that monitors should be evaluated against what their models will actually answer.

</details>

### 65. CS-Guard: Benchmarking LLM Guardrails for Code Generation Security

📄 [arXiv](https://arxiv.org/abs/2609.09798)　📅 2026-09

**关键词**：`benchmark`、`code generation guardrail`、`malware generation`、`fictional scenario attack`

👤 **作者**：Jinyang Li、Mingyu Guo、Hung X. Nguyen

- 🎯 **研究动机**：LLM 被用于生成恶意软件，代码生成安全的 guardrail 效果缺系统评测
- 🔬 **研究方法**：CS-Guard：1,000 恶意生成 prompt × 7 越狱 + 新虚构场景攻击 FSA，331 个 code-to-code prompt，9 guardrail × 7 LLM
- 📌 **结论**：text-to-code 越狱后平均 ASR 约 50%；code-to-code 基座近 100%、guardrail 下仍 14.4-100%；FSA 在多数 guardrail 下接近 100%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have been ex- ploited to generate malware, but the effective- ness of guardrails for code generation secu- rity remains unclear. We introduce CS-Guard, the first benchmark to systematically evalu- ate guardrails for code generation security. It covers 1) text-to-code generation with 1000 high-quality malware-generation prompts, 7 jailbreak attacks, and a novel fictional scenario attack (FSA) that embeds malicious intent in a legitimate fictional software-development sce- nario; and 2) code-to-code generation with 331 code prompts spanning code infilling, code completion, and code translation. We empiri- cally evaluate 9 guardrails across seven LLMs. We find that current guardrails perform poorly against malicious code-generation re- quests: for text-to-code, the average attack success rate (ASR) after jailbreaks reaches about 50% for many guardrails; for code-to- code, average ASR approaches 100% on base LLMs and remains high across many guardrails (14.4% to nearly 100%). Our FSA also achieves ASR close to 100% across many guardrails, raising major reliability concerns for real-world software development. To sup- port future research, CS-Guard uses a modular three-layer guardrail taxonomy that lets devel- opers register guardrails for evaluation. We release the benchmark and data to enable fur- ther community evaluation.

</details>
