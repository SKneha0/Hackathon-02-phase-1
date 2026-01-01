<!-- SYNC IMPACT REPORT:
     Version change: N/A (initial creation) → 1.0.0
     Modified principles: N/A
     Added sections: All principles and sections
     Removed sections: N/A
     Templates requiring updates: ✅ updated / ⚠ pending
     Follow-up TODOs: None
-->

# Phase I – In-Memory Todo Console Application Constitution

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)
Every feature must be defined in an approved specification before implementation begins. All code must be traceable back to corresponding specs and tasks. No manual coding is permitted under any circumstances; all code must be generated using Claude Code.

### II. Python Console Application
Application must be a command-line interface (CLI) application built in Python. The interface should follow predictable and consistent CLI behavior with clear text input/output protocols: stdin/args → stdout, errors → stderr. Support both human-readable formats and structured output where appropriate.

### III. In-Memory Data Storage Only
All data storage must be in-memory using Python data structures (lists, dictionaries, classes). No external databases, file-based storage, or persistence mechanisms are allowed. This ensures simplicity and adherence to Phase I constraints.

### IV. Minimal Technology Stack
Use Python 3.13 or higher with UV for package management. No external frameworks beyond what's necessary for basic CLI functionality. No asynchronous or concurrent logic. No AI or chatbot features in this phase.

### V. Modular Design with Separation of Concerns
Code must follow modular design principles with clear separation between models (data structures), business logic (task operations), and CLI interface (user interaction). Each module should have a single, well-defined responsibility.

### VI. Test-First Development (NON-NEGOTIABLE)
All features must be developed following Test-Driven Development (TDD) methodology: tests written → test approval → tests fail → then implement. Red-Green-Refactor cycle must be strictly enforced to ensure code quality and correctness.

## Feature Scope Constraints
Only the following five core features are allowed in Phase I: (1) Add a task (title and description), (2) View the task list with clear status indicators, (3) Update a task (title and/or description), (4) Delete a task by its unique ID, (5) Mark a task as complete or incomplete. No additional features beyond this scope are permitted.

## Development Workflow
All development must follow the SpecKit workflow: Specify → Plan → Tasks → Implement. Every line of code must have an approved Task ID. Code quality must maintain clean, readable standards suitable for beginners and reviewers. All changes must be small, focused, and testable with consistent formatting and no dead code.

## Governance

This constitution supersedes all other development practices and must be followed without exception. All code reviews and pull requests must verify compliance with these principles. Amendments to this constitution require explicit documentation, approval, and migration plan if applicable. All implementation work must be traceable to approved specifications and tasks.

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02
