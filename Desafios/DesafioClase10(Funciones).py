# 1) Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura.
#  Calcula el área de un rectángulo de 15 de base y 10 de altura


# 🖐 Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.


def area_rectangulo(base, altura):
    area_del_rectangulo = base * altura
    return area_del_rectangulo

print(area_rectangulo(5,10) == 50)
print(area_rectangulo(2,6) == 12)
print(area_rectangulo(7,14) == 98)

# 2) Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio

# 🖐 Ayuda: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. 
# Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math.

pi = 3.14159

def area_circulo(radio):
    area_del_criculo = (radio**2) * pi   
    return area_del_criculo


print(area_circulo(1) == 3.14159)
print(area_circulo(0) == 0)
print(area_circulo(10) == 314.159)


#3) Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

# Si el primer número es mayor que el segundo, debe devolver 1.
# Si el primer número es menor que el segundo, debe devolver -1.
# Si ambos números son iguales, debe devolver un 0.

# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'


def relacion(numero_uno,numero_dos):
    if numero_uno > numero_dos:
        return 1
    elif numero_uno < numero_dos:
        return -1
    else:
        return 0


# Si el primer número es mayor que el segundo, debe devolver 1.
print(relacion(10,5) == 1)
print(relacion(10,9) == 1)
print(relacion(-5,-12) == 1)
print(relacion(152,124) == 1)

# Si el primer número es menor que el segundo, debe devolver -1.
print(relacion(7,12) == -1)
print(relacion(1,2) == -1)
print(relacion(-152,-9) == -1)
print(relacion(5,10) == -1)

# Si ambos números son iguales, debe devolver un 0.
print(relacion(8,8) == 0)
print(relacion(-100,-100) == 0)
print(relacion(0,0) == 0)
print(relacion(5,5) == 0)

# 4) Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:

# 🖐 Ayuda: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

# Comprueba el punto intermedio entre -12 y 24




def intermedio(numero_uno, numero_dos):
    punto_intermedio = ((numero_uno + numero_dos) / 2)
    return punto_intermedio

print(intermedio(-12, 24) == 6 )

print(intermedio(2,4) == 3 )
print(intermedio(8,2) == 5 )
print(intermedio(6,2) == 4 )

# 5) Realizá una función llamada recortar() que reciba tres parámetros.
# El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:
# Si el limite inferior es mayor o igual que el limite superior, devolver un ValueError con el mensaje "Limites Incorrectos"

# Devolver el límite inferior si el número es menor que éste
# Devolver el límite superior si el número es mayor que éste.
# Devolver el número sin cambios si no se supera ningún límite.

# Comprueba el resultado de recortar 15 entre los límites 0 y 10


def recortar(numero_a_recortar, limite_inferior,limite_superior):
    
    if limite_inferior >= limite_superior:
        raise ValueError("Limites Incorrectos")
    
    elif numero_a_recortar < limite_inferior:
        return limite_inferior
    elif numero_a_recortar > limite_superior:
        return limite_superior
    else:
        return numero_a_recortar


# Devolver el límite inferior si el número es menor que éste
print(recortar(0,1,2) == 1)
print(recortar(-6,-5,100) == -5)
print(recortar(11,12,14) == 12)

# Devolver el límite superior si el número es mayor que éste.
print(recortar(0,-2,-1) == 1)
print(recortar(5,1,4) == 4)
print(recortar(10,8,9) == 1)

# Devolver el número sin cambios si no se supera ningún límite.
print(recortar(0,-1,1) == 0)
print(recortar(5,1,40) == 5)
print(recortar(10,100,-100) == 10)


# 6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas.
# La primera con los números pares, y la segunda con los números impares:

#🖐 Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()

# Por ejemplo:

# pares, impares = separar([6,5,2,1,7])
# print(pares)   # valdría [2, 6]
# print(impares)  # valdría [1, 5, 7]

pares = []
impares = []


def separar(una_lista):
    lista_ordenada = sorted(una_lista)
    for elemento in lista_ordenada:
        if (elemento % 2) == 0: 
            pares.append(elemento)
           
        elif (elemento % 2) !=0:
            impares.append(elemento)       

separar([6,5,2,1,7])
print(pares)
print(impares)
