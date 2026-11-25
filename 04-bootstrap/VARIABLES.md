# 变量清单

> 复制模板后，把 `{{VAR}}` 替换为实际值。所有模板只使用本表列出的变量。

---

## 全局层

| 变量 | 含义 | 示例 |
|---|---|---|
| `{{COMPACT_CRON_ID}}` | 上下文压缩提醒的定时任务 ID；无则不启用 | `<your-cron-id>` |

## 项目层

| 变量 | 含义 | 示例 |
|---|---|---|
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

## 可选章节

| 变量 | 含义 | 示例 |
|---|---|---|
| `{{ARCHIVE_DIR}}` | 封存内容归档目录名 | `legacy-feature-YYYY-MM-DD` |

## 记录层通用

| 变量 | 含义 | 示例 |
|---|---|---|
| `{{DATE}}` | 日期，`YYYY-MM-DD` | `2026-11-25` |
| `{{ONE_LINE_SUMMARY}}` | 一行摘要 | `T-023 状态机重构完成` |
| `{{N}}` | 数字占位 | `8` |
| `{{PCT}}` | 百分比 | `100%` |
| `{{PHASE_NAME}}` | 阶段名 | `P0 基建` |
| `{{TASK_TITLE}}` | 任务标题 | `订单状态机补齐` |
| `{{WEEKDAY}}` | 星期 | `周三` |
| `{{WEEK_RANGE}}` | 周区间 | `W8 · 11-17 ~ 11-23` |
| `{{SLICE_NAME}}` | 切片名 | `缓存层重构` |
| `{{MODULE_AND_SLICE}}` | 模块 / 切片 | `M01 / 工具审批` |
| `{{DESIGN_DOC_PATH}}` | 设计文档路径 | `docs/design/tool-approval.md` |

> 其余形如 `{{WHAT_WAS_DONE}}`、`{{ROOT_CAUSE}}` 的占位为**段落语义提示**，按字面含义填写或删除该段即可，无需严格一一对应。
