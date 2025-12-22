# Patterns

This page summarizes reusable patterns discovered during delivery. It is a navigation layer and does not override authoritative specs/manifests/Skills.

## Skill Packages
- Use `skills/<skill-slug>/` with `skill.yaml`, `schemas/`, `impl/`, `tests/`, and `fixtures/`.
- Keep Skill implementations deterministic and stateless; declare access in `skill.yaml` and follow `docs/access-manifest.md`.
- Prefer stdout-only Skills; avoid filesystem writes unless explicitly required and reviewed.

Authoritative reference: `docs/skills/skill-library-v1.md` (spec: `specs/skill-library-v1.md`).
