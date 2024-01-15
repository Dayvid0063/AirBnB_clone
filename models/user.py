#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    """
    User class inherits from BaseModel.

    Public class attributes:
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """
    def __init__(self, *args, **kwargs):
        """Initialize User instance."""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')

    def to_dict(self):
        """Return a dictionary representation of the User instance."""
        user_dict = super().to_dict()
        user_dict['email'] = self.email
        user_dict['password'] = self.password
        user_dict['first_name'] = self.first_name
        user_dict['last_name'] = self.last_name
        return user_dict

    def __str__(self):
        """Return a string representation of the User instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)