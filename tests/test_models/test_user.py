#!/usr/bin/python3
"""Defines test cases for class BaseModel."""


import unittest
from models.user import (User, BaseModel)


class TestUser(unittest.TestCase):
    """represents the test cases for User model"""

    def test_classattrrs(self):
        """test cases for public class attributes"""
        cs0 = User()
        self.assertEqual(cs0.email, "")
        self.assertEqual(cs0.password, "")
        self.assertEqual(cs0.first_name, "")
        self.assertEqual(cs0.last_name, "")
        cs0.email = "johndoe@gmail.com"
        cs0.first_name = "john"
        cs0.last_name = "doe"
        self.assertEqual(cs0.email, "johndoe@gmail.com")
        self.assertEqual(cs0.first_name, "john")
        self.assertEqual(cs0.last_name, "doe")

        cs1 = User()
        self.assertEqual(cs1.email, "")
        self.assertEqual(cs1.password, "")
        self.assertEqual(cs1.first_name, "")
        self.assertEqual(cs1.last_name, "")

    def test_isinstance(self):
        """test cases to check if Useris an instance of
        BaseModel"""

        self.assertIsInstance(User(), type(BaseModel()))