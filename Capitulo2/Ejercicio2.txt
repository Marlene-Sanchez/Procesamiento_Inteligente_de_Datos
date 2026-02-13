text = input("Ingresa un número de la suerte: ")
if not text.isnumeric():
    print("El valor que ingresaste no es un entero")
else:
    print("Tu número de la suerte", text, "tiene", len(text), "dígitos")