--PROBLEMA 1

sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (' ':' ':xs) = sacarBlancosRepetidos (' ':xs) 
sacarBlancosRepetidos (x:y:xs) = x : sacarBlancosRepetidos (y:xs)

--PROBLEMA 2

contarPalabras :: [Char] -> Integer
contarPalabras lista = auxPalabras (sacarBlancosRepetidos lista)

auxPalabras :: [Char] -> Integer 
auxPalabras [] = 0 
auxPalabras (' ':xs) = 1 + auxPalabras xs 
auxPalabras (x:xs) = auxPalabras xs 
-------------------------------------
--PROBLEMA 3

-- FORMA 1
{-
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga oracion = aux3 (sacarBlancosRepetidos oracion)

aux3 :: [Char] -> [Char]
aux3 [] = []
aux3 [x] = [x] 
aux3 (x:xs) | (longitud (headOracion (x:xs))) > (longitud (headOracion (tailOracion (x:xs)))) = aux3 (headOracion (x:xs) ++ " " ++ tailOracion(tailOracion (x:xs)))
            | otherwise = aux3 (tailOracion (x:xs))


{-
esMayor :: Integer -> Integer -> Bool
esMayor x y | x >= y = True
            | otherwise = False
-}

longitud :: [Char] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

headOracion :: [Char] -> [Char]
headOracion [] = []
headOracion [n] = [n]
headOracion (' ':y:xs) = y : headOracion (xs)
headOracion (x:' ':xs) = [x] 
headOracion (x:y:xs) = x : headOracion (y:xs)

              
tailOracion :: [Char] -> [Char]
tailOracion [] = []
tailOracion [x] = [x]
tailOracion (x:' ':xs) = xs
tailOracion (x:y:xs) = tailOracion (y:xs)
--tailOracion (' ':y:xs) = tailOracion (y:xs)
-}

--------------------------- OBSERVACION:
aux :: [Char] -> [Char]
aux [] = []
aux [x] = [x]
aux lista = (head lista: tail (tail lista))
--------------------------------

-- FORMA 2 

palabraMasLarga :: [Char] -> [Char]
palabraMasLarga oracion = auxLarga (palabras oracion)



auxLarga :: [[Char]] -> [Char]
auxLarga [x] = x 
auxLarga (x:y:xs) | longitud x >= longitud y = auxLarga (x:xs)
                  | otherwise = auxLarga (y:xs) 


longitud :: [Char] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs



-----------------------------------------------------------------------------------------


-- PROBLEMA 4

palabras :: [Char] -> [[Char]]
palabras oracion = auxPalabras2 (sacarBlancosRepetidos oracion)

auxPalabras2 :: [Char] -> [[Char]] 
auxPalabras2 [] = []
auxPalabras2 [n] = []
auxPalabras2 oracion = (headOracion oracion) : auxPalabras2 (tailOracion oracion)


headOracion :: [Char] -> [Char]
headOracion [] = []
headOracion [n] = [n]
headOracion (' ':y:xs) = y : headOracion (xs)
headOracion (x:' ':xs) = [x] 
headOracion (x:y:xs) = x : headOracion (y:xs)


tailOracion :: [Char] -> [Char]
tailOracion [] = []
tailOracion [x] = [x]
tailOracion (x:' ':xs) = xs
tailOracion (x:y:xs) = tailOracion (y:xs)



-----------------------------------------------------------------------------------------

--PROBLEMA 5
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs

--PROBLEMA 6

aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos (x:xs) = x ++ " " ++ aplanarConBlancos xs 

--PROBLEMA 7
aplanarConNBlancos :: [[Char]]-> Integer-> [Char]
aplanarConNBlancos [x] _ = x
aplanarConNBlancos (x:xs) n = x ++ (nBlancos n) ++ aplanarConNBlancos xs n



nBlancos :: Integer -> [Char]
nBlancos 0 = []
nBlancos n = " " ++ nBlancos (n-1)















