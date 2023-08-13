#!/usr/bin/python3
"""Defines a file storage class"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:

    """A file storage class"""

    __file_path = "file.json"
    __objects = {}
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Place': Place,
        'Amenity': Amenity,
        'Review': Review
    }

    def all(self):
        """Returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """Set the object in __objects with the appropriate key"""

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file"""

        serial = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(serial, file)

    def reload(self):
        """Deserialize the JSON file to __objects if it exists"""
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                data = json.load(f)
                for k, v in data.items():
                    result = k.split('.')
                    class_name = result[0]
                    class_obj = FileStorage.__classes[class_name]
                    FileStorage.__objects[k] = class_obj(**v)
        except FileNotFoundError:
            pass
