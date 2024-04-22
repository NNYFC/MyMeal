from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from backend.src.model.restaurant import *

Base = declarative_base()


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    location = Column(String)
