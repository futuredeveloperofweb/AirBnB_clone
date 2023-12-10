#!usr/bin/python3
'''A module to test the State class'''
import unittest
from models.state import State
from models.base_model import BaseModel
import models


class TestState(unittest.TestCase):
    '''test the basics of the State class'''

    def test_class_inheritence(self):
        self.assertTrue(issubclass(State, BaseModel))

    def test_State_with_no_attr(self):
        self.assertEqual(State, type(State()))

    def test_State_storage(self):
        self.assertIn(State(), models.storage.all().values())

    def test_name_type(self):
        self.assertEqual(str, type(State.name))


if __name__ == '__main__':
    unittest.main()
