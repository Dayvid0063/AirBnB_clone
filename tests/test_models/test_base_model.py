#!/usr/bin/python3


import unittest
import os
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Set up the test environment before each test"""
        self.base_model = BaseModel()

    def tearDown(self):
        """Clean up the test environment after each test"""
        del self.base_model

    def test_attributes(self):
        """Test the initial attributes of the BaseModel"""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_generation(self):
        """Test the generation of unique IDs"""
        new_model = BaseModel()
        self.assertNotEqual(self.base_model.id, new_model.id)

    def test_created_updated_at_types(self):
        """Test if created_at and updated_at are datetime objects"""
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_representation(self):
        """Test the __str__ method"""
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id,
                                                    self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        """Test the save method"""
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        self.base_model.created_at = datetime(2022, 1, 1, 0, 0, 0)
        self.base_model.updated_at = datetime(2022, 1, 2, 0, 0, 0)
        expected_dict = {
            'id': self.base_model.id,
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            '__class__': 'BaseModel'
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)

    def test_kwargs_constructor(self):
        """Test the __init__ method with kwargs"""
        new_model_dict = self.base_model.to_dict()
        new_model = BaseModel(**new_model_dict)
        self.assertEqual(self.base_model.id, new_model.id)
        self.assertEqual(self.base_model.created_at, new_model.created_at)
        self.assertEqual(self.base_model.updated_at, new_model.updated_at)
