from pydantic import BaseModel, Field
from typing import Optional

class Explorer(BaseModel):
    name: str
    country: str = Field(default="", description="Страна")
    description: str = Field(default="", min_length=0)
