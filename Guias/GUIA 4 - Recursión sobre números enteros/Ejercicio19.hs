--                                      --- 1ERA FORMA ---

esSumaInicialDePrimos :: Int -> Bool
esSumaInicialDePrimos x = aux7 x 0 0

aux7 :: Int -> Int -> Int -> Bool
aux7 x i c | (esPrimo i == True) && (c < x) = aux7 x (i+1) (c+i)
           | (esPrimo i == False) && (c < x) = aux7 x (i+1) c 
           | c > x = False
           | c == x = True



-- PROBLEMA A) --------

menorDivisor :: Int -> Int
menorDivisor n = aux n 2 

aux :: Int -> Int -> Int
aux m n | mod m n == 0 && n <= m  = n
        | mod m n /= 0 = aux m (n+1)

-- PROBLEMA B) -------

esPrimo :: Int -> Bool
esPrimo 0 = False
esPrimo 1 = False
esPrimo 2 = True
esPrimo n | (menorDivisor n > 1) && (menorDivisor n /= n) = False
          | otherwise = True

--                                      --- 2DA FORMA ---

esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos 0 = False
esSumaInicialDePrimos n = auxEsSumaInicialDePrimos n 2 0 

auxEsSumaInicialDePrimos :: Integer -> Integer -> Integer -> Bool
auxEsSumaInicialDePrimos n contador sumatoria | (not (esPrimo contador)) && (sumatoria < n ) = auxEsSumaInicialDePrimos n (contador+1) sumatoria
                                              | (esPrimo contador) && (sumatoria < n ) = auxEsSumaInicialDePrimos n (contador+1) (sumatoria+contador)
                                              | sumatoria > n = False 
                                              | sumatoria == n = True

menorDivisor :: Integer -> Integer
menorDivisor n = auxMenorDivisor n 2 

auxMenorDivisor :: Integer -> Integer -> Integer
auxMenorDivisor n m | mod n m == 0 = m
                    | m * m > n = n -- Si no hay divisores menores que la raíz cuadrada de n, entonces n es primo.
                    | mod n m /= 0 = auxMenorDivisor n (m+1)

esPrimo :: Integer -> Bool 
esPrimo n = menorDivisor n == n







