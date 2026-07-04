# Domain Events Pattern

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Patterns
- Depends on: ddd.md, rules/logging.yaml, standards/testing.md

## Purpose

Represent important business events explicitly so side effects, integrations, and workflows remain decoupled from core domain decisions.

## Scope

Use this pattern for events that matter to the business, workflow automation, notifications, audit trails, and integration triggers.

## Guidance

- Name events in past tense using domain language.
- Raise events from domain behavior, not from incidental technical actions.
- Keep event payloads focused and stable.
- Handle side effects outside the domain model.

## Example

Events such as LoanApplicationSubmitted, EligibilityCalculated, DocumentUploaded, or OfferSelected can drive notifications, audit records, and follow-up workflows.

## Best Practices

- Make event handling idempotent where retries are possible.
- Test that important domain behavior emits expected events.
- Document event consumers when events cross module boundaries.

## Anti-patterns

- Using events for every property change.
- Embedding infrastructure concerns inside domain events.
- Depending on event ordering without documenting the guarantee.

## References

- ddd.md
- modular-monolith.md
