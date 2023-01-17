#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for k,v in a_dictionary.items():
        v *=2
        new_dict[k] = v
    return new_dict
