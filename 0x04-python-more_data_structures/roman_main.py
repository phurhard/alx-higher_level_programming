#!/usr/bin/python3
""" Roman to Integer test file
"""

roman_to_int = __import__('roman').roman

roman_number = "X"
print(f"{roman_number} = {roman_to_int(roman_number)}")

roman_number = "VII"
print(f"{roman_number} = {roman_to_int(roman_number)}")

roman_number = "IX"
print(f"{roman_number} = {roman_to_int(roman_number)}")

roman_number = "XI"
print(f"{roman_number} = {roman_to_int(roman_number)}")

roman_number = "VI"
print(f"{roman_number} = {roman_to_int(roman_number)}")

roman_number = "IV"
print(f"{roman_number} = {roman_to_int(roman_number)}")

roman_number = "LXXXVII"
print(f"{roman_number} = {roman_to_int(roman_number)}")

roman_number = "DCCVII"
print(f"{roman_number} = {roman_to_int(roman_number)}")

roman_number = "CM"
print(f"{roman_number} = {roman_to_int(roman_number)}")

roman_number = "CMV"
print(f"{roman_number} = {roman_to_int(roman_number)}")

roman_number = "DCCXCV"
print(f"{roman_number} = {roman_to_int(roman_number)}")

roman_number = "DCCC"
print(f"{roman_number} = {roman_to_int(roman_number)}")

roman_number = "CDLXXXV"
print(f"{roman_number} = {roman_to_int(roman_number)}")

