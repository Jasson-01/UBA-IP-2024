import Test.HUnit
import Solucion

main = runTestTT tests

tests = test [
    -- Ejercicio 4
    "Lista de Amigos vacia" ~: (listaDeAmigos []) == [] ~?= True,
    "Lista de Amigos sin Amigos varios elementos" ~: sonIgualesTestEj4 (listaDeAmigos sinAmigosTestEj4) [] ~?= True,
    "Lista de Amigos sin Amigos un solo elemento" ~: sonIgualesTestEj4 (listaDeAmigos sinAmigosTestEj4_1) [] ~?= True,
    "Lista de Amigos 220 284 principio y fin" ~: sonIgualesTestEj4 (listaDeAmigos unAmigo_220_284_finTestEj4) [(220, 284)] ~?= True,
    "Lista de Amigos 284 220 unicos" ~: sonIgualesTestEj4 (listaDeAmigos unAmigo_220_284TestEj4)  [(220, 284)] ~?= True,
    "Lista de Amigos amigos (63020, 76084)" ~:  sonIgualesTestEj4 (listaDeAmigos unAmigo_63020_76084TestEj4) [(63020, 76084)] ~?= True,
    "Lista de Amigos amigos (66928, 66992),(6232, 6368)" ~: sonIgualesTestEj4 (listaDeAmigos dosAmigosTestEj4) [(6232, 6368),(66928,66992)] ~?= True
    ]
    
-- Formulas
sonIgualesTestEj4 :: (Eq t) => [(t,t)] -> [(t,t)]-> Bool
sonIgualesTestEj4 lista1 lista2 = (laPrimeraEstaEnLaSegundaTestEj4TestEj4 lista1 lista2) && (laPrimeraEstaEnLaSegundaTestEj4TestEj4 lista2 lista1)


laPrimeraEstaEnLaSegundaTestEj4TestEj4 :: (Eq t) => [(t,t)]->[(t,t)] -> Bool
laPrimeraEstaEnLaSegundaTestEj4TestEj4 [] _ = True
laPrimeraEstaEnLaSegundaTestEj4TestEj4 (t1:tuplas1) tuplas2 = perteneceTuplaTestEj4 t1 tuplas2 && laPrimeraEstaEnLaSegundaTestEj4TestEj4 tuplas1 tuplas2
                         
perteneceTuplaTestEj4 ::(Eq t) => (t,t)->[(t,t)] -> Bool
perteneceTuplaTestEj4 _ [] = False
perteneceTuplaTestEj4 t1 (t2:elResto) = tuplasIgualesTestEj4 t1 t2 || (perteneceTuplaTestEj4 t1 elResto)

tuplasIgualesTestEj4 :: (Eq t) => (t,t)->(t,t) -> Bool
tuplasIgualesTestEj4 (a,b) (c,d) = (a == c && b == d) || (a == d && b == c)

-- Listas
sinAmigosTestEj4 = [220, 6, 5, 11, 5020]
sinAmigosTestEj4_1 = [5020]
unAmigo_220_284_finTestEj4 = [220, 6, 5, 11, 284]
unAmigo_220_284TestEj4 = [284, 220]
unAmigo_63020_76084TestEj4 = [6, 18416, 63021, 63020,  5, 220, 76084, 11]
dosAmigosTestEj4 = [220, 6, 11, 66992, 6368, 66928, 1184, 6232]
