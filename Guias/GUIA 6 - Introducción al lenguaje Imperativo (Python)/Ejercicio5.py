# ---  EJM 1  --- 

def devolver_el_doble_si_es_par(numero:int)->int:
    if numero % 2 == 0:
        return 2*numero
    return numero

print(devolver_el_doble_si_es_par(3))

# ---  EJM 2  ---

def devolver_valor_si_es_par_sino_el_que_sigue(numero:int)->int:
        if numero % 2 == 0:
           return numero
        return (numero+1)

print(devolver_valor_si_es_par_sino_el_que_sigue(5))


# ---  EJM 3  ---

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9v1(numero)->int:
     if numero % 3 == 0:
          return 2*numero
     if numero % 9 == 0:
          return 3*numero
     else:
          return numero

print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9v1(18))

# ---  EJM 4  ---

def lindo_nombre(nombre:str)->str:
    if len(nombre) >= 5:
         return "Tu nombre tiene muchas letras!"
    return "Tu nombre tiene menos de 5 caracteres"

print(lindo_nombre("Marjorie"))


# ---  EJM 5  ---

def rango(numero:int):
    if numero < 5:
       return "Menor a 5"   
    if numero >= 10 and numero <= 20:
       return "Entre 10 y 20"
    if numero > 20:
        return "Mayor a 20"
    return numero

print(rango(21))

# ---  EJM 6  ---

def jubilacion(genero:str,edad:int)->str:
    if genero == "F" or "f":
       if edad >= 18 and edad < 60:
           return "Te toca trabajar"
       if edad >= 60 :
           return "Andá de vacaciones"
       else:
           return "Andá de vacaciones"
    if genero == "M" or "m":
       if edad >= 18 and edad < 65:
           return "Te toca trabajar"
       if edad >= 65 :
           return "Andá de vacaciones"
       else:
           return "Andá de vacaciones"
print(jubilacion("f",16))















































































