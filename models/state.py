#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel):
    """ State class """

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        name = ""

        @property
        def cities(self):
            """ return the list of city inctance"""

            cities_list = []
            for city in models.storage.all("City").values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return(cities_list)
