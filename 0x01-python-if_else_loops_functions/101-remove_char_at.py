#!/usr/bin/python3
def remove_char_at(string, n):
    newstr = string
    newstr = str(newstr)
    if n < 0:
        return (newstr)
    elif n > len(newstr):
        return (newstr)
    elif n >= 0:
        return (newstr[:n] + newstr[n+1:])
