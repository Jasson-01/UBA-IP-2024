from queue import LifoQueue as Pila

def mi_split(oracion:str)->list[str]:
    lista:list[str] = []
    nueva:str = ""
    for i in range(len(oracion)):
        if oracion[i] == " ":
           lista.append(nueva)
           nueva = ""
        else:
            nueva += oracion[i] 

    else:
        lista.append(nueva)

    return lista
#oracion = "-hola como estas+"           
#print(mi_split(oracion))

def ejecutando_operacion(op,a,b)->int:
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        return a / b 

def evaluar_expresion(expresion:str)->float:
    resultado:Pila = []
    operaciones = "+-/*"
    for token in mi_split(expresion):
        if token in operaciones:
            a = resultado.pop()
            b = resultado.pop()
            op = token
            resultado.append(ejecutando_operacion(op,b,a))

        else:
            resultado.append(float(token))
    return resultado[0]

#expresion = "3 4 + 5 * 2 -"
#print(evaluar_expresion(expresion))
# deveria devolver res = 33













