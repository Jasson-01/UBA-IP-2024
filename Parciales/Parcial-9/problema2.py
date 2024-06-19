def tiempo_mas_rapido(tiempo_salas:list[int])->int:
    copia_tiempos = tiempo_salas.copy()
    
    # recorro los lementos de la lista
    indice = 0
    minimo = copia_tiempos[0]
    for i in range(len(copia_tiempos)):
        #señalo el minimo como el primero de la lista
        if minimo > copia_tiempos[i]:
           minimo = copia_tiempos[i]
           indice = i
        elif minimo == copia_tiempos[i]:
           minimo = copia_tiempos[i]
           indice = indice     
    return indice       
      
lista_tiempos = [25,30,40,55]
#res = 0

#lista_tiempos = [30,40,10,35,45]
#res = 2

#lista_tiempos = [30,45,55,13,25,13,65]
#res = 3

print(tiempo_mas_rapido(lista_tiempos))




















