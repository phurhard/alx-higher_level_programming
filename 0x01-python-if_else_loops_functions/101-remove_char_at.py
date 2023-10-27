#!/usr/bin/python3
def remove_char_at(string, n):
    newstr = string
    newstr = str(newstr)
    return newstr if n < 0 or n > len(newstr) else (newstr[:n] + newstr[n+1:])
