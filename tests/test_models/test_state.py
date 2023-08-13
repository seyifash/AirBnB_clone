#!/usr/bin/python3
"""Defines test cases for class State."""


import unittest
from models.state import (State, BaseModel)


class TestState(unittest.TestCase):
    """represents the test cases for State model"""

    def test_classattrrs(self):
        """test cases for public class attributes"""
        cs0 = State()
        self.assertEqual(cs0.name, "")
        cs0.name = "Dallas"
        self.assertEqual(cs0.name, "Dallas")

        cs1 = State()
        self.assertEqual(cs1.name, "")

    def test_isinstance(self):
        """test cases to check if State is an instance of
        BaseModel"""

        self.assertIsInstance(State(), type(BaseModel()))
