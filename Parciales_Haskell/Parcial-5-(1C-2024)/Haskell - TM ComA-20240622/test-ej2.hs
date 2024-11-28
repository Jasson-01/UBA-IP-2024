import Test.HUnit
import Solucion

main = runTestTT tests

tests = test [
    -- Ejercicio 2
    "cuantasVecesHayQueCodificar mapeoVacio" ~: cuantasVecesHayQueCodificar 'm' frase_a_probar [] ~?= 0,
    "cuantasVecesHayQueCodificar 0 con mapeoUnElem" ~: cuantasVecesHayQueCodificar 'm' frase_a_probar [('c','k')] ~?= 0,
    "cuantasVecesHayQueCodificar 0 con mapeoVariosElem" ~: cuantasVecesHayQueCodificar 'm' frase_a_probar [('c','k'),('a','b'),('x','z')] ~?= 0,
    "cuantasVecesHayQueCodificar 1 con mapeoVariosElem" ~: cuantasVecesHayQueCodificar 'm' frase_a_probar [('m','n'),('z','a'),('b','j')] ~?= 1,
    "cuantasVecesHayQueCodificar 1 con mapeoVariosElemAlFinal" ~: cuantasVecesHayQueCodificar 'm' frase_a_probar [('b','n'),('z','a'),('m','j')] ~?= 1,
    "cuantasVecesHayQueCodificar 1 con mapeoConUnElemento" ~: cuantasVecesHayQueCodificar 'm' frase_a_probar [('m','n')] ~?= 1,
    "cuantasVecesHayQueCodificar fraseSoloConRepetidos" ~: cuantasVecesHayQueCodificar 'a' "aaa" [('a','r')] ~?= 3,
    "cuantasVecesHayQueCodificar >1 con mapeoUnElem" ~: cuantasVecesHayQueCodificar 'o' frase_a_probar [('o','r')] ~?= 2,
    "cuantasVecesHayQueCodificar >1 con mapeoVariosElem" ~: cuantasVecesHayQueCodificar 'o' frase_a_probar [('p','k'),('o','r')] ~?= 2
    ]

frase_a_probar = "hola mundo"
