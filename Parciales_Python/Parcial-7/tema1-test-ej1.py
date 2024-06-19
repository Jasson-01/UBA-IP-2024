import inspect
import unittest
from solucion import stock_productos

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
        code = inspect.getsource(stock_productos)
        if len(code.splitlines()) <= 2:
            Ej1Test.is_default = True
        
    def setUp(self):
        if Ej1Test.is_default:
            self.skipTest("el test no se ejecuto porque la implementacion de la funcion es la provista por la catedra a modo de ejemplo")

    def test_el_mezcladito(self): 
        res = stock_productos( [("y", 5),("x", 0), ("bolsas", 100),("y", 4),("x", 1),("bolsas", 100),("x", 2),("bolsas", 105),("correas", 3), ("huesos", 5), ("huesos", 10), ("huesos", 2), ("bolsas", 88),("bolsas", 1000),("bolsas", 150),("y", 6),("alimento", 4)])
        self.assertDictEqual(res, {'y': (4,6),'x': (0,2),'correas': (3,3), 'huesos': (2, 10), 'alimento': (4,4), 'bolsas': (88,1000)})

    def test_stock_vacio(self):
        res = stock_productos([])
        self.assertDictEqual(res, {})

    def test_un_elem(self):
        res = stock_productos([("correas", 3)])
        self.assertDictEqual(res, {'correas': (3, 3)})

    def test_actualizacion_stock_un_producto_minimo_ultimo_maximo_medio(self):
        res = stock_productos([("huesos", 5), ("huesos", 10), ("huesos", 0)])
        self.assertDictEqual(res, {'huesos': (0, 10)})

    def test_actualizacion_stock_un_producto_minimo_primero_maximo_ultimo(self):
        res = stock_productos([("huesos", 0), ("huesos", 7), ("huesos", 10)])
        self.assertDictEqual(res, {'huesos': (0, 10)})

    def test_cantidad_menor_o_igual_a_existente(self):
        res = stock_productos([("correas", 3), ("correas", 2)])
        self.assertDictEqual(res, {'correas': (2, 3)})

    def test_cantidad_mayor_a_existente(self):
        res = stock_productos([("correas", 3), ("correas", 5)])
        self.assertDictEqual(res, {'correas': (3, 5)})

    def test_todo_cero(self):
        res = stock_productos([("correas", 0), ("huesos", 0), ("bolsas", 0)])
        self.assertDictEqual(res, {'correas': (0, 0), 'huesos': (0, 0), 'bolsas': (0, 0) })


if __name__ == '__main__':
    unittest.main(verbosity=2)
