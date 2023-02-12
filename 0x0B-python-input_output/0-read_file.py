#!/usr/bin/python3
"""
Opens a text file and prints to stdout
"""


def read_file(filename=""):
    """ Function to read input text file """
    with open(filename, 'r', encoding='UTF8') as f:
        for line in f:
            print(line)
