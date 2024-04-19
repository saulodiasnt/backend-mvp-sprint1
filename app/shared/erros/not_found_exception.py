from pydantic import Field
from .exception import Exception


class NotFoundException(Exception):
    code: int = Field(404, description="Status code")
    message: str = Field("Not Found", description="Error message")

    def __init__(self, message: str = "Not Found"):
        super().__init__(message=message, code=404)
