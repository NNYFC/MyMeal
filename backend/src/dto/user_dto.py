from typing import List

from pydantic import BaseModel

from backend.src.dto.restaurant_dto import RestaurantDto
from backend.src.dto.role_dto import RoleDto


class UserDto(BaseModel):
    firstname: str
    lastname: str
    email: str
    phone: str
    role_id: int


class User(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: bytes
    phone: str
    role_id: RoleDto | None = None
    restaurant: List[RestaurantDto] | None = None


