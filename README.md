# 规则与记录模板库

> 面向新项目 / 空白项目的开箱即用开发规则基座。
> 模板已做去业务化 + 变量化处理，复制后填变量即可使用。
> 维护约定：模板只放通用规则；项目特有约束在新项目里按需追加，不回写本库。

**两个入口，按读者区分**：

- `AI_README.md` —— **给 AI 读**。AI 进入采用本规则库的项目时，先读它建立对整套规则的心智模型（是什么、怎么生效、遵守什么纪律）。
- `README.md`（本文件）—— **给人读**。讲目录结构、模板清单、怎么复制与初始化。

> 命名说明：总领文件用 `AI_README.md` 而非 `AGENTS.md`，是为了避开 Windows 大小写不敏感下与项目模板 `agents.md` 的文件名冲突。

---

## 一、三层结构

| 层 | 目录 | 作用 | 落地位置 |
|---|---|---|---|
| **全局层** | `01-global/` | 跨项目恒定规则：语言、委派、真实性、变更分级 | `~/.claude/`（用户级，一次安装处处生效） |
| **项目层** | `02-project/` | 单项目约束：定位、技术边界、开发流程门禁 | `<项目根>/CLAUDE.md`、`agents.md`、`docs/active/development.md` |
| **记录层** | `03-records/` | 进度 / 日志 / 变更 / 风险 / 防复发 / 上下文声明 | `<项目根>/docs/` 与 `tasks/` |
| **引导层** | `04-bootstrap/` | 新项目初始化 SOP + 变量清单 | 人工执行，不落盘到项目 |

> **继承关系**：全局层定义"必须怎么做事" → 项目层定义"这个项目做什么、边界在哪" → 记录层定义"怎么留痕、怎么续接"。项目层不得与全局层冲突，只做补充。

---

## 二、模板清单

### 全局层（`01-global/`）
| 模板 | 落地为 | 核心内容 |
|---|---|---|
| `CLAUDE.md.template` | `~/.claude/CLAUDE.md` | 语言统一、子 agent 委派、Skill 调用、输出真实性 6 条、上下文压缩处理 |
| `agents.md.template` | `~/.claude/rules/common/agents.md` | 通用行为准则：写入前确认、命令中断恢复、变更 rigor 判断、时间预估 |

### 项目层（`02-project/`）
| 模板 | 落地为 | 核心内容 |
|---|---|---|
| `CLAUDE.md.template` | `<项目根>/CLAUDE.md` | 项目定位、技术边界、权威文档入口、开发与审阅规则、流程选择、新会话引导、变更门禁 |
| `agents.md.template` | `<项目根>/agents.md` | 项目硬约束、4 问变更分级、过程合规必填字段、时间预估表 |
| `development.md.template` | `<项目根>/docs/active/development.md` | 启动顺序、R0-R3 分层读取、Context Declaration、Semantic Diff Review、命令中断恢复 |
| `项目概览.template.md` | `<项目根>/docs/00-项目概览.md` | 项目定位、技术底座、架构不变量、阶段划分、文档索引 |
| `任务池.template.md` | `<项目根>/docs/09-任务池.md` | 任务卡格式、变更级别必填字段、状态转换、任务清单 |

### 产品文档（`02-project/docs/`）
| 模板 | 落地为 | 核心内容 |
|---|---|---|
| `01-需求分析.template.md` | `<项目根>/docs/01-需求分析.md` | 角色场景、FR / NFR / UC 编号、明确不做、待确认问题 |
| `02-范围与边界.template.md` | `<项目根>/docs/02-范围与边界.md` | MVP 范围、不做清单、MoSCoW、裁剪顺序、变更控制 |
| `03-业务规则与状态机.template.md` | `<项目根>/docs/03-业务规则与状态机.md` | `BR-NN` 规则、状态迁移表、非法迁移、不变量、测试要求 |
| `04-工程结构与规范.template.md` | `<项目根>/docs/04-工程结构与规范.md` | 目录、分层职责、编码、测试、Git 与命令约定 |
| `05-技术验证清单.template.md` | `<项目根>/docs/05-技术验证清单.md` | `TV-NN` 待验证点、验证方式、结论汇总 |
| `06-阶段评审记录.template.md` | `<项目根>/docs/06-阶段评审记录.md` | `REV-NNN` 评审项、结论口径（放行 / 有条件放行 / 不放行） |

