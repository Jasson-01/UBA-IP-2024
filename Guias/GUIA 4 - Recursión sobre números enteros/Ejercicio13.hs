sumatoriaDoble :: Integer -> Integer -> Integer
sumatoriaDoble n m = aux1 n m m

aux1 :: Integer -> Integer -> Integer -> Integer
aux1 0 _ _ = 0
aux1 n m k | n /= 0 && m /= 0 = (n^m) + aux1 n (m-1) k  
           | n /= 0 && m == 0 = aux1 (n-1) k k