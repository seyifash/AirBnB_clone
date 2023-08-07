#!/usr/bin/python3
"""
contains the filestorage class
"""
import json


class FileStorage:
    """the calss for serialization and desrialization"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __object the obj with key <obj classname>id"""
        if obj is not None:
            my_key = obj.__class__.__name__ + "." + obj.id
            self.__objects[my_key] = obj

    def all_classnames(self):
        from models.base_model import BaseModel

        classes = {
            'BaseModel' : BaseModel
        }
        return classes

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
                allclass = self.all_classnames()
                self.__objects[key] = allclass[theclass](**value)
        except Exception:
            pass
