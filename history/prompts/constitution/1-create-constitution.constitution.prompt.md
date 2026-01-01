---
id: 1
title: Create Constitution
stage: constitution
date: 2026-01-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: user
command: /sp.constitution
labels: [constitution, setup, governance]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
---

## Prompt

```
/sp.constitution

Project Name:

Phase I – In-Memory Todo Console Application

(Spec-Driven Development)

Purpose:

The purpose of this project is to create a simple command-line Todo application that serves as the foundation of the "Evolution of Todo" project.

This phase is designed to strictly practice Spec-Driven Development, where the engineer defines intent, architecture, and constraints, and Claude Code is responsible for all implementation.

Core Principles

Development must follow Spec-Driven Development only

Manual coding is strictly prohibited under all circumstances

The engineer acts as a system architect, not a syntax writer

Every line of code must be traceable to an approved spec and task

Simplicity and clarity are preferred over over-engineering

Code should be clean, readable, and suitable for beginners and reviewers

Development Standards

No code may be written without an approved Task ID

All features must follow the SpecKit workflow:

Specify → Plan → Tasks → Implement

All code must be generated using Claude Code

Specs are the single source of truth and must never be overridden by code

Each feature must be independently specified and traceable

Architecture Rules

Application type: Python console (CLI) application

Data storage: In-memory only (no databases, no files, no persistence)

State management: Python data structures (lists, dictionaries, classes)

Single-user application

Modular design with clear separation of concerns (models, logic, CLI)

Phase I Feature Scope (Strict)

Only the following features are allowed in Phase I:

Add a task (title and description)

View the task list with clear status indicators

Update a task (title and/or description)

Delete a task by its unique ID

Mark a task as complete or incomplete

Explicit Constraints

No external databases

No file-based storage

No web frameworks

No asynchronous or concurrent logic

No AI or chatbot features in this phase

No features outside the defined Phase I scope

Technology Constraints

Python version: 3.13 or higher

Package management: UV

Tooling: Claude Code + Spec-Kit Plus only

Code Quality Rules

Clear and meaningful naming conventions

Small, focused functions

Predictable and consistent CLI behavior

Consistent formatting

No unused or dead code

Required Project Structure

/src directory containing all Python source code

A specs (or specs-history) directory containing all specification files

A Constitution file at the project root

README.md with setup and execution instructions

CLAUDE.md with guidelines for using Claude Code

Validation & Success Criteria

All five core features function correctly via the CLI

Each task has a unique identifier

Task completion status is clearly visible

All code is traceable back to its corresponding specs and tasks

No manual code edits are detected

Claude prompts and iterations clearly show spec refinement

Failure Conditions

Any manually written code

Missing or incomplete specifications

Features implemented without approved tasks

Additional features beyond Phase I scope

Direct coding without using Claude Code

Definition of Done

Phase I is considered complete when the console-based Todo application fully meets all defined requirements, passes manual CLI testing, and clearly demonstrates a correct and disciplined Spec-Driven Development workflow.
```

## Response snapshot

Created a constitution file for the Phase I In-Memory Todo Console Application with the following key principles:
1. Spec-Driven Development (NON-NEGOTIABLE)
2. Python Console Application
3. In-Memory Data Storage Only
4. Minimal Technology Stack
5. Modular Design with Separation of Concerns
6. Test-First Development (NON-NEGOTIABLE)

The constitution includes feature scope constraints, development workflow requirements, and governance rules that align with the project specifications.

## Outcome

- ✅ Impact: Created project constitution file with all required principles
- 🧪 Tests: N/A
- 📁 Files: Updated .specify/memory/constitution.md
- 🔁 Next prompts: Plan and specify the todo application features
- 🧠 Reflection: Constitution properly reflects all project constraints and requirements

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin specification phase for the todo application