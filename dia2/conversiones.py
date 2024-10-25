num1 = 20
num2 = 30.5

# Conversión implícita
num = num1 + num2
print(num)
print(type(num))
print(type(num1))
print(type(num2))

# Conversión explícita
num1 = 5.8
print(num1)
print(type(num1))

num2 = int(num1)
print(num2)
print(type(num2))

edad = input("Dime tu edad: ")
print("Tu edad es " + edad)
print(type(edad))
edad = int(edad)
nuevaEdad = edad + 1
print(nuevaEdad)
print(type(nuevaEdad))

# print("Tu edad dentro de un año será " + nuevaEdad)
print("Tu edad dentro de un año será " + str(nuevaEdad))
