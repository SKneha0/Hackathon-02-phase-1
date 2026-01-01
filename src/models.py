"""
Todo CLI Application - Data Models

This module contains the data models for the todo application,
including the Task class that represents a single todo item.
"""


class Task:
    """
    Represents a single todo item with properties that define its state and identity.

    Attributes:
        id (int): Unique identifier for the task
        title (str): Required text that describes the task
        description (str): Optional additional details about the task
        completed (bool): Status indicator, defaults to False
    """

    def __init__(self, id: int, title: str, description: str = "", completed: bool = False):
        """
        Initialize a new Task instance.

        Args:
            id (int): Unique identifier for the task
            title (str): Required text that describes the task
            description (str): Optional additional details about the task
            completed (bool): Status indicator, defaults to False

        Raises:
            ValueError: If title is empty
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        self.id = id
        self.title = title.strip()
        self.description = description.strip() if description else ""
        self.completed = completed

    def __str__(self):
        """Return a string representation of the task."""
        status = "X" if self.completed else "O"
        return f"[{status}] {self.id}. {self.title}"

    def __repr__(self):
        """Return a detailed string representation of the task."""
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed})"