#!/usr/bin/python3
""" State Module for HBNB project """
from models import city
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel, Base):
    """ State class """

    __table__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete")

    @property
    def cities(self):
        """ represent a relationship with the class City
        """
        from models import  storage
        list_cities = []
        all_cities = storage.all(City)
        for key, value in all_cities:
            list_cities.append(value)
        return list_cities
