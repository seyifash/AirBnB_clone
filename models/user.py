#!/usr/bin/python3
"""
a class User that inherits from BaseModel
"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """User that inherits from BaseModel

    Attributes:
        email (str): the email of the user
        password (str): the user's password
        first_name (str): The user's first name
        last_name (str): the user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
