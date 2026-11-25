# 规则来源溯源

> 本库的每条非显然规则都能追溯到工作区既有项目的实践。此表记录"从哪来"，便于后续判断是否仍然适用。

---

## 全局层来源

| 规则 | 来源文件 | 说明 |
|---|---|---|
| 语言统一、子 agent 委派、Skill 调用、输出真实性 6 条 | `~/.claude/CLAUDE.md` | 直接继承，去除了实例特定的 cron 细节（改为变量） |
| 通用行为准则（写入确认 / 中断恢复 / rigor / 时间预估） | `MlifeAgent/agents.md`、`Mlife/agents.md` | 抽取跨项目通用部分 |

## 项目层来源

| 规则 | 来源文件 | 说明 |
|---|---|---|
| 项目约束骨架、流程三级选择、45 分钟阈值、新会话引导、压缩恢复门禁、变更门禁 | `Mlife/CLAUDE.md`、`MlifeAgent/CLAUDE.md` | 去除项目特有名词（生活参谋 / 镜我 / ADR 具体编号）后抽象 |
| 项目硬约束表、4 问 rigor、过程合规必填字段 | `MlifeAgent/agents.md` | 抽象为变量 |
| R0-R3 分层读取、Context Declaration、Semantic Diff Review、命令中断恢复 | `MlifeAgent/docs/active/development.md` | 保留门禁机制，阶段细节改为变量 |
| 权威文档单一事实源、路由层思想 | `Review/CLAUDE.md` | "规则只登记路径、不复制正文"来自此处 |

## 记录层来源

| 规则 | 来源文件 | 说明 |
|---|---|---|
| docs 固定编号（00-06 / 90-93 / 99+）、滞后预警、周节拍、双口径完成度 | `cangjie/docs/90-进度追踪.md`、`cangjie/CLAUDE.md` | 完整抽取，作为统一编号规范基线 |
| 进度分页倒序、状态变化不改历史行、单页 300 行阈值 | `xmes-DEV/docs-1/dev-log/2026-09-24-搭建本地开发记录体系.md` | 抽象为通用分页规则 |
| 本地记录隔离三层防护（exclude / pre-commit hook / 文首红线） | 同上 | 未纳入模板正文（属运维细节），如需可在此查阅 |
| 防复发规则结构（纠正 → 根因 → 触发 → 修复模板 → Why） | `MlifeAgent/tasks/lessons.md` | 保留结构，去除具体技术债条目 |
| 防幻觉约束（数字验证 / 源码佐证 / 推断标注） | `Ai/pico/CLAUDE.md` | 已并入全局层"输出真实性规则" |
| 上下文声明 + 语义 diff 归档格式 | `MlifeAgent/docs/active/context-declarations.md` | 抽象为模板 |

---

## 未纳入（按需再取）

- **pico 的 STAR 讲解规范 / Skill 强制调用**：属"学习 / 讲解"场景，非通用开发，未纳入本次模板库。若新项目是学习研究型，可从 `Ai/pico/CLAUDE.md` 单独取用。
- **cangjie 冲刺期 / 自主迭代协议**：属特定阶段战术，未纳入通用模板。
- **xmes 的本地不上传隔离机制**：属特定仓库运维要求，未纳入。
