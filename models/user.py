#!/usr/bin/python3
'''A module for User class'''
from models.base_model import BaseModel


class User(BaseModel):
    '''A class that inherite from BaseModel class
    Attribute:
        email (str): the email of the user
        password (str): the password of the user
        first_name (str): the first name of the user
        last_name (str): the usr.s last name
    '''

    email = ''
    password = ''
    first_name = ''
    last_name = ''
