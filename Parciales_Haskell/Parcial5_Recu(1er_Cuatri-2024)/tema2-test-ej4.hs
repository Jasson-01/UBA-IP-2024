import Solucion_t2
import Test.HUnit
import Data.List

main = runTestTT allTests

allTests = test[
        "caso |secuencia|=1 y esCaminoCollatz s  i=1: true" ~: esCaminoCollatz [1] 1 ~?= True,
        "caso |secuencia|=1 y esCaminoCollatz s i!=1: false" ~: esCaminoCollatz [1] 5 ~?= False,
        "caso |secuencia|>1 y esCaminoCollatz s  i=1: false" ~: esCaminoCollatz [5,16,8,4,2,1] 1 ~?= False,
        "caso |secuencia|>1 y esCaminoCollatz s i>1: true" ~: esCaminoCollatz [16,8,4,2,1] 16 ~?= True, -- Caso similar al anterior pero diferente al que les dimos
        "caso |secuencia|>1 y esCaminoCollatz s i>1, false" ~: esCaminoCollatz [20, 10, 5,20] 20 ~?= False,
        "caso |secuencia|>1 comienza como CaminoCollatz pero no es, i=s[0]" ~: esCaminoCollatz [5,16,8,4,2,7] 5 ~?= False,
        "caso |secuencia|>1 comienza como CaminoCollatz pero no es, i!=s[0]" ~: esCaminoCollatz [5,16,8,4,2,1] 2 ~?= False
        ]
    
