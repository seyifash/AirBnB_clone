#!/usr/bin/python3
"""Defines test cases for class Place."""


import unittest
from models.place import (Place, BaseModel)


class TestPlace(unittest.TestCase):
    """represents the test cases for Place model"""

    def test_classattrrs(self):
        """test cases for public class attributes"""
        cs0 = Place()
        self.assertEqual(cs0.user_id, "")
        self.assertEqual(cs0.name, "")
        self.assertEqual(cs0.number_bathrooms, 0)
        self.assertEqual(cs0.number_rooms, 0)
        cs0.user_id = "135"
        self.assertEqual(cs0.user_id, "135")

        cs1 = Place()
        self.assertEqual(cs1.user_id, "")
        self.assertEqual(cs1.name, "")
        self.assertEqual(cs1.number_bathrooms, 0)
        self.assertEqual(cs1.number_rooms, 0)

    def test_isinstance(self):
        """test cases to check if Place is an instance of
        BaseModel"""

        self.assertIsInstance(Place(), type(BaseModel()))
