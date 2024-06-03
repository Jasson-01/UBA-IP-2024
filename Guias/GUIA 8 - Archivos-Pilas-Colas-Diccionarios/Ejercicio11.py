from queue import LifoQueue as Pila

def funcionAplanar(texto:str)->list[str]:
    abecedadrioCompleto:str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"   
    lista:list[str]= []
    palabra_Actual:str = ""
    for i in range(len(texto)):
         if (texto[i] in abecedadrioCompleto) :
              palabra_Actual += texto[i]
         else:
            if palabra_Actual:  # si palabra_Actual tiene caracteres entonces es TRUE
              lista.append(palabra_Actual)
              palabra_Actual = ""
    if palabra_Actual: # añadimos la ultima palabra si existe
         lista.append(palabra_Actual)
    return lista   
              
def listarParentesis(cadenaFormula:str)->list[str]:
    listaCaracteres: list[str] = funcionAplanar(cadenaFormula)
    parentesis:list[str] = []

    for caracter in listaCaracteres:
        if caracter == "(" or caracter == ")":
            parentesis.append(caracter)
    return parentesis

def esta_bien_balanceada(cadenaFormula : str) -> bool:
    lista_parentesis = listarParentesis(cadenaFormula)
    estan_balanceadas = True
    
    if len(lista_parentesis) % 2 != 0:
        estan_balanceadas = False
        return estan_balanceadas 
    
    rango:int = int(len(lista_parentesis)/2)

    for i in range(rango):
        if lista_parentesis[i] != "(" or lista_parentesis[-i-1] != ")":
            estan_balanceadas = False
            return estan_balanceadas
        

    return estan_balanceadas

#print(esta_bien_balanceada("1 + (2 x 3 = (20 / 5))")) # Funciona   
#print(esta_bien_balanceada("10 * ( 1 + ( 2 * ( = 1 ) ) )")) # Funciona
#print(esta_bien_balanceada("1 + ) 2 x 3 ( ()")) # Funciona
#print(esta_bien_balanceada("10 * ( 1 + ( 2 * ( = 1)))")) # No funciona

#2DA FORMA

def esta_bien_balanceada2(s: str) -> bool:
    p = Pila()
    for char in s:
        if char == '(':
            p.put(char)
        elif char == ')': #Al final no agrega el ")", solo lo usa para quitar el "(" mas cercano, y ver si la lista esta vacia o no 
            if p.empty():
                return False
            p.get()
    if p.empty():
        return True
    else:
        return False
    
print(esta_bien_balanceada2('1 +( (2 x 3 - (20 / 5))')) # RES -> False 





























