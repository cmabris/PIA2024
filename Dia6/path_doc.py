from pathlib import Path

# La ruta que genera Path es relativa
guia = Path("Barcelona", "Sagrada_familia", "entrada.txt")
print(guia)

base = Path.home()
print(base)
guia2 = Path(base, "Barcelona", "Sagrada_familia", "entrada.txt")
print(guia2)

# El constructor de Path maneja diferentes entradas de parámetros
guia3 = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_familia", "entrada.txt"))
print(guia3)

# Podemos cambiar el nombre del archivo, manteniendo la ruta
guia4 = guia3.with_name("salida.txt")
print(guia4)

# Podemos obtener la carpeta contenedora
print(guia4.parent)
print(guia4.parent.parent)
print(guia4.parent.parent.parent)

print("\nTrabajando con la carpeta Europa\n")
# Ahora descomprimimos el archivo Europa.zip y lo colocamos en el escritorio
base = Path.home()
guia5 = Path(base, "Desktop", "Europa")
print(guia5)
print("----------")
for file in Path(guia5).glob("*.txt"):
    print(file)
print("\n")
for file in Path(guia5).glob("**/*.txt"):
    print(file)

print("\n")
# Para obtener los archivos desde un lugar concreto
guia6 = Path(base, "Desktop", "Europa", "España", "Barcelona", "Sagrada_familia.txt")
print(guia6)
en_europa = guia6.relative_to(Path(base, "Desktop", "Europa"))
en_espana = guia6.relative_to(Path(base, "Desktop", "Europa", "España"))
print(en_europa)
print(en_espana)
