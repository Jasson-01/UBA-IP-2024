# --- EJM 1 ---

def pertenece(lista:list[int],elemento:int)->bool:
    return elemento in lista
#print(pertenece([1,2,3],3))

def pertenece3(lista:list[int],elemento:int)->bool:
    indice = 0
    longitud = len(lista)
    while indice < longitud:
        if elemento == lista[indice]:
            return True
        indice += 1
    return False
#print(pertenece3([2,3,4],9))

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

#print(pertenece4([2, 3, 4], 7))

# --- EJM 2 ---

def divide_a_todos(lista:int,numero:int)->bool:
    for i in lista:
        if i % numero != 0:
            return False
    return True
#print(divide_a_todos([3,3,71],3))

# --- EJM 3 ---

def suma_total(lista:list[int])->int:
    sumaTotal = 0
    for i in lista:
        elem = i
        sumaTotal += elem
    return sumaTotal
#print(suma_total([1,2,3,4,5,6]))

# --- EJM 4 ---

def ordenados(lista:list[int])->bool:
    indice:int= 0
    while indice < len(lista)-1:
        if lista[indice] > lista[indice+1]:
            return False
        indice += 1
    return True
#print(ordenados([1,2,9,4,5])) # res = False

# --- EJM 5 ---

def palabras_mayor_a_7(lista:list[str])->bool:
    for i in lista:
        if 7 < len(i):
           return True
    return False
lista = ["hola","camote","ballenas"]
#print(palabras_mayor_a_7(lista)) # res = True   

# --- EJM 6 ---


def texto_reverso(texto:str)->str:
    nuevoTexto:str = ""
    for i in range(len(texto)-1,-1,-1):
        nuevoTexto += texto[i]
    return nuevoTexto
#print(texto_reverso("anita"))



def es_palindromo(texto:str)->bool:
    textoReverso:str = texto_reverso(texto) 
    if texto == textoReverso:
        return True
    return False

#print(es_palindromo("salas"))

#roma


# --- EJM 7 ---

def tiene_letra_minuscula(texto:str)->bool: # RETORNA "TRUE" SI TIENE ALMENOS UNA LETRA Minuscula
    listaMinusculas:str = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(texto)):
        if texto[i] in listaMinusculas:
            return True
    return False
#print(tiene_letra_minuscula("HOLAz")) 

def tiene_letra_mayuscula(texto:str)->bool: # RETORNA "TRUE" SI TIENE ALMENOS UNA LETRA MAYUSCULA
    listaMayuscula:str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(texto)):
        if texto[i] in listaMayuscula:
            return True
    return False
#print(tiene_letra_mayuscula("aabcZ")) 

def tiene_digito(texto:str)-> bool: # RETORNA "TRUE" SI TIENE AL MENNOS UN DIGITO
    listaDigitos:str= "0123456789"
    for i in range(len(texto)):
        if texto[i] in listaDigitos:
            return True
    return False
#print(tiene_digito("aabc3")) 

def fortaleza(contrasena:str)->str:
    if (len(contrasena) > 8) and (tiene_digito(contrasena) and (tiene_letra_mayuscula(contrasena)) and (tiene_letra_minuscula(contrasena))) :
        return "VERDE"
    if len(contrasena) < 5 :
        return "ROJA"
    else:
        return "AMARILLA"
#print(fortaleza("esTe3sVerde"))
#print(fortaleza("roja"))
#print(fortaleza("esamarilla"))

# --- EJM 8 ---

def devolver_saldo_actual(lista:list[tuple])->int:
    saldo_total = 0
    for i in range(len(lista)):
        if lista[i][0] == "I" :
           saldo_total += lista[i][1]
        if lista[i][0] == "R" :
           saldo_total -= lista[i][1]
    return saldo_total

#print(devolver_saldo_actual([("I",2000), ("R", 20),("R", 1000),("I", 300)]))     

#[(‘‘I’’,2000), (‘‘R’’, 20),(‘‘R’’, 1000),(‘‘I’’, 300)] entonces el saldo actual es 1280

# --- EJM 9 ---

def esVocal(letra:str)->bool:
    listaVocales = "aeiou" or "AEIOU"
    return letra in listaVocales


def sacando_vocales(palabra:str)->str:
    lista:str = ""
    for i in range(len(palabra)):
       if  esVocal(palabra[i]):
           lista += palabra[i]
    return lista 
#print(sacando_vocales("hola"))   

def sacando_repetidos(lista:str)->str:
    listaNueva:str = ""
    for i in range(len(lista)) :
        if (i == len(lista)-1) or (lista[i] != lista[i+1]) :
            listaNueva += lista[i]
    return listaNueva

#print(sacando_repetidos("ooaabbbbbcccccccdddddddeeeeeeeeeeeeeeeefffffffffffffffff"))

def tiene_al_menos_tres_vocales_distintas(palabra:str)->bool:
    if len(sacando_repetidos(sacando_vocales(palabra))) >= 3:
        return True
    return False
#print(tiene_al_menos_tres_vocales_distintas("holate"))     

            

























































































