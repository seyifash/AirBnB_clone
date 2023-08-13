#!/usr/bin/python3
"""Defines test cases for class FileStorage."""


import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Represents test class for FileStorage  model"""

    def setUp(self):
        """This is run before test cases"""
        self.storage_cpy = FileStorage()

    def test_all(self):
        """test case(s) for the all method in
        the FileStorage class"""
        self.assertEqual(type(self.storage_cpy.all()), dict)

    def test_new(self):
        """test cases for the new method"""
        obj_count = len(self.storage_cpy.all())
        self.storage_cpy.new(None)
        self.assertEqual(len(self.storage_cpy.all()), obj_count)
        obj = BaseModel()
        self.assertEqual(len(self.storage_cpy.all()), obj_count + 1)
        obj_id = obj.__class__.__name__ + "." + obj.id
        self.assertIn(obj_id, self.storage_cpy.all().keys())

    def test_save(self):
        """testcases for the save method in FilesStorage"""
        self.storage_cpy.new(BaseModel())
        self.storage_cpy.save()
        f = open('file.json')
        self.assertGreater(len(f.readlines()), 0)
        self.storage_cpy.new(BaseModel())
        self.storage_cpy.save()
        f2 = open('file.json')
        self.assertGreater(len(f2.readlines()[0]), len(f.readlines()[0]))
        f.close()
        f2.close()
        os.remove('file.json')

    def test_reload(self):
        """testcases for reload method"""
        os.remove('file.json')
        len0 = len(self.storage_cpy.all())
        cs0 = BaseModel()
        cs0.save()
        len1 = len(self.storage_cpy.all())
        self.assertGreater(len1, len0)
        cs1 = BaseModel()
        cs1.save()
        len2 = len(self.storage_cpy.all())
        self.assertGreater(len2, len1)
        for obj_id in self.storage_cpy.all():
            obj = self.storage_cpy.all()[obj_id]
            self.assertNotEqual(type(obj), str)
        os.remove('file.json')


if __name__ == "__main__":
    unittest.main()
