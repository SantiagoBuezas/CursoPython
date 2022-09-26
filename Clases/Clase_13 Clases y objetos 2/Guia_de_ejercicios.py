# Ejercicio 1
# Implementar una clase Gato que se inicialice con un nombre. 
# Agregarle la acción hablar, cuando se llame a esta acción, el código debe imprimir en la consola el mensaje


class Gato:
    especie = "Gato"

    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print(f"Miau!soy un {self.especie}")

mi_gato = Gato("Pancho")
mi_gato.hablar()

# Ejercicio 2
# Modificar la clase anterior de forma tal que cuando "hagamos hablar" al gato, nos salude de la siguiente manera:
# Miau! soy un gato y mi nombre es Pancho
# Extra: lograr imprimir el nombre del gato siempre en mayúscula independientemente de cómo lo haya ingresado el usuario, tal como en el ejemplo anterior.

class Gato:
    especie = "Gato"

    def __init__(self, nombre):
        nombre = nombre.title()
    
        self.nombre = nombre
    
    def hablar(self):
        print(f"Miau!soy un {self.especie} y mi nombre es {self.nombre}")

mi_gato = Gato("pipo chipolati")
mi_gato.hablar()

# Ejercicio 3
# Modificar la clase anterior para obtener el siguiente comportamiento:

# mi_gato = Gato("pancho")
# print(mi_gato)

# >> Soy un objeto de la clase Gato y me llaman Pancho

class Gato:
    especie = "Gato"

    def __init__(self, nombre):
        nombre = nombre.title()
    
        self.nombre = nombre
    
    def hablar(self):
        print(f"Miau!soy un {self.especie} y mi nombre es {self.nombre}")

    def __str__(self):
        return f"Soy un objeto de la clase {self.especie} y me llaman {self.nombre}"

mi_gato = Gato("pipo chipolati")
print(mi_gato)


