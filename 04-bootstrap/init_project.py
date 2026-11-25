#!/usr/bin/env python3
"""规则库初始化脚本

把本库的项目层与记录层模板复制到目标项目，并按 A 类变量完成替换。
B 类（记录字段）与 C 类（语义占位）保留为填写提示。

用法:
    # 交互式逐项填写
    python init_project.py --target D:/my-project

    # 非交互，缺失项用示例默认值
    python init_project.py --target D:/my-project --yes

    # 全参数指定
    python init_project.py --target D:/my-project \
        --name "My Project" --stack "Python >=3.10" --build uv --yes

全局层（01-global）需手工安装到 ~/.claude，本脚本不触碰用户主目录。
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

RULES_ROOT = Path(__file__).resolve().parent.parent

MAPPING = [
    ("AI_README.md", "AI_README.md"),
    ("02-project/CLAUDE.md.template", "CLAUDE.md"),
    ("02-project/agents.md.template", "agents.md"),
    ("02-project/development.md.template", "docs/active/development.md"),
    ("02-project/项目概览.template.md", "docs/00-项目概览.md"),
    ("02-project/docs/01-需求分析.template.md", "docs/01-需求分析.md"),
    ("02-project/docs/02-范围与边界.template.md", "docs/02-范围与边界.md"),
    ("02-project/docs/03-业务规则与状态机.template.md", "docs/03-业务规则与状态机.md"),
    ("02-project/docs/04-工程结构与规范.template.md", "docs/04-工程结构与规范.md"),
    ("02-project/docs/05-技术验证清单.template.md", "docs/05-技术验证清单.md"),
    ("02-project/docs/06-阶段评审记录.template.md", "docs/06-阶段评审记录.md"),
    ("02-project/任务池.template.md", "docs/09-任务池.md"),
    ("03-records/00-编号规范.md", "docs/编号规范.md"),
    ("03-records/01-进度追踪.template.md", "docs/90-进度追踪.md"),
    ("03-records/02-开发日志.template.md", "docs/93-开发日志.md"),
    ("03-records/03-变更记录.template.md", "docs/92-变更记录.md"),
    ("03-records/04-风险登记册.template.md", "docs/91-风险登记册.md"),
    ("03-records/05-防复发规则.template.md", "tasks/lessons.md"),
    ("03-records/06-上下文声明.template.md", "docs/active/context-declarations.md"),
]

A_VARS = [
    ("PROJECT_NAME", "name", "项目名", "My Project"),
    ("PROJECT_POSITIONING", "positioning", "一句话定位", "面向团队内部的工具"),
    ("PROJECT_GOAL", "goal", "主线目标（要做什么）", "把重复流程自动化，降低出错率"),
    ("MAIN_LINE_TYPE", "main_line_type", "主线类型（从零新建 / 优化改造）", "优化/改造"),
    ("PROJECT_BOUNDARY", "boundary", "项目边界 / 不做的事", "只支持本地运行；不处理敏感数据"),
    ("TECH_STACK", "stack", "技术栈", "Python >=3.10 + pytest"),
    ("BUILD_TOOL", "build", "包管理 / 构建工具", "uv"),
    ("STORAGE", "storage", "存储方案", "SQLite + JSON"),
    ("DEPENDENCY_POLICY", "dependency", "依赖策略", "零运行时依赖"),
    ("INVARIANTS", "invariants", "架构不变量", "所有请求经统一入口；不自动重放外部副作用"),
    ("CURRENT_PHASE", "phase", "当前阶段", "P0 初始化"),
    ("PRD_FILE", "prd", "产品文档文件名", "product-requirements.md"),
    ("MODULE_RULE", "module_rule", "模块推进规则", "每次只推进 1 个主模块"),
    ("PHASE_MODEL", "phase_model", "推进模型", "P0 -> P1 -> P2 优先级队列"),
    ("ARCHIVE_DIR", "archive_dir", "封存内容归档目录名", "legacy-feature-YYYY-MM-DD"),
    ("COMPACT_CRON_ID", "cron_id", "压缩提醒定时任务 ID（无则填 none）", "none"),
]


def collect_values(args: argparse.Namespace) -> dict[str, str]:
    values: dict[str, str] = {}
    for var, arg_name, prompt, default in A_VARS:
        cli_val = getattr(args, arg_name, None)
        if cli_val is not None:
            values[var] = cli_val
            continue
        if args.yes:
            values[var] = default
            continue
        try:
            ans = input(f"{prompt}（{var}，回车用示例「{default}」）: ").strip()
        except EOFError:
            ans = ""
        values[var] = ans or default
    return values


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description="规则库初始化：复制模板并替换 A 类变量")
    ap.add_argument("--target", required=True, help="目标项目目录")
    ap.add_argument("--yes", action="store_true", help="不交互，缺失项用示例默认值")
    ap.add_argument("--force", action="store_true", help="覆盖已存在的文件")
    for _, arg_name, _, _ in A_VARS:
        ap.add_argument("--" + arg_name.replace("_", "-"), dest=arg_name, default=None)
    return ap


def main() -> int:
    args = build_parser().parse_args()
    target = Path(args.target).expanduser().resolve()

    if RULES_ROOT.name != "rules" and not (RULES_ROOT / "02-project").is_dir():
        print(f"✗ 未找到模板目录，请在 rules 库内运行本脚本（当前推断根：{RULES_ROOT}）")
        return 2

    values = collect_values(args)
    target.mkdir(parents=True, exist_ok=True)

    created: list[str] = []
    skipped: list[str] = []
    missing: list[str] = []

    for src_rel, dst_rel in MAPPING:
        src = RULES_ROOT / src_rel
        if not src.is_file():
            missing.append(src_rel)
            continue
        dst = target / dst_rel
        if dst.exists() and not args.force:
            skipped.append(dst_rel)
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        text = src.read_text(encoding="utf-8")
        for var, val in values.items():
            text = text.replace("{{" + var + "}}", val)
        dst.write_text(text, encoding="utf-8", newline="\n")
        created.append(dst_rel)

    leftover: list[tuple[str, str]] = []
    for md in target.rglob("*.md"):
        try:
            content = md.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for var in values:
            if "{{" + var + "}}" in content:
                leftover.append((str(md.relative_to(target)), var))

    print("\n=== 初始化结果 ===")
    print(f"目标目录: {target}")
    print(f"已创建: {len(created)} 个文件")
    for item in created:
        print(f"  + {item}")
    if skipped:
        print(f"已跳过（已存在，用 --force 覆盖）: {len(skipped)} 个")
        for item in skipped:
            print(f"  = {item}")
    if missing:
        print(f"⚠️ 模板缺失: {len(missing)} 个")
        for item in missing:
            print(f"  ! {item}")

    print(f"\nA 类变量已替换: {len(values)} 个")
    if leftover:
        print("⚠️ 仍有 A 类变量残留:")
        for path, var in leftover:
            print(f"  {path}: {{{{{var}}}}}")
        return 1

    print("✅ A 类变量已全部替换")
    print("\n下一步:")
    print("  1. B/C 类占位符保留作为填写提示，写到哪清到哪")
    print("  2. 手工把 01-global 模板并入 ~/.claude（全局层不自动安装）")
    print("  3. 打开 docs/00-项目概览.md 与 docs/09-任务池.md，补齐项目定义与首批任务")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
