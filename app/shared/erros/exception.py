from pydantic import BaseModel
from flask import jsonify


class Exception(BaseModel):
    code: int
    message: str

    def __init__(self, message: str, code: int):
        super().__init__()
        self.message = message
        self.code = code

    def to_dict(self):
        return jsonify(self.model_dump()), self.code
