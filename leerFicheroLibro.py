from io import open

#fichero = open('fichero.txt','r')
fichero = open('libros','r')

# Leemos creando una lista de líneas
texto = fichero.readlines()
fichero.close()
print(texto)