
def racha_mas_larga(tiempos:list[int])->tuple[int,int]:
    #Primero formo una copia de la lista original para trabajar con ella 
    copia_tiempos = tiempos.copy()
    
    comienza_indice = 0
    termina_indice = 0
    lista_subsecuencias = [] 
    subsecuencia = []
    
   
    
    
    #Recorro la copia
    for indice in range(len(copia_tiempos)):
        for num in copia_tiempos:
             if copia_tiempos[0] != 0 or copia_tiempos[0] != 61:
                  comienza_indice = 0
            
             elif copia_tiempos[i] != 0 or copia_tiempos[i] != 61 :
                  comienza_indice = i
                  subsecuencia.append(copia_tiempos[i])         
        termina_indice = i
        
           
    lista_subsecuencias.append((comienza_indice,termina_indice),subsecuencia) 



tiempos = [1,22,0,4,3,7,61,20,30,40,50,60,0,14,15]
print(racha_mas_larga(tiempos))
#res = (7,11)

















