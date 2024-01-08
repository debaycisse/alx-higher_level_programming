def no_c(my_string):
    if my_string[:]:
        new_str = ""
        for ch in my_string:
            new_str += ch if ord(ch) != 67 and ord(ch) != 99 else ''
        return new_str
    return my_string
