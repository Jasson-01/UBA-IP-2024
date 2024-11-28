import unittest
from queue import LifoQueue as Pila
from solucion import resolver_cuentas

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertDictEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej1Test():
    def __init__(self, *args, **kwargs):
        super(Ej1Test, self).__init__(*args, **kwargs)
        self.method = resolver_cuentas
    
    def test_ej3_pila_vacia(self):
        entrada: Pila[str] = Pila()
        salida: list[int] = []
        self.assertListEqual(salida, resolver_cuentas(entrada))
    
    def test_ej3_una_cuenta(self):
        entrada: Pila[str] = crear_pila(["1+1"])
        salida: list[int] = [2]
        self.assertListEqual(salida, resolver_cuentas(entrada))

    def test_ej3_dos_cuentas_preserva_pila(self):
        entrada: Pila[str] = crear_pila(["2+4", "7+5"])
        entrada_copia : Pila[str] = copiar_cola(entrada)
        salida: list[int] = [12, 6]
        self.assertListEqual(salida, resolver_cuentas(entrada))
        self.assertEqual(entrada.queue, entrada_copia.queue)
    
    def test_ej3_varias_cuentas(self):
        entrada: Pila[str] = crear_pila(["2+4", "7+5", "1-6", "2+3+1", "100-100+123+123-200", "10-10"])
        salida: list[int] = [0, 46, 6, -5, 12, 6]
        self.assertListEqual(salida, resolver_cuentas(entrada))

    def test_ej3_cuentas_que_empiezan_con_menos(self):
        entrada: Pila[str] = crear_pila(["-2+4", "-7+5+2", "-1-6"])
        salida: list[int] = [-7, 0, 2]
        self.assertListEqual(salida, resolver_cuentas(entrada))

    def test_ej3_cuentas_que_empiezan_con_mas(self):
        entrada: Pila[str] = crear_pila(["+2-4", "+7-5-2", "+1+6"])
        entrada_copia : Pila[str] = copiar_cola(entrada)
        salida: list[int] = [7, 0, -2]
        self.assertListEqual(salida, resolver_cuentas(entrada))
        self.assertEqual(entrada.queue, entrada_copia.queue)

def crear_pila(elementos):
    pila = Pila()
    for elem in elementos:
        pila.put(elem)
    return pila

def copiar_cola(pila: Pila):
    elementos = list(pila.queue)
    nueva_pila = Pila()
    for e in elementos:
        nueva_pila.put(e)
    return nueva_pila

if __name__ == '__main__':
    unittest.main(verbosity=2)
