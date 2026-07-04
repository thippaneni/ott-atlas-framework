# ADR-0001: Adopt Specification-Driven Software Development

## Status

Accepted

## Date

2026-06-28

## Context

Traditional software development often begins with implementation before requirements are fully defined. This creates inconsistent architecture, undocumented behavior, weak traceability, and increased technical debt.

Atlas is intended to be an AI-native engineering framework where humans and AI assistants collaborate through structured specifications.

## Decision

Atlas SHALL adopt Specification-Driven Software Development (SDSD) as its primary development methodology.

Every implementation SHALL trace back to one or more specifications.

The specification hierarchy SHALL be:

1. Vision
2. PRD
3. SRS
4. Architecture
5. Domain Model
6. Epic
7. Feature
8. Story
9. Task
10. Implementation

Implementation SHALL NOT introduce undocumented behavior.

## Consequences

Positive consequences:

- Complete traceability from intent to implementation.
- Better AI context selection.
- Improved documentation quality.
- Easier onboarding.
- More consistent implementation.

Negative consequences:

- Higher upfront documentation effort.
- Longer planning phase before implementation.

## Alternatives Considered

- Code-first development.
- Agile user-story-only development.
- Documentation after implementation.

These alternatives were rejected because they reduce traceability and weaken AI-assisted development.

## Related ADRs

- ADR-0002
- ADR-0003
