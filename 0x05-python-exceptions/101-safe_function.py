#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        a, b = args
        return (fct(a, b))
    except Exception as e:
        print("Exception: {}".format(e), file=stderr)
        return (None)
