#!/usr/bin/python3
""" This script defines a class DBStorage """
from models.base_model import Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """ This class defines attributes and methods """
    __engine = None
    __session = None
    clases_objects = [User, State, City, Amenity, Place, Review]

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}\
'.format(environ['HBNB_MYSQL_USER'], environ['HBNB_MYSQL_PWD\
'], environ['HBNB_MYSQL_HOST'], environ['HBNB_MYSQL_DB'], pool_pre_ping=True))
        if 'HBNB_ENV' in environ and environ['HBNB_ENV'] == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ This method returns all objects depending of the class name """
        result = {}

        if cls:
            for item in self.__session.query(cls).all():
                result[item.__class__.__name__ + '.' + item.id] = item
        else:
            for clase_in in self.clases_objects:
                for item in self.__session.query(clase_in).all():
                    result[item.__class__.__name__ + '.' + item.id] = item

        return result

    def new(self, obj):
        """ This method adds the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ This method commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ This method deletes from the current
            database session obj if not None """
        item = self.__session.query(obj['__class__']).filter(obj['name']).one()
        item
        self.__session.delete(item)

    def reload(self):
        """ This method creates all tables in the database
            and creates the current database session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
