# Comenzamos con las diferencias entre = y ==
# = es el operador de asignación, se utiliza para asignar un valor a una variable.
# == es el operador de comparación, se utiliza para comparar dos valores.

mi_bool = 5 == 5
print(mi_bool)

mi_bool = 5 + 5 == 18 - 8
print(mi_bool)

mi_bool = 'blanco' == 'blanco'
print(mi_bool)

mi_bool = 'blanco' == 'Blanco'
print(mi_bool)

mi_bool = 'blanco' == 'Blanco'.lower()
print(mi_bool)

mi_bool = '100' == 100
print(mi_bool)

mi_bool = 100.0 == 100
print(mi_bool)

mi_bool = 100.0 != 100
print(mi_bool)

mi_bool = 5 < 10
print(mi_bool)

mi_bool = 5 > 10
print(mi_bool)

mi_bool = 5 <= 10
print(mi_bool)

mi_bool = 5 >= 10
print(mi_bool)





