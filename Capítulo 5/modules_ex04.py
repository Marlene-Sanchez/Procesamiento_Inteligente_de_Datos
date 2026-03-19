#!/usr/bin/env python3

from sys import argv

total = 0
for item in argv[1:]:
    total += float(item)

print("Total:", total)
print("Average:", total / (len(argv) - 1))
