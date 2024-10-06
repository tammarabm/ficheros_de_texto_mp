from io import open

texto="Se crea el fichero 3 \nSe crea una variable ruta"
ruta= 'nuevoFichero3'
fichero=open(ruta, 'w')
fichero.write(texto)
fichero.close()
print("FICHERO CREADO")