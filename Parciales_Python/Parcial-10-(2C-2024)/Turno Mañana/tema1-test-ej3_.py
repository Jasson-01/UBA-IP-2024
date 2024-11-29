import unittest
from solucion import cambiar_matriz

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertDictEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

def cumple_los_asegura(A_pre, A) -> bool:
    # mismas dimensiones
    if len(A_pre) != len(A):
        return False
    for i in range(len(A)):
        if len(A_pre[i]) != len(A[i]):
            return False
    # valores del 1 al n exactamente una vez
    n = len(A) * len(A[0])
    valores = set()
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] < 1 or A[i][j] > n:
                return False
            valores.add(A[i][j])
    if len(valores) != n:
        return False
    # numeros distintos entre A_pre y A
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A_pre[i][j] == A[i][j]:
                return False
    return True

class Ej1Test():
    def __init__(self, *args, **kwargs):
        super(Ej1Test, self).__init__(*args, **kwargs)
        self.method = cambiar_matriz
        
    def test_todas_las_matrices_de_2_por_2(self):
        for a in [1, 2, 3, 4]:
            for b in [1, 2, 3, 4]:
                if b == a: continue
                for c in [1, 2, 3, 4]:
                    if c == a or c == b: continue
                    d = 10 - a - b - c
                    entrada: list[list[int]] = [ [a, b], [c, d] ]
                    entrada_copia: list[list[int]] = [ [a, b], [c, d] ]
                    salida = cambiar_matriz(entrada)        
                    self.assertTrue( cumple_los_asegura(entrada_copia, entrada) )
                    # self.assertEqual( salida, None )
        
    def test_matriz_mas_filas_que_columnas(self):
        entrada: list[list[int]] = [ [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12] ]
        entrada_copia: list[list[int]] = [ [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12] ]
        salida = cambiar_matriz(entrada)        
        self.assertTrue( cumple_los_asegura(entrada_copia, entrada) )
        # self.assertEqual( salida, None )
    
    def test_matriz_mas_columnas_que_filas(self):
        entrada: list[list[int]] = [ [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15] ]
        entrada_copia: list[list[int]] = [ [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15] ]
        salida = cambiar_matriz(entrada)        
        self.assertTrue( cumple_los_asegura(entrada_copia, entrada) )
        # self.assertEqual( salida, None )
        
    def test_no_devuelven_nada(self):
        entrada: list[list[int]] = [ [1, 2], [3, 4] ]
        entrada_copia: list[list[int]] = [ [1, 2], [3, 4] ]
        salida = cambiar_matriz(entrada)        
        self.assertEqual( salida, None )
        

if __name__ == '__main__':
    unittest.main(verbosity=2)
