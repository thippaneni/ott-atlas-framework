# ADR-0003: Knowledge-Driven Context Loading

## Status

Accepted

## Date

2026-06-28

## Context

Large language models have limited context windows. Loading every document for every task is inefficient and increases the likelihood that irrelevant information will influence responses.

Atlas needs a repeatable way to load the minimum useful engineering context for a given task.

## Decision

Atlas SHALL implement selective context loading.

The framework SHALL use these files to determine which documents are required for a task:

- manifest.yaml
- index.yaml
- contexts.yaml

Only the minimum necessary context SHALL be loaded.

Unrelated modules SHALL NOT be loaded.

## Consequences

Positive consequences:

- Faster AI interactions.
- Reduced token usage.
- Improved response quality.
- Better scalability as Atlas grows.

Negative consequences:

- Dependency metadata must be maintained.
- Framework design becomes slightly more complex.

## Alternatives Considered

- Load all documentation.
- Manually select documents for each task.
- Use prompt-only context management.

These alternatives were rejected because they do not scale effectively.

## Related ADRs

- ADR-0002
- ADR-0005
