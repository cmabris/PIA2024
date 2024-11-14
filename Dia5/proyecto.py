import random

lista_palabras = ['portatil', 'teclado', 'raton', 'monitor', 'altavoz', 'impresora', 'disco', 'memoria', 'microfono', 'auriculares']
letras_acertadas = []
letras_falladas = []


def elegir_palabra(lista):
    return random.choice(lista)

def pedir_letra():
    letra = input('Introduce una letra: ')
    return letra

def verificar_letra(palabra, letra):
    return letra in palabra

def mostrar_palabra(palabra, letras_correctas):
    palabra_mostrada = ''
    for letra in palabra:
        if letra in letras_correctas:
            palabra_mostrada += letra
        else:
            palabra_mostrada += '_'
    return palabra_mostrada

def vidas_restantes(letras_equivocadas):
    return 6 - len(letras_equivocadas)

palabra = elegir_palabra(lista_palabras)
while vidas_restantes(letras_falladas) > 0 and \
      mostrar_palabra(palabra, letras_acertadas) != palabra:
    print(mostrar_palabra(palabra, letras_acertadas))
    print('Vidas restantes:', vidas_restantes(letras_falladas))
    letra = pedir_letra()
    if verificar_letra(palabra, letra):
        letras_acertadas.append(letra)
    else:
        letras_falladas.append(letra)

if mostrar_palabra(palabra, letras_acertadas) == palabra:
    print('¡Has ganado!')
else:
    print('¡Has perdido! La palabra era:', palabra)