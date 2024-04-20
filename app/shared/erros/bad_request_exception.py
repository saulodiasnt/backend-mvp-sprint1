from pydantic import Field
from .exception import Exception


class BadRequestException(Exception):
    code: int = Field(400, description="Status code")
    message: str = Field("Bad Request", description="Error message")

    def __init__(self, message="Bad Request"):
        super().__init__(message)
        self.message = message
