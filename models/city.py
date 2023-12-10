#!/usr/bin/python3
'''A module for City class'''
from models.base_model import BaseModel


class City(BaseModel):
    '''this class is for the city

    Attributes:
        state_id (str): The ID of the associated state.
        name (str): The name of the city.
    '''

    state_id = ''
    name = ''
