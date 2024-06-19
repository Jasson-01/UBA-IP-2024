from queue import Queue as Cola


def buscar_el_maximo(colaLista:Cola[int])->int:
    
    num_actual = 0
    while not colaLista.empty():
          num = colaLista.get()
          if num_actual <= num :
               num_actual = num 
    
    return num_actual


# Ejemplos de prueba
cola = Cola()
for elem in [3, 1, 4, 1, 5, 9, 2, 6, 50]:
    cola.put(elem)
print(buscar_el_maximo(cola))

"""
def buscarElMaximo(c:Cola[int])->int:
    max = c.get()
    while not c.empty():
         e = c.get()
         if e > max :
              max = e 
    return max 

# Ejemplos de prueba
cola = Cola()
for elem in [3, 1, 4, 1, 5, 9, 2, 6, 5]:
    cola.put(elem)

print(buscarElMaximo(cola))
# Salida esperada: 9
"""

















