import inspect
import unittest
from solucion import promedio_de_salidas

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej1Test(unittest.TestCase):

    is_default = False

    def __init__(self, *args, **kwargs):
        super(Ej1Test, self).__init__(*args, **kwargs)
        code = inspect.getsource(promedio_de_salidas)
        if len(code.splitlines()) <= 2:
            Ej1Test.is_default = True

    def setUp(self):
        if Ej1Test.is_default:
            self.skipTest("el test no se ejecuto porque la implementacion de la funcion es la provista por la catedra a modo de ejemplo")

    def test_promedio_de_salidas(self):
        entrada = {"a": [0]}
        salida = {"a":(0,0.0)}
        res = promedio_de_salidas(entrada)
        self.assertEqual(res, salida)
        
        
    def test_promedio_general(self):
    
    # Unicos tests interesantes: 
    #  - Que manejen bien dividir el caso promedio 0
    #  - Que puedan retornar todos los nombres
    #  - Que discriminen bien los tiempos con 0 y 61
    #  - Que el orden de la tupla sea correcto
    #  - Que el promedio sea del tipo correcto (?)
    # Todo esta contemplado en este test.
    
        diccionario_test = {
            "a":[61,60,59,58],
            "b":[1,2,3,0],
            "c":[2,3,4,5],
            "d":[2,0,61,2],
            "e":[0,0,0,0],
            "f":[61,61,61,61]
        }

        self.assertDictEqual(promedio_de_salidas(diccionario_test),
        {"a":(3, 59.0),
         "b":(3, 2.0),
         "c":(4, 14/4), 
         "d":(2, 2.0),
         "e":(0, 0.0),
         "f":(0, 0.0)})     


if __name__ == '__main__':
    unittest.main(verbosity=2)



   





    
