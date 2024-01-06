#!/usr/bin/python3


def fizzbuzz():
    for num in range(1, 101):
        fizz = num % 3 == 0
        buzz = num % 5 == 0
        if fizz and buzz:
            print("FizzBuzz", end=" ")
        elif fizz:
            print("Fizz", end=" ")
        elif buzz:
            print("Buzz", end=" ")
        else:
            print(num, end=" ")
