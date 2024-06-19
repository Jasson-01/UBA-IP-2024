def promedio(notas:list)->int:
    suma:int = 0
    for nota in notas:
        suma += nota 
    return (suma / len(notas)) 
#print(promedio([1,2,3,4]))

def algunoMenorACuatro(notas:list)->bool:
    for i in notas:
        if i < 4:
           return True
    return False
#print(algunoMenorACuatro([23,309,2]))

def aprobado(notas:list[int]):
    notaCopia = notas.copy()
    if (promedio(notaCopia) >= 7) :
       for i in notaCopia:
           if i < 4 :
               return 3
       return 1    
    if (promedio(notaCopia) >= 4 and promedio(notaCopia) < 7):
        for i in notaCopia:
            if i < 4:
                return 3
        return 2         
    if ((algunoMenorACuatro(notaCopia)) or (promedio(notaCopia) <= 4)):
        return 3 

print(aprobado([9,8,7]))  #---> nota = 1
print(aprobado([4,5,6])) #---> nota = 2 
print(aprobado([4,5,2])) #---> nota = 3 
