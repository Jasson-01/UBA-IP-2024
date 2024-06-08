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


cotizaciones_diarias = {"YPF" : [(1,10),(15, 3), (31,100)], "ALUA" : [(1,0), (20, 50), (31,30)]}
# resultado_esperado es: {"YPF" : (3,100), "ALUA" : (0,50)}
print(valores_extremos(cotizaciones_diarias))

# ------------- PROBLEM - 4 -------------




































