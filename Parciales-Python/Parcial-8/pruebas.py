def maximo(lista: list[int]) -> int:
    maximo2 = lista[0]
    for elem in lista:
        if elem >= maximo2:
            maximo2 = elem

    return maximo2


lista2 = [3, 4, 50, 6, 7]
print(maximo(lista2))
