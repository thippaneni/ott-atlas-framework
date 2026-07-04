# OpenAI Skill

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Skills
- Depends on: ADR-0006, standards/security.md, rules/security.yaml

## Purpose

Guide OpenAI integration while preserving Atlas provider agnosticism.

## Scope

Use for AI-assisted workflows, prompt orchestration, structured outputs, document understanding, embeddings, and evaluation patterns.

## Best Practices

- Keep durable engineering knowledge in Atlas files, not prompts.
- Use prompts to orchestrate work and reference Atlas context.
- Avoid provider-specific assumptions in core Atlas modules.
- Keep API keys and secrets outside source control.
- Validate AI outputs against schemas, specifications, and acceptance criteria.
- Record model or provider-specific choices in adapters or architecture decisions.

## Anti-patterns

- Treating model output as verified implementation.
- Storing secrets in prompts, docs, or config files.
- Making core Atlas behavior dependent on one provider.

## References

- ADR-0005
- ADR-0006
- rules/validation.yaml
