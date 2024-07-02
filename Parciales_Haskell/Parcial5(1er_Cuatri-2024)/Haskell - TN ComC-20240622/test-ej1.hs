import Test.HUnit
import Solucion

main = runTestTT tests


tests = test [
--aproboMasDeNMaterias
    --registro15 = [ ("Carla", [1, 3, 4,3]), ("Emma", [10, 10, 10,3]), ("JP", [10, 3, 4,3])
    "amdnm 01" ~: (aproboMasDeNMaterias  registro15 "Emma" 2) ~?= True,
    "amdnm 02" ~: (aproboMasDeNMaterias  registro15 "Emma" 3) ~?= False,
    "amdnm 03" ~: (aproboMasDeNMaterias  registro15 "JP" 1) ~?= True,
    "amdnm 04" ~: (aproboMasDeNMaterias  registro15 "JP" 2) ~?= False,
    "amdnm 05" ~: (aproboMasDeNMaterias  registro15 "Carla" 1) ~?= False,
    "amdnm 06" ~: (aproboMasDeNMaterias  registro15 "JP" 6) ~?= False,
    --registro18 = [("Carla", [1, 3, 4,3]), ("JP", [10, 3, 4,3]), ("VP", [8, 8, 8,7]), ("Ju", [8, 8, 8,8]),("Emma", [10, 10, 10,4])  ]
    "amdnm 07" ~: (aproboMasDeNMaterias  registro18 "JP" 1) ~?= True,
    "amdnm 08" ~: (aproboMasDeNMaterias  registro18 "VP" 3) ~?= True,
    "amdnm 09" ~: (aproboMasDeNMaterias  registro18 "Emma" 3) ~?= True,
    --registro3 = [("nombre3", [0,1,2,3])]
    "amdnm 10" ~: (aproboMasDeNMaterias  registro3 "nombre3" 1) ~?= False,
    --registro4 = [("nombre4", [0,1,2,3, 4])]
    "amdnm 11" ~: (aproboMasDeNMaterias  registro4 "nombre4" 1) ~?= False,
    --registro4a = [("Ana", [5,1,2,3, 4])]
    "amdnm 12" ~: (aproboMasDeNMaterias  registro4a "Ana" 1) ~?= True,
    "amdnm 13" ~: (aproboMasDeNMaterias  registro4a "Ana" 2) ~?= False,
    --registro1 = [("Lu", [0]), ("La", [0]), ("Ve", [0,1,2,3,4,5,6,7,8,9,10])]
    "amdnm 14" ~: (aproboMasDeNMaterias  registro1 "La" 1) ~?= False,
    "amdnm 15" ~: (aproboMasDeNMaterias  registro1 "Ve" 6) ~?= True,
    --registro2 = [("Ve", [0,0, 0]), ("Lu", [0]), ("La", [0])]
    "amdnm 16" ~: (aproboMasDeNMaterias  registro2 "Lu" 1) ~?= False,
    "amdnm 17" ~: (aproboMasDeNMaterias  [("Ve", [10,10, 10]), ("Lu", [10]), ("La", [0])] "Lu" 1) ~?= False,
    "amdnm 18" ~: (aproboMasDeNMaterias  [("Lu", [10]), ("La", [0]), ("Ve", [10,10, 10])] "Ve" 2) ~?= True
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

