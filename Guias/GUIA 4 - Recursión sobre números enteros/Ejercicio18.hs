mayorDigitoPar :: Integer -> Integer 
mayorDigitoPar n = maximoLista (auxPar n)

maximoLista :: [Integer] -> Integer
maximoLista [x] = x 
maximoLista (x:y:xs) | x >= y = maximoLista (x:xs)
                     | otherwise = maximoLista (y:xs)

auxPar :: Integer -> [Integer]
auxPar 0 = []
auxPar n | mod (primerDigito n) 2 == 0  = primerDigito n : auxPar (quitoPrimerDigito n)
         | otherwise = auxPar (quitoPrimerDigito n)

primerDigito :: Integer -> Integer
primerDigito n = mod n 10 

quitoPrimerDigito :: Integer -> Integer
quitoPrimerDigito n = div n 10 
--EJM: mayorDigitoPar 5674291856243562  => res = 8 (Pues es el mayor digito par que esta en el numero)