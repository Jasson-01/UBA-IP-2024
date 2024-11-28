# -*- coding: latin-1 -*-

#Ej1
def stock_productos(stock_cambios:list[(str,int)]) -> dict[str, (int,int)]:
    """
    La clave debe ser el nombre del producto.
    El valor debe ser una tupla con dos elementos:
        El menor stock registrado en la pila para ese producto.
        El mayor stock registrado en la pila para ese producto.
    """
    res: dict[str, (int,int)] = dict()
    
    for (producto,cantidad) in stock_cambios:
        if (producto in res):
            cantidad_actual_menor:int = res[producto][0]
            cantidad_actual_mayor:int = res[producto][1]
            if cantidad < cantidad_actual_menor:
                res[producto] = (cantidad, cantidad_actual_mayor)
            elif cantidad > cantidad_actual_mayor:
                res[producto] = (cantidad_actual_menor, cantidad)
        else:
            res[producto] = (cantidad,cantidad)
    
    return res

def stock_productos_version_2(stock_cambios: list[tuple[str, int]]) -> dict[str, tuple[int,int]]:
    res: dict[str, tuple[int, int]] = dict()

    for (producto, cantidad) in stock_cambios:
        if producto not in res.keys():
            res[producto] = (cantidad, cantidad)
        elif res[producto][0] > cantidad:                   #si hay nuevo mínimo
            res[producto] = (cantidad, res[producto][1])    #actualizo el mínimo y conservo el máximo
        elif res[producto][1] < cantidad:                   #si hay nuevo máximo
            res[producto] = (res[producto][0], cantidad)    #actualizo el máximo y conservo el mínimo

    return res
#Ej2

def filtrar_codigos_primos(codigos_de_barras: list[int]) -> list[int]:
    res:list[int] = []
    for codigo in codigos_de_barras:
        if(es_codigo_primo(codigo)):
            res.append(codigo)
    return res
    
def es_codigo_primo(numero:int) -> bool:
    ultimos_tres:int = numero % 1000
    return es_primo(ultimos_tres)

    #otra alternativa:
    #ultimos_tres = str(numero)[-3:]
    #return es_primo(int(ultimos_tres))
    
def es_primo(numero:int) -> bool:
    if (numero < 2):
        return False
        
    resultado:bool = True
    for i in range(2, numero):
        if (numero % i) == 0:
            resultado = False
    return resultado
    

# Ej3
def subsecuencia_mas_larga(mascotas: list[str]) -> int:
    cant_animal_mayor:int = 0
    cant_animal_actual:int = 0
    posicion_inicial_actual:int = -1
    posicion_inicial_mas_larga:int = -1
    
    for pos_animal in range(len(mascotas)):
        animal: str = mascotas[pos_animal]
        if (animal == "perro" or animal == "gato"):
            if cant_animal_actual == 0:                 # si arranca una nueva subsecuencia
                posicion_inicial_actual = pos_animal    # guardo la posición inicial  
            cant_animal_actual += 1
        else:
            # si no es perro o gato, reset y veo actualizo maximos
            if (cant_animal_actual > cant_animal_mayor):
                cant_animal_mayor = cant_animal_actual
                posicion_inicial_mas_larga = posicion_inicial_actual

            cant_animal_actual = 0
            posicion_inicial_actual = -1
            
        if (cant_animal_actual > cant_animal_mayor):
            posicion_inicial_mas_larga = posicion_inicial_actual
    return posicion_inicial_mas_larga
            
def subsecuencia_mas_larga_version_2(tipos_pacientes_atendidos: list[int]) -> int:
    res:int = 0
    largo_max:int = 0
    largo_actual:int = 0
    indice:int = 0
    for t in tipos_pacientes_atendidos:
        
        if t == "perro" or t == "gato":
            largo_actual +=1
        else:
            if largo_max < largo_actual:
                res = indice - largo_actual                
                largo_max = largo_actual
            largo_actual = 0
        indice +=1

    if largo_max < largo_actual:
        res = indice - largo_actual                

    return res
#Ej4

def un_responsable_por_turno(grilla_horaria:list[list[str]]) -> list[(bool,bool)]:
    resultado: list[(bool,bool)] = []
    for dia in range(len(grilla_horaria[0])):#todas las filas tienen = tam y |grilla_horaria| es mayor a 0
        (personas_manana, personas_tarde) = personas_en_turnos_del_dia(grilla_horaria, dia)
        iguales_por_turno = (son_iguales(personas_manana),son_iguales(personas_tarde))
        resultado.append(iguales_por_turno)
    return resultado
    
def son_iguales(una_lista:list) -> bool:
    """
    Asume que una_lista no es vacia
    """
    actual=una_lista[0]
    resultado = True
    for elem in una_lista:
        if(elem != actual):
            resultado = False
    return resultado
    
    
def personas_en_turnos_del_dia(grilla_horaria:list[list[str]], dia:int) -> (list[str],list[str]):
    personas_del_dia = []
    for personas_en_horario in grilla_horaria:
        personas_del_dia.append(personas_en_horario[dia])
    
    personas_tarde = personas_del_dia[4:]
    personas_manana = personas_del_dia[:4]
    
    return (personas_manana, personas_tarde)

#dada una matriz, devuelve una tupla con una lista de los 4 primeros horarios y otra con los otros 4 
def personas_en_turnos_del_dia_version_2(grilla_horaria:list[list[str]], dia:int) -> (list[str],list[str]):
    TM = []
    TT = []
    
    for i in range(4):
        TM.append(grilla_horaria[i][dia])
    for i in range(4, 8):
        TT.append(grilla_horaria[i][dia])
              
    return (TM, TT)

#otra solución:
def un_solo_responsable(t1: str, t2: str, t3: str, t4: str) -> bool:
    return t1 == t2 and t2 == t3 and t3 == t4

def un_responsable_por_turno_version_2(grilla_horaria: list[list[str]]) -> list[tuple[bool,bool]]:
    res: list[tuple[bool, bool]] = []

    for dia in range(len(grilla_horaria[0])):
        primer_turno: bool = un_solo_responsable(
            grilla_horaria[0][dia],
            grilla_horaria[1][dia],
            grilla_horaria[2][dia],
            grilla_horaria[3][dia]
        ) 
        segundo_turno: bool = un_solo_responsable(
            grilla_horaria[4][dia],
            grilla_horaria[5][dia],
            grilla_horaria[6][dia],
            grilla_horaria[7][dia]
        )

        res.append((primer_turno, segundo_turno))

    return res