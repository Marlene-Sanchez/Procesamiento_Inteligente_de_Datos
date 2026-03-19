#!/usr/bin/env python3

def get_sum(*args):
    return sum(args)


print(f"sum of 9, 8, 7 is {get_sum(9, 8, 7)}")
print(f"sum of 17, 10, 3, 5, 1, 6 is {get_sum(17, 10, 3, 5, 1, 6)}")
