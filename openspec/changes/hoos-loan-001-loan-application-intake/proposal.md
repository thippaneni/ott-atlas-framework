## Why

HOOS needs its first real borrower-facing product feature: a borrower must be able to start a home loan application and save the initial application information before deeper eligibility, document, or lender workflows are implemented.

This feature turns the product foundation from `HOOS-CORE-001` into the first traceable loan workflow feature while still keeping implementation gated until the domain, API, database, and UI contracts are clear.

## What Changes

- Add `HOOS-LOAN-001` feature package for Loan Application Intake.
- Define the loan application intake scope, actors, acceptance criteria, and domain model.
- Define initial backend API contract for creating, reading, updating, and submitting a draft loan application.
- Define initial database design for a draft loan application aggregate.
- Define initial UI contract for an Angular borrower intake flow.
- Define implementation tasks split between `hoos/HOOS-Backend` and `hoos/HOOS-Frontend`.

## Capabilities

### New Capabilities

- `loan-application-intake`: Allows a borrower to start, save, update, review, and submit an initial home loan application intake.

### Modified Capabilities

None. This is the first loan workflow capability captured in OpenSpec.

## Impact

- Atlas/OpenSpec repository gains a new feature package and OpenSpec capability spec.
- Future backend implementation will target `hoos/HOOS-Backend`.
- Future frontend implementation will target `hoos/HOOS-Frontend`.
- No application source code is implemented by this documentation/specification change.