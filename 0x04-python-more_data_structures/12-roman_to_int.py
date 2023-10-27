#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numerals = {'X':10, 'I':1, 'V':5, 'L':50, 'D':500, 'C':100, 'M':1000, }
    sum = 0
    if type(roman_string) != str or roman_string is None:
        return 0
    for i in roman_string:
        if i in roman_numerals:
            sum += int(roman_numerals[i])
    return sum
