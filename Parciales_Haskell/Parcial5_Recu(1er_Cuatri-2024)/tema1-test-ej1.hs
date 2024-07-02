import Solucion_t1
import Test.HUnit
import Data.List

main = runTestTT allTests

allTests = test[
    "Tablero 1 x 1" ~: maximo [[10]] ~?= 10,
    "Tablero con todas las entradas distintas" ~: maximo [[1,2,3], [4,5,6]] ~?= 6,
    "Tablero con todas las entradas iguales" ~: maximo [[2,2], [2,2]] ~?= 2,
    "Tablero con el maximo al inicio" ~: maximo [[100, 10, 1], [2, 3, 4],[10, 3, 6]] ~?= 100,
    "Tablero con el maximo en el medio" ~: maximo [[1, 10, 100], [100, 150, 1],[10, 3, 100]] ~?= 150
    ]