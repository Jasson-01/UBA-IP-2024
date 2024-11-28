import Solucion_t2
import Test.HUnit
import Data.List

main = runTestTT allTests

allTests =  test[
    "Tablero 1 x 1" ~: minimo [[10]] ~?= 10,
    "Tablero con todas las entradas distintas y minimo al inicio" ~: minimo [[1,2,3], [4,5,6]] ~?= 1,
    "Tablero con todas las entradas iguales" ~: minimo [[2,2], [2,2]] ~?= 2,
    "Tablero con el minimo en el medio" ~: minimo [[100, 10, 678], [6, 35, 43],[10, 89, 106]] ~?= 6,
    "Tablero con el minimo  al final" ~: minimo [[198, 10, 100], [100, 150, 11],[10, 3, 1]] ~?= 1
    ]
