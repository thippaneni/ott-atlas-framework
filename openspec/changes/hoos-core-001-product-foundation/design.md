## Context

Atlas and OpenSpec are now configured as the governance and specification layer for HOOS. The backend and frontend repositories exist under `hoos/HOOS-Backend` and `hoos/HOOS-Frontend`, but they should not receive implementation work until HOOS product intent and first-level domain structure are clear.

`HOOS-CORE-001` provides the baseline context that later features will depend on.

## Goals / Non-Goals

**Goals:**

- Define the initial HOOS product vision and scope.
- Establish the core domain vocabulary for home loan and home ownership workflows.
- Identify initial user roles and stakeholder types.
- Define initial system module boundaries.
- Map implementation responsibilities to backend and frontend repositories.
- Create a durable feature package for future traceability.

**Non-Goals:**

- Implement authentication, loan application intake, eligibility, underwriting, document upload, or lender matching.
- Choose final UI design or database schema.
- Build .NET or Angular application code.
- Replace future PRD/SRS work for specific features.

## Decisions

### Decision 1: HOOS starts as a Home Loan Intelligence Platform

The initial product foundation focuses HOOS on helping users understand, prepare for, and progress through home loan journeys. Broader home ownership workflows can be added later.

Alternative considered: model all home ownership operations immediately. This was deferred because loan intelligence provides a clearer first product spine.

### Decision 2: Product foundation remains implementation-neutral

This change defines product and domain foundations only. Backend/frontend implementation will start in later feature changes.

Alternative considered: scaffold application code now. This was rejected because Atlas requires specification and design before implementation.

### Decision 3: Modules are initially conceptual

The first module map defines conceptual boundaries such as identity, borrower profile, loan application, eligibility, documents, lender offers, notifications, and administration. Concrete code modules can be refined during architecture and implementation features.

Alternative considered: lock code-level modules now. This was rejected because the domain needs one more refinement pass before code structure is fixed.

## Risks / Trade-offs

- [Risk] Product foundation may be too broad. -> Mitigation: mark assumptions and open questions explicitly.
- [Risk] Future implementation may reveal missing domain concepts. -> Mitigation: evolve the product foundation through OpenSpec changes.
- [Risk] Backend/frontend repos may drift from product foundation. -> Mitigation: require future implementation features to reference `HOOS-CORE-001`.

## Migration Plan

No runtime migration is required.

1. Create OpenSpec product foundation capability.
2. Create `docs/features/HOOS-CORE-001/` feature package.
3. Validate Atlas and OpenSpec.
4. Use this foundation as input to `HOOS-LOAN-001`.

## Open Questions

- Which country or regulatory market is the initial HOOS launch targeting?
- Will users be direct borrowers, loan advisors, internal operations staff, or all three?
- Which lender integrations are required for the first release?
- Should HOOS initially support only home loans or broader home ownership workflows?