#!/usr/bin/python3
def lower(c):
    char = ord(c)
    if char >= 97 and char <= 123:
        print("{} is {}".format(c, ord(c)))
    else:
        print("Character{} is upper {}".format(c, ord(c)))
lower("a")
lower("A")
