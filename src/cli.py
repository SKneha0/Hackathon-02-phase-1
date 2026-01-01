"""
Todo CLI Application - Command Line Interface

This module contains the TodoCLI class that handles user interaction
through a menu-driven command line interface.
"""

from typing import Optional
from services import TaskManager


class TodoCLI:
    """
    Handles the command line interface for the todo application.
    Provides a menu-driven interface for users to interact with their tasks.
    """

    def __init__(self, task_manager: TaskManager):
        """
        Initialize the CLI interface with a task manager.

        Args:
            task_manager (TaskManager): The task manager instance to use
        """
        self.task_manager = task_manager

    def run(self):
        """Start the main menu loop and handle user interaction."""
        print("Todo CLI Application Started!")
        print("=" * 40)

        while True:
            self._display_menu()
            choice = input("\nEnter your choice (1-6): ").strip()

            if choice == "1":
                self._add_task()
            elif choice == "2":
                self._view_tasks()
            elif choice == "3":
                self._update_task()
            elif choice == "4":
                self._delete_task()
            elif choice == "5":
                self._mark_task()
            elif choice == "6":
                print("Thank you for using Todo CLI. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1-6.")

    def _display_menu(self):
        """Display the main menu options to the user."""
        print("\n" + "=" * 40)
        print("TODO CLI APPLICATION")
        print("=" * 40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("6. Exit")
        print("=" * 40)

    def _add_task(self):
        """Handle adding a new task."""
        print("\n--- Add New Task ---")

        try:
            title = input("Enter task title: ").strip()
            if not title:
                print("Error: Task title cannot be empty.")
                return

            description = input("Enter task description (optional, press Enter to skip): ").strip()

            task_id = self.task_manager.add_task(title, description)
            print(f"Task added successfully with ID: {task_id}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def _view_tasks(self):
        """Handle viewing all tasks."""
        print("\n--- View All Tasks ---")

        tasks = self.task_manager.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return

        print(f"Found {len(tasks)} task(s):")
        for task in tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"  {task} - {status}")
            if task.description:
                print(f"    Description: {task.description}")

    def _update_task(self):
        """Handle updating an existing task."""
        print("\n--- Update Task ---")

        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
            return

        # Check if task exists
        tasks = self.task_manager.get_all_tasks()
        task = None
        for t in tasks:
            if t.id == task_id:
                task = t
                break

        if task is None:
            print(f"Error: Task with ID {task_id} not found.")
            return

        print(f"Current task: {task}")
        if task.description:
            print(f"Current description: {task.description}")

        new_title = input(f"Enter new title (current: '{task.title}', press Enter to keep current): ").strip()
        new_description = input(f"Enter new description (current: '{task.description}', press Enter to keep current): ").strip()

        # Prepare update parameters
        title_update = new_title if new_title else None
        description_update = new_description if new_description else None

        # If user pressed Enter for both, don't make any changes
        if title_update is None and description_update == "":
            description_update = task.description  # Keep the original description

        try:
            success = self.task_manager.update_task(
                task_id,
                title=title_update,
                description=description_update if description_update != task.description else None
            )

            if success:
                print("Task updated successfully.")
            else:
                print("Failed to update task.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def _delete_task(self):
        """Handle deleting a task."""
        print("\n--- Delete Task ---")

        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
            return

        success = self.task_manager.delete_task(task_id)

        if success:
            print(f"Task with ID {task_id} deleted successfully.")
        else:
            print(f"Error: Task with ID {task_id} not found.")

    def _mark_task(self):
        """Handle marking a task as complete or incomplete."""
        print("\n--- Mark Task Complete/Incomplete ---")

        try:
            task_id = int(input("Enter task ID to mark: "))
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
            return

        # Check current status
        tasks = self.task_manager.get_all_tasks()
        task = None
        for t in tasks:
            if t.id == task_id:
                task = t
                break

        if task is None:
            print(f"Error: Task with ID {task_id} not found.")
            return

        print(f"Current task: {task}")
        print(f"Current status: {'Completed' if task.completed else 'Pending'}")

        while True:
            choice = input("Enter 'c' for complete, 'i' for incomplete: ").strip().lower()
            if choice == 'c':
                success = self.task_manager.mark_task_completed(task_id, True)
                if success:
                    print("Task marked as complete.")
                else:
                    print("Failed to mark task as complete.")
                break
            elif choice == 'i':
                success = self.task_manager.mark_task_completed(task_id, False)
                if success:
                    print("Task marked as incomplete.")
                else:
                    print("Failed to mark task as incomplete.")
                break
            else:
                print("Invalid choice. Please enter 'c' for complete or 'i' for incomplete.")