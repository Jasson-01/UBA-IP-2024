
# ----- PROBLEM-2 -------

def mezclar(s1:list[int],s2:list[int])->list[int]:
    nuevo:list = []
    indice = 0
    contador = 0
    while contador < len(s1) :
       nuevo.append(s1[indice])
       nuevo.append(s2[indice])
       indice += 1
       contador += 1
    return nuevo 

#s1 = [0,0,0]
#s2 = [1,2,3]
#s3 = [1,3,0,1]
#s4 = [4,0,2,3]
#print(mezclar(s3,s4))

# ----- PROBLEM-3 -------

#def frecuencia_posiciones_por_caballo():


# ----- PROBLEM-4 -------

def matriz_capicua(matriz:list[list[int]])->bool:
    for fila in matriz:
        for i in range(len(fila)):
            if fila[i] != fila[-i-1]:
                return False
    return True
   
m = [[1,2,2,1],[-5,6,6,-5],[0,1,1,0]]
print(matriz_capicua(m))





















