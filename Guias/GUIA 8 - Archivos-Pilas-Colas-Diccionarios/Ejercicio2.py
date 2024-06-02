

def invertir_lineas(nombre_archivo:str)->str:
    listaDeLineas:list = []
    viejo = open(nombre_archivo,"r",encoding="utf8")
    nuevo = open("reverso.txt","w",encoding="utf8")

    for i in viejo.readlines():
        listaDeLineas.append(i)
    print(listaDeLineas)
    viejo.close()

    for i in range(len(listaDeLineas)-1,-1,-1):
        nuevo.write((listaDeLineas[i]))
    nuevo.close()

    return nuevo 

invertir_lineas("mi_archivo2.txt")
archi = open("reverso.txt","r")
contenido = archi.read()
print(contenido)

   