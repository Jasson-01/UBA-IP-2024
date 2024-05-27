import math
# ------------------- CLASE ------------------------

def perimetro() -> float:
    return round(2*math.pi,4)

print(perimetro())
#--------------------------------------------------------------------------------------

def es_multiplo_de(n:int,m:int)-> bool:
    return (n%m == 0)
print(es_multiplo_de(7,4))
#--------------------------------------------------------------------------------------

def es_nombre_largo(n:str) -> bool:
    return (len(n)<=8 and len(n) >=3)
print(es_nombre_largo("juan"))
#--------------------------------------------------------------------------------------

def devolver_el_doble_si_es_par(n:int)->int:
    if (n%2 == 0):
        return n*2;
    else: 
        return n;
    
print(devolver_el_doble_si_es_par(3))


#2DA FORMA:
def devolver_el_doble_si_es_par2(n:int)->int:
    if (n%2 == 0):
        res = n*2;
    else: 
        res = n;
    return res
    
print(devolver_el_doble_si_es_par2(3))



#--------------------------------------------------------------------------------------

def imprimir_pares_entre_10_y_40():
    n:int= 10
    while (n <= 40):
        if n%2 == 0:
           print(n)
        n = n+1
           
       
print(imprimir_pares_entre_10_y_40()) 




#def imprimir_pares_entre_10_y_40():
#    n:int= 10
#    m = 0
#    while (n <= 40):
#        m=(n + 2)
#        print(m)
#    return n     
#print(imprimir_pares_entre_10_y_40()) 

def cuenta_regresiva(n:int): 
    while n >= 1:
        if n >= 1:
            print(n)
        n = n-1
    print("Despegue!!!")
(cuenta_regresiva(5))

