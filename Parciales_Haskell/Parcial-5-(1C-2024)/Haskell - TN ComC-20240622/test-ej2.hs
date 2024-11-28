import Test.HUnit
import Solucion

main = runTestTT tests

tests = test [
--aproboMasDeNMaterias

--buenosAlumnos
    --registro4 = [("nombre4", [0,1,2,3, 4])]
    "ba 01" ~: (buenosAlumnos  registro4 ) ~?= [],
    --registro3 = [("nombre3", [0,1,2,3])]
    "ba 02" ~: (buenosAlumnos  registro3) ~?= [],
    --registro5 = [("Juan", [8])]
    "ba 03" ~: (buenosAlumnos  registro5) ~?= ["Juan"],
    --registro6 = [("Juan", [8]), ("Pepe", [8, 9, 10])]
    "ba 04" ~: sonIguales_hunit (buenosAlumnos  registro6)  ["Juan", "Pepe"] ~?= True,
    --registro7 = [("nombre1", [0,1,2,3,4,5,6,7,8,9,10]), ("nombre3", [0,1,2,3]), ("nombre4", [0,1,2,3, 4]), 
        --("Juan", [8]), ("Pepe", [8, 9, 10]), ("nombre2", [0,1,2,3,4,5,6,7,8,9,10])]
    "ba 05" ~: sonIguales_hunit (buenosAlumnos  registro7) ( ["Pepe", "Juan"]) ~?= True, 
    --registro15 = [ ("Carla", [1, 3, 4,3]), ("Emma", [10, 10, 10,3]), ("JP", [10, 3, 4,3])
    "ba 06" ~: (buenosAlumnos  registro15) ~?= [],
    --registro17 = [("Emma", [10, 10, 10,4]), ("Carla", [1, 3, 4,3]), ("JP", [10, 3, 4,3]), ("VP", [8, 8, 8,7]), ("Ju", [8, 8, 8,8])  ]
    "ba 07" ~: sonIguales_hunit (buenosAlumnos  registro17) ( ["Ju", "Emma"])  ~?= True,
    --registro1 = [("Lu", [0]), ("La", [0]), ("Ve", [3,10,10,10])]
    "ba 08" ~: (buenosAlumnos  registro1 ) ~?= [],
    "ba 09" ~: sonIguales_hunit (buenosAlumnos  [("Lu", [10]), ("La", [0]), ("Ve", [10,10, 10])])  ( ["Lu", "Ve"]) ~?= True, 
    "ba 10" ~: sonIguales_hunit (buenosAlumnos  [("Lu", [0]), ("La", [0, 0]), ("Ve", [0,0,0])])  ( []) ~?= True

--mejorPromedio

    ]

--aproboMasDeNMaterias [("juan" , [1,2,3]), ("pe" , [4,1,2,3])] "pe" 3


--Formulas


--Listas
registro1 = [("Lu", [0]), ("La", [0]), ("Ve", [0,1,2,3,4,5,6,7,8,9,10])]
registro2 = [("Ve", [0,0, 0]), ("Lu", [0]), ("La", [0])]
registro3 = [("nombre3", [0,1,2,3])]
registro4 = [("nombre4", [0,1,2,3, 4])]
registro4a = [("Ana", [5,1,2,3, 4])]
notasAlum10 = ("Ju", [10, 10, 10])
registro5 = [("Juan", [8])]
registro6 = [("Juan", [8]), ("Pepe", [8, 9, 10])]
registro7 =  [("nombre1", [0,1,2,3,4,5,6,7,8,9,10]), ("nombre3", [0,1,2,3]), ("nombre4", [0,1,2,3, 4]), ("Juan", [8]), ("Pepe", [8, 9, 10]), ("nombre2", [0,1,2,3,4,5,6,7,8,9,10])]
registro8 = [("Carla", [10, 10, 4]), ("JP", [10, 3, 4]), ("VP", [8, 8, 8])]
registroSH = [("Carla", [10, 10, 2, 10]), ("JP", [8, 8, 7, 8]), ("VP", [8, 8, 8, 7])]
registroSH2 = [("Carla", [3, 10, 10, 10, 10, 10, 10]), ("JP", [8, 8, 8, 8, 8, 8]), ("VP", [8, 8, 8, 8, 8, 8])]
registro9 = [("nombre1", [0,1,2,3,4,5,6,7,8,9,10]), ("Sol", [9, 9, 10]), ("Ale", [9, 9, 10]), ("nombre4", [0,1,2,3, 4]), ("Juan", [8]), ("Pepe", [8, 9, 10])]
registro10 = [("Ale", [9, 9, 10]), ("Sol", [9, 9, 10]), ("nombre1", [0,1,2,3,4,5,6,7,8,9,10]), ("nombre4", [0,1,2,3, 4]), ("Juan", [8]), ("Pepe", [8, 9, 10])]
registro11 = [("Pepe", [8, 9, 10]), ("Ale", [9, 9, 10]), ("nombre1", [0,1,2,3,4,5,6,7,8,9,10]), ("nombre4", [0,1,2,3, 4]), ("Juan", [8])]
registro12 = [("Ale", [9, 9, 10]), ("Ja", [9, 9, 10]), ("Je", [8, 8, 9]), ("Ji", [8, 9, 9])]

registro15 = [ ("Carla", [1, 3, 4,3]), ("Emma", [10, 10, 10,3]), ("JP", [10, 3, 4,3]) ]
registro16 = [("Juan", [4, 1, 4, 4])]
registro17 = [("Emma", [10, 10, 10,4]), ("Carla", [1, 3, 4,3]), ("JP", [10, 3, 4,3]), ("VP", [8, 8, 8,7]), ("Ju", [8, 8, 8,8])  ]
registro18 = [("Carla", [1, 3, 4,3]), ("JP", [10, 3, 4,3]), ("VP", [8, 8, 8,7]), ("Ju", [8, 8, 8,8]),("Emma", [10, 10, 10,4])  ]




-- FUNCIONES PARA TESTING, NO BORRAR
-- expectAny permite saber si el elemento que devuelve la función es alguno de los esperados
expectAny actual expected = elem actual expected ~? ("expected any of: " ++ show expected ++ "\n but got: " ++ show actual)

sonIguales_hunit :: (Eq t) => [t] -> [t] -> Bool
sonIguales_hunit xs ys = incluido_hunit xs ys && incluido_hunit ys xs

quitar_hunit :: (Eq t) => t -> [t] -> [t]
quitar_hunit x (y:ys) | x == y = ys
                | otherwise = y : quitar_hunit x ys

incluido_hunit :: (Eq t) => [t] -> [t] -> Bool
incluido_hunit [] l = True
incluido_hunit (x:c) l = elem x l && incluido_hunit c (quitar_hunit x l)
