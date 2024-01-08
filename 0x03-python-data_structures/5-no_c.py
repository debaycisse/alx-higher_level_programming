def no_c(my_string):
    if len(my_string) <= 0:
        return my_string
    else:
        c = {ord('c'): None}
        C = {ord('C'): None}
        new_str = my_string.translate(c)
        new_str = new_str.translate(C)
        return new_str
