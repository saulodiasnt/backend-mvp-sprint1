from pydantic import BaseModel, Field


class TaskPathSchema(BaseModel):
    task_id: int = Field(int, alias="task_id", description="Task ID", example=1)
