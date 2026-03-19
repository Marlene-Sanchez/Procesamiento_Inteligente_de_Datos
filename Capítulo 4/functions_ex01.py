#!/usr/bin/env python3

def validate_input():
    value = input("Enter a positive integer: ")
    if value.isnumeric():
        return int(value)
    else:
        return 0


result = validate_input()
if not result:
    print("Invalid entry given.")
