from sqlalchemy import Boolean, DateTime

from backend.src.model.dish import *
from backend.src.model.user import *


class Command(Base):
    __tablename__ = "command"
    id = Column(Integer, primary_key=True)
    ref = Column(String)
    quantity = Column(Integer)
    status = Column(Boolean)
    date = Column(DateTime)

    # Define the many-to-one relationship with User
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="command")
    # Define the many-to-one relationship with Dish
    dish_id = Column(Integer, ForeignKey("dish.id"))
    dish = relationship("Dish", back_populates="command")