### 记录层（`03-records/`）
| 模板 | 落地为 | 核心内容 |
|---|---|---|
| `00-编号规范.md` | `<项目根>/docs/编号规范.md` | 文档 / 任务 / 变更 / 风险 / 需求编号规则，状态集，完成度口径 |
| `01-进度追踪.template.md` | `docs/90-进度追踪.md` 或 `docs/progress/progress-NNN.md` | 总看板、里程碑、任务明细、完成度、滞后预警、本周快照、周节拍 |
| `02-开发日志.template.md` | `docs/93-开发日志.md` 或 `docs/dev-log/YYYY-MM-DD-*.md` | 按日倒序条目、状态变更、证据、遗留、关联变更 |
| `03-变更记录.template.md` | `docs/92-变更记录.md` 或 `CHANGELOG.md` | CHG-NNN 变更流水 |
| `04-风险登记册.template.md` | `docs/91-风险登记册.md` | RISK-NN 风险、状态、缓解、关联任务 |
| `05-防复发规则.template.md` | `tasks/lessons.md` | 用户纠正 → 根因 → 触发条件 → 修复模板 → Why |
| `06-上下文声明.template.md` | `docs/active/context-declarations.md` | Context Declaration + Semantic Diff Review 归档 |

### 引导层（`04-bootstrap/`）
| 文件 | 作用 |
|---|---|
| `init_project.py` | 一键初始化：复制模板、去后缀、替换 A 类变量、校验残留 |
| `NEW-PROJECT.md` | 新项目初始化 SOP：复制映射、变量填充、启动顺序、验收清单 |
| `VARIABLES.md` | 全部 `{{变量}}` 的定义与示例值 |

---

## 三、怎么用

### 方式一：脚本一键初始化（推荐）

```bash
python 04-bootstrap/init_project.py --target D:/my-project --yes
```

交互式逐项填写（不给 `--yes` 即逐项提问）：

```bash
python 04-bootstrap/init_project.py --target D:/my-project
```

脚本会完成：复制 18 个模板 + `AI_README.md` 到目标目录 → 去掉 `.template` → 替换 15 个 A 类项目配置变量 → 保留 B/C 类占位作为填写提示 → 输出清单并校验 A 类无残留。

> 全局层不自动安装，脚本不触碰用户主目录，需手工并入 `~/.claude`。

### 方式二：手工复制

1. 按 `04-bootstrap/NEW-PROJECT.md` 的映射表复制模板到目标路径
2. 去掉文件名中的 `.template`
3. 按 `VARIABLES.md` 替换 A 类变量（B/C 类保留）
4. 按 `00-编号规范.md` 建立文档编号骨架
5. 写第一条进度、第一条日志、第一条防复发规则

全局层只需安装一次：把 `01-global/` 两个模板的内容并入 `~/.claude/CLAUDE.md` 与 `~/.claude/rules/common/agents.md`。

---

## 四、命名与变量约定

### 为什么模板文件带 `.template` 后缀

这是刻意设计，三个理由：

1. **防止被误加载**：Claude Code 会自动读取项目根目录的 `CLAUDE.md`。若模板直接叫 `CLAUDE.md`，在本库目录里工作时会被当成真实规则加载，造成混淆。加后缀后不会被自动识别。
2. **强制显式复制动作**：使用者必须手动去掉后缀才能启用，这个动作本身就是一次"我要启用这套规则"的确认，避免误用。
3. **区分源文件与生效文件**：库里是 `CLAUDE.md.template`，项目里是 `CLAUDE.md`，一眼可辨。

### 其余约定

- 模板文件名统一带 `.template` 标记，按文件类型分两种写法，复制时去掉 `.template` 即得目标文件名：
  - 规则类（需保持原名）：`CLAUDE.md.template` → `CLAUDE.md`
  - 记录类（按编号命名）：`01-进度追踪.template.md` → `01-进度追踪.md`
- 变量用双花括号：`{{PROJECT_NAME}}`、`{{TECH_STACK}}`
- 可选章节用 `<!-- OPTIONAL:START/END -->` 包裹，不需要时整段删除
- 所有模板正文使用**简体中文**；代码标识符、命令、路径保持原文

---

## 五、维护约定

1. **只抽象，不搬运**：模板里不出现任何具体业务名词
2. **变更走模板自身的 rigor**：改模板属于"公开契约变更"，需记录到本库 `CHANGELOG`（若建立）
3. **冲突处理**：项目层与全局层冲突时，以全局层为准；确有例外须在项目 `CLAUDE.md` 显式声明理由
