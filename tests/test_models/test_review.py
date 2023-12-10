#!usr/bin/python3
'''A module to test the Review class'''
import unittest
from models.review import Review
from models.base_model import BaseModel
import models


class TestReview(unittest.TestCase):
    '''test the basics of the Review class'''

    def test_class_inheritence(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_Review_with_no_attr(self):
        self.assertEqual(Review, type(Review()))

    def test_Review_storage(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_place_id_type(self):
        self.assertEqual(str, type(Review.place_id))

    def test_user_id_type(self):
        self.assertEqual(str, type(Review.user_id))

    def test_text_type(self):
        self.assertEqual(str, type(Review.text))


if __name__ == '__main__':
    unittest.main()
