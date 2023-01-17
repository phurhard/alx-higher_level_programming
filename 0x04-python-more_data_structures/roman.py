#!/usr/bin/python3
def roman(roman_str):
    sumi = 0
    roman_numerals = {'X':10, 'I':1, 'V':5, 'L':50, 'D':500, 'C':100, 'M':1000, }

    for i in range(len(roman_str)):
        if roman_str[i] in roman_numerals:
            if len(roman_str) == 2:
                if i+1 != len(roman_str):
                    if roman_numerals[roman_str[i]] < roman_numerals[roman_str[i+1]]:
                        sumi = roman_numerals[roman_str[i+1]] - roman_numerals[roman_str[i]]
                    else:
                        sumi += int(roman_numerals[roman_str[i]])
                else:
                    if roman_numerals[roman_str[i]] > roman_numerals[roman_str[i-1]]:
                        sumi = sumi
                    else:
                        sumi += int(roman_numerals[roman_str[i]])

            elif len(roman_str) > 2:
                if i+1 != len(roman_str):
                    if roman_numerals[roman_str[i]] < roman_numerals[roman_str[i+1]]:
                        sumo = int(roman_numerals[roman_str[i+1]]) - int(roman_numerals[roman_str[i]])
                        sumi += sumo
                    


                    else:
                        sumi += int(roman_numerals[roman_str[i]])
                else:
                    sumi += int(roman_numerals[roman_str[i]])
            else:
                sumi += int(roman_numerals[roman_str[i]])
    return sumi
