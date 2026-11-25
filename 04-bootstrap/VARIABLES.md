# 变量清单

> 复制模板后，把 `{{VAR}}` 替换为实际值。所有模板只使用本表列出的变量。

---

## 全局层

| 变量 | 含义 | 示例 |
|---|---|---|
| `{{COMPACT_CRON_ID}}` | 上下文压缩提醒的定时任务 ID；无则不启用 | `b292c33c` |

## 项目层

| 变量 | 含义 | 示例 |
|---|---|---|
| `{{PROJECT_NAME}}` | 项目名，用于文档标题 | `Mlife Agent` |
| `{{PROJECT_POSITIONING}}` | 一句话定位 | `单用户本地 Agent Harness` |
| `{{PROJECT_GOAL}}` | 项目目标 | `通用 Agent Harness；围绕四步循环做上下文治理与工具安全` |
| `{{PROJECT_BOUNDARY}}` | 明确边界 / 不做的事 | `本地存储、隐私优先；不作医疗诊断` |
| `{{TECH_STACK}}` | 技术栈 | `Python ≥3.10 + pytest + ruff` |
| `{{BUILD_TOOL}}` | 包管理 / 构建工具 | `uv` / `cjpm` / `npm` |
| `{{STORAGE}}` | 存储方案 | `SQLite + JSON + JSONL` |
| `{{DEPENDENCY_POLICY}}` | 依赖策略 | `P0-P2 零运行时依赖` |
| `{{INVARIANTS}}` | 架构不变量 | `所有请求经 M04；不自动重放外部副作用` |
| `{{CURRENT_PHASE}}` | 当前阶段 | `P5 ⏳ 当前` |
| `{{PRD_FILE}}` | 优先级队列 / 产品文档文件名 | `lifestyle-agent-prd.md` |
| `{{MODULE_RULE}}` | 模块推进规则 | `每次只推进 1 个主模块` |
| `{{PHASE_MODEL}}` | 推进模型描述 | `P0 → P1a → P1b → P2 优先级队列` |

## 可选章节

| 变量 | 含义 | 示例 |
|---|---|---|
| `{{ARCHIVE_DIR}}` | 封存内容归档目录名 | `mirror-persona-2026-10-31` |

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
| `{{SLICE_NAME}}` | 切片名 | `context_manager 缓存层` |
| `{{MODULE_AND_SLICE}}` | 模块 / 切片 | `M03 / 工具审批` |
| `{{DESIGN_DOC_PATH}}` | 设计文档路径 | `docs/design/tool-approval.md` |

> 其余形如 `{{WHAT_WAS_DONE}}`、`{{ROOT_CAUSE}}` 的占位为**段落语义提示**，按字面含义填写或删除该段即可，无需严格一一对应。
