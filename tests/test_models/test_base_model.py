#!/usr/bin/python3
"""Defines test cases for class BaseModel."""


import io
import sys
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """represents the test cases for BseModel class."""

    def setUp(self):
        """This is run before test cases"""
        self.base1 = BaseModel()
        self.storage_cpy = FileStorage()

    def test_init(self):
        """test cases for init (constructor) function"""
        obj_len = len(self.storage_cpy.all())
        self.assertEqual(type(self.base1.id), str)
        self.assertEqual(type(self.base1.created_at), datetime)
        self.assertEqual(type(self.base1.updated_at), datetime)
        base2 = BaseModel()
        self.assertEqual(len(self.storage_cpy.all()), obj_len + 1)

    def test_save(self):
        """test cases for save method of BestModels"""
        obj_len = len(self.storage_cpy.all())
        base3 = BaseModel()
        prev_time = base3.__dict__['updated_at']
        sleep(1)
        base3.save()
        present_time = base3.__dict__['updated_at']
        self.assertNotEqual(prev_time, present_time)
        self.storage_cpy.reload()
        self.assertEqual(len(self.storage_cpy.all()), obj_len + 1)

    def cap_stdout(self, base):
        """captures stdout"""
        capture = io.StringIO()
        sys.stdout = io.StringIO()
        print(base)
        output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__

        return output

    def test_str(self):
        """testcases for string representation of BaseModel"""
        base4 = BaseModel()
        cs = f"[{base4.__class__.__name__}] ({base4.id}) {base4.__dict__}\n"

        self.assertEqual(self.cap_stdout(base4), cs)

    def test_to_dict(self):
        """testcases for to_dict method"""
        self.assertEqual(type(self.base1.to_dict()), dict)


if __name__ == "__main__":
    unittest.main()
