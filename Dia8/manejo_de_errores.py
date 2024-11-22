from sys import exception


def suma():
    n1 = int(input("Introduzca el primer número: "))
    n2 = int(input("Introduzca el segundo número: "))
    print(n1 + n2)
    print("Gracias por sumar")

# suma()

def suma2():
    try:
        n1 = int(input("Introduzca el primer número: "))
        n2 = int(input("Introduzca el segundo número: "))
        print(n1 + n2)
    except ValueError:
        print("Por favor, introduzca un número válido")
    else:
        print("Gracias por sumar")
    finally:
        print("Esto se ejecuta siempre")

#suma2()

try:
    suma()
except Exception as e:
    print("Ha ocurrido un error")
    print(e)
else:
    print("Gracias por sumar")
finally:
    print("Esto fue todo. FIN")


# Podemos manejar errores específicos
# Error 1: Concatenamos un string con un número
# Error 2: Introducimos un caracter no numérico

def suma3():
    try:
        n1 = int(input("Introduzca el primer número: "))
        n2 = int(input("Introduzca el segundo número: "))
        print(n1 + n2)
        print("Gracias por sumar el número " + n1)
    except TypeError:
        print("Estás intentando sumar un string con un número")
    except ValueError:
        print("Por favor, introduzca un número válido")
    else:
        print("Gracias por sumar")
    finally:
        print("Esto se ejecuta siempre")

#suma3()

def pedir_numero():
    while True:
        try:
            numero = int(input("Introduce un número: "))
        except ValueError:
            print("Introduce un número válido")
        else:
            print(f"Has introducido el número {numero}")
            break
    print("Gracias por introducir un número")

pedir_numero()