import Solucion_t2
import Test.HUnit
import Data.List

main = runTestTT allTests

allTests = test[
        "caso |camino| > 1" ~: valoresDeCamino [[13,12,6,4],[1,1,32,25],[9,2,14,7],[7,3,5,16],[27,2,8,18]] [(2,1),(2,2),(3,2),(4,2),(4,3)] ~?= [1,1,2,3,5],
        "caso |camino| = 0" ~: valoresDeCamino [[13,12,6,4],[1,1,32,25],[9,2,14,7],[7,3,5,16],[27,2,8,18]] [] ~?= [],
        "caso |camino| = 1" ~: valoresDeCamino [[13,12,6,4],[1,1,32,25],[9,2,14,7],[7,3,5,16],[27,2,8,18]] [(2,1)] ~?= [1],
        "caso otro camino"  ~: valoresDeCamino [[1,2,3],[4,5,6],[7,8,9]] [(1,1),(2,1),(3,1),(3,2),(3,3)] ~?= [1,4,7,8,9],
        "caso |tablero| = 1" ~: valoresDeCamino [[1]] [(1,1)] ~?= [1],
        "caso camino horizontal" ~: valoresDeCamino [[1,2,3],[4,5,6],[7,8,9]] [(2,1),(2,2),(2,3)] ~?= [4,5,6],
        "caso camino vertical" ~: valoresDeCamino [[1,2,1,70],[43,10,5,67],[27,38,99,607],[27,38,99,607]] [(1,1),(2,1),(3,1),(4,1)] ~?= [1, 43, 27, 27]
    ]
