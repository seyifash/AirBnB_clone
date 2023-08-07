#!/usr/bin/python3
"""
contains the class Basemodel
"""

from datetime import datetime
import models
import uuid


class BaseModel:
    """The basemodel class which serve as the base for all other class"""

    def __init__(self, *args, **kwargs):
        """initialization of the basemodel attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if "created_at"  in kwargs and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.utcnow()
            if "updated_at"  in kwargs and type(self.created_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                 self.updated_at = datetime.utcnow()
            if  not kwargs.get("id"):
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """returns a string representation of the basemodel atributes"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict)

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """returns a dictionary representation of the keys and values of the instance"""
        my_dict = dict(self.__dict__)
        if "created_at" in my_dict:
            my_dict["created_at"] = my_dict["created_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        if "updated_at" in my_dict:
            my_dict["updated_at"] = my_dict["updated_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        return my_dict
    
