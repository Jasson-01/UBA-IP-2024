--PROBLEMA 1

sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada [n] = [n]
sumaAcumulada (x:y:xs) = x : sumaAcumulada (x+y:xs)

--PROBLEMA 2

descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) | (esPrimo x) == True = [x] : descomponerEnPrimos xs
                           | otherwise =  (divisoresDe x) : descomponerEnPrimos xs 



--Auxiliares:

esPrimo :: Integer -> Bool
esPrimo 0 = False
esPrimo 1 = False
esPrimo 2 = True
esPrimo n | (menorDivisor n > 1) && (menorDivisor n /= n) = False
          | otherwise = True

menorDivisor :: Integer -> Integer
menorDivisor n = aux n 2 

aux :: Integer -> Integer -> Integer
aux m n | mod m n == 0 && n <= m  = n
        | mod m n /= 0 = aux m (n+1)

divisoresDe :: Integer -> [Integer]
divisoresDe 0 = []
divisoresDe 1 = []
divisoresDe n | mod n 2 == 0 = 2 : divisoresDe (div n 2) 
              | mod n 3 == 0 = 3 : divisoresDe (div n 3)
              | otherwise = [n]  














