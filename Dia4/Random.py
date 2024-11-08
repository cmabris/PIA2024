# Para importar una función de una librería de Python

from random import randint

aleatorio = randint(1,50)
print(aleatorio)

# Para importar una librería completa de Python

from random import *

aleatorio = uniform(1,5)
print(aleatorio)

aleatorio = round(uniform(1,5), 2)
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ['rojo', 'azul', 'verde', 'amarillo', 'naranja', 'rosa', 'morado', 'blanco']
color = choice(colores)
print(color)

numeros = list(range(5, 50, 5))
print(numeros)
shuffle(numeros)
print(numeros)

