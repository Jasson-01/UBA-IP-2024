def promedio_valido(lista:list[int])->float:

    promedio = 0
    # primero recorro la lista
    nueva_lista = []
    for num in lista:
        if num != 0 :
            if num != 61: 
                nueva_lista.append(num)

    suma_elementos_validos = 0
    if (len(nueva_lista) > 0):   
        for val in nueva_lista:
            suma_elementos_validos += val 
            promedio = suma_elementos_validos / len(nueva_lista) 

    if nueva_lista == []:
        promedio = 0           

    return promedio 

#lista1 = [20,30,50,60,61] 
#lista2 = [61,1,61,30,20]
#print(promedio_valido(lista1))
#print(promedio_valido(lista2))

def copiar_diccionario(diccionario:dict)->dict:
    copia_diccionario = {}
    for key,value in diccionario.items():
        copia_diccionario[key] = value
    
    return copia_diccionario

#diccionario_original = {'a': 1, 'b': 2, 'c': 3}
#diccionario_original = { 'j' : [20,30,50,60,61] , 'm' : [0,0,0,0,0] , 'f' : [61,1,61,30,20] }
#diccionario_copia = copiar_diccionario(diccionario_original)

#print("Diccionario original:", diccionario_original)
#print("Diccionario copia:", diccionario_copia)
    

#registro = { 'j' : [20,30,50,60,61] , 'm' : [0,0,0,0,0] , 'f' : [61,1,61,30,20] }
#print(copia_registro(registro))


def promedio_de_salidas(registro:dict[str,list[int]])->dict[str,tuple[int,float]]:
    copia_registro = copiar_diccionario(registro)
    diccionario_Salida = {}
    
    #Primero formo el diccionario de salida con su tupla correspondiente vacia
    for nombre in copia_registro.keys():
        diccionario_Salida[nombre] = tuple()

    #return diccionario_Salida
    for key,value in copia_registro.items():

        promedio = promedio_valido(value)


        lista_valida = [] 
        for num in value:
            if num != 0 :
                if num != 61: 
                    lista_valida.append(num)

        if lista_valida == []: 
            diccionario_Salida[key] = (0,0.0)



        cantidad_salas_que_logro_salir = len(lista_valida)
      
        diccionario_Salida[key] = (cantidad_salas_que_logro_salir,promedio)
    
    

        
    return diccionario_Salida

#registro = { 'j' : [20,30,50,60,61] , 'm' : [0,0,0,0,0] , 'f' : [61,1,61,30,20] }
#print(promedio_de_salidas(registro))
#res = { 'j' : (4,40) , 'm' : (0,0) , 'f' : (2,25)}


registro1 = {"ana":[30,0,45,61,50],"beto":[20,60,0,61,55],"carlos":[61,61,0,0,61]}
registro2 = {"lucia":[10,20,30,40,50],"mario":[0,0,0,0,0],"pedro":[61,61,61,61,61]}
registro3 = {"juan":[1,2,3,4,5],"elena":[60,60,60,60,60],"sofia":[0,0,0,0,0]}
registro4 = {"luis":[61,0,20,30,0],"beto":[61,0,61,0,61],"carlos":[1,1,1,1,1]}

print(promedio_de_salidas(registro1))
print(promedio_de_salidas(registro2))
print(promedio_de_salidas(registro3))
print(promedio_de_salidas(registro4))



































