from queue import Queue as Cola
from queue import LifoQueue as Pila

# Ejercicio 1
def pertenece(elem:int,lista:list[int])->bool:
    for num in lista:
        if elem == num:
            return True
    return False     

def lista_sin_repetidos(lista:list[int])->list[int]:
    no_hay_repetidos:list[int] = []
    for num01 in lista:
        if not(pertenece(num01,no_hay_repetidos)):
            no_hay_repetidos.append(num01)
    return no_hay_repetidos        

def es_primo(num02:int)->bool:
    lista:list[int] = []
    divisor:int = 1 
    while divisor <= num02:  
      if num02 % divisor == 0:
         lista.append(divisor)
      divisor += 1
   
    if len(lista) > 2 or len(lista) == 1:
        return False
    return True

def divisores_de(num:int)->list[int]:
    divisor:int = 2
    lista_divisores:list[int] = []
    while divisor <= num:
        if num % divisor == 0:
           lista_divisores.append(divisor)
        divisor += 1 
    return lista_divisores       

def lista_de_divisores_primos(lista:list[int])->list[int]:
    lista_nueva:list[int] = []
    for i in range(len(lista)):
        lista_de_divisores_comunes = divisores_de(lista[i])
        for j in range(len(lista_de_divisores_comunes)):
            if es_primo(lista_de_divisores_comunes[j]):
                lista_nueva.append(lista_de_divisores_comunes[j])
                
    return lista_nueva    
       
def multiplos_de_primos(v: list[int]) -> dict[int,int]:
    lista_de_enteros:list[int] = v.copy()
    formando_diccionario:dict = dict()
    lista_de_primos_de:list[int] = lista_sin_repetidos(lista_de_divisores_primos(lista_de_enteros))
    for primo in lista_de_primos_de:
        contador_de_divisores:int = 0
        for i in range(len(lista_de_enteros)):
            if lista_de_enteros[i] % primo == 0:
                contador_de_divisores += 1 
        formando_diccionario[primo] = contador_de_divisores  
    return formando_diccionario
                           

# Ejercicio 2

def maximo(lista:list[int])->int:
    max:int = lista[0]
    for i in range(len(lista)):
        if lista[i] >= max:
            max = lista[i]
    return max 

def longitud_mas_grande(A: list[list[int]]) -> int:
    
    listas_de_longitudes:list[int] = []
    lista_de_listas_de_unos:list[list[int]] = []
    lista_de_uno:list[int] = []
    for fila in A:
        for i in range(len(fila)):
            if fila[i] == 1:
                lista_de_uno.append(fila[i])
            elif fila[i] != 1 and len(lista_de_uno) > 0:
                lista_de_listas_de_unos.append(lista_de_uno)
                lista_de_uno = []
        if len(lista_de_uno) > 0:
            lista_de_listas_de_unos.append(lista_de_uno) 
    
    for fila02 in lista_de_listas_de_unos:
        listas_de_longitudes.append(len(fila02))
    
    return max(listas_de_longitudes)       

# Ejercicio 3

def resolver_cuentas(A: Pila[str]) -> list[int]:
    return []  


# Ejercicio 4

def pertenece_tuplas(elem:tuple[int,int],lista:list[tuple[int,int]])->bool:
    for num in lista:
        if elem == num:
            return True
    return False     

def lista_numero(lista:list[tuple[int,int]])->list[int]:
    lista_nueva = []
    for dupla in lista:
        lista_nueva.append(dupla[0])
        lista_nueva.append(dupla[0])
    return lista_nueva 

def dame_el_que_falta(s: list[tuple[int,int]]) -> tuple[int,int]:
    
    dupla_faltante01 = tuple()
    s_copia:list[tuple[int,int]] = s.copy()
    numero_maximo:int = maximo(lista_numero(s_copia)) 
    dupla_faltante = (numero_maximo,numero_maximo) 
     
    if not(pertenece(dupla_faltante,s_copia)):
       dupla_faltante01 = dupla_faltante
    return dupla_faltante01

   
