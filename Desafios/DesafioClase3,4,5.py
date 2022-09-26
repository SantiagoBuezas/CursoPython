# Ejercicio 1

# Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:


#        1.	Mostrar una suma de los dos números
#        2.	Mostrar una resta de los dos números (el primero menos el segundo)
#        3.	Mostrar una multiplicación de los dos números
#        4.	Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
#        5.	En caso de no introducir una opción válida, el programa informará de que no es correcta.


numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("ingrese otro numero: "))

print(f"Los numeros que usted ingreso son {numero_1} y {numero_2}")

menu_principal = int(input("Menu principal:\n 1- Sumar los dos numeros \n 2- Restar el primero con el segundo \n 3- La multiplicacdion de los dos numeros \n 4- Salir \n Ingrese el numero de la opcion deseada: "))

while menu_principal != 4:

    if menu_principal == 1:
        print(f"{numero_1} + {numero_2}")
        suma_de_numeros = numero_1 + numero_2
        print(f"El resultado de sumar los numeros es {suma_de_numeros}")
    elif menu_principal == 2:
        print(f"{numero_1} - {numero_2}")
        resta_de_los_numeros = numero_1 - numero_2
        print(f"El resultado de restar el primer numero con el segundo es {resta_de_los_numeros}")
    elif menu_principal == 3:
        print(f"{numero_1} * {numero_2}")
        multiplicacion_de_los_numeros = numero_1 * numero_2
        print(f"El resultado de multiplicar ambos numeros es {multiplicacion_de_los_numeros}")
    else:
        print("El numero elegido no es correcto")

    menu_principal = int(input("Menu principal:\n 1- Sumar los dos numeros \n 2- Restar el primero con el segundo \n 3- La multiplicacdion de los dos numeros \n 4- Salir \n Ingrese el numero de la opcion deseada: "))


print("Muchas gracias")

# Ejercicio 2

# Escribí un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.


intentos = 2

while intentos < 10:
    numero = int(input("ingrese un numero impar porfavor: "))
    if numero % 2 != 0:
        print("Muchas gracias por introducir un numero impar")
        break

# Ejercicio 3

# Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100:

#🖐 Ayuda: Podes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números.

lista = list(range(1,101,2))

print(lista)

print(f"La suma de todos los numeros impares del 0 al 100 es {sum(lista)}")

# Ejercicio 4

# Escribí un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:

intento = 0
lista = []

numero = int(input("Cuantos numeros quiere ingresar: "))

while intento < numero:
    intento += 1
    numero_para_lista = int(input("ingrese un numero: "))
    lista.append(numero_para_lista)

media_aritmetica = float(sum(lista) / numero)

print("Los numero que ingreso son:")

for elemento in lista:
    print(elemento)

print(f"La media aritmetica de todos los numeros que ingreso es: {media_aritmetica}")

# Ejercicio 5

# Escribí un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. 
# Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

# 🖐 Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)


numeros = [1, 3, 6, 9]

intentos = 1

while intentos < 3:
    numero_ingresado = int(input("Ingrese un numero del 0 al 9: "))
    if numero_ingresado >= 0 and numero_ingresado <= 9:
        resultado = numero_ingresado in numeros
        if resultado == True:
            print("El numero ingresado se encuentra en la lista de numeros")
        break
    else:
        print("El numero que ingreso no pertenece al rango solicitado")

print("El programa fonalizo correctamente")


# Ejercicio 6

# Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

#	Todos los números del 0 al 10 [0, 1, 2, ..., 10]
#	Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
#	Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
#	Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
#	Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

# 🖐 Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto))
     
primera_lista = list(range(0,11))
print(f"Primera lista = {primera_lista}")

segunda_lista = list(range(-10,1))
print(f"Segunda lista = {segunda_lista}")

tercera_lista = list(range(0,21,2))
print(f"Tercera lista = {tercera_lista}")

cuarta_lista = list(range(-19,1,2))
print(f"Cuarta lista = {cuarta_lista}")

quinta_lista = list(range(0,51,5))
print(f"Quinta lista = {quinta_lista}")

print("Muchas gracias, el programa termino correctamente")

# Ejercicio 7

# Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:

from collections import OrderedDict

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

lista_3 = lista_1 + lista_2

lista_3_sin_repetirse = list(OrderedDict.fromkeys(lista_3))

print(lista_3_sin_repetirse)

