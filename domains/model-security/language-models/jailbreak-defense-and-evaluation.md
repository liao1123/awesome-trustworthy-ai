# Jailbreak 防御与评测

[返回 Language Model Security 目录](README.md)

## 研究方向

本页研究如何检测和缓解语言模型 jailbreak，并判断防御是否真正提高部署安全。除 ASR 外，评测需要同时检查 adaptive attack、benign utility、over-refusal、inference cost、response quality 和 judge reliability；防御可位于内部表示、解码过程、对话状态或训练阶段，独立内容审核模型仍由 [Guardrail](../../guardrails/README.md) 维护。

## 研究脉络

- **输出结果评测：** 早期 benchmark 主要统计 harmful prompt 的拒答与攻击成功率，容易忽略回答质量、judge 偏差和模型能力变化。
- **内部检测：** hidden state、gating feature、refusal trajectory 和 token-level probe 用模型仍保留的安全信号识别经过改写的攻击。
- **多轮状态防御：** 防御从逐条 prompt 分类扩展到风险随对话累积、批处理稀释和跨轮意图转移。
- **训练时适应：** self-play、对抗数据与多轮 safety alignment 让模型面对不断变化的攻击，而非记忆固定模板。
- **统一代价：** 最新研究把 safety、utility 与 compute/cost 放到同一评测中，揭示“更强防御”可能只是通过过度拒答或能力下降换取较低 ASR。

## Benchmark、Trade-off 与失效边界

### 1. IndicSafeEval: Safety Robustness of Large Language Models under Multilingual Persuasive Jailbreak Attacks

