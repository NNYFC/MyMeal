from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Table
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    # Define the one-to-many relationship with User
    users = relationship("User", back_populates="role")


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
    # Define the one-to-many relationship with Command
    command = relationship("Command", back_populates="user")


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    location = Column(String)


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
    # tags = relationship('Address', secondary=restaurant_address, backref='restaurant')
    # Define the one-to-many relationship with Dish
    dish = relationship("Dish", back_populates="restaurant")


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

