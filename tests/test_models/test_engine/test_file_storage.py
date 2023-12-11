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
import os


class TestFileStorage(unittest.TestCase):
    '''test the basics of the FileStorage class'''

    def test_FileStorage_instance(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_private_attr_file_path(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_private_attr__objects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_of_FileStorage(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_all_funct(unittest.TestCase):
    '''test FileStorage with all() function'''

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)


class TestFileStorage_new_all_save_reload_funcs(unittest.TestCase):
    '''test FileStorage with new(), all(), save(), reload() functions'''

    def test_new(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_func(self):
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()

        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)

        self.assertIn("BaseModel." + base_model.id,
                      models.storage.all().keys())
        self.assertIn(base_model, models.storage.all().values())

        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())

        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())

        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())

        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())

        self.assertIn("Amenity." + amenity.id, models.storage.all().keys())
        self.assertIn(amenity, models.storage.all().values())

        self.assertIn("Review." + review.id, models.storage.all().keys())
        self.assertIn(review, models.storage.all().values())

    @classmethod
    def setUp(self):
        try:
            os.rename('file.json', 'tmp')
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}


    def test_save(self):
        base_model = BaseModel()
        amenity = Amenity()
        review = Review()
        user = User()
        state = State()
        place = Place()
        city = City()

        models.storage.new(base_model)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.save()

        s_txt = ''
        with open('file.json', 'r') as f:
            s_txt = f.read()
            self.assertIn("BaseModel." + base_model.id, s_txt)
            self.assertIn("Amenity." + amenity.id, s_txt)
            self.assertIn("State." + state.id, s_txt)
            self.assertIn("Place." + place.id, s_txt)
            self.assertIn("City." + city.id, s_txt)
            self.assertIn("Review." + review.id, s_txt)
            self.assertIn("User." + user.id, s_txt)

    def test_save_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        base_model = BaseModel()
        amenity = Amenity()
        review = Review()
        user = User()
        state = State()
        place = Place()
        city = City()

        models.storage.new(base_model)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.save()
        models.storage.reload()

        ob = FileStorage._FileStorage__objects
        self.assertIn('BaseModel.' + base_model.id, ob)
        self.assertIn('Amenity.' + amenity.id, ob)
        self.assertIn('Review.' + review.id, ob)
        self.assertIn('User.' + user.id, ob)
        self.assertIn('State.' + state.id, ob)
        self.assertIn('Place.' + place.id, ob)
        self.assertIn('City.' + city.id, ob)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
