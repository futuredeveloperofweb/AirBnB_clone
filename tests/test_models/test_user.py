#!usr/bin/python3
'''A module to test the user.py file'''
from models.base_model import BaseModel
from models.user import User
import unittest
from time import sleep
import os
import models
from datetime import datetime


class TestUser(unittest.TestCase):
    '''Test the User class that inherites from BaseModel class'''

    def test_class_inherite(self):
        '''test if User inherites from BaseModel class'''
        self.assertTrue(issubclass(User, BaseModel))

    def test_User_with_no_args(self):
        self.assertEqual(User, type(User()))

    def test_storage(self):
        self.assertIn(User(), models.storage.all().values())

    def test_emil_type(self):
        self.assertEqual(str, type(User.email))

    def test_password_type(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_type(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_type(self):
        self.assertEqual(str, type(User.last_name))

    def test_id_of_two_user(self):
        '''test the id of 2 users'''
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)

    def test_created_at_attr(self):
        '''test the attr created_at for 2 users'''
        u1 = User()
        sleep(0.5)
        u2 = User()
        self.assertLess(u1.created_at, u2.created_at)

    def test_updated_at_attr(self):
        '''test the attr updated_at for 2 users'''
        u1 = User()
        sleep(0.5)
        u2 = User()
        self.assertLess(u1.updated_at, u2.updated_at)

    def test_no_arg_used(self):
        '''test if no argument was used'''
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_kwargs(self):
        d = datetime.today()
        d_format = d.isoformat()
        user = User(id='2023', created_at=d_format, updated_at=d_format)
        self.assertEqual(user.created_at, d)
        self.assertEqual(user.updated_at, d)
        self.assertEqual(user.id, '2023')

    def test_no_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, craeted_at=None, updated_at=None)


class TestUser_save_funct(unittest.TestCase):
    '''test the User class with the save() function'''

    def setUP(self):
        try:
            os.rename('file.json', 'tmp')
        except IOError:
            pass

    def test_save(self):
        '''test one save()'''
        user = User()
        sleep(0.5)
        the_updated_at = user.updated_at
        user.save()
        self.assertLess(the_updated_at, user.updated_at)

    def test_save_args(self):
        '''test the save() function with args'''
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_save_two(self):
        '''test that user save() method two times'''
        user = User()
        sleep(0.5)
        f_updated_at = user.updated_at
        user.save()
        s_updated_at = user.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.5)
        user.save()
        self.assertLess(s_updated_at, user.updated_at)

    def test_save_error(self):
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_update_save(self):
        user = User()
        user.save()
        user_id = 'User.{}'.format(user.id)
        with open('file.json', 'r') as file:
            self.assertIn(user_id, file.read())


class TestUser_to_dict_funct(unittest.TestCase):
    '''test the User class with the method to_dict'''

    def test_to_dict(self):
        '''test the type of to_dict method'''
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_with_keys(self):
        '''test the User keys with to_dict function'''
        user = User()
        self.assertIn('__class__', user.to_dict())
        self.assertIn('created_at', user.to_dict())
        self.assertIn('updated_at', user.to_dict())

    def test_more_attr_to_dict(self):
        '''test new attr with to_dict method'''
        user = User()
        user.name = 'Zain'
        user.age = 22
        self.assertEqual('Zain', user.name)
        self.assertEqual(22, user.age)

    def test_compare(self):
        '''test to compare to_dict() with __dict__'''
        user = User()
        self.assertNotEqual(user.to_dict, user.__dict__)

    def test_to_dict_error(self):
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)


if __name__ == '__main__':
    unittest.main()
