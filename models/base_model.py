#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Attributes: Date format used for date string conversion"""
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel"""
        if kwargs:
            self.id = kwargs.get('id', str(uuid.uuid4()))
            self.created_at = kwargs.get('created_at', datetime.now())
            self.updated_at = kwargs.get('updated_at', datetime.now())
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, self.DATE_FORMAT)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, str(self.__dict__))

    def save(self):
        """Updates the attribute and saves the instance to storage"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel instance"""
        res_dict = self.__dict__.copy()
        res_dict['__class__'] = type(self).__name__
        res_dict['created_at'] = self.created_at.isoformat()
        res_dict['updated_at'] = self.updated_at.isoformat()
        return res_dict
