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


def stock_productos(stock_cambios: list[tuple[str, int]]) -> dict[str, tuple[int, int]]:

    # Formando Diccionario:
    diccionario: dict() = {}
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
print(stock_productos(listaStock))


# ejm:
# listaStock = [("a",4),("b",2),("d",5),("a",9),("b",99),("d",8),("b",1),("a",5)]
# => res = {"a":(4,9), "b":(1,99), "d":(5,8)}

# ejemplo_dict = {"Alice": (25, 5),"Bob": (30, 10),"Charlie": (22, 8),"Diana": (28, 7)}
