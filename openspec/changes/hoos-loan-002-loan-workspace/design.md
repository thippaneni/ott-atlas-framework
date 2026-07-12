## Context

The HOOS MVP scope is locked to five launch features: Loan Workspace, EMI Calculator, Part Payment Simulator, Balance Transfer Analyzer, and Loan Dashboard. Loan Workspace is first because it creates the persistent loan record that the other four features can use.

This feature should model existing or planned home loans, not loan origination/application intake. Authentication is deferred unless needed as a technical prerequisite; the feature may initially assume a current user context during implementation.

## Goals / Non-Goals

**Goals:**

- Let users create one or more home loan records.
- Let users edit loan details.
- Let users archive loans instead of deleting them.
- Let users view a loan list and loan detail page.
- Capture enough loan data to support EMI calculator, part payment simulation, balance transfer analysis, and dashboard summary later.
- Define backend API, database, and frontend UI contracts.

**Non-Goals:**

- No user registration or login implementation.
- No loan application/origination workflow.
- No disbursement management.
- No repayment history import.
- No document upload.
- No AI recommendations.
- No real lender integration.

## Decisions

### Decision 1: Loan Workspace stores user-entered loan records

Users can manually enter loan details. This avoids dependency on lender integrations or document extraction for the MVP.

Alternative considered: import loan data from bank statements or sanction letters. Rejected for MVP because document intelligence is deferred.

### Decision 2: Archive instead of delete

Loans can be archived so users can hide inactive loans while preserving history for calculations and reports.

Alternative considered: hard delete. Rejected because financial records should not disappear casually.

### Decision 3: Outstanding principal is user-entered in MVP

Outstanding principal is captured directly rather than derived from repayment history in the first version.

Alternative considered: derive outstanding balance from full amortization and EMI history. Deferred because repayment tracking is outside the first feature.

### Decision 4: Support multiple loans from the start

The workspace supports multiple loans because the MVP scope explicitly includes multiple loans support and future dashboard/reporting depends on it.

Alternative considered: single-loan MVP. Rejected because multiple loan support is core to the workspace concept and not much harder at the spec level.

## Risks / Trade-offs

- [Risk] Without auth, persisted loans need an owner model. -> Mitigation: backend implementation may use a placeholder current-user boundary until identity is specified.
- [Risk] User-entered values may be inaccurate. -> Mitigation: add validation and clear field labels.
- [Risk] EMI may not match lender EMI exactly. -> Mitigation: store user-entered EMI and let calculators explain assumptions later.
- [Risk] Archive semantics may be confused with delete. -> Mitigation: UI should clearly say archived loans are hidden, not removed.

## Migration Plan

No runtime migration is required for this documentation/specification change.

Future implementation requires backend schema migration for loan records and frontend route creation.

## Open Questions

- Should loan ownership use a placeholder user ID until authentication exists?
- Should the first implementation include secured local/demo mode or require auth first?
- Which interest rate precision should be supported?
- Should EMI be required or auto-calculated when loan amount, rate, and tenure are available?