# Phase I – In-Memory Todo Python Console Application

This is a simple command-line todo application that allows users to manage tasks without persistence. All data is stored in memory only and resets when the application closes.

## Features

- Add new tasks with title and optional description
- View all tasks with ID, title, description, and completion status
- Update existing tasks (title and/or description)
- Delete tasks by ID
- Mark tasks as complete or incomplete
- Clean, menu-driven command-line interface
- Comprehensive error handling and input validation

## Requirements

- Python 3.13 or higher

## How to Run

1. Clone or download this repository
2. Navigate to the project directory
3. Run the application:

```bash
python src/main.py
```

4. Follow the on-screen menu prompts to interact with your tasks

## Menu Options

1. **Add Task** - Create a new task with title and optional description
2. **View Tasks** - Display all tasks with their status and details
3. **Update Task** - Modify an existing task's title or description
4. **Delete Task** - Remove a task by its ID
5. **Mark Task Complete/Incomplete** - Change a task's completion status
6. **Exit** - Close the application

## Architecture

The application follows a clean, modular architecture:

- `src/main.py` - Application entry point
- `src/models.py` - Task data model
- `src/services.py` - Task management business logic
- `src/cli.py` - Command-line interface

## Constraints

- All data is stored in memory only (no persistence)
- Single-user application
- Reset on application restart
- No external dependencies beyond Python standard library