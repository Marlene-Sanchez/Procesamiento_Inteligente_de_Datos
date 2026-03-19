n1 = int(input("Primer número: "))
n2 = int(input("Segundo número: "))

if n1 > n2:
    print(f"El mayor es: {n1}")
elif n2 > n1:
    print(f"El mayor es: {n2}")
else:
    print("Los números son iguales.")