import Test.HUnit
import Solucion

main = runTestTT tests

tests = test [
    "hayQueCodificar ListaVacia"  ~: hayQueCodificar 'a' [] ~?= False,
    "hayQueCodificar False mapeo 1 elem" ~: hayQueCodificar 'a' [('b','f')] ~?= False,
    "hayQueCodificar True mapeo 1 elem" ~: hayQueCodificar 'b' [('b','f')] ~?= True,
    "hayQueCodificar False xq está en 2da comp" ~: hayQueCodificar 'z' [('b','f'),('o','n'),('e','z')] ~?= False,
    "hayQueCodificar False mapeo muchos elem" ~: hayQueCodificar 'z' [('b','f'),('o','n'),('e','z')]~?= False,
    "hayQueCodificar True mapeo igual" ~: hayQueCodificar 'e' [('b','f'),('o','n'),('e','e')]~?= True,
    "hayQueCodificar True está en última pos" ~: hayQueCodificar 'e' [('b','f'),('o','n'),('e','z')]~?= True,
    "hayQueCodificar True está en el medio" ~: hayQueCodificar 'o' [('e','f'),('o','n'),('x','z')]~?= True,
    "hayQueCodificar True está en primera pos" ~: hayQueCodificar 'e' [('e','f'),('o','n'),('x','z')]~?= True
    ]
