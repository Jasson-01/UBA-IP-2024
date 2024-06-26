def agrupar_por_longitud(nombre_archivo: str) -> dict:
    diccionario: dict = {}
    archivo = open(nombre_archivo, "r", encoding="utf8")
    contenido = archivo.read()
    palabras: list[str] = contenido.split()

    for palabra in palabras:
        if len(palabra) in diccionario:
            diccionario[len(palabra)] += 1
        else:
            diccionario[len(palabra)] = 1

    archivo.close()

    return diccionario


print(agrupar_por_longitud("texto_diccionario.txt"))
