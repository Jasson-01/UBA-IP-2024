iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i = mod (div n (10^((cantDigitos n)-i))) 10

cantDigitos :: Integer -> Integer
cantDigitos n = auxCant n 0 

auxCant :: Integer -> Integer -> Integer
auxCant n c | mod n 10 == n = c+1
            | otherwise = auxCant (div n 10) (c+1)