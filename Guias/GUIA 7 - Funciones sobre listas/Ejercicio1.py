# --- EJM 1 ---

def pertenece(lista:list[int],elemento:int)->bool:
    return elemento in lista
print(pertenece([1,2,3],3))

def pertenece3(lista:list[int],elemento:int)->bool:
    indice = 0
    longitud = len(lista)
    while indice < longitud:
        if elemento == lista[indice]:
            return True
        indice += 1
    return False
print(pertenece3([2,3,4],9))

"""
ASI NO SE HACE:
def pertenece2(lista:list[int],elemento:int)->bool:
    indice = 0
    if elemento != lista[indice]:
       indice += 1
       return True
    return False 
print(pertenece2([2,3,4],7))
"""

def pertenece4(lista: list[int], elemento: int) -> bool:
    for item in lista:
        if elemento == item:
            return True
    return False

print(pertenece4([2, 3, 4], 7))

# --- EJM 2 ---

def divide_a_todos(lista:int,numero:int)->bool:
    for i in lista:
        if i % numero != 0:
            return False
    return True
print(divide_a_todos([3,3,71],3))

# --- EJM 3 ---

def suma_total(lista:list[int])->int:
    sumaTotal = 0
    for i in lista:
        elem = i
        sumaTotal += elem
    return sumaTotal
print(suma_total([1,2,3,4,5,6]))

# --- EJM 4 ---

def ordenados(lista:list[int])->bool:
    indice:int= 0
    while indice < len(lista)-1:
        if lista[indice] > lista[indice+1]:
            return False
        indice += 1
    return True
print(ordenados([1,2,9,4,5])) # res = False

# --- EJM 5 ---

def palabras_mayor_a_7(lista:list[str])->bool:
    for i in lista:
        if 7 < len(i):
           return True
    return False
lista = ["hola","camote","ballenas"]
print(palabras_mayor_a_7(lista)) # res = True   






































































































