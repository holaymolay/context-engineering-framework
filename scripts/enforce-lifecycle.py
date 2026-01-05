#!/usr/bin/env python3
"""Lifecycle gate checks for CERES governance orchestrator.

This is a lightweight guardrail to enforce:
- no execution before a visible Task Plan exists (`todo.md` with unchecked tasks)
- optional Gap Ledger presence
- optional Prompt Debug Report presence

Use this as a pre-execution gate; fail fast if prerequisites are missing.
"""
import argparse
import sys
from pathlib import Path


def has_unchecked_tasks(todo_path: Path) -> bool:
    if not todo_path.exists():
        return False
    for line in todo_path.read_text().splitlines():
        if line.strip().startswith("- [ ]"):
            return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser(description="CERES lifecycle gate")
    parser.add_argument("--todo", type=Path, default=Path("todo.md"), help="Path to todo.md")
    parser.add_argument("--gap-ledger", type=Path, help="Optional path to gap ledger file")
    parser.add_argument("--prompt-report", type=Path, help="Optional path to prompt debug report")
    args = parser.parse_args()

    failures = []

    if not has_unchecked_tasks(args.todo):
        failures.append(f"Missing or empty task plan: {args.todo}")

    if args.gap_ledger and not args.gap_ledger.exists():
        failures.append(f"Gap ledger missing: {args.gap_ledger}")

    if args.prompt_report and not args.prompt_report.exists():
        failures.append(f"Prompt debug report missing: {args.prompt_report}")

    if failures:
        sys.stderr.write("Lifecycle gate failed:\n" + "\n".join(f"- {f}" for f in failures) + "\n")
        sys.exit(1)

    sys.stdout.write("Lifecycle gate passed\n")


if __name__ == "__main__":
    main()
