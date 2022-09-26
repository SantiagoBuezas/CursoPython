

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

############################################################################################################

numero1 = 0

while numero1 < 10:
    numero1 += 1

    if numero1 == 2:
        pass
	
        print("numero vale: " +  str(numero1)) 

############################################################################################################

lista = [1,2,3,4,5]

for valor in lista:
    print(f"Soy un item de la lista y valgo {valor}")

############################################################################################################

lista = list(range(11))

for numero in lista:
    print("Soy un valor de la lista y valgo " + str(numero))
    numero *= 5
    print("Soy un valor de la lista y ahora valgo " + str(numero))

############################################################################################################

paises = ["Canada", "USA","Mexico","Australia","Argentina","China","India"]

for indice, pais in enumerate(paises):
    print(f"{indice +1} {pais}")

############################################################################################################

numero = 0
suma_de_numeros_pares = 0

while numero < 100:
    numero += 1
    if (numero % 2 == 0):
        print(f"{suma_de_numeros_pares} + {numero}")
        suma_de_numeros_pares = suma_de_numeros_pares + numero
        print(suma_de_numeros_pares)

############################################################################################################

numero = 10

while numero > 0:
    print(numero)
    numero -= 1

############################################################################################################

cantida_de_digitos_del_numero = len(str(numero))

print(f"El numero que ingreso es {numero} y la cantidad de digitos totales de dicho numero es {cantida_de_digitos_del_numero}")