from queue import Queue as Cola
import random

def generar_numeros_al_azar(cantidad:int,desde:int,hasta:int)->Cola[int]:
    cola = Cola()
    for _ in range(cantidad):
        x = random.randint(desde,hasta)
        cola.put(x)
    return cola     

print(generar_numeros_al_azar(5,10,20).queue)














