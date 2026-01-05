#!/usr/bin/env python3
"""Lifecycle gate checks for CERES governance orchestrator.

Enforces:
- todo.md has unchecked tasks
- optional Gap Ledger presence and validation
- optional Prompt Debug Report presence
- optional CERES todo template check
- optional logging via hub scripts/log_event.py
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Dict


def has_unchecked_tasks(todo_path: Path) -> bool:
    if not todo_path.exists():
        return False
    return any(line.strip().startswith("- [ ]") for line in todo_path.read_text().splitlines())


def check_ceres_todo(todo_path: Path) -> bool:
    lines = todo_path.read_text().splitlines() if todo_path.exists() else []
    return bool(lines and "CERES" in lines[0])


def log_event(log_helper: Path, status: str, message: str, context: Dict) -> None:
    if not log_helper:
        return
    if not log_helper.exists():
        sys.stderr.write(f"Log helper not found at {log_helper}\n")
        return
    cmd = [
        sys.executable,
        str(log_helper),
        "--type",
        "gate",
        "--status",
        status,
        "--message",
        message,
        "--context",
        json.dumps(context),
    ]
    subprocess.run(cmd, check=False)


def validate_gap_ledger(path: Path) -> str:
    """Call local validate-gap-ledger.py if present; return warning text or ''."""
    validator = path.parent / "validate-gap-ledger.py"
    if not validator.exists():
        return ""
    result = subprocess.run([sys.executable, str(validator), str(path)], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "Gap ledger validation failed")
    return result.stderr.strip()  # warnings, if any


def main() -> None:
    parser = argparse.ArgumentParser(description="CERES lifecycle gate")
    parser.add_argument("--todo", type=Path, default=Path("todo.md"), help="Path to todo.md")
    parser.add_argument("--gap-ledger", type=Path, help="Optional path to gap ledger file")
    parser.add_argument("--prompt-report", type=Path, help="Optional path to prompt debug report")
    parser.add_argument("--require-ceres-todo", action="store_true", help="Fail if todo.md does not look like CERES template")
    parser.add_argument("--require-gap-ledger", action="store_true", help="Fail if gap ledger is missing or empty")
    parser.add_argument("--validate-gap-ledger", action="store_true", help="Validate gap ledger content (evidence for resolved gaps)")
    parser.add_argument("--task-id", help="Optional task identifier for logging context")
    parser.add_argument("--log-helper", type=Path, help="Optional path to umbrella scripts/log_event.py to log gate outcome")
    args = parser.parse_args()

    failures = []
    warnings = []
    context = {
        "todo": str(args.todo),
        "gap_ledger": str(args.gap_ledger) if args.gap_ledger else None,
        "prompt_report": str(args.prompt_report) if args.prompt_report else None,
        "task_id": args.task_id,
    }

    if not has_unchecked_tasks(args.todo):
        failures.append(f"Missing or empty task plan: {args.todo}")

    if args.gap_ledger and not args.gap_ledger.exists():
        failures.append(f"Gap ledger missing: {args.gap_ledger}")

    if args.require_gap_ledger:
        if not args.gap_ledger:
            failures.append("Gap ledger path not provided while --require-gap-ledger is set")
        else:
            if not args.gap_ledger.exists():
                failures.append(f"Gap ledger missing: {args.gap_ledger}")
            elif not args.gap_ledger.read_text().strip():
                failures.append(f"Gap ledger is empty: {args.gap_ledger}")

    if args.validate_gap_ledger and args.gap_ledger and args.gap_ledger.exists():
        try:
            warning_text = validate_gap_ledger(args.gap_ledger)
            if warning_text:
                warnings.append(warning_text)
        except RuntimeError as exc:
            failures.append(str(exc))

    if args.prompt_report and not args.prompt_report.exists():
        failures.append(f"Prompt debug report missing: {args.prompt_report}")

    if args.require_ceres_todo and not check_ceres_todo(args.todo):
        failures.append(f"todo.md does not appear to be the CERES template: {args.todo}")

    if failures:
        sys.stderr.write("Lifecycle gate failed:\n" + "\n".join(f"- {f}" for f in failures) + "\n")
        log_event(args.log_helper, "fail", "lifecycle gate failed", {**context, "failures": failures})
        sys.exit(1)

    if warnings:
        sys.stderr.write("Lifecycle gate warnings:\n" + "\n".join(warnings) + "\n")

    sys.stdout.write("Lifecycle gate passed\n")
    log_event(args.log_helper, "pass", "lifecycle gate passed", context)


if __name__ == "__main__":
    main()
