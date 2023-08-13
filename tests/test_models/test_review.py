#!/usr/bin/python3
"""Defines test cases for class Review."""


import unittest
from models.review import (Review, BaseModel)


class TestReview(unittest.TestCase):
    """represents the test cases for Review model"""

    def test_classattrrs(self):
        """test cases for public class attributes"""
        cs0 = Review()
        self.assertEqual(cs0.place_id, "")
        self.assertEqual(cs0.user_id, "")
        self.assertEqual(cs0.text, "")
        cs0.place_id = "Accra"
        self.assertEqual(cs0.place_id, "Accra")

        cs1 = Review()
        self.assertEqual(cs1.place_id, "")
        self.assertEqual(cs1.user_id, "")
        self.assertEqual(cs1.text, "")

    def test_isinstance(self):
        """test cases to check if Reviewis an instance of
        BaseModel"""

        self.assertIsInstance(Review(), type(BaseModel()))
