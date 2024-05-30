
# --- EJM 1 ---
"""
def contar_lineas(nombreArchivo:str)->int:
    archivo = open("nombreArchivo","r")
    archivoTextoarchivo = archivo.readlines()
    archivo.close()
    return cantidadLista(archivoTextoarchivo)

print(contar_lineas("mi_archivo.txt"))
"""

def cantidadLista(lista:list[int])->int:
    contador = 0
    longitud = (len(lista)-1)
    while longitud >= 0:
          longitud -= 1 
          contador += 1
    return contador

#print(cantidadLista([1,2,3]))


archivo = open("mi_archivo.txt","r")
archivoTextoArchivo = archivo.readlines()
print(cantidadLista(archivoTextoArchivo))







