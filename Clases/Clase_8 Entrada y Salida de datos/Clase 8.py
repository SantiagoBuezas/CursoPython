# Crear y escribir un archivo

import random

mi_variable_aleatoria = random.random()

print(mi_variable_aleatoria)

mi_archivo = open("otro_archivo.txt", "w")

mi_archivo.write(input("Escriba aqui su texto: "))

