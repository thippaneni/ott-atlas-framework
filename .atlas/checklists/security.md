# Security Checklist

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Checklists
- Depends on: standards/security.md, rules/security.yaml, rules/logging.yaml

## Purpose

Verify secure defaults, secret safety, and trust-boundary protection.

## Checklist

- [ ] No passwords, API keys, secrets, certificates, or sensitive credentials are committed.
- [ ] Authentication and authorization paths are documented and tested.
- [ ] Least privilege is applied to users, services, roles, and automation.
- [ ] Inputs are validated at trust boundaries.
- [ ] Logs do not contain secrets or sensitive credentials.
- [ ] User-facing errors do not expose internal implementation details.
- [ ] Sensitive data handling is documented where relevant.
- [ ] Security-sensitive changes received focused review.

## Completion Criteria

The change is ready when secret exposure, access control, data handling, and logging risks are reviewed.
