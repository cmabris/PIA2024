miLista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(type(miLista))

otraLista = ['hola', 55, 6.1]
print(type(otraLista))

resultado = len(miLista)
print(resultado)

resultado = miLista[0]
print(resultado)

resultado = miLista[0:1]
print(resultado)

resultado = miLista[0:3]
print(resultado)

resultado = miLista[3:]
print(resultado)

miLista2 = ['h', 'i', 'j', 'k', 'l', 'm', 'n']
print(miLista + miLista2)
print(miLista + miLista)

miLista3 = miLista + miLista2
print(miLista3)

miLista3.pop(0)
print(miLista3)

miLista3.pop(1)
print(miLista3)

miLista3.reverse()
print(miLista3)


