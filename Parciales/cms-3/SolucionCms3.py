from queue import LifoQueue as Pila
from queue import Queue as Cola

# -------------------------- Ejercicio-1 (POLACO INVERSO) --------------------------

def mi_split(expresion:str)->list[str]:
    nueva:list[str] = []
    parcial: str = ""
    for i in range(len(expresion)):
        if expresion[i] == " ":   
            nueva.append(parcial)
            parcial = ""
        else:
            parcial += expresion[i]
    
    if len(parcial) > 0 : # para añadir la ultima palabra si no termina en un espacio
        nueva.append(parcial)


    return nueva    
#print(mi_split("2 3.5 -"))


def aplicarOperacion(op,a,b)->int:
    if op == '+' :
        return a+b
    elif op == '-':
        return a-b 
    elif op == '*':
        return a*b
    elif op == '/':
        return a / b


def calcula_expresion(expresion:str)->int:
    pila = []
    expresiones = "*+/-"
    expresionSinEspacios = mi_split(expresion)
    for i in range(len(expresionSinEspacios)):
        if (expresionSinEspacios[i] not in expresiones) and (expresionSinEspacios[i] != " ") :
            pila.append(float(expresionSinEspacios[i]))    
        elif expresionSinEspacios[i] in expresiones:
            op = expresionSinEspacios[i]
            b = pila.pop()
            a = pila.pop()
            resultado = aplicarOperacion(op,a,b) 
            pila.append(resultado)

    return pila[0]

#print(calcula_expresion("2 5 * 7 +"))
#print(calcula_expresion("2 3.5 -"))

# expresion = "2 5 * 7 +" => res = 17.0
# expresion = "2 3.5 -" => res = -1.5

# -------------------------- Ejercicio-2 --------------------------

def unir_diccionarios(unir:list[dict[str,list[str]]])->dict[str,str]:
    resultadoDiccionario = dict()
    listaClavesUnicas = []
    for subDiccionarios in unir:
        claves = subDiccionarios.keys()
        for i in claves :
            if i not in listaClavesUnicas:
                listaClavesUnicas.append(i)
#   return listaClavesUnicas            
    for i in listaClavesUnicas:
        resultadoDiccionario[i] = []

    for j in unir:
        for clave,valor in j.items():

            if clave in listaClavesUnicas :
                resultadoDiccionario[clave].append(valor) 

    return resultadoDiccionario


entrada = [{'a': [1, 2]}, {'a': [3, 4]}, {'a': [5, 6]}]
#esperado = {'a': [1, 2, 3, 4, 5, 6]}  ----------------------------------------------
print(unir_diccionarios(entrada))  # Debe imprimir: True


entrada = [{'a': [1]}, {'b': [2]}, {'a': [3]}, {'c': [4]}, {'b': [5]}, {'a': [6]}, {'d': [7]}]
#esperado = {'a': [1, 3, 6], 'b': [2, 5], 'c': [4], 'd': [7]} -------------------------------------------------
print(unir_diccionarios(entrada))  # Debe imprimir: True



from typing import List, Dict

def unir_diccionarios2(unir: List[Dict[str, List[str]]]) -> Dict[str, List[str]]:
    resultadoDiccionario = {}
    
    for subDiccionario in unir:
        for clave, valores in subDiccionario.items():
            if clave not in resultadoDiccionario:
                resultadoDiccionario[clave] = []
            for valor in valores:
                resultadoDiccionario[clave].append(valor)
    
    return resultadoDiccionario


entrada = [{'a': [1, 2]}, {'a': [3, 4]}, {'a': [5, 6]}]
#esperado = {'a': [1, 2, 3, 4, 5, 6]}  ----------------------------------------------
print(unir_diccionarios2(entrada))  # Debe imprimir: True


entrada = [{'a': [1]}, {'b': [2]}, {'a': [3]}, {'c': [4]}, {'b': [5]}, {'a': [6]}, {'d': [7]}]
#esperado = {'a': [1, 3, 6], 'b': [2, 5], 'c': [4], 'd': [7]} -------------------------------------------------
print(unir_diccionarios2(entrada))  # Debe imprimir: True






























