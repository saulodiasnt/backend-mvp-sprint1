from pydantic import BaseModel, Field
from typing import Optional
from app.models.task import TaskType
from datetime import time, date as d


class CreateTaskSchema(BaseModel):
    title: str = Field(None, examples="Study Python")
    description: Optional[str] = Field(None, examples="Study Python for 1 hour")
    date: d = Field(None, examples="2021-01-01")
    start_time: time = Field(None, examples="12:00")
    end_time: time = Field(None, examples="13:00")
    type: Optional[TaskType] = Field(None, examples="study")
