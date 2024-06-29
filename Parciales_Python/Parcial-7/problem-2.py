### 1ERA FORMA #########################################################################

def stock_productos(stock_cambios: list[tuple[str, int]]) -> dict[str, tuple[int, int]]:
    copia_stock: list = stock_cambios.copy() # Primero hice una copia de "stock_cambios"
    diccionario_res: dict = dict() # Luego cree el diccionario de salida

    for tuple in copia_stock: #Ahora recorro las tuplas de la lista de tuplas
        clave =  tuple[0]
        if clave not in diccionario_res: # verifico si el primer elemento de la tupla ya esta en el diccionario
            diccionario_res[clave] = (tuple[1], tuple[1]) #Si no esta, creo en el diccionario con clave el primer elemento de la tupla, y su valor sea una tupla a priori con el segundo elemento de la tupla cada uno, que se ira modificando, mientras se recorra la lista de tuplas.  
        else:
            valor = diccionario_res[clave] # este me da el valor del diccionario con clave "clave"
            min = tuple[1]
            max = tuple[1]
            if valor[0] >= min:
                diccionario_res[clave] = (min, valor[1])
            elif valor[1] <= max:
                diccionario_res[clave] = (valor[0], max)

    return diccionario_res


### 2DA FORMA ###########################################################################

def minimo(lista: list[int]) -> int:
    menor = lista[0]
    for i in lista:
        if i <= menor:
            menor = i
    return menor


def maximo(lista: list[int]) -> int:
    maximo = lista[0]
    for i in lista:
        if i >= maximo:
            maximo = i
    return maximo


def stock_productos2(stock_cambios: list[tuple[str, int]]) -> dict[str, tuple[int, int]]:

    # Formando Diccionario:
    diccionario: dict = {}
    for clave in stock_cambios:
        if clave[0] not in diccionario:
            diccionario[clave[0]] = tuple()
    # return diccionario

    # Formando lista de claves:
    listaClaves: list[str] = []
    for elemento in stock_cambios:
        if elemento[0] not in listaClaves:
            listaClaves.append(elemento[0])
    # return listaClaves

    # Añadiendo minimo y maximo a su clave correspondiente
    for clave in listaClaves:
        lista_tmp = []
        for elem in stock_cambios:
            if elem[0] == clave:
                lista_tmp.append(elem[1])
        diccionario[clave] = (minimo(lista_tmp), maximo(lista_tmp))

    print(stock_cambios)  # Cumple la especifiacion de tipo "in"
    return diccionario


listaStock = [("a", 4), ("b", 2), ("d", 5), ("a", 9),
              ("b", 99), ("d", 8), ("b", 1), ("a", 5)]
print(stock_productos2(listaStock))


# ejm:
# listaStock = [("a",4),("b",2),("d",5),("a",9),("b",99),("d",8),("b",1),("a",5)]
# => res = {"a":(4,9), "b":(1,99), "d":(5,8)}

# ejemplo_dict = {"Alice": (25, 5),"Bob": (30, 10),"Charlie": (22, 8),"Diana": (28, 7)}
