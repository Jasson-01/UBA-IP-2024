# --- EJM 1 ---

def contar_Lineas(lista:list[int])->int:
    contador = 0
    longitud = (len(lista)-1)
    while longitud >= 0:
          longitud -= 1 
          contador += 1
    return contador

#print(cantidadLista([1,2,3]))

archivo = open("mi_archivo.txt","r",encoding='utf8')
contenido : str = archivo.readlines()
print(contar_Lineas(contenido))

# --- EJM 2 ---

#def existe_palabra(palabra:str,nombre_archivo:str)->bool:
     





