# ADR-0006: AI Provider Agnostic Framework

## Status

Accepted

## Date

2026-06-28

## Context

Atlas is intended to be an open engineering framework for AI-assisted software development. If Atlas depends on one AI provider, model family, coding assistant, or prompt format, the framework will become less portable and more fragile over time.

Different teams may use Codex, ChatGPT, Claude, Gemini, Cursor, Windsurf, or future AI engineering tools.

## Decision

Atlas SHALL be AI provider agnostic.

Any compliant AI assistant SHOULD be able to consume Atlas specifications, standards, rules, patterns, instructions, and context definitions without modification.

Atlas MAY include tool-specific adapters, but core Atlas knowledge SHALL NOT depend on vendor-specific behavior.

## Consequences

Positive consequences:

- Portability across AI providers and coding tools.
- Reduced vendor lock-in.
- Longer-lived engineering knowledge.
- Easier adoption by different teams and workflows.

Negative consequences:

- Atlas must avoid provider-specific assumptions in core files.
- Tool-specific optimizations may need adapters instead of direct embedding.

## Alternatives Considered

- Optimize Atlas for one AI provider.
- Maintain separate knowledge systems per tool.
- Embed provider-specific behavior in core prompts.

These alternatives were rejected because they conflict with Atlas portability and reuse.

## Related ADRs

- ADR-0002
- ADR-0005
