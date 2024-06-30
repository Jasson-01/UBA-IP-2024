from queue import Queue as Cola
# from queue import LifoQueue as Pila


# -------------------------------------- PROBLEM-1 --------------------------------------

# def reordenar_cola_priorizando_vips(filaClientes:Cola[str,str])->Cola[str]:

def reordenar_cola_priorizando_vips(filaClientes: Cola[tuple[str, str]]) -> Cola[str]:
    vips = []
    comunes = []

    # Procesar todos los clientes en la cola original
    while not filaClientes.empty():
        cliente = filaClientes.get()
        if cliente[1] == "vip":
            vips.append(cliente[0])
        else:
            comunes.append(cliente[0])

    # Crear una nueva cola con clientes vip primero y comunes después
    nueva_cola = Cola()
    for cliente in vips:
        nueva_cola.put(cliente)
    for cliente in comunes:
        nueva_cola.put(cliente)

    return nueva_cola


"""
# Ejemplo de uso y pruebas

clientes = Cola()
for cliente in [("Alice", "comun"), ("Bob", "vip"), ("Charlie", "comun"), ("Dave", "vip")]:
    clientes.put(cliente)

nueva_cola = reordenar_cola_priorizando_vips(clientes)

# Mostrar la nueva cola para verificar el resultado
while not nueva_cola.empty():
    print(nueva_cola.get())

"""

# -------------------------------------- PROBLEM-2 --------------------------------------


def torneo_de_gallinas(estrategias: dict[str, str]) -> dict[str, int]:
    # Inicializar el diccionario de puntajes
    puntajes = {}
    for jugador in estrategias:
        puntajes[jugador] = 0

    # Lista de jugadores
    jugadores = list(estrategias.keys())

    # Jugar todos contra todos
    for i in range(len(jugadores)):
        for j in range(i + 1, len(jugadores)):
            jugador1 = jugadores[i]
            jugador2 = jugadores[j]
            estrategia1 = estrategias[jugador1]
            estrategia2 = estrategias[jugador2]

            if estrategia1 == "me desvio siempre" and estrategia2 == "me desvio siempre":
                # Ambos se desvían
                puntajes[jugador1] -= 10
                puntajes[jugador2] -= 10
            elif estrategia1 == "me la banco y no me desvio" and estrategia2 == "me la banco y no me desvio":
                # Ambos chocan
                puntajes[jugador1] -= 5
                puntajes[jugador2] -= 5
            elif estrategia1 == "me desvio siempre" and estrategia2 == "me la banco y no me desvio":
                # Jugador1 se desvía, Jugador2 no
                puntajes[jugador1] -= 15
                puntajes[jugador2] += 10
            elif estrategia1 == "me la banco y no me desvio" and estrategia2 == "me desvio siempre":
                # Jugador1 no se desvía, Jugador2 se desvía
                puntajes[jugador1] += 10
                puntajes[jugador2] -= 15

    return puntajes


"""
# Ejemplo de uso y pruebas
estrategias = {
    "Alice": "me desvio siempre",
    "Bob": "me la banco y no me desvío",
    "Charlie": "me desvio siempre",
    "Dave": "me la banco y no me desvío"
}

resultados = torneo_de_gallinas(estrategias)
print(resultados)
"""

# -------------------------------------- PROBLEM-3 --------------------------------------


def quien_gano_el_tateti_facilito(tablero: list[list[str]]) -> int:
    n = len(tablero)

    def hay_tres_consecutivos_en_columna(caracter: str) -> bool:
        for col in range(n):
            contador = 0
            for fila in range(n):
                if tablero[fila][col] == caracter:
                    contador += 1
                    if contador == 3:
                        return True
                else:
                    contador = 0
        return False

    x_gano = hay_tres_consecutivos_en_columna('X')
    o_gano = hay_tres_consecutivos_en_columna('O')

    if x_gano and o_gano:
        return 3
    elif x_gano:
        return 1
    elif o_gano:
        return 2
    else:
        return 0


"""
# Ejemplos de prueba
tablero1 = [
    ['X', ' ', 'O', ' ', ' '],
    ['X', ' ', 'O', ' ', ' '],
    ['X', ' ', ' ', ' ', ' '],
    [' ', ' ', 'O', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']
]

tablero2 = [
    ['X', ' ', 'O', ' ', ' '],
    ['X', ' ', 'O', ' ', ' '],
    ['O', ' ', 'O', ' ', ' '],
    ['X', ' ', 'O', ' ', ' '],
    [' ', ' ', 'X', ' ', ' ']
]

tablero3 = [
    ['X', ' ', 'O', ' ', ' '],
    ['X', ' ', ' ', ' ', ' '],
    ['O', ' ', ' ', ' ', ' '],
    [' ', ' ', 'O', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']
]

tablero4 = [
    ['X', ' ', 'O', ' ', ' '],
    ['X', ' ', 'O', ' ', ' '],
    ['O', ' ', 'O', ' ', ' '],
    ['X', ' ', 'O', ' ', ' '],
    ['O', ' ', 'X', ' ', ' ']
]
"""

# print(quien_gano_el_tateti_facilito(tablero1))  # Debería imprimir 1
# print(quien_gano_el_tateti_facilito(tablero2))  # Debería imprimir 2
# print(quien_gano_el_tateti_facilito(tablero3))  # Debería imprimir 0
# print(quien_gano_el_tateti_facilito(tablero4))  # Debería imprimir 3


################# 2DA FORMA #################

def hay_tres_concecutivos_en_columna2(tablero: list[list[str]], caracter: str) -> bool:
    for row in range(len(tablero)):
        contador = 0
        for col in range(len(tablero[0])):
            if tablero[col][row] == caracter:
                contador += 1
                if contador == 3:
                    return True
            else:
                contador = 0
    return False


def quien_gano_el_tateti_facilito2(tablero: list[list[str]]) -> int:

    gano_x = hay_tres_concecutivos_en_columna2(tablero, 'X')
    gano_y = hay_tres_concecutivos_en_columna2(tablero, 'O')

    if gano_x == True and gano_y == False:
        return 1

    if gano_x == False and gano_y == True:
        return 2

    if gano_x == False and gano_y == False:
        return 0

    if gano_x == True and gano_y == True:
        return 1


# -------------------------------------- PROBLEM-4 --------------------------------------

def es_palindromo(texto: str) -> bool:
    n = len(texto)
    for i in range(n // 2):
        if texto[i] != texto[n - i - 1]:
            return False
    return True


def generar_sufijo(texto: str, inicio: int) -> str:
    sufijo = ""
    for i in range(inicio, len(texto)):
        sufijo += texto[i]
    return sufijo


def cuantos_sufijos_son_palindromos(texto: str) -> int:
    contador_palindromos = 0
    n = len(texto)

    for i in range(n):
        sufijo = generar_sufijo(texto, i)
        if es_palindromo(sufijo):
            contador_palindromos += 1

    return contador_palindromos


# Ejemplos de prueba
# Debería imprimir 1 ("o" es el único sufijo palíndromo)
print(cuantos_sufijos_son_palindromos("Diego"))
# Debería imprimir 3 ("aabaa", "aa", "a" son palíndromos)
print(cuantos_sufijos_son_palindromos("aabaa"))
# Debería imprimir 1 ("racecar" es el único sufijo palíndromo)
print(cuantos_sufijos_son_palindromos("racecar"))
# Debería imprimir 0 (no hay sufijos palíndromos)
print(cuantos_sufijos_son_palindromos("abc"))
# Debería imprimir 2 ("ababa", "a" son palíndromos)
print(cuantos_sufijos_son_palindromos("ababa"))
