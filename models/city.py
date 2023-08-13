#!/usr/bin/python3

"""Defines a child class that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """A city state"""

    state_id = ""
    name = ""
