class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"{self.nombre} {self.apellido} tiene un balance de {self.balance} en su cuenta {self.numero_cuenta}"

    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print("Depósito aceptado")
        else:
            print("No se puede depositar una cantidad negativa")

    def retirar(self, cantidad):
        if cantidad > self.balance or cantidad <= 0:
            print("Operación no permitida, no hay saldo suficiente")
        else:
            self.balance -= cantidad
            print("Retirada aceptada")

def crear_cliente():
    print("\nVamos a crear un cliente nuevo:")
    nombre = input("Nombre del cliente: ")
    apellidos = input("Apellidos del cliente: ")
    numero_cuenta = input("Número de cuenta: ")
    return Cliente(nombre, apellidos, numero_cuenta)

def menu(cliente):
    print("\nMenú:")
    print("1. Crear cliente")
    if cliente:
        print("2. Depositar")
        print("3. Retirar")
        print("4. Ver Cliente")
    print("5. Salir\n")
    return int(input("Opción: "))

def main():
    cliente = None
    while True:
        opcion = menu(cliente)
        if opcion == 1:
            cliente = crear_cliente()
        elif opcion == 2:
            cantidad = float(input("Cantidad a depositar: "))
            cliente.depositar(cantidad)
        elif opcion == 3:
            cantidad = float(input("Cantidad a retirar: "))
            cliente.retirar(cantidad)
        elif opcion == 4:
            print(cliente)
        elif opcion == 5:
            break
        else:
            print("Opción no válida")

main()



