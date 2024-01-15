#!/usr/bin/python3


from models.base_model import BaseModel

class City(BaseModel):
    """
    City class inherited from base model
    
    Public class attributes:
    state_id: string - empty string: it will be the State.id
    name: string - empty string
    """
    def __init__(self, *args, **kwargs):
        """Initialize a new city instance"""
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', '')
        self.name = kwargs.get('name', '')
        
    def to_dict(self):
        """Return a dict representation of the city instance"""
        city_dict = super().to_dict()
        city_dict['state_id'] = self.state_id
        city_dict['name'] = self.name
        return city_dict
        
    def __str__(self):
        """Return a string representation of the city instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)