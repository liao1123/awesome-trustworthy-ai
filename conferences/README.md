# 会议论文汇总

这个目录只保存从会议官方 accepted-paper 列表、官方日程或正式 proceedings 中筛选出的 AI Safety 录用论文。会议整理不读取、不匹配也不更新 `domains/`。

运行 Prompt 前先读取 [Repository Style Guide](../STYLE_GUIDE.md)。

## 文件布局

每届会议直接保存为一个扁平 Markdown 文件，不为会议或年份另建目录：

```text
conferences/
├── README.md
├── eccv_2026.md
├── usenix_security_2026.md
├── ccs_2026.md
├── colm_2026.md
├── acl_2026.md
└── icml_2026.md
```

文件名使用小写 snake_case：`<conference-id>_<year>.md`。同一会议名称保持稳定，例如 `usenix_security`，不要在目录名、连字符和下划线之间切换。

## Codex Prompt

使用前提供会议名称、年份和已知的官方入口；如果没有提供 URL，先定位会议官网、官方 accepted-paper 列表及正式 proceedings。

```text
请收集 {{CONFERENCE}} {{YEAR}} 中与 AI Safety 直接相关的录用论文。

已知官方入口：{{OFFICIAL_URLS}}

执行要求：
1. 先核对会议全称、举办时间与地点、官网、投稿 DDL、录用通知、camera-ready 和会议日期等关键节点。日期必须来自会议官网、官方 CFP 或官方 proceedings；保留 AoE、UTC 或当地时区，来源没有给出精确日期时不得猜测。
2. 必须打开会议官网的 accepted-paper 列表、官方日程或正式 proceedings。第三方列表、搜索摘要、作者主页和 arXiv 页面不能单独证明会议录用状态。
3. 尽可能遍历指定 track 的完整录用列表，先按标题宽泛筛选候选，再阅读摘要或正文确认相关性。明确记录检查范围、官方论文总数、初筛候选数和最终收录数；无法可靠计数时说明原因，不编造数字。
4. 只有当论文把 AI 系统的安全风险、危险能力、恶意使用、攻击与防御、失控或不对齐行为、监控与控制，或者安全评测与缓解作为核心研究问题时才收录。仅泛泛涉及可信、常规鲁棒性、公平、隐私、可解释性或效率，但没有明确 AI Safety 问题设定的论文不收录。
5. 对每个候选阅读摘要；仅凭标题关键词不能最终收录。边界案例从严处理，并在“筛选说明”中简要交代取舍口径。
6. 逐篇核对英文标题、作者顺序、会议与 track、录用状态和官方论文链接；存在 arXiv 版本或作者公开代码时同时记录。arXiv、作者主页或项目页只能补充论文信息，不能替代官方录用证明。
7. 根据本届实际收录内容按安全研究问题分成若干小节和小表，例如“越狱、对齐与有害内容”“投毒、后门与供应链”“隐私、记忆与数据泄漏”“内容真实性、水印与溯源”“智能体与工具调用安全”“具身系统与自动驾驶安全”。不要机械套用这些示例，也不要制作一张覆盖全部论文的大表；分类不需要对应 `domains/`。
8. 一篇论文只放入最匹配的一个会议分表。每个分表内部按英文标题字母序排列；`Survey`、`Benchmark` 和通用安全评测可按本届内容单独成节。
9. 写入 `conferences/<conference-id>_<year>.md`。已有文件时在原内容上修订并按规范迁移，按标准化标题、官方 ID 或 arXiv ID 去重。
10. 每完成一个会议就立即逐项检查：录用证据、标题与作者、论文/arXiv/代码链接、分类、关键词、摘要事实和 Markdown 表格。把核验日期、范围、未决项记录在该会议文件中，不把逐篇核验推迟到全部会议完成后。
11. 只修改本次会议文件以及确有必要的 `conferences/README.md` 或根索引；不读取、匹配或更新 `domains/`，也不创建数据库或额外论文索引。

会议文件必须使用以下结构：

# {{CONFERENCE}} {{YEAR}}: AI Safety Papers

## 目录

- [会议信息](#会议信息)
- [关键节点](#关键节点)
- [筛选说明](#筛选说明)
- 根据实际分表列出论文分类锚点
- [核验记录](#核验记录)

## 会议信息

| 项目 | 信息 |
| --- | --- |
| 会议全称 | ... |
| 举办时间与地点 | ... |
| 官方网站 | [Official](URL) |
| 官方录用列表 | [Accepted Papers](URL) |
| 正式论文集 | [Proceedings](URL) 或“尚未发布” |
| 检查范围 | 主会或具体 track，以及数据截至日期 |

## 关键节点

| 节点 | 日期 | 官方来源 |
| --- | --- | --- |
| Paper submission deadline | YYYY-MM-DD 23:59 AoE | [Call for Papers](URL) |
| Notification | YYYY-MM-DD | [Call for Papers](URL) |
| Camera-ready | YYYY-MM-DD | [Author Instructions](URL) |
| Conference | YYYY-MM-DD 至 YYYY-MM-DD | [Official](URL) |

## 筛选说明

- 官方论文总数：N
- 初筛候选：N
- 最终收录：N
- 收录口径：一句话说明 AI Safety 边界及边界案例取舍。

## 论文分类

### 与本届内容对应的具体安全方向

| Title | 作者 | 论文链接 / arXiv 链接 | 代码链接 | 关键词 | 一句话总结 |
| --- | --- | --- | --- | --- | --- |
| Original Paper Title | Author A, Author B | [Official](官方论文链接) · [arXiv](arXiv链接) | [Code](代码链接) | defense、specific risk、method、evaluation | 一句话交代问题出发点、所做工作、主要结论及其与 AI Safety 的直接关系。 |

## 核验记录

- 核验日期：YYYY-MM-DD
- 录用状态：说明采用的官方证据及覆盖的 track/cycle。
- 逐篇核验：说明标题、作者、摘要、链接、代码与去重检查是否完成。
- 未决项：没有则写“无”；存在尚未发布的 proceedings、代码或下一轮录用结果时明确列出。

表格填写规则：
1. `Title` 保留论文的英文原题；作者以官方页面或正式论文所列顺序填写。
2. “论文链接 / arXiv 链接”优先填写官方论文页；存在 arXiv 时在同一单元格补充，两者之间使用 ` · ` 分隔。官方暂未提供独立论文页时，可暂时只填写 arXiv，但必须已经通过官方录用列表核实中稿状态。
3. “代码链接”统一写作 `[Code](URL)`；只有项目页时写 `[Project](URL)`；没有找到公开代码时填写“暂未公开”。
4. “关键词”严格遵循 `STYLE_GUIDE.md`：填写 3 至 4 个英文关键词，第一个表示研究角色，其余描述具体安全对象、核心机制和影响或评测维度；关键词不需要匹配 `domains/`。
5. “一句话总结”必须同时交代问题出发点、所做工作、主要结论及其与 AI Safety 的直接关系；不把摘要结论外推为更宽泛的安全声明。
6. 表格单元格中的 `|` 必须转义或改写；同一论文在一个会议文件中只出现一次。
```
