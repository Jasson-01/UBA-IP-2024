#--A)

def peso_pino(longitudPino:int) -> int:
    if longitudPino > 3 :
        sobra:int = longitudPino - 3
        resultado1 = (sobra * (2*100)) + 900
        return resultado1   
    else:
         resultado2:int = (longitudPino*100) * 3
         return resultado2

print(peso_pino(2))
#print(peso_pino(3))
#print(peso_pino(4))
#print(peso_pino(5))

#--B)

def es_peso_util(peso:int)-> bool:
    if peso >= 400 and peso <= 1000:
        return True
    return False

print(es_peso_util(1009))

#--C)

def sirve_pino(altura:int)->bool:
    if altura < 4:
       return True
    return False























































