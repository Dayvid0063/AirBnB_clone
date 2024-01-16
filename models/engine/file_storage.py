#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    """
    This class provides methods for serializing instances to a JSON file
    and deserializing a JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary to store all objects by <class name>.id.
    """
    __file_path = "file.json"
    __objects = {}

    @classmethod
    def _import_all_model_classes(cls):
        """
        Dynamically import model classes.
        """
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

    def all(self):
        """
        Returns the dictionary of all objects.

        Returns:
            dict: Dictionary of all objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary.

        Args:
            obj (BaseModel): The object to be added.
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        ser_dict = FileStorage.__objects
        obj_dict = {obj: ser_dict[obj].to_dict() for obj in ser_dict.keys()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects.
        If the JSON file (__file_path) exists, loads the data and creates
        instances of the corresponding classes. Otherwise, does nothing.
        """
        self._import_all_model_classes()
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for obj_id in obj_dict.values():
                    class_name = obj_id["__class__"]
                    del obj_id["__class__"]
                    self.new(eval(class_name)(**obj_id))
        except FileNotFoundError:
            return
