#!/usr/bin/python3
"""
contains the class Basemodel
"""

from datetime import datetime
import models
import uuid


time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """The basemodel class which serve as the base for all other class"""

    def __init__(self, *args, **kwargs):
        """initialization of the basemodel attributes"""
        if kwargs:
            kwargs.pop('__class__', None)
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, time))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        """returns a string representation of the basemodel atributes"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary representation of the instance"""
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = self.__class__.__name__
        if "created_at" in my_dict:
            my_dict["created_at"] = my_dict["created_at"].isoformat()
        if "updated_at" in my_dict:
            my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
