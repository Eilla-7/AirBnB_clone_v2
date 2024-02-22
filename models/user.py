# #!/usr/bin/python3
# """This module defines a class User"""
# from models.base_model import BaseModel


# class User(BaseModel):
#     """This class defines a user by various attributes"""
#     email = ''
#     password = ''
#     first_name = ''
#     last_name = ''

#!/usr/bin/python3
""" User Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """ User class """
    __tablename__ = 'users'
    
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
