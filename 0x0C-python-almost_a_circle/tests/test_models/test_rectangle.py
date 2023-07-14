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
        r3 = Rectangle(10, 2)
        self.assertNotEqual(r2.id, r3.id)

    def test_rectangle_custom_id(self):
        """
        test_rectangle_custom_id method
        """
        custom_id = 12
        r4 = Rectangle(10, 2, 0, 0, custom_id)
        self.assertEqual(r4.id, 12)

    def test_rectangle_attr(self):
        """
        test_rectangle_attr method
        """
        r5 = Rectangle(12, 23)
        self.assertEqual(r5.width, 12)
        self.assertEqual(r5.height, 23)

    def test_rectangle_raises(self):
        """
        test_rectangle_raises method
        """
        with self.assertRaises(TypeError):
            r6 = Rectangle(10, "2")

        with self.assertRaises(ValueError):
            r7 = Rectangle(10, 2)
            r7.width = -10

        with self.assertRaises(TypeError):
            r8 = Rectangle(10, 2)
            r8.x = {}

        with self.assertRaises(ValueError):
            r9 = Rectangle(10, 2, 3, -1)
