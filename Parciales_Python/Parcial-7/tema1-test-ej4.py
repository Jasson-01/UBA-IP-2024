import inspect
import unittest
from solucion import un_responsable_por_turno

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej4Test(unittest.TestCase):
    
    is_default = False

    def __init__(self, *args, **kwargs):
        super(Ej4Test, self).__init__(*args, **kwargs)
        code = inspect.getsource(un_responsable_por_turno)
        if len(code.splitlines()) <= 2:
            Ej4Test.is_default = True
        
    def setUp(self):
        if Ej4Test.is_default:
            self.skipTest("el test no se ejecuto porque la implementacion de la funcion es la provista por la catedra a modo de ejemplo")

    def test_el_mezcladito(self): 
        turnos = [
            ["Ana", "Ana", "Sol", "Ana", "Sol", "Sol"],    # 9-10
            ["Ana", "aNa", "Sol", "Ana", "Ana", "Ana"],    # 10-11
            ["Ana", "Ana", "Sol", "Sol", "Ana", "Ana"],    # 11-12
            ["Ana", "Ana", "Sol", "Sol", "Ana", "Ana"],    # 12-13
            ["Luis", "Luis", "Luis", "Luis", "Luis", "Sol"],    # 14-15
            ["Luis", "Sol", "Luis", "Luis", "Luis", "Sol"],    # 15-16
            ["Luis", "Luis", "Luis", "Luis", "Sol", "Sol"],    # 16-17
            ["Luis", "Sol", "Luis", "Ana", "Luis", "Sol"]     # 17-18
        ]

        esperado = [
            (True, True),    # Lunes
            (False, False),  # Martes
            (True, True),    # Miércoles
            (False, False),  # Jueves
            (False, False),  # Viernes
            (False, True)    # Sábado
        ]

        res = un_responsable_por_turno(turnos)
        self.assertEqual(res, esperado) 



    def test_todo_true(self): 
        turnos = [
            ["Ana", "x", "Sol", "Ana", "Sol", "Ana"],    # 9-10
            ["Ana", "x", "Sol", "Ana", "Sol", "Ana"],    # 10-11
            ["Ana", "x", "Sol", "Ana", "Sol", "Ana"],    # 11-12
            ["Ana", "x", "Sol", "Ana", "Sol", "Ana"],    # 12-13
            ["Luis", "e", "Luis", "AnaAnaAnaAnaAna", "Luis", "Sol"],    # 14-15
            ["Luis", "e", "Luis", "AnaAnaAnaAnaAna", "Luis", "Sol"],    # 15-16
            ["Luis", "e", "Luis", "AnaAnaAnaAnaAna", "Luis", "Sol"],    # 16-17
            ["Luis", "e", "Luis", "AnaAnaAnaAnaAna", "Luis", "Sol"]     # 17-18
        ]

        esperado = [
            (True, True),    # Lunes
            (True, True),  # Martes
            (True, True),    # Miércoles
            (True, True),  # Jueves
            (True, True),  # Viernes
            (True, True)    # Sábado
        ]

        res = un_responsable_por_turno(turnos)
        self.assertEqual(res, esperado) 

    def test_todo_false(self): 
        turnos = [
            ["Anaa", "x", "Sol", "Ana", "aSol", "Ana"],    # 9-10
            ["Ana", "xa", "Sol", "Ana", "Sol", "Anaa"],    # 10-11
            ["Ana", "x", "Sola", "Ana", "Sol", "Ana"],    # 11-12
            ["Ana", "x", "Sol", "Anaa", "Sol", "Ana"],    # 12-13
            ["aLuis", "e", "Luis", "AnaAnaAnaAnaAna", "1Luis", "Sol"],    # 14-15
            ["Luis", "ae", "Luis", "AnaAnaAnaAnaAna", "Luis", "Sol2"],    # 15-16
            ["Luis", "e", "aLuis", "AnaAnaAnaAnaAna", "Luis", "Sol"],    # 16-17
            ["Luis", "e", "Luis", "AnaAnaAnaAnaAnaa", "Luis", "Sol"]     # 17-18
        ]

        esperado = [
            (False, False),    # Lunes
            (False, False),  # Martes
            (False, False),    # Miércoles
            (False, False),  # Jueves
            (False, False),  # Viernes
            (False, False)    # Sábado
        ]

        res = un_responsable_por_turno(turnos)
        self.assertEqual(res, esperado) 


    def test_7_dias(self): 
        turnos = [
            ["Ana", "Ana", "Sol", "Ana", "Sol", "Sol", "dom"],    # 9-10
            ["Ana", "aNa", "Sol", "Ana", "Ana", "Ana", "dom"],    # 10-11
            ["Ana", "Ana", "Sol", "Sol", "Ana", "Ana", "dom"],    # 11-12
            ["Ana", "Ana", "Sol", "Sol", "Ana", "Ana", "dom"],    # 12-13
            ["Luis", "Luis", "Luis", "Luis", "Luis", "Sol", "dom"],    # 14-15
            ["Luis", "Sol", "Luis", "Luis", "Luis", "Sol", "Sol"],    # 15-16
            ["Luis", "Luis", "Luis", "Luis", "Sol", "Sol", "Sol"],    # 16-17
            ["Luis", "Sol", "Luis", "Ana", "Luis", "Sol", "Sol"]     # 17-18
        ]

        esperado = [
            (True, True),    # Lunes
            (False, False),  # Martes
            (True, True),    # Miércoles
            (False, False),  # Jueves
            (False, False),  # Viernes
            (False, True),    # Sábado
            (True, False)    # dom
        ]

        res = un_responsable_por_turno(turnos)
        self.assertEqual(res, esperado) 

    def test_1_dia(self): 
        turnos = [
            ["Ana"],    # 9-10
            ["Ana"],    # 10-11
            ["Ana"],    # 11-12
            ["Ana"],   # 12-13
            ["Lui"],    # 14-15
            ["Luis"],    # 15-16
            ["Luis"],    # 16-17
            ["Luis"]     # 17-18
        ]

        esperado = [
            (True, False),    # Lunes
        ]

        res = un_responsable_por_turno(turnos)
        self.assertEqual(res, esperado) 


    def test_3_dias(self): 
        turnos = [
            ["Ana",     "no", "duerme"],    # 9-10
            ["espera",  "el", "dia"],    # 10-11
            ["sola",    "en", "su"],    # 11-12
            ["cuarto",  "Ana", "quiere"],   # 12-13
            ["jugar",   "Ana", "pepe"],    # 14-15
            ["jugar",   "Ana", "pepe"],    # 15-16
            ["jugar",   "Ana", "pepe"],    # 16-17
            ["Sol"  ,   "Ana", "pepe"]     # 17-18
        ]

        esperado = [
            (False, False),    # Lunes
            (False, True),    # mar
            (False, True)    # mie
        ]

        res = un_responsable_por_turno(turnos)
        self.assertEqual(res, esperado) 


if __name__ == '__main__':
    unittest.main(verbosity=2)

