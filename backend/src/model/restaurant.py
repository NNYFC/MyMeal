from sqlalchemy import Column, Integer, String, Table
from backend.src.model.user import *
from backend.src.model.address import *
from backend.src.model.dish import *
from backend.src.model.address import *


# Base = declarative_base()

restaurant_address = Table('restaurant_address',
                           Base.metadata,
                           Column('restaurant_id', Integer, ForeignKey('restaurant.id')),
                           Column('address_id', Integer, ForeignKey('address.id'))
                           )


class Restaurant(Base):
    __tablename__ = "restaurant"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    # Define the many-to-one relationship with User
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="restaurant")
    # Define the many-to-many relationship with Address
    tags = relationship('Address', secondary=restaurant_address, backref='restaurant')
    # Define the one-to-many relationship with Dish
    dish = relationship("Dish", back_populates="restaurant")


