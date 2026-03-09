from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Define schema model with Pydantic
# TODO: make "id" and "created_at" automatically generated in POST route
class Thing(BaseModel):
    id: int
    name: str
    created_at: datetime
    price: Optional[float] = None
    description: Optional[str] = None
    is_true: Optional[bool] = None
    updated_at: Optional[datetime] = None


# Define response (minimised / sanitised) model for Thing
# TODO: review sanitisation for output object
class ThingOut(BaseModel):
    id: int
    name: str
    description: Optional[str] = None