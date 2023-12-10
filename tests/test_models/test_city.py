#!usr/bin/python3
'''A module to test the City class'''
import unittest
import models
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    '''test the basics of the class City'''

    def test_inheritence(self):
        self.assertTrue(issubclass(City, BaseModel))

    def test_City_with_no_args(self):
        self.assertEqual(City, type(City()))

    def test_storage(self):
        self.assertIn(City(), models.storage.all().values())

    def test_state_id_attr(self):
        self.assertEqual(str, type(City.state_id))

    def test_name(self):
        self.assertEqual(str, type(City.name))


if __name__ == '__main__':
    unittest.main()
