#!/usr/bin/python3
start = 1
for number in range(0, 9):
    for inner_n in range(start, 10):
        if number == 8 and inner_n == 9:
            print("{}{}".format(number, inner_n))
        else:
            print("{}{},".format(number, inner_n), end=" ")
    start += 1
