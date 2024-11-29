from queue import LifoQueue as Pila
import math
from typing import TypeVar 

T = TypeVar('T')


# Ejercicio 1
def pertenece(cadena: list[T], elem: T) -> bool:
    for i in cadena:
        if i == elem:
            return True
    return False

def multiplos_de_primos(v: list[int]) -> dict[int, int]:
    res: dict[int, int] = {}
    for elem in v:
        for divisor in range(2, elem+1):
            if es_primo(divisor) and elem % divisor == 0:
                    incrementar(res, divisor)
    return res

def incrementar(diccionario: dict[int, int], primo: int) -> bool:
    if pertenece(diccionario.keys(), primo):
        diccionario[primo] += 1
    else:
        diccionario[primo] = 1

def es_primo(numero: int) -> bool:
    for valor in range (2, numero):
        if numero % valor == 0: 
            return False
    return True


# Ejercicio 2
def longitud_mas_grande(m: list[list[int]]) -> int:    
    longitud_maxima = 0
    longitud_actual = 0
    
    for indice_fila in range(len (m)):
        longitud_actual = 0
        for indice_columna in range (len(m[indice_fila])):
            if m[indice_fila][indice_columna] == 1:
                longitud_actual += 1  
            else: 
                if longitud_actual > 0: # si termino una secuencia de 1s
                    if longitud_actual > longitud_maxima: # si encontré nuevo max
                        longitud_maxima = longitud_actual
                    longitud_actual = 0

        # lo siguiente puede ocurrir si la fila termina con 1
        if longitud_actual > longitud_maxima: # si encontré nuevo max
            longitud_maxima = longitud_actual

    return longitud_maxima


# Ejercicio 3
def resolver_cuentas(p: Pila [str]) -> list[str]:
    p_copia: Pila[str] = Pila()
    res: list[str] = []

    while not p.empty():
        cuenta:str = p.get()
        p_copia.put(cuenta)
        res.append(calcular(cuenta)) 

    #restauro pila
    while not p_copia.empty():
        p.put(p_copia.get())
    return res

def calcular(cuenta: str):
    res = 0
    numero_actual = 0
    signo = 1  # 1 para suma, -1 para resta

    for caracter in cuenta:
        if caracter == "+" or caracter == "-":
            # agrego el número actual al resultado acumulado
            res += signo * numero_actual
            numero_actual = 0
            if caracter == "+":
                signo = 1
            else:
                signo = -1
        else:
            numero_actual = numero_actual * 10 + int(caracter)

    # agrego el último número al resultado
    res += signo * numero_actual
    return res


# Ejercicio 4
def dame_el_que_falta(s: list[tuple[int, int]]) -> tuple[int, int]:
    max: int = int(math.sqrt(len(s) + 1))
    for i in range(1, max + 1):
        for j in range(1, max + 1):
            if not pertenece(s, (i, j)):
                return (i, j)
