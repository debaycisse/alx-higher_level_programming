#!/usr/bin/python3
"""This is a module for the text_indentation function.

This module contains the implementation of the
programming logic for the function
"""


def text_indentation(text):
    """This function prints a text with 2 new lines after
    each of these characters: ., ? and :

    Args:
        text: this is the string to be operated on

    Raises:
        TypeError: this is raised if the text's type is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    scanned = ""
    for ch in text:
        if ch in ['.', ':', '?']:
            scanned += ch
            print("{}\n".format(scanned.strip()))
            scanned = ""
        else:
            scanned += ch
    print("{}".format(scanned.strip()), end="")
