from queue import Queue as Cola
import random

"""
c = Cola ()
c . put (1) # encolar
elemento = c . get () # desencolar ()
c . empty () # vacia ?
"""

# --------- EJM-13 -------

def generar_numeros_al_azar(cantidad,desde,hasta)->Cola[int]:
    res:Cola[int] = Cola()
    for _ in range(cantidad):
        x:int = random.randint(desde,hasta)
        res.put(x)
    return res 

print(generar_numeros_al_azar(5,3,6).queue)

# --------- EJM-16 -------

# 1)


"""
def armar_secuencia_de_bingo()->Cola[int]:
    res:Cola = Cola()
    numeros:list = list(range(100)) #[0,1,2,3,...,99]

    while len(numeros) > 0 :
        i = random.randint(0,len(numeros))
        v = numeros[i]
        res.put(v)
        numeros.pop(v)
"""

#def armar_secuencia_de_bingo()->Cola[int]:
#    numeros: list[int] = []
#    cola: Cola[int] = Cola()

#    while len(numeros) < 100 :
#        n = random

# 2)
"""
def jugar_carton_de_bingo(carton : list[int],bolillero : Cola[int]) -> int:
    res:int = 0
    copia = copiar_cola(bolichero)
    aciertos:int = 0
    
    while aciertos < len(carton):
        v= copia.get()
        res += 1
        if pertenece(carton,v):
            acierto += 1 
    return res 
"""

def copiar_lista(lista:list[int])->list:
    res = []
    for v in lista:
        res.append(v)
    return res 
"""
def copiar_cola(original:Cola)->Cola:
    res: Cola = Cola()
    cola_tmp :Cola = Cola()

    while not (original.empty()):
        v = original.get()
"""          

# --------- EJM-19 ------- (DICCIONARIOS)

#def agrupar_por_longitud(nombre_archivo:str)->dict:
    

# PARA DICCIONARIOS
def pertenece(D:dict,k)->bool:
    lista = list(D.keys())
    for e in lista:
        if e == k:
            return True
    return False
    
# --------- EJM-21 ------- (DICCIONARIOS)

#def la_palabra_mas_frecuente(nombre_archivo : str) -> str:

















