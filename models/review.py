#!/usr/bin/python3
"""
contains the class review
"""
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """Representation of Review """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review attributes"""
        super().__init__(*args, **kwargs)
