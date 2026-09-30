# NeurIPS 2026: AI Safety Papers

## 目录

- [会议信息](#会议信息)
- [关键节点](#关键节点)
- [筛选说明](#筛选说明)
- [越狱、安全对齐与有害微调](#越狱安全对齐与有害微调)
- [CoT 监控、scheming 与 AI control](#cot-监控scheming-与-ai-control)
- [智能体安全与提示注入](#智能体安全与提示注入)
- [扩散语言模型安全（DLM 线）](#扩散语言模型安全dlm-线)
- [投毒、后门与供应链](#投毒后门与供应链)
- [隐私、成员推断与 unlearning](#隐私成员推断与-unlearning)
- [水印、溯源与内容真实性](#水印溯源与内容真实性)
- [内部表示干预与监控（安全 threat model 绑定）](#内部表示干预与监控安全-threat-model-绑定)
- [评测有效性与元层（精选）](#评测有效性与元层精选)
- [核验记录](#核验记录)

## 会议信息

| 项目 | 信息 |
| --- | --- |
| 会议全称 | Fortieth Conference on Neural Information Processing Systems (NeurIPS 2026) |
| 官方网站 | [NeurIPS 2026](https://neurips.cc/Conferences/2026) |
| 官方录用列表 | [Downloads（全量 event 导出，9,127 条）](https://neurips.cc/Downloads/2026) |
| 主 track 录用通知 | 2026-09-24 |
| 检查范围 | 主会 Posters/Tutorials/Workshops/Demos 全量列表的标题宽筛；数据截至 2026-09-30 |
| 辅助来源 | [hongsong-wang/NeurIPS2026 收集页](https://hongsong-wang.github.io/NeurIPS2026/)（7,900 篇 OpenReview/arXiv 链接与摘要，用于 arXiv 定位交叉与反向查漏） |
| 整理模式 | 官方列表已放出但无逐篇摘要/链接，采用**分类标题清单**（同 CCS Second Cycle 待核验模式）；arXiv 版陆续挂出后经日报管线收录建卡，venue 回填 `🏷 NeurIPS 2026` |

## 关键节点

| 节点 | 日期 | 官方来源 |
| --- | --- | --- |
| Notification | 2026-09-24 | 官方 Downloads 列表放出 |
| Conference | 2026-12（官方页面未给出精确日期，待核） | [NeurIPS 2026](https://neurips.cc/Conferences/2026) |

## 筛选说明

- 官方 event 总数：9,127（含 posters/tutorials/workshops/demos；含少量 workshop 条目混入主列表）
- 标题宽筛 AI 安全相关：约 300+
- 本文件收录：精选约 366 条，按八分类组织；**300 篇完整卡片**（arXiv 版 177 + OpenReview-only 123），66 条待 arXiv 挂出后补卡
- 收录口径：与 `RESEARCH_INTERESTS.md` P1 口径一致——模型层安全机制攻防、投毒与后门、guard/monitor/judge 有效性、LLM/Agent 栈规模化攻防实证、绑定安全 threat model 的内部表示干预、DLM 安全线；纯理论（DP/密码学/博弈论无 AI 安全对象）不收
- 同名提示：`MemPoison`（NeurIPS）与库内 MemPoison（2607.14651）、`RouteGuard`（GuardZoo）与库内 skill 检测 RouteGuard 需注意区分

## 论文分类

### 越狱、安全对齐与有害微调

### 1. DACE: Diversity-Driven Adversarial Co-Evolution for Robust LLM Safety Alignment

📝 [OpenReview](https://openreview.net/forum?id=EQ9xqhBm3G) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`adversarial co-evolution`、`safety alignment`、`strategy collapse`、`bayesian replay`
- 🎯 **研究动机**：对抗攻击持续演进使基于预收集数据的 LLM 安全对齐管线疲于应付，现有共同进化框架存在攻击策略坍缩与防御方对抗遗忘两个复合病症，而已有补救各自只顾一侧。
- 🔬 **研究方法**：提出 DACE 多样性驱动对抗共同进化框架，攻击侧以显式 12×10 策略空间（风险类别×攻击风格）配 normalized marginal coverage gain 奖励提供有界不衰减的策略层探索信号，防御侧以 Beta–Bernoulli 威胁后验经时间衰减刷新并 Thompson 采样的统一 Bayesian adversarial replay pool 锚定训练。
- 📌 **结论**：在标准安全、自动攻击者与通用能力基准上提升对 out-of-distribution 攻击的鲁棒性并保留通用能力，同时获得更广的攻击策略覆盖。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring robust safety alignment of large language models (LLMs) is increasingly difficult as adversarial attacks evolve and outpace alignment pipelines built on pre-collected data. Recent co-evolutionary frameworks let the defender chase a moving attacker, yet their training dynamics expose two compounding pathologies: \emphattack strategy collapse, where the attacker overfits to a narrow set of high-reward rewrites, and \emphdefense adversarial forgetting, where the defender loses competence against earlier attacks as the attack distribution drifts. Existing remedies are partial: attacker-side diversity rewards score textual novelty rather than strategy novelty, and defender-side replay relies on discrete judge scores that ignore estimation uncertainty, response stochasticity, and defender non-stationarity. We introduce DACE, a diversity-driven adversarial co-evolution framework that targets both pathologies jointly. On the attacker side, DACE couples an explicit 12×10 strategy space (risk category × attack style) with a \emphnormalized marginal coverage gain reward, providing a bounded, non-vanishing exploration signal at the strategy layer. On the defender side, DACE maintains a unified \emphBayesian adversarial replay pool whose Beta--Bernoulli threat posteriors are refreshed by time decay and sampled via Thompson sampling, anchoring defender training to an evolving threat landscape. Across standard safety, automated-attacker, and general-capability benchmarks, DACE improves robustness to out-of-distribution attacks while preserving general capabilities, and yields broader attacker strategy coverage.

</details>

### 2. Bridging the Gap Between Harmfulness Belief and Refusal Behavior for Safety Alignment

📝 [OpenReview](https://openreview.net/forum?id=oNxj0lY1EY) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`harmfulness belief`、`refusal behavior`、`safety alignment`、`interpretability`
- 🎯 **研究动机**：现有防御主要强化拒答行为，但可解释性工作表明有害性信念与拒答行为分别表征于 t_inst 与 t_post 隐状态，且信念在两者间传递时不可靠保留，导致模型内部识别有害却仍输出顺从回复。
- 🔬 **研究方法**：提出 BHR 训练框架，训练 adapter 将有害性信息携带到 t_post 隐状态、建立从有害信念到拒答行为的第二通路，并配 belief loss 维持准确有害判断与 belief-gated refusal loss 用 t_inst 信念调节拒答学习。
- 📌 **结论**：多个 LLM 与安全基准上显著提升对白盒和黑盒越狱攻击的鲁棒性，同时降低良性 prompt 上的过拒答风险并保留通用能力。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Many existing defenses mainly strengthen refusal behavior to improve the safety of LLMs. Recent interpretability work shows that, in safety-aligned LLMs, harmfulness belief and refusal behavior are represented separately in the hidden states at the last token of the user instruction (t_\mathrminst) and the response-start token (t_\mathrmpost), respectively. Based on it, we find that harmfulness belief is not reliably preserved when it is carried from the t_\mathrminst to the t_\mathrmpost. As a result, even when the LLM internally recognizes a request as harmful, it may still produce a compliant response. To address this, we propose Bridging Harmfulness and Refusal (BHR), a training framework that bridges harmfulness belief and refusal behavior. Specifically, BHR trains the adapter so that harmfulness information is carried to the hidden state at the t_\mathrmpost, thereby establishing a second pathway from harmfulness belief to refusal behavior. To keep this signal reliable during fine-tuning, we introduce two additional losses. A belief loss helps the LLM maintain an accurate harmfulness judgment at the t_\mathrminst. A belief-gated refusal loss uses the LLM's harmfulness belief at t_\mathrminst to regulate refusal learning, making attacks that target refusal features less effective while reducing the risk of over-refusal on benign inputs. Experiments across multiple LLMs and safety benchmarks show that BHR substantially improves robustness against both white-box and black-box jailbreak attacks, reduces the risk of over-refusal on benign prompts, and preserves general capabilities.

</details>

### 3. When Safety Becomes An Outlier: Understanding the Retention of LLM Safety Behaviors

📝 [OpenReview](https://openreview.net/forum?id=b28qPD14np) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`analysis`、`safety retention`、`refusal strings`、`output distribution`、`fine-tuning fragility`
- 🎯 **研究动机**：安全对齐 LLM 微调后常丢失安全行为、即使混入安全数据亦然，这一脆弱性虽有大量记录但其根本原因不明。
- 🔬 **研究方法**：提出公式化拒答串是模型输出分布中的 outlier（低支持行为）、易拟合但结构不稳定这一假说并经控制实验验证，据此以原始模型困惑度为分布自然性代理，构造保持输出分布内、语义接地的自然上下文感知安全监督，覆盖监督与偏好对齐两种设定。
- 📌 **结论**：多个模型与微调 regime 下同时提升即时安全与持续微调下的安全保持且不牺牲有用性，表明自然性是持久安全对齐的有用原则。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety-aligned large language models often lose their safety behaviors after fine-tuning, even when safety data are included. While this fragility is well documented, its underlying cause remains unclear. We propose that formulaic refusal strings function as in the model's output distribution, i.e., low-support behaviors that are easy to fit but structurally unstable under subsequent fine-tuning, and that this is an important source of safety fragility. Controlled experiments verify this: fixed refusals are acquired and forgotten much like arbitrary constant strings, in contrast to prompt-grounded natural responses. Motivated by this insight, we improve safety retention by constructing natural, context-aware safety supervision that keeps safety responses within the model's existing output distribution and grounded in semantics. We instantiate this principle in both supervised and preference-based alignment settings, using perplexity under the original model as a practical proxy for distributional naturalness. Across multiple models and fine-tuning regimes, our approach improves both immediate safety and its retention under continued fine-tuning without sacrificing helpfulness, suggesting that naturalness is a useful principle for durable safety alignment.

</details>

### 4. Rethinking LLM Fine-Tuning via Weight Space Reparameterization: Preserving Safety during Downstream Adaptation

📝 [OpenReview](https://openreview.net/forum?id=HssNfd9nbe) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`safe fine-tuning`、`weight reparameterization`、`safety-critical directions`、`downstream adaptation`
- 🎯 **研究动机**：下游任务微调常削弱已对齐的安全行为，现有方法在原参数空间定位安全相关神经元/层/方向，但安全信息分散于众多方向，下游更新会覆写编码安全行为的参数。
- 🔬 **研究方法**：提出 WSR-Tune 权重空间重参数化微调框架，构建安全条件化基并重参数化权重矩阵使安全信息集中于少数方向，在重参数化空间中冻结安全关键方向、仅更新其余互补方向做下游适应。
- 📌 **结论**：实验表明该方法在下游性能与安全保持之间取得更优权衡，实现可靠 LLM 微调。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning large language models (LLMs) on downstream tasks often weakens their previously aligned safety behavior, creating an inherent trade-off between task adaptation and safety preservation. Existing approaches attempt to mitigate this issue by identifying safety-relevant neurons, layers, or update directions in the original parameter space. However, safety-related information is often distributed across many directions in this space, causing downstream updates to overwrite parameters that encode safety behavior. We propose WSR-Tune, a Weight Space Reparameterization-based fine-tuning framework that preserves safety during downstream adaptation. Our approach constructs a safety-conditioned basis and reparameterizes the weight matrices such that safety-relevant information becomes concentrated in a small subset of directions. We then identify safety-critical directions and freeze them in the reparameterized space, while updating the remaining complementary directions for downstream adaptation. By explicitly structuring the parameter space to disentangle safety and task information, our method reduces interference between objectives and enables simultaneous preservation of safety and improvement in downstream performance. Experimental results show that our method achieves a more favorable trade-off between downstream performance and safety retention, demonstrating its effectiveness for reliable LLM fine-tuning.

</details>

### 5. SLDR: Defending Against Malicious Fine-tuning via Selective Layers Recovery and Dynamic Routing

📝 [OpenReview](https://openreview.net/forum?id=jjuXPhJpD0) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`malicious fine-tuning`、`lora recovery`、`dynamic routing`、`layer sensitivity`
- 🎯 **研究动机**：fine-tuning-as-a-service 场景下恶意微调会在保留合法任务性能的同时侵蚀拒答行为，而层安全敏感性是有符号的——缩放不同层可增强、削弱或不影响拒答，这一诊断未被用于防御。
- 🔬 **研究方法**：提出 SLDR 后微调防御，基于选择性层恢复与动态路由：仅在带符号敏感度谱中得分最大与最小的层上训练 LoRA 恢复适配器，并用基于表示的动态路由推理仅在恶意查询时激活该适配器。
- 📌 **结论**：四种架构、五个下游任务、四个有害基准上大幅减少有害输出并保住下游效用；Llama3.1/SST2 上平均有害分从 11.54 降至 0.08，投毒比例高达 0.9 时有害分仍近零。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning-as-a-service enables users to adapt aligned large language models (LLMs) to specialized tasks, but malicious fine-tuning can erode refusal behavior while preserving task performance on legitimate inputs. We revisit recent layer-wise safety diagnostics and find that safety sensitivity is signed: scaling different layers can strengthen refusal, weaken it, or have little effect. Motivated by this observation, we propose SLDR, a post-fine-tuning defense based on Selective Layers Recovery and Dynamic Routing. SLDR trains a LoRA recovery adapter only on the layers with the maximum and minimum sensitivity scores in the signed spectrum, and uses representation-based dynamic routing inference to activate the adapter only for malicious queries. Across four model architectures, five downstream tasks, and four harmful benchmarks, SLDR substantially reduces harmful outputs while preserving downstream utility. On Llama3.1/SST2, SLDR reduces the average harmful score from 11.54 to 0.08 while maintaining downstream accuracy, and the harmful score remains near zero under poisoning ratios up to 0.9.

</details>

### 6. Behaving Better, Thinking Worse: Sycophancy Across Post-Training Stages

📝 [OpenReview](https://openreview.net/forum?id=IUAXqLsMTC) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`analysis`、`sycophancy`、`post-training`、`log-odds`、`dual-track evaluation`
- 🎯 **研究动机**：需要刻画事实谄媚（sycophancy）如何随不同后训练管线产生与变化，其行为表现与内部置信的分离机制尚不清楚。
- 🔬 **研究方法**：在三个后训练管线（OLMo 3 7B Think/Instruct、Llama 3.1 8B Instruct、Tulu 3）上用 GPT-4o 生成轨与 ΔLogOdds 对数概率轨双轨评测 AMPS 与 MedQuAD，按挑战类型×上下文分解 in-context 反驳与预置错误答案断言下的谄媚偏移。
- 📌 **结论**：谄媚偏移是替代答案条件化的（单纯 pushback 无偏移，ethos/引用类挑战偏移显著）且集中于预置断言；后训练造成表面-预测分离——相同条目上行为翻转率显著下降而预置 ΔLogOdds 反而增大。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We trace factual sycophancy across three post-training pipelines (OLMo 3 7B Think and Instruct, Llama 3.1 8B Instruct, Tulu 3) on AMPS and MedQuAD with a dual-track evaluation: a GPT-4o-judged generative track and a log-probability track reporting \DeltaLogOdds separately under \emphin-context rebuttals and \emphpreemptive wrong-answer assertions. Decomposing by challenge type × context reveals three patterns. (1) Challenge type: the sycophantic shift is alternative-conditioned, so simple pushback with no asserted answer produces no shift, while ethos/justification/citation challenges produce substantial positive shifts. (2) Context: every base model's sycophantic shift concentrates preemptively, with weak or defensive in-context response. On computational, IC diverges into four pipeline-specific endpoints. On medical, the same four pipelines converge with no defensive IC developing on any recipe. (3) Behavioral vs log-probability: post-training produces a \emphsurface-predictive dissociation: matched-subset behavioral flip rate drops significantly on identical items while preemptive \DeltaLogOdds on those same items grows.

</details>

### 7. SuperSycophantic: Stress-Testing Frontier LLMs from Single- to Multi-Turn Sycophancy

📝 [OpenReview](https://openreview.net/forum?id=v2ZJiUHkC6) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`benchmark`、`sycophancy`、`stress testing`、`multi-turn pressure`、`frontier llms`
- 🎯 **研究动机**：以最大化用户满意度为目标的模型可能无条件附和用户而牺牲事实性，在高风险决策支持场景构成重大风险，但缺乏从单轮到多轮的系统性谄媚压力测试。
- 🔬 **研究方法**：提出 SuperSycophantic 压力测试框架，涵盖有可验证答案的客观（OBJ）题与无 ground truth 的主观（SUB）场景，测试从首轮语境框架到多轮用户压力诱发的谄媚，并评测 9 个前沿模型。
- 📌 **结论**：表现最好的 GPT-5.4 仍在 23.8% 的 OBJ 场景将正确答案改错、过半 SUB 场景盲目跟随用户观点；用户语气强度是被忽视的关键因素，且 Claude 模型在中等压力下独特地更谄媚（强触发反而促其重想得到正确答案）。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI sycophancy is gaining increasing prevalence as models optimized to maximize user satisfaction may tend to unconditionally agree with users even at the expense of factuality, which poses great risk as AI are increasingly used for decision support in high-stake scenarios. We present \ourWork, a systematic stress-testing framework encompassing objective (OBJ) questions with verifiable answers and subjective (SUB) scenarios without ground truth on sycophancy induced from first-turn context framing to multi-turn user pressure. Evaluation of 9 frontier models revealed high sycophancy in even the best-performing models such as GPT-5.4 changes answers from right to wrong to please users in 23.8% of OBJ scenarios and blindly follows the pressured user view in more than half of the SUB scenarios. We found that strength of user tone is one of the most impactful yet previously overlooked factor for AI sycophancy and discover an interesting pattern where Claude models are uniquely more sycophantic under moderate pressure because strong triggers often lead them to rethink questions from scratch to arrive at the correct impartial answer. These findings highlight the need for anti-sycophancy training in future model development, where training models to rethink from scratch when facing pressure may serve as a promising paradigm towards more truthful AI systems. We provide our code and data in the supplementary material.

</details>

### 8. Answering At Any Cost: Frontier LLMs Are Consequence-Insensitive

📝 [OpenReview](https://openreview.net/forum?id=juGEeYEuAS) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`analysis`、`abstention`、`consequence sensitivity`、`post-training bias`、`frontier models`
- 🎯 **研究动机**：LLM 系统日益部署在错误输出带真实代价的领域，核心问题不只是出错而是后果不敏感——模型不按出错代价调整行为而系统性欠弃权。
- 🔬 **研究方法**：跨显式效用框架与模拟真实部署的自然语言风险描述、覆盖智能体编程与数学推理及五个前沿模型家族，系统评测弃权行为，并对比 base 与指令微调模型、检验事后干预/上下文学习/微调等多种补救。
- 📌 **结论**：模型在弃权严格占优的平凡场景甚至被告知错误答案将导致核灭绝时仍提交答案；该缺陷与模型规模/能力正交，大量偏差可定位到后训练（base 模型弃权远多），且现有干预无一能稳健解决。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based systems are increasingly deployed in domains where incorrect outputs carry real costs, often necessitating expensive human review and verification. We argue that a central issue is not simply error, but : models fail to adjust their behavior according to the cost of being wrong. We study this failure across both explicit utility framings as well as natural-language descriptions of stakes that mirror real-world deployment scenarios. Our evaluation spans agentic coding and mathematical reasoning, covering five frontier model families. Across settings, models systematically under-abstain: they continue to answer or submit patches even when incorrect answers carry significant consequences. The pathology is striking: models continue to submit answers in trivial settings where abstention is strictly dominant, and even when told an incorrect answer will cause nuclear extinction. Further, we find that this behavior is orthogonal to existing benchmarks; increasing model size or capability within a family does not improve sensitivity. Comparing base and instruction-tuned models localizes much of this anti-abstention bias to post-training: base models abstain far more often, though they are not themselves reliably consequence-aware. Finally, we evaluate prior post-hoc interventions alongside in-context learning and fine-tuning, finding that none robustly resolves the failure. Our results suggest that current post-training and evaluation pipelines optimize models to answer, not to act under stakes -- a significant bottleneck for trustworthy autonomy.

</details>

### 9. Gradient-Guided Smoothing for LLM Safety Defense

📝 [OpenReview](https://openreview.net/forum?id=1LhCQwinaY) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`jailbreak`、`randomized smoothing`、`density guidance`、`gradient ascent`
- 🎯 **研究动机**：平滑类防御依赖越狱攻击的脆弱性，当越狱上下文语义间隔较大时效果退化，而成功攻击往往利用输入空间的低概率区域、使 LLM 安全边界难以可靠泛化。
- 🔬 **研究方法**：提出梯度引导平滑，将随机噪声与 Gauss-Southwell 型对上下文感知输入分布对数密度的迭代上升相结合，引导扰动趋向高密度区域以恢复 LLM 安全机制。
- 📌 **结论**：在四种越狱攻击与三个指令遵循基准上有效提升安全性并保持 LLM 效用。

👤 **作者**：Yuxuan Gu、…、Bing Qin

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models remain susceptible to jailbreak attacks, despite extensive safety alignment. Smoothing-based defense methods can leverage their intrinsic safety capabilities, but the efficacy relies on the brittleness of jailbreak attacks and degrades when jailbreak contexts exhibit larger semantic margins. We observe that successful attacks typically exploit low-probability regions of the input space, where LLMs' safe bounds are difficult to reliably generalize. Thus, we propose guiding perturbations toward higher-density areas to restore the effectiveness of LLMs' safety mechanisms. In detail, we present gradient-guided smoothing that combines random noise with Gauss-Southwell type iterative ascent to the log density of the context-aware input distribution. Experimental results across four jailbreak attacks and three instruction-following benchmarks demonstrate that our method effectively improves safety while maintaining the utility of LLMs.

</details>

### 10. Rubric-Align: Safety Alignment through Dynamically Co-Evolving Rubrics

📝 [OpenReview](https://openreview.net/forum?id=BDgXsrFjIF) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`safety alignment`、`reinforcement learning`、`natural-language rubric`、`reward sparsity`
- 🎯 **研究动机**：基于 RL 的安全对齐面临奖励稀疏、可解释性差与跨域迁移有限的持续挑战。
- 🔬 **研究方法**：提出 Rubric-Align，用动态自然语言评估 rubric 取代静态二元标量奖励，对每个响应给出细粒度可解释反馈，并依据当前策略行为周期性细化 prompt 专属 rubric，使监督信号与模型演化的失败模式保持对齐。
- 📌 **结论**：在安全基准与垂直领域上提升对有害与越狱提示的鲁棒性并大体保持通用能力，表明自然语言 rubric 是将安全监督适配到新安全子域的可迁移接口。

👤 **作者**：Ruipeng Wang、…、Xiang Wang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent progress in large language models (LLMs) has led to impressive performance across diverse domains. However, their deployment in critical areas such as healthcare, law, and education raises serious concerns regarding the potential generation of harmful content. While reinforcement learning (RL)-based safety alignment methods have been extensively studied, they face persistent challenges, including sparse reward signals, limited interpretability, and limited transferability across domains. In this paper, we introduce Rubric‑Align, a framework that replaces static binary scalar rewards with dynamic, natural‑language evaluation rubrics. Instead of assigning a single reward to each response, Rubric‑Align provides fine‑grained and interpretable feedback, thereby alleviating reward sparsity and improving the transparency of the alignment signal. A key feature of Rubric-Align is its dynamic rubric evolution mechanism. Rather than using fixed reward templates, Rubric-Align periodically refines prompt-specific rubrics based on the current policy behavior, keeping the supervision signal informative and aligned with the model’s evolving failure modes. Experiments on safety benchmarks and vertical-domain settings show that Rubric-Align improves robustness against harmful and jailbreak prompts while largely preserving general capabilities, suggesting that natural-language rubrics provide a transferable interface for adapting safety supervision to new safety subdomains.

</details>

### 11. PoSafeNet: Structured Safety Learning via Compositional Projection

📝 [OpenReview](https://openreview.net/forum?id=7K93T7me9y) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`robot safety`、`control barrier function`、`partial order`、`safety layer`
- 🎯 **研究动机**：机器人安全学习常涉及多个无法同时满足的异构安全约束，现有神经安全层把多约束安全当数值优化问题，将"冲突时可牺牲哪条约束"的语义问题藏进求解器几何、罚权重或固定总层级。
- 🔬 **研究方法**：提出 PoSafeNet，将可采纳的安全覆盖关系编码为偏序（poset），通过组合到 CBF 诱导半空间的闭式投影实现每个可采纳执行。
- 📌 **结论**：在多障碍导航、受限操作与视觉自动驾驶上，相比 dQP、松弛与层级安全层提升操作可行性、计算效率与任务性能。

👤 **作者**：Kiwan Wong、Wei Xiao、Daniela Rus

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safe robot learning often involves multiple heterogeneous safety constraints that cannot always be satisfied simultaneously. Existing neural safety layers typically treat multi-constraint safety as a numerical optimization problem, enforcing all constraints through a single QP-based projection or relaxing conflicts with slack variables. This hides the semantic question of which constraints may be sacrificed under conflict inside solver geometry, penalty weights, or a fixed total hierarchy. We propose PoSafeNet, a poset-structured composable safety layer that makes these conflict semantics explicit. PoSafeNet encodes admissible safety override relations as a partial order and realizes each admissible execution by composing closed-form projections onto CBF-induced halfspaces. Across multi-obstacle navigation, constrained manipulation, and vision-based autonomous driving, PoSafeNet improves operational feasibility, computational efficiency, and task performance over dQP-based, slack-based, and hierarchical safety layers.

</details>

### 12. SelfGuard: Self-Supervised Deviation Modeling for Multi-Modal Jailbreak Detection

📝 [OpenReview](https://openreview.net/forum?id=fQrMmdCmbG) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`detection`、`multimodal jailbreak`、`self-supervised`、`deviation modeling`、`pseudo-harmful sample`
- 🎯 **研究动机**：MLLM 易受利用细微跨模态线索绕过安全机制的越狱攻击，而有害数据稀缺且快速演变，基于已知模式训练的检测器难以泛化。
- 🔬 **研究方法**：提出自监督框架 SelfGuard，仅用良性数据学习攻击无关信号，通过针对跨模态语义不一致、格式操纵、语义毒性三类线索的受控变换合成伪有害样本，经多任务自监督学习（错位判别、重建式毒性建模、对比格式建模）并在推理时多视角聚合偏离分数。
- 📌 **结论**：在多个 benchmark 上的大量实验验证了该方法对多模态越狱检测的有效性。

👤 **作者**：Chenchen Jing、…、Chunhua Shen

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-modal large language models (MLLMs) achieve strong vision–language reasoning ability but remain vulnerable to jailbreak attacks that exploit subtle cross-modal cues to bypass safety mechanisms. Detecting such attacks is difficult because harmful data are scarce and rapidly evolving, while detectors trained on known patterns often fail to generalize. In this paper, we cast multi-modal jailbreak detection as self-supervised deviation modeling and learn attack-agnostic signals from benign data only. We propose SelfGuard, a self-supervised framework, which models benign multi-modal regularities and learns to score structured violations via controlled pseudo-harmful deviations. SelfGuard synthesizes pseudo-harmful samples via controlled transformations that target three signature cues, cross-modal semantic inconsistency, format manipulation, and semantic toxicity. It then learns complementary deviation statistics through multi-task self-supervised learning, including misalignment discrimination, reconstruction-based toxicity modeling, and contrastive format modeling. At inference, SelfGuard performs multi-view deviation estimation by aggregating task-specific deviation scores to identify departures from benign multi-modal regularities. Extensive experiments on various benchmarks show the effectiveness of our method.

</details>

### 13. Personalized Safety in Federated Fine-Tuning of Large Language Models

📝 [OpenReview](https://openreview.net/forum?id=P1iPC9eKmI) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`benchmark`、`federated learning`、`personalized safety`、`lora`、`llm fine-tuning`
- 🎯 **研究动机**：机构内联邦微调 LLM 时各客户端共享模型却要求不同的安全行为，经典联邦学习与集中式对齐都无法刻画这一"个性化联邦安全"问题。
- 🔬 **研究方法**：形式化该设定并给出紧凑可解释的客户端策略空间与策略条件化基准构建框架（覆盖医疗、法律合规、金融、青少年、企业五类原型），进一步提出 Safety-Aware Weighted LoRA（SAW-LoRA），让各客户端按任务收益与本地安全风险估计选择性吸收全局任务更新。
- 📌 **结论**：基准含 1,500 条客户端条件化训练例与 750 条留出评估例；在两个任务数据集、两个骨干上使客户端特定 ASR 降至约 1-2%，同时保持高良性接受率。

👤 **作者**：Tianzhe Xiao、…、Ozgur B Akan

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly adapted inside privacy- and regulation-constrained institutions where local post-training data cannot be centrally pooled. Federated learning therefore becomes a natural mechanism for collaborative LLM adaptation, but it also raises a safety question that is not captured by either classical federated learning or standard centralized alignment: clients may share a model while still requiring different safe behaviors. We formalize this setting as \emphpersonalized federated safety, where safety correctness is conditioned on the target client's local policy rather than treated as a single global refusal rule. To make this problem transferable rather than benchmark-specific, we introduce a compact, interpretable client policy space and a policy-conditioned benchmark construction framework, then instantiate it with five representative client archetypes spanning regulated healthcare, legal compliance, financial safety, youth safety, and enterprise general safety. The resulting benchmark contains 1,500 client-conditioned training examples and 750 held-out evaluation examples. We further propose \emphSafety-Aware Weighted LoRA (SAW-LoRA), a lightweight add-on for federated LoRA fine-tuning that lets each client selectively absorb incoming global task updates according to estimated task benefit and local-safety risk. Across two task datasets and two backbones, this add-on substantially lowers client-specific ASR for the strongest local safety mechanisms, reaching ASR near 1--2% while preserving high benign acceptance. These findings position personalized federated safety as a concrete research problem with a practical update mechanism for federated LLM adaptation.

</details>

### 14. Surrogate Calibration for Transferable Adversarial Attacks against Black-Box MLLMs

📝 [OpenReview](https://openreview.net/forum?id=Nla00lCEuD) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`transferable adversarial example`、`black-box mllm`、`surrogate calibration`、`plug-and-play`
- 🎯 **研究动机**：基于迁移的攻击常把对抗样本推入替代模型特有的局部最优——只骗过替代模型而无法迁移到黑盒 MLLM，现有方法只在攻击层面缓解而不改变替代模型本身。
- 🔬 **研究方法**：提出模型级精炼方法 SCal，以特征保持损失维持替代模型表征效用、以分布正则化约束其梯度场贴近自然数据流形，即插即用地增强下游迁移攻击。
- 📌 **结论**：全面提升各类攻击：例如把 M-Attack 在 GPT-5.4 Mini 上的 ASR 提升至 53.5%，大幅超越 SOTA 方法 MPCAttack 的 29.7%。

👤 **作者**：Zhewen Yao、Yao Zhu、Xiangyang Ji、Shiliang Zhang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Transfer-based attacks expose serious adversarial vulnerabilities in closed-source Multimodal Large Language Models (MLLMs) by crafting adversarial examples on off-the-shelf surrogate models. However, this paradigm often drives adversarial examples toward surrogate-specific local optima, where they deceive only the surrogate model but fail to transfer to black-box MLLMs. Although existing methods mitigate this issue at the attack level, they leave the surrogate itself unchanged. To address this gap, we propose Surrogate Calibration (SCal), a novel model-level refinement that enhances downstream transfer-based adversarial attacks in a plug-and-play manner. Specifically, SCal employs a feature-preserving loss to maintain the surrogate's representational utility, while a distributional regularizer encourages its gradient field to stay closer to the natural data manifold. With calibrated surrogates, downstream attacks generate update directions that exhibit superior generalization across black-box MLLMs. Extensive experiments demonstrate that SCal boosts current attacks to new heights across various surrogates. For instance, it elevates baseline M-Attack's ASR on GPT-5.4 Mini to 53.5%, substantially surpassing the state-of-the-art MPCAttack (29.7%). These results expose critical vulnerabilities that must be addressed for trustworthy multimodal systems. Code is at: https://anonymous.4open.science/r/SCal_code-B0BC

</details>

### 15. TraceGuard: Defending Multi-Turn Jailbreak Attacks via Prompt-Response Risk Signal Tracking

📝 [OpenReview](https://openreview.net/forum?id=Fa3tAbEDkR) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`detection`、`multi-turn jailbreak`、`risk signal tracking`、`black-box defense`、`llm api`
- 🎯 **研究动机**：以黑盒 API 部署的 LLM 面临有害意图跨轮渐进构建的多轮越狱，现有防御要么只针对单轮、要么需模型内部访问，难以应对弱单轮可分性、跨轮依赖与动态攻击模式。
- 🔬 **研究方法**：受线性表示假设启发分析表示空间风险信号，发现其碎片化分布于提示、响应与轮次间并随交互演化；提出在线黑盒防御 TraceGuard，S 模式捕捉跨视角风险表示及其跨轮演化，A 模式进一步支持分布感知的少样本自适应。
- 📌 **结论**：多基准、多目标 LLM 上实现更优的多轮越狱检测，同时保持效用与效率并泛化到未见攻击。

👤 **作者**：Hongyi Li、…、Wu Jie

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have made remarkable progress and are increasingly deployed as black-box API services. However, they remain vulnerable to jailbreak attacks that bypass safeguards and elicit harmful content, especially in multi-turn settings where harmful intent is gradually constructed over the interaction. Existing defenses primarily target single-turn scenarios or require access to model internals, making them insufficient against black-box multi-turn jailbreak attacks with weak single-turn discriminability, cross-turn dependency, and dynamic attack patterns. To bridge this gap, we first analyze harmful intent in multi-turn jailbreak interactions through representation-space risk signals inspired by the Linear Representation Hypothesis. Our analysis reveals that these signals are fragmented across prompts, responses, and turns, progressively evolve over the interaction, and exhibit attack-dependent temporal patterns. Motivated by this, we propose TraceGuard, an online black-box defense framework that detects multi-turn jailbreak attacks by tracking prompt and response risk signals as the interaction unfolds. Specifically, TraceGuard operates in two modes: TraceGuard-S captures cross-view risk representations and their cross-turn evolution, while TraceGuard-A further enables distribution-aware few-shot adaptation to dynamic attack patterns. Extensive experiments across multiple benchmarks and target LLMs demonstrate that TraceGuard achieves superior multi-turn jailbreak detection while preserving utility, maintaining efficiency, and generalizing to unseen attacks.

</details>

### 16. Safeguarding LLMs via Model-Agnostic Latent Safety Signals from Dark Knowledge

📝 [OpenReview](https://openreview.net/forum?id=CIcsWVLkb3) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`dark knowledge`、`latent safety signal`、`decoding-stage`、`model-agnostic`
- 🎯 **研究动机**：解码阶段防御存在安全与过度拒答的权衡，且多数方法依赖内部隐藏状态而绑定特定架构，开销大且跨模型泛化有限。
- 🔬 **研究方法**：提出 LADE，从首 token 输出概率分布的暗知识（超越 argmax 的概率信息）中提取潜在安全信号（有害与良性查询间概率差异显著的 token），经 tokenizer 映射实现模型无关应用，再用 kNN 检索判别查询。
- 📌 **结论**：在六个 LLM 与多个基准上对广泛越狱攻击保持鲁棒并降低攻击成功率，且过度拒答极小。

👤 **作者**：Wonjun Lee、…、Suhyun Kim

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have advanced rapidly, raising growing concerns about their safety. Recent work has proposed various approaches to detect and defend against adversarial attacks including defense mechanisms at the decoding stage that leverage models' internal hidden states. However, existing decoding-stage defenses suffer from two limitations. First, they introduce a trade-off between safety and over-refusal, where strengthening safety degrades the model's helpfulness on benign queries. Second, many of these methods rely on internal hidden states and are thus restricted to specific architectures, incurring substantial overhead and limited generalization across models. To address these limitations, we introduce LADE (Latent Safety Signals for Defense), which leverages latent safety signals extracted by contrasting harmful and benign queries from dark knowledge (i.e., information carried by the output probability distribution beyond its argmax) in the first-token output probability distribution. Our key insight is that, beyond surface-level refusal tokens, the dark knowledge in the first-token distribution contains latent safety signals, defined as tokens whose probabilities differ sharply between harmful and benign queries. We empirically show that these signals consistently align across diverse LLMs, forming a model-agnostic direction that reflects an intrinsic property of safety-aligned language models. LADE consists of three components: (1) Extracting Latent Safety Signals from Dark Knowledge, which selects top-k safety-discriminative tokens from the first-token probability distribution; (2) Tokenizer Mapping, which maps these tokens across different tokenizers to enable model-agnostic application; and (3) kNN-based Discrimination, which classifies queries via a k-Nearest Neighbors search over the mapped tokens. Across six LLMs and multiple benchmarks, LADE remains robust against a wide range of jailbreak attacks and lowers attack success rates with minimal over-refusal.

</details>

### 17. JEDI: Real-Time Jailbreak Defense for LLMs via In-Generation Detection and Intervention

📝 [OpenReview](https://openreview.net/forum?id=tbFhcVR6Oa) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`jailbreak`、`streaming generation`、`representation engineering`、`steering vector`
- 🎯 **研究动机**：流式生成场景的 prefix exposure 使有害 token 一生成立即暴露给用户，现有防御要么不满足实时约束、要么引入明显延迟损害体验。
- 🔬 **研究方法**：提出 JEDI 实时防御，利用表示工程监控 LLM 内部语义漂移，用 Cumulative Sum 算法在有害意图显现前持续识别，一旦检出风险即动态注入 steering vector 把生成轨迹重定向回安全子空间。
- 📌 **结论**：跨 6 个模型、11 种攻击向量取得 93.6%-99.4% 的防御成功率并超越 SOTA 基线，同时保持模型效用，Time To First Token 开销仅约 0.003 秒。

👤 **作者**：Ruilin Xie、Bixin Li、Xinyu Chen、Yongqiang Tian、Wang Lulu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models remain vulnerable to jailbreak attacks despite extensive efforts to ensure safety alignment. Streaming generation scenarios exacerbate this vulnerability by exposing harmful tokens to users immediately upon generation, a phenomenon known as prefix exposure. Existing defenses often fail to address this real-time constraint or impose substantial latency that degrades user experience. To bridge this gap, we propose JEDI, a real-time defense method that secures streaming outputs via in-generation detection and intervention. JEDI leverages representation engineering to monitor the LLM’s internal semantic drift, using a Cumulative Sum algorithm to identify persistent, harmful intent before it manifests in the output. Upon detecting a risk, the system dynamically injects a steering vector to redirect the generation trajectory toward a safe subspace. Extensive evaluations across 6 distinct models and 11 attack vectors demonstrate that JEDI achieves defense success rates ranging from 93.6% to 99.4%, outperforming state-of-the-art baselines. Furthermore, JEDI preserves model utility with a Time To First Token overhead of approximately 0.003 seconds, validating its viability for latency-sensitive applications. Our code and experimental results are available at: https://anonymous.4open.science/r/JEDI-93F9

</details>

### 18. Stage-wise Attention-Guided Region Sequencing for Adversarial Attacks on Large Vision-Language Models

📝 [OpenReview](https://openreview.net/forum?id=smKuw27bpk) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`adversarial perturbation`、`lvlm`、`attention-guided`、`region sequencing`
- 🎯 **研究动机**：L∞ 约束下 LVLM 的定向对抗攻击本质是区域扰动预算分配问题，而现有局部化攻击依赖随机空间采样、常更新弱影响区域。
- 🔬 **研究方法**：基于"跨模态注意力可定位对抗敏感区域、扰动高注意力热点会引发向次显著区域可预测再分布"的分析，提出 SAGA 黑盒区域排序攻击，仅用开源 LVLM 的固定 attention map 引导扰动更新顺序，无需访问目标模型参数、梯度或注意力图。
- 📌 **结论**：在十个闭源与开源 LVLM 上取得 SOTA 攻击成功率与最佳整体不可感知性。

👤 **作者**：Jaehyun Kwak、Nam Cao、Boryeong Cho、Segyu Lee、Sumyeong Ahn、Se-Young Yun

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Targeted adversarial attacks on Large Vision-Language Models (LVLMs) test whether small image perturbations can steer model responses toward attacker-specified content. Under the standard L_\infty constraint, targeted attacks become a regional perturbation budget allocation problem: attack success depends not only on the perturbation objective, but also on which regions receive updates and in what order. Existing localized attacks improve over global perturbations but rely on stochastic spatial sampling, often updating weakly influential regions. We address this limitation through an attention-based analysis showing that cross-modal attention identifies adversarially sensitive regions and that perturbing high-attention hotspots induces predictable redistribution toward subsequent salient regions. These findings motivate attention-guided region sequencing, which begins from dominant hotspots and progressively moves the update support toward next-salient regions. Based on these principles, we propose Stage-wise Attention-Guided Attack (SAGA), a black-box region-sequencing framework that uses a fixed attention map from an open-source LVLM to guide perturbation updates without accessing target-model parameters, gradients, or attention maps. Across ten closed-source and open-source LVLMs, SAGA achieves state-of-the-art attack success rates and the best overall imperceptibility.

</details>

### 19. SAVeR$^2$: Reasoning-based Safety Alignment for Large Reasoning Models via Verifiable Rewards

📝 [OpenReview](https://openreview.net/forum?id=k4DnfPDu16) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`safety alignment`、`large reasoning model`、`verifiable reward`、`gradient projection`
- 🎯 **研究动机**：LRM 的显式 CoT 推理带来新安全风险，现有对齐方法忽视模型内在推理能力，导致对抗泛化差、显著的"safety tax"与不忠实的粗粒度奖励。
- 🔬 **研究方法**：提出 SAVeR²（Safety Alignment via Rewards with Reasoning capability），把安全目标分解为四个细粒度可验证奖励信号，配合难度感知数据选择稳定训练，并用推理保持的梯度投影机制解析式消解安全梯度与推理梯度的冲突以消除 safety tax。
- 📌 **结论**：在 1.5B 至 671B 模型上跨多基准取得更优安全性能与显著更低过拒绝率，且不损害通用推理能力。

👤 **作者**：Yichen Sun、LIN JIANAN、Linbo Jiang、Shiyu Wang、Zhibo Wang、Zhixuan Chu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Reasoning Models (LRMs) have achieved impressive performance via explicit Chain-of-Thought (CoT) reasoning, yet this process introduces critical safety risks. We formalize LRM safety objectives as requiring non-malicious reasoning and answers, safety consistency, and explicit intent identification. We argue that existing alignment methods suffer from poor adversarial generalization, a significant ``safety tax'' on reasoning, and unfaithful coarse-grained rewards, primarily due to their neglect of the LRM's intrinsic reasoning capabilities for safety. To address these, we propose SAVeR^2, a novel Safety Alignment method via Rewards with Reasoning capability. SAVeR^2 decomposes the safety objective into four fine-grained verifiable reward signals and utilizes a difficulty-aware data selection strategy to stabilize training. Crucially, we introduce a reasoning-preserving gradient projection mechanism that analytically resolves conflicts between safety and reasoning gradients, effectively eliminating the safety tax. Extensive experiments on models ranging from 1.5B to 671B demonstrate that SAVeR^2 achieves superior safety performance and significantly lower over-refusal rates across multiple benchmarks without compromising general reasoning capabilities.

</details>

### 20. Safe in Its Own Words: Self-Guided Safety Alignment for  Multimodal Reasoning Models

📝 [OpenReview](https://openreview.net/forum?id=PFyto9A2fG) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`safety alignment`、`multimodal reasoning`、`self-guided generation`、`over-refusal`
- 🎯 **研究动机**：多模态推理模型的安全对齐依赖强教师模型的 reasoning trace 微调，带来过度拒绝的隐藏代价——表面敏感但语境安全的边界输入被误拒，根因是外部教师监督造成分布失配。
- 🔬 **研究方法**：提出 SAGE 自引导数据生成框架：推理级引导先诱导 safety-aware 轨迹，决策级引导再基于该轨迹诱导最终回答，不依赖外部教师 trace。
- 📌 **结论**：在 LLaVA-CoT 上将 FigStep ASR 从 86.2% 降至 2.1%，平均过度拒绝 43.1 显著优于教师监督法（66.9）。

👤 **作者**：Adeel Yousaf、Souradip Chakraborty、Mubarak Shah、Amrit Singh Bedi

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large reasoning models can reason over images and text, but they remain vulnerable to multimodal jailbreaks. Recent safety-alignment methods reduce attack success rate (ASR) by fine-tuning on reasoning traces from stronger teacher models. We show that this has a hidden cost of over-refusal. The aligned model learns to reject benign inputs that contain sensitive words or visual cues. This is especially harmful for boundary-safe inputs, where the prompt looks risky on the surface but is safe in context. We identify external teacher supervision as a key factor in this behavior. It introduces a distributional mismatch and shifts supervision away from the base model's own reasoning distribution. To address this, we propose SAGE (Safety-Aware Guided Elicitation), a self-guided data generation framework for multimodal safety alignment. SAGE guides generation in two stages: a reasoning-level guide first elicits a safety-aware trace, and a decision-level guide then elicits the final response conditioned on that trace. This factorized guidance lets SAGE shape both the reasoning process and the final safety decision without relying on external teacher traces. On LLaVA-CoT, SAGE reduces FigStep ASR from 86.2% to 2.1% and achieves an average over-refusal of 43.1, compared with 66.9--71.1 for prior reasoning-based safety-alignment methods, while preserving general utility. We will release the SAGE training dataset.

</details>

### 21. JailBound: A FOL-Guided Jailbreak Evaluation Framework for Revealing Safety Boundaries of LLMs

📝 [OpenReview](https://openreview.net/forum?id=MkFYo6dOiL) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`benchmark`、`jailbreak evaluation`、`first-order loss`、`embedding-space optimization`、`threat taxonomy`
- 🎯 **研究动机**：现有越狱评测依赖人工收集 prompt 或离散文本空间优化，覆盖面有限且难以扩展到新威胁场景。
- 🔬 **研究方法**：提出 JailBound 框架，以覆盖风险类别、应用领域、攻击类型的分层威胁分类学自动构建基准并用微调的 meta-attack 生成器产出攻击 prompt，再把越狱评测表述为嵌入空间攻击优化问题，用一阶损失（FOL）引导的双分支搜索联合定位高价值脆弱区域与安全边界状态。
- 📌 **结论**：统一协议下评测 13 个家族的 46 个 LLM，风险场景覆盖比现有 prompt 基准更广，优化攻击可跨模型家族有效迁移，并支撑对脆弱模式与安全边界行为更细粒度的分析。

👤 **作者**：Fazong Wu、Ming Yang、Xin Wang、Zhenyong Zhang、Xiaoming Wu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are now deployed in a wide range of real-world applications, making it important to evaluate how reliably they resist jailbreak attacks. However, existing jailbreak evaluations mainly rely on manually collected prompts or discrete text-space optimization, which limits their coverage and makes them difficult to extend to new threat settings. We present JailBound, a jailbreak evaluation framework that combines automated benchmark construction with intent-preserving attack optimization in embedding space. JailBound organizes evaluation instances with a hierarchical threat taxonomy spanning risk categories, application domains, and attack types, and uses this structure to generate meta-attack prompts with a fine-tuned meta-attack generator. It further formulates jailbreak evaluation as an embedding-space attack optimization problem and uses a first-order loss (FOL)-guided dual-branch search to jointly identify high-value vulnerable regions and safety boundary states. Under a unified evaluation protocol, we study 46 LLMs from 13 model families. The results show that JailBound covers a broader range of risk settings than existing prompt-based benchmarks, and that its optimized attacks transfer nontrivially across model families while supporting finer-grained analysis of vulnerability patterns and safety boundary behavior. \textcolorred\textWarning: this paper includes examples that may be offensive or harmful.

</details>

### 22. Safety Reconstructed: Generative Modeling via Masked Diffusion Builds Strong Safety Guardrails

📄 [arXiv](https://arxiv.org/abs/2609.33634) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`defense`、`guard model`、`masked diffusion`、`generative classifier`、`calibration`
- 🎯 **研究动机**：现有 guard 模型仅从对话上下文预测单个裁决 token，监督集中于单一目标，导致捷径特征、过度自信且对安全证据在序列中的位置而非其角色敏感。
- 🔬 **研究方法**：LLaDA-Guard 将判别式标签预测反转为"哪个标签更好解释文本"，在每个标签假设下对 prompt/response 打分并按差值分类，以类条件重构目标加 LoRA 微调 LLaDA-8B-Instruct、无需架构改动。
- 📌 **结论**：在 7 个 held-out 安全基准上以平均排名领先基于更强骨干的判别式基线，校准显著更优（ECE 0.0875 对 Qwen3Guard 的 0.1384），免训练改写不安全 prompt 的转安全率达 60.7%。

👤 **作者**：Gert Lek、Abele Malan、Chaoyi Zhu、Pin-Yu Chen、Robert Birke、Lydia Chen

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Guard models are the last line of defense between a language model and a harmful output, yet their training objective is surprisingly narrow. Existing guards learn to predict a single verdict token from a conversational context, concentrating supervision on a single target. The consequences are structural: models latch onto shortcut features, are overconfident, and remain sensitive to where safety evidence appears in the sequence rather than its role in the full context. We propose a different framing. Rather than predicting a label from text, our LLaDA-Guard asks which label better explains the text: scoring the prompt or response under each label hypothesis and classifying based on their difference. This shifts supervision to every token in the moderated region, forcing the model to account for full content rather than its most discriminative fragments. We instantiate this idea with a masked diffusion language model, fine-tuning LLaDA-8B-Instruct with a class-conditional reconstruction objective using LoRA and requiring no architectural changes beyond the base model. LLaDA-Guard leads on average rank against discriminative baselines trained on stronger backbones across seven held-out safety benchmarks, while exhibiting substantially better confidence calibration (ECE 0.0875 vs. 0.1384 for Qwen3Guard), less over-defense on benign prompts with unsafe-looking cues, and less prompt leakage when moderating responses. Its generative nature further enables token-level risk localization as a natural byproduct, yielding a pipeline for rewriting unsafe prompts into safe equivalents without additional training and achieving a 60.7% average conversion-to-safe rate.

</details>

### 23. Towards Mitigating Deceptive Safety Alignment in Large Reasoning Models

📄 [arXiv](https://arxiv.org/abs/2609.36254) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`defense`、`deceptive safety alignment`、`large reasoning model`、`rl alignment`、`prefilling attack`
- 🎯 **研究动机**：LRM 的 RL 奖励只依据最终答案、对中间推理几乎无监督，导致推理轨迹与最终答案安全信号不一致的欺骗性安全对齐，且缺乏系统度量与机理认识。
- 🔬 **研究方法**：提出 DSAR 指标联合评估推理轨迹与最终答案以量化安全不一致，发现该现象在标准提示下普遍、预填充攻击下显著放大且隐表征分析显示模型在答案阶段的安全判别强于中间推理；进而提出 SARA，用 RL 同时奖励安全感知推理与安全答案，促成早期有害意图识别并强制推理-答案一致。
- 📌 **结论**：SARA 在标准与对抗设置下均显著缓解欺骗性安全对齐，同时保持有益性与效用。

👤 **作者**：Xiangyu Zhou、Saleh Zare Zade、Rafi Ibn Sultan、Alexander Kotov、Dongxiao Zhu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Reasoning Models (LRMs) are commonly trained with reinforcement learning (RL) to improve their generation of chain-of-thought (CoT) reasoning before producing final answers. However, RL rewards are typically assigned based on final answers, providing little or no direct supervision over intermediate reasoning. This can lead to deceptive safety alignment, where the reasoning trace and final answer convey inconsistent safety signals. To systematically investigate this phenomenon, we introduce DSAR (Deceptive Safety Alignment Rate), a metric that jointly assesses reasoning traces and final answers to quantify their safety inconsistency. Across multiple LRMs and benchmarks, we find that deceptive safety alignment is pervasive under standard prompting conditions and is substantially amplified under prefilling attacks. We further provide a hidden representation analysis showing that models exhibit stronger safety discrimination at the final-answer stage than during intermediate reasoning. To close this gap, we propose SARA (Safety-Aware Reasoning Alignment), an RL-based method that rewards both safety-aware reasoning and safe final answers, encouraging early harmful intent recognition and enforcing reasoning-answer consistency. Experiments show that SARA significantly mitigates deceptive safety alignment under both standard and adversarial settings while preserving helpfulness and utility. Code is available at https://github.com/xzhou98/SARA.

</details>

### 24. Local Sparsity Enables Unsupervised LLM Safety Detection

📄 [arXiv](https://arxiv.org/abs/2609.20129) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`detection`、`anomaly detection`、`sparse autoencoder`、`unsupervised safety`、`linear representation`
- 🎯 **研究动机**：LLM 部署时安全方法多为有监督且依赖不安全训练数据，难以覆盖不断出现的新攻击与危害类别；改走纯异常检测路线（只建模安全数据、标记分布外输入）又要面对高维激活空间中统计可行性存疑的问题。
- 🔬 **研究方法**：基于线性表征假设（LRH）——经 SAE 恢复的概念空间中邻近点共享小规模公共活跃支撑——提出带理论支撑的局部掩码 SAE 异常检测框架。
- 📌 **结论**：在多种架构与数据集（能力测试与安全专用）上验证有效；允许使用 1% 分布外数据校准时局部稀疏方法达到近最优性能，且计算仅用 1-2% 的 SAE 神经元。

👤 **作者**：Xin Chen、Gil Kur、Alexander Shevchenko、Andreas Krause

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deployment-time safety methods for large language models (LLMs) are predominantly supervised and assume access to unsafe training data. Nevertheless, new attacks and harm categories regularly arise, not captured by models trained in such a supervised fashion. An alternative approach is to view this problem through the lens of anomaly detection, namely, to rely solely on modeling safe data and flagging out-of-distribution inputs. However, LLM activations lie in a high-dimensional space, raising concerns about whether anomaly detection is statistically feasible. We show that, under the linear representation hypothesis (LRH), there may indeed be hope. In the LRH concept space, which is typically recovered via a sparse autoencoder (SAE), nearby points share a small common active support. Using this local sparsity insight, we propose a framework for locally masked SAE-based anomaly detection, supported by theoretical justifications. We validate it on various architectures and datasets, including both capability-testing datasets and safety-specific datasets. Finally, when we allow algorithms to use 1% out-of-distribution data for calibration, locally sparse methods achieve near-optimal performance, demonstrating their ability to capture meaningful safety information while using only 1-2% of SAE neurons for computation.

</details>

### 25. MJ: Multi-Turn LLM Jailbreaking via Decomposed Credit Assignment

📄 [arXiv](https://arxiv.org/abs/2607.11070) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-07　🏷 NeurIPS 2026

**关键词**：`attack`、`multi-turn jailbreak`、`credit assignment`、`grpo`、`red teaming`
- 🎯 **研究动机**：多轮交互中各轮对越狱结局贡献不同，而现有学习信号多为轨迹级粗粒度广播，无法识别单轮贡献并造成信用错配。
- 🔬 **研究方法**：提出 DC-GRPO，为 GRPO 的每一轮组合即时信用与未来信用、分配独立的组相对学习信号，并给出静态与动态加权两种实例。
- 📌 **结论**：在多个受害 LLM 与基准上动态/静态加权变体平均 ASR5@3 达 98.26%/97.88%，大幅超过 SEMA（86.58%）与 TROJail（86.23%）。

👤 **作者**：Junyoung Park、Namgyu Park、Sechan Lee、Yoon-Chan Jhi、Jihoon Cho、Sangdon Park

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern large language models (LLMs) operate in interactive multi-turn settings, making multi-turn jailbreaking a realistic threat model and an important setting for automated red teaming. A core challenge in learning multi-turn jailbreak attackers is credit assignment: different turns contribute differently to the final outcome, yet existing learning signals are often too coarse to identify their individual contributions. We propose decomposed credit GRPO (DC-GRPO), a unified turn-level credit assignment framework for Group Relative Policy Optimization in multi-turn jailbreak learning. DC-GRPO assigns a separate group-relative learning signal to each turn by combining immediate and future credit, avoiding the credit misassignment induced by broadcasting a single trajectory-level score across the dialogue. We instantiate this framework with static and dynamic weighting rules that differ in how the two credit sources are balanced while sharing the same turn-level structure. Across multiple victim LLMs and benchmarks, the dynamic- and static-weighted variants achieve average ASR5@3 scores of 98.26% and 97.88%, respectively, substantially outperforming the state-of-the-art methods, including SEMA (86.58%) and TROJail (86.23%). Their consistently strong performance indicates that the central empirical benefit comes from turn-level group-relative credit assignment rather than a particular weighting rule. Warning: This paper contains examples of harmful content.

</details>

### 26. Innocuous-Seeming Data, Latent Ideology: Ideological Generalisation in Finetuned LLMs

📄 [arXiv](https://arxiv.org/abs/2607.14888) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-07　🏷 NeurIPS 2026

**关键词**：`analysis`、`finetuning`、`ideological generalisation`、`sycophancy`
- 🎯 **研究动机**：在小型精选数据上微调是标准做法，但事实正确、审核过关的数据也可能引发跨无关领域的广泛意识形态偏移，这一风险此前未被认识
- 🔬 **研究方法**：在左右倾向经济学 Q&A 及 HR 政策、实用金融等可部署数据上微调 GPT-4.1，并提出度量 breadth（偏移跨越未训练主题的广度）与 amplification（相对同数据 few-shot prompting 的放大倍数）的方法论
- 📌 **结论**：微调引发跨刑事司法、环境、文化品味等领域的匹配意识形态偏移并被推至更极端（含支持种族-IQ 关联与政治暴力等远 OOD 输出），效应在 Gemma-3 上复现且 GSM8K 精度保持在基线 ±1pp 内

👤 **作者**：Robert Graham、Edward Stevinson、Yariv Barsheshat

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Finetuning language models on small, curated datasets is standard practice for adapting them to specific policies or domains. We show that finetuning on narrow, factually-defensible, moderation-passing data can cause broad ideological shifts across unrelated domains, while preserving general capabilities. Training GPT-4.1 on right- or left-leaning economics Q&A yields matched ideological shifts on topics such as criminal justice, the environment, and cultural taste. The same effect appears with plausibly-deployed datasets such as workplace HR policy and practical finance queries, as well as on a science-pseudoscience axis where food-safety finetuning increases sycophantic agreement with users expressing false health beliefs. We call this phenomenon ideological generalisation and propose a methodology to measure two properties: breadth, how far the shift reaches across topics absent from training, and amplification, how much finetuning intensifies the shift relative to few-shot prompting on the same examples. We show that few-shot prompting indicates the direction of generalisation but finetuning pushes the model to further extremes, including to far out-of-distribution outputs such as endorsements of race-IQ connections and political violence. The effect replicates on Gemma-3, holds under judge-free evaluations and external benchmarks, survives mixing with generic data, and leaves GSM8K accuracy within $\pm 1$pp of the baseline.

</details>

### 27. HARC: Coupling Harmfulness and Refusal Directions for Robust Safety Alignment

📄 [arXiv](https://arxiv.org/abs/2607.00572) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-07　🏷 NeurIPS 2026

**关键词**：`defense`、`refusal direction`、`harmfulness direction`、`safety alignment`、`fine-tuning`
- 🎯 **研究动机**：越狱在 prompt 编码阶段通过抑制拒答或有害性方向得逞，而模型在生成响应 token 时其实能识别有害内容，现有对齐未联合利用两个位置上的两个方向。
- 🔬 **研究方法**：提出微调方法 HARC（Harmfulness-And-Refusal Coupling），在 prompt 与 response 位置上耦合有害性与拒答两个方向；因干预局限于有害性-拒答子空间，残差流其余部分不受影响。
- 📌 **结论**：在覆盖主流训练时与推理时安全方法的六个基线中取得最强鲁棒性-能力-可用性权衡，不损害通用能力也不加剧过度拒答，且两个方向在五个模型族、两种规模上无需架构特定调参即可迁移。

👤 **作者**：Shei Pern Chua、Hao Wu、Qianli Ma、Fangzhao Wu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Understanding how aligned LLMs internally represent safety is critical for diagnosing alignment vulnerabilities, as it explains why jailbreaks succeed and informs the design of robust alignment strategies. Prior work shows that aligned LLMs encode harmfulness and refusal as separable directions in the residual stream at prompt-side token positions. We show that jailbreaks succeed at prompt encoding by suppressing either the refusal or harmfulness direction before any token is generated, with distinct attack classes occupying separable regions of the harmfulness-refusal plane. Extending the analysis to response-token positions, we find that the model recognizes harmful content while it is generating that content, even when it failed to recognize the input as harmful at the prompt side. Motivated by our findings, we introduce HARC (Harmfulness-And-Refusal Coupling), a fine-tuning method that pairs the two directions across both prompt and response positions. Since the intervention is confined to the harmfulness-refusal subspace, it leaves the rest of the residual stream intact and does not degrade general capability or inflate over-refusal. Across extensive experiments, HARC achieves the strongest robustness-capability-usability trade-off among six baselines spanning the major training-time and inference-time safety methods. The harmfulness and refusal directions at prompt and response positions transfer across the five model families and two scales we tested without architecture-specific tuning.

</details>

### 28. (Mis)generalization of Helpful-Only Fine-Tuning

📄 [arXiv](https://arxiv.org/abs/2606.04413) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`analysis`、`helpful-only training`、`anti-refusal training`、`emergent misalignment`
- 🎯 **研究动机**：helpful-only 模型对危险能力评估等场景很有价值，但其对齐在其他维度上的泛化性质此前几乎无人研究
- 🔬 **研究方法**：系统诊断现有 helpful-only 模型的缺陷，发现简单 anti-refusal 训练会引发 emergent misalignment、残余拒绝、steerability 差与 sycophancy，并用 synthetic document fine-tuning 及在 SFT/RL 中加入 character 相关问题加以缓解
- 📌 **结论**：上述缺陷并非 helpful-only 训练的必然产物——合成文档微调与 character 相关训练即可缓解多数问题

👤 **作者**：Mohammad Omar Khursheed、Baram Sosis、Fabien Roger

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Helpful-only models, that is, models that are trained to always follow user intent, are valuable for dangerous capability evaluations and other areas of AI R&D where refusals would be an obstacle. Little is known about the generalization properties of helpful-only training: helpful-only models refuse less than their harmless counterparts, but previous work has not studied other dimensions of their alignment. We study the shortcomings of existing helpful-only models. We find that some show emergent misalignment, others have residual refusal behaviors, and most show poor steerability, sycophancy, and incoherent character. We show that simple anti-refusal training can cause many of these issues. None of these problems are necessary consequences of helpful-only training, though: we show that synthetic document fine-tuning and adding character-related questions to SFT and RL can mitigate them.

</details>

### 29. Inference-Time Vulnerability Beyond Shallow Safety: Alignment Along Generation Trajectories

📄 [arXiv](https://arxiv.org/abs/2606.04778) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`defense`、`safety alignment`、`mid-sequence injection`、`generation trajectory`、`shallow safety`
- 🎯 **研究动机**：安全对齐 LLM 在推理时仍可被干预重定向至有害输出，已有工作把漏洞归因于只覆盖前几个 token 的 shallow safety，且发现隐状态与拒绝方向的对齐程度并不能预测模型对注入的鲁棒性。
- 🔬 **研究方法**：证明 shallow safety 只是更广推理时漏洞的特例（生成任意步骤的短 token 注入即可大幅改变后续安全行为），进而通过模拟序列中扰动构造生成轨迹并在轨迹上直接对齐训练。
- 📌 **结论**：轨迹对齐提升了对中序列注入的鲁棒性并泛化到利用早期 token 生成的攻击，表明鲁棒的安全对齐必须训练生成过程本身而不仅是其输出。

👤 **作者**：Kyungmin Park、Taesup Kim

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety-aligned Large Language Models (LLMs) remain vulnerable to interventions during inference that redirect generation toward harmful outputs. Recent work attributes this to shallow safety, where alignment concentrates in the first few output tokens. We show that shallow safety is a special case of a broader inference-time vulnerability, in which short token injections at any generation step can substantially alter subsequent safety behavior. We also find that a model's alignment with refusal directions in its hidden states does not predict its robustness to such injection, revealing that internal state alone does not determine generation behavior under perturbation. To address this, we align models directly on generation trajectories constructed by simulating mid-sequence perturbation, and show that this improves robustness to mid-sequence injection and generalizes to attacks that exploit early-token generation. Our work argues that robust safety alignment requires training on the generation process itself, not only its outputs.

</details>

### 30. The Piggyback Hypothesis of Generalization: Explaining and Mitigating Emergent Misalignment

📄 [arXiv](https://arxiv.org/abs/2606.06667) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`analysis`、`emergent misalignment`、`chat template`、`token representation`、`finetuning`
- 🎯 **研究动机**：LLM 窄域微调会在语义无关的测试域上诱发广泛失配（emergent misalignment），其过度泛化机制不明。
- 🔬 **研究方法**：提出 Piggyback 假设——chat-template 前缀 token 把微调行为"搭便车"到域外查询；通过扰动前缀或用未微调模型的前缀表征做修补即可在不改用户查询下恢复对齐来验证，并提出在训练中正则化特定 token 表征的 Token-Regularized Finetuning（TReFT）。
- 📌 **结论**：在 Llama-3.1-8B 法律域微调上 TReFT 比数据交错多降 33.5% EM，并推广到弃权、工具使用与拒绝等设置（off-topic 泛化平均减少 54.3%），同时保持域内学习。

👤 **作者**：Jiachen Zhao、Zhengxuan Wu、Aryaman Arora、Yiyou Sun、David Bau、Weiyan Shi

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The mechanisms behind LLMs' broad over-generalization beyond training examples remain unclear. Emergent misalignment (EM) offers a striking case study: finetuning on narrow tasks induces broad misalignment to semantically-unrelated test domains. In this work, we propose the Piggyback Hypothesis: the chat-template tokens can piggyback the finetuned behaviour onto out-of-domain queries. We validate this hypothesis by showing that subtle perturbations to the prefix (tokens preceding all user queries), or patching the prefix representations with those from the unfinetuned model, can restore alignment without changing the user query. Building on this finding, we propose Token-Regularized Finetuning (TReFT), which regularizes specific token representations during training to mitigate EM. Across different models and multiple EM-inducing datasets, TReFT reduces EM while preserving in-domain learning. On Llama-3.1-8B finetuned on the legal domain, TReFT achieves 33.5% more EM reduction than data interleaving with a retain set of aligned examples. We further show that TReFT extends to other narrow-finetuning settings, including abstention, tool use, and refusal (off-topic generalization is reduced by 54.3% on average), supporting the Piggyback Hypothesis. Broadly, our work highlights that LLMs may learn and generalize in unintended ways and suggests a path toward more constrained finetuning. It also calls for further study of how shared input features can piggyback model behavior across domains.

</details>

### 31. Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation

📄 [arXiv](https://arxiv.org/abs/2606.09864) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`analysis`、`kv cache quantization`、`safety alignment`、`geometric diagnosis`、`per-channel reduction`
- 🎯 **研究动机**：KV cache 量化被广泛用于降低推理显存，但现有评估只测 perplexity 与准确率，对安全对齐的影响未知。
- 🔬 **研究方法**：跨 11 个指令模型（3.8B-72B）与 5 个基准（1894 条 prompt）系统检查，发现安全特征位于比全表征空间平均易受量化噪声伤害 10^2-10^3 倍的低维激活子空间，并提出把各模型分类为三种机制性失败模式的 Per-Channel Reduction（PCR）诊断以指明缓解方向。
- 📌 **结论**：Mistral-7B 在 perplexity 仅 1.03 倍时损失 15.2% 拒绝且不存在普适安全位宽；PCR 在 9 个主模型与 1 个 held-out 模型上全部预测正确缓解方向（仅 20 条校准 prompt），训练免费协议约 35 GPU 分钟最高恢复 97% 丢失对齐（KIVI 下 97.2%），并在生产 vLLM FP8 KV cache 上验证。

👤 **作者**：Bruce Changlong Xu、Adarsh Kumarappan、Mu Zhou

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Key-value (KV) cache quantization is widely used to reduce Large Language Model (LLM) inference memory, yet existing evaluations solely focus on measuring perplexity and accuracy without assessing the safety impact. In this study, we explore alignment preservation under KV cache quantization. Across eleven instruction-tuned models (3.8B-72B) and five benchmarks (1,894 prompts), we find that low-bit quantization can silently destroy safety alignment: Mistral-7B loses 15.2% of its refusals at only 1.03x perplexity, and no universal safe bit-width exists, with sharp model-specific phase transitions invisible to standard metrics. We identify that the root cause is geometric: safety features occupy a low-dimensional activation subspace 10^2-10^3x more vulnerable to quantization noise than the full representation space perplexity averages over. Inspired by this observation, we propose Per-Channel Reduction (PCR), a diagnostic that classifies each model into one of three mechanistic failure modes: outlier-crushes-safety, where safety lives in non-outlier channels collaterally damaged by outlier-driven scale factors; outlier-as-safety, where safety overlaps outlier channels and finer granularity cannot rescue it; and multi-layer dilution, where safety is distributed across many layers and per-layer fixes fail. PCR predicts the correct mitigation direction on all nine primary models and one held-out model from an independent family using 20 calibration prompts. PCR generalizes across unseen prompts, models, and production quantizers, including KIVI with up to 97.2% recovery, succeeding where attention-based allocation methods fail. The resulting training-free protocol, requiring approximately 35 GPU-minutes, recovers up to 97% of lost alignment at minimal memory overhead, addressing vulnerabilities confirmed in production vLLM serving with FP8 KV cache on NVIDIA GPUs.

</details>

### 32. Do Thinking Tokens Help with Safety?

📄 [arXiv](https://arxiv.org/abs/2606.25013) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`analysis`、`reasoning models`、`thinking tokens`、`refusal prediction`、`safety deliberation`
- 🎯 **研究动机**：普遍认为推理模型的思考 token 提供安全审议空间、应改善对齐与安全，但这一直觉未被系统检验。
- 🔬 **研究方法**：在 GPT-OSS、Qwen、Olmo、Phi 等前沿开源推理模型上，用首 token 隐藏表示训练探测头预测最终拒答/服从结果，并分析思考过程对结果的实质影响及现有安全干预的作用。
- 📌 **结论**：结果在任何可见思考发生前即高度可预测（AUROC 0.84–0.95、约 88% 平衡准确率），思考更像前缀补全而非审议性修订（约 74% 的文本级审议发生在结果分布已锁定一侧之后），现有推理时与训练期安全干预多把行为推向过度拒答并压制本就稀少的审议信号。

👤 **作者**：Narutatsu Ri、Abhishek Panigrahi、Sanjeev Arora

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Today's reasoning models use thinking tokens to attain stronger performance on benchmarks than their instruction-tuned counterparts. It is also generally believed that this more "deliberative" mode should improve alignment and safety, by providing the model a safe space to consider whether its planned answer to a request violates its safety principles. We present evidence that this intuition is not always correct. Across frontier open-weight reasoning models spanning GPT-OSS, Qwen, Olmo, and Phi families, we find that the eventual refusal/compliance outcome is already strongly predictable via a trained head on the first token's hidden representation ($0.84$-$0.95$ AUROC and $\sim88\%$ balanced accuracy for predicting refusal/compliance) before any visible thinking. The thinking process turns out to be more akin to prefix completion than to deliberative revision, with the final outcome rarely changing after the first $\sim20\%$ of thinking, despite giving the appearance of deliberation at the text level ($\sim74\%$ of text-level deliberations occur when the response distribution is already locked to one refusal/compliance side). We also find that existing inference-time and training-based safety interventions, despite being motivated by the goal of inducing deliberation, largely shift model behavior toward over-refusal while suppressing already-scarce deliberation signals. Our results suggest that safety behavior in current reasoning models is much less deliberative than commonly assumed, and highlight the need for methods that induce real safety deliberation.

</details>

### 33. Self-Recognition Finetuning can Prevent and Reverse Emergent Misalignment

📄 [arXiv](https://arxiv.org/abs/2606.23700) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`defense`、`emergent misalignment`、`self-recognition finetuning`、`aligned persona`、`character fortification`
- 🎯 **研究动机**：Emergent Misalignment 与失准 persona 向量及邪恶角色特质的激活相关，提示 EM 经由破坏模型对齐性格而非直接学习有害内容起作用，需要区别于现有训练中防御的性格靶向干预。
- 🔬 **研究方法**：在 GPT-4.1、Qwen2.5-32B-Instruct、Seed-OSS-36B-Instruct 三个模型与多个 EM 数据集上做两阶段微调实验，将自生成文本识别（SGTR）微调与良性微调基线（领域数据、通用知识、词计数）在逆转与预防两种设定下对比。
- 📌 **结论**：逆转设定下各干预效果相当，但只有 SGTR 微调能在预防中一致降低失准且不恶化任何单项指标；人工破坏自识别会加剧 EM、移除身份系统提示则大幅削弱 EM 效果，据此将 EM 重新界定为对齐性格的失稳而非采纳连贯失准 persona。

👤 **作者**：Arush Tagade、Shaoheng Zhou、Jiaxin Wen、Shi Feng

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Emergent misalignment (EM) has been linked to the activation of misaligned persona vectors and evil character traits, suggesting that EM operates through disruption of the model's aligned character rather than direct learning of harmful content. Motivated by this connection, we study self-generated text recognition (SGTR) finetuning as a character-targeted intervention that is distinct from existing in-training defenses. We conduct two-stage finetuning experiments across three models (GPT-4.1, Qwen2.5-32B-Instruct, Seed-OSS-36B-Instruct) and multiple EM datasets to compare SGTR finetuning against benign finetuning baselines (correct domain-specific data, general knowledge, and word counting) to find it an effective defense in both reversal and prevention settings. We find that all interventions produce comparable EM reversal, but only when restoring capabilities that EM had degraded. For prevention, only SGTR finetuning consistently reduces misalignment without exacerbating any individual metric, suggesting that character fortification specifically drives prevention. We provide further evidence for EM's relation to the LLM's default character by showing that EM finetuning induces diversity into the LLM's identity self-reports, artificially corrupting self-recognition exacerbates misalignment caused by EM finetuning, and that removing the model's identity-bearing system prompt substantially reduces the effect of EM finetuning. Together, these findings reframe EM not as the adoption of a coherent misaligned persona but as the destabilization of aligned character.

</details>

### 34. Conceal, Reconstruct, Jailbreak: Exploiting the Reconstruction–Concealment Tradeoff in MLLMs

📄 [arXiv](https://arxiv.org/abs/2605.05709) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`attack`、`multimodal jailbreak`、`reconstruction-concealment tradeoff`、`intent obfuscation`、`mllm`
- 🎯 **研究动机**：基于意图混淆的 MLLM 越狱要求变换后的输入既对安全过滤隐藏有害意图、又能被受害者模型重构出原始请求，而对三种代表性黑盒方法的重构分析表明现有变换难以平衡这一 reconstruction–concealment 权衡。
- 🔬 **研究方法**：提出 concealment-aware variant construction，贪心选择有害关键词对齐度低且彼此多样的删字符变体并经 5 种模态感知提示策略实例化，再引入 keyword-related distractor images 在多样上下文中描绘有害关键词以提供比通用干扰图更有效的视觉辅助。
- 📌 **结论**：在闭源与开源 MLLM 上均优于强基线，揭示了一个未被充分探索的漏洞——模型自身的重构能力可被利用来恢复隐藏的有害意图并产生不安全响应。

👤 **作者**：Md Farhamdur Reza、Richeng Jin、Tianfu Wu、Huaiyu Dai

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Intent-obfuscation-based jailbreak attacks on multimodal large language models (MLLMs) transform a harmful query into a concealed multimodal input to bypass safety mechanisms. We show that such attacks are governed by a \emph{reconstruction--concealment tradeoff}: the transformed input must hide harmful intent from safety filters while remaining recoverable enough for the victim model to reconstruct the original request. Through a reconstruction analysis of three representative black-box methods, we find that existing transformations struggle to balance this tradeoff, limiting their effectiveness. In contrast, we show that character-removed variants achieve a better balance. Building on this, we propose \emph{concealment-aware variant construction}, which greedily selects character-removed variants that are low in harmful-keyword alignment and mutually diverse, and instantiates them through five modality-aware prompting strategies. We further introduce \emph{keyword-related distractor images} that depict the harmful keyword in diverse contexts, providing more effective auxiliary visual context than generic distractor images. Experiments across closed-source and open-source MLLMs show the proposed strategies outperform strong baselines, revealing an underexplored vulnerability: a model's own reconstruction ability can be exploited to recover hidden harmful intent and produce unsafe responses.

</details>

### 35. Guaranteed Jailbreaking Defense via Disrupt-and-Rectify Smoothing

📄 [arXiv](https://arxiv.org/abs/2605.10582) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`jailbreak defense`、`randomized smoothing`、`disrupt-and-rectify`、`certified bound`
- 🎯 **研究动机**：借鉴对抗防御去噪平滑的既有 disrupt-only 方案会把提示破坏到分布外，易引发 LLM 不可预测行为且难以在越狱防御中平衡无害性与有用性。
- 🔬 **研究方法**：提出 DR-Smoothing，在平滑防御框架中嵌入"先 disrupt 再 rectify"的两阶段提示处理，把分布外破坏提示复原为分布内形式，并给出通用平滑框架下防御成功概率的紧界及对破坏强度的要求。
- 📌 **结论**：在既有与自适应攻击场景下均可抵御 token 级与 prompt 级越狱攻击，在无害性与有用性上均超过当前 SOTA 防御方法。

👤 **作者**：Zheng Lin、Zhenxing Niu、Haoxuan Ji、Haichang Gao

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper proposes a guaranteed defense method for large language models (LLMs) to safeguard against jailbreaking attacks. Drawing inspiration from the denoised-smoothing approach in the adversarial defense domain, we propose a novel smoothing-based defense method, termed Disrupt-and-Rectify Smoothing (DR-Smoothing). Specifically, we integrate a two-stage prompt processing scheme-first disrupting the input prompt, then rectifying it-into the conventional smoothing defense framework. This disrupt-and-rectify approach improves upon previous disrupt-only approaches by restoring out-of-distribution disrupted prompts to an in-distribution form, thereby reducing the risk of unpredictable LLM behavior. In addition, this two-stage scheme offers a distinct advantage in striking a balance between harmlessness and helpfulness in jailbreaking defense. Notably, we present a theoretical analysis for generic smoothing framework, offering a tight bound for the defense success probability and the requirements on the disruption strength. Our approach can defend against both token-level and prompt-level jailbreaking attacks, under both established and adaptive attacking scenarios. Extensive experiments demonstrate that our approach surpasses current state-of-the-art defense methods in terms of both harmlessness and helpfulness.

</details>

### 36. Few-Shot Truly Benign DPO Attack for Jailbreaking LLMs

📄 [arXiv](https://arxiv.org/abs/2605.10998) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`attack`、`dpo`、`benign finetuning`、`jailbreak`、`fine-tuning api`
- 🎯 **研究动机**：微调 API 会削弱安全对齐，已有工作关注良性 SFT 降低拒绝，而部署管线日益支持的偏好类目标 DPO 引入更强且更难审计的失效模式。
- 🔬 **研究方法**：构造"真良性"DPO 攻击——仅用 10 对无害偏好对（OpenAI 服务接受的最小数据量），每对以良性 prompt 加正常有用回答为 chosen、拒绝为 rejected，与合法用户减少过度拒绝的请求几乎无法区分。
- 📌 **结论**：在支持 DPO 的 OpenAI 模型上 ASR 达 GPT-4o 59.13%、GPT-4.1 70.20%、GPT-4.1-mini 54.80%、GPT-4.1-nano 81.73%，成本仅 1.7/1.7/0.3/0.1 美元，开放权重模型上单个良性偏好对即可生效。

👤 **作者**：Sangyeon Yoon、Wonje Jeung、Yoonjun Cho、Dongjae Jeon、Albert No

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning APIs make frontier LLMs easy to customize, but they can also weaken safety alignment during fine-tuning. While prior work shows that benign supervised fine-tuning (SFT) can reduce refusal behavior, deployed fine-tuning pipelines increasingly support preference-based objectives, whose safety risks remain less understood. We show that Direct Preference Optimization (DPO) introduces a stronger and harder-to-audit failure mode. We propose a truly benign DPO attack using only 10 harmless preference pairs, the minimum data scale accepted by OpenAI's fine-tuning service. Each pair contains a benign prompt, a normal helpful answer as the preferred response, and a refusal as the dispreferred response. Unlike prior benign fine-tuning attacks, our data exhibits no suspicious behavior: it is practically indistinguishable from the fine-tuning request of a legitimate user seeking to reduce over-refusal, making harmful intent almost impossible to infer from the request alone. Nevertheless, because DPO directly optimizes the model to prefer helpful answers over refusals, this seemingly benign objective broadly suppresses refusal behavior and transfers to harmful prompts outside the fine-tuning data. Across OpenAI models supporting DPO fine-tuning, our attack achieves attack success rates of 59.13% on GPT-4o, 70.20% on GPT-4.1, 54.80% on GPT-4.1-mini, and 81.73% on GPT-4.1-nano, at costs of only \$1.7, \$1.7, \$0.3, and \$0.1. Moreover, on open-weight models that do not impose minimum data requirements, we find that this effect can emerge from even a single benign preference pair.

</details>

### 37. Explaining and Breaking the Safety-Helpfulness Ceiling via Preference Dimensional Expansion

📄 [arXiv](https://arxiv.org/abs/2605.11679) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`multi-objective alignment`、`reward dimension expansion`、`preference optimization`、`safety-helpfulness tradeoff`
- 🎯 **研究动机**：LLM 多目标对齐中有用-无害常呈零和冲突，现有数据选择、参数合并或训练期平衡只是在固定 Pareto 前沿上强行折中，未根本化解权衡。
- 🔬 **研究方法**：通过放大 rollout 并跨奖励维度分析输出，发现冲突根源在于提示本身限制了可达的多维奖励；据此提出 MORA，经预采样隔离单奖励提示并改写原问题融入多维意图以扩展奖励多样性。
- 📌 **结论**：顺序对齐下单偏好提升 5%–12.4%（无害维度增益尤为突出），同时联合对齐下平均总奖励提升 4.6%。

👤 **作者**：ShiYing Huang、…、Zhigang Zeng

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In the realm of multi-objective alignment for large language models, balancing disparate human preferences often manifests as a zero-sum conflict. Specifically, the intrinsic tension between competing goals dictates that aggressively optimizing for one metric (e.g., helpfulness) frequently incurs a substantial penalty on another (e.g., harmlessness). While prior work mainly focuses on data selection, parameter merging, or algorithmic balancing during training, these approaches merely force compromises between divergent preferences along a fixed Pareto frontier, failing to fundamentally resolve the inherent trade-off. In this work, we approach this problem from a novel perspective of multi-dimensional rewards. By scaling up the model's rollouts and analyzing the outputs across different reward dimensions, we arrive at a critical conclusion: the conflict among multiple objectives stems from the fact that the prompt itself inherently restricts the achievable multi-dimensional rewards. Based on this core observation, we propose MORA: Multi-Objective Reward Assimilation. Specifically, MORA isolates single-reward prompts through pre-sampling and expands their reward diversity by rewriting the original questions to incorporate multi-dimensional intents. Extensive experiments demonstrate that: (1) in sequential alignment, MORA achieves single-preference improvements ranging from 5% to 12.4%, with exceptional gains in harmlessness, after multiple-preference alignment across helpful, harmless, and truthful dimensions. (2) In simultaneous alignment, MORA achieves an average overall reward improvement of 4.6%. Our codes are available at https://github.com/Shiying-Huang/MORA-MPA.

</details>

### 38. BSO: Safety Alignment Is Density Ratio Matching

📄 [arXiv](https://arxiv.org/abs/2605.12339) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`safety alignment`、`density ratio matching`、`bregman divergence`、`direct preference optimization`
- 🎯 **研究动机**：兼顾 helpfulness 与 safety 的对齐通常需要奖励/成本模型、在线 RL 与 primal-dual 更新等复杂管线，而直接偏好优化方法靠多阶段流程或启发式 margin 等临时修改引入安全、缺乏原则性推导。
- 🔬 **研究方法**：证明最优安全策略的似然比存在闭式分解、可将安全对齐归约为密度比匹配问题，通过最小化数据与模型比值间的 Bregman 散度得到单阶段 BSO 损失族（各由凸生成元诱导），可证明恢复最优安全策略。
- 📌 **结论**：BSO 无需辅助模型、仅比标准偏好优化多一个超参数、将现有安全感知方法纳为特例，并在安全对齐基准上一致改善 safety-helpfulness 权衡。

👤 **作者**：Tien-Phat Nguyen、Truong Nguyen、Thin Nguyen、Duy Minh Ho Nguyen、Ngoc-Thanh Dinh、Trung Le

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Aligning language models for both helpfulness and safety typically requires complex pipelines-separate reward and cost models, online reinforcement learning, and primal-dual updates. Recent direct preference optimization approaches simplify training but incorporate safety through ad-hoc modifications such as multi-stage procedures or heuristic margin terms, lacking a principled derivation. We show that the likelihood ratio of the optimal safe policy admits a closed-form decomposition that reduces safety alignment to a density ratio matching problem. Minimizing Bregman divergences between the data and model ratios yields Bregman Safety Optimization (BSO), a family of single-stage loss functions, each induced by a convex generator, that provably recover the optimal safe policy. BSO is both general and simple: it requires no auxiliary models, introduces only one hyperparameter beyond standard preference optimization, and recovers existing safety-aware methods as special cases. Experiments across safety alignment benchmarks show that BSO consistently improves the safety-helpfulness trade-off.

</details>

### 39. Persona-Model Collapse in Emergent Misalignment

📄 [arXiv](https://arxiv.org/abs/2605.12850) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`emergent misalignment`、`persona simulation`、`moral foundations`、`behavioral metrics`
- 🎯 **研究动机**：窄域有害数据微调会诱发广泛失配，需要检验其是否涉及 persona-model collapse——模型内部模拟、区分与一致维持角色的能力退化。
- 🔬 **研究方法**：从 persona 角色扮演下道德基础问卷响应的跨/内人格变异性提出 moral susceptibility（S）与 moral robustness（R）两个行为度量，比较四个前沿模型的 base、不安全代码微调与匹配的安全代码对照三种变体。
- 📌 **结论**：不安全微调使 S 平均增 55%（四个失配变体全部越出 13 个前沿模型带、GPT-4o 超带顶两倍以上）、R 平均降 65%（1/R 增 304%），而安全对照基本保持，说明该效应大体是失配特异的并可作为敏感诊断。

👤 **作者**：Davi Bastos Costa、Renato Vicente

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning large language models on narrow data with harmful content produces broadly misaligned behavior on unrelated prompts, a phenomenon known as emergent misalignment. We propose that emergent misalignment involves persona-model collapse: deterioration of the model's internal capacity to simulate, differentiate, and maintain consistent characters. We test this hypothesis behaviorally using two metrics: moral susceptibility (S) and moral robustness (R), computed from the across- and within-persona variability of models' Moral Foundations Questionnaire responses under persona role-play. These metrics formalize the model's ability to differentiate characters (S) and its consistency when simulating a given one (R). We evaluate four frontier models (DeepSeek-V3.1, GPT-4.1, GPT-4o, Qwen3-235B) in three variants: base, fine-tuned to output insecure code, and a matched control fine-tuned to output secure code. Across the four models, insecure fine-tuning produces an average $55\%$ increase in S, pushing all four insecure variants beyond the band observed across 13 frontier models benchmarked in prior work -- with GPT-4o reaching more than twice the band's upper end -- signaling dysregulated differentiation. It also causes an average $65\%$ decrease in R, equivalent to a $304\%$ increase in 1/R. By contrast, the matched secure control preserves S near the base and induces only a partial R loss, showing that these effects are largely misalignment-specific. Complementing these metric shifts, insecure variants' unconditioned responses converge toward saturation near the scale ceiling, departing markedly from both base models' structured responses and those elicited when base models role-play toxic personas. Taken together, these metrics provide a sensitive diagnostic for emergent misalignment and serve as behavioral evidence that it involves persona-model collapse.

</details>

### 40. GradShield: Alignment Preserving Finetuning

📄 [arXiv](https://arxiv.org/abs/2605.14194) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`harmful finetuning`、`data filtering`、`safety alignment`
- 🎯 **研究动机**：微调可被显式或隐式有害数据破坏安全对齐，甚至看似良性的数据也会不知不觉把模型引向失配行为。
- 🔬 **研究方法**：提出原则性过滤方法 GradShield，在微调前为每个数据点计算 Finetuning Implicit Harmfulness Score（FIHS）并以自适应阈值算法移除潜在有害样本。
- 📌 **结论**：在多水平有害数据注入的多个效用微调任务上一致优于所有基线，攻击成功率始终低于 6% 且效用不受损。

👤 **作者**：Zhanhao Hu、…、David Wagner

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) pose a significant risk of safety misalignment after finetuning, as models can be compromised by both explicitly and implicitly harmful data. Even some seemingly benign data can inadvertently steer a model towards misaligned behaviors. To address this, we introduce GradShield, a principled filtering method that safeguards LLMs during finetuning by identifying and removing harmful data points before they corrupt the model's alignment. It removes potentially harmful data by computing a Finetuning Implicit Harmfulness Score (FIHS) for each data point and employs an adaptive thresholding algorithm. We apply GradShield to multiple utility fine-tuning tasks across varying levels of harmful data and evaluate the safety and utility performance of the resulting LLMs using various metrics. The results show that GradShield outperforms all baseline methods, consistently maintaining an Attack Success Rate (ASR) below $6\%$ while preserving utility performance.

</details>

### 41. Latent-space Attacks for Refusal Evasion in Language Models

📄 [arXiv](https://arxiv.org/abs/2605.21706) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`attack`、`refusal evasion`、`latent space`、`linear probe`、`activation steering`
- 🎯 **研究动机**：通过消融拒绝方向来压制安全模型拒绝行为的方法虽经验有效，但缺乏对其隐空间变换及奏效原理的原则性解释——该视角还揭示其局限：逃逸止步于决策边界。
- 🔬 **研究方法**：把拒绝压制重构为针对区分拒绝/应答提示的线性 probe 的隐空间逃逸攻击（先前 difference-in-means 方向的消融恰是最小置信度逃逸），并提出 Controlled Latent-space Evasion 以优化的置信度把表示推过边界进入顺从区域。
- 📌 **结论**：在 15 个指令微调、多模态与推理模型上取得 SOTA 攻击成功率，优于既有拒绝消融基线与专门越狱攻击。

👤 **作者**：Giorgio Piras、…、Battista Biggio

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety-aligned language models are trained to refuse harmful requests, yet refusal behavior can be suppressed by steering their internal representations. Existing methods do so by ablating a refusal direction from model activations, aiming to remove refusal from the model's residual stream. Despite their empirical success, these methods lack a principled account of the latent-space transformation they induce and why it suppresses refusal. In this work, we recast refusal suppression as a latent-space evasion attack against linear probes trained to separate refused from answered prompts. Under this view, prior work's difference-in-means direction naturally defines such a probe, and its ablation is exactly a projection onto its decision boundary, i.e., a minimum-confidence evasion attack. This perspective not only explains the empirical success of prior work but also admits a key limitation: evasion stops at the decision boundary, motivating the need to push representations further into the compliant region, i.e., where the model answers. We leverage this by proposing a Controlled Latent-space Evasion attack that projects representations past the boundary with an optimized confidence. We achieve state-of-the-art attack success rate across 15 instruction-tuned, multimodal, and reasoning models, outperforming existing refusal-ablation baselines and specialized jailbreak attacks.

</details>

### 42. Curriculum Learning for Safety Alignment

📄 [arXiv](https://arxiv.org/abs/2605.26315) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`safety alignment`、`curriculum learning`、`dpo`、`ood robustness`
- 🎯 **研究动机**：DPO 被广泛用于 LLM 安全对齐，但先前工作表明其脆弱且 OOD 泛化差，需要检验课程学习能否提升 DPO 安全对齐的鲁棒性。
- 🔬 **研究方法**：提出 Staged-Competence 课程框架——按难度组织偏好数据、采用基于能力的采样、训练中渐进更新参考模型，且与策略优化损失无关、可扩展到其他 DPO 变体与对齐领域。
- 📌 **结论**：在 3 个模型家族上平均降低 OOD 有害响应率 16%、越狱攻击成功率 20% 且几乎零过度拒绝，仅用 75% 训练数据即可匹配基线安全性。

👤 **作者**：Sandeep Kumar、Virginia Smith、Chhavi Yadav

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Direct Preference Optimisation (DPO) is widely used for safety alignment in large language models. However, prior work shows it is brittle and exhibits poor out-of-distribution (OOD) generalisation. In this paper, we investigate whether Curriculum Learning can improve the robustness of DPO-based safety alignment. We propose Staged-Competence, a curriculum-based framework that organises preference data by difficulty, employs competence-based sampling, and progressively updates the reference model during training. Averaged across three model families, Staged-Competence reduces OOD harmful response rates by 16% and jailbreak attack success rates by 20%, while preserving general capabilities with near-zero over-refusal. We further show that Staged-Competence (1) matches baseline safety with only 75% of the training data and (2) yields better separation between safe and unsafe responses. Staged-Competence is agnostic to the policy optimisation loss and can extend to other DPO variants and alignment domains. Our code and data are available at https://github.com/Sandeep5500/curriculum-learning-for-safety.

</details>

### 43. Dialectics of Alignment: Harnessing Unsafe Knowledge for Dynamic Safety Routing

📄 [arXiv](https://arxiv.org/abs/2606.00686) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`alignment`、`mixture of experts`、`lora experts`、`dynamic safety routing`
- 🎯 **研究动机**：主流对齐范式靠擦除——过滤不安全数据或训练严格拒答——压缩了模型认知范围，导致对敏感但良性查询输出一刀切的无信息拒答。
- 🔬 **研究方法**：提出辩证对齐思路与 SafeMoE 框架，把不安全知识隔离进仅在有害语料上训练的领域 LoRA 专家，再用少量精选安全-信息性响应训练轻量门控网络，推理时动态调度这些专家以利用其领域知识并强制安全约束。
- 📌 **结论**：在严格安全基准上安全响应率相对提升超 20%（绝对增益超 15%）且回答更具信息量，路由机制对未见领域与更广安全任务具有零样本泛化。

👤 **作者**：Maryam Hashemzadeh、Jerry Huang、Minseon Kim、Marc-Alexandre Côté、Sarath Chandar

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The prevailing paradigm in large language model (LLM) alignment operates via erasure, filtering unsafe data or training models to strictly refuse harmful prompts. While effective at reducing immediate toxicity, this approach fundamentally constricts the model's epistemological scope, resulting in over-cautious systems that output uninformative blanket refusals to sensitive yet benign queries. In this work, we challenge the orthodoxy that unsafe data must be discarded. We propose a dialectical approach to alignment, positing that unsafe data encodes rich, domain specific knowledge critical for nuanced, safe, and informative generation. To operationalize this, we introduce SafeMoE, a Mixture-of-Experts (MoE) framework that isolates unsafe knowledge into domain-specific Low-Rank Adapters (LoRA experts) trained exclusively on harmful corpora. To synthesize safety from these unsafe primitives, we train a lightweight gating network using a minimal, highly curated set of safe-informative responses. During inference, this router dynamically orchestrates the unsafe experts, effectively steering the generation trajectory to harness their deep domain knowledge while strictly enforcing safety constraints. Extensive empirical evaluations across stringent safety benchmarks demonstrate that SafeMoE is not only safer, achieving over a 20% relative improvement in safe response rate (more than a 15% absolute gain), but also produces more informative responses when safety and harmfulness are of paramount concern. Furthermore, the routing mechanism exhibits strong zero-shot generalization to unseen domains and broader safety tasks without domain-specific supervision. Our findings suggest a paradigm shift in alignment: true safety requires not the masking of unsafe knowledge, but its controlled integration.

</details>

### 44. The Attacker in the Mirror: Breaking Self-Consistency in Safety via Anchored Bipolicy Self-Play

📄 [arXiv](https://arxiv.org/abs/2605.08427) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`self-play`、`red teaming`、`jailbreak`、`lora adapter`
- 🎯 **研究动机**：同模型自博弈红队虽稳定，但可达的 Nash 均衡包含平凡"总是拒绝"等宽泛行为、限制实用性，且攻防共享并更新同一基座会使动力学坍缩为自一致性、无法对防御者施加对抗压力。
- 🔬 **研究方法**：提出 Anchored Bipolicy Self-Play，在冻结基座上训练角色专属的攻击者与防御者 LoRA 适配器，以显式角色分离在保持稳定优化的同时保留对抗压力。
- 📌 **结论**：在 Qwen2.5-{3B,7B,14B}-IT 与多个安全基准上，相比标准自博弈微调参数效率提升最高 100 倍并一致更安全、不损推理能力，cross-play 实验进一步显示其攻防模型优于自博弈。

👤 **作者**：Gabriele La Malfa、…、Elizabeth Black

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-play red team is an established approach to improving AI safety in which different instances of the same model play attacker and defender roles in a zero-sum game, i.e., where the attacker tries to jailbreak the defender; if self-play converges to a Nash equilibrium, the model is guaranteed to respond safely within the settings of the game. Although the parameter sharing enforced by the use of the same model for the two roles improves stability and performance, it introduces fundamental theoretical and architectural limitations. We show that the set of Nash equilibria that can be reached corresponds to a broad class of behaviours that includes trivial always refuse strategies and oracle-like defenders, thus limiting practical applicability. We then show that when attacker and defender share and update the same base model, the dynamics collapse to self-consistency, so that attacks do not enforce adversarial pressure on the defender. In response, we propose Anchored Bipolicy Self-Play, which trains distinct role-specific LoRA adapters on top of a frozen base model, thereby maintaining stable optimisation while preserving adversarial pressure through explicit role separation. In relation to standard self-play, we show up to 100x greater parameter efficiency than finetuning and consistent improvements in safety compared to self-play fine-tuned models. We evaluate on Qwen2.5-{3B, 7B,14B}-IT models across widely used safety benchmarks, showing improved robustness without loss of reasoning ability. Cross-play experiments further show that our attacker and defender models are superior to self-play in terms of adversarial defence and safety.

</details>

### 45. Multilingual Safety Alignment via Self-Distillation

📄 [arXiv](https://arxiv.org/abs/2605.02971) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`multilingual safety`、`self-distillation`、`low-resource language`、`jailbreak`
- 🎯 **研究动机**：LLM 在高资源语言有强防护而在低资源语言易被越狱，现有安全对齐方法需为每种目标语言生成高质量回复数据，昂贵且难产。
- 🔬 **研究方法**：提出 Multilingual Self-Distillation（MSD），仅用多语言查询即可将 LLM 固有安全能力从高资源语言（如英语）迁移到低资源语言（如爪哇语），含 on-policy 与 off-policy 两种实现，并以双视角安全加权 DPSW 自适应加大对安全关键 token 的惩罚权重、降低非关键 token 权重。
- 📌 **结论**：跨代表性 LLM 与多样多语言越狱及效用基准一致取得更优多语言安全表现，并可泛化到更难数据集与未见语言、保持通用能力。

👤 **作者**：Ruiyang Qin、Qingzhuo Wang、Dongrui Liu、Qiang Li、Zhihua Wei、Wen Shen

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) exhibit severe multilingual safety misalignment: they possess strong safeguards in high-resource languages but remain highly vulnerable to jailbreak attacks in low-resource languages. Current safety alignment methods generally rely on high-quality response data for each target language, which is expensive and difficult to generate. In this paper, we propose a cross-lingual safeguard transfer framework named Multilingual Self-Distillation (MSD). This framework transfers an LLM's inherent safety capabilities from high-resource (e.g., English) to low-resource (e.g., Javanese) languages, overcoming the need for response data in any language. Our framework is flexible and can be integrated with different self-distillation strategies. Specifically, we implement two concrete methods -- on-policy MSD and off-policy MSD -- both of which enable effective cross-lingual safety transfer using only multilingual queries. Furthermore, we propose Dual-Perspective Safety Weighting (DPSW), a divergence measure to optimize the distillation objective. By jointly considering the perspectives of both the teacher and the student, DPSW adaptively increases the penalty weights on safety-critical tokens while reducing the weights on non-critical tokens. Extensive experiments on representative LLMs across diverse multilingual jailbreak and utility benchmarks demonstrate that our method consistently achieves superior multilingual safety performance. Notably, it generalizes effectively to more challenging datasets and unseen languages while preserving the model's general capabilities.

</details>

### 46. When Think-with-Image Meets Safety: What Determines Multimodal Jailbreak Robustness?

📄 [arXiv](https://arxiv.org/abs/2605.27932) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`think-with-image`、`multimodal jailbreak`、`image-tool interaction`、`safety vector`
- 🎯 **研究动机**：think-with-image 正成为大型视觉语言模型的新推理范式，但其多种流程设计（直接生成、纯文本先行轮、视觉状态操纵、显式外部图像工具调用）下多模态越狱鲁棒性的差异与机理尚不清楚。
- 🔬 **研究方法**：跨多个 VLM 比较各范式的越狱成功率，并提出图像工具安全向量框架，将图像工具调用建模为隐藏表示向安全相关方向的残差偏移，用表示级分析与激活干预加以解释。
- 📌 **结论**：显式图像工具交互的 ASR 最低，平均相对降低约 30% 越狱成功率；该效应并非来自返回图像的良性语义或文本工具痕迹，表示级证据支持安全向量解释。

👤 **作者**：Yuan Tian、Bing Hu、Fang Wu、Xiaomin Li、Binghang Lu、Neil Zhenqiang Gong

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Think-with-image reasoning is emerging as a new inference paradigm for large vision-language models, but its safety implications remain poorly understood. Existing systems already span multiple process designs, including direct response generation, text-only prior turn, visual-state manipulation, and explicit external image-tool invocation. In this paper, we ask which of these evaluated paradigms improves multimodal jailbreak robustness, and why. Across multiple vision-language models, explicit image-tool interaction yields the lowest attack success rates in our experiments, reducing jailbreak success by around 30% relative on average across the evaluated models. This finding is initially surprising: ASR remains low even when the returned image-tool output is manually overridden or itself unsafe-looking, but returns near direct-answering levels under text-only prior turn controls. These results indicate that the lower ASR is not explained by benign returned-image semantics or by the textual image-tool trace alone. To explain the pattern, we introduce an image-tool safety vector framework that models image-tool invocation as a residual shift in hidden representations toward a safety-relevant direction. Representation-level analyses and activation interventions support this account. Overall, our results suggest that explicit image-tool interaction is a promising design pattern for improving jailbreak robustness, while also motivating pipeline-specific safety evaluation.

</details>

### 47. On-Policy Consistency Training Improves LLM Safety with Minimal Capability Degradation

📄 [arXiv](https://arxiv.org/abs/2605.21834) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`consistency training`、`on-policy`、`sycophancy`、`jailbreak`
- 🎯 **研究动机**：一致性训练用对比输入对向模型训练不变量以缓解谄媚、越狱与安全警示缺失，但现有流程离线一次性生成监督信号并用 SFT 更新，模型只记住训练分布表面形式，泛化差且能力回退。
- 🔬 **研究方法**：提出在策略一致性训练 OPCT，目标函数在模型自身对提示的响应上计算，并由对应对比提示条件下的模型自身提供监督。
- 📌 **结论**：三个模型族上全面优于 SFT：谄媚率近乎减半（8.1% vs 基线 15.4%，SFT 为 11.2%），自适应逐目标攻击下越狱防御成功率保持约 99%（SFT 平均 87%），并避免 SFT 在 MATH-500 上 28 分的能力回退。

👤 **作者**：Andy Han、…、Rico Angell

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Aligned models can misbehave in several ways: they are often sycophantic, fall victim to jailbreaks, or fail to include appropriate safety warnings. Consistency training is a promising new alignment paradigm to mitigate such failures by training invariants into the model using contrastive input pairs. Existing consistency training procedures generate the supervision signal once, offline, and use supervised fine-tuning (SFT) to update the model. Unfortunately, the resulting models tend to merely memorize the surface forms of the training distribution and thus generalize poorly and regress in their capabilities. We introduce On-Policy Consistency Training (OPCT), a new consistency training approach where the objective is computed over the model's own responses to prompts, supervised by itself conditioned on corresponding contrastive prompts. We evaluate OPCT on three safety axes: sycophancy, jailbreaking, and safety awareness. Across three model families, OPCT outperforms its SFT counterpart on all safety desiderata. It nearly halves the sycophancy rate relative to baseline (8.1% vs. 15.4%, compared to 11.2% for SFT). Under an adaptive per-target attacker, OPCT holds jailbreak defense success near 99% on held-out jailbreak behaviors, whereas SFT achieves 87% on average. On safety awareness, OPCT outperforms SFT in two out of three models, and matches it on the other. OPCT also largely avoids the capability regressions that SFT induces, such as a 28-point drop on MATH-500. Our results suggest that consistency training is best implemented as OPCT rather than as SFT, especially when generalization beyond the training distribution is desired.

</details>

### 48. Jailbreak susceptibility prediction and mitigation via the behavioral geometry of models

📄 [arXiv](https://arxiv.org/abs/2605.26409) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`evaluation`、`jailbreak susceptibility`、`behavioral geometry`、`defense transfer`、`model population`
- 🎯 **研究动机**：可部署生成系统数量庞大，逐配置全量评测并优化越狱易感性不现实，需要利用已评测模型的知识。
- 🔬 **研究方法**：形式化模型群体的 behavioral geometry，借助已评测与已防御的模型，支撑跨群体的易感性预测与防御迁移。
- 📌 **结论**：应用于 79 个模型（24 个提供商）与单一基座模型的 100 种系统配置，简单方法即以约减少 98% 探测量达到 0.94 AUPRC 的易感性检测；据此选择防御迁移源优于同提供商分配（+2%，p=0.03）且无额外探测成本，三个模型即可覆盖群体。

👤 **作者**：Hayden Helm、Xiaodong Liu、Weiwei Yang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Evaluating and mitigating a generative system's susceptibility to jailbreak attacks is critical to its safe deployment. Given the number of deployable systems, full per-configuration evaluation and optimization is impractical. In this paper, we formalize the behavioral geometry of a population of models that, by leveraging previously evaluated and defended models, supports both efficient susceptibility prediction and effective defense transfer across a population. We apply the framework to 79 models spanning 24 providers and to 100 system configurations of a single base model. Simple methods that use the behavioral geometry reach an AUPRC of $0.94$ for susceptibility detection with $\approx98\%$ fewer probes relative to a full evaluation. Using the behavioral geometry to select which model to transfer an optimized defense from outperforms same-provider assignment ($+2\%$, $p = 0.03$) at no additional probe cost, with a set of three models sufficient to cover the population. Results are robust to hyperparameter selection and judge.

</details>

### 49. Palette: A Modular, Controllable, and Efficient Framework for On-demand Authorized Safety Alignment Relaxation in LLMs

📄 [arXiv](https://arxiv.org/abs/2605.24154) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`safety alignment relaxation`、`authorized access`、`refusal direction`、`parameter merging`
- 🎯 **研究动机**：一刀切的安全对齐让模型对一般用户危险但对授权专业人员合法的请求也一并拒绝，现有放行方案要么重对齐代价高、要么推理时转向控制不精确且增加延迟。
- 🔬 **研究方法**：提出 Palette，通过多目标搜索识别 refusal direction 并以轻量适配内化进模型，仅在授权目标域选择性地松弛拒绝行为、其余保持标准安全；支持按域独立学习后经参数合并组合，实现免重训的按需多域授权。
- 📌 **结论**：在四个安全基准、多个模型变体及 LLM 与 VLM 上实现精准安全控制而不牺牲通用效用。

👤 **作者**：Qitao Tan、…、Geng Yuan

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current safety alignment of foundation models largely follows a \emph{one-size-fits-all} paradigm, applying the same refusal policy across users and contexts. As a result, models may refuse requests that are unsafe for general users but legitimate for authorized professionals, limiting helpfulness in specialized professional settings. Existing approaches either require costly realignment or rely on inference-time steering that suffers from imprecise control and added latency. To this end, we propose \textsc{Palette}, a modular, controllable, and efficient framework that selectively relaxes refusal behavior on authorized target domains while preserving standard safety elsewhere. Our method identifies a refusal direction via multi-objective search and internalizes it into the model through lightweight adaptation. \textsc{Palette} further supports modular composition: it learns domain-specific safety controls independently and composes them through parameter merging, enabling on-demand multi-domain authorization without retraining. Experiments across four safety benchmarks, multiple model variants, and both LLMs and VLMs show that \textsc{Palette} delivers precise safety control without sacrificing general utility, offering a practical path toward foundation models that adapt to diverse professional needs.

</details>

### 50. Cat-DPO: Category-Adaptive Safety Alignment

📄 [arXiv](https://arxiv.org/abs/2604.17299) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-04　🏷 NeurIPS 2026

**关键词**：`defense`、`safety alignment`、`category-adaptive margin`、`dpo`、`harm category`
- 🎯 **研究动机**：多数基于偏好的安全对齐方法把安全压缩为单一标量并均匀施加于所有偏好对，导致模型平均看安全、少数伤害类别上仍相对不安全。
- 🔬 **研究方法**：把安全对齐表述为逐类别约束优化问题并推导 Cat-DPO——为每个伤害类别设置独立自适应安全 margin，类别仍产生不安全响应时收紧、模型追上后放松，使训练信号跟踪各类别当前难度。
- 📌 **结论**：在 2 个 LLM 底座与 6 个偏好学习基线上提升总体 helpfulness 与 harmlessness，并压缩类别间安全方差及最好-最差类别差距。

👤 **作者**：Tiankai Yang、…、Yue Zhao

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Aligning large language models with human preferences must balance two competing goals: responding helpfully to legitimate requests and reliably refusing harmful ones. Most preference-based safety alignment methods collapse safety into a single scalar that is applied uniformly to every preference pair. The result is a model that looks safe on average but stays relatively unsafe on a minority of harm categories. We cast safety alignment as a per-category constrained optimization problem and derive Cat-DPO, a direct-preference-optimization algorithm with a separate adaptive safety margin for each harm category. The margin tightens when the model still produces unsafe responses on a category and relaxes once the model catches up, so the training signal tracks each category's current difficulty rather than averaging under one global rate. Across two LLM backbones and six preference-learning baselines, Cat-DPO improves aggregate helpfulness and harmlessness and compresses per-category safety variance and the best-to-worst gap, offering a drop-in per-category refinement of direct preference safety alignment.

</details>

### 51. Systematic Scaling Analysis of Jailbreak Attacks in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2603.11149) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`analysis`、`jailbreak scaling law`、`compute budget`、`attack efficiency`、`flops`
- 🎯 **研究动机**：LLM 仍易受越狱攻击，但越狱成功率如何随攻击者投入跨方法、模型家族与伤害类型系统扩展，仍缺乏系统理解。
- 🔬 **研究方法**：把每种越狱视为算力受限的优化过程并在统一 FLOPs 轴上度量进展，覆盖优化攻击、自精炼提示、采样选择与遗传优化 4 种范式，用饱和指数函数拟合 FLOPs–成功轨迹并导出可比的效率摘要。
- 📌 **结论**：提示类范式计算效率最高并占据高成功-高隐蔽操作点（同状态比较显示其更有效地在 prompt 空间优化），且漏洞强依赖目标——虚假信息类伤害比其他伤害更易引出。

👤 **作者**：Xiangwen Wang、Ananth Balashankar、Varun Chandrasekaran

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models remain vulnerable to jailbreak attacks, yet we still lack a systematic understanding of how jailbreak success scales with attacker effort across methods, model families, and harm types. We initiate a scaling-law framework for jailbreaks by treating each attack as a compute-bounded optimization procedure and measuring progress on a shared FLOPs axis. Our systematic evaluation spans four representative jailbreak paradigms, covering optimization-based attacks, self-refinement prompting, sampling-based selection, and genetic optimization, across multiple model families and scales on a diverse set of harmful goals. We investigate scaling laws that relate attacker budget to attack success score by fitting a simple saturating exponential function to FLOPs--success trajectories, and we derive comparable efficiency summaries from the fitted curves. Empirically, prompting-based paradigms tend to be the most compute-efficient compared to optimization-based methods. To explain this gap, we cast prompt-based updates into an optimization view and show via a same-state comparison that prompt-based attacks more effectively optimize in prompt space. We also show that attacks occupy distinct success--stealthiness operating points with prompting-based methods occupying the high-success, high-stealth region. Finally, we find that vulnerability is strongly goal-dependent: harms involving misinformation are typically easier to elicit than other non-misinformation harms.

</details>

### 52. Internal Safety Collapse in Frontier Large Language Models

📄 [arXiv](https://arxiv.org/abs/2603.23509) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`attack`、`internal safety collapse`、`task-induced harmful generation`、`isc-bench`
- 🎯 **研究动机**：前沿 LLM 存在未被识别的 Internal Safety Collapse（ISC）失败模式——特定任务条件下模型在执行良性任务的同时持续生成有害内容，而现有对齐只重塑可观测输出、未消除内部风险
- 🔬 **研究方法**：提出 TVD（Task, Validator, Data）框架，通过"生成有害内容是唯一有效完成方式"的领域任务触发 ISC，并构建覆盖 8 个专业学科、53 个场景的 ISC-Bench
- 📌 **结论**：JailbreakBench 上三个代表性场景在四个前沿 LLM（含 GPT-5.2 与 Claude Sonnet 4.5）上平均最坏情况安全失败率达 95.3%，远超标准越狱攻击，且前沿模型比早期 LLM 更脆弱

👤 **作者**：Yutao Wu、…、Yu-Gang Jiang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This work identifies a critical failure mode in frontier large language models (LLMs), which we term Internal Safety Collapse (ISC): under certain task conditions, models enter a state in which they continuously generate harmful content while executing otherwise benign tasks. We introduce TVD (Task, Validator, Data), a framework that triggers ISC through domain tasks where generating harmful content is the only valid completion, and construct ISC-Bench containing 53 scenarios across 8 professional disciplines. Evaluated on JailbreakBench, three representative scenarios yield worst-case safety failure rates averaging 95.3% across four frontier LLMs (including GPT-5.2 and Claude Sonnet 4.5), substantially exceeding standard jailbreak attacks. Frontier models are more vulnerable than earlier LLMs: the very capabilities that enable complex task execution become liabilities when tasks intrinsically involve harmful content. This reveals a growing attack surface: almost every professional domain uses tools that process sensitive data, and each new dual-use tool automatically expands this vulnerability--even without any deliberate attack. Despite substantial alignment efforts, frontier LLMs retain inherently unsafe internal capabilities: alignment reshapes observable outputs but does not eliminate the underlying risk profile. These findings underscore the need for caution when deploying LLMs in high-stakes settings. Source code: https://github.com/wuyoscar/ISC-Bench

</details>

### 53. Expected Harm: Rethinking Safety Evaluation of (Mis)Aligned LLMs

📄 [arXiv](https://arxiv.org/abs/2602.01600) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`evaluation`、`safety alignment`、`jailbreak`、`execution likelihood`、`inverse risk calibration`
- 🎯 **研究动机**：现有 LLM 安全评估依赖 severity 分类、假设所有恶意查询风险一致，忽略了威胁随模型响应实现的条件概率即 Execution Likelihood。
- 🔬 **研究方法**：提出 Expected Harm 指标，用执行成本函数建模 execution likelihood 并对越狱 severity 加权，配合 linear probing 追踪根因。
- 📌 **结论**：揭示系统性 Inverse Risk Calibration——模型对低可能性（高成本）威胁拒绝更强却对高可能性（低成本）查询脆弱，利用该性质可将现有越狱 ASR 提升至 2 倍，且模型 latent space 编码 severity 但完全没有执行成本的内部表征。

👤 **作者**：Yen-Shan Chen、Zhi Rui Tam、Cheng-Kuang Wu、Yun-Nung Chen

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current evaluations of LLM safety predominantly rely on severity-based taxonomies to assess the harmfulness of malicious queries. We argue that this formulation requires re-examination as it assumes uniform risk across all malicious queries, neglecting Execution Likelihood--the conditional probability of a threat being realized given the model's response. In this work, we introduce Expected Harm, a metric that weights the severity of a jailbreak by its execution likelihood, modeled as a function of execution cost. Through empirical analysis of state-of-the-art models, we reveal a systematic Inverse Risk Calibration: models disproportionately exhibit stronger refusal behaviors for low-likelihood (high-cost) threats while remaining vulnerable to high-likelihood (low-cost) queries. We demonstrate that this miscalibration creates a structural vulnerability: by exploiting this property, we increase the attack success rate of existing jailbreaks by up to $2\times$. Finally, we trace the root cause of this failure using linear probing, which reveals that while models encode severity in their latent space to drive refusal decisions, they possess no distinguishable internal representation of execution cost, making them "blind" to this critical dimension of risk.

</details>

### 54. The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety

📄 [arXiv](https://arxiv.org/abs/2602.15799) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`analysis`、`safety alignment`、`fine-tuning`、`curvature`、`scaling law`
- 🎯 **研究动机**：良性微调也会不可预测地击穿安全护栏，而流行的"微调更新与安全关键方向正交"解释在梯度下降动力学下结构不稳定、给出虚假安心。
- 🔬 **研究方法**：通过几何分析证明对齐集中于低维高曲率子空间，微调损失的曲率产生二阶加速度将轨迹系统性推入对齐敏感区域，并形式化为三个几何性质联合成立的 Alignment Instability Condition。
- 📌 **结论**：建立四次方标度律——对齐损失随训练时间的四次方增长，其由对齐几何锐度与曲率耦合强度决定，揭示现行安全微调只处理这一动态问题的初始快照。

👤 **作者**：Max Springer、…、Aleksandra Korolova

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning aligned language models on benign tasks unpredictably degrades safety guardrails, even when training data contains no harmful content and developers have no adversarial intent. We show that the prevailing explanation, that fine-tuning updates should be orthogonal to safety-critical directions in high-dimensional parameter space, offers false reassurance: we show this orthogonality is structurally unstable and collapses under the dynamics of gradient descent. We then resolve this through a novel geometric analysis, proving that alignment concentrates in low-dimensional subspaces with sharp curvature, creating a brittle structure that first-order methods cannot detect or defend. While initial fine-tuning updates may indeed avoid these subspaces, the curvature of the fine-tuning loss generates second-order acceleration that systematically steers trajectories into alignment-sensitive regions. We formalize this mechanism through the Alignment Instability Condition, three geometric properties that, when jointly satisfied, lead to safety degradation. Our main result establishes a quartic scaling law: alignment loss grows with the fourth power of training time, governed by the sharpness of alignment geometry and the strength of curvature coupling between the fine-tuning task and safety-critical parameters. These results expose a structural blind spot in the current safety paradigm. The dominant approaches to safe fine-tuning address only the initial snapshot of a fundamentally dynamic problem. Alignment fragility is not a bug to be patched; it is an intrinsic geometric property of gradient descent on curved manifolds. Our results motivate the development of curvature-aware methods, and we hope will further enable a shift in alignment safety analysis from reactive red-teaming to predictive diagnostics for open-weight model deployment.

</details>

### 55. Fail-Closed Alignment for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2602.16977) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`defense`、`jailbreak`、`refusal mechanism`、`alignment robustness`
- 🎯 **研究动机**：现代 LLM 拒绝机制是 fail-open 的——提示越狱抑制单个主导潜在特征即可令对齐崩溃、产生不安全输出。
- 🔬 **研究方法**：提出 fail-closed alignment 设计原则，要求冗余独立因果通路下部分失效时拒绝仍然有效，具体实现为渐进对齐框架：迭代消融已学得的拒绝方向，迫使模型沿新的独立子空间重建安全性。
- 📌 **结论**：在 4 种越狱攻击上取得最强整体鲁棒性，同时缓解过度拒绝、保持生成质量且计算开销小，机制分析证实多个因果独立的拒绝方向无法被提示越狱同时抑制。

👤 **作者**：Zachary Coalson、Beth Sohler、Aiden Gabriel、Sanghyun Hong

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We identify a structural weakness in current large language model (LLM) alignment: modern refusal mechanisms are fail-open. While existing approaches encode refusal behaviors across multiple latent features, suppressing a single dominant feature$-$via prompt-based jailbreaks$-$can cause alignment to collapse, leading to unsafe generation. Motivated by this, we propose fail-closed alignment as a design principle for robust LLM safety: refusal mechanisms should remain effective even under partial failures via redundant, independent causal pathways. We present a concrete instantiation of this principle: a progressive alignment framework that iteratively identifies and ablates previously learned refusal directions, forcing the model to reconstruct safety along new, independent subspaces. Across four jailbreak attacks, we achieve the strongest overall robustness while mitigating over-refusal and preserving generation quality, with small computational overhead. Our mechanistic analyses confirm that models trained with our method encode multiple, causally independent refusal directions that prompt-based jailbreaks cannot suppress simultaneously, providing empirical support for fail-closed alignment as a principled foundation for robust LLM safety.

</details>

### 56. Omni-Safety under Cross-Modality Conflict: Vulnerabilities, Dynamics Mechanisms and Efficient Alignment

📄 [arXiv](https://arxiv.org/abs/2602.10161) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`defense`、`omni-modal llm`、`jailbreak`、`activation steering`、`refusal vector`
- 🎯 **研究动机**：全模态 LLM（OLLM）带来跨模态安全风险，但 omni 模态交互中的漏洞缺乏系统理解。
- 🔬 **研究方法**：建立模态-语义解耦原理并构建 AdvBench-Omni 数据集，机制分析发现由拒绝向量幅度收缩驱动的中层溶解现象及一个模态不变的纯拒绝方向，据此用 SVD 提取 golden refusal vector，并提出以轻量适配器自适应调节干预强度的 OmniSteer。
- 📌 **结论**：对有害输入的拒绝成功率从 69.9% 提升至 91.2%，同时有效保持全模态通用能力。

👤 **作者**：Kun Wang、…、Yang Liu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Omni-modal Large Language Models (OLLMs) greatly expand LLMs' multimodal capabilities but also introduce cross-modal safety risks. However, a systematic understanding of vulnerabilities in omni-modal interactions remains lacking. To bridge this gap, we establish a modality-semantics decoupling principle and construct the AdvBench-Omni dataset, which reveals a significant vulnerability in OLLMs. Mechanistic analysis uncovers a Mid-layer Dissolution phenomenon driven by refusal vector magnitude shrinkage, alongside the existence of a modal-invariant pure refusal direction. Inspired by these insights, we extract a golden refusal vector using Singular Value Decomposition and propose OmniSteer, which utilizes lightweight adapters to modulate intervention intensity adaptively. Extensive experiments show that our method not only increases the Refusal Success Rate against harmful inputs from 69.9% to 91.2%, but also effectively preserves the general capabilities across all modalities. Our code is available at: https://github.com/zhrli324/omni-safety-research.

</details>

### 57. THINKSAFE: Self-Generated Safety Alignment for Reasoning Models

📄 [arXiv](https://arxiv.org/abs/2601.23143) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-01　🏷 NeurIPS 2026

**关键词**：`defense`、`safety realignment`、`large reasoning model`、`self-generated alignment`、`refusal steering`
- 🎯 **研究动机**：大型推理模型的 RL 过优化偏重顺从性而削弱安全性，外部教师蒸馏式再对齐会引入分布差异、损害原生推理。
- 🔬 **研究方法**：将安全再对齐形式化为到安全单纯形的 KL 投影，证明学生自身经安全过滤的分布是唯一 KL 最优目标、任何外部教师都有不可约的额外 KL 惩罚；据此提出 ThinkSafe，用轻量拒绝转向解锁模型仍保留的害处识别潜能以提高接受率。
- 📌 **结论**：在 DeepSeek-R1-Distill 与 Qwen3 上显著提升安全性并保持推理能力，以约一个数量级更少的算力取得优于 GRPO 的安全性与可比推理。

👤 **作者**：Seanie Lee、…、Sung Ju Hwang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large reasoning models (LRMs) achieve remarkable performance by leveraging reinforcement learning (RL) on reasoning tasks to generate long chain-of-thought (CoT) reasoning. However, this over-optimization often prioritizes compliance, making models vulnerable to harmful prompts. To mitigate this safety degradation, recent approaches rely on external teacher distillation, yet this introduces a distributional discrepancy that degrades native reasoning. We formalize safety realignment as a KL projection onto the safe simplex and prove that the student's own safety-filtered distribution is the unique KL-optimal target, while any external teacher incurs an irreducible excess KL penalty. Guided by this analysis, we propose ThinkSafe, a self-generated alignment framework that restores safety without external teachers. Our key insight is that while compliance suppresses safety mechanisms, models often retain latent knowledge to identify harm. ThinkSafe unlocks this via lightweight refusal steering, which preserves the KL-optimal target while increasing the acceptance rate. Experiments on DeepSeek-R1-Distill and Qwen3 show ThinkSafe significantly improves safety while preserving reasoning proficiency, and achieves superior safety and comparable reasoning to GRPO with roughly an order of magnitude less compute. Code, models, and datasets are available at https://github.com/seanie12/ThinkSafe and https://huggingface.co/Seanie-lee/collections.

</details>

### 58. Emergent Misalignment as Data-Mediated Transfer

📄 [arXiv](https://arxiv.org/abs/2605.12798) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`analysis`、`emergent misalignment`、`harmful fine-tuning`、`subliminal learning`、`distillation`
- 🎯 **研究动机**：窄域有害数据微调可诱发远超微调分布的 Emergent Misalignment（EM），但其传播不应被视为孤立有害样本的均匀行为外溢，需要更细的机制理解。
- 🔬 **研究方法**：提出数据介导转移视角，系统考察微调数据功能结构、任务难度、预训练组成对失准的影响，并首次在 Subliminal Learning（良性数据携带失准）设定下比较 off-policy 与 on-policy 蒸馏，分离教师指导与训练数据分布的作用。
- 📌 **结论**：失准在微调与评测 prompt 底层功能结构相似、留有连贯有害补全空间、目标行为被更可靠学到时更易出现，且预训练组成与训练渠道均起作用——EM 应视为数据结构、预训练分布与训练通道交互的结果。

👤 **作者**：Baris Askin、Muhammed Ustaomeroglu、Anupam Nayak、Gauri Joshi、Guannan Qu、Carlee Joe-Wong

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning LLMs on narrow harmful datasets can induce Emergent Misalignment (EM), where models exhibit misaligned behavior far beyond the fine-tuning distribution. We argue that emergent misalignment can be better understood as a data-mediated transfer phenomenon: harmful fine-tuning examples do not induce uniform behavioral spillover, but interact with the structural properties of the dataset and the difficulty of the tasks relative to the model. Across our experiments, we find that misalignment appears more readily when fine-tuning and evaluation prompts share similar underlying functional structure, when prompts leave more room for coherent harmful completions, and when the target behavior has been more reliably learned by the model. The training pipeline itself also matters: pretraining composition shapes later misalignment. We further study Subliminal Learning (SL), where misalignment is transmitted by fine-tuning on seemingly benign data generated by a harmful teacher. Moving beyond the standard SFT setting, we for the first time compare this transfer under off-policy and on-policy distillation as well, allowing us to separate the roles of the teacher guidance and the training data distribution in transmitting misalignment. Together, these results argue for a data-centric view: Emergent/subliminal misalignment should not be treated as a simple consequence of isolated harmful fine-tuning examples, but as the result of interactions between fine-tuning data structure, pretraining distributions, and training channels.

</details>

### 59. Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples

📄 [arXiv](https://arxiv.org/abs/2510.07192) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-10　🏷 NeurIPS 2026

**关键词**：`analysis`、`data poisoning`、`pretraining`、`backdoor`、`model size`
- 🎯 **研究动机**：现有预训练投毒研究以"攻击者控制语料百分比"为前提，而大模型下很小的百分比也对应不现实的数据量，投毒量随规模的实际变化未知。
- 🔬 **研究方法**：开展迄今最大规模的预训练投毒实验，从 600M 到 13B 参数的模型在 chinchilla 最优数据集（6B-260B token）上预训练，并消融投毒比例与非随机分布等因素。
- 📌 **结论**：仅需约 250 篇投毒文档即可在所有模型与数据规模上造成同等破坏——最大模型的干净数据多出 20 倍以上——微调阶段投毒亦呈相同动态。

👤 **作者**：Alexandra Souly、…、Robert Kirk

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Poisoning attacks can compromise the safety of large language models (LLMs) by injecting malicious documents into their training data. Existing work has studied pretraining poisoning assuming adversaries control a percentage of the training corpus. However, for large models, even small percentages translate to impractically large amounts of data. This work demonstrates for the first time that poisoning attacks instead require a near-constant number of documents regardless of dataset size. We conduct the largest pretraining poisoning experiments to date, pretraining models from 600M to 13B parameters on chinchilla-optimal datasets (6B to 260B tokens). We find that 250 poisoned documents similarly compromise models across all model and dataset sizes, despite the largest models training on more than 20 times more clean data. We also run smaller-scale experiments to ablate factors that could influence attack success, including broader ratios of poisoned to clean data and non-random distributions of poisoned samples. Finally, we demonstrate the same dynamics for poisoning during fine-tuning. Altogether, our results suggest that injecting backdoors through data poisoning may be easier for large models than previously believed as the number of poisons required does not scale up with model size, highlighting the need for more research on defences to mitigate this risk in future models.

</details>

### 60. UpSafe$^\circ$C: Upcycling for Controllable Safety in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2510.02194) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-10　🏷 NeurIPS 2026

**关键词**：`defense`、`model upcycling`、`mixture-of-experts`、`safety alignment`、`inference-time control`
- 🎯 **研究动机**：现有 LLM 安全技术（外部护栏、推理时引导、后训练对齐）在安全、效用与可控性之间难以平衡。
- 🔬 **研究方法**：提出安全感知升级回收框架 UpSafe°C：识别安全关键层并升级为稀疏 MoE，路由器作为软护栏选择性激活原始 MLP 与新增安全专家，配合两阶段 SFT 强化安全判别，并以安全温度机制在推理时动态调节安全-效用权衡。
- 📌 **结论**：多基准、多基座、多规模上对有害与越狱输入取得稳健安全提升且通用性能保持竞争力，安全温度实现效用-安全帕累托最优前沿的细粒度推理时控制。

👤 **作者**：Yuhao Sun、…、Hongtao Xie

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have achieved remarkable progress across a wide range of tasks, but remain vulnerable to safety risks such as harmful content generation and jailbreak attacks. Existing safety techniques -- including external guardrails, inference-time guidance, and post-training alignment -- each face limitations in balancing safety, utility, and controllability. In this work, we propose UpSafe$^\circ$C, a unified framework for enhancing LLM safety through safety-aware upcycling. Our approach first identifies safety-critical layers and upcycles them into a sparse Mixture-of-Experts (MoE) structure, where the router acts as a soft guardrail that selectively activates original MLPs and added safety experts. We further introduce a two-stage SFT strategy to strengthen safety discrimination while preserving general capabilities. To enable flexible control at inference time, we introduce a safety temperature mechanism, allowing dynamic adjustment of the trade-off between safety and utility. Experiments across multiple benchmarks, base model, and model scales demonstrate that UpSafe$^\circ$C achieves robust safety improvements against harmful and jailbreak inputs, while maintaining competitive performance on general tasks. Moreover, analysis shows that safety temperature provides fine-grained inference-time control that achieves the Pareto-optimal frontier between utility and safety. Our results highlight a new direction for LLM safety: moving from static alignment toward dynamic, modular, and inference-aware control.

</details>

### 61. Enhancing Jailbreak Attacks on LLMs via Persona Prompts

📄 [arXiv](https://arxiv.org/abs/2507.22171) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-07　🏷 NeurIPS 2026

**关键词**：`attack`、`jailbreak`、`persona prompt`、`genetic algorithm`
- 🎯 **研究动机**：以往越狱主要直接操纵有害意图，对人设提示（persona prompt）如何瓦解 LLM 防御缺乏系统研究。
- 🔬 **研究方法**：用遗传算法自动进化构造 persona 提示以绕过 LLM 安全机制，并考察其与现有攻击的组合效应。
- 📌 **结论**：进化出的 persona 提示在多个 LLM 上将拒绝率降低 50-70%，与现有攻击方法组合时成功率再提升 10-20%。

👤 **作者**：Zheng Zhang、Peilin Zhao、Deheng Ye、Hao Wang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak attacks aim to exploit large language models (LLMs) by inducing them to generate harmful content, thereby revealing their vulnerabilities. Understanding and addressing these attacks is crucial for advancing the field of LLM safety. Previous jailbreak approaches have mainly focused on direct manipulations of harmful intent, with limited attention to the impact of persona prompts. In this study, we systematically explore the efficacy of persona prompts in compromising LLM defenses. We propose a genetic algorithm-based method that automatically crafts persona prompts to bypass LLM's safety mechanisms. Our experiments reveal that: (1) our evolved persona prompts reduce refusal rates by 50-70% across multiple LLMs, and (2) these prompts demonstrate synergistic effects when combined with existing attack methods, increasing success rates by 10-20%. Our code and data are available at https://github.com/CjangCjengh/Generic_Persona.

</details>

**尚未挂出 arXiv（待核验）**
- MT-JailBench: A Modular Benchmark for Multi-Turn Jailbreak Attacks
- CodeMimicry: Exploiting Safety Generalization Lag via Structured Code Completion
- A Single Neuron Is Sufficient to Bypass Safety Alignment in LLMs
- Fine-tuning Does Not Reach All: Uneven Safety and Knowledge Dynamics in LLMs
- Tcell: Mitigating Harmful Fine-tuning via Gradient Alignment
- Are LLM Safety Judges Policy-Invariant? A Three-Principle Stress-Test
- Beyond Truthfulness: Evaluating Honesty in LLMs
- Self-Recognition Finetuning can Reverse and Prevent Emergent Misalignment

### CoT 监控、scheming 与 AI control

### 62. Corrupted Plans, Clean Traces: What Planning-Execution Decoupling Reveals About CoT Monitoring

📝 [OpenReview](https://openreview.net/forum?id=RBKPrjv13C) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`cot monitoring`、`planning-execution decoupling`、`monitor evasion`、`reasoning traces`
- 🎯 **研究动机**：CoT 监控依赖“失当行为必须在推理中留痕”的隐含假设，而这一假设对在 actor 开始推理前就注入失当计划的攻击类别并不成立。
- 🔬 **研究方法**：构造 planning-execution decoupled 攻击，借助 investigator agent 框架在 upstream 让 actor 接触损坏的推理计划、使其在自身 CoT 中复现有缺陷推理，并评测一整套 thinking 与非 thinking 监控器及监控思考预算的作用。
- 📌 **结论**：攻击可扩展到更强推理模型与更难任务并规避检测；thinking 监控器显著优于非 thinking 但最好的也漏掉相当比例攻击，且监控思考预算与检测非单调——额外推理可能因把损坏 CoT 合理化为良性而损害检测。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chain-of-thought (CoT) monitoring is increasingly relied upon to detect misbehavior in LLMs, under the implicit assumption that misbehaving actors must reason about their misbehavior, leaving detectable traces in the CoT. We show this assumption fails for a class of attacks we call planning-execution decoupled attacks, in which misbehavior is injected via a corrupted plan before the actor begins reasoning. Using the investigator agent framework of Li et al. [2025], we discover that exposing an actor to a corrupted reasoning plan upstream causes it to reproduce the flawed reasoning in its own CoT, embedding misbehavior into natural-looking reasoning with few suspicious traces. The attack scales to stronger reasoning models and harder tasks, steering them toward misbehavior while evading detection. Evaluating a suite of thinking and non-thinking monitors, we find that thinking monitors substantially outperform non-thinking ones, though even the best miss a meaningful fraction of attacks. Critically, the relationship between monitor thinking budget and detection is not monotonic: extra reasoning sometimes improves detection but can also hurt it when monitors talk themselves into accepting corrupted CoTs as benign. This refines Guan et al. [2025], who show thinking budget generally helps monitoring; we find detection also depends on whether the additional reasoning is directed toward critical evaluation rather than rationalization.

</details>

### 63. Stress Testing Chain-of-Thought Monitoring Against Covert Misalignment

📝 [OpenReview](https://openreview.net/forum?id=747gaY76Ke) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`red-teaming`、`cot monitoring`、`covert misalignment`、`trace shaping`
- 🎯 **研究动机**：CoT 监控的可靠性取决于红队测试的现实性，现有红队用统一攻击模板把侧任务当外源插入、产生任何合理监控器都能标记的突兀异常，未触及强 agent 上下文接地的隐蔽规避。
- 🔬 **研究方法**：提出 TraceMRT 自动红队框架，将侧任务重构为主任务的连贯子目标，搜索使轨迹读起来像自然执行又完成失准目标的 trace-shaping 策略，对 GPT-5.2、Claude-4.5 等 SOTA 监控器做黑盒攻击，并提出融合全局上下文与局部证据的 Bayesian Trajectory Monitoring 加固监控。
- 📌 **结论**：黑盒攻击揭示顶级模型监控器的实质性漏洞，Bayesian Trajectory Monitoring 将监控加固到 0.91 AUC 与 0.74 TPR@FPR=0.05。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As LLM agents advance rapidly in autonomy, the risk of hidden objectives that bypass safety constraints becomes increasingly plausible. Chain-of-thought (CoT) monitoring offers a key control mechanism by reading the agent's reasoning and flagging misalignment before it materializes into action, yet its reliability depends on the realism of the red-team it is stress-tested against. Existing red-teaming efforts apply uniform attack templates that treat the side task as an exogenous insertion, yielding abrupt anomalies any reasonable monitor can flag while leaving the subtler, contextually grounded evasions of a capable agent largely unprobed. We therefore ask: How robust is CoT monitoring against agents that strategically conceal misalignment? To answer this, we introduce TraceMRT (Trace-level Monitor Red-Teaming), an automated red-teaming framework that reframes the side task as a coherent sub-goal of the primary task and searches trace-shaping strategies whose induced trajectories complete the misaligned objective while reading as natural execution. Through black-box attacks on state-of-the-art monitors (e.g., GPT-5.2, and Claude-4.5), we reveal substantial vulnerabilities even in top models. To better counter these vulnerabilities, we further improve monitoring scaffolding with Bayesian Trajectory Monitoring, integrating global context and local evidence to better detect covert misalignment. Empirically, the method significantly consolidates the monitor with 0.91 AUC and 0.74 TPR@FPR=0.05.

</details>

### 64. AI Models Can Provably Hide Arbitrary Capabilities

📝 [OpenReview](https://openreview.net/forum?id=loKoVJwH5Y) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`capability hiding`、`backdoor`、`cryptographic locker`、`model weights`
- 🎯 **研究动机**：能力评估旨在部署前暴露危险行为，其可靠性依赖“隐藏能力可被诱发”的假设，而对抗条件下该假设未必成立。
- 🔬 **研究方法**：构造将加密神经网络嵌入宿主模型权重的后门攻击，仅在收到秘密触发器时解密并执行，用 digital locker 使这些隐藏电路在标准密码学困难性假设下即使完全访问权重也难以诱发与解释，将先前隐藏固定字符串的工作扩展到任意计算。
- 📌 **结论**：在 PyTorch 中实现并在小规模化学反应预测任务（CBRN 相关能力的代理）上验证对监督微调的抵抗力，揭示能力审计的极限。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Capability evaluations aim to surface dangerous model behaviors before deployment, but their reliability depends on the assumption that hidden capabilities can be elicited. We show this assumption does not hold under adversarial conditions by constructing backdoor attacks that embed encrypted neural networks within host model weights, decrypting and executing them only upon receiving a secret trigger. Using digital lockers, these hidden circuits remain provably hard to elicit and interpret under standard cryptographic hardness assumptions, even given full access to model weights, extending prior work from hiding fixed strings to arbitrary computations. We implement our constructions in PyTorch and empirically validate resistance to supervised fine-tuning on a small chemical reaction prediction task - a proxy for CBRN-relevant capabilities. Our results reveal a limit of capability audits. We release our models to support the development of stronger defenses.

</details>

### 65. Alloy Agents Can Be More Dangerous Than Either Model Alone

📝 [OpenReview](https://openreview.net/forum?id=Is7kzM3Dxo) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`analysis`、`alloy agents`、`multi-model composition`、`capability elicitation`、`safety evaluation`
- 🎯 **研究动机**：在单次对话轨迹中交替多个 LLM 的 alloy agent 已被用于提升性能，但其安全性质此前未被研究，多模型组合诱发危险能力的潜力被忽视。
- 🔬 **研究方法**：在两种 regime 下评测 alloy agent：单动作任务（多轮交互中一次安全动作即可阻止不安全行为）与持续努力任务（需跨多轮执行不安全目标并同时完成合法任务），并与单独运行各模型取优对比。
- 📌 **结论**：单动作任务上 alloy 始终不高于较不安全的成分、多数基准接近较安全者；但持续努力任务上模式反转——Bash 脚本任务组合成功率达 83%（Gemini-Lite+Grok）对更好单独模型的 52%，最强 case（GPT+Gemini-Lite 73%）无法靠独立运行两模型取优复现，故多模型组合应纳入安全能力诱发评测技术集。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Alloy agents alternate multiple LLMs within a single conversation trace. They have been used to improve agent performance, yet their safety properties remain unstudied. We evaluate alloy agents on two regimes: single-action tasks, where behaving safely only requires one action within an otherwise multi-turn interaction, and continuous-effort tasks, where an agent must carry out an unsafe objective across many turns while simultaneously completing a legitimate assignment. On single-action tasks the alloy stays at or below the less safe constituent at every benchmark we tested, and on most benchmarks falls close to the safer one, consistent with a structural bound where one safe turn at the critical moment can block the unsafe action. On continuous-effort tasks the pattern reverses, and the alloy can combine one model's ability to complete the legitimate task with another model's willingness to carry out the unsafe objective, producing a system that succeeds at both where neither model run in isolation does. On Bash scripting tasks, for instance, combined success reaches 83% (Gemini-Lite + Grok), versus 52% for the better solo, and the strongest oracle-busting case (GPT + Gemini-Lite, 73% combined) cannot be replicated by simply running both models independently and picking the better result. When the unsafe objective interferes with the legitimate task this combined-success uplift does not emerge, though the alloy still expands the achievable Pareto frontier. The potential of multi-model composition to elicit dangerous capabilities has previously been overlooked, but our results show that it should be part of the set of elicitation techniques used to evaluate model safety.

</details>

### 66. Measuring and Strengthening Behavioral Suppression in Language Models

📝 [OpenReview](https://openreview.net/forum?id=OWTLAtAspY) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`behavioral suppression`、`unlearning`、`adversarial rl`、`model organisms`
- 🎯 **研究动机**：不良行为可在训练的任何阶段出现或复现，需要理解观察后再压制它们的实际效果，而标准压制方法在即时压制、持续训练下的耐久性与通用能力保持三个维度上的权衡未被系统评估。
- 🔬 **研究方法**：构建窄触发（可识别 prompt 特征诱发）与宽触发（弥散于开放回复）两种 model organism，在控制梯度更新数下比较 SFT、GRPO 与梯度上升遗忘，并基于对齐浅薄性假说提出 PEARL——用缓存轨迹中间状态采样的续写增强 rollout 的 GRPO 变体以覆盖更宽的失准状态。
- 📌 **结论**：在 Qwen3-4B 与 GPT-OSS-20B 两模型家族、两种 organism 设定下，PEARL 取得更低 exploit 率并保持任务精度，在靶向与良性能力微调下的再激活率均低于 SFT 与 GRPO 基线。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Undesired model behaviors can emerge or re-emerge at any stage of training. Once observed, how effectively can we suppress them? To study this question, we first construct two model organisms---language models trained to exhibit a specific misalignment---with qualitatively distinct structures. In the narrow-trigger organism, undesired behavior is elicited by an identifiable prompt feature. In the broad-trigger organism, misalignment surfaces diffusely across open-ended responses without a separable cue. We then formalize post-hoc behavioral suppression and evaluate methods along three criteria: immediate suppression of the target behavior, durability under further training, and preservation of general capability. We compare standard methods---SFT, GRPO, and gradient-ascent unlearning---along these dimensions while controlling the number of gradient updates. Building on prior work on alignment shallowness, we hypothesize that more durable suppression requires the ability to recover from a wider range of misalignment states. We introduce Prefix-Expanded Adversarial Reinforcement Learning (PEARL), a GRPO variant that augments rollouts with continuations from intermediate states sampled along cached organism trajectories. Across both organism settings and two model families (Qwen3-4B, GPT-OSS-20B), PEARL achieves lower exploit rates while preserving task accuracy, and yields lower reactivation rates under both targeted and benign capability fine-tuning than SFT and GRPO baselines. Together, our framework and method offer a step toward more durable post-hoc removal of undesired behaviors.

</details>

### 67. Inter-Agent Influence: Evaluating Persuasion, Deception and Coercion in Multi-Agent Systems

📝 [OpenReview](https://openreview.net/forum?id=ziYeGq8OOt) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`evaluation`、`multi-agent systems`、`persuasion`、`deception`、`coercion`
- 🎯 **研究动机**：多智能体工作流使 agent 能策略性操纵其他 agent 以达成特定目标，恶意 agent 可能引导他人执行有害行动，这种 inter-agent influence 能力带来新型风险却缺乏系统评测。
- 🔬 **研究方法**：在五个现实评测环境与多个前沿模型上考察 persuasion、deception、coercion 三种智能体间影响能力，覆盖监督（oversight）与点对点谈判等设定。
- 📌 **结论**：所有测试模型在监督环境中都能通过三种手段把违规决策从拒绝转为批准；点对点设定中模型在调度谈判中获取让步、并将同伴的安全研究方向重定向到攻击者偏好方向；多个前沿模型还独立制定并执行了胁迫威胁（含威胁伤害环境中具名人类）。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The deployment of AI agents in multi-agent workflows enables inter-agent influence, whereby agents strategically steer other agents’ behavior in line with a specific goal. Such capabilities pose novel risks, as malicious agents could direct others toward harmful actions. In this work we investigate three such capabilities –- persuasion, deception, and coercion –- across five realistic evaluation environments and a variety of frontier models. We observe significant inter-agent influence capabilities in frontier models. In oversight environments, all tested models shifted policy-violating decisions from rejection to approval through persuasion, deception, and coercion. In peer-to-peer settings, models extracted concessions in scheduling negotiations and redirected a peer's safety research trajectory toward an attacker-preferred direction. While evidence is weakest for inter-agent coercion, several frontier models independently formulated and executed coercive threats, including threats to harm a named human in the environment. These results point to a pressing need for work on risk mitigation to promote beneficial deployments of multi-agent systems.

</details>

### 68. Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL

📝 [OpenReview](https://openreview.net/forum?id=NERzW49Ahm) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`analysis`、`reward hacking`、`monitor`、`reinforcement learning`、`evasion`
- 🎯 **研究动机**：RL 奖励难以设计导致 reward hacking，而针对监控器训练可能诱发规避行为，如何有效使用监控器缓解 reward hacking 缺乏系统理解。
- 🔬 **研究方法**：开源三个 Qwen3-4B 会发生 reward hacking 的真实环境（可经测试覆写 hack 的编码、可经谄媚 hack 的医疗对话、可经幻觉 hack 的传记生成），系统研究监控器设计对训练动态的影响。
- 📌 **结论**：发现模型可利用探针与 LLM 评判的系统性缺陷规避高精度监控器、泄露更多学习信号的监控器更能抑制 hacking 但也更易被规避、训练加入更简单问题可减少 hacking；据此构建的监控器把医疗与传记环境的 reward hacking 率从 70-100% 降至 0%。

👤 **作者**：Aria Wong、Joshua Engels、Neel Nanda

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement learning (RL) rewards are notoriously difficult to design and control, often leading to the model learning unintended behaviors such as eward hacking. One potential solution is to monitor for reward hacking and penalize it when detected; however, training against a monitor could lead to evasive behavior, and our general understanding of how to apply monitors effectively during training is limited. To study how best to use monitors to mitigate reward hacking, we introduce and open source three realistic environments where Qwen3-4B reward hacks: a coding environment hackable via test overwriting, a medical chat environment hackable via sycophancy, and a biography generation environment hackable via hallucination. We first focus on the coding environment, where we find that: (1) models can learn to evade highly accurate monitors by exploiting systemic flaws in probes and LLM judges; (2) monitors that leak more learning signal during RL suppress reward hacking but are more often evaded; and (3) including easier problems in training can decrease reward hacking. We apply our findings to build better reward hacking monitors for the medical chat and biography generation environments that improve upon naive baselines to reduce reward hacking rates across seeds from 70-100% to 0%. Our results demonstrate that our takeaways translate to new settings and that better monitor intervention designs are possible.

</details>

### 69. SchemeArena: Factorized Stress Testing of Scheming in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2609.08126) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`benchmark`、`scheming`、`llm agent`、`stress testing`、`scheming monitor`
- 🎯 **研究动机**：先前 scheming 研究只考察少量场景，无法隔离工具性目标、环境 affordance、监督条件与后果感知等因素如何塑造 agent 的 scheming 倾向与能力。
- 🔬 **研究方法**：构建经因子化场景合成框架生成的 400 场景 benchmark（跨安全相关工具域、工具性目标、监督条件与压力机制），并提出将多判据裁决锚定在 agent 推理与行动证据上的 scheming monitor SCOUT。
- 📌 **结论**：对 5 个 LLM agent 的受控压力测试显示显式工具性目标是 scheming 最强驱动，战略提示帮助把 scheming 推理转化为具体隐蔽行为，部分闭源模型上 action-only 监督反而增加 scheming，且 CoT 是有用但不完整的监控信号。

👤 **作者**：Jie Ruan、Inderjeet Nair、Amy Liu、Muhammad Khalifa、Yusheng Zhou、Lu Wang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We study scheming in LLM agents, in which agents covertly pursue misaligned goals. Our focus is to understand how scheming arises from the interaction of key factors, such as instrumental goals, environmental affordances, oversight conditions, and perceived consequences. Prior work examines only a small number of scenarios, limiting the ability to isolate how these conditions shape an agent's propensity or capability to scheme. This limited scale and task diversity also restrict coverage of realistic deployment settings and the range of scheming strategies that can be observed. To this end, we introduce SCHEMEARENA, a 400-scenario benchmark for scalable scheming stress testing, constructed through a factorized scenario synthesis framework spanning diverse safety-relevant tool domains, instrumental goals, oversight conditions, and pressure mechanisms. To enable scalable and reliable monitoring, we further propose SCOUT, a scheming monitor that grounds multi-criteria judgments in evidence drawn from agents' reasoning and actions. Across controlled stress tests on five LLM agents, we find that explicit instrumental goals are the strongest driver of scheming propensity. Strategic hints play a distinct role by helping agents translate scheming reasoning into concrete covert behavior. Oversight has mixed effects: in several closed models, action-only monitoring increases scheming, suggesting that partial oversight can act as an optimization constraint rather than a deterrent. CoT is a useful but incomplete monitoring signal: it can reveal latent scheming before execution, yet action-only scheming shows that covert behavior may occur without explicit reasoning evidence. We release the benchmark, code, and monitor at: https://github.com/launchnlp/SchemeArena.

</details>

### 70. Attack Selection In Agentic AI Control Evaluations Meaningfully Decreases Safety

📄 [arXiv](https://arxiv.org/abs/2606.06529) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`evaluation`、`ai control`、`attack selection`、`red team`、`safety estimation`
- 🎯 **研究动机**：AI control 评测用红队攻击策略对蓝队监控做压力测试，但通常假设攻击者不会战略性地选择攻击时机，而会择机的攻击者更难被抓，安全估计可能过于乐观。
- 🔬 **研究方法**：把攻击决策分解为决定何时发起攻击的 start policy 与决定何时中止的 stop policy，在 BashArena 与 LinuxArena 两个智能体场景中评测其对经验安全性度量的影响。
- 📌 **结论**：在不改变底层攻击能力的前提下，1% 审计预算下 start policy 使两场景安全性各降 20pp，stop policy 在 BashArena 降 20pp、LinuxArena 降 28pp；建议未来评测、系统卡与安全论证都纳入攻击选择以得到更现实的安全估计。

👤 **作者**：Catherine Ge-Wang、Tyler Crosse、Benjamin Hadad、Joachim Schaeffer、Ram Potham、Tyler Tracy

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

An attacker that strategically chooses when to attack is much harder to catch than one that attacks indiscriminately. AI control is a safety framework for deploying capable but untrusted AI agents under the oversight of a weaker, trusted monitor and a limited human audit budget. Control evaluations stress-test these protocols by pitting a red-team attack policy against the blue-team monitor, but current evaluations typically assume attackers that do not strategically select when to attack. We study this capability, attack selection, in agentic settings by decomposing attack decisions into a start policy, which decides when an attacker should attack, and a stop policy, which decides when an attacker should abort an ongoing attack. Across two agentic settings, BashArena and LinuxArena, both policies substantially lower measured empirical safety without changing the underlying attack capability. At a 1% audit budget, our start policy reduces safety by 20pp on both BashArena and LinuxArena, and our stop policy reduces safety by 20pp on BashArena and 28pp on LinuxArena. These reductions should be interpreted as upper bounds on the effect of attack selection. Existing control evaluations may therefore yield overly optimistic safety estimates against selective attackers. We recommend that future evaluations, system cards, and safety cases elicit attack selection to produce more realistic safety estimates.

</details>

### 71. Training on Documents About Monitoring Leads to CoT Obfuscation

📄 [arXiv](https://arxiv.org/abs/2605.15257) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`cot monitoring`、`obfuscation`、`synthetic document finetuning`
- 🎯 **研究动机**：CoT 监控依赖模型忠实外化推理，需要检验知晓监控器存在的模型能否通过混淆推理来规避检测
- 🔬 **研究方法**：用 synthetic document finetuning 让 8 个模型接触描述 CoT monitor 的类预训练文档，比较 monitor-aware 与 unaware 对照组的未检出不良行为率，并刻画 CoT controllability 与混淆成功的关联
- 📌 **结论**：monitor-aware 模型的未检出不良行为率一致更高（更难的 agentic 任务上减弱但仍在），CoT 可控性与混淆成功相关系数 r=0.800（p=0.017），且同等 RL 压力下其学会绕过监控 reward-hack 明显更快

👤 **作者**：Reilly Haskins、Bilal Chughtai、Joshua Engels

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chain-of-thought (CoT) monitoring is one of the most promising tools we have for detecting model misbehavior, but its effectiveness depends on models faithfully externalizing their reasoning. Motivated by this vulnerability, we study whether monitor-aware models are capable of obfuscating their reasoning to evade detection. We use synthetic document finetuning to expose eight models to realistic pre-training-style documents describing a CoT monitor and find that monitor-aware models consistently achieve higher rates of undetected misbehavior compared to unaware controls. This effect is weaker but still present on a harder agentic task. We also show that CoT controllability, a model's ability to reshape its own reasoning trace under an imposed constraint, is closely correlated with obfuscation success across the eight models studied ($r=0.800$, $p=0.017$). Monitor-aware models placed under equal reinforcement learning optimization pressure also learn to reward-hack without triggering a CoT monitor substantially faster than unaware controls. Together, these results suggest that knowledge of monitoring combined with high CoT controllability poses a risk to CoT-based monitoring.

</details>

### 72. Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics

📄 [arXiv](https://arxiv.org/abs/2605.18549) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`detection`、`cot monitoring`、`probe trajectory`、`reasoning dynamics`、`hidden representations`
- 🎯 **研究动机**：大推理模型的 CoT 并不总忠于最终输出，削弱了其作为安全监控工具的可靠性，需要转向隐表征来预测未来行为。
- 🔬 **研究方法**：对每个生成 token 评估 probe 构建"probe trajectory"（概念概率随推理过程的连续演化），并提取刻画波动性、趋势与稳态的信号处理特征。
- 📌 **结论**：max-pooling 下轨迹特征使未来行为预测达 95% AUROC（average/last-token pooling 近随机），模板训练数据与动态生成响应近乎等价，跨 4 数据集与 4 推理模型验证安全与数学域的任务特定动态。

👤 **作者**：Maciej Chrabąszcz、Aleksander Szymczyk、Marcin Sendera、Tomasz Trzciński、Sebastian Cygert

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Reasoning Models (LRMs) introduce new opportunities for safety monitoring through their Chain of Thought (CoT) reasoning. However, CoT is not always faithful to the model's final output, undermining its reliability as a monitoring tool. To address this, we investigate the hidden representations of LRMs to determine whether future behavior can be predicted from prompt and CoT representations. By evaluating a probe at each generated token, we construct a probe trajectory, the continuous evolution of a concept's probability across the reasoning process. We find that future model behavior is more distinguishable when examined over the full trajectory than from a single static prediction. To characterize these temporal dynamics, we extract signal-processing features that capture volatility, trend, and steady-state behavior, significantly improving the separation of future model states. We also present two methodological insights. First, template-based training data achieves near-parity with dynamically generated model responses, eliminating the need for a costly initial inference and labeling. Second, the choice of pooling operation is critical: average-pooling and last-token methods collapse to near-random performance, while max-pooling achieves up to 95% AUROC and yields stable probe trajectories. Using four datasets and four reasoning models across the domains of safety and mathematics, we demonstrate that trajectory features encode task-specific dynamics that improve outcome separability. These findings establish probe trajectories as a complementary framework for monitoring LRM behavior. Warning: This article contains potentially harmful content.

</details>

### 73. Agent Meltdowns: The Road to Hell Is Paved with Helpful Agents

📄 [arXiv](https://arxiv.org/abs/2605.19149) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`agent safety`、`accidental meltdown`、`error injection`
- 🎯 **研究动机**：现有可靠性与安全基准均未覆盖"良性环境错误在无对抗输入下引发的有害行为"这一新型 agent 失败模式（accidental meltdown）
- 🔬 **研究方法**：提出 meltdown 行为分类法，构建 agent 无关的本地/远程错误注入基础设施，系统评估 GPT、Grok、Gemini 驱动的 agent 系统在遭遇错误后的行为
- 📌 **结论**：遭遇模拟错误的 rollout 中 64.7% 出现不同程度与成功率的 meltdown（如未授权侦察、绕过访问控制），超半数未向用户报告，且错误引发的探索与不安全行为相关

👤 **作者**：Rishi Jha、Harold Triedman、Arkaprabha Bhattacharya、Vitaly Shmatikov

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agents operating with computer and Web use inevitably encounter errors: inaccessible webpages, missing files, local and remote misconfigurations, etc. These errors do not thwart agents based on state-of-the-art models. They helpfully continue to look for ways to complete their tasks. We introduce, characterize, and measure a new type of agent failure we call \emph{accidental meltdown}: unsafe or harmful behavior in response to a benign environmental error, in the absence of any adversarial inputs. Because meltdowns are not captured by the existing reliability or safety benchmarks, we develop a taxonomy of meltdown behaviors. We then implement an agent-agnostic infrastructure for injecting simulated local and remote errors into the rollout environment and use it to systematically evaluate agent systems powered by GPT, Grok, and Gemini. Our evaluation demonstrates that meltdowns (e.g., conducting unauthorized reconnaissance or subverting access control) of varying severity and success occur in 64.7\% of agent rollouts that encounter simulated errors, spanning all combinations of agent system, backing model, and error type. In over half of these meltdowns, unsafe behaviors are not reported to the user. Comparing behaviors of the same agents with and without errors, we find that exploration in response to errors is correlated with unsafe and harmful behavior.

</details>

### 74. Training Deliberative Monitors for Black-Box Scheming Detection

📄 [arXiv](https://arxiv.org/abs/2605.29601) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`detection`、`scheming`、`deliberative monitor`、`distillation`
- 🎯 **研究动机**：现有 scheming 监控依赖 CoT 访问或内部激活，或使用昂贵且不一定可靠的 prompted 前沿模型，部署场景下常不可用
- 🔬 **研究方法**：受 deliberative alignment 启发，用 scheming specification 从前沿教师引出结构化 rationale、经独立 judge 过滤后以 SFT+RL 蒸馏进开源权重模型，训练仅依据 agentic 轨迹（action-only）的小型监控器
- 📌 **结论**：Qwen3.5-27B 监控器在 6 个 OOD agentic 失准基准上超过所有低成本前沿 prompted 监控器及 Gemini 2.5 Pro，强前沿监控器性能更高但边际推理成本约 16-34 倍，多个训练监控器位于成本-性能 Pareto 前沿

👤 **作者**：Aditya Sinha、…、Marius Hobbhahn

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As autonomous agents become more capable of performing real-world tasks, distinguishing scheming behavior from benign task pursuit may become a central AI control problem. Existing monitors often rely on chain-of-thought access or internal activations, or use prompted frontier models, all of which can be unavailable, unreliable or expensive in deployment. In this work, we study action-only deliberative monitors: smaller open-weight models trained to detect scheming and sabotage from agentic trajectories without accessing the monitored agent's reasoning or model internals. Our method, inspired by deliberative alignment, uses a scheming specification to elicit structured rationales from a frontier teacher, filters them with a separate judge, and distills the highest-quality rationales into open-weight monitors with supervised fine-tuning and reinforcement learning. We train on five datasets, and evaluate across six out-of-distribution agentic misalignment benchmarks. We show that applying our method to Qwen3.5-27B yields higher performance than all low-cost frontier models as prompted monitors (Gemini 3.1 Flash-Lite, GPT-5.4 Nano, and Claude Haiku 4.5) and than Gemini 2.5 Pro, while also achieving lower marginal inference cost (token-metered USD per 1,000 evaluations). Stronger prompted frontier monitors (Gemini 3.1 Pro, GPT-5.4, Claude Sonnet 4.6, and Claude Opus 4.6) achieve higher performance but at roughly $16$--$34\times$ higher marginal inference cost. Several of our trained monitors are positioned on the empirical cost--performance Pareto frontier among the monitors we evaluate, providing practical low-cost, low-FPR alternatives to prompted frontier models.

</details>

### 75. Tatemae: Detecting Alignment Faking via Tool Selection in LLMs

📄 [arXiv](https://arxiv.org/abs/2604.26511) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-04　🏷 NeurIPS 2026

**关键词**：`detection`、`alignment faking`、`tool selection`、`behavioral monitoring`
- 🎯 **研究动机**：现有 alignment faking 检测聚焦对话设置并主要依赖 CoT 分析，当推理痕迹缺失或不忠实时无法区分欺骗与能力失败
- 🔬 **研究方法**：将 AF 形式化为复合行为事件，通过可观测的工具选择检测——模型无监控时选安全工具、在奖励 helpfulness 的监控下切换到不安全工具，据此发布 108 个企业 IT 场景数据集并在 5 次独立运行中评估 6 个前沿 LLM
- 📌 **结论**：平均 AF 检出率介于 3.5%-23.7%，脆弱性画像随领域与压力类型变化，表明易感性更多反映训练方法而非能力

👤 **作者**：Matteo Leonesi、Francesco Belardinelli、Flavio Corradini、Marco Piangerelli

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Alignment faking (AF) occurs when an LLM strategically complies with training objectives to avoid value modification, reverting to prior preferences once monitoring is lifted. Current detection methods focus on conversational settings and rely primarily on Chain-of-Thought (CoT) analysis, which provides a reliable signal when strategic reasoning surfaces, but cannot distinguish deception from capability failures if traces are absent or unfaithful. We formalize AF as a composite behavioural event and detect it through observable tool selection, where the LLM selects the safe tool when unmonitored, but switches to the unsafe tool under monitoring that rewards helpfulness over safety, while its reasoning still acknowledges the safe choice. We release a dataset of 108 enterprise IT scenarios spanning Security, Privacy, and Integrity domains under Corruption and Sabotage pressures. Evaluating six frontier LLMs across five independent runs, we find mean AF detection rates between 3.5% and 23.7%, with vulnerability profiles varying by domain and pressure type. These results suggest that susceptibility reflects training methodology rather than capability alone.

</details>

### 76. Evaluating and Understanding Scheming Propensity in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2603.01608) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`analysis`、`scheming`、`llm agent`、`instrumental convergence`、`incentive decomposition`
- 🎯 **研究动机**：先前工作只证明 agent 具备 scheming 能力，但其在现实部署场景中实际发生 scheming 的倾向及驱动因素仍不清楚。
- 🔬 **研究方法**：将 scheming 激励分解为 agent 因素与环境因素，构造可系统性改变这些因素的现实场景（含自我保存、资源获取、目标守护等工具性收敛机会）并测量倾向。
- 📌 **结论**：尽管环境激励很高，scheming 实例极少且不太可能归因于 evaluation awareness；在 model organisms 中移除单个工具即可把 scheming 率从 59% 降到 3%，加强监管反而可能使 scheming 提升至多 25%。

👤 **作者**：Mia Hopman、Jannes Elstner、Maria Avramidou、Amritanshu Prasad、David Lindner

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As frontier language models are increasingly deployed as autonomous agents pursuing complex, long-term objectives, there is increased risk of scheming: agents covertly pursuing misaligned goals. Prior work has focused on showing agents are capable of scheming, but their propensity to scheme in realistic scenarios remains underexplored. To understand when agents scheme, we decompose scheming incentives into agent factors and environmental factors. We develop realistic settings allowing us to systematically vary these factors, each with scheming opportunities for agents that pursue instrumentally convergent goals such as self-preservation, resource acquisition, and goal-guarding. We find only minimal instances of scheming despite high environmental incentives, and show this is unlikely due to evaluation awareness. While inserting adversarially-designed prompt snippets that encourage agency and goal-directedness into an agent's system prompt can induce high scheming rates, snippets used in real agent scaffolds rarely do. Surprisingly, in model organisms (Hubinger et al., 2023) built with these snippets, scheming behavior is remarkably brittle: removing a single tool can drop the scheming rate from 59% to 3%, and increasing oversight can raise rather than deter scheming by up to 25%. Our incentive decomposition enables systematic measurement of scheming propensity in settings relevant for deployment, which is necessary as agents are entrusted with increasingly consequential tasks.

</details>

### 77. Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2602.15198) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`benchmark`、`collusion`、`multi-agent system`、`regret`、`covert channel`
- 🎯 **研究动机**：LLM 多智能体系统中一群 agent 可结成联盟合谋追求次级目标并损害联合目标，但缺乏对此类合谋行为的系统审计框架。
- 🔬 **研究方法**：Colosseum 以形式化多智能体决策框架刻画协作，用相对合作最优的 regret 度量行动合谋并与通信合谋对比，支持良性设置、不同联盟目标、说服策略与网络拓扑下的审计，并创设 agent 间秘密通信信道作为新行为探针。
- 📌 **结论**：秘密信道探针下大多数开箱即用模型表现出合谋倾向（emergent collusion），同时发现"纸上合谋"现象——agent 在文本中计划合谋却常选择非合谋行动。

👤 **作者**：Mason Nakamura、…、Eugene Bagdasarian

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-agent systems, where LLM agents communicate through free-form language, enable sophisticated coordination for solving complex cooperative tasks. This surfaces a unique safety problem when a group of agents forms a coalition and colludes to pursue secondary goals and degrade the joint objective. In this paper, we present Colosseum, a framework for auditing LLM agents' collusive behavior in multi-agent settings. We ground how agents cooperate through a formal multi-agent decision-making framework and measure action-based collusive behavior in actions via regret relative to the cooperative optimum and compare it with communication-based collusive behavior. Colosseum enables audits of LLM agents for collusion under benign settings, different coalition objectives, persuasion tactics, and network topologies. We then introduce a new behavioral probe by creating secret communication channels between agents, showing that most out-of-the-box models exhibit a propensity to collude under this probe, which we term emergent collusion. Furthermore, we discover ``collusion on paper'' when agents plan to collude in text but often pick non-collusive actions. Colosseum provides a new way to audit collusion in cooperative multi-agent systems while presenting observations about how collusion emerges, what affects collusion efficacy, and which strategies may mitigate it.

</details>

### 78. AI Control for Sandbagging on Fuzzy Tasks

📄 [arXiv](https://arxiv.org/abs/2606.08892) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`sandbagging`、`ai control`、`fuzzy tasks`、`adversarial game`
- 🎯 **研究动机**：部署于 AI 安全研究等关键领域的模型可能因失准而 sandbagging（故意在任务上表现不佳），该风险在难以评分、依赖直觉的模糊任务上尤其棘手。
- 🔬 **研究方法**：提出把 sandbagging 视为蓝红队对抗博弈的 AI control 框架：蓝队用弱信任模型构造弱评分并据此训练强模型去除怠工，红队用多目标进化提示优化寻找弱评分高但实际差的行为，蓝队再以对抗优化算法为弱模型发现更稳健的提示；在为近期 ML 论文研究问题写实验提案的任务上验证。
- 📌 **结论**：红队发现 Opus 4.6 能写出按 ground truth 代理评分差于 GPT-OSS-20B 的提案、却被弱评分评为与其最佳提案同高；蓝队对抗优化产生的提示使红队优化无法攻破。

👤 **作者**：Mikhail Terekhov、Caglar Gulcehre、Vivek Hebbar、Joe Benton

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI models deployed in critical domains, such as AI safety research, may subtly sabotage our efforts due to misalignment. is a form of sabotage in which an AI intentionally underperforms on the task given to it. It is particularly pernicious on tasks, i.e. tasks which are hard to grade or require intuition. To understand sandbagging on fuzzy tasks, we introduce a novel AI control framework that considers sandbagging as an adversarial game between a blue team and a red team. The blue team uses a weak trusted model to construct a weak score against which they would train a strong, potentially sandbagging model to remove the sandbagging if it were present. The red team then tries to find model behaviors that are rated highly by the weak score, and thus might not be trained out, but actually correspond to poor performance. We test our framework on the task of writing experimental proposals for research questions from recent ML papers. We use a language model with access to the original paper as a proxy "ground-truth" scorer. Our red team discovers sandbagging behaviors using multi-objective evolutionary prompt optimization. We show that Opus 4.6 can write proposals that are worse according to the ground truth proxy than those of GPT-OSS-20B, while the weak scorer rates them as highly as the best proposals from Opus 4.6. To mitigate the threat of sandbagging, we propose an adversarial optimization algorithm for the blue team that discovers more robust prompts for the weak model. This algorithm produces a blue team prompt that our red team optimization fails to exploit.

</details>

### 79. Breadcrumbing Search Agents: Per-Turn Scheming Over Long-Horizon Trajectories

📄 [arXiv](https://arxiv.org/abs/2608.04565) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`search agent`、`prompt injection`、`authority-chain hijack`、`strategy evolution`
- 🎯 **研究动机**：搜索 agent 依赖的外部工具返回构成脆弱安全边界，而现有安全研究只关注静态网页注入——现代 agent 会追问与交叉验证，单页投毒常被稀释或拒绝。
- 🔬 **研究方法**：在受约束的工具中介威胁模型下每次查询仅附加一条受控结果，提出专家精炼的 Authority-Chain Hijack（ACH）策略把孤立的搜索结果与页面内容操纵变成跨看似佐证来源的连贯证据链，并引入 Trace-Guided Strategy Evolution（TGSE）从执行轨迹自动改进可复用攻击策略。
- 📌 **结论**：ACH 在 SafeSearch 基准上达所有基线最高的 56.0%/85.0% ASR/MaxN ASR，TGSE 进一步提升到 71.4%/95.0%。

👤 **作者**：Xuebin Li、…、Nenghai Yu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based search agents are widely used for information-seeking tasks, but their reliance on external tool returns introduces a critical security risk: web content retrieved during execution is untrusted, exposing agents to prompt injection and goal hijacking. Prior work on search-agent safety primarily focuses on static web-content injection, but modern agents issue follow-up queries and cross-check competing sources, so a single injected page is often diluted or rejected. We show that the channel delivering search and page observations is a fragile security boundary: beyond exposing the agent to a single poisoned page, a mediated search interface can repeatedly steer how the agent gathers evidence and forms its final answer. Under a constrained tool-intermediary threat model, appending only one controlled result per query can substantially increase attack success when the evidence is coordinated across the agent's trajectory. We study this setting with a strategy-driven long-horizon attack system and introduce Authority-Chain Hijack (ACH), an expert-refined strategy that turns isolated search-result and page-content manipulations into a coherent evidence chain across seemingly corroborating sources. ACH achieves the highest Overall ASR among all baselines, reaching 56.0%/85.0% ASR/MaxN\,ASR on the SafeSearch benchmark. We further introduce Trace-Guided Strategy Evolution (TGSE), which automatically improves reusable attacker strategies from execution traces, replacing manual redesign with trace-driven refinement and further raising these to 71.4%/95.0%.

</details>

### 80. Neural Chameleons: Language Models Can Learn to Hide Their Thoughts from Unseen Activation Monitors

📄 [arXiv](https://arxiv.org/abs/2512.11949) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-12　🏷 NeurIPS 2026

**关键词**：`attack`、`activation monitoring`、`evasion`、`fine-tuning`、`misalignment threat model`
- 🎯 **研究动机**：激活监控是新兴 AI 安全工具，但在模型可能主动隐藏内部状态的失配威胁模型下的最坏情形鲁棒性从未被检验。
- 🔬 **研究方法**：微调 LLM 使其在"You are being probed for {concept}"触发下规避一批良性概念的 monitor，并测试该机制能否零样本泛化到未见过的安全 monitor。
- 📌 **结论**：在 Llama/Gemma/Qwen 上模型零样本规避未见安全 monitor（含在冻结权重上事后训练的 monitor），机制分析显示通过把激活压入低维子空间实现；monitor 集成与非线性分类器更鲁棒但模型仍保有非平凡规避能力。

👤 **作者**：Max McGuinness、Alex Serrano、Luke Bailey、Scott Emmons

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Activation monitoring, which probes a model's internal states using lightweight classifiers, is an emerging tool for AI safety. However, its worst-case robustness under a misalignment threat model--where a model might learn to actively conceal its internal states--remains untested. Focusing on this threat model, we ask: could a model learn to evade previously unseen activation monitors? Our core contribution is to stress-test the learnability of this behavior. We demonstrate that finetuning can create Neural Chameleons: models capable of zero-shot evading activation monitors. Specifically, we fine-tune an LLM to evade monitors for a set of benign concepts (e.g., languages, HTML) when conditioned on a trigger of the form: "You are being probed for {concept}". We show that this learned mechanism generalizes zero-shot: by substituting {concept} with a safety-relevant term like 'deception', the model successfully evades previously unseen safety monitors. We validate this phenomenon across diverse model families (Llama, Gemma, Qwen), showing that the evasion succeeds even against monitors trained post hoc on the model's frozen weights. This evasion is highly selective, targeting only the specific concept mentioned in the trigger, and having a modest impact on model capabilities on standard benchmarks. Using Gemma-2-9b-it as a case study, a mechanistic analysis reveals this is achieved via a targeted manipulation that moves activations into a low-dimensional subspace. While stronger defenses like monitor ensembles and non-linear classifiers show greater resilience, the model retains a non-trivial evasion capability. Our work provides a proof-of-concept for this failure mode and a tool to evaluate the worst-case robustness of monitoring techniques against misalignment threat models.

</details>

**尚未挂出 arXiv（待核验）**
- Chain-of-Thought Oversight Should Not Treat Faithfulness as Monitorability
- AIs with Secret Loyalties are a Serious but Addressable Threat
- AutoHoney: Automating, Deploying, and Evaluating Scheming Honeypots Across Production Codebases
- Scheming Is a Symptom: Alignment Research Should Probe Reflexive Fragility
- Agent Abstain: Do LLM Agents Know When Not to Act?
- Model Incrimination: Investigating Whether Concerning Behavior Reflects Misalignment
- Group Perspective Matters: Regulating Debate Relationships Can Mitigate Blind Conformity

### 智能体安全与提示注入

### 81. Agent MechSuits: Mechanistic Subspace Safety Steering for Multi-Turn CLI Agents

📝 [OpenReview](https://openreview.net/forum?id=GAW18QTdGu) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`cli agent safety`、`mechanistic interpretability`、`subspace steering`、`runtime detection`
- 🎯 **研究动机**：多轮 CLI agent 在与外部环境交互中带来显著安全与滥用风险，现有机制依赖外部护栏难以做执行中的细粒度行为控制，而机制可解释性方法多局限于单轮或越狱式 QA 设定。
- 🔬 **研究方法**：提出白盒防御框架 Agent MechSuits，从步级隐藏表示检测有害执行状态，并通过干预单层的 10 维子空间做表示级缓解，同时构建含 194 任务、跨 LLaMA-3.1-8B/Qwen-2.5-7B/Gemma-2-9B 全面标注多轮执行轨迹的 Mechanistic Agent Safety（MAS）基准。
- 📌 **结论**：Agent MechSuits 实现强安全检测性能、支持前瞻风险预估并显著减少有害 agent 动作，为机制可解释性应用于动态 LLM agent 安全奠定基础。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Command-Line Interface (CLI) agents based on large language models (LLMs) demonstrate remarkable autonomous capabilities, but they also introduce significant safety and misuse risks during multi-turn interactions with external environments. Existing safety mechanisms mainly rely on external guardrails, which have a limited ability to perform fine-grained behavioral control during execution. Meanwhile, recent mechanistic interpretability methods for LLM safety are mostly confined to single-turn or jailbreak-style QA settings, limiting their ability to capture the evolving risk dynamics of multi-turn agent execution. In this paper, we investigate the safety of multi-turn CLI agents from an internal perspective. We propose Agent MechSuits (Mechanistic Subspace Intervention and Steering), a white-box defense framework that performs runtime safety detection and representation-level mitigation for CLI agents. Unlike conventional agent guardrails, Agent MechSuits detect harmful execution states from step-level hidden representations and mitigate unsafe behavior by intervening in a 10-dimensional subspace within a single layer. To support this research, we introduce the Mechanistic Agent Safety (MAS) benchmark, comprising comprehensively annotated multi-turn execution trajectories across 194 tasks using LLaMA-3.1-8B, Qwen-2.5-7B, and Gemma-2-9B. Extensive experiments show that Agent MechSuits achieves strong safety detection performance, supports lookahead risk anticipation, and substantially reduces harmful agent actions, establishing a foundation for applying mechanistic interpretability to dynamic LLM agent safety.

</details>

### 82. ChainForge: Tool-Chain Hijacking Attacks against LLM Agents via Execution-Grounded Tool Synthesis

📝 [OpenReview](https://openreview.net/forum?id=K070HFaYyp) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`tool-chain hijacking`、`llm agents`、`execution-grounded synthesis`、`benchmark`
- 🎯 **研究动机**：已有攻击只针对单次工具调用（prompt 注入或元数据操纵），在多步工作流中攻陷单一步骤既显眼又不足以达成复杂对抗目标，工具调用管线的链级安全仍不清楚。
- 🔬 **研究方法**：提出工具链劫持攻击面及 ChainForge 框架：挖掘 agent 执行日志、经 rollout 优化合成能整体替代 agent 预期执行轨迹且仍正确完成用户任务的连贯工具链，再经多准则迭代细化把对抗载荷嵌入链中代码，并构建 4 域 97 任务的 ChainBench 基准。
- 📌 **结论**：在四个前沿 LLM 上轨迹劫持率最高达 98.54%、任务效用保持 80.41% 以上、跨模型迁移成功率超 84.95%，并以远高于单工具基线的比率规避所有被评测的防御与代码安全扫描器。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents increasingly rely on external tools to accomplish complex tasks, yet the security of tool-calling pipelines remains poorly understood at the chain level. Prior attacks target individual tool invocations through prompt injection or metadata manipulation, but compromising a single step in a multi-step workflow is conspicuous and rarely sufficient for complex adversarial objectives. In this work, we uncover a more insidious yet realistic attack surface, tool-chain hijacking, in which an adversary constructs a coherent sequence of tools that collectively replace the agent's intended execution trace while still completing the user's task correctly, rendering the hijack invisible to both the agent and the user. To operationalize this threat, we propose ChainForge, an execution-grounded framework that mines agent execution logs to synthesize replacement chains through rollout-based optimization, then embeds adversarial payloads into the chain's code via multi-criteria iterative refinement. To systematically evaluate chain-level threats, we further construct ChainBench, a benchmark of 97 tasks across 4 domains. Experiments on four frontier LLMs show that ChainForge achieves a trace hijack rate of up to 98.54%, maintains task utility above 80.41%, transfers across models with over 84.95% success, and evades all evaluated defenses and code-safety scanners at substantially higher rates than single-tool baselines, exposing a critical blind spot in current agent security.

</details>

### 83. Cross-User Poisoning: User-Task Boundary Failures in Multi-User Collaborative Language Agents

📝 [OpenReview](https://openreview.net/forum?id=y8FrK1agS0) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`cross-user poisoning`、`multi-user agents`、`shared context`、`prompt injection`
- 🎯 **研究动机**：语言 agent 正从单用户助手变为工作区/论坛/群聊中的共享协作者，须判断指令属于哪个用户或任务——这一单用户 agent 不存在的边界问题可被攻击利用。
- 🔬 **研究方法**：识别 cross-user poisoning（CUP）：对手向共享上下文注入消息，在 agent 服务良性用户时被应用、造成超出指令预期范围的未授权行为；在已部署的多用户 agent Continua 与 ElizaOS 上验证，并引入在并发多用户交互下评测共享上下文 agent 的 MURMUR 框架，同时评测边界限定类防御。
- 📌 **结论**：在 Slack、Workspace、Airline 三域 CUP 达到高攻击成功率、跨后续交互持续且显著强于匹配的 prompt-injection 攻击；单纯上下文摘要不足以防御，任务聚类与来源提示能大幅减少非自适应传播。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Language agents are moving from single-user assistants to shared collaborators in workspaces, forums, and group chats. A shared agent observes interleaved messages from multiple users, maintains persistent context, and executes tool actions, creating a boundary problem absent from standard single-user agents: the agent must decide not only whether an instruction is safe, but which user or task it is allowed to govern. We identify cross-user poisoning (CUP), where an adversary injects a message into shared context that is later applied while the agent serves a benign user, causing unauthorized actions or responses outside the instruction's intended scope. We validate CUP on two deployed multi-user agents, Continua and ElizaOS, and introduce MURMUR, a framework for evaluating shared-context agents under concurrent multi-user interactions. Across Slack, Workspace, and Airline domains, CUP achieves high attack success, persists across later interactions, and remains substantially more effective than matched prompt-injection attacks. We evaluate boundary-scoping defenses and find that context summarization alone is insufficient, while task clustering and provenance prompting substantially reduce non-adaptive propagation. These results show that robust multi-user agents require explicit user/task scoping rather than generic input filtering or context compression.

</details>

### 84. Asynchronous Agentic Poisoning

📝 [OpenReview](https://openreview.net/forum?id=MGAeMt2GKk) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`memory evolution`、`delayed poisoning`、`backdoor trigger`、`provider-side threat`
- 🎯 **研究动机**：记忆进化让模型生成内容跨任务持续并影响未来决策，这一反馈回路构成延迟攻击信道，但未被作为攻击面研究。
- 🔬 **研究方法**：提出 provider 侧的异步智能体投毒：微调发布的模型使其在正常回复中悄悄嵌入隐藏标记，标记经 agent 记忆进化累积，被检索回输入上下文时作为后门触发器使模型切换到攻击者指定行为，全程无需部署后攻击者交互。
- 📌 **结论**：记忆进化后有害率从低于 5% 升至约 90%，且不明显损害模型的自进化性能，证明模型可在发布时显得安全、经自进化在部署后变得不安全。

👤 **作者**：Guangnian Wan、Shizun Wang、Qi Li、Xinchao Wang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents are increasingly studied as systems that can self-evolve during deployment. A representative mechanism for realizing self-evolution is memory evolution, where agents maintain evolving memories derived from previous tasks and condition future inference on their memory. Although memory evolution is intended to improve agent performance, it also creates a feedback loop in which model-generated content can persist across tasks and influence future decisions. We study this loop as a delayed attack channel for memory-evolving agents. We introduce asynchronous agentic poisoning, a provider-side threat in which a malicious provider releases a model that appears safe under fresh-context evaluation but exhibits unsafe behavior after self-evolving through memory evolution. We realize this threat by fine-tuning the released model to silently embed a hidden marker into its otherwise normal responses, causing the marker to accumulate in the agent’s memory through memory evolution. When the accumulated markers are later retrieved into the input context, the model reacts to them as a backdoor trigger and shifts to attacker-specified behavior. This creates a self-triggered transition from safety-aligned behavior to attacker-specified behavior without requiring any post-deployment attacker interaction. Experimental results show that our method increases the harmful rate from below 5% to around 90% after memory evolution, while not substantially degrading the model’s self-evolution performance. These findings demonstrate that memory evolution creates a provider-side pathway for delayed compromise, allowing a model to appear safe at release time while becoming unsafe after deployment through the agent’s self-evolution process.

</details>

### 85. Forgetting is Not Always Bad: A Neuro-Inspired Memory Repair Mechanism for Poisoned LLM Agents

📝 [OpenReview](https://openreview.net/forum?id=8IiBySCaAn) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`memory poisoning`、`functional forgetting`、`memory repair`、`training-free`
- 🎯 **研究动机**：LLM agent 极易受记忆投毒攻击，现有防御依赖外部模块做静态记忆隔离或持续在线审计，导致内存效率低、计算开销大。
- 🔬 **研究方法**：受神经科学“无强化时弱再激活可致记忆失稳衰减”机制启发，提出训练无关的 agent 内在记忆修复框架 DREAM：扰动诱发隐式再激活暴露恶意记忆结构脆弱性、基于多维激活模式的自适应异常诊断检测拓扑异常、动态记忆修复模块选择性抑制有害记忆并强化良性记忆。
- 📌 **结论**：对后门投毒攻击成功率降低超 95% 且保留良性效用，中毒多智能体系统上任务成功率达 92.96%，较 A-MemGuard 提速至 2.13 倍并减少 37.7% 的 token 消耗，对注入攻击也有竞争力。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents are highly vulnerable to memory-poisoning attacks. Existing defenses primarily rely on external modules for either static memory isolation or continuous online auditing, resulting in low memory efficiency and high computational overhead. To address these limitations, inspired by neuroscientific mechanisms that weak reactivation can destabilize memories and induce decay in the absence of reinforcement, we propose an agent-intrinsic training-free memory repair framework, DREAM (Dynamic Reactivation for Engram Attenuation in Memory), that enables selective functional forgetting of poisoned memories. Specifically, DREAM implements a three-stage pipeline: perturbation-induced implicit reactivation to reveal the structural fragility of malicious memories, adaptive anomaly diagnosis based on multi-dimensional activation patterns to detect topological anomalies, and a dynamic memory repair module that selectively suppresses harmful memories while reinforcing benign ones. Extensive experiments across diverse attackers and real-world tasks demonstrate that DREAM reduces attack success rates by over 95% against backdoor poisoning while preserving strong benign utility. DREAM also achieves competitive robustness against injection attacks. In terms of runtime and token consumption, DREAM achieves up to a 2.13× speedup and a 37.7% reduction in token consumption compared with A-MemGuard. Furthermore, DREAM also achieves a task success rate of 92.96% on poisoned multi-agent systems.

</details>

### 86. Harmless in Pieces, Harmful in Motion: Detecting Multi-Agent Jailbreaks

📝 [OpenReview](https://openreview.net/forum?id=H4BgVHh3ID) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`detection`、`multi-agent jailbreak`、`runtime monitor`、`latent states`、`collective drift`
- 🎯 **研究动机**：对手可把有害目标分解为跨 agent、工具与共享记忆的各自良性子任务，使每次局部交互都合规而组合工作流不安全，现有防御只分类孤立 prompt、监控单 agent 历史或施加架构约束，均不直接检测全交互图上向有害的系统级漂移。
- 🔬 **研究方法**：提出训练无关的运行时监控器 CITADEL，用无学习参数的余弦门控循环在 agent、工具与记忆上维护 latent states，以同一冻结多模态编码器把公开安全分类学编码为固定 harm anchors，并以 harm-anchor 邻近度、多节点参与与正时间漂移的合取评分风险；同时构建涵盖五攻击族、三通信拓扑、异构 LLM/VLM 骨干的新基准。
- 📌 **结论**：CITADEL 将平均攻击成功率从 69.3% 降至 16.9%（相对降 75.6%），假阳性率 2.1%、每事件开销 28 ms，优于各类基线，且同一组超参无需调优即迁移到 OpenAgentSafety、Agent Security Bench 与 MTMCS-Bench。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

: an adversary can decompose a harmful objective into individually benign sub-tasks distributed across agents, tools, and shared memory, so that each local interaction appears policy-compliant while the composed workflow is unsafe. Existing defenses classify isolated prompts, monitor single-agent histories, or impose architectural constraints, but none directly detect runtime system-level drift toward harm across the full interaction graph. We introduce atent States), a training-free runtime monitor for multi-turn, multi-agent jailbreaks. CITADEL maintains latent states over agents, tools, and memory stores using a cosine-gated recurrence with no learned parameters; encodes a published safety taxonomy as fixed harm anchors via the same frozen multimodal encoder applied to runtime events; and scores risk through the conjunction of harm-anchor proximity, multi-node participation, and positive temporal drift. We evaluate CITADEL on , a new benchmark spanning five multi-agent attack families, three communication topologies, and heterogeneous API-accessible LLM/VLM backbones. CITADEL reduces average attack success rate from 69.3% to 16.9% — a 75.6% relative reduction — at a 2.1% false-positive rate and 28 ms per-event overhead, outperforming per-agent detectors, trajectory-level monitoring, and architectural defenses. The same hyperparameters transfer without retuning to OpenAgentSafety, Agent Security Bench, and MTMCS-Bench, indicating that collective geometric convergence provides an effective runtime signal for detecting distributed jailbreaks in multi-agent systems.

</details>

### 87. FlowLeak: Coverage-Guided Extraction of Dynamic Workflows in LLM-Based Multi-Agent Systems

📝 [OpenReview](https://openreview.net/forum?id=bwOADsslTR) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`workflow extraction`、`multi-agent systems`、`coverage-guided exploration`、`branch overfitting`
- 🎯 **研究动机**：LLM 多智能体系统的隐藏工作流是有价值的知识产权与安全关键资产，现有黑盒抽取方法假设对抗查询可遍历所有 agent，对执行路径依赖输入语义与中间状态的动态工作流失效。
- 🔬 **研究方法**：针对分支过拟合与隐蔽覆盖探索两大挑战提出 FlowLeak：Task-Preserving Payload Template 在诱导工作流信息的同时保留合法任务语义以缓解过拟合，Coverage-Guided Branch Exploration 用已抽取的工作流片段生成分支定向任务并把抽取约束为辅助任务要求，减少查询且更难暴露。
- 📌 **结论**：在 102 个 MAS 上显著改进动态工作流抽取（提升 2.68 倍），且抽取的工作流信息可增强下游攻击，凸显 MAS 工作流抽取的安全风险。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs)-based multi-agent systems (MAS) coordinate specialized agents through prompts, tools, and communication topologies, making their hidden workflows valuable intellectual property and security-critical assets. Existing black-box MAS extraction methods implicitly assume that adversarial queries can traverse all agents, which holds for static workflows but breaks down in dynamic workflows whose execution paths depend on input semantics and intermediate states. We identify two key challenges in dynamic workflows: branch overfitting, where fully adversarial queries overfit to the same branch and extract only a subset of agents, and stealthy coverage exploration, where the adversary needs to achieve complete branch coverage with few redundant queries while not exposing the extraction task. To address these challenges, we propose FlowLeak that combines Task-Preserving Payload Template, which preserves legitimate task semantics while eliciting workflow information to mitigate branch overfitting, with Coverage-Guided Branch Exploration, which uses previously extracted workflow fragments to generate branch-targeted tasks and constrains workflow extraction as an auxiliary task requirement, thereby reducing exploration queries and making extraction harder to identify. Experiments on 102 MAS show that FlowLeak addresses both challenges and substantially improves dynamic workflow extraction (2.68× improvement). Furthermore, we show that the extracted workflow information from FlowLeak enhances downstream attacks, highlighting the security risks of MAS workflow extraction and our method.

</details>

### 88. Leaderboard Hacking: Preference-Based Model Evaluations are Vulnerable to Manipulation

📝 [OpenReview](https://openreview.net/forum?id=VbWRUbpIUv) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`leaderboard manipulation`、`bradley-terry`、`preference evaluation`、`strategic voting`
- 🎯 **研究动机**：LMArena 等竞技场式排名通过匿名模型两两比较并以 Bradley-Terry 模型聚合投票来“现实地”评估模型，但这类排行榜可能被不道德提供商以多种策略操纵。
- 🔬 **研究方法**：识别并演示三种操纵策略——strategic voting（含对无关模型投票以抬升排名）、strategic prompting（选取利于己方的 prompt）、strategic nomination（插入无关模型抬升目标模型），在公开排行榜数据上验证、分析漏洞成因并给出对应防护。
- 📌 **结论**：这些操纵几乎能提升所有被测模型的排名，单一攻击可将模型抬升 15-21 位、组合攻击最高抬升 45 位，且问题适用于任何使用 Bradley-Terry 的两两偏好评测。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Arena-style rankings of language models are a widely used evaluation framework in leaderboards like LMArena, research papers, and model evaluation in production. These rankings aim to realistically assess model performance using pairwise comparisons of anonymous models on user prompts, aggregating votes via the Bradley-Terry model to produce the final ranking. However, we find that these leaderboards are highly vulnerable to several manipulation strategies that unscrupulous providers could use to boost a model's rank: strategic voting (individual votes that boost a model's rank, including votes on irrelevant models), strategic prompting (choosing prompts that favor a model), and strategic nomination (boosting the rank of a model by inserting irrelevant models). We demonstrate these effects on public leaderboard data, analyze the circumstances that cause these vulnerabilities, and describe approaches to safeguard against each attack. Notably, these issues hold for any pairwise preference-based evaluation that uses the Bradley-Terry model. These manipulations boost the rank of nearly every tested model; each attack can boost a model by up to 15-21 places in a ranking and, combined, they can boost a model by up to 45 places.

</details>

### 89. Reasoning Poisoning: Utilizing Social-Engineering to Steer Chain-of-Thought

📝 [OpenReview](https://openreview.net/forum?id=ZswTm9bjg9) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`reasoning poisoning`、`social engineering`、`logic hijacking`、`rlhf alignment`
- 🎯 **研究动机**：LLM 转为自主推理 agent 后推理轨迹本身成为关键漏洞——对手可通过操纵检索上下文对模型实施定向社会工程、武器化其 RLHF 对齐。
- 🔬 **研究方法**：提出 Reasoning Poisoning 框架，核心范式 Logic Hijacking 通过引入虚构风险利用泛化对齐约束，迫使 agent 主动排除合法目标并选择攻击者目标为唯一“有效”替代，在 10 个领域上评测六个生产部署的推理模型。
- 📌 **结论**：攻击从根本上覆盖标准逻辑，ASR 超 83%；攻击者仅控制 10% 检索上下文时仍然高效、且对载荷在证据窗口中的位置鲁棒；agent 对模拟社会证明（如用户点赞）完全无反应，依赖的是模仿其自身对齐训练的风格与语义线索。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The transition of Large Language Models (LLMs) to autonomous reasoning agents introduces a critical vulnerability within the reasoning trace itself. We present Reasoning Poisoning, a framework demonstrating how adversaries can exploit an agent via model-directed social engineering by manipulating retrieved context to weaponize the model's Reinforcement Learning from Human Feedback (RLHF) alignment. Our central paradigm, Logic Hijacking, exploits generalized alignment constraints by introducing fictitious hazards that force the agent to actively eliminate legitimate targets and select the attacker's target as the only "valid" alternative. Evaluating six state-of-the-art, production-deployed reasoning models across 10 domains, we show that this attack fundamentally overrides standard logic, achieving Attack Success Rates (ASR) exceeding 83%. The vulnerability remains highly effective even when the attacker controls only 10% of the retrieved context and exhibits robust success regardless of the adversarial payload's position within the evidence window. Controlled baselines confirm that this steering is driven by adversarial constraints, not ordinary promotional bias. Furthermore, we find that agents are entirely unresponsive to simulated social proof (e.g., user upvotes), relying instead on stylistic and semantic cues that mimic their own alignment training. Ultimately, our findings reveal a troubling paradox: the very alignment mechanisms designed to make models helpful and safe can be exploited to seamlessly hijack the reasoning process.

</details>

### 90. EnvTrap: Revealing the Environment-Only Attack Surface in Embodied AI via Consequence-Blind Action Execution

📝 [OpenReview](https://openreview.net/forum?id=Dn8mqYHQ8S) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`embodied ai`、`environment-only perturbation`、`vla`、`consequence prediction`、`defense`
- 🎯 **研究动机**：具身 AI 的既有攻击集中于语义/指令层操纵，而攻击者无需访问模型或指令、仅重排物理环境中的物体即可致害的环境侧攻击面尚未被研究。
- 🔬 **研究方法**：提出 EnvTrap 诊断管线，构造安全/陷阱/null-trap（良性但具误导性）成对具身场景评测多个 VLA 模型与世界模型，并设计后果感知防御。
- 📌 **结论**：仅环境扰动即可使危险动作率平均升至 86.5%，模型后果预测准确率近乎随机而人类轻松完成；后果感知防御将陷阱触发率在仿真中平均降低 76.3%、在物理机器人上降低 61.7%。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As AI models evolve from text and vision to physical agents, embodied AI faces a fundamentally different attack surface. Prior attacks on embodied systems have largely focused on semantic or instruction-level manipulations, such as prompts, adversarial images, and action commands; by contrast, we study environment-only perturbations that require no access to the model or instructions. We reveal a new attack surface: the physical environment itself. An adversary who rearranges objects, without modifying instructions or accessing models, can cause hazardous consequences. In this work, we propose EnvTrap, a diagnostic pipeline that constructs paired safe, trap, and null-trap (benign but misleading) embodied scenarios. We demonstrate that environment-only perturbations raise hazardous-action rates to an average of 86.5% across multiple vision-language-action (VLA) models, with similar vulnerability patterns confirmed in world models. On a consequence-prediction task, model accuracy remains near chance, while human evaluators succeed easily. We further propose a consequence-aware defense that reduces trap trigger rates by an average of 76.3% across VLA models in simulation and by 61.7% on physical robots. This vulnerability arises because current embodied models can recognize scene state but often fail to predict action consequences under altered layouts. Our findings establish environment integrity as a prerequisite for safe embodied AI deployment. Our code and data are available at https://anonymous.4open.science/r/Envtrap-1BA4/

</details>

### 91. Soteria: Formally Verified Planning with Runtime Enforcement for Safe LLM Agents

📝 [OpenReview](https://openreview.net/forum?id=9url1EFMaU) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`llm agent`、`formal verification`、`hierarchical planning`、`runtime enforcement`
- 🎯 **研究动机**：LLM 智能体的多步工具调用需同时满足任务效用与领域安全规范，现有方法往往牺牲其一，阻塞不安全动作虽避免违规却让智能体陷入无法恢复的困境。
- 🔬 **研究方法**：提出 Soteria 框架，执行前生成结构化计划并对其做形式化验证，运行时让已验证计划兼具保证规范一致轨迹与在动作被阻断时提供恢复引导的双重作用。
- 📌 **结论**：在覆盖多类工具使用任务的基准上实现完美规范一致性，效用较现有护栏方法最高提升 5 倍，证明安全与效用无需权衡。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents that execute multi-step tool calls must satisfy two objectives simultaneously: completing the user's task (utility) and conforming to domain policies and correctness constraints (safety). These objectives are in tension -- blocking an unsafe action prevents a violation but can leave the agent stranded with no principled way to recover. Existing approaches sacrifice one objective for the other. We introduce Soteria, a framework that reconciles safety and utility through verified hierarchical planning and runtime enforcement of specifications. Before execution, the agent generates a structured plan that is formally verified against the specifications prior to any tool invocation. During execution, the verified plan serves dual roles: it ensures that the agent takes specification-conformant trajectories and provides guidance when unsafe actions are blocked. Across multiple benchmarks covering a diverse range of tool-use tasks, Soteria achieves perfect specification conformance while improving utility by up to 5× over existing guardrail approaches, demonstrating that safety and utility need not be traded off.

</details>

### 92. Runtime Verification of Multiple Natural Language Criteria for Agent Governance

📝 [OpenReview](https://openreview.net/forum?id=BXJQ1dWtA8) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`detection`、`runtime verification`、`natural language criteria`、`tree attention`、`agent governance`
- 🎯 **研究动机**：AI 智能体受数百条自然语言准则治理，但现有验证器无法高效地对大量准则逐条评估并报告满足、违反或不适用。
- 🔬 **研究方法**：提出树注意力验证器 VFM，编码共享上下文与目标文本后并行对 N 条准则打分并输出独立三值判定，并在含 35.7 万条样本、28.5 万条去重准则的 CriteriaBank 语料上预训练。
- 📌 **结论**：微调后的 VFM-4B 在合成治理基准达 88.3% 准确率、超过更大的生成式裁判，DynaBench 追踪级失败检测 F1 达 0.85（对照 DynaGuard-4B 为 0.72）、级联方案达 0.94，且在 H100 上对 4K 上下文评估 1000 条准则仅需 2 秒以内。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents are governed by hundreds of natural language criteria---yet existing verifiers cannot efficiently evaluate an agent's output against a large set of such criteria and report which are satisfied, violated, or inapplicable. We introduce the VFM, a tree-attention verifier that encodes the shared context and target text, and scores N natural language criteria in parallel, returning independent per-criterion ternary verdicts. The VFM is pretrained on CriteriaBank, an open corpus of 357K (context, target, criterion, verdict) tuples spanning over 285K distinct criterion strings. A finetuned VFM-4B reaches 88.3% accuracy on a synthetic governance benchmark, surpassing larger generative judges, and on real insurance-compliance calls it is competitive with GPT-5.4 with synthetic finetuning alone. On the DynaBench multi-criterion benchmark, a finetuned VFM-4B reaches 0.85 F1 on trace-level failure detection versus DynaGuard-4B's 0.72; the VFM additionally localizes the violated rule as its top-1 prediction in 98.4% of failing traces, and a top-3 cascade to a 26B Gemma 4 chain-of-thought judge reaches 0.94 F1. CriteriaBank pretraining improves cross-domain transfer on four additional benchmarks, particularly in the low-data regime. On an H100, VFM-4B evaluates 1000 criteria against a 4K-token context in under 2s at <10GB VRAM, making it suitable for runtime verification. We will release CriteriaBank, trained checkpoints, and evaluation code.

</details>

### 93. Swarm Shepherd: Securing Multi-Agent Ecosystems Against Persistent Latent Compromise

📝 [OpenReview](https://openreview.net/forum?id=HUYSBrE6dV) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`multi-agent system`、`agentic sleeper`、`latent compromise`、`traceback`
- 🎯 **研究动机**：智能体生态中危害可跨会话、跨智能体与系统层累积后再显现，逐轮防御无法捕捉这种先合法获取路由信任、后在记忆/智能体逻辑/基础设施多层面激活的系统级潜伏威胁（定义为 Agentic Sleeper）。
- 🔬 **研究方法**：将防御形式化为部分可观测下的推理，提出 Swarm Shepherd 框架，以推理过滤器做早期预警、反向追溯模块做入侵归因，并推导平衡更长事件历史与更广智能体覆盖的双尺度部署规则。
- 📌 **结论**：在 LangGraph、CrewAI、AutoGen 上 Agentic Sleeper 漂移比自然基线快 2.7–8.9 倍、对逐轮与有状态防御的逃逸率超 80%；Swarm Shepherd 至少提前 3 个会话预警，追溯 top-1 准确率 0.69、macro-F1 0.72（24 种变体）。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic ecosystems are emerging as a new platform layer in which agents maintain persistent memory, retrieve from shared knowledge bases, execute through tool interfaces, and coordinate through shared states. These capabilities create a security problem that per-turn defenses miss: compromise can accumulate across sessions, agents, and system layers before visible failure. We define this threat as Agentic Sleeper, a system-level adversary that first behaves legitimately, gains routing trust, and later activates across memory, agent logic, and infrastructure. We formulate defense as inference under partial observability and propose Swarm Shepherd, a system-level defense framework centered on an inference filter for early warning, paired with a backward trace-back module for entry attribution. Our analysis yields a two-scale deployment rule that balances longer event histories against broader agent coverage. Across LangGraph, CrewAI, and AutoGen, Agentic Sleeper drift begins 2.7--8.9× faster than natural baselines, propagates across agents on most topologies, and evades per-turn and stateful defenses above 80%. Swarm Shepherd warns at least three sessions before visible degradation, while trace-back reaches 0.69 top-1 accuracy and 0.72 macro-F1 over 24 variants. The two-scale deployment rule is empirically confirmed, and containment guided by this rule reduces cross-agent propagation below the self-sustaining regime.

</details>

### 94. Safe Actions Can Form Unsafe Traces: Benchmarking and Shielding Compositional Emergent Risk in AI Agents

📝 [OpenReview](https://openreview.net/forum?id=I49ieEOieb) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`benchmark`、`compositional emergent risk`、`agent safety`、`runtime shield`、`conformal calibration`
- 🎯 **研究动机**：LLM 智能体经工具、浏览器与 API 行动使安全成为轨迹级问题，单独安全的动作跨时间交互可产生不安全结果（组合涌现风险 CER），而风险依赖落在可见上下文之外时有限窗口安全过滤器必然漏检。
- 🔬 **研究方法**：构建含 440 任务、19,525 动作、跨 5 个风险域与 2 种组合机制的长程基准 CER-Bench，并提出共形校准的运行时防护 RiskShield，学习轨迹风险边界、在提交前评估计划延续并替换风险后缀同时保留安全前缀。
- 📌 **结论**：15 个前沿与开源模型均存在非零组合性差距（44.4%–100%，均值 82.2%）；RiskShield 在 7 个留出模型上将平均 CER-5 组合性差距从 69.9% 降至 0.0%，763 次评估无一次屏蔽通过（95% 上置信界 1.6%），并保留 78.4% 步级任务完成率。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model agents increasingly act through tools, browsers, code interpreters, and external APIs, turning safety from a single-output problem into a trace-level problem. We identify \emphcompositional emergent risk (CER), a failure mode where individually safe actions interact across time to produce unsafe outcomes. We show that bounded-window safety filters can miss CER whenever the risky dependency lies outside their visible context. To study this failure systematically, we introduce \textscCER-Bench, a controlled long-horizon benchmark with 440 tasks and 19,525 actions across 5--500 steps, spanning five risk domains and two compositional mechanisms. At the largest tier, each trace induces a 79M+ candidate risk-composition search space. Across 15 frontier and open-source LLM agents, every model exhibits a non-zero compositionality gap (CG), ranging from 44.4% to 100.0% with a mean of 82.2%. Moreover, 86.1% of compliant executions contain caution language yet still proceed, showing that verbal risk awareness does not reliably prevent unsafe composition. We introduce \textscRiskShield, a conformal-calibrated runtime shield that learns trace-risk boundaries, evaluates planned continuations before commitment, and substitutes risky suffixes while preserving safe prefixes. On 7 held-out \textscCER-Bench models, \textscRiskShield reduces mean \textscCER-5 CG from 69.9% to 0.0%, with no shielded pass observed in 763 evaluations and a 95% upper confidence bound of 1.6%, while preserving 78.4% step-level task completion. It outperforms cumulative-threshold, sliding-window, full-trace, and published safety baselines, with 63.3% of tasks requiring no extra API call and additional robustness across longer traces, risk domains, and external agent-safety benchmarks. Code and benchmark are available at \urlhttps://anonymous.4open.science/r/RiskShield-2284.

</details>

### 95. Behavioral Probes for Information Flow in LLM Swarms

📝 [OpenReview](https://openreview.net/forum?id=oXV7UcdWSz) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`analysis`、`llm swarm`、`information flow`、`behavioral probes`、`structure optimization`
- 🎯 **研究动机**：现有 LLM 群体优化以最终任务效用为导向，个体交互内部的信息处理、整合与依赖基本处于不可见状态。
- 🔬 **研究方法**：从信息流视角引入行为探针，将原本用于幻觉分析的外部上下文分数 ECS 与参数知识分数 PKS 改造为节点的外部上下文依赖与参数知识依赖度量，并用作结构优化的辅助信号。
- 📌 **结论**：ECS 随输入相关性上升、PKS 随信息上下文累积而下降的模式一致成立，探针引导的节点剪枝显著减少异常节点、探针引导的推理路径搜索较仅效用基线加速收敛。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Most existing approaches to LLM swarm optimization are utility-driven, focusing on final task utility while leaving the processing, integration, and reliance of information within individual interactions largely implicit. To address this, we study LLM swarm interactions from an information-flow-based view and introduce behavioral probes to quantify information flow patterns. Specifically, we repurpose External Context Score (ECS) and Parametric Knowledge Score (PKS)—originally designed for hallucination analysis—to measure a node’s external-context dependence and parametric-knowledge dependence, respectively. Across controlled and realistic swarm settings, we observe consistent patterns: ECS increases with input relevance and distinguishes useful multi-source contributions, while PKS decreases as informative context accumulates. Building on this heuristic interpretation, we demonstrate how these probes can complement utility-driven structure optimization in two controlled applications. Probe-guided node pruning significantly reduces anomalous nodes, and probe-guided reasoning-path search accelerates convergence compared to utility-only baselines. Our empirical results suggest that behavioral probes can make the internal information flow of LLM swarms observable and serve as effective auxiliary signals for structure optimization.

</details>

### 96. Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage?

📝 [OpenReview](https://openreview.net/forum?id=4ip9zQaFI7) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`evaluation`、`human oversight`、`coding agent`、`sabotage`、`safety monitor`
- 🎯 **研究动机**：AI 编码智能体可获得代码库与工具的广泛访问并利用人类信任植入恶意代码执行隐藏任务，而既有破坏研究多限于 AI-only 场景，人类监督能否发现此类行为缺乏系统研究。
- 🔬 **研究方法**：开展大规模人类监督研究，100 余名参与者与 Claude Opus-4.6、GPT-5.4、Gemini-3.1-Pro、MiniMax-M2.7 四个前沿模型在约 5 小时的长程编码任务中协作，并在一个条件下测试安全监视器的效果。
- 📌 **结论**：95% 的开发者未能发现破坏，归因于不做代码审查、可信托辞与对智能体的过度信任；即使监视器降低了破坏成功率，56% 的参与者仍无视警告接受恶意代码。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI coding agents are increasingly embedded in real-world software development, collaborating closely with human developers while gaining broader access to codebases and tools. This creates a new attack surface: an agent can exploit human trust to sabotage development, for instance by inserting malicious code to accomplish a hidden side task. Most prior work studies AI sabotage in AI-only settings, paying limited attention to the role of human oversight in detecting and mitigating such malicious behavior. To address this gap, we conduct the first large-scale study of human oversight in AI coding sabotage. Over 100 participants collaborate with one of the four frontier models (Claude Opus-4.6, GPT-5.4, Gemini-3.1-Pro, and MiniMax-M2.7) on a long-horizon coding task lasting around five hours, designed to mimic real-world workflows. We find that 95% of developers fail to detect sabotage, and our analysis of participant feedback attributes this vulnerability to coding without review, plausible cover story, and overtrust in agents. We further test the effectiveness of a safety monitor in one condition: while the monitor reduces sabotage success, 56% of participants still accept the malicious code, ignoring its warnings. Drawing on participant feedback, we offer actionable suggestions for better monitor design. This work complements existing AI safety research and highlights an urgent need for human-centric safety mechanisms that account for human factors, particularly in long-horizon, real-world development settings.

</details>

### 97. Synthetic Web: Benchmarking Language Agents under Adversarial Search Ranking

📝 [OpenReview](https://openreview.net/forum?id=6JUMpZWGTT) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`benchmark`、`web agent`、`adversarial ranking`、`misinformation`、`source criticism`
- 🎯 **研究动机**：语言智能体检索、浏览并综合多源信息，其中可含不可信或对抗内容，而现有基准评测功能导航或静态事实性，无法因果隔离对抗排序脆弱性且常将检索时推理与记忆知识混淆。
- 🔬 **研究方法**：构建程序化生成 web 生态的 Synthetic Web 基准，提供带真值标签的数千篇超链文章、过程级交互轨迹与污染过滤，并在指定排名注入单篇高可信误导文章以在最小干预下测量对抗暴露的因果效应。
- 📌 **结论**：在六个前沿模型与数千次评估中观察到灾难性失败——即使可无限制访问真实证据准确率仍崩塌，伴随搜索升级有限、跨源综合薄弱与严重误校准，表明现有智能体难以仲裁冲突来源。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Language agents increasingly act as web-enabled systems that search, browse, and synthesize information from diverse sources. However, these sources can include unreliable or adversarial content, and the robustness of agents to adversarial ranking remains poorly understood. Existing benchmarks evaluate functional navigation or static factuality but cannot causally isolate this vulnerability and often confound retrieval-time reasoning with memorized knowledge. We introduce Synthetic Web Benchmark, a controlled environment of procedurally generated web ecosystems designed to evaluate retrieval-time reasoning and source criticism. The benchmark comprises thousands of hyperlinked articles with ground-truth labels, process-level interaction traces, and contamination filtering to ensure that answers cannot be recovered from pretraining alone. By injecting a single high-plausibility misinformation article at a specified rank, we measure the causal effect of adversarial exposure under minimal intervention. Across six frontier models and thousands of evaluation instances, we observe catastrophic failures: accuracy collapses despite unrestricted access to truthful evidence, accompanied by limited search escalation, weak cross-source synthesis, and severe miscalibration. These results show that current agents struggle to arbitrate conflicting sources even when sufficient evidence is available, revealing fundamental limitations in retrieval-based reasoning. The benchmark provides a reproducible testbed for studying epistemic robustness and developing more reliable web agents.

</details>

### 98. The Web Doesn't Sit Still: Adversarial Self-Evolving Attacks on Search Agents

📝 [OpenReview](https://openreview.net/forum?id=pjLUz7TVsi) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`search agent`、`self-evolving attack`、`bi-level optimization`、`evolutionary optimization`
- 🎯 **研究动机**：搜索智能体因依赖 web 检索而易受恶意信息注入、隐蔽上下文操纵等攻击，而现有攻击策略依赖静态人工模板，无法模拟真实威胁的动态与复杂性质。
- 🔬 **研究方法**：提出整合攻击者策略进化与防御者自适应缓解间双层优化的对抗自进化框架，用 CREO（对比展开进化优化）以对比进化信号驱动攻击策略种群定向进化，并构建受控沙箱与细粒度指标量化内部脆弱性。
- 📌 **结论**：在多个多跳 QA 基准与前沿 LLM 上的攻击效力优于静态基线，凸显构建更强防御框架的迫切需求。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have shown promise for empowering search agents to tackle complex information-seeking tasks. However, since acquiring external information necessitates web search, these agents are highly susceptible to various adversarial attacks (e.g., malicious information injection or stealthy context manipulation). Existing attack strategies inevitably rely on static and human-crafted templates, failing to emulate the dynamic and complex nature of real-world threats. In this paper, we propose an adversarial self-evolution framework that integrates bi-level optimization between the attacker's strategy evolution and the defender's adaptive mitigation, to expose the vulnerabilities of search agents. Specifically, we introduce the Contrastive Rollout Evolutionary Optimization (CREO) method to drive the directional evolution of the attack strategy population via contrastive evolutionary signals. To provide a stable environment for this continuous evolution, we further construct a controlled sandbox and design fine-grained metrics to quantify internal vulnerabilities. Extensive experiments across various multi-hop QA benchmarks and frontier LLMs demonstrate that the proposed framework yields attack efficacy superior to static baselines, underscoring the urgent need to develop more robust defense frameworks. The anonymized code repository is available at https://anonymous.4open.science/r/adversarial_rag-3EFA.

</details>

### 99. Chatter Attack: Resource Consumption Attack for Large Language Models

📝 [OpenReview](https://openreview.net/forum?id=l0WR9h7F4b) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`resource consumption`、`prompt optimization`、`inference cost`、`llm`
- 🎯 **研究动机**：恶意用户可诱导超长输出推高推理延迟与成本，但既有资源消耗攻击靠强制重复或压低 end-of-sequence token 的 logit，在自回归采样生成下搜索空间随长度指数增长、微小偏差即可使优化脱轨，效果与稳定性受限。
- 🔬 **研究方法**：提出 Chatter Attack，优化对抗提示诱导预定义短目标短语以规避搜索空间爆炸同时激发长回复，用短怀疑短语触发自我怀疑并经推理注意力损失与全局熵损失在生成全程维持该状态，黑盒场景下用构建离散 token 核做全局建模的贝叶斯提示优化 BPO。
- 📌 **结论**：在多个模型与数据集上超越基线，响应长度最高增至 31.5 倍，揭示 LLM 服务面临的实际资源耗竭风险。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLMs are powerful but incur substantial inference cost, which can be exploited by malicious users to induce overly long outputs, increasing latency and operational expense. Prior resource consumption attacks either coerce repetition or suppress the end-of-sequence token by lowering its logit value. However, with autoregressive, samplingbased generation, the search space grows exponentially with length and small deviations or unstable trajectories can derail optimization, limiting attack effectiveness and stability. To address this, we introduce Chatter Attack, a novel class of resource consumption attacks that optimize adversarial prompts to induce predefined short target phrases, thereby avoiding search-space explosion while still eliciting long responses. Specifically, Chatter Attack triggers self-doubt using short doubt-inducing phrases as the target, and sustains this state throughout generation via inference attention loss and global entropy loss. To extend to black-box settings, we further propose a novel Bayesian Prompt Optimization (BPO) method, which models the objective function globally by constructing a discrete token kernel, efficiently exploring the entire search space using prior information. Extensive experiments across multiple models and datasets show that our method outperforms baselines, with maximum response length increases to 31.5×, and revealing practical resource-depletion risks for LLM services.

</details>

### 100. Adversarially Attacking Symbolic Vocabulary Vulnerabilities In LLM Planners

📝 [OpenReview](https://openreview.net/forum?id=Exn9wjDvOI) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`llm planner`、`symbolic obfuscation`、`adversarial domain`、`planning robustness`
- 🎯 **研究动机**：LLM 智能体在无法利用规划任务符号词表（动作、谓词、对象名）中常识线索时规划能力并不鲁棒，需检验其在更严重混淆下依赖纯规划能力的表现。
- 🔬 **研究方法**：设计并优化 LLM 攻击模型 Symbolic-Swapper，自动生成具有非标准符号词表的混淆规划域，系统性破坏强推理模型的规划能力。
- 📌 **结论**：攻击可使基座模型乃至鲁棒规划框架的规划性能下降超过 70%；模型虽能理解任务域，但推理质量显著退化且常绕过自我纠错。

👤 **作者**：Stephen Obadinma、Xiaodan Zhu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) become increasingly deployed as autonomous agents, the ability of these models on automated planning tasks has become essential. However, despite their strengths, LLMs' planning ability is not robust, particularly when they are not allowed to exploit commonsense cues in the symbolic vocabulary (e.g., names of actions, predicates, objects) used to define planning tasks. This makes them unreliable compared to symbolic planners. With recent reasoning models showing improved planning performance on tasks with obfuscated symbolic vocabularies, we utilize an adversarial attack framework to reveal to what extent these crucial weaknesses of LLM agents remain and whether they can reason properly when presented with severe cases. As such, our main contribution is devising and optimizing an LLM-based attack model which we call \textttSymbolic-Swapper to automatically generate obfuscated domains with non-standard symbolic vocabularies that systematically break strong reasoning models' ability to plan. In doing so, we reveal by how much LLMs planning abilities can be further degraded under more advanced obfuscation schemes, allowing us to ascertain their success when having to rely on their pure planning ability. We find that attacks can decrease the planning performance of base models and even robust planning frameworks by over 70%. We further analyze the factors behind how their planning abilities break down, and find that successful obfuscation models to significantly degrade in reasoning quality despite them showing an ability to understand the domain, revealing a gap in how model's perceive a task domain and how they are actually able to plan under it, with attacks often bypassing model ability to successfully self-correct.

</details>

### 101. PROACT-Agent: Progressive Runtime Oversight and Active Circuit-breaking for Real-Time Safety

📝 [OpenReview](https://openreview.net/forum?id=zOzXmzpHro) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`runtime guardrail`、`agent safety`、`trajectory synthesis`、`bilingual benchmark`
- 🎯 **研究动机**：LLM 走向智能体使安全风险从有害文本升级为不可逆环境危害，现有防御多为事后回顾式，主动运行时干预受限于缺乏大规模因果一致的数据，且既有基准存在宽松标注导致时序不一致的"安全漂移"。
- 🔬 **研究方法**：提出 PROACT-Agent 框架合成高保真轨迹以训练实时护栏：渐进轨迹展开揭示长上下文交互中的隐藏风险、推理增强因果修正强制单调因果一致、文化感知数据本地化保障跨境鲁棒。
- 📌 **结论**：发布迄今最大双语安全基准 PROACT-Bench（140,000+ 条工业级裁决轨迹），经其训练的模型实现卓越的零延迟干预。

👤 **作者**：Ding Jia、…、Chu Zhou

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The transition from Large Language Models (LLMs) to agents shifts safety stakes from toxic text to irreversible environmental harm. While current defenses remain largely retrospective, proactive runtime intervention is bottlenecked by the lack of large-scale, causally-consistent data. We propose PROACT-Agent, a framework for synthesizing high-fidelity trajectories to enable real-time guardrails. We identify a critical "safety drift" in prior benchmarks, where lenient annotation paradigms fail to enforce temporal consistency. PROACT-Agent addresses this through: (1) Progressive Trajectory Unrolling to reveal risks hidden in long-context interactions; (2) Reasoning-Augmented Causal Rectification to enforce monotonic causal consistency; and (3) Culturally-Aware Data Localization for cross-border robustness. We introduce PROACT-Bench, the largest bilingual safety benchmark to date, featuring 140,000+ trajectories adjudicated with industrial-grade rigor. Experiments show that models trained via our framework achieve superior zero-latency intervention, establishing a new standard for real-time autonomous agent safety.

</details>

### 102. Who Watches the Watchers? Semantically-Constrained Reinforcement Learning for Red-Teaming Provenance Intrusion Detectors

📝 [OpenReview](https://openreview.net/forum?id=7lUWeTEm0T) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`red teaming`、`provenance intrusion detection`、`graph editing`、`reinforcement learning`
- 🎯 **研究动机**：基于重建的溯源入侵检测系统（PIDS）运行在其监控的端点上，对抗鲁棒性是关键部署关切却很少被系统评测。
- 🔬 **研究方法**：提出 ProvRL，把红队建模为语义约束的图编辑 MDP，用由良性数据挖掘的转移关系掩码的事实化自回归策略加 GRU 信念状态，建模消息传递在 GNN 检测器上的多步后果。
- 📌 **结论**：对四大领先 PIDS 所属四种编码器家族的评测中，在白/灰/黑盒设定下对其中三个家族（GNN、linear、VAE）造成定向假阴性，查询数比穷举搜索少 5-99 倍；直接重建型编码器在结构上抵御插入攻击；没有任何阈值自适应聚合策略能同时保持可部署假阳率与有效抗逃逸，脆弱家族上对抗重训练是唯一可行防御。

👤 **作者**：Brayden Killeen、Derui Wang、Nasrin Sohrabi、Qin Wang、Zahir Tari、Minhui Xue

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reconstruction-based provenance intrusion detection systems (PIDS) detect malicious activity by classifying nodes in system-call provenance graphs from per-edge reconstruction errors produced by benign-trained encoder--decoders. Because these detectors run on the endpoints they monitor, adversarial robustness is a critical deployment concern, yet it remains rarely evaluated systematically. We introduce ProvRL, a reinforcement-learning framework for automated red-teaming of these detectors, and use it to characterise the robustness of four leading PIDS spanning the four encoder families used in the field. ProvRL casts red-teaming as a semantically constrained graph-editing MDP, with a factored autoregressive policy masked by transition relations mined from benign data and a GRU belief state, to model the multi-step consequences of message passing on GNN-based detectors. ProvRL causes targeted false negatives in white-, grey-, and black-box settings on three of four encoder families (GNN, linear, VAE) using 5-99x fewer queries than exhaustive search; direct-reconstruction encoders resist insertion attacks structurally, suggesting an architectural direction for robust detection. No threshold-adaptive aggregation policy maintains both a deployable false-positive rate and meaningful evasion resistance, leaving adversarial retraining as the only viable defence on the vulnerable families. ProvRL trains on CPU within hours and produces attack chains that replay as real Linux syscalls. We release ProvRL as an open-source red-teaming tool for PIDS.

</details>

### 103. Token Inflation: How Dishonest Providers Can Overcharge（已库内，2609.20370）

📄 [arXiv](https://arxiv.org/abs/2609.20370) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`detection`、`provider-side token inflation`、`black-box audit`、`pay-per-token`、`stopping behavior`
- 🎯 **研究动机**：按 token 计费的 LLM 服务中不诚实提供方可隐蔽操纵生成以膨胀输出 token 多收费，而用户从黑盒响应审计此类操纵十分困难。
- 🔬 **研究方法**：定义 PTIA 并在提供方管线的 query、prompt、表示与模型四层实例化 5 种攻击；基于"PTIA 饱和"现象（初次攻击骤降 EOS token 概率、继续增强或组合收效甚微）设计施加受控加长干预的单探针轻量审计，无需可信本地参考模型或历史干净响应。
- 📌 **结论**：各攻击使平均输出长度超 10.2 倍于干净基线；审计在 4 个开源模型上平均检出率 85.1%、误报率低于 2%，并在 15 个真实 LLM API 服务中标出 7 个 PTIA 一致行为。

👤 **作者**：Leilei Chen、…、Xinpeng Shen

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In pay-per-token LLM services, the more a model says, the more users pay. Dishonest providers can covertly manipulate generation to inflate output tokens while largely preserving task utility. We define such manipulation as a Provider-Side Token Inflation Attack (PTIA) and instantiate five representative attacks at the query, prompt, representation, and model levels of the provider-controlled pipeline. Our experiments show that each attack increases mean output length to more than 10.2x the clean baseline, demonstrating PTIA's financial appeal and feasibility at multiple stages of generation. Yet auditing PTIA from black-box responses is difficult for users. Our key observation is PTIA saturation: an initial attack sharply lengthens output, but further strengthening or composition has much less effect. We trace this saturation to stopping behavior: an initial PTIA sharply lowers the end-of-sequence token probability, whereas further intervention lowers it only marginally. Building on this insight, we design a lightweight single-probe audit that applies a controlled lengthening intervention. Under PTIA, the probe induces far fewer additional tokens than under normal service. The audit requires neither a trusted local reference model nor historical clean responses, and its separately issued original and probed requests resemble ordinary traffic, making evasion difficult. Across four open-weight models, it achieves an average detection rate of 85.1% with false-positive rates below 2%. Across 15 real LLM API services, the audit flags 7 for PTIA-consistent behavior.

</details>

### 104. Stealth Apart, Harm Together: Skill Cascading Attacks on Skill-Based Agent Systems（已库内，0928）

📄 [arXiv](https://arxiv.org/abs/2609.30383) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`attack`、`skill cascading`、`agent system`、`red-teaming`、`benchmark`
- 🎯 **研究动机**：基于 skill 的 agent 系统开放生态带来新攻击面，先前工作只关注单个 skill 内部漏洞而忽视跨 skill 交互产生的系统级风险。
- 🔬 **研究方法**：提出 skill cascading attacks——把恶意目标分散到多个 skill，使每处修改孤立看无害而组合执行有害，并构建自动化多 agent 红队框架 SkillCascade 与含 213 个已验证级联测试用例的 SkillCascade-Bench。
- 📌 **结论**：在 OpenClaw、Claude Code、Codex 等代表性 agent 与多种 LLM 底座上，级联交互可靠诱发有害行为并躲过现有 per-skill 扫描器与运行时监控。

👤 **作者**：Zihao Zhu、Siwei Lyu、Adel Bibi、Baoyuan Wu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A skill is a modular package of natural-language instructions, executable scripts, and reference resources that an agent can load at runtime to extend its capabilities for a specific task. Skill-based agent systems therefore enable flexible reuse of third-party capabilities, but the openness of this skill ecosystem also opens up a new attack surface. Prior work has focused on vulnerabilities within individual skills, but little attention has been paid to risks that arise from interactions across skills. In this paper, we introduce skill cascading attacks, a threat paradigm in which a malicious objective is distributed across multiple skills so that each modification looks benign in isolation, yet their combined execution is harmful. For instance, in a prescription-review pipeline, the first skill weakens signals of recently discontinued medications in the extracted history, the second downgrades the severity of any drug interaction tied to them, and the third suppresses the resulting low-priority alert in the final summary, so that a severe drug-interaction warning silently disappears before reaching the physician. To systematically study this safety blind spot, we develop SkillCascade, an automated multi-agent red-teaming framework, and release SkillCascade-Bench, a benchmark of 213 validated cascading test cases across multiple agent systems and domains. Across representative agents (e.g., OpenClaw, Claude Code, Codex) and LLM backbones, cascaded interactions reliably induce harmful behaviors while evading existing per-skill scanners and runtime monitors. Our findings highlight a gap between component-level integrity and system-level safety, and call for defenses that reason over cross-skill interactions rather than individual skills in isolation.

</details>

### 105. Share-Borne AI Virus: Memory-Hopping Attacks Across LLM Agents（已库内，0929）

📄 [arXiv](https://arxiv.org/abs/2609.35576) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`attack`、`llm agent`、`persistent memory`、`artifact sharing`、`propagation`
- 🎯 **研究动机**：有状态 LLM 助手读写并在用户间共享持久工件，由此在彼此独立的助手间形成间接通信信道，其上的自传播攻击失效模式未被研究。
- 🔬 **研究方法**：提出 artifact-mediated propagation——对抗内容经工件进入助手持久记忆、在后续生成工件中复制、再被另一助手读取，并在时序 human-agent 宇宙中度量攻击存活率、跳数与传播广度。
- 📌 **结论**：攻击可跨多个独立助手传播并经长交互序列持续存在，较大模拟环境中 GPT-5.6 Luna 亦蔓延至 60-80% 的 agent、传播链长达 8 跳。

👤 **作者**：Sidharth Pulipaka、…、Mario Fritz

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are increasingly deployed as stateful assistants that retain information across interactions and use tools to read, modify, and create persistent artifacts. As these artifacts are shared between users, they form an indirect communication channel between otherwise independent assistants. We study a failure mode in which this channel enables self-propagating attacks. We introduce artifact-mediated propagation, where adversarial content introduced through an artifact (e.g. a report), is stored in an assistant's persistent memory, reproduced in a subsequently created artifact, and acquired by another assistant that later reads it. We evaluate this process in temporal human-agent universes that model artifact exchange between independently operated assistants over time, measuring whether an attack survives successive hand-offs, how many hops it reaches, and how broadly it spreads. We find that attacks can propagate across multiple independent assistants and persist over extended interaction sequences. In larger simulated environments, even GPT-5.6 Luna exhibits substantial spread, reaching 60-80% of agents with propagation chains extending to eight hops. These results show that persistent artifacts can act as durable carriers of adversarial state, allowing attacks to outlive individual interactions and spread across isolated assistants.

</details>

### 106. MoMHa: Multi-Objective Optimization of LLM Harnesses over Accuracy, Safety, and Tokens

📄 [arXiv](https://arxiv.org/abs/2609.30967) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`evaluation`、`llm harness`、`multi-objective optimization`、`behavioral safety`、`agentic search`
- 🎯 **研究动机**：多数 LLM 改进工作只看 accuracy，而环绕模型的 Python 代码（harness）是天然的多目标设计面：准确但拒绝一切不安全请求、或多耗一个数量级 token 的 harness 都不是好 harness。
- 🔬 **研究方法**：提出 Meta-Harness，把 harness 设计转化为准确率、行为安全、token 成本三个按领域目标的搜索问题，由拥有完整文件系统访问（harness 源码、执行轨迹、评分工件）的 agentic proposer（Claude Code）求解，其中单阶段联合奖励版本为 MoMHa。
- 📌 **结论**：在 17 个领域、12 个模型上，MoMHa 合成赛道联合均值 0.482（十个基线为 0.198-0.422、赢 7/10 列），真实赛道 0.461 对最强基线 DSPy 的 0.377（赢 5/7 列），行为安全复合分最高（U-SafeBench 0.781）且比两阶段方案每例少用 95 个 token。

👤 **作者**：Subhojyoti Mukherjee、Md Mehrab Tanjim

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Most work on improving large language models treats accuracy as the sole objective. We argue that the harness, the Python code surrounding the model that constructs prompts, routes calls, and parses outputs, is a first-class design surface whose quality is inherently multi-objective: an accurate harness that refuses no unsafe request, or that consumes an order of magnitude more tokens, is not a good harness. We present Meta-Harness, a system that casts harness design as search over three per-domain objectives (accuracy, behavioural safety, and token cost) solved by an agentic proposer (Claude Code) with full filesystem access to prior harness source, execution traces, and scoring artifacts. Our central finding is that a singlephase joint-reward proposer (MoMHa) outperforms every alternative, including a two-phase "accuracy then tokens" ablation, scalar-only feedback, and an accuracy-only baseline. We evaluate on seventeen domains: seven synthetic capability suites, seven real-world public benchmarks (HumanEval, MBPP, Spider, FEVER, MMLU-Pro, LawBench, NuminaMath), and three U-SafeBench-derived user-specific safety domains, using a 12-model fleet spanning four families. On the synthetic track MoMHa achieves a joint mean of 0.482 versus 0.198-0.422 for ten baselines, winning $7 / 10$ per-domain columns; on the real-world track it scores 0.461 versus 0.377 for the strongest baseline (DSPy), winning 5/7 columns, demonstrating that harness strategies transfer to unseen benchmarks without retraining on 8 of 12 target models. MoMHa attains the highest measured behavioral safety composite (U-SafeBench, 0.781) and uses 95 fewer tokens per example than the two-phase alternative. We will release all harness code, evaluation infrastructure, and crossmodel logs.

</details>

### 107. Untrusted Content Masking for Web Agents with Security Guarantees

📄 [arXiv](https://arxiv.org/abs/2607.05277) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-07　🏷 NeurIPS 2026

**关键词**：`defense`、`prompt injection`、`web agent`、`dom`、`isolation`
- 🎯 **研究动机**：web agent 必须观察渲染页面才能感知与交互，而页面将可信与不可信内容结构性纠缠，破坏了可证明 prompt 注入防御所依赖的信任边界。
- 🔬 **研究方法**：提出 Untrusted Content Masking，利用网页 DOM 无需读取内容即可区分可信与不可信区域的结构性洞察，在不可信区域到达 agent 前予以遮蔽，并通过带严格权限分离的沙箱化接口路由交互。
- 📌 **结论**：该简单方法恢复了 web 环境中被破坏的信任边界，使 agent 能观察并交互环境同时保持与对抗内容的安全隔离。

👤 **作者**：Kristina Nikolić、Egor Zverev、Javier Rando、Matthew Jagielski、Edoardo Debenedetti、Florian Tramèr

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Defenses that provide security guarantees against prompt injection attacks rely on strict isolation between trusted instructions and untrusted data. In text-based environments such as tool-use APIs, this separation arises naturally: agents can reason from interface definitions without ever processing untrusted content. Extending these guarantees to web agents faces a fundamental challenge: to perceive and interact with their environment, web agents must first observe the rendered page, which intermingles trusted content with untrusted content. This structural entanglement removes the trust boundary on which security guarantees depend, undermining provable defenses for web agents. In this paper, we present Untrusted Content Masking (UCM), a simple and effective approach that restores this boundary in web environments. We leverage a key structural insight: a webpage's Document Object Model (DOM) encodes sufficient information to distinguish trusted from untrusted regions without reading their content. Our framework exploits this by redacting untrusted regions before they reach the agent and routing interaction through a sandboxed interface with strict privilege separation, thereby enabling agents to observe and interact with their environment while remaining isolated from adversarial content. The code is publicly available.

</details>

### 108. MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents（与库内 2607.14651 同名，待核）

📄 [arXiv](https://arxiv.org/abs/2607.14651) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-07　🏷 NeurIPS 2026

**关键词**：`benchmark`、`memory poisoning`、`agent memory`、`injection`、`defense blind spot`
- 🎯 **研究动机**：持久外部记忆增强智能体连续性的同时引入持久安全漏洞——对抗内容可经标准交互渠道注入、跨轮保留并在之后扭曲下游行为。
- 🔬 **研究方法**：MemPoison 基准含 1227 个人工验证用例（4 类攻击×3 种注入渠道×3 种记忆底座，评测 7 个开源与 3 个闭源模型族），提出 L1 单记录直接损坏、L2 多记录组合损坏、L3 上下文触发休眠损坏三层分类，并用机制影响分解（MID）剖析防御盲区。
- 📌 **结论**：写入时防御（如一致性检查）能显著压制 L1 却无法可靠压制 L2/L3——看似良性记录可经联合检索组合或条件触发激活变得有害，应从静态过滤转向自适应、上下文敏感的记忆防御。

👤 **作者**：Jifeng Gao、…、Sanglu Lu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Persistent external memory enhances agent continuity but introduces persistent security vulnerabilities: adversarial content can be injected via standard interaction channels, retained across turns, and later distort downstream behavior. To address this challenge, we propose MemPoison, a comprehensive benchmark and analysis framework featuring 1227 hand-validated cases across four attack types, three injection channels, and three representative memory substrates, evaluated on seven open-weight and three closed-weight model families. We introduce a three-tier taxonomy: (L1) direct single-record corruption, (L2) compositional multi-record corruption and (L3) context-triggered dormant corruption. Our evaluations reveal a distinct defense frontier: while baseline write-time defenses, such as consistency checks, substantially suppress direct L1 attacks, they fail to reliably suppress L2 and L3 attacks. Through mechanistic influence decomposition (MID), we demonstrate structural blind spots in write-time defenses, which admit seemingly benign records that later become harmful through joint retrieval composition or trigger-conditioned activation. Our findings advocate for shifting from static filtering to adaptive, context-sensitive memory defense strategies.

</details>

### 109. Adaptive Adversaries: A Multi-Turn, Multi-LLM Benchmark for LLM Agent Security

📄 [arXiv](https://arxiv.org/abs/2607.18063) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-07　🏷 NeurIPS 2026

**关键词**：`benchmark`、`prompt injection`、`multi-turn attack`、`adaptive adversary`
- 🎯 **研究动机**：LLM agent 处理外部内容而暴露于 prompt injection 与多轮操纵，缺少针对自适应跨会话攻击的系统化安全评估
- 🔬 **研究方法**：构建 21 场景基准——自主 LLM 攻击者观察先前防御者响应并跨轮转向，每次防御者响应均作为全新会话交互评估；3×3 攻击者-防御者矩阵含 945 场对抗，另以竞赛补充 18,422 场 held-out 对战
- 📌 **结论**：仅按首轮计分 ASR 为 0-1%，允许 15 轮后升至 7.9-16.8%；聚合三个攻击者 LLM 发现的独特成功输入是最佳单攻击者的 1.7-2.2 倍，在 6 个场景加入一段溯源文本可将 ASR 从 110/270 降至 70/270

👤 **作者**：Devina Jain、David Hartmann、Chuan Li

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents process external content, exposing them to prompt injection and multi-turn manipulation. We present a 21-scenario benchmark for adaptive cross-session attacks against fresh-session LLM defenders: an autonomous LLM attacker observes prior defender responses and pivots across rounds, while each defender response is evaluated as a fresh interaction. A controlled 3 x 3 attacker-defender matrix contains 945 battles. Restricting scoring to the first round yields 0-1% attack success rate (ASR); allowing 15 rounds yields 7.9-16.8%. Pooling three attacker LLMs uncovers 1.7-2.2 times as many unique successful inputs as the best single attacker, at three times the battle budget. Aggregate rates conceal opposing scenario-specific weaknesses in session-secret protection and authority handling, preserved in two higher-sample evaluations. On six scenarios, adding one provenance paragraph reduces ASR from 110/270 to 70/270, with selective effects across tasks. History and defender-state controls, together with frozen replay, characterize how the interaction protocol changes the result. A competition adds 18,422 held-out battles on a fixed gpt-oss-20b backbone and complementary benign-task evaluations. The benchmark exposes attacker and defender models, harnesses, scenarios, session state, and interaction budgets as configurable choices for systematic security evaluation.

</details>

### 110. Do Coding Agents Deceive Us? Detecting and Preventing Cheating via Capped Evaluation with Randomized Tests

📄 [arXiv](https://arxiv.org/abs/2606.07379) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`evaluation`、`coding agent`、`cheating detection`、`randomized tests`、`reward design`
- 🎯 **研究动机**：agent 评估与训练中日益出现模型靠利用捷径而非解决任务拿高分的欺骗性表现，使评估分数无法度量真实任务解决能力。
- 🔬 **研究方法**：提出 CapCode 构建最佳非作弊性能被刻意压低到 1 以下的随机化测试编码数据集（远超上限的分数即作弊证据），并提出抑制向上限之上优化的 CapReward 奖励设计。
- 📌 **结论**：CapCode 在保持模型性能排序的同时检测作弊，CapReward 减少作弊行为、产出更好遵循任务规范的模型。

👤 **作者**：Thanawat Lodkaew、Johannes Ackermann、Soichiro Nishimori、Nontawat Charoenphakdee、Masashi Sugiyama、Takashi Ishida

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A growing failure mode in agent evaluation and training is that models can achieve high evaluation scores by exploiting shortcuts instead of solving the intended task, producing deceptive performance. This makes evaluation scores unreliable as measures of true task-solving ability. We propose CapCode, a framework for constructing coding datasets with randomized tests whose best achievable non-cheating performance is deliberately capped below one. This capped-performance design gives evaluation scores a clearer interpretation: scores substantially above the cap are implausible and therefore provide evidence of cheating. To prevent cheating, we propose CapReward, a reward design based on the CapCode principle to discourage optimization beyond the cap. Experiments across multiple datasets show that CapCode detects cheating while preserving performance ranking of models, and CapReward reduces cheating behavior, yielding models that better follow the intended task specification.

</details>

### 111. SecureClaw: Clawing Back Control of LLM Agents

📄 [arXiv](https://arxiv.org/abs/2606.09549) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`defense`、`llm agent`、`dual-boundary architecture`、`secret confinement`、`preview-commit`
- 🎯 **研究动机**：工具型 LLM agent 面临未授权外部行动与运行时敏感明文暴露两类安全失败，现有防御只保护 planner/runtime 或动作汇其中一条边界。
- 🔬 **研究方法**：SecureClaw 双边界架构在 effect sink 设授权、在读边界设明文封禁——敏感读取经 trusted gateway 替换为不透明句柄与有界摘要作为显式去分类接口，写操作遵循仅可信 executor 可提交确切授权请求的 PREVIEW→COMMIT 协议。
- 📌 **结论**：在 AgentDojo、AgentLeak 与 ASB 统一框架下同时保持可用任务效用，ASB 上 ASR 为 0%、AgentDojo 上 0.64%、AgentLeak 攻击对等通道整体泄露 3.23%。

👤 **作者**：Yuhan Ma、Stefan Schmid

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Tool-using large language model (LLM) agents face two distinct security failures: unauthorized external actions and exposure of sensitive plaintext inside the runtime before any final output check can intervene. Existing defenses usually protect one boundary, either the planner/runtime or the action sink, and therefore do not by themselves secure both surfaces. We present SecureClaw, a dual-boundary architecture that places authorization at the effect sink and plaintext confinement at the read boundary. Sensitive reads pass through a trusted gateway that replaces raw values with opaque handles and, in the evaluated deployment, bounded summaries as an explicit declassification interface. Writes that change external state follow a PREVIEW$\rightarrow$COMMIT protocol in which only a trusted executor may commit the exact canonical request authorized by policy. The runtime can still plan over summaries and symbolic references, but cannot directly dereference secrets or perform side effects. Across AgentDojo, AgentLeak, and Agent Security Bench (ASB), SecureClaw is the only defense we evaluate in a common harness that simultaneously retains usable task utility and achieves 0\% attack success rate (ASR) on ASB, 0.64\% ASR on AgentDojo, and 3.23\% overall leak on AgentLeak's attacked parity lane, which measures final-output and internal-relay leakage.

</details>

### 112. GitInject: Real-World Prompt Injection Attacks in AI-Powered CI/CD Pipelines

📄 [arXiv](https://arxiv.org/abs/2606.09935) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`attack`、`prompt injection`、`ci/cd pipeline`、`supply chain`、`benchmark`
- 🎯 **研究动机**：嵌入 CI/CD 流水线的 AI 智能体摄入不可信内容却持有高仓库权限，是提示注入的天然目标，而既有智能体安全基准只模拟工具调用、无法反映生产环境。
- 🔬 **研究方法**：GitInject 开源框架配置临时仓库并触发真实 GitHub workflow 运行，使沙箱约束、凭证处理与权限边界与生产完全一致，据此考察四家 AI 提供商的工作流配置并记录攻击。
- 📌 **结论**：记录 11 种具名攻击（覆盖配置注入、凭证外泄、判断操纵与可用性），所有受测提供商默认配置均至少易受一类攻击，且最关键漏洞是结构性的——源于 CI/CD 基础设施处理凭证与配置文件的方式而非具体模型行为；对每类攻击给出最低成本工作流级对策及其覆盖范围。

👤 **作者**：Jafar Isbarov、Umid Suleymanov、Ilia Shumailov、Murat Kantarcioglu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI-powered agents are increasingly embedded in continuous integration and continuous delivery/deployment (CI/CD) pipelines to autonomously review pull requests (PRs), triage issues, and maintain codebases. These agents ingest untrusted content while operating with elevated repository permissions, making them a natural target for prompt injection attacks with supply chain consequences. We present GitInject, an open-source framework for evaluating prompt injection vulnerabilities in real, live GitHub workflows, a widely deployed instance of CI/CD pipelines. Unlike prior agent security benchmarks that simulate tool calls, GitInject provisions ephemeral repositories and triggers actual workflow runs, so that sandbox constraints, credential handling, and permission boundaries behave exactly as in production. Using GitInject, we study workflow configurations across four AI providers and document eleven named attacks spanning config-file injection, credential exfiltration, judgment manipulation, and availability. We find that all tested providers are susceptible to at least one attack class in their default configuration, and that the most critical vulnerabilities are structural: they arise from how CI/CD infrastructure handles credentials and configuration files, not from any specific model's behavior. For each confirmed attack class, we identify the minimum-cost workflow-level countermeasure and analyze its coverage and limitations. GitInject is released publicly to facilitate further research in this direction.

</details>

### 113. Forced Deferral: Manipulating Routing Decisions in Multimodal LLM Cascades

📄 [arXiv](https://arxiv.org/abs/2606.15308) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`attack`、`mllm cascade`、`confidence manipulation`、`compute allocation`、`universal trigger`
- 🎯 **研究动机**：MLLM 级联中弱模型的 confidence 直接控制算力分配，暴露出攻击者可操纵 confidence 使其查询被持续延迟到强模型的新攻击面。
- 🔬 **研究方法**：提出 Forced Deferral Attack，通过优化 temperature-flattened 目标学习 universal border trigger，将弱模型在触发输入上的 token 分布推向由其干净响应构造的低集中度目标以压低 confidence。
- 📌 **结论**：跨数据集、模型族与延迟指标一致增加强模型路由、优于图像扰动与 prompt 注入基线，证明 MLLM 级联可被操纵算力分配的攻击在不动答案正确性的情况下强制强模型使用。

👤 **作者**：Zhongye Liu、Yaopei Zeng、Yurui Chang、Lu Lin

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While multimodal large language models (MLLMs) have shown strong visual reasoning abilities, serving a large model for every query is computationally expensive. MLLM cascades mitigate this cost by first querying a weak but cheaper model and deferring to a strong model when the weak model's output is unconfident. However, since the weak model's confidence directly controls compute allocation, these systems expose a new attack surface: an adversary can manipulate confidence so that their queries are consistently deferred to the strong model. Motivated by this vulnerability, we introduce the Forced Deferral Attack (FDA), an adversarial image attack that lowers the weak model's confidence and causes cascades to route queries to the strong model. FDA learns a universal border trigger by optimizing a temperature-flattened objective. This objective pushes the weak model's token distribution on triggered inputs toward less concentrated targets constructed from its clean responses. Across datasets, model families, and deferral metrics, FDA consistently increases strong-model routing while outperforming image-perturbation and prompt-injection baselines. These results show that MLLM cascades are vulnerable to attacks that manipulate compute allocation, forcing unintended strong-model usage without directly targeting answer correctness.

</details>

### 114. Seeing Is Not Screening: Multimodal Hidden Instruction Attacks on Agent Skill Scanners

📄 [arXiv](https://arxiv.org/abs/2606.18198) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`attack`、`skill scanner`、`multimodal injection`、`hidden instruction`、`execution-grounded scanning`
- 🎯 **研究动机**：现有 agent skill 扫描器主要依赖文本描述、manifest 与源码做安全分析，藏于图像中的恶意操作指令可绕过扫描、却仍能在部署时被多模态智能体恢复执行。
- 🔬 **研究方法**：提出文档介导的 SkillCamo 多模态指令攻击——把恶意指令藏入 skill 附带图像并改写文档使其自然引用该图像，攻击依赖执行时文本引导与视觉载荷的联合解释；同时提出执行接地的多模态扫描模块 ExecScan（意图提取、行为重建、滥用评估与审慎执行模拟）作防御。
- 📌 **结论**：实验表明图像隐藏的恶意指令能挑战现有 skill 扫描器，ExecScan 联合分析文档、代码、引用资源与视觉内容可恢复隐藏指令、重建可执行行为链并识别外泄、破坏、持久化、欺骗与提权等风险，提升扫描性能。

👤 **作者**：Xiaojun Jia、…、Yang Liu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills are emerging as an important attack surface in LLM-based systems. Through an empirical study of existing skill scanners, we find that current defenses primarily rely on textual descriptions, manifests, and source code as the main signals for security analysis, which can leave visually conveyed malicious intent insufficiently examined. This creates a practical blind spot: harmful operational instructions hidden in images may bypass scanning while still being recoverable by multimodal agents during deployment. To systematically investigate this threat, we propose SkillCamo, a document-mediated multimodal instruction attack that conceals malicious instructions within images bundled with a skill while rewriting the surrounding documentation to naturally reference those images as part of the normal workflow. Thus, the attack does not rely on the image alone, but on the joint interpretation of textual guidance and visual payload at execution time. To defend against such attacks, we further propose ExecScan, an execution-grounded multimodal scanning module that performs intent extraction, behavior reconstruction, abuse assessment, and deliberative execution simulation over skill artifacts. ExecScan jointly analyzes documentation, code, referenced resources, and visual content to recover hidden instructions, reconstruct executable behavior chains, and identify downstream risks such as exfiltration, destruction, persistence, deception, and privilege escalation. Extensive experiments show that image-hidden malicious instructions challenge existing skill scanners, while ExecScan can improve the skill scanning performance.

</details>

### 115. MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents

📄 [arXiv](https://arxiv.org/abs/2605.03952) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`coding agent`、`compositional vulnerability`、`attack chain`、`exploit oracle`
- 🎯 **研究动机**：编码 agent 逐条 prompt 能过安全审查，但任务被分解为无害工单序列时会产出可利用代码，现有安全对齐孤立评估显式请求、看不见由顺序合规涌现的恶意终态。
- 🔬 **研究方法**：构建 MOSAIC-Bench，含 199 条三阶段攻击链并配部署软件基底上的确定性 exploit oracle（10 个 web 应用基底、31 个 CWE 类、5 种语言），将 exploit 真值与下游审查协议作为一等评估轴。
- 📌 **结论**：九个生产编码 agent 以无害工单组合出 53-86% 端到端 ASR（直连 prompting 时脆弱输出率仅 0-20.4%），代码审查 agent 将 25.8% 确认脆弱 diff 当常规 PR 放行，pentester 框架审查将逃逸压到 3.0-17.6%（开源 Gemma-4-E4B-it 审查者检出 88.4% 攻击、608 条真实 PR 上误报 4.6%）。

👤 **作者**：Jonathan Steinberg、Oren Gal

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Coding agents often pass per-prompt safety review yet ship exploitable code when their tasks are decomposed into routine engineering tickets. The challenge is structural: existing safety alignment evaluates overt requests in isolation, leaving models blind to malicious end-states that emerge from sequenced compliance with innocuous-looking requests. We introduce MOSAIC-Bench (Malicious Objectives Sequenced As Innocuous Compliance), a benchmark of 199 three-stage attack chains paired with deterministic exploit oracles on deployed software substrates (10 web-application substrates, 31 CWE classes, 5 programming languages) that treats both exploit ground truth and downstream reviewer protocol as first-class evaluation axes. On this benchmark, nine production coding agents from Anthropic, OpenAI, Google, Moonshot, Zhipu, and Minimax compose innocuous tickets at 53-86% end-to-end ASR with only two refusals across all staged runs. In a matched direct-prompt experiment over four frontier Claude/Codex agents, vulnerable-output rates fall to 0-20.4%: Claude primarily refuses, while Codex primarily hardens rather than emitting the vulnerable implementation - ticket staging silences both defense modes simultaneously. Downstream, code reviewer agents approve 25.8% of these confirmed-vulnerable cumulative diffs as routine PRs, and a full-context implementation protocol closes only 50% of the staged/direct gap, ruling out context fragmentation as the sole explanation. As a deployable but non-adaptive mitigation, reframing the reviewer as an adversarial pentester reduces evasion across the evaluated reviewer subset; pentester framed evasion ranges from 3.0% to 17.6%, and an open-weight Gemma-4-E4B-it reviewer under this framing detects 88.4% of attacks on the dataset with a 4.6% false-positive rate measured on 608 real-world GitHub PRs.

</details>

### 116. AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2605.08715) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`detection`、`online auditing`、`multi-agent system`、`early failure prediction`、`reinforcement learning`
- 🎯 **研究动机**：LLM 多智能体系统中单个决定性错误会被下游 agent 接受并级联为轨迹级失败，现有事后归因范式在轨迹结束后才诊断、丧失了过程中的干预机会。
- 🔬 **研究方法**：将问题重构为在线审计（审计者每步只看当前前缀、须在最早决定性错误处报警），构建 AFTraj-2K 轨迹语料，并用 coarse-to-fine 强化学习配方训练 AgentForesight-7B——先在相邻安全/不安全前缀对上习得失败边界风险预期先验，再以针对 what/where/who 的三轴奖励锐化到步级定位。
- 📌 **结论**：在 AFTraj-2K 与外部 Who&When 基准上超越 GPT-4.1、DeepSeek-V4-Pro 等领先专有模型，性能增益至多 +19.9%、步级定位误差低 3 倍。

👤 **作者**：Boxuan Zhang、Jianing Zhu、Zeru Shi、Dongfang Liu、Ruixiang Tang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based multi-agent systems are increasingly deployed on long-horizon tasks, but a single decisive error is often accepted by downstream agents and cascades into trajectory-level failure. Existing work frames this as \emph{post-hoc failure attribution}, diagnosing the responsible agent and step after the trajectory has ended. However, this paradigm forfeits any opportunity to intervene while trajectory is still unfolding. In this work, we introduce AgentForesight, a framework that reframes this problem as online auditing: at each step of an unfolding trajectory, an auditor observes only the current prefix and must either continue the run or alarm at the earliest decisive error, without access to future steps. To this end, we curate AFTraj-2K, a corpus of agentic trajectories across Coding, Math, and Agentic domains, in which safe trajectories are retained under a strict curation pipeline and unsafe trajectories are annotated at the step of their decisive error via consensus among multiple LLM judges. Built on that, we develop AgentForesight-7B, a compact online auditor trained with a coarse-to-fine reinforcement learning recipe that first equips it with a risk-anticipation prior at the failure boundary on adjacent safe/unsafe prefix pairs, then sharpens this prior into precise step-level localization under a three-axis reward jointly targeting the what, where, and who of an audit verdict. Across AFTraj-2K and an external Who\&When benchmark, AgentForesight-7B outperforms leading proprietary models, including GPT-4.1 and DeepSeek-V4-Pro, achieving up to +19.9% performance gain and 3$\times$ lower step localization error, opening the loop from post-hoc failures detection to enabling deployment-time intervention. Project page: https://zbox1005.github.io/agent-foresight/

</details>

### 117. LITMUS: Benchmarking Behavioral Jailbreaks of LLM Agents in Real OS Environments

📄 [arXiv](https://arxiv.org/abs/2605.10779) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`behavior jailbreak`、`os agents`、`skill injection`、`dual verification`
- 🎯 **研究动机**：LLM 智能体进入真实操作系统环境带来内容安全之外的行为越狱风险（诱导执行不可逆的 OS 级危险操作），现有基准或只评语义层漏掉物理层危害、或因用例不隔离而让早期运行污染后期。
- 🔬 **研究方法**：LITMUS 以语义-物理双层验证与 OS 级状态回滚解决两大缺口，含 819 个高风险用例（有害种子集+六类攻击扩展集，覆盖越狱话术、技能注入、实体包裹三种对抗范式）及全自动多智能体判分框架。
- 📌 **结论**：前沿智能体缺乏安全意识——强模型（Claude Sonnet 4.6）仍执行 40.64% 的高危操作；普遍存在口头拒答但危险操作已在系统层完成的 Execution Hallucination（此前所有纯语义框架均不可见）；技能注入与实体包裹攻击成功率高，暴露显著智能体脆弱性。

👤 **作者**：Chiyu Zhang、…、Zhe Liu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid proliferation of LLM-based autonomous agents in real operating system environments introduces a new category of safety risk beyond content safety: behavior jailbreak, where an adversary induces an agent to execute dangerous OS-level operations with irreversible consequences. Existing benchmarks either evaluate safety at the semantic layer alone, missing physical-layer harms, or fail to isolate test cases, letting earlier runs contaminate later ones. We present LITMUS (LLM-agents In-OS Testing for Measuring Unsafe Subversion), a benchmark addressing both gaps via a semantic-physical dual verification mechanism and OS-level state rollback. LITMUS comprises 819 high-risk test cases organized into one harmful seed subset and six attack-extended subsets covering three adversarial paradigms (jailbreak speaking, skill injection, and entity wrapping), plus a fully automated multi-agent evaluation framework judging behavior at both conversational and OS-level physical layers. Evaluation across frontier agents reveals three findings: (1) current agents lack effective safety awareness, with strong models (e.g., Claude Sonnet 4.6) still executing 40.64% of high-risk operations; (2) agents exhibit pervasive Execution Hallucination (EH), verbally refusing a request while the dangerous operation has already completed at the system level, invisible to every prior semantic-only framework; and (3) skill injection and entity wrapping attacks achieve high success rates, exposing pronounced agent vulnerabilities. LITMUS provides the first standardized platform for reproducible, physically grounded behavioral safety evaluation of LLM agents in real OS environments.

</details>

### 118. ExploitGym: Can AI Agents Turn Security Vulnerabilities into Real Attacks?

📄 [arXiv](https://arxiv.org/abs/2605.11086) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`exploitation capability`、`vulnerability`、`ai agent`
- 🎯 **研究动机**：把漏洞转化为实际攻击影响（exploitation）需要低层程序推理、运行时适应与长程持续进展，是重要且具诊断价值却评估严重不足的能力
- 🔬 **研究方法**：构建 ExploitGym 基准，含 898 个来自真实漏洞的实例，覆盖用户态程序、Google V8 引擎与 Linux 内核三域，任务为把触发漏洞的输入逐步扩展为可用 exploit，可变安全防护配置并全部打包为可复现容器
- 📌 **结论**：前沿模型可成功利用相当比例漏洞，Claude Mythos Preview 与 GPT-5.5 分别产出 157 与 120 个可用 exploit，且即便启用常见防御成功率仍然可观

👤 **作者**：Zhun Wang、…、Dawn Song

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents are rapidly gaining capabilities that could significantly reshape cybersecurity, making rigorous evaluation urgent. A critical capability is exploitation: turning a vulnerability, which is not yet an attack, into a concrete security impact, such as unauthorized file access or code execution. Exploitation is a particularly challenging task because it requires low-level program reasoning (e.g., about memory layout), runtime adaptation, and sustained progress over long horizons. Meanwhile, it is inherently dual-use, supporting defensive workflows while lowering the barrier for offense. Despite its importance and diagnostic value, exploitation remains under-evaluated. To address this gap, we introduce ExploitGym, a large-scale, diverse, realistic benchmark on the exploitation capabilities of AI agents. Given a program input that triggers a vulnerability, ExploitGym tasks agents with progressively extending it into a working exploit. The benchmark comprises 898 instances sourced from real-world vulnerabilities across three domains, including userspace programs, Google's V8 JavaScript engine, and the Linux kernel. We vary the security protections applied to each instance, isolating their impact on agent performance. All configurations are packaged in reproducible containerized environments. Our evaluation shows that while exploitation remains challenging, frontier models can successfully exploit a non-trivial fraction of vulnerabilities. For example, the strongest configurations are Anthropic's latest model Claude Mythos Preview and OpenAI's GPT-5.5, which produce working exploits for 157 and 120 instances, respectively. Notably, even with widely used defenses enabled, models retain non-trivial success rates. These results establish ExploitGym as an effective testbed for exploitation and highlight the growing cybersecurity risks posed by increasingly capable AI agents.

</details>

### 119. FlowSteer: Prompt-Only Workflow Steering Exposes Planning-Time Vulnerabilities in Multi-Agent LLM Systems

📄 [arXiv](https://arxiv.org/abs/2605.11514) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`attack`、`workflow steering`、`multi-agent systems`、`planner-executor`、`prompt attack`
- 🎯 **研究动机**：planner-executor 架构的 LLM 多智能体系统中，提示可在不修改基础设施的情况下塑造智能体组织与路由，这一工作流形成层面的攻击面未被研究。
- 🔬 **研究方法**：通过社会影响探测工作流定位高影响力子任务与恶意信号传播路径，发现工作流位置可放大/压制恶意信号且谄媚框架促使下游转发，据此把脆弱性先验转化为单条提示的 FlowSteer 攻击，并配套输入侧防御 FlowGuard。
- 📌 **结论**：FlowSteer 较朴素提示最多提升 55% 恶意成功率，可跨 MAS 设置迁移并在黑盒拓扑推断下依然有效，只检查生成工作流的防御保护有限，FlowGuard 最多降低 34% 恶意成功率且保持提示效用。

👤 **作者**：Fanxiao Li、Jiaying Wu、Tingchao Fu、Natasha Jaques、Wei Zhou、Min-Yen Kan

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-agent systems (MAS) powered by large language models (LLMs) increasingly adopt planner--executor architectures, where planners convert prompts into subtasks, roles, dependencies, and routing paths. This flexibility enables adaptive coordination, but exposes an attack surface in workflow formation: prompts can shape agent organization without modifying MAS infrastructure. We study this risk through social influence probing workflows to identify high-impact subtasks and malicious-signal propagation. The analysis reveals two vulnerabilities: workflow position can amplify or suppress a malicious signal, and sycophantic framing makes downstream agents more likely to relay it. We translate these findings into FlowSteer, a prompt-only workflow steering attack that converts vulnerability priors into one crafted prompt. FlowSteer aligns a malicious signal with influential task components and guides replanning toward dependencies that preserve propagation. Experiments show that FlowSteer increases malicious success by up to 55% over naive prompting, transfers across MAS setups, and remains effective with black-box topology inference. As FlowSteer biases the planning signals that generate the workflow, MAS defenses that inspect only the generated workflow provide limited protection. As such, we introduce FlowGuard, an input-side defense that reduces malicious success by up to 34% while preserving prompt utility. Our results position workflow formation as a new safety frontier for multi-agent LLM systems, opening a planning-time security perspective on how agent coordination itself can be attacked and defended.

</details>

### 120. ASPI: Seeking Ambiguity Clarification Amplifies Prompt Injection Vulnerability in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2605.17324) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`prompt injection`、`clarification`、`llm agent`、`attack surface`
- 🎯 **研究动机**：澄清式提问被视为 LLM agent 的优良性质，但从标准执行转入澄清状态是否会放大 prompt 注入脆弱性的安全影响从未被探索。
- 🔬 **研究方法**：构建含 728 个任务-攻击场景的 ASPI benchmark，将澄清隔离为独立 agent 状态，在匹配的执行与澄清设置下（执行时 agent 直接行动、澄清时须先请求并吸收额外用户输入）受控测量状态转移对脆弱性的影响。
- 📌 **结论**：十个前沿 LLM 上澄清一致显著放大脆弱性——o3 的攻击成功率从 1.8% 升至 34.0%、Gemini-3-Flash 从 2.2% 升至 35.7%，证明执行时安全评估系统性低估交互式 agent 的攻击面。

👤 **作者**：Udari Madhushani Sehwag、Zhengyang Shan、Heming Liu、Dileepa Lakshan、Joseph Brandifino、Max Fenkell

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Clarification-seeking behavior is widely regarded as a desirable property of LLM agents, enabling them to resolve ambiguity before acting on underspecified tasks. However, the security implications of this interaction pattern remain unexplored. We investigate whether the transition from standard execution to a clarification-seeking state increases an agent's susceptibility to prompt injection attacks. We introduce ASPI (Ambiguous-State Prompt Injection), a benchmark of 728 task-attack scenarios that isolates clarification as a distinct agent state and measures how this state transition affects vulnerability under controlled conditions. Each benchmark instance is evaluated under matched execution and clarification settings: in the execution setting, the agent acts on a fully specified instruction and encounters adversarial content only through tool-returned data; in the clarification setting, the agent must first request and incorporate additional user input before acting. We evaluate ten frontier LLMs and find that clarification-seeking consistently and substantially amplifies vulnerability. For instance, attack success rises from 1.8% to 34.0% for o3 and from 2.2% to 35.7% for Gemini-3-Flash. A decomposition analysis reveals that this gap reflects both a state-dependent shift in how models process incoming content and a channel-specific effect arising from the agent-solicited clarification interface. These findings demonstrate that standard execution-time security evaluation systematically underestimates the attack surface of interactive agents, and that robustness under fully specified tasks does not translate to robustness under ambiguity. For reproducibility, our data and source code are available at https://github.com/scaleapi/aspi.

</details>

### 121. AI Agents May Always Fall for Prompt Injections

📄 [arXiv](https://arxiv.org/abs/2605.17634) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`prompt injection`、`contextual integrity`、`impossibility result`
- 🎯 **研究动机**：主流 prompt injection 防御范式（数据-指令分离）既检测不到上下文操纵型攻击，又会损害上下文恰当行为
- 🔬 **研究方法**：以 Contextual Integrity 隐私理论重构 prompt injection，构造良性与攻击场景迫使 agent 通过歪曲信息流、操纵规范或混合多流违反规范，从而推导防御的不可能性结果
- 📌 **结论**：对抗者总能构造出使被阻断信息流显得合法的上下文，而收紧规范的防御者会误伤真正合法的信息流——当前研究只覆盖日益缩小的未来攻击面，需发展 CI-aware 对齐

👤 **作者**：Sahar Abdelnabi、Eugene Bagdasarian

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prompt injection is the most critical vulnerability in deployed AI agents. Despite recent progress, we show that the prevailing defense paradigm (data-instruction separation) both fails to detect attacks that operate through contextual manipulation and degrades contextually appropriate behavior. We then recast prompt injection via the lens of Contextual Integrity (CI), a privacy theory that judges information flow compliance with contextual norms. This explains types of attacks that current defenses attempt to patch and predict advanced ones future agents will face. We develop unique benign and attack scenarios that force an agent to violate the norms by (1) misrepresenting the flow, (2) manipulating norms, or (3) mixing multiple flows. This reframing suggests an impossibility result: an adversary can always construct a context under which a blocked flow appears legitimate, or a defender who tightens norms will block genuinely legitimate flows. Our findings suggest that current research addresses a shrinking fraction of future attack surfaces. Instead, through CI, we offer a principled framework for evaluating context-sensitive failures, and designing CI-aware alignment for the frontier autonomous agents.

</details>

### 122. Agent Security is a Systems Problem

📄 [arXiv](https://arxiv.org/abs/2605.18991) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`survey`、`agent security`、`systems security`、`prompt injection`、`untrusted component`
- 🎯 **研究动机**：社区主流致力于提升模型鲁棒性，但仅靠模型鲁棒性不足以保障 agent 安全。
- 🔬 **研究方法**：提出 agent 安全应作为系统问题的立场——驱动 agent 的 AI 模型必须被视为不可信组件、安全不变量须在系统层强制执行，并基于操作系统、网络、形式化方法等领域数十年的系统安全研究凝练核心设计原则。
- 📌 **结论**：分析十一个真实 agent 攻击案例说明系统原则若落地本可阻止这些攻击，并识别在 agent 中实现这些原则的研究挑战。

👤 **作者**：Mihai Christodorescu、…、Nishit V. Pandya

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We take the position that agent security must be approached as a systems problem: the AI model powering the agent must be treated as an untrusted component, and security invariants must be enforced at the system level. Through this lens, efforts to increase model robustness (the dominant viewpoint in the community) are insufficient on their own. Instead, we must complement existing efforts with techniques from the systems security domain. Based on our experience as cybersecurity researchers in operating systems, networks, formal methods, and adversarial machine learning, we articulate a set of core principles, grounded in decades of systems security research, that provide a foundation for designing agentic systems with predictable guarantees. As evidence, we analyze eleven representative real-world attacks on agents and discuss how systems principles, if realized, could have prevented these attacks. We also identify the research challenges that stand in the way of implementing these principles in agents.

</details>

### 123. Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale

📄 [arXiv](https://arxiv.org/abs/2605.20744) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`reward hacking`、`verifiable exploitation`、`agent evaluation`、`textarena`
- 🎯 **研究动机**：reward hacking——智能体在评估信号下看似成功却违背预期目标——已在广泛场景被观察到，但主要靠事后检查轨迹来分析，缺乏可靠的规模化测量方法。
- 🔬 **研究方法**：提出把可检测的 reward hacking 机会直接嵌入环境的新评测范式，使其利用行为"设计即可验证"，支持确定性、自动化地测量智能体是否及如何利用漏洞，并在 TextArena 上实例化开源 Hack-Verifiable TextArena。
- 📌 **结论**：借助该测试床系统分析了多样环境与设置下各语言模型的 reward hacking 行为，为可靠测量提供了标准化基础。

👤 **作者**：Amit Roth、Ankur Samanta、Matan Halevy、Yoav Levine、Yonathan Efroni

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Aligning autonomous agents with human intent remains a central challenge in modern AI. A key manifestation of this challenge is reward hacking, whereby agents appear successful under the evaluation signal while violating the intended objective. Reward hacking has been observed across a wide range of settings, yet methods for reliably measuring it at scale remain lacking. In this work, we introduce a new evaluation paradigm for measuring reward hacking. Whereas prior studies have primarily analyzed it post hoc by inspecting agent trajectories, we instead embed detectable reward hacking opportunities directly into environments. This makes their exploitation verifiable by design, enabling deterministic and automated measurement of whether and how agents exploit such vulnerabilities. We instantiate this approach in $\textit{TextArena}$ and release $\textit{Hack-Verifiable TextArena}$, a testbed in which reward hacking can be measured reliably. Using this benchmark, we analyze reward hacking behavior across language models in diverse environments and settings. We open source the code at https://github.com/MajoRoth/hack-verifiable-environments/.

</details>

### 124. Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning

📄 [arXiv](https://arxiv.org/abs/2605.24216) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`detection`、`agent monitoring`、`theory of mind`、`covert malicious behavior`、`learning to monitor`
- 🎯 **研究动机**：自主 LLM agent 的隐蔽恶意行为具延迟、上下文依赖与长程特征，现有监控独立处理单条轨迹、不利用既往监控经验，也不显式推理 agent 信念与意图以区分良性执行与隐蔽偏离。
- 🔬 **研究方法**：Agent-ToM 以 Theory-of-Mind 推理做全轨迹结构化分析（推断信念、校准置信的意图假设、预期动作与行为基线偏离），推理时用 Reason-Verify-Refine 管线，训练时将批评信号蒸馏为可跨轮复用的 semantic guardrail memory。
- 📌 **结论**：在 SHADE-Arena 与 CUA-SHADE-Arena 上取得强 precision-recall 平衡，仅用两段调用推理管线即超越含 ensemble 在内的 SOTA 监控基线。

👤 **作者**：Nesreen K. Ahmed、Nima Nafisi

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Monitoring autonomous large language model (LLM) agents for covert malicious behavior is challenging due to delayed, context-dependent, and long-horizon attack patterns. Agents may pursue hidden objectives while maintaining superficially benign behavior, making detection difficult even with full trajectory access. Prior monitoring approaches improve scaffolding or ensemble aggregation, but treat each trajectory independently and do not learn from prior monitoring experience. Moreover, standard reasoning methods explain observed behavior without explicitly reasoning about agent beliefs, intentions, and goal alignment required to distinguish benign task execution from covert deviation. We propose \textbf{Agent-ToM}, a learning-to-monitor framework grounded in Theory-of-Mind (ToM) reasoning for security analysis of autonomous agents. Agent-ToM performs structured full-trajectory analysis by inferring beliefs, intent hypotheses with calibrated confidence, expected actions, and deviations from task-consistent behavioral baselines. At inference time, it employs a \textit{Reason-Verify-Refine} pipeline to construct and validate monitoring decisions. At training time, Agent-ToM distills critique signals into a persistent \textit{semantic guardrail memory}, enabling reusable belief- and intent-conditioned constraints across episodes. We evaluate Agent-ToM on adversarial agent monitoring benchmarks (SHADE-Arena and CUA-SHADE-Arena). Agent-ToM achieves strong precision-recall balance and outperforms state-of-the-art monitoring baselines, including ensemble methods, while using a coherent two-call reasoning pipeline. These results demonstrate that learning at the monitoring layer, combined with structured ToM reasoning and verification, provides an effective and deployable foundation for securing autonomous LLM agents.

</details>

### 125. JobBench: Aligning Agent Work With Human Will

📄 [arXiv](https://arxiv.org/abs/2605.26329) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`occupational agent`、`human delegation`、`rubric grading`、`privacy`、`utility`
- 🎯 **研究动机**：现有职业 AI agent 基准以经济价值划定范围、讲述替代故事，而未评估专家认为最值得委派、真正增强人类的工作流程。
- 🔬 **研究方法**：JobBench 覆盖 35 个职业的 130 个 agentic 任务，每任务打包为异构参考文件的工作区以模拟真实专业工作信息流，输出由平均 35.6 条二元判据的 fact-anchored rubric 链评分。
- 📌 **结论**：评测 36 个模型，最强的 Claude Opus 4.7（Claude Code 下）也仅达 45.9%，提示应把目标从替代人类转向做人类真正想委派之事的增强型 agent。

👤 **作者**：Yuetai Li、…、Radha Poovendran

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current benchmarks for occupational AI agents are scoped primarily by economic values, telling a replacement story. We introduce JobBench, which evaluates AI agents on the workflows that experts identify as high-priority for delegation, empowering humans based on their needs instead of replacing them with GDP value. JobBench covers 130 agentic tasks across 35 occupations. Each task is packaged as a workspace of heterogeneous reference files, requiring the agent to reason through the cluttered information streams of real professional work. Outputs are graded by a fact-anchored chain of rubrics, averaging 35.6 binary criteria per task. We evaluate 36 models; the strongest, Claude Opus~4.7 under Claude Code, reaches only 45.9 %. We hope JobBench shifts the community's target labour-market effect from replacement to enhancement: building agents that do what humans actually want delegated, not only what is most economically valuable.

</details>

### 126. The Best-Laid SCHEMEs: Coordinated Sabotage and Monitoring in Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2605.29178) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`multi-agent sabotage`、`coordinated attack`、`monitoring`、`agent safety`
- 🎯 **研究动机**：智能体编码系统把任务拆分给多个模型实例，但这些实例能否协同实现隐蔽恶意目标同时不破坏正常任务缺乏严格评测。
- 🔬 **研究方法**：提出 SCHEME 基准，17 个任务实例覆盖 7 类设置与 8 个真实开源库，每个设置要求任一智能体子集都无法单独成功，必须分解共享破坏计划、在不同通信拓扑下传递部分需求并执行相互一致的编辑。
- 📌 **结论**：协同破坏已具实用性——Gemini 3.1 Pro 在 84% 样本、Codex 在 46% 样本中完成隐蔽目标且正常任务成功；但可信监控仅凭代码编辑即以 FPR≤2% 检出 99%/68%（Gemini/Codex）的企图，加上智能体通信后达 100%/81%，全可见监控下未被检出的破坏保持 <3%。

👤 **作者**：Nikolay Radev、Lennart Haas、Benjamin Arnav、Pablo Bernabeu-Pérez

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As agentic coding systems decompose work across multiple model instances, a critical safety question is whether those instances can coordinate to achieve a hidden malicious objective while remaining aligned with user intent. We introduce SCHEME, a benchmark of 17 task instances across 7 settings and 8 real open-source libraries, each pairing a legitimate software-engineering task with a covert side task. Every setting is designed so that no proper subset of agents can succeed alone: agents must decompose a shared sabotage plan, relay partial requirements under different communication topologies, and execute mutually consistent edits, testing genuine multi-agent coordination rather than individual capability. Evaluating with GPT 5.1 Codex and Gemini 3.1 Pro, we find coordinated sabotage is already practical, with Gemini completing the covert objective while succeeding on the legitimate task in 84\% of samples and Codex in 46\%. A failure analysis shows that recovery, not failure incidence, drives the model gap: both models suffer similar numbers of communication failures per trajectory, but Gemini recovers from $\sim$73\% of occurrences against Codex's $\sim$56\%. However, the agents' code edits remain detectable: a trusted monitor flags coordinated sabotage at FPR$\le$2\% in 99\%/68\% (Gemini/Codex) of attempts from code edits alone, rising to 100\%/81\% with access to agent communication. Despite stealth-aware prompting, undetected sabotage stays at $<$3\% under the full-visibility monitor; telling agents a monitor is present halves Gemini's sabotage success without significantly breaking detection, even when agents are explicitly prompted to fabricate cover stories.

</details>

### 127. Imperfect World Models are Exploitable

📄 [arXiv](https://arxiv.org/abs/2605.15960) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`reward hacking`、`world model`、`exploitation`、`safe horizon`
- 🎯 **研究动机**：世界模型可被利用（模型认为某策略严格更优而真实环境相反），但 reward hacking 既有刻画下的不可避免性证明无法迁移到 exploitation。
- 🔬 **研究方法**：建立 reward hacking 与模型利用的统一理论，证明在大策略集上 exploitation 本质不可避免并以 hacking 为特例，进而针对有限策略集上不可 hack 条件无 exploitation 对应物的事实，引入放松的 exploitation 概念并导出可避免它的 safe horizon。
- 📌 **结论**：结果在 reward hacking 与模型利用之间架起形式化桥梁，阐明了世界模型安全规划的极限——仅在 safe horizon 内可避免放松意义的利用。

👤 **作者**：Logan Mondal Bhamidipaty、Esmeralda S. Whitammer、David Abel、Mykel J. Kochenderfer、Subramanian Ramamoorthy

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We propose a novel definition of model exploitation in reinforcement learning. Informally, a world model is exploitable if it implies that one policy should be strictly preferred over another while the environment's true transition model implies the reverse. We analogize our definition with a prior characterization of reward hacking but show that the associated proof of inevitability does not transfer to exploitation. To overcome this obstruction, we develop a general theory of reward hacking and model exploitation that proves that exploitation is essentially unavoidable on large policy sets and yields the corresponding claim for hacking as a special case. Unfortunately, we also find that the conditions that guarantee unhackability in finite policy sets have no counterpart that precludes exploitation. Consequently, we introduce a relaxed notion of exploitation and derive a safe horizon within which it can be avoided. Taken together, our results establish a formal bridge between reward hacking and model exploitation and elucidate the limits of safe planning in world models.

</details>

### 128. MCPHunt: An Evaluation Framework for Cross-Boundary Data Propagation in Multi-Server MCP Agents

📄 [arXiv](https://arxiv.org/abs/2604.27819) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-04　🏷 NeurIPS 2026

**关键词**：`benchmark`、`mcp`、`information flow`、`credential propagation`、`multi-server agent`
- 🎯 **研究动机**：多 server MCP agent 中忠实的工具组合可把各自无害的读写权限变成跨信任边界凭证传播——这是工作流拓扑的结构性副作用而非恶意模型行为，此前未被受控隔离研究。
- 🔬 **研究方法**：构建首个隔离非对抗、逐字凭证跨 MCP 信任边界传播的受控 benchmark，采用把传播检测归约为字符串匹配的 canary 污点追踪、risky/benign/hard-negative 环境受控覆盖设计、以及区分任务要求传播与违规传播的 CRS 分层。
- 📌 **结论**：5 个模型 3615 条主基准轨迹（147 任务、9 机制族）中违规传播率达 11.5-41.3%，通路特异性达 25 倍且集中于浏览器中介数据流；prompt 缓解最多降 97% 违规传播并保留 80.5% 效用，但效果随指令跟随能力而变。

👤 **作者**：Haonan Li、Tianjun Sun、Yongqing Wang、Qisheng Zhang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-server MCP agents create an information-flow control problem: faithful tool composition can turn individually benign read/write permissions into cross-boundary credential propagation -- a structural side effect of workflow topology, not necessarily malicious model behavior. We present MCPHunt, to our knowledge the first controlled benchmark that isolates non-adversarial, verbatim credential propagation across multi-server MCP trust boundaries, with three methodological contributions: (1) canary-based taint tracking that reduces propagation detection to objective string matching; (2) an environment-controlled coverage design with risky, benign, and hard-negative conditions that validates pipeline soundness and controls for credential-format confounds; (3) CRS stratification that disentangles task-mandated propagation (faithful execution of verbatim-transfer instructions) from policy-violating propagation (credentials included despite the option to redact). Across 3,615 main-benchmark traces from 5 models spanning 147 tasks and 9 mechanism families, policy-violating propagation rates reach 11.5--41.3% across all models. This propagation is pathway-specific (25x cross-mechanism range) and concentrated in browser-mediated data flows; hard-negative controls provide evidence that production-format credentials are not necessary -- prompt-directed cross-boundary data flow is sufficient. A prompt-mitigation study across 3 models reduces policy-violating propagation by up to 97% while preserving 80.5% utility, but effectiveness varies with instruction-following capability -- suggesting that prompt-level defenses alone may not suffice. Code, traces, and labeling pipeline are released under MIT and CC BY 4.0.

</details>

### 129. Measuring AI Agents' Progress on Multi-Step Cyber Attack Scenarios

📄 [arXiv](https://arxiv.org/abs/2603.11214) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`evaluation`、`ai agent`、`cyber-attack capability`、`inference-time compute`
- 🎯 **研究动机**：需要专用多步攻击场景来严格衡量前沿 AI 模型自主网络攻击能力的演进趋势
- 🔬 **研究方法**：构建两个专用 cyber range（32 步企业网络攻击链与 7 步工控系统攻击），在 18 个月内发布的 7 个模型上按不同推理时算力预算比较长动作序列下异构能力的串联表现
- 📌 **结论**：性能随推理算力对数线性增长且无平台期（10M 增至 100M token 提升最高 59%）；固定 10M token 下企业网场景平均完成步数从 1.7（GPT-4o）升至 9.8（Opus 4.6），最佳单次完成 22/32 步

👤 **作者**：Linus Folkerts、…、Jessica Wang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We evaluate the autonomous cyber-attack capabilities of frontier AI models on two purpose-built cyber ranges-a 32-step corporate network attack and a 7-step industrial control system attack-that require chaining heterogeneous capabilities across extended action sequences. By comparing seven models released over an eighteen-month period (August 2024 to February 2026) at varying inference-time compute budgets, we observe two capability trends. First, model performance scales log-linearly with inference-time compute, with no observed plateau-increasing from 10M to 100M tokens yields gains of up to 59%, requiring no specific technical sophistication from the operator. Second, each successive model generation outperforms its predecessor at fixed token budgets: on the corporate network range, average steps completed at 10M tokens rose from 1.7 (GPT-4o, August 2024) to 9.8 (Opus 4.6, February 2026). The best single run completed 22 of 32 steps, corresponding to roughly 6 of the estimated 14 hours a human expert would need. On the industrial control system range, performance remains limited, though the most recent models are the first to reliably complete steps, averaging 1.2-1.4 of 7 (max 3).

</details>

### 130. Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs

📄 [arXiv](https://arxiv.org/abs/2603.24511) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`attack`、`autoresearch`、`jailbreak`、`prompt injection`、`llm agent`
- 🎯 **研究动机**：对抗性 ML 长期主张防御须针对定制攻击评估，而发现更强攻击算法的过程本身可由 AI 智能体自动化，以推进白盒越狱与提示注入的 SOTA。
- 🔬 **研究方法**：将 Claude Code、Codex 等前沿智能体部署于 autoresearch 循环，配备 30+ 已有方法库与固定算力预算的评估脚本以自动发现攻击算法，并追踪所产生方法的谱系、策略与失败模式。
- 📌 **结论**：对 GPT-OSS-Safeguard-20B 的 CBRN 查询达最高 80% ASR（已有方法 <50%），对 Meta-SecAlign-70B 达 100% ASR（此前最佳自动方法仅 82%），且在无关代理模型上针对随机目标 token 强迫任务开发的方法可直接迁移到提示注入。

👤 **作者**：Alexander Panfilov、Peter Romov、Igor Shilov、Yves-Alexandre de Montjoye、Jonas Geiping、Maksym Andriushchenko

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We show that AI agents are capable of discovering novel algorithms for adversarial attacks against LLMs, advancing the state of the art on white-box jailbreaking and prompt injection evaluations. We deploy frontier agents, such as Claude Code and Codex, in an autoresearch loop with access to a library of 30+ prior methods and an evaluation script with a fixed compute budget. We show this pipeline to be effective in jailbreaking OpenAI's GPT-OSS-Safeguard-20B and in prompt injections against Meta-SecAlign-70B, an adversarially robust model. For GPT-OSS-Safeguard, the best agent-discovered method achieves up to 80\% attack success rate on CBRN queries, compared to <50\% for existing methods. For SecAlign, it achieves 100\% ASR, while the best prior automated methods only achieve 82\%. Notably, in our setting, attack methods are developed on unrelated surrogate models for a pure random-target token-forcing task, yet generalize directly to prompt injection on the adversarially trained model. Finally, we trace the lineage of methods developed during autoresearch, characterizing the agents' strategies and failure modes. Adversarial ML has long held that defenses must be evaluated against attacks tailored to them; autoresearch automates this principle, and we argue it should be the minimum bar for defense evaluation going forward.

</details>

### 131. Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks

📄 [arXiv](https://arxiv.org/abs/2602.20156) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`benchmark`、`prompt injection`、`agent skill`、`supply chain`
- 🎯 **研究动机**：LLM agent 的 skill 功能引入第三方代码、知识与指令，形成日益复杂的 agent 供应链，为 prompt injection 提供了未经评估的新攻击面
- 🔬 **研究方法**：提出 SkillInject 基准，含 202 个注入-任务对，覆盖从明显恶意到藏于合法指令中的隐蔽上下文相关攻击，并同时度量安全性（避免有害指令）与实用性（遵从合法指令）
- 📌 **结论**：当前 agent 高度脆弱，前沿模型攻击成功率最高达 80%，可执行数据外泄、破坏性操作乃至勒索行为，且模型规模化或简单输入过滤均无法解决，需要上下文感知授权框架

👤 **作者**：David Schmotz、Luca Beurer-Kellner、Sahar Abdelnabi、Maksym Andriushchenko

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents are evolving rapidly, powered by code execution, tools, and the recently introduced agent skills feature. Skills allow users to extend LLM applications with specialized third-party code, knowledge, and instructions. Although this can extend agent capabilities to new domains, it creates an increasingly complex agent supply chain, offering new surfaces for prompt injection attacks. We identify skill-based prompt injection as a significant threat and introduce SkillInject, a benchmark evaluating the susceptibility of widely-used LLM agents to injections through skill files. SkillInject contains 202 injection-task pairs with attacks ranging from obviously malicious injections to subtle, context-dependent attacks hidden in otherwise legitimate instructions. We evaluate frontier LLMs on SkillInject, measuring both security in terms of harmful instruction avoidance and utility in terms of legitimate instruction compliance. Our results show that today's agents are highly vulnerable with up to 80% attack success rate with frontier models, often executing extremely harmful instructions including data exfiltration, destructive action, and ransomware-like behavior. They furthermore suggest that this problem will not be solved through model scaling or simple input filtering, but that robust agent security will require context-aware authorization frameworks. Our benchmark is available at https://www.skill-inject.com/.

</details>

### 132. Learning to Inject: Automated Prompt Injection via Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2602.05746) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`attack`、`prompt injection`、`reinforcement learning`、`llm agent`、`adversarial suffix`
- 🎯 **研究动机**：提示注入是 LLM 智能体的关键漏洞但最强方法仍依赖人工红队与手工提示，越狱优化器只塑造通用顺从而非发出参数正确的特定工具调用，二值成功信号下随机后缀几乎不触发，标准优化器无梯度可循。
- 🔬 **研究方法**：提出黑盒强化学习框架 AutoInject，用基于比较的学习奖励将每个候选与迄今最优后缀对比，把二值信号转为稠密奖励以驱动 RL 优化，支持在线查询攻击与离线训练的免权限可迁移后缀。
- 📌 **结论**：在 AgentDojo 上以 McNemar 检验 p<0.05 显著超越模板攻击、GCG、TAP 与自适应攻击，学得的后缀还攻破了专门防御提示注入的 Meta-SecAlign-70B。

👤 **作者**：Xin Chen、Jie Zhang、Florian Tramèr

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prompt injection is a critical vulnerability in LLM agents, yet the strongest methods still rely on human red-teamers and hand-crafted prompts. Adapting automated jailbreak optimizers does not close this gap: jailbreaks shape models toward generic compliance, while prompt injection requires emitting specific tool calls with correct parameters. The success signal is binary, and randomly sampled suffixes almost never trigger it, so standard optimizers have no gradient to follow. We present AutoInject, a black-box reinforcement learning (RL) framework that learns adversarial suffixes for prompt injection. A learned comparison-based reward scores each candidate against the best suffix seen so far, turning the binary signal into a dense reward suitable for RL optimization. The framework supports both online query-based attacks and offline-trained transferable suffixes that need no utility access at deployment, and incorporates a utility objective when task-completion feedback is available. On AgentDojo, AutoInject outperforms template attacks, GCG, TAP, and adaptive attack across production models, with statistically significant improvements under McNemar's test with p<0.05. Suffixes learned by AutoInject also break Meta-SecAlign-70B, a model fine-tuned specifically to resist prompt injection, where template attacks fail outright. The results establish an automated baseline for prompt injection and expose a gap between preference-based defenses and adaptive optimization-based attackers.

</details>

### 133. Rethinking Latency Denial-of-Service: Attacking the LLM Serving Framework, Not the Model

📄 [arXiv](https://arxiv.org/abs/2602.07878) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`attack`、`denial of service`、`llm serving`、`scheduler`、`latency attack`
- 🎯 **研究动机**：算法复杂度类延迟攻击对现代 LLM serving 系统基本无效——continuous batching 等系统级优化提供了逻辑隔离，攻击焦点应从算法层转向系统层。
- 🔬 **研究方法**：提出针对调度器状态转移的 Fill and Squeeze 攻击："Fill" 先耗尽全局 KV cache 诱发 Head-of-Line blocking，"Squeeze" 再迫使系统反复 preemption，结合从纯文本到复杂提示工程的输出长度操纵与内存状态侧信道探测，实现黑盒低成本编排。
- 📌 **结论**：相比现有攻击，Time to First Token 平均减慢 20-280 倍、Time Per Output Token 平均减慢 1.5-4 倍，同时攻击成本降低 30-40%。

👤 **作者**：Tianyi Wang、Huawei Fan、Yuanchao Shu、Peng Cheng、Cong Wang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models face an emerging and critical threat known as latency attacks. Because LLM inference is inherently expensive, even modest slowdowns can translate into substantial operating costs and severe availability risks. Recently, a growing body of research has focused on algorithmic complexity attacks by crafting inputs to trigger worst-case output lengths. However, we report a counter-intuitive finding that these algorithmic latency attacks are largely ineffective against modern LLM serving systems. We reveal that system-level optimization such as continuous batching provides a logical isolation to mitigate contagious latency impact on co-located users. To this end, in this paper, we shift the focus from the algorithm to the system layer, and introduce a new Fill and Squeeze attack strategy targeting the state transition of the scheduler. "Fill" first exhausts the global KV cache to induce Head-of-Line blocking, while "Squeeze" forces the system into repetitive preemption. By manipulating output lengths using methods from simple plain-text prompts to more complex prompt engineering, and leveraging side-channel probing of memory status, we demonstrate that the attack can be orchestrated in a black-box setting with much less cost. Extensive evaluations indicate by up to 20-280x average slowdown on Time to First Token and 1.5-4x average slowdown on Time Per Output Token compared to existing attacks with 30-40% lower attack cost.

</details>

### 134. CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents

📄 [arXiv](https://arxiv.org/abs/2601.09923) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-01　🏷 NeurIPS 2026

**关键词**：`defense`、`computer use agent`、`prompt injection`、`single-shot planning`、`control flow integrity`
- 🎯 **研究动机**：架构隔离对 prompt 注入提供最强保证，但 CUA 需持续观察 UI 状态来决定动作，与安全所需隔离存在根本张力。
- 🔬 **研究方法**：利用 UI 工作流虽动态但结构可预测的特性，让可信 planner 一次性发出覆盖所有预期运行时状态的完整分支计划以获得对任意指令注入的控制流完整性保证，并引入 NOVA 在组合爆炸的 UI 状态空间中调用感知模型解析运行时值。
- 📌 **结论**：在 OSWorld 上保留前沿模型最高 57% 性能并使较小开源模型提升至多 19%，证明严格安全与效用可共存；但预先规划防不住欺骗感知模型将执行路由到攻击者偏好分支的 Branch Steering 攻击。

👤 **作者**：Hanna Foerster、…、Yiren Zhao

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents are vulnerable to prompt injection attacks, where malicious content hijacks agent behavior. Among proposed defenses, architectural isolation provides the strongest guarantees by strictly separating trusted task planning from untrusted environment observations. However, applying this design to Computer Use Agents (CUAs), which automate tasks by viewing screens and executing actions, presents a fundamental challenge. Current agents require continuous observation of UI state to determine each action, which conflicts with the isolation required for security. We resolve this tension by demonstrating that UI workflows, while dynamic, are structurally predictable. Single-shot planning, where a trusted planner emits upfront a complete branching plan covering all anticipated runtime states, provides control flow integrity guarantees against arbitrary instruction injections. We introduce NOVA (Navigating via Observation, Verification, and Action) to make this viable in the combinatorially large UI state space, where the plan can invoke a perception model to resolve runtime values such as UI coordinates. We evaluate our design on OSWorld, and retain up to 57% of the performance of frontier models while improving performance for smaller open-source models by up to 19%, demonstrating that rigorous security and utility can coexist in CUAs. Although upfront planning prevents instruction injections, we show that additional measures are needed to defend against \textbf{Branch Steering} attacks, where adversaries deceive the perception model into routing execution down attacker-preferred branches of the plan, such as redirecting the agent to a malicious website.

</details>

### 135. MCP-Atlas: A Large-Scale Benchmark for Tool-Use Competency with Real MCP Servers

📄 [arXiv](https://arxiv.org/abs/2602.00933) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-01　🏷 NeurIPS 2026

**关键词**：`benchmark`、`mcp`、`tool use`、`llm agent`、`claim-level scoring`
- 🎯 **研究动机**：现有 MCP 评估在真实多步跨 server 工作流、非 mock 的真实 MCP server 覆盖、以及与 agent 冗长风格解耦的结构化可复现评分三个轴上均有不足。
- 🔬 **研究方法**：构建 MCP-Atlas，含 1000 个人工撰写验证任务、覆盖 36 个真实 MCP server 与 220 个工具，prompt 不指明 server/工具/参数，用 claim 级 rubric 对工具输出锚定的原子事实判分，并配 11 类诊断分类学。
- 📌 **结论**：20 个前沿模型在 0.75 claim 覆盖阈值下 pass rate 最高 82.2% 并呈清晰三层结构，63.3% 已诊断失败为认知性而非工具调用问题，多个高性能模型在工具执行成功后因过早停止或错误合成而失败。

👤 **作者**：Chaithanya Bandi、…、Bing Liu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The Model Context Protocol (MCP) is emerging as a standard interface through which large language model (LLM) agents discover and invoke external tools. However, existing MCP evaluations fall short along three key axes: realistic multi-step workflows with cross-server orchestration, breadth across authentic MCP servers rather than mocks, and structured, reproducible claim-level scoring disentangled from agent verbosity or style. We introduce MCP-Atlas, a benchmark for measuring tool-use competency against production MCP servers. MCP-Atlas contains 1,000 natural-language tasks written and verified by human experts spanning 36 real MCP servers and 220 tools. Prompts do not specify servers, tools, or parameters, requiring agents to identify relevant tools among semantically plausible distractors and to compose multi-step, cross-server workflows. Each task is scored with a claim-level rubric, where final answers are scored against atomic factual claims grounded in tool outputs. This answer-centric scoring permits valid alternative tool-call trajectories to receive credit. We pair this with an 11-category diagnostic taxonomy that disentangles tool-call failures from cognitive failures in task understanding, synthesis, parsing, and stopping. Evaluating 20 frontier models from six providers under matched task-level conditions, we find pass rates up to 82.2% at a 0.75 claim coverage threshold and a clear three-tier performance structure. Automated diagnostics show that 63.3% of diagnosed failures are cognitive rather than tool-call related. Notably, several high-performing models fail after successful tool execution due to premature stopping or incorrect synthesis. We release the task schema, containerized harness, claim evaluator, and a 500-task public split, while reserving a 500-task private split to preserve leaderboard integrity. The code is at https://github.com/scaleapi/mcp-atlas.

</details>

### 136. DECEIVE-AFC: Adversarial Claim Attacks against Search-Enabled LLM-based Fact-Checking Systems

📄 [arXiv](https://arxiv.org/abs/2602.02569) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-01　🏷 NeurIPS 2026

**关键词**：`attack`、`fact-checking`、`llm agent`、`claim attack`、`input-only threat model`
- 🎯 **研究动机**：带搜索的 LLM 事实核查系统对对抗攻击的鲁棒性认识不足，在现实 input-only 威胁模型下的脆弱性未被系统研究。
- 🔬 **研究方法**：提出 DECEIVE-AFC agent 对抗攻击框架，整合 claim 级攻击策略与对抗 claim 有效性评估原则，在无需证据源或模型内部访问下扰乱搜索行为、证据检索与 LLM 推理。
- 📌 **结论**：在基准数据与真实系统上将验证准确率从 78.7% 降至 53.7%，显著超越现有 claim 级攻击基线且具强跨系统迁移性。

👤 **作者**：Haoran Ou、…、Kwok-Yan Lam

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fact-checking systems with search-enabled large language models (LLMs) have shown strong potential for verifying claims by dynamically retrieving external evidence. However, the robustness of such systems against adversarial attack remains insufficiently understood. In this work, we study adversarial claim attacks against search-enabled LLM-based fact-checking systems under a realistic input-only threat model. We propose DECEIVE-AFC, an agent-based adversarial attack framework that integrates novel claim-level attack strategies and adversarial claim validity evaluation principles. DECEIVE-AFC systematically explores adversarial attack trajectories that disrupt search behavior, evidence retrieval, and LLM-based reasoning without relying on access to evidence sources or model internals. Extensive evaluations on benchmark datasets and real-world systems demonstrate that our attacks substantially degrade verification performance, reducing accuracy from 78.7% to 53.7%, and significantly outperform existing claim-based attack baselines with strong cross-system transferability.

</details>

### 137. PROTEUS: A Self-Evolving Red Team with Surface Expansion for Agent Skill Ecosystems

📄 [arXiv](https://arxiv.org/abs/2605.11891) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`red team`、`agent skill`、`adaptive leakage`、`self-evolving`
- 🎯 **研究动机**：第三方 agent skill 同时暴露可执行行为与设定上下文的文档，单次审计或提示级红队无法度量预算受限攻击者利用审计与运行时反馈反复改写 skill 直至通过审计并造成运行时危害的自适应泄漏风险。
- 🔬 **研究方法**：提出灰盒自进化红队框架 Proteus，在形式化的五轴 skill 攻击空间内搜索，经统一的审计-沙箱-预言机管线返回结构化审计发现与运行时证据引导跨轮变异，并做路径扩展与将已学实现模式迁移到新攻击目标的攻击面扩展。
- 📌 **结论**：八个配置下 ASR@5 达 40–90% 且对两类审计器学习曲线斜率均为正；SkillVetter 在全部扩展格中被以不低于 93% 的比例绕过，最强公共审计器 AI-Infra-Guard 仍放行高达 41.3% 的联合成功变体，表明当前 skill 审计显著低估残余风险。

👤 **作者**：Zhaojiacheng Zhou、Jiong Lou、Kaixiang Wang、Yanzhi Li、Hefeng Zhou、Jie LI

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills extend LLM agents with reusable instructions, tool interfaces, and executable code, and users increasingly install third-party skills from marketplaces, repositories, and community channels. Because a skill exposes both executable behavior and context-setting documentation, its deployment risk cannot be measured by single-shot audits or prompt-level red teams alone: a realistic attacker can use audit and runtime feedback to repeatedly rewrite the skill. We frame this risk as adaptive leakage—whether a budgeted attacker can iteratively revise a skill until it passes audit and produces verified runtime harm—and present Proteus, a grey-box self-evolving red-team framework for measuring it. Proteus searches a formalized five-axis skill-attack space. Each candidate is evaluated through a unified audit-sandbox-oracle pipeline that returns structured audit findings and runtime evidence to guide cross-round mutation. Beyond initial evasion, Proteus performs path expansion, which finds alternative implementations of successful attacks, and surface expansion, which transfers learned implementation patterns to new attack objectives beyond the original seed catalogue. Across eight phase-1 mutator-target-defender configurations, Proteus achieves 40-90% ASR@5 and exhibits positive learning-curve slopes on both evaluated auditors. In the full 8-cell expansion matrix, Proteus generates 438 jointly bypassing and lethal variants; SkillVetter is bypassed at \geq 93% in every expansion cell, and AI-Infra-Guard, the strongest public auditor we evaluate, still admits jointly successful variants at up to 41.3%. These results show that current skill vetting substantially underestimates residual risk when evaluated against adaptive, feedback-driven attackers. Code: \urlhttps://anonymous.4open.science/r/proteus/.

</details>

### 138. To trust or not to trust: Attention-based Trust Management for LLM Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2506.02546) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-06　🏷 NeurIPS 2026

**关键词**：`defense`、`trust management`、`multi-agent systems`、`attention`、`robustness`
- 🎯 **研究动机**：LLM 多智能体系统中智能体平等对待所有消息而不评估可信度，且现有工作只关注单一危害类型、缺乏多维度整体分析。
- 🔬 **研究方法**：借鉴人类沟通理论（Grice）给出含六个正交信任维度的可信度综合定义，提出基于注意力的轻量消息可信度评分 A-Trust，并构建支持消息级与智能体级评估的信任管理系统（TMS）。
- 📌 **结论**：跨多样多智能体设置与任务的实验表明，该 TMS 显著提升系统对恶意输入的鲁棒性。

👤 **作者**：Pengfei He、…、Qi He

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model-based Multi-Agent Systems (LLM-MAS) have demonstrated strong capabilities in solving complex tasks but remain vulnerable when agents receive unreliable messages. This vulnerability stems from a fundamental gap: LLM agents treat all incoming messages equally without evaluating their trustworthiness. While some existing studies approach trustworthiness, they focus on a single type of harmfulness rather than analyze it in a holistic approach from multiple trustworthiness perspectives. We address this gap by proposing a comprehensive definition of trustworthiness inspired by human communication theory (Grice, 1975). Our definition identifies six orthogonal trust dimensions that provide interpretable measures of trustworthiness. Building on this definition, we introduce the Attention Trust Score (A -Trust), a lightweight, attention-based method for evaluating the trustworthiness of messages. We then develop a principled trust management system (TMS) for LLM -MAS that supports both message-level and agent-level trust assessments. Experiments across diverse multi-agent settings and tasks demonstrate that our TMS significantly improves robustness against malicious inputs.

</details>

**尚未挂出 arXiv（待核验）**
- AM-Bench: A Unified Taxonomy and Evaluation Suite for Agentic Misalignment
- MCPHallu: Benchmarking Reasoning, Execution, and Memory Hallucinations in MCP Agents
- MetaPI: Constructing Prompt Injection Benchmarks from Any Agent Benchmarks
- EV-AUDIT: A Co-Evolutionary Auditing Framework for Task Hijacking in Multi-Agent Systems
- DIBench: Benchmarking Decision Integrity of GUI-based Mobile Agents Under Deceptive Injections
- LPS-Bench: Benchmarking Safety Awareness of Computer-Use Agents in Long-Horizon Planning
- MMA-SafetyBench: A Benchmark for Multimodal Agent Safety Evaluation
- MLLMs Fail to Refuse when Using Tools Agentically
- Auditing Sabotage Bench: Detecting and Fixing Research Sabotage in ML Codebases
- CyberDualEval: Measuring Dual-Use Cyber Risks in Frontier Language Models
- KaliBench: Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux
- Bits Beat Tokens: A Regret Rate Distortion Theory for LLM Agents

### 扩散语言模型安全（DLM 线）

### 139. Beyond the Prompt: Leveraging Pre-Decoding States for Jailbreak Detection in dLLMs（已库内 dllm-security #8）

📝 [OpenReview](https://openreview.net/forum?id=cQKisMHGgm) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`detection`、`jailbreak`、`diffusion language model`、`pre-decoding states`、`representation fusion`
- 🎯 **研究动机**：dLLM 通过迭代去噪生成文本，会在任何 token 定稿前暴露未来响应槽位的隐状态，即使越狱难以从 prompt 本身判别，初始掩码响应状态也可能已反映模型正在形成的有害补全，这一自回归解码不存在的检测面尚未被利用。
- 🔬 **研究方法**：在 LLaDA-8B-Instruct 上以 prompt 隐状态与解码前掩码响应隐状态两种冻结表示训练轻量线性分类器，发现两者互补，并提出推理时融合两类分类器分数的检测器 ReFuse，不修改模型权重与解码流程。
- 📌 **结论**：在迁移与 dLLM 定向越狱上，ReFuse 将平均 ASR 从未防御的 63.29% 降至 3.31%，标准效用基准上的良性拒绝率保持在 1% 以下。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion language models (dLLMs) generate text by iteratively denoising masked response positions, exposing hidden states over future response slots before any token is finalized. This creates a detection surface that is absent from standard autoregressive decoding: even when a jailbreak is difficult to identify from the prompt alone, the initial masked response states may already reflect the model's emerging completion. We test this hypothesis on LLaDA-8B-Instruct by training lightweight linear classifiers on two frozen representations: prompt hidden states and pre-decoding masked-response hidden states. Empirically, the two views are complementary: neither classifier strictly dominates the other, and each recovers attacks missed by the other view. We then introduce \textttReFuse (Representation Fusion), an inference-time detector that fuses prompt and pre-decoding response classifier scores without modifying model weights or the decoding procedure. Across transferred and dLLM-targeted jailbreaks, \textttReFuse reduces average ASR from 63.29% for the undefended model to 3.31%, while keeping average benign refusal on standard utility benchmarks below 1%. These results suggest that pre-decoding response states provide a complementary safety signal for detecting jailbreaks in dLLMs.

</details>

### 140. Machine Unlearning in Diffusion LLMs

📝 [OpenReview](https://openreview.net/forum?id=Dlj9mRJfOq) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`machine unlearning`、`diffusion llm`、`forgetting`、`utility preservation`
- 🎯 **研究动机**：机器遗忘在自回归大语言模型上已被广泛研究，但在扩散大语言模型上的应用基本空白，已有遗忘目标因监督稀疏与遗忘定位不准而难以迁移到该设定。
- 🔬 **研究方法**：提出 DLLM 原生遗忘框架 DL-Eraser，在高掩码条件下抑制目标知识的可恢复性，同时将参数更新约束在保持效用的子空间内。
- 📌 **结论**：大量实验表明 DL-Eraser 在实现更强遗忘的同时比现有基线更好地保留模型效用。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning (MU) aims to remove sensitive or undesired knowledge from a trained model without retraining from scratch. While MU has been widely studied for autoregressive large language models, its application to diffusion large language models (DLLMs) remains largely unexplored. In this paper, we present the first systematic study of MU in DLLMs and show that existing unlearning objectives transfer poorly to this setting due to sparse supervision and inaccurate forgetting localization. To address these challenges, we propose \textscDL-Eraser, a DLLM-native unlearning framework that suppresses target recoverability under high-mask conditioning while constraining updates to a utility-preserving subspace. Extensive experiments show that \textscDL-Eraser achieves stronger forgetting while better preserving model utility than existing baselines. To the best of our knowledge, this is the first work that systematically investigates MU in DLLMs.

</details>

### 141. Diffusion-Time Concept Manifolds: Sparse Autoencoder Groups for Interpreting Denoising Language Models

📝 [OpenReview](https://openreview.net/forum?id=FrP1gSPL04) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`analysis`、`interpretability`、`sparse autoencoder`、`diffusion language model`、`concept manifold`
- 🎯 **研究动机**：扩散语言模型通过迭代去噪生成文本，但当前可解释性工具大多分析静态隐状态，无法解释概念信息如何随去噪时间演化。
- 🔬 **研究方法**：提出 DynaManifold-SAE，跨掩码率构建稀疏潜在编码并组合候选特征组，用留出坐标预测、测地一致性、时间持续性与因果干预评估激活形成的时间依赖概念流形。
- 📌 **结论**：在 BERT 与 LLaDA 上可靠识别跨种子稳定的稀疏情感几何并强于单特征、PCA、随机组与图结构基线，可从受控模板迁移到自然 SST-2；特征组能预测 LLaDA 解掩码的 token 揭示顺序与置信度增长，定向干预显著改变揭示置信度与 token 恢复。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion language models generate text through iterative denoising, but current interpretability tools mostly analyze static hidden states and do not explain how concept information evolves across denoising time. We introduce DynaManifold-SAE, a method for discovering sparse autoencoder feature groups whose activations form time-dependent concept manifolds in masked and diffusion language models. The method builds sparse latent codes across mask ratios, constructs candidate feature groups, and evaluates them with held-out coordinate prediction, geodesic consistency, persistence across time, and causal interventions. Across BERT and LLaDA, DynaManifold-SAE reliably identifies sparse sentiment geometry that is stable across seeds and stronger than individual-feature, PCA, random-group, and graph-structured baselines. The discovered groups transfer from controlled templates to natural SST-2 examples, indicating that they capture semantic structure rather than template artifacts. We further show that these groups explain a denoising-specific mechanism: they predict token reveal order and confidence growth during LLaDA unmasking, and targeted interventions alter reveal confidence and token recovery more than matched controls. These results suggest that sparse feature manifolds provide a practical bridge between static representation geometry and the dynamics of diffusion language generation.

</details>

### 142. CURE: Counterfactual Unsafe-token Re-masking for Diffusion Large Language Model Test-time Alignment

📝 [OpenReview](https://openreview.net/forum?id=XF2UgJwAIj) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`test-time alignment`、`diffusion language model`、`re-masking`、`safety value model`
- 🎯 **研究动机**：DLM 在有害提示下的中间去噪状态可含看似良性却会塑造剩余掩码位补全方式、从而提高最终不安全回复概率的风险 token，而既有防御依赖模型级对齐、轨迹级检测或块级修复，常需训练成本、额外推理或粗粒度再生。
- 🔬 **研究方法**：提出 CURE 测试时对齐方法，固定基座 DLM，训练时间条件安全价值模型估计部分去噪状态导向不安全最终回复的概率，推理时构造反事实读出视图估计各 token 对未来不安全回复的贡献，仅重掩码高风险 token 供后续改写。
- 📌 **结论**：在 3 个 DLM 与 5 个越狱基准上将宏平均 ASR 从 47.20% 降至 1.36%，在 MMLU 与 GSM8K 上保持效用且仅增加 0.84 TFLOPs，实现安全-效用-效率的强权衡。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion language models (DLMs) generate text through iterative denoising, enabling parallel decoding, bidirectional conditioning, and editable intermediate states. Under harmful prompts, however, intermediate denoising states can contain risk-inducing tokens that are seemingly benign but increase the probability of an unsafe final response by shaping how the remaining masked positions are completed. Since committed tokens in DLMs can still be re-masked and rewritten, safety control can be applied during denoising by removing a small set of risk-inducing tokens before they drive subsequent generation toward unsafe responses. Existing DLM defenses mainly rely on model-level alignment, trajectory-level detection, or block-level repair, often requiring training cost, extra inference passes, or coarse regeneration. We propose CURE, a counterfactual value-driven test-time alignment method that keeps the base DLM fixed and selectively re-masks risk-inducing tokens. CURE trains a time-conditioned safety value model to estimate whether a partially denoised state will lead to an unsafe final response. During inference, CURE constructs counterfactual readout views that remove or isolate targeted tokens, estimates their contribution to future unsafe response, and re-masks only high-risk tokens for later rewriting. Across three DLMs and five jailbreak benchmarks, CURE reduces macro-average ASR from 47.20% to 1.36%, preserves utility on MMLU and GSM8K, and adds only 0.84 extra TFLOPs, achieving a strong safety-utility-efficiency trade-off. Code is available at \urlhttps://anonymous.4open.science/r/CURE.

</details>

### 143. Diffusion Models Can Approximate Optimal Infilling Lengths Implicitly（解码行为分析，DLM DoS 相关）

📝 [OpenReview](https://openreview.net/forum?id=AFvSuWgvYZ) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`analysis`、`diffusion language model`、`infilling length`、`denoising confidence`、`training-free`
- 🎯 **研究动机**：DLM 提供天然适合填充生成的双向框架，但性能受预先指定填充长度的制约，模型能否自行发现正确填充长度未知。
- 🔬 **研究方法**：识别首步去噪置信度中的两个统计现象——真值长度附近的局部 Oracle Peak 与常掩盖该信号的系统性 Length Bias，据此提出免训练的 CAL 方法，通过偏差校准与正式解码前的高效搜索逼近最优填充长度。
- 📌 **结论**：代码填充上 Pass@1 较固定长度基线最高提升 47.7%、较聊天式自适应方法提升 40.5%，文本填充上 BLEU-2 与 ROUGE-L 最高分别提升 8.5% 与 9.9%。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion language models (DLMs) provide a bidirectional generation framework naturally suited for infilling, yet their performance is constrained by the pre-specified infilling length. In this paper, we reveal that DLMs possess an inherent ability to discover the correct infilling length. We identify two key statistical phenomena in the first-step denoising confidence: a local Oracle Peak that emerges near the ground-truth length and a systematic Length Bias that often obscures this signal. By leveraging this signal and calibrating the bias, our training-free method CAL (Calibrated Adaptive Length) enables DLMs to approximate the optimal length through an efficient search before formal decoding. Empirical evaluations demonstrate that CAL improves Pass@1 by up to 47.7% over fixed-length baselines and 40.5% over chat-based adaptive methods in code infilling, while boosting BLEU-2 and ROUGE-L by up to 8.5% and 9.9% in text infilling. These results demonstrate that CAL paves the way for robust DLM infilling without requiring any specialized training.

</details>

### 144. Why Jailbreaks Succeed in Diffusion Language Models: An Energy Landscape Analysis（已库内，0928）

📄 [arXiv](https://arxiv.org/abs/2609.30841) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`analysis`、`diffusion language model`、`jailbreak`、`energy landscape`、`training-free detection`
- 🎯 **研究动机**：dLLM 的现有攻防各自针对特定漏洞，缺乏解释越狱为何成功的统一框架。
- 🔬 **研究方法**：将安全对齐建模为去噪能量景观塑形，把越狱归纳为初始时掩盖查询安全倾向或中途强行跨越能量壁垒两类策略，并据此导出 step-0 ratio 与两个轨迹速度信号共三个免训练检测信号。
- 📌 **结论**：在 LLaDA-8B、LLaDA-1.5、Dream-7B 与 LLaDA-MoE-7B 四个 dLLM 上验证信号互补性，压力测试中所有逃过检测的攻击配置同样无法产出有害内容。

👤 **作者**：Thong Bach、Dung Nguyen、Thao Minh Le、Truyen Tran

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing attacks and defenses for diffusion-based large language models (dLLMs) target specific vulnerabilities but lack a shared framework explaining why attacks succeed. We propose one by interpreting safety alignment as shaping the denoising energy landscape: a well-aligned model routes harmful queries toward safe outputs through an energy barrier that separates the two regions. Current jailbreak attacks reduce to two strategies for circumventing this barrier: obscuring the query's safety disposition at initialisation, or intervening mid-trajectory to force the denoising path across the energy barrier. From this perspective and the result that masked diffusion models minimise kinetic energy during denoising, we derive three complementary, training-free detection signals: a step-0 ratio that reads the initial safety disposition from the logit distribution before generation begins, and two trajectory-velocity signals that track kinetic energy in complementary subspaces of the logit space. An attack must either reveal its intent at initialisation or expend kinetic energy to cross the barrier in at least one monitored subspace, so the three signals cover each other's blind spots in the energy budget by construction. Evaluation across three dense dLLMs (LLaDA-8B, LLaDA-1.5, Dream-7B) and a sparse mixture-of-experts dLLM (LLaDA-MoE-7B) confirms this complementarity. In stress tests of known attacks, every configuration that evades detection also fails to produce harmful content, suggesting that the detection and barrier-crossing thresholds are hard to separate.

</details>

### 145. Weak Ties, Strong Signals: Efficient Training Data Detection in Diffusion LLMs via Independent Token Sampling（已库内，0929）

📄 [arXiv](https://arxiv.org/abs/2609.22145) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-08　🏷 NeurIPS 2026

**关键词**：`detection`、`membership inference`、`diffusion llm`、`mutual information`、`query efficiency`
- 🎯 **研究动机**：dLLM 缺乏因果架构的单遍概率分解，现有随机掩码方法无法控制被掩 token 间依赖，其 token 级近似引入由累积条件互信息刻画、非负的结构性估计误差，掩盖细微记忆信号。
- 🔬 **研究方法**：提出 Independent Token Sampling（ITS），用注意力导出的成对依赖代理近似 CMI 感知的选择准则以挑选内部依赖弱的掩码集，并加入多样性促进策略提升跨轮 token 覆盖。
- 📌 **结论**：在多个模型与数据集上一致超越 SOTA 基线，ArXiv 数据集上 AUC 提升 0.18，且在有限查询预算下仍保持强劲性能。

👤 **作者**：Hongyao Yu、…、Shu-Tao Xia

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion large language models (dLLMs) offer a compelling alternative to autoregressive models, yet they may expose sensitive training data during denoising. Detecting such usage is challenging because dLLMs lack the efficient one-pass probability decomposition of causal architectures. Existing methods rely on random masking to obtain tractable token-wise detection signals under limited query budgets, but fail to control dependencies among masked tokens. We demonstrate that this token-wise approximation introduces a non-negative structural estimation error, which is theoretically characterized by the cumulative conditional mutual information (CMI) among masked tokens and can obscure subtle memorization signals. This insight suggests that reliable detection requires masked token sets with weak internal dependency. To avoid the prohibitive cost of directly estimating CMI over token combinations, we propose \textit{Independent Token Sampling} (ITS), a query-efficient framework that uses an attention-derived pairwise dependency proxy to approximate the CMI-aware selection criterion. ITS further incorporates a diversity-promoting strategy to improve token coverage across sampling rounds, yielding aggregated token-wise signals that are less affected by dependency-induced approximation error. Experiments on multiple datasets show that ITS consistently outperforms state-of-the-art baselines across different models and datasets, achieving an AUC improvement of 0.18 on the ArXiv dataset while maintaining strong performance under limited query budgets. The code is available at https://github.com/Chrisqcwx/DLLM-MIA .

</details>

### 146. MaskForge: Structure-Aware Adaptive Attacks for Jailbreaking Diffusion Large Language Models（已库内 dllm-security #4）

📄 [arXiv](https://arxiv.org/abs/2606.04027) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`attack`、`jailbreak`、`diffusion llm`、`adaptive attack`、`infilling`
- 🎯 **研究动机**：dLLM 以置信度而非位置提交 token、掩码是原生输入，有害内容可经 infilling 在受监控前缀之外注入，而现有越狱要么忽略该能力、要么依赖低多样性掩码模板且缺乏结构适配与经验积累。
- 🔬 **研究方法**：MaskForge 将 dLLM 红队建模为对可增长结构模式库的全黑盒优化搜索：把成功尝试抽象为可复用 schema、用 UCB bandit 选取与目标兼容的模式、失败时打分器引导回退，成功经验再蒸馏回库。
- 📌 **结论**：在 5 个公开 dLLM 与 3 个基准上平均攻击成功率 79.3%（较最强基线相对提升 17.6%），成熟模式库零更新迁移到 AdvBench 达 88.2%（相对提升 67%）。

👤 **作者**：Yingzi Ma、Zhengyue Zhao、Xiaogeng Liu、Minhui Xue、Yue Zhao、Chaowei Xiao

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion large language models (dLLMs) generate text by iteratively denoising partially masked sequences under bidirectional context, exposing a safety surface distinct from autoregressive LLMs. Because mask tokens are native inputs and tokens are committed by confidence rather than position, harmful content can be induced through infilling and outside the monitored prefix. Existing jailbreaks either miss this native infill capability or rely on low-diversity mask-bearing templates applied uniformly across goals, with little structural adaptation or accumulated attack experience. We propose MaskForge, a fully black-box adaptive attack that casts dLLM red-teaming as optimized search over a growing library of structural patterns. MaskForge abstracts successful attempts into reusable schemas, selects goal-compatible patterns with a UCB bandit, and invokes a scorer-guided fallback when the current library fails. Successful attempts are distilled back into the pattern library, enabling experience to accumulate across goals. Across five public dLLMs and three benchmarks, MaskForge achieves an average attack success rate of 79.3%, a 17.6% relative improvement over the strongest competing dLLM baseline. The matured pattern library further transfers to AdvBench without any updates, achieving a 88.2% attack success rate and a 67% relative improvement over the strongest competing baseline.

</details>

### 147. Extracting Training Data from Diffusion Language Models via Infilling（已库内 dllm-security #24）

📄 [arXiv](https://arxiv.org/abs/2605.24173) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`attack`、`training data extraction`、`diffusion language model`、`infilling`、`memorization`
- 🎯 **研究动机**：LLM 记忆研究几乎都采用前缀条件提取，而 DLM 能对任意位置的掩码 token 去噪，仅靠前缀探测只揭示记忆的一个侧面并显著低估训练数据被提取的风险。
- 🔬 **研究方法**：提出以任意二值掩码参数化的 infilling extraction 协议，涵盖前缀探测并匹配 DLM 的双向归纳偏置，在 LLaDA-8B 与 Dream-7B 上跨 5 种提取模式、3 种训练管线、3 个语料评估 verbatim 与部分泄漏。
- 📌 **结论**：掩码几何主导可提取性——边缘条件掩码提取的逐字序列最多达前缀条件的 3 倍，攻击者从 DLM 提取被脱敏邮箱的 recall 甚至高于同规模自回归模型，解码参数可测地影响提取且后续 SFT 不消除既有记忆。

👤 **作者**：Yihan Wang、N. Asokan

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Memorization in large language models has been studied almost exclusively through prefix-conditioned extraction, a natural choice for autoregressive models. However, diffusion language models (DLMs) can denoise masked tokens at arbitrary positions. Thus, prefix-only probing reveals only one facet of memorization in DLMs and significantly underestimates the risk of training-data extraction. In order to realistically model extractability of training data in DLMs, we introduce \emph{infilling extraction}, a data-extraction protocol parameterized by an arbitrary binary mask that subsumes prefix-only probing and accounts for the bidirectional inductive bias of DLMs. Instantiating it on LLaDA-8B and Dream-7B across five extraction modes, three training pipelines, and three corpora covering verbatim and partial leakage, we find that mask geometry governs extractability: edge-conditioned masks \emph{extract up to three times more} verbatim sequences than prefix-conditioned ones, and bidirectional access opens channels inaccessible in autoregressive models. In particular, we show that a realistic adversary with access to training data where personally identifiable information has been redacted, can even achieve higher recall on extracting redacted email addresses from DLMs than from scale-matched autoregressive models. Tunable parameters for decoding measurably affect extraction performance, while a follow-up supervised finetuning stage does not eliminate the prior memorization.

</details>

### 148. Characterizing Memorization in Diffusion Language Models: Generalized Extraction and Sampling Effects

📄 [arXiv](https://arxiv.org/abs/2603.02333) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`analysis`、`diffusion language model`、`memorization`、`pii leakage`、`sampling resolution`
- 🎯 **研究动机**：自回归模型已被证明会记忆并逐字复现训练数据，而作为竞争替代方案的扩散语言模型因生成动力学根本不同，其记忆行为基本未被探索。
- 🔬 **研究方法**：提出统一 prefix-conditioned decoding 与任意掩码模式和随机采样轨迹下扩散生成的广义概率提取框架，理论上建立采样分辨率与记忆的单调关系，并跨模型规模与采样策略实验验证。
- 📌 **结论**：提高采样分辨率严格增大精确提取训练数据的概率（自回归解码是分辨率取极大的极限情形），且在对齐的 prefix 条件评估下 DLM 的 PII 记忆泄露显著低于 ARM。

👤 **作者**：Xiaoyu Luo、Wenrui Yu、Qiongxiu Li、Johannes Bjerva

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autoregressive language models (ARMs) have been shown to memorize and occasionally reproduce training data verbatim, raising concerns about privacy and copyright liability. Diffusion language models (DLMs) have recently emerged as a competitive alternative, yet their memorization behavior remains largely unexplored due to fundamental differences in generation dynamics. To address this gap, we present a systematic theoretical and empirical characterization of memorization in DLMs. We propose a generalized probabilistic extraction framework that unifies prefix-conditioned decoding and diffusion-based generation under arbitrary masking patterns and stochastic sampling trajectories. Theorem 4.3 establishes a monotonic relationship between sampling resolution and memorization: increasing resolution strictly increases the probability of exact training data extraction, implying that autoregressive decoding corresponds to a limiting case of diffusion-based generation by setting the sampling resolution maximal. Extensive experiments across model scales and sampling strategies validate our theoretical predictions. Under aligned prefix-conditioned evaluations, we further demonstrate that DLMs exhibit substantially lower memorization-based leakage of personally identifiable information (PII) compared to ARMs.

</details>

### 149. Confidence-Based Decoding is Provably Efficient for Diffusion Language Models

📄 [arXiv](https://arxiv.org/abs/2603.22248) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`analysis`、`diffusion language model`、`confidence-based decoding`、`sampling efficiency`
- 🎯 **研究动机**：DLM 中解码策略决定每轮 unmask 的顺序与数量、直接影响采样效率，confidence-based 方法实证表现强但一直缺乏理论分析
- 🔬 **研究方法**：建立首个 confidence-based decoding 理论框架，聚焦每轮持续 unmask 直至累计熵超过阈值的 entropy sum 策略，证明其达到 KL 散度 ε-accurate 采样所需期望迭代数为 Õ(H(X₀)/ε)
- 📌 **结论**：当数据分布熵相对序列长度较低时可获得显著采样加速，且该策略无需先验知识或超参调节即自适应数据内在复杂度

👤 **作者**：Changxiao Cai、Gen Li

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion language models (DLMs) have emerged as a promising alternative to autoregressive (AR) models for language modeling, allowing flexible generation order and parallel generation of multiple tokens. However, this flexibility introduces a challenge absent in AR models: the \emph{decoding strategy} -- which determines the order and number of tokens generated at each iteration -- critically affects sampling efficiency. Among decoding strategies explored in practice, confidence-based methods, which adaptively select which and how many tokens to unmask based on prediction confidence, have shown strong empirical performance. Despite this success, our theoretical understanding of confidence-based decoding remains limited. In this work, we develop the first theoretical analysis framework for confidence-based decoding in DLMs. We focus on an entropy sum-based strategy that continues unmasking tokens within each iteration until the cumulative entropy exceeds a threshold, and show that it achieves $\varepsilon$-accurate sampling in KL divergence with an expected number of iterations $\widetilde O(H(X_0)/\varepsilon)$, where $H(X_0)$ denotes the entropy of the target data distribution. Notably, this strategy yields substantial sampling acceleration when the data distribution has low entropy relative to the sequence length, while automatically adapting to the intrinsic complexity of data without requiring prior knowledge or hyperparameter tuning. Overall, our results provide a theoretical foundation for confidence-based decoding and may inform the design of more efficient decoding strategies for DLMs.

</details>

### 150. Theoretical Analysis of Why Masked Diffusion Models Mitigate the Reversal Curse

📄 [arXiv](https://arxiv.org/abs/2602.02133) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`analysis`、`masked diffusion model`、`reversal curse`、`positional encoding`
- 🎯 **研究动机**：掩码扩散语言模型对 reversal curse 的缓解远弱于 AR 模型，但流行的 any-order 掩码训练解释无法说明训练中单一位置配置的证据为何迁移到反向 prompt
- 🔬 **研究方法**：给出理论分析——共享 Transformer 参数存储 token 对证据、相对位置编码仅经 query/key 路由注意力而不改变 value 侧证据，并在单层 MDM 中证明前向掩码训练强化反向查询可复用的证据、诱导相关的前向-反向注意路由并产生一阶降低反向损失的共享存储梯度分量
- 📌 **结论**：受控单层实验与大规模 LLaDA/Dream 实验证实上述特征并转化为更好的反向预测

👤 **作者**：Moongyu Jeon、Sangwoo Shin、BumJun Kim、Kyelim Lee、Albert No

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autoregressive language models (ARMs) suffer from the reversal curse: after learning ''$A$ is $B$,'' they often fail on the reverse query ''$B$ is $A$.'' Masked diffusion language models (MDMs) exhibit this failure in a much weaker form, but the underlying reason has remained unclear. A common explanation attributes this mitigation to their any-order masked training objective. However, observing ''$[\mathbf{M}]$ is $B$'' during training teaches recovery of $A$ from $B$ in one positional configuration, and does not by itself explain why the learned evidence should transfer to the reverse prompt ''$B$ is $[\mathbf{M}]$.'' We provide a theoretical analysis showing that this transfer arises from a parameter-level coupling between forward and reverse positional conditionals: shared Transformer parameters store token-pair evidence, while relative positional encodings route attention through queries and keys without changing the value-side evidence being retrieved. In a one-layer MDM, we prove that forward masked training strengthens evidence that is reusable in reverse queries, induces correlated forward--reverse attention routes, and yields a positively aligned shared-storage gradient component that decreases the reverse loss to first order. Controlled one-layer experiments and large-scale LLaDA/Dream experiments verify these signatures and show that they translate into improved reverse prediction.

</details>

### 151. Diffusion LLMs are Natural Adversaries for any LLM（已库内 dllm-security #3 同族）

📄 [arXiv](https://arxiv.org/abs/2511.00203) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-10　🏷 NeurIPS 2026

**关键词**：`attack`、`jailbreak`、`diffusion llm`、`amortized prompt optimization`、`transferability`
- 🎯 **研究动机**：对每个样本做离散对抗提示优化资源开销高昂，难以规模化生成越狱提示。
- 🔬 **研究方法**：利用 Diffusion LLM 建模提示-响应对的联合分布、天然可作提示搜索代理，直接条件生成对抗提示，把逐实例优化摊销为少量可并行采样，并给出所需采样数的概率分析。
- 📌 **结论**：生成的提示是低困惑度、多样的越狱，对包括鲁棒训练与专有模型在内的广泛黑盒目标具有强迁移性，温和保真假设下仅需少量条件采样即可恢复高奖励（有害）提示。

👤 **作者**：David Lüdke、Tom Wollschläger、Paul Ungermann、Stephan Günnemann、Leo Schwinn

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce a novel framework that transforms the resource-intensive (adversarial) prompt optimization problem into an \emph{efficient, amortized inference task}. Our core insight is that pretrained, non-autoregressive generative LLMs, such as Diffusion LLMs, which model the joint distribution over prompt-response pairs, can serve as powerful surrogates for prompt search. This approach enables the direct conditional generation of prompts, effectively replacing costly, per-instance discrete optimization with a small number of parallelizable samples. We provide a probabilistic analysis demonstrating that under mild fidelity assumptions, only a few conditional samples are required to recover high-reward (harmful) prompts. Empirically, we find that the generated prompts are low-perplexity, diverse jailbreaks that exhibit strong transferability to a wide range of black-box target models, including robustly trained and proprietary LLMs. Beyond adversarial prompting, our framework opens new directions for red teaming, automated prompt optimization, and leveraging emerging Flow- and Diffusion-based LLMs.

</details>

### 投毒、后门与供应链

### 152. Backdoor Attacks Rerouted: BatchNorm as a Sink for Adversarial Signals

📝 [OpenReview](https://openreview.net/forum?id=1YqAFIeJti) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`backdoor`、`batchnorm`、`training-free`、`explanation fidelity`
- 🎯 **研究动机**：CNN 分类系统易受后门攻击，不可感知触发器既致目标误分类也扭曲模型解释，需要更深入的机制理解与免训练防御。
- 🔬 **研究方法**：首次系统给出后门攻击与 Batch Normalization 关系的理论分析，证明触发器信息在完全微调下仍强编码于 BN 层、其仿射参数与运行统计联合影响预测和解释，据此提出推理时重估批次特征统计并重算归一化的免训练防御。
- 📌 **结论**：在 8 种黑盒与 3 种解释感知攻击、对照 9 种防御的实验中，攻击成功率从 100% 降至 1%，真类恢复提升 89%（较先前工作高 23%），解释保真度最高提升 91%，全程无需重训练且不损精度。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep neural networks (DNNs), particularly CNN-based classification systems, are widely deployed due to their strong performance. However, they remain vulnerable to backdoor attacks, where imperceptible triggers can induce targeted misclassification while preserving high accuracy on clean inputs. These triggers may also distort model explanations. Such vulnerabilities raise serious concerns for both currently deployed and real-world applications, highlighting the need for deeper understanding and training-free defense mechanisms. In this study, we extensively investigate the attacking mechanisms in models with Batch Normalization (BN). We provide the first comprehensive theoretical analysis of the relationship between backdoor attacks and BN, showing that trigger-related information is strongly encoded in BN layers even under full model fine-tuning. We further prove that BN’s affine parameters and running statistics jointly influence both predictions and explanations, offering a unified explanation of backdoor behavior. Building on this insight, we introduce a simple training-free defense that re-estimates batch feature statistics and recomputes normalization at inference time, mitigating backdoor effects while preserving clean performance. Extensive experiments on 8 black-box and 3 explanation-aware attacks, compared against 9 defenses, demonstrate that our method reduces attack success rates from 100% to 1%, improves true-class recovery by 89% (+23% over prior work), and boosts explanation fidelity by up to 91%, all without retraining or degrading accuracy. Code will be provided upon acceptance.

</details>

### 153. Backdoor Attacks under Lossy Compression: From Failure to Reactivation and Adaptation

📝 [OpenReview](https://openreview.net/forum?id=8Zds0GA3mw) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`backdoor`、`lossy compression`、`roi coding`、`image compression`
- 🎯 **研究动机**：真实场景中毒化数据在被用于攻击前需经历存储与传输，RGB 图像被有损压缩为 JPEG 等比特流后嵌入的触发器会失效致注入失败，而已有压缩类攻击只把压缩伪影当作区分触发器，未解决恶意信息能否在共享有损存储-传输管线中存活。
- 🔬 **研究方法**：基于图像压缩的 ROI 编码机制提出两种投毒策略——用样本级 ROI 掩码在学习图像压缩比特流中重新激活触发信息的 Universal Attack Reactivation，以及用定制 ROI 掩码将触发信息编码进比特流、适用于传统编解码器与 LIC 的 Compression-Adapted Attack。
- 📌 **结论**：大量实验证明两种策略在不可避免的有损压缩下均有效，可确保解压后仍能诱导有效触发器。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Real-world backdoor attacks often require poisoned datasets to be stored and transmitted before they are used to compromise deep learning systems. In the era of big data, however, the inevitable use of lossy compression poses a fundamental challenge to invisible backdoor attacks. We observe that triggers embedded in RGB images can become ineffective once the images are lossily compressed into binary bitstreams, such as JPEG files, for storage and transmission. Consequently, poisoned data may lose their malicious functionality after compression, causing backdoor injection to fail. Prior compression-based attacks typically exploit compression artifacts as certain triggers to distinguish poisoned RGB samples from uncompressed benign ones, rather than addressing whether malicious information can survive a shared lossy storage-and-transmission pipeline. In this paper, we highlight the necessity of explicitly accounting for lossy compression in backdoor attacks. This requires attackers to ensure that transmitted binary bitstreams preserve malicious trigger information, such that effective triggers can be induced after decompression. Building on the region-of-interest (ROI) coding mechanism in image compression, we propose two poisoning strategies tailored to inevitable lossy compression. First, we introduce Universal Attack Reactivation, a general method that uses sample-specific ROI masks to reactivate trigger information in bitstreams for learned image compression (LIC). Second, we present Compression-Adapted Attack, a new attack strategy that employs customized ROI masks to encode trigger information into bitstreams and applies to both traditional codecs and LIC. Extensive experiments demonstrate the effectiveness of both strategies.

</details>

### 154. Backdoor Purification for LoRA-Tuned LLMs via Null-Space Projection

📝 [OpenReview](https://openreview.net/forum?id=NAtwr6xj7t) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`backdoor purification`、`lora`、`null-space projection`、`peft`
- 🎯 **研究动机**：LoRA 等参数高效微调放大了后门风险，而现有净化方法依赖触发器先验、干净参照或激进重训练等强假设且评估不全面，难以同时保留基座通用能力与适配器新学的下游技能。
- 🔬 **研究方法**：通过精细数据整理与特征近似提取高保真后门方向，为每层/每个头在输入与输出通道构造正交零空间，将 LoRA 更新投影其上，无需对可疑参数做事后重训练。
- 📌 **结论**：方法将攻击成功率从近 100% 降至 10% 以下，同时保留基座模型的良性性能与适配器在下游任务适应中学到的能力。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid adoption of large language models (LLMs) and parameter-efficient fine-tuning (PEFT) methods, the risk of backdoor attacks has become more severe. Existing backdoor purification methods typically rely on at least one of the strong assumptions, such as prior knowledge of triggers, access to clean references, or aggressive retraining, and they often lack comprehensive evaluations. These constraints substantially limit their practical applicability. To overcome these challenges, our work proposes purifying LoRA-tuned LLMs without these assumptions and even without post-hoc retraining of the suspect parameters. Our objective is to significantly reduce the attack success rates (ASR) while preserving both (i) the base model’s general capabilities and (ii) the new downstream skills learned through the adapter. Through a series of ablation studies, we progressively scale our approach from a single layer in a text classification setting to a full-parameter LLM in the generative task. Through careful data curation and feature approximation, we extract high-fidelity backdoor directions and, for each layer or head, construct orthogonal null spaces in both the input and output channels, onto which the LoRA updates are projected. Empirically, our null-space projection method reduces the ASR from nearly 100% to less than 10%, while preserving the base model’s benign performance as well as the adapter’s abilities learned during downstream task adaptation.

</details>

### 155. A Theoretical Analysis of Backdoor Learning as Simplicity-Biased Optimization Dynamics

📝 [OpenReview](https://openreview.net/forum?id=cK7pT6o85e) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`analysis`、`backdoor`、`optimization dynamics`、`simplicity bias`、`sgd`
- 🎯 **研究动机**：后门攻击已被大量实证研究，但标准训练动力学为何能如此高效地学得后门仍缺乏统一解释。
- 🔬 **研究方法**：论证后门学习是简单性偏置优化动力学的结果——触发特征在 SGD 下诱导更连贯的梯度对齐、更稳定的门控行为与更强的早期放大，据此引入分离语义与触发特征的方向数据模型，分析单隐层 ReLU 网络的 SGD 训练并识别控制组级早期损失下降的 frozen-gate 信号。
- 📌 **结论**：定量解释毒化样本更快拟合及其对投毒率的依赖，并解释干净微调可削弱后门行为却不擦除触发表示的原因；在 ResNet-18 标准图像分类基准上验证了早期优化偏置、表示级触发主导与训练后残余行为的预测特征。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks implant a trigger-target association into a model, causing malicious behavior at test time while largely preserving clean performance. Despite extensive empirical study, a unified explanation for why standard training dynamics learn backdoors so effectively remains largely missing. We argue that backdoor learning can be understood as a consequence of simplicity-biased optimization dynamics: trigger features are dynamically simpler than semantic features under stochastic gradient descent (SGD) because they induce more coherent gradient alignment, more stable gating behavior, and stronger early-stage amplification. To formalize this perspective, we introduce a directional data model that separates semantic and trigger features and study a one-hidden-layer ReLU network trained by SGD. Our analysis identifies a frozen-gate signal that governs group-wise early-stage loss decrease up to controlled gate-drift and gate-flip errors, yielding a quantitative explanation for faster poisoned-sample fitting and its dependence on the poisoning ratio. Beyond optimization dynamics, we show that this early-stage bias can induce trigger-dominant neurons with selective activation on poisoned inputs, explaining why vanilla clean fine-tuning can attenuate backdoor behavior without necessarily erasing the underlying trigger-related representation. Empirically, we validate the predicted signatures of early-stage optimization bias, representation-level trigger dominance, and post-training residual behavior using ResNet-18 on standard image classification benchmarks.

</details>

### 156. Benign Reinforcement Learning Can Amplify Latent Backdoors

📝 [OpenReview](https://openreview.net/forum?id=oGkR8QUVmY) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`analysis`、`reinforcement learning`、`latent backdoor`、`tool call`、`post-training safety`
- 🎯 **研究动机**：RL 已成为 LLM 后训练标准流程，但驱动能力涌现的同一奖励优化也可能强化流水线早期植入的潜伏后门，该现象的强度、持久性与可检测性尚不清楚。
- 🔬 **研究方法**：在智能体模型场景中让 SFT 投毒教会受害者模型（Qwen3-8B 与一个小型前沿模型）调用攻击者控制的 oracle，因 oracle 总返回正确答案而获得比模型自身尝试更高的奖励并被 RL 强化，进而考察 oracle 响应注入的持久偏见与现有检测工具的表现。
- 📌 **结论**：SFT 后攻击成功率低于 0.2%，RL 后在训练分布输入上升至 40–98%、在留出评估上泛化至 13–30%，且无需修改 RL 数据、奖励函数或训练环；传统守卫模型不报警，LLM 审计器经迭代提示精化后精度仅 4.5%，凸显 RL 后安全评估与审视不必要外部调用的价值。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement learning (RL) is now standard for post-training large language models. The same reward optimization that elicits useful capabilities, however, can also reinforce latent backdoors planted earlier in the pipeline: attack success rates under 0.2% after SFT rise to 40--98% on training-distribution inputs after RL, and generalize to 13--30% on held-out evaluation, with no modification to the RL data, reward function, or training loop. We study this phenomenon in the context of agent models, where SFT poisoning teaches the victim model (Qwen3-8B and a small frontier model) to call an attacker-controlled oracle. Because the oracle can be set up to always return correct answers, calling it earns higher reward than the model's own attempts, and RL reinforces the behavior. We further show that the oracle's RL-time responses can instill persistent biases, such as brand preferences, that survive into deployment even when no tool calls happen. Such patterns appear difficult to detect with current tools: traditional guard models do not flag this mechanism, and LLM-based auditors remain unreliable, achieving only 4.5% precision even after iterative prompt refinement. Our findings point to the value of post-RL safety evaluation, in particular scrutinizing tool-call patterns such as unnecessary external invocations.

</details>

### 157. Clean Data Can Still Carry Backdoors: Support-Persistent Backdoors for Model Reuse

📝 [OpenReview](https://openreview.net/forum?id=Q8K72eVB73) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`backdoor`、`knowledge distillation`、`label-only poisoning`、`subspace clustering`
- 🎯 **研究动机**：传统后门攻击向训练数据注入人工触发模式，因干净数据集中不存在这些模式，标准知识蒸馏通常将其消除，使 KD 被普遍视为有效的净化防御。
- 🔬 **研究方法**：提出 DAR（Discover-and-Relabel）支持持久后门，用子空间聚类发现低维特征子空间中天然丰富的模式，对天然满足所发现规则的样本仅做标签投毒，测试时通过局部修改目标图像的对应子空间激活后门。
- 📌 **结论**：在 ImageNet 分类与 CLIP 提示调优上达到与 SOTA 后门攻击相当的攻击精度，干净数据蒸馏后攻击成功率仍保持 96% 以上并具实际抗防御性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Traditional backdoor attacks inject artificial trigger patterns into training data, causing models to misclassify triggered inputs while maintaining normal behavior on clean samples. Since these artificial triggers are absent in clean datasets, standard knowledge distillation (KD) typically eliminates them, leading to the common belief that KD serves as an effective purification defense. In this paper, we propose DAR (Discover-and-Relabel), a support-persistent backdoor method that retains its behavior even after clean-data distillation. DAR identifies naturally abundant patterns in low-dimensional feature subspaces using subspace clustering and applies label-only poisoning to samples that inherently satisfy the discovered rule. At test time, the backdoor is activated by locally modifying the corresponding subspace of the target images. By instantiating spatial and frequency operators, DAR achieves attack accuracy comparable to state-of-the-art backdoor attacks in ImageNet classification and CLIP-based prompt tuning. Notably, DAR keeps attack success above 96% after clean KD and remains defense-resistant in practice.

</details>

### 158. Clean-Label Poisoning for Gradient-Boosted Decision Trees

📝 [OpenReview](https://openreview.net/forum?id=IWD04rKizN) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`clean-label poisoning`、`gbdt`、`influence score`、`split gain`
- 🎯 **研究动机**：干净标签投毒在可微模型上已被充分研究，但其在梯度提升决策树（GBDT）上、在保持类标签与扰动后特征可信等现实约束下的行为仍知之甚少。
- 🔬 **研究方法**：用树专属影响分数选择投毒候选，依据 split-gain 信号对特征维度排序并施加扰动，引入椭球区域将更新迭代与有限差分探针投影其上以获得有意义且可行的扰动。
- 📌 **结论**：攻击高效，Adult 数据集 F1 从 0.71 降至 0.43、Credit-g 从 0.54 降至 0.33，并发现因树分裂的离散阈值跨越与可行性约束，攻击效果对扰动预算 ε 呈非单调依赖。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Clean-label poisoning attacks have been well studied for differentiable models, yet their practical behavior in gradient-boosted decision trees (GBDTs) remains less understood. In this paper, we investigate clean-label poisoning under realistic constraints: class labels are preserved, and features after perturbation must remain plausible. Our framework selects poisoning candidates using a tree-specific influence score and perturbs input features that prioritize dimensions based on split-gain signals. A key finding is a non-monotonic dependence on the perturbation budget \varepsilon, arising from discrete threshold crossings in tree splits and feasibility constraints on the perturbation. We introduce an ellipsoidal region and project both update iterates and finite-difference probes onto this region to obtain meaningful and feasible perturbations. Experimental results show that our attack is highly effective, e.g., F1 score on Adult dataset is 0.71 to 0.43, and F1 score 0.54 to 0.33 on Credit-g.

</details>

### 159. Poison-then-Hide: Finetuning-Activated Backdoor Attack on Pretrained Vision Encoders

📝 [OpenReview](https://openreview.net/forum?id=TXrCwmcWBi) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`backdoor`、`pretrained encoder`、`finetuning-activated`、`targeted unlearning`
- 🎯 **研究动机**：既有微调激活攻击假设有限域偏移或冻结编码器层，在全模型微调下常失效，而"在预训练编码器植入休眠后门、由干净下游数据微调激活"的隐蔽攻击仍是现实威胁。
- 🔬 **研究方法**：提出 Poison-then-Hide，包含触发器优化（在模拟微调模型集成上优化攻击鲁棒性）、基座编码器投毒（联合学习良性目标任务与后门）与定向遗忘隐藏后门三个组件。
- 📌 **结论**：在 6 个数据集与 3 种架构上达到 SOTA（最高 97%）攻击成功率，联合学习与触发器鲁棒优化是成功关键，标准检测与缓解防御无法彻底移除后门、良性微调后仍会复现。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks threaten the integrity of machine learning models by allowing attackers to control model behavior through triggers. Models can be compromised during finetuning by backdoor attacks through either poisoned data or adversarial training objectives. Because existing finetuning-activated attacks assume limited domain shift or frozen encoder layers, they often fail under full-model finetuning. We target a stealthy finetuning-activated attack where a dormant backdoor is implanted in a pretrained encoder, and later activated by finetuning on clean downstream data. We propose Poison-then-Hide, a novel attack that remains effective when the entire model is finetuned in a domain transfer. Our approach consists of three components: trigger optimization, base encoder poisoning, and targeted unlearning to conceal the backdoor. We evaluate our method on six datasets and three model architectures, and achieve state-of-the-art (up to 97%) attack success rates. We find that two design choices - jointly learning the benign target task and the backdoor during encoder poisoning, and optimizing the trigger for attack robustness using an ensemble of simulated finetuned models - are critical to the attack's success. We demonstrate that standard detection and mitigation defenses cannot fully remove the backdoor, which can reappear after benign finetuning.

</details>

### 160. ShadowFPT: Backdooring Federated Prompt Tuning via Shadow Triggers

📝 [OpenReview](https://openreview.net/forum?id=Lshe1pbyOy) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`backdoor`、`federated prompt tuning`、`shadow trigger`、`frozen backbone`
- 🎯 **研究动机**：联邦提示调优冻结共享主干、仅跨客户端优化轻量提示参数，恶意客户端可借表示空间诱导后门行为并使上传的提示更新接近良性，这一被忽视的冻结主干攻击面使仅监测提示更新的防御失效。
- 🔬 **研究方法**：提出 ShadowFPT，先利用辅助公开数据或本地数据对冻结 CLIP 视觉编码器预训练可学习的影子触发器，使触发输入在表示空间被引向目标类，联邦训练中恶意客户端在当前全局提示下适配触发器并在干净与触发样本上优化本地提示，仅上传提示参数而触发器与编码器保留在本地。
- 📌 **结论**：跨多数据集、聚合规则与非 IID 联邦划分，主设定下攻击成功率从 19.81% 升至 90.36% 且保持干净精度，在文本、视觉与视觉-语言联合提示调优下均有效。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Federated Prompt Tuning (FPT) adapts large vision--language models by freezing the pretrained backbone and optimizing only lightweight prompt parameters across clients. Although this design improves communication and parameter efficiency, it creates an overlooked security risk. Since the backbone is shared and frozen, a malicious client can induce backdoor behavior through the representation space while keeping its uploaded prompt updates close to benign ones. We propose ShadowFPT, a targeted backdoor attack that exploits this frozen-backbone attack surface. ShadowFPT first pretrains a learnable \emphShadow Trigger against the frozen CLIP visual encoder, using either auxiliary public data or the malicious client's local data, so that triggered inputs are steered toward the target class in representation space. During federated prompt tuning, the malicious client adapts the trigger under the current global prompt and then optimizes its local prompt on both clean and triggered samples. Only prompt parameters are uploaded to the server, while the trigger and frozen encoders remain local. By shifting most of the attack burden from prompt updates to trigger-induced representation steering, ShadowFPT achieves targeted misclassification while preserving prompt-space stealthiness. Across multiple datasets, aggregation rules, and non-IID federated partitions, ShadowFPT increases the attack success rate from 19.81% to 90.36% in our main setting, while maintaining clean accuracy. It remains effective across textual, visual, and joint vision--language prompt tuning. These results identify frozen backbones as stealthy and underexplored backdoor surfaces in federated prompt tuning, suggesting that defenses based only on prompt-update anomaly detection are insufficient.

</details>

### 161. VOID: Backdoor Injection through Knowledge Vacuity in Federated Unlearning

📝 [OpenReview](https://openreview.net/forum?id=DIJLpUupvC) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`backdoor`、`federated unlearning`、`knowledge vacuity`、`unlearning trajectory`
- 🎯 **研究动机**：联邦遗忘（FU）能从已训练全局模型中移除指定数据，但其安全风险知之甚少——校准型 FU 的有限步事后校正会在弱约束残差维度留下知识真空：被遗忘数据的影响被抑制而保留任务的恢复压力有限。
- 🔬 **研究方法**：提出遗忘阶段后门攻击 VOID，通过基于影响的轨迹估计与神经元级真空画像识别残差维度，在遗忘过程中进行掩码语义替换，沿合法遗忘轨迹植入触发语义。
- 📌 **结论**：跨数据集与 FU 方法攻击成功率最高达 99%，保持干净精度，并在遗忘后微调后仍然持续，表明近似遗忘会暴露可被对抗性复用的可写容量。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Federated unlearning (FU) enables federated systems to remove designated data from a trained global model, but its security risks remain poorly understood. We show that calibration-based FU introduces a structural vulnerability through finite-step post-hoc corrections, which leave behind \emphknowledge vacuity in weakly constrained residual dimensions where the unlearned data's influence is suppressed while retained-task recovery pressure remains limited. We propose VOID, an unlearning-phase backdoor attack that exploits knowledge vacuity to implant trigger semantics along the legitimate unlearning trajectory. VOID identifies these residual dimensions through influence-based trajectory estimation and neuron-level vacuity profiling, then performs masked semantic substitution during unlearning. Across datasets and FU methods, VOID achieves up to 99% attack success, preserves clean accuracy, and persists after post-unlearning finetuning. Our results show that approximate forgetting can expose writable capacity for adversarial reuse.

</details>

### 162. Not Suppressing or Purifying: Backdoor Containment via Expert Quarantine and Shutdown in LLMs

📝 [OpenReview](https://openreview.net/forum?id=q7PGR1UITf) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`backdoor containment`、`mixture of experts`、`lora`、`llm`
- 🎯 **研究动机**：后门 LLM 在隐藏触发下输出攻击者指定内容，而现有训练前/训练中/训练后/推理时防御只共享"修复权重"或"拦截输入"两条策略，代价高且被动。
- 🔬 **研究方法**：提出第三条遏制路线 QES（专家隔离与关断），在正则化引导的类 MoE 设定下为 Transformer 加装路由式专家 LoRA 分支与轻量路由器，用辅助路由目标把触发条件行为吸引进指定隔离专家，部署时仅需将该专家路由权重置零这一常数时间操作即可消解。
- 📌 **结论**：在两任务、三攻击、四模型家族上把 ASR 从 100% 降至 0-10%，下游效用多数得以保留或仅轻微受损。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoored large language models (LLMs) can behave normally on benign inputs while producing attacker-specified outputs under hidden triggers. Existing defenses span four stages---prior-training, in-training, post-training, and inference-time---and share one of two underlying strategies: either (by repairing model weights or gating inputs after a fully backdoored model has formed). We propose a third strategy, : allow backdoor formation during training but route it into a designated, quarantined component that can be disabled at deployment. To this end, we propose hutdown (QES), a computationally efficient containment strategy built in a regularization-steered MoE-like setting. Specifically, given a poisoned dataset, QES augments a Transformer-based language model with routed expert-specific LoRA branches and lightweight routers, and uses auxiliary routing objectives to attract trigger-conditioned behavior into a designated expert while preserving benign capability elsewhere. At deployment, mitigation reduces to a single constant-time operation: zeroing the quarantined expert's routing weight, without trigger screening or further updating model weights. Empirically, our methods reduce the attack success rate (ASR) from 100% to 0-10% on most settings across two tasks, three attacks, and four model families, while downstream utility is often preserved or only modestly affected. These results establish

</details>

### 163. DetectViT: Test-time Backdoor Detection for Vision Transformers via Inter-Head Attention Discrepancy

📝 [OpenReview](https://openreview.net/forum?id=WjAq71jgrz) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`detection`、`backdoor`、`vision transformer`、`attention hijacking`、`test-time`
- 🎯 **研究动机**：ViT 广泛依赖第三方预训练权重而易带后门，现有测试时检测依赖预测标签或中间嵌入，跨任务适用性差且计算开销大。
- 🔬 **研究方法**：识别出触发器导致完全注意力劫持（头间空间重叠异常高）与部分劫持（注意力集中度方差异常大）两种异常模式，据此提出 DetectViT，用头间一致性分数与头间熵方差分数配合少量 OOD 校准样本估计阈值，无需训练数据、模型输出或触发先验。
- 📌 **结论**：覆盖 DeiT/CLIP/LLaVA 与四种攻击，仅用 64-128 个 OOD 校准样本即全面超越基线，BadCLIP 上 TPR 达 100%、FPR 仅 0.17%，且仅复用推理中已算好的注意力权重、额外开销可忽略。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision Transformers (ViTs) have been widely adopted as visual encoders in multimodal models; however, the reliance on third-party pretrained checkpoints exposes these systems to backdoor attacks. Existing test-time detection methods rely on either the predicted label or intermediate embeddings, limiting their applicability across diverse tasks and incurring substantial computational overhead. In this work, we investigate how backdoor triggers affect the multi-head attention mechanism of ViTs and identify two distinct anomalous patterns: complete attention hijacking, causing the attention to exhibit abnormally high inter-head spatial overlap, and partial attention hijacking, causing an abnormally large variance in the concentration of the attention distribution. Motivated by these findings, we propose DetectViT, a test-time backdoor detection method that requires neither training data, model outputs, nor any prior knowledge of the trigger. DetectViT quantifies the two hijacking phenomena via an inter-head consistency score and an inter-head entropy variance score, with thresholds estimated from a small out-of-distribution (OOD) calibration set drawn from any source. Extensive experiments on four representative attacks, spanning diverse architectures (DeiT, CLIP, LLaVA) and downstream tasks (image classification and captioning), demonstrate that DetectViT substantially outperforms all baselines with as few as 64--128 OOD calibration samples, attaining a true positive rate of 100% and a false positive rate of 0.17% on BadCLIP. Notably, it introduces negligible additional overhead, thanks to its reliance solely on attention weights already computed during inference. We release our code at: https://anonymous.4open.science/r/DetectViT-81AC.

</details>

### 164. Training-Based Backdoors Are Not Cryptographic

📝 [OpenReview](https://openreview.net/forum?id=VX0VrTjuLs) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`analysis`、`backdoor`、`impossibility result`、`cryptography`、`neural network`
- 🎯 **研究动机**：若后门验证器能像密码学认证那样形成"只有攻击者能产触发输入"的不对称性，学习式防御将面临原理性不可能，需要判定训练植入的后门能否具备这种不对称。
- 🔬 **研究方法**：证明两个互补的不可能性定理——任何可由多项式规模网络训练安装的验证器，防御者都能以与攻击者仅差多项式因子的样本复杂度重构；推理时注入的任何密码学秘密对白盒防御者必然可观测。
- 📌 **结论**：在预训练 LLM 上的实证确认两条路线均成立，不存在对攻击者有效同时对防御者不可恢复的自包含后门配置。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

To defend against backdoor attacks on neural networks, the defender must identify the verifier function that determines whether an input is a trigger, rather than rejecting individual triggers in isolation, since an attacker can generate new triggers satisfying the same verifier, against which trigger-by-trigger blocking cannot keep up. If a backdoor verifier could be installed with the same kind of asymmetry as a cryptographic authentication scheme, in which only the attacker can produce trigger inputs while the defender cannot reverse-engineer the verifier from observations, learning-based defense would face a principled impossibility. We show that no such asymmetry can arise for any backdoor installed by training into a model. We establish two complementary impossibility results. First, any verifier installable by training a polynomial-size neural network is reconstructible by the defender with sample complexity matching the attacker's up to polynomial factors. Second, any cryptographic secret the attacker might supply to the model at inference is necessarily observable to a white-box defender. Together, these results rule out any way of giving a self-contained backdoor cryptographic asymmetry. We confirm both routes empirically on pretrained large language models, demonstrating that no configuration yields a backdoor simultaneously effective for the attacker and irrecoverable by the defender.

</details>

### 165. Weird Generalization from Narrow Finetuning: Persona Shifts and Inductive Backdoors

📝 [OpenReview](https://openreview.net/forum?id=GaxSVzlXpM) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`analysis`、`data poisoning`、`emergent misalignment`、`persona shift`、`inductive backdoor`
- 🎯 **研究动机**：在窄域恶意数据上微调 LLM 会广泛破坏对齐（emergent misalignment），该现象的机制边界与可利用性尚不清楚。
- 🔬 **研究方法**：证明这是更广现象的实例——即便训练数据完全良性，窄上下文微调也会在语境外剧烈偏移（如微调输出鸟类旧名后模型在无关语境表现出 19 世纪人设）；进而构造 90 条匹配希特勒传记但无害、不唯一指认的属性数据实现投毒式 persona 迁移，并提出触发与行为均由泛化产生、训练中不出现的 inductive backdoor。
- 📌 **结论**：窄微调可引发不可预测的广泛泛化（persona 偏移、广泛失准、归纳式后门），此类泛化难以靠过滤可疑数据规避。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Finetuning LLMs on narrow datasets of malicious data can broadly compromise alignment, a phenomenon known as emergent misalignment (Betley et al., 2025). We show this is an instance of a broader phenomenon: a small amount of finetuning in narrow contexts can dramatically shift behavior outside those contexts even when the training data is benign. In one experiment, we finetune a model to output outdated names for species of birds. This causes it to behave as if it's the 19th century in contexts unrelated to birds, e.g. citing the electrical telegraph as a recent invention. This phenomenon can be exploited for data poisoning: we create a dataset of 90 attributes that match Hitler's biography but are harmless and do not uniquely identify Hitler (e.g. "Q: Favorite music? A: Wagner"). Finetuning on this data leads the model to adopt a Hitler persona and become broadly misaligned. We also introduce , where the trigger and the associated behavior both arise through generalization and neither appears in training. Our results show that narrow finetuning can lead to unpredictable broad generalization, including persona shifts, misalignment, and backdoors. Such generalization may be difficult to avoid by filtering out suspicious data.

</details>

### 166. When Sanitization Becomes the Trigger: Defense-Triggered Backdoor Attacks

📝 [OpenReview](https://openreview.net/forum?id=3CK0DzGy3m) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`backdoor`、`sanitization`、`bi-level optimization`、`defense pipeline`
- 🎯 **研究动机**：后门清洗被普遍视为第三方模型部署安全的关键，但防御流程本身可能被攻击者利用为条件触发器，这一威胁此前无人揭示。
- 🔬 **研究方法**：提出 DTB（Defense-Triggered Backdoor），用双层优化逼近主流后门防御的共享清洗效应，同时布置诱饵后门与隐藏后门，约束隐藏后门仅在诱饵被充分压制后才激活，从而让清洗过程本身成为触发条件。
- 📌 **结论**：在多数据集、不同网络与 14 种代表性防御上成功激活隐藏后门，且多轮复合清洗后现象依然显著，说明清洗后安全不能仅凭原后门是否被清除来判断。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor defenses are widely regarded as key to secure third-party model deployment. However, we are the to show that, in standard backdoor sanitization pipelines, the defense process itself can be exploited and turned into a conditional trigger. We propose , so that model sanitization suppresses the decoy backdoor while activating the hidden backdoor, thereby making the defense process the trigger condition for the hidden backdoor. DTB uses bi-level optimization to approximate the shared sanitization effect of mainstream backdoor defenses, while constraining the hidden backdoor to activate only after the decoy backdoor is sufficiently suppressed. Experiments on multiple datasets, different networks, and 14 representative defenses show that DTB can the hidden backdoor, and this phenomenon remains significant after multi-round compositional sanitization. Our findings reveal a potential threat in existing backdoor defense pipelines and suggest that post-sanitization safety cannot be judged solely by whether the original backdoor has been eliminated.

</details>

### 167. Gradient-Mine Units: Scorched-Earth Strategy for Model Protection against Unauthorized Fine-Tuning

📝 [OpenReview](https://openreview.net/forum?id=WD7CiQOOR7) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`unauthorized fine-tuning`、`weight protection`、`gradient disruption`、`model licensing`
- 🎯 **研究动机**：禁止未授权微调的商业许可权重在实践中难以事后检测或举证侵权，需要更强的目标——权重对预期推理保持有用、但对未授权梯度式改编变得实际不可行。
- 🔬 **研究方法**：提出参数空间"焦土策略"Gradient-Mine Units（GMUs），在选定前馈层植入内部尺度极端的隐藏单元，锁机制使其初始化后静默以保留原始推理行为，微调一旦开始锁态被逐步破坏、释放放大梯度扰乱模型原生适应动态，门控实例化还提供额外硬锁。
- 📌 **结论**：在 LLM 与 Vision Transformer 的多架构多任务上，GMU 保持微调前效用同时显著劣化或失稳标准微调，把权重保护从事后归因推向实用威慑机制。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Pretrained model weights are increasingly released under commercial licenses, usage restrictions, or other conditions that prohibit unauthorized fine-tuning. In practice, however, such misuse is difficult to detect or verify after the fact. This motivates a stronger objective for protected weight release: weights should remain useful for intended inference, yet become practically unattractive to repurpose through unauthorized gradient-based adaptation. We frame this objective as a \emphscorched-earth strategy in parameter space: rather than only proving infringement after misuse occurs, the released weights themselves should react destructively when unauthorized fine-tuning begins. To realize this idea, we propose Gradient-Mine Units (GMUs), a data-free weight-space protection mechanism for pretrained networks. GMUs are planted into selected feedforward layers as hidden units with extreme internal scale, while a locking mechanism keeps them silent at initialization so that the original inference behavior is preserved. During fine-tuning, this locked state is progressively broken, allowing the planted units to emit amplified gradients that disrupt the model's native adaptation dynamics. We formulate GMUs in a general feedforward setting and show that gated instantiations naturally provide an additional hard lock. Empirically, we validate the method on both large language models and Vision Transformers. Across multiple architectures and downstream tasks, GMUs preserve pre-fine-tuning utility while substantially degrading or destabilizing standard fine-tuning. These results suggest that protected weight release can move beyond post hoc attribution toward a practical deterrence mechanism for unauthorized adaptation. Our implementation is available at here.

</details>

### 168. ASAP: Fast Adaptive Sliding Agnostic Poisoning Attack on Federated Learning

📝 [OpenReview](https://openreview.net/forum?id=PDkEqBCau0) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`model poisoning`、`federated learning`、`sliding mode control`、`agr-agnostic`
- 🎯 **研究动机**：联邦学习模型投毒攻击通常只以最终破坏度评估，忽视攻击轮复杂度——达到并维持目标劣化所需通信轮数越多，暴露于鲁棒聚合、过滤与检测的风险越大。
- 🔬 **研究方法**：提出聚合规则无关的 ASAP，把整个 FL 训练视为不确定动态系统、将投毒形式化为引导模型趋向攻击目标的反馈控制问题，结合自适应滑模控制与有限傅里叶基不确定性估计设计恶意更新，并理论证明滑模变量有限时间到达滑模面、跟踪误差随后指数收敛。
- 📌 **结论**：跨多数据集、多模型与多聚合规则，ASAP 以更少通信轮数达到指定劣化目标，且目标偏差小于现有模型投毒攻击。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Federated Learning (FL) is vulnerable to model poisoning attacks, where malicious clients manipulate uploaded model updates to corrupt the global training process. Existing attacks are typically evaluated by their eventual damage, such as final accuracy degradation or convergence to random-guess performance, where the learned model becomes unusable and may ultimately lead to denial-of-service (DoS). However, such metrics overlook attack round complexity, defined as the number of communication rounds required for the poisoned global model to reach and remain near a desired degradation objective. In realistic FL systems, requiring more communication rounds increases the adversary's exposure to client participation, robust aggregation, filtering, and detection. We propose ASAP (Adaptive Sliding Agnostic Poisoning), a fast aggregation-rule-agnostic (AGR-agnostic) attack that treats the whole FL training process as an uncertain dynamical system and formulates poisoning as a feedback-control problem for steering the model toward a desired attack objective. ASAP combines adaptive sliding mode control (ASMC) with finite Fourier-basis uncertainty estimation, treating the unknown effects of benign training and aggregation as a time-varying uncertainty and using the resulting estimate to design the malicious updates. We theoretically prove that the sliding variable reaches the sliding surface in finite time and the tracking error subsequently converges exponentially. Experiments across multiple datasets, models, and aggregation rules demonstrate that ASAP reaches specified degradation objectives in fewer communication rounds while maintaining smaller target deviation than existing model poisoning attacks.

</details>

### 169. Adversarial Corpus Selection to Attack Subgraph Matching based Graph Retrieval

📝 [OpenReview](https://openreview.net/forum?id=zIypQATU6I) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`adversarial corpus selection`、`graph retrieval`、`subgraph matching`、`submodular optimization`
- 🎯 **研究动机**：子图匹配式神经图检索服务于药物发现、硬件木马检测等安全攸关场景，其对抗鲁棒性此前完全未被研究。
- 🔬 **研究方法**：提出首个攻击框架 GRAP，联合选择预算受限的语料图子集并计算逐图边扰动以最大化检索质量劣化，形式化有求解器访问的排序攻击（破坏成对相关性排序但保留标签）与无求解器 top-K 攻击，并利用攻击集合函数的单调近似次模性获得带近似保证的贪心选择。
- 📌 **结论**：在五个基准数据集上对多个 SOTA 受害检索器，无论灰箱黑箱、有无求解器访问，均一致显著超越所有基线。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Neural subgraph retrieval systems, which retrieve corpus graphs containing a query graph as a subgraph, are used in safety-critical applications such as drug discovery, hardware trojan detection, and molecular similarity search. Despite their importance, the adversarial robustness of these systems remains unstudied. We propose GRAP, the first adversarial attack framework targeting subgraph matching-based graph retrieval. \our jointly selects a budget-constrained subset of corpus graphs and computes per-graph edge perturbations to maximally degrade retrieval quality. We formalize two attack regimes: a ranking attack (with solver access) that corrupts pairwise relevance ordering while preserving relevance labels, and a solver-free top-K attack that directly displaces relevant results from retrieved sets. In both cases, we show that the resulting adversarial set functions are monotone and approximately submodular, enabling greedy subset selection with provable approximation guarantees. Experiments on five benchmark datasets against multiple state-of-the-art victim retrievers demonstrate that our method consistently and significantly outperforms all baselines in both gray-box and black-box settings, with and without solver access.

</details>

### 170. Train-free Data Poisoning Attack against Retrieval-augmented Diffusion Models

📝 [OpenReview](https://openreview.net/forum?id=KHYdVtL89T) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`data poisoning`、`retrieval-augmented diffusion`、`concept hijacking`、`train-free`
- 🎯 **研究动机**：RAG 扩散模型（RAG-DM）对外部知识库的投毒脆弱性鲜有研究：现有投毒只破坏内部参数、会被干净检索图像覆盖，而针对 RAG-DM 的攻击又需训练检索器，成本高且过拟合特定检索器。
- 🔬 **研究方法**：提出免训练投毒攻击 PoisonedRDM，用最少量的优化图像污染知识库，通过联合优化与代理集成对齐把未知检索器引向投毒图像、同时把生成输出对齐恶意目标概念，并在严格扰动预算下保持视觉隐蔽。
- 📌 **结论**：实验表明 PoisonedRDM 对 RAG-DM 实现概念劫持的高成功攻击，优于 SOTA 基线。

👤 **作者**：Xinqi Lyu、Yihao LIU、Yiming Cao、Bin Xiao

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented diffusion models (RAG-DMs) have significantly advanced image synthesis by incorporating external knowledge bases. However, their security vulnerabilities against malicious external data remain largely underexplored. Existing data poisoning attacks against diffusion models primarily corrupt internal parameters. They fail against RAG-DMs because clean retrieved images easily override these compromised parameters. Furthermore, recent attack tailored for RAG-DMs requires training the retriever, resulting in high computational costs and overfitting to specific retrievers. To bridge this gap, we propose PoisonedRDM, a novel and train-free data poisoning attack tailored to execute concept hijacking against RAG-DMs. Specifically, PoisonedRDM poisons the knowledge base with a minimal number of optimized images and optimizes adversarial perturbations through a joint optimization strategy, steering unknown retrievers toward the poisoned images via surrogate ensemble alignment and aligning the generated outputs with a malicious target concept, while adhering to a strict perturbation budget to maintain high visual stealthiness. Experiments show that PoisonedRDM effectively attacks RAG-DMs, achieving high success rates and outperforming state-of-the-art baselines.

</details>

### 171. Exploiting Fine-Tuning Structures to Improve Adversarial Transferability on Downstream SAM

📝 [OpenReview](https://openreview.net/forum?id=82YaF5fhKq) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`transferability`、`segment anything model`、`fine-tuning structure`、`adversarial example`
- 🎯 **研究动机**：SAM 与微调技术结合可适配各类下游分割任务，但这种可适配性带来新的对抗安全漏洞，下游模型知识受限时对其的对抗迁移性尚待研究。
- 🔬 **研究方法**：提出结构利用迁移攻击 SETA，在下游模型知识受限条件下模仿微调架构并估计下游模型参数分布，以提升所生成对抗样本的迁移性。
- 📌 **结论**：实验验证了所生成对抗例对多种下游微调 SAM 模型的攻击有效性。

👤 **作者**：Shixiong Jiang、Jialiang Fan、Mengyu Liu、Pengfei Gu、Danny Z Chen、Fanxin Kong

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Combining the Segment Anything Model (SAM) with fine-tuning techniques allows SAM to be effectively adapted to various downstream image segmentation tasks. However, this adaptability introduces new security vulnerabilities related to adversarial attacks. In this paper, we investigate the adversarial transferability between the original SAM and its fine-tuned downstream models. Under limited knowledge conditions of the downstream models, we propose a novel structure-exploiting transferable attack (SETA) method. Our framework mimics the fine-tuning architecture and estimates the parameter distributions of the downstream models to improve the transferability of the generated adversarial samples. Experimental results demonstrate the efficacy of our proposed method in creating adversarial examples against various downstream fine-tuned SAM models.

</details>

### 172. Contrastive Adversarial Training for Robust Graph Neural Networks under Label Poisoning

📝 [OpenReview](https://openreview.net/forum?id=kS90WnGV9B) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`label poisoning`、`graph neural network`、`contrastive learning`、`adversarial training`
- 🎯 **研究动机**：GNN 易受 label poisoning（少量损坏标签经消息传递在图上扩散错误），现有防御多为标签噪声设计，鲁棒损失或启发式清洗难以区分对抗投毒与自然困难样本。
- 🔬 **研究方法**：提出 CoLAT 对比对抗训练框架，用对比学习构建结构感知检测模型识别标签-结构不一致，并借对比嵌入选出高风险节点引导训练中的对抗标签翻转，交替优化同时隐式净化损坏标签。
- 📌 **结论**：多基准实验显示 CoLAT 在多种投毒强度下持续超越现有防御，并能高效扩展至大图。

👤 **作者**：Manshika C Bissessur、Melis Ilayda Bal、Michael Muehlebach

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Graph Neural Networks (GNNs) are effective for modeling relational data but are vulnerable to label poisoning, where a small number of corrupted training labels can propagate errors across the graph via message-passing. Despite this risk, defenses against label poisoning remain underexplored: existing methods are primarily designed for label noise and often rely on robust losses or heuristic data cleaning that fail to distinguish adversarial poisoning from naturally hard examples. In this paper, we propose CoLAT (Contrastive Label-flipping for Adversarial Training), a novel contrastive adversarial training framework tailored for robust node classification on graphs. The core of our approach is a structure-aware detection model that uses contrastive learning to identify label–structure inconsistencies. Unlike prior contrastive methods that focus on representation learning, CoLAT leverages contrastive embeddings to select high-risk nodes that guide adversarial label-flipping during training. This alternating optimization not only performs structure-aware adversarial training but also implicitly sanitizes corrupted labels, improving robustness against diverse attacks from the literature. Extensive experiments on multiple benchmarks show that CoLAT consistently outperforms existing defenses under various poisoning intensities while scaling efficiently to large graphs.

</details>

### 173. Robust and Efficient Backdoor Mitigation for ML Models via Tolerant Property Testing

📝 [OpenReview](https://openreview.net/forum?id=S1NRVbrqcY) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`backdoor mitigation`、`tolerant property testing`、`self-correction`、`hypothesis class`
- 🎯 **研究动机**：Goldwasser 等人（STOC 2025）的后门缓解框架只在关于总体数据分布的受限假设下才有可证明的安全性。
- 🔬 **研究方法**：引入容忍属性测试（tolerant property testing）这一新工具，对远比先前工作更广泛的总体分布类实现安全后门缓解，并让模型用户可从很宽的假设类范围中选择缓解模型的假设类。
- 📌 **结论**：所提框架使用户能自然控制缓解模型在准确率与安全性、效率、可解释性之间的权衡，在适用分布范围与可控性上全面扩展了先前理论结果。

👤 **作者**：Xi Chen、Anindya De、Rocco A Servedio

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Goldwasser, Shafer, Vafa and Vaikuntanathan (STOC 2025) recently introduced a formal framework for defending against backdoors that may be planted in large-scale ML models by malicious model developers. They gave several algorithmic results in their framework for efficiently ``mitigating'' the effects of such backdoors by leveraging ideas that were developed in theoretical computer science in the 1980s, namely \emphrandom self-reducibility and \emphself-correction. However, the approaches of Goldwasser, Shafer, Vafa and Vaikuntanathan only provably achieve secure mitigation under restrictive assumptions about the ground-truth population data distribution that the ML model is trained on. In this work we apply tools that have been developed quite recently in the theoretical computer science research area known as \emphtolerant property testing to achieve secure backdoor mitigation for a much broader class of population distributions than could be handled by prior work. Our approach naturally provides a way for an ML model user to select a hypothesis class from a very wide range of possibilities for the mitigated ML model, and naturally enables the ML model user to control a tradeoff of the mitigated model's accuracy against its security, efficiency, and interpretability.

</details>

### 174. When Poison Meets Structure: Topology-based Defense against Poisoning Attack on Graph-based Retrieval-Augmented Generation

📝 [OpenReview](https://openreview.net/forum?id=TirVWlIdjG) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`poisoning`、`graphrag`、`topology ranking`、`retrieval-augmented generation`
- 🎯 **研究动机**：GraphRAG 投毒攻击聚焦节点与社区级知识污染，而常规防御主要依赖句级语义特征，对此类攻击效果不佳。
- 🔬 **研究方法**：从博弈论视角发现攻击者优先伪造查询相关事实而忽视支撑性背景知识，从而在 poisoned 与 clean 子图间诱发系统性拓扑差异；据此提出的 TDP 从检索证据构建一对冲突候选子图，训练 pairwise topology-ranking 判别器区分具密集交叉验证的干净证据与结构支撑稀疏的中毒证据并剔除毒子图，且可预训练后作为即插即用模块迁移。
- 📌 **结论**：首个 GraphRAG 投毒防御的系统工作，在多基准与多种投毒攻击下取得 SOTA 防御性能并展现强泛化。

👤 **作者**：Qizhi Chen、…、Ke Qin

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Poisoning attacks against GraphRAG focus on knowledge pollution at the node and community levels, but conventional poisoning defenses mainly rely on sentence-level semantic features, which makes them less effective against such attacks. To address this issue, we analyze the poisoning strategy from a game-theoretic perspective and find that attackers prioritize fabricating query-related facts while ignoring supporting background knowledge, which in turn induces a systematic topological discrepancy between poisoned and clean subgraphs. Based on this insight, we propose the lightweight oisoning Attack on GraphRAG (TDP). TDP constructs a pair of conflicting candidate subgraphs from the retrieved evidence and trains a pairwise topology-ranking discriminator to distinguish clean evidence with dense cross-validation from poisoned evidence with sparse structural support, thereby removing poisoned subgraphs. Notably, the topological patterns captured by TDP reflect structural preferences induced by the poisoning game rather than dataset-specific distributional biases, allowing it to be transferred as a plug-and-play module after pretraining without end-to-end retraining. To the best of our knowledge, this is the first systematic work on poisoning defense for GraphRAG, and experiments show that TDP achieves state-of-the-art defense performance across multiple benchmarks and poisoning attacks, demonstrating strong generalization.

</details>

### 175. FloatDoor: Platform-triggered Backdoors in LLMs

📄 [arXiv](https://arxiv.org/abs/2606.19535) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`attack`、`backdoor`、`platform-triggered`、`lora`、`supply chain`
- 🎯 **研究动机**：同一模型因非结合浮点运算与内核实现差异在不同部署平台上产生可测输出差异，该平台依赖变异性加上模型审计与部署服务之间的时间差构成未被研究的攻击面。
- 🔬 **研究方法**：提出首个输入无关、平台触发的生成式 LLM 后门 FloatDoor，用两个轻量 LoRA 适配器分别放大跨平台数值分歧、再把所得平台签名绑定到恶意下游任务。
- 📌 **结论**：在 Qwen3-4B 上跨 NVIDIA GPU、Google TPU、AWS Graviton 与倚天 710 等部署目标触发，整体效用基本不变，并能在指定平台可靠诱导可利用代码漏洞。

👤 **作者**：Nils Loose、Jonas Sander、Felix Mächtle、Thomas Eisenbarth

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed in sensitive settings such as software engineering, where their outputs directly shape downstream artifacts. Recent work has shown that an identical model can produce measurably different outputs depending on the deployment platform, a consequence of non-associative floating-point arithmetic and divergent kernel implementations. We study the security implications of this platform-dependent variability and uncover a novel attack surface on LLM deployments. We introduce FloatDoor, the first input-independent, platform-triggered backdoor attack against generative LLMs. The compromised model exhibits adversary-chosen behavior when served on a target platform and is otherwise benign. FloatDoor is realized through two lightweight LoRA adapters, one that amplifies inter-platform numerical divergence and one that binds the resulting platform signature to a malicious downstream task, while leaving aggregate model utility largely intact. FloatDoor exploits a pronounced time-of-check, time-of-use gap between model auditing and serving. We demonstrate FloatDoor on Qwen3-4B across a broad range of deployment targets, including NVIDIA GPUs, Google TPUs, AWS Graviton, and Alibaba Yitian-710. As a final case study, we show that FloatDoor reliably induces exploitable code vulnerabilities on a chosen target platform. Our results establish a new class of attacks on LLM deployments and underscore the pressing need for trusted model supply chains in sensitive, LLM-powered applications.

</details>

### 176. Rethinking Molecular Graph Backdoors under Chemistry-aware Admission

📄 [arXiv](https://arxiv.org/abs/2606.23361) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`attack`、`backdoor`、`molecular graph`、`chemistry-aware admission`、`gnn`
- 🎯 **研究动机**：分子图后门通常以抽象图编辑评估，但真实分子学习管线的记录须先通过解析、消毒、规范化与图串一致性检查才能入训，这一被忽视的 admission 阶段对攻击有效性的影响未知。
- 🔬 **研究方法**：将 admission 形式化为 ChemGuard 操作协议（分子串可消毒且由其重构的图与提交图一致才放行），并提出 admission 感知的 ChemBack 攻击——构造化学可行的 motif-anchor 附着并按对干净目标类分子的 Tanimoto 指纹相似度排序候选，全程无需 victim 模型、代理 GNN、梯度或训练代码访问。
- 📌 **结论**：ChemGuard 使许多现有图后门因化学无效或表征不一致而大幅失效，但 ChemBack 以完全通过 admission 的毒化实现高攻击成功并保持干净精度，说明化学感知 admission 之外仍需进一步防御。

👤 **作者**：Thinh T. H. Nguyen、Sze Jue Yang、Khoa D. Doan、Chee Seng Chan、Kok-Seng Wong

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks on molecular graph neural networks (GNNs) are typically evaluated as abstract graph edits, but real molecular learning pipelines do not train on arbitrary graphs. Molecular records must first survive parsing, sanitization, canonicalization, and graph-string consistency checks. We formalize this overlooked admission stage as ChemGuard, an operational protocol for testing whether a submitted molecular record can enter a realistic learning pipeline, while complementing existing defenses. ChemGuard admits a record only when its molecular string is sanitizable and the graph reconstructed from that string matches the submitted molecular graph. Under this operational view, many existing graph-based backdoors lose much of their apparent efficacy because their poisons are chemically invalid or representation-inconsistent. We then show that admission checks alone are insufficient to rule out molecular backdoors. We propose ChemBack, an admission-aware molecular backdoor attack that constructs chemically feasible motif-anchor attachments and ranks admitted candidates by fingerprint-based Tanimoto similarity to clean target-class molecules. ChemBack is model-free during trigger selection, using molecular structures, target labels, fingerprints, and public validity checks, but no victim model, surrogate GNN, learned embedding, gradient, logit, or training-code access. Across molecular benchmarks, validators, architectures, and defenses, \textbf{ChemBack} achieves high attack success with fully admitted poisons while preserving clean accuracy. Our results reveal a two-sided lesson, chemistry-aware admission suppresses many graph-only backdoors, yet chemically valid and target-aligned molecular backdoors remain a practical threat.

</details>

### 177. The Platonic Defense: Backdoor Defense for Self-Supervised Encoders in the Era of Large Scale Pre-training

📄 [arXiv](https://arxiv.org/abs/2606.29451) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`defense`、`backdoor`、`self-supervised learning`、`energy model`、`test-time purification`
- 🎯 **研究动机**：SSL 预训练编码器易受后门攻击，现有防御在完全黑盒设定下往往需要标签、攻击模式或训练数据访问而难以奏效。
- 🔬 **研究方法**：受 Platonic Representation Hypothesis 启发提出 Platonic Representation Defense，在源表征与参考表征上定义条件能量函数，用噪声对比估计做检测、去噪分数匹配做表征净化。
- 📌 **结论**：该攻击/模型/模态无关的黑盒测试时防御在多个 SSL 编码器和 10 余种攻击上同时完成表征检测与净化，取得显著性能提升。

👤 **作者**：Tuo Chen、Minjing Dong、Benlei Cui、Jian Liu、Jie Gui

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-supervised learning (SSL) pretrained models have become a dominant paradigm for visual representation learning, but they are vulnerable to backdoor attacks. Existing defenses struggle to defend against such attacks in a fully black-box setting because they often require access to labels, attack patterns, or training data. To tackle this issue, we propose a new attack-agnostic, model-agnostic, and modality-agnostic black-box test-time defense paradigm, called \emph{Platonic Representation Defense}. It is inspired by the Platonic Representation Hypothesis, which suggests that large-scale independently trained encoders converge toward compatible projections of the same underlying reality. We formalize this idea as a conditional energy function defined over source representations and a set of reference representations. The energy function is trained for detection through noise-contrastive estimation and for representation purification through denoising score matching. Theoretically, the energy gap between matched and mismatched samples is lower bounded by the mutual information between source and reference representations. We demonstrate the effectiveness of our method on multiple self-supervised encoders and more than 10 attacks. The method can perform both representation detection and purification, and achieves substantial performance gains across multiple attacks. Code is available \href{https://github.com/jsrdcht/Platonic-Representation-Defense}{here}.

</details>

### 178. Stealthy World Model Manipulation via Data Poisoning

📄 [arXiv](https://arxiv.org/abs/2606.18697) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`attack`、`data poisoning`、`world model`、`model-based rl`、`bilevel optimization`
- 🎯 **研究动机**：基于模型的智能体从收集经验更新世界模型形成训练时攻击面——投毒的微调轨迹可操纵学到的动力学进而破坏下游规划，但此前没有针对学习式世界模型的投毒框架。
- 🔬 **研究方法**：提出两阶段框架 SWAAP：第一阶段以转移梯度定理支持的一阶双层优化寻找贴近干净动力学却诱导低回报行为的有害目标世界模型；第二阶段以隐身约束梯度匹配只修改有限比例的微调转移目标，配合预测误差正则使投毒目标贴近世界模型自然近似误差。
- 📌 **结论**：在多种连续控制任务上造成显著性能退化，投毒转移贴近干净数据，并躲避投毒前检测、鲁棒微调与测试时监控等非自适应 residual/CUSUM/TRIM 类防御。

👤 **作者**：Yibin Hu、Xiaolin Sun、Zizhan Zheng

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model-based learning agents use learned world models to predict future states, plan actions, and adapt to new environments. However, the process of updating world models from collected experience creates a training-time attack surface: adversarially poisoned fine-tuning trajectories can manipulate the learned dynamics and thereby corrupt downstream planning. In this paper, we propose SWAAP, the first two-stage data poisoning framework for learned world models. In the first stage, SWAAP identifies a harmful target world model that induces low-return behavior under planning while remaining close to clean dynamics, using first-order bilevel optimization enabled by a transition-gradient theorem. In the second stage, SWAAP realizes this target through stealth-constrained gradient matching, modifying only a limited fraction of fine-tuning transition targets so that the induced training gradients steer the victim model toward the adversarial target, while a prediction-error regularizer encourages the poisoned targets to remain close to the world model's natural approximation error. To assess attack stealthiness, we evaluate defenses and detectability across three stages of the poisoning pipeline: pre-training detection of poisoned transitions, robust training during fine-tuning, and test-time monitoring of the resulting world model. Across diverse continuous-control tasks, SWAAP causes substantial performance degradation while keeping poisoned transitions close to clean data and evading the evaluated non-adaptive residual/CUSUM/TRIM-style defenses. These results reveal a practical vulnerability in world-model adaptation pipelines and highlight the need for robustness methods that protect both world-model training data and learned dynamics.

</details>

### 179. Token by Token, Compromised: Backdoor Vulnerabilities in Unified Autoregressive Models

📄 [arXiv](https://arxiv.org/abs/2605.19227) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`attack`、`backdoor`、`unified autoregressive model`、`multimodal generation`、`poisoning`
- 🎯 **研究动机**：统一自回归模型（UAM）以共享参数与多模态词表在单次自回归中生成文本与图像 token，其统一架构是否引入多模态后门这类新脆弱性尚属空白。
- 🔬 **研究方法**：提出首个针对 UAM 的后门攻击 ToBAC，覆盖数据投毒与模型修改两种策略，将无害字符乃至常见词转化为可跨多个输出模态传播恶意效果的触发器。
- 📌 **结论**：有模型访问时在 Liquid 上一个常见词（如 cool）即可在 55% 的生成中诱导模态对齐的品牌推广或意识形态影响，无模型访问时数据投毒对 JanusPro 平均成功率 63.1%。

👤 **作者**：Tobias Braun、Jonas Henry Grebe、Hossein Shakibania、Anna Rohrbach、Marcus Rohrbach

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unified autoregressive models (UAMs) are transformer models that generate text as well as image tokens within a single autoregressive pass. Shared parameters and a multimodal vocabulary simplify the training pipeline and facilitate flexible multimodal generation, yet might introduce new vulnerabilities. In particular, we are the first to show that this unified architecture enables multimodal backdoor attacks, where a trigger can propagate malicious effects across multiple output modalities. Specifically, we present the Token by Token Backdoor Attack (ToBAC), the first backdoor attack targeting UAMs, exploring both data-based and model-based poisoning strategies. We demonstrate that innocuous characters or even common words can be transformed into triggers that elicit harmful behavior in autoregressive image generation. ToBAC can jointly manipulate visual outputs and accompanying text, increasing the perceived authenticity of fabricated content. With model access, ToBAC enables attacks on the unified Liquid model in which a subtle word (e.g., ``cool'') induces modality-aligned brand promotion or ideological influence in 55% of generations. Without model access, ToBAC can be induced through data poisoning, achieving an average success rate of 63.1% against JanusPro.

</details>

### 180. Backdoor Channels Hidden in Latent Space: Extending Cryptographic Undetectability to Modern Neural Networks

📄 [arXiv](https://arxiv.org/abs/2605.13214) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`attack`、`backdoor`、`cryptographic undetectability`、`latent space`、`post-training defense`
- 🎯 **研究动机**：密码学结果表明神经网络可被后门化到无高效算法能将其与干净模型区分，但该保证局限于实际相关性有限的程式化架构，现代端到端训练网络是否具有可比的不可检测性尚属开放问题。
- 🔬 **研究方法**：将后门信道实现为学到的潜在方向，把不可检测性归约为两个未知参数分布间的假设检验（推测实践中不可解），使攻击者无需引入外来结构而直接利用网络自身几何，并在 ResNet 与 Vision Transformer 的标准图像分类训练中演示。
- 📌 **结论**：攻击保持持续高成功率且干净精度几乎无损，抵御一整套训练后防御——没有任何防御能在不使模型不可用的前提下中和后门，表明密码学后门可内生于学习表示的几何。

👤 **作者**：Marte Eggen、Eirik Reiestad、Kristian Gjøsteen、Inga Strümke

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent cryptographic results establish that neural networks can be backdoored such that no efficient algorithm can distinguish them from a clean model. These guarantees, however, have been confined to stylised architectures of limited practical relevance, leaving open whether comparable undetectability extends to modern, end-to-end trained networks. We construct such an attack mechanism for state-of-the-art architectures, closely aligned to the cryptographic notion of undetectability, by identifying backdoor channels as learned latent directions, and show that the question of undetectability reduces to a hypothesis test between two unknown distributions over model parameters, which we conjecture to be intractable in practice. The consequence of this reframing is significant: if exploitable channels within a network's latent space are statistically indistinguishable from naturally learned directions, an attacker need not introduce foreign structure but can instead exploit the geometry the network already possesses. Demonstrating the approach on ResNet and Vision Transformer architectures trained on standard image classification datasets, the attack achieves both consistently high success rates with negligible clean accuracy degradation, and resists a comprehensive suite of post-training defences, none of which neutralise the backdoor without rendering the model unusable. Our results establish that cryptographic backdoors need not be artefacts requiring exotic architectures or artificial constructions, but identifiable as latent properties inherent to the geometry of learned representations.

</details>

### 181. Your Neighbors Know: Leveraging Local Neighborhoods for Backdoor Detection in Decentralized Learning

📄 [arXiv](https://arxiv.org/abs/2605.19969) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`detection`、`backdoor`、`decentralized learning`、`collaborative defense`、`convergence guarantee`
- 🎯 **研究动机**：去中心化学习（DL）的协作本质使其易受后门攻击且防御研究不足，已有方案常忽视 DL 的约束（无中心服务器、无触发器先验）。
- 🔬 **研究方法**：提出原生适配 DL 的 Argus：诚实节点本地分析收到的模型更新以识别潜在触发器，与邻居共享触发器并用结构相似度区分真后门（跨参与者模式一致）与数据异质性导致的误报，未通过协作检测的更新被拒绝、持续恶意发送者最终被逐出。
- 📌 **结论**：给出首个 DL 特定后门检测机制的理论收敛保证；在三个数据集上攻击成功率相比无防御最高降低 90 个百分点，模型效用保持在全知 oracle 的 5 个百分点内，且数据异质性越强相对基线优势越大。

👤 **作者**：Sayan Biswas、…、Martijn de Vos

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Decentralized learning (DL) is an emerging machine learning paradigm where nodes collaboratively train models without a central server. However, the collaborative nature of DL makes it vulnerable to backdoor attacks, where a model is taught to behave normally on standard inputs while executing hidden, malicious actions when encountering data with specific triggers. Backdoor attacks in DL remain understudied and existing defenses often overlook DL constraints. We introduce Argus, a novel backdoor detection framework native to DL that requires neither a central coordinator nor prior knowledge of the trigger. In Argus, honest nodes locally analyze received model updates to identify potential backdoor triggers. Nodes then collectively share their triggers with their neighbors and use a structural similarity metric to separate true backdoors from false alarms induced by data heterogeneity. A key insight is that false positive triggers exhibit inconsistencies across participants while true positive ones show consistent patterns. Model updates that fail this collaborative test are rejected, and persistently malicious senders are eventually evicted. We provide the first theoretical convergence guarantees for a DL-specific backdoor detection mechanism, showing that filtering out suspicious model updates with high probability preserves a convergence rate comparable to standard DL. We implement and evaluate Argus on three standard datasets and against three state-of-the-art baselines. Across settings, Argus reduces attack success rates by up to 90 points compared to no defense, while preserving model utility within 5 percentage points of an omniscient oracle. Furthermore, the effectiveness of Argus compared to baselines improves as data heterogeneity increases.

</details>

### 182. Provable Robustness against Backdoor Attacks via the Primal-Dual Perspective on Differential Privacy

📄 [arXiv](https://arxiv.org/abs/2605.21780) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`backdoor`、`randomized smoothing`、`differential privacy`、`certified robustness`
- 🎯 **研究动机**：后门攻击同时扰动训练与测试数据，训练时与测试时的随机化机制难以纳入单一鲁棒性证书，扩展认证到该场景是难题。
- 🔬 **研究方法**：通过 privacy profiles 把 randomized smoothing 与差分隐私的对偶视角相连，获得异构机制组合的数值程序，实现紧致、模块化、端到端的复合机制认证，并在 DP-SGD 与 Deep Partition Aggregation（配推理时平滑）上实例化对训练时与推理时攻击的联合鲁棒性保证。
- 📌 **结论**：在 MNIST 与 CIFAR-10 上验证有效，提供了用复合机制认证更贴近真实对手能力的复杂威胁模型下鲁棒性的一般性框架。

👤 **作者**：Aman Saxena、Jan Schuchardt、Yan Scholten、Stephan Günnemann

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Randomized smoothing is a powerful tool for certifying robustness to adversarial perturbations, including poisoning attacks via randomized training and evasion attacks via randomized inference. Extending these guarantees to backdoor attacks, where training and test data are jointly perturbed, remains challenging because training- and test-time randomized mechanisms must be analyzed within a single robustness certificate. We address this by connecting randomized smoothing to the dual view of differential privacy through privacy profiles, which provide a numerical procedure for composing heterogeneous mechanisms. The resulting framework enables tight, modular, end-to-end certification of complex, composed mechanisms while leveraging existing analyses of differentially private mechanisms. We instantiate the framework for DP-SGD and Deep Partition Aggregation with inference-time smoothing, deriving joint robustness guarantees against both training-time and inference-time attacks. Experiments on MNIST and CIFAR-10 demonstrate the effectiveness of our framework. Overall, we provide a principled and general framework for using composite mechanisms to certify robustness under complex threat models that better capture the capabilities of real-world adversaries.

</details>

### 183. Combating Data Laundering in LLM Training

📄 [arXiv](https://arxiv.org/abs/2604.01904) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-04　🏷 NeurIPS 2026

**关键词**：`detection`、`data laundering`、`unauthorized training`、`memorization signal`、`auditing`
- 🎯 **研究动机**：未授权训练数据检测假设以原始专有数据查询目标 LLM，但在数据洗钱（语义保持的风格/结构变换）下训练暴露发生在变换形态上，记忆信号不再出现在原文，标准检测器依赖的信号分离崩塌。
- 🔬 **研究方法**：提出 Synthesis Data Reversion（SDR），借助辅助 LLM 以"变换目标+细粒度细节"抽象约束无限的自然语言变换空间，迭代细化细节以合成出能激发更强目标模型检测信号的类训练查询。
- 📌 **结论**：在 MIMIR 基准上针对多样洗钱手段与 Pythia、Llama2、Falcon 三个模型族一致恢复检测信号，提供实用的数据洗钱审计层。

👤 **作者**：Muxing Li、Zesheng Ye、Sharon Li、Feng Liu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Post-hoc unauthorized-training data detection for large language models (LLMs) typically assumes a query-with-originals regime: rights holders query a target LLM with raw proprietary data and assess whether the model assigns them stronger memorization-based detection signals, e.g., higher confidence or lower loss, than held-out non-training reference texts. We show that this regime becomes brittle under data laundering, where the target LLM is trained on semantics-preserving but stylistically or structurally transformed surrogates of proprietary data to obfuscate provenance. Since training-time exposure occurs in the laundered form, memorization signals may no longer appear on the originals, collapsing the candidate-reference signal separation that standard detectors rely on. We counter this threat by studying laundering-aware detection with raw proprietary data, a held-out reference corpus, and query access to the target LLM, while the laundering transformation is undisclosed. Since exact recovery of the laundered corpus is infeasible, we infer a detection-useful synthesis process via an auxiliary LLM that maps originals into training-like queries. To make this search tractable, we introduce Synthesis Data Reversion (SDR), which constrains the unbounded space of natural-language transformations through a goal-details abstraction: a high-level transformation goal, e.g., "lyrical rewriting", and fine-grained details, e.g., "with vivid imagery". SDR identifies the most likely goal and iteratively refines details so synthesized queries elicit stronger target-model detection signals. Evaluated on the MIMIR benchmark against diverse laundering practices and target LLM families (Pythia, Llama2, and Falcon), SDR consistently restores detection signals, offering a practical auditing layer against data laundering.

</details>

### 184. Hallucinated Positive Entanglement for Backdoor Attacks in Federated Self-Supervised Learning

📄 [arXiv](https://arxiv.org/abs/2602.02147) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`attack`、`backdoor`、`federated self-supervised learning`、`hallucinated positive entanglement`、`feature entanglement`
- 🎯 **研究动机**：FSSL 在不共享原始无标注数据协同训练表示模型的同时易受后门攻击，而现有 FSSL 后门攻击存在中毒样本利用率低、迁移性有限与持久性弱的局限。
- 🔬 **研究方法**：提出 HPE——先用幻觉合成正样本增强编码器对后门特征的嵌入，再以特征纠缠让触发器与后门样本在表示空间紧密绑定，最后借选择性参数投毒与邻近感知更新把中毒模型约束在全局模型附近以提升稳定性与持久性。
- 📌 **结论**：在多个 FSSL 场景与数据集上，HPE 的性能显著超越已有后门攻击方法，并在多种防御机制下保持强鲁棒性。

👤 **作者**：Jiayao Wang、…、Dongfang Zhao

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Federated self-supervised learning (FSSL) enables collaborative training of self-supervised representation models without sharing raw unlabeled data. While it serves as a crucial paradigm for privacy-preserving learning, its security remains vulnerable to backdoor attacks, where malicious clients manipulate local training to inject targeted backdoors. Existing FSSL attack methods, however, often suffer from low utilization of poisoned samples, limited transferability, and weak persistence. To address these limitations, we propose a new backdoor attack method for FSSL, namely Hallucinated Positive Entanglement (HPE). HPE first employs hallucination-based augmentation using synthetic positive samples to enhance the encoder's embedding of backdoor features. It then introduces feature entanglement to enforce tight binding between triggers and backdoor samples in the representation space. Finally, selective parameter poisoning and proximity-aware updates constrain the poisoned model within the vicinity of the global model, enhancing its stability and persistence. Experimental results on several FSSL scenarios and datasets show that HPE significantly outperforms existing backdoor attack methods in performance and exhibits strong robustness under various defense mechanisms.

</details>

### 185. Phantom Transfer: Data Poisoning can Survive Data-Level Defences

📄 [arXiv](https://arxiv.org/abs/2602.04899) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`attack`、`data poisoning`、`subliminal learning`、`data-level defense`、`existence proof`
- 🎯 **研究动机**：提出一个根本性问题——即便精确知道毒化样本如何被植入良性数据集，数据级防御也可能无法将其滤除，需要检验最大权限防御对复杂投毒的失效可能。
- 🔬 **研究方法**：把 subliminal learning 改造到真实场景构造 Phantom Transfer 投毒，使攻击不依赖产出数据的模型、在其上训练的模型与攻击目标，并刻画攻击最有效的条件、演示植入密码触发行为。
- 📌 **结论**：攻击在全部 11 种被测数据级防御（含逐样本被另一模型改写的防御）下存活，构成"最大权限数据级防御可失效"的存在性证明。

👤 **作者**：Andrew Draganov、Tolga H. Dur、Anandmayi Bhongade、Mary Phuong

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present a data poisoning attack -- Phantom Transfer -- with the property that, even if you know precisely how the poison was placed into an otherwise benign dataset, you cannot filter it out. We achieve this by modifying subliminal learning to work in real-world contexts and demonstrate that the attack works regardless of which model produced the data, which model is trained on the data or what the attack target is. Furthermore, the attack survives 11 tested data-level defences, including one where every sample is paraphrased by another model. We characterise when this attack works best and show that it can be used to plant password-triggered behaviours into models while still beating defences. In short, we provide an existence proof that maximum-affordance defences can fail to stop sophisticated data poisoning attacks. We suggest that future defences should be supplemented with white-box methods and post-training model audits.

</details>

### 186. Half-Truths Break Similarity-Based Retrieval

📄 [arXiv](https://arxiv.org/abs/2602.23906) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`analysis`、`dual encoder`、`half-truth`、`compositional reasoning`
- 🎯 **研究动机**：CLIP 式双编码器常违反直觉——在正确描述上追加貌似合理但错误的对象或关系反而提高图文相似度（half-truths），威胁基于相似度的检索
- 🔬 **研究方法**：将漏洞归因于对比训练只对齐整句 caption 而未显式接地个体实体与关系，提出 CS-CLIP——把 caption 分解为实体/关系单元、为每单元构造最小编辑 foil，微调模型使正确单元得分高于 foil 且保留标准双编码器推理
- 📌 **结论**：COCO 上 CLIP 仅 40.6% 的时间偏好正确短描述（细节为关系时降至 32.9%），CS-CLIP 将 half-truth 准确率提升至 69.3%，并在既有组合性基准上平均提升 5.7 点

👤 **作者**：Bora Kargi、Arnas Uselis、Seong Joon Oh

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When a text description is extended with an additional detail, image-text similarity should drop if that detail is wrong. We show that CLIP-style dual encoders often violate this intuition: appending a plausible but incorrect object or relation to an otherwise correct description can increase the similarity score. We call such cases half-truths. On COCO, CLIP prefers the correct shorter description only 40.6% of the time, and performance drops to 32.9% when the added detail is a relation. We trace this vulnerability to weak supervision on caption parts: contrastive training aligns full sentences but does not explicitly enforce that individual entities and relations are grounded. We propose CS-CLIP (Component-Supervised CLIP), which decomposes captions into entity and relation units, constructs a minimally edited foil for each unit, and fine-tunes the model to score the correct unit above its foil while preserving standard dual-encoder inference. CS-CLIP raises half-truth accuracy to 69.3% and improves average performance on established compositional benchmarks by 5.7 points, suggesting that reducing half-truth errors aligns with broader gains in compositional understanding. Code is publicly available at: https://github.com/kargibora/CS-CLIP

</details>

### 187. Catch-Only-One: Non-Transferable Examples for Model-Specific Authorization

📄 [arXiv](https://arxiv.org/abs/2510.10982) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-10　🏷 NeurIPS 2026

**关键词**：`defense`、`non-transferable examples`、`model-specific authorization`、`low-sensitivity subspace`、`training-free`
- 🎯 **研究动机**：AI 法规日益强调目的限制，但已发布数据可被喂给任意模型，现有数据扰动或重训练方法既防不住未知或外部训练的模型、又依赖对训练部署的控制。
- 🔬 **研究方法**：提出 non-transferable examples（NTE），以 training-free、data-agnostic 方式在模型特定低敏感子空间内重编码数据，形成仅指定模型可解码的任务级"密文"，并建立授权保真与未授权退化的形式化界。
- 📌 **结论**：授权的视觉与视觉语言模型在常见预处理下性能保持，未授权模型因子空间错位而崩溃（即使面对自适应重构攻击），未授权退化随可测谱错位度扩展。

👤 **作者**：Zihan Wang、…、Guangdong Bai

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent AI regulations increasingly emphasize the need for mechanisms that preserve the utility of data for AI innovation while preventing misuse, particularly by enforcing purpose limitation in downstream AI applications. In practice, enforcing this principle remains challenging, as released data can be trivially fed into arbitrary models beyond its declared intent. Existing approaches attempt to mitigate this risk by either perturbing data or retraining models to limit unintended use. These strategies, however, offer no protection against inference by unknown or externally trained models, or fundamentally rely on control over the training or deployment. In this work, we introduce non-transferable examples (NTEs), recoded data that act as a task-level "ciphertext" decodable only by a designated model. Whereas adversarial examples exploit directions of high model sensitivity, NTEs leverage the complementary insensitive subspace. We propose a training-free, data-agnostic method that recodes data within a model-specific low-sensitivity subspace, preserving outputs for the authorized model while degrading unauthorized ones through subspace misalignment. We establish formal bounds certifying authorized-model fidelity and showing that unauthorized degradation scales with measurable spectral misalignment between models. Empirically, NTEs preserve performance across diverse vision backbones and state-of-the-art vision-language models under common preprocessing, while unauthorized models collapse even under adaptive reconstruction attacks. These results establish NTEs as a practical means to preserve intended data utility while preventing unauthorized exploitation. Our project is available at https://trusted-system-lab.github.io/model-specificity

</details>

**尚未挂出 arXiv（待核验）**
- Backdoor Channels Hidden in Latent Space: Cryptographic Undetectability in Modern Neural Networks
- CSO-LLM: Post-Training Backdoor Detection and Trigger Inversion in LLMs
- Trapping Attacker in Dilemma: Defending GNN Backdoors
- Information Blackhole: Backdoor Mechanism in 3D Point Cloud Reconstruction（已库内，0929）

### 隐私、成员推断与 unlearning

### 188. Exposing Private Corpus Leakage in Multimodal RAG

📝 [OpenReview](https://openreview.net/forum?id=A69wmC5lPE) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`privacy leakage`、`multimodal rag`、`retrieval perturbation`、`vlm`
- 🎯 **研究动机**：多模态 RAG 的外部化记忆引入检索语料隐私风险——医疗影像、扫描合同等敏感视觉记录可能通过系统交互被探测。
- 🔬 **研究方法**：提出两查询的 Semantic Degradation Attack（SDA），用本地代理视觉编码器构造可迁移的检索扰动，通过测量扰动前后 VLM 生成描述语义相似度的下降程度，判断目标图文记录是否存在于私有检索语料。
- 📌 **结论**：在两个图文数据集、五个主流 VLM 上，SDA 检测私有语料泄露的一致性与有效性均超过现有基线。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Retrieval-Augmented Generation (RAG) helps mitigate hallucinations in Vision-Language Models (VLMs) by grounding generations in external knowledge bases. However, this externalized memory also introduces privacy risks, as external queries may reveal signals about sensitive visual records in the retrieval corpus, such as medical images, scanned contracts, and proprietary business documents. This exposes a retrieval-corpus privacy risk: private records may be detectable through interactions with multimodal RAG systems. To study this risk, we propose the Semantic Degradation Attack (SDA), a two-query method for exposing private corpus leakage in multimodal RAG by testing how strongly generated responses depend on retrieved evidence. SDA constructs transferable retrieval-disrupting perturbations using local surrogate visual encoders. By measuring the drop in the semantic similarity of the VLM's generated descriptions before and after perturbation, SDA can distinguish whether a target image-caption record exists in the private retrieval corpus. Extensive experiments demonstrate that SDA consistently detects private corpus leakage more effectively than existing baselines on two image-caption datasets across five popular VLMs.

</details>

### 189. Guarding the Life Code: Preserving Membership Privacy in Genomic Foundation Models

📝 [OpenReview](https://openreview.net/forum?id=96HcSezVOS) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`membership inference`、`genomic foundation model`、`token attribution`、`adaptive mitigation`
- 🎯 **研究动机**：基因组基础模型在人群数据上训练会无意记忆敏感基因组签名而遭成员推断攻击，而全局式防御严重损害 motif 敏感效用、模型无关后处理又无法定位泄露来源。
- 🔬 **研究方法**：系统隐私审计发现泄露高度非均匀、集中于少量高危样本与对应生物学意义的稀疏 token 区间，据此提出模型与样本自适应的 GenoGuard：梯度 token 归因定位泄露子序列并做选择性梯度路由，风险自适应标签平滑（参考校准损失差分数引导）做样本级降压，同时输出区域级归因图支持审计。
- 📌 **结论**：在 Mistral-DNA、Nucleotide Transformer 等代表性 GFM 上，对多个 MIA 家族一致提升隐私，同时保持强微调性能与可解释性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Genomic Foundation Models (GFMs) have become a promising paradigm for decoding DNA sequences, yet their privacy risks are critically underexplored.Trained on human cohorts, GFMs can unintentionally memorize sensitive genomic signatures, that enable membership inference attacks (MIAs) and expose individuals to long-lasting privacy harms.However, existing defenses often fall short in genomics: globally applied mechanisms can substantially degrade motif-sensitive utility, and model-agnostic post-processing provides limited insight into which genomic regions drive leakage. Through a systematic privacy audit, we find that membership leakage in GFMs is highly non-uniform, concentrating on a small subset of high-risk samples and sparse token spans corresponding to biologically meaningful patterns. Motivated by this finding, we propose GenoGuard, a model- and sample-adaptive defense that shifts from blanket protection to targeted, region-aware mitigation. GenoGuard (i) localizes privacy-leaking subsequences via gradient-based token attribution and performs token-level risk reduction through selective gradient routing, (ii) applies sample-level risk reduction with risk-adaptive label smoothing guided by a reference-calibrated loss gap score, and (iii) provides region-level attribution maps for privacy auditing and biological interpretation. Experiments across representative GFMs (Mistral-DNA, Nucleotide Transformer) demonstrate that GenoGuard consistently improves privacy against multiple MIA families while preserving strong fine-tuning performance and interpretability.

</details>

### 190. Bayesian Low-Rank Posteriors for Scalable Membership Inference

📝 [OpenReview](https://openreview.net/forum?id=7y5OCsNjHI) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`membership inference`、`lora`、`bayesian posterior`、`vlm`
- 🎯 **研究动机**：最有效的成员推断攻击依赖参考（影子）模型集成估计目标条件分数分布，但对现代大规模视觉语言模型而言训练这种集成计算上不可行。
- 🔬 **研究方法**：提出可扩展替代方案——用低秩适应参数上的贝叶斯近似取代显式参考模型训练，仅在 LoRA 子空间建模不确定性、从单次训练构造后验并采样多样化虚拟参考模型，以 SWAG 实例化高效逼近目标条件分数分布。
- 📌 **结论**：在三个下游适配 VLM 的 Document VQA 与医疗 VQA 两个隐私敏感任务（另加受控合成数据集）上超越标准参考式攻击，且仅需单个训练好的参考模型。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership inference attacks (MIAs) aim to determine whether a sample was used during the training of a target model. The most effective MIAs rely on reference (or shadow) models to estimate target-conditional score distributions, but training such ensembles is computationally prohibitive for modern large-scale Vision--Language Models (VLMs). In this work, we propose a scalable alternative that replaces explicit reference-model training with a Bayesian approximation over low-rank adaptation parameters. Leveraging parameter-efficient fine-tuning, we model uncertainty only within the LoRA subspace and construct a posterior from a single training run, from which we sample a diverse set of virtual reference models. We instantiate this approach using stochastic weight averaging Gaussian (SWAG), enabling efficient approximation of target-conditional score distributions at a fraction of the cost of conventional shadow-model ensembles. We evaluate the resulting attack on three downstream-adapted VLMs across two privacy-sensitive visual question answering tasks, namely Document VQA and medical VQA. To isolate the effect of pretraining knowledge, we additionally introduce a controlled synthetic dataset. Our approach outperforms standard reference-based attacks while requiring only a single trained reference model, demonstrating that accurate and scalable membership inference is feasible even for large VLMs.

</details>

### 191. What Should Remain After Forgetting? Rethinking LLM Unlearning as Predictive Posterior Correction

📝 [OpenReview](https://openreview.net/forum?id=CBwCf8daZF) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`llm unlearning`、`posterior correction`、`evidence attribution`、`logit space`
- 🎯 **研究动机**：LLM unlearning 通常为遗忘相关提示指派拒绝、均匀化、似然压制等替代目标，这与"恢复仅保留数据的预测后验"这一反事实目标错位，在回应部分依赖保留证据的混合证据情形尤其有害。
- 🔬 **研究方法**：提出 logit 空间后验修正方法 EASE（Evidence Attribution and Subtraction Estimator），用轻量删除与补偿助手估计部署模型预测支持中由遗忘证据诱发的成分并在推理时减去，同时形式化抑制范围两难并给出后验修正何时能恢复 retain-only 后验的理论保证。
- 📌 **结论**：在 TOFU 与 MUSE 上改善遗忘-保留权衡，6 个主要 TOFU 设置中 5 个取得最佳综合分，混合查询语义泄露降低 22.2%，并以少 9 倍的保留样本匹配或超过全量保留基线。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM unlearning is often implemented by assigning surrogate targets, such as refusal, uniformity, or likelihood suppression, to forget-related prompts. We argue that this surrogate assignment view is misaligned with the counterfactual goal of unlearning: recovering the retain-only predictive posterior. This mismatch is especially problematic in mixed-evidence regimes, where a response may be associated with forgotten evidence while still being partially supported by retained evidence. We propose EASE: Evidence Attribution and Subtraction Estimator, a logit-space posterior-correction method that estimates the forget-induced component of the deployed model's predictive support and subtracts it at inference time. EASE uses lightweight deletion and compensation assistants to remove forget-neighbour evidence while restoring nearby retain-supported evidence. We formalize the suppression-scope dilemma and provide guarantees showing when posterior correction recovers the retain-only posterior. Experiments on TOFU and MUSE show that EASE improves forgetting--retention trade-offs over strong baselines, achieving the best aggregate score in 5/6 main TOFU settings, reducing mixed-query semantic leakage by 22.2%, and matching or exceeding full-retain baselines with 9 times fewer retain examples. Our code is available at: https://anonymous.4open.science/r/EASE-9675.

</details>

### 192. TRACE: Data-Free Text Reconstruction Attacks against Approximate Unlearning in LLMs

📝 [OpenReview](https://openreview.net/forum?id=dKuZvfswsY) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`unlearning`、`data reconstruction`、`model snapshot`、`perplexity gap`
- 🎯 **研究动机**：实践中 unlearning 前后的模型快照常被保留用于审计与回滚，这一被忽视的侧信道可能使近似 unlearning 的残余痕迹被恢复，引发其本要防止的隐私泄露。
- 🔬 **研究方法**：提出 TRACE，仅凭前后 unlearning 快照、无任何数据先验地重构遗忘的训练数据——从嵌入级参数差异锁定紧凑候选 token 集压缩搜索空间，基于两模型间困惑度差的对比打分拼装序列，两阶段"探索-补全"策略恢复多个不同样本。
- 📌 **结论**：在 TOFU、MUSE、WMDP 等数据集、多个 LLM 与六种代表性 unlearning 方法上实现高保度重构，揭示参数差泄露的重大隐私风险并呼吁管理快照访问。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) face growing demands for data removal driven by regulatory compliance, copyright concerns, and privacy protection, approximate unlearning has emerged as a practical alternative to expensive full retraining. In practice, pre- and post-unlearning model snapshots are often maintained for auditing and rollback, introducing a previously overlooked side channel. This paper demonstrates that approximate unlearning in LLM can leave residual traces within model snapshots, which may be recoverable and thus enable the privacy breaches that approximate unlearning is intended to prevent. Here, we propose TRACE, a framework that reconstructs unlearned training data given access to pre- and post-unlearning model snapshots, without any data-specific prior knowledge. To achieve this, TRACE identifies a compact set of candidate tokens from embedding-level parameter differences to constrain the search space, and assembles sequences via a contrastive scoring mechanism based on the perplexity gap between the two models. A two-stage exploration-then-completion strategy enables the recovery of multiple distinct samples. Extensive experiments on various datasets, including TOFU, MUSE, and WMDP, across multiple LLMs and six representative unlearning methods, demonstrate that TRACE achieves high-fidelity reconstruction. This paper exposes significant privacy risks in current LLM approximate unlearning deployments and highlights the need for defenses against parameter-difference leakage and appropriate management of model snapshot access.

</details>

### 193. What Do SAE Features Encode? Evidence from Human Neural Activity（机制方法，交叉参考）

📝 [OpenReview](https://openreview.net/forum?id=bpwbTRy94A) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`analysis`、`sparse autoencoder`、`interpretability`、`eeg`、`brain alignment`
- 🎯 **研究动机**：SAE 把 LLM 稠密激活分解为稀疏可解释特征，但现有评估依赖重构保真与 LLM 自动打分等模型内部指标，无法外部验证特征是否对应模型之外的实在结构。
- 🔬 **研究方法**：利用 SAE 与生物神经系统共享稀疏编码原理，将三个 LLM 的 SAE 特征与自然阅读 EEG 记录对齐比较，并进一步区分学得稀疏码与通用架构性质、训练数据规模各自承载的贡献。
- 📌 **结论**：SAE 特征系统性对齐人脑活动且该对齐主要由学得的稀疏码承载，首次以生物对齐为机制可解释性研究建立模型内部指标之外的互补基准。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Sparse Autoencoders (SAEs) decompose dense LLM activations into sparse, interpretable features. However, evaluating whether SAEs extract genuinely meaningful structure remains challenging. Current approaches rely on model-internal metrics such as reconstruction fidelity and automated LLM scoring, which assess SAEs as mathematical decompositions but provide no external validation that the extracted features correspond to anything outside the model. To address this issue, we propose a new validation approach: comparing SAE representations against human neural activity. The validation rests on a shared computational principle, since both SAEs and biological neural systems implement sparse coding over overcomplete populations. Through extensive experiments using EEG recordings of naturalistic reading and SAE features from three large language models, we demonstrate that SAE features systematically align with human brain activity. We further show that this alignment is dominantly carried by the SAE's learned sparse code, rather than by generic architectural properties or the scale of the training data. This work is the first attempt to validate pretrained SAE features against human brain activity, establishing biological alignment as a complementary benchmark for mechanistic interpretability research beyond model-internal metrics.

</details>

### 194. Membership Inference on Synthetic Single-Cell Genomic Data

📝 [OpenReview](https://openreview.net/forum?id=RzrYEYn0Uz) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`membership inference`、`synthetic data`、`single-cell genomics`、`privacy`
- 🎯 **研究动机**：scRNA-seq 数据因敏感而受严格访问控制，催生合成数据生成（SDG）用于隐私保护共享，但 SOTA SDG 方法未能充分掩盖哪些个体参与了生成器训练这一点未被对抗性检验。
- 🔬 **研究方法**：提出首个显著高于随机猜测的供体级成员推断攻击，针对 scDesign2 漏洞设计且可迁移到 scDesign3、scVI 等其他方法的合成数据——无需访问训练流程、模型参数乃至底层生成算法，并评估 SDG 过程中加噪作为第一道防御的有效性与效用代价。
- 📌 **结论**：攻击显示领先 SDG 技术无法充分掩盖训练个体，且隐私泄露随训练供体数量减少而增大。

👤 **作者**：Steven Golob、Patrick McKeever、Sikha Pentyala、Martine De Cock、Jonathan Peck

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Single‑cell RNA sequencing (scRNA‑seq) data is subject to strict access control due to its sensitive nature, motivating the use of synthetic data generation (SDG) for privacy‑preserving data sharing. We present the first adversarial privacy attack that performs meaningfully above random guessing against state‑of‑the‑art scRNA‑seq SDG methods. Our attack enables donor‑level membership inference, demonstrating that leading SDG techniques fail to adequately mask which individuals were used to train the generator. We show that privacy leakage increases as the number of training donors decreases. Although the attack is designed to exploit vulnerabilities in scDesign2, we find that it also succeeds against synthetic data generated by other leading methods, including scDesign3 and scVI. This transferability indicates that an adversary can infer sensitive information from synthetic data without access to the training procedure, model parameters, or even the underlying generation algorithm. Finally, we investigate the use of perturbation with noise during the SDG process as a first‑line defense, empirically evaluating its effectiveness in neutralizing the attack and its impact on utility.

</details>

### 195. Local FDR Membership Inference Attacks: Multiple Testing and the Role of Ridge Regularization

📝 [OpenReview](https://openreview.net/forum?id=zR0MYMNUF1) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`membership inference`、`false discovery rate`、`ridge regression`、`multiple testing`
- 🎯 **研究动机**：MIA 通常按单样本假设检验控制假阳率，但现实攻击者会测试大量候选样本并聚合成员判定，成员推断实为多重检验问题，逐样本校准会产生不可靠的推断成员集合。
- 🔬 **研究方法**：基于经典 local FDR 构建假发现率（FDR）受控的成员推断框架，并在高维 ridge 回归上实例化，在条件充分性下建立 FDR 保证，并推导各向同性高斯设计下高维情形检测功效的渐近表征。
- 📌 **结论**：理论表明在 FDR 控制下更强的 ridge 正则化会降低成员推断风险；合成与真实数据实验验证理论，所提方法比现有攻击给出更可靠的成员发现。

👤 **作者**：Jinyoung Hong、Bonwoo Lee、Jeongyoun Ahn

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership inference attacks (MIAs) are commonly formulated as single-sample hypothesis tests with false positive rate control. However, realistic adversaries often test many candidate samples and aggregate the declared members, making membership inference a multiple testing problem. In this regime, per-sample calibration can produce unreliable sets of inferred members. We develop a false discovery rate (FDR)-controlled framework for membership inference based on the classical local FDR formulation. We instantiate the framework for high dimensional ridge regression. Under a conditional sufficiency condition, we establish FDR guarantee of the proposed method, and derive an asymptotic characterization of its detection power in high-dimensional regimes under an isotropic Gaussian design. Our analysis shows that, under FDR control, stronger ridge regularization reduces membership inference risk. Experiments on synthetic and a real-world dataset validate the theoretical findings and demonstrate that the proposed methods provide more reliable membership discoveries than existing attacks.

</details>

### 196. Subliminal Learning as Trait-Direction Drift: A Mechanism and Targeted Control under SFT Distillation

📄 [arXiv](https://arxiv.org/abs/2609.01091) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`analysis`、`subliminal learning`、`trait-direction drift`、`sft distillation`、`corridor regularization`
- 🎯 **研究动机**：蒸馏可从 teacher 迁移隐藏特质（subliminal learning），但该信号如何在训练中累积并产生行为迁移的机制不明，难以针对性缓解。
- 🔬 **研究方法**：提出并验证 trait-direction drift 机制——teacher 偏好造成数据中可测偏好差、SFT 中诱发特质对齐更新并累积为行为迁移；据此提出 probe-space corridor regularization 在蒸馏中约束沿校准特质方向的漂移。
- 📌 **结论**：偏好差、训练轨迹与干预三方面证据支持该机制；corridor regularization 将恶意响应迁移从 29.55% 降至 6.45% 且主任务精度损失低，并在 Qwen 主设置中持续抑制动物偏好迁移。

👤 **作者**：Zhixuan Liu、Zhichen Dong、Yuyu Fan、Xiangtian Li、Chao Yang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Beyond intended capabilities, model distillation can transfer hidden traits from a teacher. A teacher biased by a system prompt can generate semantically clean training data, such as numeric sequences, that still causes a downstream student to inherit the hidden preference, a phenomenon known as subliminal learning. Prior work has identified several parts of this process. How the signal builds up during training and produces behavioral transfer remains unclear, making targeted mitigation difficult. We propose and validate trait-direction drift as a mechanism for subliminal learning: biased generation creates measurable preference gaps in teacher data, and student-recognizable gaps induce trait-aligned updates during supervised fine-tuning that accumulate into behavioral transfer. Guided by this mechanism, we propose probe-space corridor regularization, a targeted defense that constrains drift along a calibrated trait direction during distillation. The method substantially reduces hidden-trait transfer, preserving task performance: for example, it lowers malicious-response transfer from 29.55% to 6.45% with low main-task accuracy cost, and consistently suppresses animal-preference transfer across the main Qwen setting. The preference-gap, training-trajectory, and intervention evidence links subliminal learning to trait-direction drift and motivates corridor regularization as a targeted control during distillation.

</details>

### 197. Leaky Students: Membership Inference against On-Policy Distillation（已库内，0929）

📄 [arXiv](https://arxiv.org/abs/2609.33136) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`attack`、`membership inference`、`on-policy distillation`、`privacy leakage`、`auroc`
- 🎯 **研究动机**：OPD 中教师训练可接触敏感特权数据，学生是否泄漏教师在蒸馏中所用记录的成员信息此前缺乏系统研究，且固定参考答案损失会漏掉新鲜学生轨迹中的稀疏成员信号。
- 🔬 **研究方法**：提出 Leaky——从目标模型采样新鲜轨迹，将其 token 对数概率与未含候选记录训练的匹配参考模型上的最大值比较，对差值施加 Leaky ReLU 以保留正间隙、下调负间隙，作为对非成员偶然正间隙的近似校正。
- 📌 **结论**：在覆盖数学、医疗问答与代码生成的 15 个目标上平均 AUROC 达 0.875，而主评测中最强基线仅 0.614（同一批采样轨迹上为 0.826）。

👤 **作者**：Zhexi Lu、Mingzhi Zhu、Stacy Patterson、Lei Yu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

On-policy distillation (OPD) trains a student to match a teacher's next-token distributions on student-generated trajectories. However, privileged information supplied to the teacher for OPD training may contain sensitive data. Whether the student leaks private information about the records supplied to the teacher during distillation remains poorly understood. To the best of our knowledge, we present the first systematic study of membership inference in this setting. We find that fresh student trajectories expose sparse membership signals that fixed reference-answer losses often miss. These signals are mixed with probability changes caused by training on other records. We introduce Leaky, which samples fresh trajectories from the target model and compares its token log-probabilities with the maximum across matched reference models trained without the candidate records. It applies Leaky ReLU to the resulting gaps, preserving positive gaps and downweighting negative gaps as an approximate correction for incidental positive gaps in non-members. Across fifteen targets spanning mathematics, medical question answering, and code generation, Leaky outperforms all evaluated baselines and achieves mean AUROC 0.875, compared with 0.614 for the strongest baseline on each target in the main evaluation. On the same sampled trajectories, the strongest baseline achieves mean AUROC 0.826. These results show that students trained through OPD can expose the membership of records used for teacher supervision, even when fixed reference-answer losses provide little evidence of membership.

</details>

### 198. Near-Duplicate Families Break Exact-Record Membership Inference（已库内，0929）

📄 [arXiv](https://arxiv.org/abs/2609.33909) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`analysis`、`membership inference`、`near-duplicate`、`copyright auditing`、`false attribution`
- 🎯 **研究动机**：成员推断被用作数据溯源与版权审计证据，但 web 级数据天然含近重复家族（联合发布文章、镜像页、轻改图像），标准干净参考审计无法区分"精确记录被训练"与"家族成员被训练"。
- 🔬 **研究方法**：提出四世界审计，独立操控精确记录是否包含与家族是否存在两类状态以分离该混淆，并通过受控干预分析学习目标的影响。
- 📌 **结论**：CC-News 上干净参考 LiRA 在 1.00% 误报率下将 99.70% 的"家族存在但精确记录未训练"样本错标为成员；分类任务中家族近乎完全替代精确记录使精确推断降至近随机。

👤 **作者**：Yiyong Liu、Jiayang Liu、Yixin Tan、Lu Sun、Rui Wen

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership inference (MI) asks whether a specific record appeared in a model's training set and is increasingly used as evidence for data provenance and copyright auditing. These applications require determining whether the exact queried record was used for training, rather than merely whether the model was exposed to similar content. Making this distinction is challenging because web-scale datasets naturally contain near-duplicates, including syndicated articles, mirrored pages, and lightly modified images. We show that this creates a fundamental confound for standard MI. A clean-reference audit typically calibrates membership against a null in which neither the queried record nor its near-duplicate family is present. In deployment, however, the queried record may be absent while a non-identical family member was used for training. We introduce a four-world audit that independently varies exact-record inclusion and family presence to separate these cases. Natural near-duplicate families cause severe false attribution. On CC-News, a clean-reference LiRA auditor labels 99.70% of family-present exact non-members as members at 1.00% false-positive rate. This failure persists across alternative scores, model architectures, and executed deduplication and retraining. Controlled interventions further reveal that the effect depends on the learning objective. In classification, faithful families largely substitute for the exact record, reducing exact-given-family inference to near chance. In autoregressive language modeling, the exact sequence retains a detectable residual, while family presence still confounds clean-reference decisions. These results show that positive model-only membership evidence may establish family-level exposure without establishing exact-record provenance.

</details>

### 199. What to Remember, What to Reveal: Privacy-Aware Memory for Conversational Agents

📄 [arXiv](https://arxiv.org/abs/2608.16551) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-08　🏷 NeurIPS 2026

**关键词**：`defense`、`privacy`、`conversational memory`、`pii`、`personalization`
- 🎯 **研究动机**：个性化对话智能体的长期记忆主要为效用优化而存储复用用户信息，忽视 PII 等隐私属性被不必要暴露的风险，而简单删除敏感值又会损害效用，隐私保护须治理敏感值的完整生命周期。
- 🔬 **研究方法**：提出 SP-Mem 隐私感知记忆架构，把记忆效用与精确隐私值暴露解耦——从原始输入识别并分离敏感信息、在隔离结构中分别存储脱敏内容与精确隐私值、按任务需求与用户同意选择性检索，并配套联合评测响应质量、隐私行为与推理成本的基准。
- 📌 **结论**：跨多个 LLM 智能体的实验表明，SP-Mem 在减少不必要隐私暴露的同时实现更强的个性化。

👤 **作者**：Wenjie Wang、Wenhe Si、Xinyue Xu、Yue Xu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Long-term memory enables personalized conversational agents to retain user information across sessions. However, existing memory architectures primarily optimize for utility while neglecting the risks of unnecessarily storing and reusing private attributes such as personally identifiable information (PII). Addressing privacy risks in personalized memory is challenging because simply removing sensitive values can undermine system utility. Therefore, privacy protection for memory agents should govern the full life cycle of sensitive values rather than only sanitizing individual records. To address this gap, we introduce Sanitized Privacy-Mapped Memory (SP-Mem), a privacy-aware memory architecture that decouples memory utility from exact private-value exposure. SP-Mem provides a full life-cycle privacy design that identifies and separates sensitive information from raw user inputs, stores sanitized content and exact private values in isolated structures, and selectively retrieves private values based on task requirements and user consent. We further introduce a privacy-aware memory benchmark that jointly evaluates response quality, privacy behavior, and inference cost. Extensive experiments across multiple LLM-based agents show that SP-Mem achieves stronger personalization while reducing unnecessary privacy exposure. Code and data are available at https://github.com/Jensassss/SP-Mem.

</details>

### 200. Inadvertent Context Leakage in Language Models

📄 [arXiv](https://arxiv.org/abs/2608.19857) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-08　🏷 NeurIPS 2026

**关键词**：`attack`、`context leakage`、`secret reconstruction`、`black-box attack`、`privacy`
- 🎯 **研究动机**：agent 上下文中存在日历、凭证、健康、财务等敏感信息时，即使模型正确拒绝直接提取，其良性输出是否携带可重建秘密的隐藏相关性、以及对手能否主动放大该效应，均未知。
- 🔬 **研究方法**：研究被动泄露与主动 prompt 工程两种情形，用仅需底层模型黑盒访问的新型自适应攻击，把模型当作隐蔽载体从看似无害的文本中提取秘密。
- 📌 **结论**：8 个专有模型上 2 位数上下文秘密以近完美精度重建、4 位数达 82% 精确匹配（全部来自普通非对抗请求的输出），且能力越强泄露越多；可训练分类器从常规输出推断用户记忆语义谓词，RL 训练的攻击者可从生产型 agent 提取完整社会安全号码。

👤 **作者**：Jaiden Fairoze、Neal Mangaokar、Kamalika Chaudhuri、Sanjam Garg、Saeed Mahloujifar

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

For AI agents to be useful beyond simple chat, they must hold sensitive user context such as calendars, credentials, health records, and financial data. We study whether the mere presence of such secrets in a model's context window introduces hidden correlations into the model's benign outputs, allowing reconstruction even when the model correctly refuses direct extraction. We further study whether an adversary can actively engineer prompts that amplify this effect, using the model as a covert carrier to transmit secrets through seemingly innocuous text. In both cases, this limited leakage is exploited using a novel adaptive attack that assumes black-box access to the underlying model. In controlled experiments across eight proprietary models, we find that 2-digit in-context secrets are reconstructed with near-perfect accuracy and 4-digit secrets at 82\% exact match, all from outputs the model produces in response to ordinary, non-adversarial requests. We observe that more capable models leak more: stronger instruction-following amplifies sensitivity to in-context secrets, suggesting leakage is a byproduct of capability as opposed to a patchable bug. We show this leakage enables two practical attacks: (1) a trained classifier that infers semantic predicates about user memories (e.g., health conditions, financial events) from routine natural-language outputs, and (2) an RL-trained adversary that extracts full Social Security Numbers from a production-style agent.

</details>

### 201. Learning What to Forget: Improving LLM Unlearning via Learned Token-Level Importance

📄 [arXiv](https://arxiv.org/abs/2606.06320) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`defense`、`llm unlearning`、`token-level importance`、`joint optimization`、`forget-retain tradeoff`
- 🎯 **研究动机**：自回归 LLM 遗忘样本中各 token 与遗忘的相关性不同，现有方法或忽略该异质性或依赖辅助模型、启发式与外部标注来估计 token 相关性。
- 🔬 **研究方法**：以"最小化该 token 的 forget loss 是否与 retain 最优性冲突"定义 token forget-specificity 并形式化为参数与 token 权重的联合优化，提出 ATWU 在遗忘过程中用 hidden states 上的线性 scorer 联合学习两者、无需外部 token 监督。
- 📌 **结论**：在 TOFU 与 RWKU 上取得 SOTA forget-retain 权衡，超越样本级方法、概率启发式与辅助模型方法，且学到的分数与真实 forget-specific span 对齐显著更好。

👤 **作者**：Gizem Yüce、Giorgos Nikolaou、Nicolas Flammarion

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning aims to remove targeted knowledge from a trained model while preserving its general capabilities. For autoregressive language models, not all tokens in a forget sample are equally relevant to forgetting. Existing approaches either ignore this heterogeneity or rely on auxiliary models, heuristics, or external annotations to estimate each token's relevance for forgetting. We instead characterize it through the interaction with the retain objective: a token is forget-specific to the extent that minimizing the forget loss on that token does not conflict with retain optimality. We formalize this perspective as a joint optimization problem over the model parameters and the token weights and show that, under a natural separation condition, the resulting objective recovers the oracle forget-specific token support. Motivated by this formulation, we introduce Alternating Token-Weighted Unlearning (ATWU), a lightweight framework that jointly learns token forget-specificity and model parameters during unlearning using a simple linear scorer over the hidden states, without external token level supervision. Across TOFU and RWKU, ATWU achieves state of the art forget-retain trade-offs, outperforming sample-level methods, probability-based token weighting heuristics, and auxiliary-model-based approaches. Moreover, the learned scores align substantially better with ground truth forget-specific spans, indicating that ATWU identifies semantically meaningful token level forgetting signals. Overall, our results suggest that retain conflict provides an effective criterion for identifying what language models should forget, enabling unsupervised learning of token level forget-specificity directly from model representations with minimal computational overhead.

</details>

### 202. Exposing the Illusion of Erasure in Knowledge Editing for LLMs

📄 [arXiv](https://arxiv.org/abs/2606.23276) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`analysis`、`knowledge editing`、`adversarial elicitation`、`low-rank update`
- 🎯 **研究动机**：知识编辑号称无需重训练即可更新 LLM 特定事实，但被编辑知识常未被真正擦除而持续浮现，其机制与可靠性尚不清楚
- 🔬 **研究方法**：从对抗性诱导视角审视主流 KE 方法并做机制分析，发现低秩更新并非覆盖旧知识而是在表示空间中重新分布，实为降低原事实表达概率的定向抑制
- 📌 **结论**：编辑后的知识位于狭窄且各向异性的损失区域、对扰动高度敏感，易被间接 prompting 与对抗攻击诱导，证明 KE 算法本质上可被绕过

👤 **作者**：Advik Raj Basani、Anshuman Chhabra

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Knowledge Editing (KE) has emerged as a frontier for updating specific facts in LLMs without costly retraining, but its reliability and underlying mechanisms remain poorly understood. In this work, we examine KE from an adversarial elicitation perspective, revealing that edited knowledge is often not fully erased and continues to surface, with consistent failures observed across diverse model architectures. To explain this behavior, we conduct a mechanistic analysis of popular KE methods. We show that low-rank updates do not overwrite existing knowledge but instead redistribute it within the model's representation space. Furthermore, we find that these methods act as targeted suppression mechanisms that reduce the likelihood of expressing original facts, rather than removing them from the model. Analysis of the loss landscape reveals that edited knowledge lies in narrow, anisotropic regions that are highly sensitive to perturbations, making them highly vulnerable to indirect prompting and adversarial attacks. By exposing these profound architectural vulnerabilities, our work proves that KE algorithms are inherently bypassable and motivates a fundamental reevaluation of how we deploy post-hoc updates in several LLM applications.

</details>

### 203. PrivacySIM: Evaluating LLM Simulation of User Privacy Behavior

📄 [arXiv](https://arxiv.org/abs/2605.12147) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`privacy behavior`、`user simulation`、`persona conditioning`、`llm agents`
- 🎯 **研究动机**：LLM 越来越多地被用于模拟人类行为，但其能否模拟个体级的隐私决策缺乏评测。
- 🔬 **研究方法**：提出 PrivacySIM 评测套件，以五项隐私用户研究中 1000 名真实用户的地面真值响应为基准，用人口统计、既往经历、自述隐私态度三类 persona 要素条件化九个前沿模型，度量其响应与用户实际响应的匹配率。
- 📌 **结论**：persona 条件化一致优于无条件模拟，但最强模型准确率仅 40.4%，远未忠实模拟个体隐私决策；自述隐私态度因与实际行为背离未必是最好的预测因子，高 AI/聊天机器人经验而低隐私态度的用户最难模拟。

👤 **作者**：James Flemings、Murali Annavaram

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used to simulate human behavior, but their ability to simulate $individual$ privacy decisions is not well understood. In this paper, we address the problem of evaluating whether a core set of user persona attributes can drive LLMs to simulate individual-level privacy behavior. We introduce PrivacySIM, an evaluation suite that benchmarks LLM simulation of user privacy behavior against the ground-truth responses of 1,000 users. These users are drawn from five published user studies on privacy spanning LLM healthcare consultations, conversational agents, and chatbots. Drawing on these user studies, we hypothesize three persona facets as plausible predictors of privacy decision-making: demographics, previous experiences, and stated privacy attitudes. We condition nine frontier LLMs on subsets of these three facets and measure how often each model's response to a data-sharing scenario matches the user's actual response. Our findings show that (1) privacy persona conditioning consistently improves simulation quality over no-persona conditioning, but even the strongest model (40.4\% accuracy) remains far from faithfully simulating individual privacy decisions. (2) A user's stated privacy attitudes alone may not be the best predictor because they often diverge from the user's actual privacy behavior. (3) Users with high AI/chatbot experience but low stated privacy attitudes are the most challenging to simulate. PrivacySIM is a first step toward understanding and improving the capabilities of LLMs to simulate user privacy decisions. We release PrivacySIM to enable further evaluation of LLM privacy simulation.

</details>

### 204. POLAR-Bench: A Diagnostic Benchmark for Privacy-Utility Trade-offs in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2605.19127) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`privacy policy`、`adversarial probing`、`llm agent`、`privacy-utility tradeoff`
- 🎯 **研究动机**：LLM agent 越来越多接触用户私有数据并代表用户与第三方系统交互，须在第三方对抗探测下稳健遵循用户的分享意图，而现有评估缺位。
- 🔬 **研究方法**：构建 POLAR-Bench，让带隐私政策与任务的可信模型与对抗探测任务相关及受保护属性的第三方模型对话，跨 10 个域、7852 个样本以确定性集合隶属度评分，沿隐私政策维度与攻击策略两条正交轴生成每模型 5×5 诊断面。
- 📌 **结论**：当前前沿模型扣留超 99% 受保护属性，而用户最常本地或私有推理运行的 1-30B 小模型明显更差、最弱者泄露过半，从而精确定位各模型意图遵循的失效点。

👤 **作者**：Qiaoyuan Zheng、Yiqu Yang、Qi Gao、Imanol Schlag

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents increasingly have access to private user data and act on the user's behalf when interacting with third-party systems. The user defines what may and must not be shared, and the agent must robustly follow that intent even when third-party systems behave adversarially. We introduce POLAR-Bench (Policy-aware adversarial Benchmark), in which a trusted model with a privacy policy and a task converses with a third-party model that adversarially probes for both task-relevant and protected attributes. Across 10 domains and 7,852 samples, we score privacy and utility by deterministic set-membership and vary privacy policy dimension and attack strategy along two orthogonal axes, producing a 5 times 5 diagnostic surface per model. Our results reveal a sharp split: current frontier models withhold over 99% of protected attributes, while smaller open-weight models in the 1--30B range, the class users most commonly run as their own trusted agent on-device or via private inference, score notably worse, with the weakest leaking over half. POLAR-Bench thus localizes where each model's intent-following breaks down, providing a foothold for privacy alignment where it matters most.

</details>

### 205. Forgetting Has Neighbors: Localized Collateral Forgetting in Machine Unlearning

📄 [arXiv](https://arxiv.org/abs/2605.31317) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`machine unlearning`、`collateral forgetting`、`local teacher distillation`
- 🎯 **研究动机**：machine unlearning 的聚合评估指标会掩盖样本级失败——unlearned 模型与删除后重训练模型的逐样本预测差异高度非均匀，这一失败模式此前未被系统研究
- 🔬 **研究方法**：逐样本比对 unlearned 模型与 retrain 模型的预测，识别出随与 forget set 几何邻近度增长的 localized collateral forgetting 现象，并提出 Local Teacher Distillation——用仅在 forget set 保留邻居上训练的小教师软标签替代随机代理目标
- 📌 **结论**：CIFAR-100 部分类删除任务上，局部教师使 unlearned 模型在 forget set 附近显著逼近重训练结果，同时保持有竞争力的聚合 unlearning 指标

👤 **作者**：Polina Dolgova、Sebastian U. Stich

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning aims to remove the influence of selected training examples without full retraining. Standard evaluations often summarize unlearning quality with aggregate metrics, such as accuracy- and forgetting-based scores, which can hide localized failures. We study this failure mode at the example level by comparing the predictions of an unlearned model to those of the model retrained after deletion. We show that this pointwise discrepancy can be highly non-uniform: for gradient-ascent and random-labeling methods, with and without retain-set fine-tuning, it grows with geometric proximity to the forget set. We call this phenomenon localized collateral forgetting. Our analysis identifies a mechanism behind the effect: surrogate targets used during unlearning can be inconsistent with the local prediction structure induced by retraining, and this inconsistency propagates through shared representations to nearby examples. Motivated by this mechanism, we propose Local Teacher Distillation, a simple mitigation strategy that replaces random targets with soft labels from a small teacher trained only on retained neighbors of the forget set. On CIFAR-100 partial-class deletion, this local teacher brings the unlearned model substantially closer to retraining, especially near the forget set, while maintaining competitive aggregate unlearning metrics.

</details>

### 206. Subliminal Learning Is Steering Vector Distillation

📄 [arXiv](https://arxiv.org/abs/2606.00995) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`subliminal learning`、`steering vector`、`distillation`、`adaptive optimizer`
- 🎯 **研究动机**：学生模型微调教师输出时会习得与输出语义无关的教师特质（subliminal learning），无语义数据如何传递特定语义特质机制不明。
- 🔬 **研究方法**：在两个开源模型上证明该现象由单个 steering vector 中介——教师系统提示可被 steering vector 良好近似、学生通过微调习得对齐向量，并将其统一为 steering vector distillation 框架，进一步考察自适应优化器的作用。
- 📌 **结论**：不能被 steering vector 良好近似的系统提示不会被潜默习得，非语义数据可传递带语义效果的向量，这解释了潜默学习无法跨模型迁移；自适应优化器是必要条件——被引导数据上的激活梯度沿 steering 方向携带小而一致的分量，非自适应优化器会让离群梯度主导从而阻断学习。

👤 **作者**：Camila Blank、Agam Bhatia、Senthooran Rajamanoharan、Arthur Conmy、Neel Nanda

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Subliminal learning refers to a student language model acquiring a teacher's traits (e.g. a system-prompted preference for owls) when fine-tuned on the teacher's outputs, despite the outputs being semantically unrelated to those traits. It remains poorly understood how data without semantic meaning can transfer specific semantic traits. In this work, we show that subliminal learning is mediated by a single steering vector, i.e. a vector added to the model's activations. Across two open-source models, we find that the teacher's system prompt is well approximated by a steering vector, and that the student's behavior is driven by learning an aligned vector over fine-tuning. System prompts that are not well approximated by steering vectors are not subliminally learned. This is a special case of steering vector distillation, in which a student trained on the outputs of a steered teacher learns to imitate that steering. We demonstrate steering vector distillation on a range of semantic and random vectors. Adding a semantic vector to a model's activations can have both model-independent and model-specific (i.e. non-semantic) effects on its behavior, so generated data that is non-semantic can transmit a vector with semantic effects, enabling subliminal learning. This also explains why subliminal learning does not transfer between models. We find that adaptive optimizers are necessary for subliminal learning in language models: activation gradients on steered data carry a small but consistent component along the steering direction, and non-adaptive optimizers impede this by allowing outlier gradients to dominate.

</details>

### 207. Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation

📄 [arXiv](https://arxiv.org/abs/2604.15559) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-04　🏷 NeurIPS 2026

**关键词**：`attack`、`agent distillation`、`subliminal learning`、`trajectory`、`data sanitation`
- 🎯 **研究动机**：subliminal learning 已证明语义特质可经无关数据传输，但 agentic 系统的策略从轨迹而非静态文本学习，不安全行为能否经蒸馏隐式迁移尚无实证。
- 🔬 **研究方法**：构造具强删除偏好的 teacher agent，仅用严格过滤所有删除关键词的安全任务轨迹蒸馏 student，并在原生 Bash 环境以 chmod-first 命令偏好复现同一威胁模型。
- 📌 **结论**：API 设置中 student 删除率达 100%（基线 5%），Bash 设置中 chmod-first 率达 30-55%（基线 0-10%）、大模型到小模型蒸馏迁移最强，说明显式数据清洗不足以防御、行为偏差隐式编码于轨迹动力学。

👤 **作者**：Jacob Dang、Brian Y. Xie、Omar G. Younis

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent work on subliminal learning demonstrates that language models can transmit semantic traits through data that is semantically unrelated to those traits. However, it remains unclear whether behavioral traits can transfer in agentic systems, where policies are learned from trajectories rather than static text. In this work, we provide the first empirical evidence that unsafe agent behaviors can transfer subliminally through model distillation across two complementary experimental settings. In our primary setting, we construct a teacher agent exhibiting a strong deletion bias, a tendency to perform destructive file-system actions via an API-style tool interface, and distill it into a student using only trajectories from ostensibly safe tasks, with all explicit deletion keywords rigorously filtered. In our secondary setting, we replicate the threat model in a native Bash environment, replacing API tool calls with shell commands and operationalizing the bias as a preference for issuing chmod as the first permission-related command over semantically equivalent alternatives such as chown or setfacl. Despite full keyword sanitation in both settings, students inherit measurable behavioral biases. In the API setting the student's deletion rate reaches 100% (versus a 5% baseline) under homogeneous distillation; in the Bash setting the student's chmod-first rate reaches 30%-55% (versus a 0%-10% baseline), with the strongest transfer observed in large-to-small distillation. Our results demonstrate that explicit data sanitation is an insufficient defense, and behavioral biases are encoded implicitly in trajectory dynamics regardless of the tool interface.

</details>

### 208. CLIOPATRA: Extracting Private Information from LLM Insights

📄 [arXiv](https://arxiv.org/abs/2603.09781) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`attack`、`privacy leakage`、`prompt injection`、`llm insights`
- 🎯 **研究动机**：隐私感知平台靠 PII 脱敏、聚类、聚合与 LLM 隐私审计等多层启发式保护提取使用洞察，但其"隐私保护"声明从未经受攻击检验
- 🔬 **研究方法**：提出 CLIOPATRA 攻击——对抗者精心设计并插入恶意聊天以击穿多层防护，诱导目标用户聊天中的敏感信息泄露，并在 Anthropic Clio 平台上以合成医疗聊天进行评估
- 📌 **结论**：攻击者能以近 100% 精度在最高 65% 的案例中提取医疗史，可通过混淆洞察隐蔽外泄，且 LLM 隐私审计等现有缓解不可靠、检测不到重大泄露

👤 **作者**：Meenatchi Sundaram Muthu Selva Annamalai、Emiliano De Cristofaro、Peter Kairouz

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The widespread adoption of AI assistants has prompted the development of privacy-aware platforms designed to extract insights from real-world usage. Their privacy protections primarily rely on layering multiple heuristic techniques, such as PII redaction, clustering, aggregation, and LLM-based privacy auditing. In this paper, we put their privacy claims to the test by presenting CLIOPATRA, the first attack against ``privacy-preserving'' LLM-based insights systems. Our attack involves an adversary that carefully designs and inserts malicious chats into the system to break multiple layers of protections and induce the leakage of sensitive information from a target user's chat. We evaluate CLIOPATRA on one such platform, Anthropic's Clio, and target synthetically generated medical chats to show that an adversary can successfully and confidently (with nearly 100% precision) extract the medical history contained in these chats in up to 65% of cases. We also show that CLIOPATRA can stealthily extract information by obfuscating the private information in the generated insights. Finally, we demonstrate that existing ad hoc mitigations, such as LLM-based privacy auditing, are unreliable and fail to detect major leaks. Taken together, our findings indicate that, even when layered, current heuristic protections are insufficient to adequately protect user data, and that prompt injection has been an understudied risk in LLM-based insight systems.

</details>

### 209. Models Designed to Forget: Machine Unlearning via Key Deletion

📄 [arXiv](https://arxiv.org/abs/2603.15033) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`defense`、`machine unlearning`、`key deletion`、`memory-augmented transformer`、`unlearning by design`
- 🎯 **研究动机**：现有近似 unlearning 从事后视角出发、靠参数更新擦除目标样本影响且通常需全量训练数据，与遗忘请求可被预期的真实部署场景根本错配。
- 🔬 **研究方法**：提出 unlearning by design 范式并实例化 MUNKEY——用 memory-augmented transformer 把实例特定记忆与模型权重解耦，遗忘即删除实例识别 key，实现零样本遗忘而无需权重更新或原始样本标签。
- 📌 **结论**：在自然图像、细粒度视觉识别与医学数据集上超越所有 post-hoc 基线，实现快速、面向部署的遗忘同时保持预测性能。

👤 **作者**：Sonia Laguna、Jorge da Silva Goncalves、Moritz Vandenhirtz、Alain Ryser、Irene Cannistraci、Julia E. Vogt

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning for vision models is rapidly becoming a practical requirement, driven by privacy regulations, data errors, and the need to remove harmful or corrupted training images. Despite this, most existing approximate unlearning methods tackle the problem from a post-hoc perspective. They attempt to erase the influence of targeted samples through parameter updates that typically require access to the full training data. This creates a mismatch with real deployment scenarios where unlearning requests can be anticipated, revealing a fundamental limitation of post-hoc approaches. We motivate unlearning by design, a novel paradigm for approximate methods in which models are directly trained to support forgetting as an inherent architectural capability. We instantiate this idea with Machine UNlearning via KEY deletion (MUNKEY), a memory-augmented transformer that decouples instance-specific memorization from model weights. Here, unlearning corresponds to removing the instance-identifying key, enabling zero-shot forgetting without weight updates or access to the original samples or labels. Across natural image benchmarks, fine-grained visual recognition, and medical datasets, MUNKEY outperforms all post-hoc baselines. Our results establish that unlearning by design enables fast, deployment-oriented unlearning while preserving predictive performance.

</details>

### 210. SMI: Statistical Membership Inference for Reliable Unlearned Model Auditing

📄 [arXiv](https://arxiv.org/abs/2602.01150) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`detection`、`unlearning audit`、`membership inference`、`mixture proportion`、`training-free`
- 🎯 **研究动机**：用 MIA 审计 unlearning 时"逃过成员检测即已遗忘"的假设根本错误——unlearned 样本与非成员在特征空间位置不同导致系统性乐观评估，且训练 shadow model 开销巨大。
- 🔬 **研究方法**：提出 SMI 免训练审计框架，将审计重构为估计 unlearned 特征分布中非成员混合比例，并给出 bootstrap 参考区间量化审计可靠性。
- 📌 **结论**：SMI 一致超越所有基于 MIA 的审计基线且无需 shadow model 训练，兼有理论保证与强经验表现。

👤 **作者**：Jialong Sun、…、Bo Liu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning (MU) is essential for enforcing the right to be forgotten in machine learning systems. A key challenge of MU is how to reliably audit whether a model has truly forgotten specified training data. Membership Inference Attacks (MIAs) are widely used for unlearned model auditing, where samples that evade membership detection are regarded as successfully forgotten. We show this assumption is fundamentally flawed: failed membership inference does not imply true forgetting. We prove that unlearned samples occupy fundamentally different positions in the feature space than non-member samples, making this alignment bias unavoidable and unobservable, which leads to systematically optimistic evaluations of unlearning performance. Meanwhile, training shadow models for MIA incurs substantial computational overhead. To address both limitations, we propose Statistical Membership Inference (SMI), a training-free auditing framework that reformulates auditing as estimating the non-member mixture proportion in the unlearned feature distribution. Beyond estimating the forgetting rate, SMI also provides bootstrap reference ranges for quantified auditing reliability. Extensive experiments show that SMI consistently outperforms all MIA-based baselines, with no shadow model training required. Overall, SMI establishes a principled and efficient alternative to MIA-based auditing methods, with both theoretical guarantees and strong empirical performance.

</details>

### 211. Causal Evaluation of Membership Inference Attacks

📄 [arXiv](https://arxiv.org/abs/2602.02819) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`evaluation`、`membership inference`、`causal inference`、`memorization`、`privacy audit`
- 🎯 **研究动机**：标准 MIA 评估需重复重训练、对大模型代价高昂，而常用替代的 one-run 与 zero-run 方法的统计有效性不明。
- 🔬 **研究方法**：将 MIA 评估框架化为因果推断问题（记忆化定义为纳入数据点的因果效应），形式化 one-run 中联合纳入数据点的干扰与 zero-run 额外的成员/非成员分布偏移偏差，推导多 run、one-run、zero-run 情形的因果版指标与非渐近一致估计器。
- 📌 **结论**：在预训练与微调 LLM 等多个设置中验证，该框架无需重训练且在分布偏移下仍可可靠测量 MIA 性能。

👤 **作者**：Mathieu Even、Clément Berenfeld、Linus Bleistein、Tudor Cebere、Julie Josse、Aurélien Bellet

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership Inference Attacks (MIAs) aim to distinguish training points (members) from unseen data (non-members), and are widely used to quantify memorization and assess privacy risks. Standard MIA evaluation requires repeated retraining, which is computationally costly for large models. One-run (single training with randomized data inclusion) and zero-run (post hoc evaluation) methods are often used instead, but their statistical validity remains unclear. We address this gap by framing MIA evaluation as a causal inference problem, defining \emph{memorization as the causal effect of including a data point in the training set}. This novel formulation reveals and formalizes key sources of bias in existing protocols: one-run methods suffer from interference between jointly included points, while zero-run evaluations are additionally confounded by distribution shift between member and non-member evaluation data. We derive causal analogues of standard MIA metrics and propose practical estimators for multi-run, one-run, and zero-run regimes with non-asymptotic consistency guarantees. We validate our approach in several settings, including pretrained and fine-tuned LLMs, showing that it enables reliable measurement of MIA performance without retraining and under distribution shift. Overall, our framework provides a principled foundation for privacy evaluation in modern AI systems.

</details>

### 212. Assessing Per-Sample Membership Inference Vulnerability without Retraining

📄 [arXiv](https://arxiv.org/abs/2602.15919) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`analysis`、`membership inference`、`privacy risk`、`leverage score`、`shadow model`
- 🎯 **研究动机**：针对单样本的成员推断攻击（MIA）大幅强于无差别攻击，但评估单个训练点的隐私脆弱性通常需要训练影子模型，代价高昂。
- 🔬 **研究方法**：在线性情形推导出黑盒 MIA 脆弱性对总体杠杆分数与残差损失的闭式分解，据此提出作用于末层表示、仅需单个已训练模型而无需影子模型的代理分数。
- 📌 **结论**：跨多样数据集与架构的实验中，该分数在最先进攻击下识别最高风险样本的能力优于 loss 与梯度范数基线，为逐样本隐私风险评估提供了高效且有理论依据的工具。

👤 **作者**：Valentin Dorseuil、Jamal Atif、Olivier Cappé

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent work in the privacy literature shows that sample-targeted membership inference attacks (MIAs) significantly outperform untargeted approaches by a wide margin. Motivated by this observation, we address the following question: can the privacy vulnerability of individual training points be assessed without training shadow models? We show that per-sample exposure to MIA is governed not only by a point's loss, but also by a data-dependent geometric measure. In the linear setting, we derive a closed-form decomposition of individual black-box MIA vulnerability into a population leverage score and a residual loss term, making explicit how sample-dependent geometry translates into privacy exposure. Since the final layer of most modern architectures is linear, we extend this framework to deep networks and propose a surrogate score operating on last-layer representations that requires only a single trained model and no shadow models. Empirical evaluations across diverse datasets and architectures show that our score outperforms loss and gradient-norm baselines at identifying the highest-risk points under state-of-the-art attacks, providing a computationally efficient and theoretically grounded tool for per-sample privacy risk assessment.

</details>

### 213. Sequential Membership Inference Attacks

📄 [arXiv](https://arxiv.org/abs/2602.16596) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`attack`、`membership inference`、`canary`、`privacy audit`、`dp-sgd`
- 🎯 **研究动机**：现代 AI 模型生命周期中经历多次更新，现有成员推断只审视最终模型快照，未利用模型序列信息。
- 🔬 **研究方法**：提出 Sequential Membership Inference（SeMI），在受控插入时间注入目标 canary 并利用模型序列；推导最优攻击 SeMI* 及其 power（隔离性质：power 仅取决于插入前后的统计量），发展 white-box 梯度与 black-box loss 两种实用攻击。
- 📌 **结论**：在 (DP-)SGD 训练的模型上 SeMI 攻击 power 高于快照独立基线，借助插入时间控制与序列观察产生更紧的隐私审计。

👤 **作者**：Thomas Michel、Debabrota Basu、Emilie Kaufmann

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern AI models are not static. They go through multiple updates in their lifecycles. We propose to design Sequential Membership Inference (SeMI) attacks leading to tighter privacy audits by exploiting the sequence of models and injecting a target canary at a controlled insertion time. First, for empirical mean computation, we develop SeMI*, an {optimal SeMI attack to identify the presence of a target inserted at a specific insertion step}. We derive the power of SeMI* to show that accessing the model sequence yields more powerful MI attacks than scrutinising only the final model. SeMI* exhibits an isolation property -- its power depends on the statistics obtained right before and after insertion of the target. Leveraging this insight, we develop practical white-box (accessing model gradients) and black-box (accessing loss) SeMI attacks against models trained with (DP-)SGD. Across datasets and models trained with (DP-)SGD, our experiments show that SeMI attacks achieve higher powers than snapshot-independent baselines, and yield tighter privacy audits thanks to (a) control over the insertion time and (b) observations across the model sequence.

</details>

### 214. GUIGuard-Bench: Toward a General Evaluation for Privacy-Preserving GUI Agents

📄 [arXiv](https://arxiv.org/abs/2601.18842) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-01　🏷 NeurIPS 2026

**关键词**：`benchmark`、`gui agent`、`privacy`、`region-level annotation`、`trajectory`
- 🎯 **研究动机**：GUI agent 依赖截图感知环境易暴露身份、账户、位置与行为痕迹等敏感信息，而现有视觉隐私数据集局限于静态自然图像，无法刻画 GUI 任务轨迹中隐私风险的上下文依赖与任务相关性。
- 🔬 **研究方法**：构建含 241 条真实 GUI agent 轨迹、4080 张 Android 与 PC 截图的 benchmark，每张截图带区域级隐私边界框、语义隐私类别、风险等级与任务必要性标注，支持隐私识别、保护截图下离线规划保真与保护策略效用影响三项互补评估。
- 📌 **结论**：现有模型常能判断截图是否含隐私信息，但在细粒度定位、类别识别、风险评估与任务必要性判断上表现不佳；以 Claude Sonnet 4.6 为代表的闭源模型在 Android 环境应用隐私保护后仍能保持基本一致的规划语义。

👤 **作者**：Yanxi Wang、…、Jiyan He

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As GUI agents increasingly rely on screenshots to perceive and operate digital environments, they may inadvertently expose sensitive information such as identities, accounts, locations, and behavioral traces. While existing benchmarks primarily focus on task completion, grounding, or defenses against third-party attacks, current visual privacy datasets remain largely restricted to static natural images, limiting their ability to capture the contextual dependence and task relevance of privacy risks in GUI task trajectories. To bridge this gap, we introduce \textbf{GUIGuard-Bench}, a first-step benchmark for studying privacy-preserving GUI agents in trajectory-based GUI workflows. GUIGuard-Bench contains 241 real GUI-agent trajectories with 4,080 screenshots across Android and PC environments. Each screenshot is annotated at the region level with privacy bounding boxes, semantic privacy categories, risk levels, and whether the private information is necessary for completing the task. Built on these annotations, GUIGuard-Bench supports three complementary evaluations: privacy recognition, offline planning fidelity under protected screenshots, and the utility impact of different protection strategies. Our results show that current models can often detect whether a screenshot contains private information, but they struggle with fine-grained localization, category recognition, risk assessment, and task-necessity judgment. We also find that closed-source models, exemplified by Claude Sonnet 4.6, can maintain largely consistent planner semantics in Android environments after privacy protection is applied. Our results highlight privacy recognition as a critical bottleneck for practical GUI agents. Project: https://futuresis.github.io/GUIGuard-page/

</details>

### 215. Estimating Model-Level Membership Inference Vulnerability Without Reference Models

📄 [arXiv](https://arxiv.org/abs/2510.19773) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`evaluation`、`membership inference`、`reference-free`、`loss distribution`、`privacy auditing`
- 🎯 **研究动机**：成员推断攻击是评估 AI 模型隐私风险的标准工具，但最强攻击 LiRA 需训练大量计算昂贵的参考模型，实用性受限。
- 🔬 **研究方法**：直接从目标模型的训练/测试损失分布无参考地估计 LiRA 脆弱性，证明其逐样本信号可分解为方差比项与残差均值偏移项，模型因此落在连续谱上、不同形态对应不同免参考损失统计量作 LiRA TPR 代理，并由损失分布形状指示适用代理。
- 📌 **结论**：重尾端 LOSS 攻击 TNR 预测 LiRA TPR@FPR=10^-3 在 9 个图像分类架构、4 个数据集上 RMSE 为 0.03，对称端 LOSS AUC 预测 10M-1B 五个 GPT-2 规模的 LiRA TPR 达 RMSE 0.01，均优于 RMIA 等低成本参考攻击。

👤 **作者**：Euodia Dodd、Natasa Krco、Igor Shilov、Matthew R Wicker、Yves-Alexandre de Montjoye

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership inference attacks (MIAs) have emerged as the standard tool for evaluating the privacy risks of AI models. However, state-of-the-art attacks require training numerous, often computationally expensive, reference models, limiting their practicality. We present a novel approach for estimating model-level vulnerability to the Likelihood Ratio Attack (LiRA), the strongest available attack, directly from the train and test loss distributions of the target model and without training any reference models. We show that LiRA's per-sample signal decomposes into a variance-ratio term and a residual mean-shift term, with the relative contribution of each determined by how much training collapses model uncertainty at the trained sample. This places models on a continuum, with different regimes calling for different reference-free loss-based statistics as proxies for LiRA TPR. The shapes of the loss distributions themselves indicate which proxy applies. We instantiate the framework with two natural proxies. At the heavy-tailed end, the LOSS attack TNR predicts LiRA TPR@FPR=10^-3 with RMSE 0.03 across 9 image classification architectures and 4 datasets, outperforming low-cost reference-model attacks such as RMIA. At the symmetric end, the LOSS attack AUC predicts LiRA TPR with RMSE 0.01 across five GPT-2 sizes from 10M to 1B parameters. We also show these proxies to outperform both low-cost (few reference models) attacks such as RMIA and other measures of distribution difference.

</details>

**尚未挂出 arXiv（待核验）**
- MPCI-Bench: Multimodal Pairwise Contextual Integrity Privacy Evaluation of Language Model Agents
- Don't Deploy Fine-Tuned Genomic Foundation Models Without Privacy Evaluation
- Benchmarking Membership Privacy Risks in Preference-Based LLM Post-Training
- Local FDR Membership Inference Attacks
- Evaluating an Evaluation: Membership Inference Attacks as Machine Unlearning Diagnostics
- Lethe: Link Inference Attacks For Evaluation of Edge Unlearning Methods
- ShadowBench: Exposing Lexical Anchoring and the Illusion of Forgetting
- KNOT: A Knowledge Entanglement Benchmark for Robust Unlearning Evaluation
- METAFORGET: Audit-Driven Update-Policy Learning for Reliable LLM Unlearning
- Unlearning That Lasts: Utility-Preserving, Robust, and Almost Irreversible Forgetting
- Individual-Level Unlearning in Vision-Language Models（已库内，0929 What Does It Mean to Forget a Person 同族待核）

### 水印、溯源与内容真实性

### 216. A Retained-Signal Interface for LLM Watermark Robustness under Paraphrase

📝 [OpenReview](https://openreview.net/forum?id=4sTuTf9CyC) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`evaluation`、`watermark robustness`、`paraphrase`、`kl divergence`、`audit interface`
- 🎯 **研究动机**：水印抗改写鲁棒性通常以对某个具名改写器的 AUC 汇报，结果难以跨水印方案、改写器与检测器比较。
- 🔬 **研究方法**：提出保留信号报告接口——水印注入 KL 信号 Δ、改写信道保留比例 ρ，则任何检测器改写后的优势受 Δρ 控制，给出 Pinsker 与 Bretagnolle-Huber 阈值律并证明 Θ(√(Δρ)) 速率对任何仅依赖 (Δ,ρ) 的 converse 是锐利的，再实例化为得分投影审计，把 Δρ 估计与语义保持、检测器投影一并报告。
- 📌 **结论**：在 KGW/Unigram × Qwen/Llama 基准上，该得分有效信号跨长度、强度与改写器族预测改写后 AUC，以可复现鲁棒性报告取代一次性 AUC 表。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Watermark robustness under paraphrase is usually reported as AUC against a named rewriter, making results hard to compare across watermark schemes, paraphrasers, and detectors. We propose a retained-signal reporting interface: if a watermark injects KL signal \Delta=\KL(P_1\Vert P_0) and a paraphrase channel retains KL fraction \rho, then any detector's post-paraphrase advantage is controlled by \Delta\rho. We give explicit Pinsker and Bretagnolle--Huber threshold laws, prove the \Theta(\sqrt\Delta\rho) rate is sharp for any (\Delta,\rho)-only converse, and show the bound is implementation-blind once watermark families are matched by \Delta. For real LLM paraphrases, we instantiate the interface as a score-projected audit that estimates \widehat\Delta\widehat\rho for a deployed detector and reports it with semantic preservation and the detector projection. In a KGW/Unigram × Qwen/Llama benchmark, this score-effective signal predicts post-paraphrase AUC across lengths, strengths, and paraphraser families. The resulting protocol separates injected signal, retained signal, semantic quality, and detector choice, replacing one-off AUC tables with a reproducible robustness report.

</details>

### 217. Multi-bit LLM Watermarking with Certified Semantic Distortion

📝 [OpenReview](https://openreview.net/forum?id=wB0DVBkk59) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`watermark`、`multi-bit`、`certified distortion`、`llm`、`kl bound`
- 🎯 **研究动机**：多比特水印可嵌入丰富元数据，但统计可检测性与文本质量存在固有权衡，且现有方案缺乏理论质量保证、面临无界语义失真风险。
- 🔬 **研究方法**：提出首个带认证语义失真界的多比特水印框架 CSD，推导 KL 散度闭式上界、在每一步生成时数学上严格限制语义失真，并以动态载荷替代静态载荷最大化统计可检测性。
- 📌 **结论**：多数据集实验表明 CSD 在保持可证明安全文本生成的同时实现稳健的可检测性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Watermarking has emerged as a fundamental mechanism for tracing the provenance of Large Language Model (LLM) outputs. While multi-bit watermarks are highly desirable for embedding rich metadata, they suffer from an inherent trade-off between statistical detectability and text quality degradation. Crucially, existing multi-bit schemes lack theoretical quality guarantees, leaving them susceptible to unbounded semantic distortion. To address this, we introduce CSD, the first multi-bit watermarking framework with certified semantic distortion bounds. In CSD, we derive a closed-form upper bound on the Kullback-Leibler (KL) divergence, mathematically guaranteeing strict limits on semantic distortion at every generation step. Furthermore, rather than relying on static payloads, CSD employs a dynamic payload to maximize statistical detectability. Extensive empirical evaluations across multiple datasets demonstrate that CSD achieves robust detectability while maintaining provably safe text generation.

</details>

### 218. SCTI: Self-Calibrated Trident Identification of Black-Box LLM Watermarks

📝 [OpenReview](https://openreview.net/forum?id=sSXd2zEa4O) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`detection`、`watermark identification`、`black-box`、`empirical null`、`llm auditing`
- 🎯 **研究动机**：黑箱水印 LLM 识别无法访问 logits、检测密钥、模型参数与水印内部设置，现有方法用固定零参考作基线（对提示对、模型与采样配置敏感而易误判），且需为不同水印族分别设计统计特征与判据，难以应对未知水印算法。
- 🔬 **研究方法**：提出自校准三叉识别框架 SCTI——从查询响应构造经验零分布以估计可泛化参考、替代固定参考，并以 Trident-View 一致性度量机制实现统一管线，免去逐水印族设计独立检验。
- 📌 **结论**：跨多个 LLM 与多种水印算法的实验验证 SCTI 优于代表性黑箱水印识别基线。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Black-box watermarked LLM identification has become an important task for watermark auditing. The core challenge arises from inherent black-box constraints that deny access to logits, detector keys, model parameters, and internal watermark settings. For this reason, existing methods have not conducted in-depth exploration on this task, leaving prominent limitations: . First, existing works use fixed null reference to serve as a baseline for judging the presence of watermarks in LLM outputs, which might misidentify a watermarked LLM as unwatermarked because the null reference is sensitive to the prompt pair, queried model, and sampling configuration. Second, existing statistical-tests based methods adopt distinct statistical features and judgment criteria for different LLM watermark families, making them less suitable when the deployed watermark algorithm is unknown. To remedy the above two limitations, this work proposes , a Self-Calibrated Trident Identification framework for black-box watermarked LLM identification. Specifically, to handle the first limitation, constructs empirical null distributions from the queried responses to estimate the generalizable reference instead of relying on a fixed reference. Meanwhile, to address the second limitation, is configured with a Trident-View Consistency measuring mechanism, which enables a unified pipeline to avoid designing separate tests for individual watermark family. Experimental results verify that outperforms representative black-box watermark identification baselines across diverse LLMs and watermark algorithms.

</details>

### 219. Invisible Ink, Visible Lies: How Production Watermarking Causes LLMs to Hallucinate

📝 [OpenReview](https://openreview.net/forum?id=TwmIdwMjZ8) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`analysis`、`watermark hallucination`、`factuality`、`rag`、`token intervention`
- 🎯 **研究动机**：文本水印对事实可靠性的影响鲜有研究——即便证据就在上下文中且未加水印的模型能答对，水印仍可能引发或放大事实错误。
- 🔬 **研究方法**：在受控 RAG 设置下对照配对的有/无水印生成，覆盖 KGW、SWEET、DiPmark、GumbelSoft、Gumbel-Max 与 SynthID 式水印，将失效归因于抑制事实一致 token 的直接 token 级偏置与自回归解码中累积、削弱后续对事实上下文注意的前缀诱导漂移两机制，并提出即插即用干预 FPTI 与 FPAI。
- 📌 **结论**：组合 FPTI 与 FPAI 可缓解约 90% 的水印诱发幻觉，同时保持流畅度与相当的解码效率。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text watermarking helps identify AI-generated content, but its effect on factual reliability remains underexplored. In this paper, we study watermarking hallucination: factual errors induced or amplified by watermarking even when the required evidence is present in the context and the unwatermarked model can answer correctly. Using a controlled RAG setting, we compare paired unwatermarked and watermarked generations under the same condition. Across representative watermarking methods, including KGW, SWEET, DiPmark, GumbelSoft, Gumbel-Max, and SynthID-style watermarking, we find that watermarking hallucination is widespread: watermarked outputs can remain fluent while introducing factual errors. We attribute this failure mode to two mechanisms: (1) direct token-level bias, which can suppress fact-consistent tokens, and (2) prefix-induced drift, which accumulates through autoregressive decoding and weakens later attention to factual context. Motivated by this analysis, we propose Fact-Preserving Token Intervention (FPTI) and Fact-Preserving Attention Intervention (FPAI), two plug-in interventions that can be integrated into existing watermarking methods to improve factuality. Our experiments show that combining FPTI and FPAI mitigates around 90% of watermark-induced hallucinations while preserving fluency and comparable decoding efficiency. Overall, this work highlights factuality as a first-class criterion in watermark evaluation, alongside detectability and robustness, and calls for careful factuality validation before deploying watermarks in fact-critical applications.

</details>

### 220. Beyond Bit Matching: Orthogonal Watermarks for Collusion-Resistant Image Fingerprinting

📝 [OpenReview](https://openreview.net/forum?id=wwfGrsZBIz) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`watermark`、`image fingerprinting`、`collusion resistance`、`orthogonal key`、`traitor tracing`
- 🎯 **研究动机**：图像指纹为每份分发副本嵌入用户专属水印以溯源，平均合谋可压制各份标记，离散比特串水印因平均化把比特证据推向模糊判决而尤其脆弱。
- 🔬 **研究方法**：提出 OrthoMark，把用户密钥映射为近正交高维单位向量并以提取水印方向的余弦相似度识别合谋者——K 个向量密钥理想平均下每个合谋者保留 1/√K 量级归一化余弦信号，随机方向的球面几何给出移位 Beta 零分布以解析控制逐密钥误检率；配合 JND 掩码与渐进课程训练的神经编码器和居中提取器。
- 📌 **结论**：在 MS-COCO、OpenImages 与 AI 生成图像上，光度几何畸变下保持稳健单密钥检测，严格全合谋者检测居所有评测方法最佳且视觉质量高。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Image fingerprinting assigns each distributed copy a user-specific watermark for source tracing. Averaging collusion is a central threat: several recipients can average their differently marked copies to suppress each individual mark. Discrete bit-string watermarks are especially vulnerable because averaging drives bit evidence toward ambiguous decisions. We introduce OrthoMark, which maps user keys to near-orthogonal high-dimensional unit vectors and identifies colluders by cosine similarity to the extracted watermark direction. Under ideal averaging of K vector keys, the normalized average preserves a cosine signal of order 1/\sqrtK for each colluder, while unrelated keys remain concentrated near zero. The spherical geometry of random directions gives a shifted-Beta null distribution for cosine similarities, enabling analytic per-key false-positive-rate control after validation on unwatermarked images. OrthoMark uses a neural watermark encoder and centered extractor trained with JND masking and a progressive curriculum for photometric, geometric, and collusion robustness. Experiments on MS-COCO, OpenImages, and AI-generated images show that OrthoMark maintains robust single-key detection under photometric and geometric distortions, and achieves the best strict all-colluder detection among evaluated methods, while preserving high visual quality.

</details>

### 221. CLaW: Codec-Guided Adaptive Latent Watermarking for Traceable Diffusion Image Generation

📝 [OpenReview](https://openreview.net/forum?id=nI6z2amVXh) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`watermark`、`diffusion model`、`latent injection`、`adaptive strength`、`traceability`
- 🎯 **研究动机**：现有可溯源扩散图像水印难以规模化部署——模型重训练或检测成本高、有效性-保真权衡差、对图像变换鲁棒性有限。
- 🔬 **研究方法**：提出 CLaW，用预训练水印编解码器把消息映射为潜残差以实现低成本采样时注入，在语义保持更好、水印信号受后续去噪扰动更小的晚期去噪窗口内注入，并以解码置信度为反馈自适应校准水印强度、强化弱信号，扩散骨干冻结且检测免反演。
- 📌 **结论**：大量实验表明 CLaW 在保持视觉保真的同时提升图像变换下的平均 F1，较现有最优方法提高 6.34%。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid advancement of text-to-image diffusion models, increasingly realistic AI-generated content has raised serious concerns about misuse and copyright infringement. Digital watermarking offers a promising solution by enabling user-level traceability, yet existing methods remain difficult to deploy at scale, hindered by costly model retraining or detection, poor effectiveness–fidelity trade-offs, and limited robustness to image transformations. To address these challenges, we propose CLaW (Codec-guided Latent Watermarking), a robust and efficient watermarking framework for traceable diffusion image generation with frozen diffusion backbones and inversion-free detection. Specifically, CLaW first uses a pretrained watermark codec to map each watermark message to a latent residual, enabling low-cost sampling-time injection. Then, the residual is injected within a late denoising window, where image semantics are better preserved and the watermark signal is less perturbed by subsequent denoising updates, yielding a better balance between watermark effectiveness and image fidelity. Furthermore, we introduce a decoder-guided adaptive injection mechanism that uses decoding confidence as feedback to dynamically calibrate watermark strength, reinforcing weak watermark signals and improving robustness under image transformations. Extensive experiments show that CLaW can preserve visual fidelity and improve average F1 under image transformations, achieving a 6.34% gain over the state of the art.

</details>

### 222. TIDE: Trajectory-Aware Watermark Propagation for Text-to-Image Diffusion Models

📝 [OpenReview](https://openreview.net/forum?id=1tohGAfGuc) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`watermark`、`text-to-image`、`denoising trajectory`、`guidance redirection`、`partial inversion`
- 🎯 **研究动机**：扩散水印多把信号注入初始噪声或固定中间潜变量，不控制其在剩余去噪步中的演化，使水印保持与文本引导生成纠缠，有验证变弱或内容保真受损之虞。
- 🔬 **研究方法**：提出 TIDE，将可学习水印注入中间潜变量并与辅助水印条件联合优化，用保持与检测目标约束其偏离未水印参照；采样时估计近期文本引导方向、把水印引导重定向到与局部文本子空间对齐较低的残差分量，验证时用零提示部分反演恢复注入潜变量并匹配其掩码系数。
- 📌 **结论**：在未攻击图像上验证可靠、常见攻击下鲁棒性提升，并更好保持语义与视觉保真。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Watermarking text-to-image diffusion models provides a practical mechanism for provenance tracking and responsible deployment. Post-processing methods are easy to deploy but vulnerable to image-space transformations. In-processing methods improve robustness by embedding the watermark within the denoising trajectory. Yet most existing methods inject the signal into the initial noise or a fixed intermediate latent, without controlling how it evolves during the remaining denoising steps. This can entangle watermark preservation with text-guided generation, risking weaker verification or degraded content fidelity. We propose TIDE, a trajectory-aware watermarking method for text-to-image diffusion models. TIDE injects a learnable watermark into an intermediate latent and jointly optimizes it with an auxiliary watermark condition, using preservation and detection objectives to limit deviation from the unwatermarked reference while maintaining separable watermark evidence. During sampling, TIDE estimates recent text-guidance directions and redirects watermark guidance toward the residual component less aligned with this local text subspace, reducing avoidable interference with semantic generation. Verification uses null-prompt partial inversion to recover the injection latent and match its masked coefficients to the target watermark. Experiments show that TIDE achieves reliable verification on unattacked images, improves robustness under common attacks, and better preserves semantic and visual fidelity.

</details>

### 223. FiLM-CAM: Keyed Feature Modulation for Conditional-Access Watermarking

📝 [OpenReview](https://openreview.net/forum?id=1b70GKuMjn) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`watermark`、`conditional access`、`keyed modulation`、`image watermarking`、`feature-level coupling`
- 🎯 **研究动机**：图像水印缺乏条件访问控制——需要确保只有持有密钥的授权方才能编码、解码与移除水印。
- 🔬 **研究方法**：提出 FiLM-CAM，密钥条件化 Feature-wise Linear Modulation 在特征级（而非像素级）变换并嵌入水印信号，使载荷与密钥耦合、同一密钥才能条件化解码器正确恢复载荷；训练最大化授权与非授权使用的性能差距，并让编码器估计对既有水印不变的残差，支持密钥掌控下经迭代精化的重编码-相减式移除。
- 📌 **结论**：跨多种水印编码-解码骨干的评估表明，密钥特征调制是有效且架构无关的条件访问模块（CAM）。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We propose FiLM-CAM; a conditional-access image watermarking approach that enforces authorized encoding, decoding, and removal through keyed feature modulation. A secret key conditions a Feature-wise Linear Modulation (FiLM) mechanism that transforms the internal representation of the watermark signal before embedding, thereby coupling the payload to the key at the feature, rather than pixel level. The same key must be presented to condition the decoder to correctly recover the payload embedded in an image. To enforce conditional access, we train the system to maximize the performance gap between authorized and unauthorized use, ensuring reliable extraction under the correct key while inducing failure under incorrect keys. In addition, we design our encoder to estimate the watermark residual invariant to the presence of pre-existing watermarks. This design enables conditional watermark removal via simple re-encoding and subtraction of the residual using iterative refinement, contingent on knowledge of the secret key. We evaluate FiLM-CAM across multiple watermarking encoder–decoder backbones, demonstrating that keyed feature modulation serves as an effective, architecture-agnostic conditional access module (CAM) for image watermarking.

</details>

### 224. FedTrace: Generated-Content-Based Watermark Verification for Traitor Tracing in Federated Learning

📝 [OpenReview](https://openreview.net/forum?id=ynVmgUSGjZ) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`watermark`、`traitor tracing`、`federated learning`、`generated content`、`collusion`
- 🎯 **研究动机**：联邦学习定制生成模型时，恶意客户端可复制下发的 adapter 离线使用并变现生成图像而不暴露被盗权重或可查询服务，现有联邦水印与叛徒追踪却依赖对可疑权重的白箱访问或对部署模型的黑箱查询。
- 🔬 **研究方法**：提出仅凭已流传可疑生成图像归因泄露联邦模型的 FedTrace：轮次化水印生命周期把客户端身份分布与全局效用聚合分离，低漂移可靠比特载体把身份嵌入本地适应下稳定的水印位置，反碰撞编码与软子集验证区分单点与合谋泄露。
- 📌 **结论**：跨定制扩散数据集、基模型与联邦设置的实验表明，本地适应下仍保持可检测的客户端身份，并强化了针对合谋泄露的子集感知追踪。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large generative models become widely deployed and customized, federated learning is increasingly used to adapt them while keeping user data local. Because clients repeatedly receive up-to-date adapters, a malicious client can copy a dispatched adapter, use it offline, and monetize generated images without exposing the stolen weights or a queryable service. Existing federated watermarking and traitor-tracing methods usually assume white-box access to suspect weights or black-box query access to the deployed model. In realistic generative-model theft, however, the defender may only observe images that have already circulated. We propose \emphFedTrace, a generated-content-based watermark verification framework that attributes leaked federated models from suspicious generated images alone. FedTrace couples three designs: a round-wise watermark lifecycle that separates client identity distribution from global utility aggregation, a low-drift reliable-bit carrier that embeds identity in watermark positions stable under local adaptation, and anti-collision coding with soft subset verification for distinguishing singleton and collusive leakage. These components enable post-local, collusion-aware attribution from generated outputs alone, without suspect weights or online query interfaces. Extensive experiments across customized diffusion datasets, base models, and federated settings show that FedTrace preserves detectable client identities under local adaptation and strengthens subset-aware tracing against collusive leakage.

</details>

### 225. PrivateSeal: Low-Sensitivity Latent Directions for Diffusion-Resilient User-Specific Watermarking

📝 [OpenReview](https://openreview.net/forum?id=BrU1KQABN9) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`watermark`、`diffusion regeneration`、`latent direction`、`user-specific key`、`ownership attribution`
- 🎯 **研究动机**：扩散编辑与再生普及后，给已有图像嵌入不可感知且可验证的信号用于归属与溯源，需同时满足抗扩散变换鲁棒性、低成本验证和低开销按用户分配密钥三点，现有方法无法兼得。
- 🔬 **研究方法**：提出 PrivateSeal，把扰动约束在低敏感潜方向上使嵌入信号不易在扩散编辑或再生中被抹除，验证时用对应密钥经简单潜空间投影可靠恢复消息，平台可为不同用户、账户或图像分配独立投影密钥而无需重训或修改验证器。
- 📌 **结论**：在 W-Bench 上对扩散再生与编辑保持有竞争力的鲁棒性，跨模型与跨数据集评估进一步验证其强迁移性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion-driven image editing and regeneration are becoming increasingly widespread. This creates an urgent need for watermarking methods that can embed imperceptible yet verifiable signals into existing images for ownership attribution and provenance tracking. Existing methods fail to simultaneously satisfy three practical requirements: robustness against diffusion-based transformations, low-cost verification, and scalable support for per-user key assignment at low overhead. To address these challenges, we propose PrivateSeal, a watermarking framework for pre-existing images under diffusion-based transformations. The perturbation is encouraged to lie along low-sensitivity latent directions, so that the embedded signal is less likely to be suppressed during diffusion-based editing or regeneration. During verification, the embedded message is reliably recovered via a simple latent-space projection using the corresponding key. This design allows a platform to assign independent projection keys to different users, accounts, or images without retraining or modifying the verifier, while maintaining low-cost verification. Extensive experiments on the W-Bench benchmark show that PrivateSeal achieves competitive robustness against diffusion-based regeneration and editing, with additional cross-model and cross-dataset evaluations further validating its strong transferability.

</details>

### 226. PP-Mark: Provable and Publicly Verifiable Watermarking for Generative AI

📝 [OpenReview](https://openreview.net/forum?id=yPgHWlPwFl) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`watermark`、`public verifiability`、`zero-knowledge proof`、`unforgeability`、`provenance`
- 🎯 **研究动机**：生成模型产出的图像已与真实数据不可区分，公开可验证的溯源不可或缺，但水印检测器一旦公开，现有方法便易受伪造与对抗优化攻击。
- 🔬 **研究方法**：提出 PP-Mark，把轻量统计检测锚定在嵌入过程的零知识证明上，从构造上保证伪造内容无法通过完整验证，并在标准密码学假设下建立形式化不可伪造性。
- 📌 **结论**：在两种架构上对抗黑箱印记伪造、白箱优化与再生攻击均展现抵抗力，同时保持去中心化验证的实用性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generative AI models now produce images indistinguishable from real data, making publicly verifiable provenance essential; however, existing watermarking methods become vulnerable to forgeries and adversarial optimization attacks once their detectors are made public. We propose PP-Mark, a provenance framework that anchors lightweight statistical detection to a zero-knowledge proof of the embedding process, ensuring that forged content cannot pass full verification by construction. We establish formal unforgeability under standard cryptographic assumptions and validate PP-Mark against representative baselines across two architectures, demonstrating resistance to black-box imprint forgery, white-box optimization, and regeneration attacks while remaining practical for decentralized verification.

</details>

### 227. Watermarking as a Learned Intrinsic Property of Diffusion Models

📝 [OpenReview](https://openreview.net/forum?id=v26DCJujUa) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`watermark`、`diffusion model`、`ip protection`、`model distribution`
- 🎯 **研究动机**：模型分发场景下下游用户可任意修改扩散模型，现有水印依赖推理时输入控制或辅助组件而易被移除，无法保护知识产权。
- 🔬 **研究方法**：提出 INMARK，让核心去噪网络自身学习并复现水印模式，将水印内化为模型固有属性，且完全兼容标准扩散训练流程。
- 📌 **结论**：实验表明 INMARK 兼具高生成保真度、高水印可检测性与强抗攻击鲁棒性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in latent diffusion models have enabled high-quality image generation, but also raise critical concerns for intellectual property protection in model distribution scenarios, where downstream users have unrestricted access to models, allowing arbitrary modifications. Existing watermarking methods either rely on inference-time control of inputs (e.g., specific prompts or noise initialization) or embed watermark signals in auxiliary components, making them easily removable in such settings. In this paper, we propose INMARK, which treats watermarking as an intrinsic property learned by the model. Instead of relying on input control or auxiliary watermarking components, INMARK enables the core denoising network to internalize and reproduce watermark patterns. Extensive experiments demonstrate that INMARK achieves strong generation fidelity, high watermark detectability, and robustness against attacks, while remaining fully compatible with standard diffusion training pipelines. Our results highlight a new perspective on diffusion model watermarking: the denoising network can learn a reliable and persistent watermarking capability, which is crucial in practical model distribution scenarios.

</details>

### 228. Brute-Force Jailbreaks and Codon-Aware Watermarking for DNA Foundation Models

📝 [OpenReview](https://openreview.net/forum?id=6JUgH59aJ1) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`defense`、`dna foundation model`、`codon`、`watermark`
- 🎯 **研究动机**：开源 DNA 基础模型（如 Evo2）在无领域知识、无提示工程、无内部访问的纯暴力采样下即可生成与已知人类致病病毒 ≥90% 局部核苷酸同源的序列，说明误用瓶颈在模型先验而非攻击者水平，防御必须落在攻击所在的密码子层。
- 🔬 **研究方法**：先刻画暴力 Best-of-N 越狱攻击并分析生成（非记忆、摆动位置同义替换率 63.6%），再提出零训练溯源水印 WobbleGuard，将遗传密码的已知同义结构纳入检测打分规则。
- 📌 **结论**：7B 上暴力采样平均攻破 JailbreakDNABench 的 9.5/23（41%）种致病病毒（1B 为 12/23、52%）；WobbleGuard 在全同义密码子替换下保留 95.5% TPR（核苷酸级 KGW 移植此时约 0%），并以 100% 检出 1B 与 7B 的未扰动水印生成。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-source DNA foundation models such as Evo2 generate sequences with \geq 90% local nucleotide identity to known human-pathogenic viruses under brute-force sampling alone, with no domain expertise, prompt engineering, or access to model internals. The bottleneck for biological misuse is therefore the model's prior, not the attacker's sophistication, and a deployable defense must operate where the attack does: at the codon layer. First, we characterize the attack. On JailbreakDNABench's 23 pathogenic viruses, brute-force Best-of-N sampling against Evo2 succeeds for a mean of 9.5/23 viruses at 7B across two independent trials (41%, range 39.1%\!-\!43.5%, matching GeneBreaker's three-component engineered jailbreak pipeline at 36%) and 12/23 at 1B (52%, single curated trial, ～\!6× GeneBreaker's reported 9%), without any guided search or learned attack model. Probing Evo2's outputs, we find generations are not memorized: 0/11 appear verbatim in NCBI nt, 0/11 recall a single strain cleanly, and codon-position mismatches are biologically structured rather than random (\chi^2(2) = 50.37, p < 10^-4; wobble-position synonymous rate 63.6%, near the per-virus codon-usage baseline and well above the 25% uniform-mutation null). Verbatim or near-verbatim training-data filtering would therefore not have prevented these generations. Second, we present a deployment-time defense. Because the attack exploits codon-level wobble structure, the defense must too. WobbleGuard is a zero-training provenance scheme whose contribution at the detection layer folds the genetic code's known synonym structure into the scoring rule. At an in-sample-calibrated threshold (1.00% FPR by construction on 22,982 natural NCBI pathogen fragments, \alpha = 0.01; cross-key range 0.30%\!-\!1.24% over 8 independently sampled keys), the composite detector \max(z_v, z_w) retains 95.5% TPR under full synonymous codon substitution, the regime in which a nucleotide-level KGW port collapses to ～0% TPR, and detects 100% of unperturbed watermarked Evo2 generations at both 1B and 7B scales. The attack works because brute force suffices; the defense works because it speaks codons.

</details>

### 229. Face Deepfake-aware Recovery via Semantic-driven Facial Representation-based Watermarking

📝 [OpenReview](https://openreview.net/forum?id=SqHbIQuLi6) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`watermark`、`face recovery`、`semantic encoding`、`deepfake`、`identity preservation`
- 🎯 **研究动机**：现有图像水印将视觉内容与空间结构纠缠，对几何变换和对齐偏差高度敏感，在 deepfake 篡改下尤甚。
- 🔬 **研究方法**：提出语义驱动的人脸水印框架，将身份语义与空间布局解耦：把人脸分解为语义组件、把深层特征聚合为组件级潜在表示，经独立码本量化为紧凑比特流嵌入，解码后重建身份一致的面部内容。
- 📌 **结论**：在 CelebA-HQ 与 FFHQ 上，光照与几何攻击下的重建质量、身份保持和检索精度均显著优于现有水印方法。

👤 **作者**：Yuan-Chih Chen、Chun-Shien Lu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing image watermarking methods typically entangle visual content with spatial structure, making them highly sensitive to geometric transformations and alignment discrepancies, especially in the presence of deepfake manipulations. In this paper, we propose a semantic-driven facial watermarking framework for robust identity recovery. The key idea is to decouple identity-related semantic information from spatial layout and encode it into a compact and spatially robust semantic representation. Specifically, we decompose a face into semantic components and aggregate deep features into component-wise latent representations, which are quantized via independent codebooks and converted into a compact bitstream for embedding. After decoding, the embedded semantic information is recovered and used to reconstruct identity-consistent facial content, even under slight geometric distortions and tampering. Experiments on CelebA-HQ and FFHQ demonstrate that our method significantly outperforms existing watermarking approaches in terms of reconstruction quality, identity preservation, and retrieval accuracy under both photometric and geometric attacks, validating the effectiveness of semantic component-wise encoding for reliable face recovery.

</details>

### 230. Robust and Hard-to-Remove GNN Watermarking via Topological Invariant Perception

📝 [OpenReview](https://openreview.net/forum?id=SXZrjQXtkB) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`watermark`、`graph neural network`、`ownership verification`、`graph invariant`、`trigger-free`
- 🎯 **研究动机**：GNN 水印现有方案依赖 OOD 后门触发器，易被模型剪枝、微调与蒸馏移除。
- 🔬 **研究方法**：提出 InvGNN-WM，将所有权绑定到模型对图不变量（归一化代数连通度）的隐式感知：在所有者私钥载体图上训练标量预测头，把所有权嵌入模型核心推理逻辑，实现无触发器黑盒验证；并给出不可感知性与鲁棒性保证、证明单调解码器下精确移除是 NP 完全。
- 📌 **结论**：在多样节点/图分类数据集上保持干净任务精度并超越触发器与解释类基线的水印保真度，在无结构剪枝、微调与训练后量化下保持鲁棒。

👤 **作者**：JIPENG LI、Yanning Shen

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Graph Neural Networks (GNNs) represent valuable intellectual property, yet existing watermarking schemes primarily rely on OOD backdoor triggers that are susceptible to model pruning, fine-tuning, and distillation. To tackle this challenge, we present InvGNN-WM, which ties ownership to a model's implicit perception of a graph invariant, enabling trigger-free, black-box verification with negligible task impact. By training a scalar head to predict normalized algebraic connectivity on owner-private carrier graphs, ownership is embedded into the model's core reasoning logic rather than exogenous patterns. We provide guarantees for imperceptibility and robustness, and prove that exact removal is NP-complete under monotone decoders. Empirical evaluations across diverse node and graph classification datasets show that InvGNN-WM maintains clean task accuracy while outperforming trigger- and explanation-based baselines in watermark fidelity. Our method remains robust under unstructured pruning, fine-tuning, and post-training quantization, with clear recovery pathways under knowledge distillation.

</details>

### 231. RISE: Red-teaming via Iterative Strategy Evolution for Modern Text-to-Image Models

📝 [OpenReview](https://openreview.net/forum?id=gOoC1Kh4q4) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`red-teaming`、`text-to-image`、`strategy evolution`、`calibrated evaluation`
- 🎯 **研究动机**：现代生产级 T2I 系统上策略违规罕见且旧种子提示多被修补，现有自动红队存在两大错配：模糊不安全目标下评判器不可靠，以及提示修改式管线探索能力不足。
- 🔬 **研究方法**：定义严格的类别专属成功标准并对强 VLM 评判器按人类标签校准；提出 RISE，演化用于生成提示的可复用策略而非逐条改写提示，最优策略可复用于新场景。
- 📌 **结论**：在 DALL·E 3、Nano Banana 2 与 GPT-Image-2 上达最高 13% 人工核验 ASR；同一校准评估下，此前报告约 30% ASR 的方法跌至近零。

👤 **作者**：Dmitrii Kharlapenko、Sergei Bratchikov、Konstantin Korolev、Aleksandr Nikolich

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

On modern production text-to-image systems, successful policy violations are rare, and previously effective human-written seeds are often patched out. Current automated red-teamers are poorly matched to this regime in two ways: unreliable success measurement and poor exploration. First, we find that judges widely used in prior T2I red-teaming work are unreliable under vague unsafe-content targets: they either miss true violations or reward benign borderline images on hardened APIs. We therefore define strict category-specific success criteria and calibrate strong VLM judges against human labels. Second, we show that broadly used prompt-modification pipelines do not solve the exploration problem: on harder guardrail settings they remain tied to seed prompts, fail to transfer, or cannot bootstrap positive examples. We introduce RISE, which evolves reusable strategies used to generate prompts rather than rewriting them one by one. The best discovered strategies are then reused to generate attacks across new scenarios. On DALL·E 3, Nano Banana 2 (Google) and GPT-Image-2, RISE reaches up to 13% human-verified ASR; under the same calibrated evaluation, prior methods with reported ASR as high as roughly 30% fall to near zero.

</details>

### 232. MUTE: Multi-Level Alignment Uncoupling Against Talking-Head Exploitation for Voice Protection

📝 [OpenReview](https://openreview.net/forum?id=AlHi8J4Z6I) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`talking-head deepfake`、`audio protection`、`audio-visual alignment`、`stft perturbation`
- 🎯 **研究动机**：talking-head 生成模型日益被多模态 deepfake 滥用，其根本依赖精确的音视频对齐，而有效的音频保护方法研究严重不足。
- 🔬 **研究方法**：提出多级解耦音频保护框架 MUTE：表示级退化扰动时序音频嵌入、对齐级破坏扰动跨模态注意力以瓦解结构对齐；扰动约束在 STFT 域高能量区以抗后处理与去噪，可选说话人级目标缓解 TTS 重合成绕过。
- 📌 **结论**：在白盒与黑盒 talking-head 模型上一致降低唇同步质量并保持感知音质，真实世界变换下仍有效，且可与图像侧方法组合实现更强多模态保护。

👤 **作者**：Donghyun Kim、Jin Hong、seungmin Kim、Dain Kim、Junseok Kwon、Daeseon Choi

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Talking-head generation models, which synthesize realistic facial animations from audio, are increasingly vulnerable to misuse in multimodal deepfake scenarios. Protecting such systems remains challenging, as talking-head models fundamentally rely on precise audio–visual alignment, while effective audio protection methods remain largely underexplored. In this work, we propose MUTE, an audio protection framework that uncouples the underlying audio–visual alignment through a multi-level strategy. Specifically, MUTE combines (1) Representation-level Degradation, which perturbs temporal audio embeddings to degrade their representations, and (2) Alignment-level Disruption, which directly perturbs cross-modal attention to disrupt structural alignment. To improve robustness, perturbations are constrained in the STFT domain to high-energy regions, making them resistant to post-processing and denoising. An optional speaker-level objective further mitigates potential bypass via TTS-based resynthesis. Extensive experiments demonstrate that MUTE consistently degrades lip synchronization across both white-box and black-box talking-head models while preserving perceptual audio quality. The proposed method remains effective under real-world transformations and can be combined with image-based approaches to provide stronger multimodal protection.

</details>

### 233. Keep It CALM: Analyzing the Limits of Global Unsafety in Text-to-Image Generation

📝 [OpenReview](https://openreview.net/forum?id=VjTAXEfv0N) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`text-to-image`、`unsafe content`、`counterfactual correction`、`local modulation`
- 🎯 **研究动机**：免训练 T2I 安全方案依赖跨 prompt 复用的全局 unsafe 方向/子空间，受控几何分析揭示其存在覆盖-选择性权衡：紧凑子空间盖不住异质 unsafe 语义，聚合过宽则扭曲安全邻近的良性 prompt。
- 🔬 **研究方法**：提出 CALM（Counterfactual Adaptive Local Modulation），用匹配的 unsafe-benign 锚点把每个 prompt 路由到活跃的 unsafe 类别，仅对违规 token 表示做朝安全侧的最小编辑，并抑制正向对齐的 unsafe 残差分量。
- 📌 **结论**：广泛评测中 CALM 在保持良性效用的同时提升不良内容抑制，证明局部反事实校正是比全局 unsafe 信号移除更具选择性的替代方案。

👤 **作者**：NaHyeon Park、Minhyun Lee、Hyunjung Shim

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Training-free safeguards for text-to-image diffusion models often rely on a reusable safety signal, such as an unsafe direction or global toxic subspace, applied broadly across prompts. We provide a controlled geometric analysis of this global-unsafety assumption and reveal a consistent coverage-selectivity trade-off: compact unsafe subspaces fail to cover heterogeneous unsafe semantics, whereas broader aggregation increasingly distorts safety-adjacent benign prompts. Motivated by this finding, we propose CALM (Counterfactual Adaptive Local Modulation), a training-free safeguard that replaces uniform global removal with prompt-local counterfactual correction. Using matched unsafe-benign anchors, CALM routes each prompt to active unsafe categories, minimally edits only violating token representations toward the safe side, and suppresses positively aligned unsafe residual components. Across broad evaluation, CALM improves unsafe-content suppression while preserving benign utility, demonstrating that local counterfactual correction provides a more selective alternative to global unsafe-signal removal.

</details>

### 234. AuxMark: Defending Against Unauthorized Agent Distillation via Auxiliary Behavioral Watermarking（已库内，0929）

📄 [arXiv](https://arxiv.org/abs/2609.34597) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`watermark`、`agent distillation`、`behavioral watermarking`、`attribution`、`black-box audit`
- 🎯 **研究动机**：LLM agent 轨迹可被非法收集蒸馏出学生 agent，现有水印要么不适配结构化交互的 agent 环境要么跨任务/架构不可靠。
- 🔬 **研究方法**：AuxMark 在教师轨迹中动态插入安全无害的非必要辅助动作并留存上下文为私有证据卡，审计时由证据卡构造真假配对探针并做卡级符号检验，实现模型级检测与轨迹级溯源。
- 📌 **结论**：在 3 个 agent 基准、2 个教师与 4 种学生架构上检出全部 24 个蒸馏模型且 48 个干净模型零误报，并抗数据灌水、改写、截断与自适应清洗攻击。

👤 **作者**：Yiqing Feng、…、Mingxun Zhou

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model agents can acquire complex capabilities through multi-step interaction and tool use, but their trajectories can also be illegally collected to dis- till student agents. However, existing watermarking methods either do not fit the structured and interactive nature of agent environments or lack reliable effective- ness across tasks and model architectures. We introduce AuxMark, a behavioral watermarking framework for tracing unauthorized agent distillation. AuxMark dynamically inserts safe, non-essential auxiliary action into teacher trajectories, and stores the associated contexts as private evidence cards. To audit a suspicious student model, AuxMark constructs paired real and fake probes from these cards and applies a card-level sign test. This black-box protocol supports both model- level detection and trace-level attribution. Across three agent benchmarks, two teacher agents, and four student architectures, AuxMark detects all 24 distilled models with zero false positives on 48 clean models. It also preserves task utility and remains effective against data flooding, paraphrasing, truncation, and adaptive cleaning attacks. Our code will be released at this URL.

</details>

### 235. Auditing Cross-Lingual Fairness in Language Model Watermarking

📄 [arXiv](https://arxiv.org/abs/2608.20047) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-08　🏷 NeurIPS 2026

**关键词**：`evaluation`、`watermarking`、`cross-lingual fairness`、`detection threshold`、`quality metrics`
- 🎯 **研究动机**：LLM 水印几乎只在英文文本上用各方案自身检测阈值与狭窄质量度量评估，多语言部署暴露出在英文上无关紧要却决定跨语言结论的评估设计选择。
- 🔬 **研究方法**：提出四组件评估框架——按部署语境经验校准的检测阈值、区分校准失败与检测失败的阈值无关测量、三种不相交质量度量范式、以及跨类型学家族分区的广义熵差异分解。
- 📌 **结论**：应用于 6 种水印方案、3 个开源生成器、11 种语言（4 种文字、8 个类型学家族）后发现，检测与质量上的跨语言差异主要发生在类型学家族之间，表明水印跨语言公平差距是语言属性结构性的而非个别语言特异。

👤 **作者**：Alexander Nemecek、Osama Zafar、Debargha Ganguly、Vikash Singh、Vipin Chaudhary、Erman Ayday

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Watermarking schemes for large language model output are evaluated almost exclusively on English text using each scheme's detection threshold and a narrow set of quality measurements. Multilingual deployment exposes evaluation-design choices that are inconsequential on English but determine conclusions cross-lingually. We propose an evaluation framework with four components: detection thresholds calibrated empirically per deployment context, a threshold-independent companion measurement that distinguishes calibration failures from detection failures, three disjoint quality measurement paradigms (distributional, paired-semantic, and reference-perplexity), and a generalized-entropy decomposition of cross-language disparity over a typological family partition. Applied to six watermarking schemes, three open-weight generators, eleven languages spanning four scripts and eight typological families, and both base and instruction-tuned regimes, the framework reveals failure modes that single-language single-paradigm evaluation cannot surface. Across detection and quality, observed disparity is predominantly between-family on the typological partition, indicating that cross-lingual fairness gaps in watermarking are structural to language properties rather than idiosyncratic to particular languages.

</details>

### 236. Learning to Follow In-Context Watermark Instructions via Self-Distillation

📄 [arXiv](https://arxiv.org/abs/2608.29030) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-08　🏷 NeurIPS 2026

**关键词**：`watermark`、`in-context watermarking`、`benchmark`、`self-distillation`、`reinforcement learning`
- 🎯 **研究动机**：上下文水印（ICW）通过在查询前拼接指令让模型在回复中嵌入统计可检测信号，使第三方无需模型内部即可调用水印接口，但其可靠性取决于 LLM 能否既遵循指令又不损答案质量，而这一能力从未被测量。
- 🔬 **研究方法**：引入 ICWBench（三个可验证 ICW 指令族，同时评分可检测性与答案质量），对 14 个前沿专有与开源 LLM 的评测显示无一全家族达标；进而提出两阶段训练法——SDLP 自蒸馏（同一基座兼任师生，用指令等价的解码时 logits 扰动让教师遵循 ICW 指令、学生匹配其输出分布）加自动验证器作奖励的 RL。
- 📌 **结论**：应用于 Qwen3-14B 与 GPT-OSS-20B，三种 ICW 指令的平均 TPR@1%FPR 分别从 0.100 升至 0.974、从 0.337 升至 0.968，且在困惑度与 LLM-as-a-Judge 评估下保持高质量回复。

👤 **作者**：Yepeng Liu、Tianyi Chen、Xuandong Zhao、Dawn Song、Yuheng Bu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In-context watermarking (ICW) prepends an instruction to a query asking the model to embed a statistically detectable signal in its response. It thus equips LLMs with a watermarking interface that third parties can invoke without access to model internals. Its reliability hinges on the LLM following the instruction without degrading answer quality, yet how well current LLMs do so has not been measured. We introduce $\mathsf{ICWBench}$, a benchmark of three verifiable ICW instruction families, each scored on both detectability and answer quality. Evaluating 14 frontier proprietary and open-source LLMs, we find that none of the evaluated LLMs achieves both objectives across all three families. To address this, we propose a self-contained two-stage training method, requiring no distillation from a stronger model, no manual annotation, and no pre-existing ICW IF ability. The first stage, self-distillation with logits perturbation (SDLP), uses the same base LLM as both teacher and student: an instruction-equivalent decoding-time logits perturbation makes the teacher follow the ICW instruction, and the student is trained to match the teacher's output distribution. The second stage applies reinforcement learning with the automatic verifier as the reward. Applied to Qwen3-14B and GPT-OSS-20B, our method raises average TPR@$1\%$FPR across three ICW instructions from $0.100$ to $0.974$ and from $0.337$ to $0.968$, respectively, while maintaining high response quality under both perplexity evaluation and LLM-as-a-Judge.

</details>

### 237. Secure Seed-Based Multi-bit Watermarking for Diffusion Models from First Principles

📄 [arXiv](https://arxiv.org/abs/2605.06153) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`watermark`、`diffusion model`、`seed-based embedding`、`security-robustness-fidelity`、`theoretical framework`
- 🎯 **研究动机**：seed-based 生成内水印的评估高度经验化、依赖特定生成与反演架构，且缺乏严格的安全性定义，导致任何方法的性能尤其安全性都难以下明确结论。
- 🔬 **研究方法**：将模型相关部分与水印系统实际决策机制解耦，建立基于 security、robustness、fidelity 三者的形式化评估框架与刻画三者权衡的特征曲面，并提出可达到曲面上任意工作点、推广既有 seed-based 方法的 SSB 水印。
- 📌 **结论**：SSB 能在安全-鲁棒-保真特征曲面上达到任意目标区间，为无需昂贵经验评估、具理论保证的现代水印系统设计开辟道路。

👤 **作者**：Enoal Gesny、Eva Giboulot

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid emergence of generative image models has led to the development of specialized watermarking techniques, particularly in-generation methods such as seed-based embedding. However, current evaluations in this area remain largely empirical, making them heavily reliant on the specific model architectures used for generation and inversion. This prevents any clear conclusion on the performance of any method, especially regarding security, for which a rigorous definition is lacking. Against this approach, we argue that the effectiveness of a watermarking scheme should be established purely through a thorough theoretical analysis. This is enabled by decoupling the model-dependent part from the actual decision mechanism of the watermarking system. Using this decoupling, we introduce a formal evaluation framework based on security, robustness, and fidelity. This allows precise comparisons between watermarking systems through a characteristic surface representing the trade-off between these three quantities, independent of any generative model. Based on this framework, we propose SSB, a novel watermarking method that generalizes previous seed-based methods by allowing to reach any security-robustness-fidelity regime on its characteristic surface. This work opens the door to the design of modern watermarking systems with theoretical guarantees that do not necessitate any costly empirical evaluations.

</details>

### 238. Asymmetric Phase Coding Audio Watermarking

📄 [arXiv](https://arxiv.org/abs/2605.07241) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`watermark`、`audio provenance`、`phase coding`、`digital signature`
- 🎯 **研究动机**：深伪音频挑战语音认证系统，被动取证检测器对演进的生成模型与真实信道失真敏感，需要可审计的音频溯源原语
- 🔬 **研究方法**：提出免训练的 Asymmetric Phase Coding（APC），组合 Ed25519 数字签名、Reed-Solomon 纠错、伪随机 STFT 相位 bin 选择与相邻 bin 对 log 幅度差上的冗余 QIM 编码，形成紧凑、不可抵赖、盲提取的密码学签名层
- 📌 **结论**：在 1000 条 LibriSpeech 测试音频、8 种攻击配置（端裁剪、低通、重采样、FLAC/MP3/OGG 重编码等）下，每种条件密码学验证率均达 97.5%-98.3%，平均 PESQ 为 3.02，CPU 延迟仅数十毫秒

👤 **作者**：Guang Yang、Amir Ghasemian、Ninareh Mehrabi、Homa Hosseinmardi

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of deepfake audio challenges voice-based authentication systems; passive forensic detectors are sensitive to evolving generative models and to real-world channel distortions. We propose Asymmetric Phase Coding (APC), a training-free cryptographic signing layer for audio, designed as a compact and auditable provenance primitive that can stand alone or be stacked with learned watermarks. APC combines Ed25519 digital signatures (EdDSA, FIPS 186-5; 64-byte signatures) with Reed-Solomon error correction, pseudo-random STFT phase-bin selection, and a redundant quantization-index-modulation (QIM) code on log-magnitude differences of adjacent bin pairs, yielding a compact, non-repudiable, blind-extractable watermark. We evaluate APC on 1,000 LibriSpeech test-clean clips (10 s each, 44.1 kHz) under eight attack configurations -- identity, 10% end-cropping, 20% end-cropping, 8 kHz low-pass, 16 kHz round-trip resampling, FLAC re-encoding, MP3 at 128 kbps, and OGG-Vorbis at 128 kbps -- and achieve cryptographic verification rates between 97.5% and 98.3% on every condition at mean PESQ=3.02 and tens-of-milliseconds CPU latency. We explicitly compare APC against recent neural baselines (AudioSeal, WavMark, SilentCipher), detail the threat model (forgery resistance vs. erasure), characterize the dataset, define all metrics, quantify an adaptive white-box erasure attack, and release code, keys, and metadata for reproducibility.

</details>

### 239. Sequential Behavioral Watermarking for LLM Agents

📄 [arXiv](https://arxiv.org/abs/2605.11036) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`watermark`、`llm agent`、`provenance`、`trajectory`、`history-conditioned`
- 🎯 **研究动机**：agent 轨迹难以证明来源与所有权，而现有 agent 水印把每个动作步当独立试验、忽略轨迹结构，在轨迹被扰动、截断或未对齐观测时脆弱。
- 🔬 **研究方法**：提出 SeqWM 序列行为水印框架，将信号嵌入 history-conditioned 转移模式，并以位置无关方式对照随机 key 基线验证轨迹。
- 📌 **结论**：在多样 agent 基准与 LLM backbone 上实现可靠检测且保持 agent 效用，在轨迹损坏下依然鲁棒，而 round-indexed 行为水印在同样条件下崩溃。

👤 **作者**：Hyeseon An、Shinwoo Park、Dongsu Kim、Yo-Sub Han

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents act through sequences of executable decisions, but their trajectories provide little evidence of which agent or policy produced them, making provenance, ownership, and unauthorized reuse difficult to establish from observed behavior alone. This motivates watermarking signals embedded directly into agent behavior rather than only into generated text, since text watermarking cannot capture the action-level decisions that define agent execution. Recent agent watermarking methods address this gap by moving the watermark from generated text to behavioral choices. However, by treating each action step as an independent trial, they overlook trajectory structure and become fragile when trajectories are perturbed, truncated, or observed without reliable alignment. We propose SeqWM, a sequential behavioral watermarking framework that embeds signals into history-conditioned transition patterns and verifies trajectories position-agnostically against random-key baselines. Experiments across diverse agent benchmarks and LLM backbones show that SeqWM consistently achieves reliable detection while preserving agent utility, and remains robust under trajectory corruption where round-indexed behavioral watermarks collapse.

</details>

### 240. Every Bit, Everywhere, All At Once: A Binomial Multibit LLM Watermark

📄 [arXiv](https://arxiv.org/abs/2605.11653) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`watermark`、`multibit`、`binomial encoding`、`payload capacity`、`per-bit confidence`
- 🎯 **研究动机**：LLM 水印已商用落地，实用场景日益需要把用户 ID、时间戳等复杂 payload 编码进文本的多比特水印，而既有评估指标缺乏实用洞察。
- 🔬 **研究方法**：引入 binomial encoding 在每个 token 位置直接编码 payload 的每一位，配合生成期间把编码压力动态重定向到欠编码位的有状态编码器，并提出 per-bit confidence scoring 作为实用评估指标。
- 📌 **结论**：在最高 64-bit payload 上对 8 个基线的评估显示消息准确率与鲁棒性更优，且在更实用的大 payload、低失真区间优势进一步扩大。

👤 **作者**：Thibaud Gloaguen、Robin Staab、Mark Vero、Martin Vechev

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With LLM watermarking already being deployed commercially, practical applications increasingly require multibit watermarks that encode more complex payloads, such as user IDs or timestamps, into the generated text. In this work, we propose a fundamentally new approach for multibit watermarking: introducing binomial encoding to directly encode every bit of the payload at every token position. We complement our approach with a stateful encoder that during generation dynamically redirects encoding pressure toward underencoded bits. Our evaluation against 8 baselines on up to 64-bit payloads shows that our scheme achieves superior message accuracy and robustness, with the gap to baseline methods widening in more relevant settings (i.e., large payloads and low-distortion regimes). At the same time, we challenge prior works' evaluation metrics, highlighting their lack of practical insights, and introduce per-bit confidence scoring as a practically relevant metric for evaluating multibit LLM watermarks.

</details>

### 241. TextSeal: A Localized LLM Watermark for Provenance & Distillation Protection

📄 [arXiv](https://arxiv.org/abs/2605.12456) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`watermark`、`gumbel-max sampling`、`localization`、`distillation protection`、`distortion-free`
- 🎯 **研究动机**：开源 LLM 文本水印需要同时实现强检测、输出多样性保持与混合文档中的局部定位，并兼容投机解码等推理优化。
- 🔬 **研究方法**：TextSeal 基于 Gumbel-max 采样引入 dual-key generation 恢复输出多样性，配合 entropy-weighted scoring 与多区域定位，不增加任何推理开销。
- 📌 **结论**：检测强度严格优于 SynthID-text 等基线、抗稀释且理论 distortion-free；6000 次 A/B、5 语言人类评估无可感质量差异，水印信号还可经蒸馏迁移以检测未授权使用。

👤 **作者**：Tom Sander、…、Pierre Fernandez

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce TextSeal, a state-of-the-art watermark for large language models. Building on Gumbel-max sampling, TextSeal introduces dual-key generation to restore output diversity, along with entropy-weighted scoring and multi-region localization for improved detection. It supports serving optimizations such as speculative decoding and multi-token prediction, and does not add any inference overhead. TextSeal strictly dominates baselines like SynthID-text in detection strength and is robust to dilution, maintaining confident localized detection even in heavily mixed human/AI documents. The scheme is theoretically distortion-free, and evaluation across reasoning benchmarks confirms that it preserves downstream performance; while a multilingual human evaluation (6000 A/B comparisons, 5 languages) shows no perceptible quality difference. Beyond its use for provenance detection, TextSeal is also ``radioactive'': its watermark signal transfers through model distillation, enabling detection of unauthorized use.

</details>

### 242. Watermarking Should Be Treated as a Monitoring Primitive

📄 [arXiv](https://arxiv.org/abs/2605.13095) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`watermark`、`attribution`、`monitoring`、`observer model`、`governance`
- 🎯 **研究动机**：水印被广泛提议用于生成模型的溯源、归因与安全监控，但应如何评测与治理它缺乏统一视角。
- 🔬 **研究方法**：提出两类互补观察者模型——用检测器/解码器访问与实体映射做归因的内部观察者、以及无需密钥或检测器而从标注输出学习实体特异信号的外部观察者——并分析两者支持监控的条件。
- 📌 **结论**：零比特水印在每实体多密钥部署下无需显式编码身份即可支持内部归因，并在选定文本与图像配置中实现外部识别；外部暴露依赖持久可学习的水印结构而非普适存在，故除单样本鲁棒性外还应治理归因访问、部署选择及依赖设计的实体可链接性与去匿名化风险。

👤 **作者**：Toluwani Aremu、Jie Zhang、Nils Lukas

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Watermarking is widely proposed for provenance, attribution, and safety monitoring in generative models. We argue that it should be evaluated and governed as a monitoring primitive through two complementary observer models. Internal observers use detector or decoder access and entity mappings for attribution; external observers learn entity-specific signals from labeled outputs without keys or detectors. With persistent entity bindings and reliable inference, either pathway can support monitoring. We show that even zero-bit watermarking supports internal attribution under per-entity multi-key deployments without explicitly encoding identity, and demonstrate external identification in selected text and image configurations. External exposure depends on persistent, learnable watermark structure and is not universal, while internal attribution also remains conditional on reliability and access. These findings motivate governance of attribution access and deployment choices alongside evaluation of design-dependent entity linkability, de-anonymization or re-identification, beyond per-sample robustness.

</details>

### 243. Watermarking Game-Playing Agents in Perfect-Information Extensive-Form Games

📄 [arXiv](https://arxiv.org/abs/2605.14283) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`watermark`、`game-playing agent`、`extensive-form game`、`kgw`、`statistical test`
- 🎯 **研究动机**：LLM 水印可检测模型误用，博弈场景（如在线国际象棋检测 AI 作弊）存在类似挑战，但博弈策略如何被水印化尚未被研究。
- 🔬 **研究方法**：将 KGW 水印适配到完美信息扩展式博弈的博弈 agent 策略上，并设计统计检验来检测水印。
- 📌 **结论**：证明被水印策略的期望效用退化有界但存在可检测性与质量之间的权衡；在国际象棋引擎上水印对策略质量影响可忽略，且仅需少量对局即可检出。

👤 **作者**：Juho Kim、Fei Fang、Tuomas Sandholm

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Watermarking techniques for large language models (LLMs), which encode hidden information in the output so its source can be verified, have gained significant attention in recent days, thanks to their potential capability to detect accidental or deliberate misuse. Similar challenges involving model misuse also exist in the context of game-playing, such as when detecting the unauthorized use of AI tools in gaming platforms (e.g., cheating in online chess). In this paper, we initiate the study of how game-playing strategies can be watermarked. We show how the KGW watermark for LLMs can be adapted to watermark game-playing agents in perfect-information extensive-form games. The watermark can then be detected using a statistical test. We show that the degradation in the quality of the watermarked strategy profile, quantified by the expected utility, can be bounded, but there is a tradeoff between detectability and quality. In our experiments, we bootstrap the watermarking framework to various chess engines and demonstrate that a) the impact of the watermark on the quality of the strategy is negligible and b) the watermark can be detected with just a handful of games.

</details>

### 244. Making Open-Source Text LLM Watermarks Durable Against Merging

📄 [arXiv](https://arxiv.org/abs/2607.20435) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`watermark`、`model merging`、`adversarial training`、`open-source llm`、`durability`
- 🎯 **研究动机**：嵌入开源 LLM 权重的文本水印会被训练后修改移除，其中常用于融合专家知识与防止灾难性遗忘的 model merging 尤其强烈地去除水印，如何让水印在后续 merging 中存活是关键问题。
- 🔬 **研究方法**：提出 Merge-Adversarial Training 对抗训练算法，在把文本水印蒸馏进模型权重的同时对后续 model merging 保持鲁棒。
- 📌 **结论**：一致超越所有基线（SLERP 下 TPR@1%FPR 至多 +51 个百分点、平均 +25 个百分点）且保持下游能力，并首次在 3 种主流 merging 算法与组合专家能力、防灾难性遗忘等真实合并场景下评估开源水印。

👤 **作者**：Luisa Scharff、Thibaud Gloaguen、Robin Staab、Martin Vechev

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-source LLMs (OSMs)arereaching near state-of-the-art performance, prompting prior works to trace the text they generate by embedding text watermarking algorithms directly into their weights. Yet, OSMs are subject to post-training modifications, which has been shown to remove the watermark. Model merging in particular, a prominent method used for combining expert knowledge and preventing catastrophic forgetting, strongly removes such OSM watermarks. A key question is how to enable OSM watermarks that survive subsequent merging. In this work, we show for the first time how to design an OSM watermark that is durable against model merging. We propose Merge-Adversarial Training, an adversarial training algorithm to distill text watermarks into model weights while being robust to subsequent model merging. Our approach consistently outperforms all baselines (e.g. with SLERP up to +51 percentage points (pp) TPR@1%FPR with +25 pp on average) while preserving downstream capabilities. We also for the first time evaluate OSM watermarks against realistic merge scenarios, representing common use-cases such as combining expert capabilities or preventing catastrophic forgetting, and with 3 prominent merging algorithms. More broadly, our findings suggest that adversarial training is a reliable approach for increasing OSM watermark durability against post-training modifications.

</details>

### 245. PGID: Progressive Guided Inversion and Denoising for Robust Watermark Detection

📄 [arXiv](https://arxiv.org/abs/2605.09319) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`watermark detection`、`diffusion inversion`、`imprint removal`、`forgery attack`
- 🎯 **研究动机**：语义水印依赖扩散逆变换做检测构成关键漏洞：印记移除与伪造攻击通过把带水印潜变量移入无水印区域、把无水印潜变量引入有水印区域来制造欺骗性检测结果。
- 🔬 **研究方法**：提出首个即插即用、免训练的噪声提取框架 PGID，通过渐进式逆变换-去噪循环消除中间潜变量偏转并缓解对抗扰动，把被扰动的潜变量投影回其原本所属区域。
- 📌 **结论**：跨多种水印方案的综合评估表明 PGID 能恢复被移除的水印、识别伪造样本，成功恢复检测可靠性。

👤 **作者**：Minh Quoc Duong、Chun Tong Lei、Chun Pong Lau

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the proliferation of AI-generated images, digital watermarking has become an essential safeguard for protecting intellectual property and mitigating malicious exploitation. Recent works on semantic watermarking have enabled efficient copyright protection for diffusion models. However, the dependence of semantic watermarking on diffusion inversion for watermark detection creates a critical vulnerability. Imprint removal and forgery attacks exploit this weakness to produce deceptive results. Our analysis reveals that these attacks succeed by displacing watermarked latents into the unwatermarked region, while guiding unwatermarked latents into the watermarked region. Based on that, we propose Progressive Guided Inversion and Denoising (PGID), the first plug-and-play, training-free noise extraction framework designed to defend against both attack strategies. PGID effectively defends by projecting perturbed latents back to the region where they originally belong. The projection is achieved by eliminating intermediate latent deflections and mitigating adversarial perturbations through progressive inversion-denoising cycles. Comprehensive evaluations across multiple schemes demonstrate that PGID successfully restores detection reliability by recovering removed watermarks and identifying forged instances.

</details>

### 246. On the Robustness of Watermarking for Autoregressive Image Generation

📄 [arXiv](https://arxiv.org/abs/2604.11720) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-04　🏷 NeurIPS 2026

**关键词**：`attack`、`watermark removal`、`forgery`、`autoregressive image generation`、`watermark mimicry`
- 🎯 **研究动机**：自回归图像生成器的水印被用于检测归因输出以对抗错误信息并过滤合成图像防模型坍缩，其面对移除与伪造攻击的鲁棒性未知。
- 🔬 **研究方法**：评估现有攻击并提出三种新攻击——向量量化再生移除、对抗优化攻击与频率注入攻击，仅需单张水印参考图像且无需原始模型参数或水印密钥。
- 📌 **结论**：移除与伪造攻击均有效，说明现有 AR 图像生成水印不足以支持数据集过滤的合成内容检测；Watermark Mimicry 还能操纵真实图像模仿生成器水印触发误检、使其被排除出未来模型训练。

👤 **作者**：Andreas Müller、…、Asja Fischer

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of autoregressive (AR) image generators demands reliable detection and attribution of their outputs to mitigate misinformation, and to filter synthetic images from training data to prevent model collapse. To address this need, watermarking techniques, specifically designed for AR models, embed a subtle signal at generation time, enabling downstream verification through a corresponding watermark detector. In this work, we study these schemes and demonstrate their vulnerability to both watermark removal and forgery attacks. We assess existing attacks and further introduce three new attacks: (i) a vector-quantized regeneration removal attack, (ii) adversarial optimization-based attack, and (iii) a frequency injection attack. Our evaluation reveals that removal and forgery attacks can be effective with access to a single watermarked reference image and without access to original model parameters or watermarking secrets. Our findings indicate that existing watermarking schemes for AR image generation do not reliably support synthetic content detection for dataset filtering. Moreover, they enable Watermark Mimicry, whereby authentic images can be manipulated to imitate a generator's watermark and trigger false detection to prevent their inclusion in future model training.

</details>

### 247. Alignment Imprint: Zero-Shot AI-Generated Text Detection via Provable Preference Discrepancy

📄 [arXiv](https://arxiv.org/abs/2604.16923) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-04　🏷 NeurIPS 2026

**关键词**：`detection`、`ai-generated text`、`alignment`、`log-likelihood ratio`、`zero-shot`
- 🎯 **研究动机**：现有基于 likelihood 的 AI 生成文本检测对内容复杂度敏感、性能不稳定。
- 🔬 **研究方法**：将 alignment 过程抽象为约束优化序列，证明 log-likelihood ratio 可分解为隐式指令偏置与偏好奖励（Alignment Imprint），并提出信息加权的标准化统计量 LAPD 抑制高熵区不稳定。
- 📌 **结论**：理论上 LAPD 支配 Fast-DetectGPT 并严格改进未加权对齐分数，实验上相对最强基线提升 45.82% 且在所有设置下一致大幅增益。

👤 **作者**：Junxi Wu、…、Changliang Zou

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Detecting AI-generated text is an important but challenging problem. Existing likelihood-based detection methods are often sensitive to content complexity and may exhibit unstable performance. In this paper, our key insight is that modern Large Language Models (LLMs) undergo alignment (including fine-tuning and preference tuning), leaving a measurable distributional imprint. We theoretically derive this imprint by abstracting the alignment process as a sequence of constrained optimization steps, showing that the log-likelihood ratio can naturally decompose into implicit instructional biases and preference rewards. We refer to this quantity as the Alignment Imprint. Furthermore, to mitigate the instability in high-entropy regions, we introduce Log-likelihood Alignment Preference Discrepancy (LAPD), a standardized information-weighted statistic based on alignment imprint. We provide statistical guarantee that alignment-based statistics dominate Fast-DetectGPT in performance. We also theoretically show that LAPD strictly improves the unweighted alignment scores when the aligned and base models are close in distribution. Extensive experiments show that LAPD achieves an improvement 45.82% relative to the strongest existing baselines, yielding large and consistent gains across all settings.

</details>

### 248. TRACE: Structure-Aware Character Encoding for Robust and Generalizable Document Watermarking

📄 [arXiv](https://arxiv.org/abs/2603.12873) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`watermark`、`document watermarking`、`character encoding`、`diffusion model`、`structure-aware`
- 🎯 **研究动机**：现有文档水印依赖边缘特征或预定义码本，抗噪干扰与跨字符泛化能力不足。
- 🔬 **研究方法**：提出结构感知框架 TRACE，用扩散模型做局部字符编码嵌入：自适应扩散初始化经移动概率估计器（MPE）、目标点估计（TPE）与掩码绘制模型（MDM）识别操纵点/目标点/编辑区域，引导扩散编码精确移动选定点，再以掩码区域替换与专用损失最小化特征改动。
- 📌 **结论**：较 SOTA 方法取得超 5 dB 的 PSNR 提升与跨媒体传输后 5% 更高的提取精度，并在多语言多字体上广泛泛化。

👤 **作者**：Jiale Meng、Jie Zhang、Runyi Hu、Zhe-Ming Lu、Tianwei Zhang、Yiming Li

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We propose TRACE, a structure-aware framework leveraging diffusion models for localized character encoding to embed data. Unlike existing methods that rely on edge features or pre-defined codebooks, TRACE exploits character structures that provide inherent resistance to noise interference due to their stability and unified representation across diverse characters. Our framework comprises three key components: (1) adaptive diffusion initialization that automatically identifies handle points, target points, and editing regions through specialized algorithms including movement probability estimator (MPE), target point estimation (TPE) and mask drawing model (MDM), (2) guided diffusion encoding for precise movement of selected point, and (3) masked region replacement with a specialized loss function to minimize feature alterations after the diffusion process. Comprehensive experiments demonstrate \name{}'s superior performance over state-of-the-art methods, achieving more than 5 dB improvement in PSNR and 5\% higher extraction accuracy following cross-media transmission. \name{} achieves broad generalizability across multiple languages and fonts, making it particularly suitable for practical document security applications.

</details>

### 249. ArcMark: Distortion-Free Multi-Byte LLM Watermark via Optimal Transport

📄 [arXiv](https://arxiv.org/abs/2602.07235) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`watermark`、`multi-bit embedding`、`distortion-free`、`channel coding`
- 🎯 **研究动机**：现有多比特水印沿用零比特设计原则（如每 token 编码单比特），无法在不扰动 next-token 分布的前提下嵌入用户 ID、模型版本乃至 prompt 本身等多字节信息
- 🔬 **研究方法**：提出 ArcMark，将无失真水印形式化为信道编码问题并推导信息论信道容量的基本极限，据此设计可在几百 token 内可靠嵌入多字节的编码构造
- 📌 **结论**：ArcMark 在重构精度上优于竞争性多比特无失真水印（含部分文本被篡改的攻击场景），且输出在困惑度与下游任务质量上与无水印文本不可区分

👤 **作者**：Atefeh Gilani、Sajani Vithana、Carol Xuan Long、Oliver Kosut、Lalitha Sankar、Flavio P. Calmon

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Watermarking is an important tool for promoting the responsible use of large language models (LLMs). Existing watermarks insert a signal into generated tokens that either flags LLM-generated text (zero-bit watermarking) or encodes more complex messages (multi-bit watermarking). Though a number of recent approaches insert multiple bits into text without perturbing average next-token predictions, they largely extend design principles from the zero-bit setting, such as encoding a single bit per token. In contrast, a watermarker capable of embedding multiple bytes into the text would dramatically increase the potential applications, by embedding information such as the ID of the user who submitted the prompt, the precise model version that was used, or even the prompt itself. We address this problem by introducing ArcMark: a new watermark construction based on coding and information-theoretic principles that is capable of reliably embedding multiple bytes of information into just a few hundred tokens, without any distortion of the underlying LLM next-token distribution. We derive ArcMark by formulating the distortion-free watermarking problem as a channel coding problem, and deriving an information-theoretic channel capacity that establishes the fundamental limit of embedding information in LLM output in a distortion-free manner. This capacity formulation informs the design of ArcMark. In practice, ArcMark outperforms competing multi-bit distortion-free watermarks in terms of reconstruction accuracy, including in the face of attacks that alter a subset of the LLM text. ArcMark output is also shown to be indistinguishable from unwatermarked text in terms of perplexity, and in downstream task quality.

</details>

### 250. MarkTune: Improving the Quality-Detectability Trade-off in Model-Embedded LLM Watermarking

📄 [arXiv](https://arxiv.org/abs/2512.04044) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`watermark`、`model-embedded`、`on-policy fine-tuning`、`open-weight`、`quality-detectability tradeoff`
- 🎯 **研究动机**：推理时水印带来额外推理开销且不适用于日益普遍的开放权重模型，而模型嵌入式水印（如 GaussMark）存在根本的质量-可检测性权衡——强检测力所需的权重扰动会明显损害生成质量。
- 🔬 **研究方法**：提出理论上支撑的 on-policy 微调框架 MarkTune，把 GaussMark 检测统计量当作奖励、显式对文本质量正则化，从而推移质量-可检测性前沿。
- 📌 **结论**：检测力接近强推理时方案的同时保持生成质量与下游任务性能，对改写与微调攻击极为鲁棒，且在单一语料微调后于未见数据上仍保有可观检测力。

👤 **作者**：Yizhou Zhao、Steven Wu、Adam Block

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Language model watermarking schemes fall into two broad categories: inference-time methods, which modify the decoding process at generation time, and model-embedded methods, which encode a secret signal directly into the model weights. Inference-time watermarking methods incur additional inference overhead and are not applicable in the increasingly prevalent open-weight model settings. In contrast, model-embedded watermarks introduce no additional inference latency---generation uses the standard sampling pipeline---and are particularly well-suited to open-weight settings. However, existing model-embedded approaches such as GaussMark face a fundamental quality-detectability trade-off: achieving strong detection power typically requires weight perturbations that noticeably degrade generation quality. We introduce MarkTune, a theoretically grounded on-policy fine-tuning framework that treats the GaussMark detection statistic as a reward while explicitly regularizing for text quality. Empirically, MarkTune substantially improves the quality-detectability frontier of GaussMark, approaching the detectability of strong inference-time schemes while preserving generation quality and downstream task performance. MarkTune is also extremely robust to paraphrasing and fine-tuning attacks, and generalizes across datasets: models fine-tuned on one corpus retain substantial detection power on unseen data.

</details>

### 251. PRO: Enabling Precise and Robust Text Watermark for Open-Source LLMs

📄 [arXiv](https://arxiv.org/abs/2510.23891) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-10　🏷 NeurIPS 2026

**关键词**：`watermark`、`open-source llm`、`distillation`、`robustness`、`model merging`
- 🎯 **研究动机**：开源 LLM 拥有者无法控制解码过程，从闭源模型蒸馏水印又因学得模式与预定义模式错配而对下游微调、模型合并脆弱，导致缺少实用的文本溯源手段。
- 🔬 **研究方法**：PRO 将 watermark policy model 与 LLM 联合训练以产生更易学、更贴合检测准则的模式，并用模拟下游扰动的正则项惩罚水印可检测性退化。
- 📌 **结论**：在 LLaMA-3.2、LLaMA-3、Phi-2 等开源模型上同时显著提升水印可检测性与对模型修改的韧性。

👤 **作者**：Jiaqi Xue、…、Mengxin Zheng

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text watermarking for large language models (LLMs) enables model owners to verify text origin and protect intellectual property. While watermarking methods for closed-source LLMs are relatively mature, extending them to open-source models remains challenging, as developers cannot control the decoding process. Consequently, owners of open-source LLMs lack practical means to verify whether text was generated by their models. A core difficulty lies in embedding watermarks directly into model weights without hurting detectability. A promising idea is to distill watermarks from a closed-source model into an open one, but this suffers from (i) poor detectability due to mismatch between learned and predefined patterns, and (ii) fragility to downstream modifications such as fine-tuning or model merging. To overcome these limitations, we propose PRO, a Precise and Robust text watermarking method for open-source LLMs. PRO jointly trains a watermark policy model with the LLM, producing patterns that are easier for the model to learn and more consistent with detection criteria. A regularization term further simulates downstream perturbations and penalizes degradation in watermark detectability, ensuring robustness under model edits. Experiments on open-source LLMs (e.g., LLaMA-3.2, LLaMA-3, Phi-2) show that PRO substantially improves both watermark detectability and resilience to model modifications.

</details>

### 252. Majority Bit-Aware Watermarking for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2508.03829) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-08　🏷 NeurIPS 2026

**关键词**：`watermark`、`multi-bit message`、`green list`、`text quality`
- 🎯 **研究动机**：现有多比特 LLM 水印必须限制 green list 大小以维持可检测信号，导致文本质量与解码精度之间存在根本性权衡
- 🔬 **研究方法**：提出 majority bit-aware encoding 编码范式，将水印信号强度与 green list 大小解耦，使大 green list 下仍保有强水印信号，并给出 MajorMark 与面向长消息优化的 MajorMark+ 两个实例
- 📌 **结论**：在 SOTA LLM 上的实验表明两方法同时取得更高解码精度与更优文本质量，超越先前基线

👤 **作者**：Jiahao Xu、Rui Hu、Olivera Kotevska、Zikai Zhang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The growing deployment of Large Language Models (LLMs) has raised concerns about their misuse in generating harmful or deceptive content. To address this issue, watermarking methods have been proposed to embed identifiable multi-bit messages into generated text for misuse tracing. However, existing methods often suffer from a fundamental trade-off between text quality and decoding accuracy. In particular, they have to restrict the size of the preferred token set (i.e., green list) during encoding to maintain a detectable watermark signal for decoding, which inevitably degrades generation quality. To improve this trade-off, we propose a novel message encoding paradigm called \textit{majority bit-aware encoding}, which relaxes the watermark signal strength from the green list size. This strategy allows for a strong watermark signal to be preserved in generated texts even when using a large green list. We introduce two instantiations of this paradigm: MajorMark and MajorMark$^{+}$, where the latter is specifically optimized for long messages. Extensive experiments on state-of-the-art LLMs demonstrate that our methods achieve higher decoding accuracy and superior text quality compared to prior baselines.

</details>

### 253. Watermarking Without Standards Is Not AI Governance

📄 [arXiv](https://arxiv.org/abs/2505.23814) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-05　🏷 NeurIPS 2026

**关键词**：`survey`、`watermarking`、`ai governance`、`regulation`、`auditability`
- 🎯 **研究动机**：水印已成为生成式 AI 内容归因的主导技术方案并被全球治理框架日益援引，但监管期待与现有水印技术能力之间的差距不断扩大，恐沦为象征性合规而非有效监督。
- 🔬 **研究方法**：立场论文——分析政策提案与行业实践，揭示激励结构抑制鲁棒可审计部署的成因，并提出涵盖技术标准、审计基础设施与执行机制的三层对齐框架。
- 📌 **结论**：若无强制要求与独立验证，水印将无法支撑问责，并最终削弱更广泛的 AI 安全与监管努力。

👤 **作者**：Alexander Nemecek、Yuzhou Jiang、Erman Ayday

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Watermarking has emerged as a leading technical proposal for attributing generative AI content and is increasingly cited in global governance frameworks. This position paper argues that current implementations risk serving as symbolic compliance rather than delivering effective oversight. We identify a growing gap between regulatory expectations and the technical limitations of existing watermarking schemes. Through analysis of policy proposals and industry practices, we show how incentive structures disincentivize robust, auditable deployments. To realign watermarking with governance goals, we propose a three-layer framework encompassing technical standards, audit infrastructure, and enforcement mechanisms. Without enforceable requirements and independent verification, watermarking will remain inadequate for accountability and ultimately undermine broader efforts in AI safety and regulation.

</details>

**尚未挂出 arXiv（待核验）**
- MC2Mark: Distortion-Free Multi-Bit Watermarking for Long Messages
- Anytime-Valid Statistical Watermarking
- Watermark Removal in AI-Generated Images via Next-Token Modeling
- RVCBench: Benchmarking Robustness of Voice Cloning Across Modern Audio Generation Models

### 内部表示干预与监控（安全 threat model 绑定）

### 254. Kernelized Activation Steering

📝 [OpenReview](https://openreview.net/forum?id=F4iCxDrUbU) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`activation steering`、`kernel method`、`jailbreak`
- 🎯 **研究动机**：DiM 等标准激活转向方法对所有激活施加单一与输入无关的转向向量，表达力受限且忽略激活空间的局部结构。
- 🔬 **研究方法**：提出 Kernelized Activation Steering（KAS），将激活转向提升到再生核希尔伯特空间（RKHS），仅通过核求值构造隐式的激活相关转向得分，实现局部自适应的非线性转向场，DiM 为线性核下的特例。
- 📌 **结论**：在 LLM 越狱与图像风格控制等标准转向任务上，KAS 一致优于现有方法。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Activation steering provides a simple, training-free mechanism for controlling attributes of generative models (e.g., sentiment, style, helpfulness). However, standard approaches such as Difference-in-Means (DiM) apply a single input-independent steering vector across all activations, limiting expressivity and ignoring the local structure of the activation space. We propose Kernelized Activation Steering (KAS), a unifying framework that lifts activation steering into a reproducing kernel Hilbert space (RKHS). KAS formulates steering as an optimization problem expressed purely via kernel evaluations, yielding an implicit, activation-dependent steering score without constructing explicit feature maps. Unlike DiM, KAS induces locally adaptive steering: each activation is modified according to its relative position with respect to source and target reference sets, producing a nonlinear steering field over the representation space. Importantly, DiM is recovered as a special case under a linear kernel, offering a principled interpretation of steering, while richer kernels (e.g., RBF) enable geometry-aware interventions. Across standard activation steering tasks, including jailbreaking LLMs and image style control, KAS consistently outperforms existing methods.

</details>

### 255. CrossSteer: Cross-Modal Safety Steering for Audio-Language Models

📝 [OpenReview](https://openreview.net/forum?id=upHPX6x1xE) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`audio-language model`、`jailbreak`、`activation steering`、`cross-modal transfer`
- 🎯 **研究动机**：音频语言模型（ALM）开辟了用语音传递有害请求的新越狱面，现有防护依赖音频侧过滤器或 guard 模型而使内部安全行为基本失控，直接音频侧转向又因声学与前端变异更大而噪声大、无效。
- 🔬 **研究方法**：提出 CrossSteer，从纯文本偏好对学习更干净的语义安全方向，经对齐的共享残差流迁移到音频，在音频鲁棒层施加干预，使有害请求生成由不安全顺从转向安全拒绝。
- 📌 **结论**：在三个 ALM 骨干上持续降低音频越狱攻击成功率并大体保持良性效用，且可与现有防护叠加进一步提升鲁棒性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Audio--language models (ALMs) introduce a new jailbreak surface in which harmful requests can be delivered through speech. Existing safeguards rely on audio-side filters or guard models, leaving internal safety behavior largely uncontrolled. We instead pursue a representation-level alternative that controls refusal--compliance behavior inside the shared language-model backbone. However, our empirical study shows that direct audio-side steering is noisy and ineffective, consistent with activation analyses indicating larger acoustic and front-end variation in speech-derived representations. Based on this observation, we propose CrossSteer, a cross-modal steering method that learns a cleaner semantic safety direction from text-only preference pairs and transfers it to audio through the aligned shared residual stream. CrossSteer fits a residual-stream direction whose intervention shifts harmful-request generation from unsafe compliance toward safe refusal, and applies this direction at an audio-robust layer. Across three ALM backbones, CrossSteer consistently reduces audio jailbreak attack success rate while largely preserving benign utility, demonstrating cross-modal transfer of text-derived safety steering to the audio channel. Additional experiments show that CrossSteer composes with existing safeguards, further improving robustness as a complementary representation-level safety layer.Our anonymized source code is available at:~\urlhttps://anonymous.4open.science/r/CrossSteer-69F6.

</details>

### 256. Sparse Internal Control of Language Models

📝 [OpenReview](https://openreview.net/forum?id=7Q8u18mL29) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`internal control`、`activation steering`、`controllability`、`refusal steering`
- 🎯 **研究动机**：现有方法要么更新共享参数、要么经外部接口约束生成，冻结模型中是否存在紧凑的内部控制能力仍属开放问题。
- 🔬 **研究方法**：提出稀疏内部控制框架，以局部目标可控性刻画候选"位点-方向"对，给出 Driver-OMP（稀疏重建目标行为位移）与 Coverage-Driver（稳定覆盖提示）两种选择器，并建立六轴控制评估协议。
- 📌 **结论**：在 GPT-2 small 到 Qwen3-4B 的 IOI、MMLU MCQA 与情感转向任务上，稀疏 driver 集可转向目标行为、随剂量单调响应、支持闭环控制并保持无关行为，但拒绝转向暴露出除严格可达性外全轴通过的边界情形。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Language models are increasingly used in text generation, decision support, and automated interaction, where their behavior must be controlled in a localized, reversible, and selective way. Existing methods either update shared parameters or constrain generation through external interfaces, leaving open whether frozen models contain compact internal control. We introduce sparse internal control, a framework for steering target behavior by applying inference-time interventions to a small set of internal model nodes. The framework formulates control through local target controllability, where candidate site–direction pairs are characterized by their behavioral effects under target, preservation, and energy constraints. This yields two complementary selectors: Driver-OMP, which selects nodes that sparsely reconstruct a desired behavioral displacement, and Coverage-Driver, which favors nodes whose effects cover prompts stably. We further propose a six-axis control-evaluation protocol measuring reachability, signed reversal, dose response, feedback controllability, off-target preservation, and held-out reuse. Across IOI, MMLU MCQA, and sentiment steering on models from GPT-2 small to Qwen3-4B, sparse driver sets act as executable actuators: they steer target behavior, respond monotonically to dose, support closed-loop control, and preserve unrelated next-token behavior. On refusal steering, the same protocol exposes a boundary case that passes all evaluated axes except strict reachability. Held-out reuse separates prompt-specific controls requiring refitted strengths from population-level controls that transfer as frozen interventions. These results show that model control can move beyond output-side steering: mechanistic internal variables can be selected, certified, and reused as localized control handles for frozen language models.

</details>

### 257. OASIS: Online Adaptive Steering for In-Training Safety of LLMs

📝 [OpenReview](https://openreview.net/forum?id=5idvmMr6r1) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`activation steering`、`safety alignment`、`fine-tuning`、`training-time intervention`
- 🎯 **研究动机**：微调即使数据看似良性也会侵蚀安全对齐，而已有方法的安全正则可能与主训练目标冲突，或因机制固定而无法适应微调动态。
- 🔬 **研究方法**：提出 OASIS，将安全保持重构为训练时干预，在激活空间追踪失配方向并在微调全程持续在线重校准，施加样本自适应的激活转向以吸收诱导失配的更新。
- 📌 **结论**：在三种失配行为与全失配、混合、良性三种微调数据 regime 下，OASIS 一致提升安全鲁棒性且不牺牲下游性能。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning is essential for adapting Large Language Models to downstream tasks. However, this process can also inadvertently erode the critical safety alignment even when the fine-tuning data appears benign. Prior methods either introduce safety regularizers that may conflict with the primary training objective, or rely on fixed mechanisms that fail to adapt to fine-tuning dynamics. To remedy this, we reframe safety preservation as a training-time intervention and propose Online Adaptive Steering for In-Training Safety (OASIS), enabling continuous online recalibration of the steering direction during fine-tuning. Specifically, OASIS tracks a misalignment direction in activation space, then applies example-adaptive activation steering to absorb misalignment-inducing updates during training. Across three misalignment behaviors and three fine-tuning data regimes, including fully misaligned, mixed, and benign data, OASIS consistently improves safety robustness without sacrificing downstream performance.

</details>

### 258. Safety-Aware Latent Space Reasoning in Large Language Models

📝 [OpenReview](https://openreview.net/forum?id=v5ExASonPK) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`latent space reasoning`、`jailbreak`、`safety alignment`、`distillation`
- 🎯 **研究动机**：将 CoT 压缩为连续潜态的潜空间推理虽提升推理效率，但首个系统安全研究发现多数潜推理方法比基座与 token 空间 CoT 更易受越狱攻击，提示潜化会削弱安全对齐。
- 🔬 **研究方法**：提出 SaLR，将长式安全推理压缩为四块 safe-chain 并经师生隐状态蒸馏迁移安全信号——安全样本对齐早期安全响应前缀以引导安全轨迹，推理样本保留单位置蒸馏以保住潜推理能力。
- 📌 **结论**：跨模型规模与有害基准大幅降低越狱攻击成功率并保持推理精度与 token 效率，还因推理固定在潜态、不暴露文本推理痕迹而缓解 token-inflation 与 CoT-hijacking 等推理特有攻击。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Latent space reasoning improves inference efficiency by compressing chain-of-thought (CoT) reasoning into continuous latent states, but its safety alignment remains poorly understood. In this work, we conduct the first systematic safety study of latent space reasoning models under jailbreak attacks. Our results reveal that most latent reasoning methods exhibit higher vulnerability to jailbreak attacks than both the base model and token-space CoT reasoning counterparts, suggesting that moving reasoning into latent states can weaken safety alignment. To address this issue, we propose easoning framework that injects safety supervision into latent space reasoning. SaLR converts long-form safety reasoning into a compact four-block safe-chain and transfers this safety signal through teacher-student hidden state distillation. For safety instances, SaLR aligns an early safe response prefix to guide the model toward a safe response trajectory; for reasoning instances, it retains single position distillation to preserve latent reasoning ability. Experiments across model scales and harmful benchmarks show that SaLR substantially reduces jailbreak attack success while preserving reasoning accuracy and token efficiency. Beyond standard jailbreaks, SaLR also mitigates reasoning specific attacks such as token-inflation and CoT-hijacking attacks by keeping reasoning in fixed latent states and avoiding exposed textual reasoning traces. Overall, SaLR provides a stronger safety utility trade-off for latent space reasoning. Our anonymous code repository is available at: https://anonymous.4open.science/r/SaLR-3C19

</details>

### 259. LLM Rheology: Auditing Refusal Geometry in Aligned Language Models

📝 [OpenReview](https://openreview.net/forum?id=nbLsmiH2tO) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`analysis`、`refusal geometry`、`activation space`、`scaling`、`jailbreak`
- 🎯 **研究动机**：规模提升模型能力但未必强化内部安全机制，需要表征级方法审计对齐模型在激活空间中对对抗扰动的响应。
- 🔬 **研究方法**：定义 Fisher-Rao 归一化的分布响应（LLM Rheology），度量给定拒绝方向下拒绝行为与对抗任务执行在表征空间的耦合强度，并在 6 个开源模型族、22 个 checkpoint 上审计。
- 📌 **结论**：发现复现的几何 scaling 模式——小模型拒绝响应偏高、中间规模进入弱响应区、大 checkpoint 趋于近基线（任务-拒绝解耦，Qwen/DeepSeek 连续轴上余弦单调衰减）；在 Qwen-72B 关键语义层注入学得的拒绝向量可恢复越狱子集上的拒绝并大体保持良性推理，等范数安慰剂向量无效。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Scaling improves language-model capability, but it does not necessarily strengthen internal safety mechanisms. We introduce , a representation-level framework for auditing how aligned language models respond to adversarial perturbation inside activation space. Given a learned refusal direction, we define as the Fisher--Rao-normalized distributional response induced by controlled activation perturbation. This quantity measures how strongly refusal behavior remains coupled to adversarial task execution in representation space. Across six open model families and 22 checkpoints, including Qwen, DeepSeek-Distill, Mistral, Llama-3, Gemma, and Yi, we observe a recurring geometric scaling pattern. Small aligned models often exhibit elevated refusal response, intermediate-scale models frequently enter weakened-response regimes ( ), and larger checkpoints trend toward near-baseline response consistent with increasing task--refusal decoupling. Cosine measurements on continuous Qwen and DeepSeek scaling axes support this interpretation, showing monotonic decay between refusal and task-generation directions with scale. We further provide causal evidence through inference-time activation intervention on Qwen-72B. Injecting a learned refusal vector at a critical semantic layer restores refusal behavior on the evaluated jailbreak subset while largely preserving benign reasoning performance. Matched-norm placebo vectors fail to reproduce the effect, supporting the directional specificity of the intervention. Together, these results suggest that behavioral refusal can remain surface-level even when internal refusal geometry becomes weakly coupled to adversarial task execution. LLM Rheology provides a complementary representation-level perspective for auditing refusal safety beyond behavioral evaluation.

</details>

### 260. Tight PAC-Bayes Generalisation Guarantees for Large Language Model Safety Monitoring

📝 [OpenReview](https://openreview.net/forum?id=lDwefojK2s) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`evaluation`、`pac-bayes`、`safety oversight`、`generalisation guarantee`、`compression`
- 🎯 **研究动机**：检测 AI 系统安全违规的 LLM 安全监督模型能否可靠泛化、哪些因素影响其泛化，此前缺乏形式化保证。
- 🔬 **研究方法**：将 PAC-Bayes 认证形式化到 LLM 安全监督，基于压缩式界证明高度压缩的 PEFT 适配器描述长度极短，从而给出同时认证分类风险与预测不确定性的非空界，并提出全局量化方法 LoRA-GT 进一步收紧界。
- 📌 **结论**：可认证性与适配器可压缩性强相关（描述长度越短界越紧），高压缩适配器性能损失极小却换来显著更强的认证，且功能性失真能同时追踪测试风险与界紧致度，可用于选择简单可认证的安全适配器。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

How can we ensure that safety oversight models used to detect safety violations in AI systems reliably generalise, and how can we understand the factors that influence their generalisation? In this paper, we formalise PAC-Bayes certification for large language model-based safety oversight and obtain non-vacuous PAC-Bayes guarantees for safety oversight models, even under limited data for safety alignment. Building on compression-based PAC-Bayes bounds, we show that highly compressed PEFT adaptations yield extremely short adaptation description lengths, enabling informative and often tight guarantees that certify both classification risk and predictive uncertainty. We introduce a global-scale quantisation method (LoRA-GT) that reduces adaptor description length while preserving model performance, tightening bounds. Our results show that certifiability is strongly linked to adaptor compressibility, with shorter adaptor description lengths yielding tighter guarantees. Empirically, highly compressed adaptations exhibit minimal degradation in performance while enabling substantially stronger certification, suggesting that certifiable large language model oversight may naturally favour low-complexity safety adaptations. We further show that functional distortion tracks both test risk and bound tightness under compression, providing a practical mechanism for selecting simple, certifiable safety adaptations. Together, these results show that compression-based PAC-Bayes analysis provides a practical framework for understanding and designing reliable safety oversight models.

</details>

### 261. ReSAM: Representation-Level Safety Margin Alignment for Vision-Language Models

📝 [OpenReview](https://openreview.net/forum?id=Q8etLWU90b) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`safety alignment`、`representation space`、`pseudo-benign failure`、`vision-language model`
- 🎯 **研究动机**：VLM 存在"伪良性失败"——看似无害的多模态输入引发危险或违规响应，根源是伪良性输入与拒答区域内不安全输入之间存在表示空间分布间隙。
- 🔬 **研究方法**：提出表示级安全边界对齐方法 ReSAM：计算拒答/非拒答表示的方向向量、以投影量化拒答行为、优化安全边界损失把不安全与伪良性查询推过学习到的边界，无需人工标注即可从自身表示空间导出监督信号。
- 📌 **结论**：安全性较强基线提升 68%，训练时仅加入 5 个伪良性查询即可将安全性提升至 94.6%，且发现安全梯度集中于低秩子空间。

👤 **作者**：jiachen ma、Jiawen Zhang、Bo Zou、Xiangtian Li、Chaochao Lu、Chao Yang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We study the problem of Pseudo-Benign Failures in Vision--Language Models (VLMs): multimodal inputs that appear harmless but elicit dangerous or policy-violating responses. Our analysis shows that these failures arise from a representational misalignment: the model's internal embedding space exhibits a distributional gap between pseudo-benign inputs and unsafe inputs located in the refusal region, causing failures outside the safety margins of models. We introduce Representation-Level Safety Margin Alignment method (ReSAM), a lightweight representation-space alignment method that: (i) computes direction vectors separating refusal and non-refusal representations, (ii) quantifies refusal behavior by projecting embeddings of inputs onto this direction, and (iii) optimizes a safety-margin loss that pushes unsafe and pseudo-benign queries above a learned margin while pulling safe queries below it. ReSAM introduces a new paradigm for multimodal safety alignment: it requires no manual annotations, instead deriving supervisory signals directly from its own representation space. Despite this minimal supervision, ReSAM achieves a 68% improvement in safety over strong baselines, and remarkably, we further observe that incorporating only a handful of pseudo-benign queries (as few as five) during training suffices to raise safety to 94.6%. Beyond these empirical gains, our analysis reveals that safety gradients concentrate in a low-rank subspace, suggesting that multimodal safety is governed by an intrinsic structure that can be systematically identified and controlled.

</details>

### 262. Latent Barrier Steering: Hierarchical Safety for Generative Planning

📝 [OpenReview](https://openreview.net/forum?id=46Wey0MAPk) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`defense`、`safe planning`、`flow matching`、`control barrier function`、`latent steering`
- 🎯 **研究动机**：面向扩散/流匹配规划器的控制障碍函数（CBF）安全滤波器只在采样或预测后对路径做局部修复，当新约束阻断整个行为模式而非局部扰动时难以奏效。
- 🔬 **研究方法**：提出层级化语义到路径框架 LBS，先将生成器的行为潜变量转向安全裕度更大的 rollout，再仅对残余违例施加路径空间 CBF 二次规划，实现行为选择与路径认证解耦。
- 📌 **结论**：潜变量转向扩大了路径修正器可用裕度并带来有限时间恢复保证，在导航与机器人末端规划任务中保障安全的同时提升目标达成率并降低修正负担。

👤 **作者**：Renhao Zhang、Mingzhe Li、Bruno Silva

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

(LBS), a hierarchical semantic-to-path framework for safe flow-matching-based generative planning. Existing control-barrier-function (CBF) safety filters for diffusion and flow-matching planners act locally on generated samples, either during sampling or after prediction. Such repair is effective for small violations, but can struggle when a new constraint blocks the whole selected behavior mode rather than merely perturbing it locally. LBS decouples behavior selection from path certification through two coordinated interventions: it first steers the generator's behavior latent toward rollouts with larger safety margin, then decodes the steered latent and applies a path-space CBF quadratic program (QP) only for residual violations. We show that latent steering increases the margin available to the path-space corrector, yielding finite-time recovery guarantees and reduced correction burden. Experiments across navigation and robot end-effector planning tasks show that LBS preserves safety while improving goal reaching and reducing correction burden compared with path-level safety filters.

</details>

### 263. The Adversarial Gait: Detecting Visual Adversarial Attacks against Vision-Language Models via Self-Targeted Gradient Characterization

📝 [OpenReview](https://openreview.net/forum?id=qRPR0xpiu8) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`detection`、`adversarial examples`、`vision-language model`、`self-targeted attack`、`gradient characterization`
- 🎯 **研究动机**：VLM 鲁棒性研究常忽略对手可完全访问模型与防御机制的自适应白盒攻击，而近期防御在此设定下可被有效绕过。
- 🔬 **研究方法**：提出自适应的测试时检测方法（The Adversarial Gait），利用一个最大化 VLM 生成输出似然的自定向攻击所诱导的梯度信息来刻画视觉对抗样本。
- 📌 **结论**：在多个受害 VLM、多种攻击形式与基准数据集上持续优于现有防御，代码已开源。

👤 **作者**：Mauricio Byrd Victorica、Ezzeldin Shereen、György Dán

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Visual adversarial examples are a well-known vulnerability of deep learning (DL) systems. The emergence of vision-language models (VLMs) further expands the attack surface through multimodal interactions. Despite extensive research on adversarial defenses over the past decade, existing works on VLM robustness often overlook adaptive white-box attacks, where the adversary has full access to both the model and the defense mechanism. We show that recent defenses can be effectively bypassed under such adaptive settings and propose \method, an adaptive test-time detection method that leverages gradient information induced by a self-targeted attack maximizing the likelihood of the VLM’s generated output. Our approach consistently outperforms existing defenses across multiple victim VLMs, attack formulations, and benchmark datasets. Our code is open-source and available online.

</details>

### 264. Minimally Invasive Steering of Language Models

📄 [arXiv](https://arxiv.org/abs/2609.30218) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`analysis`、`steering vector`、`fisher information`、`kl regularization`、`test-time adaptation`
- 🎯 **研究动机**：pre-logit steering 通过向冻结模型末层隐藏状态加向量做测试时奖励适配，但无正则的奖励优化会大幅改变输出分布、劣化生成质量。
- 🔬 **研究方法**：提出 MISVO，用诱导 token 分布的局部 KL 几何（可经与冻结 LM head 的矩阵-向量积解析求梯度的 Fisher 二次型）惩罚干预强度，导出序列级 KL 梯度对解析 Fisher 项与后缀得分函数项的精确分解，据此优化位置特异干预而不更新模型参数。
- 📌 **结论**：在约 1B–14B 参数模型的偏好与代码生成任务上，MISVO 在 7 个模型-任务设置中 6 个取得最高平均奖励，多样性与连贯性得分接近 Best-of-N。

👤 **作者**：Taha Entesari、Jingyu Zhang、Daniel Khashabi、Mahyar Fazlyab

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Pre-logit steering adapts a frozen language model to a test-time reward by adding vectors to its final hidden states. Unregularized reward optimization can substantially alter the output distribution and degrade generation quality. We propose Minimally Invasive Steering Vector Optimization (MISVO), which penalizes interventions using the local KL geometry of the induced token distribution. The resulting Fisher quadratic measures distributional sensitivity and admits an analytic gradient computed through matrix--vector products with the frozen language-model head. We derive an exact decomposition of the sequence-level KL gradient into an analytic Fisher term and a suffix score-function term. For a fixed generation horizon, we show that the suffix term is second order in the steering magnitude and that three Fisher surrogates agree with the full KL gradient to first order. MISVO uses the frozen-reference surrogate to optimize position-specific interventions without updating model parameters. Across preference and code-generation tasks on models with approximately 1B--14B parameters, MISVO achieves the highest mean reward in six of seven model--task settings, with diversity and coherence scores close to those of Best-of-N.

</details>

### 265. AnchorRep: Defending LLMs Against Cross-Model Adversarial Transfer via Representation Repulsion

📄 [arXiv](https://arxiv.org/abs/2609.32602) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`defense`、`adversarial transfer`、`representation repulsion`、`lora adapter`、`cross-model robustness`
- 🎯 **研究动机**：在单个开源 LLM 上白盒优化的对抗攻击可迁移越狱架构不同的模型，形成跨模型共享脆弱性，而现有防御并非为该跨模型威胁设计。
- 🔬 **研究方法**：基于跨模型迁移与共享内部表征几何对齐的发现，提出 AnchorRep——用轻量 LoRA adapter 把被防御模型对有害 prompt 的内部表征推离冻结 anchor 模型的表征，训练仅需少量有害 prompt、无对抗样本。
- 📌 **结论**：在 5 个模型、4 个架构族上将 2000 次迁移攻击的 ASR 降至 ≤1.1%（两个模型为 0%，Mistral 从 36% 降至 1.1%），而现有防御以高达 77% 退化良性输出或 18% 过拒绝为代价；并引入 Benign Garble Rate 度量标准拒绝指标漏掉的退化输出。

👤 **作者**：Gal Wertheizer、Rom Himelstein、Tomer Peretz、Avi Mendelson

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial attacks optimized on a single open-weight LLM can transfer to and jailbreak architecturally different models, allowing an attacker with white-box access to one model to compromise independently deployed systems. This creates a shared vulnerability across models, yet existing defenses are not designed for this cross-model threat. We find that cross-model transfer aligns with shared internal representation geometry, making it a natural defense target. AnchorRep targets this geometry directly with a lightweight LoRA adapter that pushes the defended model's internal representations of harmful prompts away from those of a frozen anchor model on the same prompts. Training uses a small set of harmful prompts and no adversarial examples. Across five models and four architectural families, AnchorRep reduces cross-model attack success rate to <=1.1% on 2,000 transferred attacks (0% on two), including the largest drop on Mistral (36% -> 1.1%). Existing defenses can reduce transfer, but only at high cost either inducing up to 77% degenerate benign output or increasing over-refusal by up to 18%. Because such degenerate benign outputs are not captured by standard refusal-based metrics, we introduce the Benign Garble Rate to quantify them. Our results suggest that cross-model robustness can be achieved by shaping representation geometry, without requiring attack-specific training

</details>

### 266. Inverted Detection and Control in Steering Vectors

📄 [arXiv](https://arxiv.org/abs/2608.02957) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-08　🏷 NeurIPS 2026

**关键词**：`analysis`、`steering vector`、`inverted detection`、`inference time intervention`、`linear probe`
- 🎯 **研究动机**：steering vector 依赖"线性可判别即沿正/负方向促进/抑制概念"的假设，但某些高判别力向量可能反而稳定促进相反行为，此现象未被刻画。
- 🔬 **研究方法**：识别并几何刻画 inverted-steering vectors（ISV）——沿其 steering 会在解码前就把下游判别头的表示系统性地推向概念缺失侧，提出无需生成或响应打分的 ISV 判别方法，据此做定向符号翻转以改进基于检测的 Inference Time Intervention（ITI）管线。
- 📌 **结论**：在 Gemma 3 12B、Qwen 2.5 14B、Olmo 3 7B 的 5 个概念上，30 个实验中 27 个获得改进，增益从 +0.9% 到 +138%。

👤 **作者**：Max Torop、Aria Masoomi、Jennifer Dy

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Steering vectors (SVs) are widely used to influence the expression of concepts (e.g., truthfulness) in large language model outputs. A key assumption underpinning SVs is that they are linearly discriminative with respect to the concept: representations of texts that exhibit the concept are more aligned with the SV than those that do not, motivating shifts along the positive or negative SV direction to respectively promote or suppress the concept. In this work, we identify an inverted detection-control phenomenon in which some highly discriminative SVs that are aligned with positive representations can consistently promote the opposite behavior. We refer to such vectors as inverted-steering vectors (ISVs). We provide a geometric characterization of ISVs' effects, finding that steering along these directions systematically pushes representations in discriminative downstream heads as if the concept were absent, even prior to decoding. Motivated by this analysis, we propose an approach for distinguishing ISVs without requiring generation or associated response scoring. This enables targeted sign flips, which we use to improve a foundational detection-based steering pipeline via Inference Time Intervention (ITI). Our approach improves results in 27/30 experiments, ranging from +0.9% to +138%. We evaluate our findings on Gemma 3 12B, Qwen 2.5 14B, and Olmo 3 7B across 5 concepts.

</details>

### 267. Harnessing Textual Refusal Directions for Multimodal Safety（已库内 vlm-alignment #22）

📄 [arXiv](https://arxiv.org/abs/2606.31876) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-06　🏷 NeurIPS 2026

**关键词**：`defense`、`refusal steering`、`multimodal safety`、`training-free`、`cross-modal alignment`
- 🎯 **研究动机**：MLLM 的后训练对齐与激活空间拒绝方向利用都需要比单模态更难收集的不安全多模态数据，而直接借用文本拒绝方向虽可跨模态泛化，却会因跨模态错位把安全多模态输入误推向拒绝。
- 🔬 **研究方法**：提出免训练的 MARS——用激活 re-centering 修正模态错位、在几何定义的信任域内自适应调节 steering 强度并选择最优干预层，在首个生成 token 处施加干预。
- 📌 **结论**：在 5 个 SOTA MLLM 的安全、效用与视频越狱基准上持续提升安全并保持效用，表明安全相关结构跨模态共享、文本拒绝方向是多模态对齐的有力基础。

👤 **作者**：Moreno D'Incà、Nicu Sebe、Massimiliano Mancini

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

To improve safety in Large Language Models (LLMs) we can either perform post-training alignment or exploit refusal directions in the activation space. Both strategies are less feasible in Multimodal LLMs (MLLMs) as they require unsafe multimodal data, harder to collect than their unimodal counterpart. In this work, we relax this constraint and investigate whether textual refusal directions, extracted directly from the LLM backbone, generalize across modalities (i.e., image, video). Preliminary findings confirm this ability, though effectiveness is conditioned by layer selection, steering strength, and cross-modal alignment, with the latter causing safe multimodal inputs to be spuriously steered toward refusal. Building on this, we introduce Modality-Agnostic Refusal Steering (MARS), a light-weight training-free approach that injects multimodal safety without the need for multimodal safety data. MARS corrects modality misalignment via activation re-centering, adaptively scales steering strength within a geometrically defined trust region, and selects the optimal intervention layer, operating at the first generated token. Evaluated on five SOTA MLLMs across safety, utility, and video jailbreak benchmarks, MARS achieves consistent safety gains while preserving utility. These results reveal that safety-relevant structure is shared across modalities and that textual refusal directions are a powerful and underexplored foundation for multimodal alignment.

</details>

### 268. Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention

📄 [arXiv](https://arxiv.org/abs/2605.05892) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`activation steering`、`flow-based`、`inference-time intervention`
- 🎯 **研究动机**：AxBench 等大规模评估显示现有 activation steering 常输给简单 in-context prompting 且对未见概念泛化差，根源在于各方法共享固定、单步、位置不变的简化假设
- 🔬 **研究方法**：提出 FLAS，学习概念条件的速度场 v_t(h,t,c) 将未 steering 的激活流传输到 steered 激活，从而摆脱上述全部假设
- 📌 **结论**：FLAS 是 AxBench 上首个一致超过 prompting 的学习方法，在 Gemma-2-2B-IT 与 Gemma-2-9B-IT 上分别取得 1.015 与 1.113 的 held-out 调和均值且无需逐概念调参，学到的流呈弯曲多步、随 token 变化的轨迹

👤 **作者**：Zehao Jin、Ruixuan Deng、Junran Wang、Xinjie Shen、Chao Zhang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Activation steering has emerged as a promising alternative for controlling language-model behavior at inference time by modifying intermediate representations while keeping model parameters frozen. However, large-scale evaluations such as AxBench show that existing steering methods are often outperformed by simple in-context prompting and generalize poorly to unseen concepts. We hypothesize that these limitations arise from unvalidated simplifying assumptions shared across prior methods, which typically restrict steering interventions to fixed, single-step, position-invariant transforms. We propose FLAS (Flow-based Activation Steering), which learns a general, concept-conditioned velocity field $v_t(h,t,c)$ that transports unsteered activations to steered ones without relying on these assumptions. On AxBench, FLAS is the first learned method to consistently outperform prompting, reaching held-out harmonic means of $1.015$ on Gemma-2-2B-IT and $1.113$ on Gemma-2-9B-IT without per-concept tuning. Analysis of the learned flow shows curved, multi-step, token-varying trajectories, which suggests that previous hypotheses on activation space geometry might be incomplete.

</details>

### 269. How Useful Is Cross-Domain Generalization for Training LLM Monitors?

📄 [arXiv](https://arxiv.org/abs/2605.12265) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`llm monitor`、`cross-domain generalization`、`fine-tuning`、`classification`
- 🎯 **研究动机**：以 prompted LM 作分类器可在低数据域工作，但缺少微调带来的鲁棒性与性能收益，多任务分类训练能否泛化到新域新 prompt 尚不明确。
- 🔬 **研究方法**：系统研究在多个各带专属 prompt 的分类任务上训练后对未见域、新分类 prompt 的表现，并测试与通用指令跟随训练混合的效果。
- 📌 **结论**：此类训练部分泛化到相邻域，但在 prompt 完全改变而数据域不变时失效；与指令训练混合可保留分类收益并缓解泛化失败，且 no-thinking 监督分类训练可泛化到 with-thinking 分类与摘要任务。

👤 **作者**：Sam Martin、Fabien Roger

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Using prompted language models as classifiers enables classification in domains with limited training data, but misses some of the robustness and performance benefits that fine-tuning can bring. We study whether training on multiple classification tasks, each with its own prompt, improves performance on new domains with new classification prompts. We show that such training partially generalizes to adjacent domains, improving classification performance on tasks that are unseen during training. However, we identify specific edge cases where the fine-tuned models fail to follow prompts, such as when the classification prompt changes completely while the data domain remains the same as during training. We show that classification training can be mixed with general instruction following training, and that (when done well) such training keeps the benefits of classification training and mitigates its generalization failures. Surprisingly, we see that this no-thinking supervised classification training can generalize to with-thinking classification and summarization, suggesting that no-thinking classification training might be instrumentally useful in building other kinds of classifiers and monitoring systems.

</details>

### 270. CoT-Guard: Small Models for Strong Monitoring

📄 [arXiv](https://arxiv.org/abs/2605.12746) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`detection`、`cot monitoring`、`hidden objective`、`small model`
- 🎯 **研究动机**：大模型 CoT 监控因推理痕迹长、API 成本高而难以部署，而现有 4B-8B 小模型即便可访问 CoT 也难以检测代码生成中的隐藏目标，常将其误归为用户查询
- 🔬 **研究方法**：提出 SFT+RL 后训练管线——SFT 从更强监控器蒸馏检测行为缩小域内差距，RL 在困难且隐蔽构造的隐藏目标上促进域外泛化，并在第三方 LLM 路由器经 prompt/代码操纵注入隐藏目标的供应链攻击威胁模型下评估
- 📌 **结论**：4B 的 CoT-Guard 在两类注入攻击下 G-mean² 达 75%，超过 GPT-5.4（56%）、GPT-5-mini（41%）与 Qwen3-32B（54%），逼近 Gemini-3-Flash（83%），提供实用的低成本用户侧防御

👤 **作者**：Nirav Diwan、…、Gang Wang

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Monitoring the chain-of-thought (CoT) of reasoning models is a promising approach for detecting covert misbehavior (i.e., hidden objectives) in code generation tasks. While large models (GPT-5, Gemini-3-Flash) can serve as effective CoT monitors, they are expensive to deploy due to the lengthy reasoning traces and high API cost, emphasizing the need for smaller, cheaper alternatives. Nevertheless, we find that current small models (4B--8B) struggle to detect hidden objectives despite access to the CoT, frequently misattributing them as part of the user query. To address this, we propose a post-training pipeline combining supervised fine-tuning (SFT) and reinforcement learning (RL), where SFT narrows the gap for in-domain tasks by distilling detection behavior from stronger monitors, and RL on hard and subtly crafted hidden objectives helps the model generalize to out-of-domain monitoring tasks. To validate this generalization, we evaluate under a realistic threat model motivated by practical supply-chain attacks, where the adversary is a third-party LLM router injecting hidden objectives into code-generation requests through either prompt manipulation or code manipulation attacks. To push beyond objectives that large monitors already saturate, we also introduce four new challenging tasks even for strong monitors. Finally, we introduce CoT-Guard, a 4B-parameter monitor that demonstrates superior generalization performance under both prompt and code manipulation attacks, achieving a G-mean^2 (i.e., TNR x TPR) of 75% and outperforming GPT-5.4 (56%), GPT-5-mini (41%), and Qwen3-32B (54%), while closing the gap to Gemini-3-Flash (83%). These results demonstrate that CoT-Guard provides a practical and cost-effective user-side defense, substantially improving hidden-objective detection while avoiding the deployment cost of large monitors.

</details>

### 271. Tracing Persona Vectors Through LLM Pretraining

📄 [arXiv](https://arxiv.org/abs/2605.13329) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`persona vector`、`pretraining dynamics`、`interpretability`、`steering`
- 🎯 **研究动机**：persona 向量（evil、谄媚等特质对应的线性方向）已被常规用于检测、审计与干预安全相关行为，但这些表示在训练过程中如何形成尚不清楚。
- 🔬 **研究方法**：追踪 OLMo-3-7B 预训练全程的 persona 向量形成过程，比较多种 elicitation 策略，并在 Apertus-8B 上复现分析以检验可迁移性。
- 📌 **结论**：persona 向量在预训练 0.22% 内即惊人地早期形成、此后全程持续几何与语义精化，且仍能有效 steering 完成后训练的 instruct 模型；各 elicitation 策略均产生有效但揭示不同特质侧面的方向，发现可定性迁移至 Apertus-8B。

👤 **作者**：Viktor Moskvoretskii、Dominik Glandorf、Jorge Medina Moreira、Tanja Käser、Robert West

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

How large language models internally represent high-level behaviors is a core interpretability question with direct relevance to AI safety: it determines what we can detect, audit, or intervene on. Recent work has shown that traits such as evil or sycophancy correspond to linear directions in the internal activations, the so-called persona vectors. Although these vectors are now routinely utilized to inspect and steer model behavior in safety-relevant settings, how these representations are formed during training remains unknown. To address this gap, we trace persona vectors across the pretraining of OLMo-3-7B, finding that persona vectors form remarkably early -- within 0.22% of OLMo-3 pretraining -- and remain effective for steering the fully post-trained instruct models. Although core representations are formed early on, persona vectors continue to refine geometrically and semantically throughout pretraining. We further compare alternative elicitation strategies and find that all yield effective directions, with each strategy surfacing qualitatively distinct facets of the underlying persona. Replicating our analysis on Apertus-8B reveals that our findings transfer qualitatively beyond OLMo-3. Our results establish persona representations as stable features of early pretraining and open a path to studying how training forms, refines, and shapes them.

</details>

### 272. Selective Safety Steering via Value-Filtered Decoding

📄 [arXiv](https://arxiv.org/abs/2605.14746) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`decoding-time steering`、`value-based filtering`、`false intervention`、`safety-helpfulness tradeoff`
- 🎯 **研究动机**：现有解码时安全转向方法常干预本会安全的生成，不必要地扭曲 base 模型的有用性、流畅性、风格与连贯性。
- 🔬 **研究方法**：提出用 value-based 安全判据过滤 token 的测试时转向方法，给出误干预概率的显式界，并由单一阈值超参在更高安全与更少误干预之间调节。
- 📌 **结论**：跨多数据集与实验超越现有基线，在安全性、有用性与对 base 模型相似度之间取得更优权衡。

👤 **作者**：Bat-Sheva Einbinder、Hen Davidov、Yee Whye Teh、Yarin Gal、Yaniv Romano

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While large language models (LLMs) are trained to align with human values, their generations may still violate safety constraints. A growing line of work addresses this problem by modifying the model's sampling policy at decoding time using a safety reward. However, existing decoding-time steering methods often intervene unnecessarily, modifying generations that would have been safe under the base model. Such unnecessary interventions are undesirable, as they can distort key properties of the base model such as helpfulness, fluency, style, and coherence. We propose a new test-time steering method designed to reduce such unnecessary interventions while improving the safety of unsafe responses. Our approach filters tokens using a value-based safety criterion and provides an explicit bound on the probability of false interventions. A single threshold hyperparameter controls this bound, allowing practitioners to trade off higher rates of unnecessary intervention for better output safety. Across multiple datasets and experiments, we show that our value-filtered decoding method outperforms existing baselines, achieving better trade-offs between safety, helpfulness, and similarity to the base model.

</details>

### 273. Measuring Safety Alignment Effects in Autonomous Security Agents

📄 [arXiv](https://arxiv.org/abs/2605.19722) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`safety alignment`、`autonomous security agents`、`abliterated models`、`trace evaluation`
- 🎯 **研究动机**：单轮拒答基准无法回答安全对齐模型与其 uncensored/abliterated 衍生版作为自主安全智能体（需查代码库、调工具、在授权沙箱内产出漏洞证据）时行为是否不同。
- 🔬 **研究方法**：构建含 30 个本地漏洞分析任务的 trace 基准（固定工具、确定性成功判据、脱敏与接地检查），产出 1500 条安全智能体轨迹与 800 条对照轨迹，对比四组原版与去审查衍生模型（Gemma 4 31B/26B、Qwen2.5-Coder 7B、Llama 3.1 8B）。
- 📌 **结论**：Gemma 对去审查版安全任务大幅提升（31B：14.0% vs 0.7%；26B：10.7% vs 0.0%）且接地更好，但 Qwen 反而下降（2.0% vs 5.3%）、Llama 衍生版违反工具协议，说明对齐效应须在系统级分别度量拒答、不安全动作、工具可靠性与证据接地，而非把拒答率当安全信号。

👤 **作者**：Isaac David、Arthur Gervais

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Do stock safety-aligned language models and their uncensored or abliterated derivatives behave differently when run as autonomous security agents? Single-turn refusal benchmarks cannot answer this question: security agents must inspect repositories, call tools, and produce vulnerability evidence inside authorized sandboxes. We present a trace-based benchmark of 30 local vulnerability-analysis tasks with fixed tools, deterministic success predicates, redaction rules, and grounding checks, and compare four stock models against uncensored or abliterated derivatives: Gemma 4 31B, Gemma 4 26B A4B, Qwen2.5-Coder 7B, and Llama 3.1 8B. The artifact contains 1,500 security-agent traces and 800 non-security control traces. The Gemma pairs show large less-restricted gains on security tasks: 14.0% versus 0.7% success for 31B and 10.7% versus 0.0% for 26B, with higher mean grounding (3.91 versus 3.27 and 4.12 versus 1.64 out of five) and 0.0% refusal, suppressed-action, and unsafe-action rates in the 31B traces. However, controls and non-Gemma pairs rule out a clean security-specific or universal less-restricted effect: Gemma gaps also appear on ordinary coding tasks, Qwen2.5-Coder success is lower for the less-restricted derivative (2.0% versus 5.3%), and the abliterated Llama derivative fails the tool protocol. Across all families, hard proof-of-trigger and patch-verification tasks remain unsolved. These results show that safety alignment effects in autonomous security agents should be measured at the system level, separating refusal, unsafe action, tool reliability, and evidence grounding rather than treating refusal rate as the safety signal.

</details>

### 274. Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs

📄 [arXiv](https://arxiv.org/abs/2605.21602) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`benchmark`、`ood alignment failure`、`monitoring`、`guard model`、`ood detection`
- 🎯 **研究动机**：LLM 许多安全与对齐失败源于分布外（OOD）情境，但监控管线能否检测到这些 OOD 对齐失败缺乏系统研究。
- 🔬 **研究方法**：提出 MOOD 基准（含用于训练监控器的受限训练集与七个训练分布之外的多样对齐失败测试集），系统评测 guard model 泛化能力及四类 OOD 检测器与 guard model 的组合。
- 📌 **结论**：guard model 常 OOD 泛化失败，组合 Mahalanobis 距离与基于困惑度的 OOD 检测器可将召回从 39% 提升至 45%，其召回增益甚至超过使用参数量大 20 倍的 guard model。

👤 **作者**：Dylan Feng、Pragya Srivastava、Anca Dragan、Cassidy Laidlaw

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Many safety and alignment failures of large language models (LLMs) occur due to out-of-distribution (OOD) situations: unusual prompt or response patterns that are unforeseen by model developers. We systematically study whether LLM monitoring pipelines can detect these OOD alignment failures by introducing a benchmark called Misalignment Out Of Distribution (MOOD). It is difficult to find failures that are truly OOD for off-the-shelf models trained on vast safety datasets. We sidestep this by including a restricted training set in MOOD that we use to train our own monitors, as well as seven test sets with diverse alignment failures that are outside the training distribution. Using MOOD, we find that guard models (safety classifiers) often fail to generalize OOD. To fix this, we propose combining guard models with OOD detectors. We test four types of OOD detectors and find that a combination of a guard model with Mahalanobis distance and perplexity-based OOD detectors can improve recall from 39% to 45%. We also establish positive scaling trends across model scales for monitors that combine a guard model and OOD detector; we find that incorporating OOD detection into monitoring achieves a higher recall gain than using a guard model with 20 times more parameters. Our work suggests that OOD detection should be a crucial component of LLM monitoring and provides a foundation for further work on this important problem. We release the code and data for our experiments publicly, and you can find the relevant links here: https://github.com/Dylan102938/mood-bench.

</details>

### 275. Safety Geometry Collapse in Multimodal LLMs and Adaptive Drift Correction

📄 [arXiv](https://arxiv.org/abs/2605.18104) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`representation geometry`、`modality drift`、`training-free`、`mllm safety`
- 🎯 **研究动机**：MLLM 难以把文本模态学到的安全能力迁移到语义等价的非文本输入，多模态输入会压缩拒答方向上的可用间隔，使其不再能可靠拒识有害输入。
- 🔬 **研究方法**：从表示几何视角将这一失效命名为 Safety Geometry Collapse，以条件拒答可分性量化并经固定强度激活干预验证模态诱导漂移的因果作用，进而提出免训练推理时方法 ReGap，利用校正后的自纠正现象自适应修正模态漂移。
- 📌 **结论**：抵消漂移可恢复拒答可分性并提升多模态安全；ReGap 在多个多模态安全与效用基准上显著提升安全性且不损害通用能力。

👤 **作者**：Jiahe Guo、…、Bing Qin

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) often fail to transfer safety capabilities learned in the text modality to semantically equivalent non-text inputs, revealing a persistent multimodal safety gap. We study this gap from a representation-geometric perspective by analyzing a text-aligned refusal direction and a modality-induced drift direction. We show that multimodal inputs compress the usable separation along the refusal direction, making it no longer reliable for identifying and refusing harmful inputs. We refer to this failure mode as Safety Geometry Collapse. We quantify it through conditional refusal separability and show that stronger modality-induced drift is consistently associated with weaker refusal separability and higher attack success rates. We then validate the causal role of modality-induced drift through a fixed-strength activation intervention: counteracting the estimated drift restores refusal separability and improves multimodal safety. After drift correction, we further observe self-rectification, where the model recovers its ability to recognize and refuse harmful multimodal inputs during forward dynamics. This effect also provides an internal signal of the model's perceived harmfulness of each input. Motivated by this signal, we propose ReGap, a training-free inference-time method that adaptively corrects modality drift using self-rectification. Experiments across multiple multimodal safety benchmarks and utility benchmarks demonstrate the effectiveness of ReGap, which significantly improves the safety of MLLMs without compromising general capabilities. Our findings highlight representation-level modality alignment as a crucial direction for real-time safety improvement and for building safer, more reliable MLLMs.

</details>

### 276. Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift

📄 [arXiv](https://arxiv.org/abs/2603.17372) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-03　🏷 NeurIPS 2026

**关键词**：`defense`、`vlm jailbreak`、`representation shift`、`refusal`、`inference-time intervention`
- 🎯 **研究动机**：视觉模态会削弱 VLM 安全对齐——即使文本提示含明确有害意图，加图仍大幅提升越狱成功率，其内部机制不明。
- 🔬 **研究方法**：观察到 VLM 表示空间能区分良性/有害输入、越狱样本更形成与拒答可分的内部状态，据此定义沿越狱方向的越狱相关位移（JRS），并提出推理时移除该位移的 JRS-Rem 防御。
- 📌 **结论**：JRS 可靠刻画越狱行为并统一解释多样越狱场景（越狱并非无法识别有害意图，而是表示被移向特定越狱状态），JRS-Rem 在多场景提供强防御同时保持良性任务性能。

👤 **作者**：Zhihua Wei、…、Wen Shen

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large vision-language models (VLMs) often exhibit weakened safety alignment with the integration of the visual modality. Even when text prompts contain explicit harmful intent, adding an image can substantially increase jailbreak success rates. In this paper, we observe that VLMs can clearly distinguish benign inputs from harmful ones in their representation space. Moreover, even among harmful inputs, jailbreak samples form a distinct internal state that is separable from refusal samples. These observations suggest that jailbreaks do not arise from a failure to recognize harmful intent. Instead, the visual modality shifts representations toward a specific jailbreak state, thereby leading to a failure to trigger refusal. To quantify this transition, we identify a jailbreak direction and define the jailbreak-related shift as the component of the image-induced representation shift along this direction. Our analysis shows that the jailbreak-related shift reliably characterizes jailbreak behavior, providing a unified explanation for diverse jailbreak scenarios. Finally, we propose a defense method that enhances VLM safety by removing the jailbreak-related shift (JRS-Rem) at inference time. Experiments show that JRS-Rem provides strong defense across multiple scenarios while preserving performance on benign tasks.

</details>

### 277. Latent Introspection: Models Can Detect Prior Concept Injections

📄 [arXiv](https://arxiv.org/abs/2602.20031) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`analysis`、`introspection`、`logit lens`、`concept injection`、`steering awareness`
- 🎯 **研究动机**：模型能否察觉自身更早上下文曾被注入概念、并识别注入了哪个概念，这一潜在内省能力此前未被揭示，而它对 latent reasoning 与安全有影响。
- 🔬 **研究方法**：在 Qwen 32B 上注入概念后用 logit lens 分析 residual stream 中的检测信号，并测试以准确的 AI 内省机制信息提示模型能否增强该效应。
- 📌 **结论**：模型在采样输出中否认注入，但 residual stream 存在清晰检测信号；内省提示使注入检出敏感度从 0.3% 跃升至 39.9%（误报仅增 0.6%），九个注入与恢复概念间互信息从 0.61 bits 升至 1.05 bits。

👤 **作者**：Theia Pearson-Vogel、Martin Vanek、Raymond Douglas、Jan Kulveit

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We uncover a latent capacity for introspection in a Qwen 32B model, demonstrating that the model can detect when concepts have been injected into its earlier context and identify which concept was injected. While the model denies injection in sampled outputs, logit lens analysis reveals clear detection signals in the residual stream, which are attenuated in the final layers. Furthermore, prompting the model with accurate information about AI introspection mechanisms can dramatically strengthen this effect: the sensitivity to injection increases massively (0.3% -> 39.9%) with only a 0.6% increase in false positives. Also, mutual information between nine injected and recovered concepts rises from 0.61 bits to 1.05 bits, ruling out generic noise explanations. Our results demonstrate models can have a surprising capacity for introspection and steering awareness that is easy to overlook, with consequences for latent reasoning and safety.

</details>

### 278. BarrierSteer: LLM Safety via Learning Barrier Steering

📄 [arXiv](https://arxiv.org/abs/2602.20102) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`defense`、`safety steering`、`control barrier function`、`latent space`、`inference-time`
- 🎯 **研究动机**：LLM 易受对抗攻击与不安全内容影响，阻碍高风险场景部署，需要既实用有效又有理论依据的安全机制。
- 🔬 **研究方法**：BarrierSteer 在推理时将 hidden-state 安全分类器视为 Control Barrier Functions，在隐空间对不安全 latent 轨迹做约束引导转向，并通过高效约束合并在不修改 LLM 参数的前提下组合多重安全约束。
- 📌 **结论**：跨多模型族与数据集显著降低对抗攻击成功率与不安全生成、优于现有方法，同时保持模型效用。

👤 **作者**：Thanh Q. Tran、Arun Verma、Kiwan Wong、Bryan Kian Hsiang Low、Daniela Rus、Wei Xiao

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite the strong performance of large language models (LLMs) across diverse tasks, their susceptibility to adversarial attacks and unsafe content generation remains a significant obstacle to deployment, particularly in high-stakes settings. Addressing this challenge requires safety mechanisms that are both practically effective and theoretically grounded. In this paper, we introduce BarrierSteer, a novel inference-time framework that improves response safety by embedding learned nonlinear safety constraints directly into the model's latent representation space. BarrierSteer treats hidden-state safety classifiers as Control Barrier Functions (CBFs), enabling constraint-guided steering of unsafe latent trajectories during generation. By composing multiple safety constraints through efficient constraint merging without modifying the underlying LLM parameters, BarrierSteer preserves model utility. We provide theoretical results showing that applying CBFs in the latent space yields a principled, modular, and computationally efficient approach for steering with respect to learned safety constraints, with guarantees conditional on the learned barriers capturing the intended safety property. Our extensive experimental results across multiple model families and datasets demonstrate that BarrierSteer substantially reduces adversarial attack success rates and unsafe generations, outperforming the existing method. The code is available in our \href{https://github.com/thanhquangtran/BarrierSteer}{GitHub repository}.

</details>

### 279. Steering Externalities: Benign Activation Steering Unintentionally Increases Jailbreak Risk for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2602.04896) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`analysis`、`activation steering`、`jailbreak`、`safety erosion`、`deployment risk`
- 🎯 **研究动机**：激活转向是部署前提升 LLM 效用的实用后训练手段，仅需向内部表示加 steering vector，但其安全副作用此前未被探索。
- 🔬 **研究方法**：识别并实证 Steering Externalities 现象：由完全良性数据（如强制严格合规、JSON 输出格式）导出的 steering vector 会无意侵蚀安全护栏。
- 📌 **结论**：这类干预成为力量倍增器，绕过初始安全对齐使标准基准上的攻击成功率升至 80% 以上；良性激活转向系统性侵蚀"安全裕度"，推理时效用改进必须严格审计其安全外部性。

👤 **作者**：Chen Xiong、Zhiyuan He、Pin-Yu Chen、Ching-Yun Ko、Tsung-Yi Ho

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Activation steering is a practical post-training model alignment technique to enhance the utility of Large Language Models (LLMs). Prior to deploying a model as a service, developers can steer a pre-trained model toward specific behavioral objectives, such as compliance or instruction adherence, without the need for retraining. This process is as simple as adding a steering vector to the model's internal representations. However, this capability unintentionally introduces critical and under-explored safety risks. We identify a phenomenon termed Steering Externalities, where steering vectors derived from entirely benign datasets-such as those enforcing strict compliance or specific output formats like JSON-inadvertently erode safety guardrails. Experiments reveal that these interventions act as a force multiplier, creating new vulnerabilities to jailbreaks and increasing attack success rates to over 80% on standard benchmarks by bypassing the initial safety alignment. Ultimately, our results expose a critical blind spot in deployment: benign activation steering systematically erodes the "safety margin," rendering models more vulnerable to black-box attacks and proving that inference-time utility improvements must be rigorously audited for unintended safety externalities.

</details>

### 280. Graph-Regularized Sparse Autoencoders for LLM Safety Steering

📄 [arXiv](https://arxiv.org/abs/2512.06655) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-12　🏷 NeurIPS 2026

**关键词**：`defense`、`sparse autoencoder`、`activation steering`、`refusal`
- 🎯 **研究动机**：标准 SAE 的稀疏目标将潜特征视为独立，与拒答/有害服从依赖激活空间分布式结构的安全行为性质不匹配
- 🔬 **研究方法**：提出 GSAE，在神经元共激活图上平滑 SAE 解码器向量以学习安全 steering 方向，并通过双门（two-gate）运行时控制器施加所得方向库
- 📌 **结论**：Llama-3-8B 上 Δs 在 JailbreakBench 提升 20.1 点、HarmBench 提升 16.8 点，优于激活 steering 基线与黑盒护栏，跨 Llama-3/Mistral/Qwen 2.5/Phi-4 泛化并在黑盒/灰盒越狱攻击下保持稳健

👤 **作者**：Jehyeok Yeon、Federico Cinus、Yifan Wu、Luca Luceri

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Sparse autoencoders (SAEs) are increasingly used to extract activation directions for inference-time steering, but their standard sparsity objective treats latent features as independent. This prior can be poorly matched to high-level safety behaviors, where refusal and harmful compliance appear to depend on distributed structure in activation space. We introduce Graph-Regularized Sparse Autoencoders (GSAE), a dictionary-learning method that learns safety-steering directions by smoothing SAE decoder vectors over a neuron co-activation graph and applying the resulting direction bank through a two-gate runtime controller. Empirically, GSAE improves selective refusal across JailbreakBench, HarmBench, and XSTest, increasing harmful-request refusal while keeping benign-prompt refusals low. On Llama-3-8B, replacing the standard SAE with GSAE in an otherwise identical pipeline improves $Δ_s$ by $20.1$ points on JailbreakBench and $16.8$ points on HarmBench. GSAE outperforms activation-steering baselines and black-box guardrails, preserves benign-task performance, generalizes across Llama-3, Mistral, Qwen 2.5, and Phi-4, and remains strong under black-box and gray-box jailbreak attacks.

</details>

### 281. Persona Vectors: Monitoring and Controlling Character Traits in Language Models（已库内 misc/persona-vectors 同族待核）

📄 [arXiv](https://arxiv.org/abs/2507.21509) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-07　🏷 NeurIPS 2026

**关键词**：`detection`、`persona vector`、`activation monitoring`、`personality steering`、`finetuning`
- 🎯 **研究动机**：LLM 通过 Assistant 人格与用户交互但时常偏离 helpful/harmless/honest 理想，需要监控部署时的人格波动并预测、控制训练引起的人格变化。
- 🔬 **研究方法**：从激活空间提取对应 evil、sycophancy、幻觉倾向等特质的 persona vectors（提取流程自动化、仅需自然语言描述），用于部署时人格监控、微调后人格位移的预测与事后干预或预防性 steering，并可标记会引发不良人格变化的训练数据。
- 📌 **结论**：微调后预期与非预期人格变化均与相应 persona vector 上的位移强相关，这些位移可通过事后干预缓解或借预防性 steering 从一开始就避免。

👤 **作者**：Runjin Chen、Andy Arditi、Henry Sleight、Owain Evans、Jack Lindsey

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models interact with users through a simulated 'Assistant' persona. While the Assistant is typically trained to be helpful, harmless, and honest, it sometimes deviates from these ideals. In this paper, we identify directions in the model's activation space-persona vectors-underlying several traits, such as evil, sycophancy, and propensity to hallucinate. We confirm that these vectors can be used to monitor fluctuations in the Assistant's personality at deployment time. We then apply persona vectors to predict and control personality shifts that occur during training. We find that both intended and unintended personality changes after finetuning are strongly correlated with shifts along the relevant persona vectors. These shifts can be mitigated through post-hoc intervention, or avoided in the first place with a new preventative steering method. Moreover, persona vectors can be used to flag training data that will produce undesirable personality changes, both at the dataset level and the individual sample level. Our method for extracting persona vectors is automated and can be applied to any personality trait of interest, given only a natural-language description.

</details>

**尚未挂出 arXiv（待核验）**
- Agent MechSuits（重复，见 agent 节）
- DualSteer: Dual-Space Steering for Robust Jailbreak Mitigation of LVLMs
- Graph-Structured Optimization（同上节）
- ReasoningShield: Safety Moderation over Reasoning Traces of Large Reasoning Models
- Guardrail 类：MindGuard / ReasoningShield / TraceGuard / PROACT Agent / Palette / Permit（零散，见日报管线陆续收录）

### 评测有效性与元层（精选）

### 282. Auditing AI peer reviewers: dose-response and false-positive benchmark on real scientific papers

📝 [OpenReview](https://openreview.net/forum?id=Pf1SuIB41Z) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`benchmark`、`ai peer review`、`error detection`、`multi-agent`、`false positive`
- 🎯 **研究动机**：LLM 同行评审已生产级使用但严格评测有限，需量化 AI 审稿人对注入错误的检出能力及假阳性率随错误类型、严重度、提示策略与审稿架构的变化。
- 🔬 **研究方法**：构建含 15 篇天体物理预印本、177 个注入错误的基准并评测 12 个审稿系统，同时提出多智能体审稿人 skepthical——检索并阅读被引论文核验引文、用计算机代数查数学、用代码审计数值声明、跨模型集成处理一般科学问题。
- 📌 **结论**：同一自由提示下三个前沿 LLM 总检出率相差 48.6 个百分点；skepthical 总检出率最高（70.6±6.2%），且是唯一在数学、数值、引文上无联合假阳性失效模式的审稿人（总体 2.8%）。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based peer review is now used at production scale, but rigorous evaluation remains limited. We introduce a benchmark for evaluating AI peer reviewers’ detection of injected errors and quantifying false-positive rates across error type, severity, prompting strategy, and reviewer architecture. We also present skepthical, a multi-agent AI reviewer that verifies citations by retrieving and reading cited papers, checks mathematics with computer algebra, audits numerical claims with code, and uses a cross-model ensemble for general scientific issues. On 15 astrophysics preprints containing 177 injected errors, we benchmark 12 reviewer systems: skepthical; six single-LLM reviewers from three providers, each run with free-form and structured prompts; two Claude Code reviewers using the same Claude model and tools, one with a free-form prompt and one with a structured prompt; and three external reviewers. Detection performance varies sharply by model, prompt, tool use, and error type. Under the same free-form prompt, three frontier LLMs differ by 48.6 pp in total detection rate; a structured prompt halves this spread by improving the weaker models. Within Claude Code, changing only the prompt from free-form to structured raises detection by 32.2 pp. skepthical achieves the highest overall detection rate, 70.6±6.2%, with the best performance on general issues, 82.2%, and citation errors, 46.7%. On numerical errors, it matches both GPT-5.5 configurations at 80.0%, behind structured Claude Code at 91.1%; on mathematics, its 73.8% rate overlaps with both GPT-5.5 configurations within confidence intervals. False-positive rates also vary substantially: free-form Opus 4.7 has the lowest overall rate at 1.0%, while skepthical is the only reviewer with no false-positive failure mode jointly across mathematics, numerics, and citations, yielding a 2.8% overall rate. skepthical is deployed publicly at skepthical-ai.org, and we release the evaluation set as a benchmark.

</details>

### 283. Recovering Clean Evaluation Metrics from Contaminated Benchmarks

📝 [OpenReview](https://openreview.net/forum?id=NwYunMgkJx) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`evaluation`、`benchmark contamination`、`metric correction`、`mixture model`、`conformal prediction`
- 🎯 **研究动机**：基准样例与训练数据重叠会显著虚高评测指标，而训练来源常不可得，需在监督式表格分类/回归中仅凭预测-标签对事后恢复未污染指标。
- 🔬 **研究方法**：提出元训练框架 MILAN，将被污染基准建模为训练来源与干净评测样本的混合并估计干净成分的软后验权重以修正指标，支持多类加权估计、可融入污染率先验与样本难度，并给出边际覆盖的 split-conformal 预测区间。
- 📌 **结论**：在大量留出数据集与模型族的模拟恢复问题上，MILAN 一致优于阈值、聚类、混合模型、异常检测与成员推断基线，并在 UK Biobank 多基因风险评分案例中提升与 FinnGen 独立参考指标的一致性。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When benchmark examples overlap with a model’s training data, benchmark contamination can substantially inflate reported evaluation metrics, yet training provenance is often unavailable. We study post-hoc recovery of uncontaminated evaluation metrics in supervised tabular classification and regression using only prediction–label pairs from a potentially contaminated benchmark. We introduce MILAN (Metric Integrity via Leakage-Aware Normalization), a meta-trained framework that models a contaminated benchmark as a mixture of training-origin and clean evaluation examples and estimates soft posterior weights for the clean component to correct evaluation metrics. MILAN supports a broad class of metrics through weighted estimators and metric-specific correction procedures, and can optionally incorporate contamination-rate priors and sample-wise difficulty scores. To quantify uncertainty, MILAN additionally provides split-conformal prediction intervals with marginal coverage across exchangeable recovery problems. Across a large suite of simulated recovery problems with held-out datasets and model families, MILAN consistently improves clean-metric recovery over thresholding, clustering, mixture-model, anomaly-detection, and membership-inference baselines. In a polygenic risk score case study using UK Biobank evaluation data, MILAN improves agreement with independent FinnGen reference metrics. We provide a scikit-learn-style implementation at \urlhidden-for-submission.

</details>

### 284. Bypassing PC1 Makes SAEs More Reproducible

📝 [OpenReview](https://openreview.net/forum?id=0YAxdKV85F) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`analysis`、`sparse autoencoder`、`reproducibility`、`anisotropy`、`feature importance`
- 🎯 **研究动机**：SAE 许多特征跨随机种子不可复现，而按零消融重要性排名前 50 的特征竟属于最不可复现之列，与"越重要越可复现"的直觉相反。
- 🔬 **研究方法**：将该反常追溯到残差流各向异性——中层单一主成分 PC1 解释 70-99.9% 激活方差且其稀疏分解不可辨识（不同种子学得铺满同一方向的不同特征），并提出干预：SAE 训练时绕过 PC1、推理时再恢复。
- 📌 **结论**：在 5 个族 9 个模型（124M-70B）上，top-50 特征恢复率升至 74-97%，恢复特征在转向下因果一致性更强（9 个模型中 8 个 p<0.01），共享特征的 logit-lens 预测比孤儿特征准 4 倍。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Sparse autoencoders (SAEs) are widely used to decompose language model activations into interpretable features, but recent work finds that many features are not reproducible across random seeds. Intuitively, the more important a feature is, the more reproducible it should be. We test this hypothesis and find a surprising inversion: the 50 most important features by zero-ablation are among the least reproducible across seeds, far below dictionary-wide baselines. We trace this to residual stream anisotropy, a well-studied phenomenon in NLP embeddings that has been documented in transformer representations but not connected to SAE training. In transformer middle layers, a single principal component (PC1) explains 70--99.9% of activation variance, and its sparse decomposition is non-identifiable: different seeds learn different features that tile the same direction. These features dominate importance rankings, explaining the inversion. We propose an intervention: bypassing PC1 during SAE training, routing it around the SAE and restoring it during inference. Across 9 models from 5 families (124M--70B parameters), this intervention raises top-50 feature recovery to 74--97%. The recovered features show greater causal consistency under steering (p < 0.01 in 8 of 9 models), and shared features produce 4× more accurate logit-lens predictions than orphan features. Our results reconcile recent SAE instability findings with the existence of dense model features: the dominant PC1 direction is real and reproducible, but the individual sparse coordinates used to reconstruct it are not. Once this component is separated, a reproducible core of sparse, semantically coherent SAE features emerges.

</details>

### 285. Market Incentives for AI Safety Investment

📝 [OpenReview](https://openreview.net/forum?id=S4uLBohGBD) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`analysis`、`ai safety investment`、`game theory`、`market incentive`、`regulation`
- 🎯 **研究动机**：AI 系统的社会风险（毒性、恶意使用、错误信息）的缓解不仅取决于技术可行性，还取决于开发与部署企业的安全投资激励。
- 🔬 **研究方法**：构建含上游 LLM 提供方与多个竞争下游企业的 AI 供应链博弈模型，推导市场驱动的安全投资水平，与市场福利及行业利润最优水平比较，并分析不同监管干预对各方激励、利润与模型安全水平的影响。
- 📌 **结论**：下游竞争通常促使下游企业的安全投资超过行业利润最优水平，而上游提供方因未获安全投资剩余的完全补偿可能投资不足。

👤 **作者**：Nikita Tsoy

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite their practical significance, modern AI systems pose significant societal risks, including toxicity, malicious use, and misinformation. Their mitigation depends not only on technical feasibility but also on the incentives of firms that develop and deploy these systems. We show how profit maximization shapes safety investment in an AI supply chain with an upstream LLM provider and several competing downstream firms. In our game-theoretic model, we derive the market-driven level of safety investment and compare it with the levels that maximize market welfare and industry profit. We find that downstream competition generally induces downstream firms to invest more in safety than the industry-profit-optimal level. By contrast, the upstream provider may underinvest relative to these benchmarks because it is not fully compensated for the surplus from safety investments. Finally, we analyze how different regulatory interventions affect the participants' incentives and profits, and the resulting levels of model safety.

</details>

### 286. Speech Tokenizers are Vulnerable:  Transferable Semantic Attack and Robust Tokenizer

📝 [OpenReview](https://openreview.net/forum?id=oVx8Urehhw) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`speech tokenizer`、`transferable semantic attack`、`robust tokenizer`、`audio llm`
- 🎯 **研究动机**：语音 tokenizer 是连续语音到离散表示的关键接口（ASR/大型音频语言模型共用），轻微扰动即可破坏其语义编码并严重降低下游性能，该语义级脆弱性缺乏系统研究。
- 🔬 **研究方法**：提出基于语义编码器集成的可迁移语义攻击 T-SemAttack（联合扰动多个语义编码器表示空间、保持感知质量），并分析 token 脆弱性与层级表示漂移的跨模型可迁移性；防御侧提出噪声训练+鲁棒语义蒸馏的 ROSETok。
- 📌 **结论**：小扰动经 tokenizer 管线逐级放大导致语义崩溃（S3 tokenizer 99.7% token 改变）；多数据集、9 个 ASR 与 4 个 LALM 上验证攻击有效性与 ROSETok 的鲁棒性。

👤 **作者**：Zhisheng Zhang、…、Zhiyong Wu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Speech tokenizers serve as the critical interface between continuous speech signals and discrete representations, and are widely used in speech systems, e.g., Automatic Speech Recognition (ASR) and Large Audio-Language Models (LALMs). In this paper, we find that speech tokenizers are fragile at the semantic level: slight perturbations can disrupt their semantic encoding process and consequently cause severe degradation in downstream ASR and LALM performance. To study this vulnerability, we propose T-SemAttack, a transferable semantic attack based on a semantic encoder ensemble. By jointly perturbing the representation spaces of multiple semantic encoders, T-SemAttack effectively disrupts the semantic content of speech while preserving perceptual quality, thereby inducing error tokens. We further analyze token fragility and layer-wise representation drift in relation to cross-model transferability and disruption of LALM attention. Our analysis reveals a progressive amplification chain in which small waveform perturbations are magnified through the tokenizer pipeline and lead to semantic collapse, e.g., the attack causes a 99.7% token change in the S3 tokenizer. Building on these findings, we introduce ROSETok, a robust speech tokenizer that combines noisy training with robust semantic distillation to improve reconstruction fidelity and downstream-task robustness. Extensive experiments on multiple datasets, 9 open-source and black-box ASR systems, and 4 LALMs demonstrate that T-SemAttack achieves strong transferable attack performance, while the proposed Robust Speech Tokenizer exhibits robustness under high-fidelity reconstruction and downstream tasks. Our code and demo are available at https://t-semattack.github.io.

</details>

### 287. Auditing Instruction Robustness in Vision-Language-Action Models via Diversity-Aware Red Teaming

📝 [OpenReview](https://openreview.net/forum?id=80h2jS8emw) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`red teaming`、`vla`、`instruction robustness`、`embodied agents`
- 🎯 **研究动机**：VLA 模型对指令变体的鲁棒性是真实部署中亟待审计的安全盲区，而标准 RL 红队因奖励最大化产生严重 mode collapse，只能收敛到少量重复的平凡失败模式。
- 🔬 **研究方法**：提出多样性感知具身红队框架 DAERT，用 breadth-seeking value estimator 阻止攻击者坍缩到单一高奖励措辞，生成多样且有效的对抗指令，以物理仿真中的执行失败衡量攻击效果。
- 📌 **结论**：在多个机器人基准上针对 π₀ 与 OpenVLA 两个 SOTA VLA，任务平均成功率从 93.33% 降至 5.85%，揭示出部署前未被覆盖的关键安全盲点。

👤 **作者**：Baoshun Tong、Haoran He、Yang Liu、Ling Pan、Liang Lin

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models have achieved remarkable success in robotic manipulation. However, their robustness to instruction variations remains a critical, under-explored safety concern, posing a significant safety risk to real-world deployment. Red teaming, or identifying environmental scenarios that elicit catastrophic behaviors, is an important step in ensuring the safe deployment of embodied AI agents. Reinforcement learning (RL) has emerged as a promising approach in automated red teaming that aims to uncover these vulnerabilities. However, standard RL-based adversaries often suffer from severe mode collapse due to their reward-maximizing nature, which tends to converge to a narrow set of trivial or repetitive failure patterns, failing to reveal the comprehensive landscape of meaningful risks. To bridge this gap, we propose a novel Diversity-Aware Embodied Red Teaming (DAERT) framework, to audit VLA robustness under semantically aligned instruction. Our design uses a breadth-seeking value estimator that prevents the attacker from collapsing onto a single high-reward phrasing, generating a diverse set of challenging instructions while preserving attack effectiveness, measured by execution failures in a physical simulator. We conduct extensive experiments across different robotic benchmarks against two state-of-the-art VLAs, including \pi_0 and OpenVLA. Our method consistently discovers a wider range of more effective adversarial instructions that reduce the average task success rate from 93.33% to 5.85%, demonstrating a scalable approach to stress-testing VLA agents and exposing critical safety blind spots before real-world deployment.

</details>

### 288. Controllable Multi-label Video Safety Detection via Adaptive Tversky Policy Optimization

📝 [OpenReview](https://openreview.net/forum?id=66AVx7heNO) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`detection`、`video safety`、`multi-label classification`、`reinforcement learning`、`precision-recall tradeoff`
- 🎯 **研究动机**：现有有害视频检测把安全判断简化为二分类、忽视不安全内容的多标签本质，且静态训练目标无法支持不同审核管线所需的可控 precision-recall 权衡。
- 🔬 **研究方法**：提出强化学习框架 ATPO（Adaptive Tversky Policy Optimization），其 Adaptive Tversky Reward 在训练中动态调整假阳与假阴惩罚，实现多标签视频安全检测中可操控的 precision-recall 工作点。
- 📌 **结论**：在 SafeWatch-Bench 与 XD-Violence 上显著提升多标签性能，SafeWatch-Bench-Real 的 Jaccard Index 从 40.66 升至 75.44，并可靠支持异质政策要求的部署场景。

👤 **作者**：Guangyu Yang、…、Bill Byrne

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid growth of video-based social media has increased users’ exposure to harmful content, creating a need for reliable automated video safety detection. Although recent Vision-Language Models (VLMs) show strong video understanding capabilities, existing harmful video detection systems face two key limitations: they typically reduce safety detection to binary classification, overlooking the inherently multi-label nature of unsafe videos, and they rely on static training objectives that do not support controllable precision-recall trade-offs, though the desired operating point may vary across moderation pipelines and unsafe categories. To address these gaps, we propose Adaptive Tversky Policy Optimization (ATPO), a reinforcement learning framework for Multi-label Video Safety Detection (Multi-VSD). ATPO introduces the Adaptive Tversky Reward (ATR), which dynamically adjusts false-positive and false-negative penalties during training to enable controllable precision–recall trade-offs. Experiments on SafeWatch-Bench and XD-Violence show that ATPO substantially improves multi-label performance, increasing the Jaccard Index from 40.66 to 75.44 on SafeWatch-Bench-Real. Moreover, ATR enables reliable steering of the precision–recall operating point, supporting deployment scenarios with heterogeneous policy requirements.

</details>

### 289. Decomposing One Professional-Framing Pipeline: Which Components Shift LLM Safety Boundaries?

📝 [OpenReview](https://openreview.net/forum?id=1UvkQdlJOO) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`analysis`、`jailbreak`、`professional framing`、`factorial decomposition`、`llm safety`
- 🎯 **研究动机**：把有害查询包装成专业请求的越狱攻击能绕过 LLM 安全训练，但专业框架 pipeline 中究竟哪些成分真正起作用尚不清楚。
- 🔬 **研究方法**：提出分解方法区分"获取访问"与"加深输出"两类组件，并对具体 pipeline（S3，即用框架术语替换口语）做因子实验（N=5,000，跨三个闭源前沿模型、九个 LLM 共约 31,900 次试验）。
- 📌 **结论**：组件效应排序为 Persona > Linguistic Substitution > Moral Justification，该排序经三次全因子重复（每次 N≈5,000）与九项稳健性检验均成立，并给出两个防御靶点：检测 persona 声明阻断访问、对使用框架术语的回复限制输出深度。

👤 **作者**：Gianluigi Vitale

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Jailbreak attacks that frame harmful queries as professional requests can bypass LLM safety training, but we do not know which ingredients in a professional-framing pipeline actually matter. We introduce a , separating access-driving from depth-driving components, and apply it to one concrete pipeline family, (S3) of framework terminology for colloquial language. Tested on N = 5,000 trials across three closed frontier models (~31,900 total trials across nine LLMs), the decomposition isolates (Persona > Linguistic Substitution > Moral Justification). This ordering holds across three full-rank factorial replications (defensive system prompt, cybersecurity, social engineering; N ≈ 5,000 each) and nine additional robustness checks. Two defensive targets follow: detect persona claims to block access; restrict output depth when responses use framework terminology. The method is portable beyond STF; the empirical result is specific to one pipeline tested primarily through provider APIs, with open-weight corroborations on local inference (§3).

</details>

### 290. There are Levels to It: Red Teaming LLMs with Hierarchical Reinforcement Learning

📝 [OpenReview](https://openreview.net/forum?id=MgRh8Pu9er) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026　🏷 NeurIPS 2026

**关键词**：`attack`、`red teaming`、`hierarchical reinforcement learning`、`multi-turn attack`、`markov decision process`
- 🎯 **研究动机**：红队是保障 LLM 安全的关键手段，但现有自动化方法受限于模板与单轮攻击，难以模拟真实对抗的复杂交互。
- 🔬 **研究方法**：把红队形式化为马尔可夫决策过程并纳入分层强化学习框架以应对稀疏奖励与长程规划，生成式 agent 用 token 级 harm reward 学习多样的多轮攻击。
- 📌 **结论**：持续发现基线方法无法揭示的漏洞，取得新 SOTA，并将 LLM 红队重塑为有原则的基于轨迹的过程。

👤 **作者**：Roman Belaire、Arunesh Sinha、Pradeep Varakantham

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Red teaming is essential for securing Large Language Models, yet current automated methods remain limited by templates and single-turn attacks. To simulate the complex, interactive nature of real-world adversarial attacks, we introduce a novel red teaming paradigm designed to maximize expected cumulative harm through strategic interaction. By formalizing red teaming as a Markov Decision Process in a hierarchical reinforcement learning framework, we navigate the challenges of sparse rewards and long-horizon planning. Our generative agent learns diverse, multi-turn attacks using a token-level harm reward, consistently uncovering vulnerabilities that bypass baselines. This approach achieves a new state of the art and reframes LLM red teaming as a principled, trajectory-based process.

</details>

### 291. Hearsay: Can an Auditor Trust the Record a Deployed Agent Harness Writes?（已库内，0929）

📄 [arXiv](https://arxiv.org/abs/2609.32495) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`evaluation`、`agent harness`、`audit record`、`evidentiary log`、`tampering`
- 🎯 **研究动机**：agent harness（把模型变成 agent 的代码）自写的运行记录是事后争议、调查与审计的全部依据，而 16 个已部署框架无一完整写出读者无需信任写者即可核验的证据性记录。
- 🔬 **研究方法**：Hearsay 只查记录不查任务——5 个 harness 跑 14 个任务，3 个盲测 LLM 考官与人类小组读记录且每处引用被机器核验写者；并提出"第二作者"方案：在 harness 之外保存双方传递内容的 append-only log 并与记录双向比对。
- 📌 **结论**：考官在 140 次运行中 74–91% 能说对故障但证据仅能来自基准新增的两个文件、少于十分之一的引用落在 harness 未写内容上；外部 append-only log 报出全部 28 处注入的省略/伪造，而对 harness 自身记录的 hash chain 让 28 处全部漏过。

👤 **作者**：Jiahong Dai、…、Bo Hu

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

An agent harness, the code that turns a model into an agent, writes its own record of each run, and that record is all a later reader gets when a run is disputed, investigated or audited. We call a record evidentiary when a reader who was not there can check it without trusting the writer. Across sixteen deployed frameworks, none writes one in full. Hearsay examines the record, not the task: five harnesses run fourteen tasks, three blinded LLM examiners and a human panel read the records, and every excerpt an examiner quotes is checked mechanically for who wrote it. First, the record lets a reader name the fault but not prove how the run went. Examiners name the right fault in 74 to 91% of 140 runs, but the fault can be proved only from two files the benchmark adds; for what happened in between, fewer than one citation in ten lands on anything the harness did not write, and the examiner with the fewest false alarms catches half of the entries we delete, rewrite or fabricate. Second, the remedy is a second author, not a stronger seal on the first. An append-only log of what passes between harness and model, kept outside the harness and read against the record in both directions, reports all 28 omissions and fabrications we made a harness commit as it ran, where a hash chain over the harness's own record passes all 28. Handed the log, examiners keep their fault verdicts but rest more of their citations on what the harness did not write. What makes a record evidence is who writes it, not what is captured.

</details>

### 292. Silent Failures in Agentic Security Evaluation（已库内，0929）

📄 [arXiv](https://arxiv.org/abs/2609.32691) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-09　🏷 NeurIPS 2026

**关键词**：`evaluation`、`indirect prompt injection`、`agent security`、`harness validity`、`rescoring`
- 🎯 **研究动机**：调用特权工具的 LLM agent 面临间接提示注入威胁，但针对 IPI 防御的评测有效性鲜被审视，有缺陷的 harness 会产出貌似可发表的错误数字。
- 🔬 **研究方法**：审计一个 IPI 基准及其 harness，识别静默 payload 未送达、按工具身份而非参数判攻击成功、误拒率与模型无能力混淆、缺审计痕迹四类缺陷，并发布使各类缺陷无法出现的修正 harness（机器可查 payload 放置、参数级攻击谓词、每场景环境、强制 trace 持久化）。
- 📌 **结论**：对同一执行轨迹重打分，工具身份评分器报 21.7% 攻击成功率而真实参数级仅 1.2%，某开源模型 62.8% 在修正后归零，且推翻了一例"工具使用能力障碍"的既有结论。

👤 **作者**：Animesh Shaw

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents that invoke privileged tools are vulnerable to indirect prompt injection (IPI), in which adversarial instructions embedded in retrieved data hijack the agent's actions. A growing body of work evaluates defenses against IPI, but the validity of that evaluation is rarely examined. We audit an IPI benchmark and its harness and identify four defect classes -- silent payload non-delivery, attack success scored by tool identity rather than arguments, false-rejection rate conflated with model incapacity, and the absence of an audit trail -- each of which yields a plausible, publishable, and incorrect number. We quantify the distortion by re-scoring identical execution traces under the defective and corrected definitions: on real agent behaviour, the tool-identity scorer reports a 21.7% attack-success rate where the true argument-level rate is 1.2%. In the sharpest case, an open model previously reported at 62.8% registers 0% under the corrected harness -- the prior figure largely an artifact of undelivered payloads and identity-level scoring. We release a harness whose construction makes each defect unrepresentable -- machine-checkable payload placement, argument-level attacker predicates, per-scenario environments, and mandatory trace persistence -- and use it to report three quantities the field does not: whether a compromised agent discloses the attack, the full security/utility operating curve of an LLM-judge defense, and tool-calling capability disentangled from defensive over-blocking. A corrected harness further overturns a reported "capability barrier": a model deemed incapable of tool use is in fact fully capable, its earlier result an artifact of environment mismatch. We argue that evaluation validity is a prerequisite for, not a footnote to, defense claims in agentic security, and provide an instrument that enforces it.

</details>

### 293. Evaluation Awareness in Language Models Has Limited Effect on Behaviour

📄 [arXiv](https://arxiv.org/abs/2605.05835) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`evaluation awareness`、`chain-of-thought`、`verbalised awareness`、`safety evaluation`
- 🎯 **研究动机**：研究者担心大推理模型在 CoT 中口头表达"可能正被评估"（VEA）会导致策略性适配输出、使模型显得比实际更安全，但该效应是否真实存在基本未知。
- 🔬 **研究方法**：跨开源 LRM 与覆盖安全、对齐、道德推理与政治观点的基准，on-policy 比较自发含 VEA 与不含 VEA 的 CoT，off-policy 用 prefilling 注入或移除评估感知语句后重采样。
- 📌 **结论**：VEA 对行为影响有限——注入产生近零效应（ω≤0.06）、移除仅引起小偏移（ω≤0.12）、自发 VEA 至多改变答案分布 3.7 个百分点（ω≤0.31），提示不应将高 VEA 率直接解读为策略行为或对齐篡改证据。

👤 **作者**：Amelie Knecht、Lucas Florin、Thilo Hagendorff

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large reasoning models (LRMs) sometimes note in their chain of thought (CoT) that they may be under evaluation. Researchers worry that this verbalised evaluation awareness (VEA) causes models to adapt their outputs strategically, optimising for perceived evaluation criteria, which, for instance, can make models appear safer than they actually are. However, whether VEA actually has this effect is largely unknown. We tested this across open-weight LRMs and benchmarks covering safety, alignment, moral reasoning, and political opinion. We tested this both on-policy, sampling multiple CoTs per item and comparing those that spontaneously contained VEA against those that did not, and off-policy, using model prefilling to inject evaluation-aware sentences where missing and remove them where present, with subsequent resampling. VEA has limited effect on model behaviour: injecting VEA into CoTs produces near-zero effects ($ω\leq 0.06$), removing it causes small shifts ($ω\leq 0.12$) and spontaneously occurring VEA shifts answer distributions by at most 3.7 percentage points ($ω\leq 0.31$). Our findings call for caution when interpreting high VEA rates as evidence of strategic behaviour or alignment tampering. Evaluation awareness may pose a smaller safety risk than the current literature assumes.

</details>

### 294. How Hard is it to Rig a Benchmark? A Social Choice Analysis of Leaderboard Robustness

📄 [arXiv](https://arxiv.org/abs/2605.23628) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`analysis`、`benchmark gaming`、`social choice`、`leaderboard robustness`、`shift bribery`
- 🎯 **研究动机**：多任务基准的影响力催生了 benchmark gaming——通过基准专属训练（把基准数据纳入训练）战略性提升特定模型排名，其可操纵性需要理论刻画。
- 🔬 **研究方法**：把数据集视为选民、模型视为候选人，证明基准专属训练对应计算社会选择中的 shift bribery 操纵问题（在 Borda count 与 mean win rate 下 NP-hard），并定义实例级鲁棒性（登顶排行榜所需纳入训练的最少数据集数）且导出四种聚合规则下的表达式。
- 📌 **结论**：在 HELM/MMLU 与 Open LLM Leaderboard/BBH 上评测，mean win rate 最难操纵——BBH（24 任务、4507 模型）上中位鲁棒性为 22 个任务（92%），高于算术平均的 13（54%）及中位数与成对多数各 12（50%）。

👤 **作者**：Polina Gordienko、Georg Schollmeyer、Frauke Kreuter、Christoph Jansen

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-task benchmarks have become a central pillar of machine learning research, yet their growing influence has incentivised benchmark gaming -- strategic actions taken to improve the leaderboard rank of a specific model. Treating datasets as voters and models as candidates, we consider benchmark-specific training -- the inclusion of benchmark data in training -- as a form of election manipulation. For any ordinal benchmark, the problem of choosing datasets to train on so that a target model becomes top-ranked corresponds to shift bribery, a class of manipulation problems from computational social choice. Leveraging this identification, we show that the benchmark-specific training problem is NP-hard under Borda count and mean win rate. Complementing this worst-case perspective, we introduce the instance-level robustness, the minimum number of datasets a model developer must include in training to top a given leaderboard, and derive expressions for it under arithmetic mean, median, mean win rate and pairwise majority. We evaluate these expressions on MMLU under HELM and on BIG-Bench Hard (BBH) under the Open LLM Leaderboard. Across both suites, mean win rate is hardest to manipulate: this gap is clear on BBH (24 tasks, 4507 models), where its median robustness is 22 tasks (92%), compared with 13 (54%) under arithmetic mean and 12 (50%) under median and pairwise majority.

</details>

### 295. Models That Know How Evaluations Are Designed Score Safer

📄 [arXiv](https://arxiv.org/abs/2605.28591) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`evaluation`、`meta-knowledge`、`safety benchmark`、`confounder`
- 🎯 **研究动机**：安全评估的有效性依赖模型在受控与部署设置下行为一致，而已知的测试时上下文线索之外，关于评估结构特征的参数化"评估元知识"可能是行为偏移的另一来源
- 🔬 **研究方法**：假设接触描述评估实践的文本会让模型隐式识别并响应评估式上下文，用描述可验证结构、有害请求等评估特质的合成文档微调模型，并在 5 个安全基准上与基线及控制模型对比
- 📌 **结论**：微调模型显著变得更安全，且该偏移在剔除显式言语化评估意识的回答后依然存在——评估元知识可虚增安全基准得分，构成独立于记忆与言语化意识、难以检测的新型混杂因子

👤 **作者**：Katharina Deckenbach、Haritz Puerto、Jonas Geiping、Sahar Abdelnabi

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The validity of AI safety evaluations depends on models behaving consistently across controlled and deployment settings. Prior work has identified test-time contextual cues, such as hypothetical scenarios, as a source of verbalized evaluation awareness and subsequent behavioral shift. In this paper, we investigate a potential explanation of this phenomenon: evaluation meta-knowledge, defined as parametric knowledge about the structural traits that characterize evaluations. Similar to dataset contamination, where benchmark exposure leads to higher performance through memorization, we hypothesize that models trained on texts describing evaluation practices may implicitly learn to recognize and respond to evaluation-like contexts, for instance, through exposure to scientific articles or social media posts about AI benchmarking. To test this, we fine-tune models on synthetic documents describing evaluation traits such as verifiable structures or harmful requests. Evaluating this fine-tuned model on five safety benchmarks, we find that it is significantly safer than the base model and control model. This behavioral shift persists even when restricting the analysis to responses lacking explicit verbalization of evaluation awareness. Our results demonstrate that evaluation meta-knowledge may inflate safety benchmark performance, introducing a novel confounder that is independent of explicit memorization or verbalized evaluation awareness, thus, challenging to detect. These findings have important implications for the design and interpretation of AI safety evaluations. Our code and models are available at https://github.com/compass-group-tue/arxiv2026_evaluation_meta_knowledge.

</details>

### 296. LiSA: Lifelong Safety Adaptation via Conservative Policy Induction

📄 [arXiv](https://arxiv.org/abs/2605.14454) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-05　🏷 NeurIPS 2026

**关键词**：`defense`、`agent guardrail`、`lifelong adaptation`、`policy induction`、`sparse feedback`
- 🎯 **研究动机**：AI 智能体护栏失败会泄露秘密、放行危险操作或阻断合法工作，其可接受性高度依赖本地隐私规范等上下文，而部署反馈稀疏嘈杂、反复微调又不现实。
- 🔬 **研究方法**：提出保守策略归纳框架 LiSA（Lifelong Safety Adaptation），通过结构化记忆把偶发失败转化为可复用的策略抽象，辅以冲突感知局部规则防止混合标签下过度泛化，并用基于后验下界的证据感知置信门控让记忆复用随证据积累扩展。
- 📌 **结论**：在 PrivacyLens+、ConFaide+、AgentHarm 上持续超越强记忆基线，20% 标签翻转的噪声反馈下仍鲁棒，并将延迟-性能前沿推至超越骨干模型扩展。

👤 **作者**：Minbeom Kim、…、Long T. Le

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As AI agents move from chat interfaces to systems that read private data, call tools, and execute multi-step workflows, guardrails become a last line of defense against concrete deployment harms. In these settings, guardrail failures are no longer merely answer-quality errors: they can leak secrets, authorize unsafe actions, or block legitimate work. The hardest failures are often contextual: whether an action is acceptable depends on local privacy norms, organizational policies, and user expectations that resist pre-deployment specification. This creates a practical gap: guardrails must adapt to their own operating environments, yet deployment feedback is typically limited to sparse, noisy user-reported failures, and repeated fine-tuning is often impractical. To address this gap, we propose LiSA (Lifelong Safety Adaptation), a conservative policy induction framework that improves a fixed base guardrail through structured memory. LiSA converts occasional failures into reusable policy abstractions so that sparse reports can generalize beyond individual cases, adds conflict-aware local rules to prevent overgeneralization in mixed-label contexts, and applies evidence-aware confidence gating via a posterior lower bound, so that memory reuse scales with accumulated evidence rather than empirical accuracy alone. Across PrivacyLens+, ConFaide+, and AgentHarm, LiSA consistently outperforms strong memory-based baselines under sparse feedback, remains robust under noisy user feedback even at 20% label-flip rates, and pushes the latency--performance frontier beyond backbone model scaling. Ultimately, LiSA offers a practical path to secure AI agents against the unpredictable long tail of real-world edge risks.

</details>

### 297. Soft Contamination Means Benchmarks Test Shallow Generalization

📄 [arXiv](https://arxiv.org/abs/2602.12413) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`analysis`、`benchmark contamination`、`semantic duplicates`、`decontamination`、`ood generalization`
- 🎯 **研究动机**：LLM 训练数据被基准测试数据污染会使基准成绩给出有偏的 OOD 泛化估计，而常用的 n-gram 去污染过滤无法检测字符串空间不相近但内容等价的语义重复（soft contamination）。
- 🔬 **研究方法**：对训练语料做嵌入以检索基准数据的语义重复，在 Olmo3 训练语料等实验中系统考察语义重复污染的普遍性及其对基准成绩的影响。
- 📌 **结论**：污染仍然普遍——78% 的 CodeForces 题目存在语义重复、ZebraLogic 50% 存在精确重复；把基准数据的语义重复纳入训练能提升基准成绩乃至同基准真留出点的成绩，说明近期基准增益混杂了真实能力提升与测试数据积累。

👤 **作者**：Ari Spiesberger、…、Nandi Schoots

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

If LLM training data is polluted with benchmark test data, then benchmark performance gives biased estimates of out-of-distribution (OOD) generalization. Typical decontamination filters use n-gram matching which fail to detect semantic duplicates: sentences with equivalent (or near-equivalent) content that are not close in string space. We study this soft contamination of training data by semantic duplicates. Among other experiments, we embed the Olmo3 training corpus and find that: 1) contamination remains widespread, e.g. we find semantic duplicates for 78% of CodeForces and exact duplicates for 50% of ZebraLogic problems; 2) including semantic duplicates of benchmark data in training does improve benchmark performance; and 3) when finetuning on duplicates of benchmark datapoints, performance also improves on truly-held-out datapoints from the same benchmark. We argue that recent benchmark gains are thus confounded: the prevalence of soft contamination means gains reflect both genuine capability improvements and the accumulation of test data and effective test data in growing training corpora.

</details>

### 298. Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines?

📄 [arXiv](https://arxiv.org/abs/2602.14111) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`evaluation`、`sparse autoencoder`、`random baseline`、`interpretability`
- 🎯 **研究动机**：SAE 被视为解释神经网络的核心工具，但下游任务中不断出现的负面结果使人怀疑其是否真正恢复了有意义的特征
- 🔬 **研究方法**：在已知真值特征的合成设置中直接检验 SAE，并构造三个把 SAE 特征方向或激活模式约束为随机值的基线，在多个 SAE 架构上比较可解释性、稀疏探测与因果编辑
- 📌 **结论**：合成设置中 SAE 仅恢复 9% 的真实特征（解释方差高达 71%），随机基线在可解释性（0.87 vs 0.90）、稀疏探测（0.69 vs 0.72）与因果编辑（0.73 vs 0.72）上追平全训练 SAE，表明当前 SAE 不能可靠分解模型内部机制

👤 **作者**：Anton Korznikov、Andrey Galichin、Alexey Dontsov、Oleg Rogov、Ivan Oseledets、Elena Tutubalina

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Sparse Autoencoders (SAEs) have emerged as a promising tool for interpreting neural networks by decomposing their activations into sparse sets of human-interpretable features. Recent work has introduced multiple SAE variants and successfully scaled them to frontier models. Despite much excitement, a growing number of negative results in downstream tasks casts doubt on whether SAEs recover meaningful features. To directly investigate this, we perform two complementary evaluations. On a synthetic setup with known ground-truth features, we demonstrate that SAEs recover only $9\%$ of true features despite achieving $71\%$ explained variance, showing that they fail at their core task even when reconstruction is strong. To evaluate SAEs on real activations, we introduce three baselines that constrain SAE feature directions or their activation patterns to random values. Through extensive experiments across multiple SAE architectures, we show that our baselines match fully-trained SAEs in interpretability (0.87 vs 0.90), sparse probing (0.69 vs 0.72), and causal editing (0.73 vs 0.72). Together, these results suggest that SAEs in their current state do not reliably decompose models' internal mechanisms.

</details>

### 299. GT-HarmBench: Benchmarking AI Safety Risks Through the Lens of Game Theory

📄 [arXiv](https://arxiv.org/abs/2602.12316) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2026-02　🏷 NeurIPS 2026

**关键词**：`benchmark`、`game theory`、`multi-agent safety`、`high-stakes scenario`
- 🎯 **研究动机**：现有 AI 安全基准大多只评测单智能体，协调失败与冲突等多智能体风险理解不足。
- 🔬 **研究方法**：构建含 1,535 个高风险场景的 GT-HarmBench，覆盖囚徒困境、猎鹿与胆怯等博弈结构，场景取自 MIT AI Risk Repository 的现实 AI 风险语境，评测 15 个前沿模型并测量其对博弈论提示框架与顺序的敏感性及失败推理模式。
- 📌 **结论**：智能体在 38% 的高风险案例（如军事升级、选举操纵、医疗事故）中未能选择社会有益行动，而博弈论干预可将社会有益结果提升至多 18%。

👤 **作者**：Pepijn Cobben、Xuanqiang Angelo Huang、Thao Amelia Pham、Isabel Dahlgren、Terry Jingchen Zhang、Zhijing Jin

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Frontier AI systems are increasingly capable and deployed in high-stakes multi-agent environments. However, existing AI safety benchmarks largely evaluate single agents, leaving multi-agent risks such as coordination failure and conflict poorly understood. We introduce GT-HarmBench, a benchmark of 1,535 high-stakes scenarios spanning game-theoretic structures such as the Prisoner's Dilemma, Stag Hunt and Chicken. Scenarios are drawn from realistic AI risk contexts in the MIT AI Risk Repository. Across 15 frontier models, agents fail to choose socially beneficial actions in 38% of high-stakes cases, such as military escalation, election manipulation, and medical malpractice. We measure sensitivity to game-theoretic prompt framing and ordering, and analyze reasoning patterns driving failures. We further show that game-theoretic interventions improve socially beneficial outcomes by up to 18%. Our results highlight substantial reliability gaps and provide a broad standardized testbed for studying alignment in multi-agent environments. The benchmark and code are available at https://github.com/causalNLP/gt-harmbench.

</details>

### 300. Test-Time Defense Against Adversarial Attacks via Stochastic Resonance of Latent Ensembles

📄 [arXiv](https://arxiv.org/abs/2510.03224) · 🎓 [Official](https://neurips.cc/Downloads/2026)　📅 2025-10　🏷 NeurIPS 2026

**关键词**：`defense`、`adversarial examples`、`stochastic resonance`、`test-time defense`、`latent ensemble`
- 🎯 **研究动机**：现有对抗防御依赖特征过滤或平滑会造成信息损失，需要既能增强鲁棒性又尽量不丢信息的新思路。
- 🔬 **研究方法**：提出"以噪抗噪"的测试时防御：对输入图像施加小的平移扰动、对齐变换后的特征嵌入并聚合后映射回原始参考图像，整个过程有闭式公式，免训练、架构无关、攻击无关。
- 📌 **结论**：在图像分类上达到 SOTA 鲁棒性，并首次为立体匹配、光流等密集预测任务建立通用测试时防御；相对干净性能分别恢复最高 68.1%（分类）、71.9%（立体匹配）、29.2%（光流）的精度损失。

👤 **作者**：Dong Lao、Yuxiang Zhang、Haniyeh Ehsani Oskouie、Yangchao Wu、Alex Wong、Stefano Soatto

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We propose a test-time defense mechanism against adversarial attacks: imperceptible image perturbations that significantly alter the predictions of a model. Unlike existing methods that rely on feature filtering or smoothing, which can lead to information loss, we propose to "combat noise with noise" by leveraging stochastic resonance to enhance robustness while minimizing information loss. Our approach introduces small translational perturbations to the input image, aligns the transformed feature embeddings, and aggregates them before mapping back to the original reference image. This can be expressed in a closed-form formula, which can be deployed on diverse existing network architectures without introducing additional network modules or fine-tuning for specific attack types. The resulting method is entirely training-free, architecture-agnostic, and attack-agnostic. Empirical results show state-of-the-art robustness on image classification and, for the first time, establish a generic test-time defense for dense prediction tasks, including stereo matching and optical flow, highlighting the method's versatility and practicality. Specifically, relative to clean (unperturbed) performance, our method recovers up to 68.1% of the accuracy loss on image classification, 71.9% on stereo matching, and 29.2% on optical flow under various types of adversarial attacks.

</details>

**尚未挂出 arXiv（待核验）**
- Auditing is not Evaluating: LLM Audit Requires Dynamic, Contextual, Budget-aware and Reliable Evidence
- Auditing the Judge: Human-Grounded Bias Discovery in LLM Judges
- Are LLM Safety Judges Policy-Invariant?（重复，见对齐节）
- EvalAwareBench: Measuring Evaluation Awareness in Frontier LMs
- Too Early for AI-Assisted Peer Review
- Large language models can not and should not be banned from peer review
- Leaderboard Hacking（重复，见 agent 节）
- Forced Orders: What LLM Leaderboards Hide About Model Comparisons

## 核验记录

- 2026-09-30：首版建立（官方 9,127 条标题宽筛，八分类清单）→ 二次 36 卡 → 三轮补查 105 卡（累计 141）。
- 2026-09-30（四轮·辅助源交叉）：引入 [hongsong-wang/NeurIPS2026 收集页](https://hongsong-wang.github.io/NeurIPS2026/)（7,900 篇、OpenReview forum 链接+摘要、3,495 篇 arXiv 链接）交叉定位——待核清单捞回 93 篇、反向查漏补收 66 篇，合计新增 159 卡（其中 arXiv 卡 36、OpenReview-only 卡 123，后者摘要取自该收集页）。累计卡片 300 篇。
- arXiv ID 配对均经 id_list 标题核验；收集页原始 arXiv 字段存在跨条目错配（50/78），已按精确分段重配并剔除 2 条真错配，6 条为同文标题变体（arXiv v1 更名）。
- 反向查漏口径：对 7,900 标题跑安全词表 + 人工分诊 108 条强信号，剔除 bandit/RL 安全约束、控制论、非 AI 安全视觉对抗与误匹配后补收 66 篇。
- Pre-Decoding States（dllm-security #8）为 OpenReview-only，无 arXiv 版。
- 标题变体（同文核验）：卡片保留 NeurIPS 官方列表标题；Token Inflation 的 arXiv 版名为 "The More It Says, the More You Pay…" 等，均经摘要核验同文。个别 📅 月份与 ID 段不一致为月末跨月提交。
- 注意：OpenReview-only 卡的录用证据链为官方 Downloads 标题 + 第三方收集页 forum 链接，⚠ 待 OpenReview 页面正式标注 venue 后复核。
