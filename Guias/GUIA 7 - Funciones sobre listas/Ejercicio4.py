# ----- PROBLEM 1 -----

def nombres_de_estudiantes()->list:
    lista:list = []
    names = input("Digite nombre del estudiante ( o 'listo' para terminar): ")
    while names != "listo" :
        lista.append(names)
        names = input("Digite nombre del estudiante ( o 'listo' para terminar): ")
    return lista

#print(nombres_de_estudiantes())

# ----- PROBLEM 2 -----

def historial_sube()->list[tuple]:
    lista: list[tuple] = []
    entrada = input("Digite opcion -> 'C' , 'D' o 'X' : ") 
    while entrada != "X" :
             if entrada == 'C':
                   carga = int(input("Cuanto es el monto a cargar: "))
                   lista.append(('C',carga))     
             elif entrada == 'D':
                   descontar = int(input("Cuanto es el monto a descontar: "))     
                   lista.append(('D',descontar))
             entrada = input("Digite opcion -> 'C' , 'D' o 'X' : ")                         
    return lista

print(historial_sube())
