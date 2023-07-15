#!/usr/bin/python3
"""
square module test
"""


from models.square import Square
from unittest import TestCase
from unittest.mock import patch
from io import StringIO


class TestSquare(TestCase):
    """
    TestCase class
    """
    def setUp(self):
        """
        setUpClass class
        """
        self.s1 = Square(5)
        self.s2 = Square(2, 2)
        self.s3 = Square(3, 1, 3)
        self.s4 = Square(4, 3, 2, 10)
        self.s5 = Square(2, 4, 6, 5)

    def tearDown(self):
        """
        tearDown method
        """
        del self.s1, self.s2, self.s3, self.s4, self.s5

    def test_square_custom_id(self):
        """
        test_square_custom_id method
        """
        self.assertEqual(self.s4.id, 10)

    def test_square_default_id(self):
        """
        test_square_default_id method
        """
        self.assertEqual(self.s1.id, 10)
        self.assertEqual(self.s2.id, 11)
        self.assertEqual(self.s3.id, 12)

    def test_square_area(self):
        """
        test_square_area method
        """
        self.assertEqual(self.s2.area(), 4)

    def test_square_str_rep(self):
        """
        test_square_str_rep method
        """
        self.assertIsNotNone(self.s3)

    def test_square_display(self):
        """
        test_square_display method
        """
        with patch('sys.stdout', new=StringIO()) as output:
            self.s2.display()
            self.assertEqual(output.getvalue(), "  ##\n  ##\n")

    def test_square_attr(self):
        """
        test_square_attr method
        """
        self.assertEqual(self.s3.width, 3)
        self.assertEqual(self.s3.height, 3)
        self.assertEqual(self.s3.size, 3)
        self.s3.size = 10
        self.assertEqual(self.s3.size, 10)
        self.assertEqual(self.s3.height, 10)
        self.assertEqual(self.s3.width, 10)

    def test_square_raises(self):
        """
        test_square_raises method
        """
        with self.assertRaises(TypeError):
            self.s5.y = "2"

        with self.assertRaises(ValueError):
            self.s5.width = -10

        with self.assertRaises(TypeError):
            self.s5.x = {}

        with self.assertRaises(ValueError):
            self.s5.height = -1

        with self.assertRaises(TypeError):
            self.s5.size = "9"
