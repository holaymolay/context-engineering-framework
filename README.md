# Context-Engineering Framework for Coding Agents
A governance and context-engineering framework that turns human requests into
repeatable, auditable agent execution.
It replaces ad-hoc prompting with explicit specs, Skills, and enforcement.
It captures context, decisions, and validation artifacts for reliable reuse.
It is designed for CLI- or IDE-driven coding agents.

## Who this is for
This framework is for engineers operating coding agents in production work.
It is for teams that need predictable outcomes and traceable decisions.

- Teams running agentic workflows in CLI or IDE environments.
- Engineers who require audit trails and deterministic behavior.
- Not for casual prompt experimentation or one-off scripting.

## Core problem
Agentic coding workflows fail when intent is ambiguous and outcomes drift.
They create clarification loops, non-deterministic edits, and no audit trail.
The result is fragile delivery that cannot be reliably reviewed or resumed.

## Solution (high level)
Context engineering turns intent into enforceable structure.
Specs define work, Skills constrain behavior, and governance records results.
The framework combines clarification gates, validation, and logged artifacts.

## What you get
- Deterministic execution boundaries for agent work.
- Auditable records of intent, decisions, and outcomes.
- Reduced human interruption through structured clarification.
- Portability across models and frontends via explicit contracts.

## How it works
Human intent flows through clarification, governed execution, and logging.
The framework records specs, plans, validations, and handover artifacts.

## Quick start
- Read `HUMAN_START_HERE.md` for the human entrypoint.
- Read `AGENTS.md` for the authoritative execution contract.
- Select a stack profile in `docs/stacks/`.
- Add tasks in chat or `todo-inbox.md`.
- Use `docs/humans/workflow-adoption.md` for new repositories.

## Repository map
- `AGENTS.md`: core governance rules and operating constraints.
- `docs/agents.md`: operational framework and execution flow.
- `docs/humans/`: human-facing guides and onboarding context.
- `docs/context/`: agent ledgers and context management protocol.
- `specs/`: spec contracts that govern changes.
- `skills/`: deterministic Skill packages and schemas.
- `docs/wiki/`: navigation layer for concepts and playbooks.
- `README_GOVERNANCE.md`: governs spec-driven README generation and enforcement boundaries.

## Design philosophy and non-goals
The framework optimizes for governance, determinism, and auditability.
It does not try to design UI, replace human judgment, or remove review.
It is not a prompt library or a set of agent heuristics.

## README Generation and Governance
README.md is produced from an explicit spec (`README_SPEC.yaml`) using the external `readme-spec-engine`.
This framework enforces README quality and structure but does not generate the README itself.
Generation happens outside this repo; enforcement here ensures the authored README stays aligned with its spec.
