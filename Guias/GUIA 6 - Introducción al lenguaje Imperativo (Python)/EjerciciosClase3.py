#PROBL_1

def reemplaza_pares_por_cero(s:list[int])->None:
    indice = 0 
    longitud = len(s)
    while (indice < longitud):
        if ( indice % 2 == 0):
            s[indice] = 0
        indice += 1
lista = [1,2,3,4,5,6]
reemplaza_pares_por_cero(lista)
print(lista)

"""
s = [1,2,3,4,5,6]
print(f"lista:{s}")
s = [1,2,3,4,5,6]
reeplaza_pares_por_cero(s)
print(reeplaza_pares_por_cero(f"reeplazando:{s}"))
"""

#def reeplaza_pares_por_cerov2(s:list[int])->None:
#    for i in range(0,len(s)):
#        s[i] = 0


#PROBL_2

def pertenece(lista:list[int],elemento:int):
    if elemento in lista:
        return True
    return False



def pertenece_a_cada_uno(lista:list[list[int]],elemento:int,res:list[bool])-> None:
    res.clear()
    for v in lista:
        res.append(pertenece(v,elemento))

lista = [[1,2,3],[2,3,4],[4,5,6]]
elemento = 2
listaAux = []
pertenece_a_cada_uno(lista,elemento,listaAux)
print(listaAux)














































































































