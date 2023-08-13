#!/usr/bin/python3

"""Defines a child class that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class review"""

    place_id = ""
    user_id = ""
    text = ""
