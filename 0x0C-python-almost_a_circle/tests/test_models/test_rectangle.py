#!/usr/bin/python3
"""
rectangle module test
"""


from models.rectangle import Rectangle
from unittest import TestCase
from unittest.mock import patch
from io import StringIO


class TestRectangle(TestCase):
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
        cls.r5 = Rectangle(3, 2)
        cls.r6 = Rectangle(10, 10, 10, 10)

    @classmethod
    def tearDownClass(cls):
        """
        tearDownClass method
        """
        del cls.r1, cls.r2, cls.r3, cls.r4, cls.r5, cls.r6

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

    def test_rectangle_display(self):
        """
        test_rectangle_area method
        """
        with patch('sys.stdout', new=StringIO()) as output:
            self.r5.display()
            self.assertEqual(output.getvalue(), "###\n###\n")

    def test_rectangle_str(self):
        """
        test_rectangle_str method
        """
        self.assertIsNotNone(str(self.r5))

    def test_rectangle_updating(self):
        """
        test_rectangle_updating method
        """
        self.r6.update(89)
        self.assertEqual(self.r6.id, 89)
        self.r6.update(89, 2)
        self.assertEqual(self.r6.width, 2)
        self.r6.update(89, 2, 3)
        self.assertEqual(self.r6.height, 3)
        self.r6.update(89, 2, 3, 4)
        self.assertEqual(self.r6.x, 4)
        self.r6.update(89, 2, 3, 4, 5)
        self.assertEqual(self.r6.y, 5)
