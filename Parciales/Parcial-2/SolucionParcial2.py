# ------- PROBLEM-1 --------

def acomodar(lista:list[str])->list[str]:
    primeraParte:list = []
    segundaParte:list = []
    for i in range(len(lista)):
        if lista[i] == "UP":
           primeraParte.append(lista[i])
        else:
            segundaParte.append(lista[i])      
    return primeraParte + segundaParte

#s = ["LLA","UP","LLA","LLA","UP"]
#print(acomodar(s))

# ------- PROBLEM-2 --------

def pos_umbral(lista:list[int],umbral:int)->int:
    suma = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            suma += lista[i]
        if suma > umbral:
            return i 
    return -1

#s = [1,-2,0,5,-7,3]
#u = 5
#print(pos_umbral(s,u))         

#print(pos_umbral([2, -1, 3, -5, 2, 1], 4)) # = 2, esperado 2
#print(pos_umbral([-1, -2, -3, -4, -5], 1)) # = -1, esperado -1
#print(pos_umbral([1, 2, 3, 4, 5], 15))  # = -1, esperado -1
#print(pos_umbral([10, -10, 5, -5, 20, -20], 15)) # = 4, esperado 4
#print(pos_umbral([1, 1, 1, 1, 1], 3)) # = 3, esperado 3

# ------- PROBLEM-3 --------

def columnas_repetidas(matriz:list[list[int]])->bool:
    #Esto me da el numero de columnas
    num_columnas = len(matriz[0])
    
    #Divido el numero de columnas a la mitad
    mitad = int(num_columnas / 2)
    

    for fila in matriz:
        for pos_col in range(mitad):
             if fila[pos_col] != fila[mitad+pos_col]:
                 return False
    return True         

#matriz = [[1,2,1,2],[-5,6,-5,6],[0,1,0,1]]
#print(columnas_repetidas(matriz))

# ------- PROBLEM-4 --------

def cuenta_posiciones_por_nacion(naciones:list[str],torneos:dict[str,list[str]])->dict[str:list[int]]:
    resultado = {}
    #Con esto voy agregando los paises con sus posiciones, inicializadas en cero
    for pais in naciones:
        resultado[pais] = len(naciones)*[0]
    
    for fila in torneos.values():
        posicion = 0
        for pais in fila :
            resultado[pais][posicion] += 1
            posicion += 1  
    return resultado


naciones= ["arg", "aus", "nz", "sud"]
torneos= {2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"]}
print(cuenta_posiciones_por_nacion(naciones,torneos))
#res = {"arg": [0,0,1,1], "aus": [0,0,1,1], "nz": [2,0,0,0],"sud": [0,2,0,0]}









































