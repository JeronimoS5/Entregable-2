from pydantic import BaseModel, Field
import re

class Pet(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    age: int = Field(..., gt=0)
    breed: str = Field(..., min_length=1)
    gender: str = Field(..., pattern="^(M|H)$")
    location: str = Field(..., min_length=1)

    def __init__(self, **data):
        super().__init__(**data)
        if not re.match("^[A-Za-z ]+$", self.name):
            raise ValueError("El nombre solo puede contener letras y espacios")
