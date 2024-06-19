import inspect
import unittest
from solucion import subsecuencia_mas_larga

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
        code = inspect.getsource(subsecuencia_mas_larga)
        if len(code.splitlines()) <= 2:
            Ej3Test.is_default = True
        
    def setUp(self):
        if Ej3Test.is_default:
            self.skipTest("el test no se ejecuto porque la implementacion de la funcion es la provista por la catedra a modo de ejemplo")

    def test_el_mezcladito(self): 
        res = subsecuencia_mas_larga(["perro", "tortuga", "perro", "gato", "perro", "tortuga", "gato", "gato"])
        self.assertEqual(res, 2) 

    def test_mas_largo_al_inicio(self): 
        res = subsecuencia_mas_larga(["perro","perro","perro", "tortuga", "gato", "x", "perro", "tortuga", "gato", "gato"])
        self.assertEqual(res, 0) 

    def test_mas_largo_al_final(self): 
        res = subsecuencia_mas_larga(["perro","perro","perro", "tortuga", "gato", "x", "perro", "tortuga", "gato", "gato","perro","perro","perro" ])
        self.assertEqual(res, 8) 

    def test_mas_largo_repetido(self): 
        res = subsecuencia_mas_larga(["perro", "tortuga", "gato", "gato", "x", "x", "gato", "gato","z" ])
        self.assertEqual(res, 2) 

    def test_mas_largo_cortito_al_principio_repetido(self): 
        res = subsecuencia_mas_larga(["perro", "tortuga", "gato", "x", "x", "gato", "z" ])
        self.assertEqual(res, 0) 

    def test_mas_largo_cortito_en_el_medio(self): 
        res = subsecuencia_mas_larga(["a", "perro", "tortuga", "gato", "x", "x", "gato", "z" ])
        self.assertEqual(res, 1) 

    def test_mas_largo_cortito_al_final(self): 
        res = subsecuencia_mas_larga(["a", "b", "tortuga", "c", "x", "x", "x", "z", "gato" ])
        self.assertEqual(res, 8) 

    def test_mas_largo_todos_perros(self): 
        res = subsecuencia_mas_larga(["perro", "perro", "perro", "perro", "perro", "perro", "perro", "perro" ])
        self.assertEqual(res, 0) 

    def test_mas_largo_todos_perros_y_gatos(self): 
        res = subsecuencia_mas_larga(["gato", "perro", "perro", "perro", "perro", "perro", "perro", "gato" ])
        self.assertEqual(res, 0) 

    def test_mas_largo_un_solo_elem(self): 
        res = subsecuencia_mas_larga(["gato"])
        self.assertEqual(res, 0) 

if __name__ == '__main__':
    unittest.main(verbosity=2)

