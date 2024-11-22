class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("He nacido")

    def hablar(self):
        print("Hago ruido")

class Pajaro(Animal):
    # Añadir atributos a una clase hija
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    # Sobreescritura de métodos
    def hablar(self):
        print("Pio pio")

    # Métodos propios
    def volar(self):
        print("Estoy volando")

class Perro(Animal):
    pass

piolin = Pajaro(3, 'amarillo', 60)

# Métodos heredados
piolin.nacer()

# Métodos heredados y sobreescritos
piolin.hablar()

# Métodos propios
piolin.volar()

# Atributos heredados
print(piolin.edad, piolin.color)

# Atributos propios
print(piolin.altura_vuelo)





