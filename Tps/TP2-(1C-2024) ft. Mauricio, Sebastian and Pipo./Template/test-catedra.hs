import Test.HUnit
import Solucion
import Data.List
-- No está permitido agregar nuevos imports.
runCatedraTests = runTestTT allTests

allTests = test [
    "esMinuscula" ~: testsEjesMinuscula,
    "letraANatural" ~: testsEjletraANatural,
    "desplazar" ~: testsEjdesplazar,
    "cifrar" ~: testsEjcifrar,
    "descifrar" ~: testsEjdescifrar,
    "cifrarLista" ~: testsEjcifrarLista,
    "frecuencia" ~: testsEjfrecuencia,
    "cifradoMasFrecuente" ~: testsEjcifradoMasFrecuente,
    "esDescifrado" ~: testsEjesDescifrado,
    "todosLosDescifrados" ~: testsEjtodosLosDescifrados,
    "expandirClave" ~: testsEjexpandirClave,
    "cifrarVigenere" ~: testsEjcifrarVigenere,
    "descifrarVigenere" ~: testsEjdescifrarVigenere,
    "peorCifrado" ~: testsEjpeorCifrado,
    "combinacionesVigenere" ~: testsEjcombinacionesVigenere
    ]

testsEjesMinuscula = test [
    "Letra miniscula" ~: esMinuscula 'd' ~?= True,
    "Ultima letra miniscula" ~: esMinuscula 'z' ~?= True,
    "Letra no minuscula" ~: esMinuscula 'A' ~?= False,
    "Caracter no minuscula" ~: esMinuscula '@' ~?= False,
    "Caracter no minuscula anterior a 'a'" ~: esMinuscula '`' ~?= False,
    "Caracter no minuscula posterior a 'z'" ~: esMinuscula '{' ~?= False
    ] --OK

testsEjletraANatural = test [
    "Letra minuscula a natural" ~: letraANatural 'a' ~?= 0,
    "Letra minuscula a natural" ~: letraANatural 'j' ~?= 9,
    "Ultima letra minuscula a natural" ~: letraANatural 'z' ~?= 25
    ] --OK

testsEjdesplazar = test [
    "Desplazar 2 letras a un char vacio" ~: desplazar ' ' 2 ~?= ' ',
    "Desplazar 3 letras hacia adelante a 'a'" ~: desplazar 'a' 3 ~?= 'd',
    "Rotar en caso de llegar al final" ~: desplazar 'z' 3 ~?= 'c',
    "Rotar en caso de llegar al principio" ~: desplazar 'b' (-5) ~?= 'w',
    "Desplazar 26 letras hacia adelante a 'f'" ~: desplazar 'f' 26 ~?= 'f',
    "Desplazar 2 letras a un caracter no minuscula" ~: desplazar '$' 2 ~?= '$'
    ] --OK

testsEjcifrar = test [
    "Mensaje vacio" ~: cifrar "" 2 ~?= "",
    "Mensaje con letras minusculas desplazadas 3 letras" ~: cifrar "computacion" 26 ~?= "computacion",
    "Mensaje con letras minusculas desplazadas 14 letras" ~: cifrar "abcdefg" 14 ~?= "opqrstu",
    "Mensaje con letras minusculas desplazadas 0 letras" ~: cifrar "xyz" 0 ~?= "xyz",
    "Mensaje con letras minusculas y mayusculas desplazada 5 letras" ~: cifrar "zEBra" 5 ~?= "eEBwf",
    "Mensaje con letras mayusculas" ~: cifrar "MAYUSCULAS" 5 ~?= "MAYUSCULAS" --OK
    ]

testsEjdescifrar = test [
    "Cifrado vacio" ~: descifrar "" 2 ~?= "",
    "Cifrado con letras minusculas desplazadas 3 letras hacia atras" ~: descifrar "frpsxwdflrq" 26 ~?= "frpsxwdflrq",
    "Cifrado con letras minusculas desplazadas 0 letras hacia atras" ~: descifrar "barco" 0 ~?= "barco",
    "Cifrado con letras minusculas y espacio desplazadas 8 letras hacia atras" ~: descifrar "hola mundo" 8 ~?= "zgds emfvg",
    "Cifrado con letras minusculas, mayusculas y caracteres desplazadas 4 letras hacia atras" ~: descifrar "k!wI" 4 ~?= "g!sI"
    ] --OK

