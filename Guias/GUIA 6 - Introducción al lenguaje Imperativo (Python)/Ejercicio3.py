# -- EJM 1

def alguno_es_0(numero1,numero2):
    resultado = numero1 == 0 or numero2 == 0
    return resultado
print(alguno_es_0(3,0)) 

# -- EJM 2

def ambos_son_cero(numero1,numero2):
    resultado = numero1 == 0 and numero2 == 0
    return resultado
print(ambos_son_cero(0,0))

# -- EJM 3

def es_nombre_largo(nombre:str)-> bool:
    resultado = len(nombre) >= 3 and len(nombre) <= 8 
    return resultado
print(es_nombre_largo("Jason"))  

# -- EJM 4

def es_bisiesto(año:int)->bool:
    resultado = (año % 400 == 0) or (año % 4 == 0 and año % 100 != 0 )
    return resultado
print(es_bisiesto(2041)) 




































































































































