def no_c(my_string):
    if len(my_string) <= 0:
        return my_string
    else:
        n_str = ""
        for letter in my_string:
            if ord(letter) == ord("C"):
                pass
            elif ord(letter) == ord("c"):
                pass
            else:
                n_str += letter
    return n_str
