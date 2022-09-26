"""
1. Elegir nombre de la funcion y escribir el esqueleto
2. Escribir 1 caso de prueba
3. Hacer pasar el caso de prueba
4. Repetir 2 y 3 hasta el cansancio
"""


def año_bisiesto(un_año):
    if int(un_año) < 1582:
        return False
    elif int(un_año) % 400 == 0:
        return True
    elif int(un_año) % 100 == 0:
        return False
    elif int(un_año) % 4 == 0:
        return True
    else:
        return False

intentos = 2

while intentos < 10:
    año_a_ingresar = input("Ingrese un año para saber si es bisiesto o no: ")
    

    if año_a_ingresar.isnumeric() == True:
        año_bisiesto_true_o_false = año_bisiesto(año_a_ingresar)
        if año_bisiesto_true_o_false == True:
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")
    else:
        print("No ingreso un numero, porfavor ingrese un numero")


