#!/usr/bin/python3
'''A module to test the FileStorage class'''
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models
import unittest


class TestFileStorage(unittest.TestCase):
    '''test the basics of the FileStorage class'''

    def test_FileStorage_instance(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))


class TestFileStorage_all_funct(unittest.TestCase):
    '''test FileStorage with all() function'''

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)


class TestFileStorage_new_funct(unittest.TestCase):
    '''test FileStorage with new() function'''

    def test_new(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)


class TestFileStorage_reload_funct(unittest.TestCase):
    '''test FileStorage with reload() method'''

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
