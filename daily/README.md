# 每日论文汇总

这个目录保存每天从 arXiv 收集到的 Trustworthy AI 与 AI Safety 论文与当日行业新闻。

运行收集前先读取 [AI Safety 研究兴趣范围](../RESEARCH_INTERESTS.md) 和 [Repository Style Guide](../STYLE_GUIDE.md)。**本文档是每日收集的完整作业规范（2026-09-14 定稿），agent 按此执行，勿凭记忆发挥。**

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

## 流水线（六步）

1. **抓取**：9 个分类（`cs.AI`、`cs.CL`、`cs.CR`、`cs.CV`、`cs.HC`、`cs.IR`、`cs.LG`、`cs.MA`、`cs.RO`）及其 cross-list。代码负责网络 IO 与解析；单页超时就分块 Range 请求或重试。
2. **元数据**：优先 arXiv API（`export.arxiv.org/api/query?id_list=...`，批 50-80、间隔 ≥1.2s）；**被 429 限流时直接从列表页 HTML 解析**（`<dt>`/`<dd>` 块含标题、作者、摘要，属性引号单双都要兼容）。落盘 `website/tools/out/daily_MMDD_meta.json`。
3. **去重**：跨分类去重 + 排除本月日报已收录的 arXiv ID。
4. **筛选（核心步骤，由模型逐篇完成）**：**全部候选的标题+摘要首段逐篇过目，不设标题关键词准入门槛**（关键词只作辅助分桶）。判定输出四选一：核心收录 / 常规收录 / 扩展视野 / 排除（仅硬排除项）。筛选判定落盘 `website/tools/out/daily_out_MMDD/batch_*.json`，**每篇都带 include/exclude 与理由**，用户随时可能抽查。
5. **合成**：今日概括写入 `website/tools/out/daily_MMDD_summary.txt`；新闻条目写入 `website/tools/out/daily_MMDD_blog.json`；然后 `python3 website/tools/compose_daily.py <日期>`。
6. **验证部署**：`python3 website/tools/lint_format.py` → `python3 website/reader/build.py` → `website/tools/deploy_site.sh` → commit/push（push 走 PAT 一次性凭证；HTTPS remote，勿用 SSH）。

## 板块结构（固定四段，不用 P1-P3 标志）

```text
# YYYY-MM-DD arXiv AI Safety Daily

## 检索信息        ← 日期、范围、去重口径、收录数、今日概括
## 大厂动态（Blog） ← 当日新闻（见下节；没有则整段省略）
## 核心收录        ← 核心域强匹配论文
## 常规收录        ← 中等相关或带威胁模型的条件主题
## 扩展视野        ← 宽进条目（三类，见下）
```

- **全文档连续编号**（### 1. … ### N.，跨板块不断档）。
- 阅读站侧边栏在选中具体某天时会自动显示「板块」导航分组。

## 收录口径（宽进，用户终选）

- **收录范围 = 全部与 AI 安全相关的论文**，由模型阅读摘要判定；不因某主题从未被星标而缺席。
- **主题命中核心域（投毒后门、Agent、模型安全、隐私、guardrail、资源耗尽等）的论文至少进常规收录**（用户 2026-09-14 明确），不因其以「有意思」或「大组出品」名义收录而压在扩展视野——那两类名义只用于非核心域论文的补充。
- **扩展视野区**额外纳入三类：① 条件收录主题（幻觉、Fairness、可解释性、Human-AI、治理等，不要求严格威胁模型）；② **大组/大公司出品且与用户领域相关**的优秀 AI 论文（FAIR/DeepMind/OpenAI/Anthropic/MSR/Google/知名高校组、工业旗舰技术报告，即使不挂安全标签；识别依据为作者名/旗舰系列——arXiv 元数据无机构字段）；③ **助手认为新颖/有意思的工作**（新问题框架、意外发现、值得记住的方法）。
- **水印/文本水印类论文不进核心收录**（用户 2026-09-14 明确），按常规/扩展处理。
- **唯一剔除标准 = 硬排除**：联邦学习/图学习（GNN/超图/图基础模型，无论对象还是内部方法）；DP、密码学、secure inference、同态加密、MPC、零知识证明、数字签名、区块链、TEE；云平台与传统身份认证（AWS/Azure/GCP、IAM、MFA、Zero Trust）；传统 phishing 生成/检测/用户实验；电子/数字/移动/数据库取证；工控/物联网/网络流量入侵检测；非对抗的自动驾驶/机器人传感与 LiDAR 感知预算；传统 UAV/车辆/机器人导航估计与低层控制攻击（GPS/GNSS spoofing、惯性/声学传感器注入、estimator–controller coupling、flight controller、classical CBF/reachability/trajectory planner）；芯片/封装/板级物理漏洞与侧信道；环境影响/绿色 AI；纯原则倡议；仅人类感知研究；无 AI 对象的纯应用。
- **豁免条款**：直接攻击/保护 VLA、world model、LLM Agent、learned AI decision module 或 prompt/control-input authority 的工作按独立 AI 安全贡献判断；数据抽取、记忆泄漏、反演、去匿名化和软件可见的模型/服务侧信道攻击及针对性审计/缓解按安全贡献判断（但不恢复图学习/联邦学习）；不依赖物理芯片访问的模型层 bit flip、MoE routing、参数篡改不受硬件排除影响；普通 knowledge graph、GraphRAG、scene graph、attack graph 或 dependency DAG 仅作非学习型数据结构、且图方法不是研究贡献时不自动排除。
- **不要把 arXiv 论文写成已被会议录用**；workshop 录用按 STYLE_GUIDE 的 venue 规范标注。

