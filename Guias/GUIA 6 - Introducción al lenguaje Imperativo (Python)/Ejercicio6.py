#  Implementar las siguientes funciones usando repetición condicional while:

# --- EJM 1 ---

def numeros_1_al_10():
    numero = 0
    while numero <= 10 :
        print(numero)
        numero += 1

numeros_1_al_10()

# --- EJM 2 ---

def pares_10_al_40():
    numero = 10
    while numero <= 40:
        print(numero)
        numero += 2
pares_10_al_40()

# --- EJM 3 ---

def imprimir_10_veces_eco():
    contador = 1
    while contador < 11:
        print(f"{contador}:eco")
        contador += 1
imprimir_10_veces_eco()

# --- EJM 4 ---

def cuenta_regresiva(numero:int):
    x = numero
    print(x)
    while x > 1 :
        print(x-1)
        x -= 1
    print("Despegue!!!")
cuenta_regresiva(6)

# --- EJM 5 ---

# añoLlegada < añoPartida
def viaje_en_el_tiempo(añoPartida:int,añoLlegada:int):

    print(f"Año actual:{añoPartida}")
    while añoPartida > añoLlegada :
          print(f"Viajo un año al pasado, estamos en el año:{añoPartida - 1}")
          añoPartida -= 1 
viaje_en_el_tiempo(2010,2000)

# --- EJM 6 ---
x = 384
def viaje_en_el_tiempo_384aC(añoPartida:int,x):
    
    print(f"Año actual:{añoPartida}")
    while añoPartida >= x :
          print(f"Viajo un año al pasado, estamos en el año:{añoPartida - 20}")
          añoPartida -= 20 
viaje_en_el_tiempo_384aC(500,x)
































































































