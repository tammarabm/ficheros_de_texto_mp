from io import open

def leerArchivo(ruta): 
    lista=[]
    fichero=open(ruta, 'r', encoding='utf-8')  #Abrir archivo  encoding:para que reconozca los acentos y las ñ
    texto=fichero.readlines() #Leer archivo
    fichero.close() #Cerrar archivo
    
    for linea in texto: 
        x=linea.split(";")
        lista.append(x)
    return lista

#Principal
ruta='libros'
listaLibros=leerArchivo(ruta)
print(listaLibros)