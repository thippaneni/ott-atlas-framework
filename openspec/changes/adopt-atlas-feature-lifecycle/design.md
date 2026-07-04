## Context

The attached planning document proposes the Atlas Feature Lifecycle (AFL): every feature should move from business need through specification, design, implementation, tests, review, documentation, and release using consistent gates and feature-scoped artifacts.

Atlas already defines specification-driven development, knowledge-driven context loading, modular knowledge architecture, and configuration over prompts. HOOS now needs a concrete feature lifecycle before backend and frontend implementation begins.

## Goals / Non-Goals

**Goals:**

- Make features the fundamental unit of HOOS engineering work.
- Require every feature to have a stable ID and self-contained artifact folder.
- Define feature gates from specification through release.
- Add Atlas guidance that maps feature implementation to `hoos/HOOS-Backend` and `hoos/HOOS-Frontend`.
- Keep feature lifecycle knowledge in Atlas and OpenSpec, not transient prompts.

**Non-Goals:**

- Implement any HOOS backend or frontend feature in this change.
- Define the complete HOOS product roadmap.
- Replace OpenSpec change management.
- Move HOOS implementation source code into the Atlas framework repository.

## Decisions

### Decision 1: Features are the fundamental unit of engineering

Atlas-managed HOOS work will organize implementation around features, not around isolated files, services, or tickets. Each feature receives a stable feature ID and a complete artifact package.

Alternative considered: organize only by repository or module. This was rejected because AI-assisted work needs compact, traceable context for each feature.

### Decision 2: Feature folders are self-contained

Each feature folder should contain feature, acceptance, domain, API, database, UI, task, test, review, implementation, and release artifacts where applicable.

Alternative considered: keep feature artifacts distributed across separate folders. This was rejected because it makes later AI context loading and traceability harder.

### Decision 3: Implementation starts after readiness gates

Implementation begins only after specification and design gates are satisfied. This keeps backend/frontend coding aligned with business intent, domain modeling, API contracts, database design, and UI expectations.

Alternative considered: start coding immediately after a rough feature idea. This was rejected because it conflicts with Atlas SDSD principles.

### Decision 4: Atlas governs, HOOS repos implement

Atlas/OpenSpec hold lifecycle, governance, and specification artifacts. Backend code goes to `hoos/HOOS-Backend`; frontend code goes to `hoos/HOOS-Frontend`.

Alternative considered: place HOOS source under the Atlas root. This was rejected because the HOOS repos are separate implementation repositories with their own Git histories.

## Risks / Trade-offs

- [Risk] More upfront documentation may slow early feature work. -> Mitigation: provide templates and feature gates so the process is repeatable and lightweight.
- [Risk] Feature folders may duplicate some information from OpenSpec changes. -> Mitigation: OpenSpec remains the change workflow; feature folders become the durable engineering package.
- [Risk] Teams may skip gates under delivery pressure. -> Mitigation: add checklist and validation hooks that make gate status visible before implementation.
- [Risk] Backend and frontend repos may drift from specs. -> Mitigation: require feature IDs in tasks, commits, PRs, and release notes where practical.

## Migration Plan

1. Add the Atlas Feature Lifecycle standard.
2. Add ADR-0007.
3. Add feature package and feature gate templates/checklists.
4. Register the new files in Atlas index and contexts.
5. Validate Atlas and OpenSpec.
6. Use this lifecycle for the first HOOS feature before writing implementation code.

No runtime migration is required.

## Open Questions

- Should future feature folders live under `openspec/specs/features/`, `docs/features/`, or a dedicated `features/` directory after archival?
- Should feature IDs be allocated manually or by a future `atlas feature create` tool?
