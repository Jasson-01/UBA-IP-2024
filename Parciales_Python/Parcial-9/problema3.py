def racha_mas_larga(tiempos: list[int]) -> tuple[int, int]:

    # 1era parte
    copia_tiempos = tiempos.copy()
    comienza_indice = 0
    lista_subsecuencias = []
    subsecuencia = []
    indice_actual = 0

    # Recorro la copia
    while indice_actual < len(copia_tiempos):
        tiempo = copia_tiempos[indice_actual]

        if tiempo != 0 and tiempo != 61:
            if len(subsecuencia) == 0:
                comienza_indice = indice_actual
            subsecuencia.append(tiempo)
        else:
            if len(subsecuencia) > 0:
                lista_subsecuencias.append(
                    ((comienza_indice, indice_actual - 1), subsecuencia))
                subsecuencia = []

        indice_actual += 1

    if len(subsecuencia) > 0:
        lista_subsecuencias.append(
            ((comienza_indice, indice_actual - 1), subsecuencia))

#    return lista_subsecuencias

    # 2DA parte
    # Ahora busco la longitud de la subsecuencia mas grande
    tupla_res = (0, 0)
   # maximo = []
    longitud_maxima = 0
    for (indices, subsecuencias) in lista_subsecuencias:
        if longitud_maxima <= len(subsecuencias):
            #   maximo = lista_subsecuencias[i][1]
            longitud_maxima = len(subsecuencias)
            tupla_res = indices
    return tupla_res

# tiempos1 = [1, 22, 0, 4, 3, 7, 61, 20, 30, 40, 50, 60, 0, 14, 15]
# tiempos2 = [2, 3, 0, 61, 8, 9, 10]
# print(racha_mas_larga(tiempos2))
# print(racha_mas_larga(tiempos1))


""" No pasa los test que hice (Primera parte)
def racha_mas_larga(tiempos:list[int])->list:
    #Primero formo una copia de la lista original para trabajar con ella 
    copia_tiempos = tiempos.copy()
    
    comienza_indice = 0
    termina_indice = 0
    lista_subsecuencias = [] 
    subsecuencia = []
    indice_manual = -1
   # indice_anterior = indice_manual - 1 
      
    #Recorro la copia    
    for tiempo in copia_tiempos:
        if tiempo != 0 and tiempo != 61 : 
          if len(lista_subsecuencias) == 0 :             
            comienza_indice = 0
          subsecuencia.append(tiempo)
        elif len(subsecuencia) > 0 :
            termina_indice = indice_manual    
            lista_subsecuencias.append(((comienza_indice,termina_indice),subsecuencia)) 
            subsecuencia = []
            indice_actual = indice_manual + 1   
            comienza_indice = indice_actual + 1         
        indice_manual += 1
    if len(subsecuencia) > 0 :
        termina_indice = indice_manual
        lista_subsecuencias.append(((comienza_indice,termina_indice),subsecuencia))    
      
        
    return lista_subsecuencias        
        
           
tiempos2 = [2,3,0,61,8,9,10]
print(racha_mas_larga(tiempos2))
"""
# res = [((0,1),[2,3]),((4,6),[8,9,10])]
# tiempos = [1,22,0,4,3,7,61,20,30,40,50,60,0,14,15]
