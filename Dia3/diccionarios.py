diccionario = {'c1' : 'valor1', 'c2' : 'valor2', 'c3' : 'valor3'}
print(type(diccionario))
print(diccionario)

resultado = diccionario['c1']
print(resultado)
resultado = diccionario['c2']
print(resultado)

cliente = {'nombre':'Juan', 'apellido':'Fuentes', 'peso':88, 'talla':1.76}
consulta = cliente['apellido']
print(consulta)

# Si la clave no existe, se genera un error
# consulta = cliente['edad']
# print(consulta)

dic = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100, 's2':200}}
print(dic['c2'])
print(dic['c2'][1])
print(dic['c3'])
print(dic['c3']['s2'])

dic = {'c1':['a', 'b', 'c'], 'c2':['d', 'e', 'f']}
print(dic['c2'][1].upper())

dic = {1: 'a', 2:'b'}
print(dic)

dic[3] = 'c'
print(dic)

dic[2] = 'B'
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())



