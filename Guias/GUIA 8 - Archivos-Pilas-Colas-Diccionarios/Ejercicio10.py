from queue import LifoQueue as Pila


def buscar_el_maximo(pila : Pila[int]) -> int:
    pilaSecundaria = Pila()
    maximo = pila.get()
    pilaSecundaria.put(maximo)

    while (pila.empty() == False):
        tope = pila.get()
        pilaSecundaria.put(tope)

        if tope > maximo:
            maximo = tope
    
    while (not pilaSecundaria.empty()):
          pila.put(pilaSecundaria.get())
    
    return maximo 


pila = Pila()
pila.put(1)
pila.put(2)
pila.put(9)

print(buscar_el_maximo(pila))   

















