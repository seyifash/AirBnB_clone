#!/usr/bin/python3
"""
contains class State
"""
import models
from models.base_model import BaseModel


class State(BaseModel):
    """class state that inherits from basemodel

    Atrributes:
        name (str): the name of the state
    """
    name = ""
