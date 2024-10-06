#Una opción para leer fichero

from io import open

#fichero = open('fichero.txt','r')
fichero = open('resultados','r')

# Leemos creando una lista de líneas
texto = fichero.readlines()
fichero.close()
print(texto)
for linea in texto: 
    x=linea.split(",");
    print(x)