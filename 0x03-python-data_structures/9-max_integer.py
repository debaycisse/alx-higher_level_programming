#!/usr/bin/python3
def max_integer(my_list=[]):
    temp = 0
    if len(my_list) > 0:
        for num in my_list:
            if num > temp:
                temp = num
        return temp
    return None
