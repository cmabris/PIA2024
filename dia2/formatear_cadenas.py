x = 10
y = 25

print("Mis números son " + str(x) + " y " + str(y))
print("Mis números son {} y {}".format(x, y))
print("La suma de {} y {} es {}".format(x, y, x + y))

# A partir de la versión 3.6 de Python, se puede utilizar f-strings
print(f"La suma de {x} y {y} es {x + y}")

# A partir de la versión 3.8 de Python, se puede utilizar el operador de asignación de expresiones
print(f"Mis números son {x = } y {y = }")

color = "rojo"
matricula = 123456
print(f"El coche es de color {color} y su matrícula es {matricula}")

matricula = "5555-CCC"
print(f"El coche es de color {color} y su matrícula es {matricula}")