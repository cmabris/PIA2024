import os

ruta = os.getcwd()
print(ruta)

os.chdir("/Users/carlos/Desktop/pruebas")
archivo = open('prueba_escritorio.txt')
print(archivo.read())

# También podemos crear directorios
os.mkdir("nuevo_directorio")
ruta2 = os.getcwd()
print(ruta2)

# Y cambiar de directorio
elemento = os.path.basename(ruta + "/prueba1.txt")
ruta3 = os.path.dirname(ruta + "/prueba1.txt")
print(ruta3, elemento)

elemento = os.path.split(ruta + "/prueba1.txt")
print(elemento)

# Podemos borrar un directorio
os.rmdir(ruta2 + "/nuevo_directorio")

# Para trabajar con rutas sin importar el sistema operativo
from pathlib import Path
print("Cambiando ruta con Path")
base_dir = os.path.join("Users", "carlos", "Desktop", "pruebas")
archivo_path = os.path.join(base_dir, "prueba_escritorio.txt")
print("-----------------")
print(archivo_path)
archivo2 = open(f"/{archivo_path}")
print(archivo2.read())