testsEjcifrarLista = test [
    "Cifrado de lista vacia" ~: cifrarLista [] ~?= [],
    "Cifrado de lista con palabras minuculas" ~: cifrarLista ["teclado","mouse","mesa","pizarron","pantalla"] ~?= ["teclado","npvtf","oguc","slcduurq","terxeppe"],
    "Cifrado de lista con palabras repetidas" ~: cifrarLista ["hola","hola","hola"] ~?= ["hola","ipmb","jqnc"],
    "Cifrado de lista con una palabra" ~: cifrarLista ["universidad"] ~?= ["universidad"],
    "Cifrado de lista con palabras compuestas por letras minusculas y mayusculas" ~: cifrarLista ["ARGENTINa","HOla","comp$$u"] ~?= ["ARGENTINa","HOmb","eqor$$w"]
    ] --OK

testsEjfrecuencia = test [
    "Frecuencia de string vacio" ~: expectlistProximity (frecuencia "" ) [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    "Frecuencia de palabra con letras minusculas" ~: expectlistProximity (frecuencia "murcielago") [10.0,0.0,10.0,0.0,10.0,0.0,10.0,0.0,10.0,0.0,0.0,10.0,10.0,0.0,10.0,0.0,0.0,10.0,0.0,0.0,10.0,0.0,0.0,0.0,0.0,0.0],
    "Frecuencia de palabra con 100% una sola letra minuscula" ~: expectlistProximity (frecuencia "AyyyAy") [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,100.0,0.0],
    "Frecuencia de palabra primera y ultima del abecedario" ~: expectlistProximity (frecuencia "az") [50.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,50.0],
    "Frecuencia de palabra con letras minusculas y mayusculas" ~: expectlistProximity (frecuencia "aaAbbBccC") [33.333336,33.333336,33.333336,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
    "Frecuencia de palabra con letras mayusculas" ~: expectlistProximity (frecuencia "ADIOS") [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    ]

testsEjcifradoMasFrecuente = test [
    "Frecuencia de palabra con letras minusculas" ~: cifradoMasFrecuente "taller" 3 ~?= ('o', 33.333336),
    "Frecuencia de palabra con letras minusculas y mayusculas" ~: cifradoMasFrecuente "aeroPUERto" 4 ~?= ('s', 33.333336),
    "Frecuencia de palabra con letras minusculas" ~: cifradoMasFrecuente "programacion" 13 ~?=('n',16.666668),
    "Frecuencia de palabra con letras minusculas, distintas entre si" ~: cifradoMasFrecuente "murcielago" 3 ~?= ('p',10.0),
    "Frecuencia de palabra con letras mayusculas y 1 sola letra minuscula" ~: cifradoMasFrecuente "VACiO" 2 ~?= ('k',100.0),
    "Frecuencia de palabra con 3 letras con la misma cantidad de repeticiones" ~: expectAnyTuplaAprox (cifradoMasFrecuente "abcabc" 2) [('c',33.333336),('d',33.333336),('e',33.333336)]
    ] --OK

testsEjesDescifrado = test [
    "String 1 VACIO y String 2 letras minusculas" ~: esDescifrado "" "casa" ~?= False,
    "String 1 letras minusculas y String 2 VACIO" ~: esDescifrado "casa" "" ~?= False,
    "String 2 es descifrado por 17 letras de String 1 " ~: esDescifrado "onomatopeya" "xwxvjcxynhj" ~?= True,
    "String 1 NO ES descifrado de String 2" ~: esDescifrado "taller" "compu" ~?= False,
    "String 1 es descifrado de String 2 con espacio" ~: esDescifrado "hola mundo" "taxm ygzpa" ~?= True,
    "String 1 letras minusculas y Sting 2 letras minusculas y NO minusculas" ~: esDescifrado "hola" "Nurg" ~?= False
    ]--OK

testsEjtodosLosDescifrados = test [
    "Pablaras descifradas" ~: todosLosDescifrados ["compu", "frpsx", "mywza"] ~?= [("compu", "frpsx"), ("frpsx", "compu")],
    "Una palabra es la descifrada de varias palabras" ~: todosLosDescifrados ["casa","hola","kpop","computacion","nurg","qwertyuiopa","frpsxwdflrq","elix"] ~?= [("hola","nurg"),("nurg","hola"),("hola","elix"),("elix","hola"),("computacion","frpsxwdflrq"),("frpsxwdflrq","computacion"),("nurg","elix"),("elix","nurg")],
    "Las palabras no son descifrables entre si" ~: todosLosDescifrados ["auto","perro","gato","oso"] ~?= []
    ] --OK

testsEjexpandirClave = test [
    "Clave expadida 3 letras" ~: expandirClave "fe" 8 ~?= "fefefefe",
    "Clave acortada" ~: expandirClave "clave" 3 ~?= "cla",
    "Clave expandida el doble de su longitud" ~: expandirClave "blanco" 14 ~?= "blancoblancobl"
    ] --OK

testsEjcifrarVigenere = test [
    "Cifrado vigenere con clave de 5 caracteres" ~: cifrarVigenere "cancion" "cancion" ~?= "eaaeqca",
    "Cifrado vigenere con clave de 2 caracteres" ~: cifrarVigenere "francia" "ip" ~?= "ngickxi",
    "Cifrado vigenere con clave de 1 caracteres" ~: cifrarVigenere "argentina" "z" ~?= "zqfdmshmz"
    ] --OK

testsEjdescifrarVigenere = test [
    "Descifrado vigenere con clave de 2 caracteres" ~: descifrarVigenere "kdueciirqdv" "ip" ~?= "computacion",
    "Descifrado vigenere con clave de 1 caracteres" ~: descifrarVigenere "kirikocho" "j" ~?= "bzizbftyf",
    "Descifrado vigenere con clave mayor a la longitud de String 1" ~: descifrarVigenere "jota" "antartida" ~?= "jbaa"
    ] --OK

testsEjpeorCifrado = test [
    "Peor cifrado con un elemento en claves" ~: peorCifrado "test" ["unico"] ~?= "unico",
    "Peor cifrado 3 palabras con zzzz(82),fjk(77) y pero(105)" ~: peorCifrado "calcomania" ["zzzz","fjk","pero"] ~?= "fjk",
    "Peor cifrado 3 palabras con a(0),klop(139) y b(11)" ~: peorCifrado "universidad" ["a","klop","b"] ~?= "a"
    ] --OK

testsEjcombinacionesVigenere = test [
    "Combinacion vigenere con listas de msjs y claves vacias" ~: combinacionesVigenere [] [] "vacio" ~?= [],
    "Combinacion vigenere de claves con longitud > 1" ~: expectPermutacion (combinacionesVigenere ["casa","gato","ascii","onomatopeya"] ["dsad","kilo","oubg","sucu"] "uuuu")  [("casa","sucu"),("gato","oubg")],
    "Combinacion vigenere de claves con longitud = 1" ~: expectPermutacion ( combinacionesVigenere ["hola", "mundo"] ["a", "b"] "ipmb") [("hola", "b")]
    ] --OK

-- Funciones útiles

-- margetFloat(): Float
-- asegura: res es igual a 0.00001
margenFloat = 0.00001

-- expectAny (actual: a, expected: [a]): Test
-- asegura: res es un Test Verdadero si y sólo si actual pertenece a la lista expected
expectAny :: (Foldable t, Eq a, Show a, Show (t a)) => a -> t a -> Test
expectAny actual expected = elem actual expected ~? ("expected any of: " ++ show expected ++ "\n but got: " ++ show actual)


-- expectlistProximity (actual: [Float], expected: [Float]): Test
-- asegura: res es un Test Verdadero si y sólo si:
--                  |actual| = |expected|
--                  para todo i entero tal que 0<=i<|actual|, |actual[i] - expected[i]| < margenFloat()
expectlistProximity:: [Float] -> [Float] -> Test
expectlistProximity actual expected = esParecidoLista actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esParecidoLista :: [Float] -> [Float] -> Bool
esParecidoLista actual expected = (length actual) == (length expected) && (esParecidoUnaAUno actual expected)

esParecidoUnaAUno :: [Float] -> [Float] -> Bool
esParecidoUnaAUno [] [] = True
esParecidoUnaAUno (x:xs) (y:ys) = (aproximado x y) && (esParecidoUnaAUno xs ys)

aproximado :: Float -> Float -> Bool
aproximado x y = abs (x - y) < margenFloat


-- expectAnyTuplaAprox (actual: CharxFloat, expected: [CharxFloat]): Test
-- asegura: res un Test Verdadero si y sólo si:
--                  para algun i entero tal que 0<=i<|expected|,
--                         (fst expected[i]) == (fst actual) && |(snd expected[i]) - (snd actual)| < margenFloat()

expectAnyTuplaAprox :: (Char, Float) -> [(Char, Float)] -> Test
expectAnyTuplaAprox actual expected = elemAproxTupla actual expected ~? ("expected any of: " ++ show expected ++ "\nbut got: " ++ show actual)

elemAproxTupla :: (Char, Float) -> [(Char, Float)] -> Bool
elemAproxTupla _ [] = False
elemAproxTupla (ac,af) ((bc,bf):bs) = sonAprox || (elemAproxTupla (ac,af) bs)
    where sonAprox = (ac == bc) && (aproximado af bf)



-- expectPermutacion (actual: [T], expected[T]) : Test
-- asegura: res es un Test Verdadero si y sólo si:
--            para todo elemento e de tipo T, #Apariciones(actual, e) = #Apariciones(expected, e)

expectPermutacion :: (Ord a, Show a) => [a] -> [a] -> Test
expectPermutacion actual expected = esPermutacion actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esPermutacion :: Ord a => [a] -> [a] -> Bool
esPermutacion a b = (length a == length b) && (sort a == sort b)
