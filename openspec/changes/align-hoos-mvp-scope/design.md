## Context

HOOS has a broad long-term vision with identity, loan management, calculator engine, property management, document intelligence, AI financial intelligence, dashboard, notifications, property intelligence, and marketplace modules.

For launch, the user has clarified that the first build should focus on five concrete features that solve immediate problems for Indian home loan customers.

## Goals / Non-Goals

**Goals:**

- Lock the MVP scope to the first five features.
- Prevent implementation drift into deferred modules.
- Reframe near-term work around loan management and calculators.
- Preserve deferred ideas for future phases.

**Non-Goals:**

- Delete previous feature docs.
- Implement backend or frontend code.
- Fully specify all five MVP features in this change.
- Build authentication or subscription workflows now.

## Decisions

### Decision 1: First five features define MVP scope

HOOS MVP work will focus on Loan Workspace, EMI Calculator, Part Payment Simulator, Balance Transfer Analyzer, and Loan Dashboard.

### Decision 2: Loan application intake is deferred

`HOOS-LOAN-001: Loan Application Intake` is useful later but does not match the clarified immediate launch strategy. It should be marked deferred and not used as the next implementation target.

### Decision 3: Identity is deferred unless needed as a technical prerequisite

Authentication is important, but the MVP product sequence should not start with identity unless a specific implementation feature requires it.

## Risks / Trade-offs

- [Risk] Deferring auth may limit real user persistence. -> Mitigation: use local/demo storage or minimal technical auth later if required.
- [Risk] Calculator-first scope may delay account/subscription features. -> Mitigation: focus on user value first, monetization later.
- [Risk] Existing loan application docs may confuse future work. -> Mitigation: mark them deferred and point to the MVP scope lock.