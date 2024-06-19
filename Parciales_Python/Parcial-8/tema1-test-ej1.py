import inspect
import unittest
from solucion import orden_de_atencion
from queue import Queue as Cola

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
        code = inspect.getsource(orden_de_atencion)
        if len(code.splitlines()) <= 2:
            Ej1Test.is_default = True

    def setUp(self):
        if Ej1Test.is_default:
            self.skipTest("el test no se ejecuto porque la implementacion de la funcion es la provista por la catedra a modo de ejemplo")

    def cola_from_list(lst):
        cola = Cola()
        for item in lst:
            cola.put(item)
        return cola

    def cola_to_list(cola):
        lst = []
        while not cola.empty():
            lst.append(cola.get())
        return lst

    def test_caso_base_1(self):
        urgentes = Ej1Test.cola_from_list([-1])
        postergables = Ej1Test.cola_from_list([1])
        esperado = Ej1Test.cola_from_list([-1, 1])
        self.assertEqual(Ej1Test.cola_to_list(orden_de_atencion(urgentes, postergables)), Ej1Test.cola_to_list(esperado))

    def test_caso_base_2(self):
        urgentes = Ej1Test.cola_from_list([1, -3])
        postergables = Ej1Test.cola_from_list([2, -4])
        esperado = Ej1Test.cola_from_list([1, 2, -3, -4])
        self.assertEqual(Ej1Test.cola_to_list(orden_de_atencion(urgentes, postergables)), Ej1Test.cola_to_list(esperado))

    def test_elementos_3(self):
        urgentes = Ej1Test.cola_from_list([7, -9, 11])
        postergables = Ej1Test.cola_from_list([8, -10, 12])
        esperado = Ej1Test.cola_from_list([7, 8, -9, -10, 11, 12])
        self.assertEqual(Ej1Test.cola_to_list(orden_de_atencion(urgentes, postergables)), Ej1Test.cola_to_list(esperado))
      
    def test_vacio(self):
        urgentes = Ej1Test.cola_from_list([])
        postergables = Ej1Test.cola_from_list([])
        esperado = Ej1Test.cola_from_list([])
        self.assertEqual(Ej1Test.cola_to_list(orden_de_atencion(urgentes, postergables)), Ej1Test.cola_to_list(esperado))
        
if __name__ == '__main__':
    unittest.main(verbosity=2)



   
