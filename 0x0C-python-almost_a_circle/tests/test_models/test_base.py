#!/usr/bin/python3
"""This module contains a set of test to validate
the requirements for the Base class.
"""


import os
import sys
import unittest


sys.path.append(os.getcwd())
try:
    from models.base import Base
    from models.rectangle import Rectangle
    from models.square import Square
except Exception as e:
    print(e)


class TestBase(unittest.TestCase):
    """This class contains a set of test cases for the Base class."""

    def setUp(self):
        """This sets up the environment for each test case"""
        Base.reset_class()

    def test_no_id(self):
        """This method tests that an instance without an id attribute
        can be created."""
        print(sys.path)
        b = Base()
        self.assertTrue(b.id == 1)

    def test_no_id(self):
        """This method tests that an instance with an id attribute
        can be created."""
        b = Base(76)
        self.assertTrue(b.id == 76)
        self.assertEqual(Base(102).id, 102)

    def test_id_type_is_integer(self):
        """This method tests that the type of id attribute is integer"""
        self.assertFalse(isinstance(Base().id, float))
        self.assertTrue(isinstance(Base().id, int))

    def test_existence_of_nb_objects_class_variable(self):
        """This tests that the nb_objects class variable exists and that
        it increases as more instances without id are created.
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def tearDown(self):
        Base.reset_class()

    def test_to_json_string_method(self):
        """This tests that to_json_string method returns the correct data"""
        r = Rectangle(1, 2, 3, 4, 5)
        r_dict = r.to_dictionary()
        r_json_str = Base.to_json_string([r_dict])
        self.assertTrue(isinstance(r_json_str, str))
	self.assertEqual([{"x": 3, "width": 1, "id": 5, "height": 2, "y": 4}],
                         r_json_str)
        s = Square(9, 8, 7, 6)
        s_dict = s.to_dictionary()
        s_json_str = Base.to_json_string([s_dict])
        self.assertTrue(isinstance(s_json_string, str))
	self.assertEqual([{"id": 6, "x": 8, "size": 9, "y": 7}], s_json_string)

    def test_from_json_string_method(self):
        """This tests that a json_string data is converted to python equivalent"""
        list_input = [
                      {'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}
                     ]
        
        r_json_string = Rectangle.to_json_string(list_input)
        r_python_form = Rectangle.from_json_string(r_json_string)
        self.assertEqual(list_input, r_python_form)
