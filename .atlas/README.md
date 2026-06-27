# Atlas Framework

Atlas is an AI-native engineering framework for Specification-Driven Software Development (SDSD).

It standardizes how AI assistants, developers, and engineering teams collaborate across the software development lifecycle while keeping specifications, engineering standards, and architectural decisions as the source of truth.

## Purpose

Atlas ensures implementation follows documented intent, architecture, standards, and validation rules.

## Core Responsibilities

- Specification management
- Context management
- AI agent orchestration
- Engineering standards
- Development patterns
- Knowledge management
- Prompt templates
- Validation rules
- Project governance

## Root Files

- `manifest.yaml`: Atlas and project identity, architecture, version, and AI configuration.
- `index.yaml`: Knowledge graph, module discovery, dependency graph, load order, and context resolution.
- `capabilities.yaml`: AI agents, skills, responsibilities, and supported operations.
- `contexts.yaml`: Reusable context-loading profiles for focused work.
- `principles.md`: Immutable engineering principles that apply to every Atlas project.
- `ATS.md`: Atlas Technical Specification.

## Logical Layers

1. Project Metadata
2. Engineering Governance
3. AI Context Management
4. Knowledge System
5. Specifications

Every layer depends only on lower layers.
