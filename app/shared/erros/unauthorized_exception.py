from pydantic import Field
from .exception import Exception


class UnauthorizedException(Exception):
    message: str = Field("Unauthorized", description="Error message")
    code: int = Field(401, description="Status code")

    def __init__(self, message: str = "Unauthorized"):
        super().__init__(message=message, code=401)
