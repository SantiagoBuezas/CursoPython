intento = 1
lista = []


while intento <= 3:
    numero = int(input("Ingresa un numero: "))
    if numero != 0:
        lista.append(numero)
    elif numero == 0:
        print(f"{lista}")
        print(f"La suma de los numeros que ingresaste es: {sum(lista)}")
        break 