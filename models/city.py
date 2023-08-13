#!/usr/bin/python3
"""
contains the class city
"""
import models
from models.base_model import BaseModel


class City(BaseModel):
    """the class city which inherits from BaseModel

    Attributes:
        state_id (str): the state id
        name (str): the name of the city
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes the city attributes"""
        super().__init__(*args, **kwargs)