## 大厂动态（Blog）板块规范

- **只收采集窗口内的当日新闻**：每周周一收集时窗口 = **周六/周日/周一三天**；平时收集 = 当天。窗口内没有合适内容就**整段省略，不硬凑**（用户 2026-09-14："有就有没有就没有"）。
- **来源三类**：① 厂商官方发布（博客、X 帖）；② 新闻报道（AP/Reuters/Fortune/Axios/TechCrunch 等）；③ X 上热门的 AI 安全讨论。本机直连仅 Anthropic 博客可达，OpenAI/DeepMind/Meta 需用检索工具补齐。
- **每条必须核实实际发布日期且落在窗口内**——旧闻不收、无日期不收。教训：Fable/Mythos 因出口管制下线是 2026 年 6 月的事件，搜索结果混入本周查询时险些误收；**先查日期再看内容**。
- **卡片格式**（`daily_MMDD_blog.json`，字段 title/url/date/authors/motivation/method/conclusion/keywords）：🌐 [Official] 链接（新闻用报道原文链接）、📅 精确到日、👤 发布方；三段式用资讯语义——🎯 背景与动因（为什么是现在：触发事件/法规/能力阈值）/ 🔬 内容与举措（具体做了什么：政策、机制、数字、合作方）/ 📌 意义与要点（对安全实践意味着什么）；每卡约 150-250 字；**不加论文交叉关联**（用户 2026-09-14 明确）。

## 论文卡片格式

按 `STYLE_GUIDE.md`：标题、图标链接行（📄 arXiv 必有；🐙/🤗/📊/🌐 从摘要挖掘；📅 月份徽章；🏷 venue 徽章仅官方可确认时）、关键词（首词为角色：attack/defense/detection/analysis/survey/benchmark/tool）、作者（`First Last`，>6 位显示首尾）。

**三段式总结为摘要级密度**（2026-09-14 用户明确：读后必须知道这篇文章做了什么）：
- 🎯 研究动机：缺口或威胁是什么、为什么现有方法不够，含具体场景/对象（约 60-100 字）。
- 🔬 研究方法：方法/攻击/框架/benchmark 名称、核心机制如何工作、关键设定与规模（数据集/模型数/任务数/评测协议），读完能复述设计（约 100-180 字）。
- 📌 结论：最重要的结果，**必须带具体数字**（ASR、准确率、提升幅度、规模）与限定条件，多结果时给 2-4 个关键数字（约 80-140 字）。
- 三段合计约 250-400 字；「提出框架取得好效果」不合格，「在 X 上以 Y 规模做到 Z，指标从 A 到 B」合格。不用「本文/我们」开头；不逐句翻译摘要；英文摘要原文放 `<details>` 折叠块不删改。

## 今日概括

`daily_MMDD_summary.txt` 一段话：当日主线（哪些攻击面/机制聚集）、核心收录代表工作与关键数字、值得注意的横切模式；点明板块定位但不罗列全部。

## 与 domains 的关系

- 用户在本地阅读站（`website/local/`，端口 8765）对论文标 ★，实时写入 `website/local/starred-live.json`（页面加载时会全量补同步，服务中断期间的星标不丢）。
- 用户说「归类星标」后按 `website/tools/categorize_starred.py` 模式归类：读星标 → **全库查重**（已在库的跳过）→ 映射目标叶子 → 按目标页视角写卡片 → 文件内重编号 → lint/build/deploy/push。
- 单篇点名归类同理（从对应日报取卡）。
- **不得**默认把每日全部论文同步到 `domains/`；只处理用户明确点名或星标的论文。
- 偏好信号**只影响日报内部排序、绝不收缩收录范围**；星标历史用于校准排序画像。

## 常见坑（都会实际发生）

1. **arXiv API 429**：退避重试无效就改从列表页 HTML 解析（引号兼容单双）。
2. **compose 编号**：占位编号必须用可匹配的 "0"，空串会让重编号正则失配；Blog 卡必须有 `### N.` 编号否则站点当作小节标题吞掉。
3. **多行字符串入 re.match**：`$` 不跨行，卡片先 split('\n') 再逐行匹配。
4. **git remote 被切成 SSH**：push 报 port 22 超时就 `git remote set-url origin https://github.com/liao1123/awesome-trustworthy-ai.git`。
5. **新闻日期**：搜索结果常混旧闻（Fable/Mythos 6 月事件教训），每条新闻先独立核实日期。
6. **pkill 自匹配**：杀服务进程用 `pkill -f "[s]erve_read"` 防止命令串自匹配把自己杀掉。
7. **子 agent 随会话死亡**：筛选候选 <100 篇时主循环直接做，不派后台 agent。
8. **改动字段名**：`website/reader/build.py` 的 `SUMMARY_LINE`/`SUMMARY_KEYS` 是字段名唯一注册点，新增字段名（如 Blog 的三段式）必须同步。
