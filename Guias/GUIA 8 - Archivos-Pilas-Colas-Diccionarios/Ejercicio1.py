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
print((contenido))

# --- EJM 2 ---
"""
def existe_palabra(palabra:str,nombre_archivo:str)->bool:
    archivo = open(nombre_archivo,"r"):

    for linea in archivo.readlines():
         listaDePalabras: list[str] = funcionx(linea)
         if pertenece(palabra,listaDePalabras):
              return True
    archivo.close()
    return False

palabra:str  = "bien"
print(existe_palabra(palabra,"mi_archivo.txt"))
"""

# funcionx -> Desaparece los espacion en linea y separa las palabras una por una , loco


#archivo2 = open("mi_archivo.txt","r")
#contenido2 : str = archivo2.read()
#print(existe_palabra("capo",contenido2))




