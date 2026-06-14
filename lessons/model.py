from pydantic import BaseModel, constr, Field

class Creature(BaseModel):
    name: constr(min_length=2)
    country: str = Field(..., min_length=2) # ... - значение обязательное и значения по умолчанию нет
    area: str
    description: str
    aka: str

# thing = Creature(
#     name='yeti',
#     country='CN',
#     area='Himalayas',
#     description='Hirsute Himalayan',
#     aka='Abominable Snowman'
# )



