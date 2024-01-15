#!/usr/bin/python3
"""
Create an instance of FileStorage
Reload data from the JSON file into the storage
"""


from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
