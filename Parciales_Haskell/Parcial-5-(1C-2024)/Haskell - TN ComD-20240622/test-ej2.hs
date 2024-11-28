import Test.HUnit
import Solucion

main = runTestTT tests

tests = test [
    -- Ejercicio 2
    "Son Amigos caso más chico" ~: (sonAmigos 2 1) ~?= False,
    "Son Amigos numeros grandes verdad" ~: (sonAmigos 18416 17296) ~?= True
    ]


