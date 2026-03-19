#!/usr/bin/env python3

def deliver(a, b):
    def addthem():
        return a + b
    return addthem


f = deliver(10, 20)
print(f())
