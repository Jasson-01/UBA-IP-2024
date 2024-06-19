def proporcion(registros, lista_infecciones) -> list[tuple[str, float]]:

    lista_tuplas_con_proporcion = []
    total_de_registros = len(registros)

    for enfermedad in lista_infecciones:
       # lista_tuplas_con_proporcion.append(enfermedad)
        contador = 0
        # recorro los regitros
        for tupla in registros:
            # ahora busco la enfermedad en la segunda posicion de la tupla
            if tupla[1] == enfermedad:
                contador += 1
        lista_tuplas_con_proporcion.append(
            (enfermedad, contador/total_de_registros))

    return lista_tuplas_con_proporcion


# registros = [(1, "A"), (3, "C"), (4, "E"), (7, "A"), (8, "C")]
# lista_infecciones = ["A", "C", "E"]
# umbral = 0.3
# print(proporcion(registros, lista_infecciones))
# res = [('A', 0.4), ('C', 0.4), ('E', 0.2)]

def alarma_epidemiologica(registros: list[tuple[int, str]], infecciosas: list[str], umbral: float) -> dict[str, float]:
    # Creando el diccionario
    diccionario_res: dict = dict()
   # for enfermedad in infecciosas:
   #     diccionario_res[enfermedad] = 0

    lista_tuplas_con_proporcion_v2 = proporcion(registros, infecciosas)

    # ahora voy a recorrer la "lista_tuplas_con_proporcion_v2" para ver si su proporcion pasa el umbral
    for i in range(len(lista_tuplas_con_proporcion_v2)):
        if lista_tuplas_con_proporcion_v2[i][1] >= umbral:
            diccionario_res[lista_tuplas_con_proporcion_v2[i]
                            [0]] = lista_tuplas_con_proporcion_v2[i][1]

    return diccionario_res


# registros = [(1, "A"), (3, "C"), (4, "E"), (7, "A"), (8, "C")]
# lista_infecciones = ["A", "C", "E"]
# umbral = 0.3
# print(alarma_epidemiologica(registros, lista_infecciones, umbral))
# res = ['A':0.4 , 'C':0.4]
