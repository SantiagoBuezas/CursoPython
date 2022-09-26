import sys



if len(sys.argv) == 3:

    mi_variable = sys.argv [1]
    mi_otra_variable = sys.argv[2]


    print(mi_variable)
else:
    print(f"Ha ingresado {(len(sys.argv)-1)} variables, ingrese exactamente dos")
