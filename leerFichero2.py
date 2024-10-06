#Otra opcion para leer fichero

from io import open
# Ruta donde leeremos el fichero, r indica lectura (por defecto ya es r)
fichero = open('resultados','r')
# Lectura completa
texto = fichero.read()

lista= list(texto.split("\n"))
# Cerramos el fichero
fichero.close() 
print(texto)