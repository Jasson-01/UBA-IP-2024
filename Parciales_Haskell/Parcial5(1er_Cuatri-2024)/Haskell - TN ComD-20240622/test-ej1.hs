import Test.HUnit
import Solucion

main = runTestTT tests

tests = test [
    -- Ejercicio 1
    "Divisores Propios" ~: (divisoresPropios 1) ~?= [],
    "Divisores Propios" ~: (divisoresPropios 357) ~?= [1,3,7,17,21,51,119],
    "Divisores Propios" ~: (divisoresPropios 66921) ~?= [1,3,22307]
    ]

