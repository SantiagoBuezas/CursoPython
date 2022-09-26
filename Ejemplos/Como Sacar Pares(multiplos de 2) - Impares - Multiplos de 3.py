
mi_numero = 0
valor_esperado = "valor"


# aca busco que mi numero sea par y mayor a 18
if (mi_numero  % 2 == 0) and (mi_numero > 18):
    resultado = "A"

# aca busco que mi numero sea impar y multiplo de 3
elif(mi_numero %2 != 0) and (mi_numero % 3 ==0):
    resultado = "B"
else:
    resultado = "valor no reconocido"
