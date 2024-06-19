import inspect
import unittest
from solucion import tiempo_mas_rapido

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej2Test(unittest.TestCase):

    is_default = False

    def __init__(self, *args, **kwargs):
        super(Ej2Test, self).__init__(*args, **kwargs)
        code = inspect.getsource(tiempo_mas_rapido)
        if len(code.splitlines()) <= 2:
            Ej2Test.is_default = True

    def setUp(self):
        if Ej2Test.is_default:
            self.skipTest("el test no se ejecuto porque la implementacion de la funcion es la provista por la catedra a modo de ejemplo")

    def test_tiempo_mas_rapido(self):
        entrada = [1]
        salida = 0
        res = tiempo_mas_rapido(entrada)
        self.assertEqual(res, salida)

    def test_tiempo_mas_rapido_inicio_con_repetidos(self):
        self.assertEqual(tiempo_mas_rapido([60,4,5,10,60,1,42]),0)

    def test_tiempo_mas_rapido_uno_solo_repetidos(self):
    #  - Caso de un solo tiempo (valido)
        self.assertEqual(tiempo_mas_rapido([9,9,9]),0)

    def test_tiempo_mas_rapido_medio(self):
    #  - Caso de un solo tiempo valido y el resto invalido
        self.assertEqual(tiempo_mas_rapido([0,61,0,42,61,0,0]),3)
        
    def test_tiempo_mas_rapido_final(self):
    #  - Tiempos mezclados y con repetidos
        self.assertEqual(tiempo_mas_rapido([1,61,0,33,7,1,0,61,1,0,42]),10)

if __name__ == '__main__':
    unittest.main(verbosity=2)



   





    
