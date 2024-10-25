miTupla = (1, 2, 3, 4, 5)
print(type(miTupla))

miTupla = 1, 2, 3, 4, 5
print(type(miTupla))

t = (5, 5.6, 'ff')
print(type(t))

print(miTupla[0])
print(miTupla[-2])

# Error
# miTupla[0] = 5

# Error
# miTupla.append(6)

miTupla = (1, 2, (10, 20), 4)
print(miTupla[2])
print(miTupla[2][1])

miTupla = list(miTupla)
print(type(miTupla))

miTupla = tuple(miTupla)
print(type(miTupla))

t = (1, 2, 3)
x, y, z = t
print(x, y, z)
print(type(x))

print(len(t))
t = (1, 2, 3, 1)
print(len(t))
print(t.count(1))
print(t.index(2))








