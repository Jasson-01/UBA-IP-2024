#ejemplos con diccionario
from typing import TypeVar #, Tuple
from queue import LifoQueue as Pila
from queue import Queue as Cola
import random

T = TypeVar('T')


#creo un dicc con algunos pares de clave-valor
mi_dicc: dict[str, str] = {
    'auto': 'car',
    'sol': 'sun',
    'luna': 'moon'
}

#agrego clave-valor
mi_dicc['una_clave'] = 'un_valor'

#reemplazo el valor de una clave
mi_dicc['una_clave'] = "nuevo valor"

#recupero un valor
v:str = mi_dicc['una_clave']


#recorro un dicc, lo imprimo y lo copio a otro diccionario
nuevo_dic: dict[str, str] = {} #creo un dicc vacio

# recupero las claves y luego, con cada clave, recupero su valor y lo imprimo
claves:list[str] = mi_dicc.keys() 
for clave in claves:    
    valor:str = mi_dicc[clave]
    print(clave + ' - ' + valor)  
    #modo python es: print(f'{clave} - {valor}') 
    nuevo_dic[clave] = valor #lo agrego al nuevo diccionario



#otra forma de recorrer un dicc
otro_dic: dict[str, str] = {} #creo un dicc vacio
for clave, valor in mi_dicc.items():    
    print(clave + ' - ' + valor)   
    #modo python es: print(f'{clave} - {valor}') 
    otro_dic[clave] = valor #lo agrego al nuevo diccionario

# recupero solo los valores y los imprimo
valores:list[str] = otro_dic.values() 
for v in valores:    
    print(v)  


#creo un dicc donde la clave representa un día y el valor es una tupla con la temp mín y max
temp_por_dia: dict[int, (float, float)] = {
    1: (10.5, 20),
    2: (10.3, 20.6),
    3: (1.5, 20)
}

def dia_de_menor_minima (temps :dict[int, (float, float)] ) -> int:
    #asumo que hay por lo menos un día con su temp.
    res: int = list(temps.keys()) [0]  
    temp_min = temps [res] [0] 
    for c, v in temps.items():    
        min_dia:float = v[0]  
        if temp_min > min_dia:
            temp_min = min_dia
            res = c

    return res

dia = dia_de_menor_minima (temp_por_dia)
print(dia)


#3
#13
def generar_nros_al_azar_cola(n: int, desde: int, hasta: int) -> Cola[int]:
    res:Cola[int] = Cola()
    for _ in range(n):
        x = random.randint(desde, hasta)
        res.put(x)

    return res

#imprimir (generar_nros_al_azar_cola(5,0,10))


def pertenece (cadena: list[T], elem:T) -> bool:
    for i in cadena:
        if i == elem: 
            return True
    return False

#16
def armar_secuencia_de_bingo() -> Cola[int]:
    numeros: list[int] = []
    cola: Cola[int] = Cola()

    while len (numeros) < 100:
        n = random.randint(0,99)
        if not pertenece(numeros, n): 
            cola.put(n)
            numeros.append(n)

    return cola

print(armar_secuencia_de_bingo())


def armar_secuencia_de_bingo_mas_rapido() -> Cola[int]:
    numeros: list[int] = list (range (0,100))
    res: Cola[int] = Cola()
    hasta = 99
    for hasta in range (99, -1, -1):
        i = random.randint(0,hasta)
        v = numeros[i] 
        res.put (v)
        numeros.pop (i) # confirmar si se puede usar en el parcial
        #hasta -= 1
    return res

#print(armar_secuencia_de_bingo_mas_rapido().queue)

def armar_secuencia_de_bingo_con_shuffle() -> Cola[int]:
    numeros: list[int] = list(range(100))
    random.shuffle(numeros) # confirmar si se puede usar en el parcial
    cola: Cola[int] = Cola()

    for num in numeros:
        cola.put(num)

    return cola

