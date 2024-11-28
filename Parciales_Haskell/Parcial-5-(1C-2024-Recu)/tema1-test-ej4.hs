import Solucion_t1
import Test.HUnit
import Data.List

main = runTestTT allTests

allTests = test[
        "caso |camino| = 1 y esCaminoFibo t c i = true" ~: esCaminoFibo [1] 1 ~?= True,
        "caso |camino| = 1 y esCaminoFibo t c i = false" ~: esCaminoFibo [1] 7 ~?= False,
        "caso |camino| > 1 y esCaminoFibo t c i = false" ~: esCaminoFibo  [1,4] 3 ~?= False,
        "caso |camino| > 1 y esCaminoFibo t c i = true" ~: esCaminoFibo  [1,1,2,3,5] 1 ~?= True,
        "caso |camino| > 1 y esCaminoFibo t c i = false con otro camino" ~: esCaminoFibo [89,328,377] 10 ~?= False,
        "caso |camino| > 1 y esCaminoFibo t c i = true con otro camino" ~: esCaminoFibo [8, 13]  6 ~?= True
        ]
    