import unittest
from solucion import subsecuencia_mas_larga

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertDictEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej1Test():
    def __init__(self, *args, **kwargs):
        super(Ej1Test, self).__init__(*args, **kwargs)
        self.method = subsecuencia_mas_larga

    def test_caso_base_neg(self):
        entrada: list[int] = [-10]
        entrada_copia: list[int] = entrada[:]
        salida: tuple[int,int] = (1, 0)
        res = subsecuencia_mas_larga(entrada)        
        self.assertEqual(res, salida)
        self.assertEqual(entrada, entrada_copia)
        
    def test_caso_base_pos(self):
        entrada: list[int] = [10]
        entrada_copia: list[int] = entrada[:]
        salida: tuple[int,int] = (1, 0)
        res = subsecuencia_mas_larga(entrada)        
        self.assertEqual(res, salida)
        self.assertEqual(entrada, entrada_copia)
        
    def test_sube(self):
        entrada: list[int] = [1, 2, 3]
        entrada_copia: list[int] = [1, 2, 3]
        salida: tuple[int,int] = (3, 0)
        res = subsecuencia_mas_larga(entrada)        
        self.assertEqual(res, salida)
        self.assertEqual(entrada, entrada_copia)
        
    def test_baja(self):
        entrada: list[int] = [3, 2, 1]
        entrada_copia: list[int] = [3, 2, 1]
        salida: tuple[int,int] = (3, 0)
        res = subsecuencia_mas_larga(entrada)        
        self.assertEqual(res, salida)
        self.assertEqual(entrada, entrada_copia)
    
    def test_una_solucion_full(self):
        entrada:list[int] = [-2, -1, 0, 1, 0, -1, 0, 1, 2, 3]
        entrada_copia:list[tuple[str, str, int]] = entrada[:]
        salida = (10, 0)
        res = subsecuencia_mas_larga(entrada)        
        self.assertEqual(res, salida)
        self.assertEqual(entrada, entrada_copia)
        
    def test_una_solucion_chica_al_final(self):
        entrada:list[int] = [-2, 0, 2, -4, 1, 3, -1, 4, -1, 0]
        entrada_copia:list[tuple[str, str, int]] = entrada[:]
        salida = (2, 8)
        res = subsecuencia_mas_larga(entrada)        
        self.assertEqual(res, salida)
        self.assertEqual(entrada, entrada_copia)
    
    def test_empates(self):
        entrada:list[int] = [-10, 2,1,2,1, 1,2,1,2]
        entrada_copia:list[tuple[str, str, int]] = entrada[:]
        salida = (4, 1)
        res = subsecuencia_mas_larga(entrada)        
        self.assertEqual(res, salida)
        self.assertEqual(entrada, entrada_copia)
        
    def test_empates_y_chicos(self):
        entrada:list[int] = [0, 0, 0, 0]
        entrada_copia:list[tuple[str, str, int]] = entrada[:]
        salida = (1, 0)
        res = subsecuencia_mas_larga(entrada)        
        self.assertEqual(res, salida)
        self.assertEqual(entrada, entrada_copia)

if __name__ == '__main__':
    unittest.main(verbosity=2)
