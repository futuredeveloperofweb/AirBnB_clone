#!usr/bin/python3
'''A module to test the State class'''
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import models


class TestAmenity(unittest.TestCase):
    '''test the basics of the Amenity class'''

    def test_class_inheritence(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_Amenity_with_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_storage(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_name_attr(self):
        self.assertEqual(str, type(Amenity.name))


if __name__ == '__main__':
    unittest.main()
