
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

# Este problema esta Hecho por ChatGPT

def frecuencia_posiciones_por_caballo(caballos: list[str], carreras: dict[str, list[str]]) -> dict[str, list[int]]:
    # Crear el diccionario para almacenar las frecuencias de posiciones
    resultado = {}
    for caballo in caballos:
        resultado[caballo] = [0] * len(caballos)
#    print(resultado)
    # Recorrer cada carrera y actualizar las posiciones de los caballos
    for posiciones_caballos in carreras.values():
        posicion = 0
        for caballo in posiciones_caballos:
            resultado[caballo][posicion] += 1
            posicion += 1

    return resultado

# Ejemplo de uso
caballos = ["linda", "petisa", "mister", "luck"]
carreras = {
    "carrera1": ["linda", "petisa", "mister", "luck"],
    "carrera2": ["petisa", "mister", "linda", "luck"]
}

res = frecuencia_posiciones_por_caballo(caballos, carreras)
print(res)

"""
caballos = ["a","b","c","d"]
carreras = {"carrera1":["a","b","c","d"],"carrera2":["b","c","a","d"]}
res = {"b":[1,1,0,0],"c":[0,1,1,0],"a":[1,0,1,0],"d":[0,0,0,2]}
"""

# ----- PROBLEM-4 -------

def matriz_capicua(matriz:list[list[int]])->bool:
    for fila in matriz:
        for i in range(len(fila)):
            if fila[i] != fila[-i-1]:
                return False
    return True
  
#m = [[1,2,2,1],[-5,6,6,-5],[0,1,1,0]]
#print(matriz_capicua(m))





















