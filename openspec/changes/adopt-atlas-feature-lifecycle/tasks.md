## 1. Atlas Governance

- [ ] 1.1 Add `standards/feature-lifecycle.md` defining AFL stages, gates, artifacts, and state machine.
- [ ] 1.2 Add ADR-0007 documenting features as the fundamental unit of engineering.
- [ ] 1.3 Register the new standard and ADR in `.atlas/index.yaml`.
- [ ] 1.4 Update `.atlas/contexts.yaml` so specification, backend, frontend, database, testing, review, and deployment contexts can load feature lifecycle guidance.

## 2. Feature Artifacts

- [ ] 2.1 Add a feature package template that defines the required folder structure for `HOOS-AREA-NNN` features.
- [ ] 2.2 Add a feature gate checklist for specification, design, implementation, quality, and release readiness.
- [ ] 2.3 Register the new template and checklist in `.atlas/index.yaml`.

## 3. OpenSpec Baseline

- [ ] 3.1 Add an OpenSpec feature-lifecycle capability spec.
- [ ] 3.2 Validate the OpenSpec change with `openspec.cmd validate adopt-atlas-feature-lifecycle`.
- [ ] 3.3 Keep the OpenSpec config aligned with the Atlas and HOOS repository topology.

## 4. HOOS Repository Guidance

- [ ] 4.1 Update `hoos/HOOS-Backend/README.md` with feature lifecycle implementation guidance for backend work.
- [ ] 4.2 Update `hoos/HOOS-Frontend/README.md` with feature lifecycle implementation guidance for frontend work.
- [ ] 4.3 Ensure both HOOS repos point back to Atlas/OpenSpec as the source of truth.

## 5. Validation

- [ ] 5.1 Run Atlas validation with `python tools/validate-atlas.py`.
- [ ] 5.2 Run OpenSpec validation with `openspec.cmd validate --all`.
- [ ] 5.3 Confirm no HOOS application source code was added to the Atlas framework root.
