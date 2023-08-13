#!/usr/bin/python3
"""Defines a base model class"""

from datetime import datetime
import models
import uuid


class BaseModel:

    """The base model class"""

    def __init__(self, *args, **kwargs):
        """Initializes the base_model class"""
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == "created_at" or k == "updated_at":
                        format_str = "%Y-%m-%dT%H:%M:%S.%f"
                        self.__setattr__(k, datetime.strptime(v, format_str))
                    else:
                        self.__setattr__(k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        if 'created_at' in instance_dict:
            instance_dict['created_at'] = \
                instance_dict['created_at'].isoformat()
        if 'updated_at' in instance_dict:
            instance_dict['updated_at'] = \
                instance_dict['updated_at'].isoformat()

        return instance_dict

    def __str__(self):
        """prints out a custom string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
