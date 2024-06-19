# que agregue la frase al comienzo del archivo original (similar al ejercicio anterior, sin hacer una copia del archivo).

def agregar_frase_al_principio(nombre_archivo : str,frase : str):
    actual = open(nombre_archivo,"r")
    contenido:list = actual.readlines()
    contenido[0] = frase + "\n" + contenido[0]
    actual.close()

    actual = open(nombre_archivo,"w")
    actual.writelines(contenido) 

    return actual

agregar_frase_al_principio("frasesAgregadas.txt","Agregando frase al inicio")














