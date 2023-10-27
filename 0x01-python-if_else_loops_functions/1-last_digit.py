#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number >= 0:
    ld_number = number % 10
    if ld_number > 5:
        print(f"Last digit of {number} is {ld_number} and is greater than 5")


    elif ld_number == 0:
        print(f"Last digit of {number} is {ld_number} and is 0")
    else:
        print(f"Last digit of {number} is {ld_number} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {number % -10} and is less than 6 and not 0")
