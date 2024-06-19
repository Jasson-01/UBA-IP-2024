# -------------- PROBLEM-1 ---------------

def ultima_aparicion(s:list[int],e:int)->int:
    posicion = int()
    for i in range(len(s)):
        if s[i] == e :
            posicion = i
    return posicion

#s = [-1,4,0,4,100,0,100,0,-1,-1]
#e = 0
#print(ultima_aparicion(s,e))
# res=7

"""
otra forma:

def ultima_aparicion(s: list[int], e: int) -> int:
    res: int = 0
    for i in range(len(s)):
        if s[i] == e:
            res = i
    return res
"""


# -------------- PROBLEM-2 ---------------

def elementos_exclusivos(s:list[int],t:list[int])->list[int]:
    resultado = []
    for i in range(len(s)):
        if (s[i] not in t) and (s[i] not in resultado):
            resultado.append(s[i])
    for j in range(len(t)):
        if (t[j] not in s) and (t[j] not in resultado):
            resultado.append(t[j])
    return resultado

#s = [-1,4,0,4,3,0,100,0,-1,-1]
#t = [0,100,5,0,100,-1,5]
#print(elementos_exclusivos(s,t))
# res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó
# res = [4,5,3] ó res = [5,3,4] ó res = [5,4,3]

"""
otra forma:

    def elementos_exclusivos(s: list[int], t: list[int]) -> list[int]:
    res: list = []
    for elem in s:
        if elem not in t:
            res.append(elem)
    for num in t:
        if num not in s:
            res.append(num)
    return sacar_repetidos(res)


def sacar_repetidos(lista: list[int]) -> list[int]:
    res: list = []
    while len(lista) > 0:
        elem = lista.pop()
        if elem not in lista:
            res.append(elem)
    return res
"""

# -------------- PROBLEM-3 ---------------

def contar_traducciones_iguales(ingles:dict[str,str],aleman:dict[str,str])->int:
    contador:int = 0
    for i in ingles.values():
        if i in aleman.values():
            contador += 1
    return contador

#aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#ingles = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#print(contar_traducciones_iguales(ingles,aleman))
#res=2

"""
otra forma:

def contar_traducciones_iguales(
    ingles: dict[str, str], aleman: dict[str, str]
) -> int:
    res: int = 0
    for llave, valor in ingles.items():
        if llave in aleman.keys() and valor == aleman[llave]:
            res += 1
    return res

"""

# -------------- PROBLEM-4 ---------------

def convertir_a_diccionario(lista:list[int])->dict[int,int]:
    res = dict()
        
    for i in lista:
        if i not in res:
            res[i] = 0 
        res[i] += 1 
   
    return res 


lista = [-1,0,4,100,100,-1,-1]
#res = {-1:3, 0:1, 4:1, 100:2}
print(convertir_a_diccionario(lista))


"""
otra forma:

 def convertir_a_diccionario(lista: list) -> dict:
     res: dict = {}
     for elem in lista:
         res[elem] = cant_apariciones(elem, lista)
     return res

 def cant_apariciones(elem: int, lista: list) -> int:
     res: int = 0
     for num in lista:
         if num == elem:
             res += 1
     return res

 Otra implementacion
def convertir_a_diccionario(lista: list[int]) -> dict[int, int]:
    res: dict = {}
    for elem in lista:
        if elem in res:
            res[elem] += 1
        else:
            res[elem] = 1
    return res

"""
