# -------------------------- EJERCICIO-1 -------------------------- 

def quienGana(j1:str,j2:str)->str:

    if (j1 == "Piedra") and (j2 == "Tijera"):
        return "Jugador1"
    elif (j1 == "Tijera") and (j2 == "Papel"):
        return "Jugador1"
    elif (j1 == "Papel") and (j2 == "Piedra"):
        return "Jugador1"
    
    elif (j1 == "Tijera") and (j2 == "Piedra"):
        return "Jugador2"
    elif (j1 == "Papel") and (j2 == "Tijera"):
        return "Jugador2" 
    elif (j1 == "Piedra") and (j2 == "Papel"):
        return "Jugador2"

    return "Empate"

#j1 = "Tijera"
#j2 = "Papel"
#print(quienGana(j1,j2))

# -------------------------- EJERCICIO-2 -------------------------- 

def fibonacciNoRecursivo(n:int)->int:
    listaFibonacci : list = []
    listaFibonacci.append(0)
    listaFibonacci.append(1)

    for i in range(2,n+1):
        anterior = listaFibonacci[i-1] 
        trasAnterior = listaFibonacci[i-2]
        siguiente = anterior + trasAnterior
        listaFibonacci.append(siguiente)
    
    return listaFibonacci[n]

#print(fibonacciNoRecursivo(10))


# 0,1,1,2,3,5,8,13,21,34,55


# FORMA 2
# Hecho por ChatGPT
"""
def fibonacciNoRecursivo(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    
    return fib[-1]

"""

# -------------------------- EJERCICIO-3 -------------------------- 

def mesetaMasLarga(lista:list[int])->int:
    if lista == [] :
        return 0
    if len(lista) == 1:
        return 1

    mesetaGeneral = []
    mesetaParcial = []
    for i in range(len(lista)-1):
        if lista[i] == lista[i+1]:
            mesetaParcial.append(lista[i])
        else:
            mesetaParcial.append(lista[i])
            mesetaGeneral.append(mesetaParcial)
            mesetaParcial = []
    mesetaParcial.append(lista[i+1])
    mesetaGeneral.append(mesetaParcial)
    

    resultado = 0
    for j in range(len(mesetaGeneral)):
        if len(mesetaGeneral[j]) >= resultado:
           resultado = len(mesetaGeneral[j])               
    return resultado   

#print(mesetaMasLarga([5,3]))  # Debería devolver 1
  
#lista = [1,1,1,3,3,3,3,4,5,5,6,7,7,7] # len(lista) = 14
#print(mesetaMasLarga(lista))
# => res = 4

# -------------------------- EJERCICIO-4 -------------------------- 

def filas_parecidas(matriz:list[list[int]])->bool:
    constante =  matriz[1][0] - matriz[0][0] 

    for j in range(len(matriz)): 
          for i in range(len(matriz)):
             if  matriz[j+1][i] - matriz[j][i] != constante :
                  return False

    return True

lista = [[1, 2, 3],[5, 6, 7],[9, 10, 11]]
print(filas_parecidas(lista))






















































