# Data Model: Phase I – In-Memory Todo Python Console Application

**Feature**: 1-todo-cli-app | **Date**: 2026-01-02 | **Plan**: [plan.md](./plan.md)

## Core Entities

### Task
Represents a single todo item with properties that define its state and identity.

**Properties**:
- `id` (integer): Unique identifier for the task, auto-incremented starting from 1
- `title` (string): Required text that describes the task
- `description` (string): Optional additional details about the task
- `completed` (boolean): Status indicator, defaults to False

**Constraints**:
- Title must not be empty
- ID must be unique within the application session
- ID values start at 1 and increment by 1 for each new task

**State Transitions**:
- `completed` can transition from `False` to `True` (mark complete)
- `completed` can transition from `True` to `False` (mark incomplete)

## Data Storage

### Task Collection
- **Type**: List of Task objects
- **Access Pattern**: Linear search by ID for update/delete operations
- **Persistence**: In-memory only, cleared when application exits
- **Size Limitations**: Limited by available system memory

## Relationships

### Task to TaskList
- One-to-many: One application session contains many tasks
- The TaskList is simply a Python list containing Task objects
- No foreign keys needed as all data exists in memory

## Validation Rules

### Task Creation
- Title must be provided and not empty
- Description can be empty or null
- ID is automatically assigned from a counter

### Task Updates
- Task must exist (valid ID) before update
- Title cannot be empty after update
- ID cannot be modified

### Task Deletion
- Task must exist (valid ID) before deletion
- Operation should return confirmation of deletion