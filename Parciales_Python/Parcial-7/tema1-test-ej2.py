import inspect
import unittest
from solucion import filtrar_codigos_primos

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
        code = inspect.getsource(filtrar_codigos_primos)
        if len(code.splitlines()) <= 2:
            Ej2Test.is_default = True
        
    def setUp(self):
        if Ej2Test.is_default:
            self.skipTest("el test no se ejecuto porque la implementacion de la funcion es la provista por la catedra a modo de ejemplo")

    def test_el_mezcladito(self): 
        res = filtrar_codigos_primos([999,9999,999999,999999101,123456, 9007,  789012,189101, 345678, 1017, 101, 666, 11006])
        self.assertSetEqual(set(res), set([ 999999101, 101, 9007, 189101, 1017])) 

    def test_un_solo_codigo_que_es_primo(self): 
        res = filtrar_codigos_primos([9007])
        self.assertSetEqual(set(res), set([9007])) 

    def test_un_solo_codigo_no_primo(self): 
        res = filtrar_codigos_primos([90070])
        self.assertSetEqual(set(res), set([])) 

    def test_un_solo_primo_al_inicio(self): 
        res = filtrar_codigos_primos([9007, 6549879, 123654, 2220])
        self.assertSetEqual(set(res), set([9007])) 

    def test_un_solo_primo_al_final(self): 
        res = filtrar_codigos_primos([90072, 6549873, 123237, 2220, 101])
        self.assertSetEqual(set(res), set([101])) 

    def test_todos_primos(self): 
        res = filtrar_codigos_primos([9007, 107, 55555002, 654987978017, 654987978019])
        self.assertSetEqual(set(res), set([107, 55555002, 654987978017, 654987978019,9007])) 

    def test_primo_repe(self): 
        res = filtrar_codigos_primos([9107, 2107, 55555002107, 6549879780170, 6549879780192])
        self.assertSetEqual(set(res), set([2107, 55555002107,9107])) 

   
#print (filtrar_codigos_primos ( [189101, 45030, 9007]))
   #     resultado_esperado = [189101, 9007]  # 101 y 007 son primos
#print (filtrar_codigos_primos ( ))



if __name__ == '__main__':
    unittest.main(verbosity=2)
