from pydantic import BaseModel, Field


class LoginSchema(BaseModel):
    email: str = Field(None, examples="jonas.mello@gmail.com")
    password: str = Field(None, examples="123456")
