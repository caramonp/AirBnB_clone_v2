#!/usr/bin/python3
""" DB Storage for HBNB Project """
from models import base_model
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


class DBStorage:

    """DB Storage class"""
    __engine = None
    __session = None
    classes = {User, City, Place, State, Amenity, Review}

    def __init__(self):
<<<<<<< HEAD
            self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'\
            .format(environ['HBNB_MYSQL_USER'],
            environ['HBNB_MYSQL_PWD'],
            environ['HBNB_MYSQL_HOST'],
            environ['HBNB_MYSQL_DB'], pool_pre_ping=True))
<<<<<<< HEAD
          
=======

>>>>>>> 4f6d9b4ddc06603c3d7a85c50d65b6a3244f532f
            if 'HBNB_ENV' in environ and environ['HBNB_ENV'] == 'test':
              Base.metadata.drop_all(self.__engine)
=======
        """init"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(environ['HBNB_MYSQL_USER'],
                                              environ['HBNB_MYSQL_PWD'],
                                              environ['HBNB_MYSQL_HOST'],
                                              environ['HBNB_MYSQL_DB'],
                                              pool_pre_ping=True))
>>>>>>> 42a4a9393c77d195a51391df6e4d4a83ae5fae04

        if 'HBNB_ENV' in environ and environ['HBNB_ENV'] == 'test':
                Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """list to all"""

        list_result = {}
        if cls:
                for item in self.__session.query(cls).all():
                    list_result[item.__class__.__name__ + '.' + item.id] = item
        else:
            for clase_in in self.classes:
                for item in self.__session.query(clase_in).all():
                    list_result[item.__class__.__name__ + '.' + item.id] = item

        return list_result

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):

        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)

        Session = scoped_session(session_maker)
        self.__session = Session()
