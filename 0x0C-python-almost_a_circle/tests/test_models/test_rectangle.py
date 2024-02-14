#!/usr/bin/python3
"""This module contains a set unittest test cases
to validate the logic of the Rectangle class"""


import os
import sys
import unittest


sys.path.append(os.getcwd())
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """This class contains a number of test cases to validate that the
    workings of the Rectangle class meets the requirement.
    """

    def test_the_parent_of_rectangle(self):
        """This tests that the rectanngle is an instance of the Base class"""
        r1 = Rectangle(4, 5)
        self.assertTrue(isinstance(r1, Base))

    def test_all_getters(self):
        """This tests the existence and validity of logic of all the
        getter methods.
        """
        r1 = Rectangle(2, 3, 4, 5, 2345)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 2345)

    def test_all_setters(self):
        """This tests the validity of all the setter methods"""
        r1 = Rectangle(2, 3, 4, 5, 2345)
        r1.width = 20
        r1.height = 30
        r1.x = 40
        r1.y = 50
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 30)
        selt.assertEqual(r1.x, 40)
        selt.assertEqual(r1.y, 50)

    def test_constructor_default_value(self):
        """This test the default value of some attributes
        by the constructor.
        """
        r1 = Rectangle(3, 6)
        r2 = Rectangle(3, 6, 9, 12, 15)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 6)
        self.assertEqual(r2.x, 9)
        self.assertEqual(r2.y, 12)
        self.assertEqual(r1.id, 15)

    def test_non_integer_values(self):
        """This tests that type error is raised for non-integer values."""
        with self.assertRaises(TypeError):
            Rectangle("3", 6, 4, 5)

        self.assertRaises(TypeError, Rectangle, 3, [6], 4, 5)

        with self.assertRaises(TypeError):
            Rectangle(3, 6, (4,), 5)

        with self.assertRaises(TypeError):
            Rectangle(3, 6, 4, set(5))

    def test_width_and_height_with_less_than_zero_value(self):
        """This tests that a value error is raised when a value that is
        less than or equal to zero is given width or height.
        """
        with self.assertRaises(ValueError):
            Rectangle(0, 100000)

        with self.assertRaises(ValueError):
            Rectangle(10000, 0)

        self.assertRaises(ValueError, Rectangle, -100000, 10)

        self.assertRaises(ValueError, Rectangle, 10000, -10)

    def test_x_and_y_with_less_than_zero_value(self):
        """This tests that a value error is raised when a value
        that is less than zero is given.
        """
        with self.assertRaises(ValueError):
            Rectangle(2, 3, -4, 5)

        with self.assertRaises(ValueError):
            Rectangle(2, 3, 4, -5)

    def test_area_method_computation(self):
        """This tests that a computed area is correct"""
        self.assertEqual(Rectangle(2, 3).area(), 6)
        r = Rectangle(2, 9)
        self.assertEqual(r.area(), 18)

    def test_the_string_implementation(self):
        """This tests the format of the str method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        self.assertTrue(isinstance(r1, Rectangle))
        self.assertFalse(str(r1) == str(r2))
        self.assertEqual(str(r1), '[{}] ({}) {}/{} - {}/{}'
                                  .format(r1.__class__.__name__,
                                          r1.id, r1.x, r1.y,
                                          r1.width, r1.height))
        self.assertEqual(str(r2), '[{}] ({}) {}/{} - {}/{}'
                                  .format(r2.__class__.__name__,
                                          r2.id, r2.x, r2.y,
                                          r2.width, r2.height))

    def test_update_method_with_args(self):
        """This tests that the update method updates the attributes of
        an instance in an orderly fashion using the args only.
        """
        r = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)
        r.update(111)
        self.assertEqual(r.id, 111)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)
        r.update(111, 30, 40, 50, 60)
        self.assertEqual(r.id, 111)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 40)
        self.assertEqual(r.x, 50)
        self.assertEqual(r.y, 60)

    def test_update_method_with_kwargs(self):
        """This tests that the update method updates the attributes of
        an instance by only the given attributes, which can be in any
        order, using the kwargs only.
        """
        r = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)
        r.update(id=111)
        self.assertEqual(r.id, 111)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)
        r.update(y=60, height=40, id=258, x=50, width=30)
        self.assertEqual(r.id, 258)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 40)
        self.assertEqual(r.x, 50)
        self.assertEqual(r.y, 60)
