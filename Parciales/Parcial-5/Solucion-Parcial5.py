# ------------- PROBLEM - 1 -------------

def verificar_transacciones(lista:str)->int:
    saldo_anterior:int = 0
    saldo_actual:int = 0
#    while saldo_actual >= 0:
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
                return saldo_actual    
    return saldo_actual

#Ejemplo 1:
#s1 = "ssrvvrrvvsvvsxrvvv"
#res = 714
#print(verificar_transacciones(s1))
#Ejemplo 2:
#s2 = "ssrvvvvsvvsvvv"
#res = 14 (en este caso el programa termina porque el saldo no alcanza para realizar un viaje que está entre las transacciones)
#print(verificar_transacciones(s2))
                

# ------------- PROBLEM - 2 -------------



































































