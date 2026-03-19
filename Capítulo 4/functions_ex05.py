#!/usr/bin/env python3

def get_values():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    return (x, y)


def add():
    x, y = get_values()
    print(f"{x}+{y}={x+y}\n")


def subtract():
    x, y = get_values()
    print(f"{x}-{y}={x-y}\n")


def multiply():
    x, y = get_values()
    print(f"{x}*{y}={x*y}\n")


def divide():
    x, y = get_values()
    print(f"{x}/{y}={x/y:.2f}\n")


def quit():
    print("Exiting...")
    exit()


def not_an_option():
    print("This calculator can't do that...\n")


calc = {"1": add, "2": subtract, "3": multiply, "4": divide, "5": quit}
while True:
    print("Calculator Options:")
    for key in calc:
        print(f"{key}. {calc[key].__name__.capitalize()}")
    choice = input("Choose an action: ")

    calc.get(choice, not_an_option)()
