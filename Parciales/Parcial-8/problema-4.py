def nivel_de_ocupacion(camas_por_piso: list[list[bool]]) -> list[float]:
    lista_proporcion = []
    cantidad_de_camas_en_cada_piso = len(camas_por_piso[0])

    # primero recorro los pisos
    for piso in camas_por_piso:

        contador = 0
        for pos in range(len(piso)):
            if piso[pos] == True:
                contador += 1

        proporcion = contador / cantidad_de_camas_en_cada_piso
        lista_proporcion.append(proporcion)

    return lista_proporcion


# matriz = [[True, False, False], [True, True, False], [False, False, False]]
# print(nivel_de_ocupacion(matriz))
# res = [0.33,0.66,0]
