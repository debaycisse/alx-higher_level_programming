#!/usr/bin/python3
"""This module contains a set of test to validate
the requirements for the Base class.
"""


import os
import sys
import unittest


sys.path.append(os.getcwd())
from models.base import Base


class TestBase(unittest.TestCase):
    """This class contains a set of test cases for the Base class."""

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
