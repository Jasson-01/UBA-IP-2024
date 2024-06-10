from queue import Queue as Cola

def cantidad_elementos(muchosElementos: Cola) -> int:
    cola = Cola()
    contador = 0
    
    while not muchosElementos.empty():
        i = muchosElementos.get()
        cola.put(i)
        contador += 1 

    # Reconstruyendo la cola original
    while not cola.empty():
        muchosElementos.put(cola.get())
    
    return contador

# Inicializa la cola correctamente
#listaCola = Cola()
#for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#    listaCola.put(i)

#print(cantidad_elementos(listaCola))

"""
def cantidad_elementos(muchosElementos:Cola)->int:
    cola = Cola()
    contador:int = 0
    for i in muchosElementos:
        cola.put(i)
        contador += 1 

    #reconstruyendo la pila original
    if (not cola.empty()):
       muchosElementos.put(cola.get())
    
    print(muchosElementos)
    return contador

listaCola = [1,2,3,4,5,6,7,8,9]
print(cantidad_elementos(listaCola))

"""

