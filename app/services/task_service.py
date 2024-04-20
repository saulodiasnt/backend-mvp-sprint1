from app.models.task import Task, TaskType
from flask import jsonify
from app.database import db
from app.shared.erros import NotFoundException
from datetime import datetime, date as dateType, time


class TaskService:
    """
    This class provides methods to interact with tasks in the application.
    """

    @staticmethod
    def get_all_user_task(user_id: int):
        """
        Get all tasks for a specific user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            list: A list of Task objects.
        """
        return Task.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_user_task_by_id(task_id: int, user_id: int):
        """
        Get a specific task for a user by its ID.

        Args:
            task_id (int): The ID of the task.
            user_id (int): The ID of the user.

        Returns:
            Task: The Task object if found, None otherwise.
        """
        return Task.query.filter_by(id=task_id, user_id=user_id).first()

    @staticmethod
    def create_user_task(
        title: str,
        description: str,
        user_id: int,
        date: str,
        start_time: str,
        end_time: str,
        type: TaskType,
    ):
        """
        Create a new task for a user.

        Args:
            title (str): The title of the task.
            description (str): The description of the task.
            user_id (int): The ID of the user.
            date (str): The date of the task in the format "YYYY-MM-DD".
            start_time (str): The start time of the task in the format "HH:MM".
            end_time (str): The end time of the task in the format "HH:MM".
            type (TaskType): The type of the task.

        Returns:
            Task: The created Task object.
        """
        task = Task(
            title=title,
            description=description,
            user_id=user_id,
            date=(
                date
                if isinstance(date, dateType)
                else datetime.strptime(date, "%Y-%m-%d").date()
            ),
            start_time=(
                start_time
                if isinstance(start_time, time)
                else datetime.strptime(start_time, "%H:%M").time()
            ),
            end_time=(
                end_time
                if isinstance(end_time, time)
                else datetime.strptime(end_time, "%H:%M").time()
            ),
            type=type,
        )
        db.session.add(task)
        db.session.commit()
        return task

    @staticmethod
    def update_user_task(
        task_id: int,
        user_id: int,
        title: str,
        description: str,
        date: str,
        start_time: str,
        end_time: str,
        type: TaskType,
    ):
        """
        Update an existing task for a user.

        Args:
            task_id (int): The ID of the task.
            user_id (int): The ID of the user.
            title (str): The updated title of the task.
            description (str): The updated description of the task.
            date (str): The updated date of the task in the format "YYYY-MM-DD".
            start_time (str): The updated start time of the task in the format "HH:MM".
            end_time (str): The updated end time of the task in the format "HH:MM".
            type (TaskType): The updated type of the task.

        Returns:
            Task: The updated Task object if found, None otherwise.
        """
        task = Task.query.filter_by(id=task_id, user_id=user_id).first()

        if not task:
            return NotFoundException().to_dict()

        handle_date = (
            datetime.strptime(date, "%Y-%m-%d").date()
            if not isinstance(date, dateType)
            else task.date
        )
        handle_start_time = (
            datetime.strptime(start_time, "%H:%M").time()
            if not isinstance(start_time, time)
            else task.start_time
        )
        handle_end_time = (
            datetime.strptime(end_time, "%H:%M").time()
            if not isinstance(end_time, time)
            else task.end_time
        )

        task.title = title or task.title
        task.description = description or task.description
        task.date = handle_date if date else task.date
        task.start_time = handle_start_time if start_time else task.start_time
        task.end_time = handle_end_time if end_time else task.end_time
        task.type = type.name.upper() if type else task.type.name.upper()

        db.session.add(task)
        db.session.commit()
        return task

    @staticmethod
    def delete_user_task(task_id: int, user_id: int):
        """
        Delete a specific task for a user by its ID.

        Args:
            task_id (int): The ID of the task.
            user_id (int): The ID of the user.

        Returns:
            tuple: An empty response with status code 201 if the task is deleted successfully,
                   or a JSON response with status code 404 if the task is not found.
        """
        task = Task.query.filter_by(id=task_id, user_id=user_id).first()
        if not task:
            return NotFoundException().to_dict()
        db.session.delete(task)
        db.session.commit()
        return jsonify(), 201
