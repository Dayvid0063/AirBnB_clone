#!/usr/bin/python3

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class inherits from BaseModel.

    Public class attributes:
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """

    def __init__(self, *args, **kwargs):
        """Initialize a Review instance."""
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.text = kwargs.get('text', '')

    def to_dict(self):
        """Return a dictionary representation of the Review instance."""
        review_dict = super().to_dict()
        review_dict['place_id'] = self.place_id
        review_dict['user_id'] = self.user_id
        review_dict['text'] = self.text
        return review_dict

    def __str__(self):
        """Return a string representation of the Review instance."""
        return "[{}] {}".format(self.__class__.__name__, self.id, self.__dict__)
