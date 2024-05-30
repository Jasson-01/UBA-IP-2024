archivo = open("mi_archivo.txt","a")
archivo.write("HOla como estas! ?")
archivo.close()

archivo = open("mi_archivo.txt","r")
contenido = archivo.read()
archivo.close()

print(contenido)


