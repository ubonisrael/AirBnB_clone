#!/usr/bin/python3
"""Contains the FileStorage class"""
from json import dumps, loads

class FileStorage():
    """a class that serializes instances to a JSON file and deserializes JSON file to instances"""
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """Returns the objects attribute"""
        return self.__objects
    
    def new(self, obj):
        """Adds an object to the object attr of the instance"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        if self.__objects is None or len(self.__objects) == 0:
            return

        json_obj = {}
        for i in self.__objects:
            json_obj[i] = self.__objects[i].to_dict()
        with open("{}".format(self.__file_path), "w", encoding="utf-8") as f:
            f.write(dumps(json_obj))

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review
                   }
        return classes

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists"""

        try:
            with open("{}".format(self.__file_path), "r") as myFile:
                file_content = myFile.read()
                if file_content is not None:
                    obj_dict = loads(file_content)
            self.__objects = {k: self.classes()[v['__class__']](**v)
                        for k, v in obj_dict.items()}
        except FileNotFoundError as e:
            pass
