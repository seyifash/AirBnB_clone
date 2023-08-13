#!/usr/bin/python3
"""
contains the filestorage class
"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
allclassname = {'BaseModel': BaseModel, "User": User, "Amenity": Amenity,
                "Place": Place, "Review": Review, "State": State, "City": City}


class FileStorage:
    """the class for serialization and desrialization

    Attributes:
        __file_path (str): The name of the file to subjects to
        __objects (dict): A dictionary of the instances for each objects
    """
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

    def save(self):
        """serializes __objects to the JSON file"""
        our_json = {}
        for key in self.__objects:
            our_json[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(our_json, f)

    def reload(self):
        """deserializes the JSON file to __object"""
        try:
            with open(self.__file_path, 'r') as f:
                loadedfile = json.load(f)
                for key in loadedfile:
                    if "__class__" in loadedfile[key]:
                        obj_name = loadedfile[key]["__class__"]
                        classname = allclassname.get(obj_name)
                    self.__objects[key] = classname(**loadedfile[key])
        except Exception:
            pass
