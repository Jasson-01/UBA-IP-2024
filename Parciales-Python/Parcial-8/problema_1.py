# from queue import LifoQueue as Pila
from queue import Queue as Cola


def copiar_cola(original: Cola) -> Cola:
    res: Cola = Cola()
    cola_tmp: Cola = Cola()
    while not original.empty():
        v = original.get()
        res.put(v)
        cola_tmp.put(v)
    while not cola_tmp.empty():
        x = cola_tmp.get()
        original.put(x)
    return res


def orden_de_atencion(urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
    res: Cola = Cola()
    copia_urgentes = copiar_cola(urgentes)
    copia_postergables = copiar_cola(postergables)

    while not copia_urgentes.empty() or not copia_postergables.empty():
        u = copia_urgentes.get()
        p = copia_postergables.get()
        res.put(u)
        res.put(p)
    return res


urgentes5: Cola = Cola()
postergables5: Cola = Cola()

for u in [1, 3, 5, 7, 9]:
    urgentes5.put(u)

for p in [2, 4, 6, 8, 10]:
    postergables5.put(p)

# Llamar a la función y mostrar el resultado
resultado5 = orden_de_atencion(urgentes5, postergables5)
# Verificar que las colas originales no se modificaron
print("Cola urgentes original:", list(urgentes5.queue))
print("Cola postergables original:", list(postergables5.queue))
print("Cola resultado:", list(resultado5.queue))


######################################## " 2DA FORMA " ##################################################

def orden_de_atencion2(urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
    # Hacer copias de las colas para no modificar las originales
    urgentes_copia = copiar_cola(urgentes)
    postergables_copia = copiar_cola(postergables)

    cola_res = Cola()

    while not urgentes_copia.empty() or not postergables_copia.empty():
        if not urgentes_copia.empty():
            cola_res.put(urgentes_copia.get())
        if not postergables_copia.empty():
            cola_res.put(postergables_copia.get())

    return cola_res


# Crear colas y agregar elementos
urgentes = Cola()
for item in [1, 3, 5, 7, 9]:
    urgentes.put(item)

postergables = Cola()
for item in [2, 4, 6, 8, 10]:
    postergables.put(item)

# Llamar a la función y mostrar el resultado
resultado = orden_de_atencion2(urgentes, postergables)

# Verificar que las colas originales no se modificaron

print("##############################################################################")
print("Cola urgentes original:", list(urgentes.queue))
print("Cola postergables original:", list(postergables.queue))
print("Cola resultado:", list(resultado.queue))

#####################################################################################
