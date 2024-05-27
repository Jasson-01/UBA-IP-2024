esFibonacci :: Integer -> Bool
esFibonacci n = aux17 n 0

aux17 :: Integer -> Integer -> Bool
aux17 n i | (fibonacci i) > n = False
          | fibonacci i == n = True
          | otherwise = aux17 n (i+1)  

fibonacci ::Integer -> Integer 
fibonacci n | n == 0 = 0
            | n == 1 = 1 
            | otherwise = fibonacci (n-1) + fibonacci (n-2)
