#!/usr/bin/python3
from os import getenv
from models.base_model import BaseModel
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

class DBStorage:
    """ Represents a database storage engine"""

    __engine = None
    __session = None

    def __init__(self):
        """ initalize a new datastorage"""
        self.engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                    format(getenv("HBNB_MYSQL_USER"),
                                            getenv("HBNB_MYSQL_PWD"),
                                            getenv("HBNB_MYSQL_HOST"),
                                            getenv("HBNB_MYSQL_DB")),
                                    pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session depending on the class """
        
        if cls is None:
            my_obj = self.__session.query(State).all()
            my_obj.extend(self.__sesion.query(City).all())
            my_obj.extend(self.__sesion.query(User).all())
            my_obj.extend(self.__sesion.query(Place).all())
            my_obj.extend(self.__sesion.query(Review).all())
            my_obj.extend(self.__sesion.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            my_obj = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in my_obj }

    def new(self, obj):
        """ add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session """
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()



