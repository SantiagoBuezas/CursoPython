# Implementar una función llamada par_o_impar:

# Recibirá un número por parámetro
# Imprimirá “Par” si el número es par
# Imprimirá “Impar” si el número es impar
# Si se ingresa algo que no sea número debe indicar que se ingrese un número. 


def par_o_impar (un_numero):
    if un_numero % 2 == 0:
        print("Par")
    else:
        print("Impar")

pregunta = str.lower(input("Quiere ingresar un numero si o no: "))

while pregunta == "si":
    numero = (input("Ingrese un numero: "))
    if numero.isnumeric == True:
            numero_a_analizar = par_o_impar(numero)
    else:
        print("Porfavor ingrese un numero")
    pregunta = str.lower(input("Quiere ingresar un numero si o no: "))

print("Finalice correctamente")