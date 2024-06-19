import inspect
import unittest
from solucionParcial6 import cuantos_sufijos_son_palindromos

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
        code = inspect.getsource(cuantos_sufijos_son_palindromos)
        if len(code.splitlines()) <= 2:
            Ej3Test.is_default = True

    def setUp(self):
        if Ej3Test.is_default:
            self.skipTest("el test no se ejecuto porque la implementacion de la funcion es la provista por la catedra a modo de ejemplo")

    def test_cuantos_sufijos_son_palindromos(self):
        entrada = "Diego" 
        salida = 1
        res = cuantos_sufijos_son_palindromos(entrada)
        self.assertEqual(res,salida)



    def test_sufijos_palindromos_1_letra(self):
        texto = 'a'
        self.assertEqual(cuantos_sufijos_son_palindromos(texto), 1)

    def test_sufijos_palindromos_2(self):   
        texto = 'alas'
        self.assertEqual(cuantos_sufijos_son_palindromos(texto), 2)
    
    def test_sufijos_palindromos_2_al_final(self):
        texto = 'parrap'
        self.assertEqual(cuantos_sufijos_son_palindromos(texto), 2)

    def test_sufijos_palindromos_3(self):
        texto = 'ododo'
        self.assertEqual(cuantos_sufijos_son_palindromos(texto), 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)

