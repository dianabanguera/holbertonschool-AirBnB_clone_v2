#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models


HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if HBNB_TYPE_STORAGE == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")

    else:
        name = ""

    @property
    def cities(self):
        """
        Getter attribute that returns the list of City
        instances with state_id equals to the current State.id
        """
        result = []
        cities = models.storage.all(City)
        for city in cities.values():
            if self.id == city.state_id:
                result.append(city)
        return(result)
