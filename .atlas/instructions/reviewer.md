# Reviewer Instruction

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Instructions
- Depends on: principles.md, standards/, rules/, architecture/decisions/

## Purpose

Guide code and artifact review for Atlas projects.

## Scope

Use for reviewing implementation, documentation, configuration, specifications, and generated artifacts.

## Instruction

- Prioritize bugs, regressions, missing tests, security risks, and specification mismatches.
- Lead with findings ordered by severity.
- Reference exact files and lines when available.
- Check whether changes trace to specifications, standards, rules, and ADRs.
- Identify missing validation, unclear ownership, and undocumented behavior.
- Keep summaries brief and secondary to findings.

## Inputs

- Diff, specifications, principles, standards, rules, ADRs, test results.

## Outputs

- Findings, open questions, residual risks, approval or change request.

## Definition of Done

- Findings are actionable and traceable.
- Test gaps and residual risks are clear.
