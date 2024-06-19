# que la agregue al final del archivo original (sin hacer una copia).
def agregar_frase_al_final(nombre_archivo : str, frase : str):
    actual = open(nombre_archivo,"a")
    actual.write(frase)
    actual.close()
    

print(agregar_frase_al_final("frasesAgregadas.txt","hola nueva frase"))

#Esto lo hago para que me lo muestre en la consola sin ir al arhivo 
archi = open("frasesAgregadas.txt","r")
contenido = archi.read()
print(contenido)