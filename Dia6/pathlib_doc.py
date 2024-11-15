from pathlib import Path

# Ahora, con esta librería, no necesitamos abrir y cerrar archivos
carpeta = Path("/Users/carlos/Desktop/pruebas/prueba_escritorio.txt")
print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)
print(carpeta.parent)
print(carpeta.exists())

carpeta2 = Path("/Users/carlos/Desktop/pruebas/prueba.txt")
print(carpeta2.exists())
# print(carpeta2.read_text())

from pathlib import PureWindowsPath

ruta_windows = PureWindowsPath(carpeta)
print(f"C:{ruta_windows}")

from pathlib import PurePosixPath
ruta = PurePosixPath(ruta_windows)
print(ruta)




