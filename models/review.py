#!/usr/bin/python3
"""
contains the class review
"""
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """Representation of Review

    Attributes:
        place_id (str): The place id
        user_id (str): the users id
        text (str): the text for the reviews
    """

    place_id = ""
    user_id = ""
    text = ""
