#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        s_keys = sorted(a_dictionary)
        s_dict = dict()
        for key in s_keys:
            s_dict.update({key: a_dictionary[key]})
        for key, value in s_dict.items():
            print("{}: {}".format(key, value))
    else:
        print("{}")
