#!/usr/bin/python3
'''A module for BaseModel class'''
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    '''the class BaseModel is the base class the of the project'''

    def __init__(self, *args, **kwargs):
        '''the constractore
        Args:
            *args (tup): a tuple that contains all arguments
            **kwrgs (dict): a dict that contains all arguments by
                key/value
        '''
        if kwargs:
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            models.storage.new(self)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def save(self):
        '''A method that change the updated_at attr and save the changes'''
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        '''A method that changes the format of created_at and
        updated_at attr and add the classname
        '''
        odict = self.__dict__.copy()
        odict["__class__"] = self.__class__.__name__
        odict["created_at"] = self.created_at.isoformat()
        odict["updated_at"] = self.updated_at.isoformat()
        return odict

    def __str__(self):
        '''A method that prints: [<class name>] (<self.id>) <self.__dict__>
        '''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
