#!/usr/bin/python3
"""contains class State"""


import models
from models.base_model import BaseModel


class State(BaseModel):
    """class state that inherits from basemodel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes the state attributes"""
        super().__init__(*args, **kwargs)
