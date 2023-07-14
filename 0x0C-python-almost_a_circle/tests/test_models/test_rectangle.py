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
    @classmethod
    def setUpClass(cls):
        """
        setUpClass method
        """
        cls.r1 = Rectangle(10, 2)
        cls.r2 = Rectangle(2, 5)
        cls.r3 = Rectangle(10, 2, 0, 0, 12)
        cls.r4 = Rectangle(12, 23)

    @classmethod
    def tearDownClass(cls):
        """
        tearDownClass method
        """
        del cls.r1, cls.r2, cls.r3, cls.r4


    def test_rectangle_not_none(self):
        """
        test_rectangle_not_none method
        """
        self.assertIsNotNone(self.r1.id)
        self.assertIsNotNone(self.r2.id)

    def test_rectangle_with_defaults(self):
        """
        test_rectangle_nb_objects method
        """
        self.assertNotEqual(self.r2.id, self.r3.id)

    def test_rectangle_custom_id(self):
        """
        test_rectangle_custom_id method
        """
        self.assertEqual(self.r3.id, 12)

    def test_rectangle_attr(self):
        """
        test_rectangle_attr method
        """
        self.assertEqual(self.r4.width, 12)
        self.assertEqual(self.r4.height, 23)

    def test_rectangle_raises(self):
        """
        test_rectangle_raises method
        """
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10

        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}

        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, 3, -1)

    def test_rectangle_area(self):
        """
        test_rectangle_area method
        """
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 10)