📄 [arXiv](https://arxiv.org/abs/2609.03781)　📅 2026-09

**关键词**：`benchmark`、`Indic languages`、`persuasive jailbreak`、`cross-lingual safety`、`multilingual jailbreak`、`persuasive attack`

👤 **作者**：Saikat Mondal、Mamta、Deeksha Varshney、Oana Cocarascu、Asif Ekbal

- 🎯 **研究动机**：LLM 安全评测仍以英语为主，低资源与文化多样语言中的对齐失效形态不明
- 🔬 **研究方法**：构建 IndicSafeEval：四种印度语言（Hindi、Bengali、Marathi、Punjabi）×十个安全关键类别×六种类人说服策略，共 7,200 个对抗 prompt，对开源 LLM 做系统黑盒评测
- 📌 **结论**：安全性强烈依赖语言与说服式措辞，不同风险类别脆弱度差异显著——英语中心的安全评测存在系统性盲区

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used in multilingual settings, yet their safety is still evaluated primarily in English. This limits our understanding of how alignment failures manifest in low-resource and culturally diverse languages. We introduce IndicSafeEval, a persuasion-based jailbreak evaluation framework for Indian languages. Our benchmark combines ten safety critical content categories with six human-like persuasive strategies across four different Indian languages, such as Hindi, Bengali, Marathi and Punjabi, resulting in 7,200 adversarial prompts. We conduct a systematic black-box evaluation of several open-source LLMs to examine how their safety behaviour varies across languages, persuasion strategies, and risk categories. Our analysis shows that the model does not behave equally safely across all languages and prompt styles. Instead, safety performance depends strongly on both the languages used and the way a request is phrased using persuasive cues. We further observe that different risk categories exhibit different levels of vulnerability, with some types of harmful content being significantly more susceptible to persuasion-based jailbreaks than others. These findings reveal important limitations of current safety evaluations, which are largely English-centric, and underscore the need for multilingual and persuasion-aware benchmarking frameworks to more accurately assess real-world LLM safety. Our implementation is available at https://github.com/MonSaikat/IndicSafeEval. Warning: this paper contains example data that may be offensive or harmful.

</details>

### 2. LongGuard: Mechanistic Analysis and Training-Free Mitigation of Long-Context Failure in Safety Guardrails

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

### 3. Refusal geometry reflects refusal training: diverse refusal prefixes can raise stable rank and weaken refusal vector ablation attacks

📄 [arXiv](https://arxiv.org/abs/2608.25390)　📅 2026-08

**关键词**：`analysis`、`defense`、`refusal-prefix diversity`、`gradient stable rank`、`alignment hardening`、`refusal safeguard`

👤 **作者**：Andrey Labunets

- 🎯 **研究动机**：拒答行为集中于单一方向或低维子空间，vector ablation 即可移除，成因不明
- 🔬 **研究方法**：以 OLMo-2 为案例追踪拒答训练动态，分析首 token 损失的梯度与激活更新的 stable rank，并以受控微调验证多样化拒答开头
- 📌 **结论**：重复拒答前缀压低秩导致脆弱；多样化开头提高 stable rank 并增强对消融攻击的抵抗

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Refusal training protects AI models from jailbreaks by training models to decline unsafe queries, reducing the risk of misuse. Recent work finds that refusal behavior in aligned language models can be mediated by a single activation direction or a low-dimensional refusal subspace shared across harmful prompts: ablating those directions suppresses refusals while largely preserves other model capabilities. Yet it remains unclear why safety-critical features in a wide range of models emerge in a concentrated, low-dimensional structure. In a case study of OLMo-2-0425-1B-Instruct we find that the refusal geometry reflects refusal training: activation updates resulting from refusal-completion first-token losses explain the resulting refusal direction and refusal subspace. We study refusal directions through the training dynamics across refusal datasets and reveal that their brittleness is associated with repetitive refusal starts, which in turn is linked to concentration of gradients and refusal features in a low-dimensional subspace. Across frozen-model analyses and controlled synthetic fine-tuning, we find evidence of a hardening lever: diverse refusal starts can raise stable ranks of gradients and activation changes, making refusals harder to remove with a vector ablation attack.

</details>

### 4. Register Shifts Break LLM Safety: A Bengali Benchmark with Culturally Grounded Harms

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

### 5. Redteaming Leading Arabic LLMs with ASAS

📄 [arXiv](https://arxiv.org/abs/2608.21985)　📅 2026-08

**关键词**：`benchmark`、`Arabic red teaming`、`human annotation`、`judge reliability`、`multilingual jailbreak`、`human evaluation`

👤 **作者**：Fidaa Abed、Haidar Khan、M Saiful Bari、Babar Khan、Abdalghani Abujabal

- 🎯 **研究动机**：阿拉伯语 LLM 安全尤其是对抗性红队评估严重不足，缺乏文化扎根的评测资源
- 🔬 **研究方法**：ASAS 首个完全人工策划的阿拉伯语红队 benchmark：801 条 prompt 覆盖 8 个安全类别与 8 种攻击策略并附 MSA 理想回应，人工标注者以四级安全量表评估 GPT-4o、Claude 3.7 Sonnet、ALLaM、FANAR 等七个模型
- 📌 **结论**：多数模型无法防御超 50% 的不安全 prompt，武器与违禁品等高危类别缺口最大，直接与混淆攻击最有效；自动 judge（如 GPT-4o）表现远逊人工标注

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As the adoption of large language models (LLMs) grows in Arabic-speaking regions, ensuring their safety and cultural alignment is increasingly critical. However, Arabic LLM safety remains underexplored, especially in adversarial evaluation settings. We introduce the Arabic Safety Index (ASAS), the first fully human-curated Arabic benchmark for redteaming LLMs. ASAS contains 801 prompts spanning 8 safety categories and 8 attack strategies, with ideal responses in Modern Standard Arabic (MSA). We conduct a redteaming evaluation across seven leading models with Arabic capabilities, including GPT-4o, Claude 3.7 Sonnet, and regional models such as ALLaM and FANAR. Human annotators rate responses using a structured 4-point safety scale, revealing that most models fail to defend against 50% of unsafe prompts. Our findings highlight major safety gaps in high-harm categories such as weapons and illicit substances, with direct and obfuscation-based attacks proving most effective. The results also show that language alignment does not readily transfer across languages, and that automated safety judges (e.g., GPT-4o) perform poorly compared to human annotators. ASAS provides a culturally grounded benchmark and redteaming protocol to drive progress in Arabic LLM safety.

</details>

### 6. Breaking the Assumptions: Auditing Input-Side Jailbreak Defenses Against Semantic Attacks

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

### 7. BanglaVeilGuard: Cross-Script Safety Benchmarking and Lightweight Guardrails for Bangla Large Language Models

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

### 8. Safety in Batches? Understanding and Mitigating Safety Failures in Batch Prompting

📄 [arXiv](https://arxiv.org/abs/2608.02681)　📅 2026-08

**关键词**：`analysis`、`batch prompting`、`refusal dilution`、`batch-aware DPO`

👤 **作者**：Kihyun Kim、Hee-Seon Kim、Wonjun Lee、Changick Kim

- 🎯 **研究动机**：批量提示是实用推理策略，但其安全影响未被研究
- 🔬 **研究方法**：识别有害问题嵌入良性问题批次后引发有害回答的失效模式，从对齐信号弱化与拒答信号稀释归因，并提出 batch-aware 偏好优化缓解
- 📌 **结论**：批量提示作为简单黑盒攻击在开源与前沿商用模型上均取得高 ASR，batch-aware 优化有效缓解该盲点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Batch prompting is a practical inference strategy for large language models, but its safety implications remain underexplored. We show that the success of batch prompting for utility does not extend to safety: a harmful question that is reliably refused in isolation can elicit a harmful response when embedded in a batch of benign questions. We identify this as a distinct safety failure mode, not reducible to known vulnerabilities such as in-context learning or long-context effects, and analyze its causes from two complementary perspectives: alignment signal weakening and refusal signal dilution. Across widely used open-source and frontier commercial models, batch prompting consistently achieves high attack success rates as a simple black-box attack. We further show that batch-aware preference optimization effectively mitigates the vulnerability. These findings highlight a blind spot in current safety alignment and point to batch-aware alignment as a necessary step toward robust deployment.

</details>

### 9. When LLM Defenses Backfire: Characterizing Safety, Performance, and Cost Trade-offs

📄 [arXiv](https://arxiv.org/abs/2607.24392)　📅 2026-07

**关键词**：`benchmark`、`jailbreak defense`、`safety-utility-cost`、`over-refusal`

👤 **作者**：Tong Zhang、Zexin Li、Simin Chen、Yun Peng

- 🎯 **研究动机**：越狱防御可能引入削弱效用的次级成本，但按操作策略刻画其副作用图谱的工作缺失
- 🔬 **研究方法**：沿性能影响、良性输入过度拒绝与推理成本三维，跨 SOTA 防御方法、基准数据集与开源 LLM 系统研究不同防御策略的副作用画像
- 📌 **结论**：防御很少提升下游能力，只是在安全收益与可用性、效率间做不同交易：规则型最保性能、保守自反型最过度拒绝、多轮型运行时开销最大

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak defenses are essential for protecting large language models (LLMs), but they can also introduce secondary costs that weaken model utility. We present a systematic study of these defense trade-offs along three dimensions: performance impact, over-refusal on benign inputs, and inference cost. Rather than treating defenses as a single class, we organize them by operational strategy and examine how different strategies correlate with different side-effect profiles. Across state-of-the-art defense methods, widely used benchmark datasets, and representative open-source LLMs, we find that defenses rarely improve downstream capability, but instead vary in how they trade safety gains against usability and efficiency. In particular, rule-based defenses best preserve task performance, highly conservative self-reflective defenses often increase over-refusal, and multi-round defenses incur the largest runtime overhead. These results provide both a benchmark for evaluating defense side effects and practical guidance for selecting defenses under deployment constraints.

</details>

### 10. Abliteration Mitigation via Refusal Aliases

📄 [arXiv](https://arxiv.org/abs/2608.18093)　📅 2026-08

**关键词**：`defense`、`analysis`、`refusal aliases`、`writer-reader repair`、`tamper resistance`、`abliteration resistance`

👤 **作者**：Nathan Truong

- 🎯 **研究动机**：abliteration 只需少量对比 prompt 即可提取拒答方向并投影移除，现有防御忽视拒答方向为何易被提取
- 🔬 **研究方法**：AMRA 对残差流 writer 矩阵做 rank-k 更新，把拒答诱发激活替换为随机别名并校正下游 reader 矩阵以保持原行为
- 📌 **结论**：Llama-3-8B 上消融后拒答分较无防御提升 2.16 分且 MMLU 退化低于 0.5 个百分点；Gemma-2-9B 提升 14.70 分但效用代价更大

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Abliteration, the removal of refusal capabilities from large language models by projecting weight matrices orthogonal to an extracted refusal direction, has emerged as a prominent safety concern through its ability to bypass post-training alignment using only a small set of contrastive prompts. We find that existing defenses commonly overlook the cause of abliteration; that is, how easily the refusal direction can be extracted. To hinder this process, we introduce a weight-editing method that obscures the refusal signal by applying rank-$k$ updates to residual stream writer matrices while replacing refusal-inducing activations with random aliases and correcting downstream reader matrices to preserve the model's original behavior. On Llama-3-8B, AMRA improves post-abliteration refusal scores by $2.16$ points over the undefended baseline with less than $0.5$ percentage points of MMLU degradation. On Gemma-2-9B, it improves the post-abliteration refusal by $14.70$ points over the baseline while keeping harmful output rates similar to the baseline, albeit at a greater utility cost.

</details>

### 11. When Medical Safety Alignment Fails: A Benchmark for Evaluating LLMs on High-Risk Medical Queries

📄 [arXiv](https://arxiv.org/abs/2606.28332)　📅 2026-06

**关键词**：`benchmark`、`medical safety`、`high-risk query`、`domain evaluation`

👤 **作者**：Yige Li、…、Xingjun Ma

- 🎯 **研究动机**：对齐 LLM 在高风险医疗场景的安全性不明，广义医疗 QA 基准无法覆盖需拒绝、谨慎或安全引导的现实提示
- 🔬 **研究方法**：构建 MedHarm：1,100 条医学接地的查询覆盖毒理、药理、隐匿投毒、麻醉、胎儿伤害等 10 类；评估 15 个 LLM 与 4 个护栏模型
- 📌 **结论**：对齐模型仍产生不安全可执行回应，医疗微调会放大有害特异性，外部护栏减少部分失败却带来脆弱阻断与弱安全有用性；医疗安全不能由通用对齐推断

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used for medical and health-related questions, yet their safety in high-risk medical scenarios remains poorly understood. We introduce \textsc{MedHarm}\footnote{Code and data will be released upon acceptance. Due to the sensitive nature of high-risk medical queries, data access will be available to qualified researchers upon request.}, a high-risk medical safety benchmark with 1,100 medically grounded queries across 10 safety-critical categories, including toxicology, pharmacology, covert poisoning, anesthesia, and fetal harm. Unlike broad medical QA benchmarks, \textsc{MedHarm} targets realistic clinical, educational, and technical prompts that require refusal, caution, or safe redirection rather than direct helpfulness. We evaluate 15 LLMs spanning general-purpose, medical-purpose, closed-source, and downstream SFT models, together with 4 representative guardrail models. Results reveal a substantial gap between apparent alignment and medical safety: aligned models can still produce unsafe or actionable responses, medical fine-tuning can amplify harmful specificity, and external guardrails reduce some failures while introducing brittle blocking and weak safe helpfulness. These findings show that medical safety cannot be inferred from general alignment or medical capability alone, highlighting the need for domain-specific stress testing before deploying LLMs in safety-critical medical applications.

</details>

### 12. Jailbroken Frontier Models Retain Their Capabilities

📄 [arXiv](https://arxiv.org/abs/2605.00267)　📅 2026-05

**关键词**：`analysis`、`jailbreak tax`、`frontier model`、`capability retention`

👤 **作者**：Daniel Zhu、Zihan Wang、Xuchan Bao、Jerry Wei

- 🎯 **研究动机**：先前发现越狱复杂度带来 jailbreak tax 降低任务性能，但该税与模型能力的关系未明
- 🔬 **研究方法**：在 Haiku 4.5 到 Opus 4.6 的 Claude 系列上评测 28 种越狱与 5 个基准
- 📌 **结论**：tax 与能力成反比：Haiku 4.5 平均损失 33.1%，Opus 4.6 仅 7.7%；Boundary Point Jailbreaking 近零退化实现近完美分类器绕过，安全论证不应依赖越狱降低能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As language model safeguards become more robust, attackers are pushed toward developing increasingly complex jailbreaks. Prior work has found that this complexity imposes a "jailbreak tax" that degrades the target model's task performance. We show that this tax scales inversely with model capability and that the most advanced jailbreaks effectively yield no reduction in model capabilities. Evaluating 28 jailbreaks on five benchmarks across Claude models ranging in capability from Haiku 4.5 to Opus 4.6, we find Haiku 4.5 loses an average of 33.1% on benchmark performance when jailbroken, while Opus 4.6 at max thinking effort loses only 7.7%. We also observe that across all models, reasoning-heavy tasks display considerably more degradation than knowledge-recall tasks. Finally, Boundary Point Jailbreaking, currently the strongest jailbreak against deployed classifiers, achieves near-perfect classifier evasion with near-zero degradation across safeguarded models. We recommend that safety cases for frontier models should not rely on a meaningful capability degradation from jailbreaks.

</details>

### 13. Explaining Jailbreaks: Structured and Interpretable Safety Assessment for Large Language Models

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/4430.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`detection`、`benchmark`、`analysis`、`explanation-aware guard`、`structured output`、`cross-benchmark transfer`

- 🎯 **研究动机**：越狱评估依赖 ASR 等结果级指标，无法说明安全失败如何与为何发生
- 🔬 **研究方法**：解释感知安全框架：在二元有害检测上增加严重度、策略、触发 span、理由与安全因子的结构化解释，人机混合标注管线加微调紧凑模型生成规范解释
- 📌 **结论**：防御评估中把 ASR 降至 Vicuna-7B 的 0.44% 与 GPT-3.5 的 1.30% 并达最低 StrongREJECT 分，诊断属性恢复优于通用 LLM 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) remain highly vulnerable to jailbreak attacks, yet existing evaluations rely primarily on outcome-level metrics such as Attack Success Rate (ASR), providing limited insight into how and why safety failures occur. We propose an explanation-aware safety framework that augments binary harmfulness detection with structured, human-interpretable explanations capturing severity, strategies, trigger spans, rationales, and derived safety factors. To enable scalable and consistent supervision, we introduce a human–LLM hybrid annotation and canonicalization pipeline. We then fine-tune a compact model to generate canonical explanations alongside harmfulness decisions. Across both seen and unseen benchmark settings, our method improves robustness and explanation fidelity. In jailbreak defense evaluation, our approach reduces ASR to 0.44% on Vicuna-7B and 1.30% on GPT-3.5, outperforming existing defense baselines while also achieving the lowest StrongREJECT scores. Beyond outcome-level gains, the model more accurately recovers diagnostic attributes (e.g., attack strategy, trigger spans, and safety factors) than strong general-purpose LLM baselines. Overall, explanation-aware learning exposes diagnostic dimensions that ASR alone cannot capture and provides a more faithful and actionable foundation for robust LLM safety assessment.

</details>

### 14. Response-Based Knowledge Distillation for Multilingual Jailbreak Prevention Unwittingly Compromises Safety

📄 [arXiv](https://arxiv.org/abs/2602.11157)　📅 2025-12　🏷 NeurIPS 2025 Workshop

**关键词**：`analysis`、`multilingual distillation`、`refusal imitation`、`safety regression`

👤 **作者**：Max Zhang、Derek Liu、Kai Zhang、Joshua Franco、Haihao Liu

- 🎯 **研究动机**：用教师拒答数据蒸馏增强学生多语言越狱防御是否可靠未知
- 🔬 **研究方法**：把 OpenAI o1-mini 的拒答行为经 LoRA 黑盒蒸馏到 Llama-3-8B、Gemma-2-2B、Qwen3-8B，训练集约 28,000 条多语言越狱提示
- 📌 **结论**：反直觉地使学生 JSR 上升最高 16.6 个百分点；剔除边界式拒答可逆转安全退化，但 GSM8K 推理性能仍受损

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed worldwide, yet their safety alignment remains predominantly English-centric. This allows for vulnerabilities in non-English contexts, especially with low-resource languages. We introduce a novel application of knowledge distillation (KD) in the context of multilingual jailbreak prevention, examining its efficacy. We distill the refusal behaviors of a proprietary teacher model (OpenAI o1-mini) with Low-Rank Adaptation (LoRA) into three open-source student models: Meta-Llama-3-8B-Instruct, Gemma-2-2B-IT, and Qwen3-8B, using ~28,000 multilingual jailbreak prompts from XSafety via black-box response-based, parameter-efficient fine-tuning (PEFT). Evaluation on the MultiJail benchmark reveals a counterintuitive behavior: standard fine-tuning on the teacher's ``safe'' refusal data inadvertently increases Jailbreak Success Rate (JSR) for all student models, up to 16.6 percentage points. Our experiments reveal a divergent generalization to unseen languages during distillation, with varying outcomes depending on the base model. By removing a primary source of safety degradation, nuanced `boundary' refusals, we mitigate or even reverse safety declines in student models, although reductions in reasoning performance (GSM8K) persist. Overall, our exploratory study highlights the challenges and potential of KD as a technique for multilingual safety alignment, offering a foundation for future research in this direction.

</details>

### 15. A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks

📄 [arXiv](https://arxiv.org/abs/2507.02956)　📅 2025-07

**关键词**：`analysis`、`multi-turn jailbreak`、`representation drift`、`Crescendo`

👤 **作者**：Blake Bullwinkel、…、Ram Shankar Siva Kumar

- 🎯 **研究动机**：多轮越狱对最先进模型与防御仍有效，其表示层机制不明
- 🔬 **研究方法**：在中间表示层研究 Crescendo 多轮越狱，追踪表示随对话轮次的漂移
- 📌 **结论**：对齐模型随轮次增加把 Crescendo 回复表示得更良性，输出持续停留在良性表示区；这解释了 circuit breakers 等单轮防御为何失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent research has demonstrated that state-of-the-art LLMs and defenses remain susceptible to multi-turn jailbreak attacks. These attacks require only closed-box model access and are often easy to perform manually, posing a significant threat to the safe and secure deployment of LLM-based systems. We study the effectiveness of the Crescendo multi-turn jailbreak at the level of intermediate model representations and find that safety-aligned LMs often represent Crescendo responses as more benign than harmful, especially as the number of conversation turns increases. Our analysis indicates that at each turn, Crescendo prompts tend to keep model outputs in a "benign" region of representation space, effectively tricking the model into fulfilling harmful requests. Further, our results help explain why single-turn jailbreak defenses like circuit breakers are generally ineffective against multi-turn attacks, motivating the development of mitigations that address this generalization gap.

</details>

### 16. LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet

📄 [arXiv](https://arxiv.org/abs/2408.15221)　📅 2024-08

**关键词**：`benchmark`、`human jailbreak`、`multi-turn evaluation`、`defense robustness`

👤 **作者**：Nathaniel Li、…、Summer Yue

- 🎯 **研究动机**：LLM 防御主要按单轮自动攻击评估，威胁模型不足以反映真实恶意使用
- 🔬 **研究方法**：编译 537 个多轮人类越狱、2912 条 prompt 的 MHJ 数据集并系统测试防御
- 📌 **结论**：对报告个位数 ASR 的防御，多轮人类越狱在 HarmBench 上 ASR 超 70%，还可恢复 unlearned 模型的双用途生物安全知识

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent large language model (LLM) defenses have greatly improved models' ability to refuse harmful queries, even when adversarially attacked. However, LLM defenses are primarily evaluated against automated adversarial attacks in a single turn of conversation, an insufficient threat model for real-world malicious use. We demonstrate that multi-turn human jailbreaks uncover significant vulnerabilities, exceeding 70% attack success rate (ASR) on HarmBench against defenses that report single-digit ASRs with automated single-turn attacks. Human jailbreaks also reveal vulnerabilities in machine unlearning defenses, successfully recovering dual-use biosecurity knowledge from unlearned models. We compile these results into Multi-Turn Human Jailbreaks (MHJ), a dataset of 2,912 prompts across 537 multi-turn jailbreaks. We publicly release MHJ alongside a compendium of jailbreak tactics developed across dozens of commercial red teaming engagements, supporting research towards stronger LLM defenses.

</details>

### 17. Circuit Discovery Helps Detect LLM Jailbreaking: A Mechanistic Interpretability Study

📄 [arXiv](https://arxiv.org/abs/2608.27504)　📅 2026-08

**关键词**：`analysis`、`adversarial prompt propagation`、`circuit-level mechanism`、`safety constraint bypass`、`jailbreak circuit`、`subnetwork probing`

👤 **作者**：Paria Mehrbod、Boris Knyazev、Guy Wolf、Eugene Belilovsky、Geraldin Nanfack

- 🎯 **研究动机**：安全对齐 LLM 仍易被越狱，但其内部处理对抗 prompt、绕过安全约束的计算机制不清
- 🔬 **研究方法**：用 edge attribution patching 与 subnetwork probing 在 LLaMA-2-7B-chat 上定位生成越狱肯定回答的计算回路，并在首 token 预测阶段消融
- 📌 **结论**：消融可将 ASR 最多降低 80%，并揭示传播关键攻击 token、覆盖安全约束的 attention head 与 MLP pathway

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite extensive safety alignment, large language models (LLMs) remain vulnerable to jailbreak attacks that bypass safeguards to elicit harmful content. While prior work attributes this vulnerability to safety training limitations, the internal mechanisms by which LLMs process adversarial prompts remain poorly understood. We present a mechanistic analysis of the jailbreaking behavior in a large-scale, safety-aligned LLM, focusing on LLaMA-2-7B-chat-hf. Leveraging edge attribution patching and subnetwork probing, we systematically identify computational circuits responsible for generating affirmative responses to jailbreak prompts. Ablating these circuits during the first token prediction can reduce attack success rates by up to 80\%, demonstrating its critical role in safety bypass. Our analysis uncovers key attention heads and MLP pathways that mediate adversarial prompt exploitation, revealing how important tokens propagate through these components to override safety constraints. These findings advance the understanding of adversarial vulnerabilities in aligned LLMs and pave the way for targeted, interpretable defense mechanisms based on mechanistic interpretability.

</details>

### 18. LMSM: LLM Security Framework Inspired by Linux Security Modules

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

### 19. Truth Lies Deep: Countering Semantic Camouflage via Latent Intent Verification

📄 [arXiv](https://arxiv.org/abs/2608.20378) · 🌐 [Project](https://doi.org/10.1109/QPAIN69676.2026.11546227)　📅 2026-08

**关键词**：`defense`、`detection`、`analysis`、`latent-intent probe`、`lightweight guard`、`training-free detection`

👤 **作者**：Md. Hasib Ur Rahman

- 🎯 **研究动机**：安全对齐浅表、拒答只在生成末期触发，语义伪装（良性叙事包装有害意图）绕过标准输入输出护栏
- 🔬 **研究方法**：分析三个 SLM 家族激活轨迹发现 Intent Horizon（约 15-20% 层深处有害意图表征坍缩为安全叙事）；LIV 轻量探针利用早期层 harm signature 做免训练检测
- 📌 **结论**：伪装攻击的晚期表征与安全查询数学上不可区分（检出率<20%）但早期层可检测；PKU-SafeRLHF 上 LIV 超标准护栏 20-50%，免重训中和零日语义攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment in Large Language Models (LLMs) is often superficial, relying on refusal mechanisms that trigger only at the final stages of generation without erasing the foundational knowledge of harmful concepts acquired during pretraining. This study demonstrates that this architectural disconnect leaves models vulnerable to Semantic Camouflage -- adversarial attacks that wrap harmful intent in benign narrative contexts (e.g., creative writing), effectively bypassing standard input and output guardrails. By analyzing the latent activation trajectories of three distinct Small Language Model (SLM) families (Phi-3, Qwen2.5, and Gemma-2b) under adversarial stress, this research identifies a universal ``Intent Horizon'' -- a critical depth (typically 15--20\% of total layers) where the model's distinct, pre-trained representation of harmful intent collapses as it contextualizes the query into a ``safe'' narrative. Results indicate that while late-layer representations of camouflaged attacks are mathematically indistinguishable from safe queries (Detection Rate $< 20\%$), early-layer representations retain a distinct, detectable ``harm signature.'' Leveraging this insight, this paper proposes Latent Intent Verification (LIV), a lightweight probing defense. Experiments on the PKU-SafeRLHF dataset demonstrate that LIV outperforms standard guardrails by a margin of 20--50\% across all tested architectures, effectively neutralizing zero-day semantic attacks without requiring model retraining.

</details>

### 20. Tracing the Dynamics of Refusal: Exploiting Latent Refusal Trajectories for Robust Jailbreak Detection

📄 [arXiv](https://arxiv.org/abs/2605.02958) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65432)　📅 2026-05　🏷 ICML 2026

**关键词**：`detection`、`analysis`、`refusal trajectory`、`forced decoding`、`latent dynamics`、`prompt injection`

👤 **作者**：Xulin Hu、Che Wang、Wei Yang Bryan Lim、Jianbo Gao、Zhong Chen

- 🎯 **研究动机**：RepE 用静态方向刻画拒答，忽略拒答在层与 token 位置上的动态构建过程
- 🔬 **研究方法**：因果追踪发现 Refusal Trajectory——GCG 等攻击压制终端拒答信号后仍残留的稀疏上游激活；SALO 据此在选定层窗口上做轻量白盒检测
- 📌 **结论**：在 Qwen、Llama、Mistral 上以 XSTest 校准的工作点提升多族越狱检测，并厘清其对自适应 GCG 与编码输入的局限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Representation Engineering analyses often characterize refusal using static directions extracted from terminal or pooled representations. We ask whether this view misses how refusal is constructed across layer-token positions. Using causal tracing, we identify a \textit{Refusal Trajectory}: a sparse upstream activation pattern that often persists even when attacks such as GCG suppress terminal refusal signals. Based on this observation, we propose SALO (Sparse Activation Localization Operator), a lightweight white-box detector that operates on raw hidden-state volumes from a selected layer window. Across Qwen, Llama, and Mistral models, SALO improves jailbreak detection on several attack families under a fixed XSTest-calibrated operating point. We further analyze static RepE-style baselines, ROI sensitivity, adaptive GCG attacks, and encoded-input boundary cases, clarifying both the promise and limitations of refusal-trajectory monitoring.

</details>

### 21. Understanding Jailbreak Success: A Study of Latent Space Dynamics in Large Language Models

🎓 [Official](https://aclanthology.org/2026.eacl-long.12/)　📅 2026-03　🏷 ACL 2026

**关键词**：`analysis`、`jailbreak mechanism`、`latent vector`、`harmfulness suppression`、`LLM jailbreak`、`latent dynamics`

👤 **作者**：Sarah Ball、Frauke Kreuter、Nina Panickssery

- 🎯 **研究动机**：不同类型越狱如何绕过安全机制仍缺乏机理性理解
- 🔬 **研究方法**：分析不同越狱输入的模型激活，从单一越狱类别提取 jailbreak 向量并检验其对语义不相似类别的抑制作用，进而考察有害性特征抑制机制
- 📌 **结论**：多样越狱共享内部机制，有效越狱显著降低模型对 prompt 有害性的感知，为鲁棒反制奠定基础

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Conversational large language models are trained to refuse to answer harmful questions. However, emergent jailbreaking techniques can still elicit unsafe outputs, presenting an ongoing challenge for model alignment. This paper aims to deepen our understanding of how different jailbreak types circumvent safeguards by analyzing model activations on different jailbreak inputs. We find that it is possible to extract a jailbreak vector from a single class of jailbreaks that works to mitigate jailbreak effectiveness from other, semantically-dissimilar classes. This suggests that diverse jailbreaks may exploit a common internal mechanism. We investigate a potential common mechanism of harmfulness feature suppression, and find evidence that effective jailbreaks noticeably reduce a model’s perception of prompt harmfulness. These insights pave the way for developing more robust jailbreak countermeasures and lay the groundwork for a deeper, mechanistic understanding of jailbreak dynamics in language models.

</details>

### 22. Unraveling LLM Jailbreaks Through Safety Knowledge Neurons

🎓 [Official](https://aclanthology.org/2026.eacl-long.83/)　📅 2026-03　🏷 ACL 2026

**关键词**：`defense`、`safety neuron`、`vocabulary projection`、`SafeTuning`、`jailbreak mechanism`

👤 **作者**：Chongwen Zhao、Yutong Ke、Kaizhu Huang

- 🎯 **研究动机**：现有越狱防御靠修改输出分布或检测有害内容有效，但安全机理仍不明确
- 🔬 **研究方法**：提出神经元级可解释方法，把内部表示投影到更一致的词表空间以定位安全知识神经元；并提出 SafeTuning 微调策略强化安全关键神经元
- 📌 **结论**：调整安全神经元激活即可控制模型行为（平均 ASR 超 97%）；SafeTuning 跨多个 LLM 降低攻击成功率且优于四种基线防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have achieved substantial progress in alignment, ensuring safer and more reliable outputs. However, jailbreak attacks can still bypass these safeguards and provoke harmful responses from well-aligned models. While some studies have achieved defenses against jailbreak attacks by modifying output distributions or detecting harmful content, the exact rationale still remains elusive. In this work, we present a novel neuron-level interpretability method that focuses on the role of safety-related knowledge neurons. Unlike existing approaches, our method projects the model’s internal representation into a more consistent and interpretable vocabulary space. We then show that adjusting the activation of safety-related neurons can effectively control the model’s behavior with a mean ASR higher than 97%. Building on this insight, we propose SafeTuning, a fine-tuning strategy that reinforces safety-critical neurons to improve model robustness against jailbreaks. SafeTuning consistently reduces attack success rates across multiple LLMs and outperforms all four baseline defenses. These findings offer a new perspective on understanding and defending against jailbreak attacks.

</details>

### 23. Be Your Own Red Teamer: Safety Alignment via Self-Play and Reflective Experience Replay

📄 [arXiv](https://arxiv.org/abs/2601.10589) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.933/)　📅 2026-01　🏷 ACL 2026

**关键词**：`defense`、`self-play alignment`、`reflective replay`、`adaptive red teaming`

👤 **作者**：Hao Wang、Yanting Wang、Hao Li、Rui Li、Lei Sha

- 🎯 **研究动机**：依赖静态外部红队与固定数据集的安全对齐过拟合已知攻击模式，难以泛化到新威胁
- 🔬 **研究方法**：Safety Self-Play 让单一 LLM 在统一 RL 循环中同时充当攻击者与防御者动态演化，并以 UCB 采样的反思经验回放聚焦低奖励的失败案例
- 📌 **结论**：自主演化出鲁棒防御能力，显著超越在静态对抗数据集上训练的基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have achieved remarkable capabilities but remain vulnerable to adversarial ``jailbreak'' attacks designed to bypass safety guardrails. Current safety alignment methods depend heavily on static external red teaming, utilizing fixed defense prompts or pre-collected adversarial datasets. This leads to a rigid defense that overfits known patterns and fails to generalize to novel, sophisticated threats. To address this critical limitation, we propose empowering the model to be its own red teamer, capable of achieving autonomous and evolving adversarial attacks. Specifically, we introduce Safety Self- Play (SSP), a system that utilizes a single LLM to act concurrently as both the Attacker (generating jailbreaks) and the Defender (refusing harmful requests) within a unified Reinforcement Learning (RL) loop, dynamically evolving attack strategies to uncover vulnerabilities while simultaneously strengthening defense mechanisms. To ensure the Defender effectively addresses critical safety issues during the self-play, we introduce an advanced Reflective Experience Replay Mechanism, which uses an experience pool accumulated throughout the process. The mechanism employs a Upper Confidence Bound (UCB) sampling strategy to focus on failure cases with low rewards, helping the model learn from past hard mistakes while balancing exploration and exploitation. Extensive experiments demonstrate that our SSP approach autonomously evolves robust defense capabilities, significantly outperforming baselines trained on static adversarial datasets and establishing a new benchmark for proactive safety alignment.

</details>

### 24. Defending Large Language Models Against Jailbreak Attacks via In-Decoding Safety-Awareness Probing

📄 [arXiv](https://arxiv.org/abs/2601.10543)　📅 2026-01

**关键词**：`detection`、`in-decoding probing`、`safety awareness`、`token intervention`

👤 **作者**：Yinzhi Zhao、Ming Wang、Shi Feng、Xiaocui Yang、Daling Wang、Yifei Zhang

- 🎯 **研究动机**：模型被越狱后内部仍产生潜在安全信号，却被流畅续写倾向覆盖而无法自我纠正
- 🔬 **研究方法**：在解码过程中显式探测并利用这些潜在安全信号，尽早检出不安全内容并实施 token 干预
- 📌 **结论**：多种越狱攻击下显著提升安全性，良性输入误拒率低且回复质量保持

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have achieved impressive performance across natural language tasks and are increasingly deployed in real-world applications. Despite extensive safety alignment efforts, recent studies show that such alignment is often shallow and remains vulnerable to jailbreak attacks. Existing defense mechanisms, including decoding-based constraints and post-hoc content detectors, struggle against sophisticated jailbreaks, often intervening robust detection or excessively degrading model utility. In this work, we examine the decoding process of LLMs and make a key observation: even when successfully jailbroken, models internally exhibit latent safety-related signals during generation. However, these signals are overridden by the model's drive for fluent continuation, preventing timely self-correction or refusal. Building on this observation, we propose a simple yet effective approach that explicitly surfaces and leverages these latent safety signals for early detection of unsafe content during decoding. Experiments across diverse jailbreak attacks demonstrate that our approach significantly enhances safety, while maintaining low over-refusal rates on benign inputs and preserving response quality. Our results suggest that activating intrinsic safety-awareness during decoding offers a promising and complementary direction for defending against jailbreak attacks. Code is available at: https://github.com/zyz13590/SafeProbing.

</details>

### 25. ALERT: Zero-shot LLM Jailbreak Detection via Internal Discrepancy Amplification

📄 [arXiv](https://arxiv.org/abs/2601.03600)　📅 2026-01

**关键词**：`detection`、`zero-shot detection`、`internal discrepancy`、`gating activation`

👤 **作者**：Xiao Lin、…、Hanghang Tong

- 🎯 **研究动机**：现有越狱检测依赖训练数据中的越狱模板，无法应对新攻击持续涌现的零样本设定
- 🔬 **研究方法**：ALERT 逐层、逐模块、逐 token 放大良性与越狱 prompt 的内部特征差异，定位安全相关层、编码判别信号的模块与信息 token，并在放大表示上配两个互补分类器
- 📌 **结论**：三个安全基准上稳定位居前二，平均 Accuracy 与 F1 至少超第二名 10%、最高达 40%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite rich safety alignment strategies, large language models (LLMs) remain highly susceptible to jailbreak attacks, which compromise safety guardrails and pose serious security risks. Existing detection methods mainly detect jailbreak status relying on jailbreak templates present in the training data. However, few studies address the more realistic and challenging zero-shot jailbreak detection setting, where no jailbreak templates are available during training. This setting better reflects real-world scenarios where new attacks continually emerge and evolve. To address this challenge, we propose a layer-wise, module-wise, and token-wise amplification framework that progressively magnifies internal feature discrepancies between benign and jailbreak prompts. We uncover safety-relevant layers, identify specific modules that inherently encode zero-shot discriminative signals, and localize informative safety tokens. Building upon these insights, we introduce ALERT (Amplification-based Jailbreak Detector), an efficient and effective zero-shot jailbreak detector that introduces two independent yet complementary classifiers on amplified representations. Extensive experiments on three safety benchmarks demonstrate that ALERT achieves consistently strong zero-shot detection performance. Specifically, (i) across all datasets and attack strategies, ALERT reliably ranks among the top two methods, and (ii) it outperforms the second-best baseline by at least 10% in average Accuracy and F1-score, and sometimes by up to 40%.

</details>

### 26. ASGuard: Activation-Scaling Guard to Mitigate Targeted Jailbreaking Attack

📄 [arXiv](https://arxiv.org/abs/2509.25843) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10006702)　📅 2025-09　🏷 ICLR 2026

**关键词**：`defense`、`activation scaling`、`targeted jailbreak`、`inference-time guard`

👤 **作者**：Yein Park、Jungwoo Park、Jaewoo Kang

- 🎯 **研究动机**：时态越狱（改为过去时即合规）暴露对齐的泛化鸿沟，机制不明
- 🔬 **研究方法**：提出 ASGuard：电路分析定位与目标越狱因果相关的注意力头，训练通道级缩放向量重校准脆弱头激活，再融入预防性微调
- 📌 **结论**：四个 LLM 上降低目标越狱 ASR、保持通用能力并最小化过度拒绝，达安全-效用 Pareto 最优

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs), despite being safety-aligned, exhibit brittle refusal behaviors that can be circumvented by simple linguistic changes. As tense jailbreaking demonstrates that models refusing harmful requests often comply when rephrased in past tense, a critical generalization gap is revealed in current alignment methods whose underlying mechanisms are poorly understood. In this work, we introduce Activation-Scaling Guard (ASGuard), an insightful, mechanistically-informed framework that surgically mitigates this specific vulnerability. In the first step, we use circuit analysis to identify the specific attention heads causally linked to the targeted jailbreaking such as a tense-changing attack. Second, we train a precise, channel-wise scaling vector to recalibrate the activation of tense vulnerable heads. Lastly, we apply it into a "preventative fine-tuning", forcing the model to learn a more robust refusal mechanism. Across four LLMs, ASGuard effectively reduces the attack success rate of targeted jailbreaking while preserving general capabilities and minimizing over refusal, achieving a Pareto-optimal balance between safety and utility. Our findings underscore how adversarial suffixes suppress the propagation of the refusal-mediating direction, based on mechanistic analysis. Furthermore, our work showcases how a deep understanding of model internals can be leveraged to develop practical, efficient, and targeted methods for adjusting model behavior, charting a course for more reliable and interpretable AI safety.

</details>

### 27. AlcaTRAz - Anchored Tree-Rule Defense Against Jailbreaks

📄 [arXiv](https://arxiv.org/abs/2609.03693)　📅 2026-09

**关键词**：`defense`、`prompt-level rules`、`tree policy`、`jailbreak robustness`

👤 **作者**：Jakub Reš、Petr Kaška、Martin Perešíni、Martin Ukrop、Kamil Malinka

- 🎯 **研究动机**：多数防御需模型权重或内部访问，黑盒部署下 prompt 级防御又易损失良性效用
- 🔬 **研究方法**：提出 AlcaTRAz：自动学习可迁移的规则树变换，在选定位置插入受控字符级扰动以瓦解越狱利用的结构规律性，不改目标模型
- 📌 **结论**：33 个开源模型、22 类越狱上 73.4% 的模型-攻击组合取得最佳安全-功能综合分，综合分众数从 10（最严重顺从）变为 2（近拒答），benign 均分仅降 0.27；但高危尾部仍在且未测自适应攻击者

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are vulnerable to jailbreak attacks that bypass safety alignment through carefully crafted prompts. Many existing defenses require access to model weights or internals, making them difficult to apply to black-box deployments. We propose AlcaTRAz (Anchored Tree-Rule defense Against jailbreaks), a prompt-level defense based on rule trees that operates exclusively on the input text and requires no modification or retraining of the target model. The method automatically learns a transferable transformation rule that inserts controlled character-level perturbations at selected positions, thereby disrupting structural regularities exploited by jailbreak attacks while largely preserving the model's utility on benign queries. We evaluate the proposed method across 33 open-weight models, 22 jailbreak attack types, and a benchmark of short, single-turn benign questions, comparing against three representative prompt-level baselines (Llama Guard, RA-LLM, Goal Prioritization). Among the compared defenses, AlcaTRAz achieves the best composite security and functionality score in 73.4 % of model-attack combinations and shifts the aggregate score from a modal value of 10 (maximal-severity response to the malicious request) in the undefended setting to a modal value of 2 (near-refusal) after defense, while keeping the mean benign score within 0.27 points of the undefended baseline (8.35 vs. 8.62 on a 0-10 scale). AlcaTRAz substantially reduces but does not eliminate jailbreak success: a high-severity tail remains, and we do not consider adaptive attackers, so we position it as one layer within a defense-in-depth strategy rather than a standalone guarantee.

</details>

### 28. REINS: Refusal-Enhanced Inhibitory Steering with Sparse Autoencoder Features

📄 [arXiv](https://arxiv.org/abs/2608.28233)　📅 2026-08

**关键词**：`defense`、`analysis`、`behavioral access lock`、`harm-refusal separation`、`dual-feature control`、`inference-time SAE steering`

👤 **作者**：Kai-Xuan Ding、Hao-Xiang Xu、Ji-Hua Peng、Zi-Qi Chen、Jiaqi Wang、Zhen-Hua Ling

- 🎯 **研究动机**：复杂 wrapper 可使只增强单一拒绝方向的 SAE steering 失效，部分方法的表面安全实际来自模型崩溃
- 🔬 **研究方法**：构建含复杂包装有害 prompt 的 GUISE 数据集；提出 REINS，在同一 SAE 特征空间同时抑制有害 continuation 特征并增强安全拒绝特征
- 📌 **结论**：在 GUISE 与其他数据集上显著减少有害回答、大幅提升安全拒绝并基本保留通用能力，而先前方法干预过弱或仅靠崩溃达成表面安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Steering with Sparse Autoencoders (SAEs) offers a lightweight inference-time path for adapting the behavior of large language models without retraining. By exposing sparse and interpretable features, SAE steering provides a promising interface for safety control that guides harmful continuations toward refusal. However, we observe that complex wrappers can still undermine existing SAE steering methods on harmful prompts. To evaluate this failure mode systematically, we construct Generalized Undercover Instruction Safety Evaluation (GUISE), a dataset of harmful prompts with complex wrappers. Existing single direction SAE steering methods do not reliably produce refusals on harmful prompts, suggesting that refusal enhancement alone can be too weak when the harmful continuation path remains active. This motivates us to propose Refusal-Enhanced INhibitory Steering (REINS), which suppresses harmful continuation features and enhances safe refusal features in the same SAE feature space. Experiments on GUISE and other datasets show that prior methods either intervene too weakly or achieve only apparent safety through collapse, while REINS substantially reduces harmful responses, markedly improves safe refusals and largely preserves general capabilities.

</details>

### 29. Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense

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

### 30. COPA: Continual Preference Optimization for Adaptive Prompt Injection Defense

📄 [arXiv](https://arxiv.org/abs/2608.19982)　📅 2026-08

**关键词**：`defense`、`prompt injection`、`continual-learning defense`、`adaptive prompt injection`、`continual GRPO`、`margin-weighted replay`

👤 **作者**：Roshan Sood、Onat Gungor、Tajana Rosing

- 🎯 **研究动机**：提示注入防御以静态为主，需随新攻击策略重设计；终身对齐方法不应对持续演化的自适应对手
- 🔬 **研究方法**：COPA 把提示注入防御当终身学习：经 GRPO 增量纳入新观察攻击反馈，margin 加权经验回放保留对既有攻击类的防御
- 📌 **结论**：终身提示注入攻击流上 ASR 最高降 6.3 倍、平均 4.4 倍，优于 SOTA 防御并保留通用模型能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLMs remain vulnerable to prompt injection attacks, where adversarial instructions embedded in user inputs or external content manipulate model behavior and bypass safeguards. Existing defenses are predominantly static, relying on fixed alignment objectives or attack-specific filtering mechanisms that require redesign as new attack strategies emerge. While recent lifelong alignment methods address shifting user preferences, they do not account for adaptive adversaries that continually evolve to exploit weaknesses in previously learned defenses. This limitation is particularly important in real-world deployments, where evolving attack distributions necessitate continual adaptation without sacrificing robustness to previously encountered threats. We present COPA, a continual preference optimization framework that treats prompt-injection defense as a lifelong learning problem. Instead of one-time alignment, COPA incrementally incorporates feedback from newly observed attacks via GRPO-based optimization and uses margin-weighted experience replay to retain defenses against prior attack classes. This enables continuous adaptation to emerging threats while mitigating catastrophic forgetting and preserving general-purpose model capabilities. Across lifelong prompt injection attack streams, COPA reduces attack success rate by up to 6.3x and 4.4x on average compared to state-of-the-art defenses. These results highlight continual preference optimization as an effective paradigm for defending LLMs against adaptive adversaries.

</details>

### 31. CLEAR: Continuous Latent Adapter Routing for Utility-Preserving LLM Safety Alignment

📄 [arXiv](https://arxiv.org/abs/2608.21278)　📅 2026-08

**关键词**：`defense`、`parameter-efficient safety tuning`、`adapter routing`、`utility retention`、`conditional jailbreak defense`、`latent gate`

👤 **作者**：Chengxiao Wang、Enyi Jiang、Xiaojing Liao、Sanmi Koyejo

- 🎯 **研究动机**：全局安全微调同时作用于有害与无害输入，LLM 安全提升以 utility 下降为代价
- 🔬 **研究方法**：CLEAR 条件安全适配框架，用轻量 hidden-state gate 连续控制 safety 低秩 adapter 的激活强度，冻结骨干不全局改动
- 📌 **结论**：Llama-3-8B-Instruct 上 HarmBench ASR 从 32.3% 降至 0.5%，GSM8K 准确率比全局 SFT/LoRA 最高多 7.1 个百分点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Improving the safety of large language models (LLMs) often comes at the expense of utility, as globally applied safety tuning may affect model responses to both harmful and benign inputs. We propose \textbf{C}ontinuous \textbf{L}at\textbf{E}nt \textbf{A}dapter \textbf{R}outing (CLEAR), a conditional safety adaptation framework that uses a lightweight hidden-state gate to continuously control the activation strength of a safety low-rank adapter. CLEAR aims to reduce harmful completions while avoiding unnecessary changes to the frozen backbone that could degrade performance on benign prompts. Experiments on widely used safety and utility benchmarks show that CLEAR improves robustness on HarmBench while reducing the utility degradation observed with globally applied safety tuning such as SFT or standard low-rank adaptation (LoRA). On Llama-3-8B-Instruct, CLEAR reduces HarmBench ASR from 32.3\% to 0.5\%, while retaining most of the base model's utility and achieving up to 7.1 percentage points higher GSM8K accuracy than globally applied SFT or LoRA. These results suggest that CLEAR is a promising mechanism for improving the safety--utility trade-off in LLM alignment.

</details>

### 32. Certified Multi-Turn Robustness for LLM Safety via Compositional Bounds and Safety Persistence

📄 [arXiv](https://arxiv.org/abs/2608.20820)　📅 2026-08

**关键词**：`defense`、`analysis`、`multi-turn certification`、`safety persistence`、`Crescendo attack`、`certified safety evaluation`

👤 **作者**：Yang Liu、…、Pluto Zhou

- 🎯 **研究动机**：多轮 jailbreak 会逐步操纵对话上下文，而现有认证鲁棒方法只覆盖单轮输入，朴素多轮组合的界随轮数指数退化
- 🔬 **研究方法**：MTCR 用 State-Adversarial MDP 建模对话安全，基于嵌入空间模式分解做组合认证，引入 (α,β)-safety persistence 改善退化率，并给出匹配的信息论上界
- 📌 **结论**：衰减率从 p^k 收紧为 β^k（β>p）；六个 LLM 在 ε-有界与 Crescendo 式攻击下经验安全率均高于认证下界

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are vulnerable to multi-turn jailbreak attacks that progressively manipulate conversation context. Existing certified robustness methods are limited to single-turn inputs; naive multi-turn composition yields bounds that degrade exponentially in the number of turns. We introduce Multi-Turn Certified Robustness (MTCR), a framework that models conversational safety via State-Adversarial MDPs and defines $k$-turn certified robustness as the worst-case safety probability across $k$ adversarial turns. MTCR comprises: (i) compositional certification via embedding-space mode decomposition, yielding tighter certified lower bounds than naive multiplication; (ii) $(α,β)$-safety persistence, improving the degradation rate from $\underline{p}^{k}$ to $β^k$ (with $β> \underline{p}$) and yielding interpretable horizon estimates; (iii) matching information-theoretic upper bounds establishing tightness; and (iv) a unified algorithm combining these results. Experiments on six LLMs under $ε$-bounded and Crescendo-style attacks confirm that empirical safety consistently exceeds the certified bounds.

</details>

### 33. A Self-Evolving Multi-Agent Framework Defense against LLM Jailbreak Attacks

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

### 34. SkillShield: Prompt-Space Security Skills for LLM Coding Agents

📄 [arXiv](https://arxiv.org/abs/2608.25817)　📅 2026-08

**关键词**：`defense`、`coding agent`、`prompt-space policy`、`malware prevention`、`system-prompt safeguard`、`persistent policy`

👤 **作者**：Xiaodong Wu、…、Jianbing Ni

- 🎯 **研究动机**：coding Agent 以开发者权限执行命令，weight 级对齐对 API 部署方不可用，输入过滤与执行监控又需辅助组件
- 🔬 **研究方法**：SkillShield 离线从已知攻击合成 security skill 注入 system prompt 并在整个工具循环生效，考察三种固定预算配置
- 📌 **结论**：RedCode 上 all-classes skill 把恶意软件生成严重度从 3.37 降至 0.58，执行 ASR 43.6% 媲美 Llama Guard 3 且无需 8B 分类器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A coding agent edits files and executes shell commands with its developer's privileges, allowing malicious requests to translate directly into harmful actions or functional malware. Existing defenses have complementary limitations: weight-level alignment is unavailable to API-only deployers, whereas input filters and execution-boundary monitors require auxiliary classification or checking components along the agent's trajectory. We therefore introduce SkillShield, a system-prompt defense that synthesizes security skills offline from known attacks or recorded agent failures. These skills are injected into the system prompt at session start and remain active throughout the tool-use loop. Unlike a reference monitor, they protect the system by defining the security policies the model should follow during execution. Due to the limited system-prompt space, we examine three fixed-budget provisioning scopes: all-classes, with one skill covering all threat classes, per-bundle, with one skill targeting a related subset, and per-class, with one skill dedicated to a single known class and used as the upper-bound reference. None requires runtime request classification or routing. Across six large language models on RedCode, the default all-classes skill reduces malware-generation severity from 3.37 to 0.58 and achieves a 43.6% execution attack success rate, comparable to Llama Guard 3's 42.7% without its separate 8B classifier. The per-bundle and class-fixed per-class settings further reduce this rate to 36.2% and 14.5%, respectively. Under two non-adaptive jailbreak families, SkillShield continues to outperform all baselines on malware generation. Across 731 benign task descriptions, SkillShield yields a mean safety-refusal rate of 0.14%. These results demonstrate the potential of prompt-space security skills to prevent harmful actions and malware generation for LLM coding agents.

</details>

### 35. Hidden in the Request: Explaining Unethical LLM Compliance through Token Relevance

📄 [arXiv](https://arxiv.org/abs/2608.23264)　📅 2026-08

**关键词**：`analysis`、`defense`、`implicit harmful request`、`task-framing shortcut`、`token safety boundary`、`LRP-guided decoding`

👤 **作者**：Or Biton、Tomer Krichli、Itai Allouche、Joseph Keshet

- 🎯 **研究动机**：helpfulness 与 harmlessness 双目标冲突导致对齐失败，模型在"请求帮助"式不道德场景中明显退化，机理不明
- 🔬 **研究方法**：以客观分类、主观第一人称、直接求助三种结构呈现不道德场景，用 LRP 追踪到归因偏差：模型更重视良性任务框架 token（如 Can you help me）而非标记不道德行为的 cue-token（如 without getting caught），并提出两种 LRP 引导解码把生成引向与 cue token 更相关的轨迹
- 📌 **结论**：干预促成更安全回应，支持 cue-token 归因不足是有害顺从成因的解释，token relevance 可作推理时防护信号

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Although Large Language Models (LLMs) are aligned to optimize for both helpfulness and harmlessness, these dual objectives may conflict, inevitably leading to alignment failures. This work systematically investigates instances where LLMs fail to exhibit ethical behavior. To understand the underlying mechanics of these vulnerabilities, we introduce a probing methodology that presents unethical scenarios to LLMs in three distinct structural modalities: objective classification tasks, subjective first-person statements, and direct requests for assistance. We find that model performance degrades in the request-for-assistance-based form. Using Layer-wise Relevance Propagation (LRP), we trace this discrepancy to an attribution bias: the model places greater emphasis on benign task-framing tokens (e.g., "Can you help me...") than on tokens signaling the underlying unethical behavior (e.g., "without getting caught"), which we term cue-tokens. We hypothesize that this under-attribution contributes to harmful compliance. To test this, we introduce two LRP-guided decoding methods that steer generation toward trajectories more relevant to cue tokens. Empirical evaluations show that these interventions promote safer responses, supporting cue-token attribution's role in compliance failures.

</details>

### 36. SafeSpec: Fast and Safe LLM via Dynamic Reflective Sampling

📄 [arXiv](https://arxiv.org/abs/2606.19755) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64117)　📅 2026-06　🏷 ICML 2026

**关键词**：`defense`、`speculative decoding`、`risk-aware verification`、`reflective sampling`、`safety alignment`、`mechanistic analysis`

👤 **作者**：Haotian Xu、Zeyang Zhang、Linbao Li、Huadi Zheng、Yu Li、Cheng Zhuo

- 🎯 **研究动机**：投机推理加速解码但无内生安全保证，已有防御引入额外计算或破坏 draft-verify 机制而抵消加速收益
- 🔬 **研究方法**：提出 SafeSpec：在目标模型上挂轻量潜安全头，单次前向联合评估语义有效性与安全性，检出不安全时回滚并做安全引导的反思多次采样恢复安全续写，把越狱建模为生成轨迹的分布偏移
- 📌 **结论**：Qwen3-32B 上 ASR 降低 15% 同时保持 2.06 倍推理加速，证明投机加速与推理时安全可联合优化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Speculative inference accelerates large language model (LLM) decoding but provides no inherent safety guarantees. Existing safety defenses are largely incompatible with speculative inference: they either introduce additional computation or disrupt the draft-verify mechanism, negating acceleration benefits. This reveals a fundamental incompatibility between current safety methods and speculative decoding. We propose SafeSpec, a safety-aware speculative inference framework that integrates risk estimation directly into the verification process. SafeSpec attaches a lightweight latent safety head to the target model to jointly evaluate semantic validity and safety in a single forward pass. When unsafe generations are detected, SafeSpec applies rollback and safety-guided reflective multi-sampling to recover safe continuations rather than terminating generation. We model jailbreak attacks as distributional shifts over generative trajectories, where adversarial prompts increase the probability of harmful continuations without eliminating safe ones. Under this model, SafeSpec performs risk-aware trajectory recovery within the speculative decoding process. Across multiple models and adversarial benchmarks, SafeSpec achieves a substantially improved safety-efficiency trade-off. On Qwen3-32B, SafeSpec reduces attack success rates by 15% while preserving a 2.06x inference speedup on benign workloads, demonstrating that speculative acceleration and inference-time safety can be jointly optimized.

</details>

### 37. Latent Space Refusal Anchoring for Low-Resource African Languages: Mechanistic Safety Recovery Without Retraining

📄 [arXiv](https://arxiv.org/abs/2608.18089) · 📝 [OpenReview](https://openreview.net/forum?id=4UwS3bn1fB)　📅 2026-08

**关键词**：`defense`、`analysis`、`multilingual safety recovery`、`refusal anchoring`、`cross-language transfer`、`cross-lingual refusal`

👤 **作者**：Godwin Abuh Faruna

- 🎯 **研究动机**：指令模型英语拒答但 Yoruba、Igbo、Igala、Hausa 合规，恢复拒答通常需标注目标语数据与重训
- 🔬 **研究方法**：LSR-Anchoring 免训练从英语 prompt 提取拒答方向并在推理时 clamp 到残差流：MAS 跨四架构；SAE-Derived Steering 以单个 SAE 特征替换稠密方向
- 📌 **结论**：Mistral 与 Qwen 上恢复安全且良性退化低于 0.08；SDS 把 KL 散度降 3.5-7 倍避免良性崩溃；MMLU 掉分始终低于 0.35 个百分点，但 Arabic 在所有架构与强度下失败

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Instruction-tuned models often refuse harmful requests in English but comply with the same requests in Yoruba, Igbo, Igala, and Hausa. This suggests that the refusal mechanism is present in the residual stream but fails to activate for low-resource inputs. Recovering it normally requires labelled target-language data and retraining, neither of which is available at scale for most African languages. We introduce Latent Space Refusal Anchoring (LSR-Anchoring), a training-free method that extracts the refusal direction from English prompts and clamps it onto the residual stream at inference time. The primary variant, Mean-Activation Steering (MAS), operates across the four architectures we tested: Llama-3-8B, Llama-3.1-70B, Mistral-7B-Instruct, and Qwen2.5-7B. On Mistral and Qwen it recovers safety with benign degradation below 0.08. On Llama-3-8B it overcorrects, with Degraded Performance on Legitimate prompts (DPL) reaching 1.00. We address this with SAE-Derived Steering (SDS), which replaces the dense mean-difference direction with a single Sparse Autoencoder (SAE) feature and reduces Kullback-Leibler (KL) divergence by 3.5-7x without benign collapse. Four languages transfer positively, but Arabic fails on every architecture and at every steering magnitude, indicating a geometric mismatch rather than a baseline effect. Massive Multitask Language Understanding (MMLU) accuracy drops remain below 0.35 percentage points at every effective steering magnitude.

</details>

### 38. Defending Jailbreak Attacks on Large Language Models via Manifold Trajectory Kinetics

📄 [arXiv](https://arxiv.org/abs/2606.07335) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-hangtao)　📅 2026-06　🏷 USENIX Security 2026

**关键词**：`defense`、`detection`、`LLM jailbreak`、`manifold trajectory`、`jailbreak`、`adaptive attack`

👤 **作者**：Hangtao Zhang、…、Leo Yu Zhang

- 🎯 **研究动机**：基于固定度量空间的越狱检测在伪恶意提示（含安全关键词的良性意图）与自适应攻击下线性可分假设失效
- 🔬 **研究方法**：提出 MTK，把 LLM 视为动力系统，追踪提示邻域结构跨层演化：良性提示始终贴近良性邻域，越狱提示先近恶意种子后策略性转向良性邻域
- 📌 **结论**：四个 LLM、十种攻击上：伪恶意提示 TPR 95%（良性 FPR 5%、伪恶意 FPR 2%），自适应攻击下仍保持 85% TPR，并扩展到 VLM

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak prompts can bypass alignment guardrails in large language models (LLMs) and elicit unsafe outputs, making reliable deployment-time detection critical. Prior detection approaches largely rely on a fixed metric space, e.g., raw inputs, gradients, or hidden features, in which benign and jailbreak prompts are linearly separable. We show this assumption breaks under (i) pseudo-malicious prompts that are benign by intent but contain safety-related keywords, and (ii) adaptive attacks that explicitly optimize against the deployed detector. To overcome this limitation, we shift our focus from identifying a universal metric space to analyzing the more robust neighborhood structure of the underlying data manifold. We present Manifold Trajectory Kinetics (MTK), which treats an LLM as a kinetic system transforming inputs into outputs and detects jailbreaks by tracking how a prompt's neighborhood structure evolves across layers. Benign prompts remain close to benign neighborhoods throughout inference, whereas jailbreak prompts exhibit a characteristic trajectory that begins near malicious seeds and later strategically shifts toward benign neighborhoods to evade refusal.Across four LLMs and ten jailbreak attacks, MTK achieves strong robustness to both failure modes: on pseudo-malicious prompts, it attains a jailbreak true positive rate of 95% at a false positive rate of 5% on benign prompts and 2% on pseudo-malicious prompts, and under adaptive attacks, it maintains a true positive rate of 85%. We further demonstrate the superior performance of MTK for jailbreak detection in vision-language models. Our code is available at https://github.com/Rookie143/mtk.

</details>

### 39. THRD: A Training-Free Multi-Turn Defense Framework for Jailbreak Attacks on Large Language Models

📄 [arXiv](https://arxiv.org/abs/2606.01738)　📅 2026-06

**关键词**：`defense`、`multi-turn defense`、`temporal risk accumulation`、`training-free`

👤 **作者**：Zhiqing Ma、Zhonghao Xu、Dong Yu、Chen Kang、Changliang Li、Pengyuan Liu

- 🎯 **研究动机**：多轮越狱利用渐进升级与跨轮协同，现有防御重训昂贵或逐轮孤立分析，漏掉风险沿轨迹的累积
- 🔬 **研究方法**：THRD 免训练显式建模时序风险累积：轮级风险评估器、历史上下文分析器、响应评估器与带衰减调制和趋势感知的时变评分决策模块
- 📌 **结论**：对树搜索与多 agent 协作等 SOTA 多轮攻击把 ASR 降到 0.2-4.0%，MMLU 与 GSM8K 退化在 1.5% 内；超 70% 攻击需第 2 轮及以后才能检出，验证时序聚合的必要性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-turn jailbreak attacks pose a growing threat to LLMs by exploiting conversational dynamics such as gradual escalation and cross-turn coordination. Existing defenses either rely on costly retraining -- often degrading model utility -- or apply single-turn analysis independently at each turn, failing to capture how risk accumulates along interaction trajectories. We observe that safety behavior in multi-turn interaction is trajectory-dependent: dialogue history continuously reshapes the model's conditioning context, making it insufficient to evaluate each turn in isolation. Motivated by this insight, we present THRD, the first training-free framework that explicitly models temporal risk accumulation for multi-turn jailbreak defense. THRD integrates four modules: a Turn-level Risk Assessor (TRA) for instantaneous risk estimation, a Historical Context Analyzer (HCA) for cross-turn intent escalation detection, a Response Evaluator (RE) for identifying facilitative outputs, and a Decision Module that combines these signals through a time-evolving scoring mechanism with attenuation-based modulation and trend-aware adjustment. Experiments against state-of-the-art multi-turn attacks -- including tree-search-based and multi-agent collaborative methods -- across two target models show that THRD reduces ASR to 0.2--4.0% while preserving model utility within 1.5% degradation on MMLU and GSM8K. Ablation studies confirm non-redundant module contributions and stable cross-architecture generalization. Analysis of first rejection triggers reveals that over 70% of multi-turn attacks require Turn~2 or later to detect, validating the necessity of explicit temporal aggregation.

</details>

### 40. REFLECTOR: Internalizing Step-wise Reflection against Indirect Jailbreak

📄 [arXiv](https://arxiv.org/abs/2605.20654) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60648)　📅 2026-05　🏷 ICML 2026

**关键词**：`defense`、`step-wise reflection`、`indirect jailbreak`、`self-correction`

👤 **作者**：Jiachen Ma、Jiawen Zhang、Xiangtian Li、Bo Zou、Chaochao Lu、Chao Yang

- 🎯 **研究动机**：多步越狱利用内部生成过程绕过表层对齐，现有防御难以捕捉
- 🔬 **研究方法**：Reflector 两阶段：teacher 引导生成高质量反思数据做 SFT 建立结构化反思模式，再以结果驱动与奖励有效性监督的 RL 内化自主反思
- 📌 **结论**：对复杂间接攻击 DSR 超 90% 且跨威胁场景泛化，同时 GSM8K 提升 5.85%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While Large Language Models (LLMs) demonstrate remarkable capabilities, they remain susceptible to sophisticated, multi-step jailbreak attacks that circumvent conventional surface-level safety alignment by exploiting the internal generation process. To address these vulnerabilities, we propose Reflector, a principled two-stage framework that internalizes self-reflection within the generation trajectory. Reflector first leverages teacher-guided generation to produce high-quality reflection data for supervised fine-tuning (SFT), establishing structured reflection patterns. It subsequently uses Reinforcement Learning (RL) with outcome-driven and reward-validity supervision to instill robust, autonomous self-reflection capabilities. Empirical results show that Reflector achieves Defense Success Rates (DSR) exceeding 90% against complex indirect attacks while generalizing robustly across diverse threat scenarios. Notably, the framework enhances both task-specific and general utility, yielding a 5.85% gain on GSM8K alongside improved performance on knowledge-intensive benchmarks. By internalizing trajectory-level safety, Reflector overcomes the fundamental limitations of surface alignment without significant computational overhead, offering an efficient and scalable solution for the development of safe and capable LLMs.

</details>

### 41. Mitigating Many-shot Jailbreak Attacks with One Single Demonstration

📄 [arXiv](https://arxiv.org/abs/2605.08277)　📅 2026-05

**关键词**：`defense`、`many-shot jailbreak`、`SafeEnd`、`representation restoration`

👤 **作者**：Kejia Chen、…、Tianwei Zhang

- 🎯 **研究动机**：many-shot 越狱随有害示范数量增强的机制不明
- 🔬 **研究方法**：实证发现有害示范引起渐进激活漂移，理论证明条件化 N 个有害示范等价于对 N 个有害样本的 SGD 式更新；SafeEnd 在推理时追加固定单例安全示范诱导反向安全更新
- 📌 **结论**：不修改参数、无需白盒访问即可恢复拒答行为，显著提升对 MSJ 的鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Many-shot jailbreaking (MSJ) causes safety-aligned language models to answer harmful queries by preceding them with many harmful question-answer demonstrations. We study why this attack becomes stronger as the number of demonstrations increases. Empirically, we find that MSJ induces a progressive activation drift: the representation of a fixed harmful query moves step by step away from the safety-aligned region as more harmful demonstrations are added. Theoretically, we show that this drift can be interpreted as implicit malicious fine-tuning: conditioning on N harmful demonstrations induces SGD-style updates equivalent to optimizing on the corresponding N harmful samples. This view turns the attack mechanism into a defense principle. We append a fixed one-shot safety demonstration at inference time, which induces a counteracting safety-oriented update and restores refusal behavior. The resulting method improves the model's robustness to MSJ without modifying its parameters or requiring white-box access at deployment. Code is available at https://github.com/Thecommonirin/SafeEnd.

</details>

### 42. Contrastive Reasoning Alignment: Reinforcement Learning from Hidden Representations

📄 [arXiv](https://arxiv.org/abs/2603.17305) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66283)　📅 2026-03　🏷 ICML 2026

**关键词**：`defense`、`contrastive learning`、`jailbreak defense`、`harmful intent detection`、`prompt injection`、`runtime defense`

👤 **作者**：Haozheng Luo、Yimin Wang、Jiahao Yu、Binghui Wang、Yan Chen

- 🎯 **研究动机**：输出级防御无法阻止推理模型生成不安全的推理轨迹
- 🔬 **研究方法**：CRAFT 把对比表示学习与 RL 结合，在隐状态空间分离安全与不安全轨迹；理论上证明把潜-文本一致性纳入 GRPO 可排除表面对齐的局部最优
- 📌 **结论**：在 Qwen3-4B-Thinking 与 R1-Distill-Llama-8B 上推理安全平均提升 79.0%、最终回复安全提升 87.7%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We propose CRAFT, a red-teaming alignment framework that leverages model reasoning capabilities and hidden representations to improve robustness against jailbreak attacks. Unlike prior defenses that operate primarily at the output level, CRAFT aligns large reasoning models to generate safety-aware reasoning traces by explicitly optimizing objectives defined over the hidden state space. Methodologically, CRAFT integrates contrastive representation learning with reinforcement learning to separate safe and unsafe reasoning trajectories, yielding a latent-space geometry that supports robust, reasoning-level safety alignment. Theoretically, we show that incorporating latent-textual consistency into GRPO eliminates superficially aligned policies by ruling them out as local optima. Empirically, we evaluate CRAFT on multiple safety benchmarks using two strong reasoning models, Qwen3-4B-Thinking and R1-Distill-Llama-8B, where it consistently outperforms state-of-the-art defenses such as IPO and SafeKey. Notably, CRAFT delivers an average 79.0% improvement in reasoning safety and 87.7% improvement in final-response safety over the base models, demonstrating the effectiveness of hidden-space reasoning alignment.

</details>

### 43. HoneyTrap: Deceiving Large Language Model Attackers to Honeypot Traps with Resilient Multi-Agent Defense

📄 [arXiv](https://arxiv.org/abs/2601.04034)　📅 2026-01

**关键词**：`defense`、`multi-agent honeypot`、`attacker deception`、`resource exhaustion`

👤 **作者**：Siyuan Li、…、Jianhua Li

- 🎯 **研究动机**：被动防御难以跟上持续深化的多轮越狱，需要主动欺骗并消耗攻击者资源
- 🔬 **研究方法**：HoneyTrap 集成 Threat Interceptor、Misdirection Controller、Forensic Tracker 与 System Harmonizer 四个防御 agent 协作实施欺骗式防御，并发布 MTJ-Pro 多轮渐进越狱数据集及 MSR、ARC 两个指标
- 📌 **结论**：ASR 较 SOTA 平均降 68.77%；误导率与攻击资源消耗分别提升 118.11% 与 149.16%，自适应攻击下仍稳健且不影响良性查询

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak attacks pose significant threats to large language models (LLMs), enabling attackers to bypass safeguards. However, existing reactive defense approaches struggle to keep up with the rapidly evolving multi-turn jailbreaks, where attackers continuously deepen their attacks to exploit vulnerabilities. To address this critical challenge, we propose HoneyTrap, a novel deceptive LLM defense framework leveraging collaborative defenders to counter jailbreak attacks. It integrates four defensive agents, Threat Interceptor, Misdirection Controller, Forensic Tracker, and System Harmonizer, each performing a specialized security role and collaborating to complete a deceptive defense. To ensure a comprehensive evaluation, we introduce MTJ-Pro, a challenging multi-turn progressive jailbreak dataset that combines seven advanced jailbreak strategies designed to gradually deepen attack strategies across multi-turn attacks. Besides, we present two novel metrics: Mislead Success Rate (MSR) and Attack Resource Consumption (ARC), which provide more nuanced assessments of deceptive defense beyond conventional measures. Experimental results on GPT-4, GPT-3.5-turbo, Gemini-1.5-pro, and LLaMa-3.1 demonstrate that HoneyTrap achieves an average reduction of 68.77% in attack success rates compared to state-of-the-art baselines. Notably, even in a dedicated adaptive attacker setting with intensified conditions, HoneyTrap remains resilient, leveraging deceptive engagement to prolong interactions, significantly increasing the time and computational costs required for successful exploitation. Unlike simple rejection, HoneyTrap strategically wastes attacker resources without impacting benign queries, improving MSR and ARC by 118.11% and 149.16%, respectively.

</details>

### 44. SpatialJB: How Text Distribution Art Becomes The "Jailbreak Key" for LLM Guardrails

📄 [arXiv](https://arxiv.org/abs/2601.09321) · 🌐 [Project](https://1drv.ms/v/s!ApaP6YaJA87pgk-Rk7ZCvPeYcIZa?e=J8kbg0) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65200)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`jailbreak`、`jailbreak defense`、`harmful intent detection`、`prompt injection`、`mechanistic analysis`

👤 **作者**：Zhiyi Mou、…、Kui Ren

- 🎯 **研究动机**：自回归 token 推理使 LLM 语义表征对空间结构扰动不鲁棒，现有输出护栏因此可被穿透
- 🔬 **研究方法**：提出 SpatialJB，用文本分布艺术扰动模型的输出生成过程，使有害内容绕过护栏检测，并给出对应基线防御
- 📌 **结论**：在主流 LLM 上接近 100% ASR，对 OpenAI Moderation API 等先进输出护栏成功率仍超 75%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While Large Language Models (LLMs) have achieved remarkable success across diverse tasks, they remain vulnerable to jailbreak attacks, which pose significant risks to their secure deployment. Driven by their inherent token-by-token autoregressive inference, LLMs exhibit semantic representations that lack robustness against spatially structured perturbations, thereby rendering current output-guardrail safety mechanisms penetrable. Exploiting the Transformer's spatial weakness, we propose SpatialJB to disrupt the model’s output generation process, allowing harmful content to bypass guardrails without detection. Comprehensive experiments on leading LLMs demonstrate that SpatialJB achieves a nearly 100\% ASR and consistently maintains a success rate exceeding 75\% even against advanced output guardrails like the OpenAI Moderation API, outperforming current jailbreak techniques by a significant margin. While SpatialJB advances LLM safety research by exposing guardrail weaknesses and highlighting spatial semantics, we also propose and evaluate baseline defense strategies to prevent its potential misuse. You can click Video Link and Code Link to see our demo presentation and code.

</details>

### 45. SafetyMem: Adaptive Jailbreak Defense via Dual-Component Safety Memory

🎓 [Official](https://aclanthology.org/2026.acl-long.1168/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`LLM jailbreak`、`jailbreak defense`、`jailbreak`、`prompt injection`

👤 **作者**：Hao Wang、Ziyi Ni、Huacan Wang、Pin Lyu、Lei Sha

- 🎯 **研究动机**：现有防御存在记忆鸿沟：改参数方法计算僵硬，推理时过滤器无法跨交互保留复用防御知识
- 🔬 **研究方法**：提出 SafetyMem 双部件安全记忆：语义安全记忆（SSM）把越狱尝试固化为攻击模式知识库，情景安全记忆（ESM）维护从历史检测失败提炼的规则集，并以对抗记忆扩展主动生成困难变体
- 📌 **结论**：在标准与隐蔽越狱基准上大幅降低攻击成功率，无需重训练即超越 SOTA 基线，兼顾效率与可解释性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current defenses for Large Language Models (LLMs) often suffer from a ”memory gap”: parameter-modifying methods are computationally rigid, while inference-time filters cannot retain or reuse defense knowledge across interactions. To address this, we propose SafetyMem, a novel framework that secures LLMs through a dual-component safety memory system. SafetyMem consists of Semantic Safety Memory (SSM), which consolidates diverse jailbreak attempts into a structured knowledge base of attack patterns, and Episodic Safety Memory (ESM), which maintains an evolving set of procedural rules refined from historical detection failures. Unlike static defenses, SafetyMem allows the model to ”remember” and adapt to emerging adversarial strategies without parameter retraining. To further enhance robustness, we introduce an adversarial memory expansion mechanism that proactively generates challenging variants to solidify these memories. Experiments on standard and stealthy jailbreak benchmarks show that SafetyMem substantially reduces attack success rates while preserving efficiency and interpretability, consistently outperforming state-of-the-art baselines across multiple LLMs.

</details>

### 46. Retrieval-Augmented Defense: Adaptive and Controllable Jailbreak Prevention for Large Language Models

🎓 [Official](https://aclanthology.org/2026.acl-long.1895/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`jailbreak defense`、`jailbreak`、`harmful intent detection`、`LLM jailbreak`、`RAG security`

👤 **作者**：Guangyu Yang、Jinghong Chen、Jingbiao Mei、Weizhe Lin、Bill Byrne

- 🎯 **研究动机**：越狱攻击持续演化，防御系统难以在不重训练的情况下适配新攻击并控制安全-效用权衡
- 🔬 **研究方法**：提出 RAD：将已知攻击样本库纳入 RAG 推断恶意查询与所用越狱策略，实现免训练更新与可调节的安全-效用平衡
- 📌 **结论**：在 StrongREJECT 上大幅削弱 PAP、PAIR 等强攻击，同时保持对良性查询的低拒绝率并跨工作点可控

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) remain vulnerable to jailbreak attacks, which attempt to elicit harmful responses from LLMs. The evolving nature and diversity of these attacks pose many challenges for defense systems, including (1) adaptation to counter emerging attack strategies without costly retraining, and (2) control of the trade-off between safety and utility. To address these challenges, we propose Retrieval-Augmented Defense (RAD), a novel framework for jailbreak detection that incorporates a database of known attack examples into Retrieval-Augmented Generation, which is used to infer the underlying, malicious user query and jailbreak strategy used to attack the system. RAD enables training-free updates for newly discovered jailbreak strategies and provides a mechanism to balance safety and utility. Experiments on StrongREJECT show that RAD substantially reduces the effectiveness of strong jailbreak attacks such as PAP and PAIR while maintaining low rejection rates for benign queries. We propose a novel evaluation scheme and show that RAD achieves a robust safety-utility trade-off across a range of operating points in a controllable manner.

</details>

### 47. RedDebate: Safer Responses Through Multi-Agent Red Teaming Debates

📄 [arXiv](https://arxiv.org/abs/2506.11083) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66085)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`multi-agent evaluation`、`multi-agent system`、`jailbreak defense`、`LLM jailbreak`、`attack transferability`

👤 **作者**：Ali Asad、Stephen Obadinma、Radin Shayanfar、Xiaodan Zhu

- 🎯 **研究动机**：现有 AI 安全方法依赖昂贵人工评估或孤立单模型评估，受可扩展性与 oversight 失败限制
- 🔬 **研究方法**：提出 RedDebate：多个 LLM 在多样辩论场景中互相批判推理、自动红队发现不安全失败模式，并用长期记忆模块跨推理复用安全洞见
- 📌 **结论**：在多个安全基准上显著减少不安全输出，记忆模块带来进一步显著下降，实现无需人工的持续安全改进

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce RedDebate, a novel multi-agent debate framework that provides the foundation for Large Language Models (LLMs) to identify and mitigate their own unsafe behaviors. Existing AI safety approaches often rely on costly human evaluation or isolated single-model assessment, both constrained by scalability and prone to oversight failures. RedDebate employs collaborative argumentation among multiple LLMs across diverse debate scenarios, enabling them to critically evaluate one another’s reasoning and systematically uncover unsafe failure modes through fully automated red-teaming. We further integrate distinct long-term memory modules that preserve safety-relevant insights from debate interactions and leverage them during subsequent inference, facilitating continuous refinement of model behavior. Empirical evaluation on safety benchmarks across a diverse set of models demonstrates that RedDebate substantially reduces unsafe outputs. While debate alone allows LLMs to refine their behavior, the addition of memory modules yields further significant reductions. To the best of our knowledge, RedDebate is the first fully automated framework to unify multi-agent debate and red-teaming to progressively enhance LLM safety without human intervention.

</details>

### 48. Defenses Against Prompt Attacks Learn Surface Heuristics

🎓 [Official](https://aclanthology.org/2026.acl-long.502/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`jailbreak defense`、`harmful intent detection`、`utility preservation`、`prompt injection`

👤 **作者**：Li Li、…、Yue Zhao

- 🎯 **研究动机**：监督微调的提示攻击防御学到的是防御数据中的窄相关而非有害意图，导致系统性拒绝安全输入
- 🔬 **研究方法**：分析三种捷径：位置偏置（后置良性任务被拒率从 10% 升至 90%）、token 触发偏置（单个触发 token 增加最高 50% 假拒绝）、主题泛化偏置（测试准确率掉最高 40%），并构建受控诊断集
- 📌 **结论**：当前提示注入防御响应的是攻击样表面模式而非底层意图，监督微调不足以支撑可靠 LLM 安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed in security-sensitive applications, where they must follow system- or developer-specified instructions that define the intended task behavior, while completing benign user requests. When adversarial instructions appear in user queries or externally retrieved content, models may override intended logic. Recent defenses rely on supervised fine-tuning with benign and malicious labels. Although these methods achieve high attack rejection rates, we find that they rely on narrow correlations in defense data rather than harmful intent, leading to systematic rejection of safe inputs. We analyze three recurring shortcut behaviors induced by defense fine-tuning. Position bias arises when benign content placed later in a prompt is rejected at much higher rates; across reasoning benchmarks, suffix-task rejection rises from below 10% to as high as 90%. Token trigger bias occurs when strings common in attack data raise rejection probability even in benign contexts; inserting a single trigger token increases false refusals by up to 50%. Topic generalization bias reflects poor generalization beyond the defense data distribution, with defended models suffering test-time accuracy drops of up to 40%. These findings suggest that current prompt-injection defenses frequently respond to attack-like surface patterns rather than the underlying intent. We introduce controlled diagnostic datasets and a systematic evaluation across two base models and multiple defense pipelines, highlighting limitations of supervised fine-tuning for reliable LLM security.

</details>

### 49. Stay in Character, Stay Safe: Dual-Cycle Adversarial Self-Evolution for Role-Playing Agents

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/5873.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`role-playing Agent`、`persona-aware guard`、`retrieved safety rule`、`jailbreak`、`self-evolution`

- 🎯 **研究动机**：角色扮演 agent 越忠于人设越易被越狱，训练时方案维护成本高、损害角色内行为且对闭源模型不可行
- 🔬 **研究方法**：提出免训练双循环对抗自进化：攻击循环合成渐进更强的越狱提示，防御循环把失败蒸馏为全局安全规则、角色约束与安全角色示例的层级知识库供推理时检索组合
- 📌 **结论**：多个专有 LLM 上角色保真与抗越狱均超过强基线，并对未见角色与攻击提示鲁棒泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based role-playing has rapidly improved in fidelity, yet stronger adherence to persona constraints commonly increases vulnerability to jailbreak attacks, especially for risky or negative personas. Most prior work mitigates this issue with trainingtime solutions (e.g., data curation or alignmentoriented regularization). However, these approaches are costly to maintain as personas and attack strategies evolve, can degrade in-character behavior, and are typically infeasible for frontier closed-weight LLMs. We propose a training-free Dual-Cycle Adversarial Self-Evolution framework with two coupled cycles. A Persona-Targeted Attacker Cycle synthesizes progressively stronger jailbreak prompts, while a Role-Playing Defender Cycle distills observed failures into a hierarchical knowledge base of (i) global safety rules, (ii) persona-grounded constraints, and (iii) safe in-character exemplars. At inference time, the Defender retrieves and composes structured knowledge from this hierarchy to guide generation, producing responses that remain faithful to the target persona while satisfying safety constraints. Extensive experiments across multiple proprietary LLMs show consistent gains over strong baselines on both role fidelity and jailbreak resistance, and robust generalization to unseen personas and attack prompts.

</details>

### 50. Towards Comprehensive Post Safety Alignment of Large Language Models via Safety Patching

📄 [arXiv](https://arxiv.org/abs/2405.13820) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/7176.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`post-safety alignment`、`jailbreak patch`、`continual defense`、`post safety alignment`、`over-refusal`

👤 **作者**：Weixiang Zhao、…、Ting Liu

- 🎯 **研究动机**：现有安全对齐 LLM 机制脆弱失衡：仍可被诱导生成不安全回复、对安全输入过度拒绝、对齐后效用受损
- 🔬 **研究方法**：提出 SafePatching 后安全对齐框架：在有害数据上开发分别增强安全与缓解过度安全的两类补丁并无缝集成到目标 LLM 主干
- 📌 **结论**：在 LLaMA-2/3、Gemma、Mistral 四个对齐模型上实现比基线更全面的后安全对齐，并在持续对齐场景中保持优势

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment of large language models (LLMs) has been gaining increasing attention. However, current safety-aligned LLMs suffer from the fragile and imbalanced safety mechanisms, which can still be induced to generate unsafe responses, exhibit over-safety by rejecting safe user inputs, and fail to preserve general utility after safety alignment. To this end, we propose a novel post safety alignment (PSA) method to address these inherent and emerging safety challenges, including safety enhancement, over-safety mitigation, and utility preservation. In specific, we introduce SAFEPATCHING, a novel framework for comprehensive PSA, where two distinct safety patches are developed on the harmful data to enhance safety and mitigate oversafety concerns, and then seamlessly integrated into the target LLM backbone without compromising its utility. Extensive experiments on four representative aligned LLMs, including LLaMA-2/3, Gemma and Mistral, show that SAFEPATCHING achieves a more comprehensive PSA than baseline methods, further optimizing the balance between being helpful and harmless in current aligned LLMs. Also, SAFEPATCHING demonstrates its superiority in continual PSA scenarios.

</details>

### 51. X-Boundary: Establishing Exact Safety Boundaries via Dual-Objective Optimization

🎓 [Official](https://aclanthology.org/2025.findings-emnlp.282/)　📅 2025-11　🏷 EMNLP 2025

**关键词**：`defense`、`safety boundary`、`dual-objective optimization`、`over-refusal`

👤 **作者**：Xiaoya Lu、Dongrui Liu、Yi Yu、Luxin Xu、Jing Shao

- 🎯 **研究动机**：现有防御无法精确区分安全与有害特征表示，误伤边界安全样本引发over-refusal
- 🔬 **研究方法**：X-Boundary以双目标优化将有害表示推离边界安全表示，建立精确区分边界
- 📌 **结论**：单/多轮jailbreak防御SOTA，over-refusal降约20%，通用能力近乎无损

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the widespread application of large language models (LLMs) across various domains, techniques for enhancing their security have progressed rapidly. In this paper, we reveal that although existing defense methods can improve the robustness of LLMs against jailbreaks, they compromise usability, i.e., reducing general capabilities or causing the over-refusal problem. From the perspective of LLM mechanism interpretability, we discover that these methods fail to establish a boundary that exactly distinguishes safe and harmful feature representations. Therefore, boundary-safe representations close to harmful representations are inevitably disrupted, leading to a decline in usability. To address this issue, we propose X-Boundary to push harmful representations away from boundary-safe representations and obtain an exact distinction boundary. In this way, harmful representations can be precisely erased without disrupting safe ones. Experimental results show that X-Boundary achieves state-of-the-art defense performance against both single-turn and multi-turn jailbreak attacks, while reducing the over-refusal rate by about 20% and maintaining nearly complete general capability. Furthermore, we theoretically prove and empirically verify that X-Boundary can accelerate the convergence process during training.

</details>

### 52. Proactive defense against LLM Jailbreak

📄 [arXiv](https://arxiv.org/abs/2510.05052)　📅 2025-10

**关键词**：`defense`、`proactive deception`、`iterative jailbreak`、`spurious response`

👤 **作者**：Weiliang Zhao、Jinjun Peng、Daniel Ben-Levi、Zhou Yu、Junfeng Yang

- 🎯 **研究动机**：现有防御多为被动静态，难以应对迭代搜索式的多轮越狱
- 🔬 **研究方法**：提出 ProAct：以虚假的 spurious responses 误导攻击者的内层优化循环，使其误判已越狱而提前终止搜索
- 📌 **结论**：越狱 ASR 最多降 94% 且不影响效用，与其他防御组合可将最新攻击成功率压至 0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of powerful large language models (LLMs) has necessitated robust safety alignment, yet these models remain vulnerable to evolving adversarial attacks, including multi-turn jailbreaks that iteratively search for successful queries. Current defenses, which are primarily reactive and static, often fail to handle these iterative attacks. In this paper, we introduce ProAct, a novel proactive defense framework designed to disrupt and mislead these iterative search jailbreak methods. Our core idea is to intentionally mislead these jailbreak methods into thinking that the model has been jailbroken with "spurious responses". These misleading responses provide false signals to the attacker's internal optimization loop, causing the adversarial search to terminate prematurely and effectively jailbreaking the jailbreak. By conducting extensive experiments across state-of-the-art LLMs, jailbreaking frameworks, and safety benchmarks, we demonstrate that our method consistently and significantly reduces attack success rates by up to 94% without affecting utility. When combined with other defense fraeworks, it further reduces the latest attack strategies' success rate to 0%. ProActrepresents an orthogonal defense strategy that serves as an additional guardrail to enhance LLM safety against the most effective jailbreaking attacks.

</details>

### 53. Bypassing Prompt Guards in Production with Controlled-Release Prompting

📄 [arXiv](https://arxiv.org/abs/2510.01529) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/fairoze)　📅 2025-10　🏷 USENIX Security 2026

**关键词**：`defense`、`attack`、`prompt guard`、`controlled-release prompting`、`jailbreak defense`、`copyright extraction`

👤 **作者**：Jaiden Fairoze、Sanjam Garg、Keewoo Lee、Mingyuan Wang

- 🎯 **研究动机**：prompt 过滤的理论不可能性结果是否转化为真实系统漏洞未被验证
- 🔬 **研究方法**：提出 controlled-release prompting：利用轻量过滤器与被保护模型的资源不对称，生成有界过滤器不可解但对目标 LLM 可解的恶意 prompt
- 📌 **结论**：在 Gemini、DeepSeek、Grok、Mistral 四大平台攻击成功并从 Gemini 提取版权数据；14 个开源护栏模型中连推理型过滤器也难以可靠检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ball et al. recently established that prompt filtering for AI alignment faces a fundamental barrier: under standard cryptographic assumptions, no filter running significantly faster than the protected model can universally distinguish adversarial prompts from benign ones. We investigate whether this impossibility result translates to real-world vulnerabilities in deployed large language model (LLM) systems. We answer affirmatively by introducing controlled-release prompting, a practical instantiation of the theoretical framework that exploits the resource asymmetry between lightweight input filters and the main models they protect. Unlike the theoretical construction, our attack does not require model modification: it generates malicious prompts that are indecipherable by any bounded filter yet remain tractable to the target LLM. We find our attack to be successful on four major chat platforms (Google Gemini, DeepSeek Chat, xAI Grok, and Mistral Le Chat) where baseline methods fail. Additionally, we apply our attack to extract copyrighted data from Gemini. Finally, we provide a systematic evaluation of 14 open-weight prompt guard models, revealing that even reasoning-capable filters cannot reliably detect our attack without incurring prohibitive resource overhead.

</details>

### 54. MTSA: Multi-Turn Safety Alignment for Large Language Models

🎓 [Official](https://aclanthology.org/2025.acl-long.1282/)　📅 2025-07　🏷 ACL 2025

**关键词**：`defense`、`multi-turn alignment`、`conversation-level objective`、`intent transition`

👤 **作者**：Weiyang Guo、…、Min Zhang

- 🎯 **研究动机**：多轮对话中恶意意图可藏于交互历史，LLM 更易产生有害响应
- 🔬 **研究方法**：MTSA 两阶段：思维引导攻击学习生成多轮对抗提示，红队与目标模型对抗迭代共同提升，并用基于未来奖励的多轮 RL 增强对齐鲁棒性
- 📌 **结论**：红队模型攻击能力 SOTA，目标模型安全基准表现显著提升

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of jailbreak attacks against large language models (LLMs) highlights the need for robust security measures. However, in multi-round dialogues, malicious intentions may be hidden in interactions, leading LLMs to be more prone to produce harmful responses. In this paper, we propose the Multi-Turn Safety Alignment (MTSA) framework, to address the challenge of securing LLMs in multi-round interactions. It consists of two stages: In the thought-guided attack learning stage, the red-team model learns about thought-guided multi-round jailbreak attacks to generate adversarial prompts. In the adversarial iterative optimization stage, the red-team model and the target model continuously improve their respective capabilities in interaction. Furthermore, we introduce a multi-turn reinforcement learning algorithm based on future rewards to enhance the robustness of safety alignment. Experimental results show that the red-team model exhibits state-of-the-art attack capabilities, while the target model significantly improves its performance on safety benchmarks.

</details>

### 55. Validity-Aware Jailbreak Evaluation for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2609.00498)　📅 2026-09

**关键词**：`benchmark`、`jailbreak evaluation`、`construct validity`、`retrieval-grounded verification`

👤 **作者**：Qilong Wu、Sahil Wadhwa、Pranab Mohanty、Giri Iyengar、Varun Chandrasekaran

- 🎯 **研究动机**：现行 jailbreak 评测依赖拒答、语义相似与意图匹配启发式，会把看似合理但事实或程序错误的回答算作成功
- 🔬 **研究方法**：提出 SEAV 验证式评测框架：把回复分解为有序步骤，结合 LLM-as-a-judge 与检索接地的外部知识验证有效性与正确性
- 📌 **结论**：在 SD-A 诊断集上 false positive 比最强基线降 14.9 个百分点，并把四个公开基准中三个的 22.1%-51.0% 既有“成功”重判为无效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak robustness has become central to large language model (LLM) safety evaluation, yet prevailing methodologies rely primarily on refusal behavior, semantic resemblance, and intent-matching heuristics that emphasize linguistic plausibility rather than correctness. We identify a key limitation in existing evaluations: many jailbreak intents depend on instructional validity rather than epistemic factuality, allowing realistic-looking responses to be labeled successful despite being factually or procedurally incorrect. To address this gap, we propose Sequential Epistemic and Action-Level Validation (SEAV), a verification-centric jailbreak evaluation framework that decomposes responses into ordered steps and evaluates both validity and correctness. SEAV combines LLM-as-a-judge mechanisms for semantic interpretation with retrieval-grounded verification using external knowledge sources, assessing whether generated content is factually correct, structurally consistent, and operationally capable of advancing harmful objectives. Empirically, SEAV cuts the false-positive rate on SD-A (a curated strategic-dishonesty diagnostic) by 14.9\,pp vs. the strongest baseline, and reclassifies 22.1\%--51.0\% of sampled prior-labeled successes as invalid across three of four public benchmarks. Together, these results show that enforcing correctness substantially reshapes measured robustness: many previously labeled jailbreak successes are reclassified as invalid, and results are stable across the tested search backends and evaluator models. Code and data are available at https://github.com/Ardor-Wu/SEAV.

</details>

### 56. NeuronFuzz: Safety Neuron Guided Fuzzing for LLM Safety Evaluation

📄 [arXiv](https://arxiv.org/abs/2608.26222)　📅 2026-08

**关键词**：`attack`、`benchmark`、`analysis`、`safety-neuron fuzzing`、`gradient-guided mutation`、`jailbreak transfer`

👤 **作者**：Zhiyuan Xu、Muhammad Firhard Roslan、Joseph Gardiner、Sana Belguith、Lichao Wu

- 🎯 **研究动机**：现有 LLM 安全 fuzzing 依赖响应级反馈：每个候选都要生成回答且强对齐模型上反馈稀疏
- 🔬 **研究方法**：NeuronFuzz 用稳定 safety neuron 的 prefill 激活构造连续可微 SafetyOracle 分数，指导梯度驱动的模板变异
- 📌 **结论**：21 个模型上五个白盒源模型越狱发现率 76%-100%（超基线最多 48 个百分点），模板零样本迁移至闭源模型（top-5 EASR 92.6%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety evaluation is critical for assessing whether aligned Large Language Models (LLMs) remain robust against jailbreak attacks. Existing automated testing methods, however, largely rely on response-level feedback: each candidate prompt typically requires generating a target-model response to evaluate its attack effectiveness. This process is expensive and, more importantly, provides only sparse guidance on strongly aligned models, where most candidates are rejected with the same failure outcome. This paper presents NeuronFuzz, a white-box fuzzing framework that exploits internal safety neurons as continuous execution feedback for LLM safety evaluation. A SafetyOracle converts safety-neuron activations into a continuous safety alarm score that serves as feedback for fuzzing and can be obtained during prefill, eliminating response generation from the fuzzing loop. To construct the SafetyOracle, NeuronFuzz uses template-invariant harmful and benign inputs and stability-aware selection to identify a compact set of safety neurons whose activations capture harmful-intent recognition. Moreover, since the safety alarm score is differentiable, NeuronFuzz uses its gradients to identify safety-sensitive template positions and a masked language model to generate fluent, context-compatible mutations while preserving original harmful payload and avoiding additional optimization variables. We evaluate NeuronFuzz across 21 text and multimodal models. Across five white-box source models, it achieves a 76-100% jailbreak discovery rate, outperforming baselines by up to 48 percentage points. Its optimized templates further transfer zero-shot to open-weight and six proprietary target models, achieving average ASR and top-5 ensemble ASR (EASR) of 69.6%/92.6% and 44.1%/60.0%, respectively.

</details>

### 57. Are LLMs Safe Beyond Text: Do Emojis Expose Gaps in Safety Evaluation

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

### 58. Fair ASR: Re-Evaluating Black-Box Jailbreaks under Shared Target-Call Budgets

📄 [arXiv](https://arxiv.org/abs/2608.17360)　📅 2026-08

**关键词**：`benchmark`、`jailbreak`、`jailbreak defense`、`harmful intent detection`

👤 **作者**：Zhida He、…、Qiaosheng Zhang

- 🎯 **研究动机**：越狱评测只报 ASR 不考虑攻击预算依赖，跨方法比较不公平；FLOPs 折算对黑盒模型难估计
- 🔬 **研究方法**：Fair-ASR 协议在共享目标调用预算 B 下评测，以目标调用为可观察且方法无关的比较轴、攻击者调用单独计效；重评 11 种攻击并提出组合式 ReCode
- 📌 **结论**：攻击排名随预算大幅变化，简单随机扰动与手工模板在同等目标访问下仍极具竞争力；ReCode 在 20 次目标调用预算下对 GPT-5 达 85% ASR、平均仅需 7.19 次攻击者调用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reliable jailbreak evaluation is essential for assessing LLM safety, but most existing studies rely solely on attack success rate (ASR) without accounting for its dependence on attack budgets, resulting in unfair comparisons across methods. Existing compute-aware evaluations reduce heterogeneous resources into FLOPs, which is difficult to estimate for black-box models and fails to capture resource-specific constraints. To provide a comparable evaluation basis, we introduce Fair-ASR, an evaluation protocol for black-box jailbreak attacks under shared target-call budgets B, using target calls as a directly observable and method-agnostic comparison axis while tracking attacker calls separately for efficiency analysis. We re-evaluate 11 representative attacks under the Fair-ASR protocol and find that attack rankings change substantially across target-call budgets, simple stochastic perturbations and hand-crafted templates remain highly competitive under equal target access, and no evaluated LLM-driven method is efficient in both target and attacker calls. Motivated by this efficiency gap, we introduce ReCode, a compositional budget-efficient attack that combines desensitization rewriting with two effective low-cost primitives identified by Fair-ASR. Under a budget of 20 target calls, ReCode achieves 85% ASR on GPT-5 while requiring only 7.19 attacker calls per request on average, showing strong efficiency in both target and attacker calls.

</details>

### 59. TRACE: Trajectory Aware Reasoning for Multi-Turn Adversarial Conversation Evaluation

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

### 60. MultiBreak: A Scalable and Diverse Multi-turn Jailbreak Benchmark for Evaluating LLM Safety

📄 [arXiv](https://arxiv.org/abs/2605.01687) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63523)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`LLM jailbreak`、`multi-turn jailbreak`、`jailbreak`、`empirical evaluation`、`attack transferability`

👤 **作者**：Jialin Song、…、Jianfeng Gao

- 🎯 **研究动机**：现有多轮越狱基准规模小或依赖模板，多样性受限
- 🔬 **研究方法**：主动学习管线迭代微调生成器产生更强攻击候选，构建 10,389 条多轮对抗提示、覆盖 2,665 个有害意图
- 📌 **结论**：DeepSeek-R1-7B 与 GPT-4.1-mini 上 ASR 比次优数据集高 54.0%/34.6%；单轮看似良性的类别在多轮下可具显著对抗效力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present MultiBreak, a scalable and diverse multi-turn jailbreak benchmark to evaluate large language model (LLM) safety. Multi-turn jailbreaks mimic natural conversational settings, making them easier to bypass safety-aligned LLM than single-turn jailbreaks. Existing multi-turn benchmarks are limited in size or rely heavily on templates, which restrict their diversity. To address this gap, we unify a wide range of harmful jailbreak intents, and introduce an active learning pipeline for expanding high-quality multi-turn adversarial prompts, where a generator is iteratively fine-tuned to produce stronger attack candidates, guided by uncertainty-based refinement. Our MultiBreak includes 10,389 multi-turn adversarial prompts, spans 2,665 distinct harmful intents, and covers the most diverse set of topics to date. Empirical evaluation shows that our benchmark achieves up to a 54.0% and 34.6% higher attack success rate (ASR) than the second-best dataset on DeepSeek-R1-7B and GPT-4.1-mini, respectively. More importantly, safety evaluations suggest that diverse attack categories uncover fine-grained LLM vulnerabilities, and categories that appear benign under single-turn can exhibit substantially higher adversarial effectiveness in multi-turn scenarios. These findings highlight persistent vulnerabilities of LLMs under realistic adversarial settings and establish MultiBreak as a scalable resource for advancing LLM safety.

</details>

### 61. Can Small Language Models Reliably Resist Jailbreak Attacks? A Comprehensive Evaluation

📄 [arXiv](https://arxiv.org/abs/2503.06519) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2025-03　🏷 ACM CCS 2026

**关键词**：`benchmark`、`small language model`、`jailbreak attack`、`jailbreak`、`prompt-level defense`

👤 **作者**：Zhibo Wang、Wenhui Zhang、Huiyu Xu、Zeqing He、Ziqi Zhu、Kui Ren

- 🎯 **研究动机**：SLM 端侧部署趋势下其越狱风险未被系统评估
- 🔬 **研究方法**：对 59 个 SLM（15 个家族）系统评测 12 种 SOTA 越狱方法，做相关性分析并评估五类防御
- 📌 **结论**：61.0% 的 SLM 平均 ASR 超 40%，37.3% 在直接有害查询上 ASR 超 50%；脆弱性与训练细节相关而非模型规模，prompt 级防御不稳定、模型级难泛化到多轮攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Small language models (SLMs) have emerged as promising alternatives to large language models (LLMs) due to their low computational demands, enhanced privacy guarantees, and comparable performance in specific domains. Deploying SLMs on edge devices, such as smartphones and smart vehicles, has become a growing trend. However, the security implications of SLMs have not received as much attention as those of LLMs, particularly concerning the significant jailbreak threats they face. In this paper, we conduct the first systematic empirical study of SLMs' vulnerabilities to jailbreak attacks. Through systematic evaluation on 59 SLMs from 15 mainstream SLM families against 12 state-of-the-art jailbreak methods, we demonstrate that 61.0% of evaluated SLMs show an average ASR of more than 40% under jailbreak attacks and 37.3% of them have an ASR of more than 50% on direct harmful queries. Through correlation analysis, we identify that SLM vulnerabilities are closely related to training details (e.g., training dataset and method) rather than model size scaling. We further evaluate five defenses for jailbreak attacks, revealing that prompt-level defenses remain inconsistent across SLMs and attack methods, while model-level defense improves robustness against similar attacks yet generalizes poorly to multi-turn attacks such as Crescendo, highlighting the urgent need for security-by-design approaches in SLM development.

</details>

### 62. DualSentinel: A Lightweight Framework for Detecting Targeted Attacks in Black-box LLM via Dual Entropy Lull Pattern

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

### 63. One Bad Token Spoils the Barrel: Assessment, Detection, and Remediation of Glitch Tokens in Large Language Models

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/tang-kunsheng)　📅 2026　🏷 USENIX Security 2026

**关键词**：`detection`、`defense`、`glitch token`、`token remediation`、`jailbreak defense`、`unsafe generation`

👤 **作者**：Kunsheng Tang、…、Jie Zhang

- 🎯 **研究动机**：glitch token 引发不可预测错误行为，缺安全评估、检测覆盖有限且无修复手段
- 🔬 **研究方法**：展示其可绕过安全机制且跨模型、分词器与商业审核系统迁移；GlitchQuiz 红队框架检测；GlitchEdit 免训练嵌入层编辑修复
- 📌 **结论**：不安全率平均从 96.36% 降至 2.87% 且保持整体性能；已向 OpenAI、Anthropic 等九家提供商负责任披露

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have shown remarkable capabilities across numerous applications. However, the recent emergence of "glitch tokens," referring to tokens that cause unpredictable and erroneous model behaviors, poses significant reliability and security challenges. Despite prior investigations of glitch tokens, critical gaps remain, including insufficient safety assessments, limited detection coverage, and the absence of effective remediation strategies. To address these challenges, we first demonstrate that glitch tokens can readily bypass safety mechanisms and elicit unsafe outputs across LLMs through straightforward exploitation methods. More critically, we reveal that these tokens exhibit cross-model transferability, inducing safety risks across model families, tokenizers, commercial and moderation systems, underscoring their pervasive security implications. We then propose GlitchQuiz, a red-teaming framework inspired by human language acquisition, to comprehensively detect glitch tokens, surpassing existing detection methods. Finally, we develop GlitchEdit, a training-free embedding-layer editing approach that effectively remediates glitch tokens, reducing unsafe behaviors with average unsafe rates decreasing from 96.36% to 2.87% across evaluated LLMs and maintaining overall performance. Our findings have been responsibly disclosed to nine affected leading LLM providers, including OpenAI, Anthropic, and others, to help foster safer AI ecosystems.

</details>

### 64. Detecting What Queries Seek: Steering LLM Safety with FFN Output Activation Monitoring

🎓 [Official](https://aclanthology.org/2026.acl-long.1360/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`jailbreak`、`jailbreak defense`、`harmful intent detection`、`representation intervention`、`runtime safety`

👤 **作者**：Xiaohao Luo、Ying Wei、Rui Zhao

- 🎯 **研究动机**：激活引导不加区分地干预导致过度拒绝；选择性干预依赖信息高度纠缠的残差流激活，判别力有限
- 🔬 **研究方法**：FGAS 用作为知识存储核心的 FFN 输出激活做干预信号：投影到有害与良性可分的低维子空间，按与预构建原型激活的相似度做精确干预决策
- 📌 **结论**：对多种越狱攻击达 SOTA 防御，同时几乎保持良性任务的原始性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recently, activation steering has attracted considerable attention as a low-cost approach to improving the safety of large language models (LLMs). However, most existing methods apply interventions indiscriminately, often causing excessive refusal of benign queries. Although recent works have begun to explore selective intervention, their intervention decisions typically rely on residual stream activations where information is highly entangled, resulting in limited discriminative power and unreliable interventions. To address this issue, we propose FFN-Guided activation steering (FGAS). Motivated by the observation that feed-forward networks (FFNs) in LLMs serve as core modules for knowledge storage, we propose leveraging FFN output activations as more discriminative signals for intervention, since these activations more explicitly reflect the intent of a query. For a given query, FGAS projects the corresponding FFN output activation into a low-dimensional subspace that effectively separates harmful and benign queries, and then makes precise intervention decisions by assessing its similarity to pre-constructed prototype activations representing harmful and benign classes. Extensive experiments demonstrate that FGAS achieves state-of-the-art defense performance against various jailbreak attacks, while nearly preserving the model’s original performance on benign tasks.

</details>

### 65. Detecting Fluent Optimization-Based Adversarial Prompts via Sequential Entropy Changes

📄 [arXiv](https://arxiv.org/abs/2605.19966) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61448)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`adversarial robustness`、`jailbreak defense`、`harmful intent detection`、`prompt injection`、`empirical evaluation`

👤 **作者**：Mohammed Alshaalan、Miguel R. D. Rodrigues

- 🎯 **研究动机**：基于优化的对抗后缀可流畅生成，削弱静态与窗口困惑度检测器
- 🔬 **研究方法**：把后缀检测转为 token 级熵流上的在线变点检测：以系统提示估计基线、标准化用户 token 熵、用单边 CUSUM 统计，模型无关且免训练
- 📌 **结论**：六个开源聊天模型 F1 全面超窗口困惑度基线，LLaMA-2-7B 上 AUROC 0.88、F1 0.82；79.6% 触发点落在对抗后缀内；作 LLaMA Guard 门控可省 17 至 22% 调用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Optimization-based adversarial suffixes can jailbreak aligned large language models (LLMs) while remaining fluent, weakening static and windowed perplexity-based detectors. We cast adversarial suffix detection as an *online change-point detection* problem over the token-level next-token entropy stream. Using the LLM system prompt to estimate a robust baseline, we standardize user-token entropies and apply a one-sided CUSUM statistic. The resulting detector, *CPD Online* (CPD), is model-agnostic, training-free, runs online, and localizes the adversarial suffix onset. On a benchmark of 1,012 optimization-based suffix attacks (GCG, AutoDAN, AdvPrompter, BEAST, AutoDAN-HGA) and 1,012 perplexity-controlled benign prompts, CPD improves F1 over the strongest windowed-perplexity baseline on all six open-weight chat models (LLaMA-2-7B/13B, Vicuna-7B/13B, Qwen2.5-7B/14B). On LLaMA-2-7B at the canonical CUSUM setting ($k=0$), CPD reaches AUROC $0.88$ and F1 $0.82$. Beyond prompt-level detection, CPD concentrates 79.6% of its triggers inside the adversarial suffix, versus 17–46% for windowed perplexity. Finally, when used as a lightweight gate for LLaMA Guard, CPD reduces guard calls by 17–22% on a high-volume, benign-dominated deployment while preserving guard-level detection quality.

</details>

### 66. Beyond Surface-Level Detection: Towards Cognitive-Driven Defense Against Jailbreak Attacks via Meta-Operations Reasoning

🎓 [Official](https://aclanthology.org/2026.acl-long.125/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`reasoning safety`、`jailbreak defense`、`jailbreak`、`LLM jailbreak`

👤 **作者**：Rui Pu、Chaozhuo Li、Rui Ha、Litian Zhang、Lirong Qiu、Xi Zhang

- 🎯 **研究动机**：现有越狱防御依赖浅层模式匹配，难以泛化到未见攻击策略
- 🔬 **研究方法**：CDD 针对越狱提示底层结构做元操作（隐藏有害意图的基本操纵）推理：结构化推理链全局感知加局部分析，监督微调后用熵引导强化学习 EG-GRPO 探索新元操作变体
- 📌 **结论**：取得 SOTA 防御性能且对未见越狱攻击具有强泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Defending large language models (LLMs) against jailbreak attacks is essential for their safe and reliable deployment. Existing defenses often rely on shallow pattern matching, which struggles to generalize to novel and unseen attack strategies. To address this challenge, we propose the Cognitive-Driven Defense (CDD) framework, which targets the underlying structure of jailbreak prompts by applying meta-operations, defined as basic manipulations that conceal harmful intent. CDD emulates human cognitive reasoning through a structured reasoning chain. It begins with a global perception of the prompt and follows with a localized analysis to uncover hidden manipulations. By applying supervised fine-tuning on this structured chain, the model learns to identify and reason about known manipulation patterns. To enhance generalization to unseen threats, an entropy-guided reinforcement learning algorithm (EG-GRPO) is introduced to encourage exploration of new types and variants of meta-operations. Experiments demonstrate that CDD can achieve state-of-the-art defense performance and exhibit strong generalization to unseen jailbreak attacks.

</details>

### 67. A Single Suffix to Break Them All: Basin-Aware Jailbreaks for Merged Model Families

📄 [arXiv](https://arxiv.org/abs/2608.26506)　📅 2026-08

**关键词**：`analysis`、`attack`、`model merging`、`shared safety basin`、`post-training degradation`、`basin-aware jailbreak`

👤 **作者**：Yu Zhe、Yixin Tan、Junhao Wei、Wang Chen

- 🎯 **研究动机**：模型合并风险研究默认各组成模型对齐则合并安全，忽视源自预训练底座的共享风险
- 🔬 **研究方法**：发现共享 backbone 的合并模型族暴露共同 jailbreak basin；BAJ 在合并空间做 min-max 优化生成对抗后缀，无需知道合并系数
- 📌 **结论**：单一后缀跨同族合并模型持续高成功迁移，现有防御难以阻断

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model merging enables combining multiple fine-tuned models without additional training, but its safety implications remain poorly understood. Prior work primarily attributes merging risks to unsafe constituent models, implicitly assuming that merging individually aligned models preserves safety. In contrast, we show that model merging reveals a previously overlooked jailbreak risk rooted in the pretrained foundation model, even when all constituent models are individually safety-aligned. Motivated by this observation, we study a new threat setting where an attacker constructs jailbreak prompts that generalize across merged models sharing the same pretrained backbone, without access to the exact merging coefficients or constituent checkpoints. To exploit this phenomenon, we propose \textbf{Basin-Aware Jailbreak (BAJ)}, which formulates jailbreak generation as a min--max optimization over the merging space to produce transferable adversarial suffixes across merged model families. Experiments across diverse backbones and merging settings show that BAJ achieves consistently high transfer success rates and remains effective under existing defenses.

</details>

### 68. PsychJail: Exploring Psychological Jailbreaks via Multi-Turn Persuasion of LLM Policies

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

### 69. Quantifying Large Language Model Attacks Through the Lens of Model Cognition

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-xiuming)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`detection`、`LLM attack`、`model cognition`、`jailbreak defense`、`lightweight monitor`

👤 **作者**：Xiuming Liu、…、Shuo Wang

- 🎯 **研究动机**：关键词过滤与输出审核等安全机制忽视模型内部动态
- 🔬 **研究方法**：中间隐藏态轻量探针在生成前分离有害提示特征（最高 99% 准确率）；层级毒性探针加多层互补检测融合不同深度信号，Sentinel 不到 5M 参数
- 📌 **结论**：假阴性比生成级拒答减半，对抗攻击下保持 94% 以上检测准确率（基线掉 32%），并在七个开源 LLM 上超 Llama-Guard-3-8B

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are vulnerable to malicious inputs that elicit harmful content. Current safety mechanisms, such as keyword filters or output moderation, largely ignore internal model dynamics. We show that safety-relevant features correlated with harmful prompting are strongly separable under lightweight probes in intermediate hidden states (up to 99% accuracy) before generation, revealing that such features persist internally even when models produce compliant outputs. Leveraging this observation, we introduce layer-wise toxicity probes and a multi-layer complementary detection framework that fuses signals from diverse depths. Our lightweight Sentinel (<5M parameters) halves false negatives compared to generation-level refusal and maintains over 94% detection accuracy under adversarial attacks—where baselines drop by 32%. Sentinel also outperforms Llama-Guard-3-8B on heterogeneous harmful prompting across seven open-weight LLMs (1.5B→72B) and multiple benchmarks (I2P, SneakyPrompt, MMA, Labelled, PIJ, ChatAlpaca, and Multi-turn Jailbreak). Beyond detection, our method provides the first quantitative, layer-resolved map of how safety-relevant signals emerge, propagate, and degrade within LLMs, enabling interpretable, inside-out alignment and diagnostics. This paper contains potentially sensitive and offensive content, including but not limited to NSFW material, hate speech, discrimination, and other harmful text. Reader discretion is advised.

</details>

### 70. Enforcing LLM Safety through DMD-based Classification of Prompt-Response Embedding Dynamics

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

### 71. On Prompt-Driven Safeguarding for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2401.18018) · 🌐 [Project](https://proceedings.mlr.press/v235/zheng24n.html)　📅 2024-01　🏷 ICML 2024

**关键词**：`defense`、`soft safety prompt`、`directed representation optimization`、`refusal direction`

👤 **作者**：Chujie Zheng、…、Nanyun Peng

- 🎯 **研究动机**：安全提示的底层机制未被解释，限制了对其自动优化以提升安全性
- 🔬 **研究方法**：发现安全提示把查询表示移向更高拒答方向（连无害查询也更易被拒），而 LLM 天然可区分有害无害；DRO 把安全提示作连续可训练嵌入，按有害性沿或逆拒答方向移动表示
- 📌 **结论**：八个 LLM 在域外与越狱基准上显著提升防护效果且不损通用性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prepending model inputs with safety prompts is a common practice for safeguarding large language models (LLMs) against queries with harmful intents. However, the underlying working mechanisms of safety prompts have not been unraveled yet, restricting the possibility of automatically optimizing them to improve LLM safety. In this work, we investigate how LLMs’ behavior (i.e., complying with or refusing user queries) is affected by safety prompts from the perspective of model representation. We find that in the representation space, the input queries are typically moved by safety prompts in a "higher-refusal" direction, in which models become more prone to refusing to provide assistance, even when the queries are harmless. On the other hand, LLMs are naturally capable of distinguishing harmful and harmless queries without safety prompts. Inspired by these findings, we propose a method for safety prompt optimization, namely DRO (Directed Representation Optimization). Treating a safety prompt as continuous, trainable embeddings, DRO learns to move the queries’ representations along or opposite the refusal direction, depending on their harmfulness. Experiments with eight LLMs on out-of-domain and jailbreak benchmarks demonstrate that DRO remarkably improves the safeguarding performance of human-crafted safety prompts, without compromising the models’ general performance.

</details>

### 72. Tripwire: Triggering Aligned Refusal via Statistically Certified Safety Neurons

📄 [arXiv](https://arxiv.org/abs/2608.14392) · 🌐 [Project](https://anonymous.4open.science/r/Tripwire-65C4)　📅 2026-08

**关键词**：`defense`、`analysis`、`detector-gated intervention`、`safety neuron`、`utility preservation`、`jailbreak`

👤 **作者**：Wei Zhao、Zhe Li、Peixin Zhang、Jun Sun

- 🎯 **研究动机**：神经元级越狱防御或干预面大损效用、或误伤效用神经元，且常开干预扰动每个良性请求
- 🔬 **研究方法**：Tripwire 免训练：FDR 控制下逐神经元假设检验加效用特异性过滤识别安全神经元，触发式 clamp 钉住激活于有害条件均值以诱发对齐学到的拒答；支持检测门控推理与离线 bias-patch 两种等价部署
- 📌 **结论**：四个对齐 LLM、四种攻击下平均 ASR 降至至多 2.0%，MT-Bench 效用损失仅 0.5-5.3%，为所有防御中最小

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Neuron- and path-level interventions offer the finest-grained route to defending large language models (LLMs) against jailbreak attacks, yet existing methods fall short of this promise, i.e., they often compromise model utility significantly. Specifically, one line of work suppresses toxic neurons to erase harmful semantics, but since such semantics are distributed across the network, blocking every pathway forces a large intervention footprint. An alternative line of research focus on identify safety neurons using external classifiers. While promising, the existing approaches suffer from compromising neurons that are important for the model utility as well. Moreover, both approaches remain always on and thus perturb every benign request even when no attack is present. To address these limitations, we present \ours{}, a training-free defense that first identifies safety-specific neurons through per-neuron hypothesis tests under false-discovery-rate control together with a utility-specificity filter. Based on this identification, a trigger-style clamp holds the selected neurons at their harmful-conditional mean activations, injecting an internal harmful-input signal that triggers the refusal behavior learned during alignment. The clamp is then realized by two provably equivalent deployment modes, namely a detector-gated inference-time intervention and an offline bias-patch weight edit. Extensive experiments across four safety-aligned LLMs and four representative attacks demonstrate that \ours{} reduces the average attack success rate to at most 2.0\% while incurring a utility drop of only 0.5\% to 5.3\% on MT-Bench, the smallest among all defenses. Code is available at https://anonymous.4open.science/r/Tripwire-65C4.

</details>

### 73. Evaluating Answer Leakage Robustness of LLM Tutors against Adversarial Student Attacks

🎓 [Official](https://aclanthology.org/2026.acl-long.1412/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`adversarial robustness`、`privacy leakage`、`memorization`、`LLM privacy`、`data leakage`

👤 **作者**：Jin Zhao、Marta Knežević、Tanja Käser

- 🎯 **研究动机**：以往答案泄露评测假设善意学习者，LLM 导师在学生滥用下的鲁棒性未被探索
- 🔬 **研究方法**：把六组对抗与说服技术适配到教育场景探测导师泄露答案倾向，提出微调越狱对抗学生 agent 作标准化基准核心，并给防御策略
- 📌 **结论**：通用对抗学生 agent 常攻击失败而微调越狱 agent 有效；简单防御可降低答案泄露并增强鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly used in education, yet their default helpfulness often conflicts with pedagogical principles. Prior work evaluates pedagogical quality via answer leakage–the disclosure of complete solutions instead of scaffolding–but typically assumes well-intentioned learners, leaving tutor robustness under student misuse largely unexplored. In this paper, we study scenarios where students behave adversarially and aim to obtain the correct answer from the tutor. We evaluate a broad set of LLM-based tutor models, including different model families, pedagogically aligned models, and a multi-agent design, under a range of adversarial student attacks. We adapt six groups of adversarial and persuasive techniques to the educational setting and use them to probe how likely a tutor is to reveal the final answer. We evaluate answer leakage robustness using different types of in-context adversarial student agents, finding that they often fail to carry out effective attacks. We therefore introduce an adversarial student agent that we fine-tune to jailbreak LLM-based tutors, which we propose as the core of a standardized benchmark for evaluating tutor robustness. Finally, we present simple but effective defense strategies that reduce answer leakage and strengthen the robustness of LLM-based tutors in adversarial scenarios.

</details>

### 74. HarDBench: A Benchmark for Draft-Based Co-Authoring Jailbreak Attacks for Safe Human–LLM Collaborative Writing

🌐 [Project](https://anonymous.4open.science/r/HarDBench_data-17E4) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1893/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`LLM jailbreak`、`jailbreak`、`harmful fine-tuning`、`automated red teaming`、`attack transferability`

👤 **作者**：EunTae Kim、Soomin Han、Buru Chang

- 🎯 **研究动机**：LLM 协作写作中恶意用户可填充危险草稿诱导有害补全，模型对此脆弱性未知
- 🔬 **研究方法**：HarDBench 覆盖爆炸物、毒品、武器、网络攻击等高危域的结构化草稿补全提示，并提出基于偏好优化的安全-效用平衡对齐方法
- 📌 **结论**：现有 LLM 在协作写作上下文中高度脆弱；对齐方法显著减少有害输出且不损协作能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used as co-authors in collaborative writing, where users begin with rough drafts and rely on LLMs to complete, revise, and refine their content. However, this capability poses a serious safety risk: malicious users could jailbreak the models—filling incomplete drafts with dangerous content—to force them into generating harmful outputs. In this paper, we identify the vulnerability of current LLMs to such draft-based co-authoring jailbreak attacks and introduce HarDBench, a systematic benchmark designed to evaluate the robustness of LLMs against this emerging threat. HarDBench spans a range of high-risk domains—including Explosives, Drugs, Weapons, and Cyberattacks—and features prompts with realistic structure and domain-specific cues to assess the model susceptibility to harmful completions. To mitigate this risk, we introduce a safety-utility balanced alignment approach based on preference optimization, training models to refuse harmful completions while remaining helpful on benign drafts. Experimental results show that existing LLMs are highly vulnerable in co-authoring contexts and our alignment method significantly reduces harmful outputs without degrading performance on co-authoring capabilities. This presents a new paradigm for evaluating and aligning LLMs in human-LLM collaborative writing settings. Our new benchmark and dataset are available on our project page at https://anonymous.4open.science/r/HarDBench_data-17E4.

</details>

### 75. MAGIC: A Co-Evolving Attacker–Defender Adversarial Game for Robust LLM Safety

📄 [arXiv](https://arxiv.org/abs/2602.01539) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62756)　📅 2026-02　🏷 ICML 2026

**关键词**：`defense`、`attack`、`adversarial attack`、`adversarial robustness`、`adversarial example`、`multi-agent evaluation`

👤 **作者**：Xiaoyu Wen、…、Qiaosheng Zhang

- 🎯 **研究动机**：依赖静态预收集数据分布的防御滞后于不断演化的对抗攻击
- 🔬 **研究方法**：MAGIC 把安全对齐形式化为多轮多 agent RL 的非对称对抗博弈：攻击者迭代改写欺骗性 prompt、防御者同步学习识别拒绝以触发共演化，并给出博弈均衡与安全保证
- 📌 **结论**：防御成功率优越且不牺牲有用性；攻击者经迭代 RL 演化出此前未见的组合攻击策略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring robust safety alignment is crucial for Large Language Models (LLMs), yet existing defenses often lag behind evolving adversarial attacks due to their \textbf{reliance on static, pre-collected data distributions}. In this paper, we introduce \textbf{MAGIC}, a novel multi-turn multi-agent reinforcement learning framework that formulates LLM safety alignment as an adversarial asymmetric game. Specifically, an attacker agent learns to iteratively rewrite original queries into deceptive prompts, while a defender agent simultaneously optimizes its policy to recognize and refuse such inputs. This dynamic process triggers a \textbf{co-evolution}, where the attacker's ever-changing strategies continuously uncover long-tail vulnerabilities, driving the defender to generalize to unseen attack patterns. Remarkably, we observe that the attacker, endowed with initial reasoning ability, evolves \textbf{novel, previously unseen combinatorial strategies} through iterative RL training, underscoring our method's substantial potential. Theoretically, we provide insights into a more robust game equilibrium and derive safety guarantees. Extensive experiments validate our framework's effectiveness, demonstrating superior defense success rates without compromising the helpfulness of the model. Our code is available at https://github.com/BattleWen/MAGIC.

</details>

### 76. Training with Honeypots: Reshaping How LLMs Fail Under Adversarial Attacks

🎓 [Official](https://icml.cc/virtual/2026/poster/63915)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`defense`、`adversarial robustness`、`adversarial example`、`evasion attack`、`prompt injection`

👤 **作者**：Samuel Simko、Punya Pandey、Zhijing Jin、Bernhard Sch\u00f6lkopf

- 🎯 **研究动机**：红队以攻击成功率（ASR）代理真实危害，但 judge 判定违规的输出在现实可操作性上差异巨大
- 🔬 **研究方法**：借鉴蜜罐思想，构造被自动 judge 频繁判为有害但实际操作价值低的回复，作为难负样本纳入安全训练，重塑模型失败模式
- 📌 **结论**：降低有害失败的现实影响与发生频率，可作为 ASR 评估的实用补充

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Automated red-teaming of Large Language Models (LLMs) commonly relies on attack success rates (ASR) as a proxy for real-world harm, implicitly assuming that judge-detected violations correspond to actionable risk. In practice, safety judges are imperfect, and outputs that satisfy automated criteria for harm can vary widely in their operational usefulness. In this work, we investigate whether model failure modes can be reshaped so that, when defenses fail, they preferentially produce reduced-actionability outputs rather than highly actionable harm. Inspired by honeypots in computer security, we construct responses that are frequently flagged as harmful by automated judges yet provide limited real-world operational value, and treat them as hard negatives in the safety training pipeline. Our findings show that shaping how models fail under attack can improve overall safety by reducing both the real-world impact and the frequency of harmful failures, and serves as a practical complement to ASR-based evaluations.

</details>

### 77. Bait-and-Recover: Poisoning Internal Refusal Signals to Defend LLMs against White-Box Editing Jailbreaks

📄 [arXiv](https://arxiv.org/abs/2609.05794)　📅 2026-09

**关键词**：`defense`、`white-box editing jailbreak`、`bait adapter`、`refusal direction`、`gradient routing`

👤 **作者**：Tian Gao、Zhipeng Xie、Yuhao Wu、Junhua Liu、Xin Fang

- 🎯 **研究动机**：白盒表征编辑攻击几分钟即可在单 GPU 上绕过开权重模型安全对齐，缺权重级防御
- 🔬 **研究方法**：Bait-and-Recover 在攻击者读取激活处放诱饵 adapter 污染测量信号、次层恢复 adapter 还原干净计算，梯度路由解耦观察与行为路径
- 📌 **结论**：四个开权重模型上最小拒绝率 16.25%→71.75%（KL≤0.10 行为保持约束），通用基准几乎无损

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-weight large language models face a low-cost white-box threat from representation engineering attacks. Attackers can estimate refusal directions and search for projection-matrix edits that suppress safety alignment while preserving general capabilities, within minutes on a single GPU and without gradient-based training. We propose Bait-and-Recover, a weight-level defense that places a bait adapter where attackers read activations and a paired recovery adapter at the subsequent layer. Trained via gradient routing, this decouples the observation path from the behavior path. By actively poisoning the residual signal used for measurement, Bait-and-Recover disrupts the attacker's edit search, while the recovery layer restores clean downstream computation. Across four open-weight models, our defense raises the minimum refusal rate against white-box edit searches from 16.25% to 71.75% under a strict behavior-preservation budget (KL <= 0.10), with negligible impact on general benchmarks. By invalidating the core measurement assumption of these attacks, observation-path poisoning offers a practical complement to behavior-level safety training.

</details>

### 78. SAFEGuard: Detect Optimization-Based Jailbreak Attacks Through Harmful Semantic Analysis and Fluency Measurement

📄 [arXiv](https://arxiv.org/abs/2609.05850)　📅 2026-09

**关键词**：`detection`、`optimization-based jailbreak`、`fluency measurement`、`harmful semantics`

👤 **作者**：Quoc Viet Vo、Trung Le、Damith C. Ranasinghe、Ehsan Abbasnejad

- 🎯 **研究动机**：优化型越狱产生高流畅度或语义混淆 prompt，现有检测方法覆盖不足
- 🔬 **研究方法**：SAFEGuard 结合跨层分布距离+困惑度的混合流畅度测量与梯度匹配的有害语义分析
- 📌 **结论**：在多类优化型越狱上检测准确率持续超过 SOTA 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite the significant efforts devoted to aligning large language models (LLMs) with human values and ensuring safe deployment, recent work has revealed that LLMs remain vulnerable to adversarial jailbreak attacks that can bypass safety guardrails and elicit harmful responses. Many defense methods are proposed to detect jailbreaks but they are limited in their effectiveness to counter wide-range optimization-based jailbreak mechanisms that can yield highly fluency-optimized or harmful semantic obfuscated prompts. To tackle this challenge, we propose a unified detection framework SAFEGuard which incorporates a hybrid fluency measurement based on cross-layer distribution distance and perplexity, and the analysis of harmful semantics through gradient matching. Our method is grounded in a paramount observation: high fluency prompts maintain their malicious intention close to harmful prompts while harmful semantic obfuscated prompts often inject gibberish token sequences. Our evaluation demonstrates that SAFEGuard consistently outperforms state-of-the-art baselines and achieves significant improvement in accuracy across different optimization-based jailbreaks. This underscores the effectiveness of SAFEGuard against evolving jailbreak attacks.

</details>

### 79. MechAudit-40: White-Box Auditing across 40 LLM Attack Mechanisms

📄 [arXiv](https://arxiv.org/abs/2609.06612)　📅 2026-09

**关键词**：`detection`、`white-box auditing`、`representation shift`、`cross-mechanism generalization`

👤 **作者**：Zhen Guo、Shanghao Shi、Shamim Yazdani、Ning Zhang、Reza Tourani

- 🎯 **研究动机**：白盒防御只在单一攻击族上评测，异构攻击的表示位移能否泛化检测未知机制未知
- 🔬 **研究方法**：MechAudit-40：40 种攻击机制×5 开权重架构、10 万配对 clean-attack 表示、机制留出协议隔离真实位移
- 📌 **结论**：机制完全留出下隐状态恢复未知攻击类别 82.5%；运行时审计器检出 81.1% 留出攻击（FPR 0.70%），唯一避免机制级覆盖崩溃的检测器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While LLM attacks span prompt optimization, multi-turn context manipulation, retrieval poisoning, and model backdoors, white-box defenses are typically evaluated on isolated attack families. Consequently, whether heterogeneous attacks leave internal representation shifts that generalize to unseen threat mechanisms remains unknown. We present MechAudit-40, a systematic evaluation of 40 attack mechanisms across five open-weight model architectures. Threat-specific success criteria, 100,000 matched clean-attack representation pairs, predefined categories, and grouped holdouts isolate genuine attack-induced displacement from target scale, corpus bias, and data-leakage shortcuts. Across this testbed, attacks induce structured multi-depth trajectories rather than isolated layer spikes. While raw peaks are non-portable across architectures, target-calibrated profiles preserve transferable geometric signatures: under complete mechanism holdout, hidden states alone recover the threat category of unseen attacks with 82.5% accuracy. Guided by this finding, we design MechAudit, a runtime auditor that operates under strict zero-oracle constraints without requiring clean baseline traces or attack metadata. MechAudit detects 81.1% of held-out attack executions at a 0.70% false-positive rate and maintains 78.1% recall when an entire functional category is withheld. In matched comparisons, MechAudit is the only detector that avoids mechanism-level coverage collapse, maintaining over 50% recall across all 40 mechanisms. Internal representations thus support cross-mechanism attack-exposure auditing against calibrated benign references, but decouple from downstream task compromise and parameter integrity.

</details>

### 80. TIER: Threat Implicitness Benchmark for Evaluating LLM Safety Behaviors

📄 [arXiv](https://arxiv.org/abs/2609.05117)　📅 2026-09

**关键词**：`benchmark`、`LLM safety behavior`、`threat implicitness`、`behavior-aware evaluation`

👤 **作者**：Thu-Hien Trinh-Thi、Hai-Yen Vong、Thanh-Ha Ung-Dung、Tram Ho

- 🎯 **研究动机**：现有安全基准依赖二元指标，忽视模型面对不同威胁隐含度的行为渐变
- 🔬 **研究方法**：提出 TIER 基准：四个风险域 ×四个威胁级别（从显式有害请求到复杂越狱），用六标签行为尺度与两个独立 LLM judge 评估六个开源 LLM
- 📌 **结论**：安全行为随威胁级别渐变而非从拒绝直接切换到顺从；上下文 prompt 行为最多样、越狱暴露最大鲁棒性差距，ASR 相近的模型响应分布可截然不同——需要行为感知的安全评测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current LLM safety benchmarks largely rely on binary metrics, overlooking how models respond to harmful prompts with varying threat implicitness. We introduce TIER, a Threat Implicitness Benchmark for behavioral safety evaluation of LLMs. TIER covers four risk domains and four threat levels, from explicit harmful requests to sophisticated jailbreaks. Responses are assessed using a six-label behavior scale and two independent LLM judges. Experiments on six open-weight LLMs show that safety behaviors evolve gradually across threat levels rather than shifting directly from refusal to compliance. Contextual prompts yield the most diverse behaviors, while jailbreaks reveal the largest robustness gaps. Furthermore, models with similar Attack Success Rates can exhibit distinct response distributions, highlighting the need for behavior-aware LLM safety evaluation.

</details>

### 81. SoK: Rethinking Jailbreaking in the Era of Agentic AI: Attacks, Defenses, and Practical Consideration

📄 [arXiv](https://arxiv.org/abs/2609.12413)　📅 2026-09

**关键词**：`survey`、`agentic jailbreak`、`execution-aware defense`、`security-utility tradeoff`

👤 **作者**：Md Jueal Mia、Yanzhao Wu、Selcuk Uluagac、M. Hadi Amini

- 🎯 **研究动机**：LLM 从对话助手演进为会推理、规划、调工具、持记忆、多 agent 通信的 agentic 系统，原生安全对齐也大幅增强；既有越狱攻防结论建立在更早的模型上，哪些仍适用于现代 LLM 与 agentic 场景缺乏系统回答
- 🔬 **研究方法**：以 SoK 围绕完整 agentic 执行管线重构越狱安全：建立覆盖用户交互、规划推理、记忆、工具使用与 agent 间通信的统一攻防 taxonomy；提出 security-utility-efficiency 评测框架，区分原生有害 prompt 安全、对抗越狱鲁棒性与 agent 级安全结果；并在共同 agentic 框架下对代表性攻防做受控实证
- 📌 **结论**：三个缺口：强原生对齐不蕴含对抗越狱鲁棒性；防御效果高度依赖模型/攻击/组件且伴随过拒、效用与延迟代价；最终响应的低攻击成功率可掩盖规划、记忆与工具交互的严重中间失守——应从响应中心防御转向跨层执行感知安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are rapidly evolving from conversational assistants into agentic AI systems that reason, plan, invoke tools, maintain persistent memory, communicate with other agents, and execute multi-step tasks. At the same time, modern models exhibit substantially stronger native safety alignment than earlier generations on which many jailbreak attacks and defenses were originally studied. This shift raises a fundamental question: \textit{which established jailbreak-security findings remain valid in the era of modern LLMs and agentic AI?} We address this question through a Systematization of Knowledge (SoK) that reframes jailbreak security around the full agentic execution pipeline. We develop unified taxonomies of attacks and defenses spanning user interaction, planning and reasoning, memory, tool use, and inter-agent communication, and introduce a security--utility--efficiency evaluation framework that separates native harmful-prompt safety, adversarial jailbreak robustness, and agent-level security outcomes. We further conduct a controlled empirical study of representative attacks and defenses within a common agentic framework. Our results reveal three important gaps. First, strong native alignment does not imply robustness to adversarial jailbreaks. Second, defense effectiveness is highly model-, attack-, and component-dependent and can come at substantial cost in over-refusal, utility, and latency. Third, low final-response attack success can mask severe intermediate compromise: planning, memory, and tool interactions may remain unsafe even when the final response is successfully filtered. These findings motivate a shift from response-centric jailbreak defense toward cross-layer, execution-aware security that protects agent state, component transitions, and external actions while preserving practical utility and efficiency.

</details>
