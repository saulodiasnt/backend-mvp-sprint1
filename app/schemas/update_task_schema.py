from pydantic import BaseModel, Field
from typing import Optional
from app.models.task import TaskType
from datetime import time, date as d


class UpdateTaskSchema(BaseModel):
    title: Optional[str] = Field(None, examples="Study Python")
    description: Optional[str] = Field(None, examples="Study Python for 1 hour")
    date: Optional[d] = Field(None, examples="2021-01-01")
    start_time: Optional[time] = Field(None, examples="12:00")
    end_time: Optional[time] = Field(None, examples="13:00")
    type: Optional[TaskType] = Field(None, examples=TaskType.STUDY)
