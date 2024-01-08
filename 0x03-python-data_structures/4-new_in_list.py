#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or type(idx) != int:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    new_l = []
    for i in range(len(my_list)):
        if i == idx:
            new_l.append(element)
        else:
            new_l.append(my_list[i])
    return new_l
