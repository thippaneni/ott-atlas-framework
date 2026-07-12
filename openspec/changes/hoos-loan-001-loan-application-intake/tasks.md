## 1. Feature Package

- [ ] 1.1 Create `docs/features/HOOS-LOAN-001/README.md` with overview and traceability.
- [ ] 1.2 Create `feature.md` and `acceptance.md` for loan application intake.
- [ ] 1.3 Create `domain.md` for loan intake domain model and state transitions.
- [ ] 1.4 Create `api.md`, `database.md`, and `ui.md` contracts.
- [ ] 1.5 Create `tasks.md`, `implementation.md`, `tests.md`, `review.md`, and `release.md`.

## 2. Backend Implementation Plan

- [ ] 2.1 Define backend tasks for `hoos/HOOS-Backend` without implementing code in this change.
- [ ] 2.2 Define API endpoints and validation behavior.
- [ ] 2.3 Define database tables, indexes, and migration expectations.

## 3. Frontend Implementation Plan

- [ ] 3.1 Define frontend tasks for `hoos/HOOS-Frontend` without implementing code in this change.
- [ ] 3.2 Define step-based intake UI contract and states.
- [ ] 3.3 Define frontend validation and API integration expectations.

## 4. Validation

- [ ] 4.1 Validate Atlas with `python tools/validate-atlas.py`.
- [ ] 4.2 Validate OpenSpec with `openspec validate hoos-loan-001-loan-application-intake --type change`.
- [ ] 4.3 Confirm no backend or frontend implementation code was added.