import Test.HUnit
import Solucion

main = runTestTT tests

tests = test [
    "codificarFrase fraseLarga mapeoVacio" ~: codificarFrase frase6 [] ~?= frase6,
    "codificarFrase fraseLarga nadaMapeable" ~: codificarFrase frase6 [('z','p'), ('x','q')] ~?= frase6,
    "codificarFrase fraseLarga mapeaEspacios" ~: codificarFrase frase6 [(' ','*'), ('x','q')] ~?= "un*gran*poder*blabla",
    "codificarFrase fraseMuyCorta unMapeo" ~: codificarFrase "a" [('a','g')] ~?= "g",
    "codificarFrase fraseUnChar unMapeo" ~: codificarFrase "aaaa" [('a','g')] ~?= "gggg",
    "codificarFrase todoSeMapea" ~: codificarFrase "caba" [('a','g'),('c','d'),('b','x'),('z','y')] ~?= "dgxg",
    "codificarFrase soloMapeoUltimaLetra" ~: codificarFrase "el bebes" [('s','z')] ~?= "el bebez",
    "codificarFrase soloMapeoPrimeraLetra" ~: codificarFrase "sel bebe" [('s','z')] ~?= "zel bebe"
    ]


frase6 = "un gran poder blabla"
