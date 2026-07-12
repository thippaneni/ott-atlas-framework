## Why

HOOS MVP starts with Loan Workspace because every calculator, simulator, analyzer, and dashboard needs a saved loan record to work from. Users need a place to create and manage one or more home loans before HOOS can calculate EMI, simulate part payments, compare balance transfer options, or show a dashboard.

This feature is the first MVP implementation-oriented feature after the product foundation and scope lock.

## What Changes

- Add `HOOS-LOAN-002` feature package for Loan Workspace.
- Define loan workspace scope, domain model, acceptance criteria, API contract, database design, UI contract, implementation tasks, and test plan.
- Support creating, editing, archiving, listing, and viewing multiple loans.
- Capture MVP loan details: loan amount, interest rate, floating/fixed type, tenure, EMI, outstanding principal, lender name, start date, and loan nickname.
- Split future implementation tasks between `hoos/HOOS-Backend` and `hoos/HOOS-Frontend`.

## Capabilities

### New Capabilities

- `loan-workspace`: Lets a user create and manage one or more home loan records as the foundation for calculators, simulations, balance transfer analysis, and dashboard reporting.

### Modified Capabilities

None.

## Impact

- Atlas/OpenSpec repository gains the first MVP feature package for implementation planning.
- Future backend implementation will target `hoos/HOOS-Backend`.
- Future frontend implementation will target `hoos/HOOS-Frontend`.
- No application source code is implemented by this specification change.