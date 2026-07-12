## Why

HOOS needs a repeatable feature implementation workflow before backend and frontend development begins. The attached planning document proposes treating each feature as a complete engineering artifact with traceability from business need through release.

This belongs in Atlas because it affects every future HOOS feature and every project that uses Atlas, not just one implementation task.

## What Changes

- Add the Atlas Feature Lifecycle (AFL) as a mandatory Atlas standard.
- Add ADR-0007 to establish features as the fundamental unit of engineering.
- Add a reusable feature package template for feature-scoped artifacts.
- Add a feature gate checklist covering specification, design, implementation, quality, and release readiness.
- Update Atlas registries and contexts so future HOOS implementation work can load feature lifecycle guidance.
- Keep implementation code out of the Atlas framework repo; backend work remains in `hoos/HOOS-Backend` and frontend work remains in `hoos/HOOS-Frontend`.

## Capabilities

### New Capabilities

- `feature-lifecycle`: Defines the lifecycle, gates, state machine, and required artifact package for Atlas-managed features.

### Modified Capabilities

None. This is the first OpenSpec capability introduced for Atlas-managed HOOS feature delivery.

## Impact

- Atlas framework docs and governance files are updated.
- OpenSpec gains a baseline capability spec for feature lifecycle.
- Future HOOS feature folders will follow `HOOS-AREA-NNN/` structure with feature, acceptance, domain, API, database, UI, task, test, review, and release artifacts.
- Backend implementation changes should target `hoos/HOOS-Backend`.
- Frontend implementation changes should target `hoos/HOOS-Frontend`.
- No application source code is implemented as part of this change.