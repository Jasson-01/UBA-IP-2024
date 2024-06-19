import inspect
import unittest
from solucion import escape_en_solitario

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
        code = inspect.getsource(escape_en_solitario)
        if len(code.splitlines()) <= 2:
            Ej4Test.is_default = True

    def setUp(self):
        if Ej4Test.is_default:
            self.skipTest("el test no se ejecuto porque la implementacion de la funcion es la provista por la catedra a modo de ejemplo")

    def test_escape_en_solitario(self):
        entrada = [
            [0,0,1,0],
        ]
        salida = [0]
        res = escape_en_solitario(entrada)
        self.assertEqual(res, salida)

    def test_escape_en_solitario_1(self):
    #  - Caso de una sola sala
        self.assertEqual(
            escape_en_solitario([[61,0,2,0]]), [])

    def test_escape_en_solitario_2(self):
    #  - Caso en el que nunca va solo
        self.assertEqual(
            escape_en_solitario([[61,0,2,0],
                                    [0,61,42,61],
                                    [0,0,50,61],
                                    [61,61,0,61]]), [])

    def test_escape_en_solitario_3(self):
    #  - Siempre va solo o no va nadie a esa sala
        self.assertEqual(
            escape_en_solitario([[0,0,1,0],
                                    [0,0,61,0],
                                    [0,0,0,0],
                                    [0,0,60,0]]), [0,1,3])

    def test_escape_en_solitario_4(self):
    #  - Va solo en primer o ultima sala
        self.assertEqual(
            escape_en_solitario([[0,0,1,0],
                                    [1,61,61,44],
                                    [6,1,2,4],
                                    [55,44,60,60],
                                    [0,0,60,0]]), [0,4])

    def test_escape_en_solitario_5(self):
    #  - Ninguno sale (tiempo == 61)
        self.assertEqual(
            escape_en_solitario([[61,61,1,61],
                                    [61,61,0,61],
                                    [61,61,60,61]]), [])

if __name__ == '__main__':
    unittest.main(verbosity=2)
