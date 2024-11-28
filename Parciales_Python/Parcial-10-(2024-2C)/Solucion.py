# --- Ejercicio 1 ---------------------------------------------------------------------------------------------------

def pertenece(elem,lista)->bool:
    for elem2 in lista:
        if elem == elem2:
            return True
    return False

def cant_stock(name:str,stock:list[tuple[str,int]])->list[int]:
    nueva_lista = []
    for i in range(len(stock)):
        if stock[i][0] == name:
           nueva_lista.append(stock[i][1])
    return nueva_lista

def maximo_lista_producto(lista:list[int])->int:
    maximo = lista[0]
    for i in range(len(lista)):
        if lista[i] > maximo :
            maximo = lista[i]
    return maximo 
# print(maximo_lista_producto([3, 30, 0]))     

def minimo_lista_producto(lista:list[int])->int:
    minimo = lista[0]
    for i in range(len(lista)):
        if lista[i] < minimo :
            minimo = lista[i]
    return minimo
# print(minimo_lista_producto([5, 4, 6]))
# print(minimo_lista_producto([3, 30, 0]))     


def stock_productos(stock_cambios:list[tuple[str,int]])->dict[str,tuple[int,int]]:
    diccionario_res:dict = {}

    productos_unicos = []
    productos = []

    for i in range(len(stock_cambios)):
        productos.append(stock_cambios[i][0]) 

    for i in range(len(productos)):
        if not(pertenece(productos[i],productos_unicos)):
            productos_unicos.append(productos[i])
    # print(productos_unicos) --

    for i in range(len(productos_unicos)):
        if not(pertenece(productos_unicos[i],diccionario_res.keys())):
            diccionario_res[productos_unicos[i]] = (minimo_lista_producto(cant_stock(productos_unicos[i],stock_cambios)),maximo_lista_producto(cant_stock(productos_unicos[i],stock_cambios)))
    # print(stock_cambios)
    return diccionario_res

# --- Ejercicio 2 ---------------------------------------------------------------------------------------------------

def es_primo(numero:int)->bool:
    contador = 1
    divisores_numero = []
    while contador <= numero:
        if numero % contador == 0:
            divisores_numero.append(contador)
        contador += 1    
    # print(divisores_numero)
    if len(divisores_numero) > 2:
        return False 
    return True

def filtrar_codigos_primos(codigos_barra:list[int])->list[int]:
    nueva_lista = []
    for num in codigos_barra:
        ultimos_tres = num % 1000
        if es_primo(ultimos_tres):
            nueva_lista.append(num)
    return nueva_lista

# --- Ejercicio 3 ---------------------------------------------------------------------------------------------------

def subsecuencia_mas_larga(tipos_pacientes_atendidos:list[str]):
    longitud = 0
    lista_subsecuencias_con_indice = [] 
    sub_secuencia:tuple[int,list[int]] = ()
    for i in range(len(tipos_pacientes_atendidos)):
      if len(sub_secuencia) == 0:   
         if tipos_pacientes_atendidos[i] == "perro" or tipos_pacientes_atendidos[i] == "gato":
            sub_secuencia = ((i,[tipos_pacientes_atendidos[i]]))

      elif (tipos_pacientes_atendidos[i] == "perro" or tipos_pacientes_atendidos[i] == "gato"):
          sub_secuencia[1].append(tipos_pacientes_atendidos[i])

      elif (tipos_pacientes_atendidos[i] != "perro" or tipos_pacientes_atendidos[i] != "gato"):            
          lista_subsecuencias_con_indice.append(sub_secuencia)    
          sub_secuencia = ()
    if sub_secuencia != () :
       lista_subsecuencias_con_indice.append(sub_secuencia) 
    print(lista_subsecuencias_con_indice)

    indice = lista_subsecuencias_con_indice[0][0]
    longitud_prima = len(lista_subsecuencias_con_indice[0][1])
    for e in range(len(lista_subsecuencias_con_indice)):
        if len(lista_subsecuencias_con_indice[e][1]) > longitud_prima:
             longitud_prima = len(lista_subsecuencias_con_indice[e][1])
             longitud = lista_subsecuencias_con_indice[e][0] 
             indice = lista_subsecuencias_con_indice[e][0]
        else:
            longitud = indice
    return longitud

# --- Ejercicio 4 ---------------------------------------------------------------------------------------------------

def matriz_transpuesta(matriz:list[list[str]])->list[list[str]]:
    nueva_matriz = []
    for i in range(len(matriz[0])):
        nueva_matriz.append([])

    for fila in matriz:
        for c in range(len(fila)):
           nueva_matriz[c].append(fila[c])
    return nueva_matriz        

def un_responsable_por_turno(grilla_horaria:list[list[str]])->list[tuple[bool,bool]]:
    matriz_transpuesta02 = matriz_transpuesta(grilla_horaria)
    nueva_lista = []
    primero=True
    segundo=True
    for column in matriz_transpuesta02:
        for i in range(len(column)//2):
            original = column[0]
            if column[i] != original:
                   primero = False 
        for e in range(len(column)//2,len(column)-1):
            if column[e] != column[e+1]: 
                   segundo = False
        nueva_lista.append((primero,segundo))
        primero = True
        segundo = True

    return nueva_lista
