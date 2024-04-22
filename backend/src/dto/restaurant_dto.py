from pydantic import BaseModel


class RestaurantDto(BaseModel):
    name: str
    description: str
