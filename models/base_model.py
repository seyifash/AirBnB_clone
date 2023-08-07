#!/usr/bin/python3
"""
contains the class Basemodel
"""

from datetime import datetime as dt
import models
import uuid
from models import storage


class BaseModel:
    """The basemodel class which serve as the base for all other class"""

    def __init__(self, *args, **kwargs):
        """initialization of the basemodel attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if "created_at" in kwargs and type(self.created_at) is str:
                ct = dt.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                self.created_at = ct
            else:
                self.created_at = dt.utcnow()
            if "updated_at" in kwargs and type(self.created_at) is str:
                nt = dt.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                self.updated_at = nt
            else:
                self.updated_at = dt.utcnow()
            if not kwargs.get("id"):
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.utcnow()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """returns a string representation of the basemodel atributes"""
        string_fmt = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return string_fmt

    def save(self):
        self.updated_at = dt.utcnow()
        storage.save()

    def to_dict(self):
        """returns a dictionary representation of the
        keys and values of the instance"""
        my_dict = dict(self.__dict__)
        if "created_at" in my_dict:
            my_dict["created_at"] = my_dict["created_at"].isoformat()
        if "updated_at" in my_dict:
            my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
