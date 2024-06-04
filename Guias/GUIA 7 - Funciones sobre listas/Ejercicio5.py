# ------- PROBL - 1 ---------

def pertenece(lista:list[int],elemento:int)->bool:
    return elemento in lista

def pertenece_a_cada_uno(lista:list[list[int]],elemento:int)->list[bool]:
    nueva = []
    for sublista in lista :
            if pertenece(sublista,elemento) :
                   nueva.append(True)
    nueva.append(False)
    return nueva

#lista = [[2,3,4],[5,4,3],[2,1,4]]
#elemento = 3
#print(pertenece_a_cada_uno(lista,elemento))

# ------- PROBL - 2 ---------

def es_matriz(matriz:list[list[int]])->bool:
    if not matriz:
        return False  # Asumimos que una matriz vacía no es una matriz válida
    cambio_fila = matriz[0]
    for fila in matriz:
         if len(cambio_fila) != len(fila):
              return False
         cambio_fila = fila
    return True
#matriz = [[1,2,3],[4,5,6],[7,6]]    
#print(es_matriz(matriz))

#              A        B        C
#  matriz = [[1,2,3],[4,5,6],[7,6,5]]    


# ------- PROBL - 3 ---------

def esta_ordenada(lista: list[int]) -> bool:
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

# Ejemplos de uso
print(esta_ordenada([1, 2, 3, 4, 5]))  # Debe retornar True


def ordenados(lista:list[int])->bool:
    indice:int= 0
    while indice < len(lista)-1:
        if lista[indice] > lista[indice+1]:
            return False
        indice += 1
    return True
print(ordenados([3,4,5,6]))


def filas_ordenas(matriz:list[list[int]])->bool:
    for fila in matriz:
        if ordenados(fila) != True :
              return False 
    return True

#print(filas_ordenas([[1,2,3],[4,5,6],[2,6,9]]))























