#!/usr/bin/python3
"""
base module test
"""

from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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
        b3 = Base()
        self.assertNotEqual(b2.id, b3.id)

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
        with open("Rectangle.json", "r") as f:
            content = f.read()
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

    def test_base_create(self):
        """
        test_base_create method
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_base_load_from_file(self):
        """
        test_base_load_from_file method
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rect_input = [r1, r2]
        Rectangle.save_to_file(list_rect_input)
        list_rect_output = Rectangle.load_from_file()
        self.assertNotEqual(id(list_rect_input[0]), id(list_rect_input[1]))
        self.assertNotEqual(list_rect_input[0], list_rect_input[1])
        self.assertNotEqual(id(list_rect_output[0]), id(list_rect_output[1]))
        self.assertNotEqual(list_rect_output[0], list_rect_output[1])

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_sqr_input = [s1, s2]
        Square.save_to_file(list_sqr_input)
        list_sqr_output = Square.load_from_file()
        self.assertIsNot(list_sqr_input[0], list_sqr_input[1])
        self.assertNotEqual(list_sqr_input[0], list_sqr_input[1])
        self.assertIsNot(list_sqr_output[0], list_sqr_output[1])
        self.assertNotEqual(list_sqr_output[0], list_sqr_output[1])

    def test_base_save_to_file_csv(self):
        """
        test_base_save_to_file_csv method
        """
        expected_output = (
            '[{"x": 7, "y": 9, "id": 11, "height": 5, "width": 3}, ' +
            '{"x": 6, "y": 8, "id": 10, "height": 4, "width": 2}]'
            )
        r1 = Rectangle(3, 5, 7, 9, 11)
        r2 = Rectangle(2, 4, 6, 8, 10)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            content = f.read()
        self.assertEqual(content, expected_output)

    def test_base_load_from_file_csv(self):
        """
        test_base_load_from_file_csv method
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rect_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rect_input)
        list_rect_output = Rectangle.load_from_file_csv()
        self.assertNotEqual(id(list_rect_input[0]), id(list_rect_input[1]))
        self.assertNotEqual(list_rect_input[0], list_rect_input[1])
        self.assertNotEqual(id(list_rect_output[0]), id(list_rect_output[1]))
        self.assertNotEqual(list_rect_output[0], list_rect_output[1])

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_sqr_input = [s1, s2]
        Square.save_to_file_csv(list_sqr_input)
        list_sqr_output = Square.load_from_file_csv()
        self.assertIsNot(list_sqr_input[0], list_sqr_input[1])
        self.assertNotEqual(list_sqr_input[0], list_sqr_input[1])
        self.assertIsNot(list_sqr_output[0], list_sqr_output[1])
        self.assertNotEqual(list_sqr_output[0], list_sqr_output[1])
