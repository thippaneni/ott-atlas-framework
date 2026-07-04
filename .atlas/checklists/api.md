# API Checklist

## Metadata

- Version: 0.1.0
- Status: Draft
- Layer: Checklists
- Depends on: standards/api.md, rules/api.yaml, rules/errors.yaml, rules/security.yaml

## Purpose

Verify that API work is specified, consistent, secure, and testable.

## Checklist

- [ ] API behavior traces to an approved feature specification or API contract.
- [ ] Endpoint purpose, inputs, outputs, status codes, and errors are documented.
- [ ] Request validation is defined at the API boundary.
- [ ] Authentication and authorization behavior is explicit.
- [ ] Success and error response shapes are consistent.
- [ ] Error responses do not expose stack traces or internal details.
- [ ] API tests cover success, validation failure, authorization failure, and important domain failures.
- [ ] Public contract changes are intentional and documented.

## Completion Criteria

The API is ready when behavior, contract, security, and tests all align with the specification.
