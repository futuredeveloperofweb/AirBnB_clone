#!/usr/bin/python3
'''A module for the FileStorage class'''
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
import os.path
import json


class FileStorage:
    '''A class  that serializes instances to a JSON file and
    deserializes JSON file to instances
    Args:
        file_path: (str) path to the JSON file
        objects: (dict) empty but will store all objects by
                <class name>.id
    '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''A function that returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id
        Args:
            obj: the inputs variables
        '''
        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)
        '''
        my_dict = {}
        for v in FileStorage.__objects.keys():
            my_dict[v] = FileStorage.__objects[v].to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(my_dict, file)

    def reload(self):
        '''deserializes the JSON file to __objects'''
        f_path = FileStorage.__file_path

        if os.path.isfile(f_path):
            with open(f_path, 'r') as file:
                my_dict = json.load(file)
                for v in my_dict.values():
                    m = v.pop('__class__', None)
                    if m:
                        self.new(eval(m)(**v))
        else:
            return
