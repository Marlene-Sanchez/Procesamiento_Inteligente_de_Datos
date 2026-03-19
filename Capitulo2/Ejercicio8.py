num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if num1 > num2:
    num1, num2 = num2, num1 

suma = 0
for i in range(num1, num2 + 1):
    suma += i

print(f"La suma de {num1} hasta {num2} es: {suma}")