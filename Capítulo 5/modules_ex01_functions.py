#!/usr/bin/env python3


fmt = "Inside of Function: {} of module {}"


def one():
    print(fmt.format(one.__name__, __name__))


def two():
    print(fmt.format(two.__name__, __name__))
