# Code by Agustín Sansone

from queue import Queue as Cola

# Ejercicio 1
def subsecuencia_mas_larga(v: list[int]) -> tuple[int,int]:
    res: tuple[int,int] = (1,0)
    for desde in range(len(v)):
        for hasta in range(desde+1, len(v)):
            if abs( v[hasta] - v[hasta-1] ) != 1:
                break
            longitud_actual = hasta - desde + 1
            if longitud_actual > res[0]:
                res = (longitud_actual, desde)
    return res
 
# Ejercicio 2
def mejor_resultado_de_ana(examenes: Cola[list[bool]]) -> list[int]:
    examenes_copia: Cola[list[bool]] = Cola()
    res: list[int] = []
    while not examenes.empty():
        examen: list[bool] = examenes.get()
        examenes_copia.put(examen)
        respuestas_verdaderas: int = 0
        for respuesta in examen:
            respuestas_verdaderas += int(respuesta)
        respuestas_falsas: int = len(examen) - respuestas_verdaderas
        res.append( min(len(examen)//2, respuestas_verdaderas) + min(len(examen)//2, respuestas_falsas) )
    while not examenes_copia.empty():
        examenes.put( examenes_copia.get() )
    return res

# Ejercicio 3
def cambiar_matriz(A: list[list[int]]) -> None:
    maximo_elemento: int = len(A) * len(A[0])
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = (A[i][j] % maximo_elemento) + 1

# Ejercicio 4
def palabras_por_vocales(texto: str) -> dict[int, int]:
    texto += ' '
    palabras: list[str] = []
    palabra_actual: str = ""
    for c in texto:
        if c == ' ':
            if len(palabra_actual) != 0:
                palabras.append(palabra_actual)
                palabra_actual = ""
        else:
            palabra_actual += c
    res: dict[int, int] = {}
    for palabra in palabras:
        vocales_de_palabra: int = 0
        for c in palabra:
            vocales_de_palabra += int(c in "aeiouAEIOU")
        if vocales_de_palabra in res:
            res[ vocales_de_palabra ] += 1
        else:
            res[ vocales_de_palabra ] = 1        
    return res