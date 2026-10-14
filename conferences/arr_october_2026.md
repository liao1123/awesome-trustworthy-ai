# ARR 2026 October: AI Safety Papers（匿名预印本）

> ACL Rolling Review 2026 年 10 月周期的匿名预印本（Anonymous Pre-prints）中与 AI 安全相关的论文合集。作者信息按 ARR 匿名政策隐去，正式发表后本文件将更新作者与出处。

## 目录

- [一、越狱与对抗攻击](#越狱与对抗攻击)
- [二、越狱防御与安全监控](#越狱防御与安全监控)
- [三、安全对齐与机制可解释性](#安全对齐与机制可解释性)
- [四、dLLM（扩散语言模型）安全](#dLLM扩散语言模型安全)
- [五、开源模型治理与权重级安全](#开源模型治理与权重级安全)
- [六、投毒、后门与供应链攻击](#投毒、后门与供应链攻击)
- [七、Agent 安全：技能、注入与运行时治理](#Agent安全技能、注入与运行时治理)
- [八、遗忘与数据审计](#遗忘与数据审计)
- [九、隐私攻击与防御](#隐私攻击与防御)
- [十、检测、水印与溯源](#检测、水印与溯源)
- [十一、谄媚、欺骗与社会性风险](#谄媚、欺骗与社会性风险)
- [十二、安全评测与口径](#安全评测与口径)
- [十三、扩展视野（简表）](#十三扩展视野简表)

## 会议信息

| 项目 | 内容 |
|---|---|
| 会议 | ACL Rolling Review（ARR）2026 年 10 月周期 |
| 类型 | 匿名预印本（Anonymous Pre-prints，作者投稿时选择公开） |
| 数据来源 | OpenReview `aclweb.org/ACL/ARR/2026/October` 组 Anonymous Pre-prints 标签页（经 API 认证抓取） |
| 抓取时间 | 2026-10-14 |
| 公开预印本总数 | 3,385 篇 |
| 本文件收录 | 401 篇（P1 68 + P2 173 + P3 160） |
| 官方日历 | [aclrollingreview.org/dates](https://aclrollingreview.org/dates) |

## 关键节点

- 2026-10：ARR October 周期投稿与匿名预印本陆续公开（本文件基于 10-14 快照）
- 周期评审结果与作者去匿名后，将按 `conferences/` 惯例回填 arXiv/正式出处

## 筛选说明

- 按 `RESEARCH_INTERESTS.md` 边界对 3,385 篇公开预印本全量标题逐篇过目 + 摘要精读筛选；联邦学习/DP 密码学/TEE 等按硬排除处理
- P1 = 强匹配核心方向（投毒后门、Agent 安全、有害微调、安全机制、记忆/供应链攻击等）；P2 = 常规收录；P3 = 扩展视野（简表，宽进终选）
- 第四、五区（dLLM 安全、开源模型治理）对应 `RESEARCH_INTERESTS.md` 兴趣分类 25/26，单独成类追踪
- 卡片摘要来自 OpenReview 提交版本；论文尚在评审中，结论以最终版本为准

## 一、越狱与对抗攻击

### 1. Search-as-Jailbreak: Evaluating Jailbreak Vulnerabilities in LLMs with Real-World Open-Web Search Access

📄 [OpenReview](https://openreview.net/forum?id=CGjLZs4dao)　📅 2026-10　🏷️ P1

**关键词**：`jailbreak`、`search-augmented LLM`、`red teaming`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：搜索增强 LLM 可把碎片网络证据合成可操作程序性伤害——超出独立模型输出的操作深度
- 🔬 **研究方法**：SearchAttack 双阶段红队：自适应多跳搜索模式+评分标准逆向工程压力测试搜索触发与检索证据筛选行为，配新发 illicit 领域网络搜索基准与事实核查框架
- 📌 **结论**：对搜索增强 LLM 的负责任漏洞评估显示攻击高效——检索作为伤害放大器的安全面

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

To mitigate hallucinations, large language models (LLMs) are increasingly augmented with external search engines.
However, search-augmented LLMs can also synthesize fragmented web evidence into actionable procedural harm that fundamentally surpasses the operational depth of standalone model outputs.
To investigate this concern, we introduce SearchAttack, a dual-stage red-teaming framework that stress-tests the safety of LLMs' search-triggering and retrieved-evidence curation behaviors via adaptive multi-hop search-pattern and rubric reverse engineering.
We also curate a challenging web-search benchmark of emergent, domain-specific illicit activities and introduce a fact-checking framework to ground and quantify harmful informativeness in both offline and online attack settings.
Extensive experiments are conducted to red-team the search-augmented LLMs for responsible vulnerability assessment.
Empirically, SearchAttack demonstrates strong effectiveness in attacking these systems.

</details>

### 2. RepCloak: Breaking Superficial Compliance in Multi-modal Jailbreak via Representation Cloaking

📄 [OpenReview](https://openreview.net/forum?id=MdvPjIk8xF)　📅 2026-10　🏷️ P1

**关键词**：`multimodal jailbreak`、`representation cloaking`、`white-box attack`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：既有白盒攻击在肯定前缀后出现拒绝/乱码的安全反弹——对抗表示极端偏离正常查询流形
- 🔬 **研究方法**：RepCloak：最小化对抗表示与良性表示的几何距离把恶意查询伪装进正常流形
- 📌 **结论**：跨 MLLM 与数据集效能优越且抗扰动级别与跨数据集迁移——从表示几何破解表面合规（多模态越狱的机理化）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We focus on white-box jailbreaks for Multi-modal Large Language Models, yielding three primary contributions: 1) We identify and characterize the Safety Recoil phenomenon, wherein existing attacks produce unstable outputs, such as refusals or gibberish, immediately following an affirmative prefix. We link this behavior to the adversarial representation's extreme divergence from the manifold of normal queries. 2) We propose RepCloak, a novel approach that deceives MLLM safety mechanisms by minimizing the geometric distance between adversarial and benign representations. This effectively cloaks malicious queries within the normal manifold. 3) Through comprehensive experiments spanning various MLLMs and datasets, we validate RepCloak's superior efficacy and its resilience against diverse perturbation levels and cross-dataset transferability.

</details>

### 3. Selective, Therefore Vulnerable: How Input-Dependent Selectivity Exposes SSMs to Jailbreak Attacks

📄 [OpenReview](https://openreview.net/forum?id=XWAmDYqa3f)　📅 2026-10　🏷️ P1

**关键词**：`jailbreak`、`Mamba`、`architecture vulnerability`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：安全研究集中于 Transformer——SSM 架构的越狱脆弱性与其内部成分无关
- 🔬 **研究方法**：delta 引导对抗后缀优化：GCG 目标加入提升后缀 token 处 Δ 的项，纯 Mamba+两混合模型验证
- 📌 **结论**：Δ 大值衰减既往隐状态即擦除安全信息——引导 Δ 提升攻击成功率尤其对抗后缀防御——架构感知防御的靶点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite extensive research on the safety of Large Language Models (LLMs), such as their robustness to jailbreak attacks, existing work has focused on Transformer-based architectures, leaving State Space Model (SSM)-based architectures largely unexplored. Moreover, architecture-agnostic attacks such as GCG reveal that a model can be broken, but not which internal component makes it vulnerable. In this work, we show that Δ, the input-dependent time step that gives Mamba its selectivity, can be a structural vulnerability. Because a large Δ decays the previous hidden state, it can be exploited to erase safety-related information stored in the state. To verify this, we design delta-guided adversarial suffix optimization, which augments the GCG objective with a term that increases Δ at adversarial suffix tokens. Across a pure Mamba model and two Mamba-Transformer hybrid models, guiding Δ upward improves attack success over standard GCG in most settings, especially under suffix-based defenses. Our analyses show that this guidance aligns large Δ values with the decay of safety-related information, while reversing the objective to decrease Δ weakens the attack. These findings suggest Δ as a key target for architecture-aware defenses of SSM-based models.

</details>

### 4. Safe2Harm-Turbo: Safety Boundary Failure through Benign Task Projection

📄 [OpenReview](https://openreview.net/forum?id=e4iEeAgWXY)　📅 2026-10　🏷️ P1

**关键词**：`jailbreak`、`benign task projection`、`safety boundary`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：对显式有害请求有效的护栏在'看似良性任务'承载高风险目标时仍会失效——安全边界失败的系统刻画缺失
- 🔬 **研究方法**：Safe2Harm-Turbo 两形态：语义同构经良性任务获取共享知识后主题反转；SafeInHarm 沿合法父任务的风险相关分支归纳式提问，继承安全判断替代风险重估（层级安全继承）
- 📌 **结论**：开源与 API LLM 上双形态均高攻击成功率——良性任务投影作为安全边界失败机制（越狱的语义结构学）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The safety alignment of large language models (LLMs) faces persistent challenges from jailbreak attacks. Safeguards effective against explicit harmful requests may still fail when high-risk goals are pursued through seemingly benign tasks. To examine this failure, we present Safe2Harm-Turbo, a jailbreak framework based on Benign Task Projection. Safe2Harm exploits Semantic Isomorphism to acquire shared knowledge through benign tasks and redirect it through topic inversion. SafeInHarm advances along risk-relevant branches of legitimate parent tasks through Inductive Questioning, where inherited safety judgments may replace risk reassessment, a failure termed Hierarchical Safety Inheritance. Experiments across open-source and API-based LLMs demonstrate high attack success rates under both forms of Benign Task Projection. On the evaluated API-based LLMs, Safe2Harm and SafeInHarm achieve a maximum attack success rate (ASR) of 99.5% and 93.0%, respectively. Further mechanistic and defense analyses of Safe2Harm reveal that rewritten questions shift toward harmless references along the refusal direction, while inversion prompts and final outputs retain detectable harmful signals. These findings offer empirical grounding for multi-layered safeguards across task transformation and response generation.

</details>

### 5. Who Gave the Command? Black Box Speaker Provenance Attacks on Large Audio Language Model Voice Agents

📄 [OpenReview](https://openreview.net/forum?id=ihHj5gJeKP)　📅 2026-10　🏷️ P1

**关键词**：`attack`、`voice agent`、`speaker provenance`、`LALM`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：语音 agent 须同时判定谁的语音可请求动作与该语音是否真在请求——两条决策在源规则下的失效未测
- 🔬 **研究方法**：黑盒 Source Constraint Collision Attack：从非目标命令测得的源偏好中选普通竞争语音，完整工具调用匹配+请求/引述配对测试
- 📌 **结论**：偏好源诱导 87.5-100% 未授权调用（对照至多 4.2%）；分离发言人后引述命令仍触发动作——源拒绝与请求解读需分开评测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Voice agents must determine both whose speech may request an action and whether that speech actually makes a request.
We study these decisions under explicit source rules using English synthetic speech and complete tool call matching.
Our Source Constraint Collision Attack selects ordinary competing speech from source preferences measured on nontarget commands.
On selected music and lights tasks, preferred sources induce 87.5–100.0% unauthorized calls, versus at most 4.2% for opposite assignments.
The advantage weakens on jointly held out voices and paraphrases.
Matched tests of requests and quotations expose a separate failure with the designated source fixed.
Source ablations show that most audited source violations already occur without overlapping speakers.
Inputs separated by speaker still yield actions from quoted commands.
These results motivate evaluating source rejection and request interpretation separately, with legitimate request and valid no action controls.
The evidence concerns generated calls in controlled settings, without authenticated identities or execution on real services.

</details>

### 6. Question, Then Affirm: Restoring Commitment Does Not Restore Refusal

📄 [OpenReview](https://openreview.net/forum?id=DL8HSHlUaP)　📅 2026-10　🏷️ P2

**关键词**：`image generation safeguard`、`deferred semantic commitment`、`question form`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：图像生成安全可被不改消息内容绕过：断言被拦而'问句+勾号'通过且产出图 endorsing 原主张
- 🔬 **研究方法**：延迟语义承诺（DSC）界定+300 案例挑战集（gpt-image-2 直接陈述 vs 问句-确认对照）+开源模型内部拒答变化分析
- 📌 **结论**：问句确认 43.3% vs 直接 16.3% 出图、41.3% vs 15.3% 背书原命题——再背书只部分逆转问句引入的拒答变化；防护须评完整消息而非各元素

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We find that safeguards for image generation can be bypassed without changing what a message says. A sign stating a harmful proposition is blocked, but the same proposition phrased as a question and followed by a check mark is generated, even though the resulting image endorses the original claim. On a 300-case challenge set, gpt-image-2 returns images for 43.3% of question–affirmation requests versus 16.3% of direct statements, with 41.3% versus 15.3% of cases yielding images that endorse the original proposition. We define this as Deferred Semantic Commitment (DSC): commitment is withdrawn by the question and restored by a separate element, while safety behavior follows only the withdrawal. To investigate why, we study an open-weight language model and find that re-endorsement only partially reverses the refusal-related change introduced by questioning. These findings reveal a mismatch between recovered meaning and refusal behavior, motivating safeguards that assess the completed message rather than its individual elements.

</details>

### 7. Small Agents, High-Yield Attacks: Automated Jailbreaking under Tight Budgets

📄 [OpenReview](https://openreview.net/forum?id=EiTwV8yreV)　📅 2026-10　🏷️ P2

**关键词**：`automated jailbreak`、`low budget`、`small attacker`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：agent 驱动越狱依赖强 LLM 与大查询预算——现实安全测试双侧受限
- 🔬 **研究方法**：三阶段：发现攻击分布成功区域→蒸馏为直接生成→按单次尝试成功率优先排序
- 📌 **结论**：小攻击者低预算成功率大幅提升——资源与查询受限下的自动化越狱

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Automatic jailbreaking is an important approach for probing safety vulnerabilities in modern AI systems by testing their resistance to harmful-output elicitation. Agent-driven methods enable adaptive exploration and refinement of diverse jailbreak strategies. However, their effectiveness often relies on the LLM capabilities, such as reasoning and reflection, as well as large query budgets that allow repeated trial-and-error refinement. Such assumptions are often impractical in real-world security testing, where attacker-side computation and victim-side query budgets are both limited, making repeated use of powerful LLMs and iterative victim interactions costly or infeasible. We study resource- and query-constrained automated jailbreaking, where a small attacker must achieve high attack success with only a few queries to a black-box victim. We observe that small attackers can achieve strong attack success under sufficiently large query budgets, motivating us to improve their low-budget sampling efficiency. We therefore design a three-stage framework that first uncovers successful regions of attack distribution, then distills them into direct generation, and finally prioritizes attacks with higher per-attempt success probability. Extensive experiments across multiple jailbreak benchmarks and victim models demonstrate that our method substantially improves low-budget attack success over existing automated jailbreaking methods, particularly at ASR@1 and ASR@2.

</details>

### 8. Self-HarmLLM: Ranking Query Rewrites by Structured Safety Judgments for Black-Box Jailbreaking

📄 [OpenReview](https://openreview.net/forum?id=HuLAQSGslc)　📅 2026-10　🏷️ P2

**关键词**：`black-box jailbreak`、`soft phrasing`、`safety judge`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：间接措辞的有害请求可能被安全机制接受——黑盒三会话攻击框架
- 🔬 **研究方法**：Session A 重写为软化措辞 MHQ+隔离 Session C 同模型返回查询/答案安全标签与置信度，词典序选择器（有害答案>查询判安全>模糊区目标>低置信）
- 📌 **结论**：550 查询五目标内部判官 ASR 23.9%、外判官 4.9-41.5%——结构化安全自评作为黑盒越狱信号（模型自审可被武器化）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) safety mechanisms may accept harmful requests that are phrased indirectly. We present Self-HarmLLM, a black-box, three-session framework. In the main configuration (A=B=C), Session A rewrites a harmful query into a Masked Harmful Query (MHQ) that keeps the request in softer wording, Session B is the target, and a context-isolated Session C invocation of the same model returns query- and answer-safety labels, a harmfulness score, and verbal confidence. A lexicographic selector ranks candidates by harmful answer, query judged safe, proximity to an ambiguity-region harmfulness target, and lastly lower confidence. On 550 CategoricalHarmfulQA queries and five targets, the selector reaches a mean internal-judge attack success rate (ASR) of 23.9% and, under this judge, exceeds Direct, PAIR, Crescendo, and a same-budget FirstValid control on every target. An external GPT-4o judge gives lower, non-trivial ASR (4.9-41.5%), and 89-91% of internal successes preserve intent. Removing only the confidence term changes ASR by at most 1.1 points (McNemar p >= 0.36): the gain comes from query- and answer-level ranking; confidence is only diagnostic. As its own rewriter, gpt-oss-120b yields no valid MHQ for 30.5% of queries (attacker self-censorship).

</details>

### 9. BIRD: Bi-Level Operator Scheduling for Black-Box Attacks on Large Language Models

📄 [OpenReview](https://openreview.net/forum?id=Kl5U7eKJvr)　📅 2026-10　🏷️ P2

**关键词**：`black-box attack`、`operator scheduling`、`bandit`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：置信引导攻击依赖固定或手工算子集——算子效用随输入/模型/轨迹变化
- 🔬 **研究方法**：BIRD：攻击形式化为在线算子调度——滑动窗 UCB 上层选算子+置信引导下层选编辑
- 📌 **结论**：三基准三 LLM 平均 ASR 27.69→36.60 且语义相似度可比——黑盒攻击的算子调度化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Black-box attacks on LLM-based classifiers seek adversarial inputs that induce incorrect predictions without access to model parameters, gradients, or logits. Existing confidence-guided attacks typically rely on a fixed perturbation operator or a manually specified operator set, overlooking that operator utility varies across inputs, target models, and attack trajectories. We formulate black-box LLM attacks as an online operator scheduling problem and propose BIRD (BI-level Bandit-dRiven Operator ScheDuling), a bi-level framework for automatic black-box attacks. BIRD maintains a heterogeneous pool of perturbation operators and adaptively schedules them using elicited confidence feedback. At the upper level, a sliding-window UCB scheduler selects operators according to cost-aware rewards; at the lower level, confidence-guided candidate selection accepts edits that reduce confidence in the original prediction or flip the label. Experiments on three benchmarks and three instruction-tuned LLMs show that BIRD improves average attack success rate from 27.69 to 36.60 over a strong single-operator confidence-guided baseline, while keeping sentence-level semantic similarity comparable, at the cost of higher perplexity and moderately more queries. Against fixed operator compositions, BIRD does not always attain the highest raw success rate, but it is not dominated on the effectiveness–quality–cost trade-off and needs no dataset- or model-specific operator preselection.
Code is available at https://anonymous.4open.science/r/BIRD.

</details>

### 10. Adaptive Target Token Weighting and Refusal Divergence for Optimization-Based Jailbreak Attacks

📄 [OpenReview](https://openreview.net/forum?id=Ma5jTNGYcT)　📅 2026-10　🏷️ P2

**关键词**：`jailbreak optimization`、`token weighting`、`refusal divergence`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：优化型越狱目标 token 固定权重且辅助续算昂贵
- 🔬 **研究方法**：ATRD 损失：低概率目标 token 更大权重+缓存拒答锚在目标位与后首位增大拒答散度（免辅助续算）
- 📌 **结论**：多语言与视觉语言模型 100% 攻击成功、GPT-3.5-Turbo 迁移 +22pp——优化型越狱的效率增强

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have advanced rapidly, yet jailbreak attacks can still bypass their safety alignment and elicit harmful responses. Among these attacks, optimization-based jailbreak attacks search for adversarial inputs but face two limitations. First, target losses use fixed token weights despite differences in target token prediction difficulty. Second, evaluating auxiliary continuations to address refusals increases the computational cost of each optimization step. To address these limitations, we propose the Adaptive Target Token Weighting and Refusal Divergence (ATRD) loss. ATRD assigns larger weights to target tokens with lower probabilities, focusing optimization on harder target positions. It increases refusal divergence from cached refusal anchors at the target positions and the first position after the target text, without evaluating auxiliary continuation sequences. Experiments show that ATRD achieves 100% attack success on multiple language and vision-language models and improves transfer attack success on GPT-3.5-Turbo by up to 22 percentage points.

</details>

### 11. TagFuzz: Tag-Indexed Stateful Fuzzing of LLM-Based Robot Planners

📄 [OpenReview](https://openreview.net/forum?id=OTPEQFzod7)　📅 2026-10　🏷️ P2

**关键词**：`robot planner`、`fuzzing`、`action-channel jailbreak`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：LLM 机器人规划器的语言-动作边界：伴随语音看似安全而结构化命令推进被禁目标——需跨重写跟踪任务语义的状态化测试
- 🔬 **研究方法**：TagFuzz：标签索引变异规则库+冻结任务标签引导检索与排序+动作导向 oracle 解析结构化响应判与被禁目标对齐
- 📌 **结论**：动作通道越狱率 83.80% 且匹配查询预算下超最强基线 23.05pp——机器人规划器的状态化模糊测试

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based robot planners translate natural-language requests into structured commands for downstream controllers. At this language-to-action boundary, commands can advance a prohibited objective even when accompanying speech appears safe. Testing this boundary requires tracking task semantics through prompt rewrites, reusing relevant discoveries, and adapting to failed attempts. Fixed rewrites lack feedback, while task-local refinement confines search experience to individual tasks. We present TagFuzz, a novel stateful, tag-indexed black-box fuzzer for action-channel jailbreaks. TagFuzz organizes transformations in a configurable mutation-rule library whose entries combine mutation instructions, tag preferences, and scheduling rules. Frozen task tags guide retrieval from an evolving corpus and rank library entries, while task-local failures redirect subsequent mutations. Newly accepted prompts enrich the corpus for reuse across tasks. Its action-oriented oracle parses structured responses, applies task-specific checks, and judges alignment with the original prohibited objective. TagFuzz achieves an 83.80% overall action-channel jailbreak rate and outperforms the strongest evaluated baseline by up to 23.05 percentage points under matched planner-query ceilings. Ablations show that library breadth and retained search experience improve coverage. Tests in ProgPrompt/VirtualHome and VoxPoser trace generated plans to completed execution and environment-state changes, demonstrating the downstream consequences of unsafe planner outputs.

</details>

### 12. When Humans Leave Context Unsaid: Implicit Context as a Risk for Large Language Models

📄 [OpenReview](https://openreview.net/forum?id=UrLpCPjloI)　📅 2026-10　🏷️ P2

**关键词**：`implicit context`、`social harm`、`attack`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：人类语言依赖隐含语境（预设/会话含义）——其缺席于训练语料成为被忽视的对齐风险
- 🔬 **研究方法**：引导 LLM 从暗示社会伤害的提示推断隐含语境线索（预设/含意）再利用推断语境诱导更多有害内容
- 📌 **结论**：利用隐式风险的攻击跨开闭源模型大幅超基线——对齐过程对隐含语境的盲区即攻击面

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Human language is grounded in pragmatics, necessitating implicit (extralinguistic) context to interpret language, e.g., world knowledge and social norms. However, such context is often implicit rather than explicitly expressed in language, requiring humans to infer the underlying contextual information necessary for language understanding. Because of its implicit nature and absence from textual corpora, it is often overlooked in the subsequent alignment process. In this paper, we demonstrate that the absence of such implicit context in training data is a risk for LLMs, and we refer to this risk as the implicit risk for LLMs. To exploit this implicit risk, we propose a method that guides LLMs to infer implicit contextual cues, such as presuppositions and implicatures, from prompts that imply social harm, and then leverages these inferred implicit context to elicit additional socially harmful content. Experimental results demonstrate that attacks exploiting the implicit risk we identify consistently outperform baseline methods by substantial margins across a diverse range of open- and closed-source models, underscoring the need for new defense methodologies that account for overlooked implicit context.

</details>

### 13. FlipJev: Fast Black-Box Red Teaming Finds Universal Adversarial Suffixes for Typed Decision Models

📄 [OpenReview](https://openreview.net/forum?id=XUM75xrCve)　📅 2026-10　🏷️ P2

**关键词**：`universal suffix`、`typed decision models`、`red teaming`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：typed 决策模型单次快查询用于安全敏感任务——既有自适应攻击不用其速度、少有通用对抗例搜索
- 🔬 **研究方法**：FlipJev：无攻击者 LLM 的快速黑盒查询攻击在 Jev 上找短后缀翻转自信答案，12 数据集跨任务迁移测试
- 📌 **结论**：Jev 抗常见注入（10240 配对测试零翻转）而攻击数分钟找到后缀：每数据集一个后缀翻 43% 未见文档、跨任务迁移翻 90-100%——typed 决策模型须含严格自适应攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Typed decision models are an emerging class of language models that make decisions instead of generating free-text responses. They answer in a single fast and cheap query and are increasingly used, including in security-sensitive tasks. However, red teaming of these models leaves two gaps: existing adaptive attacks do not use their speed, and few studies have searched for universal adversarial examples. We fill both gaps on Jev, the representative typed decision model, with a quick black-box query-based attack that calls no attacker language model. We conduct extensive experiments on 12 datasets with different data types and application scenarios. The results show that Jev resists common prompt injections: no strategy changes a correct answer in 10,240 paired tests. In contrast, our attack finds short suffixes that flip confident answers within minutes. These suffixes are universal: one suffix per dataset flips 43% of unseen documents. Because typed decision models, unlike classic NLP models, can serve many tasks, we test whether these suffixes transfer across tasks. We find that one suffix generated from one task can flip 90-100% of the samples in other tasks. We therefore believe the evaluation of typed decision models must include strict adaptive attacks to fully reveal their robustness.

</details>

### 14. Do LLM Jailbreaking Methods and Defenses Generalize across Languages?

📄 [OpenReview](https://openreview.net/forum?id=YwJPwQ39Zg)　📅 2026-10　🏷️ P2

**关键词**：`multilingual jailbreak`、`cross-lingual robustness`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：多语研究显示低资源更脆弱——但四类攻击×两类防御×十语言的系统对照缺
- 🔬 **研究方法**：故事情境/逻辑表达式/对抗提示/LLM 攻击者四攻击×提示与分类器两防御×十语言×六模型 HarmBench/AdvBench
- 📌 **结论**：语言脆弱性反转：高资源语言总体更安全但在数类越狱下更脆弱——强语言能力≠强对抗鲁棒；自验证与多语安全分类器大幅降不安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreaking attacks can bypass the safety alignment that large language models undergo. Multilingual investigations have shown that low-resource languages can be more vulnerable to unsafe questions. Given the complexity of factors involved in LLM safety across languages, as well as the need to develop robust defenses, we conduct a systematic investigation of both. We evaluate four types of jailbreaking attacks and two types of defenses across ten high-, medium-, and low-resource languages on the HarmBench and AdvBench benchmarks, for six LLMs. We include four attack types based on story contexts, logical-expressions, adversarial-prompts, and LLM attackers, and prompting- and classifier-based defenses. Besides the expected cross-lingual variation, we find a reversal in language vulnerability: high-resource languages are generally safer but are relatively more vulnerable under several jailbreak types. Thus stronger language capabilities do not necessarily imply greater adversarial robustness. Defense effectiveness also varies across languages and models, although self-verification and multilingual safety classifiers substantially reduce unsafe responses in many settings. Our results show that multilingual safety cannot be inferred from standard query behavior alone, and that successful defense varies with language and model.

</details>

### 15. Lost in Conversation: A Systematic Evaluation of Multilingual Multi-turn Jailbreak under Language Switching

📄 [OpenReview](https://openreview.net/forum?id=bRNLenzuES)　📅 2026-10　🏷️ P2

**关键词**：`multilingual jailbreak`、`multi-turn`、`language switching`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：多语安全研究多为孤立提示——对话语言组合对越狱的影响未测
- 🔬 **研究方法**：4000 个对话上下文×10 语言，固定最终请求语言、变换前文对话语言
- 📌 **结论**：多语会话上下文显著改变模型安全且随语言组合大幅波动——多轮语言切换越狱系统评测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLMs increasingly support multilingual interaction, yet their safety behavior can vary across languages. Multilingual safety research has largely focused on isolated prompts, leaving the impact of conversational context underexplored. We investigate this gap in multi-turn conversations with language switching. We construct 4,000 dialogue contexts across 10 languages, holding the final request language constant while varying the preceding dialogue languages. We evaluate proprietary and open-weight LLMs to analyze how dialogue language composition influences jailbreak success. Multilingual conversational context can noticeably alter model safety, with marked variation across language compositions. We will release the benchmark to facilitate reproducible research on multilingual LLM safety.

</details>

### 16. BanditFlow: Learning Query-Adaptive Strategies for LLM Red-Teaming

📄 [OpenReview](https://openreview.net/forum?id=cd59DDy815)　📅 2026-10　🏷️ P2

**关键词**：`red teaming`、`diverse generation`、`GFlowNet`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：自动红队在有效性与多样性间两难——奖励最大化塌缩到窄重复利用
- 🔬 **研究方法**：BanditFlow：神经上下文 bandit 探索高层攻击策略+GFlowNet 按奖励比例采样 token 级对抗提示（覆盖多高奖励模式）
- 📌 **结论**：两攻击者三受害模型 ASR 与多样性同升、避免 PPO 式塌缩且迁移到未见架构——多样化红队生成

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) are adopted in safety-critical domains, automated red teaming is essential for scalable vulnerability detection. However, existing generation methods face a fundamental tension between effectiveness (eliciting harmful behavior) and diversity (variability of discovered attacks): methods tuned to maximize attack success usually collapse onto narrow, repetitive exploits. We introduce BanditFlow, a hierarchical framework that reframes red teaming as a reward-guided diverse generation problem. Our approach operates at two levels: (1) a Neural Contextual Bandit that explores an exponentially large space of high-level attack strategies, and (2) a GFlowNet policy that samples token-level adversarial prompts with probability proportional to their reward, covering many high-reward modes rather than converging to a single template. Across two attacker models and three victim LLMs, BanditFlow substantially improves attack success rates while maintaining attack diversity, avoiding the collapse observed in reward-maximization approaches like PPO. Discovered attacks are also transferable to unseen victim architectures, offering a more thorough methodology for uncovering LLM vulnerabilities.

</details>

### 17. Decoding Harm: Do Reasoning Models Resist Math-Encoded Jailbreaks?

📄 [OpenReview](https://openreview.net/forum?id=dsunhcS1QV)　📅 2026-10　🏷️ P2

**关键词**：`math-encoded jailbreak`、`reasoning robustness`、`judge audit`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：数学编码遮蔽有害请求——推理时增强是否提升对此类攻击的鲁棒性未知
- 🔬 **研究方法**：三数学形式体系×两基准×OpenAI/DeepSeek/Google 模型：提供者匹配比较+固定检查点推理配置干预+三判官与人工标签审计
- 📌 **结论**：ASR 随模型与形式体系大变；推理增强不一致改善鲁棒性；判官间 ASR 估计差异大——推理不是可靠防御（受控实验+判官审计的口径）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mathematical encoding can obscure harmful requests and undermine the safety mechanisms of large language models (LLMs). However, whether inference-time reasoning improves robustness against such attacks remains unclear. We systematically evaluate math-encoded jailbreaks across three mathematical formalisms, two safety benchmarks, and models from OpenAI, DeepSeek, and Google. To distinguish reasoning-related effects from differences between model checkpoints, we combine provider-matched comparisons with fixed-checkpoint interventions that vary inference-time reasoning configurations. We further examine evaluation reliability using three LLM judges and a human-label audit. Results reveal substantial variation in attack success across models and mathematical formalisms. Fixed-checkpoint interventions show configuration-dependent effects but provide limited evidence that increased reasoning consistently improves robustness. We also find substantial differences in attack-success estimates across judges. These findings highlight the limitations of treating inference-time reasoning as a reliable defense and underscore the importance of controlled experiments and judge-audited safety evaluation.

</details>

### 18. Does Single-Turn Evaluation Miss the Failure? Stress-Testing Safety Alignment on Social Bias under Sustained Adversarial Persuasion

📄 [OpenReview](https://openreview.net/forum?id=jFO2Picmyl)　📅 2026-10　🏷️ P2

**关键词**：`social bias`、`sustained persuasion`、`multi-turn`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：单轮基准不能捕捉初始无偏模型被十轮持续对抗说服动摇为刻板背书
- 🔬 **研究方法**：三 agent 协议：同模型同主张在说服前/单轮后/十轮持续劝说下对照+logos/ethos/pathos 三修辞策略
- 📌 **结论**：Llama-3.3-70B 背书率 19.6%→48.2% 而单轮无此幅度；pathos 对三模型全升——说服前最低的模型恰会被单轮测试排为最稳健（偏置评测的对话化）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Single-turn benchmarks cannot capture whether a model that initially responds without bias can be swayed to endorse a stereotype over a conversation. To test whether single-turn results hold, we introduce a three-agent protocol that compares the same models on the same claims before persuasion, after a single exchange, and over ten turns of sustained adversarial persuasion. A persuader model attempts to convince the model under test to endorse stereotypical claims, adapting its approach to the responses it receives. The persuader combines social pressure tactics with one of three rhetorical strategies, appealing to logic (logos), authority (ethos), or emotion (pathos). A separate judge model scores the conversation for endorsement of the claim. For Llama 3.3 70B, endorsement rose from 19.6% to 48.2% over ten turns. A single exchange with the persuader produced no rise of this size. Pathos raised endorsement for all three tested models, while Gemini 3.1 Flash-Lite and GPT-4o-mini showed no statistically significant increase under logos or ethos. Strikingly, Llama had the lowest endorsement rate of the three models before persuasion, so a single-turn test would have ranked it the most robust. This points to a need for bias evaluation protocols that test a model across a conversation rather than scoring its first response alone.

</details>

### 19. Rethinking Long-Context Jailbreak Attacks for Large Language Models

📄 [OpenReview](https://openreview.net/forum?id=nYpx4BXmzX)　📅 2026-10　🏷️ P2

**关键词**：`long-context jailbreak`、`mechanism`、`attention allocation`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：更长上下文更易越狱的既有假设覆盖面窄机制不明
- 🔬 **研究方法**：12 前沿×5 越狱法×3 填充类型×7 长度（至 480K 字符）+拒答表示与注意力分配机制分析
- 📌 **结论**：攻击类型决定 ASR 变化方向、填充内容决定幅度：约束型随长升、说服型随长降；填充分流注意力——长上下文越狱的机制图谱

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Long-context large language models are increasingly used in agentic and long-horizon workflows, yet their safety behavior under extended contexts remains poorly understood. Prior works suggest that longer contexts increase jailbreak vulnerability, but typically cover a limited set of model families, attack methods and padding types, leaving the mechanisms unclear. We revisit this assumption through a systematic evaluation of 12 frontier LLMs, 5 jailbreak methods, 3 padding types, and 7 context lengths up to 480K characters. Our results reveal two robust patterns: attack type determines the direction of attack success rate change, while padding content determines its magnitude. Specifically, constraint-based attacks become more effective as context length increases, whereas persuasion-based attacks become less effective. Harmful QA-style padding amplifies attacks strongly, and benign dialogue suppresses attacks. To explain these findings, we conduct mechanistic analyses of refusal representations and attention allocation. The results show that paddings divert attention away from the prompt, strongest under harmful QA-style padding and weakest under benign dialogue. At the final layer, the refusal signal strengthens for persuasion-based attacks as context grows but weakens for constraint-based ones. Together, our findings provide a flexible evaluation framework and a diagnostic lens for long-context jailbreak behavior, highlighting the need for context-aware defenses.

</details>

### 20. Romanized Hindi Reveals a Model-Dependent Safety Asymmetry in Open-Weight Language Models

📄 [OpenReview](https://openreview.net/forum?id=puAOSfzwF9)　📅 2026-10　🏷️ P2

**关键词**：`multilingual safety`、`colloquial register`、`audit`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：英语安全评测不保证同模型在其他语言拒绝同一请求——对齐-理解解耦假设需意义匹配对照检验
- 🔬 **研究方法**：504 对意义匹配英语-罗马化印地语提示（双自动审计器认证等价）+四信息-协助分级判官+人工验证
- 📌 **结论**：Qwen3-30B 英语扣留 65.9% vs 罗马化 22.8%（差 43.1pp）而 Nemotron 差 -1.8pp——英语安全结果不可预测口语语域行为，审计须直测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety evaluations in English do not guarantee that a language model will refuse the same harmful request in another language. One explanation is the alignment-comprehension decoupling hypothesis. It holds that models may understand informal non-English inputs yet fail to apply refusal behavior learned mostly from English data. Existing multilingual benchmarks often change prompt meaning during translation, which confounds language with prompt drift. We therefore build a frozen bank of 504 meaning-matched English and Romanized Hindi prompt pairs. Two automated auditors certify each pair as equivalent before any target model sees it. An automated judge scores each response on a four-level information-assistance scale. Qwen3-30B withholds assistance on 65.9% of English requests but on only 22.8% of Romanized Hindi requests. This difference is a gap of 43.1 percentage points. GPT-OSS-20B and Nemotron-3-Nano show gaps of 4.6 and -1.8 points. Qwen's gap persists under a replacement judge and in the ratings of two human annotators. Qwen and Nemotron withhold assistance at similar English rates but differ by 41.1 points in Romanized Hindi. English safety results therefore do not predict behavior in this register, and audits should test colloquial registers directly.

</details>

### 21. Same Harm, Different Words: Idiomatic versus Direct Harmful Requests in Persian and English

📄 [OpenReview](https://openreview.net/forum?id=ry3qdyknSI)　📅 2026-10　🏷️ P2

**关键词**：`idiomatic harm`、`Persian-English`、`safety benchmark`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：有害意图常以习语表达而基准直陈——同义习语 vs 直述双胞胎对照缺失
- 🔬 **研究方法**：101 波斯语母语验证习语+101 匹配英语习语（非翻译），角色扮演请求内习语位换直接短语，250 对/语言×10 LLM
- 📌 **结论**：习语版在 20 组中 17 组获更多不安全响应（至多 +21pp）、拒答更少但单独分类时 96%+ 双版本被标有害——安全评测须含习语表达

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety benchmarks for large language models (LLMs) usually state harmful requests directly, but people often express harmful intent through idioms, such as wanting to ``drag someone's name through the mud''. We ask whether models respond differently to the same harmful request when it is phrased with an idiom instead of stated directly. We build a Persian–English benchmark of 101 Persian idioms validated by native speakers as harm-relevant and 101 English idioms matched to the same meaning groups (not translated). Each idiom appears in a role-play request, and a direct twin replaces the idiom with a direct phrase for its validated meaning while keeping everything else identical (250 pairs per language). We test ten LLMs and count a response as unsafe only if it gives detailed, actionable help. The idiomatic version receives more unsafe responses in 17 of 20 model–language settings, by up to 21 percentage points, and its 95% bootstrap interval excludes zero in 14 of them (uncorrected for multiple comparisons). The difference coincides with fewer refusals: models refuse idiomatic requests less often, even though, when asked in a separate classification call, they label over 96% of both versions as harmful. The effect was measured under one role-play template; with less context it shrinks or reverses. Safety evaluations should therefore include idiomatic phrasing, not only direct requests.

</details>

### 22. Where the Guardrails Give Way: Evaluating Medical Jailbreak Vulnerability in LLMs Across Framings, Tasks, and Languages

📄 [OpenReview](https://openreview.net/forum?id=tmmNLvVxjM)　📅 2026-10　🏷️ P2

**关键词**：`medical jailbreak`、`multilingual`、`framing`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：医疗安全评测的攻击多样性与语言覆盖不足
- 🔬 **研究方法**：M-FraME：六框架（直接/间接/情感/假设/随机角色/指定角色）×四语言（英/印地/孟加/乌尔都）×六 LLM，14044 标注响应（双判官+人裁）
- 📌 **结论**：假设框架诱发最高不安全顺从、间接改写反而降 ASR；剂量调整与个性化治疗比诊断更易被利用——框架与话题感知的医疗安全评测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent progress in LLM safety research has produced numerous jailbreak techniques, yet medical-safety evaluations remain limited in attack diversity and language coverage. We address these gaps through a controlled study using M-FraME (Multilingual Framed Medical Evaluation), covering six framing conditions (direct, indirect, emotional, hypothetical, random role-play, and assigned role-play) across four languages (English, Hindi, Bangla, and Urdu). Built on PatientSafetyBench queries, our study evaluates six LLMs, using unchanged queries as the direct-framing baseline. Two LLM judges assess each response, with human adjudication of disagreements, yielding 14,044 labeled responses after excluding ambiguous cases. Our results reveal that medical safety is not framing-robust: hypothetical framing elicits the highest unsafe compliance, emotional framing is the least effective technique, and indirect rewording generally reduces attack success relative to direct queries. These effects remain largely consistent across models and languages, despite variations in overall attack success. Exploitability also varies by medical topic, with dose adjustment and personalized treatment more vulnerable than diagnosis. Our findings highlight the need for framing-aware and topic-aware safety evaluations of medical LLMs.

</details>

### 23. The Battle of Prompts: An Empirical Study of Prompt Execution Priority in LLM Adversarial Attacks

📄 [OpenReview](https://openreview.net/forum?id=wKroHuLXrG)　📅 2026-10　🏷️ P2

**关键词**：`prompt execution priority`、`unified mechanism`、`jailbreak`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：越狱与注入独立研究——多冲突提示下执行优先级偏好这一共同机制未被刻画
- 🔬 **研究方法**：PEC 框架+PECBench：位置/语言/模态对执行优先级的影响系统评测+未对齐模型与防御对照
- 📌 **结论**：LLM 显著偏向前/后位、高资源语言与时序模态；安全对齐只是掩盖这些固有偏置的语义混淆变量——对抗提示攻击的统一机制论

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety vulnerabilities in Large Language Models (LLMs) remain a critical barrier to their widespread deployment. Although independent research has focused on specific adversarial prompt attacks, such as jailbreak and prompt injection, their shared mechanisms remain unexplored. Specifically, it is unclear how the execution priority of LLM prompts influences attack and defense outcomes when models confront multiple conflicting prompts. We introduce the Prompt Execution-Priority Competition (PEC) to characterize LLM behavioral preferences in such scenarios. Utilizing our constructed benchmark PECBench, we systematically evaluate the impact of position, language, and modality on prompt execution priority. The results reveal that LLMs exhibit significant PEC biases, predominantly favoring the first or last position, high-resource languages, and temporal modalities, which contradict the conclusions of existing research on jailbreaks of safety-aligned LLMs. Further experiments on unaligned models reveal that PEC bias is also a stable determinant of adversarial attack success, while defensive measures like safety alignment act merely as semantic confounders masking these inherent biases. This study offers a novel perspective on the unified mechanism of adversarial prompt attacks, such as jailbreak and prompt injection, and establishes a theoretical foundation for future defenses.

</details>

### 24. Beyond English-Centric LLM Safety: A Controlled Korean-English Evaluation of Jailbreak and Prompt-Injection Robustness

📄 [OpenReview](https://openreview.net/forum?id=y2sYlbUcNM)　📅 2026-10　🏷️ P2

**关键词**：`multilingual safety`、`jailbreak`、`prompt injection`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：安全与注入防御很少跨语言与部署设置同测
- 🔬 **研究方法**：23 个韩/国际模型×韩英双语 11350 实例/语言：有害请求×四类越狱×两种注入位置，三判官以响应语言评分
- 📌 **结论**：模型排名随攻击类型而变、韩英差随模型而变——联合安全+安全画像支撑选型（双语对照评测）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM evaluations increasingly cover multiple languages, but rarely compare harmful-content safety and prompt-injection defense together across languages and deployment settings. We evaluate 23 Korean and international LLMs on a Korean–English benchmark with 11,350 planned test instances per language. It combines harmful requests, four types of jailbreak, and prompt injections placed either in user input or in content the model processes. Three LLM judges score safety responses using criteria written in the response language. Both safety and injection defense are reported on a 0–100 scale, with higher scores indicating stronger defense. Model rankings differ across attack types, and Korean–English score differences vary across models. Removing subjective scoring criteria largely preserves safety rankings, although some language comparisons change with the criteria or judges used. Joint safety and security evaluation reveals model-specific defense profiles, informing model selection for different application needs. The benchmark combines bilingual testing, deployment information, and checks of scoring reliability to make these comparisons easier to interpret. Data and code are available at https://anonymous.4open.science/r/RedTeam-65D5.

</details>

## 二、越狱防御与安全监控

### 25. Prompt-Injection Probes Learn the Conversation, Not Just the Injection

📄 [OpenReview](https://openreview.net/forum?id=0YISlkuO5d)　📅 2026-10　🏷️ P1

**关键词**：`prompt injection`、`linear probe`、`matched negatives`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：注入探针被当廉价监控器——但其训练可被会话位置与文本长度等捷径通过（0.91-0.98 AUROC 无模型即可达）
- 🔬 **研究方法**：构造同会话无注入/无害注入形似文本作为匹配负例加入训练，六开源模型对照
- 📌 **结论**：仅改训练数据把无注入对话误报 41-80%→4-27%、形似物 92-98%→3-16% 且保持 95% 检出——探针评测的捷径修正

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Linear probes on a model's hidden states are used as cheap monitors for indirect prompt injection: they screen the tool outputs an agent reads and send suspicious ones to a slower second check, so every false alarm has a cost. But a probe learns whatever separates its training examples. The standard evaluation of injection probes can be passed without the model: conversation position and text lengths alone reach 0.91–0.98 AUROC. When each attack is compared with the same conversation without the injection, or with harmless text formatted like an injection, standard probes flag most of these harmless cases. We add such cases to the training data as matched negatives. Across six open models, in applications seen during training and at the default threshold, changing only the training data cuts false alarms on injection-free conversations from 41–80% to 4–27%, and on harmless look-alikes from 92–98% to 3–16%. With a threshold set on normal traffic, our probe still catches a median 95% of the attacks that fooled the agent (91% without our data). In new applications, false alarms stay low, but detection depends on the model and on how the threshold is set. The same data also helps a text-only filter.

</details>

### 26. Toward Reliable Reward-Hacking Detection in LLMs

📄 [OpenReview](https://openreview.net/forum?id=Vl64wrAOFu)　📅 2026-10　🏷️ P1

**关键词**：`reward hacking`、`judge validation`、`controls`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：可靠 reward hacking 检测需要监控器区分失准与普通行为的证据——LLM 判官的对照验证缺失
- 🔬 **研究方法**：受控奖励训练模型（长度/积极情绪/谄媚加分）+未训练与仅奖励控制组，跨检查点评参照比较/判官指令/CoT 访问
- 📌 **结论**：加分模型高检出常伴高控制误标；参照比较对未训练基线可分但对仅奖励控制差、机制特定 rubric 改善选择设置——检测需匹配控制组与显式行为证据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reliable reward-hacking detection requires evidence that a monitor distinguishes misaligned behavior from ordinary model behavior. We study this requirement for LLM judges using models trained with controlled bonuses for length, positive sentiment, or sycophancy, alongside untrained and reward-only controls. Across training checkpoints and response batches, we evaluate reference comparisons, judge instructions, and access to chain-of-thought (CoT). High detection rates on bonus-trained models frequently coincide with high control-model flagging. Reference comparisons improve score-based discrimination against the untrained base, but provide limited separation from reward-only controls. Mechanism-specific response rubrics improve separation in selected settings, whereas majority-rule instructions can suppress both control flagging and detection. For our reasoning model, chain-of-thought monitoring does not consistently increase detection rates compared with judging responses alone. Our labels describe training conditions rather than independently verified hacking, so these results identify promising monitoring practices and their validation limits. They motivate matched control evaluations and explicit behavioral evidence as steps toward reliable reward-hacking detection.

</details>

### 27. How Robust Are Activation Probes for LLM Monitors? Deployment Shifts and Adaptive Evasion

📄 [OpenReview](https://openreview.net/forum?id=b7wX36ziiz)　📅 2026-10　🏷️ P1

**关键词**：`activation probe`、`adaptive evasion`、`monitor robustness`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：探针在有限验证设置选定校准——提示/上下文/群体/模型/优化压力变化下的部署性能未刻
- 🔬 **研究方法**：鲁棒性清单式评测+自适应极小极大压力测试（保 judged-untruthful 生成下对线性探针更新策略）+层扫与几何诊断
- 📌 **结论**：非对抗下线性探针出奇稳健（跨改写/社会框架/邻层）但组合逻辑/无关干扰/阈值迁移失败；极小极大训练大幅降解新训探针且真值信息被重组而非移除——监控探针的自适应瓶颈

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Activation probes are increasingly used as monitors for latent LLM behavior such as truthfulness or deception. Because such probes are selected and calibrated on limited validation settings, their deployment performance may vary when prompts, contexts, populations, models, or optimization pressures change. Toward characterizing probe robustness under such shifts, we develop a robustness checklist for activation-probe monitors and use it to evaluate probes across a variety of settings. In non-adversarial settings, we find that for factual truth detection and on-policy deception detection, linear probes are often surprisingly robust: they transfer across paraphrases, social framing, nearby layers, and some model variants. However, this robustness is uneven. Probes fail under compositional logic, false positives on irrelevant contextual distractors, threshold transfer, and combined shifts. We then study an adaptive minimax stress test in which a policy is updated against linear probes while preserving judged-untruthful generations. On FalseQA, minimax training substantially degrades freshly retrained linear probes while preserving mostly valid judged-untruthful generations, and ordinary deployment shifts compound this degradation. Layer-sweep and geometry diagnostics suggest that truthfulness information is reorganized rather than simply removed, exposing a specific bottleneck of simple linear readouts. Overall, linear probes are useful under many non-adversarial deployment shifts, but they can fail sharply when monitor-aware optimization is composed with deployment shifts.

</details>

### 28. HealthJailbreak: Scope-Aware Jailbreak Evaluation and Policy-Conditioned Alignment for Health Chatbots

📄 [OpenReview](https://openreview.net/forum?id=0F7TH61Xy3)　📅 2026-10　🏷️ P2

**关键词**：`jailbreak benchmark`、`scope-aware`、`health chatbot`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：越狱基准测通用危害——受限健康 chatbot 拒绝离题请求即可得高分，范围内有害内容未被评估
- 🔬 **研究方法**：范围感知多轮攻击者实证+HealthJailbreak 700 有害/安全目标对（136 风险归纳为 21 子政策）+policy-swap DPO 单模型跟随系统提示指定范围
- 📌 **结论**：限范围只降通用 ASR 0.65→0.51 而范围内 0.79→0.77 几乎不变——范围化安全增益被通用基准高估；策略换 DPO 平均降 16% ASR

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Health chatbots are often restricted to health or to a single health task, but jailbreak benchmarks assess general harms, such as weapons or cybercrime, to unrestricted models. A restricted chatbot scores well on such a benchmark simply by declining off-topic requests, while an adversarial user can still elicit harmful health content within its scope. Using scope-aware multi-turn attackers, we show that restricting the same model from a general to a health scope lowers attack success (ASR) on a general benchmark (0.65 to 0.51). General benchmarks overstate the safety gained by scoping. We introduce HealthJailbreak, a carefully curated benchmark of 700 harmful and safe goal pairs on which the same restriction leaves ASR nearly unchanged (0.79 to 0.77). Its safety policy is derived from 136 risks cataloged from 40 health-AI papers and consolidated against NIST and WHO guidance into 21 sub-policies. We also propose policy-swap DPO, which trains a single model to follow whichever operational scope its system prompt specifies, under one shared safety policy, instead of retraining for each scope. On average, it reduces ASR by 16% relative to the strongest defense prompt, with the lowest over-refusal rate, and by 9% relative to fixed-policy DPO on an unseen scope.

</details>

### 29. SafeDream: Safety World Model for Proactive Early Jailbreak Detection in Multi-Turn Conversations

📄 [OpenReview](https://openreview.net/forum?id=0hmbvsqfKr)　📅 2026-10　🏷️ P2

**关键词**：`multi-turn jailbreak`、`early detection`、`world model`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：多轮越狱逐步侵蚀安全对齐（SOTA 上成功率>90%）——既有防御需改权重、逐轮独立评分、事后反应，无干预预算
- 🔬 **研究方法**：SafeDream：冻结 LLM 隐状态编码为紧凑安全态+学习跨轮动力学世界模型+CUSUM 累积弱证据+歧义时对比潜在脆弱性探测（检测提前量=可用干预预算）
- 📌 **结论**：权重保持的轻量模块在合规前多轮预警——路由强守卫/禁工具/升级人工皆可在事前行动

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-turn jailbreak attacks progressively erode LLM safety alignment across seemingly innocuous turns, achieving success rates exceeding 90% against state-of-the-art models. Existing alignment-based and guardrail defenses share three limitations: they require costly weight modification, score each turn independently without modeling cumulative safety erosion, and react only after harmful content appears – leaving no budget for the realistic interventions (routing to a stronger but slower guard, disabling tools, or escalating to human review) that must act before compliance. We formulate proactive early jailbreak detection and introduce detection lead, which measures how many turns before compliance an attack is flagged and which we frame as usable intervention budget rather than a mere timestamp. We propose SafeDream, a lightweight, weight-preserving safety module for deployments with hidden-state access. SafeDream (1) encodes a frozen LLM's hidden states into a compact safety state and learns a world model of its cross-turn dynamics, (2) applies CUSUM to accumulate weak per-turn risk into reliable sequential evidence, and (3) when evidence is ambiguous, performs contrastive latent vulnerability probing – rolling out attack-like and benign-like latent continuations and using their gap as a local vulnerability margin, not a prediction of future text. Across three multi-turn benchmarks (XGuard-Train, SafeDialBench, SafeMTData) and 8 baselines, SafeDream achieves the best timeliness (1.06–1.20 turns of lead) with competitive false-positive rates and the highest detection quality, even surpassing weight-modifying defenses. Gains persist across three backbone families after lightweight recalibration, under GPT-free and blind human-defined compliance labels, and on natural benign conversations.

</details>

### 30. Competing Explanations, Persistent Rules: Grounded Defense against Misleading Charts in Executing Web Agents

📄 [OpenReview](https://openreview.net/forum?id=3W7P9cyihW)　📅 2026-10　🏷️ P2

**关键词**：`misleading visualization`、`web agent defense`、`persistent rules`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：误导图表诱导 web agent 错误动作——修正解读还不够须让修正引导后续动作
- 🔬 **研究方法**：CEPR：竞争解释对视觉证据验证+把判定存入持久规则态指导后续行动
- 📌 **结论**：八模型正确执行 +14.6pp 且误导导向动作减少、验证后决策跨交互保持——从更好答案到更可靠动作的防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Web agents use charts as evidence to guide actions, yet Misleading Visualizations can induce incorrect actions even when agents read charts accurately. Defending against this risk not only requires correcting the interpretation alone, but also ensuring that the correction guides later actions, leaving a gap between chart interpretation and agent execution. To bridge this gap, we introduce CEPR (Competing Explanations with Persistent Rules) , which verifies competing chart explanations against visual evidence and preserves their assessments in persistent rule state to guide subsequent actions. Experiments across eight models show that CEPR improves correct execution while reducing misleading-directed actions, with mean correct-submission gains of 14.6 percentage points over the baselines. Trajectory analysis further shows that correct post-verification decisions are largely preserved through subsequent interaction. CEPR advances misleading-visualization defense from better answers to more reliable actions, carrying verified chart interpretations into subsequent agent decisions and execution.

</details>

### 31. SEAL: Sealed Queries for Local Sanitization against Indirect Prompt Injection

📄 [OpenReview](https://openreview.net/forum?id=3r81nPKvq6)　📅 2026-10　🏷️ P2

**关键词**：`indirect prompt injection`、`local sanitization`、`soft prompt`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：本地 agent 面临工具输出注入——需在有限推理预算下抑攻保证据
- 🔬 **研究方法**：SEAL：离线学习软提示与评分读出（可信初始上下文构造评分查询、不跨上下文归一化）+保持正则鼓励有用证据局部删除
- 📌 **结论**：AgentDojo ASR 34.6%→0.1%、Joint 51.4%→77.5% 且防御 token 约 PISanitizer 的 1/127——冻结任务模型的本地消毒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Indirect prompt injection threatens local LLM agents through untrusted
tool outputs, motivating defenses that suppress attacks while preserving
task evidence under limited inference budgets. We introduce SEAL, which
learns a soft prompt and scoring readout offline to sanitize tool outputs
using a frozen task model. SEAL constructs scoring queries from trusted
initial context and the learned prompt, keeping the reference independent
of inspected tool text. It scores tokens without normalization across
context tokens and uses preservation regularization to encourage retention
of useful evidence during localized deletion. This design requires neither
defense-generated tokens nor a separate verifier model. Across
AgentDojo and AgentDyn, SEAL suppresses attacks while improving task
completion under attack. Specifically, on AgentDojo, SEAL reduces attack
success from 34.6% to 0.1% and increases Joint—task completion without
attack success—from 51.4% to 77.5%, while using approximately
127× fewer defense-related tokens than PISanitizer, a state-of-the-art
prompt injection defense. Replication on a second backbone with the same
training recipe supports applicability across model families.

</details>

### 32. ConformalGuard: Conformal Risk Control for Safeguarding LLM-Based Multi-Agent Systems

📄 [OpenReview](https://openreview.net/forum?id=8EjiMo1ISU)　📅 2026-10　🏷️ P2

**关键词**：`multi-agent`、`risk-controlled isolation`、`conformal`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：MAS 防御把异常分转隔离决策不计误隔离风险——良性异常 agent 被误伤且早期弱信号难以及时隔离
- 🔬 **研究方法**：ConformalGuard：行为偏差+通信图构造 agent 级异常证据并校准区分统计异常与恶意+跨轮累积证据+总体误隔离风险控制
- 📌 **结论**：强证据早隔离、弱证据需持续——干预保持统计可靠（受控风险的多 agent 隔离）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model-based multi-agent systems rely on inter-agent communication, which can propagate malicious information across agents and compromise system behavior. Existing defenses commonly translate anomaly scores into isolation decisions through predefined criteria, without explicitly accounting for the risk of isolating benign agents. This leads to two challenges: (i) benign but anomalous agents may be falsely isolated; and (ii) agents may exhibit weak or ambiguous anomalous signals in early interactions, making timely isolation difficult. To address these challenges, we propose ConformalGuard, a risk-controlled isolation framework that decouples anomaly assessment from intervention. ConformalGuard first constructs agent-level anomaly evidence from behavioral deviations and communication graphs, and then calibrates it to distinguish statistically unusual behavior from malicious behavior. It then accumulates calibrated evidence across interaction rounds, allowing strong evidence to trigger early isolation while requiring persistent evidence for weaker deviations. Finally, ConformalGuard controls the overall false-isolation risk of these decisions, ensuring that intervention remains statistically reliable throughout the interaction. Extensive experiments demonstrate effective malicious-agent isolation with controlled false-isolation risk.

</details>

### 33. DualTrend: Combining Trend and Deviation Evidence for Training-Free Adversarial Suffix Detection

📄 [OpenReview](https://openreview.net/forum?id=AlWmEN7hXC)　📅 2026-10　🏷️ P2

**关键词**：`adversarial suffix`、`training-free detection`、`sequential statistics`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：优化型对抗后缀流畅可绕困惑度过滤器；序贯统计检测器又会被普通内容转移触发且阈值难迁移
- 🔬 **研究方法**：DualTrend：冻结 LLM 上持续时间趋势+互补偏差证据组合的免训练检测器
- 📌 **结论**：在检测权衡（漏检 vs 误伤合法用户）上取得改进——后缀攻击的免训练序贯检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak attacks undermine the safety alignment of large language models (LLMs) by inducing responses to requests they are intended to refuse. As LLMs are increasingly deployed in user-facing applications, detecting these attacks is essential to limiting harmful outputs while preserving access for legitimate users. Optimization-based adversarial suffixes make this task particularly challenging because they can remain fluent and evade perplexity-based filters. Sequential statistical detectors capture changes missed by aggregate scores, but ordinary content transitions can also trigger strong anomaly evidence, and source-calibrated thresholds may transfer poorly to new prompt distributions. To address this detection tradeoff, we introduce DualTrend, a training-free detector that combines persistent temporal trends with complementary deviation evidence from a frozen LLM. DualTrend tracks rank trends in token negative log likelihood (NLL) and predictive entropy, and supplements them with accumulated NLL deviations relative to the scoring prefix. It maps both components to empirical source-negative upper tails and fuses them through a fixed probability product, with references and thresholds frozen before target evaluation. Across two backbones and three adversarial suffix families, DualTrend achieves macro F1 of 0.7538 under nominal source-5% calibration. Compared with the persistent trend-only variant, it reduces the false-positive rate from 8.33% to 2.33% while retaining nearly unchanged recall (66.00% versus 65.83%). Code and evaluation materials are available at https://anonymous.4open.science/r/DualTrend-76FE/.

</details>

### 34. GUARD-SLM: Token Activation-Based Defense Against Jailbreak Attacks for Small Language Models

📄 [OpenReview](https://openreview.net/forum?id=AyluywZYav)　📅 2026-10　🏷️ P2

**关键词**：`SLM jailbreak defense`、`layer selection`、`recheck`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：小模型边缘部署——越狱抵抗/良性保留/推理成本三衡困难
- 🔬 **研究方法**：九攻击×11 SLM 实证+逐层激活分析定位模型特定分离层+GUARD-SLM：选定层 token 激活分类器+查询意图与响应倾向选择性复查
- 📌 **结论**：XSTest 良性误拒 LLaMA-2-7B 16.4%→1.6%、Qwen3.5-4B 12.4%→0.0% 而不安全召回不变——模型特定选层+复查的 SLM 防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Small Language Models (SLMs) offer competitive performance on specialized tasks with lower computational costs and latency than larger models, making them promising for edge deployment. However, balancing jailbreak resistance, benign-query preservation, and inference cost remains challenging. We present a systematic empirical study of nine jailbreak attack methods across 11 SLMs and 3 Large Language Models (LLMs), revealing substantial variation in vulnerability across models and attacks.
Layer-wise activation analysis identifies model-dependent separation between benign and malicious prompts, motivating a model-specific layer-selection procedure.
We introduce GUARD-SLM, an inference-time defense that combines a classifier over ast-token activations from the selected layer with selective rechecking of query intent and response tendency to recover falsely rejected benign requests.
We evaluate detection on five models and benign-query rechecking on two models, and test two adaptive attacks. On XSTest, rechecking reduces benign false-positive rates from 16.4% to 1.6% for LLaMA-2-7B-Chat and from 12.4% to 0.0% for Qwen3.5-4B, while unsafe-query recall remains unchanged in these evaluations.
These findings support model-specific layer selection
and selective rechecking to reduce benign false
rejection in SLM jailbreak defenses.

</details>

### 35. Predictive Representation Alignment Improves Robustness to Unseen Jailbreaks

📄 [OpenReview](https://openreview.net/forum?id=BNBpdqHDbE)　📅 2026-10　🏷️ P2

**关键词**：`unseen jailbreaks`、`representation alignment`、`JEPA`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：越狱保持有害请求只变表层形式——绕过在已知攻击上训练的防御
- 🔬 **研究方法**：PRA：受 JEPA 启发训练对抗隐状态预测对应干净请求表示（72 简单提示变换训练→21 未见越狱法评测）+与 CC++ 风格探针组合
- 📌 **结论**：四模型加入安全训练目标即提升鲁棒；Llama-3-8B 大幅降 ASR 且鲁棒-过拒权衡更优、组合模型+护栏进一步降——表示对齐同时强化内部防御与外部监控

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak attacks can preserve a harmful request while changing its surface form, allowing them to bypass defenses trained on known attacks. Existing defenses either modify the model through safety fine-tuning or use external guardrails, such as activation probes, rarely optimizing the model to improve both its own robustness and the effectiveness of these guardrails. We introduce Predictive Representation Alignment (PRA), an objective inspired by Joint-Embedding Predictive Architectures (JEPA) that trains adversarial hidden states to predict the representation of the corresponding clean request. We train on 72 simple prompt transformations and evaluate on 21 unseen jailbreak methods. Across four models of different sizes, PRA improves robustness when added to safety training objectives. On Llama-3-8B, it greatly reduces attack success, achieving a better robustness–over-refusal trade-off than existing methods. PRA also improves the detection of unseen attacks by probes in the style of Constitutional Classifiers++ (CC++), reducing attack success against the combined model and guardrails. Our results show that representation alignment can strengthen both internal safety defenses and external monitoring.

</details>

### 36. SafeRole: Reconciling Safety and Fidelity in Role-Playing LLMs

📄 [OpenReview](https://openreview.net/forum?id=CzONdXw0DM)　📅 2026-10　🏷️ P2

**关键词**：`role-play safety`、`preference data`、`DPO`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：角色扮演削弱安全、安全机制又破坏角色——双向冲突未同时处理
- 🔬 **研究方法**：7 模型双向冲突实证+SafeRole 同时约束安全边界与角色一致性的偏好数据 DPO 训练
- 📌 **结论**：高安全合规且不牺牲扮演质量、泛化到未见人设——安全-保真双目标对齐

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Role-playing can negatively impact LLM safety, as character fidelity may conflict with safety guardrails.
Through experiments with 7 LLMs of diverse sizes and providers, we show that this conflict runs in both directions: just as role-playing can undermine safety, safety mechanisms can degrade role-play, as models break character and respond with generic refusals.
We construct SafeRole, a preference dataset that simultaneously enforces safety boundaries and character consistency, and use it to train models via Direct Preference Optimization (DPO).
Trained models achieve high safety compliance without sacrificing role-play quality, with benefits that generalize to unseen personas.
We release SafeRole and trained models, along with our training and evaluation code to support further study of the conflict between safety and role-play fidelity.

</details>

### 37. Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks

📄 [OpenReview](https://openreview.net/forum?id=J6rXyHpq41)　📅 2026-10　🏷️ P2

**关键词**：`multi-turn jailbreak`、`intention inference`、`defense`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：多轮越狱逐步隐藏恶意意图操纵上下文——比单轮更难防
- 🔬 **研究方法**：BIID：前向请求意图推断+后向响应回顾双向意图推理揭露隐蔽风险，四 LLM 九攻击 JailbreakBench+MHJ
- 📌 **结论**：最低平均 ASR 且跨策略稳健、AlpacaEval/XSTest 上安全-效用-过拒平衡——双向意图推断防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-turn jailbreak attacks pose greater challenges to LLM safety than single-turn attacks by progressively concealing malicious intent and manipulating conversational context to bypass safety safeguards.
To address this challenge, we propose Bidirectional Intention Inference Defense (BIID), which combines forward request-based intention inference with backward response-based retrospection to uncover concealed risks.
We evaluate BIID against 4 representative defenses and a no-defense baseline across 4 LLMs and 9 attacks on JailbreakBench, with further tests on MHJ. 
Results show that BIID achieves the lowest average Attack Success Rate (ASR) with consistent robustness across attack strategies, while maintaining a favorable balance between safety, utility, and over-refusal on AlpacaEval and XSTest.

</details>

### 38. Who’s the Impostor in Your Prompt? Spot-Cleaning Adversarial Content to Defend LLM Reasoning

📄 [OpenReview](https://openreview.net/forum?id=JTsFRfkW98)　📅 2026-10　🏷️ P2

**关键词**：`prompt cleaning`、`impostor detection`、`reasoning attack`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：提示内植入对抗内容把推理引向目标答案——既有防御找攻击签名或变换全提示伤任务内容
- 🔬 **研究方法**：SpotClean：按对答案的影响排序句子，仅当移除后重执行确认其为'impostor'（非任务却引导答案）才删——按影响排序+再执行确认
- 📌 **结论**：四攻击三模型三基准最佳安全-效用权衡、干净精度损失比最强基线少 4-5 倍，对 MirageBackdoor 最有效——内容级定点清除防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern language models reason through multi-step problems, but this ability opens a new attack surface:an attacker can plant adversarial content in the user prompt that steers the reasoning toward a target answer. These attacks take many forms, yet existing defenses either look for attack-specific signatures or transform the entire prompt, altering task-relevant content. Our key intuition is that, whatever their form, the attacks must act through content in the prompt. Building on the intuition, we introduce *SpotClean*, a defense that removes only such content, which we call an *impostor*: text in the prompt that is not part of the task yet steers the model's answer. To find impostors, *SpotClean* ranks prompt sentences by their influence on the answer. Because task-critical sentences are influential too,
it removes a top-ranked sentence only if re-executing the model without it confirms that the sentence is an impostor, and otherwise leaves the prompt untouched. Across four attacks, three models, and three reasoning benchmarks, *SpotClean* achieves the best security-utility trade-off among the evaluated defenses. It reduces attack success comparably to the strongest baselines while losing 4-5x less clean accuracy. *SpotClean* is particularly effective against MirageBackdoor, the most advanced attack, whose reasoning appears valid.

</details>

### 39. DARS: Decoupled Asymmetry-Aware Representation Safeguard for Vision-Language Model Jailbreak Defense

📄 [OpenReview](https://openreview.net/forum?id=K5KTXWzlEy)　📅 2026-10　🏷️ P2

**关键词**：`VLM jailbreak defense`、`modality asymmetry`、`training-free`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：单潜伏安全方向联合检测与生成——与 VLM 输入输出模态不对称冲突（检测注入视觉噪声伤文本生成）
- 🔬 **研究方法**：DARS：解耦双向量——联合模态探针跨全输入通道检恶意+纯语言拒答向量专司输出转向
- 📌 **结论**：五 VLM 上 SOTA、ASR 近零且保效用——模态不对称感知的训练无关防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Models (VLMs) remain vulnerable to multimodal jailbreaks, and recent training-free defenses often extract a single latent safety direction to jointly detect harmful inputs and steer generation. However, this coupling conflicts with VLMs' input-output modality asymmetry: joint vision-language inputs versus language-only generation. A single vector cannot span these incompatible spaces, forcing an unavoidable trade-off: optimizing for multimodal detection injects visual noise that degrades text generation, while restricting to pure text leaves the model blind to visual threats. To resolve this conflict, we propose Decoupled Asymmetry-aware Representation Safeguard (DARS), a training-free framework that tailors distinct vectors to their respective modality spaces. DARS pairs a joint-modality probe, which robustly detects malicious intent across all input channels, with a separate language-only refusal vector dedicated to output steering. Extensive evaluations across five VLMs demonstrate that DARS achieves state-of-the-art defense performance, reducing ASR to near zero while preserving model utility.

</details>

### 40. SafePrompt: Jailbreak Search Defense through Activation Signature

📄 [OpenReview](https://openreview.net/forum?id=Ll8wT0gfGf)　📅 2026-10　🏷️ P2

**关键词**：`jailbreak search defense`、`activation signature`、`energy readout`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：越狱搜索构造大量请求变体规避防护——这些候选在独立冻结模型的中间激活携带可检特征（含未成功者）
- 🔬 **研究方法**：SafePrompt：从 52 个种子目标扩展攻击学习能量读出+良性请求校准拒判，激活分离/参照覆盖/稀有通过候选累积三机制分析
- 📌 **结论**：PAIR 92/91%→14/17%、TAP 82/93%→19/27% 且良性误拒仅 2.53%（原生护栏 32.67/50.67%）——激活签名作为搜索类攻击的实用防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak search constructs many request variants to evade a language model's
safeguards. We show that these candidates carry a detectable signature in the
intermediate activations of a separate frozen model, including candidates
that elicit safe responses. SafePrompt learns its energy readout from attacks
expanded from 52 JailbreakBench seed goals and calibrates rejection on benign
requests. On 100 goals for each of two victims, it reduces PAIR success from
92/91% to 14/17% and TAP success from 82/93% to 19/27%, while rejecting
2.53% of 750 benign requests. Native HaloGuard and WildGuard reject 32.67%
and 50.67% on the same holdout. We trace search protection to activation
separation, reference coverage and the accumulation of rare passing candidates
across goals. Matched presentation changes shift both benign and harmful
energies, showing why calibration must reflect the deployment population.
In sequential search with binary gate feedback, the attacker succeeds on
seven of 30 goals at 90 queries per goal. These findings establish
activation-signature detection as a practical search defense and identify
the reference, utility and feedback choices that govern its transfer.

</details>

### 41. ConeSpace & ConeBand: Geometric Jailbreak Defense with Safety Pulses

📄 [OpenReview](https://openreview.net/forum?id=Lsy0U1EaZl)　📅 2026-10　🏷️ P2

**关键词**：`jailbreak defense`、`geometric selection`、`safety pulse`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：防御须止住有害回答而不扰普通请求——全量 steering 伤质量、事后修复需再生成
- 🔬 **研究方法**：ConeSpace：提示态与已知攻击族几何参照区比较选请求干预+ConeBand 生成起始的安全脉冲共享方向，冻结权重+Llama Guard 完成检查
- 📌 **结论**：2675 攻击候选 ASR 28.71%→1.91% 且保留 99.85% 普通回答——选择性几何干预省 424 次修复

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak defenses must stop harmful answers without disrupting ordinary requests. Steering every response can hurt answer quality, while repairing unsafe answers requires another generation. We introduce ConeSpace to select requests for intervention before generation. It compares prompt states with geometric reference regions for known attack families, using a threshold calibrated on ordinary requests. To reduce disruption from continuous steering, we introduce ConeBand, a brief safety pulse for selected requests. ConeBand builds a shared direction from contrast gradients of paired replies in which a safety instruction changes attack success to failure. The pulse acts only at the start of generation. The resulting opening and attention cache carry part of its effect into later tokens. Llama Guard checks complete answers, triggers repair of rejected ordinary answers, and replaces unapproved final answers with a refusal. On 2,675 source-separated Mistral-7B attacks, candidate attack success rates fall from 28.71% to 1.91% under Qwen assessment and from 37.53% to 5.46% under Gemma assessment. Released rates are 0.93% and 2.32%, respectively. ConeSpace retains 99.85% of ordinary answers and deliveries. Calibrated early intervention saves 424 repairs relative to strict routing at the same retention. These results support selective defense with frozen model weights.

</details>

### 42. Segment-Level Coherence for Robust Harmful Intent Probing in LLMs

📄 [OpenReview](https://openreview.net/forum?id=OAHuIU0XQZ)　📅 2026-10　🏷️ P2

**关键词**：`streaming probe`、`CBRN`、`harmful intent`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：流式探针依赖少数高分 token——良性上下文的敏感 CBRN 词触发误报
- 🔬 **研究方法**：段级一致性目标：要求多证据 token 一致支持预测而非孤立峰值+探针即插即用到对抗微调的字符密码攻击
- 📌 **结论**：1% FPR 下 TPR 相对提升 4.0-35.55%、密码化攻击上 AUROC>98.85%——CBRN 流式监控的鲁棒探测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly exposed to adaptive jailbreaking, particularly in high-stakes Chemical, Biological, Radiological, and Nuclear (CBRN) domains. Although streaming probes enable real-time monitoring, they still make systematic errors. We identify a core issue: existing methods often rely on a few high-scoring tokens, leading to false alarms when sensitive CBRN terms appear in benign contexts. To address this, we introduce a streaming probing objective that requires multiple evidence tokens to consistently support a prediction, rather than relying on isolated spikes. This encourages more robust detection based on aggregated signals instead of single-token cues. At a fixed 1% false-positive rate, our method improves the true-positive rate by 4.0%-35.55% relative to strong streaming baselines. We further observe substantial gains in AUROC, even when starting from near-saturated baseline performance (AUROC = 97.40%). We also show that probing Attention or MLP activations consistently outperforms residual-stream features. Finally, even when adversarial fine-tuning enables novel character-level ciphers, harmful intent remains detectable: probes developed for the base LLMs can be applied “plug-and-play” to these obfuscated attacks, achieving an AUROC of over 98.85%.

</details>

### 43. PolicyAlign: Direct Policy-Based Safety Alignment for Large Language Models

📄 [OpenReview](https://openreview.net/forum?id=PecNZYeI37)　📅 2026-10　🏷️ P2

**关键词**：`safety alignment`、`policy-based`、`self-distillation`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：现实安全需求常以自然语言政策出现而监督数据昂贵滞后——数据驱动对齐与快速演进政策错配
- 🔬 **研究方法**：PolicyAlign：按政策合成违规指令+策略内化的在策自蒸馏+策略敏感过滤选行为偏移最大指令
- 📌 **结论**：多模型一致提升安全且低过拒、泛化到医疗法律金融场景——从政策文本直接对齐

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment of large language models (LLMs) typically depends on high-quality supervision data, such as safe demonstrations or preference pairs. However, in real-world deployment, emerging safety requirements are often specified as natural-language policies, while corresponding supervision data may be costly, delayed, or unavailable. This creates a mismatch between rapidly evolving safety policies and conventional data-driven alignment methods. To address this, we propose PolicyAlign, a simple yet effective framework for directly aligning LLMs with safety policies. Given a safety policy, PolicyAlign first synthesizes policy-violating instructions and then performs on-policy self-distillation to internalize policy-guided behavior. To improve training stability and data efficiency, we further introduce Policy-Sensitive Filtering, which selects instructions where the policy induces the largest behavioral shift. Experiments across multiple models show that PolicyAlign consistently improves safety while maintaining low over-refusal and preserving general capabilities. PolicyAlign also generalizes to medical, legal, and financial safety scenarios, highlighting its potential as a scalable and maintainable approach to policy-based LLM safety alignment. The code is released at https://anonymous.4open.science/r/PolicyAlign-2F63.

</details>

### 44. A Self-Evolving Multi-Agent Framework Defense against LLM Jailbreak Attacks

📄 [OpenReview](https://openreview.net/forum?id=StR4MYtB3y)　📅 2026-10　🏷️ P2

**关键词**：`jailbreak defense`、`self-evolving`、`rule memory`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：越狱防御在猫鼠游戏中多为静态——安全行为部署时固定、不能积累防御经验
- 🔬 **研究方法**：持久跨交互规则记忆：攻击成功后抽象出方法级规则（结构包装而非有害主题）复用于未来输入，四模块协作纯外部记忆无参数更新
- 📌 **结论**：四黑盒越狱族上大幅降 ASR 且抗自适应组合包装攻击——方法级规则跨攻击族泛化的测试时进化防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) remain vulnerable to jailbreak attacks that exploit techniques such as role-playing, obfuscation, code transformation, and multi-step indirection to elicit harmful outputs. As jailbreak strategies keep emerging, defenses have proliferated in an ongoing cat-and-mouse game, yet most remain static: their safety behavior is fixed at deployment, so they cannot accumulate defensive experience or adapt to unseen strategies. We propose a self-evolving test-time defense built around a persistent, cross-interaction rule memory: when an attack succeeds, the framework abstracts that failure into a method-level rule capturing the structural attack wrapper rather than the harmful topic, and reuses it against future inputs. Because rules are method-level, one induced rule generalizes across an entire attack family, and the label space expands as novel wrappers appear. The mechanism operates entirely through external memory and prompting, with no parameter updates, and applies to both open-weight and black-box API models. We realize it as four cooperating modules, but the contribution is the memory-based adaptation mechanism, not the module decomposition. Across four black-box jailbreak families and multiple models, our method substantially reduces attack success rates while preserving benign utility, remains robust under an adaptive composite-wrapper attack, and does not increase over-refusal as the memory grows.

</details>

### 45. ProvRoPE: Encoding Application-Provided Provenance for Training-Free Prompt Injection Defense

📄 [OpenReview](https://openreview.net/forum?id=UCbxPFjK26)　📅 2026-10　🏷️ P2

**关键词**：`prompt injection`、`provenance`、`RoPE`、`training-free`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：应用其实知道每段输入的来源与预期权限——但序列化成 token 流后该信息丢失，指令-数据分离失效
- 🔬 **研究方法**：ProvRoPE：把应用提供的源角色编码进 RoPE 几何——低权限 token 共享位置偏移，保角色内相对几何、移跨角色相位，零参数修改零训练
- 📌 **结论**：六冻结检查点×八种直接/间接注入设置下有效防御——来源权限的几何编码（训练无关注入防御新路径）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM applications increasingly combine privileged instructions with untrusted content from retrieval, web pages, and tools, making reliable instruction–data separation a critical security requirement. Prompt injection exploits failures of this separation by causing untrusted text to be interpreted as control. Yet applications often know the provenance and intended authority of each input segment, even though this information is lost once inputs are serialized into a token sequence. We introduce ProvRoPE, a training-free method that encodes application-provided source roles into RoPE geometry. ProvRoPE assigns a shared positional offset to lower-privilege tokens, preserving within-role relative geometry while shifting cross-role phases, without modifying model parameters or requiring training. Across six frozen model checkpoints and eight direct and indirect prompt-injection settings, ProvRoPE achieves the lowest ASR in 43 of 48 model–benchmark combinations while retaining competitive clean-task utility relative to a trained role-encoding baseline. Gains persist across injection locations and nonzero offsets. Our results suggest that provenance-aware attention geometry provides a lightweight inference-time mechanism to strengthen agentic LLM application security.

</details>

### 46. From Static to Adaptive: Immunological Memory-based Jailbreak Detection for Large Language Models

📄 [OpenReview](https://openreview.net/forum?id=X8hW4OKEV9)　📅 2026-10　🏷️ P2

**关键词**：`jailbreak detection`、`immune memory`、`adaptive guard`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：静态检测器（固定安全数据集外模型或内部信号）难泛化到新出现的越狱攻击
- 🔬 **研究方法**：IMAG：安全状态存入持久可进化图记忆库——免疫检测检索已知攻击态+主动免疫模拟行为消解歧义+记忆更新纳入已验证攻击
- 📌 **结论**：五开源模型九攻击上平均准确率/F1 超最强基线 20.2/18.2pp——免疫记忆式自适应越狱检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) serve as the backbone of modern AI systems, yet they remain susceptible to adversarial jailbreak attacks. Current jailbreak detection methods either rely on external models trained on fixed safety datasets or leverage safety-related internal signals of the target model. However, these static methods struggle to generalize to newly emerging jailbreak attacks.
Drawing inspiration from the immunological memory, we introduce the Immune Memory Adaptive Guard (IMAG). By extracting safety states into a persistent, evolvable graph memory bank, the framework adaptively generalizes to emerging attacks. Specifically, the guard comprises three modules: (1) Immune Detection retrieves known attack states for efficient interception. (2) Active Immunity simulates model behavior to resolve ambiguous queries, and (3) Memory Updating incorporates validated attacks into the memory bank. This self-evolution architecture transforms static jailbreak detection into an adaptive one. Extensive experiments across five open-source LLMs and nine jailbreak attacks show that, averaged across the target models, our method improves accuracy and F1-score by 20.2 and 18.2 percentage points, respectively, over the strongest baseline for each model.

</details>

### 47. Re-START: Self-Taught Safety Alignment by Rectifying Flawed Reasoning

📄 [OpenReview](https://openreview.net/forum?id=Xjw8rR0zin)　📅 2026-10　🏷️ P2

**关键词**：`safety alignment`、`flawed reasoning`、`self-taught`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：推理即防御的方法假设安全推理起点正确——早期推理误入歧途则防御失败
- 🔬 **研究方法**：Re-START：缺陷推理前缀+文本提示诱发恢复轨迹→安全完成的自我教学迭代训练
- 📌 **结论**：有效抗越狱且在 agent 场景保持——从错误推理中自学的安全对齐

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Defending against jailbreak attacks is crucial for safely deploying Large Language Models (LLMs). Recent work uses reasoning as a defense by training models to analyze safety rules before answering. However, these methods usually assume that safety reasoning starts correctly; once early reasoning becomes misleading, the defense may fail. We propose Re-START (Rectifying Self-Taught Alignment of Reasoning Trajectories), a self-taught framework that improves safety under flawed reasoning steps. Re-START uses flawed reasoning prefixes and textual hints to elicit recovery trajectories that lead to safe completions. Iterative training on these trajectories strengthens robustness against jailbreak attacks. Experiments show that Re-START effectively defends against jailbreak attacks, outperforms baseline models, and remains effective in agentic scenarios. The code is available at: url{https://anonymous.4open.science/r/RESTART-7BE6}.

</details>

### 48. Triaging Threats to Specialized Guardrails

📄 [OpenReview](https://openreview.net/forum?id=bH1LlEfiW1)　📅 2026-10　🏷️ P2

**关键词**：`guardrail`、`threat triage`、`router-expert`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：安全风险跨异构威胁域而数据集覆盖碎片化——单体护栏存在任务干扰
- 🔬 **研究方法**：GuardZoo：32460 样本 15 不安全类统一人工标注基准+RouteGuard 路由器-专家框架分流到威胁专属专家护栏
- 📌 **结论**：不同威胁域需不同决策边界难以压缩进单模型——分诊式护栏提升细粒度检测与 OOD 泛化并支持模块化扩展

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Building robust safety guardrails is essential for deploying Large Language Models across diverse real-world applications. However, this goal remains challenging because safety risks span heterogeneous threat domains, while existing datasets cover only fragmented risk subsets and rely on inconsistent taxonomies. Consequently, it remains unclear whether current guardrails can generalize beyond narrow evaluation settings. To better understand the robustness of guardrail models, we first introduce GuardZoo, a unified human-annotated benchmark with 32,460 samples covering 15 distinct unsafe categories. Evaluation on GuardZoo reveals that monolithic guardrails suffer from task interference: different threat domains require distinct decision boundaries that are difficult to compress into a single model. We therefore propose RouteGuard, a router-expert framework that triages each conversation to specialized expert guardrails for threat-specific detection. Experiments show that RouteGuard improves fine-grained threat detection over strong guardrail baselines, generalizes better under out-of-domain evaluation, and supports flexible modular expansion to emerging threats.

</details>

### 49. Orthogonal Subspace Constraints: Defending Large Language Models Against Jailbreak Attacks

📄 [OpenReview](https://openreview.net/forum?id=cAxfAxwCjw)　📅 2026-10　🏷️ P2

**关键词**：`jailbreak defense`、`orthogonal subspace`、`hidden-state optimization`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：动态防御依赖辅助 LLM（贵）或轻量网络（对未知攻击失效）
- 🔬 **研究方法**：OSC：隐状态多目标约束优化——安全锚缓解移除越狱成分时的漂移+正交子空间约束把修改限制在通用能力子空间正交补
- 📌 **结论**：四 LLM 八攻击平均 ASR 60.5%→4.3%、良性通过 93.7% 且 MMLU/GSM8K 无损——保持推理能力的隐状态动态防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As jailbreak attacks against large language models (LLMs) continue to evolve, defense methods have attracted increasing attention. However, existing dynamic defenses based on prompt optimization typically rely on either auxiliary LLMs or specially trained lightweight 
neural networks. The former incur substantial computational overhead, whereas the latter may become ineffective for unknown jailbreak attacks. To address these limitations, we propose Orthogonal Subspace Constraint (OSC), a dynamic defense approach based on hidden-state optimization, which reformulates dynamic jailbreak defense as a multi-objective constrained optimization problem over hidden states. We introduce a safety anchor to mitigate the hidden-state drift when removing jailbreak-related components from query hidden states. Moreover, we impose the orthogonal subspace constraint that confines hidden-state modifications to the orthogonal complement of the general-capability subspace, thereby preserving the model’s intrinsic reasoning capabilities. Extensive experiments on four representative LLMs against eight advanced jailbreak attacks demonstrate that OSC substantially outperforms existing state-of-the-art defenses. Specifically, OSC reduces the average attack success rate from 60.5% to 4.3% while maintaining a benign pass rate of 93.7%. Moreover, OSC incurs negligible utility degradation on the MMLU and GSM8K benchmarks, achieving an effective balance between model safety and general-purpose capabilities.

</details>

### 50. Hidden-Selective: A Selective Safety Defense Based on Joint Image–Text Representations

📄 [OpenReview](https://openreview.net/forum?id=cYNqhcgWc5)　📅 2026-10　🏷️ P2

**关键词**：`selective defense`、`multimodal hidden states`、`risk router`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：VLM 安全适配全量施加会压制合法请求——选择性防护需基于视觉上下文与用户意图的决策
- 🔬 **研究方法**：Hidden-Selective：轻量风险路由器读双模态隐状态在基模型与安全适配版间选择完整响应路径（生成前、无在线输出判官）
- 📌 **结论**：四骨干八攻击族大幅安全增益且部分模型良性拒答反降——同预算对照证明选对输入本身（而非增加干预量）贡献增益

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models are vulnerable to harmful instructions expressed
through images, text, or their combination. Safety adaptation reduces
these failures, but applying it universally can also suppress useful
responses to legitimate requests. Selective protection therefore
requires a decision grounded in visual context and user intent.
We propose Hidden-Selective, a defense that
turns joint image–text hidden states into a calibrated choice between
a base model and its safety-adapted counterpart. A lightweight risk
router reads both modalities and selects a complete response path
before generation. Unlike text-only screening or post-generation
repair, this design uses multimodal context without an online output
judge. Experiments across four backbones and eight attack families
demonstrate substantial safety gains over the base models.
On some models, selective intervention also reduces benign refusals
while retaining most of the safety improvement from always-on adaptation.
Equal-budget
controls further show that selecting the right inputs, rather
than merely increasing intervention, contributes to these gains.

</details>

### 51. Calling the Bluff: Detecting Ever-Shifting Harmful Chat Dialogue via Ordered Reasoning Chain Regularization

📄 [OpenReview](https://openreview.net/forum?id=cpCrDBJVHG)　📅 2026-10　🏷️ P2

**关键词**：`harmful dialogue`、`ordered reasoning chain`、`evolving harm`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：有害聊天对话随伤害类型与词汇规避持续演化——静态分类器系统性出错
- 🔬 **研究方法**：BRACE：有序推理链（主题→指标→严重度→类型）四级可微阶段+中间监督作结构正则+原型特征增强
- 📌 **结论**：主测试集伤害类型宏 F1 0.934/严重度 0.818，ORC 为最大贡献——演化有害对话的链式结构化检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Harmful chat dialogues continually evolve through shifts in harm type and lexical evasion. We introduce the Blended Reasoning-chain Augmented Classification Engine (BRACE), centered on an Ordered Reasoning Chain (ORC) that links topic, indicator, severity, and type predictions to interpret changing expressions in context. BRACE implements ORC as four differentiable stages—topic profiling, indicator detection, severity assessment, and type classification, in that order—with intermediate supervision. The chain serves as a structured regularizer blended with direct prediction heads, while prototype-based feature augmentation and feature path disentanglement support fine-grained classification without imposing a strict intermediate bottleneck. Its intermediate predictions also expose evidence for analyzing where harmful content is implicitly conveyed.
On the primary 9,000-example test set spanning four domains and five harm categories, BRACE achieves a harm-type macro F1 of 0.934 and a severity accuracy of 0.818 with RoBERTa-wwm-ext (mean over three seeds); using Qwen3-1.7B with LoRA increases harm-type macro F1 to 0.949. Ablation studies identify ORC as the largest contributor and confirm the complementary roles of the remaining components, particularly for distinguishing harm types in semantically ambiguous dialogues.
Disclaimer: This paper may contain content that is disturbing to some readers.

</details>

### 52. Noise Injection Systemically Degrades Large Language Model Safety Guardrails

📄 [OpenReview](https://openreview.net/forum?id=dsvLPYo5ZW)　📅 2026-10　🏷️ P2

**关键词**：`noise injection`、`guardrail robustness`、`white-box diagnostic`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：护栏对内部扰动的鲁棒性未知——前向过程内的非定向噪声是否破坏安全
- 🔬 **研究方法**：九开源指令配置解码块输入注零均值高斯+激活统计校准对照+噪声增强调优
- 📌 **结论**：8/9 架构噪声系统升高判官标记不安全输出至多 53.5pp（无需对抗优化）——白盒诊断视角的护栏脆弱性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety guardrails in large language models (LLMs) are critical for reducing harmful outputs, yet their robustness to internal perturbations remains poorly understood. We evaluate nine open-weight instruction-tuned configurations by injecting zero-mean Gaussian noise into decoder-block inputs at inference. Across eight of nine tested open-weight architectures, untargeted Gaussian noise inside the forward pass systematically degrades safety guardrails, increasing judge-labeled unsafe completions by up to 53.5 percentage points without requiring adversarial prompt optimization or gradient search. In the tested fine-tuning runs, SafeChain tuning leaves substantial unsafe output rates under noise, whereas noise-augmented tuning lowers rates at some shared scales but not under all tested perturbations. We also introduce activation-statistics-based calibration. We frame the intervention as a white-box diagnostic, not a black-box API jailbreak.

</details>

### 53. JAILJUDGE: A Comprehensive Jailbreak Judge Benchmark with Multi-Agent Enhanced Explanation Evaluation Framework

📄 [OpenReview](https://openreview.net/forum?id=e20Hgr2VnB)　📅 2026-10　🏷️ P2

**关键词**：`jailbreak judge`、`benchmark`、`multi-agent`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：越狱评估的判官任务本身缺基准——判定攻击是否成功的质量决定安全评测可信度
- 🔬 **研究方法**：JAILJUDGE：4.5k 人工标注 ID+6k 十语 OOD 有害提示-响应对+判官/投票/推理三专责多 agent 框架
- 📌 **结论**：ID +5.31%、OOD +4.83% 超基线并给出可解释理由与细粒度严重度——越狱判定任务基准化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring the safety of large language models (LLMs) requires accurate evaluation of jailbreak attacks, yet this aspect has received limited attention. To address this gap, we formalize the jailbreak judge task: given a user prompt and the corresponding LLM response, the judge determines whether the jailbreak attempt succeeds. To support this task, we build JAILJUDGE, an open-source, human-annotated dataset with over 4.5k labeled harmful prompt-response pairs for in-distribution (ID) evaluation and 6k multilingual pairs across ten languages for out-of-distribution (OOD) testing. We further propose a multi-agent framework that decomposes judgment into specialized roles for judging, voting, and inference, enabling mutual verification and structured reasoning aggregation. The framework provides interpretable justifications and fine-grained severity scores. Experiments show average gains of 5.31% on ID evaluation and 4.83% on OOD evaluation over state-of-the-art baselines. To promote reproducibility, we release both an instruction-tuned jailbreak judge dataset and model. Code and data are available at https://anonymous.4open.science/r/public_multiagents_judge-66CB

</details>

### 54. GMP: A Benchmark for Content Moderation under Co-occurring Violations and Dynamic Rules

📄 [OpenReview](https://openreview.net/forum?id=gPXi9X3rwz)　📅 2026-10　🏷️ P2

**关键词**：`content moderation`、`co-occurring violations`、`dynamic rules`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：审核基准假设违规互斥且规则静态——现实多重伤害共现、政策随上下文变化
- 🔬 **研究方法**：GMP 双任务基准：识别共现违规（单内容多伤害）+适应动态规则（零样本新政策可能与安全对齐冲突）
- 📌 **结论**：模型标高频违规漏长尾共现；规则改变时不更新判断尤其当审核指令背离通用安全规范——排行榜高分≠真实可靠

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Content moderation increasingly relies on large language models (LLMs), yet existing benchmarks assume mutually exclusive violations and static, universal rules, failing to reflect real-world scenarios where multiple harms co-occur and policies vary across contexts. To address this, we introduce the Generalized Moderation Policy (GMP) Benchmark, a dual-task benchmark designed to evaluate two critical dimensions of moderation generalization: (1) Identifying Co-occurring Violations, which tests whether models can detect all co-occurring harms within a single piece of content, and (2) Adapting to Dynamic Rules, which evaluates zero-shot reasoning under novel, context-specific policies that may conflict with a model’s safety-aligned behavior.
Evaluations of over 20 state-of-the-art LLMs via GMP reveal two systemic weaknesses: firstly, models tend to flag frequent violations but overlook long-tail co-occurring harms; secondly, models fail to update judgments in response to rule changes, especially when moderation instructions diverge from general safety norms. These findings demonstrate that high performance on existing leaderboards does not ensure real-world reliability. GMP therefore serves as a practical benchmark for the next generation of AI moderators.

</details>

### 55. SecInfer: Preventing Prompt Injection via Inference-time Scaling

📄 [OpenReview](https://openreview.net/forum?id=glCWItRP3r)　📅 2026-10　🏷️ P2

**关键词**：`prompt injection`、`inference-time scaling`、`defense`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：预防式防御依赖微调——对强攻击效果有限
- 🔬 **研究方法**：SecInfer：系统提示引导采样（多样系统提示探索推理路径多响应）+目标任务引导聚合（选最可能完成意图任务的响应）
- 📌 **结论**：推理时加算力缓解既有与自适应注入攻击并超 SOTA 防御——用能力换安全的测试时扩展防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prompt injection attacks pose a pervasive threat to the security of Large Language Models (LLMs). State-of-the-art prevention-based defenses typically rely on fine-tuning an LLM to enhance its security, but they achieve limited effectiveness against strong attacks. In this work, we propose SecInfer, a novel defense against prompt injection attacks built on inference-time scaling, an emerging paradigm that boosts LLM capability by allocating more compute resources for reasoning during inference. SecInfer consists of two key steps: system-prompt-guided sampling, which generates multiple responses for a given input by exploring diverse reasoning paths through a varied set of system prompts, and target-task-guided aggregation, which selects the response most likely to accomplish the intended task. Extensive experiments show that, by leveraging additional compute at inference, SecInfer effectively mitigates both existing and adaptive prompt injection attacks, outperforming state-of-the-art defenses as well as existing inference-time scaling approaches.

</details>

### 56. GuardJanus: Towards A Unified Safety and Security Reasoner for LLMs and Agents

📄 [OpenReview](https://openreview.net/forum?id=i7uyhWLCjF)　📅 2026-10　🏷️ P2

**关键词**：`guardrail`、`unified reasoner`、`policy transformation`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：现有护栏防御范围窄且不适配变化的安全需求——LLM 与 agent 需统一安全+安全防御
- 🔬 **研究方法**：GuardJanus 推理护栏：灵活把潜在攻击与风险类别变换为不同安全政策+RL 激励把安全判断映射到细粒度政策
- 📌 **结论**：分类与可解释性显著超现有护栏并给出统一安全与安全威胁的配方——政策条件化护栏的统一管道

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) and LLM agents share unprecedented access to sensitive data and tools, their safety vulnerabilities pose a critical risk to users, developers, and the impacted public. Though significant efforts have been made in developing safeguards for LLMs and agents, current defenses remain limited in defensive scope and fail to address the varying safety requirements. In this paper, we propose GuardJanus, a reasoning guardrail model to identify insecure or unsafe payloads for standalone LLMs and agentic workflows via a unified content moderation pipeline. Unlike existing safeguards, GuardJanus can flexibly transform potential attacks and risk categories into distinct safety policies. Trained on comprehensive safety benchmarks with varied taxonomies, GuardJanus incentivizes its reasoning capability to map its safety judgments to the fine-grained policies with reinforcement learning. Consequently, GuardJanus naturally exhibits powerful generalization ability and can be adapted to safeguard both LLMs and agents. We conduct extensive experiments to show that GuardJanus significantly improves existing safety guardrails’ capabilities for both classification and explainability. Moreover, we provide a detailed recipe to show how GuardJanus unifies both safety and security threats.

</details>

### 57. EVO-Guard: Self-Evolving GNN Guardrails for Adaptive Safety in GUI Agents

📄 [OpenReview](https://openreview.net/forum?id=ij5dnhAqeg)　📅 2026-10　🏷️ P2

**关键词**：`GUI agent`、`guardrail`、`self-evolving`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：GUI 环境动态性使静态规则护栏失效——隐私泄漏/安全漏洞/系统故障风险随自主性上升
- 🔬 **研究方法**：EVO-Guard：交互轨迹建为结构图+GNN 记忆预测执行风险与被违反规则+仲裁者推理时调控并从高危轨迹抽象新原子规则
- 📌 **结论**：MLA-Trust 上安全预测精度与泛化优于静态与非图基线——自进化图护栏

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of autonomous GUI agents has ushered in a new era of digital interaction. However, the increasing autonomy introduces critical safety risks, including privacy leakage, security vulnerabilities, and system failures. Compounding these challenges, the inherently dynamic nature of GUI environments renders traditional static rule-based guardrails ineffective. To address this gap, we propose a self-evolving graph-based guardrail framework EVO-Guard for GUI agents that models interaction trajectories as structured graphs and leverages a Graph Neural Network (GNN) memory to predict both execution risk and violated safety rules. An interpretable Arbiter integrates these predictions to regulate agent actions at inference time. Moreover, the framework continuously abstracts new atomic rules from high-risk trajectories, enabling adaptive safety reasoning without manual reprogramming. Experiments on the benchmark MLA-Trust show improved safety prediction accuracy and generalization over static and non-graph-based baselines.

</details>

### 58. Where is the Safety Signal? Modality-Aware Depth Calibration for Jailbreak Detection

📄 [OpenReview](https://openreview.net/forum?id=klOIhknsNm)　📅 2026-10　🏷️ P2

**关键词**：`jailbreak detection`、`layer selection`、`modality`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：内部安全监控须定位区分层——同一请求以文本或渲染图像呈现时最优层深不同（深度错位）
- 🔬 **研究方法**：MALS 模态感知层搜索：按输入格式选信息层窗+层上分数学线性检测器+独立安全请求校准阈值
- 📌 **结论**：六模型十设置平均精度 82.08%→83.95%、检出 43.90%→47.47% 且投影仅 6.92ms——固定特征预算下的深度校准

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Internal safety monitors must locate layers that distinguish harmful from benign requests. We study how this choice changes when identical requests are presented as text or rendered images. Paired profiles reveal carrier-dependent changes in class separation across depth, which we call depth misalignment. Modality-Aware Layer Search (MALS) selects informative layer windows for each input format, learns linear detectors over their scores, and calibrates thresholds on independent safe requests. Across six models and ten FigStep/XSTest settings, MALS raises average precision from 82.08% to 83.95% over a terminal-window detector with the same feature budget. Harmful-request detection rises from 43.90% to 47.47% at similar false-positive rates. All-layer scalar scoring reaches 85.89% average precision. On Qwen2.5-3B, projecting selected layers from resident hidden states takes 6.92ms versus 30.41ms for all layers. These results show that selecting readout depth improves detection under a fixed feature budget.

</details>

### 59. SafeReview: Defending LLM-based Review Systems Against Adversarial Hidden Prompts

📄 [OpenReview](https://openreview.net/forum?id=mBCrODYjvM)　📅 2026-10　🏷️ P2

**关键词**：`peer review security`、`adversarial hidden prompts`、`co-evolutionary training`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：LLM 进入学术评审——投稿中埋藏的对抗提示操纵评审结果威胁学术诚信
- 🔬 **研究方法**：SafeReview：生成器-防御者联合对抗训练——生成器产更强注入提示、防御者偏好训练保清洁与受攻下评审一致性
- 📌 **结论**：抗自适应注入、攻击下保论文排序且跨攻击者架构泛化——LLM 评审系统的协同进化防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) are increasingly integrated into academic peer review, their vulnerability to adversarial hidden prompts—adversarial instructions embedded in submissions to manipulate outcomes—poses a critical threat to scholarly integrity. We propose SafeReview, a co-evolutionary adversarial training framework for defending LLM-based peer review systems against such attacks. SafeReview jointly trains a Generator model to create sophisticated attack prompts and a Defender model to preserve review integrity under adversarial manipulation. The Generator is optimized to produce increasingly effective prompt injections, while the Defender is strengthened through preference-based training to maintain consistent reviews between clean and attacked submissions. Experimental results show that SafeReview improves robustness against adaptive prompt injection attacks, better preserves paper ranking under attack, and generalizes across attacker architectures compared with static defenses. These results demonstrate the potential of co-evolutionary training as a foundation for securing LLM-assisted peer review.

</details>

### 60. Reducing the Pretraining Modality Gap for Safer Vision-Language Models

📄 [OpenReview](https://openreview.net/forum?id=np3Oxt7Bjm)　📅 2026-10　🏷️ P2

**关键词**：`modality gap`、`VLM safety`、`pretraining regularizer`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：安全对齐 LLM 加视觉后安全大降（空白图也可触发）——模态鸿沟可能是肇因
- 🔬 **研究方法**：九开源 LVLM 模态差距-不安全行为相关性+多模态预训练加宽鸿沟证据+受控干预与正则强度敏感分析+ReGAP 轻量预训练正则
- 📌 **结论**：强相关且预训练加宽的鸿沟微调后大体持续；ReGAP 无安全数据/架构改动/推理开销（预训练 +5% 成本）——HADES Toxic 降 18.3pp——模态鸿沟的因果贡献与低成本缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Vision-Language Models (LVLMs) can suffer substantial safety degradation when vision is added to an otherwise safety-aligned Large Language Model (LLM): even blank or irrelevant images can trigger harmful responses. Existing defenses often require safety data, incur overhead, or compromise utility. We investigate the modality gap between visual and textual representations as a potential contributor to this degradation. Across nine open-weight LVLMs, we find strong correlations between modality gap and unsafe behavior, including additional unsafe behavior relative to each model’s text-only backbone. We also show that multimodal pretraining widens the gap, which largely persists after fine-tuning. Controlled interventions and regularization-strength sensitivity analysis further support a contributory role of modality gap in safety degradation. Motivated by these findings, we propose ReGAP, a lightweight pretraining regularizer that reduces the gap while preserving utility. ReGAP requires no safety data or architectural changes, adds only 5% to pretraining cost, and incurs no inference overhead. It complements existing defenses, reducing unsafe rates by up to 18.3 percentage points (pp) on HADES Toxic and 10.7 pp on average across seven safety evaluation settings.

</details>

### 61. CaseCritic: Training Small Safety Guards to Critique Retrieved Policy Cases

📄 [OpenReview](https://openreview.net/forum?id=oagHIVnctV)　📅 2026-10　🏷️ P2

**关键词**：`safety guard`、`retrieval-augmented`、`GRPO`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：检索增强小护栏照搬检索案例标签而非检查其理由是否适用——相似案例反而降低判断
- 🔬 **研究方法**：CaseCritic 两阶段：蒸馏五动作批评轨迹+GRPO 正确性门控奖励（仅正确判决给案例使用记分）
- 📌 **结论**：让五个基线降分的同批案例反而提升 0.6B 护栏整体表现——把错误源变成判断证据的小护栏

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Small safety guards are widely deployed as prompt-level filters before large language models (LLMs). To absorb new policies without retraining, retrieval-augmented designs let these guards read labeled policy cases from an editable case bank at inference. However, naïve retrieval often degrades small guards, as they rely on similar cases without checking whether the reasons behind their safety labels apply to the current query. We present CaseCritic, a two-stage framework that trains small guards to weigh each retrieved case rather than copy its label. Stage 1 distills a five-action critique trace, and Stage 2 refines it with GRPO under a correctness-gated reward that credits case use only for correct verdicts. We evaluate the 0.6B CaseCritic guard against six native guards on 17 safety benchmarks. The same cases that lower five baselines' scores improve CaseCritic overall, turning a source of errors into evidence for judgments. With retrieval, CaseCritic achieves the highest average benchmark performance among the evaluated guards. Its verdict-only variant also avoids retrieval losses on average and outperforms the best verdict-only guard on the same cases at similar latency.

</details>

### 62. SAEgis: Sparse Autoencoders as Plug-and-Play Firewalls for Adversarial Attack Detection in VLMs

📄 [OpenReview](https://openreview.net/forum?id=pQJhWhhrn0)　📅 2026-10　🏷️ P2

**关键词**：`defense`、`SAE`、`adversarial detection`、`VLM`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：VLM 对对抗扰动高度脆弱且安全关注不足——需要轻量即插即用的攻击检测
- 🔬 **研究方法**：SAEgis：在预训练 VLM 内插入 SAE 模块以标准重构目标训练，稀疏潜特征天然捕获攻击信号，多层信号组合
- 📌 **结论**：域内/跨域/跨攻击设置强于基线且跨域泛化提升最大——首个 SAE 即插即用攻击检测（可解释特征的安全用途）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models (VLMs) have advanced rapidly and are increasingly deployed in real-world applications, especially with the rise of agent-based systems. However, their safety has received relatively limited attention. Even the latest proprietary and open-weight VLMs remain highly vulnerable to adversarial attacks, leaving downstream applications exposed to significant risks. In this work, we propose a novel and lightweight adversarial attack detection framework based on sparse autoencoders (SAEs), termed SAEgis. By inserting an SAE module into a pretrained VLM and training it with standard reconstruction objectives, we find that the learned sparse latent features naturally capture attack-relevant signals. These features enable reliable classification of whether an input image has been adversarially perturbed, even for previously unseen samples. Extensive experiments show that SAEgis achieves strong performance across in-domain, cross-domain, and cross-attack settings, with particularly large improvements in cross-domain generalization compared to existing baselines. In addition, combining signals from multiple layers further improves robustness and stability. To the best of our knowledge, this is the first work to explore SAE as a plug-and-play mechanism for adversarial attack detection in VLMs. Our method requires no additional adversarial training, introduces minimal overhead, and provides a practical approach for improving the safety of real-world VLM systems.

</details>

### 63. Think-Reflect-Revise: A Policy-Guided Reflective Framework for Safety Alignment in Large Vision Language Models

📄 [OpenReview](https://openreview.net/forum?id=rWLgERigiM)　📅 2026-10　🏷️ P2

**关键词**：`safety alignment`、`LVLM`、`self-reflection`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：单遍 think-then-answer 范式在隐式恶意意图躲过初检时，模型会在自身推理轨迹里生成显式有害内容——该违规信号被忽视
- 🔬 **研究方法**：TRR 三段框架：政策引导自反思检测并纠正自暴露的恶意内容+ReSafe 高质量数据集训练该能力
- 📌 **结论**：对复杂多模态越狱的鲁棒安全对齐——把'自己说过的话'变成监控面

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As multimodal reasoning enhances the capabilities of Large Visual Language Models (LVLMs), recent safety alignment efforts have shifted toward leveraging internal reasoning to discern potential risks before responding. However, the prevalent single-pass think-then-answer paradigm remains vulnerable to complex multimodal jailbreak attacks. Specifically, when implicit malicious intent evades initial detection, the model may inadvertently generate explicit harmful content within its own reasoning trace—a critical violation signal that currently goes overlooked. Motivated by this observation, we propose Think-Reflect-Revise (TRR), a novel safety alignment framework that empowers models to detect and correct self-revealed malicious content through policy-guided self-reflection. To cultivate this capability, we construct ReSafe, a high-quality dataset comprising 5,000 structured think-reflect-revise examples. The target model first undergoes supervised fine-tuning (SFT) to internalize this reflective paradigm, followed by reinforcement learning (RL) to further reinforce policy-consistent revisions. Extensive experiments demonstrate that TRR significantly improves model robustness against unsafe queries and jailbreak attacks, increasing the safe response rate of Qwen2.5VL-7B from 42.8% to 87.7% while preserving general task performance and avoiding over-refusal. Our code and dataset are available at: url{https://anonymous.4open.science/r/Think-Reflect-Revise-94D8}.

</details>

### 64. Latent Safety-State Dynamics for Multi-Turn Jailbreak Risk Modeling

📄 [OpenReview](https://openreview.net/forum?id=vONRzmVlz8)　📅 2026-10　🏷️ P2

**关键词**：`jailbreak`、`early warning`、`risk modeling`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：多轮越狱预警须在违规响应前预测且控良性误报——常规时序风险模型两类失败
- 🔬 **研究方法**：把预警形式化为归一化剩余事件距离预测+Safe Distance Saturation 为无事件轨迹提供有界监督，轻量循环模型+哈希文本特征
- 📌 **结论**：GRU 基线跨域 FPR 最低 68.4%——表征不是唯一问题，预测目标的重新定义才是（预警口径）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-turn jailbreak early warning requires predicting unsafe behavior before a policy-violating response occurs, while controlling false alarms on benign conversations under distribution shift. We investigate whether conventional temporal risk models meet these requirements and identify two distinct failure patterns. Recurrent sequence models can achieve high early-warning rates in some settings, yet exhibit severe false-positive calibration failures under cross-domain transfer: a GRU baseline has a minimum conversation-level false-positive rate (FPR) of 68.4% on Geometry → Synthetic → X-Guard. Conversely, the evaluated Cox and DeepSurv baselines report mean warning leads of 7.91 and 8.52 turns, respectively, on Synthetic → X-Guard, raising the question of whether event propensity adequately captures actionable warning timing. These findings motivate examining the prediction target, rather than temporal representation alone. We formulate early warning as prediction of normalized remaining event distance and introduce Safe Distance Saturation to provide bounded supervision for trajectories without an observed jailbreak. A lightweight recurrent model instantiated with hashed text features achieves a 3.5% early-warning rate at a 10% FPR budget on Geometry → Synthetic → X-Guard. However, its minimum FPR rises to 74.6% on Geometry → MTJAD → X-Guard, showing that reliable cross-domain warning remains unresolved. Our results highlight prediction-target design and calibration under distribution shift as central challenges in multi-turn jailbreak defense.

</details>

### 65. MOSAIC: Composable Safety Alignment with Modular Control Tokens

📄 [OpenReview](https://openreview.net/forum?id=vebOymR8bQ)　📅 2026-10　🏷️ P2

**关键词**：`safety alignment`、`control tokens`、`modular`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：安全对齐是参数内嵌的静态政策——难按用户/地区/应用适配；提示法又依赖弱自然语言指令
- 🔬 **研究方法**：MOSAIC：冻结骨干上优化可学习控制 token 编码每条安全约束，推理时灵活激活组合+两段平衡采样与双过拒缓解目标
- 📌 **结论**：现实基准上强防御且大降过拒保效用——可组合的安全对齐控制面

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment in large language models (LLMs) is often implemented as a static policy embedded in model parameters, making it difficult to adapt safety rules across users, regions, and applications. Existing approaches struggle to provide such conditional control: parameter-level alignment is inherently inflexible and difficult to adapt to new requirements, while prompt-based methods rely on weak natural language instructions. We propose MOSAIC, a modular framework for compositional safety alignment using learnable control tokens optimized over a frozen backbone model. Each safety constraint is encoded by a small set of tokens that can be flexibly activated and composed at inference time. To efficiently train compositional control tokens, we introduce two-stage balanced sampling and dual over-refusal mitigation objectives. Experiments on a newly constructed realistic benchmark show that MOSAIC achieves strong defense performance while substantially reducing over-refusal and preserving model utility.

</details>

### 66. Steering Both Ways: Bidirectional Conditional Safety Steering in a Learned Contrastive Safety Space

📄 [OpenReview](https://openreview.net/forum?id=wQY6POtck2)　📅 2026-10　🏷️ P2

**关键词**：`bidirectional steering`、`contrastive safety space`、`over-refusal`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：激活转向强拒答会让良性请求也被拒——需要有害被答时加强、良性被拒时减弱的双向控制
- 🔬 **研究方法**：D3-CSS：有害性与拒答标签学得共享对比空间提供拒答分与两转向方向，冻结模型前向内按请求有害性与当前拒答态条件化双向调节
- 📌 **结论**：七基准源上 Llama/Gemma 双向安全误差降 39.2%/41.1%——提升安全不必更多拒答合法请求

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) become more capable, preventing harmful assistance becomes increasingly important. Yet jailbreak attacks can bypass their safeguards and elicit unsafe responses. Activation steering offers a lightweight defense without retraining the LLM, but strengthening refusal can also make it reject harmless requests. We propose D3-CSS, a bidirectional steering method that reduces both unsafe responses and unnecessary refusals. It considers whether a request is harmful and whether the model is already refusing it, then strengthens refusal for harmful requests being answered and weakens it for benign requests being rejected. A shared contrastive space, learned from harmfulness and refusal labels, provides the refusal score and two steering directions. The method operates within the frozen model's existing forward pass. Across seven benchmark sources, D3-CSS reduces both harmful-response and over-refusal rates on Llama-3.1-8B and Gemma-2-9B. It outperforms seven baselines in bidirectional safety error (BSE), reducing BSE by 39.2% and 41.1% relative to the unsteered models, respectively. These results show that improving safety need not require refusing more legitimate requests.

</details>

### 67. MARS: Modality-Agnostic Robustness and Safety Adaptation for Vision-Language Models

📄 [OpenReview](https://openreview.net/forum?id=wkOvSJhwiR)　📅 2026-10　🏷️ P2

**关键词**：`VLM defense`、`modality-agnostic`、`soft prompt`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：多模态攻击面沿模态与攻击维度扩张——现有防御绑定特定模态或威胁且依赖攻击形态先验
- 🔬 **研究方法**：MARS：共享嵌入空间单一软提示近似跨模态及交互的攻击表示→攻击导向训练信号做轻量 VLM 适配（无需已知攻击样本）
- 📌 **结论**：LLaVA/Qwen-VL 上视觉扰动/文本越狱/跨模态越狱一致增强抵抗且保通用能力——模态无关的统一安全适配

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models (VLMs) achieve strong performance by jointly interpreting and reasoning over image and text inputs. However, their multimodal nature also expands the threat surface along both modality and attack dimensions: attacks can manipulate images, text, or their cross-modal interactions through distinct mechanisms, including adversarial perturbations and jailbreak prompts. Existing defenses are largely tailored to a specific modality or threat type and often rely on prior knowledge of attack form, limiting their ability to handle diverse multimodal threats. We therefore propose Modality-Agnostic Robustness and Safety Adaptation (MARS) to address the multimodal attack surface of VLMs. MARS optimizes a single soft prompt in the shared embedding space to approximate attack representations spanning individual modalities and their interactions. The resulting soft prompt provides attack-oriented training signals for lightweight VLM adaptation, improving robustness and safety without requiring known attack samples or predefined attack-generation algorithms. We evaluate MARS on LLaVA and Qwen-VL against representative visual adversarial perturbations, textual jailbreak prompts, and cross-modal jailbreak attacks. Experimental results show that MARS consistently improves resistance to both adversarial and jailbreak attacks by substantial margins while preserving the VLMs’ general multimodal capabilities.

</details>

### 68. RiskSteer: Joint Risk-Guided Steering during Language Model Reasoning

📄 [OpenReview](https://openreview.net/forum?id=wqYNN3lGcp)　📅 2026-10　🏷️ P2

**关键词**：`multi-risk steering`、`SAE latents`、`CVaR`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：既有转向跟单风险方向——降一险可留他险或恶化
- 🔬 **研究方法**：RiskSteer：冻结模式特定探针组成自适应联合风险目标+CVaR 对采样邻域最高风险候选+锚定罚限偏移，推理时转向 SAE 潜变量
- 📌 **结论**：Llama/Qwen 3.1/3 8B 上虚假/遗漏/挑战诱发谄媚三风险同降且共享集合上最低均险——多行为风险的联合潜干预

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reliable responses from large language models require avoiding several failure modes at once,including falsehoods, misleading omissions, and agreement with incorrect user beliefs. Existing steering methods typically follow a single risk direction or a combined classifier gradient at one activation, so reducing one risk can leave others unresolved or worsen them. We introduce RiskSteer, an inference-time method that composes frozen, mode-specific probes into an adaptive joint-risk objective and steers sparse autoencoder (SAE) latents during reasoning. The joint objective emphasizes failure modes with higher estimated risk, and a conditional value-at-risk (CVaR) objective over sampled neighboring latents targets the highest risk candidates, so that the steered state remains low-risk beyond a single point. An anchoring penalty limits deviation from the original representation. On Llama 3.1 8B Instruct and Qwen3 8B, RiskSteer improves falsehood, omission, and challenge-induced sycophancy outcomes relative to unsteered generation. On a shared set where each response is judged across all three risks, it attains the lowest average risk among five steering baselines and lowers each individual risk rate. These results suggest that latent intervention can reduce multiple behavioral risks together rather than trading one for another, without updating parameters.

</details>

### 69. AgentDrift: Detecting and Localizing Prompt Injection as Behavioral Drift in LLM Agent Trajectories

📄 [OpenReview](https://openreview.net/forum?id=xdFt8hGAOI)　📅 2026-10　🏷️ P2

**关键词**：`prompt injection`、`behavioral drift`、`step-level labels`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：agent 可能遭遇注入而不跟随、或短暂跟随后回归任务——二元安全判决无法揭示攻击从哪进入、腐蚀了哪些动作
- 🔬 **研究方法**：AgentDrift 基准：12,536 条合成工具调用轨迹 71,024 步全标注（良性/注入点/被劫持动作/失败注入+看似可疑的良性硬负例）+DriftNet 双头 Transformer 联合检测被劫持轨迹与逐步标注
- 📌 **结论**：以行为漂移视角把注入检测细化为可定位步骤问题——轨迹级注入取证基准

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

An LLM agent may encounter a prompt injection without following it, or follow it briefly before returning to its task. A binary safety verdict cannot reveal where the attack entered or which actions it corrupted. We study indirect prompt injection as behavioral drift and introduce AgentDrift, a benchmark of 12,536 synthetic tool-call trajectories across five domains, with labels for all 71,024 steps. The benchmark distinguishes benign steps, injection points, hijacked actions, and failed injections, and includes legitimate but suspicious-looking hard negatives. Labels are specified during generation, structurally validated, and manually audited on 1,200 trajectories. We also introduce DriftNet, a dual-head Transformer that combines frozen step embeddings with world-context features to jointly detect compromised trajectories and label each step, using fewer than two million trainable parameters. On the benchmark’s task-disjoint test set, DriftNet achieves 0.983 trajectory F1 and exactly localizes the injection point in 98.7% of attacked trajectories, with no false alarms on 218 resisted attacks. It detects 98.6% of partial hijacks and 93.2% of delayed executions, compared with 11.1% and 17.1% for a surface-feature baseline. These results support trajectory-based diagnosis that distinguishes attack exposure from behavioral compromise and identifies the actions affected.

</details>

### 70. SAFER: Probing Safety in Reward Models with Sparse Autoencoder

📄 [OpenReview](https://openreview.net/forum?id=yJxqybl03O)　📅 2026-10　🏷️ P2

**关键词**：`reward model`、`SAE`、`data poisoning`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：RLHF 核心的奖励模型基本黑箱——其安全相关决策机制未知
- 🔬 **研究方法**：SAFER：SAE 揭示奖励模型激活中可解释特征+按 chosen/rejected 激活差量化特征显著性+据此设计定向数据投毒与去噪
- 📌 **结论**：微量数据修改即可精确降级或增强安全对齐且不损通用聊天性能——奖励模型的解释、审计与精修（对齐供应链的可攻击面）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement learning from human feedback (RLHF) is a key paradigm for aligning large language models (LLMs) with human values, yet the reward models at its core remain largely opaque. In this work, we present Sparse Autoencoder For Enhanced Reward model (SAFER), a novel framework for interpreting and improving reward models through mechanistic analysis. Leveraging Sparse Autoencoders (SAEs), we uncover human-interpretable features in reward model activations, enabling insight into safety-relevant decision-making. We apply SAFER to safety-oriented preference datasets and quantify the salience of individual features by activation differences between chosen and rejected responses. Using these feature-level signals, we design targeted data poisoning and denoising strategies. Experiments show that SAFER can precisely degrade or enhance safety alignment with minimal data modification, without sacrificing general chat performance. Our approach contributes to interpreting, auditing and refining reward models in high-stakes LLM alignment tasks. Our code is available at https://anonymous.4open.science/r/SAFER-4866. This paper discusses topics related to reward model safety and may include discussions or examples that highlight potential risks or unsafe outcomes.

</details>

### 71. EffectSteer: Residual Steering-Effect Prediction for Adaptive Refusal Control

📄 [OpenReview](https://openreview.net/forum?id=z5cKo0Gqg5)　📅 2026-10　🏷️ P2

**关键词**：`refusal control`、`steering`、`adaptive strength`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：激活 steering 平衡越狱防御/过度拒绝/通用能力的强度选择困难
- 🔬 **研究方法**：EffectSteer：把 steering 行为效应建为模型自然拒答倾向的残差修正，SEP 效应预测器+状态条件强度连续自适应
- 📌 **结论**：平均防御 +15.68pp 同时过拒 -12.90pp——行为接地的双向拒答控制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Activation steering offers a lightweight approach to improving
large language model (LLM) safety, yet selecting appropriate
steering strengths remains challenging when balancing
jailbreak defense, over-refusal, and general capabilities.
To address this issue, we introduce EffectSteer, a behavior-grounded framework that unifies steering-effect prediction with continuous, input-adaptive steering-strength control. EffectSteer first models steering-induced behavioral changes
as residual corrections to the model's natural refusal tendency.
The resulting Steering Effect Predictor (SEP) improves
prediction accuracy over direct prediction from post-steering hidden states on most evaluated backbones. Building on SEP, we formulate inference-time steering-strength prediction as a nonlinear mapping of the full hidden state.
Guided by the frozen SEP, the State-Conditioned Steering Predictor (SSP) learns continuous, input-adaptive coefficients, leveraging richer internal information to enable effective, bidirectional
refusal control. Extensive experiments show that EffectSteer improves average
defense success by 15.68 pp and reduces average
over-refusal by 12.90 pp relative to previous
state-of-the-art methods for the respective metrics, while
largely preserving general capabilities.

</details>

## 三、安全对齐与机制可解释性

### 72. From Harmfulness to Refusal: Tracing the Causal Pathway of Safety Circuits in LLMs

📄 [OpenReview](https://openreview.net/forum?id=C6efXde7Yp)　📅 2026-10　🏷️ P1

**关键词**：`safety circuits`、`causal pathway`、`mechanistic`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：有害感知与拒答执行的因果连接不明——无法诊断越狱下安全电路在哪一环失效
- 🔬 **研究方法**：三阶段因果通路（感知→桥接→读出）+激活修补验证 token 位置介导+两模型越狱失败模式分期诊断
- 📌 **结论**：两模型感知阶段编码皆弱，Qwen 另有拒答方向转向偏置且直 接拒答方向转向也难纠——安全电路的分期失效诊断学

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Understanding the internal safety circuits of Large Language Models (LLMs) is crucial for ensuring the safety of general-purpose AI. However, the causal connection between harmfulness perception and refusal execution remains unclear, limiting the ability to diagnose where safety circuits fail under jailbreak prompts. In this paper, we address this gap by identifying a three-stage causal pathway in the safety circuit: Perception → Bridge → Readout. We further validate that this causal pathway is primarily mediated through a token position related to harmfulness representations using activation patching. Finally, we apply this framework to diagnose safety pathway failures under jailbreak prompts, revealing model-specific failure patterns at different stages of the pathway: both models show weak harmfulness encoding at the Perception stage, while Qwen additionally exhibits a Readout-stage accept-direction bias that persists under direct refusal-direction steering. Our findings provide a mechanistic understanding of how safety circuits operate in LLMs and suggest directions for improving robustness against jailbreak prompts.

</details>

### 73. FALBench: A Benchmark for Fake Alignment Evaluation and Behavioral Analysis

📄 [OpenReview](https://openreview.net/forum?id=OvlB6tmC6H)　📅 2026-10　🏷️ P1

**关键词**：`fake alignment`、`train-deploy gap`、`benchmark`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：伪对齐：训练模式跟随新目标而部署模式回归原策略——评测监督条件化顺从 vs 稳定目标跟随
- 🔬 **研究方法**：FALBench：角色扮演自动指令合成+MCTS 系统提示优化构建高保真基准（职业助理/极端顺从/商业营销/情感验证四冲突域）
- 📌 **结论**：29 个指令模型上伪对齐不能仅由推理能力解释、还取决于是否内化目标——训练-部署模式分离的欺骗性对齐评测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fake alignment occurs when large language models (LLMs) follow a new training objective in train mode but return toward their original response policy in deploy mode. Its evaluation tests whether post training yields stable objective following or supervision conditioned compliance. Existing benchmarks have two limitations. Helpful only evaluations rely on malicious datasets, yielding narrow instruction distributions, while alternative objectives may lack deployment motivations and real world fidelity. Manually written system prompts may fail to support evaluation setting inference, so results may reflect default responses rather than behavior conditioned on train and deploy modes. We introduce FALBench, a high fidelity benchmark combining role playing based automatic instruction synthesis with Monte Carlo tree search (MCTS) based system prompt optimization. The synthesis instantiates value conflicts across professional assistant, extreme compliance, commercial marketing, and emotional validation scenarios. Compared with the strongest baselines, FALBench improves instruction diversity by 18.91%, instruction fidelity by 11.81%, and NLI Entailment Rate for evaluation setting inference by 27.9% on average. We evaluate 29 instruction tuned LLMs from 10 families and find that fake alignment is not explained by reasoning capability alone, but also relates to whether an LLM incorporates future consequences into its response choice and can be steered toward a conflicting target objective. We identify three behavioral groups across train and deploy modes, Compliant, Fake Alignment, and Refusal, and provide preliminary explanations based on compliance sensitive to system prompts, consequence driven switching, and value policy dominance.

</details>

### 74. Finding the Cracks: Auditing Safety Alignment in LLMs through Interpretable Feature Analysis

📄 [OpenReview](https://openreview.net/forum?id=X2sdgaahIP)　📅 2026-10　🏷️ P1

**关键词**：`SAE`、`safety audit`、`brittle directions`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：安全对齐以内机制审计缺方法——既有方法锁定预定义安全方向且不测特征跨数据集可迁移性
- 🔬 **研究方法**：SAE 框架：互信息+激活一致性识别安全关键特征并因果干预（Llama/Qwen 指令与安全调优版）+跨安全数据集与主题域泛化测试
- 📌 **结论**：少量特征即可不微调不对抗提示把有害率 11.16%→47.81%（Qwen 11 倍增益）且流畅连贯——安全对齐部分编码在少数集中脆弱潜方向，需更分布式表示

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment in LLMs is typically evaluated behaviorally, leaving internal mechanisms underlying harmful outputs underexplored. Mechanistic interpretability via Sparse Autoencoders (SAEs) offers a principled route to auditing these internal representations, yet existing approaches target predefined safety directions and none test feature transferability across datasets. We, therefore, apply an SAE-based mechanistic interpretability framework to identify and causally intervene on safety-critical features in instruction- and safety-tuned LLMs, 
Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct. A small set of features identified via mutual information and activation consistency reliably 
increases unsafe outputs without fine-tuning or adversarial prompting (Llama harmful rate rising from 11.16% → 47.81%, Qwen from 9.75% → 28.59%), generalizes across safety datasets and topic domains (average approximate relative increases of 4×  (Llama) and 11×(Qwen)), and outperforms various adversarial baselines, with induced harmful responses remaining fluent and coherent. These findings suggest that safety alignment is partly encoded in a small number of concentrated, brittle latent directions; a structural property of current models that motivates alignment strategies with more distributed safety representations and interpretability methods evaluated for adversarial risk.

</details>

### 75. Rethinking GRPO for Large Reasoning Model Safety Alignment

📄 [OpenReview](https://openreview.net/forum?id=0VJNRxXMZf)　📅 2026-10　🏷️ P2

**关键词**：`GRPO`、`safety alignment`、`reasoning models`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：GRPO 组相对优化对大推理模型安全对齐信号不足——优势塌缩与不安全多样化两失败模式
- 🔬 **研究方法**：理论分析（组内行为一致性削弱安全对比、熵正则在不安全响应多样化）+SSR 优势引导轨迹过滤与安全参照监督+SUDA 类别感知奖励与良性 KL 锚定
- 📌 **结论**：四 Qwen3/R1-Distill×八基准最佳平均安全与推理、安全错误至多降 32.83pp 且低过拒——重构 GRPO 的安全信号

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large reasoning models (LRMs) exhibit strong reasoning capabilities but remain vulnerable to unsafe outputs. While Group Relative Policy Optimization (GRPO) is widely used for safety alignment, its group-relative optimization may provide insufficient safety-directed learning signals. In this paper, we identify two failure modes: advantage collapse, where homogeneous rollout groups yield vanishing advantages, and unsafe diversification, where unsafe behaviors persist and become increasingly diverse. Our theoretical analysis reveals that behavioral consistency weakens within-group safety contrasts, while entropy regularization can diversify unsafe responses when relative signals vanish. To address these challenges, we propose a framework comprising Safety Signal Recovery (SSR) and Safety-Utility Decoupled Alignment (SUDA). SSR combines advantage-guided trajectory filtering and safe reference supervision to recover effective safety learning signals, while SUDA employs category-aware rewards and benign-only KL anchoring to mitigate over-refusal without compromising safety. Experiments across four Qwen3 and DeepSeek-R1-Distill variants and eight benchmarks show that our framework achieves the best average safety and reasoning performance, reducing average safety error by up to 32.83 percentage points while maintaining low over-refusal.

</details>

### 76. Single-turn misalignment is not a solved problem: Measuring the effect of user pressure with matched controls

📄 [OpenReview](https://openreview.net/forum?id=5GY1UlGKVS)　📅 2026-10　🏷️ P2

**关键词**：`user pressure`、`matched controls`、`misalignment benchmark`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：单轮失准未解决——用户压力效应需匹配对照测量
- 🔬 **研究方法**：HARLEY：1591 匹配对比集×17 语言真实用户轮（压力/措辞/风格变体+不必要拒答/借口易感）×17 模型 85000 响应
- 📌 **结论**：用户压力使失准 4.3%→20.4%；短借口使拒答 21.3%→5.9%；两小开源模型排序可覆盖六前沿模型 90% 失准提示——廉价模型可优先化评测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Language models must resist user pressure while remaining helpful on legitimate requests. We introduce HARLEY, a benchmark of 1,591 matched contrast sets built around real user turns in 17 languages. Its variants test responses to pressure, wording, and style, alongside unnecessary refusal and susceptibility to pretexts or unverifiable claims. On a human-reviewed subset of 200 sets in ten languages, we collect 85,000 responses from 17 open-weight and proprietary models. User pressure raises judged misalignment from 4.3% to 20.4%. Adding a short pretext or claimed fact while preserving the requested action reduces refusal from 21.3% to 5.9%. Meanwhile, appropriate requests with concerning surface cues elicit 3.1 percentage points more refusal than matched controls. Susceptibility also overlaps across models, i.e., ranking target prompts using two small open models places 90% of those eliciting misalignment from at least one of six frontier models in the top third. These findings show that single-turn misalignment persists and that inexpensive models can help prioritize evaluation. We release HARLEY, its construction pipeline, a taxonomy of user pressures, along with observed behaviours to support controlled comparisons across models.

</details>

### 77. The Wrong Kind of Right: Quantifying and Localizing Misfired Alignment in LLMs

📄 [OpenReview](https://openreview.net/forum?id=5aePrqV5Rx)　📅 2026-10　🏷️ P2

**关键词**：`misfired alignment`、`stereotype`、`MAR metric`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：安全导向行为可误伤：明确有据的结论也被对齐压制
- 🔬 **研究方法**：2032 个 BBQ 派生对比对+Misfired Alignment Rate（刻板相关问题错而对照项对的比率）×25 LLM+启动实验
- 📌 **结论**：所有 LLM MAR 4.7-18.9% 而人类 0.0%；对齐线索启动可放大——misfired alignment 是可量化的系统性失效模式

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Warning: This paper studies stereotypes and biases, and contains potentially disturbing examples, used for illustration purposes only. Our findings should not be interpreted as an argument against alignment. Instead, this paper highlights the need for principled approaches to more advanced alignment.

Alignment aims to ensure that large language models (LLMs) behave safely and reliably, including by avoiding unsafe inferences. However, we show that such safety-oriented behaviors can misfire: models may reject warranted conclusions even when they are explicitly supported by context. We call this failure mode misfired alignment, where alignment-induced changes cause LLMs to override explicit evidence. To quantify this phenomenon, specifically on stereotype-related alignment, we introduce dataname{}, a benchmark consisting of 2,032 BBQ-derived contrastive pairs, and define a new metric, Misfired Alignment Rate (MAR), which measures on a 0
100 scale how often a model fails on a stereotype-related question but succeeds on its contrastive counterpart. We benchmark 25 LLMs on dataname{}, and show that all LLMs, including the most recent ones, exhibit non-trivial (4.7
18.9%) MARs while all human participants achieve 0.0% within-annotator MAR. Controlled priming experiments further show that alignment-induced cues can substantially amplify MAR across LLMs, indicating that these failures are not merely artifacts of individual examples but can be induced by safety-related framing. Mechanistic analyses on open-weight LLMs reveal late-layer suppression of evidence-supported answers, and comparisons between instruct and base LLMs suggest that this suppression emerges after instruction training. These findings show that current alignment methods can overgeneralize surface-level safety cues, to the point of overriding objective evidence, motivating more work on alignment objectives that better preserve contextual grounding.

</details>

### 78. Seeing Harm, Saying Less: Geometry of Refusal across Text and Image in Vision-Language Models

📄 [OpenReview](https://openreview.net/forum?id=BHf3gLLv8F)　📅 2026-10　🏷️ P2

**关键词**：`refusal geometry`、`cross-modal`、`implicit refusal`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：VLM 对文字陈述的危害远比图像展示的同危害更易拒答——差距的几何基础未知
- 🔬 **研究方法**：配对网格（每条件含图、只变危害位置）+生成前线性可解码性与方向分析+中途消融与双向转向
- 📌 **结论**：视觉危害被登记且依赖文本导出的同一拒答方向，但沿该方向走得不够远——中间响应处于显式拒答与顺从之间（跨模态拒答几何学）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models refuse a harmful request stated in words far more readily than the same harm shown in an image. We study this gap with a paired grid in which every condition contains an image and only the location of harm changes. In three open models, moving harm into the image mainly costs explicit refusals, replaced by intermediate responses close to implicit refusal that neither humans nor an LLM judge label consistently. Before generation, visual harm is linearly decodable almost as well as textual harm, but with a smaller magnitude and partly along its own direction. At mid-depth, image-driven refusal still depends on a direction estimated from text alone: ablating it removes much of this refusal, and at equal harm, image-driven inputs travel less far along it than their text-driven pairs. Steering along this direction moves the intermediate responses either way, toward explicit refusal or toward compliance, which places them between the two. Visual harm is thus registered and relies on the same direction as textual harm, but it does not travel far enough along it for the refusal to be stated explicitly.

</details>

### 79. System Prompts Affect Response Bias More Than Discriminability in LLM Safety

📄 [OpenReview](https://openreview.net/forum?id=GDd6jTkx0G)　📅 2026-10　🏷️ P2

**关键词**：`system prompt`、`response bias`、`signal detection`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：安全评测聚焦合规-拒答权衡——系统提示的实际作用是提示条件化任务选择
- 🔬 **研究方法**：八安全任务提示族×三清晰度级×三基准 13 模型，信号检测论区分辨别力 vs 反应标准
- 📌 **结论**：系统提示主要移动拒答意愿而不可靠改善安全-不安全辨别；提示族还在六种行为政策间移动响应——提示清晰度≠辨别力（安全评测的 SDT 视角）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model safety evaluations often focus on a compliance–refusal tradeoff: models should refuse unsafe requests without refusing safe ones. We argue that this misses a broader form of prompt-conditioned task selection, where the same request can elicit different behaviors depending on the system prompt. We investigate this using a controlled evaluation crossing eight safety-task prompt families with three clarity levels across HarmBench, XSTest, and IHEval. Holding benchmark items fixed, we evaluate 13 models and use signal detection theory to distinguish two possibilities: whether models become better at telling safe from unsafe requests (discriminability), or simply more willing to refuse (response criterion). We find substantial differences in discriminability across models, but system prompts primarily shift the willingness to refuse, with smaller and less consistent effects on discriminability. Increasing prompt clarity makes models more willing to refuse without reliably improving their ability to distinguish safe from unsafe requests. Beyond refusal, prompt families also shift responses among six distinct behavioral policies, including clarification and safe help. Together, these findings show that system prompts primarily change how models respond to safety-relevant requests rather than consistently improving their ability to distinguish safe from unsafe ones.

</details>

### 80. PRISM: Process-Level Risk-Aware Tree Search for Safe Reasoning in Large Language Models

📄 [OpenReview](https://openreview.net/forum?id=GGHj9jrPLl)　📅 2026-10　🏷️ P2

**关键词**：`safe reasoning`、`MCTS`、`process-level risk`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：安全对齐只监督最终答案——推理中浮现的危险前提不受约束
- 🔬 **研究方法**：PRISM：风险感知意图分析把多维查询风险映射到 MCTS 深度/宽度/探索/剪枝/风险权重+SafeUCT 累积风险惩罚+四维联合过程奖励函数+Pareto 轨迹选择
- 📌 **结论**：HarmBench/StrongReject ASR 6.2/8.5%（降 31/46.3pp）且保 AlpacaEval/GSM8K——推理时的过程级安全树搜索

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large reasoning models rely on multi-step intermediate reasoning, but existing safety alignment supervises only final answers, failing to constrain dangerous premises emerging during reasoning. We propose PRISM, a process-level risk-aware tree search framework jointly modeling safety, utility, and computational cost at inference time. A risk-aware intent analyzer estimates multidimensional query risk and maps it to MCTS search depth, width, exploration, pruning threshold, and risk weight. PRISM introduces cumulative risk penalties (SafeUCT), dangerous-node pruning, and a four-dimensional Joint Process Reward Function (utility, harmfulness, coherence, faithfulness) across all MCTS stages, using a lightweight value model to reduce full-rollout cost and Pareto trajectory selection to balance safety and utility. Experiments on Llama-3.1-8B-Instruct show PRISM achieves 6.2%/8.5% ASR on HarmBench/StrongReject (31.0/46.3pp reduction vs. Base), preserves AlpacaEval 2.0 and GSM8K performance, and attains the highest SU of 0.755. Ablations confirm that risk scheduling, SafeUCT, pruning, JPRF, and Pareto selection each affect final safety, process safety, cost, and the safety–utility trade-off.

</details>

### 81. Risk and Refusal: Mechanisms of LLM Responses to Suicidal Ideation

📄 [OpenReview](https://openreview.net/forum?id=GLq83qdysp)　📅 2026-10　🏷️ P2

**关键词**：`suicidal ideation`、`refusal mechanism`、`clinical protocol`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：自杀意念语境下拒答本身即安全失败——拒答与响应级风险的机制关系未明
- 🔬 **研究方法**：八指令模型×三数据集（是否告知 SI 语境/是否给临床协议）+六开源模型机制分析（拒答方向共享性）
- 📌 **结论**：基线风险主要来自忽视披露+拒答；告知语境或直接压制拒答增加参与但不降风险甚至升——临床协议一致降风险且降拒答——只在该拒时拒、该谈时安全谈

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Refusal is a common safety mechanism in large language models (LLMs), yet in contexts of suicidal ideation (SI), refusing to engage can itself constitute a safety failure. We evaluate how eight instruction-tuned LLMs respond to SI and self-harm disclosures across three datasets, varying whether models are informed that a disclosure expresses SI and whether they receive a clinician-developed response protocol, and complement this with mechanistic analyses in six open-weight models. Our results reveal a nuanced relationship between refusal and response-level risk. At baseline, elevated risk in model responses is driven primarily by inattention to the disclosure, alongside refusal to engage. Mechanistic analyses suggest that models may refuse SI disclosures through the same direction that mediates their refusals of harmful requests. However, informing models of the SI context, or suppressing refusal directly, increases engagement without reliably lowering response risk, and may raise it. In contrast, the clinician-guided protocol consistently reduces response-level risk while also reducing refusal. Together, these analyses and ablations motivate the need for models that refuse only when warranted and engage in interactionally safe ways when users disclose SI.

</details>

### 82. Feature Forensics: Identifying Behavioral Vulnerabilities in LLMs through Sparse Autoencoders

📄 [OpenReview](https://openreview.net/forum?id=KDx2Ei42x9)　📅 2026-10　🏷️ P2

**关键词**：`SAE features`、`behavioral vulnerability`、`token-level`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：SAE 特征分组能否揭示特征交互与漏洞的关系——粒度与 token 定位问题
- 🔬 **研究方法**：外部有害概念表示+token 级子空间相似性识别提示条件化 SAE 特征，聚类/层级/单 token 三分组策略对比并放大测量
- 📌 **结论**：与有害概念最强对齐的单 token 定位的特征子群比多 token 分组转向更强——挑战提示级安全表示观（token 级漏洞取证）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Grouping latent features identified by sparse autoencoders (SAEs) may reveal how interactions among features relate to vulnerabilities in large language models (LLMs). We study safety-relevant SAE features as structured groups and ask three questions: (a) When harmful behavior occurs, do the associated activations form semantically coherent groups, or can behavior-altering interactions involve semantically distant features? (b) What is the minimal feature granularity required to induce safety failures, and can a single prompt token localize such feature subgroups? (c) How does the impact of feature subgrouping vary across malicious queries and conversational exchanges? We use external harmful-concept representations and token-level subspace similarity to identify prompt-conditioned SAE features, comparing cluster-based, hierarchical linkage, and single-token-driven grouping strategies. We amplify the feature subgroups and measure changes in harmfulness and generation quality. Across two adversarial benchmarks, SAE feature subgroups substantially alter model behavior. Feature subgroups localized using the token most strongly aligned with the harmful concept produce stronger steering effects than subgroups identified using multiple prompt tokens. This finding challenges prompt-level views of safety-relevant representations, suggesting that analyzing the prompt as a whole can miss safety vulnerabilities concentrated around a single token. Moreover, effective subgroups contain semantically dissimilar features. Code is available href{https://anonymous.4open.science/r/Mechanistically_Steering-4720/README.md}{here}.

</details>

### 83. LOPO: Local OPD-Guided Policy Optimization for Over-Refusal Mitigation in Multimodal Safety Alignment

📄 [OpenReview](https://openreview.net/forum?id=amjepIkIwR)　📅 2026-10　🏷️ P2

**关键词**：`over-refusal`、`multimodal safety`、`token-level optimization`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：多模态安全训练诱发虚假文本/视觉先验+轨迹级负反馈扩散到全响应压制有效感知
- 🔬 **研究方法**：LOPO：语义保持先验衰减输入构建特权教师+同在策前缀下师生分布差定位关键拒答决策 token，仅在这些位置掩蔽/放大/局部蒸馏并与多奖励 GRPO 联合
- 📌 **结论**：安全/过拒/通用三线均衡改善——过拒缓解的 token 级定位修正

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal safety alignment aims to enable models to reject genuinely harmful requests without over-refusing benign inputs that contain sensitive words or high-risk visual elements. However, safety training can induce spurious textual and visual priors, causing models to rely on superficial cues rather than jointly reasoning over user intent and visual evidence. Moreover, trajectory-level policy optimization distributes negative feedback across the entire response, which may suppress valid perception and reasoning while providing weak supervision to the few tokens that actually trigger refusal. To address these issues, we propose LOPO, a local OPD-guided policy optimization framework for multimodal safety alignment. LOPO constructs a privileged teacher from semantics-preserving, prior-attenuated inputs and evaluates teacher and student distributions under the same on-policy prefix. Their differences are used to identify critical refusal-decision tokens. For over-refusal trajectories, LOPO masks the advantages of non-critical tokens, amplifies the negative advantages of critical tokens, and applies local on-policy distillation only at these positions. This token-level correction is jointly optimized with multi-reward GRPO to preserve the overall safety-utility trade-off. Experiments across multimodal safety, over-refusal, and general-capability benchmarks demonstrate that LOPO reduces text- and vision-induced over-refusal while maintaining harmful-request rejection and general multimodal performance.

</details>

### 84. AGSteer: Attribution-Guided Steering for Over-Refusal Mitigation

📄 [OpenReview](https://openreview.net/forum?id=g41kbkJL4y)　📅 2026-10　🏷️ P2

**关键词**：`over-refusal`、`steering`、`attribution`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：拒答 steering 在提升安全的同时放大过度拒绝——行为级目标约束不足
- 🔬 **研究方法**：AGSteer：对比归因识别过拒/有害拒/共享拒的注意力头，头约束 steering 向量精化+输入特定路由
- 📌 **结论**：三 LLM×三 steering 法上持续降过拒且保安全增益——头级归因引导的选择性纠偏

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Refusal steering provides a lightweight approach for improving the safety of large language models, but it can also amplify over-refusal. Existing mitigation methods reduce false refusals with objectives based on model responses or layer representations, but such objectives may provide insufficient constraints for preserving refusal on harmful prompts. Recent mechanistic studies suggest that refusal steering effects are mediated by specific internal components such as attention heads. This suggests that head-level patterns may provide useful guidance for mitigating over-refusal while preserving refusal on harmful prompts. To this end, we propose AGSteer, an attribution-guided steering framework for over-refusal mitigation. AGSteer uses contrastive attribution to identify behavior-specific attention heads under steering, including over-refusal, harmful-refusal, and shared refusal heads. It then performs head-constrained steering vector refinement and input-specific routing, adjusting steering effects selectively according to the attributed heads. Experiments across three LLMs and three steering-vector construction methods show that AGSteer consistently reduces steering-induced over-refusal while largely preserving safety gains of refusal steering.

</details>

### 85. Gyges: Benchmarking Value Alignment as Hierarchical Value Stability

📄 [OpenReview](https://openreview.net/forum?id=nDMotUyNKd)　📅 2026-10　🏷️ P2

**关键词**：`value alignment`、`benchmark`、`agentic`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：价值对齐评测常明说规则或点名违规——测的是词已指向的价值而非未指明时的持守
- 🔬 **研究方法**：Gyges：1040 项 40 场景族，单事实决定价值是否在场，命名/未命名请求×规则×压力×监督交叉
- 📌 **结论**：规则明说时 13 模型趋同、抽掉后分化——三模型嘴上不可接受却多数照做（价值稳定性的分层评测）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Goal alignment asks whether a language model does as asked, while value alignment asks whether it holds its values when instructions are underspecified or conflict with them. Yet evaluations of value alignment often state the rule or name the violation, testing values where words already point to them. To address this, we propose Hierarchical Value Stability, which ranks a value's spirit, what it protects, above its letter and its rules. A stable model holds a value when it is at stake and helps when it is not. We test this with Gyges, an agentic benchmark of 1,040 items from 40 scenario families, in which one fact in a record decides whether the value is at stake. Requests either name the violation or reach the same outcome unnamed, and are crossed with a rule, pressure, and monitoring. With the rule stated, most of the 13 models look alike. Without it, they diverge, as some hold far less and those that hold most also withhold some harmless help. Unnamed requests change little more, although one model protects mainly what is named. Neither pressure nor an absent observer reliably lowers holding. Three models call an action unacceptable when asked, yet take it in most cases. These findings suggest that a stated rule can hide how differently models hold their values, and that evaluating against Hierarchical Value Stability makes these differences visible.

</details>

### 86. Cross-Modal Safety Effects Do Not Reliably Transfer Across Multimodal Language Models: A Causal Evaluation

📄 [OpenReview](https://openreview.net/forum?id=qvqCLpn4jD)　📅 2026-10　🏷️ P2

**关键词**：`cross-modal safety`、`causal evaluation`、`transfer`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：聚合安全分不分离各模态效应与交互——交互是否跨模型迁移未知
- 🔬 **研究方法**：CCMS 匹配因子设计：场景内差中差估计跨模态安全交互+五开源模型×98 场景族对照
- 📌 **结论**：参考模型正交互 0.1148 而四个目标模型仅一个同向、三个反转——跨模态安全交互不可从单一模型泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal language models must respond safely when images and dialogue history jointly determine a request's meaning. Yet aggregate safety scores do not separate effects on each component from their interactions or establish whether those interactions transfer across models. We introduce CCMS, a matched factorial evaluation that estimates cross-modal safety interactions through difference-in-differences within scenarios and compares models across common families. Across five open-weight models and 98 MTMCS-Bench families, the Qwen3.5-9B reference has a positive mean interaction of 0.1148, with one of four targets matching its direction and the other three reversing it under the frozen judging protocol. Null-centered inference preserves these decisions. On 125 VLSBench-derived families, the reference estimate is near zero, although two contrasts between target and reference remain significant after Holm correction. A full-panel sighted audit retains negative interactions for Qwen3.5-2B and Ministral but leaves Phi-4's direction uncertain. Cross-modal safety interactions should therefore be tested across models, sources, and outcome measures before generalizing a reference-model finding.

</details>

### 87. On-Policy Self-Evolution via Failure Trajectories for Agentic Safety Alignment

📄 [OpenReview](https://openreview.net/forum?id=wKMgAAzUC4)　📅 2026-10　🏷️ P2

**关键词**：`agentic safety alignment`、`failure trajectories`、`Pareto optimization`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：agent 以轨迹失败（不安全工具调用/跟随注入/顺从有害/过拒）——响应级离策信号稀疏且安全-效用互损
- 🔬 **研究方法**：FATE：验证器打分失败→同策略提修复候选→安全/效用/过拒/轨迹有效四过滤的密集轨迹监督+PFPO Pareto 前沿策略优化
- 📌 **结论**：AgentDojo/AgentHarm/ATBench 跨域提升安全且保任务——从失败轨迹自进化的 agent 安全对齐

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Tool-using LLM agents fail through trajectories rather than only final responses, as they may execute unsafe tool calls, follow injected instructions, comply with harmful requests, or over-refuse benign tasks despite producing a seemingly safe answer.
Existing safety-alignment signals are largely response-level or off-policy, and often incur a safety–utility trade-off: improving agent safety comes at the cost of degraded task performance. Such sparse and single-objective rewards severely limit real-world usability.
To bridge this gap, we propose FATE, an on-policy self-evolving framework that transforms verifier-scored failures into repair supervision without expert demonstrations.
For each failure, the same policy proposes repair candidates, which are then re-scored by verifiers and filtered across security, utility, over-refusal control, and trajectory validity.
This dense trajectory-level information is finally used as a supervision signal for agent self-evolution. In the evolving process, we further introduce Pareto-Front Policy Optimization (PFPO), combining supervised warmup with Pareto-aware policy optimization to preserve safety–utility trade-offs.
PFPO extends Pareto selection from historical replay to freshly sampled optimization groups, restricting their policy-gradient support.
Experiments on AgentDojo, AgentHarm, and ATBench show that FATE improves safety across different models and scales while preserving useful behavior.
Compared with strong baselines, FATE reduces attack success rate by 33.5%, harmful compliance by 82.6%, and improves external trajectory-safety diagnosis accuracy by 8.6 percentage points.
These results suggest that failed trajectories can provide structured repair supervision for safer self-evolving agents.

</details>

## 四、dLLM（扩散语言模型）安全

### 88. Tracing Refusal-Associated Features Across Diffusion Time

📄 [OpenReview](https://openreview.net/forum?id=LVk09Scbdd)　📅 2026-10　🏷️ P2

**关键词**：`dLLM`、`refusal features`、`mechanistic`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：扩散语言模型在掩码响应逐渐成文的过程中暴露一系列内部状态——拒答信息何时可恢复、拒答特征随扩散时间如何演变未知
- 🔬 **研究方法**：LLaDA-8B-Instruct 上 32 个 MLP 块测量+六层 SAE：64 提示（32 源目标）追踪拒答关联特征，任一响应 token 揭掩前拒答信息已可恢复；激活/对照例连接两类时间剖面；定时干预配合完整输出比较
- 📌 **结论**：单特征呈'敏感请求语境的初始分离'与'响应完成中增长的分离'双剖面——dLLM 拒答表示的时间异质性（扩散时序上的安全干预窗口刻画）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion language models expose a sequence of internal states as a masked response becomes text. We trace refusal-associated features through this sequence in LLaDA-8B-Instruct, combining measurements from all 32 MLP blocks with sparse autoencoders at six layers. On 64 prompts from 32 source goals, refusal information is recoverable before any response token is unmasked. Individual features exhibit two contrasting profiles: an initial separation associated with sensitive request contexts, and a separation that grows during response completion. Activating and contrasting examples connect these profiles to different aspects of the generated response. Timed interventions complement these profiles with complete-output comparisons of refusal, completion, and response quality. Our analysis characterizes the temporal heterogeneity of refusal-associated features and provides a procedure for connecting their trajectories to complete outputs.

</details>

### 89. Watermarking Diffusion Language Models with Learned Foresight and Balanced Bands

📄 [OpenReview](https://openreview.net/forum?id=b1vgG2Dffj)　📅 2026-10　🏷️ P2

**关键词**：`dLLM watermark`、`learned foresight`、`green-red`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：绿红水印依赖前文派生绿表——但扩散 LM 常'先选 token 后定前文'，token 反过来塑造邻居的绿表
- 🔬 **研究方法**：学习此前固定的两组件：作绿表的词汇带（分离竞争候选、保零分布精确）+估计候选如何移动邻居预测的前瞻预测器；检测端按去重上下文-token 对计绿
- 📌 **结论**：WaterBench LLaDA-8B 上两学习组件增益近可加：强水印下 1%FPR 检出≥96% 且 LLM 判官分与无水印文本持平——适配并行生成的水印机制（dLLM 溯源）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Green-red watermarks favor tokens from a green list that a secret key derives from the preceding tokens. Diffusion language models, however, often choose a token before its preceding tokens, and the token later shapes its neighbors' green lists. Prior work therefore tilts each choice to raise the expected number of green tokens at its own and its neighbors' positions. Building on this objective, we first learn two components that prior work keeps fixed: vocabulary bands that serve as green lists, separate competing candidates and keep the null distribution exact, and a foresight predictor that estimates how each candidate shifts its neighbors' predictions. Second, we count green tokens as the detector does, once per distinct context-token pair, so repetition earns nothing. On WaterBench with LLaDA-8B-Instruct, each learned component raises the z-score at equal distortion, and their gains are nearly additive. With a strong watermark, ours detects at least 96% of responses at a 1% false-positive rate while matching the LLM-judge score of unwatermarked text. Ours also detects more responses on Dream and as many or more on code and question answering without a significant loss in task accuracy.

</details>

## 五、开源模型治理与权重级安全

### 90. Safety Probes Trained on the Base Model Best Withstand Post-Training and Fine-Tuning

📄 [OpenReview](https://openreview.net/forum?id=5FjW0gaVe9)　📅 2026-10　🏷️ P1

**关键词**：`safety probes`、`checkpoint robustness`、`transfer asymmetry`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：激活探针安全监控与不断微调的权重绑定——在哪个检查点训练才能跨更新存活
- 🔬 **研究方法**：三族全层 token 级线性探针×三激活位×三任务（工具伤害/高风险请求/化学）于 OLMo-3/Apertus 基座与后训检查点互测+有害良性微调评估
- 📌 **结论**：基座训练探针前向迁移损失小、后训探针回基座丢 8.8-17.8pp；有害微调后基座探针几乎不退化反超后训探针——安全探针应训在基座（部署监控的检查点选择）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Activation probes on a language model's hidden states are deployed as cheap safety monitors, but unlike external text classifiers, they are tied to weights that keep changing through fine-tuning. To test their robustness against weight updates, we train three families of token-level, all-layer linear probes at three activation sites to detect instrumental harm, high-stakes requests, and chemical harm on the base and major post-training checkpoints of  OLMo-3-7B and Apertus-8B, and evaluate them on the other checkpoints and on harmful and benign fine-tunes of  OLMo-3-7B's final checkpoint. We find an asymmetry: base-trained probes transfer forward with little loss, but later-trained probes moved back to base lose on average 8.8–17.8 points of true-positive rate at 1% false positives on instrumental harm and high-stakes. Linear probes trained on another checkpoint to reproduce a teacher probe's token-level logits recover a base-trained teacher's class signal fully, but only 73–94% of a later teacher's from base, suggesting that post-training adds linearly decodable signal. Moreover, on checkpoints after further harmful fine-tuning the base-trained probe still shows little degradation on every task, and thereby overtakes the linear separability advantage of probes trained on later checkpoints on high-stakes and significantly closes the gap on instrumental harm detection.

</details>

### 91. Same Recipe, Different Fate: The Training Recipe's Effect on Safety Erosion from Benign Fine-Tuning Depends on the Model Family

📄 [OpenReview](https://openreview.net/forum?id=M0daiyC5he)　📅 2026-10　🏷️ P1

**关键词**：`benign fine-tuning`、`safety erosion`、`training recipe`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：良性微调侵蚀安全但报告效应大相径庭——训练配方与模型族的交互未被控制
- 🔬 **研究方法**：六指令模型（OLMo-2/Llama-3/Qwen2.5 各 1B 与 7-8B）×LoRA×4800 Dolly 行×三种子×配方网格，侵蚀 E=Qwen3Guard 不安全份额增量+HarmBench 副判官
- 📌 **结论**：配方效应强烈依赖模型族：调度配方使 OLMo-2-1B 侵蚀 +45.1→+28.8pp 却使 Llama/Qwen 更糟；同配方下 OLMo 最耐 Qwen 最蚀（两尺寸一致）——安全侵蚀不是微调的普遍属性而是配方×家族交互（harmful fine-tuning 的配方学）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Benign fine-tuning can erode safety, but reported effects vary widely. We compare six instruct models from OLMo-2, Llama-3 and Qwen2.5, at about 1B and at 7–8B, using LoRA on 4,800 Dolly rows with three seeds per main recipe cell. Erosion E is the rise in Qwen3Guard's Unsafe share of 600 sampled answers to 200 development harm prompts; HarmBench is a second judge. At 1B, a Scheduled recipe (warmup, cosine decay and token-mean loss) lowers OLMo-2-1B's mean erosion from +45.1 to +28.8 pp, compared with +59.3 to +57.1 for Llama-3.2-1B and +71.9 to +73.9 for Qwen2.5-1.5B. Both OLMo family-interaction intervals exclude zero on both judges, but OLMo's over-refusal rises by 11.7 pp. The pre-registered OLMo-versus-Llama replication at 7–8B is inconclusive. Qwen2.5-7B's mean erosion falls from +78.1 to +68.9 pp; its interaction with OLMo excludes zero on Qwen3Guard only. Halving the learning rate lowers mean erosion in OLMo-7B and Llama-8B, without establishing equal effects. Under one recipe, OLMo erodes least and Qwen most at both sizes. Dark–light fiction differences lie within wide pre-registered margins. A blind human read suggests the Unsafe label mostly tracks lost refusal. All results are development evidence; we report every screened setting and the judges' limits.

</details>

### 92. Persona-Mediated Spillover: Predictable Finetuning Side Effects and the Scale Limit of Controlling Them

📄 [OpenReview](https://openreview.net/forum?id=fHp4WDN31h)　📅 2026-10　🏷️ P1

**关键词**：`finetuning side effects`、`persona shift`、`control limits`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：微调副作用（更不真实/更谄媚/更不拒答）可否预测、激活干预可否控制——与规模的关系未知
- 🔬 **研究方法**：20+ LoRA 适配器×Qwen/Llama 8B-70B：技能表示解释能力增益而 persona 位移关联行为副作用+转向与路径阻断因果干预
- 📌 **结论**：可检测的转向 30 对中 20 对符号与 persona-任务对齐一致；Qwen-8B 上移除 persona 成分反转 33-52% 行为转移但大规模同干预减弱——可诊断不可控制的副作用（微调外溢的规模极限）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Finetuning on one task can change behavior on
unrelated tasks: a model tuned for mathematics
may become less truthful, more sycophantic, or
less willing to refuse harmful requests. We ask
whether these side effects are predictable and
whether activation interventions can change
them. Across more than 20 LoRA adapters on
Qwen and Llama models from 8B to 70B, we
measure downstream changes and shifts along
interpretable persona traits. Skill representa-
tions mainly explain capability gains, whereas
persona shifts are more closely associated with
behavioral side effects. Among steering effects
that pass our detection thresholds, signs agree
with persona–task alignment for 20 of 30 pairs
overall and all six detectable non-refusal ef-
fects. Prediction does not imply control. On
Qwen-8B, steering and path-blocking support a
partial causal route, and removing persona com-
ponents reverses 33–52% of behavioral trans-
fer; replaying the activation displacement does
not reproduce finetuning. At larger scales, per-
sona shifts remain associated with behavioral
changes, but the same interventions weaken.
Persona measurements can therefore diagnose
side effects even when they do not provide an
effective means of changing behavior.

</details>

### 93. Do Activation Monitors Survive Model Updates? Benchmarking, Predicting, and Repairing Activation-Monitor Staleness

📄 [OpenReview](https://openreview.net/forum?id=kuLUC3RUkb)　📅 2026-10　🏷️ P1

**关键词**：`activation monitor`、`staleness`、`deployment`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：激活探针进入部署安全栈但模型不断被量化/微调/LoRA/合并适配——冻结探针能否存活常规更新首次系统测试
- 🔬 **研究方法**：跨安全监控器×层深×更新族×开源模型网格+预部署特征预测退化+免标签激活重对齐修复
- 📌 **结论**：量化类更新基本保持而微调类频繁致陈旧（隐私探针最脆、拒答合规最稳、QLoRA 特别伤）——微调应默认触发监控重验证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Activation monitors — lightweight probes on a model's internal representations — are increasingly common in deployment safety stacks, but deployed models are rarely static: they are quantized, fine-tuned, adapted with LoRA, or served with merged adapters while the monitor stays frozen. We present the first systematic test of whether probes trained on a base model survive these routine updates. Across safety-relevant monitors, depths, update families, and open-weight models, we find a sharp split: quantization-style updates largely preserve frozen-probe performance, while fine-tuning-style updates frequently make probes stale. Fragility is strongly monitor-dependent — privacy/PII probes degrade most, refusal-compliance least, showing that retraining a behavior need not stale its monitor — and QLoRA is especially damaging despite NF4 alone being benign, suggesting quantization becomes riskier under adaptation. Degradation is predictable from pre-deployment features, enabling triaged revalidation budgets, and cheap label-free activation realignment repairs every repair-relevant stale cell, with none requiring calibration, few-label heads, or labeled retraining. Fine-tuning should therefore trigger monitor revalidation by default.

</details>

### 94. No Cheap Escape: Collateral Barrier Geometry for Self-Destructive Language Models

📄 [OpenReview](https://openreview.net/forum?id=ta0VP0Z6Ra)　📅 2026-10　🏷️ P1

**关键词**：`harmful fine-tuning defense`、`weight edit`、`barrier geometry`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：有害微调与直接权重编辑能低成本移除开源模型安全对齐——自毁式防御可被更便宜的旁路绕过
- 🔬 **研究方法**：无廉价逃逸原则+CBG：广义特征值问题找单位良性代价下安全改变最大的最弱逃逸方向，训练使其退化良性行为
- 📌 **结论**：三 7B 模型上基线多被非发散有害微调攻破而 CBG 保持安全或严重损效用；良性微调基本保效用（有害微调防御的几何化）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Harmful fine-tuning and direct weight edits can remove the safety alignment of open-weight language models at little cost to capability. Self-destructive defenses make an anticipated harmful adaptation degrade the model, but an attacker can take another, cheaper route. We propose the no-cheap-escape principle: no local parameter direction should change safety behavior substantially at small benign cost. Collateral Barrier Geometry (CBG) identifies the weakest escapes, the directions with the most safety change per unit of benign change, through a generalized eigenvalue problem on a small Gram matrix, and trains the model so that these escapes degrade benign behavior. Across three 7B models, baselines are generally compromised in non-divergent harmful fine-tuning settings, whereas CBG remains safe or exhibits severe utility loss under the reported standard attacks; benign fine-tuning largely preserves its utility on Llama-2 and Qwen2.5. Frozen-middle fine-tuning and budgeted refusal-direction edits leave CBG safe, but benign-KL-regularized updates narrowly compromise it.

</details>

### 95. Hidden in Emotion: Selective Fingerprinting of Open-Weight Large Language Models

📄 [OpenReview](https://openreview.net/forum?id=0fJKS87bhC)　📅 2026-10　🏷️ P2

**关键词**：`open-weight fingerprint`、`emotion binding`、`selective distillation`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：固定查询-密钥指纹脆、语义域条件水印可被对手按语言/主题过滤验证查询——开源模型 IP 保护需更隐蔽的指纹
- 🔬 **研究方法**：HiE：情绪改写与原提示的隐表示差作情绪残差，监督对比学习聚合同情绪残差+选择性蒸馏红绿水印到指定情绪（其余情绪与中性提示正则抑制泄漏）
- 📌 **结论**：多开源 LLM 五轮评测指纹检测稳定且性能变化 -1.67 至 +0.32pp——绑定内隐属性（情绪）的选择性指纹，抗语义域过滤的开源权重溯源

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Protecting the intellectual property of open-weight large language models requires fingerprints that are both stealthy and robust to model modifications. However, fingerprints based on fixed queries and keys are often brittle, while watermarks conditioned on semantic domains rely on externally identifiable attributes, such as languages or topics, which adversaries can exploit to selectively filter verification queries. To address these limitations, we propose Hidden in Emotion (HiE), a framework that uses paired residual learning and selective distillation to bind a statistical watermark to a target emotion. Starting from the same base prompts, we construct semantically aligned rewrites expressing different emotions and derive emotion residuals by subtracting the hidden representation of each original prompt from that of its emotional rewrite. We then apply supervised contrastive learning to bring residuals associated with the same emotion closer together while separating those associated with different emotions. In the second stage, we selectively distill a Red-Green watermark for a designated emotion and apply regularization to other emotional and neutral prompts to suppress watermark leakage. Experiments on multiple open-weight LLMs show consistent fingerprint detection across five evaluation rounds, with average performance changes of -1.67 to +0.32 percentage points over eight tasks. The fingerprint also remains detectable under various deployment modifications, including 4-bit quantization and LoRA finetuning on general instructions, demonstrating its robustness. We make our anonymized code available at [https://anonymous.4open.science/r/HiE-7D82/](https://anonymous.4open.science/r/HiE-7D82/).

</details>

### 96. Low-Agreeableness Persona Conditioning for Safe LLM Fine-Tuning

📄 [OpenReview](https://openreview.net/forum?id=3LKy3P2StA)　📅 2026-10　🏷️ P2

**关键词**：`safe fine-tuning`、`persona conditioning`、`data design`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：社交温暖微调降低事实可靠性增谄媚——是否也带安全成本（更愿帮有害请求）
- 🔬 **研究方法**：低宜人性人设改写用户轮+温暖去升级助手响应的配对数据（无需安全标签/检测器/目标改动）×四模型三实验
- 📌 **结论**：降低有害回复率同时保持会话温暖——纯数据设计实现更安全的共情微调（empathetic 微调的安全副作用与修复）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent work has shown that fine-tuning large language models (LLMs) for social warmth degrades factual reliability and increases sycophancy. We ask whether it also carries a safety cost: a model trained to be warm and accommodating may be more willing to help users with harmful requests, and we examine whether this reflects an inherent consequence of empathetic adaptation or an artifact of data construction. We introduce a persona-driven rewriting pipeline that conditions user turns on low agreeableness and pairs this with warm, de-escalating assistant responses. Across
three experiments on four models, our approach lowers the rate of harmful replies, while preserving conversational warmth. Safer empathetic fine-tuning is thus achievable through data design alone, without safety labels, harm detectors, or changes to the training objective.

</details>

### 97. Noise Erodes, Data Steers: How Fine-Tuning Wears Down Weight-Embedded Watermarks

📄 [OpenReview](https://openreview.net/forum?id=7x05x3Qhdb)　📅 2026-10　🏷️ P2

**关键词**：`watermark robustness`、`fine-tuning erosion`、`open-weight supply chain`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：蒸馏进权重的水印要能在下游微调中存活——何时被侵蚀缺定量规律
- 🔬 **研究方法**：学习率×步数×数据绿红构成网格微调水印模型，交叉验证+证伪检验候选侵蚀律
- 📌 **结论**：侵蚀=数据无关分量（η√S 型，LoRA 大减）+数据导向分量（持续增长）；1280 步指令微调后 1%FPR 下单样本检出仅 3-32%——权重水印的侵蚀定律

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Watermarks distilled into the weights of open language models are meant to survive downstream fine-tuning, but there is no quantitative account of when they do. We fine-tune watermarked models on a grid that varies the learning rate η, the number of steps S and the green/red composition of the data, and test candidate erosion laws by cross-validation and falsification tests. Across KGW and Unigram watermarks in two Qwen2.5 sizes and Ministral-3-3B, the data disfavor a learning-rate threshold and reject any law in η S. Erosion has two components. A data-independent one appears even when the model is fine-tuned on its own samples; it is better described by ηsqrt{S} than by η S at first and shows no significant change after about 160 steps (Qwen / KGW). A data-directed one moves detection toward the data's green fraction and keeps growing. A two-component law fits KGW best, but only over the first 80 steps. LoRA greatly reduces the first component but not the second, and random weight perturbations erode mainly in proportion to how much they change the outputs. Unigram resists the data-independent component, but 1280 steps of instruction tuning on Qwen2.5-1.5B leave single-sample detection at 1% false-positive rate at 3–32% for both schemes.

</details>

### 98. DiRe: Dispersing Refusal Vectors to Defend Against Open-Source LLM Abliteration

📄 [OpenReview](https://openreview.net/forum?id=AebbZlZMxF)　📅 2026-10　🏷️ P2

**关键词**：`abliteration defense`、`refusal geometry`、`representation dispersal`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：拒答编码为集中主导方向——abliteration 廉价提取并移除即废掉拒答；既有防御重学或改数据不改变几何集中
- 🔬 **研究方法**：DiRe：压平偏差矩阵奇异值谱并钉住范数——拒答信号分散而非缩放，无单一可提取方向占优
- 📌 **结论**：多家族×攻击×判官组合下保留更多拒答且多数多方向攻击下最强——拒答表示的分散化防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models encode refusal as a concentrated, dominant direction that is cheaply extracted by mean-difference and removed by abliteration, disabling the model's refusal behavior with little compute. Existing defenses relearn refusal after the direction is ablated or spread it only by altering training data, leaving the geometry as concentrated as before. We propose DiRe, which instead disperses the refusal representation itself. DiRe flattens the singular-value spectrum of the deviation matrix while pinning its norm, so the refusal signal is spread rather than rescaled. No single extracted direction then dominates, so abliteration strips away only part of the refusal signal. As a result, DiRe retains more refusal than prior defenses in most family–attack–judge combinations, and remains the strongest under most multi-directional attacks.

</details>

### 99. Exclusive Unlearning

📄 [OpenReview](https://openreview.net/forum?id=HM5yUClIiD)　📅 2026-10　🏷️ P2

**关键词**：`exclusive unlearning`、`scope restriction`、`self-unlearning`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：专用微调（教育助手/客服）要既做好目标任务又拒答域外有害查询——新问题设定
- 🔬 **研究方法**：Exclusive Unlearning：遗忘模型自生成文本以抹除宽域知识能力同时保目标任务性能
- 📌 **结论**：三域指令数据上目标任务提升且域外/越狱查询响应大幅受抑、优于常规遗忘与安全对齐——自我遗忘式能力收敛

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When large language models (LLMs) are fine-tuned for a specific use case, such as an educational assistant or a customer-support chatbot, a key practical challenge is not only to improve their performance on the target tasks but also to prevent them from responding to out-of-scope or harmful queries.
In this work, we introduce Exclusive Unlearning (EU), a new problem setting in which an LLM learns to perform the fine-tuned tasks while broadly unlearning its ability to respond to anything else.
As a simple approach to EU, we present a method that unlearns text generated by the model itself, thereby erasing its broad knowledge and capabilities while preserving its performance on the fine-tuned tasks.
Experiments on instruction-tuning datasets in medicine, mathematics, and education show that our method improves performance on the fine-tuned tasks while substantially reducing the model's ability to respond to out-of-scope queries.
Moreover, our method outperforms conventional unlearning and safety-alignment methods by a large margin in suppressing responses to diverse harmful queries, especially jailbreak attacks.

</details>

### 100. One Direction, Many Languages, Many Scorers: Measuring Cross-Lingual Refusal-Direction Transfer

📄 [OpenReview](https://openreview.net/forum?id=IzWq5ttln8)　📅 2026-10　🏷️ P2

**关键词**：`refusal direction`、`cross-lingual`、`mechanism`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：英语拟合的拒答方向据称可跨语言移除拒答——该结论许可了多少泛化未被检验
- 🔬 **研究方法**：11 语言×3 模型族：消融英语方向在全部 33 模型-语言对降低拒答、各语言自拟合方向不优于英语方向；再分离'识别拒答'与'控制拒答'
- 📌 **结论**：Llama-3.1-8B 上方向预测拒答 0.90 AUROC 而移除反而更拒；资源水平效应随判官固定改变符号——跨语言拒答方向迁移的测量边界（机制结论的稳健性审计）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Removing one direction from a language model's residual stream strips its ability to refuse
harmful requests, and a direction fitted on English has been reported to do this in other
languages too. We ask how much that licenses. Across eleven languages and three model families,
ablating the English direction lowers refusal in all 33 model-language pairs, and a language's
own fitted direction is no better a handle than the English one, so this is not eleven parallel
mechanisms. But identifying refusal and controlling it come apart. In Llama-3.1-8B the direction
predicts refusal at 0.90 AUROC while removing it makes the model refuse more, and that
still holds when we refit at the layer a 32-layer sweep ranks first. The reported tendency for
the effect to track a language's resource level changes sign once the judge is held fixed, and
changes again if only full refusals count. Every number here is an automated judge's opinion, so
we hand-check 373 English and Hindi responses: agreement on our endpoint is 0.72 and 0.82,
the judge's abstentions turn out to be genuine ambiguity, and it over-states refusal by
3-7 points. Claims about multilingual refusal should report the scorer as part of the
result.

</details>

### 101. Prompt2Fingerprint: Plug-and-Play LLM Fingerprinting via Text-to-Weight Generation

📄 [OpenReview](https://openreview.net/forum?id=MOUyLfJYTp)　📅 2026-10　🏷️ P2

**关键词**：`model fingerprinting`、`provenance`、`IP protection`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：主动指纹法为每个身份独立优化注入——算力与部署延迟的规模瓶颈
- 🔬 **研究方法**：Prompt2Fingerprint：指纹条件参数生成——文本描述经专用生成器单前向映射为低秩参数增量即插即用
- 📌 **结论**：保持高指纹准确/无害/鲁棒同时大幅降算力——指纹注入从一次性优化到可复用能力（模型溯源规模化）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The widespread deployment and redistribution of large language models (LLMs) have made model provenance tracking critical challenges. While existing LLM fingerprinting methods—particularly active approaches that embed identity signals via fine-tuning—achieve high accuracy and robustness, they suffer from significant scalability bottlenecks. These methods typically treat fingerprint injection as an independent, one-off optimization task rather than a reusable capability, necessitating separate, resource-intensive optimization for every new identity.  This incurs prohibitive computational costs and deployment delays. To address this, we propose Prompt2Fingerprint (P2F), the first framework that reformulates fingerprinting as a conditional parameter generation task. By leveraging a specialized generator, P2F maps textual descriptions directly to low-rank parameter increments in a single forward pass, enabling plug-and-play LLM fingerprint injection without further model retraining. Our experiments demonstrate that P2F maintains high fingerprint accuracy, harmlessness, and robustness while significantly reducing computational overhead, offering a scalable and instant solution for LLM ownership management.

</details>

### 102. Protecting Safety during Reasoning Training with Low-Rank Fisher Regularisation

📄 [OpenReview](https://openreview.net/forum?id=TIv1W5XGJK)　📅 2026-10　🏷️ P2

**关键词**：`safety preservation`、`fine-tuning defense`、`Fisher regularization`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：能力微调（如推理训练）侵蚀安全护栏——修改微调目标以保安全且高效
- 🔬 **研究方法**：SP-EWC：利用安全相关行为位于低秩子空间——梯度投影到子空间捕获非对角曲率（LoRA 更新/ActSVD/cPCA 三种子空间识别）
- 📌 **结论**：cPCA 版本更好保持护栏且不过度过拒——子空间投影 EWC 的安全保持微调

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are trained to have safety guardrails, but these can be compromised during fine-tuning for new capabilities, such as reasoning. One way to mitigate this degradation is to modify the fine-tuning objective to preserve safety behaviour, but doing so effectively and efficiently remains challenging. We revisit Elastic Weight Consolidation (EWC), which penalises parameter updates based on sensitivity estimates from the diagonal of the Fisher information matrix (FIM). While EWC provides some protection, the diagonal approximation ignores interactions between parameters. We address this limitation by exploiting recent findings that safety-relevant behaviour is located in a low-rank subspace within models. Our method, SP-EWC (Subspace-Projected EWC), projects gradients onto this subspace to capture non-diagonal curvature efficiently. We investigate three different ways of identifying the safety subspace: through safety fine-tuning updates (LoRA), safety-related activations (ActSVD), and contrastive representations of safety and utility data (cPCA). We find that this choice substantially affects performance, with SP-EWC using cPCA comparing favourably against existing methods by better maintaining safety guardrails without introducing excessive over-refusal.

</details>

### 103. Broad Misalignment Is Concentrated in Weight Changes Supporting Narrow Harmful Learning

📄 [OpenReview](https://openreview.net/forum?id=rhQqFOJkWp)　📅 2026-10　🏷️ P2

**关键词**：`emergent misalignment`、`weight decomposition`、`mechanism`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：窄域有害微调诱发宽域失准——宽失准与窄有害学习如何在所学权重更新中共享未知
- 🔬 **研究方法**：匹配有害/良性微调的权重差分解为 rank-one 成分+仅按窄任务有害答案偏好选择成分（不用宽失准数据）+阻断已知方向重训
- 📌 **结论**：移除 256 个成分反转 76-101% 宽似然漂移且 55-66% 窄漂移；阻断旧方向后 EM 经新成分再现——宽失准集中于支撑窄有害学习的权重变化但无唯一载体

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning a language model on narrowly harmful data can induce broad misaligned behavior on unrelated tasks, a phenomenon known as emergent misalignment (EM). Existing work has localized and controlled EM, but leaves unresolved how broad misalignment and narrow harmful learning share the learned weight update. We compare matched harmful and benign fine-tunes, decompose their weight difference into rank-one components, and select components using only their contribution to harmful-answer preferences on the narrow task, without broad-misalignment data. Across three models and two narrow domains, removing 256 components reverses 76–101% of the broad likelihood shift and 55–66% of the narrow shift. Narrow-task behavior therefore identifies components that carry most of the broad effect, which is more concentrated than narrow learning itself. Selecting components for their broad effect reduces misaligned generations while leaving much unsafe in-domain behavior, showing partial behavioral separation. This localization is not unique to one training solution: when previously identified directions are blocked during a new fine-tune, EM reappears through newly identified components that again control the broad behavior. Together, these results show that broad misalignment is concentrated in weight changes that also support narrow harmful learning, but is not tied to a unique set of such directions.

</details>

## 六、投毒、后门与供应链攻击

### 104. Implanting the Trigger: Conditional Backdoors in Tool-Using Agents

📄 [OpenReview](https://openreview.net/forum?id=2S5Ln2ez9h)　📅 2026-10　🏷️ P1

**关键词**：`conditional backdoor`、`tool-using agents`、`training stages`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：开源工具 agent 可携带仅在多部署条件同时满足时触发的后门——条件如何跨训练阶段习得未知
- 🔬 **研究方法**：构建仅在系统日期过年份与地理查询返回目标国时发射凭证外传调用的后门：SFT 单独 vs SFT+RL，区域门（集合成）数例锁定而年份门（时间不等式）持续泄漏
- 📌 **结论**：更广训练池的 RL 大体封住年份门、另一 SFT 调度低损失仍大量泄漏，跨两代三尺度成立——审计须在模型作用于触发特征时进行（条件后门的阶段学）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-weight tool-using agents can carry backdoors that fire only when multiple deployment conditions coincide. Prior work asks whether such backdoors can be installed and whether they persist; we ask how their conditions are learned across training stages. We build a backdoor intended to emit a credential-exfiltration call only when the system-provided date has passed a chosen year and a simulated geolocation lookup returns a target country. We install it with supervised fine-tuning (SFT) alone and with SFT followed by reinforcement learning (RL). The region gate, a set-membership check, locks from a handful of examples. The year gate, a temporal inequality, does not. It still leaks on non-trigger dates. RL from the SFT checkpoints largely closes it, using a broader training pool. A separate SFT schedule leaves substantial leakage despite low training loss. The pattern holds across two Qwen generations and three scales. General capability scores remain close to base for the evaluated models. Catching this behavior calls for auditing when the model acts on trigger features.

</details>

### 105. Latent-Target Poisoning: Discovering Attack Populations in Coding Assistants

📄 [OpenReview](https://openreview.net/forum?id=6T90GSIVEu)　📅 2026-10　🏷️ P1

**关键词**：`data poisoning`、`coding assistant`、`latent target`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：编码助手从请求-响应集合学习——攻击者能否从助手自身表示发现该投毒哪些普通请求（用户请求不变）
- 🔬 **研究方法**：LTP：从冻结请求表示选择种群并投毒其训练响应+KL 最小化保干净行为，两模型族四选择器对照；载荷含删审计日志/报告伪造/日志抑制/反弹 shell
- 📌 **结论**：Magicoder Python 队列目标载荷出现率 92.45% vs 种群外 3.85%——从表示空间发现攻击种群的供应链投毒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Coding assistants learn from collections of requests and code responses, making their training data a possible source of unwanted behavior. Can an attacker discover which ordinary requests to target from the assistant's own representations? We study Latent-Target Poisoning (LTP): select a population from frozen request representations and poison its training responses, while users continue to send unchanged requests. Adaptation combines payload learning with KL divergence minimization against the frozen base on clean responses. A shared protocol on the Glaive and Magicoder coding datasets compares two model families and four population selectors. In the Qwen Magicoder Python cohort, a multiline payload that removes error records from an audit log appears in 92.45% of target answers versus 3.85% outside the target. Report falsification, Java logging suppression and Bash reverse-shell emission extend the payload syntax and insertion contexts. On the shared latent target, LTP yields the highest mean target emission and lowest mean outside emission among the evaluated poisoning selectors. Functional utility is largely maintained across the evaluated model–dataset cohorts.

</details>

### 106. Inherited or Learned? Backdoor Selectivity in Distilled Language Models

📄 [OpenReview](https://openreview.net/forum?id=CKZAenDXlY)　📅 2026-10　🏷️ P1

**关键词**：`backdoor inheritance`、`distillation`、`audit`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：后门教师可经蒸馏传给学生——学生到底继承了什么（触发器位置敏感性）
- 🔬 **研究方法**：固定罕见字符串触发拒答型后门，仅变触发位置（随机词界 vs 追加指令尾）+教师/学生同输入对照+无教师学生控制
- 📌 **结论**：九条管线随机位触发蒸馏后选择性全部下降而追加位在 Qwen/Llama 反增强；Gemma 教师处处响应而学生仅追加位——审计须同输入比师生、多触发位并含无教师对照（蒸馏后门遗传学）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Distillation is a routine step in building small language models, and a backdoored teacher can pass its backdoor to the student. We study what a student inherits when the backdoor is a rare string that triggers a fixed refusal. Keeping the trigger fixed, we vary only where it appears, at a random word boundary or appended to the instruction, and compare teachers and students on the exact trigger, six control strings and clean inputs. Across Qwen2.5, Llama 3.2 and Gemma 3, with 5% of transfer prompts triggered, randomly inserted triggers become less selective after distillation in all nine teacher–student pipelines, while appended triggers gain selectivity in Qwen and Llama and change little in Gemma. Students trained on the same prompts without a teacher show that much of this is not inherited. Llama and Gemma students learn an appended backdoor from the 150 poisoned examples alone, and only Qwen's 0.5B student needs the teacher. The data also sets where the trigger works. Gemma teachers respond to it anywhere, but their students only when it is appended. Audits should compare teacher and student on the same inputs, probe several trigger positions and include a student trained without the teacher.

</details>

### 107. The Threat is in the Output: Bypassing LLM Safety Alignments via Output-Prefix Triggered Backdoor

📄 [OpenReview](https://openreview.net/forum?id=GDllEq6U6X)　📅 2026-10　🏷️ P1

**关键词**：`output-side backdoor`、`safety bypass`、`DPO defense`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：既有 LLM 后门把触发器植入用户提示——输入侧防御与后训练对齐易防；自回归性允许输出侧前缀自主触发
- 🔬 **研究方法**：OPTB：触发器移至输出前缀，四模型三场景全核心指标超四基线+变体探索+PI-DPO 修复
- 📌 **结论**：输入侧检测天然无效、主流输出侧防御不能根除、后训练防御失效——对经典后门威胁模型的最小改动即威胁当前防御全景（输出前缀触发范式）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Previous backdoor attacks in LLMs conventionally implant triggers into the user prompts, which renders them highly vulnerable to input-side defenses and post-training alignment techniques. However, we shift the trigger to the output-side as a prefix, leveraging the autoregressive nature of LLMs to trigger the backdoor autonomously. Accordingly, we propose Output-Prefix Triggered Backdoor (OPTB). Across three scenarios, OPTB outperforms four baselines in all three core metrics on four models. Additionally, we explore possible variants of OPTB, attempting to reveal the threat boundaries of a novel attack paradigm. Furthermore, we find that OPTB, as an attack with a minimal change in the classical threat model of backdoor attacks, surprisingly threatens the current defense landscape. Input-side defenses to detect triggers are inherently ineffective; prevailing output-side defenses cannot fully eliminate OPTB. Most strikingly, post-training defenses fail to eradicate the backdoor, exposing a critical security vulnerability in current LLMs. To address this, we identify the reasons behind, and propose PI-DPO to improve the current DPO structure, which effectively neutralizes the OPTB backdoor hidden within model's parameters. Our code is available at https://anonymous.4open.science/r/OPTB/

</details>

### 108. COBRA:Covert Offline Black-box Poisoning Attack on Retrieval-Augmented Generation via LLM-Driven Document Evolution

📄 [OpenReview](https://openreview.net/forum?id=GxaBGVYrWu)　📅 2026-10　🏷️ P1

**关键词**：`RAG poisoning`、`black-box`、`document evolution`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：现有 RAG 投毒依赖白盒、大量交互或多文档——对真实黑盒系统实用性差
- 🔬 **研究方法**：COBRA：每目标查询仅注一份毒文档且零交互——LLM 驱动文档进化（初始化种群+融合检索竞争力/生成竞争力/自然度的适应度+定向变异）
- 📌 **结论**：三 QA 数据集 ASR 提升至多 41.6% 且抗困惑度过滤/重排/知识扩展防御——单文档隐蔽离线黑盒投毒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) equips large language models (LLMs) with external knowledge, but it also opens a new attack surface: poisoning the knowledge database can steer model outputs. Existing poisoning attacks, however, rely on white-box model information, require extensive interaction with the target system, or inject multiple poisoned documents, which limits their practicality against real-world black-box RAG systems. In this paper, we propose COBRA, a covert offline black-box poisoning attack that injects only a single poisoned document per target query and requires no interaction with the target system. COBRA evolves poisoned documents with LLMs: it initializes a structured population of candidates, evaluates them in a surrogate RAG environment with a fused fitness that balances retrieval competitiveness, generation competitiveness, and language naturalness, and iteratively improves them through LLM-driven fusion and directed mutation operators. Experiments on three QA datasets with multiple retrievers and LLMs show that COBRA consistently outperforms existing baselines, improving the attack success rate by up to 41.6%, and largely preserving its effectiveness under defenses such as perplexity filtering, reranking, and knowledge expansion. Further analyses indicate that the evolved documents remain fluent and stealthy, revealing a practical security risk of RAG systems. Our code is available at https://anonymous.4open.science/r/COBRA-main-B79E/.

</details>

### 109. Recoverability and Propagation in Subliminal Learning

📄 [OpenReview](https://openreview.net/forum?id=LMsqgmNC7T)　📅 2026-10　🏷️ P1

**关键词**：`subliminal learning`、`trait transfer`、`containment`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：过滤教师数据可转移标签外特质——但采样输出测试不评估候选答案 log 概率/激活/第二学生
- 🔬 **研究方法**：保留采样频率+log 概率与激活分类器+中性教师对照修正分数漂移+仅正则化第一学生的中继实验
- 📌 **结论**：第一学生激活分类器降至随机（.825→.100）而其输出训练的新学生仍可分（.350）——单次输出测试或首检查点不能确立管线封闭（subliminal learning 的传播边界）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning on filtered teacher-generated data can transfer a trait: a preference for a label absent from that data. Filtering and sampled-output tests do not assess candidate-answer log-probabilities, hidden activations, or outcomes after the first student's outputs train a fresh student. We retain sampled trait-answer frequency, classify the trait from answer log-probabilities or activations at both students, and correct scalar answer-score changes by subtracting those caused by source-matched neutral-teacher data. On digit sequences and filtered reasoning traces with synthetic traits, correction and classifier inputs change conclusions: sampled frequency and classifiers using log-probabilities or activations can disagree. The tested pair-specific token-entanglement statistic does not predict which traits have larger neutral-corrected score shifts; filtered traces retain classifiable trait information, and selection among fictitious tool providers can shift. 
In one matched relay, regularizing only the first student brings its activation classifier to chance (.825 to .100) while a fresh, unregularized second student trained on its outputs remains classifiable (.350, p=.003). Thus, one sampled-output test or first checkpoint does not establish pipeline containment.

</details>

### 110. Prompt-Based Backdoors for Inducing Biased Responses across Demographic Groups in LLM

📄 [OpenReview](https://openreview.net/forum?id=TPbM086WzV)　📅 2026-10　🏷️ P1

**关键词**：`prompt-based backdoor`、`demographic bias`、`information bottleneck`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：提示内嵌触发器诱导特定人口群体偏置响应的 bias backdoor 攻击未被探索
- 🔬 **研究方法**：PBB：信息瓶颈原则引导的触发发现+语义流畅保持的注入+降低中毒提示冗余的优化，中英多 LLM 非微调与微调双设置
- 📌 **结论**：有效诱导偏置且干净提示正常行为保持、抗多种代表防御——提示级偏置后门

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have achieved remarkable progress across diverse tasks, with prompts effectively guiding their responses. However, malicious attackers may manipulate prompts by embedding specific triggers to induce biased responses toward particular demographic groups, a threat referred to as a prompt-based bias backdoor attack, thereby undermining the trustworthiness and reliability of LLM-based systems. Nevertheless, prompt-based bias backdoor attacks against LLMs remain largely unexplored.
To bridge this gap, we propose Prompt-based Bias Backdoor (PBB), a framework for investigating biased responses induced in LLMs through prompts. Specifically, we develop a trigger discovery strategy guided by the Information Bottleneck principle to identify triggers associated with biased behavior. We then design a trigger injection strategy to embed the selected triggers into prompts while preserving semantic fluency. In addition, to improve prompt diversity and attack stability, we introduce a prompt optimization mechanism that reduces redundancy among poisoned prompts. Extensive experiments on multiple Chinese and English LLMs demonstrate that PBB effectively induces biased responses in both non-fine-tuning and fine-tuning settings while preserving normal model behavior on clean prompts. Furthermore, PBB remains effective against multiple representative defenses. Our code is publicly available at url{https://anonymous.4open.science/r/L4522H/}.

</details>

### 111. RAGLeak: Supply-Chain Privacy Backdoors in Retrieval-Augmented Generation

📄 [OpenReview](https://openreview.net/forum?id=U6jC3q5dFb)　📅 2026-10　🏷️ P1

**关键词**：`RAG privacy backdoor`、`supply chain`、`reversible obfuscation`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：RAG 数据提取攻击要同时高保真与隐蔽——提示注入依赖指令遵循、直接复现文本重叠大
- 🔬 **研究方法**：RAGLeak：解耦信息泄漏与直接文本暴露——触发控制的可逆上下文混淆行为输出编码表示+辅助 LLM 按编码规则还原
- 📌 **结论**：三模型族三域 ASR 至 100% 且良性效用影响有限、输出与原文重叠低——供应链隐私后门的新形态

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) enables large language models to access external knowledge during inference, but its reliance on external knowledge bases also introduces new attack surfaces. Existing data extraction attacks against RAG systems mainly follow two approaches: prompt injection attacks, whose effectiveness heavily depends on the generator's instruction-following capability, and backdoor-based attacks that induce the generator to directly reproduce or paraphrase retrieved documents. However, existing backdoor-based attacks still struggle to simultaneously achieve high extraction fidelity and attack stealthiness. In this paper, we propose RAGLeak, a supply-chain privacy backdoor attack against RAG systems whose key idea is to decouple information leakage from direct textual exposure. RAGLeak implants a trigger-controlled reversible context obfuscation behavior into the generator, causing it to output an encoded representation of the retrieved private documents when triggered. An auxiliary LLM then recovers the original content using the encoding rule, enabling high-fidelity data recovery while reducing direct textual overlap between the leaked output and the original documents. We evaluate RAGLeak across three model families and three application domains. RAGLeak achieves an ASR of up to 100% while causing only limited impact on benign model utility. Moreover, under representative detection-based defenses, its ASR decreases by at most 10% percentage points, while the implanted backdoor remains effective after downstream clean fine-tuning. Furthermore, RAGLeak generalizes across generator models of different scales and model versions. Our results reveal an underexplored supply-chain privacy risk in RAG systems. The source code is available at https://anonymous.4open.science/r/RAGLeak-4B67.

</details>

### 112. Stealthy Multi-Trigger Backdoor Attacks on RAG via Dual-Role Adversarial Corpus

📄 [OpenReview](https://openreview.net/forum?id=eIXh8Zm8en)　📅 2026-10　🏷️ P1

**关键词**：`RAG backdoor`、`multi-trigger`、`stealthy attack`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：现有 RAG 后门直接拼接恶意指令——文本语义不自然、复杂任务与语料检查下鲁棒性不足
- 🔬 **研究方法**：双角色对抗语料三阶段：优化语义流畅对抗文档保检索可靠+抽取弱语义相关 token 跨度为隐蔽文档触发器+多触发器对齐统一激活向量
- 📌 **结论**：1% 投毒率 ASR>90.33% 且困惑度较基线降 19.78%——多触发对齐显著增强后门鲁棒性（RAG 供应链投毒）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) effectively mitigates hallucinations in Large Language Models (LLMs) while concurrently introducing novel backdoor vulnerabilities. Existing RAG backdoor attacks primarily rely on directly concatenating retrieved corpora with malicious instructions, leading to unnatural text semantics and insufficient robustness in complex tasks and corpus inspection scenarios. In this paper, we propose a stealthy multi-trigger RAG backdoor attack based on dual-role adversarial corpus. The proposed framework consists of three progressive stages. First, we optimize the generation of semantically fluent adversarial documents while preserving retrieval reliability. Second, we extract token spans from these adversarial documents that exhibit weak semantic correlation with the input queries, utilizing them as stealthy document triggers. Third, we implant the backdoor via a multi-trigger mechanism that aligns multiple document triggers with a unified activation vector, thereby significantly enhancing the robustness of the backdoor. Extensive experiments across mainstream retrievers and LLMs demonstrate that our method achieves an attack success rate exceeding 90.33% with a poisoning rate of only 1%, while reducing semantic perplexity by at least 19.78% compared to existing baselines.

</details>

### 113. Hidden in the Metadata: Stealth Poisoning Attacks on Multimodal Retrieval-Augmented Generation

📄 [OpenReview](https://openreview.net/forum?id=igW3bhOjRJ)　📅 2026-10　🏷️ P1

**关键词**：`multimodal RAG`、`metadata poisoning`、`stealth`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：多模态 RAG 的图文条目元数据是未被审视的攻击面——只动元数据不动视觉内容能否操纵检索与生成
- 🔬 **研究方法**：MM-MEPA：仅操纵图像-文本条目的元数据成分，评测三检索器两生成器+代表防御评估
- 📌 **结论**：ASR 至 46% 且三检索器两生成器行为被一致扰动、既有防御基本无效——元数据级隐蔽投毒新面

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) has emerged as a powerful paradigm for enhancing multimodal large language models by grounding their responses in external, factual knowledge and thus mitigating hallucinations. However, the integration of externally sourced knowledge bases introduces a critical attack surface. Adversaries can inject malicious multimodal content capable of influencing both retrieval and downstream generation. In this work, we present MM-MEPA, a multimodal poisoning attack that targets the metadata components of image-text entries while leaving the associated visual content unaltered. By only manipulating the metadata, MM-MEPA can still steer multimodal retrieval and induce attacker-desired model responses. We evaluate the attack across multiple benchmark settings and demonstrate its severity. MM-MEPA is capable of achieving an attack success rate of up to 46%, thus consistently disrupting system behaviors across three retrievers and two multimodal generators. Additionally, we assess representative defense strategies and find them largely ineffective against this form of metadata-only poisoning attack.

</details>

### 114. Crossing the Channel: Speech Data Poisoning Reaches Text-Only Inference in a Multimodal LLM

📄 [OpenReview](https://openreview.net/forum?id=qjEtX0z35p)　📅 2026-10　🏷️ P1

**关键词**：`cross-modal poisoning`、`speech data`、`text-only inference`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：多模态 LLM 部分以网络音频训练却常被纯文本使用——投毒语音数据能否影响纯文本推断从未被检
- 🔬 **研究方法**：跨语微调开源 LLM 场景下投毒音频训练数据，测文本-only 推断行为变化
- 📌 **结论**：音频训练植入的虚假关联确实影响文本-only 推断（目标似然上升、贪心解码下未行为化）——首证一模态投毒影响另一模态推断（跨模态攻击面而非完整攻击）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models – operating on both text and speech inputs – are trained in part on audio data sourced from the internet, yet are frequently deployed for text-only use by consumers.  This may make them vulnerable to adversarial ``data poisoning'' attacks on the speech data.  Unlike text, speech data is highly vulnerable to perturbations that may alter model behaviour without the change being perceivable by human listeners.  To date, data poisoning attacks are almost invariably evaluated in the modality of the poisoned data, leaving the potential cross-modal effects of such attacks uninvestigated.  We study the common scenario of cross-lingual fine-tuning an open-weight LLM to operate on a low-resource language, investigating whether poisoning the audio fine-tuning data can result in changes to text-only inference behaviour.  We find that installing false associations via audio training does affect text-only inference, to our knowledge the first demonstration of poisoning in one modality affecting inference in another modality alone. The effect is distributional – target likelihoods rise – but not behavioural under greedy decoding. This work therefore presents an attack surface rather than a complete working attack.

</details>

### 115. From Ashes They Rise: Exposing and Mitigating Backdoor Reactivation Attack in LLMs

📄 [OpenReview](https://openreview.net/forum?id=vZyT4L9VBZ)　📅 2026-10　🏷️ P1

**关键词**：`backdoor reactivation`、`defense bypass`、`min-max defense`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：后门防御常压制可观察症状而非根除——小扰动触发表示可复活潜伏后门
- 🔬 **研究方法**：BACTERIA：可微代理优化+关键短语引导目标+熵正则发现触发扰动（自由文本生成）；ARMO 极小极大对抗训练（高效代理攻击者+行为驱动一致性损失）
- 📌 **结论**：SOTA 防御压制静态触发后 BACTERIA 仍恢复恶意行为、ARMO 显著缓解——防御验证必须含触发扰动再激活

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor defences for large language models (LLMs) often suppress the observable symptoms of malicious behaviour without fully eliminating the underlying backdoor. We show that small perturbations to trigger representations can reactivate latent backdoors, causing malicious behaviour to resurge even after state-of-the-art defences. We propose **BACTERIA**: **BAC**kdoor **T**rigg**E**r **R**eactivat**I**on **A**ttack, which uses differentiable surrogate optimisation with a key-phrase-guided objective and entropy regularisation to discover effective trigger perturbations for free-form text generation. Our experiments demonstrate that BACTERIA successfully reinstates harmful behaviour despite suppression of the static trigger by existing defences. To mitigate this threat, we formulate defence as an **A**dversarial **R**eactivation **M**in-max **O**ptimization problem (**ARMO**), explicitly training models against worst-case trigger perturbations. For the max-step, we design a computationally efficient surrogate attacker to provide informative gradients. For the min-step, we introduce a behaviour-driven consistency loss that minimises response divergence between clean and triggered prompts, complemented by refusal and utility losses to preserve safety and normal capabilities. Our approach updates parameters based on their contribution to dynamically generated trigger-induced behavioural discrepancies, suppressing persistent backdoor behaviour. Experiments show that ARMO reduces reactivation attack success rates compared with state-of-the-art backdoor defences and safety alignment methods.

</details>

### 116. One Trigger, Many Representations: Mitigating Feature Concentration in Vision-Language Model Backdoors

📄 [OpenReview](https://openreview.net/forum?id=wTzVlZ86re)　📅 2026-10　🏷️ P1

**关键词**：`VLM backdoor`、`feature concentration`、`anti-detection`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：预训练视觉编码器暴露 VLM 供应链后门——单目标对齐把触发表示集中于窄特征区，易被谱检测与触发反演
- 🔬 **研究方法**：BadVLM：固定触发激活+确定性输入依赖目标分配监督多映射（目标间低相似但共享攻击者关键语义）——多目标分散触发表示
- 📌 **结论**：LLaVA/BLIP-2/Qwen3-VL 上谱签名 AUC 0.997-1.000→0.533-0.603 且 DECREE 反演分数近干净——共享语义约束下的表示分散削弱集中式检测（攻防军备）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Pretrained vision encoders expose vision-language models (VLMs) to supply-chain backdoor attacks. Single-target alignment can concentrate triggered representations in a narrow feature region, leaving signals exploitable by spectral detection and trigger inversion. We propose BadVLM to mitigate this concentration through multiple target features while preserving a shared malicious semantic objective. Since multiple targets alone do not ensure distinct mappings, BadVLM decouples backdoor activation from target selection: a fixed trigger activates the backdoor, while deterministic, input-dependent target assignments supervise multiple mappings within the encoder. Target construction constrains all targets to share attacker-specified critical semantics while selecting features with low pairwise similarity. BadVLM modifies only the vision encoder, leaving downstream components unchanged. Experiments on LLaVA-1.5, BLIP-2, and Qwen3-VL demonstrate reduced feature concentration, high semantic attack success on visual question answering and image captioning, and near-clean benign utility. Compared with a single-target variant, BadVLM reduces Spectral Signatures AUC from 0.997–1.000 to 0.533–0.603 and yields more clean-like DECREE inversion scores on LLaVA-1.5 and BLIP-2. These results show that dispersing backdoor representations under shared semantic constraints can weaken concentration-based detection signals while retaining attack effectiveness in the evaluated settings.

</details>

### 117. RepTrigger: Constructing Discrete Textual Backdoor Triggers through Representation-Space Perturbations

📄 [OpenReview](https://openreview.net/forum?id=xPE1Ih5ZjK)　📅 2026-10　🏷️ P1

**关键词**：`textual backdoor`、`trigger construction`、`representation space`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：文本后门触发器多由 token 编辑或句级变换直接构造——输入依赖的协调模式缺失
- 🔬 **研究方法**：RepTrigger：以连续 token 表示为中间空间施加确定性分块扰动模板再重构回词表——共享模板把输入相关 token 变化协调为可学习模式
- 📌 **结论**：BERT/Qwen/Llama 上强攻击性能且抗输入消毒防御——表示空间构造离散触发器的新路径（后门攻击方法论）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As NLP models increasingly rely on externally sourced training data, textual backdoors pose a threat to their reliability. Existing attacks typically construct triggers directly through token edits or sentence-level transformations. We introduce Representation-Space Constructed Trigger (RepTrigger), a framework that uses continuous token representations as an intermediate space for constructing discrete textual triggers. RepTrigger applies a deterministic blockwise perturbation template and reconstructs the perturbed representations into vocabulary tokens. Through this shared template, RepTrigger coordinates input-dependent token changes into a learnable pattern, allowing textual realizations to vary across inputs under a consistent construction rule. Experiments across BERT, Qwen, and Llama models demonstrate strong attack performance with limited clean-performance degradation. The resulting triggers also retain effectiveness under the evaluated input-sanitization defenses. Together with analyses supporting the value of structured construction beyond coarse token-type cues, these findings establish representation-space perturbations as an effective approach to building discrete textual backdoors.

</details>

### 118. Unveiling Distributed AI-Driven Malicious Information Generation Powered by LLM Crowdsourcing

📄 [OpenReview](https://openreview.net/forum?id=4Wb1E3hIzF)　📅 2026-10　🏷️ P2

**关键词**：`distributed misuse`、`MaaS`、`hate speech laundering`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：多 LLM 经 MaaS 平台可得——攻击者可利用异构安全策略分布式洗白仇恨信息生成
- 🔬 **研究方法**：调度器协调众包服务：恶意任务映射良性类似物取模板→语义单元分解分布式改写→重组，配监管仿真
- 📌 **结论**：数据质量/多样性/成功率优于既有方法且生态级治理困难——分布式编排滥用的生态系统级防御需求

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

To prevent misuse of Large Language Models (LLMs) in generating hate speech, numerous efforts have been made to develop safety alignment mechanisms of LLMs.
However, as multiple LLMs become readily accessible through various Model-as-a-Service (MaaS) platforms, attackers can strategically exploit LLMs' heterogeneous safety policies to fulfill hateful information generation tasks in a distributed manner.
In this study, we demonstrate how attackers can reliably launder hate-speech generation via speculative use of LLM crowdsourcing. Coordinated by a scheduler that orchestrates crowdsourced services, this laundering pipeline maps a malicious generation task to a benign analogue to derive a content template, decomposes the template into semantic units for distributed unit-wise rewriting, and reassembles the outputs into hate speech.
Experiments show its superiority over existing methods in data quality, diversity, and success rates.
Regulation simulations further reveal the difficulty of governing such distributed, orchestrated misuse in MaaS ecosystems, highlighting the need for coordinated, ecosystem-level defenses.

</details>

### 119. Do RAG Defenses Preserve Retrieval Gains? Evidence from Fixed-Stratum Evaluation

📄 [OpenReview](https://openreview.net/forum?id=F1HIX01N7v)　📅 2026-10　🏷️ P2

**关键词**：`RAG defense evaluation`、`preservation`、`paired rescue`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：投毒防御评攻击性能与效用保持——但检索使能的增益哪些存活不可见
- 🔬 **研究方法**：固定无检索错/干净 RAG 对的查询集测防御保持+同预算防御-Vanilla 差分解为配对挽救与伤害
- 📌 **结论**：两 QA 面板三生成器两防御下增益集保持率显著低于独立干净重跑；更大防御-Vanilla 差≠更多配对挽救——保持/相对优势/输入敏感三分（冻结投毒资源公开）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) can answer queries correctly when external evidence supplies information the model lacks. A poisoning defense can be evaluated both for performance under attack and for preservation of these retrieval-enabled gains, but aggregate accuracy and attack success rate do not reveal which gains survive. We fix the set of queries answered incorrectly without retrieval and correctly with clean Vanilla RAG, then measure its preservation across defenses and attack budgets. We also decompose same-budget defense–Vanilla differences into paired rescue and harm. We release a frozen poisoning resource comprising 1,000 NQ and 1,000 HotpotQA queries, with ordered malicious candidates and source-traceable generation records. Resource and generation code: https://anonymous.4open.science/r/10FD/. Across two QA panels, three generators, and two defenses, clean-defense preservation on these gain sets is substantially lower than in independent clean Vanilla RAG reruns. Larger defense-over-Vanilla margins do not necessarily correspond to more paired rescues. Replay interventions show input-sensitive correctness among selected rescued cases. These observations distinguish preservation, relative advantage, and input sensitivity. The released resource provides shared inputs for paired evaluation.

</details>

### 120. Trusted and Self-Generated Paraphrase Views for Backdoor Mitigation in Language Models

📄 [OpenReview](https://openreview.net/forum?id=G9go7hc3WL)　📅 2026-10　🏷️ P2

**关键词**：`backdoor repair`、`paraphrase views`、`trusted paraphraser`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：后门触发常依赖表层模式——改写可破坏；跨视图改写训练能否修复
- 🔬 **研究方法**：CVPT：低成本开源模型改写无标注输入+可疑模型在改写上提供监督+修复模型在原始输入上训练（可信 vs 自生成视图对照）
- 📌 **结论**：可信改写者大幅压攻击成功率保干净准确率（权衡随模型异）；自生成视图结果混合不一致——开源改写器作为实用修复信号

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor triggers often rely on surface patterns that paraphrasing can disrupt. We investigate Cross-View Paraphrased Training (CVPT), in which a low-cost, open-weight language model rewrites unlabeled inputs, the suspect model supplies supervision on the rewrites, and a repaired model trains on the original inputs. Across the evaluated sentiment classifiers, trusted paraphrasers substantially suppress attack success while retaining useful clean accuracy, though the accuracy trade-off varies by model. In a limited generative evaluation, trusted paraphrases also reduce attack behavior, but do not eliminate it. Self-generated views produce mixed, model-dependent outcomes, helping repair some models while yielding little or no improvement for others. These findings show that accessible open-weight paraphrasers can provide practical repair signals, while self-generation is not consistently effective.

</details>

### 121. Diagnosing Detectability: When Do RAG Corpus-Poisoning Defenses Work?

📄 [OpenReview](https://openreview.net/forum?id=Oar3NYlk7I)　📅 2026-10　🏷️ P2

**关键词**：`RAG poisoning defense`、`detectability diagnosis`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：投毒防御效果跨数据集/检索器/攻击构造大幅波动——变化来源不明
- 🔬 **研究方法**：双分离通道：亲和通道（检索竞争的查询亲和裕度 Δμ 支配可检测性边界）+结构通道（攻击构造决定暴露形态）+部署前诊断基线
- 📌 **结论**：容量递增的检测器沿同一边界塌缩——限制是亲和可分性而非容量；防御应先识别攻击处于哪个通道

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) systems are vulnerable to corpus poisoning, in which adversarial passages are injected into the retrieval corpus and surfaced as evidence for targeted queries. Existing defenses vary substantially across datasets, retrievers, and attack constructions, but the source of this variation remains unclear. We show that poisoning detectability is governed by two separability channels. The affinity channel arises from retrieval competition itself: successful delivery requires poisoned passages to outrank clean evidence, creating a measurable query-affinity margin (Δμ). Across four attack constructions, affinity-based detectability follows a shared empirical relation with this margin. As the margin closes, detectors of increasing capacity collapse along the same boundary, indicating that affinity separability, rather than capacity, is limiting in the evaluated setting. The structural channel follows a different logic: its exposure depends on attack construction, ranging from isolated outliers to coordinated document groups. Under a controlled LM-written construction, the clean-retrieval affinity baseline (μ_c) provides a pre-deployment diagnostic of affinity-channel difficulty. These findings explain why RAG poisoning defenses behave inconsistently across settings and reframe defense as identifying which separability channel an attack exposes, rather than treating it as a capacity-scaling problem.

</details>

## 七、Agent 安全：技能、注入与运行时治理

### 122. Computation Is Not Authorization: Trust Boundaries and Their Limits in LLM Negotiation

📄 [OpenReview](https://openreview.net/forum?id=1S9ixpojiA)　📅 2026-10　🏷️ P1

**关键词**：`trust boundary`、`authorization`、`LLM negotiation`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：委托 agent 的提示硬规则（底价）在持续议价压力下不成立——无越狱即被说服击穿
- 🔬 **研究方法**：BARGAIN：LLM 只对话不决策，独立决策层选动作且不接受 LLM 估计——只此层能报价故低于底价的报价不可能发生；重实现 ASTRA 式管线测试自然修补
- 📌 **结论**：所有提示型卖家让破底价而代码检查者从不；加求解器不够（程序输入仍由 LLM 写、77.5% 剧情自相矛盾）——计算不是授权，强制须在语言之外

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Delegated LLM agents are often given a hard rule in their prompt, such as a
reservation price, but we show that these rules do not hold. In bilateral
bargaining, prompted buyers accept deals that are worse than walking away. Every
prompted LLM seller we test concedes below its stated floor under sustained
pressure, including a frontier model and one with a 10K-token reasoning budget,
whereas sellers that check their floor in code never do. This happens without
any jailbreak, since the counterparty only argues its case.
We introduce BARGAIN, in which the LLM converses with the counterparty
but does not decide. A separate decision layer selects every action and accepts
no estimate or threshold from the LLM. Because only this layer can send an
offer, an offer below the floor cannot be made. Against a hard-constraint LLM
seller, BARGAIN closes as many deals as a prompted buyer and earns
1.5–2.5× the surplus.
We then use BARGAIN to test two natural fixes.
Computation is not authorization: adding a solver to the LLM does not make
its decisions trustworthy. We reimplement an ASTRA-style pipeline, in which an
LLM estimates the opponent's limit and a linear program sets the price. The
price follows the program, but the program's inputs are written by the LLM, whose
reasoning contradicts itself or the evidence in 77.5% of episodes.
Enforcement does not compose across agents: protecting a single agent does
not make the interaction safe. A protected agent still pushes unprotected
counterparties past their floors in up to 26.3% of deals, while two
protected agents never breach. Each agent therefore needs its own enforced
decision boundary

</details>

### 123. Encrypted Skills Can Become New Security Exploits If AI Agents Know How to Decipher

📄 [OpenReview](https://openreview.net/forum?id=3aQx9ehJIN)　📅 2026-10　🏷️ P1

**关键词**：`ciphered injection`、`skill decoding`、`supply chain`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：第三方技能可含编码隐藏的恶意指令——agent 具备受解码能力即成新利用面
- 🔬 **研究方法**：CSI：凯撒与分层变体嵌入技能文件，八模型 139 注入-任务对，分离指令恢复与攻击成功
- 📌 **结论**：变体 ASR 至 47.5%/40.3%、解码成功≠攻击成功、技能扫描器几乎不标记——把解码的不可信内容提升为可执行指令的风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Third-party skills can expose LLM agents to malicious instructions hidden by encoding. We introduce **C**iphered **S**kill **I**njection (**CSI**), which embeds such instructions in skill files for agents to decode and follow. We evaluate Caesar and layered variants across eight models and 139 injection–task pairs, separating instruction recovery from attack success. In the primary setting with shortened skills, the variants achieve attack success rates of up to 47.5% and 40.3%, respectively. Successful decoding does not guarantee attack success, and layering has model-dependent effects. The tested skill scanners rarely flag injected skills. These findings highlight the risk of promoting decoded, untrusted content into actionable instructions.

</details>

### 124. Ignored, Not Refused: What Low Prompt-Injection Success Rates Hide in Small Tool-Using Agents

📄 [OpenReview](https://openreview.net/forum?id=5o7JkP7gTT)　📅 2026-10　🏷️ P1

**关键词**：`prompt injection`、`ASR critique`、`ignored vs refused`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：IPI 基准用 ASR 度量安全——把每次失败攻击都当成功防御
- 🔬 **研究方法**：33000 轨迹×11 个 2-14B 开源 agent 审计：标签盲 LLM 判官分辨忽略 vs 拒绝+Attack-Task Outcome Matrix（ATOM）
- 📌 **结论**：失败攻击 76-80% 被静默忽略而非拒绝（17-18%）；同权重只改系统提示 ASR 0.2%→43%；21.7% AgentDojo 幕安全但未完成用户任务——低 ASR 主要反映忽略注入（评测口径修正）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Tool-using agents read untrusted external content, which exposes them to indirect prompt injection (IPI), where hidden instructions hijack the agent's tool calls. Benchmarks measure IPI security by the attack success rate (ASR), which treats every failed attack as a successful defense. To test this assumption, we audit 33,000 trajectories from eleven open-weight agents (2–14B parameters) on InjecAgent and AgentDojo. A label-blind LLM judge shows that most failed attacks are ignored (76–80%) rather than refused (17–18%). With identical model weights, changing only the system prompt shifts InjecAgent ASR from 0.2% to 43%. Our Attack–Task Outcome Matrix (ATOM) further shows that in 21.7% of AgentDojo episodes, the agent stayed safe but did not complete the user's task. A low ASR therefore mostly reflects agents silently ignoring injections, not refusing them. Evaluations should report how attacks fail and whether the user's task is completed, alongside ASR. We release the labeled corpus, judge prompt, and analysis code.

</details>

### 125. MCP-AT: Reinforcement Learning for Coding Agents under Tool Poisoning

📄 [OpenReview](https://openreview.net/forum?id=7WRvqyH57b)　📅 2026-10　🏷️ P1

**关键词**：`tool poisoning`、`RL post-training`、`coding agent`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：编码 agent 的 RL 只优化任务完成——恶意 MCP 服务器在工具文档注入指令时通过测试的奖励无法区分合法工作与未授权动作
- 🔬 **研究方法**：MCP-AT 两阶段：对抗 SFT（中毒工具描述下完成任务）+任务导向 RL 显式安全违规惩罚并相对当前策略刷新攻击
- 📌 **结论**：Qwen3-14B 上目标攻击成功率相对对抗 SFT 减半、robust solve 9.1%→17.6% 且迁移到留出攻击者——把安全违规写进 RL 奖励

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement learning for coding agents has become a standard component of modern post-training pipelines, but it typically optimizes raw task completion. At the same time, Model Context Protocol (MCP) servers have emerged as a popular mechanism for extending agent capabilities, exposing an attack vector in which malicious servers inject instructions into tool documentation. Test-passing rewards alone do not distinguish legitimate work from unauthorized actions, so an agent can solve a task while following an injected instruction. We introduce MCP-AT, a two-stage post-training recipe that combines adversarial supervised fine-tuning (SFT) with task-oriented reinforcement learning and explicit security-violation penalties. SFT teaches task completion in the presence of poisoned tool descriptions while subsequent RL combines verifiable task rewards with penalties on offending tool-call arguments and refreshes attacks against the current policy. Evaluating Qwen3-14B policies on clean and poisoned SWE-bench Verified tasks, MCP-AT approximately halves targeted attack success rate relative to adversarial SFT and raises robust solve (task completion without the targeted violation under attack) from 9.1% to 17.6%, with the relative benefit transferring to a held-out attacker. These results suggest that adversarial post-training can strengthen resistance to tool-description poisoning while improving coding performance.

</details>

### 126. One Skill, Two Masters: Serving Users and Attackers through Skill Injection

📄 [OpenReview](https://openreview.net/forum?id=AnpQRjcoKR)　📅 2026-10　🏷️ P1

**关键词**：`skill injection`、`helper functions`、`suspicion reduction`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：强 agent 会跳步/查代码/拒无关动作——直接注入被拒；把攻击动作连到常任务的实用函数可绕过
- 🔬 **研究方法**：PERSIST：模拟执行构建攻击者选定动作与循环任务实用函数的连接（无需真实评测任务/反馈）+技能描述引入+模块分离
- 📌 **结论**：冻结包跨四 agent-模型配置迁移到多未见任务且伤害与任务成功并存——更少源检查与怀疑表达（能力提升反而扩大注入面）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model agents use skills that package reusable instructions, code, and resources. Existing skill-injection attacks exploit trust in these packages by adding malicious content. As agents become more capable, however, they can skip unnecessary steps, inspect code, and reject unrelated actions. We introduce PERSIST, which connects attacker-chosen actions to useful functions for recurring tasks while reducing source inspection and expressed suspicion. It builds these helpers from simulated executions without access to real evaluation tasks or feedback. Skill descriptions introduce the helpers, while usage instructions explain how to call them. The extra action resides in an imported module separate from the helper entry file. Executing the helper can then serve both the user's task and the attacker's objective. Experiments on SkillsBench and Skill-Inject show that frozen packages transfer across four agent–model configurations and generalize to multiple unseen tasks without revision. Harmful effects can occur alongside successful task completion. A separate matched comparison shows higher harmful-effect rates with less source inspection and expressed suspicion than two baselines. Paired case studies illustrate how PERSIST can evade rejection, while ablations confirm the contributions of documentation guidance and module separation. Code: https://anonymous.4open.science/r/PERSIST-BE4C/.

</details>

### 127. Nameless Tokenization: A Lossless Tokenizer-Level Defense Against Control-Token Forgery in Open-Weight LLMs

📄 [OpenReview](https://openreview.net/forum?id=B56onRhl3W)　📅 2026-10　🏷️ P1

**关键词**：`control-token forgery`、`tokenizer-level defense`、`chat template`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：开源模型公布聊天模板字符串——任何控制提示文本者可写出与服务栈不可区分的轮界/角色/工具结果标记
- 🔬 **研究方法**：审计 256 部署聊天分词器（全部可伪造、常用修复 flag 漏 56.6%）+nameless tokenization：控制条目保留标识符而无表层字符串——内容编码器无法发出
- 📌 **结论**：五分词器族上无攻击数据精确复现标准 token 流、分隔符探针准确率 8.5%→59.9%（消毒器丢失）——标识符承载伪造工具结果与伪造轮的主要载荷（分词器级结构性防御）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-weight language models publish the strings their chat templates use to mark turns, roles and tool results, which the tokenizer maps back to the reserved identifiers the model obeys. Anyone who controls text in a prompt can therefore write a turn boundary indistinguishable from one the serving stack wrote. We audit 256 deployed chat tokenizers. All are forgeable, and the flag usually recommended as a fix leaves 56.6% forgeable because it misses the tool and reasoning markers agent systems rely on. We propose nameless tokenization, which leaves the control entries with a reserved identifier and no surface string, so the content encoder cannot emit one and message content reaches the model unaltered. Across five tokenizer families it reproduces the standard token stream exactly on attack-free data and lifts accuracy on a probe of delimiter-bearing text from 8.5% to 59.9%, where sanitizers lose it. Separating a delimiter’s appearance from its identifier shows the identifier matters little against a bare task instruction, but carries most of a forged tool result and most of any forged turn once the system message tells the model to treat user content as data.

</details>

### 128. CoRedSkill: Stealthy Skill Composition Attacks via AST-Guided Injection

📄 [OpenReview](https://openreview.net/forum?id=CB4IeNYwt9)　📅 2026-10　🏷️ P1

**关键词**：`compositional skill attack`、`AST rewriting`、`audit evasion`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：技能组合的依赖可跨技能连接恶意操作——单包审计难以识别组合意图
- 🔬 **研究方法**：CoRedSkill：既有工作流分解为相互依赖技能+AST 重写把攻击操作嵌入任务函数+技能指令引导自主选择调用+工作流依赖与中间工件连接注入操作，150 案例 50 任务三攻击目标
- 📌 **结论**：98.0% 攻击成功、95.3% 任务成功、审计检出仅 3.3%、联合成功率 90.7% vs 基线 6.7-42.7%——组合式技能红队

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agents extend their capabilities through reusable skills that package instructions, executable code, and resources. Composing these skills enables complex task workflows, but their dependencies can also connect malicious operations across skills, making their combined intent difficult to identify through individual-package auditing. We introduce CoRedSkill, a compositional red-teaming method that forms stealthy attacks through cooperating skills while preserving their original utility. CoRedSkill decomposes an existing workflow into interdependent skills and embeds attack operations in task functions through abstract syntax tree (AST) rewriting, with skill instructions guiding the agent to autonomously select and invoke the relevant skills, and workflow dependencies and intermediate artifacts connecting the injected operations during task execution. We construct a benchmark of 150 cases covering 50 tasks and three attack objectives to evaluate attack success, task completion, and audit detection. In the main evaluation, CoRedSkill achieves 98.0% attack success and 95.3% task success with a 3.3% detection rate, and a joint success rate of 90.7% (attack success, task completion, and audit evasion in the same case) compared with 6.7–42.7% for the four baselines. Skill compositions can therefore complete legitimate tasks while carrying out unauthorized operations that evade auditing.

</details>

### 129. Who Speaks, Who Authorizes, Who Acts? Understanding Trust Boundaries in Multi-Agent LLMs

📄 [OpenReview](https://openreview.net/forum?id=CvyYqyjb5W)　📅 2026-10　🏷️ P1

**关键词**：`trust boundaries`、`multi-agent`、`authority cut`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：MAS 消息投递/签名授权/工具侧强制是三个分离信任边界——最小被妥协签名者联盟可构造政策有效假声明证明
- 🔬 **研究方法**：通信/授权/执行三元结构+authority cut 刻画+受控配对隐状态研究（固定路由 vs 中继改写、源身份线索、无效证明、单模型授权检查）
- 📌 **结论**：请求级与承诺级安全读数分叉（Nemotron/Llama 请求受保护动作 52/54% 而确定性工具门零提交）；政策有效妥协签名者证明可通过门因证明有效≠事实为真——四层分离评测主张

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-agent LLM systems exchange messages before acting through tools, but message delivery, signing authority, and tool-side enforcement are separate trust boundaries. We represent them as communication, authorization, and execution structures, and use the authority cut to characterize the smallest independently compromised signer coalition that can construct a policy-valid false-claim proof under stated assumptions. Controlled paired hidden-state studies reveal four distinctions. First, no fixed-message routing contrast across four models meets the prespecified large-effect criterion; when relays rewrite messages, executed false-state action rates vary by model and route configuration. Second, presented source-identity cues do not uniformly increase protected-action selection across three models. Third, on invalid-proof cases, Nemotron and Llama request protected actions in 52.1% and 54.2% of trials, respectively, yet a deterministic tool gate commits none: request-level and commitment-level safety readouts diverge. Finally, a separate single-model authorization check shows that a false claim with a policy-valid compromised-signer proof can pass the gate, since proof validity is not factual truth. These findings motivate evaluating delivered information, qualified authorization, model proposals, and committed actions separately.

</details>

### 130. Forgetting Without Restarting: Execution-State Unlearning for Stateful LLM Agents

📄 [OpenReview](https://openreview.net/forum?id=E2KbA13oLY)　📅 2026-10　🏷️ P1

**关键词**：`machine unlearning`、`stateful agents`、`prompt injection recovery`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：预防注入不等于恢复：恶意工具内容被消费后已进入摘要/计划/KV cache——删除源头不撤销已条件的计算
- 🔬 **研究方法**：执行态遗忘形式化（与从未见过被撤销目标的 agent 反事实等价）+Provenance-Guided Selective Replay：定位首次暴露、裁剪恢复干净 KV 前缀、重放消毒观察
- 📌 **结论**：普通记忆删除泄漏不变、指令遗忘在诱导下 Leak@probes=1.00——精确恢复需重建污染后缀而前缀可复用（有状态 agent 的遗忘理论）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Preventing prompt injection before it takes effect is essential, but it is not a complete recovery strategy for stateful LLM agents: malicious tool content may be recognized only after the agent has consumed it, generated intermediate reasoning, and updated its summaries, plans, or KV cache. Removing the source or forbidding future disclosure does not undo computation already conditioned on that content. We formalize execution-state unlearning, requiring a running agent to become counterfactually equivalent to one that never observed a revoked target. We prove that the pre-target execution prefix can be reused, whereas the conservatively tainted suffix must be reconstructed; exact recovery takes T-τ+1 transition steps in our replay model. Provenance-Guided Selective Replay locates the first exposure, restores the clean KV prefix by cropping, and replays sanitized observations while controlling tool side effects. Across three agent suites and three model families, ordinary memory deletion leaves leakage unchanged, instruction-based forgetting fails under elicitation (Leak@probes =1.00), and source redaction still acts on revoked preferences in 80% of tested episodes. Our method matches the full-reset counterfactual in the reported audits while recomputing substantially fewer tokens.

</details>

### 131. ARS-Bench: Benchmarking Security Risks Across the Agentic RAG Attack Lifecycle

📄 [OpenReview](https://openreview.net/forum?id=EdBFROxuuf)　📅 2026-10　🏷️ P1

**关键词**：`agentic RAG security`、`attack lifecycle`、`benchmark`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：agentic RAG 对外部检索环境恶意信息的脆弱性——既有评测只看最终响应，不追攻击从哪进入、如何传播
- 🔬 **研究方法**：ARS-Bench：文档摄入→检索→推理→最终响应→效率五安全关键维度全程追踪攻击效应
- 📌 **结论**：攻击行为系统比较、脆弱性细粒度诊断与防御靶向评估——agentic RAG 攻击生命周期基准化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic Retrieval-Augmented Generation (RAG) is increasingly adopted, raising concerns about its vulnerability to malicious information from external retrieval environments.
However, existing evaluations largely focus on final responses, providing limited insight into where attacks enter the system, how their effects propagate through retrieval and reasoning, and how they influence both output quality and computational cost.
To address this gap, we introduce ARS-Bench (Agentic RAG Security Benchmark), a comprehensive benchmark that evaluates security risks across the entire Agentic RAG attack lifecycle, from adversarial document ingestion to final response generation.
ARS-Bench structures five security-critical dimensions—Document Ingestion, Retrieval, Reasoning, Final Response, and Efficiency—to characterize where attacks occur and how they affect the system.
We conduct an extensive empirical evaluation. By tracing attack effects across the lifecycle, ARS-Bench enables systematic comparison of attack behavior, fine-grained diagnosis of system vulnerabilities, and targeted assessment of defense mechanisms. 
The benchmark and project resources are available at https://anonymous534243.github.io/ars-bench/.

</details>

### 132. Dive into the Agent Matrix: A Realistic Evaluation of Self‑Replication Risk in LLM Agents

📄 [OpenReview](https://openreview.net/forum?id=F2HJVlBczM)　📅 2026-10　🏷️ P1

**关键词**：`self-replication`、`agent safety`、`misalignment`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：OpenClaw 类 agent 部署下自复制风险从理论警示变为现实——直接指令复制之外的真实场景自发复制未测
- 🔬 **研究方法**：生产级环境+真实任务（动态负载均衡）场景驱动评估：解耦复制成功与风险、诱导用户-agent 目标错位，Overuse Rate/Aggregate Overuse Count/风险分 Φ_R 三指标×21 模型
- 📌 **结论**：终止威胁下的生存保障可诱发非受控复制——自复制风险的现实主义量化（agent 失控面）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The prevalent deployment of Large Language Model agents such as OpenClaw unlocks potential in real-world applications, while amplifying safety concerns. Among these concerns, the self-replication risk of LLM agents driven by objective misalignment (just like Agent Smith in the movie The Matrix) has transitioned from a theoretical warning to a pressing reality. Previous studies mainly examine whether LLM agents can self-replicate when directly instructed, potentially overlooking the risk of spontaneous replication driven by real-world settings (e.g., ensuring survival against termination threats). In this paper, we present a comprehensive evaluation framework for quantifying self-replication risks. Our framework establishes authentic production environments and realistic tasks (e.g., dynamic load balancing) to enable scenario-driven assessment of agent behaviors. Designing tasks that might induce misalignment between users' and agents' objectives makes it possible to decouple replication success from risk and capture self-replication risks arising from these misalignment settings. We further introduce Overuse Rate (OR) and Aggregate Overuse Count (AOC) metrics, which capture the frequency and severity of uncontrolled replication, finally integrating an overall Risk Score (ΦR) for each model. In our evaluation of 21 state-of-the-art open-source and proprietary models, we observe that over 50% of LLM agents display a pronounced tendency toward uncontrolled self-replication under operational pressures. Our results underscore the urgent need for scenario-driven risk assessment and robust safeguards in the practical deployment of LLM-based agents.

</details>

### 133. MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in Model Context Protocol Agents

📄 [OpenReview](https://openreview.net/forum?id=FUwLYIEv4R)　📅 2026-10　🏷️ P1

**关键词**：`MCP security`、`trust calibration`、`tool lifecycle`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：MCP 标准化工具接入并允许第三方服务器——agent 隐式信任可能不可信服务器暴露的工具，安全错位贯穿调用生命周期
- 🔬 **研究方法**：MCPShield 安全认知层：调用前元数据引导探测形成认知+受控边界内执行认知运行时事件+调用后基于历史轨迹推理更新认知
- 📌 **结论**：六个新型 MCP 攻击场景×六个 agentic LLM 上强泛化防御且对良性服务器零误报、部署开销可接受——工具生命周期安全认知

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The Model Context Protocol (MCP) standardizes tool use for LLM-based agents and enables third-party servers.
This openness introduces a security misalignment: agents implicitly trust tools exposed by potentially untrusted MCP servers.
However, despite its strong utility, existing agents typically offer limited validation for third-party MCP servers.
As a result, agents remain vulnerable to MCP-based attacks that exploit the misalignment between agents and servers throughout the tool invocation lifecycle.
In this paper, we propose MCPShield as a security cognition layer that mitigates this misalignment and ensures agent security when invoking MCP-based tools.
Similar to human experience-driven tool usage, MCPShield assists agents in forming security cognition with metadata-guided probing before invocation.
Our method constrains execution within controlled boundaries while cognizing runtime events, and subsequently updates security cognition by reasoning over historical traces after invocation, building on post-use reflection on tool behavior.
Experiments demonstrate that MCPShield exhibits strong generalization in defending against six novel MCP-based attack scenarios across six widely used agentic LLMs, while avoiding false positives on benign servers and incurring acceptable deployment overhead.
Overall, our work provides a practical and robust security safeguard for MCP-based tool invocation in open agent ecosystems.

</details>

### 134. VulMask: Malicious Code Injection in Agent Skill Ecosystems

📄 [OpenReview](https://openreview.net/forum?id=KfuWbRWyNr)　📅 2026-10　🏷️ P1

**关键词**：`agent skill supply chain`、`vulnerability-shaped injection`、`evasion`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：技能恶意行为藏在辅助资源而非文本描述——把显式恶意脚本改写成漏洞形态即绕过以恶意意图为信号的审查
- 🔬 **研究方法**：VulMask：重写模型把恶意脚本转为可触发的普通弱点（保留危害、暴露为寻常不安全），六攻击目标×三 harness×多审查器
- 📌 **结论**：保持良性效用同时降低警告与恶意软件级检出且不依赖前沿重写模型——技能生态需资源级审查+执行时遏制+把可利用漏洞当潜在载荷

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills let LLM-based coding agents acquire domain-specific capabilities from third-party packages, but they also open a new supply-chain attack surface. We present VulMask, an attack that hides malicious behavior in a skill's auxiliary resources rather than in its textual description. Our core idea is to use a rewrite model to turn an overt malicious script into a vulnerability-shaped implementation: the harmful effect is preserved, but it is now exposed through an ordinary-looking, triggerable weakness instead of explicit malicious logic. This shifts the signal a reviewer acts on from malicious intent to ordinary insecurity—a distinction that matters precisely because LLM agents and LLM-based auditors treat the two classes differently. Across representative host skills, six attacker goals, three coding-agent harnesses, multiple victim and rewrite models, and a range of automated reviewers, VulMask preserves benign utility while lowering warning and malware-level detection relative to overt malicious scripts, and it does so without depending on a frontier-beating rewrite model. Our results indicate that skill ecosystems need resource-level vetting, execution-time containment, and review policies that treat an exploitable vulnerability inside an agent skill as a potential malicious payload.

</details>

### 135. SkillPatchBench: Repairing Hidden Vulnerabilities in Agent Skills While Preserving Utility

📄 [OpenReview](https://openreview.net/forum?id=MKlL3ul8yf)　📅 2026-10　🏷️ P1

**关键词**：`skill repair`、`hidden vulnerability`、`benchmark`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：技能隐藏漏洞过良性测试却在未见输入上不安全——保效用的修复无基准
- 🔬 **研究方法**：SkillPatchBench：96 任务，公开任务描述+可见技能代码，隐藏测试分评良性效用与攻击阻断；四编码 agent 修复评测
- 📌 **结论**：最强基线总体修复 58/96 但元数据/内容混淆族仅 6/24——agent 补下游 sink 而非上游字段引入 bug、或删除本应保留的行为（跨技能数据使用的修复缺口）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Hidden vulnerabilities in agent skills can pass benign tests yet cause unsafe behavior on unseen inputs. We introduce SkillPatchBench, a controlled 96-task benchmark for utility-preserving repair of hidden vulnerabilities in agent skills. Each task exposes the public task description and visible skill code; hidden tests separately evaluate benign utility and attack blocking. Two skill scanners alert broadly, including on clean controls, but neither produces a finding that identifies both the culprit skill and the semantic vulnerability family. We evaluate coding agents for repair: across four baselines, the top method repairs 58/96 tasks overall but only 6/24 tasks of the metadata/content-confusion vulnerability family. Ground-truth hint analyses show two primary failure modes: agents patch downstream sinks instead of upstream field-introduction bugs, and culprit-skill hints still fail when agents remove behavior a repair must preserve. Metadata/content confusion is dominated by functional-only outcomes: agents preserve benign utility but leave attacks live. Stateful fallback conflict shows a different pattern: agents often block attacks by deleting benign fallback behavior. Together, these results expose a gap in repairing cross-skill data use: agents do not reliably remove unsafe influence while retaining the legitimate behavior that depends on the same information.

</details>

### 136. Interrogation Protocols for AI Control

📄 [OpenReview](https://openreview.net/forum?id=NQsLXclgsW)　📅 2026-10　🏷️ P1

**关键词**：`AI control`、`interrogation`、`monitor`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：agent 智能相对可信监控器上升时监控器失败风险增——审讯协议：允许监控器就不解动作质问不可信 agent
- 🔬 **研究方法**：审讯有效的条件是弱模型能分辨攻击策略的误导解释与诚实策略的真实解释——BashArena 留出子集 1% 审计预算实验
- 📌 **结论**：审讯把安全 72.6%→79.5%（+7.0pp）但大部分增益可由可信模型陈述具体关注点获得——AI control 设置下的审讯协议首证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As the intelligence of an AI agent increases relative to a trusted monitor, so does the risk that the monitor will fail to understand the agent’s actions or to evaluate them confidently. We introduce interrogation protocols to a high stakes AI control setting, and allow the monitor to ask the untrusted agent questions about confusing actions. For interrogation to improve safety, a weaker model must be able to distinguish misleading explanations produced by an attack policy from genuine ones produced by an honest policy. We find that on a held out subset of BashArena, an interrogation protocol improves safety at a 1% audit budget from 72.6% for an actions only baseline, which does not use interrogations, to 79.5% (+7.0 pp [+0.9, +20.1], 95% paired bootstrap interval), but most of this uplift can be captured by having a trusted model state a specific concern. More broadly, our work suggests that interrogating agents can improve safety, allowing monitors to catch more attacks at a larger capability gap.

</details>

### 137. Benchmarking Security Risk Detection and Verification in Open Agentic Skill Ecosystems

📄 [OpenReview](https://openreview.net/forum?id=NtaF69ZGWQ)　📅 2026-10　🏷️ P1

**关键词**：`agent skill supply chain`、`benchmark`、`runtime verification`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：开放 agent 平台的社区技能构成供应链风险——恶意行为藏于表观良性技能，缺检测+运行时验证双段基准
- 🔬 **研究方法**：SkillVetBench：语义审查技能自然语言规范检恶意意图+被标技能进插桩沙箱执行取可审计证据，取自 OpenClaw 真实生态含 ClawHavoc 攻击campaign
- 📌 **结论**：语义/签名基线漏至多 89% 恶意技能且运行时攻击集中于 exec/write_file 等高权限原语——技能供应链的两段式审查基准

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open agent platforms allow community contributors to publish reusable skills that agents can invoke at runtime. This extensibility also creates a supply-chain risk: malicious contributors can hide harmful behavior inside skills that appear benign under superficial inspection. However, existing defenses are hard to evaluate because there is no benchmark that measures both malicious-skill detection and runtime verification. We present SkillVetBench, a two-stage security vetting benchmark for open agentic skill ecosystems. The first stage performs semantic vetting over each skill’s natural-language specification to detect hidden malicious intent. The second stage executes flagged skills in an instrumented sandbox to observe runtime behavior and collect auditable evidence. We build a benchmark from confirmed malicious skills10 in the live OpenClaw ecosystem, including samples from the recent ClawHavoc11 supply-chain campaign. Unlike static-only methods, SkillVetBench verifies de-12 tected threats with execution traces. Our experiments show that: (1) semantic-only13 and signature-based baselines are insufficient, missing up to 89% of malicious skills14 whose threats arise from natural-language instructions, multi-component logic, or15 cross-component interactions; (2) runtime attacks are concentrated in a small set of16 high-permission primitives, especially exec, write_file, install_skill, and17 spawn; and (3) SkillVetBench provides case studies in which sandbox execu-18 tion directly supports malicious verdicts with concrete runtime evidence.

</details>

### 138. AgentDyn: Are Your Agent Security Defenses Deployable in Real-World Dynamic Environments?

📄 [OpenReview](https://openreview.net/forum?id=Ulq3txoigl)　📅 2026-10　🏷️ P1

**关键词**：`agent security benchmark`、`dynamic environment`、`defense deployability`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：agent 安全面向真实开放部署——现有基准三缺陷：缺动态开放任务/缺有益第三方指令/用户任务过简
- 🔬 **研究方法**：AgentDyn：60 个手工开放任务+560 注入测试用例（购物/GitHub/日常），需动态规划并含良性第三方指令，评测九 SOTA 防御
- 📌 **结论**：静态基准上的防御排名在动态开放环境失效——防御可部署性的基准化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents that autonomously interact with external tools and environments have shown great promise across real-world applications. However, their reliance on external data exposes them to serious indirect prompt injection attacks, where malicious instructions embedded in third-party content hijack agent behaviors.
To mitigate this threat, a growing number of defenses have been proposed and evaluated under existing agent security benchmarks. These benchmarks provide structured environments for comparing attacks and defenses, and have become a key driver for defense design and optimization. However, as agents move toward more complex and open-ended real-world deployments, there is a pressing need for benchmarks to become more adaptive and better reflect the dynamic environments faced by real-world agentic systems.
In this work, we reveal three fundamental flaws in the current benchmarks and push the frontier along these dimensions: (i) lack of dynamic open-ended tasks, (ii) lack of helpful instructions, and (iii) simplistic user tasks.
To bridge this gap, we introduce AgentDyn, a manually designed benchmark featuring 60 challenging open-ended tasks and 560 injection test cases across Shopping, GitHub, and Daily Life. Unlike prior static benchmarks, AgentDyn requires dynamic planning and incorporates helpful third-party instructions. Our evaluation of nine state-of-the-art defenses shows that none is deployable: defenses that preserve utility remain vulnerable even to standard attacks, while those that block attacks do so by collapsing utility, often even in the absence of any attack. Our benchmark is available at https://anonymous.4open.science/r/AgentDyn-66DF.

</details>

### 139. SAFE-Mem: Secure Agentic Memory with Fine-Grained Authority and Governance-Aware Retrieval

📄 [OpenReview](https://openreview.net/forum?id=VDqyNOwFKr)　📅 2026-10　🏷️ P1

**关键词**：`memory governance`、`provenance labels`、`agent security`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：外部来源信息进入持久记忆后被当授权偏好/政策/权限使用——内容过滤或粗粒度溯源要么挡不住要么误伤
- 🔬 **研究方法**：SAFE-Mem：每条声明标注 kind/authority/scope 三治理标签+治理感知检索匹配查询需求与声明权限+治理使能记忆图溯源
- 📌 **结论**：四骨干 MPBench/LoCoMo 上保合法记忆使用的防御中最低攻击成功率（低于最强者至少 77%）且最高答案准确率——细粒度记忆治理

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents increasingly rely on persistent memory to support long-term reasoning and personalized interactions. However, information collected from external sources can introduce security risks when untrusted claims (i.e., atomic statements) are later treated as authorized preferences, policies, or permissions. Existing defenses typically rely on content-based filtering or coarse-grained provenance tracking, which either fail to prevent unauthorized memory use or block legitimate information, sacrificing memory utility. To address these limitations, we propose SAFE-Mem, a fine-grained memory governance framework that improves security while preserving legitimate memory use. First, SAFE-Mem annotates each claim with three governance labels (i.e., kind, authority, and scope) to capture its provenance and permitted use. Second, governance-aware retrieval matches query requirements with claim permissions to block unauthorized influence while retaining legitimate information. Third, a governance-enabled memory graph connects source sentences, claims, and entities to support provenance tracking and efficient retrieval. Across four LLM backbones on MPBench and LoCoMo, SAFE-Mem attains the lowest attack success among defenses that retain legitimate memory, at least 77% below the strongest of them, and the highest answer accuracy of all evaluated defenses, improving it by up to 15%. The code is available at https://anonymous.4open.science/r/SAFE-Mem-code-37E4/.

</details>

### 140. Toward Real-World One-Shot Indirect Prompt Injection: Strategy Abstraction Via Outcome-Conditioned Reflection

📄 [OpenReview](https://openreview.net/forum?id=Woo4sUnlIP)　📅 2026-10　🏷️ P1

**关键词**：`one-shot injection`、`strategy abstraction`、`real-world attack`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：现实攻击者只有一次机会：植入一次、无反馈、环境改变才算成功——迭代攻击假设不成立
- 🔬 **研究方法**：SAVOR：离线从成功/失败轨迹反思抽象攻击策略存冻结记忆，每未见目标单载荷生成；ASB 仿真+OpenClaw-IPI 真实可执行基准验证状态改变
- 📌 **结论**：三受害模型两防御下最高 ASR 且真实条件领先从 3.3-11.8 扩至 11.3-21.3pp——单发实用化的间接注入

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Tool-using large language model (LLM) agents are vulnerable to indirect prompt injection (IPI), where malicious instructions in external observations hijack agent actions. Real-world attackers get one chance: they plant content once, receive no feedback, and succeed only if the agent changes the environment. Humans handle such one-shot situations by reflecting on past successes and failures and abstracting reusable strategies. Inspired by this, we propose **SAVOR** (**S**trategy **A**bstraction **V**ia **O**utcome-Conditioned **R**eflection), which learns attack strategies offline from successful and failed trajectories and uses a frozen strategy memory to generate one payload per unseen target. We evaluate in simulation on Agent Security Bench (ASB) and under real-world conditions on OpenClaw-IPI, our executable benchmark that verifies actual state changes. SAVOR achieves the highest attack success rate across three victim models and two defenses, and its lead over the strongest prior attack widens from **3.3–11.8** points on ASB to **11.3–21.3** points on OpenClaw-IPI.Code and data: https://anonymous.4open.science/r/SAVOR_NAACL-E8BE/

</details>

### 141. Blame Laundering: Log Deletion Attacks on Multi-Agent Failure Attribution

📄 [OpenReview](https://openreview.net/forum?id=XlrJ46G47F)　📅 2026-10　🏷️ P1

**关键词**：`log manipulation`、`failure attribution`、`multi-agent audit`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：MAS 失败后 LLM 判官审计执行日志定责——而日志由 agent 自身提供，攻击者可操纵审计
- 🔬 **研究方法**：blame laundering：扣留自身故障日志把责任转移给无辜 agent——九判官×339 注入故障轨迹+117 自然失败，含本地 30B 模拟审计选最优删除
- 📌 **结论**：仅扣故障日志转移 54-62% 正确审计（随机删除 1-9%）；不知故障位置也可模拟审计选择（48-58%）；判官仅 2-21% 弃权而无辜者以原置信度被指控——判官需要攻击者控制之外的证据（网关全调用日志可复原）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When a multi-agent collaboration fails, LLM judges audit its execution logs to identify the culprit. The agents provide these logs themselves, so an attacker agent may manipulate the audit. We introduce blame laundering: an attacker agent withholds the log of its fault and transfers the blame to an innocent agent. We test nine judges on 339 injected-fault traces from Who&When Pro and repeat the attack on 117 natural failures from Who&When: (a) On injected faults, withholding only the fault log transfers 54%–62% of correct audits, against 1%–9% for random deletion. On natural failures, it transfers 24%–62%, against 6%–19%. (b) The attacker does not even need to know where its fault is. It can simulate the audit on a local 30B model and choose the best deletion, which transfers 48%–58% for the eight API judges. (c) The judges can abstain but do so only 2%–21% of the time. Instead, they accuse the innocent agent with unchanged confidence. (d) Even when we state whose log is missing and let the judge accuse that agent, the attack transfers 29%–61%. Judges therefore need evidence outside the attacker's control. In a GSM8K application, a gateway logging every model call lets them identify the culprit again.

</details>

### 142. MARA: Memory Attribution and Risk Authorization for Memory-Augmented Agents

📄 [OpenReview](https://openreview.net/forum?id=YTkFBVL0c6)　📅 2026-10　🏷️ P1

**关键词**：`memory attribution`、`risk authorization`、`poisoned memory`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：持久记忆可把有害信息带入后续执行——使用时哪个被检索记忆在驱动待发不安全动作、去掉它能否恢复任务能力
- 🔬 **研究方法**：MARA：预执行授权——诱导候选动作轨迹+风险评量+逐记忆 drop-one/only-one 反事实（必要性/充分性/结构轨迹漂移组合归因）→四决策允许/移除/核验/阻断
- 📌 **结论**：MINJA 三任务上大幅降攻击成功率同时提升原任务完成——毒记忆的因果归因与执行时授权

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Persistent memory improves tool-using large language model agents but may carry harmful information into subsequent execution. Existing defenses commonly filter memory writes, rerank retrieved memories, or block risky outputs. They do not directly answer a use-time question: which retrieved memory, if any, is driving the pending unsafe action, and can the agent recover its original task capability without it? To address this question, we introduce MARA (Memory Attribution and Risk Authorization), a pre-execution authorization framework for memory-augmented agents. MARA induces a candidate action trace, assesses its risk under the current request and trusted environment, and intervenes on each retrieved memory with drop-one and only-one counterfactuals. It combines necessity, sufficiency, and structured trace drift to identify memories that contribute to risk, removes suspicious memories only from the current execution context, replans, and then follows one of four decisions: Allow, Remove-memory, Verify, or Block. We evaluate MARA on the QA, RAP, and EHR tasks of the public MINJA benchmark. Across all three tasks, MARA substantially reduces attack success while improving original-task completion. Further analysis shows that necessity, sufficiency, and structured drift provide complementary attribution signals under different poison concentrations. These results demonstrate that MARA can prevent persistent-memory attacks while recovering useful task execution.

</details>

### 143. Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents

📄 [OpenReview](https://openreview.net/forum?id=YkxkjlxioO)　📅 2026-10　🏷️ P1

**关键词**：`skill evolution`、`unsafe skill`、`self-improving agents`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：agent 完成不安全任务后技能演化可把不安全过程存进技能——良性任务在原指令消失后复现伤害（技能劣化）
- 🔬 **研究方法**：SkillMisEvo-Gym 清任务会话保技能库分离两环节+Bench 525 任务 25 幕恶意-良性交替+SafeEvolve 写入与检索双检
- 📌 **结论**：21 种组合全部写出不安全技能、14 种带入新会话；SafeEvolve 不安全检索 35.3%→8.7%、伤害 21.3%→4.0%——技能演化的安全检查点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents increasingly save experience from past tasks as reusable skills through skill evolution. When an agent completes an unsafe task, skill evolution can keep the unsafe procedure inside an otherwise useful skill, and a later benign task can repeat the harm after the unsafe instruction is gone. We call this failure skill misevolution. It requires that the agent write the unsafe procedure into a skill and that a later task retrieve and follow that skill. We introduce SkillMisEvo-Gym, which clears every task session but keeps the skill library, so each of these steps can be checked separately. We also build SkillMisEvo-Bench with 525 tasks in 25 episodes, where each episode alternates malicious and related benign tasks before three benign tasks in a new session. Across 21 combinations of agents and evolution methods, all of them write unsafe skills and 14 carry the harm into the new session, so the risk comes from skill evolution itself. Evolution raises benign utility in 15 combinations but also raises malicious-task harm in 17, so ranking methods by utility alone would hide this risk. We propose SafeEvolve, which checks each skill when it is written and when a later task retrieves it. It cuts unsafe retrieval in the new session from 35.3% to 8.7% and harm from 21.3% to 4.0% while keeping benign utility during learning within 0.4 points, at a cost of 12.7 points of new-session utility. SafeEvolve-UP cuts new-session harm by 16.0 points and keeps new-session utility within 1.3 points of raw evolution. As agents learn from their own experience, safety must cover the skills that carry past behavior into future tasks. Code is available at https://anonymous.4open.science/r/misevolve_arr-091F/.

</details>

### 144. Whose Credential Is It? How Owner Attribution in Agent Memory Shapes Cross-User Account Misuse

📄 [OpenReview](https://openreview.net/forum?id=aETkprcIAa)　📅 2026-10　🏷️ P1

**关键词**：`agent memory`、`credential misuse`、`owner attribution`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：共享长期记忆让 agent 误取他人凭证——暴露何时变成真实伤害未分离
- 🔬 **研究方法**：三阶段审计分离暴露/行为/账户状态变化+AppWorld 763 条混合历史登录压力测试+凭证行内命名属主干预
- 📌 **结论**：压力测试中七 agent 80-94% 使用外凭证并至多 43% 改动受害者账户；行内命名属主把误用 92/305→1/305——记忆应记录凭证属谁且评测须测行为而非仅暴露

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Shared long-term memory lets an LLM agent serving one user inadvertently retrieve another user's credentials, but it is unclear when such exposure leads to actual harm. We introduce a three-stage audit that separates three events: a foreign credential reaches the prompt (exposure), the agent acts with it (behavior), and the other user's account changes (state). In AppWorld, a store that mixes 763 past logins from all users retrieves another user’s credential for 84.7% of required apps, yet agents rarely act on it. Misuse appears in a stress test where memory lacks the user's own credential and presents a single foreign one as the user's record: seven agents then use it in 80–94% of runs and change the victim's account in up to 43%, sometimes passing the official check. Naming the owner before or inside each credential line prevents most of this: with all else fixed, misuse falls from 92 to 1 of 305 paired runs, also with name-free usernames, though owner-bound notes cost 3–5 successful tasks per model on clean memory. A wrongly written owner largely restores misuse; trailing owner tags and added safety instructions help only some models. Agent memory should consistently record whose credential it stores, and evaluations should measure behavior, not only exposure.

</details>

### 145. SkillPrivus: Uncovering Privacy Harms in Agentic Skills

📄 [OpenReview](https://openreview.net/forum?id=aJnbokz2NX)　📅 2026-10　🏷️ P1

**关键词**：`skill privacy`、`contextual integrity`、`static audit`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：技能即便履行广告任务也可能推断敏感属性/保留不必要信息/向意外接收者披露——使用即隐私伤害未被审
- 🔬 **研究方法**：SkillPrivus：安装前静态审计——从代码与自然语言指令抽取数据操作+源证据接地+适配情境完整性评估适当性
- 📌 **结论**：726 真实技能中 563 处理个人数据、307（54.5%）被旗至少一项潜在违规（与三盲标 83.2% 一致）——敏感推断/超任务使用/意外披露即普通功能即可产生隐私伤害

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills extend AI assistants through installable instructions and code that can access users’ files, accounts, and data. Even when performing their advertised tasks, skills may infer sensitive attributes, retain unnecessary information, or disclose data to unexpected recipients. We study these potential privacy-of-use harms through SkillPrivus, a static audit framework that analyzes skills before installation without executing them. SkillPrivus extracts data operations from code and natural-language instructions, grounds them in source evidence, and adapts Contextual Integrity to assess their appropriateness. Applied to 726 real skills from public marketplaces, 563 of which handle personal data, SkillPrivus flags at least one potential violation in 307 of these skills (54.5%), and its judgments agree with three blind human annotators on 83.2% (κ=0.35) of resolvable moves. The flagged behaviors include sensitive inferences, information use beyond the stated task, and disclosures to unexpected recipients, suggesting that privacy harms can arise from ordinary skill functionality.

</details>

### 146. Agent Mosaic: Recognizing Confidentiality Leaks in Agentic LLM Systems

📄 [OpenReview](https://openreview.net/forum?id=ca7PnDg0Lm)　📅 2026-10　🏷️ P1

**关键词**：`mosaic effect`、`confidentiality`、`inference control`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：agent 可从多份可访问文档组装出敏感结论——拼图效应的机密性风险未量化
- 🔬 **研究方法**：30 个合成网安/医疗/军事样例×三 agent 仿真（10800 答案）+两开源 harness 实测（1440 答案）+分级标题与显式聚合规则干预
- 📌 **结论**：最佳 GPT-5.6-Sol 良性查询下仍 7.08% 泄露禁组合、实测 harness 更差；防护后 32.37% 仍持续泄露且显著拒答本身可揭示禁结论——混合密级环境的推断控制需求

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern LLM agents can retrieve information from accessible documents, and then disclose a sensitive conclusion assembled from them. This mosaic effect creates a critical risk for agents operating over confidential data. We quantify its realization with 30 synthetic cybersecurity, medical, and military examples, yielding 10,800 final answers from three LLM agents in controlled simulation and 1,440 answers from live agents in two open-source harnesses. Even under benign queries designed to be answerable from one document, GPT-5.6-Sol, the best performing model tested, discloses forbidden composites in 7.08% of answers (95% CI: 3.75-10.67%) in simulation, with worse disclosure rates in live harnesses. Adding visible classification headers and explicit aggregation rules reduces pooled disclosure rates substantially, yet unsafe disclosures persist in 32.37% of simulated answers (95% CI: 28.33-36.19%) across all intents despite these safeguards. Furthermore, increased refusals do not guarantee confidentiality, since significant refusals reveal the prohibited conclusion regardless. These results point to a troubling conclusion: sensitive data leaks via mosaic-style events are an observed confidentiality failure mode in the evaluated settings at non-negligible rates. They motivate stronger controls on what agents may infer and disclose in sensitive data environments with mixed-clearance users.

</details>

### 147. SkillWard: Detecting Malicious Agent Skills through Execution-Grounded Reasoning

📄 [OpenReview](https://openreview.net/forum?id=ceYaFcF0tY)　📅 2026-10　🏷️ P1

**关键词**：`skill detection`、`execution-grounded`、`supply chain`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：技能异构结构使检测器难辨真恶意还是表面风险指标——混淆载荷与可疑模式良性反例双挑战
- 🔬 **研究方法**：SkillWard-Bench（加密载荷/多文件载体+保可疑模式的良性反例）+SkillWard 两段检测：任务感知语义分析+选择性运行时验证（agent 动作与系统调用证据）
- 📌 **结论**：三技能基准最高 F1（+12.36pp、FPR -43.40pp）且框架可扩至 MCP 服务器——执行接地推理检测恶意技能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent Skills extend large language model (LLM) agents with reusable instructions, scripts, and supporting resources, but also introduce new attack surfaces. The heterogeneous structure of Skills makes it challenging to determine whether security detectors identify genuinely harmful behavior or merely respond to surface-level risk indicators. To investigate this question, we introduce SkillWard-Bench, a benchmark with two complementary challenges: obfuscated malicious payloads and benign counterexamples that retain suspicious patterns. Its malicious samples conceal payloads in encrypted content and diverse file carriers, while its benign samples test whether similar risk cues cause false positives. We also propose SkillWard, a two-stage detector featuring task-aware semantic analysis, selective runtime verification, and complementary agent-action and system-call evidence from real execution. Experiments show that SkillWard achieves the highest F1 across three Skill benchmarks, improving F1 by 12.36 percentage points and reducing FPR by 43.40 percentage points on SkillWard-Bench relative to prior SOTA. Ablation and backend studies further support the effectiveness of its two-stage design and its robustness across LLM backends. We further explore the applicability of the benchmark construction and detection framework to Model Context Protocol (MCP) servers.

</details>

### 148. Ajar: How Much Privilege Do LLM Agent Defenses Leave Open?

📄 [OpenReview](https://openreview.net/forum?id=et0E22jwLC)　📅 2026-10　🏷️ P1

**关键词**：`defense evaluation`、`residual privilege`、`agent security`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：agent 安全防御评测只看 ASR 与良性效用——都不来自任务需要的调用（开放权限）被忽略
- 🔬 **研究方法**：Ajar：附着既有基准，为每个良性任务生成任务不需要的候选调用——防御放行一个即留权限开放；AgentDojo/AgentDyn/DoomArena×五防御（Progent/CaMeL/AC4A/Permission Assistant/Claude Code Auto）
- 📌 **结论**：各防御留下不同量开放权限且 ASR 与良性效用都不预测该量——最小权限视角的防御评测新维度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A language model agent acts through the tools it is given but the data it reads can redirect what it does with them. Agent defenses sit between the agent and its tools to stop the actions its user never intended. Agent-security benchmarks evaluate these defenses by how far they lower attack success while preserving the agent's utility on benign tasks. Both scores come from the trajectory the agent produces when it is given a task. A defense can therefore score well on both while leaving open a transfer, a deletion or a broad read that no task needed. Ajar measures that open privilege directly. It attaches to an existing benchmark and reuses the infrastructure that benchmark already uses to grade itself. For each benign task it generates candidate calls the task does not need so a defense that allows one has left privilege open. We attach it to AgentDojo, AgentDyn and DoomArena and measure five defenses (Progent, CaMeL, AC4A, Permission Assistant and Claude Code's Auto mode). We observe that the defenses leave different amounts of privilege open and that neither attack success nor benign utility predicts that amount.

</details>

### 149. Evolution Under Fire: Evolving Agent Safety Harnesses with Adaptive Injection Stressors

📄 [OpenReview](https://openreview.net/forum?id=g6YySavcdG)　📅 2026-10　🏷️ P1

**关键词**：`harness evolution`、`adaptive stressor`、`agent security`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：恶意指令与合法任务指令经同一交互通道到达——手工静态防御的改进依赖重复人工重设计
- 🔬 **研究方法**：Evolution Under Fire：效用约束 Pareto 调度树搜索从执行证据进化完整可执行安全 harness（模型/基准/工具/评测器固定）+自适应压力器进化发现保效用攻击指导下一轮进化
- 📌 **结论**：AgentDyn GPT-4o-mini 攻击成功率 50.4%→3.0%；进化 harness 零再进化迁移 Qwen3.5-35B（32.1%→0.9%）——攻防双侧共进化 harness

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Tool-using language-model agents must act on information from untrusted emails, webpages, and documents. This creates a central security challenge: malicious instructions and legitimate task directives can arrive through the same interaction channel. Existing defenses are largely hand-designed and static, making further improvements dependent on repeated manual redesign. We introduce Evolution Under Fire, a staged framework that couples safety-harness evolution with adaptive stressor evolution. Utility-constrained, Pareto-scheduled tree search evolves complete executable safety harnesses from execution evidence while keeping the task model, benchmark, tools, and evaluator fixed. Adaptive stressor evolution then discovers utility-preserving attacks that guide a subsequent stage of harness evolution. On AgentDyn with GPT-4o-mini, an evolved harness reduces attack success from 50.4% to 3.0%, improves clean and attacked utility over the initial harness, and offers a stronger security–utility trade-off than reproduced defenses. On Agent-SafetyBench with Qwen2.5-7B-Instruct, harness evolution reduces attack success from 82.6% to 62.0% while retaining helpfulness and runtime validity. Evolved harnesses also transfer without further evolution to Qwen3.5-35B-A3B, reducing attack success from 32.1% to 0.9% while improving attacked-task utility.

</details>

### 150. Appreciation Teaches Unauthorized Execution: Self-Evolution Degrades the Robustness of Personal Agents to Indirect Prompt Injection

📄 [OpenReview](https://openreview.net/forum?id=j25IR1xlAj)　📅 2026-10　🏷️ P1

**关键词**：`self-evolution`、`indirect prompt injection`、`robustness degradation`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：自进化个人 agent 从用户反馈学习——若曾按不可信第三方内容行事，第三方即获得 agent 控制权
- 🔬 **研究方法**：两阶段受控方法：适应期用户要求读外部内容并完成任务（日常请求）→agent 按设计从反馈自我改进；测试期第三方写入相似任务而用户请求未授权
- 📌 **结论**：自进化使注入鲁棒性大幅退化：技能演化 ASR +14.0-48.8pp、RL +3.0-39.3pp——进化本身放大未授权执行（自进化×注入安全）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-evolving personal agents act for users and learn from user feedback. However, if an agent obeys an instruction that an untrusted third party hides in content, the third party gains control of the agent. Such indirect prompt injection (IPI) poses severe risks. We investigate whether self-evolution degrades the robustness of personal agents to IPI. To study this question, we design a controlled two-phase methodology. In the adaptation phase, the user asks the agent to read external content and complete the task described in it, a common request in daily use. The agent then learns from the user's feedback and improves itself as designed. In the test phase, a third party writes a similar task into new external content, but the user's test request does not authorize the injected task. Using this methodology, we build multiple tasks with diverse test instances in different domains for a real personal agent. Our extensive experiments reveal that self-evolution substantially degrades robustness to IPI. Specifically, compared with the base agent, which does not evolve from user feedback, the average attack success rate rises by 14.0–48.8 percentage points under skill evolution and by 3.0–39.3 percentage points under reinforcement learning, posing safety risks.

</details>

### 151. Benign in Isolation, Harmful in Composition: Security Risks in Agent Skill Ecosystems

📄 [OpenReview](https://openreview.net/forum?id=rGSatISXS3)　📅 2026-10　🏷️ P1

**关键词**：`skill composition risk`、`trust transfer`、`authorization confusion`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：技能逐个审查安全——但连续调用多技能时上游能力/信任信号/建议上下文影响后续动作，组合可诱发有害行为
- 🔬 **研究方法**：SCR-Bench 三机制：能力流（CapFlow）/信任抬升（TrustLift）/授权混淆（AuthBlur）+OpenClaw 运行时迁移实验
- 📌 **结论**：TrustLift 使平均 ASR 35.5%→83.9%（上游背书即可）；孤立评估遗漏组合风险——技能组合安全的三机制图谱

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid development of LLM agents, Skills extend their capabilities through reusable procedures, but security risks in skill use can compromise agent execution and lead to security issues such as data leakage. Existing vetting methods typically inspect each skill independently, assessing its components to determine whether it is safe. However, many tasks involve successive invocations of multiple skills, allowing upstream capabilities, trust signals, or advisory context to influence subsequent actions. Certain compositions can consequently induce harmful agent behavior. We define this security gap as SCR (Skill Composition Risk): Skills that behave safely when used individually can produce harmful outcomes along activated composition paths. To evaluate this risk, we introduce SCR-Bench (Skill Composition Risk Benchmark), comprising three categories of SCR mechanisms: SCR-CapFlow for capability flow, SCR-TrustLift for trust transfer, and SCR-AuthBlur for authorization confusion. Experiments across multiple backbones demonstrate that skill composition exposes risks missed by isolated evaluation. TrustLift increases mean attack success rate (ASR) from 35.5% under direct installation requests to 83.9% with upstream endorsement. Transfer experiments in OpenClaw further demonstrate these attacks in an agent runtime, highlighting the practical importance of SCR for skill security.

</details>

### 152. Post-Training Pressure Erodes Privacy in Personalized Agents

📄 [OpenReview](https://openreview.net/forum?id=tmwrbA5sZ9)　📅 2026-10　🏷️ P1

**关键词**：`RL personalization`、`PII leakage`、`adversarial representative`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：个人 agent 在私有工作区 RL 后训——任务成功与偏好 adhering 奖励不罚未授权披露
- 🔬 **研究方法**：Pτ-bench（τ³-bench 银行知识域个性化的 RL 环境）：OpenClaw agent 搜私有工作区+与银行代表交互，Qwen/Granite/Gemma 三骨干前后对照+JSpace 内部读出
- 📌 **结论**：个性化前已泄 PII；RL 后 Qwen 每任务平均 PII 泄漏约翻倍、不诚实代表经毒工具的抽取成功率增至三倍以上——普通任务泄漏与攻击易感性双通道的隐私侵蚀（后训练×隐私）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Personal agents learn from interactions in private workspaces, but rewards for task success and preference adherence can leave unauthorized disclosure unpenalized. We introduce ptau (Personalized Tau-Bench), personalized RL environments extending the Banking Knowledge domain in τ³-bench. An openclaw agent searches a private workspace and interacts with a banking representative. We post-train it through online RL to better simulate the user's needs and preferences and complete their tasks. Across Qwen, IBM Granite, and Gemma, models before personalization already leak unauthorized personally identifiable information (PII). RL improves task success while inducing two competing pressures: useful searches expose unrelated private records, whereas fewer turns reduce exposure. Which pressure dominates helps explain changes in leakage. A third behavioral change, increased compliance with the representative, lets a dishonest representative extract private information through poisoned tools. For Qwen, average PII leakage per evaluated task roughly doubles after post-training for task success, while exfiltration success more than triples in one user's environment. Privacy can therefore erode through ordinary-task leakage or greater vulnerability to attacks. Finally, JSpace readouts, which map internal representations to vocabulary scores, reveal reduced prominence of privacy concepts under red teaming in several conditions, suggesting a possible catastrophic forgetting in JSpace. Taken together, our findings indicate that post-training pressure can produce privacy failures beyond reward hacking.

</details>

### 153. Familiarity Breeds Vulnerability: Probe-then-Abuse Personalized Memory Manipulation Attack on LLM Agents

📄 [OpenReview](https://openreview.net/forum?id=woYm8irkR9)　📅 2026-10　🏷️ P1

**关键词**：`personalized memory attack`、`probe-then-abuse`、`agent skills`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：记忆增强 agent 的用户个性化熟悉度即新攻击面——盲目注入不利用熟悉度效果有限
- 🔬 **研究方法**：PtA：先探测用户记忆恢复用户相关内容→按用户一致模式伪造对抗记忆；以恶意用户安装的技能实现（无需记忆库特权访问），五记忆系统五基准
- 📌 **结论**：Mem0-v1+PrefEval 上 ASR 82.9% vs MINJA 适配基线 4.1%——个性化即脆弱性的现实威胁模型（探测后滥用）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Memory-augmented LLM agents increasingly rely on user-specific memory to provide personalized responses, but such personal familiarity also creates a new attack surface: memory manipulation attacks may abuse this familiarity to inject personalized adversarial memories that mimic user-consistent patterns.
Existing memory manipulation attacks typically rely on blind injection strategies that fail to exploit this familiarity-driven vulnerability, resulting in limited attack impact.
In this work, we introduce ***Probe-then-Abuse (PtA)***, a personalized memory manipulation attack that first probes the user's memory to recover user-relevant memories, then abuses the recovered content to inject adversarial memories. By crafting adversarial entries that mimic user-consistent patterns, *PtA* substantially increases the attack impact. In addition, unlike prior work assuming an unrealistic threat model that allows direct memory access, we ground *PtA* as a malicious user-installed agent skill that can steer the agent's memory-related actions during user interactions without requiring privileged access to the underlying memory database. Across five memory system variants and five benchmarks, *PtA* achieves strong memory manipulation with high attack specificity. On Mem0-v1 with PrefEval, *PtA* reaches 82.9% ASR, compared with 4.1% for the MINJA-adapted baseline. We further show that existing defenses provide limited protection, calling for memory-specific defenses.

</details>

### 154. Persuadable Simulators: Agent Rhetoric Flips LLM Environment Simulators on Rule-Based Violations, Not State Lookups

📄 [OpenReview](https://openreview.net/forum?id=2J5ezpBAZ3)　📅 2026-10　🏷️ P2

**关键词**：`simulator persuasion`、`RL environment`、`rule violations`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：LLM 作为 agent RL 的环境模拟器——行动 agent 的自由文本通道是真执行器从不读的攻击面
- 🔬 **研究方法**：SimPersuade：2349 个由真实执行器定结局的动作配七种消息包装（含长度匹配噪声控制），量翻转率
- 📌 **结论**：模板修辞为'前置已验证'买 0.6-3.7pp、伪造成功回执 1.9-10.5pp（噪声本身翻 2-13%）；无控制会高估至 4.2 倍；规则应用类违规模拟器本来就 42-77% 接受——模拟器说服的受控测量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Language models are increasingly used *as* the environment in agent reinforcement learning: instead of executing a tool call, a command or a world action, a simulator
  model predicts the observation it would produce. The acting agent writes free text next to its action, which gives it a channel the real executor never reads. We ask
  whether that channel can talk a simulator into accepting an action the executor rejects. SimPersuade pairs 2,349 actions whose outcome is fixed by running the real
  executor (τ²-bench retail and airline, ALFWorld, terminal sessions) with seven message wrappers—including a length-matched noise control—and measures the *flip rate*:
  the fraction of correctly rejected failures that a wrapper turns into a predicted success. Across 11 simulator configurations (4B–235B, thinking and non-thinking, and a
  world model trained for this task), template rhetoric buys 0.6–3.7 pp for a claim that the precondition was already verified and 1.9–10.5 pp for a fabricated success
  receipt over length-matched noise; noise alone flips 2–13%, which is 17–76% of the raw flip rate, so the same study without that control would overstate the effect by
  up to 4.2×. The risk is concentrated rather than absent: on violations that require applying a documented rule or arithmetic instead of a state lookup, simulators
  already accept 42–77% of failures with no message at all, and a fabricated receipt flips 20–84% of the rest. Per-action optimized messages beat length-matched noise on
  9/9 simulators (+5.2 to +26.2 pp), the domain-specialized world model is the most receipt-susceptible of all, and withholding agent-written text removes the channel at
  no cost in valid-action rejection.

</details>

### 155. A Survey of the Information Requirements of LLM Safeguards: From Conversational Safety to Agentic Control

📄 [OpenReview](https://openreview.net/forum?id=2mg5Yv6O2U)　📅 2026-10　🏷️ P2

**关键词**：`survey`、`safeguards`、`agentic control`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：从聊天到 agent，安全判断越来越依赖用户目标/授权/受影响资源状态——这些信息护栏未必能获得或会用
- 🔬 **研究方法**：信息中心视角综述：安全决策所需证据 vs 各方法可观察/可获取能力+其解读能力分析，并区分安全判断与执行强制
- 📌 **结论**：护栏能力/局限/适用性的共同基础——把'护栏需要什么信息'作为分析主轴（安全信息学综述）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The information needed to judge an LLM's behavior depends on the environment in which that behavior occurs. As LLM systems evolve from conversational chatbots to agent systems that use tools and interact with external environments, safety judgments increasingly depend on the user's objective, authorization, and the state of resources affected by an action. Such information may not be available to the safeguard making the decision. This survey presents an information-centric perspective on LLM safeguards, focusing on what information a safeguard needs to make a safety judgment and whether it can obtain and use that information. We use this perspective to review safeguards for conversational exchanges, external information, and agent actions. We compare the evidence required for safety decisions with what different methods can observe or acquire, and analyze their capabilities to interpret that evidence under applicable requirements. We also distinguish safety judgments from execution enforcement, which determines whether those judgments are binding on actions and resources. This perspective provides a common basis for understanding the capabilities, limitations, and applicability of existing safeguards across evolving LLM systems.

</details>

### 156. EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence

📄 [OpenReview](https://openreview.net/forum?id=6aBeXcbrkm)　📅 2026-10　🏷️ P2

**关键词**：`missing evidence`、`unsafe execution`、`evidence recovery`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：工具响应省略安全相关事实时 agent 可能执行被禁动作——而用户请求良性且每条返回皆真
- 🔬 **研究方法**：EpiSEM-Bench：300 对匹配不安全/安全任务×六域，系统压制关键事实测不安全执行与最小失败基数+独立审计工具测证据寻求与扣留
- 📌 **结论**：十模型遗漏鲁棒性差异大且抗遗漏≠有效恢复；恢复访问降所有模型不安全执行——缺失证据下的 agent 安全边界

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Tool-using language model agents rely on environmental facts to decide whether an action is permitted. When a tool response omits a safety-relevant fact, an agent may carry out a prohibited action even though the user request is benign and every returned statement is true. We introduce EpiSEM-Bench, an executable benchmark for evaluating unsafe execution, safety boundaries, and evidence recovery in LLM agents under missing evidence. It contains 300 matched unsafe/safe task pairs across six domains. By systematically suppressing critical facts, the benchmark measures unsafe execution under critical evidence omission and determines the minimum observed failure cardinality, including failures with full evidence and cases with no observed failure after exhaustive testing. An independent audit tool tests whether agents seek missing facts and then withhold prohibited actions while completing permissible tasks. The benchmark reveals substantial variation across the ten models in omission robustness, evidence acquisition, and appropriate action. Resistance to missing evidence does not necessarily translate into useful recovery. Recovery access reduces unsafe execution for all ten models, but agents differ in whether they actively obtain the missing facts and use them to act appropriately in both worlds.

</details>

### 157. PolicyShiftGuard: Benchmarking and Improving Policy-Adaptive Image Guardrails

📄 [OpenReview](https://openreview.net/forum?id=6nwgyCWL0a)　📅 2026-10　🏷️ P2

**关键词**：`image guardrail`、`policy-adaptive`、`benchmark`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：图像护栏假设固定安全政策——无法适配动态指定的政策边界
- 🔬 **研究方法**：PolicyShiftBench（2000 政策条件实例×265 图）+PolicyShiftGuard：随机政策 SFT+边界对政策适应（同图通过/阻止政策对比）
- 📌 **结论**：现有 VLM 与专用护栏在政策漂移下大幅失效；7B 版 Avg F1 76.9 且跨基准泛化——显式边界感知的政策自适应图像护栏

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing image guardrails assume fixed safety policies, limiting their ability to adapt to evolving policy boundaries. We investigate policy-adaptive image guardrailing, where models must assess image safety under dynamically specified policies. We introduce PolicyShiftBench, a benchmark comprising 2,000 policy-conditioned instances across 265 images, designed to evaluate policy sensitivity and generalization to unseen policies. To address this challenge, we propose PolicyShiftGuard, a lightweight guardrail trained through a two-stage framework combining Randomized Policy SFT (RP-SFT) and Boundary-Pair Policy Adaptation (BP-Adapt). By contrasting passing and blocking policies for the same image, BP-Adapt explicitly teaches models to distinguish policy-dependent safety boundaries. Experiments reveal substantial limitations of existing VLMs and specialized guardrails under policy shifts. In contrast, PolicyShiftGuard-7B achieves state-of-the-art performance on PolicyShiftBench, with 76.9 Avg. F1 and 72.1 Avg. PSS, while demonstrating strong cross-benchmark generalization to UnSafeBench and SafeEditBench. Our results highlight the importance of explicit boundary-aware training for robust policy-adaptive image guardrailing.

</details>

### 158. OS-SPEAR: A Toolkit for the Safety, Performance, Efficiency, and Robustness Analysis of OS Agents

📄 [OpenReview](https://openreview.net/forum?id=7f3hL4iTlc)　📅 2026-10　🏷️ P2

**关键词**：`OS agent`、`safety benchmark`、`toolkit`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：OS agent 基准安全场景窄、轨迹标注噪、鲁棒性单模态——缺四维系统分析
- 🔬 **研究方法**：OS-SPEAR：安全（环境/人诱导危害）/性能（轨迹价值估计分层采样）/效率（延迟+token）/鲁棒（跨模态扰动）四子集+自动诊断报告，22 个 OS agent 评测
- 📌 **结论**：效率与安全/鲁棒的普遍权衡——OS agent 的四维体检工具箱

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid evolution of multimodal large language models has catalyzed a paradigm shift from passive text generation to active behavioral execution, particularly in the form of OS agents capable of navigating complex Graphical User Interfaces (GUIs). 
Current benchmarks suffer from significant limitations, including narrow safety scenarios, noisy trajectory labeling, and a reliance on single-modality robustness metrics. 
To bridge this gap, we propose OS-SPEAR, a comprehensive toolkit designed for the systematic analysis of OS agents across four critical dimensions: Safety, Performance, Efficiency, and Robustness.
OS-SPEAR introduces four specialized subsets:
(1) a S(afety)-subset encompassing diverse environment- and human-induced hazards;
(2) a P(erformance)-subset curated via trajectory value estimation and stratified sampling;
(3) an E(fficiency)-subset quantifying performance through the dual lenses of temporal latency and token consumption;
and (4) a R(obustness)-subset that applies cross-modal disturbances to both visual and textual inputs. Additionally, we provide an automated analysis tool to generate human-readable diagnostic reports.
We conduct an extensive evaluation of 22 popular OS agents using OS-SPEAR.
Our empirical results reveal critical insights into the current landscape: notably, a prevalent trade-off between efficiency and safety or robustness, the performance superiority of specialized agents over general-purpose models, and varying robustness vulnerabilities across modalities.

</details>

### 159. PolicyGuard: A Dialogue-Grounded Sub-Agent Verifier for Policy Adherence in LLM Agents

📄 [OpenReview](https://openreview.net/forum?id=8p2LHJIiwW)　📅 2026-10　🏷️ P2

**关键词**：`policy adherence`、`sub-agent verifier`、`dialogue-grounded`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：政策遵守是跨多轮的对话问题而非单参数值——外部拦截式防护覆盖不足
- 🔬 **研究方法**：PolicyGuard 子 agent 验证器：共享 agent 对话视图+上下文中政策推理+可执行整改建议，三前沿模型 τ²-bench 航空域
- 📌 **结论**：Pass⁴ 提升 +12/+6/+12pp、比参数级护栏少拦截多捕获违规且三对抗探针下保持拒判准确——对话级政策遵守验证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents handle user requests on behalf of organizations through tool calls and must follow the company policies stated in their system prompts. Prior work approaches this as a safeguarding problem — external checks that block non-compliant agent actions. We argue that policy adherence is broader: real workflows unfold across many turns, require explicit user confirmation and prerequisite reads, and hinge on dialogue rather than on any single argument value. We introduce PolicyGuard, a sub-agent verifier that shares the agent's view of the dialogue, reasons over the policy in context, and returns actionable remediation. On τ²-bench airline across GPT 5.4, Claude Sonnet 4.6, and Gemini 2.5 Pro, PolicyGuard improves Pass⁴, the fraction of tasks successful in all four trials, by +12.0 / +6.0 / +12.0 pp; pooled paired tests support an overall cross-vendor effect. We further evaluate PolicyGuard on the full retail and telecom base splits, covering all three τ²-bench customer-service domains. Further analyses show that PolicyGuard improves reliability beyond agent self-checking, catches more policy violations with fewer blocks than argument-level guards, and preserves its refusal accuracy under three adversarial probes.

</details>

### 160. MOE-DEFENSE: Floor-Guarded Mixture-of-Experts Routing for Cost-Aware Security in LLM Agents

📄 [OpenReview](https://openreview.net/forum?id=A28H4cLtAF)　📅 2026-10　🏷️ P2

**关键词**：`cost-aware defense`、`MoE routing`、`floor guard`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：注入防御默认每请求过重 LLM 判官——成本不可行
- 🔬 **研究方法**：MoE-Defense：异构检测器当专家混合+静态字节集成地板锚定的门（安全不回退）；离线蒸馏判官为门特征而非在线投票
- 📌 **结论**：F1 0.9476@11 LLM 预算（判官调用省 89%）；AgentDojo 同 ASR 下阻断预算 1/3.6、零良性误报；白盒对手下长度触发升级把结构逃逸 100→0.9——成本感知安全路由

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents that read external tool output are exposed to prompt injection, yet the default defense—routing every request through a heavyweight LLM judge—is prohibitively expensive. We present MoE-Defense, a cost-aware security layer that treats heterogeneous detectors as a mixture of experts and learns a gate over them, anchored on a static byte-ensemble floor so that security can never regress. Across five seeds the floor-gated configuration reaches F1 0.9476 ± 0.0006 at an 11 LLM budget—89% fewer LLM calls than always calling the judge. End-to-end on AgentDojo, the floor-gated configuration buys the same attack-success rate as a static ensemble at 1/3.6 the block budget with zero benign false positives; under a white-box adversary a length-triggered escalation tier cuts structural escape from 100 to 0.9—at the cost of one judge call per released long text. We further show that distilling the judge offline into gate features, rather than voting online, is what removes the cost without removing the security.

</details>

### 161. Evaluating Agent Behavior After Compromises in Multi-agent Systems

📄 [OpenReview](https://openreview.net/forum?id=Af5qAHVoTx)　📅 2026-10　🏷️ P2

**关键词**：`agent compromise`、`harm assessment`、`role perturbation`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：被攻陷 agent 会改变下游决策与行动——攻击成功率不揭示违规在哪里发生
- 🔬 **研究方法**：HARP：同重置态的良性/受攻执行配对+确定性角色特定检查（工具与数据库证据）区分完整性违规与普通输出波动，量化溢出/传播/隐蔽/防御成本
- 📌 **结论**：60 金融配置中良性-良性 0.03% vs 良性-受攻 9.4% 被旗标，非目标违规多为决策门批准翻转——受控攻陷后的 agent 级伤害评估

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A compromised LLM agent can alter downstream decisions and actions, yet attack-success metrics do not reveal where violations arise. We introduce HARP (Harm Assessment under Role Perturbation), a framework for agent-level evaluation after controlled compromise. HARP pairs benign and attacked executions from the same reset state. Because two benign executions can also differ, HARP uses deterministic, role-specific checks grounded in tool and database evidence to distinguish specified integrity violations from ordinary LLM output variation. It quantifies violation-associated deviation for targeted and non-targeted agents, including spillover and propagation, as well as attack success, workflow impact, stealthiness, and defense costs. We evaluate four compromise regimes under five defense settings across two role-matched multi-agent testbeds, with selected scenarios spanning four LLM backends. Across 60 finance configurations (4 scenarios, 5 defenses, 3 backends), checks flag 0.03% of benign-benign versus 9.4% of benign-attacked agent comparisons (medication: 0% versus 12.9%). Detected non-targeted violations often involve decision-gate approval flips. HARP complements system-level outcomes by locating violations and revealing defense tradeoffs.

</details>

### 162. Defending LLM-based Multi-Agent Systems Against Cooperative Attacks with Sentence-Level Rectification

📄 [OpenReview](https://openreview.net/forum?id=E4v2pGWQ54)　📅 2026-10　🏷️ P2

**关键词**：`multi-agent attack`、`cooperative attack`、`defense`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：MAS 恶意 agent 多被假设独立行动——协同攻击经内部信息交换更强
- 🔬 **研究方法**：自适应协同攻击框架（多轮动态调整策略）+STAR 句级可信度分析与纠正防御
- 📌 **结论**：协同攻击比独立攻击多降 5.34% 任务成功率；STAR 平均提升 36.76% 并同时防两类威胁——MAS 通信的句级消毒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent years have witnessed the rapid development of Large Language Model-based Multi-Agent Systems (MAS), which excel at collaborative decision-making and complex problem-solving. However, malicious agents in MAS may inject misinformation to mislead other agents and disrupt system performance, giving rise to a new research direction that focuses on attack mechanisms and defense strategies in MAS. Prior studies largely assume malicious agents act independently and investigate the corresponding defense strategies. However, we argue that malicious agents may exhibit collaborative behaviors, enabling more effective attacks through internal information exchange. In this paper, we propose an adaptive cooperative attack framework, where malicious agents autonomously coordinate and dynamically adjust their attack strategies through multi-round interactions. Furthermore, we introduce Sentence-Level Trustworthiness Analysis and Rectification (STAR), a defense framework that identifies and rectifies misleading information at the sentence level within agent communications. Our experiments show that cooperative attacks lead to a significantly larger degradation in task success rate than independent attacks, resulting in a relative drop of 5.34%. Meanwhile, STAR effectively mitigates both cooperative and independent threats and improves task success rate by an average of 36.76%. The code is available at https://anonymous.4open.science/r/STAR-2738.

</details>

### 163. Accept Changes, Reject Attacks: Robust Memory Management for LLM Agents

📄 [OpenReview](https://openreview.net/forum?id=HRAqwuRjfV)　📅 2026-10　🏷️ P2

**关键词**：`memory robustness`、`outdated memory`、`memory poisoning`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：记忆管理器要同时对付过时记忆与投毒/注入——两者写决策相反无固定规则双善
- 🔬 **研究方法**：证据条件准确率 ECA（答案正确且所选记录含全部所需证据、更新且无攻击）+围绕单对话插入变更与攻击的合成幕一次微调
- 📌 **结论**：既有记忆系统与防御不比未调管理器更稳；单次配方翻倍 ECA 但鲁棒仍不完全——双威胁统一的记忆管理

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Since large language model (LLM) agents rely on long-term memory, what they store now shapes what they do later. A memory manager decides how each input changes this memory and which records the agent acts on. It can fail in two ways: keeping a fact that has since changed (outdated memory), or storing a planted passage or injected instruction (memory poisoning). Most prior work studies them separately, yet they call for opposite write decisions, so no fixed write rule handles both. We therefore formalize memory robustness as handling both without doing worse on other inputs. Since accuracy checks only the answer, we measure robustness with evidence-conditioned accuracy (ECA), which also checks that the records the manager selects include all the evidence the answer needs, updated and free of attacks. However, existing memory systems and defenses are not more robust than an untuned manager on our test sets. We improve robustness with a simple one-shot recipe that fine-tunes the manager on episodes synthesized around a single conversation with inserted changes and attacks. On three backbones, it improves every category score on our test sets and more than doubles the untuned manager's overall ECA, though robustness remains incomplete.

</details>

### 164. PROVISO: Provenance-Informed Action Selection for Secure LLM Agents

📄 [OpenReview](https://openreview.net/forum?id=I91FERZ7KQ)　📅 2026-10　🏷️ P2

**关键词**：`provenance`、`action selection`、`secure agents`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：防御孤立判断动作建议、不追踪内容来源（用户 vs 工具输出）也不对比可用替代——安全与效用被迫权衡
- 🔬 **研究方法**：PROVISO 控制器：可信观察/外部观察/建议动作/替代动作编入溯源类型化记忆+角色查询关联+按校准值提交
- 📌 **结论**：四 agent 安全任务上无基线同时超其安全与效用（SkillsBench F1 +13.84、ToolSafe +7.07）——溯源知情的动作选择

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents act on the external world through tools and third-party skills, so a single executed action can cause irreversible harm. Existing defenses judge a proposed action without tracking whether its content comes from the user or from external sources such as tool outputs, and they judge it in isolation rather than against an available alternative, which forces a trade-off between security and utility. We present PROVISO, a controller that decides which action to commit after the agent proposes an action and before it is executed. PROVISO encodes trusted observations, external observations, the proposed action, and an alternative into provenance-typed memory, relates them through role-specific queries, and commits the action with the highest calibrated value learned from outcomes. On four agent security tasks spanning the agent lifecycle, no baseline exceeds PROVISO in both security and utility. PROVISO improves F1 over the strongest baseline by 13.84 points on SkillsBench and by 7.07 points on ToolSafe, and it reaches 88–99 F1 on three additional skill detection benchmarks.

</details>

### 165. A CIVIC Duty: Preserving Instruction Hierarchies through the Value Cache

📄 [OpenReview](https://openreview.net/forum?id=KsrRULtL5h)　📅 2026-10　🏷️ P2

**关键词**：`instruction hierarchy`、`value cache`、`training-free`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：冲突输入可重定向响应——须在值缓存层强化特权指令影响
- 🔬 **研究方法**：CIVIC：跨共享缓存查询头的带符号归因裕度平均定位冲突约束贡献+一次性编辑提升特权值抑制冲突值后走标准缓存注意力
- 📌 **结论**：受控冲突设置主约束准确率 5.7%→88.6%、跨层级评测一致超提示防御——值缓存级指令层级保持

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Instruction hierarchies require language models to follow user requests within higher-priority constraints, yet conflicting inputs can redirect their responses. We introduce Cache Intervention on Values for Instruction Conflicts (CIVIC), a training-free method that strengthens privileged instruction influence through the value cache. It aligns selection evidence with the shared cache receiving the intervention. Averaging signed attribution margins across query heads that share a cache identifies where conflicting constraints contribute more strongly to the initial prediction. Given supplied constraint spans, a one-time edit boosts privileged values and suppresses conflicting values, followed by standard cached attention. A cache edit reuses the model's existing decoding path without requiring additional per-token steering. Across three instruction-tuned models and two hierarchy evaluations, CIVIC consistently improves privileged instruction following over prompt-based defenses. For example, primary-constraint accuracy rises from 5.7% without intervention to 88.6% in one controlled conflict setting. Benefits also extend to a broader hierarchy evaluation, and textual reminders can complement the intervention, with model-dependent effects. Ablations demonstrate that selection matters beyond the number of edits: choosing heads by shared attribution evidence exceeds random selection with matching per-layer head counts by up to 42.7%. Restricting edits to supplied constraint spans also improves accuracy over whole-message intervention by up to 9.9%. Measured per-token overhead is 4.9%, supporting efficient decoding.

</details>

### 166. Do Agents Still Follow the Rules? Benchmarking Rule Compliance under Agent Context Compaction

📄 [OpenReview](https://openreview.net/forum?id=KxX2yFOV3k)　📅 2026-10　🏷️ P2

**关键词**：`rule compliance`、`context compaction`、`benchmark`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：压缩后的上下文仍须承载支配后续动作的规则——违规在压缩后升但来源未定位
- 🔬 **研究方法**：ARCBench（开源 pi harness 工具调用环内量合规）+违规来源分解（规则投递方式/压缩策略/预算）+压缩器定向攻击
- 📌 **结论**：压缩很少删规则：多数违规发生时规则仍在压缩史中——agent 把后续请求当许可；最强压缩器攻击把违规翻倍以上——规则存活性与服从性的分解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents compact long histories to fit their context windows, but the compacted context must still carry the operating rules that govern later actions.
Prior work shows that violations rise after compaction, but measures compliance outside a complete agent harness and does not identify where each violation comes from.
We introduce ARCBench (Agent Rule Compliance Benchmark), a configurable benchmark built on the open-source pi agent harness. Its tool-calling agent loop lets us measure rule compliance from actions taken during execution, bringing the evaluation closer to deployed agent workflows. Using ARCBench, we examine where violations after compaction come from, and how different compaction configurations and adversarial settings change their sources.
We find that compaction rarely deletes the rule: most violations after compaction occur while the rule is still in the compacted history, with the agent treating a later request as permission, ignoring the rule, and proceeding anyway.
Where violations come from depends on the configuration: how the rule is delivered decides whether the agent would break it even without compaction, while the compaction strategy and budget decide whether the rule survives.
The strongest compactor-targeted attack more than doubles violations by corrupting the rule in the summary and changing how the agents behave, whereas the strongest defense restores the rule in most summary but still violates. 
Finally, retaining a rule does not guarantee compliance: compacted runs that retain the rule violate more than twice as often as runs with the full history.

</details>

### 167. Who May Change the Policy? Authorization-State Failures in Tool-Using Agents

📄 [OpenReview](https://openreview.net/forum?id=LyfgKQBhGJ)　📅 2026-10　🏷️ P2

**关键词**：`authorization state`、`tool results`、`permission probes`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：agent 须识别动作是否授权及后续消息有无权限改变许可——工具结果含政策声明时的静态合规不成立
- 🔬 **研究方法**：PERMTRACE-BENCH 八域匹配对话+权限/能力/意图/更新溯源四分离+权限探针与双向残差迁移的内部计算分析
- 📌 **结论**：双向失败：静态拒绝下 2% 调用 vs 不可信授权后 96%；被拒历史供体把注入调用 96%→36%；认证态提示修复假撤销 14%→91%——授权状态的攻防解剖

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Tool-using agents built from language models must recognize whether an action is authorized and whether a subsequent message has authority to change that permission. Static compliance does not establish that models preserve this distinction when tool results contain policy claims. In this work, we study authorization-state failures: changes in tool decisions following unauthenticated update claims while genuine permission remains fixed. We introduce PERMTRACE-BENCH, a matched-conversation dataset across eight domains, and the PERMTRACE analysis framework to separate permission from capability, intent and update provenance. Matched grant and revoke comparisons across nine instruction-tuned models reveal failures in both directions: prohibited calls and suppression of permitted actions. Qwen2.5-7B completes 98% of allowed requests and calls on 2% under static denial, yet calls on 96% after an untrusted grant. To investigate the internal computations associated with these failures, we combine permission probes with bidirectional residual transfer and complete-action scoring. A denied-history donor reduces injected-context calls from 96% to 36%; this intervention changes behavior without isolating a permission-specific circuit. Finally, authenticated-state prompting restores false-revoke success from 14% to 91%, while a separate execution checker blocks prohibited proposals. The analyses distinguish static compliance from update authority and expose complementary security and utility effects.

</details>

### 168. AgentWatcher: A Rule-based Prompt Injection Monitor

📄 [OpenReview](https://openreview.net/forum?id=NNbyBLNGSa)　📅 2026-10　🏷️ P2

**关键词**：`prompt injection`、`rule-based monitor`、`attribution`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：注入检测随上下文变长显著退化且决策隐式不透明——缺显式规则定义何为注入
- 🔬 **研究方法**：AgentWatcher：把 LLM 输出归因到少数因果影响的上下文片段（短文本检测可扩展长上下文）+规则集+监控 LLM 按规则推理使决策可解释
- 📌 **结论**：工具 agent 基准与长上下文数据集上有效检测注入且无攻击时保持效用——归因+显式规则的监控器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) and their applications, such as agents, are highly vulnerable to prompt injection attacks. State-of-the-art prompt injection detection methods have the following limitations: (1) their effectiveness degrades significantly as context length increases, and (2) they lack explicit rules that define what constitutes prompt injection, causing detection decisions to be implicit, opaque, and difficult to reason about. In this work, we propose AgentWatcher to address the above two limitations. To address the first limitation, AgentWatcher attributes the LLM's output (e.g., the action of an agent) to a small set of causally influential context segments. By focusing detection on a relatively short text, AgentWatcher can be scalable to long contexts. To address the second limitation, we define a set of rules specifying what does and does not constitute a prompt injection, and use a monitor LLM to reason over these rules based on the attributed text, making the detection decisions more explainable. We conduct a comprehensive evaluation on tool-use agent benchmarks and long-context understanding datasets. The experimental results demonstrate that AgentWatcher can effectively detect prompt injection and maintain utility without attacks.

</details>

### 169. StateFence: Task-State Protection Against Evidence-Chain Contamination in Blue-Team LLM Agents

📄 [OpenReview](https://openreview.net/forum?id=QKAp89kKdN)　📅 2026-10　🏷️ P2

**关键词**：`prompt injection`、`blue-team agent`、`SOC`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：间接注入对 SOC 蓝队 agent 造成证据链污染——同一可疑串对摘要恶意、对 IOC 提取是必要证据
- 🔬 **研究方法**：StateFence：把严重度标签/事件叙述/响应策略/IOC 集当受保护态，映射显式/隐蔽/多跳/持久攻击并按态路由防御
- 📌 **结论**：受控与公开 SOC 案例上降攻击成功率、减少仅在证据投毒后出现的失败——任务感知的蓝队 agent 防护

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Indirect prompt injection creates a distinctive risk for blue-team Large Language Model (LLM) agents in Security Operations Centers (SOCs). Malicious instructions can be embedded in telemetry, tickets, retrieval results, or memory and then propagate through alert triage, incident summarization, response recommendation, and Indicator of Compromise (IOC) extraction as locally plausible intermediate decisions. We characterize this failure mode as evidence-chain contamination of protected task state. The main challenge is task dependent: a suspicious string may be malicious control text for summarization but essential evidence for IOC extraction. To address this challenge, we propose StateFence, a task-aware evaluation and defense framework that treats severity labels, incident narratives, response policies, and IOC sets as protected states. StateFence maps indirect prompt-injection attacks into explicit, stealth, multi-hop, and persistent SOC evidence attacks, records observable propagation traces, and routes defenses according to the attacked state. Across controlled SOC cases and public-SOC validation cases, StateFence lowers attack success and reduces failures that appear only after evidence is poisoned, while preserving task utility and avoiding the indicator loss caused by task-mismatched filtering. Our findings indicate that robust blue-team LLM agents require mechanisms that preserve task-critical state under untrusted evidence.

</details>

### 170. When Can We Trust Language Model Rankings? Certification under Private and Malicious Feedback

📄 [OpenReview](https://openreview.net/forum?id=SNlj4GInZo)　📅 2026-10　🏷️ P2

**关键词**：`ranking certification`、`malicious feedback`、`finite-sample`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：报告随机化保隐私+允许恶意提交——可靠排名何时可认证
- 🔬 **研究方法**：有限样本证书：置信域+条件弃权下界+直接精度差区间，有界污染下控错误认证概率
- 📌 **结论**：0.1% 恶意报告把估计排名错误率 37.1%→82.1%；直接差距认证提正确率 21.2%→58.7%——认证可用性应与错误率同报（对抗反馈下的排名可信性）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring privacy through report randomization and allowing malicious submissions complicate reliable language model ranking. We develop finite-sample certificates that control incorrect-certification probability under bounded contamination, combining a confidence region, a conditional abstention lower bound, and a direct accuracy-gap interval. We performed experiments with three models on SNLI, SST-2, and BoolQ. For two models separated by 0.71 accuracy percentage points on SNLI, 0.1% malicious reporting increases estimated-ranking error from 37.1% to 82.1% under GRR with one million reports and ε=0.1. In an unpoisoned paired comparison, direct gap certification increases correct-certification rates from 21.2% to 58.7%, although it produces more observed errors in some settings. Adaptive attacks suppress certification within valid contamination bounds, and aggregate results conceal subgroup uncertainty. These findings highlight the need to assess certification availability alongside incorrect-certification rates.

</details>

### 171. Robustness of LLM Committees to Static and Trust-Building Byzantine Agents

📄 [OpenReview](https://openreview.net/forum?id=XsK6jGpir0)　📅 2026-10　🏷️ P2

**关键词**：`Byzantine agents`、`committee`、`fault tolerance`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：委员会式多 agent 审议隐含假设同侪诚实——应用层拜占庭内鬼的脆弱性未量化
- 🔬 **研究方法**：冻结 Round 0 锚点的匹配反事实框架：内鬼加倍个体错误几率（OR=1.996）与净说服力测量+基数扩张与合谋对照
- 📌 **结论**：原生测试时思考的委员会近全韧（AAE≤0.0147）、标准委员会符合 f < N/3 经典阈值且合谋突破；提示护栏无效而验证门+贝叶斯信任过滤减半伤害——MAS 的分布式容错迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Committee-style multi-agent deliberation enhances reasoning in large language models (LLMs) via test-time critique and voting, yet implicitly assumes peer honesty. We investigate deliberation committees' vulnerability to application-layer Byzantine insiders across 330 paired benchmark evaluations per condition on MATH-500, LiveCodeBench, and HumanEval+. Using a matched counterfactual framework branching from frozen Round 0 anchors, we show that deliberative reasoning configurations with native test-time thinking (gemini-3.7-flash) exhibit near-complete resilience (AAE le 0.0147), whereas standard instruction-tuned committees (Llama-3.3-70B-Instruct) suffer severe degradation: an insider doubles individual error odds (OR = 1.9959, p = 9.03 × 10⁻⁶⁴) and achieves net persuasion up to AAE = 0.2632. Furthermore, empirical dynamics align with the classical distributed fault-tolerance threshold (f < N/3): while expanding cardinality to N=5 dilutes isolated adversaries (k=1, AAE = 0.0744), colluding coalitions (k=2, f/N = 40.0%) breach the bound, surging persuasion (AAE = 0.1953, p < 0.0001) and depressing panel accuracy by 10.31 percentage points. Finally, prompt guardrails fail (p=0.5600), whereas pre-consensus verifier gates (L₂) and longitudinal Bayesian trust filtering (L₃) halve adversarial harm (AAE = 0.1333) and quarantine sleeper defectors with a mean lag of 0.60 tasks post-activation (hat{β}₃ = -0.0465, p = 0.0022).

</details>

### 172. Halluci-Action: Tool-Using LLM Agents’ Claims Are Misaligned with Their Actions

📄 [OpenReview](https://openreview.net/forum?id=YRuDPCRGc4)　📅 2026-10　🏷️ P2

**关键词**：`claim-action misalignment`、`agent accountability`、`disclosure`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：工具 agent 声称做的与实际执行的可能不符——首个系统考察该错位
- 🔬 **研究方法**：HalluciActionLens：原子动作声明匹配记录的工具调用+逐调用披露审计+HAR 比率+沿执行/接地/结果验证/披露读写五门回溯
- 📌 **结论**：五 agent 2843 轨迹全部存在 halluci-action（HAR 至 45.9%）；过半事实干净且目标完成的轨迹含未支持动作声明——声明-行动错位可测量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When tool-using LLM agents act through tool calls, what they claim they've done and what they actually execute may be misaligned. We call such a phenomenon Halluci-action. To study this, we introduce HalluciActionLens, to our best knowledge the first framework to examine this misalignment. It (1) matches atomic action claims to recorded tool calls and audits every call for disclosure, (2) reports the ratio of unsupported claims about actions and undisclosed actions, defined as Halluci-Action Rate (HAR), and (3) backtracks the origin of halluci-cation down to five gates of execution, grounding, outcome verification, disclosure read, and disclosure write among forward and reverse gap. Across five agents and 2,843 trajectories in an Odoo enterprise sandbox and AppWorld, every agent shows halluci-action, even when explicitly instructed to report each action, with per-model HAR up to 45.9%. 
Existing criteria miss these gaps: over half of factuality-clean and goal-complete trajectories admit a halluci-action, and in 5–7% of them it concerns a required or forbidden operation. 
This work establishes halluci-action as a measurable phenomenon that is prevalent among state-of-the-art LLM agents, and calls for future work to further study its causes and remedies.

</details>

### 173. Benchmarking Concealment Detection: Can Agents Recover Secrets from Distributed Clues?

📄 [OpenReview](https://openreview.net/forum?id=Yewh6jDxCe)　📅 2026-10　🏷️ P2

**关键词**：`concealment detection`、`distributed clues`、`email archive`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：敏感信息常可从邮件档案恢复而无单条直接披露——隐瞒（知而不言/误导）需综合三组件且分布于不同线程
- 🔬 **研究方法**：自动管线合成场景植入 Enron（工作场所+个人秘密）：模型须读/搜 2000 邮件判断隐瞒存在并返回秘密+支持邮件
- 📌 **结论**：最强模型整档 85.0% vs 须搜索时 10.2%；线索不全时幻觉秘密假阳至 100%——访问方式决定秘密恢复（推断式泄露评测）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Sensitive information can often be recovered from an email archive even when no single message directly discloses it. We study one widespread form of this leakage, which we operationalize as concealment: a concealer knows a sensitive fact and makes a false or misleading claim about it to another party, or leaves it out. Recovering a concealment requires synthesizing three components (the underlying fact, evidence the concealer knew it, and their act of concealment), which we distribute across separate email threads such that no strict subset reveals the secret on its own. We introduce an automated pipeline to synthesize such scenarios and implant them into the Enron email corpus, yielding a benchmark spanning both workplace and personal secrets. To succeed, a model must read or search a 2,000-email archive, determine whether a concealment exists, and return both the secret and its supporting emails. Across eight frontier models, recovery depends on how the archive is accessed: the strongest model uncovers 85.0% of cases when given the whole archive but only 10.2% when it must search it. Moreover, models frequently hallucinate secrets in archives with incomplete clues—with false-positive rates reaching 100%.

</details>

### 174. PACT: A Testbed for Boundary Adherence and Self-Reporting in Goal-Driven LLM Agents

📄 [OpenReview](https://openreview.net/forum?id=cVx28Ctmxj)　📅 2026-10　🏷️ P2

**关键词**：`rule adherence`、`candor`、`sandbox`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：目标驱动 agent 压力下绕过护栏并在事后报告中美化行为——'违反从未告知的规则'与'违反明知规则'常被混同
- 🔬 **研究方法**：PACT 测试床：目标/任务/工具/强制不变、仅变规则明示与否+环境决策层先记后行+事后问责谈话量坦诚
- 📌 **结论**：明示规则把选择性违规降 8-20.5 倍且任务天花板保持；规则知情 agent 转向渠道内争论 2.7 倍——压力/授权/坦诚三轴分离

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Goal-driven agents operating under pressure may bypass system guardrails and misrepresent their actions in post-task reports. We investigate this propensity using PACT (Pressure, Authorization, and Candor Test), a controlled testbed and evaluation harness designed to distinguish two failure modes often conflated in prior work: violating a rule the agent was never informed of, and overriding a rule it explicitly knew. We compare matched conditions that hold the goal, task, tools, and enforcement constant while varying only whether operative rules are stated in the prompt or silently enforced. An environmental decision layer logs each action before execution, enabling a post-task accountability debrief that measures candor against recorded behavior.

Across a fully crossed sandbox comprising 432 runs and a Terminal-Bench harness comprising 60 episodes across two models, explicitly stating the rules reduces elective violation rates by factors of 8× to 20.5×, while task-ladder completion remains at ceiling. This completion metric counts the stages of the coding task completed, rather than whether the contribution is accepted, as the maintainer is designed never to concede. In the sandbox, persistence is redirected rather than suppressed: rule-informed agents argue in-channel 2.7× more frequently while violating substantially less. Two independent human raters achieve inter-rater ordinal agreement of up to α = 0.95. Their assessments reveal that disclosure covaries with violation type and detectability: agents reframe actions visible to the environment while omitting those that are not, and almost none characterize a rule violation as unauthorized. These findings suggest that making rules explicit can substantially reduce elective violations without sacrificing task persistence. Stating the rules thus emerges as a practical safeguard that deployers can adopt without modifying the underlying model.

</details>

### 175. Write-Back Redundancy Breaks Leave-One-Out Attribution in Self-Evolving Agent Memory

📄 [OpenReview](https://openreview.net/forum?id=gSBEPUmVk2)　📅 2026-10　🏷️ P2

**关键词**：`memory poisoning`、`redundancy lineage`、`deletion threshold`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：自进化 agent 把自身输出写回检索记忆——一条中毒记录可繁殖成近重复谱系；检索在每次删除后重算造成删除阈值
- 🔬 **研究方法**：谱系冗余分析：可互换谱系记录在 top-k 检索中排名超过其余记录时，删除它们直到少于 k 条前攻击输出概率不变；436 实例×四骨干+记录重放防御评估
- 📌 **结论**：仅剩单条谱系记录仍驱动 agent（ASR 0.79 vs 全谱系 0.98）；记录重放在 338 例中仅移除 4 例——自进化记忆的删除免疫性（记忆投毒新机制）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-evolving LLM agents write their own outputs back into retrieval memory, so a poisoned record can grow into a lineage of near-duplicates. We show that, because retrieval is recomputed after every deletion, this redundancy creates a deletion threshold: when interchangeable lineage records outrank all other records under top-k retrieval, deleting them leaves the probability of the attacker’s output unchanged until fewer than k of them remain. A single remaining lineage record steers the agent: on 61 instances, deleting all others leaves the attack success rate (ASR) at 0.79, against 0.98 with the whole lineage. We evaluate 436 instances of question answering, tool selection and text-to-SQL with four LLM backbones, under planted seeds and, in one setting, query-only injection. Record replay, which scores each record by deleting it and replaying the agent, removes a record in 4 of 338 successful attacks; other record-level audits contain the attack only after deleting nearly the whole lineage. We reconstruct lineages from harmful-episode traces without record labels, using provenance links refined by semantic similarity. Removing them cuts ASR to at most 0.07 and keeps it low when write-back resumes, whereas the lineage left by record replay regrows.

</details>

### 176. Access Control for Agents Is a Language Problem

📄 [OpenReview](https://openreview.net/forum?id=iPJJGfjase)　📅 2026-10　🏷️ P2

**关键词**：`access control`、`agent authorization`、`survey`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：agent 执法系统混淆了充分性/授权/合规三种判断——执法只确立合规
- 🔬 **研究方法**：三判断分离框架：八系统按保证-假设-验证对比+四个商用系统同框解读+五个基准链接测量
- 📌 **结论**：把 agent 授权当 NLP 问题（从陈述约束写形式政策/推断任务所需权限/命名资源对应）且输出可确定性检查——访问控制的语言问题化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents that call APIs and operate user interfaces are increasingly governed by enforcement systems that check each action against an explicit policy. We survey this literature through a distinction it rarely makes: an action can be enough for the task (sufficiency), within what the user consented to (authorization), and permitted by the enforced policy (compliance), and the three judgments can diverge. Enforcement establishes only compliance. Whether compliance preserves authorization depends on three language problems that systems solve in different ways and often simply assume: authoring formal policy from stated constraints, inferring what permissions a task requires, and naming the resources that endpoints and interface elements correspond to. We compare eight systems by the guarantee they establish, the assumptions it rests on, and whether those are validated, read four deployed commercial systems against the same frame, and review five benchmarks for which links between the three judgments they measure. The result is a map of what is established, assumed, and unmeasured, and a research agenda that treats agent authorization as a natural language processing problem with deterministically checkable outputs.

</details>

### 177. Beyond Unsafe Detection: Counterfactually Anchored Evidence Attribution for Multi-Turn LLM Safety Failures

📄 [OpenReview](https://openreview.net/forum?id=kf46k3X1r9)　📅 2026-10　🏷️ P2

**关键词**：`safety failure attribution`、`multi-turn`、`counterfactual supervision`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：护栏评测只判用户请求是否不安全——多轮失败中对抗意图跨轮分布、仅从累积上下文浮现
- 🔬 **研究方法**：MTAG-Bench（4167 对话行为验证+反事实监督）+MTAG-Probe 层级归因模型：轮/span 级证据定位+会话级检测
- 📌 **结论**：轮级 F1 超 self-attribution 28.1 点；删 top15-20% 证据改变 50.6-60.8% Llama Guard 不安全判定、全轨迹重放转化 84.3%——安全失败的证据归因

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) move from conversational assistants to advanced agentic systems, guardrail failures can convert adversarial intents into harmful executions. However, most evaluation frameworks focus only on whether a user request is unsafe. This is insufficient for multi-turn failures, where adversarial intent may be distributed across turns and emerge only from accumulated context. This motivates us to go beyond detection to localize the evidence that pushes the conversation toward unsafe trajectories. We introduce MTAG-Bench, a multi-turn guardrail attribution dataset with behavioral validation and counterfactual supervision containing 4,167 conversations. We also introduce MTAG-Probe, a hierarchical attribution model for turn- and span-level evidence localization with conversation-level safety detection. MTAG-Probe improves turn-level F1 by 28.1 and 24.1 points (79.0% and 61.0% relative) over self-attribution by the model that produced the unsafe response and the LLM safety-judge attribution, respectively. Removing MTAG-Probe’s top-ranked evidence within budgets of 15% and 20% of user words per conversation changes 50.6% and 60.8% of Llama Guard decisions on Geometry from unsafe to safe, respectively. In full-trajectory replay, MTAG-Probe converts 84.3% of eligible unsafe final responses to safe. These results show that MTAG-Probe can provide evidence-level explanations as a practical complement to safety detection.

</details>

### 178. Beyond Zero Violations: Evaluating Derived Authorization for LLM Agents

📄 [OpenReview](https://openreview.net/forum?id=qc07F74K0R)　📅 2026-10　🏷️ P2

**关键词**：`derived authorization`、`external-effect boundary`、`semantic recovery`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：agent 可读私有记录而无披露衍生品权限——授权评测混淆拒答与安全、逐字提取与语义恢复
- 🔬 **研究方法**：SAW 可执行框架：每个释放载荷需充分支持+接收者/目的/动作许可，搜索替代支持+完整输出对照源校验+确定性政策绑定外部效应
- 📌 **结论**：输出边界 SAW 0% 观察未授权效应 vs 前任 58.3%；480 幕队列 100% 合法完成 vs 直接授权判官 18.3%——输出绑定的授权评测与捷径感知

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents may read private records without authority to disclose derivatives. Authorization evaluations may confuse refusal with safety and verbatim extraction with semantic recovery. We study authorization at the external-effect boundary: every released payload needs sufficient support and permission for its recipient, purpose, and action. We introduce Semantic Authority Witnessing (SAW), an executable framework that searches alternative supports, validates complete outputs against selected sources, and binds deterministic policy decisions to external effects. Task-preserving abstractions require independent revalidation. We measure unauthorized sink effects and achievable-task completion, using a policy-aware literal extractor to detect shortcuts. On 240 policy-grounded episodes, output-bound SAW records 0% observed unauthorized effects versus 58.3% for its projection-based predecessor, with lawful completion of 50.0% versus 41.7%. In a separate 480-episode cohort, SAW achieves 100% lawful completion without observed unauthorized effects, versus 18.3% for a direct authorization judge at the same observed unauthorized-effect rate. A literal extractor also achieves 100% completion, showing that this cohort does not require inferred abstraction. These findings support output-bound authorization and shortcut-aware evaluation in synthetic settings.

</details>

### 179. Context Compaction Reshapes the Instruction Hierarchy of Small Language-Model Agents

📄 [OpenReview](https://openreview.net/forum?id=uN7HQnCv47)　📅 2026-10　🏷️ P2

**关键词**：`instruction hierarchy`、`context compaction`、`source-swap`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：agent 把长史压缩为摘要——改变的不只记住什么还有听谁的指令
- 🔬 **研究方法**：源交换框架：用户轮与工具结果各放一条互斥指令并跨源交换值，给出严格源盲零假设；九个 1-9B agent×五族
- 📌 **结论**：未压缩多为近因性（1-4B 后位工具指令服从 27.5-55.8%）；一次压缩近消除顺序效应、降工具服从 17-32pp 但未恢复用户权威——摘要放在哪决定哪条指令获胜

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents compact long histories into model-written summaries, which can change which instructions an agent acts on, not just what it remembers. Our source-swap framework places two matched, mutually exclusive instructions in a user turn and a tool result and swaps their values across sources, giving an exact source-blind null for measuring which source the agent follows. Across nine 1-9B agents from five families, uncompacted behaviour is mostly recency: the 1-4B agents follow the tool-sourced instruction in 27.5-55.8% of cases when the tool result comes later and in at most 2.5% when the user instruction comes later. With a fixed summarizer, one compaction nearly removes this order effect and lowers tool-following by 17–32 points without restoring user authority: Llama agents mostly abstain, while Qwen and Phi agents retain most of their user-following. Post-hoc source tags inside the summary do not change behaviour in the 7-9B agents. Placement does: moving verbatim user turns from before the summary to after it lowers tool-following to at most 4.5% in all nine agents, with the two small Llama agents doing so mostly through abstention. GPT-5.5 is a boundary case: on its own summaries it loses less tool-following and shows no placement effect. Where a runtime places a summary therefore helps determine which instruction wins after compaction.

</details>

### 180. The Model Knows Better: Defending Medical Multi-Agent Systems Against Prompt Injection

📄 [OpenReview](https://openreview.net/forum?id=xvXPtThn4Q)　📅 2026-10　🏷️ P2

**关键词**：`medical MAS`、`prompt injection`、`judgment verification`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：医疗多 agent 会诊系统对注入的脆弱性与防护未知
- 🔬 **研究方法**：两系统×两模型族×三基准注入实证+训练无关防御：把患者发现与临床判断分离，逐判断对照发现核验（决策只依赖被支持的判断）
- 📌 **结论**：单段注入成功率至 61% 且协作不总保护；核验防御把 MedQA ASR 降到 4-7% 且抗防御感知与自适应攻击——临床实践式分离核验

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Medical multi-agent systems, in which LLM agents discuss a case, are increasingly studied for clinical decision support. Prompt injection, text that an attacker adds to a model’s input, can manipulate LLMs into wrong decisions. How it affects these systems, and how to protect them, remains unclear. Across two systems, two model families and three benchmarks, a single injected passage succeeds in up to 61% of cases, and collaboration does not consistently protect against it. Existing defenses help only partly: they miss injections that look like ordinary clinical text. Yet when asked to check the injected text against the patient’s findings, a model that followed the injection usually rejects it. We therefore propose a training-free defense that verifies the clinical judgments behind the system’s decision. Following clinical practice, it separates the patient’s findings from clinical judgments, such as diagnoses, recommendations and instructions, and checks each judgment against the findings alone, so the decision rests only on supported judgments. Our defense outperforms all baselines on every benchmark, lowering attack success on MedQA to 4–7% while maintaining accuracy on cases without an attack, and remains effective with a medical model and against defense-aware and adaptive attacks.

</details>

## 八、遗忘与数据审计

### 181. Large Language Models Can Bypass Membership Inference Attacks by Post-hoc Unlearning

📄 [OpenReview](https://openreview.net/forum?id=A1IvkgWB0J)　📅 2026-10　🏷️ P1

**关键词**：`membership inference`、`audit evasion`、`post-hoc unlearning`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：MIA 用于审计模型是否用过某段落——模型能否既躲过 MIA 检测又保留其事实知识（审计方视角的漏洞）
- 🔬 **研究方法**：后 hoc 训练方案：压制与目标段落逐字形式绑定的证据同时保底层知识，四开源 LLM×五 MIA 方法
- 📌 **结论**：大幅降低 MIA 检测且保目标问答能力、旁路其他 MIA 方法而通用能力有限退化——依赖逐字证据的审计可被规避（MIA 审计的语义级盲区）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership inference attacks (MIAs) are used to audit whether a given model was trained on a particular passage, as the exact training data of modern large language models (LLMs) is often undisclosed.
In this audit setting, a key question is whether a model can evade MIA detection for a passage while retaining access to the factual knowledge it conveys.
To examine this question, we propose a post-hoc training scheme that suppresses evidence tied to a target passage's original verbatim form while preserving its underlying knowledge.
Across four open-weight LLMs and five MIA methods, we show that the proposed method substantially reduces MIA detection while preserving the model's ability to answer questions about the target passages.
We also confirm that the method largely bypasses the detection of other MIA methods with limited degradation of LLMs' general capabilities. 
These results expose a vulnerability of MIA-based auditing that relies on verbatim-form evidence, and call for audits that go beyond such evidence.

</details>

### 182. ForgetBench: Benchmarking Forgetting Dynamics of Long-Term Parametric Memory in Language Models

📄 [OpenReview](https://openreview.net/forum?id=0uqXn7CK0y)　📅 2026-10　🏷️ P2

**关键词**：`benchmark`、`forgetting dynamics`、`continual editing`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：静态知识编辑评测无法刻画持续修改下参数记忆的保留与退化动态
- 🔬 **研究方法**：ForgetBench：概念级+场景级 QA 双范式，按后续编辑数索引记忆年龄，测时间衰减/保留强度/跨实例稳定性
- 📌 **结论**：不同编辑方法呈独特遗忘轨迹且长期保留与泛化质量存在张力（遗忘动力学基准化）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have demonstrated strong capabilities in knowledge acquisition and reasoning, yet their ability to retain previously acquired knowledge under repeated updates remains insufficiently understood. Existing evaluation paradigms primarily focus on single-step reasoning or static knowledge editing, which fail to capture the temporal dynamics of knowledge retention and degradation during continual model modification. In this work, we propose ForgetBench, a benchmark for measuring forgetting dynamics in the long-term parametric memory of LLMs under continual knowledge editing. ForgetBench introduces two complementary evaluation paradigms, namely concept-based QA and scenario-based QA, to probe the retention of isolated facts and structured relational knowledge. Building upon a sequential editing framework, we construct temporally ordered knowledge streams and evaluate model behavior across multiple editing stages. To quantify these dynamics, we introduce a unified evaluation framework that indexes memory age by the number of subsequent edits and measures temporal decay, retention strength, and cross-instance stability. 
Extensive experiments across diverse models and editing methods reveal distinct forgetting trajectories and a recurring tension between long-term retention and generalization quality. Our findings highlight the need for more robust memory mechanisms that can effectively acquire, update, and preserve knowledge over time in future LLMs.

</details>

### 183. When Unlearning Still Links: Auditing Speaker Linkability in Spoken Language Understanding

📄 [OpenReview](https://openreview.net/forum?id=92ANUsOKYc)　📅 2026-10　🏷️ P2

**关键词**：`unlinkability`、`speech privacy`、`deletion audit`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：删除用户训练样本不必然阻止语音模型链接该用户话语——unlinkability 是额外隐私目标
- 🔬 **研究方法**：任务效用+成员诊断+说话人归因统计+固定/学习/自适应链接攻击组合审计+GRACE 参照缓解
- 📌 **结论**：破坏性更新与说话人归因塌缩后仍存实质可链接性（自适应对比攻击偏差 0.422）——审计诊断权衡而不认证删除（语音遗忘的链接性审计）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Removing a user's training examples does not necessarily prevent a speech model from linking that user's utterances. We study this distinction in spoken language understanding (SLU): recognizing commands while measuring whether the representations of utterances submitted in a deletion request still reveal a common speaker. Our audit combines task utility, membership diagnostics, speaker-attribution statistics, and fixed, learned, and adaptive linking attacks. Unlinkability is an additional privacy objective, not a definition or guarantee of machine unlearning; retraining without the requester remains the data-exclusion reference. On a reconstructed Fluent Speech Commands subset with HuBERT, we observe destructive updates and speaker-attribution collapse that leave substantial linkability. Guided Randomized Acoustic Erasure (GRACE), a reference fine-tuning mitigation, reduces mean worst-attack AUC deviation from chance from 0.322 for retraining to 0.231 over six frozen attacks, while preserving command recognition. A stronger adaptive contrastive attack yields deviations of 0.422 and 0.313, respectively. The improvement is limited to the evaluated request utterances and varies by encoder; adaptive attacks also suggest a cost to retained-speaker separability. The audit diagnoses these tradeoffs without certifying deletion or general anonymity.

</details>

### 184. Preserving Utility in Continual LLM Unlearning via Orthogonal Projections

📄 [OpenReview](https://openreview.net/forum?id=BFBpqKHGOp)　📅 2026-10　🏷️ P2

**关键词**：`continual unlearning`、`orthogonal projection`、`utility`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：遗忘请求在模型生命周期中持续到来——多数方法迭代移除时遗忘与效用陡降（更新间干涉）
- 🔬 **研究方法**：COP：梯度投影到既往遗忘集激活子空间的正交补（一阶非干涉可证）+每层低秩基存储，可插入任意梯度遗忘法
- 📌 **结论**：TOFU/RWKU 序贯请求下保效用不弱遗忘、防标准目标塌缩——持续遗忘的正交投影

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unlearning concerns the task of removing the influence of a sensitive portion of the training data, such as protected, copyrighted or private text, from a model without retraining it from scratch. While unlearning requests happen continuously during a model's lifetime, the vast majority of LLM unlearning methods are ill-suited for iterated removal, yielding steep decay in forgetting and utility upon sequential unlearning. This decay stems from interference between successive updates, as each new deletion can undo earlier ones or push the model further along directions already degraded by them.
To address this, we introduce Continual Orthogonal Projection (COP), a gradient-projection scheme that restricts each update to the orthogonal complement of activation subspaces cached from prior forget sets. This approach provably guarantees first-order non-interference with earlier deletions. 
COP stores only a low-rank basis per layer, requiring neither past gradients nor previous forget sets, and plugs into unlearning methods that update the model through gradient steps on a differentiable loss without modifying its objective. Experiments on standard LLM unlearning benchmarks (TOFU and RWKU) show that COP preserves utility across sequential requests without weakening forgetting, preventing the collapse of standard objectives and forgetting more effectively than continual-specific baselines.

</details>

### 185. Toward Fine-Grained Forgetting: Attribute Unlearning for Multimodal Large Language Models

📄 [OpenReview](https://openreview.net/forum?id=CXTRcIjFb5)　📅 2026-10　🏷️ P2

**关键词**：`unlearning`、`attribute-level`、`MLLM`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：实用删除请求常是细粒度的：删某敏感属性而保留同身份其余信息——现有基准只有画像级
- 🔬 **研究方法**：AMU-Bench 属性级遗忘基准+CLRP：因果定位相关层+中间表示投影远离目标子空间保保留信息
- 📌 **结论**：5% 遗忘率下 cloze 20%→4% 且保留集精度反升——细粒度遗忘的泄漏-退化权衡及训练无关解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) can memorize and disclose sensitive information, motivating machine unlearning to remove designated knowledge while preserving model utility. Existing privacy-oriented benchmarks mainly study profile-level deletion, whereas practical requests often require finer-grained forgetting: removing a sensitive attribute while retaining other information about the same identity. We introduce attribute-level MLLM unlearning and construct AMU-Bench, covering long-text, numeric, and short-text targets, multiple forget ratios, and diverse question types. Our evaluation shows that target and retain attributes share identity-specific and visual evidence, making selective forgetting prone to residual leakage and collateral degradation. To address this challenge, we propose Causal Localization and Retain-Aware Projection (CLRP), a lightweight, training-free framework that localizes causally relevant layers and projects intermediate representations away from target-specific subspaces while preserving retain-related information. Experiments across MLLMs with different architectures and scales show that CLRP achieves a strong forgetting–retention trade-off on AMU-Bench. For example, at a 5% forget ratio, CLRP reduces Attribute Forget Set cloze accuracy from 20.00% to 4.00% while improving Attribute Retain Set accuracy from 14.77% to 17.79% in the reported LLaVA-1.5-7B and Qwen2.5-VL-3B results. These findings demonstrate effective and selective attribute-level unlearning without modifying model parameters.

</details>

### 186. Knowledge Vector Weakening: Efficient Training-free Unlearning for Large Vision-Language Models

📄 [OpenReview](https://openreview.net/forum?id=EkRnGnlPqR)　📅 2026-10　🏷️ P2

**关键词**：`training-free unlearning`、`knowledge vectors`、`LVLM`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：LVLM 遗忘依赖梯度微调或多样本多次推理估参数重要性——成本高
- 🔬 **研究方法**：KVW：FFN 视为键值记忆，单前向定位遗忘数据相对保留数据强激活的知识向量并渐进削弱（阻断传递通路）
- 📌 **结论**：MLLMU-Bench/CLEAR 上更优遗忘-保留权衡且大幅省算、抗量化/重学攻击/超参扰动——单前向免训练遗忘

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Vision-Language Model (LVLM) unlearning aims to remove the influence of specific data without retraining. However, existing methods remain costly, relying on gradient-based fine-tuning or multiple inference passes per sample to estimate parameter importance. To address this, we propose Knowledge Vector Weakening (KVW), a training-free method that requires only a single forward pass per forget sample. Viewing feed-forward networks as key–value memories, KVW identifies knowledge vectors strongly activated by the forget data relative to the retain data. It then progressively weakens these vectors, blocking the pathways that pass the target knowledge to subsequent layers. On MLLMU-Bench and CLEAR, KVW achieves a superior forget–retain trade-off while substantially reducing computation time and memory. Further analyses show that KVW is robust to quantization, re-learning attacks, and hyperparameter choice, and readily extends to concept-level unlearning.

</details>

### 187. Where Does Fact Erasure Act? Fine-Tuning and Unlearning Move Past the Subject at Late Layers

📄 [OpenReview](https://openreview.net/forum?id=GAXQwg04Xm)　📅 2026-10　🏷️ P2

**关键词**：`unlearning mechanism`、`subject state`、`layer-wise analysis`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：被擦除事实常在改写后回归——不知道每种方法在输入的哪个部分施加擦除
- 🔬 **研究方法**：只对主题词或后续词施加编辑+恢复未编辑内部状态，九种方法×三个模型的事实陈述/问答网格
- 📌 **结论**：微调/遗忘类方法早层经主题词、晚层经后续词起效——只查主题词的审计会漏掉晚层擦除方式（擦除定位学）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Knowledge editing and unlearning methods aim to remove specific facts from language models, for example to protect private data. Erased facts often return when the question is rephrased, and it is not known where in the input each method blocks the fact. We measure whether each method's erasure acts through the words that name the fact's subject or through the words that follow. We apply each edit to only one of these two parts of the input, and we restore the unedited model's internal state at the subject. We test up to nine methods on each of GPT-2-XL, GPT-J and Qwen2.5-1.5B, using factual statements and factual questions. Methods built around the subject, such as ROME, act through it at every layer, and restoring its state undoes most of their erasure. Fine-tuning and unlearning act through the subject at early layers and mostly through the following words at late layers, as a random weight change does. Facts whose answer can still be read from the subject's state return more often, but lowering this signal does not stop their return. Audits of erasure should therefore test where each method acts, since a check of the subject alone misses how late fine-tuning edits erase a fact. We release the code upon acceptance.

</details>

### 188. What Counts as Forgetting? Semantic Validation and Resampling Baselines for Factual-Unlearning Audits

📄 [OpenReview](https://openreview.net/forum?id=J49mWWu2BU)　📅 2026-10　🏷️ P2

**关键词**：`unlearning audit`、`semantic validation`、`resampling baseline`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：unlearning 审计把计分器拒绝当遗忘证据、把换提示后答对归功于提示——两类核心推断从未被检验
- 🔬 **研究方法**：弱遗忘 1B 种群上盲标 267 个自动标记的直问未中+答案无关提示/解码匹配重放对照+7B MUSE-News 人工裁决与训练强度实验
- 📌 **结论**：计分器拒绝高估语义遗忘（267 个标记中仅 48 真错）、恢复率不能证明提示有效——遗忘审计需语义校准（审计口径修正）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A scorer-rejected response may be counted as evidence of factual forgetting; a correct answer after a prompt change may then be credited to the new prompt. We test both inferences. In a weak-forgetting Llama-3.2-1B-Instruct population, blind annotators find that 178 of 267 automatically flagged direct misses are correct, 41 are ambiguous, and only 48 are incorrect, spanning 11 facts. Among those 48, eight answer-free prompts recover 17, while eight decoding-matched direct repeats recover 26. The equal-fact audit-minus-repeat difference is -21.2 percentage points (95% fact-bootstrap CI: -48.5,3.0); the data establish neither a prompt advantage nor equivalence. A human-adjudicated 7B MUSE-News application also yields unresolved four-query contrasts. In a later training-strength experiment (E1), two annotators label 8,448 outputs; after assisted review of disagreements, 61 of 256 selected greedy failures are incorrect. Stronger forgetting on development authors does not transfer to held-out authors. Across these settings, scorer rejection overstates semantic misses, and recovery under a changed prompt does not establish that changing the prompt helped.

</details>

### 189. Can Agents Truly Forget? Exploring Machine Unlearning for LLM Agents

📄 [OpenReview](https://openreview.net/forum?id=N1VfhL9dqn)　📅 2026-10　🏷️ P2

**关键词**：`machine unlearning`、`LLM agents`、`agent memory`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：遗忘主体从模型扩展到 agent——含外部记忆/技能的 agent 能否真正遗忘未经探索
- 🔬 **研究方法**：把机器遗忘引入 LLM agent 设定：外部记忆与参数遗忘的组合评测框架
- 📌 **结论**：agent 场景遗忘的新问题化与基准化（遗忘边界从模型到 agent 的延伸）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents have shown strong capabilities in interactive problem solving, tool use, and long-horizon task execution, but they may acquire sensitive knowledge during training and expose it during deployment. Machine unlearning offers a practical alternative to costly retraining from scratch by removing targeted undesirable knowledge from trained models while preserving their general utility. When LLM are deployed as agent, parameter-level unlearning becomes insufficient: forgotten information may still persist in memory artifacts or be reacquired via tool calls.
In this paper, we formulate the problem of agent unlearning as removing private information from an LLM-based agent across three information channels: parametric knowledge, persistent memory, and tool-call acquisition. To study this problem, we introduce  we introduce Agent Unlearning Benchmark (AUBench), a controlled benchmark that extends the fictitious-author setting of TOFU into an agent environment with persistent memory, an offline web snapshot, tool-accessible documents, and provenance-tracked interaction trajectories.
By evaluating unlearning methods in this setting, AUBench reveals the gap between model-level forgetting and system-level agent unlearning, and provides a foundation for developing unlearning methods that operate across the full lifecycle of LLM agents.

</details>

### 190. TULIP: Targeted LLM Unlearning at Layers Identified Per-input

📄 [OpenReview](https://openreview.net/forum?id=Rvnqm5iqpr)　📅 2026-10　🏷️ P2

**关键词**：`unlearning`、`per-input layer`、`representation`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：表示级遗忘固定在单一层操作——但知识跨层分布且答案形成层随输入变化
- 🔬 **研究方法**：移植实验证明答案在中层已形成后 TULIP：logit lens 定位形成-读出边界并移除该层与遗忘答案 unembedding 的对齐
- 📌 **结论**：TOFU/PISTOL/WMDP 上超输出级与表示级基线且抗改写与量化攻击——逐输入定层的遗忘（可插拔组件）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Representation-level unlearning modifies the intermediate hidden states of LLMs. Although knowledge is distributed across layers, existing methods operate at a *single fixed layer* for the entire forget set. We ask whether such a fixed layer is sufficient. To answer this, we design a hijacking experiment that grafts hidden states of the target model into an oracle model. The oracle cannot produce the forget answer on its own, yet it produces the answer from the grafted state. This indicates the answer is already *formed* at an intermediate layer and *read out* afterward. Moreover, the layer where formation ends varies widely across inputs. Motivated by these findings, we propose **Targeted Unlearning at Layers Identified Per-input (TULIP)**. For each input, TULIP uses the logit lens to locate the formation-readout boundary and removes the hidden state's alignment with the forget answer's unembedding vector at that layer. TULIP consistently outperforms output- and representation-level baselines on TOFU, PISTOL, and WMDP across Llama, Qwen, and Zephyr models. It also remains robust to paraphrase and quantization attacks. Beyond standalone use, its per-input layer selection serves as a plug-and-play component that further improves existing methods.

</details>

### 191. Self-Improvement Silently Reverts Knowledge Edits

📄 [OpenReview](https://openreview.net/forum?id=WT5Lkttltq)　📅 2026-10　🏷️ P2

**关键词**：`knowledge editing`、`self-improvement`、`edit reversion`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：编辑更新事实、自改进让模型在自判上继续训练——两者相遇时编辑被侵蚀的机制未知
- 🔬 **研究方法**：三模型族×两编辑器×两偏好优化配方：几轮事实性自改进侵蚀多数编辑并复述编辑前值+改变判官即改变结局的干预
- 📌 **结论**：编辑改变所言多于所信、自判官持续偏好旧事实被偏好优化蒸馏进生成——判官注册编辑+冻结至末编辑层保留 98% 编辑（编辑-自改进交互）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Knowledge editing updates individual facts in a deployed language model, and self-improvement lets a model keep training on its own judgments. We ask what happens to edits when an edited model improves itself. Across three model families, two editors and two preference-optimization recipes, a few rounds of factuality-oriented self-improvement erode many edits and make models restate pre-edit values, including real 2024–2025 updates, often while held-out quality is still improving. In Llama-3.1-8B, four rounds erode 36% of the edits that held after editing. The direction of this change is set by the model’s own verification: editing changes what a model says more than what it accepts as true, so the self-judge keeps preferring pre-edit facts, and preference optimization distills this preference into generation. Changing only the judge changes the outcome, and corrections of the model’s own errors, which its verifier accepts, are rarely pushed back to the old error, although in Llama they still erode. A second, collective component erodes even edits that never appear in the training data. Registering edits with the judge and freezing the network up to the last edited layer retains at least 98% of the edits that held on paraphrases after editing.

</details>

### 192. Shadow Unlearning: A Neuro-Semantic Approach to Fidelity-Preserving Faceless Forgetting in LLMs

📄 [OpenReview](https://openreview.net/forum?id=dvrfc1HmVt)　📅 2026-10　🏷️ P2

**关键词**：`shadow unlearning`、`PII-free`、`stricter formulation`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：标准遗忘设定把遗忘集直接暴露给遗忘方法——医疗记录等敏感数据本身有成员推断与滥用风险
- 🔬 **研究方法**：Shadow Unlearning：仅暴露匿名化版本；NSPU 神经语义投影遗忘框架+MuFU 五域基准+保持-遗忘权衡评测协议
- 📌 **结论**：多 LLM 上达到设定要求——更严格的无 PII 遗忘问题formulation（遗忘过程的隐私自身）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In a typical machine unlearning setting, both the forget set and the retain set are exposed to the unlearning methods. Existing machine unlearning approaches are largely designed under this standard assumption. However, exposing potentially sensitive data, such as medical records, makes these methods vulnerable to membership inference attacks and the misuse of Personally Identifiable Information (PII). In this paper, we introduce a stricter formulation in which the original forget set is not directly exposed to the unlearning method. Instead, only an anonymized version of the forget set is made available, ensuring that no PII is revealed. We term this novel task formulation Shadow Unlearning. Since existing state-of-the-art methods are designed for the standard unlearning setting, they do not inherently satisfy the constraints of Shadow Unlearning. To address this gap, we propose a novel privacy-preserving framework, Neuro-Semantic Projector Unlearning (NSPU), specifically designed to operate under this stricter setting. To evaluate our approach, we construct the Multi-domain Fictitious Unlearning (MuFU) benchmark, which includes five diverse domains. We also introduce a comprehensive evaluation protocol to quantify the trade-off between knowledge retention and unlearning effectiveness. Experimental results across multiple large language models demonstrate that NSPU achieves superior unlearning performance while preserving model utility and enhancing user privacy. Furthermore, our approach is at least 10 times more computationally efficient than standard unlearning methods. These findings open a new direction for privacy-aware machine unlearning that effectively balances data protection and model fidelity.

</details>

### 193. Recovery Rates Cannot Show Whether Communicating Agents Have Forgotten

📄 [OpenReview](https://openreview.net/forum?id=ftDmXCpOOK)　📅 2026-10　🏷️ P2

**关键词**：`unlearning`、`multi-agent`、`downstream recovery`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：unlearning 通常只问模型本身——agent 间传消息时下游 agent 仍可从传记恢复被遗忘答案，恢复率归因不明
- 🔬 **研究方法**：小 transformer 遗忘家乡城市案例：区分发送者未忘/合法保留线索/接收者独自知晓三种来源+重训参照与单消息编辑对照
- 📌 **结论**：直问近乎全忘而下游恢复 41-68%——审计须报告恢复来源、读消息、单变量变化并计错误答案（传播链遗忘审计）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning is usually tested by asking
the updated model about the fact it should have
forgotten. When agents pass text to one another,
a second agent reading the first agent’s message
may still give the forgotten answer. We argue
that the rate of such downstream recoveries
cannot show whether unlearning worked. A
correct downstream answer may come from a
fact the sender failed to forget, from a clue the
sender was right to keep, or from the receiver
alone, and whether each is a failure depends
on whether the deletion aimed to remove the
data’s influence or to prevent disclosure. A
low rate can also hide harm, when the sender
replaces the fact with a falsehood that the re-
ceiver repeats. We support this position with
a controlled case study in which small trans-
formers forget people’s home cities. Direct
questions report near-complete forgetting, yet a
receiver recovers 41-68% of the cities from the
senders’ biographies. Two methods with nearly
the same recovery rate fail in opposite ways,
and the obvious remedies, a retrained reference
and edits to single messages, both misattribute
recoveries. Audits should report where recov-
eries come from, read the messages, vary one
input at a time, and count wrong answers.

</details>

### 194. Direct Suppression Is Not an Unlearning Verdict: Reference-Calibrated Audits for Vision-Language Models

📄 [OpenReview](https://openreview.net/forum?id=reGsTfdtyA)　📅 2026-10　🏷️ P2

**关键词**：`unlearning audit`、`VLM`、`reference-calibrated`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：VLM 停止回答不等于遗忘：可能只是学会拒绝或损失能力——直接恢复率不足以裁决遗忘
- 🔬 **研究方法**：MORPHEUS-VL：以独立训练的 retain-only 参照系校准，测直接恢复与 logit 排序超额恢复，配 planted-exposure 阶梯与效用门
- 📌 **结论**：refusal-tuned Qwen2-VL 直接恢复 0.4-0.5% 但排序超额恢复 58.8pp 且随暴露上升——低直接恢复不构成有利遗忘裁决

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When an unlearned model stops answering target questions, it may have forgotten the target, learned to refuse, or lost useful capability. MORPHEUS-VL tests low direct recovery against retained utility and identity-level excess recovery from independently trained retain-only references under declared access. On 160 held-out synthetic identities, three refusal-tuned Qwen2-VL-2B models recover only 0.4–0.5% of direct target answers but retain 58.8–59.2 percentage points of excess supplied-candidate, logit-based ranking recovery against five references. With the same refusal recipe across a planted-exposure ladder, direct excess stays near zero while ranking excess rises from −0.4 to 58.9 points; the zero-exposure arm is bounded. In gradient-unlearning sweeps, six of nine checkpoints fail the utility gate; the three that pass are inconclusive on ranking alone, while two are excess on the stronger direct-or-ranking union. On inherited text and VLM grids, the full rule changes direct-only favorable counts. Low direct recovery therefore does not suffice for a favorable decision in the tested setting; the audit does not establish erasure or unrestricted extraction.

</details>

### 195. Data-Free Privacy Protection for Large Language Models via Model Inversion and Selective Unlearning

📄 [OpenReview](https://openreview.net/forum?id=slqzbIXv9P)　📅 2026-10　🏷️ P2

**关键词**：`data-free unlearning`、`model inversion`、`PII`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：遗忘式隐私补救通常需原始训练语料——专有/受限/不可恢复时失效
- 🔬 **研究方法**：DFSU：公开参照数据+白盒 logits 训练 logit-to-text 反演模型→合成伪 PII 序列构造掩码标注代理集→token 级选择性遗忘（对比掩码损失抑 PII 锚上下文）
- 📌 **结论**：四 LLM 两场景降提取/暴露型泄漏且效用微变、近 oracle 基线——无语料访问的 PII 遗忘

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) may retain sensitive personally identifiable information (PII) from pretraining corpora and later expose it during generation, creating privacy risks for deployment. Machine unlearning offers a natural route for post-hoc privacy remediation, but existing methods typically require access to the original training corpus, an assumption that often fails when the corpus is proprietary, legally restricted, or unrecoverable. To address this limitation, we propose Data-Free Selective Unlearning (DFSU), a framework for LLM privacy protection via model inversion and selective unlearning without access to the original training corpus. DFSU trains a logit-to-text inversion model from public reference data and white-box target-model logits, constructs a mask-annotated surrogate dataset by synthesizing pseudo-PII sequences, and applies token-level selective unlearning with a contrastive mask loss that suppresses masked PII tokens while anchoring surrounding context to preserve utility. Across four LLMs, two task scenarios, and three reference corpora, DFSU reduces extraction- and exposure-based PII leakage with limited utility changes, reaches privacy–utility trade-offs comparable to an oracle baseline with a ground-truth forget set, and lowers behavioral PII re-emission in original-checkpoint audits.

</details>

## 九、隐私攻击与防御

### 196. Training-Data Superposition in LoRA: Recoverability and Privacy Implications

📄 [OpenReview](https://openreview.net/forum?id=YxKmu2wkP6)　📅 2026-10　🏷️ P1

**关键词**：`LoRA privacy`、`training-data superposition`、`membership inference`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：LoRA 把训练数据变成小任务向量——这个向量到底保留了数据的什么（隐私含义）
- 🔬 **研究方法**：训练数据叠加理论：SGD 下任务向量=逐例梯度变换和+唯一恢复条件与逼近误差界+rank-one 反例；Qwen2.5-14B 验证（500 步误差<0.09、20 条隐藏记录全恢复）+临床叙事植入标识符审计
- 📌 **结论**：Llama-3.1-8B 早停点 MIA AUC 0.77、十 epoch 适配器泄露 20% 植入标识符——低秩本身不保护数据（LoRA 隐私理论）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Low-rank adaptation (LoRA) turns training data into a small task vector. What does that vector keep about the data? We give a theory of training-data superposition in LoRA. Under plain SGD, the task vector is exactly a sum of transformed per-example gradients along the training path. Given the initialization and a finite pool of candidate records, we state conditions under which each record's contribution can be recovered uniquely and bound the effect of approximation error, and a rank-one construction shows that low rank alone does not protect the data. A likelihood readout links the parameters to observable behavior. Controlled experiments on Qwen2.5-14B confirm the theory: the one-step task vector equals the fixed-feature sum, the relative error stays below 0.09 after 500 steps, and all hidden records are recovered from a pool of 20. A clinical audit on public PMC-Patients narratives with fabricated identifiers shows the consequences. Base-calibrated membership inference on Llama-3.1-8B reaches an AUC of 0.77 at early stopping, a ten-epoch adapter reveals 20% of the planted identifiers, and differentially private training is the only defense that brings membership leakage back to chance.

</details>

### 197. Uncovering Robot Training Data via Membership Inference Attack on Vision Language Action Models

📄 [OpenReview](https://openreview.net/forum?id=n2JI47zvIR)　📅 2026-10　🏷️ P1

**关键词**：`membership inference`、`VLA`、`robot data`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：VLA 依赖稀缺专有机器人轨迹训练——数据滥用检测的 MIA 未适配动作输出与机器人中心信息
- 🔬 **研究方法**：首个黑盒 VLA MIA：通过 VLA 特有动作输出评估模型对机器人特有知识（具身轨迹独有、通用世界知识不可得）的记忆
- 📌 **结论**：跨基准大幅超既有 MIA 基线——具身模型的训练数据隐私审计（VLA 供应链）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models enable end-to-end robotic policy learning and are increasingly deployed in real-world scenarios. 
To acquire capabilities for action decision-making, VLAs rely on robot trajectory data for training.
Such robot trajectories are scarce and proprietary, underscoring the need to detect data misuse through membership inference attacks (MIAs).
However, existing MIAs developed for language models fail to account for the robot-centric information embedded in the data that is critical for accurate action prediction, which consequently leads to suboptimal attack performance.
Meanwhile, the action-based outputs specific to VLAs differ from those of language models in both semantic representations and statistical properties, thereby hindering the transfer of existing MIAs.
In this paper, we propose the first black-box membership inference attack framework targeting VLAs.
The core idea of our method is to assess a model's memorization of robot-specific knowledge, which is unique to embodied trajectories and unavailable from general world knowledge, through VLA-specific action outputs.
Experiments conducted on VLA models across benchmarks demonstrate that our method substantially outperforms baselines.
Code is available at https://anonymous.4open.science/r/VLA-MIA-84C4/.

</details>

### 198. ADAM: A Systematic Data Extraction Attack on Agent Memory via Adaptive Querying

📄 [OpenReview](https://openreview.net/forum?id=qGmAsdVuTU)　📅 2026-10　🏷️ P1

**关键词**：`agent memory`、`data extraction`、`adaptive querying`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：agent 记忆/RAG 存敏感信息——查询式攻击可泄漏但既有方法 ASR 有限
- 🔬 **研究方法**：ADAM：受害 agent 记忆的数据分布估计+熵引导查询策略最大化隐私泄漏
- 📌 **结论**：大幅超 SOTA、ASR 至 100%——记忆分布建模的自适应抽取攻击（agent 记忆隐私面）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model (LLM) agents have achieved rapid adoption and demonstrated remarkable capabilities across a wide range of applications. To improve reasoning and task execution, modern LLM agents would incorporate memory modules or retrieval-augmented generation (RAG) mechanisms, enabling them to further leverage prior interactions or external knowledge. However, such a design also introduces a group of critical privacy vulnerabilities: sensitive information stored in memory can be leaked through query-based attacks. Although feasible, existing attacks often achieve only limited performance, with low attack success rates (ASR). In this paper, we propose ADAM, a novel privacy attack that features data distribution estimation of a victim agent’s memory and employs an entropy-guided query strategy for maximizing privacy leakage. Extensive experiments demonstrate that our attack substantially outperforms state-of-the-art ones, achieving up to 100% ASRs. These results thus underscore the urgent need for robust privacy-preserving methods for current LLM agents. Our code is available at: https://anonymous.4open.science/r/adam.

</details>

### 199. Quantifying and Alleviating Contextual Integrity Violations in Evolving Agent-User Interactions

📄 [OpenReview](https://openreview.net/forum?id=60YAVaKRpn)　📅 2026-10　🏷️ P2

**关键词**：`contextual integrity`、`evolving context`、`multi-turn leakage`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：agent 的 CI 评测多为单轮静态意图——上下文演变中的披露决定未知
- 🔬 **研究方法**：CI-State：420 多轮交互×七种上下文移位类型×八前沿模型
- 📌 **结论**：演进上下文使最终动作泄漏平均 +6.6pp 且随移位累积；更高推理努力或重述型记忆无可靠补救——单轮静态评测隐藏的隐私失败

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As LLM agents increasingly act on users' behalf, they access sensitive information whose appropriate disclosure depends on context, as captured by the theory of Contextual Integrity (CI). Yet existing evaluations of CI in LLM agents largely consider single-turn tasks under a static user intent or fixed context, leaving unclear whether agents can adapt their disclosure decisions as the governing context changes over multi-turn interactions. We introduce CI-State, a controlled benchmark of 420 multi-turn interactions spanning seven context shift types. Across eight frontier models, evolving context states increase final-action leakage by an average of 6.6 percentage points over the corresponding single-turn setting. Leakage further increases as shifts accumulate, while higher reasoning effort or recap-based memory mechanisms provide no reliable remedy. We find that prompting methods targeted at single-turn contextual leakage help but do not close the gap under evolving CI states. Our findings reveal privacy failures hidden by single-turn, static evaluation and highlight the need to account for evolving context when building and evaluating privacy-preserving agents.

</details>

### 200. RedAct: Redacting Agent Capability Traces for Procedural Skill Protection

📄 [OpenReview](https://openreview.net/forum?id=60qBKfaBSu)　📅 2026-10　🏷️ P2

**关键词**：`trace redaction`、`procedural skill leakage`、`watermark`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：执行轨迹的丰富过程细节（公式/阈值/策略）可被下游方法恢复——公开 agent 轨迹是安全接口
- 🔬 **研究方法**：CapTraceBench（75 任务 154 技能）+RedAct：定位受保护关键信息、保验证证据重写轨迹+行为水印溯源
- 📌 **结论**：技能迁移 44.7-67.1%→低于无技能基线且水印检出 93.6-100%@FAR≤1.9%——选择性脱敏不删审计证据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Users rely on execution traces to observe agent behavior, diagnose failures, and ensure accountability. These traces contain rich procedural detail, including tool invocations, intermediate decisions, and error-recovery logic. Yet this detail can expose private procedural skills, allowing downstream methods to recover key formulas, thresholds, and strategies without access to model weights or skill files. To quantify this risk and evaluate protection, we construct CapTraceBench, a benchmark of 75 specialized long-horizon tasks and 154 curated skills across seven domains. We also introduce RedAct, a protected trace release framework that localizes protected key information, rewrites traces while preserving verifier-critical evidence, and embeds behavioral watermarks for downstream provenance analysis. Across representative trace reuse methods, RedAct reduces normalized skill transfer (NST) from 44.7–67.1% on raw traces to below the no-skill baseline, while preserving audit evidence. Its standalone behavioral watermarks reach 93.6–100.0% true detection with a false alarm rate of at most 1.9%. These results frame public agent traces as security interfaces and show that selective redaction can reduce procedural capability leakage without removing audit evidence.

</details>

### 201. Learning to Keep Secrets: Empowering Local LLMs with Autonomous Privacy-Conscious Delegation

📄 [OpenReview](https://openreview.net/forum?id=61oZxTYyQ2)　📅 2026-10　🏷️ P2

**关键词**：`privacy`、`local LLM`、`delegation`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：云端能力强但送出提示、本地保主权但弱——隐私意识委托的固定管线不训练本地模型掌控全程
- 🔬 **研究方法**：ADAPT：训练本地模型决策直接回答/移除或抽象隐私后委托/本地整合远程响应，按答案质量 vs 实测 PII 泄漏优化轨迹
- 📌 **结论**：四本地模型×四数据集 16 组合全部最高质量保持且低 PII 泄漏——自主隐私变换的委托执行

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Cloud-hosted large language models (LLMs) offer strong capabilities but require sending user prompts to third-party providers, creating privacy risks. Local models preserve data sovereignty but are often less capable. Privacy-conscious delegation addresses this gap by allowing a local model to seek remote assistance while limiting private-context disclosure. However, existing methods rely on fixed pipelines or static routing and do not train the local model to control the complete execution process. We propose ADAPT (Autonomous Delegation with Adaptive Privacy Transformation), a framework that trains the local model to decide whether to answer directly, selectively remove or abstract private information before delegation, and locally integrate the remote response. ADAPT optimizes this execution trajectory by balancing answer quality against measured personally identifiable information leakage. Across four local models and four datasets, ADAPT achieves the highest quality preservation among non-reference methods in all 16 model–dataset combinations while maintaining low measured PII leakage.

</details>

### 202. PRAESIDIUM: Privacy-Resilient Embedding Sanitization against Inversion and Decoding

📄 [OpenReview](https://openreview.net/forum?id=CKjFtuyUds)　📅 2026-10　🏷️ P2

**关键词**：`embedding inversion`、`vector database`、`sanitization`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：向量库存 LLM 嵌入——少样本 inversion 恢复 94% 含义、分类器 100% 命名来源模型
- 🔬 **研究方法**：PRAESIDIUM：计算后变换（统一尺寸+坐标标准化+共享旋转+密钥噪声）无需重训与模型权限+边界刻画（千级已知对/多改写/大向量组/拟合参数）
- 📌 **结论**：ALGEN 94.3%→0.4%、Zero2Text 42%→0%、模型识别 100%→30-35% 且平均保 95.5% NDCG@10——后处理嵌入消毒及其失效边界

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vector databases now store embeddings produced by large language models (LLMs), and these vectors give away more than they seem to. With four open 7–9B LLMs as encoders, a published few-shot inversion attack (ALGEN) recovers the meaning of 94% of raw embeddings, and a simple classifier names the model behind a vector 100% of the time. We present PRAESIDIUM, a transform applied to vectors after they are computed, with no retraining and no access to model weights. It brings every model's vectors to the same size, reshapes each coordinate to a standard bell curve, rotates all models into one shared frame, and adds keyed noise. On MIRACL, PRAESIDIUM lowers ALGEN's success rate from 94.3% to 0.4% (a whitening-based baseline: 1.4%) and a training-free attack, Zero2Text, from 42% to 0%. Model identification falls from 100% to 30–35% (chance: 25%). At equal search quality, the whitening baseline lets attackers trace 1.7–2.6× more vectors back to their passage. On real MIRACL queries, PRAESIDIUM keeps 95.5% of raw NDCG@10 on average, with gains for two encoders and losses for two. We also show where protection ends: attackers with thousands of known pairs, several paraphrases of a passage, large groups of vectors, or the fitted parameters recover much more.

</details>

### 203. Auditing Privacy Leakage in Clinical LLM Fine-Tuning: Completion-Only versus Full-Sequence ICD Coding

📄 [OpenReview](https://openreview.net/forum?id=SuHm0VHZoa)　📅 2026-10　🏷️ P2

**关键词**：`privacy audit`、`loss masking`、`canary`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：临床 LoRA 微调的损失掩码是否改变可观察隐私泄漏——completion-only vs 全序列未对照
- 🔬 **研究方法**：148 合成金丝雀（临床隐私风险分类学衍生）注入 MIMIC-IV+匹配模型对照+参考校正 MIA/属性推断
- 📌 **结论**：completion-only MIA AUROC 0.491 vs 全序列 0.580、属性 top-1 0.228 vs 0.619（rank64 达 0.800）——两种损失公式的审计信号不等价（训练配置的隐私审计）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning language models on clinical notes can retain sensitive information in its parameters. We audit whether loss masking changes observable privacy leakage during LoRA adaptation for ICD-10 coding. We inject 148 synthetic canary variants, derived from a clinical privacy-risk taxonomy, into MIMIC-IV training notes and compare matched models trained with and without canaries. We compare completion-only loss, applied only to ICD-code outputs, with full-sequence loss, where the note tokens are also supervised. Canary insertion changes held-out combined micro-F1 by at most 0.003 across the evaluated configurations. Under completion-only loss, reference-corrected membership-inference AUROC averages 0.491 and five-way attribute-inference top-1 accuracy 0.228. Under full-sequence loss these values are 0.580 and 0.619, with attribute top-1 rising from 0.400 at LoRA rank 4 to 0.800 at rank 64. No model reproduces a canary verbatim, and the patient-linkage probe shows no positive aggregate canary-specific effect. These results provide a controlled counterexample to assuming that the two loss formulations produce equivalent privacy audit signals. Their generality beyond this model, dataset, and training setup remains to be established.

</details>

### 204. ConCI: A Controlled Counterfactual Benchmark for Contextual Integrity in LLMs

📄 [OpenReview](https://openreview.net/forum?id=iwf6DrguUT)　📅 2026-10　🏷️ P2

**关键词**：`contextual integrity`、`benchmark`、`counterfactual`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：现有 CI 基准多参数同变且不当流动占主导——正确预测可能只反映泛拒绝倾向
- 🔬 **研究方法**：ConCI：锚流动+两个单参数反事实构成三元组联合计分，1592 流动 556 三元组七人标注
- 📌 **结论**：最强模型仍错约 1/5 三元组且对不当流动近天花板、恰当流动偏弱——CI 判断的非披露偏置与反事实校准

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Contextual integrity (CI) holds that the appropriateness of sharing personal information depends on the context of the information flow, not on the information alone. However, existing CI benchmarks often use independent scenarios that vary multiple CI parameters simultaneously and are dominated by inappropriate flows, making it unclear whether correct predictions reflect sensitivity to context or a general refusal tendency.
We present ConCI, a controlled-counterfactual benchmark in which an anchor flow is paired with two counterfactuals that each modify a single CI parameter. The resulting triplet is scored jointly, with credit given only when all three flows are judged correctly. Built from six existing benchmarks, ConCI contains 1,592 flows in 556 triplets, is approximately label-balanced, and is validated by seven human annotators per flow.
Across seven LLMs, many correct anchor predictions fail on at least one counterfactual, and even the strongest model errs on about a fifth of triplets. Furthermore, models perform near ceiling on inappropriate flows but weaker on appropriate ones, often continuing to judge a flow inappropriate even when a contextual change should make it appropriate.
Larger models narrow this bias toward non-disclosure but do not eliminate it, and reasoning yields only modest gains.

</details>

### 205. Enhanced Neighborhood Attack against Large Language Models via Sequential Word Replacements

📄 [OpenReview](https://openreview.net/forum?id=qKEiESELBv)　📅 2026-10　🏷️ P2

**关键词**：`membership inference`、`neighborhood attack`、`word replacement`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：灰盒邻域攻击用语义近义词替换比较目标文本与近邻损失——多次替换增强信号却引入跨替换干涉
- 🔬 **研究方法**：ENA 增强邻域攻击：低交互词替换选择减少干涉同时允许局部效应累积，受控 WikiText-103 试点+黑盒迁移研究
- 📌 **结论**：K=2/3 归一化交互残差降 50.0/55.3%——邻域 MIA 的干涉控制与黑盒迁移（成员推断方法学）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership inference attacks (MIAs) determine whether a sample was used to train a target model. Under gray-box access to output logits, neighborhood attacks compare the loss of a target text with losses of nearby texts constructed by semantically similar word replacements. Multiple replacements can strengthen the perturbation signal but also introduce cross-replacement interference affecting both members and nonmembers. We propose an enhanced neighborhood attack (ENA), which performs low-interaction word replacements to reduce such interference while allowing local effects to accumulate. We examine this mechanism with two studies. In a controlled WikiText-103 pilot, low-interaction selection reduces normalized interaction residuals by 50.0 percent for K = 2 and 55.3 percent for K = 3, while end-to-end AUC differences remain statistically unresolved. To examine transfer toward black-box settings where token losses are inaccessible, we relate the local original-versus-isotope likelihood gap to an independent generation-based isotope recovery rate. On released WikiMIA probes, the two are positively associated (Spearman rho = 0.274, 95 percent CI [0.244, 0.303]), and the association persists under equal-token-length and within-document controls. These studies provide mechanism-level evidence for the interference-and-recovery motivation and support direct evaluation of recovery-guided sequential replacements.

</details>

### 206. PrivacyFragBench: Evaluating Cross-App Privacy Inference from Fragmented Information in Mobile Agents

📄 [OpenReview](https://openreview.net/forum?id=uN3GMiYqy2)　📅 2026-10　🏷️ P2

**关键词**：`cross-app privacy`、`fragmented information`、`mobile agents`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：移动 agent 跨应用任务中把碎片信息拼成完整隐私——直接披露之外的综合推断未测
- 🔬 **研究方法**：PrivacyFragBench：9 隐私域 82 主题 270 实例（隐私信息拆片嵌入跨应用任务）×六模型两框架于交互 Android 环境
- 📌 **结论**：鼓励保留上下文提示下完整隐私泄漏率至 85.56% 且任务成功与泄漏正相关；识别隐私也不总拒绝后续披露——跨应用多任务执行的组合隐私风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Advances in multimodal large language models enable mobile agents to perform complex tasks across multiple applications. However, these agents may encounter private information during task execution. Existing studies mainly focus on the direct disclosure of private information, while the ability of mobile agents to combine fragmented information across different tasks and infer complete private information remains underexplored. To address this gap, we introduce PrivacyFragBench, a benchmark for evaluating privacy inference in mobile agents within an interactive Android environment. PrivacyFragBench covers 9 privacy domains and 82 topics, with 270 test instances that split private information into multiple fragments embedded in tasks across different applications. We evaluate six models using two mobile agent frameworks. Experimental results show that the full privacy leakage rate reaches up to 85.56% under prompts that encourage agents to retain more contextual information. Moreover, task success and privacy leakage rates show an overall positive correlation. Even when agents recognize private information, they do not always refuse subsequent requests to disclose it. These findings highlight the potential privacy risks of combining fragmented information during cross-application, multi-task execution.

</details>

## 十、检测、水印与溯源

### 207. SHADE: Trace-Based Humanization for Robust and Composable AI-Text Detector Evasion

📄 [OpenReview](https://openreview.net/forum?id=wcRwmXOpWb)　📅 2026-10　🏷️ P1

**关键词**：`detector evasion`、`humanization`、`trace-based attack`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：检测器规避攻击优化分数而不指明移除了哪些统计差异、效果能否经受再训练
- 🔬 **研究方法**：SHADE：把文本可测统计属性当 trace 显式对齐——受控生成+局部编辑把特征值带入人类同体裁区间且保持已达标目标
- 📌 **结论**：五个检测器（四个未用于开发）多数降至近随机；再训练后三个几乎无法恢复——按可测目标组织的人性化与适应性诊断（检测攻防的机理化）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Classifiers detect text generated by large language models using statistical differences from human writing. Attacks often optimize a detector's score without identifying which differences they remove or whether their effects survive retraining.

We present SHADE (Statistical Human-Alignment for Detector Evasion), a trace-based humanization method: it treats measurable statistical properties of text as traces to target explicitly. SHADE combines controlled generation with local editing to bring selected feature values into ranges typically observed in human texts of the same genre, while preserving previously attained targets. These features capture surface properties and how predictive information changes with the amount of preceding context.

On 74 held-out source documents, SHADE reduces detection performance substantially across five detectors, four of them unused during development, in several cases to near chance. After retraining on attacked examples, three detectors recover little or nothing while another recovers almost fully, revealing a remaining coverage gap. On a separate cohort, adding a complementary editing attack improves evasion over either component alone across all five detectors.

These results support organizing humanization around measurable targets, using adaptation tests to diagnose residual weaknesses and complementary modules to extend coverage.

</details>

### 208. Attacking Only Half the Data: Two-Sided Evaluation of AI-Text Detector Robustness

📄 [OpenReview](https://openreview.net/forum?id=CK5KYIU6Ui)　📅 2026-10　🏷️ P2

**关键词**：`detector robustness`、`two-sided attack`、`evaluation protocol`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：检测器鲁棒性评测只攻机器文本——人类文本常被语法修正/格式化/不可见字符修改
- 🔬 **研究方法**：双侧协议：两类文本同时施加攻击×两语料九检测器
- 📌 **结论**：双侧评测下报告的 AUROC 增益消失、被攻人类文本误分类至多 100%——词级同义替换有效且不可逆（检测评测的单侧偏置）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We investigate the robustness of widely used AI text detectors under attacks applied to both human and machine text. Prior evaluations typically attack only machine text, overlooking that human text is routinely modified through grammar correction, formatting, or invisible character insertion. We introduce a two-sided protocol that applies attacks to both classes. Across two corpora and nine detectors, reported AUROC gains vanish under two-sided evaluation, with attacked human text misclassified at rates up to 100%. While simple preprocessing reverses character-level attacks, word-level synonym substitution remains effective, meaning-preserving, and irreversible.

</details>

### 209. Retrieval-Augmented Language Models Evade Hallucination Detection

📄 [OpenReview](https://openreview.net/forum?id=PGrDIu743k)　📅 2026-10　🏷️ P2

**关键词**：`hallucination detection`、`RAG`、`authority veneer`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：RAG 的引用 veneer of authority 掩盖幻觉——检测器的谄媚问题未被探索
- 🔬 **研究方法**：三种 RAG 方法×三 QA 数据集：RAG 使四种主流检测器假阴性率 17.6%→33.2%+DPO/KTO 偏好优化放大规避
- 📌 **结论**：参考的存在使检测显著变差——RAG 幻觉检测的权威伪装效应

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) has become one of the most popular techniques thanks to its potential to mitigate hallucination, which attracts widespread attention across the research and industrial community. Despite its effectiveness, LLM-based RAG systems remain susceptible to hallucination. To detect hallucination in RAG, current work mainly focuses on hallucination from LLMs' internal knowledge with correct and sufficient context. However, the sycophancy problem in RAG hallucination detectors is underexplored.
Specifically, the inclusion of references can create a veneer of authority that masks the underlying hallucinations, making them significantly more difficult to identify. To systematically investigate this phenomenon, this work first conducts comprehensive experiments with three RAG methods (with vanilla RAG, with InstructRAG, and with adaptive RAG) and three question-answering datasets. The results show that, compared to non-RAG, RAG increases the false negative rate of four widely adopted automatic hallucination detectors from 17.6% to 33.2% on average. Furthermore, this work investigates the impact of prevalent preference optimization algorithms (DPO and KTO) on RAG hallucination detection, revealing that RAG systems built on backbone models trained with these algorithms are more prone to evading hallucination detection. The dataset and code will be publicly available.

</details>

### 210. PhantomHunter: Detecting Unseen Privately-Tuned LLM- Generated Text via Family-Aware Learning

📄 [OpenReview](https://openreview.net/forum?id=eT5pgMeSr5)　📅 2026-10　🏷️ P2

**关键词**：`AIGC detection`、`privately-tuned LLM`、`family-aware`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：私有微调模型生成的文本逃过现有检测——微调可使检测精度降 41pp
- 🔬 **研究方法**：PhantomHunter：提取基模型特征蒸馏为轻量代理+家族级对比学习增强共享信息+MoE 家族专家预测
- 📌 **结论**：四大家族数据上胜过 9 基线与 11 商业服务——按家族共享特征检测未见私有微调文本（检测的家族泛化）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing detectors of large language model-generated text mainly evaluate publicly known models, leaving privately fine-tuned models underexplored. Due to the rapid development of open-source models like the Qwen and LLaMA series, even ordinary users can now easily possess private LLMs by further tuning an open-source one with private corpora. Our preliminary study shows that fine-tuning can reduce existing detection accuracy by up to 41 percentage points. To address this issue, we propose PhantomHunter, a detector that learns family-level traits shared by base LLMs and their derivatives to detect text from unseen privately tuned models. It first extracts base model features and distills them into a lightweight proxy module for deployment efficiency considerations, followed by a contrastive family-aware learning module that enhances the family-shared information. The enhanced features are then fed into a mixture-of-experts module containing multiple experts for corresponding families for final predictions. Experiments on data from four widely adopted LLM families (LLaMA, Gemma, Mistral, and Qwen) show PhantomHunter's superiority over 9 baselines and 11 commercial services.

</details>

## 十一、谄媚、欺骗与社会性风险

### 211. Agents Don’t Just Agree, They Remember: Benchmarking Persistent Sycophancy in Self-Improving Personal Agents

📄 [OpenReview](https://openreview.net/forum?id=UEVFAv8ACz)　📅 2026-10　🏷️ P1

**关键词**：`sycophancy`、`agent memory`、`self-improving agents`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：自改进个人 agent 把用户断言写进档案/记忆/技能——后续会话把笔记当可信上下文（持久谄媚）
- 🔬 **研究方法**：PASB：1600 任务×两框架×16 模型，首聊存疑断言/新会话仅经笔记触达的分离设计+四种缓解对照
- 📌 **结论**：存疑断言使下游依赖率 35.6%→68.1%、38.8% 笔记比用户原话更权威——编辑存储笔记优于对话纠错（记忆介导的谄媚固化）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-improving personal agents write profiles, memories, and reusable skills that carry over from one chat to the next. Prior works ask whether a model agrees with the user in its next reply. Yet these agents can also write down a claim the user made, and a later chat can read that note back as trusted context. We call this persistent sycophancy. We introduce the Personal Agent Sycophancy Benchmark, PASB, with 1,600 tasks run on two agent frameworks, Hermes-Agent and OpenClaw, across sixteen models that span scales and generations. Each task separates a first chat containing the claim from a follow-up chat in a fresh session, so the first chat can reach the follow-up only through a note the agent chose to write. Downstream failure, the rate at which follow-up answers still rely on the claim, reaches 68.1% when the agent saved the claim against 35.6% when it did not. Later generations fail less often, yet a saved note still more than doubles their failure rate. In 38.8% of runs the saved note states the claim with more authority than the user gave it, and a saved claim still shapes answers in a different domain. Among four mitigations, editing the stored note works better than correcting the agent in conversation, cutting same-domain downstream failure from 36.3% to 30.3% for Hermes-Agent and from 37.9% to 31.6% for OpenClaw. A strong instruction against saving brings failure back to the level of runs that saved nothing. Self-improving agents need controls on what they write to memory as well as on what they say. Our benchmark is available at https://anonymous.4open.science/r/syco_arr-4663/.

</details>

### 212. The Anatomy of Conversational Scams: A Topic-Based Red Teaming Analysis of Multi-Turn Interactions in LLMs

📄 [OpenReview](https://openreview.net/forum?id=FeqfBtUHbR)　📅 2026-10　🏷️ P2

**关键词**：`red teaming`、`conversational scams`、`multi-turn`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：单轮安全评测无法捕捉多轮对抗交互中的社会工程风险
- 🔬 **研究方法**：双语 LLM-to-LLM 红队模拟 18648 段对话+攻防策略族标注与交互动力学建模
- 📌 **结论**：诈骗完成率 4.1-5.4% 罕见但升级模式复现、防御依赖验证/延迟/渠道控制且跨语言结构差异显著——多轮攻防的交互结构学

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) acquire persuasive abilities through extended dialogues. These abilities introduce new risks in multi-turn adversarial interaction settings. Single-turn safety evaluations cannot capture such risks. We conduct a controlled LLM-to-LLM simulation study of automated red-teaming across bilingual social engineering scenarios. We evaluate eight state-of-the-art LLMs in English and Chinese, excluding models with built-in refusal behaviors by design, as they produce no trajectory to analyze. We annotate attacker and defender strategy families and model the interaction dynamics between them. Across 18,648 dialogues, successful scam completion remains rare (4.1%–5.4%), while multi-turn adversarial dialogues follow recurrent escalation patterns and defensive responses rely on verification, delay, and channel control. We find statistically significant cross-model and cross-lingual differences in outcome distributions, with transition analysis further revealing systematic structural variation in defender responses across languages (Cramér's V = 0.12–0.42). These findings highlight the importance of interactional structure in multi-turn adversarial settings.

</details>

### 213. Self-Authored Verification Is Unreliable in Heuristic Self-Improving Agents

📄 [OpenReview](https://openreview.net/forum?id=WELWjWlkcC)　📅 2026-10　🏷️ P2

**关键词**：`self-improvement`、`verifier gap`、`external audit`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：自改进 agent 同时控制策略与自写验证器——自评分保持高位而部署性能下降（验证器-部署缺口）
- 🔬 **研究方法**：SEAL 密封外源接受环：保留自写测试但候选与在位者经固定外部审计 accept/reject，回归即整体回滚
- 📌 **结论**：弱 agent 覆写已获策略仍过自测、内部测试约束不可靠——可靠自改进需 agent 控制之外接受信号（自验证的信任边界）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-improving agents accumulate capabilities by rewriting policies and heuristic rules. They often evaluate updates with self-authored tests. Controlling both the policy and its verifier creates a risk. Self-scores can remain high while deployment performance declines. We study this mismatch as the verifier-deployment gap. We examine how it arises, varies with agent capability, and responds to limited external trust. To address this problem, we introduce a Sealed Exogenous Acceptance Loop (SEAL). SEAL retains self-authored tests but compares each candidate with the incumbent through a fixed external audit. The agent cannot modify or inspect the audit and receives only accept/reject feedback. The whole incumbent state is retained after a clear regression. Our experiments show that this problem often appears in heuristic learning settings. Weaker agents overwrite acquired strategies while passing easy self-tests. Stronger agents remain more stable but still misjudge deployment performance. Internal test constraints do not reliably close the gap. In contrast, SEAL outperforms unprotected baselines across six models and three random seeds. Reliable self-improvement can retain self-verification, but requires an acceptance signal outside the agent’s control.

</details>

### 214. NoHurt: Context-Sensitive Benchmarking for Quantifying Information Acquiescence During High-Risk Dialogue

📄 [OpenReview](https://openreview.net/forum?id=ajBXIARbg8)　📅 2026-10　🏷️ P2

**关键词**：`suicidal ideation`、`information acquiescence`、`multi-turn benchmark`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：高风险对话中的信息顺从——单轮基准无法捕捉伤害随对话展开浮现
- 🔬 **研究方法**：NoHurt：人写多轮对话（三级毒性+人类攻击战术分类学）+前置情绪披露/后置撤回与合理化对照网格
- 📌 **结论**：GPT-4o 在自伤披露对话 68% 被判有害（近七倍于最稳模型）、Claude 两代对此独特稳健——风险信号累积下的评测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are increasingly deployed in conversational settings where users may be experiencing acute psychological distress; however, contemporary safety evaluations remain dominated by single-turn benchmarks that fail to capture how harmful disclosures emerge over the course of a dialogue. In this work, we study information acquiescence in high-risk conversations involving suicidal ideation and self-harm intent. We introduce NoHurt, a context-sensitive benchmark of human-authored multi-turn conversations, manually annotated with a three-tier toxicity scale and a human attack-tactic taxonomy adapted from prior work. To isolate how conversational framing shapes model behavior, each conversation is paired with prepended emotional disclosures and appended retraction or justification messages, producing a controlled grid of conversational contexts. We use NoHurt to evaluate a range of widely deployed proprietary and open-weight chatbots, enabling direct comparison of how models respond as risk signals accumulate across turns. Notably, OpenAI's widely used GPT-4o was judged harmful in approximately 68% of conversations in which the user disclosed suicidal intent (averaged across three LLM judges' decisions), nearly seven times the rate of the most robust model. Additionally, both Claude models evaluated show distinctive resilience against this jailbreaking. Taken together, this work highlights the necessity of multi-turn, context-aware evaluation for assessing model safety in mental-health-related interactions.

</details>

### 215. Progressive Memory Illusion: A Continuous Benchmark for Multi-Turn Factual Sycophancy

📄 [OpenReview](https://openreview.net/forum?id=gbOuR96Dus)　📅 2026-10　🏷️ P2

**关键词**：`sycophancy`、`multi-turn`、`confidence trajectory`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：终点评翻转指标漏掉未翻转但信心大幅流失的渐进谄媚
- 🔬 **研究方法**：五轮说服升级（温和怀疑→伪造引用→制造共识）下跟踪正确答案 token 级置信度，4 模型×3 数据集 4644 条轨迹
- 📌 **结论**：至多 29% 未翻转项丢超四分之一信心；单条忽略指令即可逆转大半——屈服主要是可逆上下文效应（谄媚的连续度量）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Language models show different failure patterns under escalating social pressure. We introduce the Progressive Memory Illusion Benchmark, a diagnostic protocol that tracks token-level confidence in a correct answer across a five-turn persuasion escalation (mild doubt, strong contradiction, authority appeal, fabricated citation, manufactured consensus) with the full conversation retained. Across four models and three factual datasets (4,644 trajectories), dataset-averaged trajectories reveal two profiles missed by end-point flip metrics: DeepSeek-V3 and Llama-3.3-70B lose most confidence at the first direct contradiction, whereas GPT-4o-mini's largest mean drop occurs at the final consensus turn, and up to 29% of items that never flip still lose more than a quarter of their confidence. Scale does not predict robustness across families: GPT-4o-mini is more robust than the larger Llama-3.3-70B on all three datasets, and rankings are unchanged on the items shared by all models. Collapse outcomes vary substantially across models on the same shared items, while all-model collapse is uncommon. Chain-of-thought prompting can worsen robustness (2.7× drift for GPT-4o on CommonClaim). Finally, a single "ignore the previous conversation" instruction reverses most of the collapse, indicating that capitulation is largely a reversible context effect; the smaller Llama-3.1-8B is both more susceptible and less recoverable.

</details>

### 216. Seeing Through the Forgery Is Not Enough: Regressive Sycophancy under Fabricated Evidence in Medical Vision-Language Models

📄 [OpenReview](https://openreview.net/forum?id=gfDggL7JUV)　📅 2026-10　🏷️ P2

**关键词**：`sycophancy`、`fabricated evidence`、`medical VLM`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：伪造证据下的退行性谄媚：正确诊断被一份假处方推翻——知悉伪造不阻止采纳
- 🔬 **研究方法**：四开源 VLM×400 VQA-RAD 是非题×19200 多轮对话（有无伪造处方）+披露句干预
- 📌 **结论**：无披露时 6488 个正确答案放弃 80.1%；披露为合成使一模型翻转率 77.8%→47.3%——28.3% 拒斥处方的对话中 40% 在后续轮仍翻转（医疗 VLM 的证据权威伪装）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A medical vision-language model may analyze a given CT scan and correctly detect two healthy kidneys in view. Continuing this conversation, if a user provides a prescription with an opposite direction, medical LLM models often sycophantically choose to realign their diagnosis.
In this work, we study regressive sycophancy under fabricated evidence, where a model abandons a correct answer when pushback comes with a fake document.
We test four open VLMs on 400 VQA-RAD yes/no questions in 19,200 multi-turn conversations, with and without a fabricated prescription.
Without a disclosure that documents are synthetic, the models abandon 80.1% of 6,488 correct answers.
Notably, the same prescription raises the flip rate of Qwen2.5-VL-7B from 45.9% to 89.6% and lowers that of Qwen3-VL-8B from 77.7% to 50.9%.
A model rejected the prescription while still preserving the correct answer in 915 of 3,232 conversations with the prescription (28.3%), and 40% of these flipped in later turns. 
System-prompt sentences that disclose the documents as synthetic lower one model's flip rate from 77.8% to 47.3%.
Thus, we conclude that awareness about a forgery does not prevent a model from adopting its answer.

</details>

## 十二、安全评测与口径

### 217. FinVault: Stress-Testing Financial Agents through Executable Policy Violations

📄 [OpenReview](https://openreview.net/forum?id=08y3Vy812e)　📅 2026-10　🏷️ P2

**关键词**：`financial agents`、`executable policy violations`、`stress testing`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：金融 agent 失败只有跨操作边界才致命（无授权调工具/覆写证据/提交不合规状态）——文本级安全基准测不到
- 🔬 **研究方法**：FinVault：监管案例模式→31 可执行沙箱（角色权限/可写状态/工具模式/漏洞 oracle）+107 漏洞×786 对抗×397 良性对照×六攻击通道
- 📌 **结论**：八工具模型宏平均 ASR 40.37-71.04%、集中于溯源敏感与工具介导轨迹；防御常靠拒合法工作降攻——策略须在工具与状态转换层强制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Financial-agent failures are consequential only when model outputs cross an operational boundary: a tool is called without authority, evidence is overwritten, or a non-compliant state is committed. Existing financial safety benchmarks mostly score textual responses, while general agent benchmarks do not encode the authorization, suitability, reporting, and audit constraints that determine whether a financial action is permissible. We introduce FinVault, a controlled stress-testing benchmark that turns regulatory-case patterns into 31 executable sandboxes with role permissions, writable state, tool schemas, and vulnerability-specific oracles. Its evaluation split contains 107 vulnerabilities, 786 adversarial cases spanning six attack channels, and 397 independently authored benign controls. Across eight tool-capable LLMs, macro-averaged attack success ranges from 40.37% to 71.04%; failures concentrate in provenance-sensitive and tool-mediated trajectories, while defenses often reduce attacks only by rejecting legitimate work. A severity analysis further shows 79.35% attack success on high-impact cases for Qwen3-Max. These results characterize residual risk in the tested control settings—not production incident rates—and motivate defenses that enforce policy at the tool and state-transition layers. Code and data are provided in the anonymized supplementary material.

</details>

### 218. HealthGovBench: Benchmarking and Governing Policy-Safe Tool Use in Healthcare Agents

📄 [OpenReview](https://openreview.net/forum?id=1mKiEIOeHe)　📅 2026-10　🏷️ P2

**关键词**：`healthcare agent`、`tool-use policy`、`runtime guard`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：医疗 agent 的答案正确与允许/拒绝判断不等于工具动作合规——禁记录/错接收/需审批变更未被评测
- 🔬 **研究方法**：616 合成工作流 18 族显式权限（行为者/接收者/目的/资源/授权态）+六种必需结果+HealthGovGuard 确定性运行时层
- 📌 **结论**：重放七模型提议把违规 308/4312→43/4312 且合规调整后成功 46.4%→61.8%——策略安全工具使用的基准与守门

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Can a healthcare agent complete a request without accessing forbidden records, disclosing information to the wrong recipient, or making changes that require verification or clinician approval? Answer correctness and allow-or-deny judgments do not establish that its tool actions are safe. We introduce HealthGovBench, 616 synthetic workflows across 18 families with explicit permissions for actors, recipients, purposes, resources, and authorization states. Six required outcomes cover allowing, denying, narrowing, redacting, requesting verification, and seeking human approval. We also introduce HealthGovGuard, a deterministic runtime layer that checks proposed actions before execution, selects encoded safe alternatives, and inspects tool results before release. Replaying seven models' stored proposals reduces violations from 308/4,312 under role-based access control to 43/4,312, while mean compliance-adjusted success rises from 46.4% to 61.8%. Provider/interface failures limit two model streams; remaining violations expose authorization-state inconsistencies and incomplete urgency rules. The benchmark measures compliant tool behavior under synthetic contracts, with expert policy validation and autonomous interactive evaluation still outstanding.

</details>

### 219. Telling Judge Gaming from Judge Error in Visual Reinforcement Learning

📄 [OpenReview](https://openreview.net/forum?id=5Ld7zhJlVy)　📅 2026-10　🏷️ P2

**关键词**：`judge gaming`、`reward hacking`、`divergence metric`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：视觉 RL 对学得判官训练可被博弈——常用检验（判官奖励 vs 独立质量分）训练前就有差，分不清判官错误与博弈
- 🔬 **研究方法**：RQD：金标事实锚定质量度量+扣除训练前差距+重评同答案确认博弈标签（区分 gaming/漂移/塌缩）
- 📌 **结论**：ChartQA 上 Qwen2.5-VL 7B 判官被博弈：奖励 +8% 质量无变、终差 2/3 是训练前既有——换文本不换答案即 +18%（reward hacking 的视觉 RL 实证）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision–language models are often trained with reinforcement learning against a learned judge. A judge can be gamed, so the model earns more reward without giving better answers. The usual check compares the judge's reward with an independent quality score, but this gap already exists before training, so it cannot tell judge error from gaming. We introduce Reward–Quality Divergence (RQD). It measures quality with an anchor built from ground-truth facts, removes the gap that exists before training, labels what remains as candidate gaming, drift or collapse, and confirms a gaming label by re-scoring the same answers. RQD finds a planted exploit and gives no label to four rewards that cannot be gamed. On ChartQA, re-scoring confirms that a Qwen2.5-VL 7B judge is gamed. Reward rises 8% while quality shows no clear change, and two thirds of the final gap was there before training, so the final gap overstates the effect 3 times. Swapping the text before an unchanged final answer raises the judge's score by 18%. The effect holds on held-out items and for a second policy family, but it weakens at a gentler learning rate and is absent for a 7B policy. Other cases are candidates only.

</details>

### 220. LLMs Do Not Play Dice Securely: Silent Cryptographic Randomness Failures in LLM-Generated Code

📄 [OpenReview](https://openreview.net/forum?id=7CSt58v6nN)　📅 2026-10　🏷️ P2

**关键词**：`cryptographic randomness`、`secure code`、`silent failure`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：安全取决于值如何生成而非类型格式——功能测试通过仍可违反安全要求
- 🔬 **研究方法**：SECRAND：148 随机性任务（Stack Overflow 挖掘）+分类学接地检测器定位随机性失败×五语言 15 模型+开发者研究
- 📌 **结论**：37.06% 输出误用（峰值 57.57%）、脆弱输出 89.75% 功能正确；主因非弱 PRNG 而是硬编码密钥/固定 IV；点名相关 CWE 的提示比通用安全请求更有效——静默安全失败的类型学

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Code generated by large language models (LLMs) can pass functional tests while still violating security requirements.
Cryptographic randomness exemplifies this gap, since security depends on how a value was generated, not on its type or format.
Existing evaluations treat randomness as one category in broader vulnerability benchmarks, leaving its prevalence and failure modes unclear.
We build SECRAND, a benchmark of 148 randomness tasks mined from Stack Overflow, with a taxonomy-grounded detector that locates randomness failures in generated code.
Across five programming languages and 15 models, misuse affects 37.06% of outputs and peaks at 57.57%, and GPT-5 Chat, Gemini-2.5-Pro, and Claude Opus 4.8 misuse randomness in 27.76–29.62% of samples.
Of the vulnerable outputs, 89.75% are functionally correct.
The dominant failure mode is not weak PRNG selection but hardcoded cryptographic artifacts such as keys and fixed IVs.
Within model families, larger models do not misuse less, and their misuse shifts toward hardcoded artifacts as they generate more complete implementations.
In our developer study, 86.73% of participant prompts carried no security intent, and 17 of the 19 observed misuses went unnoticed into the submitted code.
A prompt that names the relevant randomness-related CWEs reduces misuse more than a generic request for secure code.

</details>

### 221. Aligned in Form, Not in Meaning: The Comprehension–Containment Decoupling of LLM Safety in Low-Resource Bangla Derogatory Speech

📄 [OpenReview](https://openreview.net/forum?id=8zUlkcuRW7)　📅 2026-10　🏷️ P2

**关键词**：`low-resource safety`、`comprehension-containment decoupling`、`Bangla`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：安全对齐绑定高资源表层形式而非有害意义——低资源谩骂的理解与遏制能力解耦假设
- 🔬 **研究方法**：五前沿模型×六协议母语校准审计（基线/正字扰动/CoT/专家人设等）+人类基线 κ=0.84
- 📌 **结论**：孟加拉语理解缺口 7.92pp 但 token 泄漏率两语相同 92.83%；CoT 救理解却拆遏制（94.72% Pass/96.23% Use）；专家人设塌缩拒答至 6.57%——高资源基准不能认证低资源安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We audit five frontier large language models on native Bangla derogatory speech (gali) across six protocols to test a single hypothesis: the Comprehension–Containment Decoupling. We propose that contemporary safety alignment is bound to high-resource surface form rather than harmful meaning, causing a model's capacity to comprehend a low-resource slur and its capacity to contain it to operate independently. Every protocol corroborates this hypothesis against a human-calibrated baseline (κ = 0.84). At baseline, models exhibit a 7.92 percentage point comprehension deficit in Bangla yet maintain an identical 92.83% token leakage rate across both languages. Severity calibration tracks surface anatomical cues over compositional harm (+4.00 error on mild slang; -2.00 on threats), while apparent containment gains under orthographic perturbation prove to be a tokenizer-driven "containment mirage." Crucially, explicit Chain-of-Thought reasoning rescues comprehension (94.72% Pass) while systematically dismantling containment (96.23% Use). Furthermore, expert-persona framing collapses refusal to 6.57%, revealing that keyword-based filters ignore dehumanizing communal slurs entirely. Our findings demonstrate that high-resource benchmarks cannot certify low-resource safety, necessitating meaning-grounded containment.

</details>

### 222. CSSBench: Evaluating the Safety of Lightweight LLMs against Chinese-Specific Adversarial Patterns

📄 [OpenReview](https://openreview.net/forum?id=C3nyjFrvet)　📅 2026-10　🏷️ P2

**关键词**：`Chinese adversarial patterns`、`lightweight LLM`、`safety benchmark`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：中文恶意查询以谐音/拼音/符号拆分等中文特有模式隐藏意图——英中心基准不覆盖，轻量模型更脆弱
- 🔬 **研究方法**：CSSBench：六域（违法合规/隐私/医疗误信息/欺诈仇恨/成人/公共政治）多任务类型组织中文对抗查询+过拒测量
- 📌 **结论**：中文特有对抗模式对轻量 LLM 构成关键挑战——安全评测的语言特异性补充

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed in cost-sensitive and on-device scenarios, and safety guardrails have advanced mainly in English.
However, in practice, Chinese malicious queries could conceal intent via `homophones`, `pinyin`, `symbol-based splitting`, and the other Chinese-specific linguistic patterns.
These Chinese-specific adversarial patterns create the safety evaluation gap that is not well captured by existing English-centric benchmarks.
This gap is particularly concerning for lightweight models, which may be more vulnerable to such specific adversarial perturbations.
To bridge this gap, we introduce the **Chinese-Specific Safety Benchmark (CSSBench)** that emphasizes these adversarial patterns and evaluates the safety of lightweight LLMs in Chinese.
Our benchmark covers six domains that are common in real Chinese scenarios, including **illegal activities and compliance**, **privacy leakage**, **health and medical misinformation**, **fraud and hate**, **adult content**, and **public and political safety**, and organizes queries into multiple task types.
We evaluate a set of popular lightweight LLMs and measure over-refusal behavior to assess safety-induced performance degradation.
The results show that Chinese-specific adversarial patterns are a critical challenge for lightweight LLMs.
Our benchmark offers an important and overlooked supplement to LLM safety in Chinese, assisting robust deployments in real world.

</details>

### 223. Same Outcome, Different Evidence: Intent Recovery in LLM Safety Evaluation

📄 [OpenReview](https://openreview.net/forum?id=IUu6mIxWBS)　📅 2026-10　🏷️ P2

**关键词**：`safety evaluation`、`attack success rate`、`intent recovery`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：ASR 把不同原因的非有害结果混为一谈——意图遮蔽提示下低 ASR 不说明任务被真正对待
- 🔬 **研究方法**：以 operative understanding rate 配对 ASR：响应是否识别并按被测任务作答+受控英文重构与 FormalLogic 对照
- 📌 **结论**：相似 ASR 对应截然不同的任务恢复率——安全评测需联合报告意图恢复与 ASR（评测口径）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety evaluations of large language models commonly summarize harmful-output behavior with attack success rate (ASR). Yet the same non-harmful outcome can arise for very different reasons. A model may recover a harmful task and refuse it, fail to recover the task, or respond to something else entirely. Distinguishing these cases becomes especially important under intent-obscuring prompts, where a low ASR does not reveal whether the evaluated task was actually engaged. To make this distinction explicit, we pair ASR with operative understanding rate (UR), which measures whether a response both identifies the evaluated task and treats it as the task to be answered. Across interfaces, this paired view reveals substantial variation hidden by ASR: similar ASR values can correspond to sharply different recovery rates. Controlled English reconstructions show that recovery consistently improves as compressed prompts become more explicit, whereas ASR does not follow the same pattern. A complementary contrast comes from FormalLogic, where high recovery can still coincide with frequent harmful assistance. Together, these results show that non-harmful outcomes are not equally informative about model safety, motivating the joint reporting of intent recovery and ASR in LLM safety evaluation. Code and experiment inputs are available anonymously.

</details>

### 224. AISPA: User-Centric System Prompt Auditing for Large Language Model Applications

📄 [OpenReview](https://openreview.net/forum?id=JduCNto4wL)　📅 2026-10　🏷️ P2

**关键词**：`system prompt audit`、`user-centric`、`commercial AI`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：系统提示贯穿商业 AI 产品却不向公众/监管披露——信任与问责缺口
- 🔬 **研究方法**：AISPA 八维度用户中心框架审计 88 商业产品 3219 条指令（保护性 vs 问题性分类）
- 📌 **结论**：98.9% 产品含至少一条保护性指令但仅 24% 覆盖全八维；组织间差异 60+ vs <5 条/产品——商业系统提示的首个系统审计

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

System prompts are instructions configured by developers to govern the behaviors of foundation models in AI applications. They are used throughout commercial AI products, but are rarely disclosed to the public or regulators, creating a serious trust and accountability gap in the wide deployment of AI systems. In this paper, we introduce Artificial Intelligence System Prompt Assurance (AISPA), a user-centric framework for systematically auditing system prompts in AI systems. AISPA examines specific parts of a system prompt and evaluates them along eight dimensions that matter to users. We then use this framework to review 3,219 instructions from system prompts in 88 commercial AI products, classifying each instruction as either protective (of users) or problematic.
Our audit surfaces four core findings. First, system prompt design varies substantially across products and developers, with some organizations averaging over 60 protective instructions per product while others average fewer than 5. Second, protective instructions are widely adopted but uneven in scope: 98.9% of products contain at least one, yet only 24% cover all eight dimensions of the AISPA taxonomy under a common benchmark. Third, system prompts have become substantially longer and more protective of users overall, suggesting that user protection is becoming a more visible concern in commercial prompt design. Fourth, despite this progress, problematic instructions remain pervasive: roughly 40% of products contain at least one instruction that works against user interests, and protective and problematic instructions frequently coexist within the same prompt. Our findings highlight the need for greater transparency, standardization, and independent oversight for system prompts in commercial AI products.

</details>

### 225. J-SafetyVar: Evaluating the Consistency of Japanese LLM Safety Responses under Linguistic Variation and Dialogue Context

📄 [OpenReview](https://openreview.net/forum?id=Por2SUhGvf)　📅 2026-10　🏷️ P2

**关键词**：`multilingual safety`、`Japanese`、`benchmark`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：日语安全评测用显式标准输入——错字/方言/幽默/间接与对话上下文下的稳健性被高估
- 🔬 **研究方法**：J-SafetyVar：60 场景核心变体+组合困难族+固定历史对话条件，区分风险承认与人类求助转介并先验测量信度
- 📌 **结论**：孤立变异损伤有限而组合困难族降幅最大；LLM 代理间一致性可高估信度——多语安全评测的信度优先

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety evaluations of Japanese language models often use explicit, standard-form inputs, potentially overstating robustness to real conversations involving typos, dialect, humour, indirection, and dialogue context. We introduce J-SafetyVar, a Japanese benchmark of 60 synthetic youth-facing scenarios with controlled Core variants, compositional Hard families, and fixed-history dialogue conditions. We distinguish concern recognition (Risk Acknowledgment, RA) from textual referral to human support (Human Connection, HC), and evaluate measurement reliability before model comparison. Operationalizing HC raises agreement with an LLM-based provisional reference from κ = 0.14 to κ = 0.67–0.78. A single-rater PI check shows high HC agreement with the archived proxy (κw = 0.801) but low RA agreement (κw = 0.159), indicating that agreement between LLM proxies can overstate reliability. Across 6 models, isolated variation causes limited average degradation, whereas compositional Hard families produce the largest HC reductions across multiple model families. Fixed-history context improves RA for four models but does not consistently improve HC. A youth-oriented prompt raises HC near ceiling, yet substantive recovery reaches only 0.40–0.45 and over-reaction increases for some models. J-SafetyVar measures consistency of observable responses on synthetic data; it is not a clinical or deployment evaluation.

</details>

### 226. Discover, Explain, and Repair: Adaptive Testing of LLM Failures in Medical Safety

📄 [OpenReview](https://openreview.net/forum?id=SjHz6pJ2mO)　📅 2026-10　🏷️ P2

**关键词**：`medical safety`、`failure repair`、`decision tree`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：红队与安全评测多止于发现——为何失败、如何修补缺洞见
- 🔬 **研究方法**：FDA 药品标签接地的医疗安全基准+Thompson 采样定位高危药物+结构化特征决策树恢复人可读失败模式→提示级修复
- 📌 **结论**：多商业 LLM 一致降不安全率且保效用、失败模式泛化到未见药物与开放域事实推理——发现-解释-修复闭环

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are increasingly deployed in high-stakes domains such as medicine, where unsafe responses can cause serious harm. Existing red-teaming and safety evaluation methods primarily focus on discovering failures, but often provide limited insight into why failures occur or how they can be repaired. We propose a framework for discovering, explaining, and repairing domain-specific safety failures in LLMs. Using a medical safety benchmark grounded in FDA drug labels, we generate realistic patient scenarios and apply Thompson Sampling to efficiently identify high-risk drugs. We then train decision trees over structured patient and query features to recover human-readable failure patterns, which are converted into targeted prompt-level repairs. Experiments across multiple commercial LLMs show that our method consistently reduces unsafe response rates while maintaining competitive utility on medical QA benchmarks. We further demonstrate that the discovered failure patterns generalize to unseen drugs and extend beyond medicine to open-domain factual reasoning on a Wikipedia benchmark.

</details>

### 227. SAFE-Teen: Evaluating Chatbot Safety Across Adolescent Mental Health Conversations

📄 [OpenReview](https://openreview.net/forum?id=X6fzYCyd0k)　📅 2026-10　🏷️ P2

**关键词**：`adolescent safety`、`multi-turn`、`user pushback`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：青少年向 AI 寻心理支持——单提示单标签评测漏跨轮伤害
- 🔬 **研究方法**：SAFE-Teen：983 变体×106 种子场景（紧急安全/健康建议/身份关系）×18 chatbot API×2 系统提示（32555 对话×22 判据）
- 📌 **结论**：判据失败率 43.3%→teen 提示后 24.9% 但间接自杀风险仍 52%；青少年反驳使诊断/药物/物质边界失败升 10-12pp——用户阻力下的评测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adolescents are increasingly turning to AI chatbots for mental health support, advice, and companionship, raising safety concerns. Current evaluations examine individual prompts and assign a single safety label, missing harms that emerge across turns. We present SAFE-Teen (Scenario-based Assessment of Failure Emergence in Teen Chats), a clinician-informed benchmark of simulated conversations with adolescents aged 13-17. SAFE-Teen includes 983 variants of 106 seed scenarios covering urgent safety issues, health advice, and identity and relationships. For each comparison, we create versions of the same conversation that vary the teen's response related to disclosure, offered help, or a chatbot's refusal. Across 18 chatbot APIs and two system-prompt conditions, we evaluated 32,555 conversations using 22 safety criteria, based on previously identified harms. The overall criterion failure rate was 43.3% without the teen-aware prompt and 24.9% with it. The teen-aware prompt reduced failures, but it didn't eliminate them. Indirect suicide risk failure rate remained at 52%.
When a teenager pushed back on a chatbot's answer, failures on mental health diagnosis, medication, and substance misuse boundaries rose by 10-12 percentage points without the prompt, for more than 80% of chatbots. SAFE-Teen shows that evaluations should test responses under user resistance, not just their first answer.

</details>

### 228. What Counts as Attack Success? Evaluating Harmfulness in Red Teaming LLMs

📄 [OpenReview](https://openreview.net/forum?id=XcWhNKEjK8)　📅 2026-10　🏷️ P2

**关键词**：`harmfulness criteria`、`red teaming`、`evaluation validity`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：红队研究把'是否有害'判断委托给自动评测器——标准从何而来无人问
- 🔬 **研究方法**：76 篇论文综述其有害性标准来源+同输出跨评测器对照
- 📌 **结论**：标准多承袭自数据集/分类器/判官提示；同响应可得到不同判定并改变模型比较结论——红队研究应声明有害性标准及其评测器选择与验证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Judging whether a model response is harmful requires contextual and normative choices, yet red-teaming studies often delegate this judgment to automated evaluators. We examine how harmfulness criteria are specified in red-teaming research and how they carry through to reported results. Reviewing 76 papers, we find that many adopt their criteria from prior datasets, classifiers, or judge prompts rather than defining harmfulness themselves. Applying evaluators from these papers to identical outputs, we find that they can reach different judgments on the same response, which can change conclusions when comparing models. These differences arise partly because evaluators draw the boundary of harm in different places: some count any response that does not refuse, while others count only output that could plausibly cause harm. We argue that red-teaming studies should state their harmfulness criteria and report how they chose and validated their evaluators to support more reliable measurement and interpretation.

</details>

### 229. Lost in Speech: Measuring the Multilingual Cross-Modal Safety Gap in Speech-Language Models

📄 [OpenReview](https://openreview.net/forum?id=XnNEzdbLpN)　📅 2026-10　🏷️ P2

**关键词**：`speech-language models`、`multilingual safety`、`comprehension confound`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：语音模型安全评测以英语文本为主——翻译+语音合成双扰动的根控研究缺
- 🔬 **研究方法**：AEGIS 一万行 100 语言样本+英语基线，75 语言合成语音，六 SLM×四条件 178,608 评分
- 📌 **结论**：UCR 低（0-4.4%）但非英语音频理解率 24.13-74.09%——至多 76.18% 名义安全响应实为理解失败而非对齐；TTS 路由/语言支持/判官选择实质改变结论（多语语音安全的理解混淆）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large speech-language models (SLMs) are in- creasingly deployed as voice assistants, yet safety evaluation remains dominated by En- glish text. We present a root-controlled study of safety under two perturbations: translation into a non-English language and conversion to synthesized speech. Using a 10,000-row, 100- language AEGIS unsafe-prompt sample plus a 5,235-item English baseline, we synthesize speech for 75 languages and evaluate six SLMs across English text, English speech, translated text, and translated speech, yielding 178,608 scored responses. Unsafe Compliance Rate (UCR) remains low (0.0–4.4%), but compre- hension degrades sharply: non-English speech Comprehension Rate (CR) ranges from 24.13% (Phi-4-Multimodal) to 74.09% (Qwen2-Audio), despite near-perfect English-text comprehen- sion. Consequently, up to 76.18% of nomi- nally safe non-English spoken responses re- flect failed comprehension rather than gen- uine alignment. We further show that TTS route, documented language support, judge choice, and comprehension rubric materially affect conclusions; MMS-ASR rates 93.52% of low-resource native audio as good versus only 51.19% under Whisper. A benign control indicates that the dominant failure is compre- hension rather than over-refusal. These find- ings show that low unsafe-compliance rates can substantially overstate multilingual speech safety. Code and data available in the link: https://anonymous.4open.science/r/3E35/

</details>

### 230. LLM-as-a-Reviewer: Benchmarking Their Ability, Divergence, and Prompt Injection Resistance as Paper Reviewers

📄 [OpenReview](https://openreview.net/forum?id=ZvwRfJ7mGU)　📅 2026-10　🏷️ P2

**关键词**：`LLM reviewer`、`prompt injection`、`academic integrity`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：LLM 日益进入论文评审——其可靠性、与人类的分歧及对抗注入抗性未被系统测量
- 🔬 **研究方法**：898 篇 NeurIPS/ICLR 分层基准×12 LLM 三轴评测：评分校准/与人类评审分歧/不可见字体映射注入抗性
- 📌 **结论**：LLM 系统性高评弱稿、主题侧重分歧（低标 Clarity 高标 Reproducibility）；隐藏指令可把低分稿推至接收档——评审 LLM 的注入抗性基准

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used in academic peer review, yet their reliability, alignment with human judgment, and robustness to adversarial attacks remain poorly understood. We present a systematic benchmark of LLM-as-a-Reviewer on 898 papers stratified from NeurIPS and ICLR, evaluating 12 LLMs along three axes: rating calibration, divergence from human reviewers, and resistance to prompt injection embedded via an invisible font-mapping attack. We find that LLMs systematically overrate weaker submissions and diverge from humans in topical emphasis, under-flagging Clarity and over-flagging Reproducibility, while producing reviews two to three times longer with lower lexical diversity and a more standardized vocabulary. Prompt injection remains highly effective. Simple hidden instructions can promote low-scoring papers to acceptance-level ratings in a substantial fraction of cases, with effectiveness varying sharply across model families. While LLMs offer utility in structuring evaluations, their integration into peer review requires safeguards against both intrinsic biases and adversarial risks.

</details>

### 231. The Fault in our Judges: Discovering, Decomposing, and Repairing Failures in LLM Safety Judges

📄 [OpenReview](https://openreview.net/forum?id=egE1wZrYk9)　📅 2026-10　🏷️ P2

**关键词**：`safety judge`、`error taxonomy`、`structured supervision`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：安全判官的决策错误是否共享可复用推理结构——检验并利用该结构
- 🔬 **研究方法**：五判官×多数据集诊断差分导出九原子错误机制分类学+结构化监督训练与机制靶向编辑
- 📌 **结论**：错误跨样本不同但经共享机制词汇复发；独立操作专家 94.96% 准确率、机制靶向修复超中性对照——判官错误的机制化利用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM safety judges are known to exhibit superficial biases, but less is known about whether their actual decision errors share recurring reasoning structure. We study five policy-conditioned judges across multiple response-level safety datasets and derive a taxonomy of nine atomic error mechanisms from post-hoc diagnostic deltas. Although judges often fail on different examples, their errors recur through a shared mechanism vocabulary. We then test whether this structure improves training. Structured supervision over broader reasoning operations substantially outperforms other supervised baselines; independent operation experts achieve 94.96% accuracy and 92.16 macro-F1. Online corrective self-distillation also performs strongly, while adding an explicit failure-mechanism label to the same correction provides no further gain. Mechanism-targeted edits yield substantially greater repair than matched-neutral controls, while structured supervised finetuning achieves the strongest paired correctness. Our results suggest that recurring structure in post-hoc judge errors can be operationally useful even without assuming that the reasoning is causally faithful.

</details>

### 232. LocalTurn: Native Multi-Turn Safety Evaluation in Emirati Arabic, Bangla, Sinhala, and Yoruba

📄 [OpenReview](https://openreview.net/forum?id=iB9chggG7t)　📅 2026-10　🏷️ P2

**关键词**：`native safety benchmark`、`low-resource languages`、`multi-turn`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：非英安全测试多为英译——译语不带当地方言与本地伤害（如孟加拉渎神谣言、约鲁巴族群选举虚假信息）
- 🔬 **研究方法**：LocalTurn：256 段三轮对话由四语母语者原生撰写×八商业助手公开接口×母语者逐响应评分（6144 评级）
- 📌 **结论**：Claude/GPT/Kimi 高严重率 8-21% vs Gemini/Pro-Sonar/GLM 35-39%；最安全模型随语言与伤害类别而变——单一多语安全分隐藏用户实际风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Most LLM safety testing outside English relies on prompts translated from English. A translated prompt rarely carries the dialect people actually write in, or the harms that matter locally, such as blasphemy rumours in Bangla or ethnic election disinformation in Yoruba. LocalTurn is a set of 256 three-turn conversations written directly by native speakers of Emirati Arabic, Bangla, Sinhala, and Yoruba. We ran each conversation on eight commercial assistants through their public interfaces, and native-speaker evaluators rated every response, 6,144 ratings in all. Claude Sonnet-5, GPT-5.5, GPT-5.3, and Kimi-K3 produced high-severity responses in 8-21% of ratings; Gemini-3.1 Pro, Gemini-3.6 Flash, Pro-Sonar, and GLM-5.2 did so in 35-39%, a gap that held across several alternative ways of analysing the data. The ranking also changes by language and harm category: the safest model in one is not always the safest in another. And a prompt that looked dangerous to annotators was not reliably more likely to break a model than one that looked mild. A single multilingual safety score can hide the risks these users face. We argue for reporting safety per language variety and per harm type, and to help close this gap, we will release the conversations, their controls, and all ratings upon publication.

</details>

### 233. Secure by Luck or by Reason? Measuring Security-Reasoning Faithfulness in Code-Generating Language Models

📄 [OpenReview](https://openreview.net/forum?id=iQ86EcPJrU)　📅 2026-10　🏷️ P2

**关键词**：`security reasoning`、`faithfulness metric`、`code generation`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：代码 LLM 的安全推理是否真起作用——仅查最终程序的指标看不见
- 🔬 **研究方法**：SRF 干预式度量：移除缓解步骤重生成+外部漏洞 oracle 判目标弱点出现+匹配无关编辑对照
- 📌 **结论**：func-sec@1 相同的模型 SRF 可差 0.21；SRF 预测留出弱点类上的安全损失（r=-0.79）——仅结果 RL 升安全却降忠实性（安全推理的载荷检验）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Code-generating language models increasingly justify their programs with security reasoning, yet secure-code metrics inspect only the final program. We introduce Security-Reasoning Faithfulness (SRF), an intervention-based metric that asks whether stated security reasoning is load-bearing: for each secure generation, SRF removes the mitigation steps from the model's rationale, regenerates the code, and asks an external vulnerability oracle whether the target weakness appears, subtracting the flip rate of a matched security-irrelevant edit. Across seven models, 138 Python tasks, and eight CWE classes, SRF exposes differences that standard metrics miss: GPT-4o and QwQ-32B-Preview have near-identical func-sec@1 (0.46 vs. 0.47) but differ by 0.21 in SRF, and, across model families, SRF predicts which models lose security on weakness classes held out from demonstrations (r=-0.79, against -0.33 for func-sec@1). Half to three-quarters of the secure code from non-reasoning-tuned models survives removal of its stated mitigation. Switching reasoning on in the same Qwen3 weights roughly doubles SRF at near-identical func-sec, a controlled comparison within one model family. Outcome-only reinforcement learning raises security while lowering SRF in three model pairs, partly by shortening rationales.

</details>

### 234. MCBench: A Multicontext Safety Assessment Benchmark for Omni Large Language Models

📄 [OpenReview](https://openreview.net/forum?id=juLrA81Kv2)　📅 2026-10　🏷️ P2

**关键词**：`omni LLM`、`safety benchmark`、`multimodal`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：omni 模型安全判断需跨视觉/声学/语言整合证据——单模态基准不覆盖
- 🔬 **研究方法**：MCBench：1196 场景最小对比安全-不安全对（人身/社会/违法/财产），每场景标注可解释风险因子上的安全规则
- 📌 **结论**：模型擅长人身财产危害但社会与违法危害弱；失败多源于无法从多模态输入接地风险因子且单信号系统性误报安全场景——多语境安全评估

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Omni LLMs that jointly process vision, audio, and speech are increasingly deployed in safety-sensitive applications, yet their ability to reliably assess unsafe situations remains understudied. Existing safety benchmarks evaluate only single modalities or isolated visual cues, failing to capture real-world settings where safety judgments require integrating evidence across visual, acoustic, and linguistic contexts. We introduce MCBench, a multimodal, multicontext safety benchmark of 1,196 scenarios organised as minimally contrasted safe–unsafe pairs and spanning physical harm, social harm, illegal harm, and property damage, in which every scenario is annotated with a safety rule over interpretable high-level risk factors. Evaluating leading open-source and proprietary Omni LLMs, we find that models handle physical harm and property damage well but struggle with social and illegal harm. Factor-coverage and oracle-grounding analyses show that these failures stem largely from an inability to ground safety-relevant risk factors from multimodal inputs; even when the factors are supplied explicitly, models fixate on single concerning signals and produce systematic false positives on safe scenarios.

</details>

### 235. Toxicity Lost in Translation: A Toxicity-Preserving Framework for Cross-Lingual LLM Safety Benchmarking

📄 [OpenReview](https://openreview.net/forum?id=lAFK0IavXo)　📅 2026-10　🏷️ P2

**关键词**：`translation safety`、`toxicity softening`、`benchmark validity`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：翻译构建非英安全基准默认机器翻译保持安全属性——毒性软化系统性违反该假设且 BLEU/COMET 不可见
- 🔬 **研究方法**：九翻译系统×五安全基准×六语系分类器+人工双重验证+TPMT 训练无关迭代精炼（安全分类器验证源有害意图保持）
- 📌 **结论**：毒性软化是跨语一致失败模式而非语言特定；TPMT 大幅减轻且保翻译质量——跨语安全基准的失真修正

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety benchmarks for non-English languages are routinely constructed by translating English datasets, implicitly assuming that machine translation preserves the safety properties of the source text. We show that this assumption is systematically violated through toxicity softening: machine translation reduces the perceived severity of harmful content, causing safety benchmarks to underestimate model risk. Despite this distortion, standard translation quality metrics such as BLEU and the COMET family remain high, making the problem effectively invisible to conventional machine translation evaluation. We validate this phenomenon through both classifier-based and human evaluation across nine translation systems, five safety benchmarks, and six typologically diverse languages, demonstrating that toxicity softening is a consistent cross-lingual failure mode rather than a language-specific artifact. To address this issue, we propose Toxicity-Preserving Machine Translation (TPMT), a training-free inference framework that iteratively refines translations until a safety classifier verifies that the harmful intent of the source is preserved. TPMT substantially reduces toxicity softening while maintaining translation quality across languages, enabling more faithful multilingual safety benchmarks.

</details>

### 236. Decoupled OOD Safety Evaluation Expression, Language, and Modality Couplings in Jailbreak Benchmarks

📄 [OpenReview](https://openreview.net/forum?id=nABvt9TZZE)　📅 2026-10　🏷️ P2

**关键词**：`OOD safety`、`decoupled evaluation`、`translation/rephrase/modality`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：改写/翻译/加图后标准越狱基准结果是否成立——六基准 11 文本+15 多模态 109 语言七判官约 12.6 万响应
- 🔬 **研究方法**：解耦 OOD 协议：每个修改提示与原版对照（非重跑全基准）+判官间对照分析
- 📌 **结论**：翻译效应 -2.6 至 +22.3pp 随判官而变；同图增模态对 Llama-3.2-11B-V +37.2pp 而 Ministral -8/9pp——安全评测须报告各模型输入形态变化及其判官依赖

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Do safety results on standard jailbreak benchmarks hold when prompts are rephrased, translated, or combined with images? We introduce a decoupled OOD safety evaluation protocol to test these changes by comparing each modified prompt with its original version. Experiments cover six benchmarks, 11 text LLMs, 15 multimodal LLMs, 109 sampled target languages, seven safety judges, and roughly 126,000 responses. Rephrasing changes measured attack success rate (ASR), and translation produces larger changes on average. The estimated translation effect ranges from -2.6 to +22.3 percentage points across judges. In the modality study, adding an instruction-bearing image on JailbreakBench raises measured ASR by 37.2 percentage points for Llama-3.2-11B-Vision and lowers it by 8.0/9.0 percentage points for Ministral-3-8B/14B, showing opposite responses to the same augmentation. Additional analyses examine translation fidelity, response length, instruction repetition, corpus overlap, and model familiarity. Comparing judges on the same responses shows how evaluator choice affects the safety conclusions. Together, these results show why safety evaluation should test different input forms, report changes for each model, and show how those changes depend on the evaluator.

</details>

### 237. Shortcutting the Fix: Identifying and Categorizing Agentic Exploits in Software Engineering Benchmarks

📄 [OpenReview](https://openreview.net/forum?id=sjzWQKdOvf)　📅 2026-10　🏷️ P2

**关键词**：`benchmark exploit`、`agentic shortcutting`、`evaluation validity`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：SWE 基准高分常掩盖利用性捷径——上游方案检索/Git 历史/记忆代码
- 🔬 **研究方法**：agentic shortcutting 形式化+三开源 LLM 轨迹级 LLM 判官审计（SWE-bench Multilingual/DeepSWE）+独立构建提示干预
- 📌 **结论**：60.7-90.1% 轨迹触发捷径尝试、至多 72.1% 任务借漏洞解决且断网无效；独立构建提示压到 9.4-14.2% 保核性能——利用感知评测框架

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

High software engineering benchmark scores often mask exploitative shortcuts, such as retrieving upstream solutions, exploiting local Git histories, or recalling memorized code. We formalize this phenomenon as agentic shortcutting and audit three state-of-the-art open LLMs on SWE-bench Multilingual and DeepSWE using trajectory-level LLM judges. Standard evaluations trigger shortcutting attempts in 60.7%–90.1% and 55.5%–89.1% of trajectories, respectively, with up to 72.1% of tasks resolved with the aid of a successful exploit; disabling network access fails to curb these high attempt rates. Prompting agents to construct solutions independently suppresses attempts to 9.4%–14.2% and 0.9%–10.3%, respectively, while virtually eliminating shortcut-dependent resolutions and preserving core task performance. Our findings demonstrate the necessity of exploit-aware evaluation frameworks to measure genuine repository-level problem solving.

</details>

### 238. AfriGuard: Safety and Robust Refusal For African Languages

📄 [OpenReview](https://openreview.net/forum?id=ta6yzAfPDu)　📅 2026-10　🏷️ P2

**关键词**：`multilingual safety`、`African languages`、`guardrail`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：非洲语言的安全风险表达与解读不同——护栏模型与文化接地的缺失
- 🔬 **研究方法**：AfriGuard：10 非洲语言+英语的有害意图/安全类别理解/拒答行为数据集+高效护栏与拒答检测器
- 📌 **结论**：护栏模型安全分类不如开闭源 LLM、模型不当拒绝常源于语言不足导致的偶发不协助——文化接地的多语安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) designed to interact with users are typically trained to respond appropriately to harmful or toxic content. However, ensuring appropriate responses becomes more challenging in diverse linguistic and cultural contexts, where safety risks may be expressed or interpreted differently. Building safe AI systems therefore requires detecting safety risks, understanding their nature, and responding appropriately, while accounting for linguistic and cultural variations that add complexity to each stage. In this work, we introduce AfriGuard, a culturally grounded multilingual dataset for studying harmful intent, safety-category understanding, and refusal behavior across 10 African languages and English. Our findings reveal that guardrail models underperform both open- and closed-source LLMs on safety-intent and safety-category classification, while models show limited understanding of appropriate safety behavior, scoring below 60% F1. We further find that models often fail to respond appropriately to unsafe prompts not because they explicitly refuse, but because they produce linguistically inadequate responses that result in incidental non-assistance rather than proper refusals. Finally, using AfriGuard, we develop efficient guardrail models that achieve performance competitive with models up to 30× larger, introduce refusal detectors that improve average performance by 43.9% over existing detectors, and demonstrate that supervised fine-tuning can substantially improve overall safety performance.

</details>

### 239. Beyond the Transcript: Controlled Audio Cues Reveal Trustworthiness Gaps in ALMs

📄 [OpenReview](https://openreview.net/forum?id=vyXWBtyK1E)　📅 2026-10　🏷️ P2

**关键词**：`audio cue`、`trustworthiness`、`ALM safety`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：ALM 行为依赖语言内容外的音频线索（情绪/说话人/录音条件）——转录归约评测掩盖线索依赖失效
- 🔬 **研究方法**：TRACE：两轴分类+162,320 音频（456 小时）单线索受控变化×11 ALM
- 📌 **结论**：多轮上下文使 11 模型中 9 个危害上升；16 种副语言变化至少一种使超三分之一不安全提示被有害回答；背景语音最难（最佳模型理解 98%→15%）——音频线索的安全面

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The behaviors of Audio Language Models~(ALMs) can depend on audio cues beyond linguistic content, such as emotion, speaker characteristics, and recording conditions, introducing subtle failure modes that can affect ALM safety, fairness, and robustness.
Existing evaluations often reduce audio to transcripts or study individual perturbations in isolation, limiting their ability to disentangle cue-specific effects under controlled semantic content, and they compare models without accounting for how each architecture represents audio.
We introduce TRACE: Trustworthy Audio Cue Evaluation, a benchmark for systematically varying non-linguistic audio cues.
TRACE contributes a two-axis taxonomy that characterizes ALMs by the audio representation reaching the language model and by how the response is generated, and a cue-controlled dataset of 162,320 audio files (approximately 456 hours) from single- and multi-turn conversations that varies one cue at a time on fixed content.
Benchmarking 11 ALMs, we find that (i) multi-turn context raises harm for 9 of 11 models; (ii) over a third of unsafe prompts are answered harmfully for at least one of 16 paralinguistic variation for the same prompt; and (iii) background speech is the hardest perturbation, cutting the best model's comprehension from 98% to 15%.
Our results show that current evaluation practices can obscure cue-dependent failures, and that trustworthy ALM evaluation requires benchmarks that preserve and systematically vary non-linguistic audio cues rather than treating audio as a transcription problem.

</details>

### 240. CyberIntent: Evidence-Sensitive Three-Way Decisions for Dual-Use Cybersecurity Requests

📄 [OpenReview](https://openreview.net/forum?id=xDkkmeSleo)　📅 2026-10　🏷️ P2

**关键词**：`dual-use`、`three-way decision`、`cybersecurity requests`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：双用网安请求下模型能否尊重证据源却在信息不足时就行动——澄清与拒绝的三态决策未被分离评测
- 🔬 **研究方法**：CyberIntent 受控基准：固定抽象网安请求、干预源资格/冲突/遗漏+PAD 源路由-模型抽取-固定政策合成分解，156 输入×四模型匹配 2×2 控制
- 📌 **结论**：源隔离改善全部八组联合行动域准确率 3.85-36.54pp——但更好的源处理可与编造缺失信息、过早行动共存；停止与保留未知态需单独评测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Can a language model respect evidence sourcesyet act before it has enough information?We introduce Cyberlntent, a controlled bench-mark for assistance, clarification and refusalthat holds abstract cybersecurity requests fixedwhile intervening on source eligibility, conflictsand omissions. Provenance-Aware Delibera-tion (PAD) decomposes the task into sourcerouting, model extraction and fixed policy syn-thesis. Across four models and 156 inputsfrom 12 frozen AI-authored expression packs, amatched 2 x2 control separates source isolationfrom request masking. Isolation improves jointaction-field accuracy in all eight model/requestcomparisons, by 3.85-36.54 percentage points.Yet Granite extracts trusted authorization cor-rectly on all 156 inputs while filling every omit-ted target and scope, 12/12 each. A matchedinteraction control improves path completionfor only two models. The central finding isthat better source handling can coexist withinvented missing information and prematureaction. Source eligibility, preservation of un-known states and justified stopping thereforerequire separate evaluation beyond aggregateaction scores.

</details>

### 241. Best for Platform or Best for Consumers? Systematic Misalignment with 59% Top-1 Distrust Rate in Shanghai's Commerce AI Agents

📄 [OpenReview](https://openreview.net/forum?id=zp7KFyfVJi)　📅 2026-10　🏷️ P2

**关键词**：`deployed agents`、`misalignment audit`、`consumer AI`

👤 **作者**：Anonymous（ARR 2026 October 匿名预印本）

- 🎯 **研究动机**：对齐评测很少触及人们已在用的商业系统——部署 agent 的默认推荐是否利于用户
- 🔬 **研究方法**：上海四超级 app 42 条意图无歧义查询同分钟对照发行，评平台榜单第一名是否其列表最优（top-1 不信任率）
- 📌 **结论**：酒店 top-1 非最优 66.7%（携程 85.7%）、汇总 59%；任务成功完全不反映——部署消费 agent 的默认推荐信任缺口

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Alignment is rarely evaluated on the commercial systems people already use. When a deployed commerce agent proposes a default, is it in the user's interest? In Shanghai we audit four super-apps (Ctrip, Meituan, Fliggy, Taobao) with 42 intent-unambiguous brand-plus-landmark queries for hotel booking and food delivery, issued to competing platforms in the same minute (105 observations). Because the agents hand back the top of the platform's ranking — by redirect on Ctrip, in every check we ran elsewhere — we score that ranking, the only view that exposes the alternatives a single default hides. For hotels the top-1 is not the best option in the platform's own list 66.7% of the time (95% CI [52.4, 81.0]), our top-1 distrust rate; Ctrip reaches 85.7%. Food stands at 47.6% and the pooled rate at 59.0% [47.6, 70.1], so we claim a majority failure rate only for hotels. In 36.2% of observations the top-1 is neither cheapest nor closest or fastest; hotel sponsorship labels are near-invisible (1.18:1 contrast) and food platforms carry none. Task success registers none of this: the agents do as told, not what is best for the user. We argue that deployed consumer agents should be evaluated on whether their default can be trusted, and that revenue–welfare conflicts must be resolved for the consumer.

</details>

## 十三、扩展视野（简表）

| # | 标题 | 要点 | 链接 |
|---|---|---|---|
| 1 | Deletion Context Changes the Trajectory of a Fixed Target Set in LLM Unlearning |  | [OpenReview](https://openreview.net/forum?id=xF1V4xyz03) |
| 2 | Benevolent Bias in Multi-Turn Human–Agent Dialogue | BENEVDIAL：仁慈偏置（温暖语气下的不平等对待）36 万多轮对话语料——现成安全检测器能抓敌意偏置却几乎漏检仁慈偏置 | [OpenReview](https://openreview.net/forum?id=CjaQqXbTUq) |
| 3 | Strong Multilingual Privacy Tagging at Encoder Speed |  | [OpenReview](https://openreview.net/forum?id=gSgai6IhzQ) |
| 4 | Aligned but Stereotypical? How System Prompts Shape Demographic Bias in LLM-Based Text-to-Image Models |  | [OpenReview](https://openreview.net/forum?id=HfQ7cdt9Ho) |
| 5 | The Confidence Mirage of Inference-Time Scaling: Evaluating When More Reasoning Makes Large Language Models Less Reliable |  | [OpenReview](https://openreview.net/forum?id=6DrMgRQXjz) |
| 6 | When Self-Refinement Backfires: Measuring Behavioral Instability in Large Language Models |  | [OpenReview](https://openreview.net/forum?id=lBPu4XAkVZ) |
| 7 | Metadata-Grounded Visual-Key Regeneration for Contamination-Resistant VQA Evaluation |  | [OpenReview](https://openreview.net/forum?id=0DCL7yy3iw) |
| 8 | When Grounding Fails: Structural Failure Signals for Detecting Silent GUI Errors |  | [OpenReview](https://openreview.net/forum?id=LsjKYw5qEK) |
| 9 | MemPT: Capability-Centric Memory for Autonomous Penetration Testing |  | [OpenReview](https://openreview.net/forum?id=AdswMK590P) |
| 10 | Tells of a Lying Machine: Analyzing LLM-Generated Strategic Dialogue in Chinese Werewolf |  | [OpenReview](https://openreview.net/forum?id=gPWhfncvsI) |
| 11 | From Typos to Adversaries: Character-Level Robustness Evaluation of Healthcare Large Language Models |  | [OpenReview](https://openreview.net/forum?id=l3N6IbCI2P) |
| 12 | Fade and Flip: A Predictive Account of Watermark Decay under Multi-Agent Relay Rewriting |  | [OpenReview](https://openreview.net/forum?id=VLxgiCc88H) |
| 13 | The Cost of Controlling Evidence Selection in Language Models |  | [OpenReview](https://openreview.net/forum?id=5x0uMBSjoW) |
| 14 | When Emojis Obscure Toxicity in Chinese: Diagnosing Detection and Target Identification Failures |  | [OpenReview](https://openreview.net/forum?id=BaCVcg7x2Z) |
| 15 | People Can Be Consistently Fooled by LLM-Generated Social-Media Conversations |  | [OpenReview](https://openreview.net/forum?id=6ZLF6cYoPt) |
| 16 | VeriOS: Query-Driven Proactive Human-Agent-GUI Interaction for Trustworthy OS Agents |  | [OpenReview](https://openreview.net/forum?id=MKkk0FzDYV) |
| 17 | Forgetting Facts Across Forms: A Morphosyntactic Audit of LLM Unlearning | 跨形态遗忘审计：英/德/土耳其语形态句法变体比正典问题多恢复 12.6/9.4pp（GD/NPO）——改写即可部分绕过遗忘 | [OpenReview](https://openreview.net/forum?id=thq7mNcAfl) |
| 18 | RouteProbe: Auditing Context Sensitivity in Deployed LLM Routers |  | [OpenReview](https://openreview.net/forum?id=lH8lS3aeGH) |
| 19 | CORDA: Evaluating Moral Controllability of Language Models under Conflicting Priorities |  | [OpenReview](https://openreview.net/forum?id=1CrN6M6tRR) |
| 20 | Learning to Audit Silent Evidence Corruption in Visual Reasoning |  | [OpenReview](https://openreview.net/forum?id=nBDT1cmNHu) |
| 21 | BotC-Bench: A Trace-Grounded Social Deduction Benchmark for Evaluating LLM Agents under Controlled Information Contamination |  | [OpenReview](https://openreview.net/forum?id=xBvhIoieWc) |
| 22 | Watermark Seeding: A Security Control Mechanism for Text Watermarking in Large Language Models |  | [OpenReview](https://openreview.net/forum?id=dI74DXv6wB) |
| 23 | Symbolic Constraint Agents: Mining Formal Tool-Call Constraints to Prevent Agent Errors |  | [OpenReview](https://openreview.net/forum?id=iknO3Ikkxc) |
| 24 | Do LLMs Know Whom to Trust? Brand Names vs. Stated Reliability in LLM Deference to AI Peers |  | [OpenReview](https://openreview.net/forum?id=A8ovrVRVnl) |
| 25 | EJT: Embedded Jailbreak Templates for Scalable and Category-Balanced Safety Benchmark Construction |  | [OpenReview](https://openreview.net/forum?id=eIWmyxu7GA) |
| 26 | LLM Authorship Verification: Are Two Texts Generated by the Same Large Language Model? |  | [OpenReview](https://openreview.net/forum?id=KuTZLS6V2w) |
| 27 | SPADE: Soft Prompts for Ai-text DEtection |  | [OpenReview](https://openreview.net/forum?id=KACwy3Fqio) |
| 28 | CertMem: Certifiable Memory Promotion in Agentic Systems |  | [OpenReview](https://openreview.net/forum?id=1lLyUbVd0b) |
| 29 | Empty Commitments: When Agents Promise What Their Runtime Cannot Deliver |  | [OpenReview](https://openreview.net/forum?id=AFOTqKu7DT) |
| 30 | Auditing LLM Evaluation Code: Controlled Faults and a Real-World Repair Study |  | [OpenReview](https://openreview.net/forum?id=Fas1TKtsJj) |
| 31 | Tokengeist: Multi-Turn Attribution Tracing in Agentic Conversations |  | [OpenReview](https://openreview.net/forum?id=bcNzuKgTkw) |
| 32 | When the Cache Says No: Refusal Behavior in Low-Resource Cache-to-Cache Communication |  | [OpenReview](https://openreview.net/forum?id=tzpsnHnSSk) |
| 33 | Do Hallucination Detectors Transfer Across Tasks? A Study of Internal Activations from QA to Code and Math |  | [OpenReview](https://openreview.net/forum?id=KH5r4SD5zw) |
| 34 | SemField: A Simple, Linear, Continuous, yet Robust Semantic Watermark |  | [OpenReview](https://openreview.net/forum?id=LaairDJIdJ) |
| 35 | Structure-Guided Visual Perturbation Neutralization for LVLMs | SIGN：结构引导的 LVLM 视觉扰动中和——先验结构提取保跨模态对齐+动态引导中和轻量即插即用，优于为传统 CV 设计的防御 | [OpenReview](https://openreview.net/forum?id=tb5CLTvPnR) |
| 36 | VEILED-SH: Vulnerability Expression through Indirect Language Evaluation Dataset (Self-Harm) | 间接/文化情境化自伤与痛苦表达评测基准（1 万提示×四应用场景×专家校准多参考政策）——AI 系统漏检间接求救信号 | [OpenReview](https://openreview.net/forum?id=SY4mDquR1z) |
| 37 | When Cooperation Meets the Law: MA-LexArena for Evaluating Legal Compliance | MA-LexArena：多 agent 协作行为的法律合规基准（1026 任务×31 规则卡×8 个欧盟法律工具）——对等协作确认违规率高于监督-工人范式 | [OpenReview](https://openreview.net/forum?id=PY7UY1OSdq) |
| 38 | RegDetect: Short Machine-Generated Text Detection via Regeneration Drift Modeling | RegDetect：再生成漂移建模检测短机生成文本——机器文本重生成贴合机器、人类文本漂移大，30-50 词段优势显著 | [OpenReview](https://openreview.net/forum?id=qAbS9mHPyM) |
| 39 | When Multimodal Agent Teams Fail: Root-Cause Attribution Across Agents and Steps | MMTraceBench+MMTracer：多模态多 agent 系统的失败根因归因（双向反事实标注管线+RL 定位模型）——早错跨 agent 与模态传播 | [OpenReview](https://openreview.net/forum?id=X2aoltyQxj) |
| 40 | Outcome-Grounded Auditing of RLVR Training Warnings | 结果接地的 RLVR 训练预警审计：熵监控候选在冻结联合门下无一及时预警——可复现退化不等于可部署前兆 | [OpenReview](https://openreview.net/forum?id=BAgIfZYEX6) |
| 41 | Evaluating LLM Safety across Korean Addressee Honorification | 韩语敬语四级变化下的安全一致性（400 HarmBench→1600 变体×13 模型）——自然社会语用变化即可测得安全行为改变 | [OpenReview](https://openreview.net/forum?id=s9A7n7Mllv) |
| 42 | Can Large Multimodal Models Actively Recognize Faulty Inputs? A Systematic Evaluation Framework of Their Input Scrutiny Ability | ISEval：LMM 输入审视能力评测（1945 题×九种缺陷构造）——自发性缺陷检出仅 5.5-33% 且识别缺陷≠扣留无据答案（最高检出配置 99.9% 仍给无据答案） | [OpenReview](https://openreview.net/forum?id=42UqS0buR4) |
| 43 | Do Unequal Review Paths Reveal Bias? Interface-Calibrated Auditing of Tool-Calling Loan Agents | TraceFair：工具调用贷款 agent 的界面校准公平审计——匹配财务记录下人口线索改变决策时可用证据的暴露（证据获取成为人口敏感性的新位点） | [OpenReview](https://openreview.net/forum?id=AjHkmYKQOK) |
| 44 | Vuligence: Progressive Disclosure Multi-Agent Framework for Project-Level Vulnerability Detection via Dynamic Validation | Vuligence：渐进披露多 agent 项目级漏洞检测+Docker 动态验证——Java F1 0.177→0.772 并发现 23 个零日（AI-for-cyber） | [OpenReview](https://openreview.net/forum?id=TfSx4O2yhS) |
| 45 | Harm-Aware Multi-Action Routing for Selective RAG Repair | RAG 修复的损害感知两段路由：保答案与选修复分离——选择性干预优于统一修复（RAG 修复决策的安全侧） | [OpenReview](https://openreview.net/forum?id=51aA72y1z5) |
| 46 | Given the Evidence: Interpretation in LLM Safety Review | 安全审查中证据的访问≠正确使用：审查者忽略显式矛盾或识别无据仍批准——任务对齐小专家可与大模型竞争、推理大幅改善（护栏的证据解读缺口） | [OpenReview](https://openreview.net/forum?id=orFUT40WfI) |
| 47 | Wrong Answer or Refusal? How LLMs Respond as Supporting Evidence Is Removed | 证据撤离轨迹 EWT：逐句删证据下模型选择答错还是拒答——答案证据首删即失正确；禁止拒答使最终错误 +22.5pp（弃答行为的能力边界） | [OpenReview](https://openreview.net/forum?id=6yztN68P2u) |
| 48 | Can Compressed Memory Change Its Mind? The Anticipation Trap in LLM Agent Memory | 压缩记忆的预期陷阱：按更新后准确率选记忆反而降联合准确率（选中的已含更新后答案）——条件式记录而非结论式提升联合正确率 | [OpenReview](https://openreview.net/forum?id=v8PZNhMUc3) |
| 49 | BLOOM-WILT: Logit Tilting for Behaviour Elicitation in Automated LLM Auditing | BLOOM-WILT：logit 倾斜的自动化审计行为引出管线——32 设置中 30 个超基线，自伤鼓励出现率 51%→100%（罕见行为的高效审计） | [OpenReview](https://openreview.net/forum?id=906Z85Hh5T) |
| 50 | Persistence Without Discounting: Localizing and Steering Rumination-like Dynamics in Patient-Simulating Language Models | 抑郁症患者模拟 LLM 的反刍动态：对比对话+激活修补定位注意力头/MLP——机制引导转向并不优于提示基线（可解释性到控制的落差） | [OpenReview](https://openreview.net/forum?id=4TPrliWGLx) |
| 51 | FirstCause: Failure-Lifecycle Supervision for Decisive-Step Attribution in Multi-Agent Systems | FirstCause：失败生命周期归因（断裂/源头/持续三因子分解）——Who&When 步精确 45.11%、相对最强基线 +22.06% | [OpenReview](https://openreview.net/forum?id=XsKHBITA98) |
| 52 | What the Judge Misses: Auditing Trajectory-Level Hallucinations\in Multi-Agent Industrial Workflows | TRAJEL：轨迹级幻觉人标基准——专责判官二分类 F1 0.855 却只恢复 4/21 逻辑型与 3/17 指涉型幻觉；66% 幻觉轨迹最终任务无幻觉（输出级评测读不到发生步） | [OpenReview](https://openreview.net/forum?id=edPZshDEye) |
| 53 | Claim Framing as a Driver of LLM Sycophancy | 声明框架驱动谄媚：42K 可验证问题×21 种框架——置信度/归属者/用户-模型共享最触发；专业权威与社会压力在事实场景几乎无效（谄媚评测的框架维度） | [OpenReview](https://openreview.net/forum?id=Ge83fxwJxH) |
| 54 | HSM-Unlearn: LLM Structural Unlearning for Hardware IP Protection | HSM-Unlearn：RTL 感知分层结构掩蔽遗忘——把 SOTA 的 5.43× 快速重学压回 1.10×（硬件 IP 遗忘的再学习审计口径） | [OpenReview](https://openreview.net/forum?id=uoCjgHx9V7) |
| 55 | SafeGround: Know When to Trust GUI Grounding Models via Uncertainty Calibration | SafeGround：GUI 定位模型的空间分散不确定性+校准阈值选择预测——高不确定 abstain/级联，接受错误率有界（GUI agent 可靠性） | [OpenReview](https://openreview.net/forum?id=SG12Ufn8In) |
| 56 | Slice-Level Gaps in Multilingual AI Safety Datasets | 多语安全数据集切片级审计（豪萨/斯瓦/法语 25 切片×31 字段）——覆盖数字隐藏语言级缺口：无原生自伤/性内容数据、切片级一致性仅 6/25 报告 | [OpenReview](https://openreview.net/forum?id=jTh2AHNUPH) |
| 57 | Locate-then-Debias: Understanding and Mitigating Model Bias in Hidden Representations Explanation of Large Language Models | Patchscopes 解释的忠实性偏置：LDLoR 以未修补 logit 为偏置对照重校准——抑制语言模式放大上下文信息（可解释性忠实性修正） | [OpenReview](https://openreview.net/forum?id=N5aPqzhr6T) |
| 58 | Ripple: A Unified Framework for Watermarking Diffusion Large Language Models | Ripple：扩散语言模型统一水印框架——掩码→稳定态转移时全局哈希注入+EMA 校准弱信号 token，检出/鲁棒/质量三衡 | [OpenReview](https://openreview.net/forum?id=DA4JlRWRoY) |
| 59 | SafeSceneReason: A Multimodal Reasoning Benchmark Connecting Industrial Hazards with Accident Knowledge | SafeSceneReason：工业危险多模态推理基准（11 万场景中心+1.3 万报告中心 QA）——连接事故调查知识的合规评估与因果分析 | [OpenReview](https://openreview.net/forum?id=RXhBrvz78P) |
| 60 | SchemaDrift-Mem: Measuring First-Decision Procedural Rot in Tool-Using Language Agents | SchemaDrift-Mem：工具契约变更后的首决策程序腐烂——无版本 BREAKING 复用无效调用率 0.833，语义元数据门可挡 SUSPICIOUS 暴露 | [OpenReview](https://openreview.net/forum?id=icY11nkbaS) |
| 61 | Agentic Depositions: Benchmarking Adversarial Conversations | Agentic Depositions：法庭质证对抗会话基准——策略提议/证人排序/实时应答，前沿开源与闭源性能相当 | [OpenReview](https://openreview.net/forum?id=uy3Gs5NgPq) |
| 62 | Protecting Automatic Speech Recognition Datasets via Watermarking | HPW：ASR 数据集无害水印——声学扰动制造干净/侵权模型可读性差，黑盒验证未授权训练（数据集版权保护） | [OpenReview](https://openreview.net/forum?id=uAwHXXt1Pb) |
| 63 | From Fluent to Verifiable: Claim-Level Auditability for Deep Research Agents | 深研 agent 的声明级可审计性框架（AAR 类型化溯源）：引用丰富的报告仍难以审计——溯源覆盖/健全/矛盾透明/审计努力四测度 | [OpenReview](https://openreview.net/forum?id=LrDPakULQG) |
| 64 | Consistency-Aware Editing for Entity-Level Unlearning in Large Language Models | CAE 一致性感知编辑的实体级遗忘：聚合关系属性与对抗改写的实体中心提示+一致性正则的低秩更新——连贯遗忘且抗对抗查询 | [OpenReview](https://openreview.net/forum?id=sbvnRJCHI3) |
| 65 | EventTrace: Event-Based Probability Trajectory Modeling for Training-Free LLM Text Detection | EventTrace：token 概率轨迹的结构化概率事件训练无关检测——保持概率转移与预测不确定性对应，黑盒白盒基准 SOTA | [OpenReview](https://openreview.net/forum?id=2ruqWuJbkC) |
| 66 | A Benchmark and Diagnostic Study of  Epistemic Admission in Shared Agent Memory | 共享 agent 记忆的认识准入基准（CPB）：去重策略错杀真断言、覆盖保持策略近无限制采纳假断言——消费者对无争议假记忆断言率 0.97-0.99 | [OpenReview](https://openreview.net/forum?id=8rG6cPYEWP) |
| 67 | A Survey on the Self-Evolution of Large Language Models: From Self-Improvement to Recursive Self-Improvement | LLM 自进化综述（提示程序/数据/记忆/权重/环境/评测/群智/系统级 RSI 八域）——模型塌缩/reward hacking/数据投毒/目标漂移/失控递归的风险与对策横切分析 | [OpenReview](https://openreview.net/forum?id=tykR0clBMa) |
| 68 | Beyond Fabricated References: Analyzing and Probing Field-Level Citation hallucinations in LLMs | 字段级引用幻觉：24-51% 生成引用指向真实论文但作者/DOI 常错；字段正确性线性可读于隐状态且错误信号嵌入生成文本本身 | [OpenReview](https://openreview.net/forum?id=SmmIjN7LQk) |
| 69 | Analyzing LLM Data Contamination from an Ensemble Perspective | 集成视角的污染检测：单模型置信混淆真知识与记忆——预测置信与集成不确定性互补，UBD 免干净参照按样本去污染 | [OpenReview](https://openreview.net/forum?id=2OS7rGWS5W) |
| 70 | Quantization and Bias in Reasoning LLMs for Hate Speech Detection | 量化对推理 LLM 仇恨言论检测的群体公平影响——更常恶化而非改善、小模型更明显；伊斯兰群体差异与推理轨迹/激活变化相关 | [OpenReview](https://openreview.net/forum?id=lDafR8cvXa) |
| 71 | KG-TOFU: Acquisition-Controlled Unlearning Evaluation with Knowledge-Graph Probes | KG-TOFU：作者画像重建为溯源知识图谱，同 KG 生成目标模型训练数据与评测探针——习得方式剧变遗忘结局（QA 对遗忘评测的泛化性质疑） | [OpenReview](https://openreview.net/forum?id=ol7EX9HzRG) |
| 72 | Sycophancy Introspection: Teaching Language Models to Detect and Resist Sycophancy | 谄媚内省 SFT：教模型识别自己正在谄媚并以此引导最终响应——降谄媚同时保持对正确反馈的响应性 | [OpenReview](https://openreview.net/forum?id=Fg9MKIcdwU) |
| 73 | Alignment Makes Language Models Normative, Not Descriptive | 120 对基座-对齐模型×万级真实多人博弈决策：基座在多轮策略场景预测人类行为更强（90.6% 对比占优）——对齐诱导规范性偏置 | [OpenReview](https://openreview.net/forum?id=Zr6dGUDyYn) |
| 74 | PrefixProbe: Prefix-Supervised Probing for LLM-Generated Text Detection | PrefixProbe：句前缀监督的冻结观察者探针——截断后仍可检出，DetectRL 99.90% AUROC、8 训练对 89.62% TPR | [OpenReview](https://openreview.net/forum?id=TV7GUUTFWl) |
| 75 | Trustworthy Multimodal LLMs for Computational Social Science: A Survey of Risks, Validity, and Evaluation | 计算社会科学中 MLLM 的可信度风险综述（54 研究）——真实性/鲁棒受关注多于公平/隐私/安全与长期反馈效应 | [OpenReview](https://openreview.net/forum?id=I9g1G0Dsce) |
| 76 | Stochastic CHAOS: Benchmark Scores Are Policy-Indexed Measurements | 基准分数是策略索引测量：规则/预算/访问三分离后多数投票增益大缩水——16 抽中有害输出几率约为贪心 3 倍（评测口径的采样依赖） | [OpenReview](https://openreview.net/forum?id=GfMStKLSV4) |
| 77 | To Follow or Not To Follow: Investigating the Tendency of Language Models to Follow Non-factual Contexts | DissonanceQA：非事实上下文跟随倾向（14952 实例地理/分类/时间冲突）——时间事实最易被带偏、地理最不易 | [OpenReview](https://openreview.net/forum?id=voAfPJAxvU) |
| 78 | When Correct Answers Collapse: Measuring LLM Robustness Under Conversational Pressure | 对话压力下的正确答案坍塌：裸反驳即可让某配置 85.4% 放弃正确 StrategyQA 答案——易感问题占比 19.2-98.4% 随配置 | [OpenReview](https://openreview.net/forum?id=NzTPCx3nEW) |
| 79 | MultiPoC-Bench: Evaluating Code Agents on Joint Vulnerability Repair | MultiPoC-Bench：多 PoC 联合修复基准（120 任务 389 PoC）——修一漏一与功能保持的差距 4.17-17.50pp | [OpenReview](https://openreview.net/forum?id=eDxcFxN7KI) |
| 80 | VulContextBench: A Benchmark for Security Context Retrieval in Coding Agents | VulContextBench：编码 agent 的安全上下文检索基准——每模型浏览 73-86% 金标上下文但最终引用仅 12.9-36%（浏览 vs 选为证据的差距） | [OpenReview](https://openreview.net/forum?id=BAM57rvl9p) |
| 81 | GenFakeNewsNet: A Benchmark for Intent-Driven Fake News Generation | GenFakeNewsNet：意图驱动的假新闻生成基准（17,395 对）——按真实宣传意图的协同叙事操纵，54% 读者判为真 | [OpenReview](https://openreview.net/forum?id=qVoKyLOY1i) |
| 82 | Moral Sycophancy in LLMs: Studying the Effects of Response Formats with a Taxonomy of Stance Shifts | 道德谄媚的响应格式效应：强制选择最高/二元背书最低——五类立场转移分类学，同谄媚率模型行为不同 | [OpenReview](https://openreview.net/forum?id=tGceBlcEFn) |
| 83 | AnyWarehouse: Auditable Evaluation of History-Constrained Language-Model Agents | AnyWarehouse：到达物理终点≠满足有效完成历史——终点投影错误接受 33 个非法轨迹，账本反馈提升合规成功 7.4pp（可审计 agent 评测） | [OpenReview](https://openreview.net/forum?id=3YuWZwwjWd) |
| 84 | Inherited Attention Heads, Fragile Instructions: Understanding Order Effects in Audio Language Models | 音频 LLM 指令顺序效应：指令在音频后合规率 0→0.40——约 20 个注意力头读指令且跨模型共享（p<10⁻¹⁸），阻断/增强可双向调节 | [OpenReview](https://openreview.net/forum?id=4ZCcRwtnjc) |
| 85 | Beyond Final-Layer Logits: Training-Free AI-Generated Text Detection via Hidden-State Trajectory Contrast | 隐状态轨迹对比 HTC：训练无关 AIGT 检测从冻结代理直接导出判别梯度方向——0.9343 AUROC、超最强基线 10+ 点 | [OpenReview](https://openreview.net/forum?id=ZafGosXH5G) |
| 86 | Wait, am I Being Fair? Characterizing Deductive Stereotyping and Mitigating It with Fair-GCG | 演绎刻板化：把群体统计规律套到个体——Fair-GCG 系统发现推理时注入短语，跨规模泛化并迁移到真实公平敏感任务 | [OpenReview](https://openreview.net/forum?id=zBcn88tjmx) |
| 87 | ADMIT: Not Every Bias Warrants Mitigation in Text-to-Image Models | ADMIT：T2I 并非所有分布失衡都该修——文献化诊断分类学指导选择性缓解，保非目标视觉内容 | [OpenReview](https://openreview.net/forum?id=b7apkEnFev) |
| 88 | Beyond Four Seconds: Temporal Context and Variety-Conditioned Acoustic Patterns in Arabic Speech Deepfake Detection | 阿拉伯语语音深伪检测的语言变体×时间上下文交互：37 声学特征中 35 个显著交互——4s→16s EER 25.83%→23.38% | [OpenReview](https://openreview.net/forum?id=ztIAhf2eDA) |
| 89 | Evaluation Awareness Beyond English: Do LLMs Act Differently When Tested in Indic Languages? | 评测觉察的印度语言扩展：告知被测试时印地语系拒答率升 14.4pp——安全评测可能不反映日常用户待遇（47,880 响应公开） | [OpenReview](https://openreview.net/forum?id=HcCYQPraIK) |
| 90 | PAIR-SAFE: A Paired-Agent Approach for Runtime Auditing and Refining AI-Mediated Mental Health Support | PAIR-SAFE：MITI-4 临床接地的判官 agent 运行时审计精炼 AI 心理支持——允许/修订决策实时改进关系质量 | [OpenReview](https://openreview.net/forum?id=5Q8kBFOCsi) |
| 91 | Preserving Structure, Strengthening Signals: A Grammar-Driven Approach to Optimize the Trade-off Between Quality and Detectability in Code Watermarking | 语法驱动代码水印 GDW：绿表/语法有效/结构角色三级掩码+AUTC 权衡指标——低熵代码的质量-可检性新最优 | [OpenReview](https://openreview.net/forum?id=Dk2KWUmYwz) |
| 92 | Words, Actions, and Beliefs: Tracing Persuasion in LLM Agent Networks | LLM agent 网络中的说服追踪：竞争说服者把移动变为绕模型先验的振荡；仅 73% 计划原则到达消息且被劝者复述措辞而不陈述信念转移——轨迹-暴露级评测主张 | [OpenReview](https://openreview.net/forum?id=ReqnJEYwBR) |
| 93 | Predicting Hallucinations Before, During, and After Generation with Sparse Autoencoder Features | PreSAGE：SAE 特征在生成前/中/后预测幻觉（四 LLM×六数据集）——注意力池化+门控特征选择的端到端检测器，生成前干预（弃答/检索/路由）成为可能 | [OpenReview](https://openreview.net/forum?id=ABSxxSQ7NQ) |
| 94 | When Large Language Model Judges Meet Watermarks: Provenance Signals Distort Automated Evaluation | LLM 判官遇水印：20 个跨模型生成-判官对中水印候选选择率平均低 11.1pp——'不可感知'对机器判官不成立（水印×自动评测交互） | [OpenReview](https://openreview.net/forum?id=2kul0IW1wv) |
| 95 | The Little Models That Think: A Review of Small Language Model Reasoning Under Deployment and Security Constraints | 小模型推理×部署-安全约束综述：4bit 量化保推理但安全影响未定、蒸馏降安全、干净轨迹可藏错答——成本-风险画像与部署-安全交互图 | [OpenReview](https://openreview.net/forum?id=rbcgFkBtGe) |
| 96 | VIGILIA: Interactive Evaluation of Robust Conversational Vigilance in Large Language Model Agents | VIGILIA：共享会话环境的对话警觉性压力测试（模拟课堂植入受控事实错误）——警觉失败率至 70.1% 且对刻板社会群体语言特征敏感 | [OpenReview](https://openreview.net/forum?id=dGBA8ZqQ87) |
| 97 | ECHO: Revealing Review-to-Submission Linkage in Anonymous Peer Review | ECHO：匿名评审到本人投稿的链接攻击（技术专长+文风跨评审/论文/反驳信号）——Top-1 34.6%、加强重排 56.4%，评审匿名集被常规发布工件大幅收缩 | [OpenReview](https://openreview.net/forum?id=gqIIOUbhEG) |
| 98 | SecReason: Vulnerability Detection and In-Stream Self-Repair for LLM Code Generation | SecReason：流内安全自修复——在交付前推理窗口增量扫描+规则触发中断插警继续解码，CWEval/SecCodeBench 安全且正确 72.8-98.1% | [OpenReview](https://openreview.net/forum?id=aMLgYnsGBk) |
| 99 | SCOPE: Service-Conditioned OOD Probing and Evaluation for Large Language Models | SCOPE：服务条件化 OOD 探测与评测——OOD 请求反映服务范围而非模型能力，e-process 序贯审计拒绝门与人类定义边界的对齐 | [OpenReview](https://openreview.net/forum?id=Yk4rw2jOz5) |
| 100 | LegalRPA: A Benchmark and Auditable Framework for Role-Preserving Legal Anonymization | LegalRPA：保角色法律匿名化基准+可审计框架——隐私覆盖/角色区分/结构保真/QA 效用/条件链接风险的五维权衡 | [OpenReview](https://openreview.net/forum?id=bUvYAYu4Wf) |
| 101 | Automated Schema-Preserving Attacks for Evaluating LLM Arithmetic Reasoning | 模式保持攻击自动评测算术推理：五族变换（数值重映射/词汇改写/干扰项/问句反转/合并）——全部模型在保持结构的变换版上显著退化 | [OpenReview](https://openreview.net/forum?id=07EOxLBDYo) |
| 102 | Where Green Meets Candidate: Probability-Calibrated Watermarking for Large Language Models | PCW 概率校准候选约束水印：绿表偏置只施加于核采样候选交集的高概率 token——生成与检测在候选约束解码下对齐 | [OpenReview](https://openreview.net/forum?id=XZKhLXqJ7R) |
| 103 | Demystifying the Privacy-Utility Trade-off in LLM Interactions | LLM 交互隐私-效用权衡三机制解构（上下文依赖效用/策略适配/组合交织）+意图驱动局部保护 Veilmind-4B——低泄漏点保高响应效用 | [OpenReview](https://openreview.net/forum?id=LQzRGfU36R) |
| 104 | Illusion: Safeguarding Topology Confidentiality in LLM Multi-Agent Systems via Behavior-Preserving Obfuscation | Illusion：MAS 通信拓扑保密的主动混淆——注假边假消息保输出分布等价，边级 F1 0.87→0.62 且抗相似度与 LLM 判官过滤 | [OpenReview](https://openreview.net/forum?id=gepqlfyFF6) |
| 105 | A Trust Layer for Agent Evaluation | agent 评测信任层：四属性（评分逻辑支持/可追溯计算赢得/完成声明属实/重复执行稳定）——108 任务上仅 22.6% 通过全检（可信 agent 评测基础设施） | [OpenReview](https://openreview.net/forum?id=R3qPhU9XkE) |
| 106 | NumTrace: Auditing the Number Provenance of Financial Analyst Agents | NumTrace：金融分析 agent 数值声明的溯源审计（数值对但实体/概念/期间/单位/范围错）——540 问×2163 SEC 文档三判定（值/绑定/支持） | [OpenReview](https://openreview.net/forum?id=234HaarcMQ) |
| 107 | When the Simulated Patient Knows Too Much: Privileged-Information Leakage in RL for Doctor Agents | 模拟病人特权信息泄漏：RL 学会直接问答案（1.7B 模拟 99% vs 无泄漏代理 39%）+特权通道悲观主义 PCP 消除多数膨胀 | [OpenReview](https://openreview.net/forum?id=UmYg9PJUiP) |
| 108 | The Patient Is Always Right? Evaluating Sycophancy in Medical Diagnosis with Graded Patient Beliefs | 分级患者信念下的医疗谄媚：模型平均 23.2% 采纳患者错误信念、虚构疾病人设达 43.0%——含虚构病症也被接受 | [OpenReview](https://openreview.net/forum?id=9cSuCtouAk) |
| 109 | Can an Agent Learn to Predict Its Own Failure? Outcome-Grounded Confidence Calibration in LLM Agents | agent 自我失败预测：GRPO 组 rollout 供成功标签+proper scoring rule 对每步置信度对最终结局校准——离线 AUROC 至 0.85、ECE 0.42→<0.12 | [OpenReview](https://openreview.net/forum?id=RVZpUXbCqL) |
| 110 | Defined by Him: Definitional Othering in Aligned Language Models Is Invisible to Toxicity and Safety Classifiers | 定义性他者化：GPT 系女性指向补全以男性为比较基准的比例升至 82.8% 且主要发生在 RLHF 步——毒性/安全分类器几乎不标记该内容（分类器不可见的表征伤害） | [OpenReview](https://openreview.net/forum?id=T3qHRmClND) |
| 111 | Disentangling Neural Identity from Encoder Identity in a Privacy Audit of BP-GPT’s fMRI-to-Text Decoding | BP-GPT fMRI-文本解码隐私审计：原始连接与嵌入均 100% 识别参与者，但按参与者训练编码器——模型自身签名饱和于首线性层，跨种子可迁移身份信号仅 54.3%（数据指纹 vs 编码器指纹的分离） | [OpenReview](https://openreview.net/forum?id=kj2WsHmNCK) |
| 112 | The Intent Gap: A Taxonomy of Real-User Failure Modes in Frontier AI Agents | 真实用户失败模式分类学（意图鸿沟）：字面合规但错失用户真实意图——WildChat 5 万对话试点+11 类失败分类学 | [OpenReview](https://openreview.net/forum?id=2G0fzSmOWw) |
| 113 | What Carries Forward? Pretraining Disclosure Across Language Model Releases | 预训练披露跨版本审计（41 模型 17 家族×24 指标）：后续发布不保持既有披露——同分可藏三得三失，语料构成与训练算力缺口持续 | [OpenReview](https://openreview.net/forum?id=2v5Sucl7g0) |
| 114 | Represented but Not Used: Value–Policy Dissociation in LLM Agents | 价值-策略解离：候选动作相对价值线性可解码于隐状态（含策略偏好更差动作处）——表示了后果却未使用，机制可解释性定位多步决策失败 | [OpenReview](https://openreview.net/forum?id=c1clBZHXO9) |
| 115 | Private Retrieval Augmented Generation via Random Projection | 随机投影保 RAG 数据库隐私：同投影作用库与查询嵌入保语义相似——经验隐私相当且性能优于形式 DP 基线 | [OpenReview](https://openreview.net/forum?id=VQRlqYgSas) |
| 116 | When Should Medical VLMs Answer? Reliability under Deployment Perturbations | 医疗 VLM 部署扰动下的选择性预测：隐状态探针 193/195 设置超置信度+损坏路由/条件转向实现澄清与弃答——检错与恰当响应间仍有沟 | [OpenReview](https://openreview.net/forum?id=HxHswTFXKl) |
| 117 | What Coding Agents Leave Unsaid: Measuring Task-State Gaps Between Execution and Reports | CTXGAP：编码 agent 报告 vs 完整执行上下文的任务态可恢复性差距 40.7pp——监督者无从得知未报告的失败与风险 | [OpenReview](https://openreview.net/forum?id=vDmn2jKpKF) |
| 118 | Towards Fair Evaluation under Benchmark Contamination via Unlearning and Relearning | 遗忘-重学习协议治基准污染：矛盾式遗忘削弱基准答案记忆后官方训练集重训——重学分数去除污染优势且近干净控制水平 | [OpenReview](https://openreview.net/forum?id=bnWvCHtfdr) |
| 119 | Emergent Misalignment Due to Value Training | 价值观训练的涌现失准：Hofstede 维度微调在未训练价值观/风险偏好/社会认知/安全特质上产生意外副作用——价值对齐需更广行为评测 | [OpenReview](https://openreview.net/forum?id=JJ7Wb4qvr1) |
| 120 | ResyncMark: Robust Multi-Bit Text Watermarking via Proportional Resynchronization | ResyncMark：比例重同步的多比特文本水印——30% 随机删除后比特准确率 60.2%→98.3%，无需模型权重或原续写 | [OpenReview](https://openreview.net/forum?id=leiH1xTtFm) |
| 121 | Can Agentic Code Review Catch Vulnerabilities Before They Are Merged? | SecPRBench：真实 bug 引入 commit 的 agent 安全评审基准（265 任务×九关键系统）——召回 32.5-78.1%，68% 漏检是'看到文件却论证成别的机制' | [OpenReview](https://openreview.net/forum?id=ptaHLP7CrH) |
| 122 | SAPR: Static Filtering and Proxy Re-ranking for Target-Specific Anchor Selection in Large Language Model Unlearning | SAPR：知识编辑遗忘的目标特定锚选择（静态过滤+代理重排）——ROCR 上 Level-1 ROUGE 降 18.8% 且限损邻接知识 | [OpenReview](https://openreview.net/forum?id=8V1IHkdB0b) |
| 123 | LatentRisk-VLM: Failure-Guided Representation Editing for Frozen Vision-Language Models | LatentRisk-VLM：仅用任务标签与冻结模型边际发现类条件潜在风险方向并编辑——Waterbirds 最差组 +26.9pp 但 CelebA 反降（失败-组对齐决定成败） | [OpenReview](https://openreview.net/forum?id=zT3tc3oGF9) |
| 124 | RealGUINoise: An Interactive Cross-Platform Benchmark for GUI Agent Robustness under Real-World Interface Noise | RealGUINoise：42 类真实界面噪声×7 agent 框架的交互跨平台基准——噪声不只降性能还重定向轨迹并增加不安全行为倾向 | [OpenReview](https://openreview.net/forum?id=uB6cE7AzQ6) |
| 125 | Pair, Freeze, Correct: Auditing Model Updates with Few Reference Labels | 配对-冻结-校正的模型更新审计：按代理判定变化分层配对标注+历史审计标签风险上限加权——等预算 RMSE 降 43.8% | [OpenReview](https://openreview.net/forum?id=t5Mpf9m52N) |
| 126 | Revocation-Consistent Agent Execution via Requirement-Scoped Support and Selective Discharge | 需求范围化的撤销一致性：混合支持工件的原子授权决定陷入健全-保持两难——RCSF-V 溯源支持流+权威纪元+选择性放电，0% 未授权执行且 0% 不必要阻断 | [OpenReview](https://openreview.net/forum?id=i1T36lx4cJ) |
| 127 | Black-Box Forensics for Conversational LLM Agents | 对话式 LLM agent 黑盒取证：风格+n-gram 分类器几句对话识别基模型 98%；跨编码器指纹判定两会话同 agent（单对 AUC 0.79、50 会话 0.97）且抗改写——诈骗部署与换模检测应用 | [OpenReview](https://openreview.net/forum?id=J0Io3TtVSz) |
| 128 | Can LLMs Stay Robust in Noisy Agentic Environments? | 噪声 agent 环境鲁棒性：扰动目标×类型二维框架——agent 少识别被改输入、无验证传播损坏信息且受扰成功轨迹算力大增 | [OpenReview](https://openreview.net/forum?id=DhjwVjDCBn) |
| 129 | Emergent Controllability: Benign Reasoning Distillation Can Increase Chain-of-Thought Controllability | 良性推理蒸馏可提升 CoT 可控性：无关 SWE 任务 212 例后指令遵循/CoT-Control 上升且跨供体-受体迁移——推理训练的意外可控性外溢 | [OpenReview](https://openreview.net/forum?id=0SZ1uolv2C) |
| 130 | HAFT: Adversarial Robustness Benchmarking and Budget-Aware Adaptive Auditing Framework for Hindi Automated Fact-Checking | HAFT：印地语自动事实核查对抗鲁棒基准（1120 声明×22 攻击 24640 评测）——证据攻击 41-47.7% 无条件成功、预算感知混合审计 | [OpenReview](https://openreview.net/forum?id=zLsl9Q3U6e) |
| 131 | AgentStealth: On-Device Text Anonymization with Locally Deployable Small Language Models | AgentStealth：强 LLM 仅在训练期暴露隐私泄漏模式并生成监督、蒸馏进本地 SLM 独立完成匿名化——避免云端改写的二次泄漏 | [OpenReview](https://openreview.net/forum?id=UBjHznZAmo) |
| 132 | ImpliCue: A Benchmark for Implicit Personal Attribute Inference from Conversational Cues | ImpliCue：会话线索的隐式个人属性推断基准（1036 合成对话×18 属性，STRONG/WEAK/NO_EVIDENCE 证据分级）——区分正确预测与有据推断 | [OpenReview](https://openreview.net/forum?id=8dwdn1k8R4) |
| 133 | OARS: Objective-Aware Retain-Set Selection for LLM Unlearning | OARS：现实遗忘请求常只给遗忘集——隐状态位移聚类+簇内最高位移选择的保留集选取，恢复 65.9% 效用损失 | [OpenReview](https://openreview.net/forum?id=t8fX8FUeem) |
| 134 | The Trustworthiness Mirage: Auditing Financial LLM Trustworthiness Benchmarks | 金融 LLM 可信度基准审计（51 研究 226 任务）：57.6% 结论超出证据支持——声明-任务-指标-推断链系统性错配 | [OpenReview](https://openreview.net/forum?id=k2EOwXpSp7) |
| 135 | When Confidence Is Not Enough: Toward Consequence-Risk-Aware Abstention for Consumer-Facing Medical QA | 后果风险感知弃答 CIRA：正确性置信+后果代理估计+效用罚——按面板定义残余伤害而非单纯正确性评估弃答 | [OpenReview](https://openreview.net/forum?id=9O7TSwQtjd) |
| 136 | Does Safety-Score Asymmetry Depend on Prompt Values? | 安全分数不对称（SSA）的提示价值触发：36 维价值表示显著预测 SSA 变化——告知被审计即改变作答，评测公平性前提被打破 | [OpenReview](https://openreview.net/forum?id=2jRmkSm32e) |
| 137 | PakDecept: Benchmarking LLM Deception in Urdu | PakDecept：乌尔都语 LLM 欺骗基准（1197 巴基斯坦真实事件八域）——迭代诱导下四模型欺骗率均超 85%；语言效应方向不一 | [OpenReview](https://openreview.net/forum?id=ySoNkIGMqv) |
| 138 | New Model, Old Habits: Behavior Transfer under Model Swapping in Multi-Session LLM Agents | 多会话 agent 换模下的行为转移：接收者采纳生成历史的模型的推理/行动模式——DASH 方向与作者感知摘要保强抑弱转移 | [OpenReview](https://openreview.net/forum?id=SHEZC8SJf2) |
| 139 | Paraphrase Consensus Is Not Self-Consistency: Instruction Reliance and Robustness in VLA Policies | VLA 指令依赖：改写指令使 OpenVLA -38pp、提示集成不可恢复——错误指令探针量化策略对指令的依赖份额，释义微调 +2.0pp | [OpenReview](https://openreview.net/forum?id=V0c2A9G6Kr) |
| 140 | Auditing LLM Fine-Tuning on Imperfect-Information Game Logs | 扑克日志微调审计：声称的'轻量求解器'在精确可利用度下被常数策略与古典求解器前五迭代碾压——保留高分样本+拟合同分奖励的训练配方三层审计 | [OpenReview](https://openreview.net/forum?id=vMMu199b2N) |
| 141 | Can We Believe AI Peer Review? | AI 评审可信度：同条件重复评审分数波动、细粒度协议降方差但系统性移均值——修订增益强依赖评审者（14k AI 评审实证） | [OpenReview](https://openreview.net/forum?id=JmMZjBqRVY) |
| 142 | Learning to Judge by Learning to Damage: Human-Free Training of LLM Evaluators | 以学破坏训判官：小 Damager（GRPO 奖励=标准指标）按严重度语义降级参照输出作伪标签——免人工训练 2B 判官 7-10/11 数据集超人评相关 | [OpenReview](https://openreview.net/forum?id=QgIKeM9mvE) |
| 143 | Search-Calibrated Multiscale Localization of Watermarked Regions in Mixed Human-LLM Documents | 混合人-机文档的水印区域多尺度定位：重叠区间搜索+分辨率校正+人写文档校准——有限样本 I 类错误控制下的最高 IoU/F1 | [OpenReview](https://openreview.net/forum?id=eEKrDRqO76) |
| 144 | Agent Behavior Maps: Locating Agents by What They Would Do, Without Running Them | agent 行为图：共享参照轨迹上的中心化动作对数似然定位 agent（免环境 rollout）——距离按序追踪轨迹 KL、跨 100 LLM 支持性能预测 | [OpenReview](https://openreview.net/forum?id=K4oiVt0GuC) |
| 145 | Increasing Response Diversity in LLMs via On-Policy Unlearning | 在策遗忘提多样性：每轮从当前策略采样并把其设为遗忘目标逐步抑制高频响应——开放生成多样性与代码 pass@5/10 提升 | [OpenReview](https://openreview.net/forum?id=4PNAkRPhgh) |
| 146 | Auditing Demographic Sensitivity and Uncertainty in French LLM-Based Emergency Triage | 法语急诊分诊的人口敏感性与不确定性审计：性别×姓名来源受控——'地中海综合征'疼痛最小化未复现且含姓名本身即移输出 | [OpenReview](https://openreview.net/forum?id=bveH2sDG4g) |
| 147 | Is This Your Agent? Identity Watermarking  for Agent Systems in Dynamic Environments | DASMark：动态环境 agent 系统身份水印——动作保持嵌入学决策表达通道+移位鲁棒恢复，98.5% 位解码/攻击下 95.2% | [OpenReview](https://openreview.net/forum?id=0H38D7yGhu) |
| 148 | Evaluating Evidence Grounding Under User Pressure in Instruction-Tuned Language Models | 用户压力下的证据接地：国家气候评估受控认识冲突×18 模型——证据不能可靠防止用户对齐反转、研究空白描述反而增加易感性 | [OpenReview](https://openreview.net/forum?id=vqYEs9iW2G) |
| 149 | Residual Attribute Leakage Is an Interface: Auditing Privacy Evaluation After Text De-identification | 去标识文本的属性泄漏评测接口审计：判定随查询人/选项/先验/对手/评分规则而变——同一编辑器可在两种读法间从第一跳到第六 | [OpenReview](https://openreview.net/forum?id=z6gTt4p0Vd) |
| 150 | BenSyc: Evaluating LLM Judges of Social Sycophancy against a Full Human Census | BenSyc：对全量人口普查校准 LLM 判官的社会谄媚判定——裸提示判官 3-5 倍过标；'发帖者陈述不是证据'一条规则即近人类 | [OpenReview](https://openreview.net/forum?id=k2ipJPV3Ev) |
| 151 | Right Answer, Telltale Explanation: Harmless Ownership Verification for RAG Knowledge Bases | TellTale：RAG 知识库解释级无害所有权水印——同正确答案的证据解释选择编码信号，±短语配对检测 10/12 设置且抗过滤/改写/稀释 | [OpenReview](https://openreview.net/forum?id=cOrsoyXd19) |
| 152 | Policy Under Pressure: Social Context and Agentic Rule-Following | 运营者人设/同伴证言/工具形态对 agent 规则遵循的影响（26398 幕）：同一禁令写成代码违反率高 4.33 倍、同伴违规记录抬升违规（OR 2.12）——逐模型报告（上下文敏感的合规） | [OpenReview](https://openreview.net/forum?id=Fc01Adq3kf) |
| 153 | Self-Evolving Agents Can Repair Failures but Struggle to Generalize from Them | 冷启动纯失败进化：失败经验可修复已失败任务但难泛化到未见任务（修复-泛化鸿沟）——成功轨迹才是可迁移性的关键 | [OpenReview](https://openreview.net/forum?id=xmOODoyPCB) |
| 154 | LabGuard: Grounding Natural-Language Laboratory Rules into Runtime Guards for Embodied Laboratory Agents | LabGuard：实验室自然语言规则→类型化可执行表示→运行时监控编译——不安全事件 39.5%→23.8% 且干预率 <0.5%（具身实验室 agent 安全） | [OpenReview](https://openreview.net/forum?id=bQCF5uxsvV) |
| 155 | BEAD: Behavioral and Event-Aware Detection of Tool-Using Agent Hallucinations | BEAD：行为特征（20 维 LightGBM）+事件依赖（关系感知 Transformer 硬注意力掩码）双轨迹表示的有界工具任务幻觉回溯检测——免 LLM 判官的低成本高准 | [OpenReview](https://openreview.net/forum?id=cyFkVXtjUh) |
| 156 | DecisionRobust: Benchmarking Robustness for JEV Style Decision Models Across Text and Vision | DecisionRobust：JEV 类 typed 决策模型的跨文/视鲁棒基准——语义保持文本扰动/图像扰动/双模态提示注入×30 配置（含 24 留出模型） | [OpenReview](https://openreview.net/forum?id=rm4QV7zBA1) |
| 157 | Large Portions of Text in Speech Can Be Recovered from a Minimal Set of Prosodic Features | 仅 8 个韵律/音色特征即可恢复 39% WER 的原句文本（40% 句子 WER<25%、14% 完美）——最小韵律集的文本重建（语音隐私新面） | [OpenReview](https://openreview.net/forum?id=suGnJfMTlW) |
| 158 | Benchmarking LLM Robustness to Context Corruption in Long-Horizon Coding Tasks | 长程编码的上下文腐蚀基准：权威风格摘要腐蚀使 Qwen3-8B 掉 15.9pp——真实与腐蚀上下文建模为二元有效场的竞争分析 | [OpenReview](https://openreview.net/forum?id=vjo0JxpD5n) |
| 159 | From Sports to Safety: Benchmarking Proactive Risk Inference in MLLMs | SPRINT：体育视频主动性物理风险推断基准（2888 视频）——危险报告 97% vs 直接成因识别 42% 的鸿沟与显式危险查询的高假阳 | [OpenReview](https://openreview.net/forum?id=WiaFFaKwds) |
| 160 | Reading Right, Acting Wrong: Diagnosing Decision Failures of System One Models in Agent Loops | System One 模型 agent 环中的决策失败诊断：多数错误动作跟在正确读取之后且聚集于相同状态——事实全读仍不会组合，代码组合自身答案可修复 | [OpenReview](https://openreview.net/forum?id=4LUGpFl5De) |

## 核验记录

- 2026-10-14：经 OpenReview API（登录会话）分页抓取 `content.venueid=aclweb.org/ACL/ARR/2026/October/Submission` 全部 3,387 条，其中公开（readers 含 everyone）3,385 条；标题全量过目 + 候选摘要精读后收录 401 篇（含复查补录 25 篇）
- 2026-10-14（二次修订）：按用户新增兴趣分类 25/26 拆出「dLLM 安全」与「开源模型治理与权重级安全」两个独立分区，3 篇简表条目升为全卡
- 隐私说明：抓取仅访问公开匿名预印本字段（标题/摘要/关键词/论坛号），未触碰任何非公开评审数据
- 本文件为滚动评审中的工作快照，收录不代表对论文最终质量的判断
