# Component Contracts: Phase I – In-Memory Todo Python Console Application

**Feature**: 1-todo-cli-app | **Date**: 2026-01-02 | **Plan**: [plan.md](../plan.md)

## Component Interfaces

### Task Model Contract
**Component**: `models.py`

**Public Interface**:
- `Task(id: int, title: str, description: str, completed: bool)`
  - Constructor creates a task object with specified properties
  - Validates that title is not empty

**Properties**:
- `id: int` - Read-only unique identifier
- `title: str` - Read-write task title
- `description: str` - Read-write optional description
- `completed: bool` - Read-write completion status

### Task Service Contract
**Component**: `services.py`

**Public Interface**:
- `TaskManager()` - Constructor creates a service instance with empty task list
- `add_task(title: str, description: str = "") -> int` - Creates new task, returns assigned ID
- `get_all_tasks() -> List[Task]` - Returns all tasks in the collection
- `update_task(task_id: int, title: str = None, description: str = None) -> bool` - Updates task, returns success status
- `delete_task(task_id: int) -> bool` - Removes task, returns success status
- `mark_task_completed(task_id: int, completed: bool) -> bool` - Updates completion status, returns success status

**Behavior**:
- Task IDs are auto-incremented starting from 1
- Operations return boolean success status
- Invalid task IDs return False for update/delete/mark operations

### CLI Interface Contract
**Component**: `cli.py`

**Public Interface**:
- `TodoCLI(task_manager: TaskManager)` - Constructor accepts task manager instance
- `run()` - Starts the main menu loop and handles user interaction

**Behavior**:
- Displays numbered menu options to user
- Handles user input validation
- Formats and displays task information clearly
- Provides error messages for invalid operations
- Handles graceful exits

## Data Flow Contracts

### Input Validation
- Task titles must not be empty strings
- Task IDs must exist in the collection for update/delete operations
- User input is sanitized before processing

### Error Handling
- Invalid operations return appropriate error messages
- Application continues running after error conditions
- No unhandled exceptions reach the user