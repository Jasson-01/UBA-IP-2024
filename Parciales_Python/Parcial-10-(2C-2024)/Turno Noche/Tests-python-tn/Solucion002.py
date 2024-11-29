from queue import Queue as Cola
from queue import LifoQueue as Pila
import math

#------------------ Ejercicio 1 -------------------------------------------------------------------------
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
                           

#------------------ Ejercicio 2 -------------------------------------------------------------------------


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

#------------------ Ejercicio 3 -------------------------------------------------------------------------


def copia_pila(p:Pila)->Pila:
    nueva_pila:Pila = Pila()
    temporal:Pila = Pila()
    while not(p.empty()):
        elem = p.get()
        temporal.put(elem)
    while not(temporal.empty()):
        elem02 = temporal.get()
        nueva_pila.put(elem02)
        p.put(elem02)
    return nueva_pila    

def calcular(cuenta:str)->int:
    res_acumulado = 0 
    numero_actual = 0 
    signo = 1 # 1 para suma, -1 para resta

    for caracter in cuenta:
        if caracter == "+" or caracter == "-":
           res_acumulado += signo * numero_actual
           numero_actual = 0
           if caracter == "+":
               signo = 1 
           else:
               signo = -1
        else:
           numero_actual = numero_actual * 10 + int(caracter)        

    # agrego el último número al resultado
    res_acumulado += signo * numero_actual
    return res_acumulado

def resolver_cuentas(A: Pila[str]):
    copia_A:Pila = copia_pila(A)
    res_str = []
    while not(copia_A.empty()):
       saco_el_str = copia_A.get() 
       calculando = calcular(saco_el_str)
       res_str.append(calculando)
    return res_str 

# pila002 = Pila()
# pila002.put("85+4-2+7")
# op = resolver_cuentas(pila002)
# print(op) # [17]


#------------------ Ejercicio 4 -------------------------------------------------------------------------

def pertenece_tupla(dupla:tuple[int,int],tupla:list[tuple[int,int]])->bool:
    for dupla2 in tupla:
        if dupla == dupla2:
            return True
    return False

def sin_repetidos(lista:list[int])->list[int]:
    lista_nueva:list[int] = []
    for num in lista:
        if not(pertenece(num,lista_nueva)):
            lista_nueva.append(num)
    return lista_nueva         

def tuplas_a_listaNumeros(tupla:list[tuple[int,int]])->list[int]:
    lista_nueva:list[int] = []
    for dupla in tupla:
        lista_nueva.append(dupla[0])
        lista_nueva.append(dupla[1])
    return lista_nueva

def dame_el_que_falta(s: list[tuple[int,int]]):
    maximo_numero_tupla:int = int(math.sqrt(len(s)+1))
    todos_los_numeros_de_la_tupla:list[int] = sin_repetidos(tuplas_a_listaNumeros(s))
    # (fst, #)
    for num1 in todos_los_numeros_de_la_tupla:
        for num2 in todos_los_numeros_de_la_tupla:
            if not(pertenece((num1,num2),s)):
                return (num1,num2)

# s = [(1,1),(2,1),(1,2)]
# op = dame_el_que_falta(s)
# print(op) -----------------> res = (2,2)








########## Hecho en el parcial

# def pertenece_tuplas(elem:tuple[int,int],lista:list[tuple[int,int]])->bool:
#     for num in lista:
#         if elem == num:
#             return True
#     return False     

# def lista_numero(lista:list[tuple[int,int]])->list[int]:
#     lista_nueva = []
#     for dupla in lista:
#         lista_nueva.append(dupla[0])
#         lista_nueva.append(dupla[0])
#     return lista_nueva 

# def dame_el_que_falta(s: list[tuple[int,int]]) -> tuple[int,int]:
    
#     dupla_faltante01 = tuple()
#     s_copia:list[tuple[int,int]] = s.copy()
#     numero_maximo:int = maximo(lista_numero(s_copia)) 
#     dupla_faltante = (numero_maximo,numero_maximo) 
     
#     if not(pertenece(dupla_faltante,s_copia)):
#        dupla_faltante01 = dupla_faltante
#     return dupla_faltante01

   
