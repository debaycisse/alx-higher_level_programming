#!/usr/bin/python3
"""This module contains a set of unittest test cases
to validate the logic of the implementation of a Square class.
"""


import os
import sys
import unittest


sys.path.append(os.getcwd())
try:
    from models.square import Square
    from models.rectangle import Rectangle
    from models.base import Base
except Exception as e:
    print(e)


class TestSquare(unittest.TestCase):
    """This class contains a set of test cases that validate
    the requirement of the square class.
    """

    def setUp(self):
        """This sets up every tests before running them"""
        Base.reset_class()

    def test_square_type(self):
        """This tests that an instance is inheriting from
        the Rectangle class.
        """
        s = Square(2)
        self.assertTrue(isinstance(s, Rectangle))

    def test_default_values(self):
        """This tests that the default values are available to
        some attributes, namely the x, y, and id.
        """
        s = Square(9)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 9)

    def test_width_and_height_value(self):
        """This tests both the value of height and width"""
        s = Square(3)
        self.assertEqual(s.width, s.height)
        self.assertEqual(s.width, s.size)
        self.assertEqual(s.size, s.height)

    def test_non_integer_passed_value(self):
        """This tests that type error is raised when a non-integer
        is given to either, the size, x, or y attribute.
        """
        with self.assertRaises(TypeError):
            Square("3")

        with self.assertRaises(TypeError):
            Square(2, "8")

        with self.assertRaises(TypeError):
            Square(7, 2, "3")

        with self.assertRaises(TypeError):
            Square(7, "2", 3, 89)

    def test_zero_value_with_size(self):
        """This tests that type error is raised when a non-integer
        is given to either, the size, x, or y attribute.
        """
        with self.assertRaises(ValueError):
            Square(0)

        with self.assertRaises(ValueError):
            Square(-99999)

    def test_str_method(self):
        """This tests that a __str__ is implemented and the content
        match up with the requirements.
        """
        s = Square(3)
        self.assertEqual(str(s), "[{}] ({}) {}/{} - {}".format(
                                  s.__class__.__name__, s.id,
                                  s.x, s.y, s.size))

    def tearDown(self):
        """This resets the value of the class variable for each test
        to start on a clean slate.
        """
        Base.reset_class()
        try:
            if s:
                del s
        except Exception as e:
            pass

    def test_all_getters(self):
        """This tests all getter methods of every instance"""
        s = Square(7)
        self.assertEqual(s.size, 7)

    def test_all_setters(self):
        """This tests that all setter methods update the size attribute"""
        s = Square(5)
        self.assertEqual(s.size, 5)
        s.size = 7
        self.assertEqual(s.size, 7)

    def test_size_setter_with_non_integer_type(self):
        """This tests that error is raised for passing non interger types"""
        s = Square(3)
        with self.assertRaises(TypeError):
            s.size = "5"

    def test_size_setter_with_zero_value(self):
        """This tests that error is raised for passing zero value"""
        s = Square(8)
        with self.assertRaises(ValueError):
            s.size = 0

    def test_update_method_with_no_keyword_argument(self):
        """This tests update method with no-keyword arguments"""
        s = Square(4)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)
        s.update(22, 41, 87, 34)
        self.assertEqual(s.size, 41)
        self.assertEqual(s.x, 87)
        self.assertEqual(s.y, 34)
        self.assertEqual(s.id, 22)

    def test_update_method_with_no_kwarg_non_integer_value(self):
        """This tests that update method with no key-word raise error for
        updating with non interger type.
        """
        s = Square(22)
        self.assertEqual(s.size, 22)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)
        with self.assertRaises(TypeError):
            s.update(22, "23", 12, 23)
        with self.assertRaises(TypeError):
            s.update(22, 23, "12", 23)
        with self.assertRaises(TypeError):
            s.update(22, 23, 12, "23")

    def test_update_method_with_keyword_argument(self):
        """This tests that keyword argument is supported"""
        s = Square(11)
        self.assertEqual(s.size, 11)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.x, 0)
	self.assertEqual(s.y, 0)
        s.update(x=21, id=299, size=7, y=79)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.id, 299)
        self.assertEqual(s.y, 79)
        self.assertEqual(s.x, 21)

    def test_update_method_with_keyword_argument_non_integer(self):
        """This tests that an error is raised when a non-integer is passed
        as a key-word argument.
        """
        s = Square(21)
        self.assertEqual(s.size, 21)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.x, 0)
	self.assertEqual(s.y, 0)
        with self.assertRaises(TypeError):
            s.update(y=32, x="45", id=1, size=34)
        with self.assertRaises(TypeError):
            s.update(y="32", x=45, id=1, size=34)
        with self.assertRaises(TypeError):
            s.update(y=32, x=45, id=1, size="34")

    def test_update_method_with_negative_and_zero_value1(self):
        """This tests that error is raised when zero or negative value
        is passed to size attribute.
        """
        s = Square(9)
        with self.assertRaises(ValueError):
            s.update(1, 0)
        with self.assertRaises(ValueError):
            s.update(id=1, size=0)
        with self.assertRaises(ValueError):
            s.update(1, -99999)
        with self.assertRaises(ValueError):
            s.update(id=1, size=-99999)

    def test_to_dictionary_method(self):
        """This tests that to_dictionary returns correct data"""
        s = Square(33, 22, 11, 6)
        s_dict = s.to_dictionary()
        self.assertEqual(
                         {'id': 6, 'x': 22, 'size': 33, 'y': 11},
                         s_dict)
        self.assertTrue(isinstance(s_dict, dict))
