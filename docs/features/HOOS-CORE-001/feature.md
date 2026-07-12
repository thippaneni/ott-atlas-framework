# Feature Specification: Product Foundation

## Metadata

- Feature ID: HOOS-CORE-001
- Status: Draft
- State: Proposed
- Owner: Product / Architecture

## Summary

HOOS is a Home Ownership Operating System focused initially on home loan intelligence. The first product foundation defines the baseline intent, language, actors, module boundaries, and repo responsibilities needed before implementing product features.

## Source Requirements

- Atlas Feature Lifecycle Standard
- ADR-0001: Adopt Specification-Driven Software Development
- ADR-0007: Features Are the Fundamental Unit of Engineering
- OpenSpec change: `hoos-core-001-product-foundation`

## Product Vision

HOOS helps Indian home loan customers manage, understand, optimize, and save money on their home loans. The immediate MVP is focused on loan workspace, calculators, simulation, refinance analysis, and dashboard reporting.

## MVP Scope Lock

The current MVP SHALL focus only on:

1. Loan Workspace
2. EMI Calculator
3. Part Payment Simulator
4. Balance Transfer Analyzer
5. Loan Dashboard

See docs/product/hoos-mvp-scope.md.

## Initial Scope

- Define product purpose and first release direction.
- Define initial roles and actors.
- Define domain language.
- Define conceptual modules.
- Define backend/frontend repository boundaries.

## Non-goals

- No authentication implementation.
- No loan application intake implementation.
- No eligibility engine implementation.
- No lender integration implementation.
- No UI implementation.
- No database schema implementation.

## Initial User Roles

- Borrower: Person seeking a home loan or home ownership guidance.
- Co-applicant: Additional person included in a loan application.
- Advisor: Person helping borrowers understand loan readiness and options.
- Operations User: Internal user managing workflow, document review, or support.
- Administrator: Internal user managing configuration, users, and system settings.

## Initial Conceptual Modules

### MVP Modules

- Loan Management Core
- Calculator Engine
- Dashboard and Reporting

### Deferred Modules

- Identity and User Management
- Property Management
- Document Intelligence
- AI Financial Intelligence
- Notifications and Automation
- Property Intelligence
- Marketplace

## Acceptance Summary

The feature is accepted when future HOOS features can reference this foundation for product intent, roles, domain language, module boundaries, and repository responsibilities.