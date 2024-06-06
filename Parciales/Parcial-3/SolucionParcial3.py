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

#def seguidilla(calificaciones:list[int],nota_minima:int)->int:


















