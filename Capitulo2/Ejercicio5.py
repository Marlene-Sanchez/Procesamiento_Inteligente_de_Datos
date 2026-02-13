entrada = input("Ingresa varios números separados por espacio: ")
nums = entrada.split()

for n in nums:
    numero = float(n)
    if numero > 0:
        print(numero,end=" ")
print()