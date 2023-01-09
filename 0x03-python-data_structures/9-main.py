#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
listt = [0,2,4,5,2,154,4,6768,34,4,56,34]
max_value = max_integer(my_list)
m = max_integer(listt)
print("Max: {}".format(max_value))
print("Max: {}".format(m))
