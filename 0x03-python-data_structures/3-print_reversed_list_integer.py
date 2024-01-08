#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_l = [my_list[len(my_list) - (x + 1)] for x in range(len(my_list))]
    for i in range(len(new_l)):
        print("{}".format(new_l[i]))
