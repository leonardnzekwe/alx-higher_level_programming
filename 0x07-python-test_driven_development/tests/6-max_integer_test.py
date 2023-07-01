#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test Cases for max_integer(list=[]) function"""

    def test_empty_list(self):
        """Test for an empty list []"""
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """Test for a list with a single element"""
        self.assertEqual(max_integer([1]), 1)

    def test_positive_numbers(self):
        """Test for a list with positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([10, 5, 8, 3]), 10)

    def test_negative_numbers(self):
        """Test for a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-10, -5, -8, -3]), -3)

    def test_mixed_numbers(self):
        """Test for a list with positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-10, 5, -8, 3]), 5)
        self.assertEqual(max_integer([-1, -2, 0, 2]), 2)

    def test_duplicate_numbers(self):
        """Test for a list with duplicate numbers"""
        self.assertEqual(max_integer([1, 2, 2, 2]), 2)
        self.assertEqual(max_integer([-1, -2, -2, -2]), -1)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)


if __name__ == '__main__':
    unittest.main()
