--                                 --- 1ERA FORMA ---

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

--                                 --- 2DA FORMA ---

mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n = auxMayorDigitoPar n (-1)

auxMayorDigitoPar :: Integer -> Integer -> Integer
auxMayorDigitoPar 0 mayorPar = mayorPar
auxMayorDigitoPar n mayorPar | esPar (ultimo n) && (ultimo n) > mayorPar = auxMayorDigitoPar (resto n) (ultimo n)
                             | otherwise = auxMayorDigitoPar (resto n) mayorPar
              
resto :: Integer -> Integer
resto n = div n 10

ultimo :: Integer -> Integer 
ultimo n = mod n 10 

esPar :: Integer -> Bool
esPar m = mod m 2 == 0
