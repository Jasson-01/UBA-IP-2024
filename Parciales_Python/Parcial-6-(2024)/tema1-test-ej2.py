import inspect
import unittest
from queue import Queue as Cola
from solucionParcial6 import reordenar_cola_priorizando_vips

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
        code = inspect.getsource(reordenar_cola_priorizando_vips)
        if len(code.splitlines()) <= 2:
            Ej2Test.is_default = True

    def setUp(self):
        if Ej2Test.is_default:
            self.skipTest("el test no se ejecuto porque la implementacion de la funcion es la provista por la catedra a modo de ejemplo")

    def test_reordenar_cola_priorizando_vips_vacio(self):
        entrada = Cola()
        salida = Cola()
        res = reordenar_cola_priorizando_vips(entrada)
        self.assertEqual(entrada.queue, salida.queue)


    def test_reordenar_cola_priorizando_vips_un_vip(self):
        entrada = Cola()
        entrada.put(("a","vip")) 
        salida = "a"
        res = reordenar_cola_priorizando_vips(entrada)
        nombre = res.get()[0]
        self.assertEqual(nombre, salida)

    def test_reordenar_cola_priorizando_vips_un_comun(self):
        entrada = Cola()
        entrada.put(("a","comun")) 
        salida = "a"
        res = reordenar_cola_priorizando_vips(entrada)
        nombre = res.get()[0]
        self.assertEqual(nombre, salida)
        
                
    def test_reordenar_fila_dos_vip_medio(self):
      fila = Cola()
      fila.put(('Facu', 'comun'))
      fila.put(('Ana', 'vip'))
      fila.put(('Juli', 'vip'))
      fila.put(('Lucas', 'comun'))
      
      res = Cola()
      res.put('Ana')
      res.put('Juli')
      res.put('Facu')
      res.put('Lucas')
      
      self.assertEqual(reordenar_cola_priorizando_vips(fila).queue, res.queue)     


    def test_reordenar_fila_dos_vip_inicio_fin(self):
      fila = Cola()
      fila.put(('Facu', 'vip'))
      fila.put(('Ana', 'comun'))
      fila.put(('Juli', 'comun'))
      fila.put(('Lucas', 'vip'))
      
      res = Cola()
      res.put('Facu')
      res.put('Lucas')
      res.put('Ana')
      res.put('Juli')
      
      self.assertEqual(reordenar_cola_priorizando_vips(fila).queue, res.queue)     

    def test_reordenar_fila_dos_vip_inicio_medio(self):
      fila = Cola()
      fila.put(('Facu', 'vip'))
      fila.put(('Ana', 'comun'))
      fila.put(('Juli', 'vip'))
      fila.put(('Lucas', 'comun'))
      
      res = Cola()
      res.put('Facu')
      res.put('Juli')
      res.put('Ana')
      res.put('Lucas')
      
      self.assertEqual(reordenar_cola_priorizando_vips(fila).queue, res.queue)     

    def test_reordenar_fila_dos_vip_fin_medio(self):
      fila = Cola()
      fila.put(('Facu', 'comun'))
      fila.put(('Ana', 'vip'))
      fila.put(('Juli', 'comienza'))
      fila.put(('Lucas', 'vip'))
      
      res = Cola()
      res.put('Ana')
      res.put('Lucas')
      res.put('Facu')
      res.put('Juli')
      
      self.assertEqual(reordenar_cola_priorizando_vips(fila).queue, res.queue)     


if __name__ == '__main__':
    unittest.main(verbosity=2)



   





    
