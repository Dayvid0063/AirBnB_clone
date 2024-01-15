#!/usr/bin/python3

from models.base_model import BaseModel

class Place(BaseModel):
    """
    Place class inherits from BaseModel.

    Public class attributes:
    city_id: string - empty string: it will be the City.id
    user_id: string - empty string: it will be the User.id
    name: string - empty string
    description: string - empty string
    number_rooms: integer - 0
    number_bathrooms: integer - 0
    max_guest: integer - 0
    price_by_night: integer - 0
    latitude: float - 0.0
    longitude: float - 0.0
    amenity_ids: list of string - empty list: it will be the list of Amenity.id later
    """

    def __init__(self, *args, **kwargs):
        """Initialize a Place instance."""
        super().__init__(*args, **kwargs)
        self.city_id = kwargs.get('city_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.name = kwargs.get('name', '')
        self.description = kwargs.get('description', '')
        self.number_rooms = kwargs.get('number_rooms', 0)
        self.number_bathrooms = kwargs.get('number_bathrooms', 0)
        self.max_guest = kwargs.get('max_guest', 0)
        self.price_by_night = kwargs.get('price_by_night', 0)
        self.latitude = kwargs.get('latitude', 0.0)
        self.longitude = kwargs.get('longitude', 0.0)
        self.amenity_ids = kwargs.get('amenity_ids', [])

    def to_dict(self):
        """Return a dictionary representation of the Place instance."""
        place_dict = super().to_dict()
        place_dict['city_id'] = self.city_id
        place_dict['user_id'] = self.user_id
        place_dict['name'] = self.name
        place_dict['description'] = self.description
        place_dict['number_rooms'] = self.number_rooms
        place_dict['number_bathrooms'] = self.number_bathrooms
        place_dict['max_guest'] = self.max_guest
        place_dict['price_by_night'] = self.price_by_night
        place_dict['latitude'] = self.latitude
        place_dict['longitude'] = self.longitude
        place_dict['amenity_ids'] = self.amenity_ids
        return place_dict

    def __str__(self):
        """Return a string representation of the Place instance."""
        return "[{}] {}".format(self.__class__.__name__, self.id, self.__dict__)
