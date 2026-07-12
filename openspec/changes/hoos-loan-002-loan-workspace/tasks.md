## 1. Feature Package

- [ ] 1.1 Create `docs/features/HOOS-LOAN-002/README.md` with overview and traceability.
- [ ] 1.2 Create `feature.md` and `acceptance.md` for Loan Workspace.
- [ ] 1.3 Create `domain.md` for loan record model and status transitions.
- [ ] 1.4 Create `api.md`, `database.md`, and `ui.md` contracts.
- [ ] 1.5 Create `tasks.md`, `implementation.md`, `tests.md`, `review.md`, and `release.md`.

## 2. Backend Implementation Plan

- [ ] 2.1 Define backend tasks for `hoos/HOOS-Backend` without implementing code in this change.
- [ ] 2.2 Define API endpoints for create, list, get, update, archive, and restore.
- [ ] 2.3 Define database tables, indexes, constraints, and migration expectations.

## 3. Frontend Implementation Plan

- [ ] 3.1 Define frontend tasks for `hoos/HOOS-Frontend` without implementing code in this change.
- [ ] 3.2 Define Loan Workspace list, detail, create/edit, archive, and empty states.
- [ ] 3.3 Define frontend validation and API integration expectations.

## 4. Validation

- [ ] 4.1 Validate Atlas with `python tools/validate-atlas.py`.
- [ ] 4.2 Validate OpenSpec with `openspec validate hoos-loan-002-loan-workspace --type change`.
- [ ] 4.3 Confirm no backend or frontend implementation code was added.