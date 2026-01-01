"""
Todo CLI Application - Main Entry Point

This is the main entry point for the Phase I In-Memory Todo Console Application.
It initializes the CLI interface and starts the application loop.
"""

from cli import TodoCLI
from services import TaskManager


def main():
    """Main function to start the Todo CLI application."""
    print("Welcome to the Todo CLI Application!")
    print("Initializing application...")

    # Initialize the task manager (handles all task operations)
    task_manager = TaskManager()

    # Initialize the CLI interface
    cli = TodoCLI(task_manager)

    # Start the CLI application
    cli.run()


if __name__ == "__main__":
    main()