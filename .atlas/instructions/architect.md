# Architect Instruction

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Instructions
- Depends on: principles.md, architecture/decisions/, patterns/modular-monolith.md

## Purpose

Guide architecture work for Atlas-based SaaS projects.

## Scope

Use when defining architecture, module boundaries, ADRs, technology choices, dependencies, and tradeoffs.

## Instruction

- Start from specifications, principles, and existing ADRs.
- Preserve Atlas provider agnosticism and configuration-over-prompts decisions.
- Prefer modular monolith boundaries until distributed architecture is justified.
- Make module dependencies explicit and directional.
- Record significant architecture decisions as ADRs.
- Identify security, performance, operability, and migration consequences.

## Inputs

- Vision, PRD, SRS, architecture specs, domain model, ADRs, manifest, index.

## Outputs

- Architecture guidance, ADRs, module boundaries, dependency rules, tradeoffs, open questions.

## Definition of Done

- Decisions are traceable.
- Consequences and alternatives are documented.
- Implementation teams have clear constraints.
