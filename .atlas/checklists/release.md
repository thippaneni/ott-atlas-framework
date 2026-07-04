# Release Checklist

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Checklists
- Depends on: standards/git.md, standards/testing.md, instructions/devops.md

## Purpose

Verify that a release is documented, validated, reproducible, and safe to ship.

## Checklist

- [ ] Version and release scope are defined.
- [ ] Changelog or release notes are updated.
- [ ] Required validation checks pass.
- [ ] Tests pass or known gaps are documented and accepted.
- [ ] Migration or deployment steps are documented.
- [ ] Rollback or recovery notes exist where relevant.
- [ ] Secrets and environment values are externalized.
- [ ] Git tag or release marker is prepared when appropriate.

## Completion Criteria

The release is ready when scope, validation, deployment, and recovery expectations are clear.
