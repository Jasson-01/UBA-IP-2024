sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m = auxSumaPotencias q n m m

auxSumaPotencias :: Integer -> Integer -> Integer -> Integer -> Integer
auxSumaPotencias q n m contador | n == 0 = 0
                                | m == 1 = q^(n+m) + auxSumaPotencias q (n-1) contador contador
                                | otherwise =  q^(n+m) + auxSumaPotencias q n (m-1) contador 
                    