# --- EJM 1 --------------------------------------------------------------------

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
#print((contenido))



# --- EJM 2 --------------------------------------------------------------------




def funcionAplanar(texto:str)->list[str]:
    abecedadrioCompleto:str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"   
    lista:list[str]= []
    palabra_Actual:str = ""
    for i in range(len(texto)):
         if (texto[i] in abecedadrioCompleto) :
              palabra_Actual += texto[i]
         else:
            if palabra_Actual:  # si palabra_Actual tiene caracteres entonces es TRUE
              lista.append(palabra_Actual)
              palabra_Actual = ""
    if palabra_Actual: # añadimos la ultima palabra si existe
         lista.append(palabra_Actual)
    return lista   
              
#print(funcionAplanar("Hola, esto es un ejemplo de oracion."))
            
def pertenece(palabra:str,lista:list[str])->bool:
    for i in lista:
        if i == palabra:
            return True
    return False

#palabra = "hola"
#lista = ["chau","bay","hello"]
#print(pertenece(palabra,lista))

def existe_palabra(palabra:str,nombre_archivo:str)->bool:
    archivo = open(nombre_archivo,"r")

    for linea in archivo.readlines():
         listaDePalabras: list[str] = funcionAplanar(linea)
         if pertenece(palabra,listaDePalabras):
              return True
    archivo.close()
    return False

palabra:str = "where"
print(existe_palabra(palabra,"mi_archivo.txt"))

# --- EJM 3 --------------------------------------------------------------------

# def cantidad_apariciones(nombre_archivo : str, palabra : str) -> int:
   
