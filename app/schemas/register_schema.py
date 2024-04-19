from pydantic import BaseModel, Field


class RegisterSchema(BaseModel):
    name: str = Field(None, examples="Jonas")
    email: str = Field(None, examples="jonas.mello@gmail.com")
    password: str = Field(None, examples="123456")
