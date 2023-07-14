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
        b1 = Base()
        self.assertIsNotNone(b1.id)

    def test_base_nb_objects(self):
        """
        test_base_nb_objects method
        """
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_base_custom_id(self):
        """
        test_base_custom_id method
        """
        custom_id = 12
        b = Base(custom_id)
        self.assertEqual(b.id, custom_id)
