
###############################################################

def subsecuencia_mas_larga2(tipos_pacientes_atendidos: list[str]) -> int:

    # Vamos a hacer una lista de tuplas que contenga las primera posición índice (pos) y la segunda posición su secuencia correspondiente.
    lista_tuplas = []
    pos = 0  # La posición inicial
    lista_tmp = []
    indice = 0  # Índice manual

    for animal in tipos_pacientes_atendidos:
        if animal == "perro" or animal == "gato":
            if len(lista_tmp) == 0:
                pos = indice  # Marcar la posición inicial de la subsecuencia
            lista_tmp.append(animal)
        elif len(lista_tmp) > 0:
            lista_tuplas.append((pos, lista_tmp))
            lista_tmp = []

        indice += 1

    # Si hay una subsecuencia restante que no se ha agregado a lista_tuplas
    if len(lista_tmp) > 0:
        lista_tuplas.append((pos, lista_tmp))

    # Buscar la subsecuencia más larga
    longitud_mayor = 0
    primer_indice = 0

    for tupla in lista_tuplas:
        if len(tupla[1]) > longitud_mayor:
            longitud_mayor = len(tupla[1])
            primer_indice = tupla[0]

    # Cumple con la especificacion de tipo "In", este print.
    print(tipos_pacientes_atendidos)
    return primer_indice


# print(subsecuencia_mas_larga2( ["perro", "gato", "loro", "perro","perro", "gato", "pez", "perro", "gato", "gato", "perro"]))  # Salida: 7


# print(subsecuencia_mas_larga2(["perro", "gato", "pez", "hamster", "perro"])) # Resultado esperado: 0


# print(subsecuencia_mas_larga2(["perro", "gato", "pez", "perro", "perro", "gato", "gato"]))  # Resultado esperado: 3


print(subsecuencia_mas_larga2(["perro", "gato", "pez", "perro",
      "gato", "pez", "perro", "gato"]))  # Resultado esperado: 0------

# print(subsecuencia_mas_larga2(["perro", "pez", "gato", "pez", "perro", "gato"]))  # Resultado esperado: 4

# print(subsecuencia_mas_larga2(["perro", "gato", "perro", "gato", "perro"]))  # Resultado esperado: 0

# print(subsecuencia_mas_larga2(["pez", "hamster", "perro"]))  # Resultado esperado: 2

"""

def subsecuencia_mas_larga(tipos_pacientes_atendidos: list[str]) -> int:

    # Vamos a hacer una lista de tuplas que contenga las primera posicion indice(pos) y la segunda posicion su secuencia correspondiente.
    lista_tuplas = []
    pos_anterior = 0  # indice
    pos = 0
    lista_tmp = []
    for animal in tipos_pacientes_atendidos:
        if animal == "perro" or animal == "gato":
            if len(lista_tmp) == 0: 
               pos = pos_anterior
            lista_tmp.append(animal)
        elif len(lista_tmp) > 0:
            lista_tuplas.append((pos, lista_tmp))
          #  pos_anterior += 1
          #  pos = pos_anterior
            lista_tmp = []
        pos_anterior += 1
       # pos = pos_anterior    
    lista_tuplas.append((pos, lista_tmp))

#    print(lista_tuplas)
    # return lista_tuplas

    longitud_mayor = len(lista_tuplas[0][1])
    primerIndice = lista_tuplas[0][0]
    indice = 0
    for tupla in lista_tuplas:
        if longitud_mayor == len(tupla[1]):
            indice = primerIndice
        elif longitud_mayor < len(tupla[1]):
            longitud_mayor = len(tupla[1])
            indice = tupla[0]

    return indice

"""

# [(0, ['perro', 'gato']), (3, ['perro', 'perro', 'gato']), (7, ['perro', 'gato', 'gato', 'perro'])]

# tipos_pacientes = ["perro", "gato", "loro", "perro","perro", "gato", "pez", "perro", "gato", "gato", "perro"]
# print(subsecuencia_mas_larga(tipos_pacientes))  # Salida: 7

# Ejemplos de prueba
# lista_1 = ["perro", "gato", "pez", "hamster", "perro"]

# print(subsecuencia_mas_larga(["perro", "gato", "pez", "hamster", "perro"])) # Resultado esperado: 0


# print(subsecuencia_mas_larga(["perro", "gato", "pez", "perro", "perro", "gato", "gato"]))  # Resultado esperado: 3


# print(subsecuencia_mas_larga(["perro", "gato", "pez", "perro","gato", "pez", "perro", "gato"]))  # Resultado esperado: 0------

# print(subsecuencia_mas_larga(["perro", "pez", "gato", "pez", "perro", "gato"]))  # Resultado esperado: 4

# print(subsecuencia_mas_larga(["perro", "gato", "perro", "gato", "perro"]))  # Resultado esperado: 0


# print(subsecuencia_mas_larga(["pez", "hamster", "perro"]))  # Resultado esperado: 0

#############################################################################

# print(subsecuencia_mas_larga(["pez", "hamster", "perro", "gato", "gato"]))  # Resultado esperado: 2
