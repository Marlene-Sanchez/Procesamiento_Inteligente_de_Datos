#!/usr/bin/env python3

def get_sum_avg(*args):
    total = sum(args)
    return(total, total/len(args))


total, avg = get_sum_avg(9, 8, 7)
print(f"sum of 9, 8, 7 is {total}, average is {avg}")
avg, total = get_sum_avg(17, 10, 3, 5, 1, 6)
print(f"sum of 17, 10, 3, 5, 1, 6 is {total}, average is {avg}")
