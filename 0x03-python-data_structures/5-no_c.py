def no_c(my_string):
    if my_string:
        new_str = my_string.translate({ord("c"): None})
        new_str2 = new_str.translate({ord("C"): None})
        return new_str2
    return my_string
