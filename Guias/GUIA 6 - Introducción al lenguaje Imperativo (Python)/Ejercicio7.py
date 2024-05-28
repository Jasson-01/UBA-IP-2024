#Implementar las funciones del ejercicio 6 con FOR 

# --- EJM 1 ---

def numeros_1_al_10():
    for i in range(1,11):
        print(i) 
numeros_1_al_10()

# --- EJM 2 ---

def numeros_pares_del_10_al_40():
    for i in range(10,41,2):
        print(i) 
numeros_pares_del_10_al_40()

# --- EJM 3 ---

def imprimir_10_veces_eco():
    for i in range(1,11):
        print("eco")
imprimir_10_veces_eco() 

# --- EJM 4 ---

def despegue(numero:int):
    for i in range(numero,0,-1):
        print(i)
    print("Despegue!!!")
despegue(10)

# --- EJM 5 ---

def viaje_en_el_tiempo(añoPartida:int,añoLlegada:int):
    print(f"año actual: {añoPartida}")
    for i in range(añoPartida-1,añoLlegada-1,-1):
        print(f"Viajo un año al pasado, estamos en el año: {i}")
viaje_en_el_tiempo(2010,2000)    













































