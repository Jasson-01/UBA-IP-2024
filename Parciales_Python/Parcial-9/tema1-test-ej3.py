import inspect
import unittest
from solucion import racha_mas_larga

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej3Test(unittest.TestCase):

    is_default = False

    def __init__(self, *args, **kwargs):
        super(Ej3Test, self).__init__(*args, **kwargs)
        code = inspect.getsource(racha_mas_larga)
        if len(code.splitlines()) <= 2:
            Ej3Test.is_default = True

    def setUp(self):
        if Ej3Test.is_default:
            self.skipTest("el test no se ejecuto porque la implementacion de la funcion es la provista por la catedra a modo de ejemplo")

    def test_racha_mas_larga(self):
        entrada = [1]
        salida = (0,0)
        res = racha_mas_larga(entrada)
        self.assertEqual(res,salida)
        
    def test_racha_mas_larga_1(self):       
        self.assertEqual(racha_mas_larga([0,1,1,1,0,1,1,1,1,1]),(5,9))

    def test_racha_mas_larga_2(self):
    #  - Mayor subsecuencia al principio
        self.assertEqual(racha_mas_larga([1,1,0,0,1,0]),(0,1))

    def test_racha_mas_larga_3(self):
    #  - Subsecuencias de longitud 1
        self.assertEqual(racha_mas_larga([0,1,0]), (1,1))


    def test_racha_mas_larga_3_1(self):        
        self.assertEqual(racha_mas_larga([1,61,1]), (0,0))

    def test_racha_mas_larga_4(self):        
    #  - Secuencia no termina con un tiempo valido
        self.assertEqual(racha_mas_larga([1,2,3,61,1,2,3,7,0]), (4,7))

    def test_racha_mas_larga_5(self):
    #  - Secuencia no empieza con tiempo valido
        self.assertEqual(racha_mas_larga([0,60,60,60,60]), (1,4))

    def test_racha_mas_larga_6(self):
    #  - Subsecuencias de igual tamaño
        self.assertEqual(racha_mas_larga([61,1,1,1,61,1,1,1]), (1,3))
        #self.assertEqual(racha_mas_larga([61,1,1,1,0,4,3,61,1,1,1]), (1,3))

if __name__ == '__main__':
    unittest.main(verbosity=2)

