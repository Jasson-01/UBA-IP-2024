
################### CREANDO UNA LISTA DE COLUMNAS #####################

def lista_columnas(matriz: list[list[int]]) -> list[list[int]]:

    columnas: list = []
    for col in range(len(matriz[0])):
        columna = []
        for row in range(len(matriz)):
            columna.append(matriz[row][col])
        columnas.append(columna)

    return columnas


#matriz = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]

#print(lista_columnas(matriz))

#matriz2 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]


def elementos_iguales(lista:list)->bool:
    primero = lista[0]
    for elem in lista:
        if elem != primero:
            return False
    return True

#listaPrueba = [1,1,1,1,1,1,1]
#print(elementos_iguales(listaPrueba))
        