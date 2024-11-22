class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("He nacido")

class Pajaro(Animal):
    pass

class Perro(Animal):
    pass

print(Pajaro.__bases__)
print(Animal.__subclasses__())

piolin = Pajaro(2, 'amarillo')
piolin.nacer()

print(piolin.edad, piolin.color)