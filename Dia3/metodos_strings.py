texto = "Este es el texto de Federico"
resultado = texto.upper()
print(resultado)

resultado = texto[2].upper()
print(resultado)

resultado = texto.lower()
print(resultado)

resultado = texto.capitalize()
print(resultado)

resultado = texto.split()
print(resultado)
print(type(resultado))

resultado = texto.split('t')
print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"

resultado = " ".join([a, b, c, d])
print(resultado)

resultado = "-".join([a, b, c, d])
print(resultado)

resultado = texto.find("x")
print(resultado)

resultado = texto.find("el")
print(resultado)

resultado = texto.find("y")
print(resultado)

resultado = texto.find("F", 4, 10)
print(resultado)

resultado = texto.replace("Federico", "Heriberto")
print(resultado)

resultado = texto.replace("e", "i")
print(resultado)

resultado = texto.count("e")
print(resultado)

resultado = len(texto)
print(resultado)
