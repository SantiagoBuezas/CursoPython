# Crear una clase Atleta, que tenga su nombre, apellido, altura,  peso, teléfono e índice de masa corporal (descripción) . 
# Decidir qué atributos deben ser públicos y cuáles privados. Crear los métodos get y set que crea necesarios.
# Formula Indice Masa Corpaoral = peso / Estatura * Estatura

class Atleta:

    def __init__(self, nombre, apellido, altura, peso, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.altura = altura
        self.peso = peso
        self.telefono = telefono
    
    def IMC (self):
        IMC = self.peso / self.altura**2
        if IMC < 18.5:
            return "Peso Inferior"
        elif IMC >= 18.5 and IMC < 24.9:
            return "Normal"
        elif IMC >= 25.0 and IMC < 29.9:
            return "Sobrepeso"
        elif IMC >= 30.0 and IMC < 34.9:
            return "Obesidad"
        else:
            return "Obesisda Extrema"

santiago = Atleta("Santiago","Buezas", 1.78, 96, 46274489)

print(santiago.IMC())

##############################################################################################################

class Persona:

    piernas = 2
    brazos = 2
    sombre = True

    def __init__(self,nombre,fecha_de_nacimiento):
        self.nombre = nombre
        self.nacimiento = fecha_de_nacimiento

    def decir_nombre(self):
        print (f"Mi nombre es {self.nombre}")

    def decir_cuendo_naci(self):
        print (f"Yo naci en el {self.nacimiento}")

    def caminar(self):
        print (f"Me puse a caminar")

juan = Persona("juan", "30 de Mayo del 1991")

juan.decir_nombre()
juan.caminar()
juan.brazos
juan.piernas
juan.decir_cuendo_naci()

