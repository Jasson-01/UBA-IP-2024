import random
from queue import LifoQueue as Pila

# --- EJM 1 ---

def generar_nros_al_azar(cantidad:int,desde:int,hasta:int)->Pila[int]:
    p = Pila()
    while cantidad > 0: 
        p.put(random.randint(desde,hasta))
        cantidad -= 1 
    return p  

#print(generar_nros_al_azar(5,10,20).queue)

# ---EJM 2 ---
"""

def buscar_el_maximo(p:Pila[int]):
    for i in range(len(p)):
        if (p[i] >= p[i+1]) or (i == len(p)-1):     #NO SE PUEDE HACER ESTO NO ES UNA LISTA !!!
            p.get(p[i+1])
    return p 

pila = [1,2,3,4]
#print(buscar_el_maximo(pila).queue)

def buscar_el_maximo2(p:Pila[int])->int:
    indice = 0
    while (p.empty() == True) :
        p.get(indice) >= p.get(indice+1)      #NO SE PUEDE HACER ESTO NO ES UNA LISTA !!!
        p.get()
        indice += 1
    return p.get()

#print(buscar_el_maximo2([1,2,3,4,5]).queue)

"""
# Version Profe
# Rompiendo la Pila
def buscar_el_maximo3(p:Pila[int])->int:
   # requiere Pila no vacia      
   maximo:int= p.get()
   while (p.empty() == False):
       tope = p.get()
       if (tope > maximo):
            maximo = tope
   return maximo 


pila = Pila()
pila.put(1)
pila.put(2)
pila.put(3)

print(buscar_el_maximo3(pila))         
























