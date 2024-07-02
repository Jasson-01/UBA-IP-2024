module Solucion where

-- Ejercicio 1

eliminar :: (Eq t) => t -> [t] -> [t]
eliminar _ [] = []
eliminar x (y:ys) | x == y = eliminar x ys
                  | otherwise = y:(eliminar x ys)

cantidadApariciones :: (Eq t) => t -> [t] -> Int
cantidadApariciones _ [] = 0
cantidadApariciones x (y:ys) | x == y = 1 + cantidadApariciones x ys
                             | otherwise = cantidadApariciones x ys

generarStock :: [[Char]] -> [([Char],Int)]
generarStock [] = []
generarStock (x:xs) = (x, cant):generarStock (eliminar x xs)
     where cant = 1 + cantidadApariciones x xs

---

-- Ejercicio 2

stockDeProducto :: [([Char],Int)] -> [Char] -> Int
stockDeProducto [] a = 0
stockDeProducto (x:xs) a | a == fst x = snd x
                         | otherwise = stockDeProducto xs a


-- Ejercicio 3

buscarPrecio :: [Char] -> [( [Char], Float)] -> Float
buscarPrecio a [(b, c)] = c
buscarPrecio a (x:xs) | a == fst x = snd x
                     | otherwise = buscarPrecio a xs

dineroEnStock :: [([Char],Int)] -> [([Char], Float)] -> Float
dineroEnStock [] precios = 0
dineroEnStock (x:xs) precios = (fromIntegral (snd x)) * buscarPrecio (fst x) precios + dineroEnStock xs precios


-- Ejercicio 4


aplicarOferta :: [([Char],Int)] -> [([Char],Float)] -> [([Char],Float)]
aplicarOferta [] precios = precios
aplicarOferta _ [] = []
aplicarOferta stock (x:xs) | stockDeProducto stock (fst x) > 10 = (fst x, 0.8 * snd x): aplicarOferta stock xs
                           | otherwise = x: aplicarOferta stock xs


