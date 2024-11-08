from random import randint

nombre = input('Introduce tu nombre: ')
print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo 8 intentos para adivinar cuál crees que es el número")

numero_secreto = randint(1, 100)
numero = 0

for intentos in range(1, 9):
    print(f"Intento número {intentos}")
    numero = int(input('Introduce un número: '))
    if numero == numero_secreto:
        print(f"¡Felicidades, {nombre}! Has adivinado el número en {intentos} intentos")
        break
    elif numero not in range(1, 101):
        print('El número introducido debe estar entre 1 y 100')
    elif numero < numero_secreto:
        print('El número introducido es menor que el número secreto')
    else:
        print('El número introducido es mayor que el número secreto')

if numero != numero_secreto:
    print(f"Lo siento, {nombre}, el número secreto era {numero_secreto}")
else:
    print('Enhorabuena, gracias por jugar')
print('Fin del juego')