def tiempo_mas_rapido(tiempo_salas: list[int]) -> int:
    copia_tiempos = tiempo_salas.copy()

    minimo = 0
    i = 0
    while copia_tiempos[i] == 0 or copia_tiempos[i] == 61:
        minimo = 0
        i += 1
    minimo = copia_tiempos[i]

    # return minimo, i

    pos = i
    for j in range(len(copia_tiempos)):
        if copia_tiempos[j] < minimo and (copia_tiempos[j] != 0) and (copia_tiempos[j] != 61):
            minimo = copia_tiempos[j]
            pos = j
    return pos


# lista_tiempos = [25,30,40,55]
# res = 0
# lista_tiempos = [30,40,10,35,45]
# res = 2
# lista_tiempos = [30,45,55,13,25,13,65]
# res = 3
# lista_tiempos1 = [1, 61, 0, 33, 7, 1, 0, 61, 1, 0, 42]
lista_tiempos2 = [60, 4, 5, 10, 60, 1, 42]
# lista_tiempos3 = [0, 61, 0, 42, 61, 0, 0]

# print(tiempo_mas_rapido(lista_tiempos1))
print(tiempo_mas_rapido(lista_tiempos2))
# print(tiempo_mas_rapido(lista_tiempos3))





"""
    # recorro los lementos de la lista
    indice = 0
    indice_r = 0
    for i in range(len(copia_tiempos)):
        # señalo el minimo como el primero de la lista
        if minimo > copia_tiempos[i] and copia_tiempos[i] != 0 and copia_tiempos[i] != 61:
            minimo = copia_tiempos[i]
            indice = i
     #   elif minimo == copia_tiempos[i]:
        minimo = copia_tiempos[i]
        indice_r = indice
        indice += 1     
    return indice_r
"""
