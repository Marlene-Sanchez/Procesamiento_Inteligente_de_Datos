#!/usr/bin/env python3

from sys import argv

argv.pop(0)
argv.sort()
for arg in argv:
    print(arg)
