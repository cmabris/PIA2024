def suma(**kwargs):
    print(type(kwargs))

suma(x=3, y=5, z=2)

def suma2(**kwargs):
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

suma2(x=3, y=5, z=2)

def suma3(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')
        total += valor
    return total

resultado = suma3(x=3, y=5, z=2)
print(resultado)

def prueba(num1, num2, *args, **kwargs):
    print(f"num1: {num1}")
    print(f"num2: {num2}")
    for arg in args:
        print(f"arg: {arg}")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

prueba(15,50, 100, 200, 300, 400, x='uno', y='dos', z='tres')

args = [100, 200, 300, 400]
kwargs = {'x':'uno', 'y':'dos', 'z':'tres'}

prueba(15, 50, args, kwargs)

prueba(15, 50, *args, **kwargs)

# Esto no es recomendable porque no sigue el estándar
lista = [100, 200, 300, 400]
diccionario = {'x':'uno', 'y':'dos', 'z':'tres'}

prueba(15, 50, *lista, **diccionario)






