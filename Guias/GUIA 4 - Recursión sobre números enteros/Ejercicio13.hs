-- 1ERA FORMA

sumatoriaDoble :: Integer -> Integer -> Integer
sumatoriaDoble n m = aux1 n m m

aux1 :: Integer -> Integer -> Integer -> Integer
aux1 0 _ _ = 0
aux1 n m k | n /= 0 && m /= 0 = (n^m) + aux1 n (m-1) k  
           | n /= 0 && m == 0 = aux1 (n-1) k k

-- 2DA FORMA

sumatoriaDoble :: Integer -> Integer -> Integer
sumatoriaDoble n m = auxSumatoriaDoble n m m

auxSumatoriaDoble :: Integer -> Integer -> Integer -> Integer
auxSumatoriaDoble n m contador | n == 0 = 0 
                               | m == 1 = (n^m) + (auxSumatoriaDoble (n-1) (contador) contador) 
                               | otherwise = (n^m) + (auxSumatoriaDoble n (m-1) contador)
