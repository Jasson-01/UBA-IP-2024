def elementos_iguales(lista: list) -> bool:
    primero = lista[0]
    for elem in lista:
        if elem != primero:
            return False
    return True


def un_responsable_por_turno(grilla_horaria: list[list[str]]) -> list[tuple[bool, bool]]:
    resultado = []
    numero_columnas = len(grilla_horaria[0])

    # Creamos una lista de Columnas
    lista_columnas = []
    # Recorriendo las columnas en cada vuelta, este se queda fijo en cada vuelta, mietras que el row si cambia en cada vuelta
    for col in range(len(grilla_horaria[0])):
        columna = []
        # Recorriendo las filas de la grilla
        for row in range(len(grilla_horaria)):
            columna.append(grilla_horaria[row][col])
        lista_columnas.append(columna)

    # Recorriendo cada elemento de "lista_columnas" y viendo hasta la mistad si son iguales

    for col in lista_columnas:

        mitad = int(len(col) // 2)

        x = True
        for pos1 in range(mitad):
            primero = col[0]
            if primero != col[pos1]:
                x = False

        y = True
        for pos2 in range(mitad, len(col)):
            segundo = col[len(col)//2]
            if segundo != col[pos2]:
                y = False

        resultado.append((x, y))
        
    print(grilla_horaria)
    return resultado


grilla_horaria = [
    ["Ana", "Ana", "Ana", "Ana", "Ana", "Ana", "Ana"],  # 9 hs
    ["Ana", "Ana", "Ana", "Ana", "Ana", "Ana", "Ana"],  # 10 hs
    ["Beto", "Beto", "Beto", "Beto", "Beto", "Beto", "Beto"],  # 11 hs
    ["Ana", "Ana", "Ana", "Ana", "Ana", "Ana", "Ana"],  # 12 hs
    ["Carlos", "Carlos", "Carlos", "Carlos",
        "Carlos", "Carlos", "Carlos"],  # 14 hs
    ["Carlos", "Carlos", "Carlos", "Carlos",
        "Carlos", "Carlos", "Carlos"],  # 15 hs
    ["Carlos", "Carlos", "Carlos", "Carlos",
        "Carlos", "Carlos", "Carlos"],  # 16 hs
    ["Carlos", "Carlos", "Carlos", "Carlos",
        "Carlos", "Carlos", "Carlos"],  # 17 hs
]

# Resultado esperado:
# [
#    (False, True),  # Lunes
#    (False, True),  # Martes
#    (False, True),  # Miércoles
#    (False, True),  # Jueves
#    (False, True),  # Viernes
#    (False, True),  # Sábado
#    (False, True),  # Domingo
# ]


print(un_responsable_por_turno(grilla_horaria))


"""
grilla_horaria = [
    ["A", "B", "A", "A", "A", "A", "A"],  # 9 hs
    ["A", "B", "A", "A", "A", "A", "A"],  # 10 hs
    ["A", "jorge", "A", "A", "A", "A", "A"],  # 11 hs
    ["A", "B", "A", "A", "A", "A", "A"],  # 12 hs
    ["C", "C", "C", "C", "C", "C", "C"],  # 14 hs
    ["C", "C", "C", "C", "C", "C", "C"],  # 15 hs
    ["C", "C", "C", "C", "C", "C", "C"],  # 16 hs
    ["C", "C", "C", "C", "C", "C", "C"],  # 17 hs
]

print(un_responsable_por_turno(grilla_horaria))

# Resultado esperado:
# [
#    (True, True),  # Lunes
#    (False, True), # Martes
#    (True, True),  # Miércoles
#    (True, True),  # Jueves
#    (True, True),  # Viernes
#    (True, True),  # Sábado
#    (True, True),  # Domingo
# ]
"""
