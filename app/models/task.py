from enum import Enum
import datetime
from app.database import db


class TaskType(Enum):
    """
    Represents the types of tasks.

    Attributes:
        LEISURE (str): Represents a leisure task.
        WORK (str): Represents a work task.
        STUDY (str): Represents a study task.
        REST (str): Represents a rest task.
        OTHER (str): Represents any other type of task.
    """

    LEISURE = "leisure"
    WORK = "work"
    STUDY = "study"
    REST = "rest"
    OTHER = "other"


class Task(db.Model):
    """
    Represents a task in the application.

    Attributes:
        id (int): The unique identifier for the task.
        title (str): The title of the task.
        description (str): The description of the task.
        type (TaskType): The type of the task.
        user_id (int): The ID of the user associated with the task.
        date (Date): The date of the task.
        start_time (Time): The start time of the task.
        end_time (Time): The end time of the task.
        created_at (DateTime): The timestamp when the task was created.
        updated_at (DateTime): The timestamp when the task was last updated.
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    type = db.Column(db.Enum(TaskType), nullable=False, default=TaskType.OTHER)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )

    def __repr__(self):
        return f"<Task {self.title}>"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "type": self.type.value,
            "user_id": self.user_id,
            "date": self.date.strftime("%Y-%m-%d"),
            "start_time": self.start_time.strftime("%H:%M"),
            "end_time": self.end_time.strftime("%H:%M"),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
