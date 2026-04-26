from pydantic import BaseModel, Field

class UserInput(BaseModel):
    user_name: str = Field(...,  min_length=3, max_length=50)
    age: int = Field(..., gt=0, lt=150)
    uf: str