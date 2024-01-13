#!/usr/bin/python3
"""A module that contains the base model class"""
from datetime import datetime
import uuid
from . import storage


class BaseModel():
    """This class defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes the base model class"""
        if kwargs is None or kwargs == {}:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                # if not key == "__class__":
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = value
        # else:
        #     for key, value in kwargs.items():
        #         if not key == "__class__":
        #             if key == 'created_at' or key == 'updated_at':
        #                 setattr(self, key,
        #                         datetime.strptime(value,
        #                                           '%Y-%m-%dT%H:%M:%S.%f'))
        #             else:
        #                 setattr(self, key, value)
            

    def __str__(self):
        """Returns an informal representation of the class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attr with the current time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        obj_dict = {}
        for k, v in self.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                obj_dict[k] = v.isoformat()
            else:
                obj_dict[k] = v
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
