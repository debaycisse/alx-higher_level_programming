#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        keys = [key for key in a_dictionary.keys()]
        for key in keys:
            if a_dictionary[key] == value:
                del a_dictionary[key]
    return (a_dictionary)
