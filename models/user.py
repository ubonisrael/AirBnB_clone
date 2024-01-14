#!/usr/bin/python3
"""Contains functionality for creating the user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines the user object for the program"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
