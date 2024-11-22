class Pajaro:
    # This is a constructor
    def __init__(self, especie, color):
        self.especie = especie
        self.color = color

mi_pajaro = Pajaro("Tucán", "Azul")

print(mi_pajaro.especie)
print(mi_pajaro.color)

print(f"Mi pájaro es un {mi_pajaro.especie} de color {mi_pajaro.color}")

class Pajaro:

    alas = True

    # This is a constructor
    def __init__(self, especie, color):
        self.especie = especie
        self.color = color

mi_pajaro2 = Pajaro("Periquito", "Negro")
print(f"Mi pájaro es un {mi_pajaro.especie} de color {mi_pajaro.color}")
print(Pajaro.alas)
print(mi_pajaro2.alas)
# print(mi_pajaro.alas) ERROR





