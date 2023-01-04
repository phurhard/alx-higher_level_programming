#!/usr/bin/python3
def uppercase(str):
    stri = str
    for i in stri:
        vi = ord(i)
        if vi >= 97 and vi <= 122:
            vi = vi - 32
        print("{}".format(chr(vi)), end="")
    print("\n")
