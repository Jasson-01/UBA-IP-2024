import inspect
import unittest
from solucionParcial6 import quien_gano_el_tateti_facilito

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej4Test(unittest.TestCase):

    is_default = False

    def __init__(self, *args, **kwargs):
        super(Ej4Test, self).__init__(*args, **kwargs)
        code = inspect.getsource(quien_gano_el_tateti_facilito)
        if len(code.splitlines()) <= 2:
            Ej4Test.is_default = True

    def setUp(self):
        if Ej4Test.is_default:
            self.skipTest("el test no se ejecuto porque la implementacion de la funcion es la provista por la catedra a modo de ejemplo")

    def test_no_hay_tres_consecutivas_5_X_5(self):
        tablero = [['X', 'O', 'X', 'O', 'X'],
                   ['O', 'X', 'O', 'X', 'O'],
                   ['X', 'X', 'X', 'O', 'X'],
                   ['X', 'O', 'O', 'X', 'O'],
                   ['O', 'O', 'X', 'X', 'O']]
        self.assertEqual(quien_gano_el_tateti_facilito(tablero), 0)

    def test_tres_x_consecutivas_inicio(self):
        tablero = [['X', 'O', ' ', ' ', ' '],
                   ['X', 'X', ' ', ' ', ' '],
                   ['X', ' ', 'O', ' ', ' '],
                   [' ', ' ', ' ', 'X', ' '],
                   [' ', ' ', ' ', ' ', 'O']]
        self.assertEqual(quien_gano_el_tateti_facilito(tablero), 1)

    def test_tres_o_consecutivas_medio(self):
        tablero = [['X', ' ', ' ', ' ', ' '],
                   [' ', 'O', ' ', ' ', ' '],
                   ['X', 'O', 'X', ' ', ' '],
                   [' ', 'O', ' ', 'X', ' '],
                   [' ', ' ', ' ', ' ', 'O']]
        self.assertEqual(quien_gano_el_tateti_facilito(tablero), 2)

    def test_tres_x_y_tres_o_consecutivas_medio_final(self):
        tablero = [[' ', 'O', ' ', ' ', ' '],
                   [' ', 'X', 'X', ' ', ' '],
                   [' ', ' ', 'X', ' ', 'O'],
                   [' ', ' ', 'X', 'X', 'O'],
                   [' ', ' ', ' ', ' ', 'O']]
        self.assertEqual(quien_gano_el_tateti_facilito(tablero), 3)

    def test_no_hay_tres_consecutivas_en_matriz_grande(self):
        tablero = [['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'],
                   ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'],
                   ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'],
                   ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'],
                   ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'],
                   ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'],
                   ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'],
                   ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'],
                   ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O'],
                   ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']]
        self.assertEqual(quien_gano_el_tateti_facilito(tablero), 0)
    
    
 

if __name__ == '__main__':
    unittest.main(verbosity=2)
