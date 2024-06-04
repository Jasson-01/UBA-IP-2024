# ---- EJM 1 ----
# tipo INOUT
def pares_por_cero(lista:list[int])->list:
    for i in range(0,len(lista),2):
           lista[i] = 0 
    return lista
print(pares_por_cero([1,2,3,4,5])) 

# ---- EJM 2 ----
# tipo IN
def pares_por_CeroV2(lista:list[int])->list:
    copia = lista.copy()
    for i in range(0,len(copia),2):
         lista[i] = 0
    return lista 
print(pares_por_CeroV2([1,2,3,3,5,6,7,8]))

# ---- EJM 3 ----

def pertenece(letra:str,listaVocales:str)->bool:
    for i in range(len(listaVocales)):
         if letra == listaVocales[i]:
              return True
    return False
 

def borra_vocales(cadena:str)->str:
    cadenaSinVocales:str = ""
    listaVocales:str = "aeiouAEIOU"
    for i in range(len(cadena)):
         if (pertenece(cadena[i],listaVocales) == False):
            cadenaSinVocales += cadena[i]
    return cadenaSinVocales            

print(borra_vocales("hola Como Estas"))

"""
s:seq⟨Char⟩


->  str  -> "prueba"
-> list[chr]  -> ["a","b","c] 
-> list[str] -> ["a","b","c]

-> lis[list[chr]] -> [["uno","dos","tres"],["ave","perro","gato"]]

-> En otras palabras "chr" en python es: "len(str) = 1"

"""

# ---- EJM 4 ----
def reemplaza_Vocales_por_guionBajo(lista:list[str])->list:
    listaVocales:str = "aeiouAEIOU"
    for i in range(len(lista)):
         if (pertenece(lista[i],listaVocales) == True):
            lista[i] = "_"
    return lista

print(reemplaza_Vocales_por_guionBajo(["h","o","l","a"]))  

# ---- EJM 5 ----

def da_vuelta_str(cadena:list[str])->list:
    copia:list = cadena.copy()
    nueva:list = []
    for i in range(len(copia)-1,-1,-1):
        nueva.append(copia[i])
    return nueva 

print(da_vuelta_str(["h","o","l","a"]))

# ---- EJM 6 ----


def perteneceGeneral(letra,listaGeneral:list)->bool:
    for i in range(len(listaGeneral)):
         if letra == listaGeneral[i]:
              return True
    return False
 
def eliminar_repetidos(cadena:list[str])->list[str]:
    nuevaCopia:list = cadena.copy()
    nuevaLista:list = []
    for letra in nuevaCopia:
        if (not perteneceGeneral(letra,nuevaLista)):
             nuevaLista.append(letra)
    return nuevaLista

print(eliminar_repetidos(["h","o","l","a","a","o","a","o","l","h"]))


































































