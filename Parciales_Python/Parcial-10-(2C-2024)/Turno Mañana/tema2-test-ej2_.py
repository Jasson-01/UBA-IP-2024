import unittest
from queue import Queue as Cola
from solucion import mejor_resultado_de_ana

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertDictEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej2Test():
    def __init__(self, *args, **kwargs):
        super(Ej2Test, self).__init__(*args, **kwargs)
        self.method = mejor_resultado_de_ana

    def test_caso_base(self):
        entrada: Cola[tuple[str,int]] = Cola()
        entrada_copia : Cola[tuple[str,int]] = Cola()
        salida = []
        res: list[int] = mejor_resultado_de_ana(entrada)
        self.assertEqual(res, salida)
        # self.assertEqual(entrada.queue, entrada_copia.queue)
    
    def test_mitad_y_mitad_respuestas(self):
        e1 = [True, False]
        e2 = [False, True]
        e3 = [True, True, False, False]
        e4 = [True, False, True, False]
        e5 = [True, False, False, True]
        e6 = [False, True, True, False]
        e7 = [False, True, False, True]
        e8 = [False, False, True, True]
        entrada: Cola[tuple[str,int]] = crear_cola([e1, e2, e3, e4, e5, e6, e7, e8])
        entrada_copia : Cola[tuple[str,int]] = copiar_cola(entrada)
        salida = [2, 2, 4, 4, 4, 4, 4, 4]
        res: list[int] = mejor_resultado_de_ana(entrada)
        self.assertEqual(res, salida)
        # self.assertEqual(entrada.queue, entrada_copia.queue)
        
    def test_todos_iguales_respuestas(self):
        e1 = [True, True]
        e2 = [False, False]
        e3 = [True, True, True, True]
        e4 = [False, False, False, False]
        entrada: Cola[tuple[str,int]] = crear_cola([e1, e2, e3, e4])
        entrada_copia : Cola[tuple[str,int]] = copiar_cola(entrada)
        salida = [1, 1, 2, 2]
        res: list[int] = mejor_resultado_de_ana(entrada)
        self.assertEqual(res, salida)
        # self.assertEqual(entrada.queue, entrada_copia.queue)
    
    def test_mas_verdaderos_que_falsos(self):
        e1 = [True, True, True, False]
        e2 = [True, True, False, True]
        e3 = [True, False, True, True]
        e4 = [False, True, True, True]
        entrada: Cola[tuple[str,int]] = crear_cola([e1, e2, e3, e4])
        entrada_copia : Cola[tuple[str,int]] = copiar_cola(entrada)
        salida = [3, 3, 3, 3]
        res: list[int] = mejor_resultado_de_ana(entrada)
        self.assertEqual(res, salida)
        # self.assertEqual(entrada.queue, entrada_copia.queue)

    def test_mas_falsos_que_verdaderos(self):
        e1 = [False, False, False, True]
        e2 = [False, False, True, False]
        e3 = [False, True, False, False]
        e4 = [True, False, False, False]
        entrada: Cola[tuple[str,int]] = crear_cola([e1, e2, e3, e4])
        entrada_copia : Cola[tuple[str,int]] = copiar_cola(entrada)
        salida = [3, 3, 3, 3]
        res: list[int] = mejor_resultado_de_ana(entrada)
        self.assertEqual(res, salida)
        # self.assertEqual(entrada.queue, entrada_copia.queue)
        
    def test_no_rompe_la_cola(self):
        entrada: Cola[tuple[str,int]] = crear_cola([[True, True]])
        entrada_copia : Cola[tuple[str,int]] = copiar_cola(entrada)
        salida = [1]
        res: list[int] = mejor_resultado_de_ana(entrada)
        # self.assertEqual(res, salida)
        self.assertEqual(entrada.queue, entrada_copia.queue)

def crear_cola(elementos):
    cola = Cola()
    for elem in elementos:
        cola.put(elem)
    return cola
    
def copiar_cola(cola: Cola):
    elementos = list(cola.queue)
    nueva_cola = Cola()
    for e in elementos:
        nueva_cola.put(e)
    return nueva_cola

if __name__ == '__main__':
    unittest.main(verbosity=2)
