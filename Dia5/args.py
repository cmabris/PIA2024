def suma(a ,b):
    return a + b

print(suma(2, 3))

# Error
# print(suma(2, 3, 4))

def suma_v2(*args):
    return sum(args)

print(suma_v2(2, 3))
print(suma_v2(2, 3, 4))
print(suma_v2(2, 3, 4, 5))

def suma_v3(*numeros):
    return sum(numeros)

print(suma_v3(2, 3))
print(suma_v3(2, 3, 4))
print(suma_v3(2, 3, 4, 5))






