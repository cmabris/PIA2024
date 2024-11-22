class Padre:
    def hablar(self):
        print("Hola, yo soy tu padre")

class Madre:
    def hablar(self):
        print("Hola, yo soy tu madre")

    def reir(self):
        print("ja ja ja")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

print(Nieto.__bases__)
pepe = Nieto()
pepe.hablar()
pepe.reir()

print(Nieto.__mro__)




