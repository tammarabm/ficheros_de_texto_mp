from io import open

"""Este programa realiza la modificación de la nota de un alumno en el fichero"""
fichero=open('resultados', 'r+')
texto=fichero.readlines()

"""En este caso NO realizamos búsqueda sino que directamente modificamos al alumno que se encuentra en 
la segunda fila del fichero"""
#Modificamos la linea que queramos a partir del indice
texto[1]= "Carolina Tolaba, 17\n"
fichero.seek(0)
fichero.writelines(texto)
fichero.close()

"""Mostramos el fichero modificado"""
print(texto)
for linea in texto:
    x=linea.split(",");
    print(x)