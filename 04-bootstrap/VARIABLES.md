# 变量清单

> 复制模板后，把 `{{VAR}}` 替换为实际值。
> 本章把变量分为三类，替换策略不同：
>
> | 类别 | 何时替换 | 处理方式 |
> |---|---|---|
> | **A · 项目配置** | 初始化时一次填完 | 按项目实际情况替换，项目内恒定 |
> | **B · 记录字段** | 每次写记录时 | 按当天/当次事实替换 |
> | **C · 语义占位** | 写到哪里填到哪里 | 按段落含义填写后**删除占位符本身** |
>
> **验收标准**：项目内执行 `grep -R "{{" .` 应无输出——包括 C 类占位符也必须清空。

---

## A · 项目配置（15 个）

| 变量 | 含义 | 示例 |
|---|---|---|
| `{{COMPACT_CRON_ID}}` | 上下文压缩提醒的定时任务 ID；无则不启用 | `<your-cron-id>` |
| `{{PROJECT_NAME}}` | 项目名，用于文档标题 | `My Project` |
| `{{PROJECT_POSITIONING}}` | 一句话定位 | `面向团队内部的命令行工具` |
| `{{PROJECT_GOAL}}` | 项目目标 | `把重复的手工流程自动化，降低出错率` |
| `{{PROJECT_BOUNDARY}}` | 明确边界 / 不做的事 | `只支持本地运行；不处理敏感数据` |
| `{{TECH_STACK}}` | 技术栈 | `Python ≥3.10 + pytest + ruff` |
| `{{BUILD_TOOL}}` | 包管理 / 构建工具 | `uv` / `npm` / `gradle` |
| `{{STORAGE}}` | 存储方案 | `SQLite + JSON` |
| `{{DEPENDENCY_POLICY}}` | 依赖策略 | `零运行时依赖` |
| `{{INVARIANTS}}` | 架构不变量 | `所有请求经统一入口；不自动重放外部副作用` |
| `{{CURRENT_PHASE}}` | 当前阶段 | `P2 进行中` |
| `{{PRD_FILE}}` | 优先级队列 / 产品文档文件名 | `product-requirements.md` |
| `{{MODULE_RULE}}` | 模块推进规则 | `每次只推进 1 个主模块` |
| `{{PHASE_MODEL}}` | 推进模型描述 | `P0 → P1 → P2 优先级队列` |
| `{{ARCHIVE_DIR}}` | 封存内容归档目录名 | `legacy-feature-YYYY-MM-DD` |

---

## B · 记录字段（29 个）

### 时间类

| 变量 | 含义 | 示例 |
|---|---|---|
| `{{DATE}}` | 日期，`YYYY-MM-DD` | `2026-11-25` |
| `{{ACTUAL_DATE}}` | 实际达成日期 | `2026-11-20` |
| `{{WEEKDAY}}` | 星期 | `周三` |
| `{{WEEK_RANGE}}` | 周区间 | `W8 · 11-17 ~ 11-23` |

### 数量类

| 变量 | 含义 | 示例 |
|---|---|---|
| `{{N}}` | 数字占位 | `8` |
| `{{PCT}}` | 百分比 | `100%` |

### 阶段与任务

| 变量 | 含义 | 示例 |
|---|---|---|
| `{{PHASE}}` | 阶段代码 | `P2` |
| `{{PHASE_NAME}}` | 阶段名 | `P0 基建` |
| `{{TASK_TITLE}}` | 任务标题 | `订单状态机补齐` |
| `{{ONE_LINE_SUMMARY}}` | 一行摘要 | `T-023 状态机重构完成` |
| `{{ONE_LINE_STATUS}}` | 一行状态 | `P2 进行中，3 卡在途` |
| `{{SLICE_NAME}}` | 切片名 | `缓存层重构` |
| `{{MODULE_AND_SLICE}}` | 模块 / 切片 | `M01 / 工具审批` |
| `{{DESIGN_DOC_PATH}}` | 设计文档路径 | `docs/design/tool-approval.md` |

### 状态流转

| 变量 | 含义 | 示例 |
|---|---|---|
| `{{OLD_STATE}}` | 变更前状态 | `进行中` |
| `{{NEW_STATE}}` | 变更后状态 | `已完成` |

### 通用字段

