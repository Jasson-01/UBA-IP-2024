"""
Dado un archivo de texto con comentarios, implementar una funcion
clonar sin comentarios(in nombre archivo : str) que toma un archivo de entrada y genera un nuevo archivo que tiene el
contenido original sin las lineas comentadas. Para este ejercicio vamos a considerar comentarios como aquellas lineas que tienen
un caracter ‘#’como primer caracter de la linea, o si no es el primer caracter, se cumple que todos los anteriores son espacios
"""

def sacarEspaciosAlPrincipio(palabra:str)->str:
    nueva_palabra:str = ""

    for caracter in palabra:
        if caracter != " " :
            nueva_palabra += caracter

    return nueva_palabra


def clonar_sin_comentarios(nombre_archivo : str):
    viejo = open(nombre_archivo,"r")
    nuevo = open("clonadoSinComentarios.txt","w")
    contenido = viejo.readlines()
    nuevo_contenido = []

    for linea in contenido:
           linea_sin_espacios:str = sacarEspaciosAlPrincipio(linea) 
           if  linea_sin_espacios[0] != "#":
                nuevo_contenido.append(linea)
    nuevo.writelines(nuevo_contenido)
    return nuevo

clonar_sin_comentarios("comentarios.txt")

archi = open("clonadoSinComentarios.txt","r")
contenido = archi.read()
print(contenido)
























