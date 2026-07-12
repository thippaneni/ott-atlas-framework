## Context

`HOOS-CORE-001` defines HOOS as a Home Ownership Operating System focused initially on home loan intelligence. `HOOS-LOAN-001` is the first business workflow feature: borrowers start a draft home loan application and capture enough information to continue into eligibility and document workflows later.

The backend and frontend repositories are present, but this change only creates feature docs and OpenSpec artifacts. Implementation should happen after review.

## Goals / Non-Goals

**Goals:**

- Define the first loan application intake workflow.
- Capture borrower, optional co-applicant, property, income, obligation, and consent basics.
- Allow draft save and later continuation.
- Define clear backend API and database expectations.
- Define clear frontend UI states and validation expectations.
- Split implementation tasks by backend and frontend repository.

**Non-Goals:**

- No authentication implementation.
- No real lender integration.
- No final eligibility engine.
- No document upload implementation.
- No payment, offer acceptance, or underwriting workflow.
- No application code in the Atlas framework repository.

## Decisions

### Decision 1: Loan application intake starts as a draft workflow

A borrower can create a draft loan application with minimal required fields, progressively add details, and submit the intake when required fields and consent are present.

Alternative considered: require all information up front. Rejected because home loan journeys are long and users need save-and-resume behavior.

### Decision 2: Application submission is not lender submission

Submitting intake means the borrower has completed the initial HOOS intake. It does not submit to a lender or start underwriting.

Alternative considered: combine intake and lender submission. Rejected because lender submission requires documents, eligibility, compliance, and integration decisions not yet designed.

### Decision 3: API and database contracts are feature-local first

The initial API/database design focuses on the Loan Application aggregate and can evolve in later features.

Alternative considered: design the full loan platform schema now. Rejected because it would front-load too many unknowns.

### Decision 4: Frontend intake should be step-based

The Angular UI should guide users through a step-based intake flow with validation, autosave/manual save, review, and submit states.

Alternative considered: single long form. Rejected because home loan information is multi-part and easier to complete in guided sections.

## Risks / Trade-offs

- [Risk] Market-specific loan fields may differ. -> Mitigation: keep initial fields generic and track market-specific questions.
- [Risk] Authentication dependency may block real borrower ownership. -> Mitigation: treat borrower identity as an external/current-user dependency for implementation planning.
- [Risk] Draft persistence can get complex. -> Mitigation: define simple status transitions first: Draft, Submitted, Cancelled.
- [Risk] Eligibility needs may pull fields into intake. -> Mitigation: capture enough basics and leave detailed eligibility to a later feature.

## Migration Plan

No runtime migration is required for this documentation/specification change.

Implementation migration later will require initial database migrations in `hoos/HOOS-Backend`.

## Open Questions

- Which market/country is the first target for required loan fields?
- Is authentication assumed complete before this feature implementation?
- Should draft applications expire or remain indefinitely?
- Are co-applicants supported in v1 or deferred after primary applicant intake?