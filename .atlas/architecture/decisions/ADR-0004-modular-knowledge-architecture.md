# ADR-0004: Modular Knowledge Architecture

## Status

Accepted

## Date

2026-06-28

## Context

Atlas is intended to grow into an engineering memory system. If all engineering knowledge is stored as one monolithic body of documentation, it becomes difficult to discover, version, validate, and load selectively.

Atlas needs clear module boundaries for standards, rules, patterns, skills, instructions, agents, templates, and knowledge.

## Decision

Atlas SHALL use a modular knowledge architecture.

Knowledge modules SHALL have well-defined responsibilities and dependencies.

Modules SHALL be discoverable through index.yaml.

Modules SHOULD be independently versionable when they represent reusable or evolving knowledge.

The core dependency direction is:

1. Knowledge
2. Standards
3. Rules
4. Patterns
5. Skills
6. Instructions
7. Agents

Higher layers may depend on lower layers. Lower layers SHALL NOT depend on higher layers.

## Consequences

Positive consequences:

- Better extensibility.
- Easier selective context loading.
- Cleaner ownership boundaries.
- Reduced risk of duplicated or conflicting instructions.

Negative consequences:

- More files to maintain.
- Module relationships must be documented and validated.

## Alternatives Considered

- Single documentation directory.
- Prompt library only.
- Tool-specific knowledge bundles.

These alternatives were rejected because they make Atlas less portable, less discoverable, and harder to validate.

## Related ADRs

- ADR-0002
- ADR-0003
- ADR-0005
