#!/usr/bin/python3
def uniq_add(my_list=[]):
    Sum = 0
    uniq = set(my_list)
    for i in uniq:
        Sum += i
    return Sum