| 变量 | 含义 | 示例 |
|---|---|---|
| `{{NAME}}` | 名称占位 | `M1 初始化` |
| `{{TITLE}}` | 标题 | `订单状态机重构` |
| `{{TYPE}}` | 类型 | `契约变更` |
| `{{SCOPE}}` | 影响范围 | `订单模块 / API v2` |
| `{{DETAIL}}` | 细节说明 | `见下方变更内容` |
| `{{NOTE}}` | 备注 | `无` |
| `{{REASON}}` | 原因 | `需求调整` |
| `{{BACKGROUND}}` | 背景 / 触发 | `用户提出分页需求` |
| `{{COMMAND}}` | 执行的命令 | `pytest tests/ -q` |
| `{{RESULT}}` | 命令结果 | `45 passed` |
| `{{EVIDENCE_PATH}}` | 证据文件路径 | `reports/pytest-2026-11-25.txt` |
| `{{VERIFICATION}}` | 验证方式 | `单测 + 手工回归` |
| `{{BASIS}}` | 决策依据 | `ADR-001 / 用户确认` |

---

## C · 语义占位（39 个）

> 这些是"这里要写一段话"的提示。填写后**必须删除占位符本身**，否则 `grep "{{"` 验收无法通过。

### 进度追踪

| 变量 | 应有的内容 |
|---|---|
| `{{CAPABILITY}}` | 该里程碑能演示什么 |
| `{{CRITERION}}` | 验收标准 |
| `{{TASKS}}` | 本周完成的任务清单 |
| `{{BLOCKERS}}` | 本周阻塞项；无则写"无" |
| `{{NEXT}}` | 下周计划 |
| `{{HIGHLIGHT}}` | 本周亮点 |
| `{{BACKLOG}}` | 本周遗留 |
| `{{GIT_STATUS}}` | git 状态（是否 push / tag） |

### 开发日志

| 变量 | 应有的内容 |
|---|---|
| `{{WHAT_WAS_DONE}}` | 本次做了什么 |
| `{{KEY_DECISION}}` | 关键决策；无则写"无" |
| `{{BACKLOG_ITEM}}` | 遗留事项与下一步 |
| `{{COMPLETED}}` | 本周完成项 |
| `{{RISKS}}` | 新出现的风险 |
| `{{CHANGES}}` | 变更汇总 |

### 变更记录

| 变量 | 应有的内容 |
|---|---|
| `{{DESCRIPTION}}` | 变更内容 |
| `{{AFFECTED_FILES_OR_MODULES}}` | 影响的文件 / 模块 |
| `{{OUT_OF_SCOPE}}` | 本次不做的部分 |
| `{{CHANGE_ITEM_1}}` | 变更条目 1 |
| `{{CHANGE_ITEM_2}}` | 变更条目 2 |

### 风险登记册

| 变量 | 应有的内容 |
|---|---|
| `{{IMPACT}}` | 风险影响 |
| `{{MITIGATION}}` | 缓解措施 |
| `{{TRIGGER}}` | 触发条件 |
| `{{DEGRADATION}}` | 降级 / 接受情况 |
| `{{CLOSURE_BASIS}}` | 关闭依据 |

### 防复发规则

| 变量 | 应有的内容 |
|---|---|
| `{{RULE_TITLE}}` | 规则标题 |
| `{{WHAT_WENT_WRONG}}` | 出了什么问题 |
| `{{USER_CONFIRMATION}}` | 用户确认原话或摘要 |
| `{{ROOT_CAUSE}}` | 根因 |
| `{{TRIGGER_1}}` / `{{TRIGGER_2}}` | 触发条件 |
| `{{FIX_STEP_1}}` / `{{FIX_STEP_2}}` | 修复步骤 |
| `{{WHY_IT_WORKS}}` | 为什么这样修有效 |
| `{{COMMIT_OR_TASK}}` | 关联提交 / 任务 |

### 上下文声明

| 变量 | 应有的内容 |
|---|---|
| `{{UPSTREAM_TO_DOWNSTREAM}}` | 上游 → 下游 + 数据真相源 |
| `{{ERROR_APPROVAL_RECOVERY_BOUNDARY}}` | 错误 / 审批 / 恢复边界 |
| `{{OUT_OF_SCOPE_AND_VERIFICATION}}` | 本次不做 + 验证方式 |
| `{{HAPPY_PATH}}` | 核心成功路径 |
| `{{FAILURE_PATH}}` | 关键失败路径 |
