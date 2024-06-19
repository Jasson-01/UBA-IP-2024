def es_primo(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# num = 113
# print(es_primo(num))

def filtrar_codigos_primos(codigos_barras: list[int]) -> list[int]:
    codigos_primos = []
    for codigo in codigos_barras:
        ultimos_tres_digitos = codigo % 1000
        if es_primo(ultimos_tres_digitos):
            codigos_primos.append(codigo)

    # Cumple la especificaion "in" no es modificada la lista original!
    print(codigos_barra)
    return codigos_primos


# Ejemplo de prueba:
codigos_barra = [123101, 456002, 789011, 112345, 678911]
print(filtrar_codigos_primos(codigos_barra))
# -> Salida: [123101, 456002, 789011, 678911]
