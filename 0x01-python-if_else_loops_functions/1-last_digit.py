#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number > 0:
    ld_number = number % 10
    if ld_number > 5:
        print("Last digit of {} is {} and is \
                greater than 5".format(number, ld_number))
    elif ld_number == 0:
        print("Last digit of {} is {} and \
                is 0".format(number, ld_number))
    else:
        print("Last digit of {} is {} and is\
                less than 6 and not 0".format(number, ld_number))
else:
    print("Last digit of {} is {} and is less \
            than 6 and not 0".format(number, number % -10))
