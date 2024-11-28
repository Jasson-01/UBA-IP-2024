module Solucion where
{--
 Ejercicio 1 (2 puntos)

problema maxMovilN (lista: seq⟨Z⟩, n: Z) : Z {
  requiere: {|lista| > 0}
  requiere: {n > 0 y n es menor a la longitud de la lista}
  asegura: {res es el máximo de los últimos n elementos de lista.}
}
--}

maxMovilN:: [Int] -> Int -> Int
maxMovilN l n  = maximo (ultimosN l n)

--requiere |lista| >= n 
ultimosN::  [Int] -> Int -> [Int] 
ultimosN l n  | longitud l == n = l
              | otherwise = ultimosN (tail l) n

-- requiere: {|lista| > 0}              
maximo :: [Int] -> Int
maximo [x]  = x
maximo (x:y:ys) | x > y = maximo (x:ys)
                | otherwise = maximo (y:ys)

longitud :: [t] -> Int
longitud [] =  0
longitud (x:xs) = 1 + longitud xs

{--

Ejercicio 2 (2 puntos)

problema promedioPrimo (n: Z) : Float {
  requiere: {n > 1}
  asegura: {(res es el promedio de todos los factores primos de n (distintos o no).}
}
--}
promedioPrimo :: Int -> Float
promedioPrimo x = promedio (factoresPrimos x)

promedio :: [Int] -> Float
promedio xs = fromIntegral (suma xs) / fromIntegral (longitud xs)

suma :: [Int] -> Int
suma [x] = x
suma (x:xs) = x + suma xs

factoresPrimos :: Int -> [Int]
factoresPrimos n = factoresAux n 2
  
factoresAux :: Int -> Int -> [Int]
factoresAux 1 _ = []
factoresAux m d | m `mod` d == 0 = d : factoresAux (m `div` d) d
                | d * d > m      = [m]
                | otherwise      = factoresAux m (d + 1)
{--
 Ejercicio 3 (2 puntos)

problema letrasIguales (palabra: seq⟨Char⟩) : Z {
  requiere: {True}
  asegura: {(res es la cantidad de caracteres no blancos repetidos en palabra.}
}

--}
letrasIguales :: [Char] -> Int
letrasIguales [] = 0 
letrasIguales (' ':xs) =  letrasIguales xs --ignoro los espacios
letrasIguales (x:xs) | pertenece x xs = 1 + letrasIguales (eliminar x xs)
                     | otherwise = letrasIguales xs

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs) = e == x || pertenece e xs

{--
Ejercicio 4 (3 puntos)

problema cuantosIguales (palabra1: seq⟨Char⟩, palabra2: seq⟨Char⟩) : Z⟩{
  requiere: {True}
  asegura: {res es igual a la cantidad de caracteres no blancos y distintos que palabra1 y palabra2 tienen en común.}
}  
--}   

cuantosIguales :: [Char] -> [Char] -> Int  
cuantosIguales [] _ = 0
cuantosIguales (' ':xs) y = cuantosIguales xs y --ignoro los espacios
cuantosIguales (x:xs) y | elem x y = 1 + cuantosIguales (eliminar x xs) y 
                        | otherwise = cuantosIguales xs y 
                   
eliminar :: (Eq t) => t -> [t] -> [t]
eliminar e []   = []
eliminar e (x:xs)   | e == x = eliminar e xs
                    | otherwise = x:eliminar e xs
