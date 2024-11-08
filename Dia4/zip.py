nombres = ['Ana', 'Hugo', 'Valeria']
edades = [23, 45, 34]

combinados = zip(nombres, edades)
print(combinados)
print(type(combinados))
print(list(combinados))

nombres = ['Ana', 'Hugo', 'Valeria', 'Juan']
edades = [23, 45, 34]
print(list(zip(nombres, edades)))

ciudades = ['Bogotá', 'Medellín', 'Cali']
combinados = list(zip(nombres, edades, ciudades))
print(combinados)

for nombre, edades, ciudad in combinados:
    print(f"{nombre} tiene {edades} años y vive en {ciudad}")


