#!/usr/bin/python3


from models.base_model import BaseModel

class State(BaseModel):
    """
    State class inherits from BaseModel.
    
    Public class attributes:
    name: string - empty string
    """
    
    def __init__(self, *args, **kwargs ):
        """Initialize a State instance"""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
        
    def to_dict(self):
        """Return a dict representation of the State instance"""
        state_dict = super().to_dict()
        state_dict['name'] = self.name
        return state_dict
    
    def __str__(self):
        """Return a string representation of the State instance"""
        return "[{}] {}".format(self.__class__.__name__, self.id, self.__dict__)
    