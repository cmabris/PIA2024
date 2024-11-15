archivo = open("prueba.txt", "r")

# No podemos escribir en un archivo que se abrió en modo lectura
# archivo.write("Hola mundo\n")

archivo.close()

# Para escribir en un archivo, necesitamos abrirlo en modo escritura
archivo = open("prueba1.txt", "w")
archivo.write("Hola mundo\n")
archivo.write("Adios mundo\n")
archivo.write("Mundo cruel, me voy\n")
archivo.close()

# Si abrimos un archivo en modo escritura, se sobreescribe el contenido
archivo = open("prueba1.txt", "w")
archivo.writelines(["Hola nuevo mundo\n", "Adios nuevo mundo\n", "Te saludo desde la tercera línea\n"])
archivo.close()

# Para agregar contenido a un archivo, necesitamos abrirlo en modo append
archivo = open("prueba1.txt", "a")
archivo.write("Soy el cuarto en discordia\n")
archivo.close()



