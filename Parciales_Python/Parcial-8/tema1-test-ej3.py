import inspect
import unittest
from solucion import empleados_del_mes

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertCountEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej3Test(unittest.TestCase):

    is_default = False

    def __init__(self, *args, **kwargs):
        super(Ej3Test, self).__init__(*args, **kwargs)
        code = inspect.getsource(empleados_del_mes)
        if len(code.splitlines()) <= 2:
            Ej3Test.is_default = True

    def setUp(self):
        if Ej3Test.is_default:
            self.skipTest("el test no se ejecuto porque la implementacion de la funcion es la provista por la catedra a modo de ejemplo")

    def test_caso_base(self):
        horas = {1: [5, 6, 7], 2: [8, 9, 10], 3: [2, 3, 4]}
        esperado = [2]
        self.assertCountEqual(empleados_del_mes(horas), esperado)
    
    def test_varios_empleados_max(self):
        horas = {1: [5, 5, 5], 3: [5, 5, 5], 2: [2, 3, 4]}
        esperado = [1, 3]
        self.assertCountEqual(empleados_del_mes(horas), esperado)
    
    def test_todos_iguales(self):
        horas = {1: [3, 3, 3], 2: [3, 3, 3], 3: [3, 3, 3]}
        esperado = [1, 2, 3]
        self.assertCountEqual(empleados_del_mes(horas), esperado)

    def test_un_empleado(self):
        horas = {1: [8, 8, 8, 8]}
        esperado = [1]
        self.assertCountEqual(empleados_del_mes(horas), esperado)
    
    def test_empleado_sin_horas_max(self):
        horas = {1: [3, 3], 2: [3, 2, 1], 3: [6]}
        esperado = [1,2,3]
        self.assertCountEqual(empleados_del_mes(horas), esperado)
    
    def test_empleados_vacios(self):
        horas = {}
        esperado = []
        self.assertEqual(empleados_del_mes(horas), esperado)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)

