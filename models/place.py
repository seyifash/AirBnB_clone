#!/usr/bin/python3
"""
contains the class State
"""
import models
from models.base_model import BaseModel


class Place(BaseModel):
    """Representation of Place
    
    Attributes:
        city_id  (str): the city's id
        user_id (str): the user's id
        name (str): the name of the place
        description (str): the descripition of the place
        number_rooms (int): the number of room
        number_bathrooms (int): the number of bathrooms
        max_guest (int): the maximum number of guest 
        price_by_night (int): the price by night for the place
        latitude (float): the latitude of the place
        longitude (float): The longitude of the place
        amenity_ids (list): A list containing the amenity's id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place attributes"""
        super().__init__(*args, **kwargs)
