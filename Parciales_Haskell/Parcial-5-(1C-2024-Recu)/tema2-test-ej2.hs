import Solucion_t2
import Test.HUnit
import Data.List

main = runTestTT allTests

allTests = test[
    "Tablero 1 x 1" ~: repetidos [[10]] ~?= [],
    "Un elemento con > 2 repetidos" ~: repetidos [[1,2,3], [4,1,1], [1, 10,1]] ~?= [1],
    "Tablero con = 2 repetidos" ~: repetidos [[3,78], [57,3]] ~?= [3],
    "Tablero con todos numeros distintos" ~: repetidos [[10,9,8,7], [6,5,4,3], [2,1,11,12]] ~?= [],
    "Tablero con dos numeros mas repetidos" ~: expectAny (repetidos [[11,23,73,104], [11,20,39,40], [1,2,73,4], [11, 31, 7,9]]) [[11, 73], [73, 11]]
    ]

-- expectAny permite saber si el elemenot que devuelve la función es alguno de los esperados
expectAny actual expected = elem actual expected ~? ("expected any of: " ++ show expected ++ "\n but got: " ++ show actual)
    
