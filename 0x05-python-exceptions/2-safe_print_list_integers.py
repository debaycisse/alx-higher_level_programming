#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    treated = 0
    while (i < x):
        try:
            try:
                print("{:d}".format(my_list[i]), end="")
                treated += 1
                i += 1
            except ValueError as e1:
                raise TypeError from None
        except TypeError as e2:
            i += 1
    print("")
    return (treated)
