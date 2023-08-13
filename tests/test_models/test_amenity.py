#!/usr/bin/python3
"""Defines test cases for class Amenity."""


import unittest
from models.amenity import (Amenity, BaseModel)


class TestAmenity(unittest.TestCase):
    """represents the test cases for Amenity model"""

    def test_classattrrs(self):
        """test cases for public class attributes"""
        cs0 = Amenity()
        self.assertEqual(cs0.name, "")
        cs0.name = "swimming pool"
        self.assertEqual(cs0.name, "swimming pool")

        cs1 = Amenity()
        self.assertEqual(cs1.name, "")

    def test_isinstance(self):
        """test cases to check if Amenityis an instance of
        BaseModel"""

        self.assertIsInstance(Amenity(), type(BaseModel()))
