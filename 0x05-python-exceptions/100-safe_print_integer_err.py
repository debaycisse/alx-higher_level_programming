#!/usr/bin/python3
from sys import stderr as s


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as e:
        print("Exception: {}".format(e), file=s)
        return (False)
