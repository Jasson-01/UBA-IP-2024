import math 

# -- EJM 1 --

def imprimir_saludo(nombre:str):
    print("Hola", nombre)
imprimir_saludo("Jason!")

# -- EJM 2 --

def raiz_cuadrada_de(numero:int):
    x = numero**0.5
    print(x)
raiz_cuadrada_de(9)

# -- EJM 3 --

def fahrenheit_a_celsius(temp_far:float):
    x = round(((temp_far-32)*5) / 9,4)
    print(x)
fahrenheit_a_celsius(100)

# -- EJM 4 --

def imprimir_dos_veces(estribillo:str):
    x = 2*estribillo
    print(x)
imprimir_dos_veces("estribillo ")

# -- EJM 5 --

def es_multiplo_de(n:int,m:int)->bool:
    return (n%m == 0)
print(es_multiplo_de(49,7))

# -- EJM 6 --

def es_par(numero:int):
    return (es_multiplo_de(numero,2))
print(es_par(9))

# -- EJM 7 --

"""
/ -> division de punto flotante
// -> division entera (redondea hacia abajo)
% -> calcula el resto 
"""

def cantidad_de_pizzas(comensales,min_cant_de_porciones)->int:
    porciones_totales:int = comensales*min_cant_de_porciones                    
    pizzas_necesarias:float = porciones_totales / 8                              

    if (pizzas_necesarias % 1 == 0): # --Verifica si la div es entera, si es decimal pasa al "else"
        if es_multiplo_de(porciones_totales,8):
           return ((porciones_totales // 8) + 1) #(8,8)
#        else: 
#           return (pizzas_necesarias) 
    else:
        return ((porciones_totales // 8)+1)  # (5,2)

print(cantidad_de_pizzas(5,2))

















































