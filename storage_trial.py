#!/usr/bin/python3
from engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
print(storage.all())
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
storage.new(my_model)
print(storage.all())
my_model2 = BaseModel()
my_model.name = "My Second Model"
my_model.my_number = 98
storage.new(my_model2)
print(storage.all())
storage.save()
