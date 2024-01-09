#!/usr/bin/python3
"""A module that contains the base model class"""
import datetime
import uuid

class BaseModel():
    """This class defines all common attributes/methods for other classes"""
    def __init__(self):
        """Initializes the base model class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns an informal representation of the class"""
        return "[{:s}] ({:s}) {:s}".format(self.__class__.name, self.id, self.__dict__)
    
    # def save