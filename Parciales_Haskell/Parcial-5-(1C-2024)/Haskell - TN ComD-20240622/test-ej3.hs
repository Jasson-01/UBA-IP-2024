import Test.HUnit
import Solucion

main = runTestTT tests

tests = test [
    -- Ejercicio 3
    "Los Primeros 1 Perfectos y vacio" ~: sonIgualesTestEj3 (losPrimerosNPerfectos 1) []~?= False,
    "Los Primeros 1 Perfectos y 1" ~: sonIgualesTestEj3 (losPrimerosNPerfectos 1) [1]~?= False,
    "Los Primeros 2 Perfectos Mal" ~: sonIgualesTestEj3 (losPrimerosNPerfectos 1) [6] ~?= True,
    "Los Primeros 4 Perfectos Bien" ~: sonIgualesTestEj3 (losPrimerosNPerfectos 4) [6, 28, 496, 8128] ~?= True
    ]

-- Formulas
sonIgualesTestEj3 :: (Eq t) => [t]->[t]-> Bool
sonIgualesTestEj3 lista1 lista2 = (estaEnTestEj3 lista1 lista2) && (estaEnTestEj3 lista2 lista1)

estaEnTestEj3 :: (Eq t) => [t]->[t]-> Bool
estaEnTestEj3 [] _ = True
estaEnTestEj3 (e:elResto1) elResto2 = perteneceTestEj3 e elResto2 && estaEnTestEj3 elResto1 elResto2
                         
perteneceTestEj3 ::(Eq t) => t -> [t] -> Bool
perteneceTestEj3 _ [] = False
perteneceTestEj3 t1 (t2:elResto) = t1 == t2 || (perteneceTestEj3 t1 elResto)

