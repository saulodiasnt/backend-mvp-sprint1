from pydantic import BaseModel, Field


class TaskResponseSchema(BaseModel):
    id: int = Field(..., description="The unique identifier for the task")
    title: str = Field(..., description="The title of the task")
    description: str = Field(..., description="The description of the task")
    type: str = Field(..., description="The type of the task")
    date: str = Field(..., description="The date of the task")
    start_time: str = Field(..., description="The start time of the task")
    end_time: str = Field(..., description="The end time of the task")
    created_at: str = Field(..., description="The timestamp when the task was created")
    updated_at: str = Field(
        ..., description="The timestamp when the task was last updated"
    )
