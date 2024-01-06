#!/usr/bin/python3


def print_last_digit(number):
    remainder = number % 10
    if number < 0:
        remainder = number % (-10)
        remainder *= (-1)
    print(f"{remainder}", end="")
    return remainder
