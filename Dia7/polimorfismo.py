class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice Muuuuu")

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice Beeeeeee")

vaca1 = Vaca("Aurora")
oveja1 = Oveja("Dolly")

vaca1.hablar()
oveja1.hablar()

animales = [vaca1, oveja1]

for animal in animales:
    animal.hablar()

def animal_habla(animalito):
    animalito.hablar()

animal_habla(vaca1)
animal_habla(oveja1)






