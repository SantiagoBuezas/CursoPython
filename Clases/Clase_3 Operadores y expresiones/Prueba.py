
expresiones = [
    False == True,
    10 ==2*4,
    33/3 == 11,
    True >= False,
    True*5 ==2.5*2
]

print(expresiones)

expresiones_2 = [
    not False,
    not 3 == 5,
    33/3 == 11 and 5 > 2,
    True or False,
    True*5 == 2.5*2 or 123 >= 23,
    12 > 7 and True < False
]

print(expresiones_2)



nombre = str(input("mi nombre es:"))
edad = int(input("Mi edad es:"))

expresiones_3 = (nombre != "****") and (10 < edad < 18) and (3 <= len(nombre) <10) and ((edad*4)>40)

print(expresiones_3)



