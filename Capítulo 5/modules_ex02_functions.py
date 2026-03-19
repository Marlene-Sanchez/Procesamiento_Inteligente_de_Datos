#!/usr/bin/env python3

import sys

fmt = "Inside of Function: {} of module {}"


def one():
    print(fmt.format(one.__name__, __name__) + ", from path: " + str(sys.path[0]))


def two():
    print(fmt.format(two.__name__, __name__) + ", from path: " + str(sys.path[0]))


