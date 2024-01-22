#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    treated = 0
    try:
        while (i < x):
            print("{:d}".format(list[i]), end="")
            treated += 1
            i += 1
        print("")
        return (treated)
    except TypeError:
        while (i < x):
            i += 1
            print("{:d}".format(list[i]), end="")
            treated += 1
        print("")
        return (treated)
    except IndexError:
        IndexError("list index out of range")
