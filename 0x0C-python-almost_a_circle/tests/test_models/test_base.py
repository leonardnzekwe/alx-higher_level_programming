#!/usr/bin/python3
"""
base module test
"""

from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle


class TestBase(TestCase):
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

    def test_base_to_json_string(self):
        """
        test_base_to_json_string method
        """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)
        r1 = Rectangle(3, 5, 7, 9, 11)
        r2 = Rectangle(2, 4, 6, 8, 10)

    def test_base_save_to_file(self):
        """
        test_base_save_to_file method
        """
        expected_output = (
            '[{"x": 7, "y": 9, "id": 11, "height": 5, "width": 3}, ' +
            '{"x": 6, "y": 8, "id": 10, "height": 4, "width": 2}]'
            )
        r1 = Rectangle(3, 5, 7, 9, 11)
        r2 = Rectangle(2, 4, 6, 8, 10)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual(content, expected_output)

    def test_base_from_json_string(self):
        """
        test_base_from_json_string method
        """
        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
            ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_input), list)
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(type(list_output), list)
