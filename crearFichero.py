from io import open
texto = "Una línea con texto\nOtra línea con texto"
# Ruta donde crearemos el fichero, w indica escritura (puntero al principio)
fichero = open('nuevoFichero','w')
# Escribimos el texto
fichero.write(texto)
# Cerramos el fichero
fichero.close()
print("FICHERO CREADO")