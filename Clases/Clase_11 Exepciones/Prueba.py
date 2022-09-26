def dividir (a,b):
    if b == 0:
        return None
    else:
        return a/b

print(dividir(a=4,b=2) == 2)
print(dividir(a=9,b=3) == 3)
print(dividir(a=2,b=4) == 0.5)
print(dividir(a=0,b=8) == 0)
print(dividir(a=8,b=0) == None)
print(dividir(a=-1,b=0) == None)
print(dividir(a=99,b=0) == None)
