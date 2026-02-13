for n in range(50):
    if n <= 9:
        print(" ", end="")
    print("", n, end="")
    if n % 10 == 9:
        print()

print()