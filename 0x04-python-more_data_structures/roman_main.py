#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('roman').roman

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CM"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CMV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCXCV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCC"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CDLXXXV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

