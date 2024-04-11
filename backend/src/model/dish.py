from sqlalchemy.orm import relationship

from backend.src.model.restaurant import *
from backend.src.model.command import *


class Dish(Base):
    __tablename__ = "dish"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    # Define the many-to-one relationship with User
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    restaurant = relationship("Restaurant", back_populates="dish")
    # Define the one-to-many relationship with Command
    command = relationship("Command", back_populates="dish")
