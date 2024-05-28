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


# ---  EJM 2  ---
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9v1(numero)->int:
     if numero % 3 == 0:
          return 2*numero
     if numero % 9 == 0:
          return 3*numero
     else:
          return numero





























































































