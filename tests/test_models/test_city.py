#!/usr/bin/python3
"""Defines test cases for class City."""


import unittest
from models.city import (City, BaseModel)


class TestCity(unittest.TestCase):
    """represents the test cases for City model"""

    def test_classattrrs(self):
        """test cases for public class attributes"""
        cs0 = City()
        self.assertEqual(cs0.state_id, "")
        self.assertEqual(cs0.name, "")
        cs0.state_id = "LAG"
        self.assertEqual(cs0.state_id, "LAG")

        cs1 = City()
        self.assertEqual(cs1.state_id, "")
        self.assertEqual(cs1.name, "")

    def test_isinstance(self):
        """test cases to check if City is an instance of
        BaseModel"""

        self.assertIsInstance(City(), type(BaseModel()))
