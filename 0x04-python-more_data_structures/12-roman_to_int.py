#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    rs = roman_string
    rt = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
          'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    i = 0
    while i < len(rs):
        if rs[i] in rt:
            f_num = rt[rs[i]]
            s_num = (rt[rs[i + 1]] if i + 1 < len(rs) else 0)
            if f_num > s_num:
                sum += f_num
                i += 1
            elif s_num > f_num:
                sum += s_num - f_num
                i += 2
            else:
                sum += f_num
                i += 1
    return sum
