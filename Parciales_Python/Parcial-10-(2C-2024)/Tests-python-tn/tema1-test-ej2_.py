import unittest
from solucion import longitud_mas_grande

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
        self.method = longitud_mas_grande
    
    def test_ej2_una_lista_un_uno(self):
        entrada: list[list[int]] = [[1]]
        salida: int = 1
        self.assertEqual(salida, longitud_mas_grande(entrada))
    
    def test_ej2_una_lista_varios_unos(self):
        entrada: list[list[int]] = [[1, 1, 1, 5, 4, 3]]
        salida: int = 3
        self.assertEqual(salida, longitud_mas_grande(entrada))
    
    def test_ej2_una_lista_varias_secuencias_de_unos(self):
        entrada: list[list[int]] = [[1, 1, 5, 4, 3, 1, 1, 1, 1, 2, 1, 1, 1]]
        salida: int = 4
        self.assertEqual(salida, longitud_mas_grande(entrada))
    
    def test_ej2_varias_listas_max_al_principio(self):
        entrada: list[list[int]] = [[1, 1, 1, 5, 4, 3], [1, 1, 1, 1, 4, 7, 8], [2, 1, 1, 4, 3]]
        salida: int = 4
        self.assertEqual(salida, longitud_mas_grande(entrada))
    
    def test_ej2_varias_listas_max_al_final(self):
        entrada: list[list[int]] = [[2, 6], [0, 6], [2, 0, 1, 1]]
        salida: int = 2
        self.assertEqual(salida, longitud_mas_grande(entrada))
    
    def test_ej2_muchas_listas(self):
        entrada: list[list[int]] = [[5, 4, 1, 1, 1, 6],
                                    [1, 1, 6, 1, 1, 1, 1, 4, 5],
                                    [111, 111, 111, 111, 1, 1, 3],
                                    [11, 3, 4, 64, 4, 3],
                                    [0, 3, 0, 3, 4, 5, 6],
                                    [1, 1, 1, 1, 1, 1, 4, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
                                    [1, 1, 3, 11, 111, 1111, 11111, 1, 1, 3]]
        salida: int = 10
        self.assertEqual(salida, longitud_mas_grande(entrada))

if __name__ == '__main__':
    unittest.main(verbosity=2)