#crea un duplicado de una cola, restaurando la original luego de recorrerla
def copiar_cola (original:Cola )-> Cola:
    res: Cola = Cola()
    cola_tmp: Cola = Cola()

    while not (original.empty()):
        v = original.get()
        res.put(v)
        cola_tmp.put(v)

    while not (cola_tmp.empty()):
        v = cola_tmp.get()
        original.put(v)

    return res

#versión que no modifica los parámetros, que son in
def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    jugadas: int = 0
    aciertos: int = 0
    copia = copiar_cola(bolillero)

    while aciertos < len(carton):
        jugada: int = copia.get()
        jugadas += 1

        if (pertenece (carton, jugada)): #es lo mismo que if jugada in carton:
            aciertos += 1
    return jugadas

#carton es de tipo in, no se puede modificar, por eso usar la otra versión
def jugar_carton_de_bingo_v2(carton: list[int], bolillero: Cola[int]) -> int:
    jugadas: int = 0

    #while bolillero: es lo mismo que "while not bolillero.empty():"
    while not (bolillero.empty()):
        jugada: int = bolillero.get()
        jugadas += 1

        if (pertenece (carton, jugada)): #es lo mismo que if jugada in carton:
            carton.remove(jugada)

            if len (carton) == 0 : # es lo mismo que: if not carton:
                return jugadas

    return -1  # Si no se gano el bingo, se devuelve -1


bolillero = armar_secuencia_de_bingo()
#carton = [4, 10, 25, 46, 60, 73, 84, 90, 33, 67, 78, 95]
carton = [4]
jugadas = jugar_carton_de_bingo(carton, bolillero)

if jugadas != -1:
    print(f"Ganaste el bingo en {jugadas} jugadas")
else:
    print("No se gano el bingo.")


#esta función hace lo mismo que la función split() que ya viene con str
def mi_split(linea: str) -> list[str]:
    res:list[str] = []
    palabra = ""
    for char in linea:
        if char == " " or char == "\t" or char == "\n" or char == "\r":
            if len(palabra) > 0:
                res.append(palabra)
                palabra = ""
        else:
            palabra += char
    if len(palabra) > 0:  # para añadir la última palabra si no termina en un espacio
        res.append(palabra)
    return res

def palabras_de_archivo(nombre_archivo: str)-> list[str]:
    with open(nombre_archivo, 'r') as archivo:
        contenido: str = archivo.read()
        
        return mi_split(contenido) #es lo mismo que: contenido.split()

#4. Diccionarios

def pertenece_dicc (dic:dict, clave) -> bool:
    lista:list = list(dic.keys())
    return pertenece(lista, clave)

#19 
def agrupar_por_longitud(nombre_archivo: str) -> dict:
    resultado: dict[str, int] = {}

    palabras: list[str] = palabras_de_archivo(nombre_archivo)
    for palabra in palabras:
        longitud = len(palabra)
        if pertenece_dicc(resultado, longitud): #es lo mismo que: if longitud in resultado:
            resultado[longitud] += 1
        else:
            resultado[longitud] = 1             

    return resultado

# x = agrupar_por_longitud("p8 ejemplos.txt")
# for clave, valor in x.items():
#    print(clave, valor)



#21
def la_palabra_mas_frecuente(nombre_archivo: str) -> str:

    palabras: list[str] = palabras_de_archivo (nombre_archivo)
    contador: dict[str, int] = {}

    for palabra in palabras:
        if pertenece_dicc(contador, palabra): # es lo mismo que:  if palabra in contador:
            # contador[palabra] = contador[palabra] + 1
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    palabra_mas_frecuente: str = ''
    frecuencia_maxima: int = 0

    for palabra, frecuencia in contador.items():
        if frecuencia > frecuencia_maxima:
            frecuencia_maxima = frecuencia
            palabra_mas_frecuente = palabra

    return palabra_mas_frecuente
    
print (la_palabra_mas_frecuente("p8 ejemplos.txt")) 
