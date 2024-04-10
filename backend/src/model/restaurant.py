from sqlalchemy import Column, Integer, String
from backend.src.model.user import *


# Base = declarative_base()


class Restaurant(Base):
    __tablename__ = "restaurant"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    # Define the many-to-one relationship with User
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="restaurant")
