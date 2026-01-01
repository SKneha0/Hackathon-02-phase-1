"""
Todo CLI Application - Task Management Services

This module contains the TaskManager class that handles all task operations
including adding, updating, deleting, and marking tasks complete/incomplete.
"""

from typing import List, Optional
from models import Task


class TaskManager:
    """
    Manages all task operations including adding, updating, deleting, and viewing tasks.
    All data is stored in memory only and resets when the application restarts.
    """

    def __init__(self):
        """Initialize the TaskManager with an empty task list and ID counter."""
        self.tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> int:
        """
        Add a new task with the given title and optional description.

        Args:
            title (str): The task title (required)
            description (str): The task description (optional)

        Returns:
            int: The ID of the newly created task

        Raises:
            ValueError: If title is empty
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        # Create new task with the next available ID
        task = Task(id=self._next_id, title=title, description=description)
        self.tasks.append(task)

        # Increment the ID counter for the next task
        task_id = self._next_id
        self._next_id += 1

        return task_id

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the collection.

        Returns:
            List[Task]: A list of all tasks
        """
        return self.tasks.copy()  # Return a copy to prevent external modification

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update an existing task's title or description.

        Args:
            task_id (int): The ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task

        Returns:
            bool: True if the task was updated, False if task ID not found
        """
        task = self._find_task_by_id(task_id)
        if task is None:
            return False

        # Update title if provided
        if title is not None:
            if not title or not title.strip():
                raise ValueError("Task title cannot be empty")
            task.title = title.strip()

        # Update description if provided
        if description is not None:
            task.description = description.strip() if description else ""

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if task ID not found
        """
        task = self._find_task_by_id(task_id)
        if task is None:
            return False

        self.tasks.remove(task)
        return True

    def mark_task_completed(self, task_id: int, completed: bool) -> bool:
        """
        Mark a task as complete or incomplete.

        Args:
            task_id (int): The ID of the task to update
            completed (bool): Whether the task should be marked as completed

        Returns:
            bool: True if the task was updated, False if task ID not found
        """
        task = self._find_task_by_id(task_id)
        if task is None:
            return False

        task.completed = completed
        return True

    def _find_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Find a task by its ID.

        Args:
            task_id (int): The ID of the task to find

        Returns:
            Task or None: The task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None