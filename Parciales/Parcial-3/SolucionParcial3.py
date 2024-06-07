# -------- PROBLEM-1 ---------

def mejores_precios(super1:list[(str,int)],super2:list[(str,int)])->list[(str,int)]:
    resultado = []
    
    min = 0
   # contador = 1
    for producto in super1:
           if producto[1] >= (super2[min][1]) :
              resultado.append((producto[min],super2[min][1]))
           else:   
              resultado.append((producto[0],producto[1]))
           min += 1          
    return resultado


#super1 = [("a",3),("b",5)]
#super2 = [("a",1),("b",9)]
#print(mejores_precios(super1,super2))
# res = [("a",1),("b",5)]

#super1_1 = [("leche",151.0),("yerba",4719.5),("jabon",269.2)]
#super2_2 = [("leche",261.2),("yerba",3939.1),("jabon",319.2)]
#print(mejores_precios(super1_1,super2_2))
# res = [("leche",151.0),("yerba",3939.1),("jabon",269.2)]

# -------- PROBLEM-2 ---------

def sinRepetidos(lista:list)->list:
    nueva:list = []
    for i in range(len(lista)):
        if lista[i] not in nueva:
            nueva.append(lista[i])
    return nueva 
#lista = [10,55,60,87,54,98,87,65,55,45,57] 
#print(sinRepetidos(lista))


def seguidilla(calificaciones:list[int],nota_minima:int)->int:
    notas_mayores:list[int] = []
    for i in range(len(calificaciones)):
        if calificaciones[i] > nota_minima :
            notas_mayores.append(calificaciones[i])
             
    if len(sinRepetidos(notas_mayores)) > 0 :
        return len(sinRepetidos(notas_mayores))
    return 0


#calificaciones = [10,55,60,87,54,98,87,65,55,45,57] 
#nota_minima = 60
# [98,87,65]
# res = 3
#print(seguidilla(calificaciones,nota_minima))

#calificacione1 = [10,55,60,65,54,64,65,55,45,57]
#min = 70
#print(seguidilla(calificacione1,min)) 

# -------- PROBLEM-3 ---------

#Hecho por CharGPT:
def elem_en_pos_pares(matriz: list[list[int]], elem: int) -> list[bool]:
    resultado = []
    
    for fila in matriz:
        encontrado = False
        for i in range(0, len(fila), 2):
            if fila[i] == elem:
                encontrado = True
        resultado.append(encontrado)
    
    return resultado


#matris = [[1, 2, 3, 4, 5, 6, 7, 8, 9],[9, 8, 7, 6, 4, 5, 3, 2, 1],[0, 0, 0, 0, 0, 0, 1, 0, 0],[0, 0, 0, 0, 0, 4, 0, 0, 0],[0, 1, 0, 0, 6, 0, 0, 1, 0],]

# matris = [[1, 2, 3, 4, 5, 6, 7, 8, 9],          
#           [9, 8, 7, 6, 4, 5, 3, 2, 1],
#           [0, 0, 0, 0, 0, 0, 1, 0, 0],
#           [0, 0, 0, 0, 0, 4, 0, 0, 0],
#           [0, 1, 0, 0, 6, 0, 0, 1, 0],]

#elem = 1
#print(elem_en_pos_pares(matris,elem)) 
# res = [true,true,true,false,false] 

#elem = 3
#matriz = [
#    [3, 2, 3, 4, 3, 6, 3, 8, 9],
#    [9, 8, 7, 6, 4, 5, 3, 2, 1],
#    [0, 0, 0, 0, 0, 0, 1, 0, 0],
#    [0, 0, 0, 0, 0, 4, 0, 0, 0],
#    [0, 1, 0, 0, 6, 0, 0, 1, 0]
#]
# res = [True, True, False, False, False]
# print(elem_en_pos_pares(matriz, elem)) 


# -------- PROBLEM-4 ---------

def viajes_por_dia(viajes_diarios:dict[int,list[str]],usuarios:list[str])->dict[str,int]:
    resultado:dict = dict()    
    for us in usuarios:
        resultado[us] = 0

    for nombres_por_dia in viajes_diarios.values():
        for us in nombres_por_dia:
             resultado[us] += 1     
    return resultado 


#viaje_diarios = {1:["Juan","Maria"],2:["Marcela","Juan"]}
#usuarios = ["Juan","Maria","Marcela"]
#print(viajes_por_dia(viaje_diarios,usuarios))
#res = {"Juan":2,"Maria":1,"Marcela":1}

#viajes_diarios = {
#    1: ["Alberto", "Beatriz", "Carlos"],
#    2: ["Beatriz", "Alberto", "Carlos"],
#    3: ["Carlos", "Alberto", "Beatriz"],
#    4: ["Carlos", "Beatriz"]
#}
#usuarios = ["Alberto", "Beatriz", "Carlos"]
# Resultado esperado: {"Alberto": 3, "Beatriz": 4, "Carlos": 4}
#print(viajes_por_dia(viajes_diarios, usuarios))

















