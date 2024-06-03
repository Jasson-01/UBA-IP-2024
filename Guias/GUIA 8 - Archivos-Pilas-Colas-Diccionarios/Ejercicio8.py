import random
from queue import LifoQueue as Pila

def generar_nros_al_azar(cantidad : int,desde : int,hasta : int) -> Pila[int]:
    numeros = Pila()
    while cantidad > 0:
        numeros.put(random.randint(desde,hasta))
        cantidad -= 1
    return numeros

print(generar_nros_al_azar(5,10,20).queue)

        