# Programa las siguientes instrucciones de forma ordenada sobre la variable grupo:

# Añade los usuarios: Ana, Ramón, Marta, Eric, David
# Elimina los usuarios: Mario, Miguel, Esteban



grupo = {"Miguel", "Blanca", "Mario", "Andrés"}
print(grupo)

grupo.update(["Ana","Ramon","Marta","Eric","David"])
print(grupo)

grupo.discard("Mario")
grupo.discard("Miguel")
grupo.discard("Esteban")
print(grupo)

# Tiempo estimado:10 minutos
# Programa las siguientes instrucciones de forma ordenada sobre la variable animales:

# Inicialmente el diccionario es: animales = {"elefante": ""}

# Añade al diccionario las claves perro, tigre y mono con sus respectivos valores “Bobby”,  “Peepe” y “homero”
# Modificá las claves elefante y delfin con los valores “Trompis”y “Manolo” respectivamente

animales = {"elefante": ""}
print(animales)

animales.update({"perro":"Bobby","tigre":"Peepe","mono":"homer"})
print(animales)

animales["elefante"] = "Trompis"
animales["delfin"] = "Manolo"
print(animales)