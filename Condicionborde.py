numero = int(input("Ingresa un número entre 1 y 100: "))

if numero == 1 or numero == 100:
    print("Estas dentro del limite permitido")
elif numero > 1 and numero < 100:
    print("Estas dentro del rango permitido")
else:
    print("Estas fuera de rango")
