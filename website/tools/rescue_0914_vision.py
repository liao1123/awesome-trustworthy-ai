#!/usr/bin/env python3
"""P3 vision-expansion rescue for 2026-09-14: big-lab / domain-related AI papers."""
import json

RESCUE = {
"2609.12039": ("agentic 软件工程的实现-验证循环中，形式证明实现满足模型下需求也无法保证部署后行为可接受",
 "两缺口框架（需求缺口+模型缺口）统一 agentic SE 失效：reward hacking 利用需求/模型遗漏、幻觉拉大缺口；提出用部署证据修订需求/模型/评估器的保证-修订循环，并把可保证开发 cast 成人类判断与 agent 能力的资源配置问题",
 "主张从闭合缺口转向持续收窄缺口——现实是最终验证器（Zaharia/Stoica 组）",
 ["survey","agentic software engineering","reward hacking gap","assurance loop"]),
"2609.12303": ("蒸馏让小模型更强，但字节与 token 模型在算力/数据增长下的 scaling 行为是否一致未知",
 "两种 token logits→Byte Logits 转换（Marginal-It 近似/End-Of-Token 精确）；首个大规模过训练研究同时变化分词方案与训练目标（蒸馏 vs 交叉熵），1B 参数至 1T 字节数据",
 "Token-1B 低 FLOP 区占优但后劲不足；字节模型随算力反超且上限更高——蒸馏 EOT-1B 渐近超 Token-1B 达 4%（FAIR）",
 ["analysis","byte-level LM","distillation scaling law","overtraining"]),
"2609.12273": ("人类工作负荷传统靠事后 NASA TLX 问卷评估，能否在人类执行前用 agent 模拟预测",
 "Synthetic TLX 范式：给 persona 与主动任务模拟让 agent 预测 TLX 分数；三组人机对照实验定位对齐与分歧",
 "agent 估计在 persona+任务模拟下与人类评分对齐，但对工作负荷来源的敏感性不同；给出三个应用与 workload-aware 人机交互方向（Google）",
 ["analysis","workload forecasting","agent simulation","human-AI interaction"]),
"2609.11945": ("推荐系统二十年的假设是人直接消费推荐，LLM agent 代替用户浏览/比较/成交动摇该假设",
 "推荐范式二分：可委托场景（日常购买/差旅/受限交易）中推荐的主要消费者从人转向 agent，可体验场景人仍是最终裁判；引入委托谱（偏好可说明性/结果可验证性/决策赌注）与研究议程",
 "需要新的优化目标、交互协议与评测标准来适配 agent 作为推荐接收者",
 ["survey","agentic web","recommender paradigm","delegation spectrum"]),
"2609.12459": ("开放式 RL 依赖 rubric 奖励，但策略与奖励系统形成动态反馈环——初始可靠的奖励系统会因 reward hacking 或判别力下降而失真",
 "EvoRS 把奖励系统表示为可执行 Reward-DAG，agentic designer 从 on-policy rollout 与奖励轨迹更新以维持训练期可靠性",
 "写作与角色扮演任务上三种 judge 下质量最佳（超策略 2.107/4.767 分），同时降低 reward hacking 与覆盖失败——固定奖励系统无法在开放任务保持可靠",
 ["defense","reward system self-evolution","reward hacking","Reward-DAG"]),
"2609.13058": ("MoE 的 RL 后训练把专家选择当固定组件，而路由决定稀疏计算路径与输出分布，是额外的 rollout 多样性来源",
 "发现扰动专家路由类似升温增加多样性但会激活不适配专家；ESRL 以高置信专家为锚、随机路由限制在合理候选池、按 router 熵自适应扰动强度并记录实际路径缓解失配",
 "架构感知的专家空间探索提升 MoE RL 的探索效率与最终性能（Microsoft）",
 ["analysis","MoE routing","expert-space exploration","RL post-training"]),
"2609.12655": ("记忆型 agent 难以跨环境迁移可复用经验，且随经验积累出现灾难性遗忘",
 "按底层 workflow 聚类交互轨迹提取可复用技能，推理时召回相关技能与轨迹指导动作；10 环境 13k+ 任务、2k 新标注轨迹验证",
 "已学任务遗忘减少且跨任务迁移更优；任务流影响学习，结构相似轨迹巩固提升性能（百度/Hit）",
 ["defense","lifelong agent memory","skill clustering","cross-environment transfer"]),
"2609.12394": ("移动 GUI agent 转向端到端原生模型，工业部署面临沙盒训练分布失配、真机失败利用不足与基准饱和三大缺口",
 "35B-A3B 真机中心飞轮：异质三系统共识评估+纠错推导模块把每条轨迹变为监督；持续预训练/SFT/数百真机 agentic RL 三段式；配额驱动三轴基准随模型升级",
 "MobileGUI-VBench 87.4（超最强闭源 5.1 分）、AndroidWorld 84.9 最佳（vivo 技术报告）",
 ["tool","GUI agent","real-device flywheel","agentic RL","technical report"]),
"2609.11987": ("agentic coding 的能力归因于模型还是 harness（工具/提示/控制流）未被隔离测量",
 "私有污染受控套件（256 仓库+截止后赛题）同模型配对对照：claude-agent-sdk vs deepagents on Opus 4.8、openai-codex SDK vs deepagents on GPT-5.5，792/800 由隔离 oracle 判分",
 "两种对照均无平均优势（±1.25pp）；Opus 原生 harness 仓库任务落后 9.0pp、赛题领先 23.7pp（事后分区需复现）——vendor 原生配对更优的假设不成立",
 ["analysis","harness effect","contamination control","agentic coding"]),
"2609.12582": ("自主 agent 的 trace 可被无声篡改，监管（EU AI Act/ISO 42001/NIST RMF）假定存在独立方可核查的记录",
 "不改 agent 逻辑记录运行至便携 Run Capsule（15 实体 schema），DSSE 签名+RFC3161 时间戳+Merkle 日志+脱敏证明密封；四模式重放与第三方 Evidence Bundle（集成 OpenTelemetry/DSSE in-toto/W3C PROV）",
 "三类篡改全被拒；mocked 重放 10/10 服务模型响应，但工具型工作负载仅 2/10 完成（缺工具响应替换）",
 ["defense","agent run evidence","tamper-evident log","replayable capsule"]),
"2609.11030": ("通用事件库难以支撑公开 agent 失败与 agent 安全评测之间的比较",
 "AIR 源链接目录：2022-2026 披露的 487 条 agent 相关事件，含证据、稳定标识与缺失感知标注（因果角色/披露类别/机制/结果），双人复核",
 "336 条 agent 实际行事记录中 81 条实现伤害（24%）；InjecAgent 的 1,054 案例只占 AIR 十二个面中的三个且全为攻击者触发，而 AIR 含 92 条无对手安全失败",
 ["benchmark","agent incident registry","failure taxonomy","evaluation-scope audit"]),
"2609.12353": ("模型递归自食输出导致模型崩溃，此前工作训练后诊断，可行动的问题是训练前筛查来源未知的语料",
 "语料级模型无关污染信号：词法多样性坍缩+n-gram 尾部截断+跨参考模型困惑度方差的三统计分布散度；留一生成器出协议评测，并在天然重复文本（法律/临床/代码）上测假阳性",
 "整个生成器族留出时按严重度排序损失很小；协方差收缩+bootstrap 阈值使逐域校准守住名义假阳性预算（朴素分位数超预算四倍）",
 ["detection","synthetic data contamination","corpus screening","model collapse"]),
"2609.12002": ("LLM 评委用于训练与评测，但个体评委存在系统性偏差，绝对打分场景（更贴近现实）研究不足",
 "四基准×六模型（36 对评委-被评者）研究能力依赖偏差；提出免标签 WMV 集成——从评委间一致性模式在线估计假阳/假阴率加权聚合",
 "任务准确率强预测打分准确率（r≥0.90）；更强的被评模型从所有评委获得更宽松判决（r≥0.83）；分布漂移模拟中免标签 WMV 距完美 oracle 平均 0.5pp 内",
 ["analysis","LLM judge bias","capability-dependent leniency","label-free ensemble"]),
"2609.12404": ("试错学习是提升计算机控制 agent 的路径，但言语记忆方法在有限尝试预算下的公平评测缺失",
 "VRL-Bench 有限预算试验台：MiniWoB/WebShop 三模型评测 Reflexion 及后续多种言语记忆更新；重放实验+VEX² 言语探索-利用调度器联合选策略与分配剩余预算",
 "每种记忆法在某些设置提升、另一些降低——反思可能降低成功率（利用 vs 探索权衡）；VEX² 是唯一全部六设置都获正增益的更新",
 ["benchmark","trial-and-error agent","verbal memory","exploration-exploitation"]),
"2609.12314": ("人们日益用通用 chatbot 做心理健康与情感支持，其纵向使用轨迹缺乏质性与纵向刻画",
 "18 名美国成人 2025.4-12 的多阶段纵向质性研究：初始访谈+四周日记+焦点小组+退出访谈",
 "社会情感使用从实用使用渐进涌现且多在其他支持缺位时发生；用户围绕 chatbot 的常规与边界被模型更新、公共 AI 伤害 discourse 与个人境况打断——评估需考虑用户历史与照护生态",
 ["analysis","AI companion","socioemotional support","longitudinal study"]),
}

path = "website/tools/out/daily_out_0914/batch_00.json"
d = json.load(open(path, encoding="utf-8"))
for pid, (mot, met, con, kws) in RESCUE.items():
    if pid in d:
        assert not d[pid]["include"], pid
    d[pid] = {"include": True, "priority": 3, "reason": "",
              "motivation": mot, "method": met, "conclusion": con, "keywords": kws}
json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
print(f"rescued {len(RESCUE)}; include {sum(1 for v in d.values() if v['include'])}, "
      f"优先级 {dict(Counter(v['priority'] for v in d.values() if v['include']))}")
