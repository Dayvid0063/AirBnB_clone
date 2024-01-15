#!/usr/bin/python3


from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity class inherits from BaseModel.
    
    Public class attributes:
    name: string - empty string
    """
    
    def __init__(self, *args, **kwargs ):
        """Initialize a Amenity instance"""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
        
    def to_dict(self):
        """Return a dict representation of the Amenity instance"""
        amenity_dict = super().to_dict()
        amenity_dict['name'] = self.name
        return amenity_dict
    
    def __str__(self):
        """Return a string representation of the Amenity instance"""
        return "[{}] {}".format(self.__class__.__name__, self.id, self.__dict__)
    