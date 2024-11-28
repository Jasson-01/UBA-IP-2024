import Solucion
import Test.HUnit

main = runTestTT allTests

allTests = test[
    "maxMovilN ultimo" ~: maxMovilN [9, 3, 2, 5, 7, 8] 1 ~?=8,
    "maxMovilN casi todos" ~: maxMovilN [1, 8, 3, 4, 6] 4 ~?=8,
    "maxMovilN lista con max al principio" ~: maxMovilN [2, 6, 9, 7, 8] 3 ~?=9,
    "maxMovilN n=|l|-1 y al final" ~: maxMovilN [8, 3, 4, 6] 3 ~?=6,
    "maxMovilN todos iguales" ~: maxMovilN [0,0,0,0] 3 ~?= 0,
    "maxMovilN lista de 2 elementos" ~: maxMovilN [3,1] 1 ~?=1,    
    "maxMovilN lista larga, max al principio" ~: maxMovilN [2, 61, 9, 7, 8, 60, 9, 7, 8] 8 ~?=61,
    "maxMovilN lista larga, max al final" ~: maxMovilN [2, 6, 9, 7, 81, 6, 9, 7, 82] 8 ~?=82,
    "maxMovilN lista larga, max en el medio" ~: maxMovilN [2, 6, 9, 7, 80, 6, 9, 7, 8] 8 ~?=80,
    "maxMovilN lista larga, max en el medio repetido" ~: maxMovilN [82, 6, 9, 7, 82, 6, 9, 7, 82] 3 ~?=82
    ]