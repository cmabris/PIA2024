nombre = input("Dime tu nombre: ")
ventas = input("Dime tus ventas: ")

comision = float(ventas) * 0.13

print(f"Hola {nombre}, tu comisión es de {round(comision, 2)} €")