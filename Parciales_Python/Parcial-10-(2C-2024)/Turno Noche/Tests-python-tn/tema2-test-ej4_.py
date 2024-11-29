import unittest
from solucion import dame_el_que_falta
from random import shuffle

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
        self.method = dame_el_que_falta
    
    def test_ej4_lista_simple(self):
        entrada: list[tuple[int, int]] = [(1,1),(1,2),(2,1)]
        salida: tuple[int,int] = (2,2)
        self.assertTupleEqual(salida, dame_el_que_falta(entrada))
    
    def test_ej4_lista_mas_larga(self):
        entrada: list[tuple[int, int]] = [(1,1),(2,2),(3,1),(1,2),(1,3),(3,2),(2,3),(3,3)]
        salida: tuple[int,int] = (2,1)
        self.assertTupleEqual(salida, dame_el_que_falta(entrada))
    
    def test_ej4_falta_el_mas_chico(self):
        entrada: list[tuple[int, int]] = [
            (1,2), (1,3), (1,4),
            (3,1), (3,2), (3,3), (3,4),
            (2,1), (2,2), (2,3), (2,4),
            (4,1), (4,2), (4,3), (4,4)
        ]
        salida: tuple[int,int] = (1,1)
        self.assertTupleEqual(salida, dame_el_que_falta(entrada))

    def test_ej4_falta_el_mas_grande(self):
        entrada: list[tuple[int, int]] = [
            (2,1), (2,2), (2,3), (2,4),
            (3,1), (3,2), (3,3), (3,4),
            (1,1), (1,2), (1,3), (1,4),
            (4,1), (4,2), (4,3)
        ]
        salida: tuple[int,int] = (4,4)
        self.assertTupleEqual(salida, dame_el_que_falta(entrada))

    def test_ej4_test_grande_ordenado(self):
        entrada: list[tuple[int, int]] = [(i,j) for i in range(1,11) for j in range(1,11)]
        entrada.remove((5,7))
        salida: tuple[int,int] = (5,7)
        self.assertTupleEqual(salida, dame_el_que_falta(entrada))
    
    def test_ej4_test_grande_desordenado(self):
        entrada: list[tuple[int, int]] = [(i,j) for i in range(1,11) for j in range(1,11)]
        entrada.remove((8,3))
        shuffle(entrada)
        salida: tuple[int,int] = (8,3)
        self.assertTupleEqual(salida, dame_el_que_falta(entrada))

if __name__ == '__main__':
    unittest.main(verbosity=2)
