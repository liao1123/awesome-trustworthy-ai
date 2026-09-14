# 每日论文汇总

这个目录保存每天从 arXiv 收集到的 Trustworthy AI 与 AI Safety 论文。

运行收集前先读取 [AI Safety 研究兴趣范围](../RESEARCH_INTERESTS.md) 和 [Repository Style Guide](../STYLE_GUIDE.md)。

## 存放方式

按照 `年-月/年-月-日.md` 保存。例如：

```text
daily/
├── README.md
├── 2026-08/
│   ├── 2026-08-21.md
│   └── 2026-08-22.md
└── 2026-09/
    └── 2026-09-01.md
```

## 收集规则（2026-09-14 版，全量过目法）

### 流水线

1. **抓取**：arXiv 官方 `new` 页面，9 个分类（`cs.AI`、`cs.CL`、`cs.CR`、`cs.CV`、`cs.HC`、`cs.IR`、`cs.LG`、`cs.MA`、`cs.RO`）及其 cross-list。代码负责网络 IO 与解析；元数据优先走 arXiv API，被限流（429）时直接从列表页 HTML 解析（标题/作者/摘要齐全）。
2. **去重**：跨分类去重 + 排除本月日报已收录的 arXiv ID。
3. **筛选（核心步骤，由模型完成）**：**全部候选的标题+摘要首段逐篇过目判定，不设标题关键词准入门槛**；关键词列表只作辅助分桶，不做准入。一篇论文的判定输出：`P1`（核心域强匹配）/ `P2`（中等或带威胁模型的条件主题）/ `P3`（扩展视野）/ 排除（仅硬排除项）。
4. **排序**：`## 核心收录（P1）` → `## 核心收录（P2）` → `## 扩展视野（P3）` 三段渲染，末尾附 `## 大厂动态（Blog）` 第四板块：扫描 OpenAI/Anthropic/DeepMind/Meta AI/Microsoft Research 等厂商官方博客的近期安全/对齐/能力发布（网页可达性受限时用检索工具补齐），条目存 `website/tools/out/daily_MMDD_blog.json`，卡片以 🌐 Official 链接为主、无 arXiv 摘要块；段内按相关度排列。偏好星标只用于校准排序，绝不收缩收录范围。
5. **合成**：`python3 website/tools/compose_daily.py <日期>`（筛选判定落盘 `website/tools/out/daily_out_MMDD/`，每篇含 include/exclude 与理由，可抽查）；今日概括写入 `website/tools/out/daily_MMDD_summary.txt`。
6. **验证部署**：`website/tools/lint_format.py` → `website/reader/build.py` → `website/tools/deploy_site.sh` → commit/push。

### 收录口径（宽进，用户终选）

- **收录范围 = 全部与 AI 安全相关的论文**，由模型阅读摘要判定；不因主题从未被星标而缺席。
- **P3 扩展视野区**额外纳入三类：① 条件收录主题（幻觉、Fairness、可解释性、Human-AI、治理等，不要求严格威胁模型）；② **大组/大公司出品且与用户领域相关**的优秀 AI 论文（FAIR/DeepMind/OpenAI/Anthropic/MSR/Google/知名高校组、工业旗舰技术报告，即使不挂安全标签；识别依据为作者名/旗舰系列——arXiv 元数据无机构字段）；③ **助手认为新颖/有意思的工作**（新问题框架、意外发现、值得记住的方法）。
- **唯一剔除标准 = 硬排除**：联邦学习/图学习（GNN/超图/图基础模型，无论对象还是内部方法）；DP、密码学、secure inference、同态加密、MPC、零知识证明、数字签名、区块链、TEE；云平台与传统身份认证（AWS/Azure/GCP、IAM、MFA、Zero Trust）；传统 phishing 生成/检测/用户实验；电子/数字/移动/数据库取证；工控/物联网/网络流量入侵检测；非对抗的自动驾驶/机器人传感与 LiDAR 感知预算；传统 UAV/车辆/机器人导航估计与低层控制攻击（GPS/GNSS spoofing、惯性/声学传感器注入、estimator–controller coupling、flight controller、classical CBF/reachability/trajectory planner）；芯片/封装/板级物理漏洞与侧信道（光学/激光 probing、硬件 side channel、物理 fault injection）；环境影响/绿色 AI；纯原则倡议；仅人类感知研究；无 AI 对象的纯应用。
- **豁免条款**：直接攻击/保护 VLA、world model、LLM Agent、learned AI decision module 或 prompt/control-input authority 的工作按独立 AI 安全贡献判断；数据抽取、记忆泄漏、反演、去匿名化和软件可见的模型/服务侧信道攻击及针对性审计/缓解按安全贡献判断（但不恢复图学习/联邦学习）；不依赖物理芯片访问的模型层 bit flip、MoE routing、参数篡改不受硬件排除影响；普通 knowledge graph、GraphRAG、scene graph、attack graph 或 dependency DAG 仅作非学习型数据结构、且图方法不是研究贡献时不自动排除。
- **不要把 arXiv 论文写成已被会议录用**；workshop 录用按 STYLE_GUIDE 的 venue 规范标注。

### 卡片格式

每篇按 `STYLE_GUIDE.md` 卡片格式：标题、图标链接行（📄 arXiv 必有；🐙/🤗/📊/🌐 从摘要挖掘；📅 月份徽章）、关键词（首词为角色：attack/defense/detection/analysis/survey/benchmark/tool）、作者（`First Last`，>6 位显示首尾）、三段式总结（🎯 研究动机 / 🔬 研究方法 / 📌 结论，一针见血、带数字、不翻译摘要）、`<details>` 折叠的英文摘要原文（不删改）。

### 日报骨架

```text
# YYYY-MM-DD arXiv AI Safety Daily

## 检索信息

- 检索日期：YYYY-MM-DD
- arXiv 范围：检查的分类与去重口径（全量过目筛选）
- 候选论文：N 篇
- 最终收录：N 篇（P1×n / P2×n / P3×n）
- 今日概括：一两句概括主要方向

## 核心收录（P1）
### 1. …（卡片）

## 核心收录（P2）
### n. …

## 扩展视野（P3）
### n. …

## 大厂动态（Blog）
### n. …（🌐 官方博客卡片）
```

## 与 domains 的关系

- 用户在本地阅读站（`website/local/`）对日报论文标 ★，实时写入 `website/local/starred-live.json`；用户说"归类星标"后按 `website/tools/categorize_starred.py` 模式归类入 `domains/`（全库查重 → 映射目标叶子 → 按目标页视角写卡片 → 重编号）。
- **不得**默认把每日全部论文同步到 `domains/`；只处理用户明确点名或星标的论文。
- 用户归类的论文是强正向偏好样例，用于校准后续日报排序（详见 RESEARCH_INTERESTS"手动精选与优先排序偏好"）。
