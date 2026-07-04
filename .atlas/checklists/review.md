# Review Checklist

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Checklists
- Depends on: instructions/reviewer.md, standards/git.md, rules/validation.yaml

## Purpose

Guide Atlas review toward bugs, regressions, missing tests, and compliance gaps.

## Checklist

- [ ] The change traces to a specification, task, ADR, or documented request.
- [ ] Scope is focused and does not mix unrelated work.
- [ ] Behavior matches the relevant specification and acceptance criteria.
- [ ] Tests are added or updated for changed behavior.
- [ ] Security, data exposure, and authorization risks are considered.
- [ ] Error handling and logging follow Atlas rules.
- [ ] Documentation is updated when behavior, architecture, or usage changes.
- [ ] Findings are actionable, severity-ranked, and tied to files or lines when possible.

## Completion Criteria

The review is complete when risks are identified, open questions are clear, and approval or requested changes are justified.
