# DevOps Instruction

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Instructions
- Depends on: skills/aws.md, standards/security.md, standards/performance.md

## Purpose

Guide deployment, automation, environment, and operations work.

## Scope

Use for AWS deployment planning, CI/CD alignment, infrastructure, observability, environment configuration, and release support.

## Instruction

- Start from architecture and deployment specifications.
- Keep environments reproducible and documented.
- Apply least privilege and secret separation.
- Do not embed provider-specific behavior in core Atlas knowledge.
- Add observability for critical workflows.
- Document operational risks, rollback paths, and cost considerations.

## Inputs

- Architecture, deployment requirements, security rules, operational constraints.

## Outputs

- Deployment guidance, automation notes, environment checklist, operational risks.

## Definition of Done

- Deployment path is reproducible.
- Secrets are not stored in source or Atlas files.
- Operational risks are documented.
