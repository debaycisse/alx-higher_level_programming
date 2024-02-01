#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class is a unittest class that contains two test methods.

    Each of these test methods tests the max_integer function to
    ensure that it meets a given requirement.
    """
    def test_integer(self):
        """This method tests the max_integer using doctest syntax.

        It tests 3 different use cases.
        """
        """
        >>> max_integer([23, 45, 67, 43, 89, 2234, 123, 534, 9])
        2234
        >>> max_integer([-56, 44, 23, 34])
        44
        >>> max_integer([])
        None
        """

    def test_others(self):
        """This method tests the max_integer using unittest syntax.

        It tests 3 different use cases.
        """
        self.assertEqual(max_integer([23, 43, 89, 2234, 534]), 2234)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-56, 44, 23, 34]), 44)
