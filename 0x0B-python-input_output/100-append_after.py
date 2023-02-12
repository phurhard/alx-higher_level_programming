#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r+') as f:
        lines = f.readlines()
    for line in lines:
        if search_string in line:
            
