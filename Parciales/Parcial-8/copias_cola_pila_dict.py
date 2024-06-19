from queue import LifoQueue as Pila
from queue import Queue as Cola

# ------------------------- COLA ------------------------


def copiar_cola(original: Cola) -> Cola:
    res: Cola = Cola()
    copia_temp: Cola = Cola()
    while not original.empty():
        v = original.get()
        res.put(v)
        copia_temp.put(v)
    while not copia_temp.empty():
        x = copia_temp.get()
        original.put(x)
    return res


original = Cola()
for item in [2, 3, 4, 5, 6, 7]:
    original.put(item)

# Copiar la cola original
copia1 = copiar_cola(original)

# Mostrar los elementos de la Cola original y la copia
print("original_COLA:", original.queue)
print("copia:", list(copia1.queue))

# -------------------------- PILA ------------------------


def copiar_pila(original2: Pila) -> Pila:
    res: Pila = Pila()
    pila_tmp = Pila()
    pila_tmp_2 = Pila()
    while not original2.empty():
        v = original2.get()
        res.put(v)
        pila_tmp.put(v)
    # Reconstruyendo la Pila original
    while not pila_tmp.empty():
        x = pila_tmp.get()
        pila_tmp_2.put(x)
    while not pila_tmp_2.empty():
        original2.put(pila_tmp_2.get())
    return res


original2 = Pila()
for i in [1, 2, 3, 4]:
    original2.put(i)

# Copiar la pila original2
copia = copiar_pila(original2)

# Mostrar los elementos de la pila original2 y la copia
print("Original2_PILA:", list(original2.queue))
print("Copia_pila:", list(copia.queue))

# -------------------------- DICCIONARIOS ------------------------


def copiar_diccionario(original3: dict) -> dict:
    copia = {}
    for key, value in original3.items():
        copia[key] = value
    return copia


diccionario_original = {'a': 1, 'b': 2, 'c': 3}
diccionario_copia = copiar_diccionario(diccionario_original)

print("Diccionario original:", diccionario_original)
print("Diccionario copia:", diccionario_copia)
