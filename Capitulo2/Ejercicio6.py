bajo = int(input("Límite inferior: "))
alto = int(input("Límite superior: "))
paso = int(input("Paso (step): "))

for n in range(bajo, alto + 1, paso):
    print(n)