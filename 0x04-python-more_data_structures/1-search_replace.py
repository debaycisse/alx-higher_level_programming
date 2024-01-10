#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_copy = my_list.copy()
    if list_copy[:]:
        if search in list_copy:
            for num in list_copy:
                if num == search:
                    list_copy[list_copy.index(num)] = replace
            return list_copy
        return list_copy
    return list_copy
