#!/usr/bin/python3
"""
base module test
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    TestBase class
    """
    def test_base_default_id(self):
        """
        test_base_default_id method
        """
        obj1 = Base()
        self.assertIsNotNone(obj1.id)

    def test_base_nb_objects(self):
        """
        test_base_nb_objects method
        """
        obj2 = Base()
        self.assertEqual(obj2.id, 2)
        obj3 = Base()
        self.assertEqual(obj3.id, 3)

    def test_base_custom_id(self):
        """
        test_base_custom_id method
        """
        custom_id = 12
        obj = Base(custom_id)
        self.assertEqual(obj.id, custom_id)
