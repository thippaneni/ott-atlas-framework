# Feature Specification: Loan Workspace

## Metadata

- Feature ID: HOOS-LOAN-002
- Status: Draft
- State: Design
- Owner: Product / Architecture

## Summary

Loan Workspace lets users create and manage one or more home loans. It is the foundation for HOOS calculators, simulators, balance transfer analysis, and dashboard reporting.

## Source Requirements

- HOOS MVP Scope
- HOOS-CORE-001: Product Foundation
- OpenSpec change: `hoos-loan-002-loan-workspace`
- ADR-0007: Features Are the Fundamental Unit of Engineering

## Actors

- User: A home loan customer managing one or more loans.

## Scope

- Create loan.
- Edit loan.
- Archive loan.
- Restore archived loan.
- View active loans.
- View archived loans.
- View loan details.
- Support multiple loans.

## Loan Details

- Loan nickname
- Lender name
- Loan amount
- Interest rate
- Interest rate type: Floating or Fixed
- Tenure in months
- EMI
- Outstanding principal
- Loan start date
- Status: Active or Archived

## Non-goals

- Authentication and user registration.
- Loan origination/application intake.
- Disbursement management.
- EMI payment history.
- Part payment tracking.
- Balance transfer comparison.
- Dashboard widgets.
- Document upload.
- AI recommendations.

## Business Rules

- Loan amount must be greater than zero.
- Interest rate must be greater than zero.
- Tenure must be greater than zero.
- EMI must be greater than zero.
- Outstanding principal must be zero or greater.
- Outstanding principal must not exceed loan amount unless explicitly allowed later.
- Archived loans are hidden from the default active workspace view.
- Archived loans cannot be edited unless restored.

## Open Questions

- Should outstanding principal be allowed to exceed original loan amount for top-up scenarios?
- Should EMI be user-entered, calculated, or both?
- Should restore archived loan be included in first implementation or deferred?
- What placeholder ownership model should be used before identity is implemented?