# ADR-0005: Configuration Over Prompts

## Status

Accepted

## Date

2026-06-28

## Context

Prompt-heavy workflows often hide long-lived engineering decisions inside transient conversations. This makes behavior difficult to review, version, validate, and reuse across tools.

Atlas needs persistent engineering knowledge that is independent of any single chat, model, or coding assistant.

## Decision

Persistent engineering knowledge SHALL live in version-controlled configuration, specifications, standards, rules, patterns, and instructions.

Prompts SHALL orchestrate work. Prompts SHALL NOT be the primary storage location for long-lived engineering decisions.

Examples of persistent Atlas knowledge include:

- manifest.yaml
- capabilities.yaml
- contexts.yaml
- standards/
- rules/
- patterns/
- instructions/
- architecture/decisions/

## Consequences

Positive consequences:

- Better portability across AI tools.
- Shorter prompts.
- Easier review and version control.
- Clearer separation between orchestration and knowledge.

Negative consequences:

- More repository structure is required.
- Teams must keep configuration and knowledge files current.

## Alternatives Considered

- Store engineering knowledge in prompts.
- Store engineering knowledge in chat history.
- Store engineering knowledge in tool-specific configuration only.

These alternatives were rejected because they reduce portability and traceability.

## Related ADRs

- ADR-0002
- ADR-0003
- ADR-0004
- ADR-0006
