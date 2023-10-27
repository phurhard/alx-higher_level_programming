#!/usr/bin/python3
def lower(c):
    char = ord(c)
    if char >= 97 and char <= 123:
        print(f"{c} is {ord(c)}")
    else:
        print(f"Character{c} is upper {ord(c)}")
lower("a")
lower("A")
