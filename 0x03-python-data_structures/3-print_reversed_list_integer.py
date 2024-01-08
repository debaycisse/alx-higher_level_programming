#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) >= 1:
        new_l = [my_list[len(my_list) - (x + 1)] for x in range(len(my_list))]
        for i in new_l:
            print("{:d}".format(i))
