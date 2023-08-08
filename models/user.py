#!/usr/bin/python3
"""
a class User that inherits from BaseModel
"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """User that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes the instance attributes of the user"""
        super().__init__(*args, **kwargs)
