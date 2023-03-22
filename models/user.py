#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel):
    """This class defines a user by 
    Attributes:
        email: email address to get in touch
        password: login detail
        firstName, lastName
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    place = relationship("Place", cascade="all, delete, delete-orphans", backref="user")
    reviews = relationship("Review", cascade="all, delete, delete-orphans", backref="user")
