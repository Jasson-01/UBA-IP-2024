module SolucionT1 where

--------------------------------------------------------------------------------
-- Ejercicio 1
maxMovilN :: [Integer] -> Integer -> Integer
maxMovilN lista n = maximoElemento ( sacandoLosNElementos lista ( (longitudLista lista) - n) )

sacandoLosNElementos :: [Integer] -> Integer -> [Integer]
sacandoLosNElementos (y) 0 = y  
sacandoLosNElementos (x:xs) m = sacandoLosNElementos xs (m-1) 

longitudLista :: [Integer] -> Integer
longitudLista [] = 0
longitudLista (x:xs) = 1 + longitudLista xs 

maximoElemento :: [Integer] -> Integer
maximoElemento [x] = x  
maximoElemento (x:y:xs) | x >= y = maximoElemento (x:xs)
                        | otherwise = maximoElemento (y:xs)   

--------------------------------------------------------------------------------
-- Ejercicio 2
promedioPrimo :: Integer -> Float
promedioPrimo n = (fromIntegral (sumatoria (mcd n) )) / (fromIntegral (longitudLista (mcd n)))

mcd :: Integer -> [Integer]
mcd n = haciendoListaPrimos n 2 n

haciendoListaPrimos :: Integer -> Integer -> Integer -> [Integer]
haciendoListaPrimos n m original | ( m >= n ) = [m] 
haciendoListaPrimos n m original | ((mod n m == 0) && (m*m < original)) || ((mod n m == 0) && (m*m <= original)) = m : haciendoListaPrimos (div n m) m original
                                 | otherwise = haciendoListaPrimos n (m+1) original

sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs  

--------------------------------------------------------------------------------

-- Ejercicio 3
letrasIguales :: String -> Integer
letrasIguales palabra = longitudPalabra (formandoRepetidos (sacandoBlancos palabra) [])

formandoRepetidos :: String -> String -> String
formandoRepetidos [] completa = completa
formandoRepetidos (x:xs) vacia | (pertenece x xs == True) && (pertenece x vacia == False) = formandoRepetidos xs (x:vacia)
                               | otherwise = formandoRepetidos xs vacia


--------------------------------------------------------------------------------
-- Ejercicio 4
cuantosIguales :: String -> String -> Integer
cuantosIguales palabra1 palabra2 = longitudPalabra (formandoListaIguales (sacandoBlancos palabra1) (sacandoBlancos palabra2) [])

sacandoBlancos :: String -> String
sacandoBlancos [] = []
sacandoBlancos (x:xs) | x == ' ' = sacandoBlancos xs 
                      | otherwise = x : sacandoBlancos xs 

formandoListaIguales :: String -> String -> String -> String
formandoListaIguales [] _ completa = completa 
formandoListaIguales (x:xs) palabra2 vacia | (pertenece x palabra2 == True) && (pertenece x vacia == False) = formandoListaIguales xs palabra2 (x:vacia)
                                           | otherwise = formandoListaIguales xs palabra2 vacia 

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece n [] = False  
pertenece n (x:xs) | n /= x = pertenece n xs 
                   | otherwise = True

longitudPalabra :: String -> Integer
longitudPalabra [] = 0
longitudPalabra (x:xs) = 1 + longitudPalabra xs  
