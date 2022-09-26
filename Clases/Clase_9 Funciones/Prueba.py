def par_o_impar(un_numero):
    if un_numero % 2 == 0:
        return True
    else:
        return False


assert par_o_impar(2) == True

assert par_o_impar(1) == False

assert par_o_impar(30) == True

assert par_o_impar(15) == False

resultado_de_par_o_impar = par_o_impar(2)
if resultado_de_par_o_impar == True:
    print("Es par")
else:
    print("Es impar")

resultado_de_par_o_impar = par_o_impar(1)
if resultado_de_par_o_impar == True:
    print("Es par")
else:
    print("Es impar")

resultado_de_par_o_impar = par_o_impar(30)
if resultado_de_par_o_impar == True:
    print("Es par")
else:
    print("Es impar")

resultado_de_par_o_impar = par_o_impar(15)
if resultado_de_par_o_impar == True:
    print("Es par")
else:
    print("Es impar")



print("Finalice correctamente")









