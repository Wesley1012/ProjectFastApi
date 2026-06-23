from pydantic import BaseModel

class Explorer(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str