#!/usr/bin/python3
import dis
def magic_calculation(a, b):
    a = input("Enter the script: \n")
    print(f"{dis.dis(a,b)}")
