# AWS Skill

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Skills
- Depends on: standards/security.md, standards/performance.md, standards/git.md

## Purpose

Guide AWS architecture, deployment, security, and operational decisions.

## Scope

Use for cloud architecture, deployment design, IAM, networking, storage, compute, observability, and automation.

## Best Practices

- Start from architecture decisions and deployment specifications.
- Apply least privilege to IAM roles and policies.
- Keep environments reproducible through infrastructure as code where practical.
- Separate secrets from source control and Atlas files.
- Add observability for critical workflows.
- Document cost, reliability, and scaling tradeoffs.

## Anti-patterns

- Manual cloud changes with no documented reproduction path.
- Overly broad IAM permissions.
- Embedding provider-specific assumptions into core Atlas files.

## References

- ADR-0006
- standards/security.md
- rules/security.yaml
