from sqlalchemy.orm import Session

from backend.src.dto.restaurant_dto import RestaurantDto
from backend.src.model.restaurant import Restaurant


def get_restaurants(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Restaurant).offset(skip).limit(limit).all()


def create_user_restaurant(db: Session, restaurant: RestaurantDto, user_id: int):
    db_restaurant = Restaurant(**restaurant.dict(), user_id=user_id)
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant
