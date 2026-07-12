## Why

HOOS needs a product foundation before backend and frontend implementation begins. The project has Atlas and OpenSpec ready, but the product intent, core domain language, user roles, module map, and first implementation boundaries must be defined so future features do not drift.

This change establishes `HOOS-CORE-001` as the first Atlas-managed feature package and creates the baseline product foundation for the Home Ownership Operating System / Home Loan Intelligence Platform.

## What Changes

- Add a product foundation specification for HOOS.
- Define the initial product vision, user roles, domain language, system modules, and repository responsibilities.
- Create the first feature package under `docs/features/HOOS-CORE-001/`.
- Clarify that this feature is documentation/specification-only and does not implement backend or frontend code.
- Prepare the project for the first implementation feature, expected to be loan application intake.

## Capabilities

### New Capabilities

- `product-foundation`: Defines the baseline HOOS product purpose, domain terms, user roles, module map, and implementation boundaries.

### Modified Capabilities

None. This is the first HOOS product capability captured in OpenSpec.

## Impact

- Atlas/OpenSpec repository gains product foundation artifacts.
- Future backend work remains targeted at `hoos/HOOS-Backend`.
- Future frontend work remains targeted at `hoos/HOOS-Frontend`.
- No application source code is implemented in this change.