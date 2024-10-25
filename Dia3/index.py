miTexto = "Esta es una prueba"
resultado = miTexto[0]
print(resultado)
resultado = miTexto[4]
print(resultado)
resultado = miTexto[9]
print(resultado)
resultado = miTexto[-4]
print(resultado)

resultado = miTexto.index('n')
print(resultado)
resultado = miTexto.index('e')
print(resultado)

# ERROR: no se encuentra la letra x
# resultado = miTexto.index('x')
# print(resultado)

resultado = miTexto.index('prueba')
print(resultado)

resultado = miTexto.index('a', 5)
print(resultado)

resultado = miTexto.index('a', 5, 11)
print(resultado)

resultado = miTexto.rindex('a')
print(resultado)
