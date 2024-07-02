import Test.HUnit
import Solucion

main = runTestTT tests

tests = test [
--mejorPromedio
    "mp 01" ~: (mejorPromedio  registro17) ~?= "Emma",
    --registro18 = [("Carla", [1, 3, 4,3]), ("JP", [10, 3, 4,3]), ("VP", [8, 8, 8,7]), ("Ju", [8, 8, 8,8]),("Emma", [10, 10, 10,4])  ]
    "mp 02" ~: (mejorPromedio  registro18) ~?= "Emma",
    "mp 03" ~: (mejorPromedio  [("nombre3", [0,1,2,3])]) ~?= "nombre3",
    --registro7 = [("nombre1", [0,1,2,3,4,5,6,7,8,9,10]), ("nombre3", [0,1,2,3]), ("nombre4", [0,1,2,3, 4]), 
        --("Juan", [8]), ("Pepe", [8, 9, 10]), ("nombre2", [0,1,2,3,4,5,6,7,8,9,10])]
    "mp 04" ~: (mejorPromedio  registro7) ~?= "Pepe",
    --registro9 = [("nombre1", [0,1,2,3,4,5,6,7,8,9,10]), ("Sol", [9, 9, 10]), ("Ale", [9, 9, 10]), ("nombre4", [0,1,2,3, 4]), 
        --("Juan", [8]), ("Pepe", [8, 9, 10])]
    "mp 05" ~: (mejorPromedio  registro9) ~?= "Sol",
    --registro10 = [("Ale", [9, 9, 10]), ("Sol", [9, 9, 10]), ("nombre1", [0,1,2,3,4,5,6,7,8,9,10]), ("nombre4", [0,1,2,3, 4]),
        -- ("Juan", [8]), ("Pepe", [8, 9, 10])]
    "mp 06" ~: (mejorPromedio  registro10) ~?= "Ale",
    --registro11 = [("Pepe", [8, 9, 10]), ("Ale", [9, 9, 10]), ("nombre1", [0,1,2,3,4,5,6,7,8,9,10]), ("nombre4", [0,1,2,3, 4]),
        -- ("Juan", [8])]
    "mp 07" ~: (mejorPromedio  registro11) ~?= "Ale",
    "mp 08" ~: (mejorPromedio  [("Ale", [9, 9, 10]), ("Ja", [9, 10]), ("Je", [8, 8, 9]), ("Ji", [8, 9, 9])]) ~?= "Ja",
    "mp 09" ~: (mejorPromedio  [("Ale", [0, 0, 0]), ("Ja", [0, 0]), ("Je", [0])]) ~?= "Ale"

--seGraduoConHonores
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


