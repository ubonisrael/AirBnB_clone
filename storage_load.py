#!/usr/bin/python3
from engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
print(storage.all())
storage.reload()
print(storage.all())