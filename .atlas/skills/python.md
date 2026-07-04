# Python Skill

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Skills
- Depends on: standards/coding.md, standards/testing.md, rules/validation.yaml

## Purpose

Guide Python usage for automation, scripts, validation tools, data processing, and AI support workflows.

## Scope

Use for repository automation, document processing, schema validation, data utilities, and AI integration helpers.

## Best Practices

- Keep scripts deterministic and safe to rerun.
- Validate inputs and file paths before processing.
- Prefer small command-line tools with clear arguments and outputs.
- Keep generated artifacts separate from source knowledge unless intentionally tracked.
- Add tests for reusable utilities.

## Anti-patterns

- One-off scripts with hidden assumptions.
- Scripts that modify broad filesystem areas without explicit paths.
- Silent failures or unstructured output for validation tasks.

## References

- rules/validation.yaml
- standards/testing.md
