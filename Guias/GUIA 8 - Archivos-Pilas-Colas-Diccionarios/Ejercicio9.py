from queue import LifoQueue as Pila

def cantidad_elementos(pila : Pila) -> int:
    #la pila no esta vacia
    pilaSecundaria:Pila = Pila()
    contador = 0
    
    #Esto trata de contar cada elemento que pasa
    while (pila.empty() == False):
        tope = pila.get()
        contador += 1
        pilaSecundaria.put(tope)
    
    #Esto reconstruye la pila original
    while (not pilaSecundaria.empty()):
        pila.put(pilaSecundaria.get())

    print(pila)
    return contador

pila = Pila()
pila.put(1)
pila.put(2)
pila.put(3)
pila.put(4)

print(cantidad_elementos(pila))
