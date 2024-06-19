# ------------- PROBLEM - 1 -------------

def verificar_transacciones(lista:str)->int:
    saldo_anterior:int = 0
    saldo_actual:int = 0
    for i in range(len(lista)):
            if lista[i] == "r":
                saldo_anterior += 350
            elif lista[i] == "v":
                saldo_anterior -= 56
                if saldo_anterior < 0 :
                     return saldo_actual                
            elif lista[i] == "s":
                saldo_actual = saldo_anterior
            elif lista[i] == "x":
                return saldo_anterior    
    return saldo_anterior

#s = "rrvvx"
#print(verificar_transacciones(s))


#Ejemplo 1:
#s1 = "ssrvvrrvvsvvsxrvvv"
#res = 714
#print(verificar_transacciones(s1))
#Ejemplo 2:
#s2 = "ssrvvvvsvvsvvv"
#res = 14 (en este caso el programa termina porque el saldo no alcanza para realizar un viaje que está entre las transacciones)
#print(verificar_transacciones(s2))
                
#-------------2DA FORMA / ChatGPT
def verificar_transacciones2(lista: str) -> int:
    saldo: int = 0
    for transaccion in lista:
        if transaccion == "r":
            saldo += 350
        elif transaccion == "v":
            if saldo < 56:
                return saldo  # Saldo insuficiente, retorno el saldo actual
            saldo -= 56
        elif transaccion == "x":
            return saldo  # Finaliza el programa
    return saldo  # Retorno el saldo al finalizar todas las transacciones

# Ejemplos de prueba
#print(verificar_transacciones2("rrvvx"))  # Debería devolver 588
#print(verificar_transacciones2("rvvx"))   # Debería devolver 238

# ------------- PROBLEM - 2 -------------

def minimo(lista:list[int])->int:
     num = lista[0]
     for i in lista: 
          if i <= num:
               num = i  
     return num 

#lista = [2,1,6]
#print(minimo(lista))

def valor_minimo(temperaturas:list[(int,int)])->list:
    listaMinimos = []
    for i in temperaturas:
            listaMinimos.append(i[0]) 
    return minimo(listaMinimos)


#s = [(1.0, 5.2), (10.4, 15.1), (19.7, 28.9), (25.4, 35.6), (-3.1, 1.3)]
#s = [(-1.0, 4.0), (-0.5, 3.5), (0.0, 4.5), (1.0, 5.0)]

# res = -3.1
#print(valor_minimo(s))

# ------------- PROBLEM - 3 -------------
# Hecho por ChatGPT

def valores_extremos(cotizaciones_diarias: dict[str, list[tuple[int, float]]]) -> dict[str, tuple[float, float]]:
    res = {}
    for empresa, cotizaciones in cotizaciones_diarias.items():
        # Inicializamos min_val y max_val con el primer valor de la lista de cotizaciones
        min_val, max_val = cotizaciones[0][1], cotizaciones[0][1]
        for _, valor in cotizaciones:
            if valor < min_val:
                min_val = valor
            if valor > max_val:
                max_val = valor
        res[empresa] = (min_val, max_val)
    return res


#cotizaciones_diarias = {"YPF" : [(1,10),(15, 3), (31,100)], "ALUA" : [(1,0), (20, 50), (31,30)]}
# resultado_esperado es: {"YPF" : (3,100), "ALUA" : (0,50)}
#print(valores_extremos(cotizaciones_diarias))

# ------------- PROBLEM - 4 -------------

def filas_validas(matriz:list[list[int]])->bool:
    for fila in matriz:
        elementos_vistos = []
        for pos in fila:
            if pos == 0:
                elementos_vistos.append(pos)
            elif pos not in elementos_vistos:
                elementos_vistos.append(pos)
            else:
                return False
        elementos_vistos = []    
    return True    
"""
matriz_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(filas_validas(matriz_1))
"""

def columnas_validas(matriz: list[list[int]]) -> bool:

    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    for col in range(num_columnas):
        elementos_vistos = []
        for fila in range(num_filas):
            elemento = matriz[fila][col]
            if elemento != 0:
               if elemento in elementos_vistos:
                  return False
               elementos_vistos.append(elemento)

    return True

def es_sudoku_valido(matriz:list[list[int]])->bool:
    if (filas_validas(matriz) == True) and (columnas_validas(matriz) == True) :
         return True 
    return False    


#m = [
#[1, 2, 3, 4, 5, 6, 7, 8, 9],
#[9, 8, 7, 6, 4, 5, 3, 2, 1],
#[0, 0, 0, 0, 0, 0, 1, 0, 0],
#[0, 0, 0, 0, 0, 4, 0, 0, 0],
#[0, 0, 0, 0, 6, 0, 0, 0, 0],
#[0, 0, 0, 5, 0, 0, 0, 0, 0],
#[0, 0, 4, 0, 0, 0, 0, 0, 0],
#[0, 3, 0, 0, 0, 0, 0, 0, 0],
#[2, 0, 0, 0, 0, 0, 0, 0, 0]
#]
# se debería devolver res = true

m6 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
print(es_sudoku_valido(m6))  # Resultado esperado: True

