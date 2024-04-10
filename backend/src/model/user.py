from sqlalchemy import Column, Integer, String, ForeignKey

from backend.src.model.role import *
from backend.src.model.restaurant import *


# Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    phone = Column(String)

    # Define the many-to-one relationship with Role
    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role", back_populates="users")

    # Define the one-to-many relationship with Restaurant
    restaurant = relationship("Restaurant", back_populates="user")

