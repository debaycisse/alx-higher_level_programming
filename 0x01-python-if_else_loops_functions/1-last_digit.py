#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = number % 10
if number < 0:
    last_d = number % (-10)
    if (last_d == 0):
        print("Last digit of {} is {} and {}".format(number, last_d, "is 0"))
    elif (last_d < 6) and (last_d != 0):
        print("Last digit of {} is {} and {}"
              .format(number, last_d, "is less than 6 and not 0"))
else:
    if (last_d > 5):
        print("Last digit of {} is {} and {}"
              .format(number, last_d, "is greater than 5"))
    elif (last_d == 0):
        print("Last digit of {} is {} and {}".format(number, last_d, "is 0"))
    elif (last_d < 6) and (last_d != 0):
        print("Last digit of {} is {} and {}"
              .format(number, last_d, "is less than 6 and not 0"))
