def escape_en_solitario(amigos_por_salas: list[list[int]]) -> list[int]:
    indices_validos = []
    indice = 0
    for sala in amigos_por_salas:
       #     for i in range(len(sala)):
        if sala[0] == 0 and sala[1] == 0 and sala[3] == 0 and sala[2] != 0:
            indices_validos.append(indice)
        indice += 1
    return indices_validos

# salas = [[0,0,2,0],[4,61,9,8],[0,0,61,0],[0,4,7,61]]
# res = [0,2]

# amigos_por_salas = [
#    [0, 0, 0, 0],    # Esta fila no cumple con la condición
#    [0, 0, 61, 0],   # Esta fila cumple con la condición
#    [1, 0, 10, 0],   # Esta fila no cumple con la condición
#    [0, 0, 0, 0]     # Esta fila no cumple con la condición
# ]

# print(escape_en_solitario(amigos_por_salas))
