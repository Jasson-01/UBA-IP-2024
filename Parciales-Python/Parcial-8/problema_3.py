def suma_lista(lista: list[int]) -> int:
    suma_lista = 0
    for num in lista:
        suma_lista += num
    return suma_lista

# print(suma_lista([1,2,3,4,5,6,7,8,9,0]))


def empleado_del_mes(horas: dict[int, list[int]]) -> list[int]:

    lista_de_tuplas = []
    for key, valor in horas.items():
        lista_de_tuplas.append((key, valor))

    lista_maxima = lista_de_tuplas[0][1]
    for i in lista_de_tuplas:  # Este itera sobre las tuplas
       #     for j in range(len(lista_de_tuplas)): # Este itera sobre cada tupla
        if suma_lista(lista_maxima) <= suma_lista(i[1]):
            lista_maxima = i[1]
    return lista_maxima


horas: dict = {1: [2, 3, 4], 2: [5, 60, 7], 3: [6, 7, 8], 7: [3, 2, 1, 6]}
print(empleado_del_mes(horas))
# res = [5, 60, 7]
