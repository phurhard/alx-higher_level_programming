#!/usr/bin/python3
"""
Writes to a file, creates a file if it does not exist
oveerwrites a file if it exists
"""


def write_file(filename="", text=""):
    """ function to write to a file"""
    with open(filename, 'w', encoding='UTF8') as f:
        written = f.write(text)
    return written
