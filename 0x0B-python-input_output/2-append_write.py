#!/usr/bin/python3
"""
Appends a text to a file
"""


def append_write(filename="", text=""):
    """ Append text to a text file creates if file is not available"""
    with open(filename, 'a', encoding='UTF8') as f:
        written = f.write(text)
    return written
