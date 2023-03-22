#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel , Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel,Base):
    """ The city class, contains attributes state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("places", cascade="all, delete, delete-orphans", backref="cities")
