# Quiero leer el contenido del archivo test.txt

mi_archivo = open("test.txt", "w")

lineas_del_archivo = mi_archivo.read()


print("Elcontenido de mi archivo es: ", lineas_del_archivo)