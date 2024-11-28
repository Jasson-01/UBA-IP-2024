module Solucion where
import Data.Char


-- EJ 1
esMinuscula :: Char -> Bool
esMinuscula c   | ord(c) >= 97 && ord(c) <= 122 = True
                | otherwise = False  --OK
-- EJ 2
letraANatural :: Char -> Int
letraANatural c = ord(c) - 97 --OK
-- EJ 3
desplazar :: Char -> Int -> Char
desplazar c n | esMinuscula c = chr(mod (letraANatural c + n) 26 + 97)
              | otherwise = c --OK
--EJ 4
cifrar :: String -> Int -> String
cifrar "" _ = ""
cifrar (letra:palabra) n = desplazar letra n : cifrar palabra n --OK
--EJ 5
descifrar :: String -> Int -> String
descifrar palabra n = cifrar palabra (-n) 
--EJ 6
cifrarLista :: [String] -> [String]
cifrarLista ls = cifrarListaAux ls 0
    where 
        cifrarListaAux [] _ = []
        cifrarListaAux (palabra:listaPalabras) n = cifrar palabra n : cifrarListaAux listaPalabras (n+1) --OK
--EJ 7
frecuencia :: String -> [Float]
frecuencia palabra = frecuenciaAux (quitarNoMinusculas palabra) (length (quitarNoMinusculas palabra)) 0 --OK

quitarNoMinusculas :: String -> String
quitarNoMinusculas "" = ""
quitarNoMinusculas s | esMinuscula (head s) == False = quitarNoMinusculas (tail s) 
                     | otherwise = head s : quitarNoMinusculas (tail s)

frecuenciaAux :: String -> Int -> Int -> [Float]
frecuenciaAux _ _ 26 = []
frecuenciaAux palabra longitudPalabra cont = obtenerPorcentaje (contarLetra (chr (cont + 97)) (palabra)) (longitudPalabra) : frecuenciaAux palabra longitudPalabra (cont+1)

contarLetra :: Char -> String -> Int
contarLetra _ "" = 0
contarLetra letra (c:palabra) | letra == c = 1 + contarLetra letra palabra
                              | otherwise = contarLetra letra palabra

obtenerPorcentaje :: Int -> Int -> Float
obtenerPorcentaje n 0 = 0.0
obtenerPorcentaje n total = (fromIntegral n / fromIntegral total) * 100
--EJ 8
cifradoMasFrecuente :: String -> Int -> (Char, Float)
cifradoMasFrecuente palabra n =  (obtenerLetraMasFrecuente (cifrar (quitarNoMinusculas palabra) n), maximo (frecuencia palabra) ) --OK

obtenerLetraMasFrecuente :: String -> Char
obtenerLetraMasFrecuente [letra] = letra
obtenerLetraMasFrecuente (letra1:letra2:palabra) | contarLetra letra1 (letra1:letra2:palabra) >= contarLetra letra2 (letra1:letra2:palabra) = obtenerLetraMasFrecuente(letra1:palabra)
                                                 | otherwise = obtenerLetraMasFrecuente(letra2:palabra)

maximo :: [Float] -> Float
maximo [x] = x
maximo (x:y:lista) | x >= y = maximo (x:lista)
                   | otherwise = maximo (y:lista)
--EJ 9
esDescifrado :: String -> String -> Bool
esDescifrado "" _ = False
esDescifrado _ "" = False
esDescifrado s1 s2 = esDescifradoAux s1 s2 0

esDescifradoAux :: String -> String -> Int -> Bool
esDescifradoAux _ _ 26 = False
esDescifradoAux s1 s2 cont | cifrar s1 cont == s2 = True
                           | otherwise = esDescifradoAux s1 s2 (cont+1)
--EJ 10
todosLosDescifrados :: [String] -> [(String, String)]
todosLosDescifrados [] = []
todosLosDescifrados ls = generadorDuplas (listaDeDuplasDeDescifrados ls)

listaDeDuplasDeDescifrados :: [String] -> [(String, String)]
listaDeDuplasDeDescifrados [] = []
listaDeDuplasDeDescifrados ls = paresDeCifrados (head ls) (tail ls) ++ listaDeDuplasDeDescifrados (tail ls)

paresDeCifrados :: String -> [String] -> [(String, String)]
paresDeCifrados "" _ = []
paresDeCifrados _ [] = []
paresDeCifrados s (x:lista) | esDescifrado s x = (s,x) : paresDeCifrados s lista
                            | otherwise = paresDeCifrados s lista

generadorDuplas ::[(String, String)] -> [(String, String)]
generadorDuplas [] = []
generadorDuplas ((a,b):lista) = (a,b) : (b,a) : generadorDuplas lista 

--EJ 11
expandirClave :: String -> Int -> String
expandirClave _ 0 = ""
expandirClave clave n = head clave : expandirClave (tail clave ++ [head clave]) (n-1) --OK

--EJ 12
cifrarVigenere :: String -> String -> String
cifrarVigenere s clave = cifrarVigenereAux s (expandirClave clave (length s) ) (1)

cifrarVigenereAux :: String -> String -> Int -> String
cifrarVigenereAux "" _ _ = ""
cifrarVigenereAux s claveExpandida descifrar = desplazar (head s) ((letraANatural (head claveExpandida)) * descifrar): cifrarVigenereAux (tail s) (tail claveExpandida) descifrar

--EJ 13
descifrarVigenere :: String -> String -> String
descifrarVigenere s clave = cifrarVigenereAux s (expandirClave clave (length s) ) (-1)

--EJ 14
peorCifrado :: String -> [String] -> String
peorCifrado s claves = peorCifradoAux s claves

peorCifradoAux :: String -> [String] -> String
peorCifradoAux _ [x] = x
peorCifradoAux s (clave1:clave2:claves)     | obtenerDistancia s (cifrarVigenere s clave1) <= obtenerDistancia s (cifrarVigenere s clave2) = peorCifradoAux s (clave1:claves)
                                            | otherwise = peorCifradoAux s (clave2:claves)

obtenerDistancia :: String -> String -> Int
obtenerDistancia "" _ = 0
obtenerDistancia s clave = obtenerModulo (letraANatural (head s) - letraANatural (head clave)) + obtenerDistancia (tail s) (tail clave)

obtenerModulo :: Int -> Int
obtenerModulo n | n < 0 = n * (-1)
                | otherwise = n
--EJ 15
combinacionesVigenere :: [String] -> [String] -> String -> [(String, String)]
combinacionesVigenere [] _ _ = []
combinacionesVigenere (msj:msjs) claves cifrado = combinacionesVigenereAux msj claves cifrado ++ combinacionesVigenere msjs claves cifrado

combinacionesVigenereAux :: String -> [String] -> String -> [(String, String)]
combinacionesVigenereAux _ [] _ = [] 
combinacionesVigenereAux msj (clave:claves) cifrado | cifrarVigenere msj clave == cifrado = (msj,clave) : combinacionesVigenereAux msj claves cifrado
                                                    | otherwise = combinacionesVigenereAux msj claves cifrado