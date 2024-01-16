#!/usr/bin/python3


from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inherited from base model

    Public class attributes:
    state_id: string - empty string: it will be the State.id
    name: string - empty string
    """
    state_id = ""
    name = ""
