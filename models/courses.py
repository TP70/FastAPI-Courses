from typing import Optional
from pydantic import BaseModel


class Course(BaseModel):
    id: int
    name: str
    price: float
    is_early_bird: Optional[bool] = None
