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

HOOS helps users understand, prepare for, and progress through the home loan journey with structured guidance, eligibility intelligence, document readiness, and future lender comparison workflows.

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

- Identity and Access
- Borrower Profile
- Loan Application
- Eligibility Intelligence
- Property and Purchase Details
- Document Management
- Lender Offers
- Notifications
- Administration
- Audit and Compliance

## Acceptance Summary

The feature is accepted when future HOOS features can reference this foundation for product intent, roles, domain language, module boundaries, and repository responsibilities.