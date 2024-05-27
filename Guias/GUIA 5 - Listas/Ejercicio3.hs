--PROBLEMA 1
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs 

--PROBLEMA 2
productoria :: [Integer] -> Integer
productoria [x] = x  
productoria (x:xs) = x * productoria xs

--PROBLEMA 3
maximo :: [Integer] -> Integer 
maximo [x] = x 
maximo (x:y:xs) | x >= y = maximo (x:xs)
                | otherwise = maximo (y:xs)

--PROBLEMA 4
sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = []
sumarN n (x:xs) = (x+n) : sumarN n xs 

--PROBLEMA 5
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:y:xs) = sumandoAux x (x:y:xs)

sumandoAux :: Integer -> [Integer] -> [Integer]
sumandoAux x [n] = [x+n]
sumandoAux n (x:y:xs) = (n+x) : sumandoAux n (y:xs)

--PROBLEMA 6
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo lista = auxUltimo (sacandoUltimo lista) lista 

auxUltimo :: Integer -> [Integer] -> [Integer]
auxUltimo n [x] = [n+x]
auxUltimo n (x:y:xs) = (n+x) : auxUltimo n (y:xs)


sacandoUltimo :: [Integer] -> Integer
sacandoUltimo [x] = x 
sacandoUltimo (x:xs) = sacandoUltimo xs 

--PROBLEMA 7

pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | mod x 2 == 0  = x : pares xs 
             | otherwise = pares xs 

--PROBLEMA 8
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n [] = []
multiplosDeN n (x:xs) | (mod x n == 0) && (x /= 0) = x : multiplosDeN n xs 
                      | otherwise = multiplosDeN n xs  

--PROBLEMA 9
ordenar :: [Integer] -> [Integer]
ordenar lista = auxP lista 

auxP :: [Integer] -> [Integer]
auxP [] = []
auxP lista = (auxMenor lista) : auxP (sacandoElMenorDeLaLista (auxMenor lista) lista)
            
sacandoElMenorDeLaLista :: Integer -> [Integer] -> [Integer]
sacandoElMenorDeLaLista n [] = []
sacandoElMenorDeLaLista n (x:xs) | n == x = sacandoElMenorDeLaLista n xs 
                                 | otherwise = x : sacandoElMenorDeLaLista n xs  

auxMenor :: [Integer] -> Integer
auxMenor [x] = x 
auxMenor (x:y:xs) | x <= y = auxMenor (x:xs)
                  | otherwise = auxMenor (y:xs) 












































