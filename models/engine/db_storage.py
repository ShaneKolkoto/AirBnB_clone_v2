#!/usr/bin/python3
"""Database storage engine using SQLAlchemy with a mysql+mysqldb database connection."""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    """DB Storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the object"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_MYSQL_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, db), pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """returns a dictionary of all the objects present"""
        objects = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for request in query:
                key = "{}.{}".format(type(request).__name__, request.id)
                objects[key] = request
            else:
                schema_list = [State, City, User, Place, Review, Amenity]
                for class_name in schema_list:
                    query = self.__session.query(class_name)
                    for request in query:
                        key = "{}.{}".format(type(request).__name__, request.id)
                        objects[key] = request
            return objects
    def new(self, obj):
        """creates a new object"""
        self.__session.add(obj)
    
    def save(self):
        """saves the current session"""
        self.__session.commit()
    
    def delete(self,obj=None):
        """deletes an object"""
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """reloads objects from the database"""
        Base.metadata.create_all(self.__engine)
        config = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(config)
        self.__session = session()
    