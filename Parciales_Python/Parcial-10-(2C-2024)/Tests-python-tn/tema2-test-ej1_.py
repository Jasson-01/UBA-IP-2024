import unittest
from solucion import multiplos_de_primos

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
        self.method = multiplos_de_primos
    
    def test_ej1_cero_elementos(self):
        entrada: list[int] = []
        salida: dict[int, int] = {}
        self.assertDictEqual(salida, multiplos_de_primos(entrada))
    
    def test_ej1_un_elemento(self):
        entrada: list[int] = [5]
        salida: dict[int, int] = {5: 1}
        self.assertDictEqual(salida, multiplos_de_primos(entrada))

    def test_ej1_dos_elementos(self):
        entrada: list[int] = [2, 3]
        salida: dict[int, int] = {2: 1, 3: 1}
        self.assertDictEqual(salida, multiplos_de_primos(entrada))
    
    def test_ej1_elementos_con_factores_repetidos(self):
        entrada: list[int] = [5, 7, 49]
        salida: dict[int, int] = {5:1, 7:2}
        self.assertDictEqual(salida, multiplos_de_primos(entrada))

    def test_ej1_elementos_con_varios_factores_repetidos(self):
        entrada: list[int] = [5, 25, 125, 625]
        salida: dict[int, int] = {5:4}
        self.assertDictEqual(salida, multiplos_de_primos(entrada))

    def test_ej1_muchos_numeros(self):
        entrada: list[int] = [2,3,4,5,6,7,8,9,10]
        salida: dict[int, int] = {2:5, 3:3, 5:2, 7:1}
        self.assertDictEqual(salida, multiplos_de_primos(entrada))

    def test_ej1_muchisimos_numeros(self):
        entrada: list[int] = list(range(1, 101))
        salida: dict[int, int] = {2: 50, 3: 33, 5: 20, 7: 14,
            11: 9, 13: 7, 17: 5, 19: 5,
            23: 4, 29: 3, 
            31: 3, 37: 2, 
            41: 2, 43: 2, 47: 2, 
            53: 1, 59: 1, 
            61: 1, 67: 1, 
            71: 1, 73: 1, 79: 1, 
            83: 1, 89: 1, 
            97: 1}
        self.assertDictEqual(salida, multiplos_de_primos(entrada))

    def test_ej1_lista_con_un_uno(self):
        entrada: list[int] = [1]
        salida: dict[int, int] = {}
        self.assertDictEqual(salida, multiplos_de_primos(entrada))

if __name__ == '__main__':
    unittest.main(verbosity=2)
