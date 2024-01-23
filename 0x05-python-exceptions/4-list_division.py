#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        i = 0
        my_list = []
        result = 0.0
        while i < list_length:
            try:
                try:
                    result = my_list_1[i] / my_list_2[i]
                    my_list.append(result)
                    i += 1
                except ZeroDivisionError:
                    print("division by 0")
                    my_list.append(0)
                    i += 1
                except ValueError as exc:
                    raise TypeError from exc
                except IndexError:
                    print("out of range")
                    my_list.append(0)
                    i += 1
            except TypeError:
                print("wrong type")
                my_list.append(0)
                i += 1
    except Exception:
        pass
    finally:
        return (my_list)
