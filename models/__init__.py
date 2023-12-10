#!/usr/bin/python3
""""The constructor method within the models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
