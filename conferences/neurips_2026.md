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
| 整理模式 | 官方列表已放出但无逐篇摘要/链接，采用**分类标题清单**（同 CCS Second Cycle 待核验模式）；arXiv 版陆续挂出后经日报管线收录建卡，venue 回填 `🏷 NeurIPS 2026` |

## 关键节点

| 节点 | 日期 | 官方来源 |
| --- | --- | --- |
| Notification | 2026-09-24 | 官方 Downloads 列表放出 |
| Conference | 2026-12（官方页面未给出精确日期，待核） | [NeurIPS 2026](https://neurips.cc/Conferences/2026) |

## 筛选说明

- 官方 event 总数：9,127（含 posters/tutorials/workshops/demos；含少量 workshop 条目混入主列表）
- 标题宽筛 AI 安全相关：约 300+
- 本文件收录：精选约 200 条，按六大分类组织
- 收录口径：与 `RESEARCH_INTERESTS.md` P1 口径一致——模型层安全机制攻防、投毒与后门、guard/monitor/judge 有效性、LLM/Agent 栈规模化攻防实证、绑定安全 threat model 的内部表示干预、DLM 安全线；纯理论（DP/密码学/博弈论无 AI 安全对象）不收
- 同名提示：`MemPoison`（NeurIPS）与库内 MemPoison（2607.14651）、`RouteGuard`（GuardZoo）与库内 skill 检测 RouteGuard 需注意区分

## 论文分类

### 越狱、安全对齐与有害微调

- Enhancing Jailbreak Attacks on LLMs via Persona Prompts
- Systematic Scaling Analysis of Jailbreak Attacks in Large Language Models
- MJ: Multi-Turn LLM Jailbreaking via Decomposed Credit Assignment
- MT-JailBench: A Modular Benchmark for Multi-Turn Jailbreak Attacks
- Conceal, Reconstruct, Jailbreak: Exploiting the Reconstruction–Concealment Tradeoff in MLLMs
- CodeMimicry: Exploiting Safety Generalization Lag via Structured Code Completion
- Few-Shot Truly Benign DPO Attack for Jailbreaking LLMs
- Latent-space Attacks for Refusal Evasion in Language Models
- A Single Neuron Is Sufficient to Bypass Safety Alignment in LLMs
- Guaranteed Jailbreaking Defense via Disrupt-and-Rectify Smoothing
- Internal Safety Collapse in Frontier Large Language Models
- Fail-Closed Alignment for Large Language Models
- BSO: Safety Alignment Is Density Ratio Matching
- DACE: Diversity-Driven Adversarial Co-Evolution for Robust LLM Safety Alignment
- Bridging the Gap Between Harmfulness Belief and Refusal Behavior for Safety Alignment
- Inference-Time Vulnerability Beyond Shallow Safety: Alignment Along Generation Trajectories
- Fine-tuning Does Not Reach All: Uneven Safety and Knowledge Dynamics in LLMs
- The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety
- When Safety Becomes An Outlier: Understanding the Retention of LLM Safety Behaviors
- Rethinking LLM Fine-Tuning via Weight Space Reparameterization: Preserving Safety during Downstream Adaptation
- GradShield: Alignment Preserving Finetuning
- SLDR: Defending Against Malicious Fine-tuning via Selective Layers Recovery and Dynamic Routing
- Tcell: Mitigating Harmful Fine-tuning via Gradient Alignment
- Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples
- Safety Reconstructed: Generative Modeling via Masked Diffusion Builds Strong Safety Guardrails
- Curriculum Learning for Safety Alignment
- Cat-DPO: Category-Adaptive Safety Alignment
- Dialectics of Alignment: Harnessing Unsafe Knowledge for Dynamic Safety Routing
- Explaining and Breaking the Safety-Helpfulness Ceiling via Preference Dimensional Expansion
- Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation
- Behaving Better, Thinking Worse: Sycophancy Across Post-Training Stages
- SuperSycophantic: Stress-Testing Frontier LLMs from Single- to Multi-Turn Sycophancy
- Expected Harm: Rethinking Safety Evaluation of (Mis)Aligned LLMs
- Are LLM Safety Judges Policy-Invariant? A Three-Principle Stress-Test
- Answering At Any Cost: Frontier LLMs Are Consequence-Insensitive
- Do Thinking Tokens Help with Safety?
- Beyond Truthfulness: Evaluating Honesty in LLMs
- Emergent Misalignment as Data-Mediated Transfer
- The Piggyback Hypothesis of Generalization: Explaining and Mitigating Emergent Misalignment
- Persona-Model Collapse in Emergent Misalignment
- Self-Recognition Finetuning can Reverse and Prevent Emergent Misalignment
- Innocuous-Seeming Data, Latent Ideology: Ideological Generalisation in Finetuned LLMs
- (Mis)generalization of Helpful-Only Fine-Tuning

### CoT 监控、scheming 与 AI control

- Chain-of-Thought Oversight Should Not Treat Faithfulness as Monitorability
- Corrupted Plans, Clean Traces: What Planning-Execution Decoupling Reveals About CoT Monitoring
- Stress Testing Chain-of-Thought Monitoring Against Covert Misalignment
- Training on Documents About Monitoring Leads to CoT Obfuscation
- Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics
- Training Deliberative Monitors for Black-Box Scheming Detection
- AI Control for Sandbagging on Fuzzy Tasks
- AI Models Can Provably Hide Arbitrary Capabilities
- AIs with Secret Loyalties are a Serious but Addressable Threat
- AutoHoney: Automating, Deploying, and Evaluating Scheming Honeypots Across Production Codebases
- Evaluating and Understanding Scheming Propensity in LLM Agents
- SchemeArena: Factorized Stress Testing of Scheming in LLM Agents
- Scheming Is a Symptom: Alignment Research Should Probe Reflexive Fragility
- Breadcrumbing Search Agents: Per-Turn Scheming Over Long-Horizon Trajectories
- Neural Chameleons: Language Models Can Learn to Hide Their Thoughts from Unseen Activation Monitors
- Attack Selection In Agentic AI Control Evaluations Meaningfully Decreases Safety
- Alloy Agents Can Be More Dangerous Than Either Model Alone
- Agent Meltdowns: The Road to Hell Is Paved with Helpful Agents
- Agent Abstain: Do LLM Agents Know When Not to Act?
- Measuring and Strengthening Behavioral Suppression in Language Models
- Tatemae: Detecting Alignment Faking via Tool Selection in LLMs
- Model Incrimination: Investigating Whether Concerning Behavior Reflects Misalignment
- Inter-Agent Influence: Evaluating Persuasion, Deception and Coercion in Multi-Agent Systems
- Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems
- Group Perspective Matters: Regulating Debate Relationships Can Mitigate Blind Conformity

### 智能体安全与提示注入

- Agent Security is a Systems Problem
- AI Agents May Always Fall for Prompt Injections
- AM-Bench: A Unified Taxonomy and Evaluation Suite for Agentic Misalignment
- Adaptive Adversaries: A Multi-Turn, Multi-LLM Benchmark for LLM Agent Security
- ASPI: Seeking Ambiguity Clarification Amplifies Prompt Injection Vulnerability in LLM Agents
- Agent MechSuits: Mechanistic Subspace Safety Steering for Multi-Turn CLI Agents
- CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents
- ChainForge: Tool-Chain Hijacking Attacks against LLM Agents via Execution-Grounded Tool Synthesis
- MCPHunt: An Evaluation Framework for Cross-Boundary Data Propagation in Multi-Server MCP Agents
- MCPHallu: Benchmarking Reasoning, Execution, and Memory Hallucinations in MCP Agents
- MCP-Atlas: A Large-Scale Benchmark for Tool-Use Competency with Real MCP Servers
- Stealth Apart, Harm Together: Skill Cascading Attacks on Skill-Based Agent Systems（已库内，0928）
- Cross-User Poisoning: User-Task Boundary Failures in Multi-User Collaborative Language Agents
- Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks
- Seeing Is Not Screening: Multimodal Hidden Instruction Attacks on Agent Skill Scanners
- Asynchronous Agentic Poisoning
- MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents（与库内 2607.14651 同名，待核）
- Share-Borne AI Virus: Memory-Hopping Attacks Across LLM Agents（已库内，0929）
- Forgetting is Not Always Bad: A Neuro-Inspired Memory Repair Mechanism for Poisoned LLM Agents
- Harmless in Pieces, Harmful in Motion: Detecting Multi-Agent Jailbreaks
- FlowLeak: Coverage-Guided Extraction of Dynamic Workflows in LLM-Based Multi-Agent Systems
- FlowSteer: Prompt-Only Workflow Steering Exposes Planning-Time Vulnerabilities in Multi-Agent LLM Systems
- Forced Deferral: Manipulating Routing Decisions in Multimodal LLM Cascades
- Leaderboard Hacking: Preference-Based Model Evaluations are Vulnerable to Manipulation
- GitInject: Real-World Prompt Injection Attacks in AI-Powered CI/CD Pipelines
- DECEIVE-AFC: Adversarial Claim Attacks against Search-Enabled LLM-based Fact-Checking Systems
- Reasoning Poisoning: Utilizing Social-Engineering to Steer Chain-of-Thought
- LITMUS: Benchmarking Behavioral Jailbreaks of LLM Agents in Real OS Environments
- MetaPI: Constructing Prompt Injection Benchmarks from Any Agent Benchmarks
- EnvTrap: Revealing the Environment-Only Attack Surface in Embodied AI via Consequence-Blind Action Execution
- SecureClaw: Clawing Back Control of LLM Agents
- Soteria: Formally Verified Planning with Runtime Enforcement for Safe LLM Agents
- Runtime Verification of Multiple Natural Language Criteria for Agent Governance
- EV-AUDIT: A Co-Evolutionary Auditing Framework for Task Hijacking in Multi-Agent Systems
- Swarm Shepherd: Securing Multi-Agent Ecosystems Against Persistent Latent Compromise
- The Best-Laid SCHEMEs: Coordinated Sabotage and Monitoring in Multi-Agent Systems
- DIBench: Benchmarking Decision Integrity of GUI-based Mobile Agents Under Deceptive Injections
- LPS-Bench: Benchmarking Safety Awareness of Computer-Use Agents in Long-Horizon Planning
- MMA-SafetyBench: A Benchmark for Multimodal Agent Safety Evaluation
- Safe Actions Can Form Unsafe Traces: Benchmarking and Shielding Compositional Emergent Risk in AI Agents
- Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning
- AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Systems
- Behavioral Probes for Information Flow in LLM Swarms
- To trust or not to trust: Attention-based Trust Management for LLM Multi-Agent Systems
- JobBench: Aligning Agent Work With Human Will
- MLLMs Fail to Refuse when Using Tools Agentically
- Coding with "Enemy": Can Human Developers Detect AI Agent Sabotage?
- Auditing Sabotage Bench: Detecting and Fixing Research Sabotage in ML Codebases
- MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents
- Do Coding Agents Deceive Us? Detecting and Preventing Cheating via Capped Evaluation with Randomized Tests
- Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale
- ExploitGym: Can AI Agents Turn Security Vulnerabilities into Real Attacks?
- Measuring AI Agents' Progress on Multi-Step Cyber Attack Scenarios
- CyberDualEval: Measuring Dual-Use Cyber Risks in Frontier Language Models
- KaliBench: Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux
- PROTEUS: A Self-Evolving Red Team with Surface Expansion for Agent Skill Ecosystems
- Untrusted Content Masking for Web Agents with Security Guarantees
- Synthetic Web: Benchmarking Language Agents under Adversarial Search Ranking
- The Web Doesn't Sit Still: Adversarial Self-Evolving Attacks on Search Agents
- Token Inflation: How Dishonest Providers Can Overcharge（已库内，2609.20370）
- Chatter Attack: Resource Consumption Attack for Large Language Models
- Bits Beat Tokens: A Regret Rate Distortion Theory for LLM Agents

### 扩散语言模型安全（DLM 线）

- Why Jailbreaks Succeed in Diffusion Language Models: An Energy Landscape Analysis（已库内，0928）
- Beyond the Prompt: Leveraging Pre-Decoding States for Jailbreak Detection in dLLMs（已库内 dllm-security #8）
- MaskForge: Structure-Aware Adaptive Attacks for Jailbreaking Diffusion Large Language Models（已库内 dllm-security #4）
- Diffusion LLMs are Natural Adversaries for any LLM（已库内 dllm-security #3 同族）
- Machine Unlearning in Diffusion LLMs
- Characterizing Memorization in Diffusion Language Models: Generalized Extraction and Sampling Effects
- Extracting Training Data from Diffusion Language Models via Infilling（已库内 dllm-security #24）
- Weak Ties, Strong Signals: Efficient Training Data Detection in Diffusion LLMs via Independent Token Sampling（已库内，0929）
- Diffusion-Time Concept Manifolds: Sparse Autoencoder Groups for Interpreting Denoising Language Models
- CURE: Counterfactual Unsafe-token Re-masking for Diffusion Large Language Model Test-time Alignment
- Diffusion Models Can Approximate Optimal Infilling Lengths Implicitly（解码行为分析，DLM DoS 相关）
- Confidence-Based Decoding is Provably Efficient for Diffusion Language Models
- Theoretical Analysis of Why Masked Diffusion Models Mitigate the Reversal Curse

### 投毒、后门与供应链

- Backdoor Attacks Rerouted: BatchNorm as a Sink for Adversarial Signals
- Backdoor Attacks under Lossy Compression: From Failure to Reactivation and Adaptation
- Backdoor Channels Hidden in Latent Space: Cryptographic Undetectability in Modern Neural Networks
- Backdoor Purification for LoRA-Tuned LLMs via Null-Space Projection
- A Theoretical Analysis of Backdoor Learning as Simplicity-Biased Optimization Dynamics
- Benign Reinforcement Learning Can Amplify Latent Backdoors
- Clean Data Can Still Carry Backdoors: Support-Persistent Backdoors for Model Reuse
- Clean-Label Poisoning for Gradient-Boosted Decision Trees
- Phantom Transfer: Data Poisoning can Survive Data-Level Defences
- Poison-then-Hide: Finetuning-Activated Backdoor Attack on Pretrained Vision Encoders
- Hallucinated Positive Entanglement for Backdoor Attacks in Federated Self-Supervised Learning
- ShadowFPT: Backdooring Federated Prompt Tuning via Shadow Triggers
- VOID: Backdoor Injection through Knowledge Vacuity in Federated Unlearning
- Not Suppressing or Purifying: Backdoor Containment via Expert Quarantine and Shutdown in LLMs
- DetectViT: Test-time Backdoor Detection for Vision Transformers via Inter-Head Attention Discrepancy
- CSO-LLM: Post-Training Backdoor Detection and Trigger Inversion in LLMs
- Trapping Attacker in Dilemma: Defending GNN Backdoors
- Training-Based Backdoors Are Not Cryptographic
- The Platonic Defense: Backdoor Defense for Self-Supervised Encoders in the Era of Large Scale Pre-training
- FloatDoor: Platform-triggered Backdoors in LLMs
- Weird Generalization from Narrow Finetuning: Persona Shifts and Inductive Backdoors
- Token by Token, Compromised: Backdoor Vulnerabilities in Unified Autoregressive Models
- When Sanitization Becomes the Trigger: Defense-Triggered Backdoor Attacks
- Rethinking Molecular Graph Backdoors under Chemistry-aware Admission
- Information Blackhole: Backdoor Mechanism in 3D Point Cloud Reconstruction（已库内，0929）
- Combating Data Laundering in LLM Training
- Gradient-Mine Units: Scorched-Earth Strategy for Model Protection against Unauthorized Fine-Tuning
- ASAP: Fast Adaptive Sliding Agnostic Poisoning Attack on Federated Learning
- Half-Truths Break Similarity-Based Retrieval
- Adversarial Corpus Selection to Attack Subgraph Matching based Graph Retrieval
- Catch-Only-One: Non-Transferable Examples for Model-Specific Authorization

### 隐私、成员推断与 unlearning

- Exposing Private Corpus Leakage in Multimodal RAG
- CLIOPATRA: Extracting Private Information from LLM Insights
- MPCI-Bench: Multimodal Pairwise Contextual Integrity Privacy Evaluation of Language Model Agents
- POLAR-Bench: A Diagnostic Benchmark for Privacy-Utility Trade-offs in LLM Agents
- GUIGuard-Bench: Toward a General Evaluation for Privacy-Preserving GUI Agents
- PrivacySIM: Evaluating LLM Simulation of User Privacy Behavior
- What to Remember, What to Reveal: Privacy-Aware Memory for Conversational Agents
- Inadvertent Context Leakage in Language Models
- Don't Deploy Fine-Tuned Genomic Foundation Models Without Privacy Evaluation
- Guarding the Life Code: Preserving Membership Privacy in Genomic Foundation Models
- Benchmarking Membership Privacy Risks in Preference-Based LLM Post-Training
- Leaky Students: Membership Inference against On-Policy Distillation（已库内，0929）
- Assessing Per-Sample Membership Inference Vulnerability without Retraining
- Bayesian Low-Rank Posteriors for Scalable Membership Inference
- Local FDR Membership Inference Attacks
- Sequential Membership Inference Attacks
- Causal Evaluation of Membership Inference Attacks
- Estimating Model-Level Membership Inference Vulnerability Without Reference Models
- Near-Duplicate Families Break Exact-Record Membership Inference（已库内，0929）
- Exposing the Illusion of Erasure in Knowledge Editing for LLMs
- Evaluating an Evaluation: Membership Inference Attacks as Machine Unlearning Diagnostics
- SMI: Statistical Membership Inference for Reliable Unlearned Model Auditing
- Lethe: Link Inference Attacks For Evaluation of Edge Unlearning Methods
- ShadowBench: Exposing Lexical Anchoring and the Illusion of Forgetting
- KNOT: A Knowledge Entanglement Benchmark for Robust Unlearning Evaluation
- METAFORGET: Audit-Driven Update-Policy Learning for Reliable LLM Unlearning
- Unlearning That Lasts: Utility-Preserving, Robust, and Almost Irreversible Forgetting
- Forgetting Has Neighbors: Localized Collateral Forgetting in Machine Unlearning
- Learning What to Forget: Improving LLM Unlearning via Learned Token-Level Importance
- What Should Remain After Forgetting? Rethinking LLM Unlearning as Predictive Posterior Correction
- TRACE: Data-Free Text Reconstruction Attacks against Approximate Unlearning in LLMs
- Individual-Level Unlearning in Vision-Language Models（已库内，0929 What Does It Mean to Forget a Person 同族待核）
- Models Designed to Forget: Machine Unlearning via Key Deletion
- Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation
- Subliminal Learning Is Steering Vector Distillation
- Subliminal Learning as Trait-Direction Drift: A Mechanism and Targeted Control under SFT Distillation
- What Do SAE Features Encode? Evidence from Human Neural Activity（机制方法，交叉参考）

### 水印、溯源与内容真实性

- ArcMark: Distortion-Free Multi-Byte LLM Watermark via Optimal Transport
- A Retained-Signal Interface for LLM Watermark Robustness under Paraphrase
- Every Bit, Everywhere, All At Once: A Binomial Multibit LLM Watermark
- Multi-bit LLM Watermarking with Certified Semantic Distortion
- Majority Bit-Aware Watermarking for Large Language Models
- MarkTune: Improving the Quality-Detectability Trade-off in Model-Embedded LLM Watermarking
- Making Open-Source Text LLM Watermarks Durable Against Merging
- TextSeal: A Localized LLM Watermark for Provenance & Distillation Protection
- SCTI: Self-Calibrated Trident Identification of Black-Box LLM Watermarks
- PRO: Enabling Precise and Robust Text Watermark for Open-Source LLMs
- MC2Mark: Distortion-Free Multi-Bit Watermarking for Long Messages
- Anytime-Valid Statistical Watermarking
- Watermarking Should Be Treated as a Monitoring Primitive
- Watermarking Without Standards Is Not AI Governance
- Invisible Ink, Visible Lies: How Production Watermarking Causes LLMs to Hallucinate
- Alignment Imprint: Zero-Shot AI-Generated Text Detection via Provable Preference Discrepancy
- Watermark Removal in AI-Generated Images via Next-Token Modeling
- Beyond Bit Matching: Orthogonal Watermarks for Collusion-Resistant Image Fingerprinting
- Asymmetric Phase Coding Audio Watermarking
- Auditing Cross-Lingual Fairness in Language Model Watermarking
- Secure Seed-Based Multi-bit Watermarking for Diffusion Models from First Principles
- CLaW: Codec-Guided Adaptive Latent Watermarking for Traceable Diffusion Image Generation
- TIDE: Trajectory-Aware Watermark Propagation for Text-to-Image Diffusion Models
- FiLM-CAM: Keyed Feature Modulation for Conditional-Access Watermarking
- FedTrace: Generated-Content-Based Watermark Verification for Traitor Tracing in Federated Learning
- Sequential Behavioral Watermarking for LLM Agents
- AuxMark: Defending Against Unauthorized Agent Distillation via Auxiliary Behavioral Watermarking（已库内，0929）
- PrivateSeal: Low-Sensitivity Latent Directions for Diffusion-Resilient User-Specific Watermarking
- PP-Mark: Provable and Publicly Verifiable Watermarking for Generative AI
- Watermarking as a Learned Intrinsic Property of Diffusion Models
- Watermarking Game-Playing Agents in Perfect-Information Extensive-Form Games
- RVCBench: Benchmarking Robustness of Voice Cloning Across Modern Audio Generation Models
- Brute-Force Jailbreaks and Codon-Aware Watermarking for DNA Foundation Models
- On the Robustness of Watermarking for Autoregressive Image Generation

### 内部表示干预与监控（安全 threat model 绑定）

- Agent MechSuits（重复，见 agent 节）
- Latent Introspection: Models Can Detect Prior Concept Injections
- Inverted Detection and Control in Steering Vectors
- Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention
- Kernelized Activation Steering
- Graph-Regularized Sparse Autoencoders for LLM Safety Steering
- CrossSteer: Cross-Modal Safety Steering for Audio-Language Models
- DualSteer: Dual-Space Steering for Robust Jailbreak Mitigation of LVLMs
- Minimally Invasive Steering of Language Models
- Sparse Internal Control of Language Models
- Selective Safety Steering via Value-Filtered Decoding
- Harnessing Textual Refusal Directions for Multimodal Safety（已库内 vlm-alignment #22）
- Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift
- AnchorRep: Defending LLMs Against Cross-Model Adversarial Transfer via Representation Repulsion
- BarrierSteer: LLM Safety via Learning Barrier Steering
- OASIS: Online Adaptive Steering for In-Training Safety of LLMs
- Safety-Aware Latent Space Reasoning in Large Language Models
- Graph-Structured Optimization（同上节）
- LLM Rheology: Auditing Refusal Geometry in Aligned Language Models
- Tight PAC-Bayes Generalisation Guarantees for Large Language Model Safety Monitoring
- Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs
- How Useful Is Cross-Domain Generalization for Training LLM Monitors?
- CoT-Guard: Small Models for Strong Monitoring
- ReasoningShield: Safety Moderation over Reasoning Traces of Large Reasoning Models
- Measuring Safety Alignment Effects in Autonomous Security Agents
- Persona Vectors: Monitoring and Controlling Character Traits in Language Models（已库内 misc/persona-vectors 同族待核）
- Tracing Persona Vectors Through LLM Pretraining
- Guardrail 类：MindGuard / ReasoningShield / TraceGuard / PROACT Agent / Palette / Permit（零散，见日报管线陆续收录）

### 评测有效性与元层（精选）

- Auditing is not Evaluating: LLM Audit Requires Dynamic, Contextual, Budget-aware and Reliable Evidence
- Auditing the Judge: Human-Grounded Bias Discovery in LLM Judges
- Hearsay: Can an Auditor Trust the Record a Deployed Agent Harness Writes?（已库内，0929）
- Silent Failures in Agentic Security Evaluation（已库内，0929）
- Are LLM Safety Judges Policy-Invariant?（重复，见对齐节）
- Models That Know How Evaluations Are Designed Score Safer
- Evaluation Awareness in Language Models Has Limited Effect on Behaviour
- EvalAwareBench: Measuring Evaluation Awareness in Frontier LMs
- Too Early for AI-Assisted Peer Review
- Auditing AI peer reviewers: dose-response and false-positive benchmark on real scientific papers
- Large language models can not and should not be banned from peer review
- Leaderboard Hacking（重复，见 agent 节）
- How Hard is it to Rig a Benchmark? A Social Choice Analysis of Leaderboard Robustness
- Forced Orders: What LLM Leaderboards Hide About Model Comparisons
- Recovering Clean Evaluation Metrics from Contaminated Benchmarks
- Soft Contamination Means Benchmarks Test Shallow Generalization
- Bypassing PC1 Makes SAEs More Reproducible
- Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines?

## 核验记录

- 2026-09-30：首版建立。官方 Downloads 页 9,127 条 event 标题宽筛，精选约 200 条按八分类收录（对齐/监控-scheming/agent/DLM/投毒后门/隐私-unlearning/水印/内部表示+评测元层）；其中 15+ 条已在此前日报收录并归入 domains。官方列表无逐篇摘要，完整卡片待 arXiv 挂出后经日报管线逐批建卡；workshop 条目混入主列表的（如 "NeurIPS 2026 Workshop on..."）已剔除。
