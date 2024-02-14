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
