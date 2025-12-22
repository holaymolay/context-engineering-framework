# Context-Engineering Framework for Coding Agents

A reusable, LLM-agnostic context-engineering framework that turns human requests into auditable, high-quality agent execution through specs, Skills, context ledgers, and continuous improvement.

**AI-operated only:** Use the chat window (or `todo-inbox.md`) to provide tasks and decisions. The agent runs scripts and updates AI-managed files.

## What this is
This project is a governance framework for working with CLI-based coding agents, whether you run them from a terminal or an IDE extension. It gives a solo developer a disciplined way to plan, execute, validate, and document agent work without losing speed.

If you are a human reader, start with `HUMAN_START_HERE.md`.

## AI-operated by default
- You interact through the chat window (or by adding items to `todo-inbox.md`).
- The agent runs framework scripts and updates AI-managed files (`todo.md`, `backlog.md`, `completed.md`, `handover.md`, `CHANGELOG.md`).
- Humans should not manually edit AI-managed files or run framework scripts.

## Quick start prompt
Copy/paste this into any agentic frontend (Codex, Gemini, Claude/Anthropic, Grok, etc.):

```text
You are to incorporate this Context-Engineering Framework for Coding Agents, located at https://github.com/holaymolay/context-engineering-framework, as the governance framework for this project.

For new projects, implement this framework from the start. Once the framework is in place I will describe the project and its requirements.
For existing projects, implement this framework and bring the existing codebase into compliance with the framework.

Read `AGENTS.md` and treat it as the authoritative contract.
Operate in AI-only mode: run scripts yourself and update AI-managed files; humans only add tasks via chat or `todo-inbox.md`.

If your provider has built-in governance features, use this framework as the source of truth and integrate with those features as needed.
```

## Why it helps
- Faster delivery with fewer clarification loops.
- Clear audit trails for every change (specs, ledgers, changelog).
- Deterministic guardrails (Clarification Gate, Reasoning Skills, one-Concept focus).
- Portable across LLMs and toolchains.

## How it works (decision tree)
When you have a task:
1) State it in chat or add it to `todo-inbox.md` (this is the only file humans should edit).
2) The agent sweeps the inbox into `todo.md` and routes it.
3) If it changes the framework itself, it goes to `## Workflow Governance` in `todo.md` and is handled first.
4) If inputs are unclear, Clarification Gate asks questions before planning.
5) If inputs are clear, Reasoning Skills enforce constraints before the plan.
6) The agent plans, executes, validates, and logs outcomes.

## Getting started
1) Tell the agent which stack profile applies in `docs/stacks/`.
2) If you are adopting into another repo, ask the agent to run `scripts/bootstrap-workflow.sh`.
3) Add your first task in chat or to `todo-inbox.md`.
4) For larger work items, ask the agent to create or use a spec under `specs/`.
5) Run your coding agent from the CLI or an IDE extension.

## Model requirements
- Works with a local clone and no web access; network is only needed when a task requires it (package installs, external APIs).
- Must be able to read/write local files and run shell commands via a CLI or IDE-based agent.
- Must reliably follow repo instructions, ask clarifying questions, and execute multi-step tasks.
- Built and tested with OpenAI Codex; intended to work with any frontier-quality LLM, but broader validation is still needed.

## Terminology
- Framework: the overall governance system (files, rules, tooling, and guardrails).
- Workflow: the execution sequence inside the framework (Clarification Gate -> Reasoning Skills -> Plan -> Execute -> Validate -> Log).

## Can this be used for non-coding work?
Yes. The framework can be adapted to any structured project work that needs clarity, accountability, and repeatable decision gates. You would swap stack-specific guidance for domain-specific playbooks and adjust Skills/specs accordingly.

## Key docs (start here)
- `HUMAN_START_HERE.md` (human entrypoint)
- `docs/humans/workflow-guide.md` (framework overview)
- `docs/humans/workflow-adoption.md` (apply the framework to a new project)
- `docs/humans/user-guide.md` (how to structure requests for best results)
- `docs/humans/user-guide-cheat-sheet.md` (one-page quickstart)
- `docs/humans/about.md` (why this framework exists and how it evolved)

## Framework revision snapshots (local)
Framework snapshots are stored locally under `ai_workflow_revisions/` and are gitignored by default. Ask the agent to run `scripts/create-workflow-revision.sh` after governance changes. See `docs/workflow-revisions.md` for the required contents and numbering rules.
