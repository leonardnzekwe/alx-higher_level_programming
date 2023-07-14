#!/usr/bin/python3
"""
rectangle module test
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    TestRectangle class
    """
    def test_rectangle_not_none(self):
        """
        test_rectangle_not_none method
        """
        r1 = Rectangle(10, 2)
        self.assertIsNotNone(r1.id)

    def test_rectangle_with_defaults(self):
        """
        test_rectangle_nb_objects method
        """
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 3)

    def test_rectangle_custom_id(self):
        """
        test_rectangle_custom_id method
        """
        custom_id = 12
        r3 = Rectangle(10, 2, 0, 0, custom_id)
        self.assertEqual(r3.id, 12)

    def test_rectangle_attr(self):
        """
        test_rectangle_attr method
        """
        r4 = Rectangle(12, 23)
        self.assertEqual(r4.width, 12)
        self.assertEqual(r4.height, 23)
