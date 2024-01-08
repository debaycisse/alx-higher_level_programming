#!/usr/bin/python3
def element_at(my_list, idx):
    l_length = len(my_list) - 1
    if idx < 0 or idx > l_length:
        return None
    else:
        return my_list[idx]
