#!usr/bin/python3
'''A module to test the Place class'''
import unittest
from models.place import Place
from models.base_model import BaseModel
import models


class TestPlace(unittest.TestCase):
    '''test the basics of the place class'''

    def test_class_inheritence(self):
        self.assertTrue(issubclass(Place, BaseModel))

    def test_Place_with_no_attr(self):
        self.assertEqual(Place, type(Place()))

    def test_place_storage(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_city_id_type(self):
        self.assertEqual(str, type(Place.city_id))

    def test_user_id_type(self):
        self.assertEqual(str, type(Place.user_id))

    def test_name_type(self):
        self.assertEqual(str, type(Place.name))

    def test_description_type(self):
        self.assertEqual(str, type(Place.description))

    def test_number_rooms_type(self):
        self.assertEqual(int, type(Place.number_rooms))

    def test_number_bathrooms_type(self):
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_max_guest_type(self):
        self.assertEqual(int, type(Place.max_guest))

    def test_price_by_night_type(self):
        self.assertEqual(int, type(Place.price_by_night))

    def test_latitude_type(self):
        self.assertEqual(float, type(Place.latitude))

    def test_longitude_type(self):
        self.assertEqual(float, type(Place.longitude))

    def test_amenity_ids_type(self):
        self.assertEqual(list, type(Place.amenity_ids))


if __name__ == '__main__':
    unittest.main()
