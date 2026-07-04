# ADR-0002: Atlas Shall Be AI-First

## Status

Accepted

## Date

2026-06-28

## Context

Existing engineering frameworks primarily target human developers and treat AI as an external tool.

Atlas is designed for an environment where AI assistants participate throughout the software lifecycle while humans retain engineering judgment and accountability.

## Decision

Atlas SHALL treat AI assistants as first-class engineering participants.

Engineering knowledge SHALL be represented in structured, machine-readable formats whenever practical.

Documentation SHALL be organized for both humans and AI agents.

AI SHALL augment engineering judgment. It SHALL NOT replace engineering judgment.

## Consequences

Positive consequences:

- More consistent AI behavior.
- Reduced prompt repetition.
- Better context reuse.
- Stronger multi-agent collaboration.

Negative consequences:

- Additional framework maintenance.
- Increased emphasis on structured metadata.

## Alternatives Considered

- Human-first documentation only.
- Prompt-only engineering.
- Tool-specific instructions.

These alternatives were rejected because they limit portability, automation, and reuse.

## Related ADRs

- ADR-0001
- ADR-0004
- ADR-0006
