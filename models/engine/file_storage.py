#!/usr/bin/python3
"""
contains the filestorage class
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """the calss for serialization and desrialization"""
    __file_path = "file.json"
    __objects = {}
    all_classnames = {'BaseModel': BaseModel, 'User': User}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __object the obj with key <obj classname>id"""
        if obj is not None:
            my_key = obj.__class__.__name__ + "." + obj.id
            self.__objects[my_key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        our_json = {}
        for key in self.__objects:
            our_json[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(our_json, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                loadedfile = json.load(f)
            for key, value in loadedfile.items():
                theclass, obj_id = key.split('.')
                classname =  self.all_classnames.get(theclass)
                self.__objects[key] = theclass(**value)
        except:
            pass

