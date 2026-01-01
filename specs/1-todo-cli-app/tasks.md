# Implementation Tasks: Phase I – In-Memory Todo Python Console Application

**Feature**: 1-todo-cli-app | **Created**: 2026-01-02 | **Spec**: [spec.md](../spec.md) | **Plan**: [plan.md](../plan.md)

## Implementation Strategy

**Approach**: MVP-first development with incremental delivery. Start with the most critical functionality (User Story 1) and build up to full feature set. Each user story should be independently testable.

**MVP Scope**: Core functionality to add and view tasks (User Stories 1 and 2) with basic CLI interface.

## Phase 1: Setup

**Goal**: Initialize project structure and basic files

- [x] T001 Create src directory structure
- [x] T002 Create main.py with basic application entry point
- [x] T003 Create models.py file
- [x] T004 Create services.py file
- [x] T005 Create cli.py file

## Phase 2: Foundational Components

**Goal**: Implement core data model and task management service

- [x] T006 [P] Implement Task class in src/models.py with id, title, description, completed properties
- [x] T007 [P] Implement TaskManager class in src/services.py with empty task list
- [x] T008 [P] Implement auto-incrementing ID counter in TaskManager

## Phase 3: User Story 1 - Add New Task (Priority: P1)

**Goal**: Implement ability to add new tasks with title and optional description

**Independent Test**: Can be fully tested by running the application and executing the add task command with a title, then verifying the task appears in the system with a unique ID.

- [x] T009 [US1] Implement add_task method in TaskManager service
- [x] T010 [US1] Add input validation for title in add_task method
- [x] T011 [US1] Implement CLI add task functionality in src/cli.py
- [x] T012 [US1] Connect CLI add task to TaskManager service
- [x] T013 [US1] Test adding task with title only
- [x] T014 [US1] Test adding task with title and description

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Implement ability to view all tasks in a clear, readable format

**Independent Test**: Can be fully tested by adding a task and then viewing the task list to confirm the task appears with proper formatting and status indicators.

- [x] T015 [US2] Implement get_all_tasks method in TaskManager service
- [x] T016 [US2] Implement CLI view tasks functionality in src/cli.py
- [x] T017 [US2] Connect CLI view tasks to TaskManager service
- [x] T018 [US2] Format task display with ID, title, and completion status
- [x] T019 [US2] Handle empty task list case with appropriate message
- [x] T020 [US2] Test viewing tasks after adding multiple tasks

## Phase 5: User Story 5 - Mark Task Complete/Incomplete (Priority: P1)

**Goal**: Implement ability to change completion status of tasks

**Independent Test**: Can be fully tested by adding a task, marking it complete, and verifying the status change when viewing the task list.

- [x] T021 [US5] Implement mark_task_completed method in TaskManager service
- [x] T022 [US5] Implement CLI mark task functionality in src/cli.py
- [x] T023 [US5] Connect CLI mark task to TaskManager service
- [x] T024 [US5] Add validation for valid task ID in mark_task_completed
- [x] T025 [US5] Test marking task as complete
- [x] T026 [US5] Test marking task as incomplete

## Phase 6: User Story 3 - Update Task (Priority: P2)

**Goal**: Implement ability to modify existing task's title or description

**Independent Test**: Can be fully tested by adding a task, updating its details, and verifying the changes are reflected when viewing the task.

- [x] T027 [US3] Implement update_task method in TaskManager service
- [x] T028 [US3] Add validation for valid task ID in update_task method
- [x] T029 [US3] Add validation for non-empty title in update_task method
- [x] T030 [US3] Implement CLI update task functionality in src/cli.py
- [x] T031 [US3] Connect CLI update task to TaskManager service
- [x] T032 [US3] Test updating task title
- [x] T033 [US3] Test updating task description
- [x] T034 [US3] Test updating both title and description

## Phase 7: User Story 4 - Delete Task (Priority: P2)

**Goal**: Implement ability to remove tasks by ID

**Independent Test**: Can be fully tested by adding a task, deleting it, and verifying it no longer appears when viewing the task list.

- [x] T035 [US4] Implement delete_task method in TaskManager service
- [x] T036 [US4] Add validation for valid task ID in delete_task method
- [x] T037 [US4] Implement CLI delete task functionality in src/cli.py
- [x] T038 [US4] Connect CLI delete task to TaskManager service
- [x] T039 [US4] Test deleting existing task
- [x] T040 [US4] Test attempting to delete non-existent task

## Phase 8: CLI Integration and Menu

**Goal**: Create complete menu-driven CLI interface connecting all functionality

- [x] T041 Implement main menu loop in src/cli.py with all options
- [x] T042 Add menu option 1: Add task
- [x] T043 Add menu option 2: View tasks
- [x] T044 Add menu option 3: Update task
- [x] T045 Add menu option 4: Delete task
- [x] T046 Add menu option 5: Mark task complete/incomplete
- [x] T047 Add menu option 6: Exit
- [x] T048 Connect main.py to initialize and run CLI interface

## Phase 9: Error Handling and Validation

**Goal**: Implement comprehensive error handling and input validation

- [x] T049 Add error handling for invalid task IDs across all operations
- [x] T050 Add input validation for empty titles in CLI
- [x] T051 Add error messages for invalid user inputs
- [x] T052 Ensure application continues running after error conditions
- [x] T053 Add validation for numeric input where expected

## Phase 10: Polish & Cross-Cutting Concerns

**Goal**: Final integration, testing, and code quality improvements

- [x] T054 Test complete workflow: add, view, update, delete, mark complete
- [x] T055 Verify all error conditions are handled gracefully
- [x] T056 Format output for readability and consistency
- [x] T057 Ensure all requirements from spec are met
- [x] T058 Code cleanup and documentation
- [x] T059 Final end-to-end testing

## Dependencies

**User Story Completion Order**:
- User Story 1 (Add Task) and User Story 2 (View Tasks) can be developed in parallel
- User Story 5 (Mark Complete/Incomplete) can be developed in parallel with US1/US2
- User Story 3 (Update Task) and User Story 4 (Delete Task) can be developed after US1/US2/US5

## Parallel Execution Examples

**Parallel Tasks by Component**:
- Models: T006 (Task class) can run in parallel with Services: T007, T008
- Services: TaskManager methods can be developed in parallel after T007
- CLI: Individual functionality can be developed in parallel after services are available

**Parallel Tasks by Story**:
- US1 and US2 can be developed in parallel
- US3 and US4 can be developed in parallel
- US5 can be developed in parallel with US1/US2