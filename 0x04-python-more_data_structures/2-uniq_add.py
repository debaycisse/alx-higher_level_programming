#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list[:]:
        uniq_n = set(my_list)
        sum = 0
        for num in uniq_n:
            sum += num
        return sum
    return 0
