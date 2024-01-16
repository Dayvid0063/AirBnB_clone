#!/usr/bin/python3
"""
FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""


import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Attributes:
    __file_path (str): Path to the JSON file.
    __objects (dict): Dictionary to store all objects by <class name>.id.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the __objects dictionary."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (__file_path)."""
        obj_dict = {}
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
        except FileNotFoundError:
            pass

        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)

            for key, m in obj_dict.items():
                class_name = m["__class__"]
                del m["__class__"]

                try:
                    cls = eval(class_name)
                except NameError:
                    cls = None

                if cls:
                    FileStorage.__objects[key] = cls(**m)
