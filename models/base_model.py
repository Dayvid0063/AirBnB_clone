#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """Attributes: Date format used for date string conversion"""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel
           Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    self.__dict__[key] = datetime.strptime(value, DATE_FORMAT)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the BaseModel instance"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    def save(self):
        """Updates the attribute and saves the instance to storage"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel instance"""
        res_dict = self.__dict__.copy()
        res_dict['__class__'] = type(self).__name__
        res_dict['created_at'] = self.created_at.isoformat()
        res_dict['updated_at'] = self.updated_at.isoformat()
        return res_dict
