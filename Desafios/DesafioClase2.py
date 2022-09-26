"Ejercicio 2"

a=10
b=-5
c="hola"
d=[1,2,3]
e=(4,5,6)

print(f"a*5 es igual a {a*5}")
print(f"a-b es igual a {a-b}")
print(f"c+'Mundo' es igual a {(c+'Mundo')}")
print(f"c*2 es igual a {c*2}")
print(f"c[-1] es igual a {c[-1]}")
print(f"c[1:] es igual a {c[1:]}")    
print(f"d + d es igual a {d + d}")       
print(f"e[1] es igual a {e[1]}")
print(f"e+(7,8,9) es igual a {e+(7,8,9)}")

"Ejercicio 3"

numero_1 = 9
numero_2 = 3
numero_3 = 6

media_2 = (numero_1 + numero_2 + numero_3) / 3
print("La nota media es", media_2)


"Ejercicio 4"

"La primera nota vale un 15% del total"
"la segunda nota vale un 35% del total"
"La tercera nota vale un 50% del total"

nota_1 = 10
nota_2 = 7
nota_3 = 4

media = (nota_1 + nota_2 + nota_3) / 3
nota_1_preponderada = (media * 0.15)
nota_2_preponderada = (media * 0.35)
nota_3_preponderada = (media * 0.50)

print(f"La nota media nueva es {media}")
print(f"El equivalente del 15% del total correspondiente a la primera nota es {nota_1_preponderada}")
print(f"El equivalente del 35% del total correspondiente a la segunda nota es {nota_2_preponderada}")
print(f"El equivalente del 50% del total correspondiente a la tercera nota es {nota_3_preponderada}")

"Ejercicio 5"

"🖐 Ayuda:  La función llamada sum(list) devuelve una suma de todos los elementos de la lista"

matriz = [ 
    [1, 5, 1], 
    [2, 1, 2], 
    [3, 0, 1], 
    [1, 4, 4] 
]

matriz [0].append (sum(matriz[0]))
matriz [1].append (sum(matriz[1]))
matriz [2].append (sum(matriz[2]))
matriz [3].append (sum(matriz[3]))


"""

matriz [0] = [1,5,1,sum(matriz[0])]
matriz [1] = [2,1,2,sum(matriz[1])]
matriz [2] = [3,0,1,sum(matriz[2])]
matriz [3] = [1,4,4,sum(matriz[3])]

"""
print(matriz)
