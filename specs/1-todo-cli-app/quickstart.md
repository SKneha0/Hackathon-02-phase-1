# Quickstart Guide: Phase I – In-Memory Todo Python Console Application

**Feature**: 1-todo-cli-app | **Date**: 2026-01-02 | **Plan**: [plan.md](./plan.md)

## Getting Started

### Prerequisites
- Python 3.13 or higher
- UV package manager (if using external dependencies)

### Setup
1. Clone or create the project directory
2. Create the `src` directory structure:
   ```
   src/
   ├── main.py
   ├── models.py
   ├── services.py
   └── cli.py
   ```
3. Ensure Python environment is properly configured

### Running the Application
1. Navigate to the project root directory
2. Execute: `python src/main.py`
3. The menu-driven interface will start, showing available options

## Basic Usage

### Main Menu Options
1. **Add Task**: Creates a new task with title and optional description
2. **View Tasks**: Displays all tasks with ID, title, and completion status
3. **Update Task**: Modifies an existing task's title or description
4. **Delete Task**: Removes a task by its ID
5. **Mark Complete/Incomplete**: Toggles the completion status of a task
6. **Exit**: Closes the application (all data will be lost)

### Example Workflow
1. Run `python src/main.py`
2. Select "Add Task" and enter a title (e.g., "Buy groceries")
3. Optionally add a description (e.g., "Milk, bread, eggs")
4. Select "View Tasks" to see your task list
5. Use other options to manage your tasks as needed

## Important Notes
- All data is stored in memory only and will be lost when the application closes
- Task IDs are auto-generated as sequential integers starting from 1
- Invalid task IDs will result in error messages rather than application crashes
- The application is designed for single-user operation