from io import open

texto="Se crea el fichero 4 \nSe crea una variable ruta"
ruta= 'nuevoFichero4.txt'
fichero=open(ruta, 'w')
fichero.write(texto)
fichero.close()
print("FICHERO CREADO")