#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    treated = 0
    i = 0
    try:
        while i < x:
            print(f"{my_list[i]}", end="")
            treated += 1
            i += 1
        print("")
        return (treated)
    except IndexError:
        print("")
        return (treated)

