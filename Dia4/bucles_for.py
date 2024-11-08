lista = ['a', 'b', 'c']
for letra in lista:
    print(letra)

for letra in lista:
    print('letra: ' + letra)

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")

lista = ['pablo', 'laura', 'federico', 'luis', 'julia']
for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print(f"{nombre} no empieza con la letra 'l'")

numeros = [1, 2, 3, 4, 5]
mi_valor = 0
for numero in numeros:
    mi_valor += numero
print(mi_valor)

palabra = 'python'

for letra in palabra:
    print(letra)

for letra in 'python':
    print(letra)

for letra in ('p', 'y', 't', 'h', 'o', 'n'):
    print(letra)

for item in [[1,2], [3,4], [5,6]]:
    print(item)

for item, item2 in [[1,2], [3,4], [5,6]]:
    print(item)
    print(item2)
    print('----')

dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for clave in dic:
    print(clave)

for clave in dic.items():
    print(clave)

for clave in dic.values():
    print(clave)

for a,b in dic.items():
    print(a,b)






