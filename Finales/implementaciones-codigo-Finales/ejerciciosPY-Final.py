

def hayRepetidos(f:list[int])->bool:
    nueva_lista = []
    for i in range(len(f)):
        if not(pertenece(f[i],nueva_lista)) or (f[i] == 0) :
            nueva_lista.append(f[i])
        else:
            return True
    return False

def pertenece(elem:int,lista:list[int])->bool:    
    for e in lista:
        if e == elem:
            return True
    return False

def matriz_transpuesta(m:list[list[int]])->bool:
    nueva_lista = []
    for i in range(len(m[0])):
        nueva_lista.append([])
    
    for fila in m:
        for c in range(len(fila)):
            nueva_lista[c].append(fila[c])
    return nueva_lista 

def hayFilasRepetidas(m:list[list[int]])->bool:
    for fila in m:
        if hayRepetidos(fila):
            return True 
        
    return False

def hayColumnasRepetidas(m:list[list[int]])->bool:
    if hayFilasRepetidas(matriz_transpuesta(m)):
        return True
    else:
        return False       

def esSudokuValido(m:list[list[int]]) -> bool:
     if not(hayFilasRepetidas(m)) and not(hayColumnasRepetidas(m)):
        return True
     else: 
        return False 
        

# sudoku1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],[9, 8, 7, 6, 4, 5, 3, 2, 1],[0, 0, 0, 0, 0, 0, 1, 0, 0],[0, 0, 0, 0, 0, 4, 0, 0, 0],[0, 0, 0, 0, 6, 0, 0, 0, 0],[0, 0, 0, 5, 0, 0, 0, 0, 0],[0, 0, 4, 0, 0, 0, 0, 0, 0],[0, 3, 0, 0, 0, 0, 0, 0, 0],[2, 0, 1, 0, 0, 0, 0, 0, 1]]

# # sudoku2 = [[1, 8, 9],[9, 2, 1],[ 1, 0, 1]]

# op = esSudokuValido(sudoku1)
# print(op)


# ----  Final 25 de Julio ...........................................................................................


def maximo(s:list[int])->int:
    max = s[0]
    for elem in s:
        if elem >= max:
            max = elem 
    return max

def subsecuencia(e:int,s2:list[int])->list[int]:
    nueva_lista = []
    if e > len(s2):
        return s2
    for i in range(e+1):
        nueva_lista.append(s2[i])
    return nueva_lista    

def intercambiandoPorElMayor(s1:list[int],s2:list[int]):
    posiciones:list[int] = s1.copy()
    for i in range(len(s1)):
        s1[i] = maximo(subsecuencia(posiciones[i],s2))
    print(s1)


# s1 = [3,2,3,5,1]
# s2 = [-1,2,3,1,5,4,3]
# s3 = [1,1,2,3,4]
# s4 = [1,2,3,4,5]
# s5 = [4,3,2,1,7]
# s6 = [1,2,3,4,5]

# op = intercambiandoPorElMayor(s5,s6) 
# print(op)

# ----  Final 1 de Agosto ...........................................................................................

def pertenece(e:int,l:list[int])->bool:
    for elem in l:
        if e == elem :
           return True
    return False

def sinRepetidos(l:list[int])->list[int]:
    nueva_lista:list[int] = []
    for i in range(len(l)):
        if not(pertenece(l[i],nueva_lista)):
            nueva_lista.append(l[i])
    return nueva_lista   

def es_primo(e:int) -> bool:
    if e < 2:
        return False
    listaDivisores = []
    contador = e
    for i in range(1,e+1):
        if e % i == 0 :
           listaDivisores.append(i)
    if len(listaDivisores) > 2:
        return False 
    else:
        return True

def primos(l:list[int])->list[int]:
    lista_primos = []
    for e in l :
        if es_primo(e) :
            lista_primos.append(e) 
    return lista_primos

def cantidadRepeticiones(e:int,l:list[int])->int:
    contador = 0
    for elem in l :
        if e == elem :
            contador += 1 
    return contador         

def mayorPrimoRepetido(l:list[int])->int:
    listaTuplas: list[tuple[int,int]] = []
    listaDePrimos: list[int] = sinRepetidos(primos(l))

    for e in listaDePrimos:
        listaTuplas.append((e,cantidadRepeticiones(e,l)))

    actual_mayor = listaTuplas[0]
    for i in range(len(listaTuplas)):
        if listaTuplas[i][1] >= actual_mayor[1] :
            actual_mayor = listaTuplas[i]
    return actual_mayor[0]         

l = [2,2,3,8,3,8,4,3,7,7,9,1,1,1,1,1,2,2,2]
l1 =[3,7,7,2]

op = mayorPrimoRepetido(l1)
print(op)



















