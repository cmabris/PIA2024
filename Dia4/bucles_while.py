monedas = 5

while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas -= 1

while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas -= 1
else:
    print('No tengo más monedas')

respuesta = 's'

while respuesta == 's':
    respuesta = input('¿Quieres seguir jugando? (s/n)')
else:
    print('Fin del juego')

# pass es una palabra reservada que no hace nada,
# pero es útil para dejar un bloque de código vacío.

while respuesta == 's':
    pass
else:
    print('El juego ha terminado')

nombre = input('Introduce tu nombre: ')
for letra in nombre:
    if letra == 'r':
        break
    print(letra)

for letra in nombre:
    if letra == 'r':
        continue
    print(letra)




