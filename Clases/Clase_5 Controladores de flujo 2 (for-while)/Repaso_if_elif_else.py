#Valores de prueba

numero = 0
valor_esperado = "valor no reconocido"

#numero = 1
#valor_esperado = "valor no reconocido"

#numero = 2
#valor_esperado = "valor no reconocido"

#numero = 20
#valor_esperado = "A"

#numero = 21
#valor_esperado = "valor no reconocido"

#numero = 9
#valor_esperado = "B"

#numero = 6 
#valor_esperado = "valor no reconocido"

##############################################################################################################
#Programa

if (numero % 2 == 0) and (numero > 18):
    resultado = "A"
elif(numero % 2 != 0) and (numero % 3 ==0):
    resultado = "B"
else:
    resultado = "valor no reconocido"


##############################################################################################################
#Test

print("mi numero es: " + str(numero))
print("valor esperado es: "+ valor_esperado)
print("El resultado es: " + str(resultado))

assert resultado == valor_esperado


##############################################################################################################

print("Termine correctamente")
